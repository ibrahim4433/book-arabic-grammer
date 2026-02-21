#!/usr/bin/env python3
import os
import subprocess
import json
import re
import time
import requests
from pathlib import Path

# --- CONFIGURATION ---
PROJECT_ROOT = Path(__file__).parent.parent.parent
RAW_DIR = PROJECT_ROOT / "system-workspace/text-data/raw"
PLANS_DIR = PROJECT_ROOT / "plans"
RATINGS_DIR = PROJECT_ROOT / "ratings"
INDEX_FILE = PROJECT_ROOT / "system-workspace/text-data/raw_to_lesson_index.json"
STATE_FILE = PROJECT_ROOT / "tools/automation/project_state.json"
SECRETS_DIR = PROJECT_ROOT / "secrets"

JULES_API_URL = "https://jules.googleapis.com/v1alpha/sessions"
JULES_SOURCE = "sources/github/ibrahim4433/book-arabic-grammer"

# --- HELPERS ---

def load_json(path):
    if path.exists():
        return json.loads(path.read_text(encoding='utf-8'))
    return {}

def save_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')

def run_gemini(prompt, files=None):
    cmd = ["gemini", "--prompt", prompt]
    if files:
        for f in files:
            cmd.append("\n\n@ " + str(f))
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ Gemini CLI Error: {e.stderr}")
        return None

def get_lesson_text(lesson_name, index):
    if lesson_name not in index:
        return None
    
    start_info = index[lesson_name]["start"].split(':')
    end_info = index[lesson_name]["end"].split(':')
    
    start_file = start_info[0]
    start_line = int(start_info[1])
    
    end_file = end_info[0]
    end_line = int(end_info[1])
    
    all_lines = []
    def sort_key(p):
        return int(p.stem.split('_')[1])
    raw_files = sorted(list(RAW_DIR.glob("raw_*.txt")), key=sort_key)
    
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

class JulesClient:
    def __init__(self):
        self.api_key = (SECRETS_DIR / "Jules_API.txt").read_text().strip()
        self.headers = {
            "X-Goog-Api-Key": self.api_key,
            "Content-Type": "application/json"
        }

    def create_session(self, prompt, title):
        payload = {
            "prompt": prompt,
            "sourceContext": {
                "source": JULES_SOURCE,
                "githubRepoContext": { "startingBranch": "main" }
            },
            "automationMode": "AUTO_CREATE_PR",
            "title": title
        }
        resp = requests.post(JULES_API_URL, headers=self.headers, json=payload)
        if resp.status_code == 200:
            return resp.json()["name"]
        else:
            print(f"❌ Jules Session Creation Failed: {resp.text}")
            return None

    def poll_session(self, session_name):
        print(f"⏳ Waiting for Jules ({session_name})...")
        url = f"https://jules.googleapis.com/v1alpha/{session_name}"
        while True:
            resp = requests.get(url, headers=self.headers)
            data = resp.json()
            state = data.get("state")
            if state == "COMPLETED":
                print("✅ Jules finished task.")
                return data
            elif state == "FAILED":
                print("❌ Jules session failed.")
                return data
            elif state == "SUGGESTION_PENDING":
                print("❓ Jules needs input.")
                return data
            time.sleep(30)

# --- WORKFLOW ---

def process_lessons(lesson_names):
    print(f"\n🚀 Processing Lessons: {', '.join(lesson_names)}")
    
    index = load_json(INDEX_FILE)
    state = load_json(STATE_FILE)
    
    combined_text = ""
    for name in lesson_names:
        text = get_lesson_text(name, index)
        if text:
            combined_text += f"\n\n--- {name} ---\n{text}"
        else:
            print(f"⚠️ Lesson '{name}' not found.")

    if not combined_text:
        return

    # Use first lesson name for file reference
    base_name = lesson_names[0].replace(' ', '_')
    PLANS_DIR.mkdir(exist_ok=True)
    plan_path = PLANS_DIR / ("plan_" + base_name + "_batch.md")
    
    print("🧠 Generating Combined Plan...")
    arch_prompt = (PROJECT_ROOT / "Architect_GEM_PROMPT.md").read_text()
    prompt = arch_prompt + "\n\n=== PROJECT STATE ===\n" + json.dumps(state) + "\n\n=== LESSON CONTENT ===\n" + combined_text
    
    plan_content = run_gemini(prompt)
    if plan_content:
        plan_path.write_text(plan_content, encoding='utf-8')
        print(f"✅ Plan saved to {plan_path}")
    else:
        return

    jules = JulesClient()
    session_name = jules.create_session("Execute this Architect Plan strictly:\n\n" + plan_content, "Batch: " + ", ".join(lesson_names))
    if not session_name: return
    
    print("🔗 Jules Session: https://jules.google/sessions/" + session_name.split('/')[-1])
    jules.poll_session(session_name)
    print("🔔 Jules has finished. Please review the PR on GitHub.")

def main():
    import sys
    index = load_json(INDEX_FILE)
    if len(sys.argv) < 2:
        if not index:
            print("❌ Index is empty.")
            return
        # Default to first two lessons if small
        first_lessons = list(index.keys())[:2]
        process_lessons(first_lessons)
    else:
        process_lessons(sys.argv[1:])

if __name__ == "__main__":
    main()