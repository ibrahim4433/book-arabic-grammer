#!/usr/bin/env python3
import os
import sys
import time
import json
import argparse
import subprocess
import requests
from pathlib import Path
from workflow_state import WorkflowState, STATE_RAW, STATE_PLANNED, STATE_PENDING_JULES, STATE_CODED, STATE_VERIFIED

# --- CONFIGURATION ---
PROJECT_ROOT = Path(__file__).parent.parent.parent
PLANS_DIR = PROJECT_ROOT / "plans"
RAW_DIR = PROJECT_ROOT / "output/text-data/raw"
SECRETS_DIR = PROJECT_ROOT / "secrets"
JULES_API_URL = "https://jules.googleapis.com/v1alpha"
REPO_NAME = "ibrahim4433/book-arabic-grammer"
DEBUG_DIR = PROJECT_ROOT / "output/debug"

def get_secret(name):
    secret_file = SECRETS_DIR / f"{name}.txt"
    if secret_file.exists():
        return secret_file.read_text().strip()
    return os.getenv(name.upper())

class GithubClient:
    """Handles PR merging and repository updates."""
    def __init__(self, token):
        self.token = token
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }

    def get_latest_pr(self):
        url = f"https://api.github.com/repos/{REPO_NAME}/pulls"
        resp = requests.get(url, headers=self.headers)
        if resp.status_code == 200:
            prs = resp.json()
            # Return newest open PR
            return prs[0] if prs else None
        return None

    def merge_pr(self, pr_number):
        print(f"🔀 Merging PR #{pr_number}...")
        url = f"https://api.github.com/repos/{REPO_NAME}/pulls/{pr_number}/merge"
        resp = requests.put(url, headers=self.headers)
        if resp.status_code == 200:
            print("✅ PR Merged Successfully.")
            # Local update
            subprocess.run(["git", "pull", "origin", "main"], check=True)
            return True
        else:
            print(f"❌ Merge Failed: {resp.text}")
            return False

class ProxyAgent:
    """Handles Jules' questions by consulting the project context."""
    def answer_question(self, question, plan_content):
        print(f"🤔 Proxy Agent thinking about: {question}")
        prompt = f"""
        You are the Project Manager for this book.
        The developer (Jules) asked: "{question}"
        
        CONTEXT:
        We are building an HTML5 Arabic Grammar book.
        Strictly follow 'design_patterns.json' and the Plan below.
        
        PLAN:
        {plan_content[:2000]}...
        
        Answer the question concisely to unblock the developer.
        """
        try:
            cmd = ["gemini", "--non-interactive", "--output-format", "text"]
            result = subprocess.run(cmd, input=prompt, capture_output=True, text=True, encoding='utf-8')
            return result.stdout.strip()
        except:
            return "Proceed according to standard templates."

