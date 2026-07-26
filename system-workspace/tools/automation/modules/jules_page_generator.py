import logging
import random
import re
import sys
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# Ensure modules are importable
sys.path.append(str(Path(__file__).parent))

from gemini_client import GeminiClient
from github_utils import GithubClient
from jules_client import APIBlockError
from jules_client_plans import JulesPlanClient  # Reusing PR pulling logic


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
        delay = random.uniform(5, 15)
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

            if self.is_1_page_mode:
                naming_instruction = f"The output file should follow the strict naming convention: `pages/page_{lesson_num}.html`.\n"
            else:
                naming_instruction = f"The output file should follow the strict naming convention: `pages/[LESSON_NUMBER].0_nXX_[TITLE].html`.\n"

            prompt = (
                f"Generate the HTML page for the following plan.\n"
                f"CRITICAL RULES (ANTI-HALLUCINATION):\n"
                f"1. You are FORBIDDEN from inventing raw HTML structures. You MUST strictly use the HTML snippets from `Jules-workspace/Templates/` as defined in `elements_index.md`.\n"
                f"2. You are FORBIDDEN from adding inline CSS styles (no `style=`). Use only the utility classes specified in `styles/main.css`.\n"
                f"3. You must preserve EXACT Tashkeel and output 100% Arabic text (except HTML tags).\n"
                f"4. EVERY content block must have a unique ID (e.g., id='bXXXXX').\n"
                f"5. Maintain continuity of style: use `.highlight-red` for primary focus, `.highlight-blue` for secondary. `.irab-word` MUST remain white.\n"
                f"{naming_instruction}"
                f"{auditor_rules}"
                f"PLAN:\n{plan_content}{elements_text}"
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


            try:
                session = self.jules_client.create_session(
                    prompt, f"PageGen: {lesson_title}", automation_mode="AUTO_CREATE_PR"
                )
            except APIBlockError as e:
                self.abort_event.set()
                callback(lesson_title, "API_BLOCKED", "API Quota/Limit Reached")
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
        if not branch:
            callback(lesson_title, "ERROR", "No Branch info found.")
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
            return True
        else:
            callback(lesson_title, "ERROR", "Pull Failed")
            return False

    def _monitor_and_handle_session(self, session_id, lesson_title, callback):
        """
        Monitors a running session.
        If Jules asks a question, uses Gemini to answer.
        """
        start_time = time.time()
        timeout = 25 * 60  # 25 minutes
        last_log_time = start_time

        while time.time() - start_time < timeout:
            status_data = self.jules_client.get_session_status(session_id)
            if not status_data:
                time.sleep(30)
                continue

            state = status_data.get("state", "UNKNOWN")

            # Periodic Heartbeat Log (Every 60s)
            if time.time() - last_log_time > 60:
                elapsed_min = int((time.time() - start_time) / 60)
                callback(lesson_title, "RUNNING", f"Still running... ({elapsed_min}m elapsed)")
                last_log_time = time.time()

            if state in ["SUCCEEDED", "COMPLETED"]:
                return "SUCCEEDED"
            if state in ["FAILED", "CANCELLED"]:
                return state

            if state in ["ACTION_REQUIRED", "WAITING_FOR_INPUT"]:
                callback(lesson_title, "INTERACT", "Jules needs input...")

                question = self.jules_client.get_latest_message(status_data)
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
        self, max_concurrent=5, update_callback=None, excluded_lessons=None, only_lessons=None, force_remake=False
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

            if html_exists and not force_remake:
                update_callback(plan.stem, "SKIP", "HTML exists")
                continue

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

        with ThreadPoolExecutor(max_workers=max_concurrent) as executor:
            future_to_plan = {
                executor.submit(self.process_plan, plan, update_callback): plan.stem
                for plan in to_process
            }

            for future in as_completed(future_to_plan):
                pass  # Callbacks handle updates
