import json
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

from jules_client_plans import JulesPlanClient
from jules_client import APIBlockError
from text_processing import TextProcessor


class JulesPlanner:
    """
    Orchestrates the batch generation of plans using Jules Sessions.
    """

    def __init__(self, project_root, state_manager=None, is_1_page_mode=False, is_1_part_mode=False, part_instruction='', part_number=''):
        self.project_root = Path(project_root)
        self.state_manager = state_manager
        self.client = JulesPlanClient(project_root=self.project_root)
        self.tp = TextProcessor(project_root=self.project_root)
        self.is_1_page_mode = is_1_page_mode
        self.is_1_part_mode = is_1_part_mode
        self.part_instruction = part_instruction
        self.part_number = part_number

        self.abort_event = threading.Event()
        self._first_task_done = False
        self._delay_lock = threading.Lock()

        # Load Prompts
        if self.is_1_part_mode:
            master_prompt_name = "Architect_GEM_MASTER_1_PART.md"
        else:
            master_prompt_name = "Architect_GEM_MASTER_1_PAGE.md" if self.is_1_page_mode else "Architect_GEM_MASTER.md"
            
        self.architect_prompt = (
            self.project_root / f"system-workspace/{master_prompt_name}"
        ).read_text(encoding="utf-8")

        # Inject elements_index.md to prevent Context Starvation
        elements_index_path = self.project_root / "Jules-workspace/elements_index.md"
        if elements_index_path.exists():
            elements_text = elements_index_path.read_text(encoding="utf-8")
            self.architect_prompt += f"\n\n--- ELEMENTS INDEX DICTIONARY ---\n{elements_text}\n"

        if self.is_1_part_mode:
            auditor_prompt_name = "Architect_AUDITOR_1_PART.md"
        else:
            auditor_prompt_name = "Architect_AUDITOR_1_PAGE.md" if is_1_page_mode else "Architect_AUDITOR.md"
            
        self.auditor_prompt = (
            self.project_root / f"system-workspace/{auditor_prompt_name}"
        ).read_text(encoding="utf-8")
        
        if self.is_1_part_mode and self.part_instruction:
            custom_inst = f"\n\n--- CUSTOM PART INSTRUCTION ---\n{self.part_instruction}\n"
            self.architect_prompt += custom_inst
            self.auditor_prompt += custom_inst

        # Load Raw Text Index
        self.raw_text_path = self.project_root / "system-workspace/text-data/full_raw_indexed.txt"
        if not self.raw_text_path.exists():
            logging.warning("⚠️ Raw text index missing. Generating...")
            self.tp.merge_raw_text()

        self.raw_lines = self.raw_text_path.read_text(encoding="utf-8").splitlines()

    def _extract_lesson_text(self, start_marker, end_marker):
        """
        Extracts lines from full_raw_indexed.txt between start and end markers.
        Markers format: "raw_filename.txt:line_number"
        """
        extracted = []
        capturing = False

        # Parse markers to match format [filename:line]
        # TextProcessor index format: "raw_1.txt:5"
        # File format: "[raw_1.txt:5] Content..."

        start_pattern = f"[{start_marker}]"
        end_pattern = f"[{end_marker}]"

        for line in self.raw_lines:
            if start_pattern in line:
                capturing = True

            if capturing:
                # Remove the [marker] prefix for cleaner prompt
                clean_line = re.sub(r"^\[.*?\]\s*", "", line)
                extracted.append(clean_line)

            if end_pattern in line:
                capturing = False
                break

        return "\n".join(extracted)

    def count_existing_plans(self, excluded_lessons=None, only_lessons=None):
        """Counts how many plans already exist for the current index."""
        index_path = self.project_root / "system-workspace/text-data/raw_to_lesson_index.json"
        if not index_path.exists(): return 0
        mapping = json.loads(index_path.read_text(encoding="utf-8"))
        count = 0
        for title, info in mapping.items():
            lesson_number = self.tp.get_lesson_number(title)
            if excluded_lessons:
                if lesson_number and (lesson_number in excluded_lessons or str(int(lesson_number)) in excluded_lessons): continue
            if only_lessons:
                if not lesson_number or (lesson_number not in only_lessons and str(int(lesson_number)) not in only_lessons): continue
            
            clean_title = re.sub(r"^\d+\s*-\s*", "", title).strip()
            if getattr(self, "is_1_page_mode", False):
                base_name = f"page_{lesson_number}-plan"
            elif getattr(self, "is_1_part_mode", False):
                base_name = f"part_{getattr(self, 'part_number', '1')}_lesson_{lesson_number}-plan"
            else:
                base_name = f"{lesson_number}-{clean_title}-plan"
            if list((self.project_root / "plans").glob(f"{base_name}*.md")):
                count += 1
        return count

    def run_batch_planning(
        self, max_concurrent=10, update_callback=None, excluded_lessons=None, only_lessons=None, force_remake=False
    ):
        """
        Main entry point. Orchestrates the batch processing.
        Args:
            update_callback (callable): Function(lesson_title, status, message)
            excluded_lessons (set): Set of lesson numbers (str) to skip.
        """
        if not update_callback:

            def default_callback(title, status, msg):
                logging.info(f"[{status}] {title}: {msg}")

            update_callback = default_callback

        if excluded_lessons is None:
            excluded_lessons = set()

        logging.info(f"\n🧠 Starting Jules Batch Planning (Max Concurrent: {max_concurrent})...")

        # 0. Wrap callback to include part number if in 1-part mode
        original_callback = update_callback
        def wrapped_callback(t, s, m):
            if getattr(self, "is_1_part_mode", False) and not t.startswith("[Part"):
                if t == "System":
                    t = f"System (Part {getattr(self, 'part_number', '1')})"
                else:
                    t = f"[Part {getattr(self, 'part_number', '1')}] {t}"
            original_callback(t, s, m)
        update_callback = wrapped_callback

        # 1. Get Lesson Index
        index_path = self.project_root / "system-workspace/text-data/raw_to_lesson_index.json"
        if not index_path.exists():
            update_callback("System", "WARN", "Lesson index missing. Generating...")
            mapping = self.tp.generate_lesson_index()
        else:
            mapping = json.loads(index_path.read_text(encoding="utf-8"))

        if not mapping:
            update_callback("System", "ERROR", "No lessons to process.")
            return

        # 2. Filter Processed Lessons?
        to_process = {}
        for title, info in mapping.items():
            lesson_number = self.tp.get_lesson_number(title)

            # Check Exclusions
            if excluded_lessons:
                if lesson_number and (lesson_number in excluded_lessons or str(int(lesson_number)) in excluded_lessons):
                    update_callback(title, "SKIP", f"Lesson {lesson_number} excluded (Page exists)")
                    continue

            if only_lessons:
                if not lesson_number or (lesson_number not in only_lessons and str(int(lesson_number)) not in only_lessons):
                    continue  # Skip if we only want specific lessons

            clean_title = re.sub(r"^\d+\s*-\s*", "", title).strip()
            
            if getattr(self, "is_1_page_mode", False):
                base_name = f"page_{lesson_number}-plan"
            elif getattr(self, "is_1_part_mode", False):
                base_name = f"part_{getattr(self, 'part_number', '1')}_lesson_{lesson_number}-plan"
            else:
                base_name = f"{lesson_number}-{clean_title}-plan"

            existing = list((self.project_root / "plans").glob(f"{base_name}*.md"))
            if existing and not force_remake:
                update_callback(title, "SKIP", "Plan exists")
            else:
                if force_remake and existing:
                    for f in existing:
                        try:
                            f.unlink()
                        except:
                            pass
                to_process[title] = info
                update_callback(title, "PENDING", "Queued")

        if not to_process:
            update_callback("System", "DONE", "All plans exist.")
            return

        # 3. Execute Batch
        def _get_num(t):
            import re
            m = re.match(r"^(\d+)", t)
            return int(m.group(1)) if m else 999
            
        sorted_items = sorted(to_process.items(), key=lambda x: _get_num(x[0]))
        
        with ThreadPoolExecutor(max_workers=max_concurrent) as executor:
            future_to_lesson = {
                executor.submit(
                    self.process_lesson_with_callback, title, info, update_callback
                ): title
                for title, info in sorted_items
            }

            for future in as_completed(future_to_lesson):
                pass  # The callback handles updates inside the future

        if hasattr(self, "pull_threads"):
            for t in self.pull_threads:
                t.join()

    def process_lesson_with_callback(self, lesson_title, range_info, callback):
        """Wrapper for process_lesson that uses callback."""
        # Note: callback is already wrapped by run_batch_planning
        callback(lesson_title, "RUNNING", "Starting...")
        try:
            self.process_lesson(lesson_title, range_info, callback)
        except Exception as e:
            callback(lesson_title, "ERROR", str(e))

    def process_lesson(self, lesson_title, range_info, callback=None, force_remake=False):
        """
        Worker function for a single lesson.
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
            callback(lesson_title, "RUNNING", f"Safety Delay ({delay:.1f}s)...")
            time.sleep(delay)

        # Attempt to parse number and title from the lesson_title (which is a key from index)
        match = re.match(r"^(\d+)\s*-\s*(.*)", lesson_title)
        if match:
            # Found "9 - Title"
            inferred_number = match.group(1).zfill(3)
            clean_title = match.group(2).strip()
            lesson_number = inferred_number
        else:
            # Fallback for "Title" only
            clean_title = lesson_title.strip()
            lesson_number = self.tp.get_lesson_number(clean_title)

        # Determine filename based on mode
        if getattr(self, "is_1_page_mode", False):
            base_filename = f"page_{lesson_number}-plan"
        elif getattr(self, "is_1_part_mode", False):
            p_num = getattr(self, "part_number", "1")
            base_filename = f"{lesson_number}.{p_num}_nXXX_{clean_title}-plan"
        else:
            base_filename = f"{lesson_number}-{clean_title}-plan"
            
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
            filename = f"{base_filename}_{workspace_code}.md"
        else:
            filename = f"{base_filename}.md"

        # 0. Check if Plan Exists (Early Exit)
        existing_files = list((self.project_root / "plans").glob(f"{base_filename}*.md"))
        if existing_files and not force_remake:
            callback(lesson_title, "SUCCESS", f"Plan exists: {existing_files[0].name}")
            return True

        callback(lesson_title, "RUNNING", "Extracting Text...")

        # 1. Extract Text
        raw_text = self._extract_lesson_text(range_info["start"], range_info["end"])
        if not raw_text:
            callback(lesson_title, "ERROR", "No text found")
            return False

        # 2. Get Metadata from TOC.json
        lesson_metadata = {}
        if self.tp.toc_path.exists():
            try:
                toc_data = json.loads(self.tp.toc_path.read_text(encoding="utf-8"))
                # Try to find by number (stripping leading zeros if key is integer-like string)
                key = str(int(lesson_number)) if lesson_number.isdigit() else lesson_number
                if key in toc_data:
                    lesson_metadata = toc_data[key]
                else:
                    # Fallback: search by title
                    for k, v in toc_data.items():
                        if v.get("title", "").strip() == clean_title:
                            lesson_metadata = v
                            break
            except Exception:
                pass

        # 3. Construct Prompt
        lesson_data = {
            "number": lesson_number,
            "title": clean_title,
            "raw_text": raw_text,
            "level": lesson_metadata.get("level", ""),
            "unit": lesson_metadata.get("Unit", ""),
            "author": lesson_metadata.get("author", ""),
            "author_number": lesson_metadata.get("author_number", ""),
        }
        mega_prompt = self.client.construct_mega_prompt(
            lesson_data, self.architect_prompt, self.auditor_prompt, getattr(self, "is_1_page_mode", False)
        )
        
        if workspace_code and workspace_code != "None":
            mega_prompt += f"\n\nIMPORTANT INSTRUCTION: You MUST append the batch workspace code '_{workspace_code}' to the filename of the generated plan (e.g. {base_filename}_{workspace_code}.md)."

        mega_prompt += f"\n\nCRITICAL PATH INSTRUCTION: Do NOT place the generated plan inside `Jules-workspace/plans/`. You MUST place the generated plan in the root `plans/` directory."


        # 4. Check or Create Session
        session_id = None
        session_key = f"session_id_{base_filename}"

        # Check State Manager for existing session
        if self.state_manager:
            session_id = self.state_manager.get_lesson_data(lesson_title, session_key)
            if session_id:
                callback(lesson_title, "RUNNING", f"Checking Existing Session ({session_id})...")
                status_data = self.client.get_session_status(session_id)
                if status_data:
                    state = status_data.get("state", "UNKNOWN")
                    if state in ["SUCCEEDED", "COMPLETED"]:
                        callback(lesson_title, "RUNNING", f"Existing Session Completed: {state}")
                        # Skip creation, jump to pull
                    elif state in ["FAILED", "CANCELLED", "ERROR"]:
                        callback(
                            lesson_title,
                            "WARN",
                            f"Previous Session Failed ({state}). Creating New...",
                        )
                        session_id = None  # Force new session
                    else:
                        # RUNNING or UNKNOWN
                        callback(lesson_title, "RUNNING", f"Resuming Monitoring ({state})...")
                        # Keep session_id, proceed to wait
                else:
                    callback(lesson_title, "WARN", "Existing Session ID invalid. Creating New...")
                    session_id = None

        if not session_id:
            callback(lesson_title, "RUNNING", "Creating Session...")
            try:
                session = self.client.create_plan_session(base_filename, mega_prompt)
            except APIBlockError as e:
                self.abort_event.set()
                callback(lesson_title, "API_BLOCKED", "API Quota/Limit Reached")
                return

            if not session:
                callback(lesson_title, "ERROR", "Session Creation Failed")
                return False

            session_id = session.get("name")
            if self.state_manager:
                self.state_manager.update_lesson_data(lesson_title, {session_key: session_id})

        callback(lesson_title, "RUNNING", f"Monitoring Session ({session_id})...")

        # 5. Monitor Session
        # Define status callback for wait_for_completion
        def status_update(state):
            callback(lesson_title, "RUNNING", f"Status: {state}")

        status = self.client.wait_for_completion(
            session_id, timeout_minutes=20, status_callback=status_update
        )

        if status not in ["SUCCEEDED", "COMPLETED"]:
            callback(lesson_title, "FAILED", f"Session ended: {status}")
            return False

        # 6. Pull Result asynchronously to free up the thread for a new session immediately
        def bg_pull():
            callback(lesson_title, "PULLING", "Pulling Plan in background...")
            details = self.client.get_session_details(session_id)
            if not details:
                callback(lesson_title, "WARN", "No PR found. Manual check needed.")
                return

            target_path = f"plans/{filename}"

            def pr_callback(ignored_path, state, msg):
                callback(lesson_title, state, msg)

            success = self.client.finalize_pr_and_pull(details, target_path, callback=pr_callback)
            if success:
                callback(lesson_title, "SUCCESS", f"Plan saved: {filename}")
            else:
                callback(lesson_title, "ERROR", "Pull Failed")

        import threading
        t = threading.Thread(target=bg_pull, daemon=False)
        if not hasattr(self, "pull_threads"):
            self.pull_threads = []
        self.pull_threads.append(t)
        t.start()
        
        # We don't wait for bg_pull here to free the executor slot, 
        # but we will join it at the end of run_batch_planning.
        return True


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    planner = JulesPlanner()
    planner.run_batch_planning(max_concurrent=2)
