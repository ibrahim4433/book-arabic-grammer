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
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") # Required for Vision
JULES_API_URL = "https://jules.googleapis.com/v1alpha" # Placeholder for the Jules/Code Assist API
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent"
PROJECT_ROOT = Path(__file__).parent.parent.parent

class VisionGEM:
    """
    Handles Image-to-Text extraction using Gemini 1.5 Pro via REST API.
    """
    def __init__(self, api_key):
        self.api_key = api_key
        if not self.api_key:
            print("⚠️ GEMINI_API_KEY is missing! Vision features will fail.")

    def extract_text(self, image_paths):
        """
        Sends images to Gemini and requests a raw transcription.
        """
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY is required for image processing.")
        
        print(f"👁️ VisionGEM: Processing {len(image_paths)} images...")

        # 1. Prepare Content Parts
        contents_parts = []
        
        # Add the Prompt
        prompt_text = (
            "You are an expert Arabic OCR engine. "
            "Transcribe the Arabic text from these educational images EXACTLY as it appears. "
            "Preserve all diacritics (Harakat) strictly. "
            "Do not summarize. Do not explain. Just output the raw Arabic text. "
            "If there are headers, use markdown headers (#). "
            "If there are tables, represent them as markdown tables. "
            "Ignore page numbers or irrelevant footer text."
        )
        contents_parts.append({"text": prompt_text})

        # Add Images (Base64 encoding)
        import base64
        for img_path in image_paths:
            try:
                with open(img_path, "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
                
                # Determine mime type
                mime_type = "image/jpeg"
                if img_path.suffix.lower() in ['.png']:
                    mime_type = "image/png"
                elif img_path.suffix.lower() in ['.webp']:
                    mime_type = "image/webp"

                contents_parts.append({
                    "inline_data": {
                        "mime_type": mime_type,
                        "data": encoded_string
                    }
                })
            except Exception as e:
                print(f"❌ Error reading image {img_path}: {e}")

        # 2. Construct Payload
        payload = {
            "contents": [{
                "parts": contents_parts
            }],
            "generationConfig": {
                "temperature": 0.0, # Deterministic for OCR
                "maxOutputTokens": 8192
            }
        }

        # 3. Call API
        try:
            url = f"{GEMINI_API_URL}?key={self.api_key}"
            response = requests.post(url, headers={"Content-Type": "application/json"}, json=payload)
            response.raise_for_status()
            
            result = response.json()
            # Extract text from response
            try:
                extracted_text = result['candidates'][0]['content']['parts'][0]['text']
                return extracted_text
            except (KeyError, IndexError):
                print(f"❌ Unexpected API Response: {result}")
                return ""

        except requests.exceptions.RequestException as e:
            print(f"❌ VisionGEM API Failed: {e}")
            if e.response:
                print(f"   Response: {e.response.text}")
            sys.exit(1)

class ArchitectGEM:
    """
    Official Headless Wrapper for Gemini CLI.
    Uses cached credentials from 'gemini login' via the --non-interactive flag.
    Reference: https://geminicli.com/docs/cli/headless/
    """

    def __init__(self, model="gemini-1.5-pro"):
        self.model = model

    def generate_plan(self, system_prompt_path, user_content_str, project_state_str):
        """
        Executes the Architect Logic using the official 'Piping' method.
        Equivalent to: cat prompt.md content.txt state.json | gemini --non-interactive
        """
        print(f"🤖 Architect is thinking (Model: {self.model})...")

        # 1. Prepare the Input Stream (Context + Prompt)
        try:
            with open(system_prompt_path, 'r', encoding='utf-8') as f:
                sys_prompt = f.read()
        except FileNotFoundError as e:
            print(f"❌ Error reading input files: {e}")
            sys.exit(1)

        full_stream_input = (
            f"{sys_prompt}\n\n"
            f"=== PROJECT STATE ===\n[PROJECT_STATE]\n{project_state_str}\n\n"
            f"=== LESSON CONTENT ===\n{user_content_str}"
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
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--lesson", help="Path to the raw lesson text file")
    group.add_argument("--image-dir", help="Path to directory containing lesson images")
    
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

    # 2. Get Content (Text or Images)
    user_content = ""
    
    if args.lesson:
        current_lesson = Path(args.lesson)
        if not current_lesson.exists():
            print(f"❌ Lesson file not found: {current_lesson}")
            sys.exit(1)
        with open(current_lesson, 'r', encoding='utf-8') as f:
            user_content = f.read()
            
    elif args.image_dir:
        img_dir = Path(args.image_dir)
        if not img_dir.exists():
            print(f"❌ Image directory not found: {img_dir}")
            sys.exit(1)
            
        # Find images
        images = sorted(list(img_dir.glob("*.jpg")) + list(img_dir.glob("*.png")) + list(img_dir.glob("*.webp")))
        if not images:
            print(f"❌ No images found in {img_dir}")
            sys.exit(1)
            
        vision = VisionGEM(api_key=GEMINI_API_KEY)
        user_content = vision.extract_text(images)
        
        # Save extraction for debugging
        output_dir = PROJECT_ROOT / "output"
        output_dir.mkdir(exist_ok=True)
        with open(output_dir / "extracted_vision.txt", "w", encoding='utf-8') as f:
            f.write(user_content)
        print(f"📄 Text extracted and saved to {output_dir / 'extracted_vision.txt'}")

    # 3. Define Architect Prompt
    architect_prompt = PROJECT_ROOT / "Architect_GEM_PROMPT.md"

    # 4. Run Architect (Headless CLI)
    architect = ArchitectGEM(model=args.model)
    print("⏳ Running Architect...")
    # Note: We pass the STRING content now, not path
    raw_response = architect.generate_plan(architect_prompt, user_content, project_state_str)

    # Extract the actual plan content (remove markdown wrapper)
    plan = extract_plan_block(raw_response)

    # 5. Save Plan (Optional Debugging)
    output_dir = PROJECT_ROOT / "output"
    output_dir.mkdir(exist_ok=True)
    plan_file = output_dir / "latest_plan.md"

    with open(plan_file, "w", encoding='utf-8') as f:
        f.write(plan)
    print(f"📋 Plan generated and saved to {plan_file}")

    # 6. Execute Jules
    jules = JulesClient(api_key=JULES_API_KEY)
    jules.create_session(plan, repo_name=args.repo)

if __name__ == "__main__":
    main()
