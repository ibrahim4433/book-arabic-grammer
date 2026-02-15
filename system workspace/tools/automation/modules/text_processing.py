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

    def __init__(self, project_root=None, api_key=None):
        self.project_root = Path(project_root) if project_root else Path(__file__).parent.parent.parent.parent.parent
        self.raw_dir = self.project_root / "system workspace/text-data/raw"
        self.toc_path = self.project_root / "input/TOC.txt"
        self.index_file = self.project_root / "system workspace/text-data/raw_to_lesson_index.json"
        
        self.client = GeminiClient(api_key, self.project_root)
        
        # Ensure directories exist
        self.raw_dir.mkdir(parents=True, exist_ok=True)
        self.index_file.parent.mkdir(parents=True, exist_ok=True)

    def validate_toc(self):
        """
        Validates the structure of TOC.txt.
        Expected format: One lesson title per line.
        """
        if not self.toc_path.exists():
            print(f"❌ TOC file not found at {self.toc_path}")
            return False

        content = self.toc_path.read_text(encoding='utf-8').strip()
        lines = content.splitlines()
        
        if not lines:
            print("❌ TOC file is empty.")
            return False

        print(f"✅ TOC Validated: {len(lines)} topics found.")
        return True

    def get_lesson_number(self, lesson_title):
        """
        Retrieves the lesson number for a given title from TOC.txt.
        Assumes TOC format: "09 - Lesson Title"
        """
        if not self.toc_path.exists():
            return "00"
            
        content = self.toc_path.read_text(encoding='utf-8')
        for line in content.splitlines():
            # Regex to match "09 - Title" or "9 - Title"
            match = re.match(r"^(\d+)\s*-\s*(.*)", line.strip())
            if match:
                number = match.group(1).zfill(2) # Ensure 2 digits
                title = match.group(2).strip()
                if title == lesson_title.strip():
                    return number
        return "00"

    def merge_raw_text(self):
        """
        Merges all raw_*.txt files into a single context file with line numbers.
        Returns the path to the merged file.
        """
        # Sort files numerically
        def sort_key(p):
            try:
                match = re.search(r'\d+', p.stem)
                return int(match.group()) if match else 0
            except ValueError:
                return 0

        files = sorted(list(self.raw_dir.glob("raw_*.txt")), key=sort_key)
        
        if not files:
            print("⚠️ No raw text files found to merge.")
            return None

        all_content = []
        for f in files:
            lines = f.read_text(encoding='utf-8').splitlines()
            for i, line in enumerate(lines):
                if len(line.strip()) < 2: continue
                all_content.append(f"[{f.name}:{i+1}] {line}")

        merged_content = "\n".join(all_content)
        output_path = self.project_root / "system workspace/text-data/full_raw_indexed.txt"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(merged_content, encoding='utf-8')
        
        print(f"📄 Merged {len(files)} files into {output_path}")
        return output_path

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
        
        toc_content = self.toc_path.read_text(encoding='utf-8')
        
        # System Prompt
        system_instruction = f"""You are an expert Arabic book editor.
I have a file containing lines from transcribed Arabic grammar images (format: [filename:line] text).
Your task is to identify the START and END line markers for every lesson/topic found in that text.
Use the provided Table of Contents as the ground truth for lesson names.
Output ONLY a valid JSON object mapping Lesson Title to its range.

=== TABLE OF CONTENTS ===
{toc_content}

=== OUTPUT FORMAT ===
{{
  "Lesson Title": {{'start': "raw_1.txt:5", 'end': "raw_2.txt:10"}}
}}
"""
        
        # User Content (The merged raw text)
        user_content = merged_path.read_text(encoding='utf-8')

        # Call Gemini (Headless CLI)
        full_prompt = f"{system_instruction}\n\n{user_content}"
        resp_text = self.client.generate_content_headless(
            full_prompt
        )
        
        if not resp_text:
            print("❌ Failed to generate index mapping.")
            return None
            
        try:
            # Clean potential markdown block ```json ... ```
            cleaned_json = resp_text.replace("```json", "").replace("```", "").strip()
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