class WorkflowManager:
    def __init__(self):
        self.state = WorkflowState()
        self.proxy = ProxyAgent()
        self.jules_key = get_secret("Jules_API")
        self.github_token = get_secret("Github_Token")
        
        if not self.jules_key:
            print("⚠️ Warning: Jules API Key not found.")
        
        self.headers = {"X-Goog-Api-Key": self.jules_key, "Content-Type": "application/json"}
        self.github = GithubClient(self.github_token) if self.github_token else None

    def generate_plan(self, lesson_name, raw_path):
        print("🧠 Phase 2: Planning (Refiner Loop)...")
        output_plan = PLANS_DIR / f"plan_{lesson_name}.md"
        cmd = [sys.executable, str(PROJECT_ROOT / "tools/automation/plan_refiner.py"), str(raw_path), str(output_plan)]
        result = subprocess.run(cmd)
        if result.returncode == 0:
            self.state.update_lesson(lesson_name, status=STATE_PLANNED, plan_file=str(output_plan))
            return output_plan
        else:
            print("❌ Planning failed.")
            sys.exit(1)

    def execute_jules(self, lesson_name, plan_path):
        print("🚀 Phase 3: Jules Execution...")
        if not self.jules_key: return

        plan_content = Path(plan_path).read_text(encoding='utf-8')
        payload = {
            "prompt": f"Execute this Architect Plan strictly:\n\n{plan_content}",
            "sourceContext": {"githubRepo": {"name": REPO_NAME}},
            "config": {"tools": ["EDIT_CODE", "RUN_COMMAND"]}
        }
        
        try:
            resp = requests.post(f"{JULES_API_URL}/sessions", headers=self.headers, json=payload)
            resp.raise_for_status()
            session_name = resp.json()["name"]
            print(f"✅ Session Started: {session_name}")
            self.state.update_lesson(lesson_name, status=STATE_PENDING_JULES, session_id=session_name)
            self.monitor_session(session_name, plan_content)
            
            # Post-Jules: Check for PR and Merge
            if self.github:
                print("⏳ Checking for Pull Request...")
                time.sleep(10) # Give Jules a moment to create the PR
                pr = self.github.get_latest_pr()
                if pr:
                    self.github.merge_pr(pr["number"])
            
            self.state.update_lesson(lesson_name, status=STATE_CODED)

        except Exception as e:
            print(f"❌ Jules Error: {e}")

    def monitor_session(self, session_name, plan_content):
        print("⏳ Monitoring Jules...")
        while True:
            time.sleep(15)
            try:
                resp = requests.get(f"{JULES_API_URL}/{session_name}", headers=self.headers)
                data = resp.json()
                state = data.get("state")
                print(f"   Status: {state}")
                if state == "COMPLETED": break
                elif state == "FAILED": break
                elif state == "SUGGESTION_PENDING":
                    question = "Jules needs clarification on the data structure."
                    answer = self.proxy.answer_question(question, plan_content)
                    print(f"   Proxy Replying: {answer}")
            except: break

    def verify_result(self, lesson_name):
        print("🔍 Phase 4: Verification...")
        files = sorted(list((PROJECT_ROOT / "pages").glob("*.html")), key=os.path.getmtime)
        if not files: return
        newest_file = files[-1]
        print(f"   Verifying: {newest_file.name}")
        cmd = [sys.executable, str(PROJECT_ROOT / "tools/automation/verify_headless.py"), str(newest_file)]
        result = subprocess.run(cmd, capture_output=True, text=True)
        try:
            data = json.loads(result.stdout)
            if data["status"] == "PASS":
                print("✅ Verification Passed.")
                self.state.update_lesson(lesson_name, status=STATE_VERIFIED)
            else:
                print(f"❌ Verification Failed: {data['status']}")
        except: print("❌ Verification script failed.")

    def get_lesson_text(self, lesson_name):
        index_file = PROJECT_ROOT / "system workspace/text-data/raw_to_lesson_index.json"
        if not index_file.exists():
            return None
        
        index = json.loads(index_file.read_text(encoding='utf-8'))
        if lesson_name not in index:
            return None
            
        start_info = index[lesson_name]["start"].split(':')
        end_info = index[lesson_name]["end"].split(':')
        
        start_file, start_line = start_info[0], int(start_info[1])
        end_file, end_line = end_info[0], int(end_info[1])
        
        # Sort raw files numerically
        def sort_key(p):
            return int(p.stem.split('_')[1])
        raw_files = sorted(list(RAW_DIR.glob("raw_*.txt")), key=sort_key)
        
        all_lines = []
        collecting = False
        for rf in raw_files:
            if rf.name == start_file:
                collecting = True
                lines = rf.read_text(encoding='utf-8').splitlines()
                if rf.name == end_file:
                    return "\n".join(lines[start_line-1 : end_line])
                else:
                    all_lines.extend(lines[start_line-1:])
            elif collecting:
                lines = rf.read_text(encoding='utf-8').splitlines()
                if rf.name == end_file:
                    all_lines.extend(lines[:end_line])
                    break
                else:
                    all_lines.extend(lines)
        return "\n".join(all_lines)

    def run(self, lesson_name):
        print(f"🚀 Processing Lesson: {lesson_name}")
        
        lesson_text = self.get_lesson_text(lesson_name)
        if not lesson_text:
            print(f"❌ Could not find text for lesson: {lesson_name}")
            return

        # Save to temp file for the refiner
        temp_lesson_path = PROJECT_ROOT / f"output/text-data/current_lesson.txt"
        temp_lesson_path.write_text(lesson_text, encoding='utf-8')
        
        plan_path = self.generate_plan(lesson_name, temp_lesson_path)
        self.execute_jules(lesson_name, plan_path)
        self.verify_result(lesson_name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("lesson")
    args = parser.parse_args()
    wm = WorkflowManager()
    wm.run(args.lesson)
