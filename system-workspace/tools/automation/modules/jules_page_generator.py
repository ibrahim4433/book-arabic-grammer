import sys
import time
import random
import logging
import re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# Ensure modules are importable
sys.path.append(str(Path(__file__).parent))

from gemini_client import GeminiClient
from jules_client_plans import JulesPlanClient  # Reusing PR pulling logic
from github_utils import GithubClient

class JulesPageGenerator:
    """
    Orchestrates the batch generation of HTML Pages from Plans using Jules Sessions.
    Handles interactive Q&A with Gemini Headless.
    """

    def __init__(self, project_root=None, state_manager=None):
        self.project_root = Path(project_root) if project_root else Path(__file__).parent.parent.parent.parent.parent
        self.state_manager = state_manager
        self.jules_client = JulesPlanClient(project_root=self.project_root) # Reuse for PR pulling
        self.gemini_client = GeminiClient(project_root=self.project_root)
        self.github = GithubClient(token_path=self.project_root / "secrets/Github_Token.txt")
        
        # Load Context for Gemini (Headless)
        self.context_files = [
            "GEMINI.md",
            "CODING_STANDARDS.md",
            "Jules-workspace/Templates/TEMPLATE_C_BASE.html"
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
        if not callback:
            def default_callback(t, s, m):
                logging.info(f"[{s}] {t}: {m}")
            callback = default_callback

        # API Safety Delay (5-15s) to prevent burst
        delay = random.uniform(5, 15)
        callback(plan_path.stem, "RUNNING", f"Safety Delay ({delay:.1f}s)...")
        time.sleep(delay)

        plan_content = plan_path.read_text(encoding='utf-8')
        lesson_title = plan_path.stem
        
        # Extract Lesson Number
        match = re.match(r'^(\d+)', lesson_title)
        lesson_num = match.group(1) if match else None

        # 1. Check Existing Session
        session_id = None
        state_key = None # Key used in StateManager

        if self.state_manager and lesson_num:
            # Try to find matching key in StateManager
            all_lessons = self.state_manager.get_all_lessons()
            for key in all_lessons.keys():
                if key.startswith(f"{lesson_num} -") or key.startswith(f"{str(int(lesson_num))} -"):
                    state_key = key
                    break

            if state_key:
                stored_sid = self.state_manager.get_lesson_data(state_key, "page_session_id")
                if stored_sid:
                    callback(lesson_title, "RUNNING", f"Checking Existing Session ({stored_sid})...")
                    status_data = self.jules_client.get_session_status(stored_sid)
                    if status_data:
                        state = status_data.get('state', 'UNKNOWN')
                        if state in ['SUCCEEDED', 'COMPLETED']:
                            callback(lesson_title, "RUNNING", "Existing Session Completed. Pulling...")
                            session_id = stored_sid
                            # Skip creation & monitoring
                        elif state in ['FAILED', 'CANCELLED']:
                            callback(lesson_title, "WARN", f"Previous Session Failed ({state}). Creating New...")
                            session_id = None
                        else:
                            callback(lesson_title, "RUNNING", f"Resuming Session ({state})...")
                            session_id = stored_sid
        
        # 2. Start Session (if needed)
        if not session_id:
            callback(lesson_title, "RUNNING", "Starting Session...")
            
            prompt = (
                f"Generate the HTML page for the following plan.\n"
                f"Use the templates in `Jules-workspace/Templates/`.\n"
                f"Follow `GEMINI.md` rules strictly (One-Page Law, Tashkeel, IDs).\n"
                f"The output file should be `pages/{lesson_title.replace('-plan', '.html')}` (Keep nXX as it is without replaceing XX with numbers !).\n"
                f"PLAN:\n{plan_content}"
            )

            session = self.jules_client.create_session(prompt, f"PageGen: {lesson_title}", automation_mode="AUTO_CREATE_PR")
            if not session:
                callback(lesson_title, "ERROR", "Session Create Failed")
                return False

            session_id = session.get('name')

            # Save Session ID
            if self.state_manager:
                if not state_key:
                     # Create a new key if not found (best guess)
                     clean_title = lesson_title.replace("-plan", "").replace("-", " ")
                     state_key = clean_title # Fallback
                self.state_manager.update_lesson_data(state_key, {"page_session_id": session_id})

        callback(lesson_title, "RUNNING", f"Monitoring {session_id}...")
        
        # 3. Monitor (if not already done)
        # Check status first to see if we can skip monitoring
        status_data = self.jules_client.get_session_status(session_id)
        current_state = status_data.get('state', 'UNKNOWN') if status_data else 'UNKNOWN'

        if current_state in ['SUCCEEDED', 'COMPLETED']:
             status = "SUCCEEDED"
        else:
             status = self._monitor_and_handle_session(session_id, lesson_title, callback)
        
        if status != "SUCCEEDED":
            callback(lesson_title, "FAILED", f"Ended with {status}")
            return False
            
        # 4. Pull Result
        callback(lesson_title, "RUNNING", "Downloading generated page...")
        details = self.jules_client.get_session_details(session_id)
        
        # Attempt 1: Exact Match Pull using JulesPlanClient logic
        target_file = f"{lesson_title.replace('-plan', '')}.html"
        target_path = f"pages/{target_file}"

        success = self.jules_client.finalize_pr_and_pull(details, target_path, callback=callback)
        
        if success:
            callback(lesson_title, "SUCCESS", f"Page Saved: {target_file}")
            return True

        # Attempt 2: Smart Search in Branch (Fallback)
        callback(lesson_title, "WARN", "Exact Pull Failed. Searching Branch...")

        branch = details.get('branch')
        if not branch:
             callback(lesson_title, "ERROR", "No Branch info found.")
             return False

        repo_full_name = f"{self.jules_client.repo_owner}/{self.jules_client.repo_name}"

        try:
            # List files in pages/ directory of the branch
            files = self.github.get_file_info(repo_full_name, "pages", branch)

            found_url = None
            found_name = None

            if files and isinstance(files, list):
                # Try to find a file that matches the lesson number
                match = re.search(r'^(\d+)', lesson_title)
                lesson_num = match.group(1) if match else None

                for f in files:
                    if not f['name'].endswith(".html"):
                        continue

                    # If we have a number, check if file starts with it
                    if lesson_num:
                        if f['name'].startswith(lesson_num) or f['name'].startswith(str(int(lesson_num))):
                            found_url = f['download_url']
                            found_name = f['name']
                            break
                    else:
                        # Fallback: Check if file name is similar to target?
                        # Or just take the first HTML if we assume 1-to-1 session?
                        # Let's match stem at least partially
                        if lesson_title.replace('-plan', '') in f['name']:
                             found_url = f['download_url']
                             found_name = f['name']
                             break

            if found_url:
                 callback(lesson_title, "DOWN", f"Found alternative: {found_name}")
                 local_path = self.project_root / "pages" / found_name
                 if self.github.download_file(found_url, local_path):
                      callback(lesson_title, "SUCCESS", f"Page Saved: {found_name}")
                      return True
                 else:
                      callback(lesson_title, "ERROR", "Download Failed")
                      return False
            else:
                 callback(lesson_title, "ERROR", "File not found in branch.")
                 return False

        except Exception as e:
            callback(lesson_title, "ERROR", f"Search Exception: {e}")
            return False

    def _monitor_and_handle_session(self, session_id, lesson_title, callback):
        """
        Monitors a running session.
        If Jules asks a question, uses Gemini to answer.
        """
        start_time = time.time()
        timeout = 25 * 60 # 25 minutes
        last_log_time = start_time
        
        while time.time() - start_time < timeout:
            status_data = self.jules_client.get_session_status(session_id)
            if not status_data:
                time.sleep(30)
                continue
                
            state = status_data.get('state', 'UNKNOWN')
            
            # Periodic Heartbeat Log (Every 60s)
            if time.time() - last_log_time > 60:
                elapsed_min = int((time.time() - start_time) / 60)
                callback(lesson_title, "RUNNING", f"Still running... ({elapsed_min}m elapsed)")
                last_log_time = time.time()

            if state in ['SUCCEEDED', 'COMPLETED']:
                return "SUCCEEDED"
            if state in ['FAILED', 'CANCELLED']:
                return state
                
            if state in ['ACTION_REQUIRED', 'WAITING_FOR_INPUT']:
                callback(lesson_title, "INTERACT", "Jules needs input...")
                
                question = self.jules_client.get_latest_message(status_data)
                if not question: question = "Please continue."
                
                # Ask Gemini Headless
                answer = self._ask_gemini_headless(question)
                callback(lesson_title, "INTERACT", "Sending Answer...")
                
                self.jules_client.send_response(session_id, answer)
                time.sleep(10)

            time.sleep(30)
            
        return "TIMEOUT"

    def run_batch_generation(self, max_concurrent=5, update_callback=None, excluded_lessons=None):
        """
        Main entry point.
        """
        if not update_callback:
            def update_callback(t, s, m): logging.info(f"[{s}] {t}: {m}")

        if excluded_lessons is None:
            excluded_lessons = set()

        logging.info(f"\n🏭 Starting Jules Page Generation (Batch Size: {max_concurrent})...")
        
        plans_dir = self.project_root / "plans"
        all_plans = sorted(list(plans_dir.glob("*.md")))
        
        if not all_plans:
            update_callback("System", "WARN", "No plans found.")
            return

        to_process = []
        for plan in all_plans:
            # Check if output exists
            html_name = plan.name.replace("-plan.md", ".html")
            html_path = self.project_root / "pages" / html_name

            # Check Lesson Number (Assuming "09-Title-plan.md")
            match = re.match(r'^(\d+)', plan.name)
            lesson_num = match.group(1) if match else None

            if html_path.exists():
                update_callback(plan.stem, "SKIP", "HTML exists")
                continue

            if lesson_num and (lesson_num in excluded_lessons or str(int(lesson_num)) in excluded_lessons):
                update_callback(plan.stem, "SKIP", "Excluded (Page exists)")
                continue

            to_process.append(plan)

        update_callback("System", "INFO", f"Queued {len(to_process)} plans for generation.")
        
        with ThreadPoolExecutor(max_workers=max_concurrent) as executor:
            future_to_plan = {
                executor.submit(self.process_plan, plan, update_callback): plan.stem
                for plan in to_process
            }
            
            for future in as_completed(future_to_plan):
                pass # Callbacks handle updates
