#!/usr/bin/env python3
import subprocess
import requests
import json
import os
import sys
import re
import argparse
from pathlib import Path

# --- CONFIGURATION ---
JULES_API_KEY = os.getenv("JULES_API_KEY")
JULES_API_URL = "https://jules.googleapis.com/v1alpha" # Placeholder for the Jules/Code Assist API
PROJECT_ROOT = Path(__file__).parent.parent

class ArchitectGEM:
    """
    Official Headless Wrapper for Gemini CLI.
    Uses cached credentials from 'gemini login' via the --non-interactive flag.
    Reference: https://geminicli.com/docs/cli/headless/
    """

    def __init__(self, model="gemini-1.5-pro"):
        self.model = model

    def generate_plan(self, system_prompt_path, user_content_path, project_state_str):
        """
        Executes the Architect Logic using the official 'Piping' method.
        Equivalent to: cat prompt.md content.txt state.json | gemini --non-interactive
        """
        print(f"🤖 Architect is thinking (Model: {self.model})...")

        # 1. Prepare the Input Stream (Context + Prompt)
        try:
            with open(system_prompt_path, 'r', encoding='utf-8') as f:
                sys_prompt = f.read()
            with open(user_content_path, 'r', encoding='utf-8') as f:
                usr_content = f.read()
        except FileNotFoundError as e:
            print(f"❌ Error reading input files: {e}")
            sys.exit(1)

        full_stream_input = (
            f"{sys_prompt}\n\n"
            f"=== PROJECT STATE ===\n[PROJECT_STATE]\n{project_state_str}\n\n"
            f"=== LESSON CONTENT ===\n{usr_content}"
        )

        # 2. Call Gemini CLI with Official Headless Flags
        # --non-interactive: Disables UI/Browser prompts
        # --output-format text: We want the raw markdown/text response
        command = [
            "gemini",
            "--non-interactive",
            "--model", self.model,
            "--output-format", "text"
        ]

        try:
            # We use subprocess ONLY to bridge the pipe, strictly following the docs' piping logic
            result = subprocess.run(
                command,
                input=full_stream_input,
                text=True,
                capture_output=True,
                encoding='utf-8',
                check=False
            )

            if result.returncode != 0:
                print(f"❌ Architect Error (CLI): {result.stderr}")
                # For development/testing without the CLI installed, we might want to fail gracefully or mock
                # But strict adherence requires raising.
                raise Exception("Gemini CLI failed to generate plan.")

            return result.stdout.strip()

        except FileNotFoundError:
            print("❌ Error: 'gemini' command not found. Did you run 'npm install -g @google/gemini-cli'?")
            # In a real environment, we exit.
            sys.exit(1)

class JulesClient:
    """
    Client for the Jules (Code Assist) API.
    """
    def __init__(self, api_key):
        if not api_key:
            print("⚠️ JULES_API_KEY is missing! Jules submission will fail.")
            # We don't raise immediately to allow Architect testing without Jules key
        self.headers = {
            "Content-Type": "application/json",
            "X-Goog-Api-Key": api_key
        }
        self.api_key = api_key

    def create_session(self, plan_content, repo_name="ibrahim4433/book-arabic-grammer"):
        """
        Starts a Jules session with the Architect's plan.
        """
        if not self.api_key:
             print("❌ Skipping Jules submission (No API Key).")
             return None

        print("🚀 Dispatching Plan to Jules...")

        payload = {
            "prompt": f"Execute this Architect Plan strictly:\n\n{plan_content}",
            "sourceContext": {
                "githubRepo": {"name": repo_name}
            },
            "config": {
                "tools": ["EDIT_CODE", "RUN_COMMAND"] # Enable Jules to run verify_layout.py
            }
        }

        # NOTE: Verify the specific endpoint for your Jules/Code Assist preview
        try:
            resp = requests.post(f"{JULES_API_URL}/sessions", headers=self.headers, json=payload)
            resp.raise_for_status()

            session_data = resp.json()
            session_id = session_data.get('name', 'Unknown-Session')
            print(f"✅ Jules Session Started: {session_id}")
            return session_id

        except requests.exceptions.RequestException as e:
            print(f"❌ Jules Connection Failed: {e}")
            if e.response:
                print(f"   Response: {e.response.text}")
            sys.exit(1)

def extract_plan_block(full_response):
    """
    Extracts the content inside the quadruple backtick block (text).
    Looks for ```text ... ``` or ````text ... ````
    """
    # Try quadruple backticks first as per prompt instructions
    pattern = r'````text\s*(.*?)\s*````'
    match = re.search(pattern, full_response, re.DOTALL)
    if match:
        return match.group(1)

    # Fallback to triple backticks
    pattern_triple = r'```text\s*(.*?)\s*```'
    match_triple = re.search(pattern_triple, full_response, re.DOTALL)
    if match_triple:
        return match_triple.group(1)

    return full_response # Return full response if no block found (fallback)

# --- MAIN WORKFLOW ---
def main():
    parser = argparse.ArgumentParser(description="Architect-Jules Orchestrator")
    parser.add_argument("--lesson", required=True, help="Path to the raw lesson text file")
    parser.add_argument("--model", default="gemini-1.5-pro", help="Gemini model to use")
    parser.add_argument("--repo", default="ibrahim4433/book-arabic-grammer", help="GitHub repo name for Jules")
    args = parser.parse_args()

    # 1. Detect State
    state_file = PROJECT_ROOT / "tools/project_state.json"
    project_state_str = "{}"
    if state_file.exists():
        try:
            with open(state_file, 'r', encoding='utf-8') as f:
                project_state_str = f.read()
        except Exception as e:
             print(f"⚠️ Could not read project state: {e}")

    # 2. Define Inputs
    architect_prompt = PROJECT_ROOT / "Architect_GEM_PROMPT.md"
    current_lesson = Path(args.lesson)

    if not current_lesson.exists():
        print(f"❌ Lesson file not found: {current_lesson}")
        sys.exit(1)

    # 3. Run Architect (Headless CLI)
    architect = ArchitectGEM(model=args.model)
    print("⏳ Running Architect...")
    raw_response = architect.generate_plan(architect_prompt, current_lesson, project_state_str)

    # Extract the actual plan content (remove markdown wrapper)
    plan = extract_plan_block(raw_response)

    # 4. Save Plan (Optional Debugging)
    output_dir = PROJECT_ROOT / "output"
    output_dir.mkdir(exist_ok=True)
    plan_file = output_dir / "latest_plan.md"

    with open(plan_file, "w", encoding='utf-8') as f:
        f.write(plan)
    print(f"📋 Plan generated and saved to {plan_file}")

    # 5. Execute Jules
    jules = JulesClient(api_key=JULES_API_KEY)
    jules.create_session(plan, repo_name=args.repo)

if __name__ == "__main__":
    main()
