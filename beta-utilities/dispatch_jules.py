import requests
import json
import os
from pathlib import Path

# --- CONFIGURATION ---
PROJECT_ROOT = Path(__file__).parent.parent
SECRETS_DIR = PROJECT_ROOT / "secrets"
JULES_API_URL = "https://jules.googleapis.com/v1alpha/sessions"
JULES_SOURCE = "sources/github/ibrahim4433/book-arabic-grammer"

def load_key(filename):
    with open(SECRETS_DIR / filename, 'r') as f:
        return f.read().strip()

def create_jules_session(api_key, plan_content, title):
    headers = {
        "X-Goog-Api-Key": api_key,
        "Content-Type": "application/json"
    }
    # Using a simple string concat to avoid multi-line f-string issues in write_file
    prompt_text = "Execute this Architect Plan strictly:\n\n" + plan_content
    payload = {
        "prompt": prompt_text,
        "sourceContext": {
            "source": JULES_SOURCE,
            "githubRepoContext": {
                "startingBranch": "main"
            }
        },
        "automationMode": "AUTO_CREATE_PR",
        "title": title
    }
    print(f"🚀 Dispatching: {title}...")
    resp = requests.post(JULES_API_URL, headers=headers, json=payload)
    if resp.status_code == 200:
        data = resp.json()
        print(f"✅ Created: {data['name']}")
        return data['name']
    else:
        print(f"❌ Failed: {resp.status_code} - {resp.text}")
        return None

def main():
    api_key = load_key("Jules_API.txt")
    
    plans = [
        {"path": PROJECT_ROOT / "output/plan_1.md", "title": "Lesson 28: As-Sarf and Mizan"},
        {"path": PROJECT_ROOT / "output/plan_2.md", "title": "Lesson 29: Verb Types and Augmentation"}
    ]
    
    for plan_info in plans:
        if plan_info["path"].exists():
            with open(plan_info["path"], 'r', encoding='utf-8') as f:
                plan_content = f.read()
            create_jules_session(api_key, plan_content, plan_info["title"])
        else:
            print(f"⚠️ Plan file not found: {plan_info['path']}")

if __name__ == "__main__":
    main()