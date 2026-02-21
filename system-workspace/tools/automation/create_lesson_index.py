#!/usr/bin/env python3
import os
import sys
import json
import re
from pathlib import Path

# --- CONFIGURATION ---
# Path(__file__) is system-workspace/tools/automation/create_lesson_index.py
# .parent -> automation
# .parent.parent -> tools
# .parent.parent.parent -> system-workspace
# .parent.parent.parent.parent -> REPO ROOT
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent
RAW_DIR = PROJECT_ROOT / "system-workspace/text-data/raw"
INDEX_FILE = PROJECT_ROOT / "system-workspace/text-data/raw_to_lesson_index.json"
TOC_FILE = PROJECT_ROOT / "input/TOC.json"

# Add modules path to sys.path to import GeminiClient
MODULES_PATH = PROJECT_ROOT / "system-workspace/tools/automation/modules"
if str(MODULES_PATH) not in sys.path:
    sys.path.append(str(MODULES_PATH))

try:
    from gemini_client import GeminiClient
except ImportError:
    print(f"❌ Failed to import GeminiClient from {MODULES_PATH}. Ensure the file exists.")
    sys.exit(1)

def get_lesson_mapping():
    print("🔍 Mapping raw text to lessons...")
    
    # Sort files numerically
    def sort_key(p):
        try:
            match = re.search(r'raw_(\d+)', p.name)
            return int(match.group(1)) if match else 0
        except (IndexError, ValueError):
            return 0

    if not RAW_DIR.exists():
        print(f"❌ Raw directory not found: {RAW_DIR}")
        return None

    all_content = []
    files = sorted(list(RAW_DIR.glob("raw_*.txt")), key=sort_key)
    
    if not files:
        print(f"⚠️ No raw text files found in {RAW_DIR}")
        return None

    for f in files:
        try:
            lines = f.read_text(encoding='utf-8').splitlines()
            for i, line in enumerate(lines):
                # Strip potential preamble noise
                if i < 2 and ("I will read" in line or "confirming the existence" in line):
                    continue
                if not line.strip():
                    continue
                all_content.append(f"[{f.name}:{i+1}] {line}")
        except Exception as e:
            print(f"⚠️ Error reading file {f.name}: {e}")

    content_str = "\n".join(all_content)
    
    # We write the content to a temp file (optional, but good for debugging)
    temp_content_path = PROJECT_ROOT / "system-workspace/output/text-data/full_raw_indexed.txt"
    temp_content_path.parent.mkdir(parents=True, exist_ok=True)
    temp_content_path.write_text(content_str, encoding='utf-8')
    print(f"📄 Merged raw text to {temp_content_path}")
    
    toc_content = ""
    if TOC_FILE.exists():
        try:
            toc_data = json.loads(TOC_FILE.read_text(encoding='utf-8'))
            lines = []
            sorted_keys = sorted(toc_data.keys(), key=lambda x: int(x) if x.isdigit() else float('inf'))
            for k in sorted_keys:
                v = toc_data[k]
                title = v.get('title', 'Unknown')
                lines.append(f"{k} - {title}")
            toc_content = "\n=== TABLE OF CONTENTS (Reference) ===\n" + "\n".join(lines)
            print(f"✅ Loaded TOC with {len(lines)} entries.")
        except Exception as e:
            print(f"⚠️ Warning: Failed to parse TOC.json: {e}")
            toc_content = "\n=== TABLE OF CONTENTS (Reference) ===\n(Failed to load TOC)"

    prompt = f"""You are an expert Arabic book editor.
I have provided a file containing lines from transcribed Arabic grammar images.
Each line is prefixed with `[filename:line_number]`.

Your task is to identify the EXACT START and END line markers for every lesson/topic found in that text based on the provided Table of Contents (TOC).
CRITICAL RULES:
1. You MUST use the provided Table of Contents as the definitive source for lesson titles.
2. The keys in your JSON output MUST match the exact titles from the TOC. Do not invent, paraphrase, or skip any lesson titles.
3. Find the exact `[filename:line_number]` where each lesson begins (usually indicated by a title heading) and where it ends (just before the next lesson begins, or at the end of the text).
4. Output ONLY a valid JSON object. No explanations.

Format:
{{
  "Exact Lesson Title 1": {{
    "start": "raw_X.txt:lineN",
    "end": "raw_Y.txt:lineM"
  }}
}}

{toc_content}
"""

    try:
        # Initialize Gemini Client
        client = GeminiClient(project_root=PROJECT_ROOT)

        print("🚀 Sending request to Gemini...")

        # Use generate_content instead of subprocess
        # We pass the prompt as system instruction + user content (merged text)
        # Note: GeminiClient.generate_content expects (system_instruction, user_content)

        # Since the content is large, we pass it as user_content.
        resp = client.generate_content(
            system_instruction=prompt,
            user_content=content_str
        )
        
        if not resp:
            print("❌ Gemini returned empty response.")
            return None

        # Clean markdown code blocks if present
        resp = resp.replace("```json", "").replace("```", "").strip()

        # Find JSON block
        try:
            # First try parsing the whole response
            return json.loads(resp)
        except json.JSONDecodeError:
            # Fallback regex search
            match = re.search(r'\{.*\}', resp, re.DOTALL)
            if match:
                return json.loads(match.group(0))
            else:
                print(f"❌ No valid JSON found in response:\n{resp[:500]}...")
                return None
        
    except Exception as e:
        print(f"❌ Error during mapping: {e}")
        return None

def main():
    mapping = get_lesson_mapping()
    if mapping:
        INDEX_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(INDEX_FILE, "w", encoding="utf-8") as f:
            json.dump(mapping, f, ensure_ascii=False, indent=2)
        print(f"✅ Index created successfully at: {INDEX_FILE}")
        # Print a preview
        print(json.dumps(mapping, ensure_ascii=False, indent=2))
    else:
        print("❌ Failed to create index.")

if __name__ == "__main__":
    main()
