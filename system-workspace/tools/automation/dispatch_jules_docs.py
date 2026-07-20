import os
import glob
from pathlib import Path
import requests
import json

# --- CONFIGURATION ---
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent
SECRETS_DIR = PROJECT_ROOT / "secrets"
JULES_API_URL = "https://jules.googleapis.com/v1alpha/sessions"
JULES_SOURCE = "sources/github/ibrahim4433/book-arabic-grammer"


def load_key(filename):
    secret_path = SECRETS_DIR / filename
    if not secret_path.exists():
        print(f"❌ Secret file not found: {secret_path}")
        return None
    with open(secret_path) as f:
        return f.read().strip()


def create_jules_session(api_key, plan_content, title):
    headers = {"X-Goog-Api-Key": api_key, "Content-Type": "application/json"}

    # We construct the prompt to instruct Jules to follow the plan exactly
    prompt_text = "Execute this Architect Plan strictly:\n\n" + plan_content
    payload = {
        "prompt": prompt_text,
        "sourceContext": {"source": JULES_SOURCE, "githubRepoContext": {"startingBranch": "main"}},
        "automationMode": "AUTO_CREATE_PR",
        "title": title,
    }

    print(f"🚀 Dispatching session for: {title}...")
    resp = requests.post(JULES_API_URL, headers=headers, json=payload)
    if resp.status_code == 200:
        data = resp.json()
        print(f"✅ Created Session: {data['name']}")
        return data["name"]
    else:
        print(f"❌ Failed: {resp.status_code} - {resp.text}")
        return None


def main():
    api_key = load_key("Jules_API.txt")
    if not api_key:
        return

    prompts_dir = PROJECT_ROOT / "system-workspace" / "prompts_for_docs"
    if not prompts_dir.exists():
        print(f"⚠️ Prompts directory not found: {prompts_dir}")
        return

    # Get all numbered prompt files
    prompt_files = sorted(glob.glob(str(prompts_dir / "prompt_*.md")))

    if not prompt_files:
        print("⚠️ No prompt files found to dispatch.")
        return

    for p_file in prompt_files:
        path = Path(p_file)
        with open(path, encoding="utf-8") as f:
            plan_content = f.read()

        title = f"Document Tools - {path.name}"
        create_jules_session(api_key, plan_content, title)


if __name__ == "__main__":
    main()
