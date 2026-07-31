import logging
import random
import re
import sys
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

try:
    import requests as _requests
except ImportError:
    _requests = None

# Ensure modules are importable
sys.path.append(str(Path(__file__).parent))

from gemini_client import GeminiClient
from github_utils import GithubClient
from jules_client import APIBlockError
from jules_client_plans import JulesPlanClient  # Reusing PR pulling logic


def _is_network_error(exc):
    """Returns True if the exception looks like a transient network connectivity issue."""
    if _requests is None:
        return False
    network_error_types = (
        _requests.exceptions.ConnectionError,
        _requests.exceptions.Timeout,
        _requests.exceptions.ChunkedEncodingError,
    )
    if isinstance(exc, network_error_types):
        return True
    # Also catch status 503/502 gateway errors
    if isinstance(exc, _requests.exceptions.HTTPError):
        if exc.response is not None and exc.response.status_code in [502, 503, 504]:
            return True
    return False


def _wait_for_network(callback_fn, lesson_title, retry_interval_secs=300, max_wait_secs=3600):
    """
    Blocks until internet connectivity is restored.
    Retries every `retry_interval_secs` seconds (default 5 min).
    Gives up after `max_wait_secs` (default 60 min) and returns False.
    Returns True when connectivity is confirmed.
    """
    waited = 0
    test_url = "https://www.google.com"
    while waited < max_wait_secs:
        try:
            if _requests is not None:
                _requests.get(test_url, timeout=5)
            return True  # Connection OK
        except Exception:
            pass
        remaining_min = (max_wait_secs - waited) // 60
        callback_fn(
            lesson_title,
            "WARN",
            f"No internet. Retrying in {retry_interval_secs // 60}m... ({remaining_min}m left)",
        )
        time.sleep(retry_interval_secs)
        waited += retry_interval_secs
    return False  # Gave up

