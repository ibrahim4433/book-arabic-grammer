import sys
import os
import json
import time
import re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# Ensure modules are importable
sys.path.append(str(Path(__file__).parent))

from jules_client import JulesClient
from gemini_client import GeminiClient
from jules_client_plans import JulesPlanClient  # Reusing PR pulling logic

class JulesPageGenerator:
    """
    Orchestrates the batch generation of HTML Pages from Plans using Jules Sessions.
    Handles interactive Q&A with Gemini Headless.
    """

    def __init__(self, project_root=None):
        self.project_root = Path(project_root) if project_root else Path(__file__).parent.parent.parent.parent.parent
        self.jules_client = JulesPlanClient(project_root=self.project_root) # Reuse for PR pulling
        self.gemini_client = GeminiClient(project_root=self.project_root)
        
        # Load Context for Gemini (Headless)
        self.context_files = [
            "GEMINI.md",
            "CODING_STANDARDS.md",
            "assets/Templates/TEMPLATE_C_BASE.html"
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

    def _monitor_and_handle_session(self, session_id, lesson_title):
        """
        Monitors a running session.
        If Jules asks a question (WAITING_FOR_INPUT or similar), uses Gemini to answer.
        """
        print(f"👀 Monitoring {lesson_title} ({session_id})...")
        
        # We poll for a bit longer than standard planning because coding takes time
        start_time = time.time()
        timeout = 25 * 60 # 25 minutes
        
        while time.time() - start_time < timeout:
            status_data = self.jules_client.get_session_status(session_id)
            if not status_data:
                time.sleep(30)
                continue
                
            state = status_data.get('state', 'UNKNOWN')
            print(f"   [{lesson_title}] Status: {state}")
            
            # 1. Handle Success
            if state == 'SUCCEEDED':
                return "SUCCEEDED"
                
            # 2. Handle Failure
            if state in ['FAILED', 'CANCELLED']:
                return state
                
            # 3. Handle Interaction (Hypothetical state 'NEEDS_INPUT' or 'WAITING_FOR_USER_INPUT')
            # If the API doesn't explicitly say "WAITING", we might infer from 'turns' 
            # if the last turn was from MODEL and it ended with a question mark?
            # For now, let's assume a state or if the log indicates waiting.
            # If we don't know the exact state name for waiting, we rely on the user's description.
            # "if Jules asked questions..." implies a pause.
            
            # Let's check the last message from the Model
            last_msg = self.jules_client.get_latest_message(status_data)
            
            if state == "NEEDS_INTERACTION" or (last_msg and "?" in last_msg and state not in ['SUCCEEDED', 'FAILED']):
                 # Heuristic: If it looks like a question and not done, answer it.
                 # But we must be careful not to answer the *same* question twice.
                 # We need to track turns.
                 pass # Logic to be added if we can confirm state. 
            
            # If the system explicitly exposes a "waiting" state (e.g. 'ACTION_REQUIRED'), handle it.
            if state == 'ACTION_REQUIRED' or state == 'WAITING_FOR_INPUT':
                print(f"❓ [{lesson_title}] Jules is asking for input...")
                
                question = self.jules_client.get_latest_message(status_data)
                if not question:
                    question = "Please continue." # Fallback
                
                print(f"   Question: {question[:100]}...")
                
                # Ask Gemini Headless
                answer = self._ask_gemini_headless(question)
                print(f"   💡 Gemini Answer: {answer[:100]}...")
                
                # Send back
                self.jules_client.send_response(session_id, answer)
                
                # Wait a bit to let it process
                time.sleep(10)

            time.sleep(30)
            
        return "TIMEOUT"

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
        if not callback: callback = lambda t, s, m: print(f"[{s}] {t}: {m}")

        plan_content = plan_path.read_text(encoding='utf-8')
        lesson_title = plan_path.stem
        
        # 1. Start Session
        callback(lesson_title, "RUNNING", "Starting Session...")
        
        prompt = (
            f"Generate the HTML page for the following plan.\n"
            f"Use the templates in `assets/Templates/`.\n"
            f"Follow `GEMINI.md` rules strictly (One-Page Law, Tashkeel, IDs).\n"
            f"The output file should be `pages/{lesson_title.replace('-plan', '.html')}` (adjust naming to nXX format if needed).\n"
            f"PLAN:\n{plan_content}"
        )
        
        session = self.jules_client.create_session(prompt, f"PageGen: {lesson_title}", automation_mode="AUTO_CREATE_PR")
        if not session:
            callback(lesson_title, "ERROR", "Session Create Failed")
            return False
            
        session_id = session.get('name')
        callback(lesson_title, "RUNNING", f"Monitoring {session_id}...")
        
        # 2. Monitor
        status = self._monitor_and_handle_session(session_id, lesson_title, callback)
        
        if status != "SUCCEEDED":
            callback(lesson_title, "FAILED", f"Ended with {status}")
            return False
            
        # 3. Pull Result
        callback(lesson_title, "RUNNING", "Pulling Page...")
        details = self.jules_client.get_session_details(session_id)
        target_file = f"{lesson_title.replace('-plan', '')}.html" 
        
        success = self.jules_client.pull_plan_from_github(details, f"pages/{target_file}")
        
        if success:
            callback(lesson_title, "SUCCESS", f"Page Saved: {target_file}")
            return True
        else:
             callback(lesson_title, "WARN", "Pull failed, check Branch.")
             return False

    def _monitor_and_handle_session(self, session_id, lesson_title, callback):
        """
        Monitors a running session.
        If Jules asks a question, uses Gemini to answer.
        """
        start_time = time.time()
        timeout = 25 * 60 # 25 minutes
        
        while time.time() - start_time < timeout:
            status_data = self.jules_client.get_session_status(session_id)
            if not status_data:
                time.sleep(30)
                continue
                
            state = status_data.get('state', 'UNKNOWN')
            
            # Update Status only if changed? Or just show current state
            # callback(lesson_title, "RUNNING", f"State: {state}")

            if state == 'SUCCEEDED':
                return "SUCCEEDED"
            if state in ['FAILED', 'CANCELLED']:
                return state
                
            if state == 'ACTION_REQUIRED' or state == 'WAITING_FOR_INPUT':
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

    def run_batch_generation(self, max_concurrent=5, update_callback=None):
        """
        Main entry point.
        """
        if not update_callback:
            def update_callback(t, s, m): print(f"[{s}] {t}: {m}")

        print(f"\n🏭 Starting Jules Page Generation (Batch Size: {max_concurrent})...")
        
        plans_dir = self.project_root / "plans"
        plans = sorted(list(plans_dir.glob("*.md")))
        
        if not plans:
            update_callback("System", "WARN", "No plans found.")
            return

        update_callback("System", "INFO", f"Found {len(plans)} plans.")
        
        with ThreadPoolExecutor(max_workers=max_concurrent) as executor:
            future_to_plan = {
                executor.submit(self.process_plan, plan, update_callback): plan.stem
                for plan in plans
            }
            
            for future in as_completed(future_to_plan):
                pass # Callbacks handle updates
