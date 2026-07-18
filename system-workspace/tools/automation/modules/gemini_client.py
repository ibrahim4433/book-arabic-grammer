import base64
import os
import subprocess
from pathlib import Path

import requests


class GeminiClient:
    """
    A generic client for the Google Gemini API.
    Handles authentication and content generation (Text & Vision).
    Supports both REST API (with Key) and Headless CLI (No Key).
    """

    # Class-level variables to share state across all instances in the session
    models_chain = [
        "gemini-3-pro-preview",
        "gemini-2.5-pro",
        "gemini-3-flash-preview",
        "gemini-2.5-flash",
        "gemini-2.5-flash-lite",
    ]
    current_model_index = 0

    def __init__(self, api_key=None, project_root=None, use_headless=False):
        self.project_root = (
            Path(project_root)
            if project_root
            else Path(__file__).parent.parent.parent.parent.parent
        )
        self.api_key = api_key or self._load_api_key()
        self.use_headless = use_headless
        self.base_url = (
            "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent"
        )

    def _load_api_key(self):
        """Loads API key from environment, Gemini_API.txt, or Jules_API.txt."""
        key = os.getenv("GEMINI_API_KEY")
        if key:
            return key

        # Try Gemini specific key
        gemini_path = self.project_root / "secrets/Gemini_API.txt"
        if gemini_path.exists():
            return gemini_path.read_text().strip()

        # Fallback to Jules key
        jules_path = self.project_root / "secrets/Jules_API.txt"
        if jules_path.exists():
            return jules_path.read_text().strip()

        return None

    def generate_content(self, system_instruction, user_content, images=None, response_schema=None):
        """
        Generates content using Gemini REST API.
        """
        if self.use_headless or not self.api_key:
            print("⚠️ API Key missing or Headless mode requested. Switching to Headless CLI...")
            return self.generate_content_headless(
                system_instruction + "\n\n" + user_content, images=images
            )

        parts = []
        full_prompt = (
            f"{system_instruction}\n\n{user_content}" if system_instruction else user_content
        )
        parts.append({"text": full_prompt})

        # Process Images
        if images:
            for img_path in images:
                img_path = Path(img_path)
                if not img_path.exists():
                    print(f"⚠️ Image not found: {img_path}")
                    continue

                try:
                    with open(img_path, "rb") as image_file:
                        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

                    mime_type = "image/jpeg"
                    if img_path.suffix.lower() == ".png":
                        mime_type = "image/png"
                    elif img_path.suffix.lower() == ".webp":
                        mime_type = "image/webp"

                    parts.append({"inline_data": {"mime_type": mime_type, "data": encoded_string}})
                except Exception as e:
                    print(f"❌ Error reading image {img_path}: {e}")

        payload = {"contents": [{"parts": parts}], "generationConfig": {"temperature": 0.0}}

        if response_schema:
            payload["generationConfig"]["response_mime_type"] = "application/json"

        url = f"{self.base_url}?key={self.api_key}"

        try:
            resp = requests.post(
                url, headers={"Content-Type": "application/json"}, json=payload, timeout=120
            )
            resp.raise_for_status()
            result = resp.json()
            return result["candidates"][0]["content"]["parts"][0]["text"]

        except requests.exceptions.RequestException as e:
            status_code = getattr(e.response, "status_code", None)
            print(f"❌ Gemini API Failed (Status: {status_code}): {e}")

            # Fallback for authentication or quota errors
            if status_code in [401, 403, 429] or not self.api_key:
                print("🔄 Falling back to Headless CLI...")
                return self.generate_content_headless(full_prompt, images)
            return ""
        except (KeyError, IndexError):
            print(f"❌ Unexpected API Response: {result}")
            return ""

    def generate_content_headless(self, full_prompt, images=None):
        """
        Generates content using the `gemini` CLI tool (Headless) with a multi-model fallback chain.
        Starts from the last successful model in the chain (shared across all instances).
        """
        # If images are provided, append them to the prompt to guide the CLI
        if images:
            image_refs = "\n".join([f"Processing Image: {Path(img).absolute()}" for img in images])
            full_prompt = f"{full_prompt}\n\n[System Note: The user has attached the following images for processing. If your environment allows, read them.]\n{image_refs}"

        # Start from the current successful model index
        for i in range(GeminiClient.current_model_index, len(GeminiClient.models_chain)):
            model = GeminiClient.models_chain[i]
            result_text = self._run_cli(full_prompt, model)

            if result_text:
                if i != GeminiClient.current_model_index:
                    print(f"🔄 Switched to model '{model}' for this session.")
                GeminiClient.current_model_index = i
                return result_text

            print(f"⚠️ Model '{model}' failed or quota exhausted. Trying next in chain...")

        print("❌ All models in the fallback chain failed.")
        return ""

    def _run_cli(self, full_prompt, model):
        """Helper to run the CLI command."""
        try:
            print(f"⏳ Running Gemini CLI (Model: {model})...")
            # The CLI requires -p/--prompt to trigger non-interactive mode.
            cmd = [
                "gemini",
                "--prompt",
                "Process input from stdin.",
                "--model",
                model,
                "--output-format",
                "text",
            ]

            result = subprocess.run(
                cmd,
                input=full_prompt,
                capture_output=True,
                text=True,
                encoding="utf-8",
                check=False,
                timeout=300,  # 5 minutes timeout to prevent indefinite hangs
            )

            if result.returncode != 0:
                print(f"❌ Gemini CLI Error ({model}): {result.stderr}")
                return ""

            return result.stdout.strip()

        except subprocess.TimeoutExpired:
            print(f"❌ Gemini CLI Timeout ({model}) after 300s.")
            return ""
        except FileNotFoundError:
            print("❌ Error: 'gemini' command not found. Ensure it is installed and in PATH.")
            return ""
        except Exception as e:
            print(f"❌ Execution Error: {e}")
            return ""