class JulesPageGenerator:
    """
    Orchestrates the batch generation of HTML Pages from Plans using Jules Sessions.
    Handles interactive Q&A with Gemini Headless.
    """

    def __init__(self, project_root=None, state_manager=None, is_1_page_mode=False):
        self.is_1_page_mode = is_1_page_mode
        self.project_root = (
            Path(project_root)
            if project_root
            else Path(__file__).parent.parent.parent.parent.parent
        )
        self.state_manager = state_manager
        self.jules_client = JulesPlanClient(project_root=self.project_root)  # Reuse for PR pulling
        self.gemini_client = GeminiClient(project_root=self.project_root)
        self.github = GithubClient(token_path=self.project_root / "secrets/Github_Token.txt")
        self.abort_event = threading.Event()
        self._first_task_done = False
        self._delay_lock = threading.Lock()

        # Load Context for Gemini (Headless)
        self.context_files = [
            "GEMINI.md",
            "CODING_STANDARDS.md",
            "Jules-workspace/elements_index.md",
        ]
        self.project_context = self._load_context()

    def _load_context(self):
        """Loads key documentation to help Gemini answer Jules' questions."""
        context = "=== PROJECT CONTEXT ===\n"
        for fname in self.context_files:
            fpath = self.project_root / fname
            if fpath.exists():
                context += f"\n--- {fname} ---\n{fpath.read_text(encoding='utf-8')}\n"
        return context

    def _ask_gemini_headless(self, question):
        """
        Uses the headless Gemini client to answer a question about the project.
        """
        system_prompt = (
            "You are the Lead Architect for the Arabic Grammar Book project.\n"
            "A developer (Jules) is asking a question about the implementation.\n"
            "Answer the question clearly and concisely using the provided Project Context.\n"
            "If you need to provide a path, use the relative path from project root.\n"
            "Do not be conversational, just answer."
        )

        full_prompt = f"{self.project_context}\n\n=== QUESTION ===\n{question}"
        return self.gemini_client.generate_content_headless(system_prompt + "\n\n" + full_prompt)

    def process_plan(self, plan_path, callback=None):
        """
        Worker for a single plan.
        """
        if self.abort_event.is_set():
            return

        if not callback:

            def default_callback(t, s, m):
                logging.info(f"[{s}] {t}: {m}")

            callback = default_callback

        # API Safety Delay (5-15s) to prevent burst
        with self._delay_lock:
            if not self._first_task_done:
                self._first_task_done = True
                delay = 0
            else:
                delay = random.uniform(5, 15)

        if delay > 0:
            callback(plan_path.stem, "RUNNING", f"Safety Delay ({delay:.1f}s)...")
            time.sleep(delay)

        plan_content = plan_path.read_text(encoding="utf-8")
        lesson_title = plan_path.stem

        # Extract Lesson Number
        match = re.search(r"(?:^|page[_\s]*)(\d+)", lesson_title, re.IGNORECASE)
        lesson_num = match.group(1) if match else None

        # 1. Check Existing Session
        session_id = None
        state_key = None  # Key used in StateManager

        if self.state_manager and lesson_num:
            # Try to find matching key in StateManager
            all_lessons = self.state_manager.get_all_lessons()
            for key in all_lessons.keys():
                if key.startswith(f"{lesson_num} -") or key.startswith(f"{int(lesson_num)!s} -") or key.startswith(f"page {lesson_num}") or key.startswith(f"page {int(lesson_num)!s}"):
                    state_key = key
                    break

            if state_key:
                stored_sid = self.state_manager.get_lesson_data(state_key, "page_session_id")
                if stored_sid:
                    callback(
                        lesson_title, "RUNNING", f"Checking Existing Session ({stored_sid})..."
                    )
                    status_data = self.jules_client.get_session_status(stored_sid)
                    if status_data:
                        state = status_data.get("state", "UNKNOWN")
                        if state in ["SUCCEEDED", "COMPLETED"]:
                            callback(
                                lesson_title, "RUNNING", "Existing Session Completed. Pulling..."
                            )
                            session_id = stored_sid
                            # Skip creation & monitoring
                        elif state in ["FAILED", "CANCELLED"]:
                            callback(
                                lesson_title,
                                "WARN",
                                f"Previous Session Failed ({state}). Creating New...",
                            )
                            session_id = None
                        else:
                            callback(lesson_title, "RUNNING", f"Resuming Session ({state})...")
                            session_id = stored_sid

        # 2. Start Session (if needed)
        if not session_id:
            callback(lesson_title, "RUNNING", "Starting Session...")

            # Inject elements_index.md
            elements_text = ""
            elements_path = self.project_root / "Jules-workspace/elements_index.md"
            if elements_path.exists():
                elements_text = f"\n\n--- ELEMENTS INDEX DICTIONARY ---\n{elements_path.read_text(encoding='utf-8')}\n"

            # Determine prompt
            auditor_rules = ""
            if self.is_1_page_mode:
                auditor_path = self.project_root / "system-workspace/Architect_AUDITOR_1_PAGE.md"
                if auditor_path.exists():
                    auditor_rules = f"\n\n--- 1-PAGE STRICT RULES ---\n{auditor_path.read_text(encoding='utf-8')}\n"

            # 1. Goal
            goal_section = (
                f"=== 1. GOAL ===\n"
                f"You are the Expert HTML Generation Agent for the Arabic Grammar Book project.\n"
                f"Your task is to generate a single, pristine HTML file in the `pages/` directory based EXACTLY on the provided PLAN.\n"
                f"You are running in a headless, automated batch environment. Do NOT ask questions. Solve problems autonomously.\n"
            )

            # 2. Tools and Docs
            tools_and_docs = (
                f"=== 2. TOOLS AND DOCS ===\n"
                f"You have access to predefined templates. You MUST strictly use the HTML snippets defined in the Elements Index Dictionary.\n"
                f"You have workspace tools available:\n"
                f"- `verify_layout.py`: To check if the page fits on 1 A4 page without overflow.\n"
                f"- `lint_pages.py`: To validate HTML structure and rule compliance.\n"
                f"- `id_manager.py`: To generate sequential unique IDs (`bXXXXX`).\n"
            )
            if elements_text:
                tools_and_docs += f"{elements_text}\n"

            # 4. Rules and Elements Usage
            if self.is_1_page_mode:
                target_file = f"`pages/page_{lesson_num}.html`" if lesson_num else "`pages/[LESSON_TITLE].html`"
                naming_constraints = (
                    f"=== STRICT FILE GENERATION CONSTRAINTS ===\n"
                    f"1. You MUST generate ONLY ONE SINGLE FILE: {target_file}.\n"
                    f"2. Do NOT generate multiple pages (e.g. page_X, page_Y). Focus ONLY on the requested plan.\n"
                    f"3. Do NOT split the page into multiple parts (e.g. `_part1`, `_part2`, or `_cont`). You must fit everything into the single requested file.\n"
                    f"4. Do NOT edit `styles/main.css` or any other existing project files. Your only output should be the new HTML file in the `pages/` directory.\n"
                    f"5. Do NOT place the file inside `Jules-workspace/pages/`. It MUST be in the root `pages/` directory.\n"
                )
                specific_rules = (
                    f"=== 1-PAGE STRICT RULES & CONSTRAINTS ===\n"
                    f"1. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST verify this using `verify_layout.py` or equivalent tools. If it overflows, it is a catastrophic failure. Do NOT try to solve overflow by deleting text (Strict Typographer Rule). Solve it by choosing denser templates or omitting optional white-space.\n"
                    f"2. Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`. Ensure exact visual continuity (same title, same classes).\n"
                    f"3. Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the Keyword-to-Template Deterministic Mapping in elements_index.md to identify the correct template to use for the continuation. You are forbidden from guessing. Scan the raw text for the preceding keyword to determine the active template and apply the correct `_PART_2.html` wrapping.\n"
                    f"4. Templates: You are forbidden from inventing new HTML tags or classes or template elements. You must map all content using Jules-workspace/Templates/ components. **CRITICAL 1-PAGE MODE RULE**: You MUST NOT use `<section>` tags when applying templates. Replace any `<section>` tags from the templates with `<div>` tags (keep `<header>` for page headers as is).\n"
                    f"5. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). The ID MUST be applied to the `<div>` tag that replaced the `<section>` tag. Use Jules-workspace/id_manager.py to generate or verify them.\n"
                    f"6. Self-Correction: Run Jules-workspace/lint_pages.py --one-page-mode <filename> after creating html files. If it fails, you MUST fix the errors (usually inline styles or forbidden section tags) before submitting.\n"
                    f"7. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.\n"
                    f"8. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal\n"
                    f"9. Page Wrappers: The compiler will automatically wrap the final page in `TEMPLATE_C_PAGE_WRAPPER.html`. Do NOT include this template in your HTML.\n"
                    f"10. Exam Section: ONLY include the `TEMPLATE_C_EXAM.html` block if the provided raw text slice actually contains test/exam questions (e.g., keywords like \"تطبيق\", \"امتحان\"). Do NOT hallucinate an exam if it is not in the source text. **CRITICAL:** If an exam or exercise contains the answers in the raw text, you MUST use `TEMPLATE_C_EXAM_SOLVED.html` instead of `TEMPLATE_C_EXAM.html`.\n"
                    f"11. **EXTREME CONDENSATION PROTOCOL (AUTHORIZED)**: If the content overflows A4, you are explicitly authorized to deviate from the Architect's suggested templates to maximize density:\n"
                    f"    - **Split the Page:** Use `TEMPLATE_C_TWO_COLUMNS_WRAPPER.html` or `<div class=\"split-grid\">` to split the page into left/right halves and pack independent blocks side-by-side.\n"
                    f"    - **Template Overrides:** If a vertical `TEMPLATE_C_LIST` was suggested, you may override it and use `TEMPLATE_C_CHIPS` (for single words) or `TEMPLATE_C_COMPACT_QA_TABLE` if it saves vertical space.\n"
                    f"    - **Zero Margins:** Safely strip non-essential vertical spacing by applying `mb-0`, `p-0`, or `mt-0` utility classes defined in `main.css`.\n"
                    f"12. **LAST RESORT (OVERFLOW ESCAPE HATCH)**: If you have exhausted all spacing utilities and aggressive 2-column groupings, and the page STILL overflows, **you MUST submit the file anyway with the overflow**.\n"
                    f"    - Do NOT split the output into multiple files (no `_part1`, `_part2`).\n"
                    f"    - Do NOT pause to ask a question or request permission.\n"
                    f"    - Submit the best possible condensed version so a human can manually review the physical overflow later.\n"
                )
            else:
                naming_constraints = (
                    f"=== STRICT FILE GENERATION CONSTRAINTS ===\n"
                    f"1. You MUST generate ONLY ONE SINGLE FILE: `pages/[LESSON_NUMBER].0_nXX_[TITLE].html`.\n"
                    f"2. Do NOT generate multiple pages. Focus ONLY on the requested plan.\n"
                    f"3. Do NOT split the page into multiple parts (e.g. `_part1`, `_part2`).\n"
                    f"4. Do NOT edit `styles/main.css` or any other existing project files. Your only output should be the new HTML file in the `pages/` directory.\n"
                    f"5. Do NOT place the file inside `Jules-workspace/pages/`. It MUST be in the root `pages/` directory.\n"
                )
                specific_rules = (
                    f"=== STRICT RULES & CONSTRAINTS ===\n"
                    f"1. Templates: You are forbidden from inventing new HTML tags or classes. You must map all content using `Jules-workspace/Templates/` components.\n"
                    f"2. Unique IDs: All content blocks must have a unique ID (`id='bXXXXX'`). Use `Jules-workspace/id_manager.py` to generate or verify them.\n"
                    f"3. Self-Correction: Run `Jules-workspace/lint_pages.py <filename>` after creating html files. You MUST fix any errors before submitting.\n"
                )

            general_rules = (
                f"=== GENERAL RULES & ELEMENTS USAGE ===\n"
                f"1. Source of Truth: Adhere strictly to `BOOK_RULES.md` and `elements_index.md`.\n"
                f"2. Text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice. Do not summarize examples. Do not provide uncompleted text using (...).\n"
                f"3. Tashkeel (Harakat): You MUST preserve the EXACT Tashkeel from the input. Stripping diacritics is a critical failure. Do not generate bare Arabic letters without their vowels.\n"
                f"4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`, `.highlight-green` for secondary.\n"
                f"5. Definitions: Must use `.text-accent` class.\n"
                f"6. Mandatory Style Guide:\n"
                f"   - **Rule:** NO INLINE STYLES. You are FORBIDDEN from adding inline CSS styles (no `style=`). Use only the utility classes specified in `styles/main.css`.\n"
                f"   - **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.\n"
                f"   - **Mapping Examples:** `style=\"width: 20%\"` -> `class=\"w-20pct\"`, `style=\"margin-top: 2mm\"` -> `class=\"mt-2mm\"`, `style=\"text-align: center\"` -> `class=\"text-center\"`, `style=\"font-weight: bold\"` -> `class=\"font-bold\"`.\n"
            )

            # 5. Verification, Auditing & Refinement
            audit_section = (
                f"=== 5. VERIFICATION, AUDITING & REFINEMENT ===\n"
                f"To ensure success, your output must pass the Quality Assurance checks. The checks evaluate:\n"
                f"- Content Integrity (No dropped text, 100% preservation of plan).\n"
                f"- Strict 1-Page Fit. If it overflows, you must resolve it (using denser templates/CSS).\n"
                f"- No Hallucinations (No exams if not requested, no invented examples).\n"
            )
            
            if auditor_rules:
                audit_section += (
                    f"\n[Auditor Guidelines Reference]\n"
                    f"The following is what the QA Auditor checks for. Ensure your page respects these constraints. "
                    f"WARNING: Ignore any instructions in the text below asking you to output JSON. You are the builder, not the auditor, so your ultimate output must be generating the HTML file and a summary, not a JSON response.\n"
                    f"{auditor_rules}\n"
                )

            execution_protocol = (
                f"=== NON-INTERACTIVE EXECUTION PROTOCOL (CRITICAL) ===\n"
                f"1. You are running in a headless, automated batch environment.\n"
                f"2. NEVER ask the user questions. There is no user to answer you.\n"
                f"3. NEVER ask for permission to continue, finalize, or clean up.\n"
                f"4. If you encounter an error (like an overflow in verify_layout.py), you MUST solve it autonomously using the provided tools and rules (e.g., adjusting padding/margins). Do NOT ask for a recommendation.\n"
                f"5. Execute ALL steps, from generation to verification to final cleanup, in a SINGLE continuous process.\n"
                f"6. Once finished, just output a final summary of what you did. Do NOT end with a question like 'Should I continue?' or 'Is there anything else?'.\n"
            )

            prompt = (
                f"{goal_section}\n"
                f"{tools_and_docs}\n"
                f"=== 3. RAW PLAN ===\n"
                f"{plan_content}\n\n"
                f"=== 4. RULES AND ELEMENTS USAGE ===\n"
                f"{naming_constraints}\n"
                f"{general_rules}\n"
                f"{specific_rules}\n"
                f"{audit_section}\n"
                f"{execution_protocol}\n"
            )

            # Inject Workspace Code
            settings_file = self.project_root / "system-workspace/settings.json"
            workspace_code = None
            import json
            if settings_file.exists():
                try:
                    with open(settings_file, encoding="utf-8") as f:
                        workspace_code = json.load(f).get("workspace_code")
                except:
                    pass
            
            if workspace_code and workspace_code != "None":
                prompt += f"\n\nIMPORTANT INSTRUCTION: You MUST append the batch workspace code '_{workspace_code}' to the filename of the generated page (e.g. before the .html extension)."


            # Network-aware session creation: retry on connection errors
            session = None
            _max_create_attempts = 15
            for _attempt in range(_max_create_attempts):
                try:
                    session = self.jules_client.create_session(
                        prompt, f"PageGen: {lesson_title}", automation_mode="AUTO_CREATE_PR"
                    )
                    break  # Success
                except APIBlockError as e:
                    self.abort_event.set()
                    callback(lesson_title, "API_BLOCKED", "API Quota/Limit Reached")
                    return False
                except Exception as e:
                    is_precondition = False
                    if hasattr(e, 'response') and e.response is not None:
                        if e.response.status_code == 400 and "FAILED_PRECONDITION" in e.response.text:
                            is_precondition = True

                    if (is_precondition or _is_network_error(e)) and _attempt < _max_create_attempts - 1:
                        if is_precondition:
                            callback(lesson_title, "WARN", f"Jules API busy (Precondition Failed). Waiting 60s...")
                            time.sleep(60)
                        else:
                            callback(lesson_title, "WARN", f"Network error on create: {e}. Waiting for internet...")
                            if not _wait_for_network(callback, lesson_title):
                                callback(lesson_title, "ERROR", "Internet did not recover. Giving up.")
                                return False
                        callback(lesson_title, "RUNNING", "Retrying session create...")
                    else:
                        callback(lesson_title, "ERROR", f"Session create failed: {e}")
                        return False
            if not session:
                callback(lesson_title, "ERROR", "Session Create Failed")
                return False

            session_id = session.get("name")

            # Save Session ID
            if self.state_manager:
                if not state_key:
                    # Create a new key if not found (best guess)
                    clean_title = lesson_title.replace("-plan", "").replace("-", " ")
                    state_key = clean_title  # Fallback
                self.state_manager.update_lesson_data(state_key, {"page_session_id": session_id})

        callback(lesson_title, "RUNNING", f"Monitoring {session_id}...")

        # 3. Monitor (if not already done)
        # Check status first to see if we can skip monitoring
        status_data = self.jules_client.get_session_status(session_id)
        current_state = status_data.get("state", "UNKNOWN") if status_data else "UNKNOWN"

        if current_state in ["SUCCEEDED", "COMPLETED"]:
            status = "SUCCEEDED"
        else:
            status = self._monitor_and_handle_session(session_id, lesson_title, callback)

        if status != "SUCCEEDED":
            callback(lesson_title, "FAILED", f"Ended with {status}")
            return False

        # 4. Pull Result
        callback(lesson_title, "RUNNING", "Downloading generated page...")
        details = self.jules_client.get_session_details(session_id)

        branch = details.get("branch")
        pr_number = details.get("pr_number")
        if not branch and not pr_number:
            callback(lesson_title, "ERROR", "No Branch or PR info found.")
            return False

        repo_full_name = f"{self.jules_client.repo_owner}/{self.jules_client.repo_name}"

        # Attempt 1: Smart Search to find exact filename in multiple dirs
        found_name = None
        found_path = None
        search_dirs = ["pages", "Jules-workspace/pages"]

        try:
            for d in search_dirs:
                files = self.github.get_file_info(repo_full_name, d, branch)
                if files and isinstance(files, list):
                    for f in files:
                        if not f["name"].endswith(".html"):
                            continue
                        if (
                            lesson_num
                            and (
                                f["name"].startswith(lesson_num)
                                or f["name"].startswith(str(int(lesson_num)))
                            )
                        ) or (not lesson_num and lesson_title.replace("-plan", "") in f["name"]):
                            found_name = f["name"]
                            found_path = f"{d}/{found_name}"
                            break
                if found_path:
                    break
        except Exception as e:
            callback(lesson_title, "WARN", f"Branch search failed: {e}")

        # If we couldn't find it dynamically, guess it
        if not found_path:
            found_name = f"{lesson_title.replace('-plan', '')}.html"
            found_path = f"pages/{found_name}"
            callback(
                lesson_title, "WARN", f"Could not determine exact filename. Guessing: {found_path}"
            )

        def bg_pull():
            def pr_callback(ignored_path, state, msg):
                callback(lesson_title, state, msg)

            success = self.jules_client.finalize_pr_and_pull(details, found_path, callback=pr_callback)

            if success:
                import shutil

                # If it downloaded to Jules-workspace/pages, move it to pages
                if found_path.startswith("Jules-workspace/pages/"):
                    source_file = self.project_root / found_path
                    dest_file = self.project_root / "pages" / found_name
                    if source_file.exists():
                        dest_file.parent.mkdir(exist_ok=True, parents=True)
                        shutil.move(str(source_file), str(dest_file))
                callback(lesson_title, "SUCCESS", f"Page Saved: {found_name}")
            else:
                callback(lesson_title, "ERROR", "Pull Failed")

        import threading
        t = threading.Thread(target=bg_pull, daemon=False)
        if not hasattr(self, "pull_threads"):
            self.pull_threads = []
        self.pull_threads.append(t)
        t.start()
        
        return True

    def _monitor_and_handle_session(self, session_id, lesson_title, callback):
        """
        Monitors a running session.
        If Jules asks a question, uses Gemini to answer.
        Network errors trigger a 5-minute wait-and-retry loop.
        """
        start_time = time.time()
        timeout = 25 * 60  # 25 minutes
        last_log_time = start_time
        consecutive_network_errors = 0

        while time.time() - start_time < timeout:
            status_data = None
            try:
                status_data = self.jules_client.get_session_status(session_id)
            except Exception as e:
                if _is_network_error(e):
                    consecutive_network_errors += 1
                    callback(lesson_title, "WARN", f"Network error #{consecutive_network_errors} while polling: {e}")
                    if not _wait_for_network(callback, lesson_title):
                        callback(lesson_title, "ERROR", "Internet did not recover after 60 min. Giving up.")
                        return "NETWORK_TIMEOUT"
                    callback(lesson_title, "RUNNING", "Internet restored. Resuming monitoring...")
                    consecutive_network_errors = 0
                    continue
                else:
                    callback(lesson_title, "WARN", f"Unexpected error polling: {e}")

            if not status_data:
                time.sleep(30)
                continue

            consecutive_network_errors = 0  # Reset on success
            state = status_data.get("state", "UNKNOWN")

            # Periodic Heartbeat Log (Every 60s)
            if time.time() - last_log_time > 60:
                elapsed_min = int((time.time() - start_time) / 60)
                callback(lesson_title, "RUNNING", f"Still running... ({elapsed_min}m elapsed)")
                last_log_time = time.time()

            if state in ["SUCCEEDED", "COMPLETED"]:
                return "SUCCEEDED"
            if state in ["FAILED", "CANCELLED"]:
                try:
                    acts = self.jules_client.get_activities(session_id)
                    if acts:
                        acts.sort(key=lambda x: x.get("createTime", ""), reverse=True)
                        for act in acts:
                            if "progressUpdated" in act and "title" in act["progressUpdated"]:
                                callback(lesson_title, "WARN", f"Jules Error: {act['progressUpdated']['title']} - {act['progressUpdated'].get('description', '')}")
                                break
                except:
                    pass
                return state

            if state in ["ACTION_REQUIRED", "WAITING_FOR_INPUT"]:
                callback(lesson_title, "INTERACT", "Jules needs input...")

                question = self.jules_client.get_latest_message(session_id)
                if not question:
                    question = "Please continue."

                # Ask Gemini Headless
                answer = self._ask_gemini_headless(question)
                callback(lesson_title, "INTERACT", "Sending Answer...")

                self.jules_client.send_response(session_id, answer)
                time.sleep(10)

            time.sleep(30)

        return "TIMEOUT"

    def count_existing_pages(self, excluded_lessons=None, only_lessons=None):
        """Counts how many HTML pages already exist for the current plans."""
        plans_dir = self.project_root / "plans"
        pages_dir = self.project_root / "pages"
        if not plans_dir.exists(): return 0
        
        all_plans = sorted(list(plans_dir.glob("*.md")))
        count = 0
        for plan in all_plans:
            match = re.search(r"(?:^|page[_\s]*)(\d+)", plan.name, re.IGNORECASE)
            lesson_num = match.group(1) if match else None

            if lesson_num and excluded_lessons and (lesson_num in excluded_lessons or str(int(lesson_num)) in excluded_lessons):
                continue
            if lesson_num and only_lessons and (lesson_num not in only_lessons and str(int(lesson_num)) not in only_lessons):
                continue

            html_exists = False
            if lesson_num:
                for f in pages_dir.glob("*.html"):
                    if f.name.startswith(f"{lesson_num}.") or f.name.startswith(f"{lesson_num}_"):
                        html_exists = True
                        break
            else:
                html_name = plan.name.replace("-plan.md", ".html")
                if (pages_dir / html_name).exists():
                    html_exists = True
            
            if html_exists: count += 1
            
        return count

    def run_batch_generation(
        self, max_concurrent=10, update_callback=None, excluded_lessons=None, only_lessons=None, force_remake=False
    ):
        """
        Main entry point.
        """
        if not update_callback:

            def update_callback(t, s, m):
                logging.info(f"[{s}] {t}: {m}")

        if excluded_lessons is None:
            excluded_lessons = set()

        logging.info(f"\n🏭 Starting Jules Page Generation (Batch Size: {max_concurrent})...")

        plans_dir = self.project_root / "plans"
        all_plans = sorted(list(plans_dir.glob("*.md")))

        if not all_plans:
            update_callback("System", "WARN", "No plans found.")
            return

        to_process = []
        pages_dir = self.project_root / "pages"
        pages_dir.mkdir(exist_ok=True, parents=True)

        # Smart Recovery: Move any stray files from Jules-workspace/pages into the main pages/ dir
        jules_pages_dir = self.project_root / "Jules-workspace" / "pages"
        if jules_pages_dir.exists() and jules_pages_dir.is_dir():
            import shutil

            for stray_file in jules_pages_dir.glob("*.html"):
                target_file = pages_dir / stray_file.name
                shutil.move(str(stray_file), str(target_file))
                update_callback("System", "INFO", f"Moved stray file: {stray_file.name} -> pages/")

        for plan in all_plans:
            # Check Lesson Number (Assuming "09-Title-plan.md" or "page_09-plan.md")
            match = re.search(r"(?:^|page[_\s]*)(\d+)", plan.name, re.IGNORECASE)
            lesson_num = match.group(1) if match else None

            # Smart check if output exists (Jules uses dynamic names like 09.0_nXX_title.html)
            existing_htmls = []
            if lesson_num:
                for f in pages_dir.glob("*.html"):
                    if f.name.startswith(f"{lesson_num}.") or f.name.startswith(f"{lesson_num}_"):
                        existing_htmls.append(f)
            else:
                html_name = plan.name.replace("-plan.md", ".html")
                f = pages_dir / html_name
                if f.exists():
                    existing_htmls.append(f)

            if existing_htmls and not force_remake:
                update_callback(plan.stem, "SKIP", "HTML exists")
                continue
                
            if existing_htmls and force_remake:
                for f in existing_htmls:
                    try:
                        f.unlink()
                    except:
                        pass

            if (
                lesson_num
                and excluded_lessons
                and (lesson_num in excluded_lessons or str(int(lesson_num)) in excluded_lessons)
            ):
                update_callback(plan.stem, "SKIP", "Excluded (Page exists)")
                continue

            if (
                lesson_num
                and only_lessons
                and (lesson_num not in only_lessons and str(int(lesson_num)) not in only_lessons)
            ):
                continue  # Skip if we only want specific lessons

            to_process.append(plan)

        update_callback("System", "INFO", f"Queued {len(to_process)} plans for generation.")
        
        def _get_num(plan_path):
            match = re.search(r"(?:^|page[_\s]*)(\d+)", plan_path.name, re.IGNORECASE)
            return int(match.group(1)) if match else 999
            
        to_process = sorted(to_process, key=_get_num)

        with ThreadPoolExecutor(max_workers=max_concurrent) as executor:
            future_to_plan = {
                executor.submit(self.process_plan, plan, update_callback): plan.stem
                for plan in to_process
            }

            for future in as_completed(future_to_plan):
                pass  # Callbacks handle updates

        if hasattr(self, "pull_threads"):
            for t in self.pull_threads:
                t.join()
