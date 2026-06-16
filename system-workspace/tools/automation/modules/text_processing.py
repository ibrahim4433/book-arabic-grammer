import sys
import json
import re
from pathlib import Path

# Ensure modules are importable
sys.path.append(str(Path(__file__).parent))

from gemini_client import GeminiClient

class TextProcessor:
    """
    Handles text processing tasks:
    1. Validating TOC structure.
    2. Merging raw OCR text.
    3. Mapping raw text to lessons using GeminiClient.
    """

    def __init__(self, project_root=None, api_key=None, use_headless=False):
        self.project_root = Path(project_root) if project_root else Path(__file__).parent.parent.parent.parent.parent
        self.raw_dir = self.project_root / "system-workspace/text-data/raw"
        self.toc_path = self.project_root / "input/TOC.json"
        self.index_file = self.project_root / "system-workspace/text-data/raw_to_lesson_index.json"
        
        self.client = GeminiClient(api_key, self.project_root, use_headless=use_headless)
        
        # Ensure directories exist
        self.raw_dir.mkdir(parents=True, exist_ok=True)
        self.index_file.parent.mkdir(parents=True, exist_ok=True)

    def validate_toc(self):
        """
        Validates the structure of TOC.json.
        Expected format: JSON object where keys are lesson numbers and values are metadata dicts.
        """
        if not self.toc_path.exists():
            print(f"❌ TOC file not found at {self.toc_path}")
            return False

        try:
            content = self.toc_path.read_text(encoding='utf-8').strip()
            data = json.loads(content)

            if not isinstance(data, dict):
                print("❌ TOC JSON is not a dictionary object.")
                return False

            if not data:
                print("❌ TOC file is empty.")
                return False

            # Check for required fields in at least one item
            first_key = next(iter(data))
            if not isinstance(data[first_key], dict) or 'title' not in data[first_key]:
                 print("❌ TOC items do not have 'title' field.")
                 return False

            print(f"✅ TOC Validated: {len(data)} topics found.")
            return True

        except json.JSONDecodeError as e:
            print(f"❌ TOC JSON Decode Error: {e}")
            return False

    def get_lesson_number(self, lesson_title):
        """
        Retrieves the lesson number for a given title from TOC.json.
        """
        if not self.toc_path.exists():
            return "00"
            
        try:
            content = self.toc_path.read_text(encoding='utf-8')
            data = json.loads(content)

            # Clean the input title by removing prefix (e.g., "9 - Title" -> "Title")
            clean_input_title = re.sub(r'^\d+\s*-\s*', '', lesson_title).strip()

            for number, metadata in data.items():
                title = metadata.get('title', '').strip()
                if title == clean_input_title:
                    return number.zfill(2) # Ensure 2 digits

            return "00"
        except Exception as e:
            print(f"⚠️ Error reading TOC for lesson number: {e}")
            return "00"

    def merge_raw_text(self):
        """
        Merges all raw_*.txt files into a single context file with line numbers.
        Returns the path to the merged file.
        """
        # Sort files numerically
        def sort_key(p):
            try:
                match = re.search(r'raw_(\d+)', p.name)
                return int(match.group(1)) if match else 0
            except ValueError:
                return 0

        files = sorted(list(self.raw_dir.glob("raw_*.txt")), key=sort_key)
        
        if not files:
            print("⚠️ No raw text files found to merge.")
            return None

        all_content = []
        for f in files:
            try:
                lines = f.read_text(encoding='utf-8').splitlines()
                for i, line in enumerate(lines):
                    if len(line.strip()) < 2: continue
                    all_content.append(f"[{f.name}:{i+1}] {line}")
            except Exception as e:
                print(f"⚠️ Error reading {f.name}: {e}")

        merged_content = "\n".join(all_content)
        output_path = self.project_root / "system-workspace/text-data/full_raw_indexed.txt"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(merged_content, encoding='utf-8')
        
        print(f"📄 Merged {len(files)} files into {output_path}")
        return output_path

    def generate_toc(self, merged_path):
        """
        Uses Gemini to generate the TOC.json from the merged raw text.
        """
        print("🔍 Generating TOC from raw text via Gemini...")
        # Load settings
        settings_file = self.project_root / "system-workspace" / "settings.json"
        author = "أ. الياس خفيف"
        author_number = "994066850 963+"
        if settings_file.exists():
            try:
                with open(settings_file, "r", encoding="utf-8") as f:
                    settings = json.load(f)
                    author = settings.get("author", author)
                    author_number = settings.get("author_number", author_number)
            except Exception as e:
                print(f"⚠️ Could not load settings: {e}")

        system_instruction = f"""You are an expert Arabic book editor.
I have a file containing transcribed Arabic grammar text.
Your task is to extract the Table of Contents (TOC) from this text and output it as a JSON object.
CRITICAL RULES:
1. Identify all the main lessons or topics.
2. The output MUST be a JSON object where the keys are lesson numbers (e.g., "01", "02").
3. Each value must be an object with the exact following fields: 'title', 'level', 'Unit', 'author', 'author_number'. You must infer or supply these details logically, or leave them blank if truly unknown.
4. Output ONLY a valid JSON object. No explanations.

=== OUTPUT FORMAT ===
{{
  "01": {{
    "title": "Exact Arabic Title 1",
    "level": "فوائد",
    "Unit": "المستوى الفني",
    "author": "{author}",
    "author_number": "{author_number}"
  }}
}}
"""
        user_content = merged_path.read_text(encoding='utf-8')

        resp_text = self.client.generate_content(
            system_instruction=system_instruction,
            user_content=user_content
        )
        
        if not resp_text:
            print("❌ Failed to generate TOC.")
            return False
            
        try:
            cleaned_json = resp_text.replace("```json", "").replace("```", "").strip()
            match = re.search(r'\{.*\}', cleaned_json, re.DOTALL)
            if match:
                cleaned_json = match.group(0)

            toc_data = json.loads(cleaned_json)
            
            # Save the TOC
            self.toc_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.toc_path, "w", encoding="utf-8") as f:
                json.dump(toc_data, f, ensure_ascii=False, indent=2)
            
            print(f"✅ TOC created at {self.toc_path}")
            return True
            
        except json.JSONDecodeError:
            print(f"❌ Failed to parse JSON response for TOC: {resp_text[:100]}...")
            return False

    def generate_lesson_index(self):
        """
        Uses Gemini to map the merged raw text to the TOC.
        """
        if not self.validate_toc():
            return None

        merged_path = self.merge_raw_text()
        if not merged_path:
            return None

        print("🔍 Mapping raw text to lessons via Gemini...")
        
        try:
            toc_data = json.loads(self.toc_path.read_text(encoding='utf-8'))
            # Simplify TOC for the prompt: "Number - Title" list
            toc_lines = []
            sorted_keys = sorted(toc_data.keys(), key=lambda x: int(x) if x.isdigit() else float('inf'))
            for num in sorted_keys:
                meta = toc_data[num]
                toc_lines.append(f"{num} - {meta.get('title', 'Unknown')}")
            toc_content = "\n".join(toc_lines)
        except Exception as e:
             print(f"❌ Failed to process TOC.json: {e}")
             return None
        
        # System Prompt
        system_instruction = f"""You are an expert Arabic book editor.
I have a file containing lines from transcribed Arabic grammar images (format: [filename:line] text).

Your task is to identify the EXACT START and END line markers for every lesson/topic found in that text based on the provided Table of Contents (TOC).
CRITICAL RULES:
1. You MUST use the provided Table of Contents as the definitive source for lesson titles.
2. The keys in your JSON output MUST match the exact titles from the TOC. Do not invent, paraphrase, or skip any lesson titles.
3. Find the exact `[filename:line]` where each lesson begins (usually indicated by a title heading) and where it ends (just before the next lesson begins, or at the end of the text).
4. Output ONLY a valid JSON object. No explanations.

=== TABLE OF CONTENTS ===
{toc_content}

=== OUTPUT FORMAT ===
{{
  "Exact Lesson Title 1": {{
    "start": "raw_1.txt:5",
    "end": "raw_2.txt:10"
  }}
}}
"""
        
        # User Content (The merged raw text)
        user_content = merged_path.read_text(encoding='utf-8')

        # Call Gemini (Smart Client handles API Key vs CLI)
        # Using generate_content instead of forced headless mode
        resp_text = self.client.generate_content(
            system_instruction=system_instruction,
            user_content=user_content
        )
        
        if not resp_text:
            print("❌ Failed to generate index mapping.")
            return None
            
        try:
            # Clean potential markdown block ```json ... ```
            cleaned_json = resp_text.replace("```json", "").replace("```", "").strip()

            # Additional cleanup if needed (e.g. remove preamble text before {)
            match = re.search(r'\{.*\}', cleaned_json, re.DOTALL)
            if match:
                cleaned_json = match.group(0)

            mapping = json.loads(cleaned_json)
            
            with open(self.index_file, "w", encoding="utf-8") as f:
                json.dump(mapping, f, ensure_ascii=False, indent=2)
            
            print(f"✅ Index created at {self.index_file}")
            return mapping
            
        except json.JSONDecodeError:
            print(f"❌ Failed to parse JSON response: {resp_text[:100]}...")
            return None

if __name__ == "__main__":
    tp = TextProcessor()
    tp.validate_toc()
