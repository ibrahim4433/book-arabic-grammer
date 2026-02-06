#!/usr/bin/env python3
import os
import sys
import json
import base64
import requests
import re
import time
from pathlib import Path

# --- CONFIGURATION ---
PROJECT_ROOT = Path(__file__).parent.parent
SECRETS_DIR = PROJECT_ROOT / "secrets"
INPUT_DIR = PROJECT_ROOT / "input"
OUTPUT_DIR = PROJECT_ROOT / "output"

GEMINI_MODEL = "gemini-1.5-pro"
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"
JULES_API_URL = "https://jules.googleapis.com/v1alpha/sessions"
JULES_SOURCE = "sources/github/ibrahim4433/book-arabic-grammer"

# --- HELPERS ---

def load_key(filename):
    try:
        with open(SECRETS_DIR / filename, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"❌ Secret file not found: {filename}")
        sys.exit(1)

def load_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

class GeminiClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {"Content-Type": "application/json"}

    def generate(self, prompt_parts, system_instruction=None):
        url = f"{GEMINI_API_URL}?key={self.api_key}"
        contents = [{"parts": prompt_parts}]
        payload = {
            "contents": contents,
            "generationConfig": {
                "temperature": 0.0,
                "maxOutputTokens": 8192
            }
        }
        if system_instruction:
            payload["systemInstruction"] = {"parts": [{"text": system_instruction}]}

        try:
            response = requests.post(url, headers=self.headers, json=payload)
            response.raise_for_status()
            data = response.json()
            return data['candidates'][0]['content']['parts'][0]['text']
        except Exception as e:
            print(f"❌ Gemini API Call Failed: {e}")
            if 'response' in locals(): print(f"Response: {response.text}")
            return None

class JulesClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            "X-Goog-Api-Key": api_key,
            "Content-Type": "application/json"
        }

    def create_session(self, prompt, title):
        payload = {
            "prompt": prompt,
            "sourceContext": {
                "source": JULES_SOURCE,
                "githubRepoContext": {
                    "startingBranch": "main"
                }
            },
            "automationMode": "AUTO_CREATE_PR",
            "title": title
        }
        try:
            print(f"🚀 Dispatching session to Jules: {title}...")
            response = requests.post(JULES_API_URL, headers=self.headers, json=payload)
            response.raise_for_status()
            data = response.json()
            session_name = data.get("name")
            print(f"✅ Jules Session Created: {session_name}")
            return session_name
        except Exception as e:
            print(f"❌ Jules API Call Failed: {e}")
            if 'response' in locals(): print(f"Response: {response.text}")
            return None

# --- WORKFLOW STEPS ---

def step_1_vision(client, image_path):
    print(f"👁️ [Vision] Extracting text from {image_path.name}...")
    with open(image_path, "rb") as img_file:
        img_data = base64.b64encode(img_file.read()).decode("utf-8")
    
    mime_type = "image/jpeg"
    if image_path.suffix.lower() == ".png": mime_type = "image/png"
    
    prompt_text = (
        "You are an expert Arabic OCR engine. Transcribe the Arabic text from this image EXACTLY as it appears. "
        "Preserve all diacritics (Harakat) strictly. Do not summarize. Do not explain. Just output the raw Arabic text. "
        "Ignore page numbers or irrelevant footer text."
    )
    parts = [
        {"text": prompt_text},
        {"inline_data": {"mime_type": mime_type, "data": img_data}}
    ]
    return client.generate(parts)

def step_2_plan(client, raw_text, current_state):
    print(f"🧠 [Architect] Generating Plan...")
    sys_prompt = load_file(PROJECT_ROOT / "Architect_GEM_PROMPT.md")
    rules = load_file(PROJECT_ROOT / "BOOK_RULES.md")
    
    user_prompt = (
        f"=== PROJECT STATE ===\n{current_state}\n\n"
        f"=== LESSON CONTENT (Raw Arabic) ===\n{raw_text}\n\n"
        f"=== INSTRUCTION ===\nGenerate the Architect Plan for this content."
    )
    full_sys_prompt = sys_prompt + "\n\n=== BOOK RULES ===\n" + rules
    return client.generate([{"text": user_prompt}], system_instruction=full_sys_prompt)

# --- MAIN ---

def main():
    gemini_key_path = SECRETS_DIR / "Gemini_API.txt"
    jules_key_path = SECRETS_DIR / "Jules_API.txt"
    
    if gemini_key_path.exists():
        gemini_key = load_key("Gemini_API.txt")
    else:
        print("⚠️ Gemini_API.txt not found, using Jules_API.txt for Gemini calls.")
        gemini_key = load_key("Jules_API.txt")
        
    jules_key = load_key("Jules_API.txt")
    
    gemini = GeminiClient(gemini_key)
    jules = JulesClient(jules_key)
    
    # Load state
    state_path = PROJECT_ROOT / "beta-utilities/project_state.json"
    state_str = load_file(state_path) if state_path.exists() else "{}"

    # Process first two images as a trial
    images = [INPUT_DIR / "1.jpg", INPUT_DIR / "2.jpg"]
    OUTPUT_DIR.mkdir(exist_ok=True)

    for img in images:
        if not img.exists():
            print(f"⚠️ Skipping missing image: {img.name}")
            continue
            
        print(f"\n--- Processing {img.name} ---")
        
        # 1. Vision (OCR)
        raw_text = step_1_vision(gemini, img)
        if not raw_text: continue
        (OUTPUT_DIR / f"raw_{img.stem}.txt").write_text(raw_text, encoding='utf-8')
        
        # 2. Architect (Planning)
        plan = step_2_plan(gemini, raw_text, state_str)
        if not plan: continue
        (OUTPUT_DIR / f"plan_{img.stem}.md").write_text(plan, encoding='utf-8')
        
        # 3. Jules (Coding)
        jules_prompt = f"Execute this Architect Plan strictly:\n\n{plan}"
        title = f"Implementation for {img.name}"
        session_id = jules.create_session(jules_prompt, title)
        
        if session_id:
            print(f"🔗 View session at: https://jules.google/sessions/{session_id.split('/')[-1]}")

if __name__ == "__main__":
    main()
