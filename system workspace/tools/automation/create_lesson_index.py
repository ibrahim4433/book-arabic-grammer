#!/usr/bin/env python3
import os
import subprocess
import json
import re
from pathlib import Path

# --- CONFIGURATION ---
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent
RAW_DIR = PROJECT_ROOT / "system workspace/text-data/raw"
INDEX_FILE = PROJECT_ROOT / "system workspace/text-data/raw_to_lesson_index.json"

def get_lesson_mapping():
    print("🔍 Mapping raw text to lessons...")
    
    # Sort files numerically
    def sort_key(p):
        try:
            return int(p.stem.split('_')[1])
        except (IndexError, ValueError):
            return 0

    if not RAW_DIR.exists():
        print(f"❌ Raw directory not found: {RAW_DIR}")
        return None

    all_content = []
    files = sorted(list(RAW_DIR.glob("raw_*.txt")), key=sort_key)
    
    for f in files:
        lines = f.read_text(encoding='utf-8').splitlines()
        for i, line in enumerate(lines):
            # Strip potential preamble noise
            if i < 2 and ("I will read" in line or "confirming the existence" in line):
                continue
            all_content.append(f"{f.name}:{i+1}: {line}")

    content_str = "\n".join(all_content)
    
    # We write the content to a temp file to avoid shell argument length limits
    temp_content_path = PROJECT_ROOT / "system workspace/text-data/full_raw_indexed.txt"
    temp_content_path.parent.mkdir(parents=True, exist_ok=True)
    temp_content_path.write_text(content_str, encoding='utf-8')
    
    toc_path = PROJECT_ROOT / "system workspace/TOC.json"
    toc_content_str = ""

    if toc_path.exists():
        try:
            toc_data = json.loads(toc_path.read_text(encoding='utf-8'))
            toc_lines = []
            # Sort by key assuming numeric keys "1", "2", etc.
            sorted_keys = sorted(toc_data.keys(), key=lambda x: int(x) if x.isdigit() else 999)

            for k in sorted_keys:
                item = toc_data[k]
                title = item.get("title", "Unknown Title")
                level = item.get("level", "")
                unit = item.get("Unit", "")
                toc_lines.append(f"{k} - {title} (Level: {level}, Unit: {unit})")

            toc_content_str = "\n\n=== TABLE OF CONTENTS (Reference) ===\n" + "\n".join(toc_lines)
            print(f"✅ Loaded TOC with {len(toc_lines)} entries.")
        except Exception as e:
            print(f"⚠️ Error reading TOC.json: {e}")
    else:
        print(f"⚠️ TOC file not found at {toc_path}")

    prompt = f"""You are an expert Arabic book editor. I have provided a file at {temp_content_path} containing lines from transcribed Arabic grammar images. 
Your task is to identify the START and END lines for every lesson/topic found in that text.
Use the provided Table of Contents as a reference for the correct lesson names.
Output ONLY a JSON object mapping Lesson Title to its address range.

Format:
{{
  "Lesson Title": {{"start": "raw_x.txt:lineN", "end": "raw_y.txt:lineM"}}
}}

{toc_content_str}
"""

    try:
        # Pass prompt and use @ to read the large content file in gemini-cli
        result = subprocess.run(
            ["gemini", "--prompt", prompt + f"\n\n@ {temp_content_path}"],
            capture_output=True,
            text=True,
            check=True
        )
        
        resp = result.stdout
        # Find JSON block
        match = re.search(r'\{.*\}', resp, re.DOTALL)
        if match:
            return json.loads(match.group(0))
        else:
            print(f"❌ No JSON found in response: {resp}")
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
        print(f"✅ Index created at {INDEX_FILE}")
    else:
        print("❌ Failed to create index.")

if __name__ == "__main__":
    main()
