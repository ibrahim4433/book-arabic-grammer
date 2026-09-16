import json
import re
import sys
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
        self.project_root = (
            Path(project_root)
            if project_root
            else Path(__file__).parent.parent.parent.parent.parent
        )
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
            content = self.toc_path.read_text(encoding="utf-8").strip()
            data = json.loads(content)

            if not isinstance(data, dict):
                print("❌ TOC JSON is not a dictionary object.")
                return False

            if not data:
                print("❌ TOC file is empty.")
                return False

            # Check for required fields in at least one item
            first_key = next(iter(data))
            if not isinstance(data[first_key], dict) or "title" not in data[first_key]:
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
        # First, attempt to extract the number directly if the title has a "XXX - Title" format
        match = re.match(r'^(\d+)', lesson_title.strip())
        if match:
            return match.group(1).zfill(3)

        # Fallback for titles that don't have a number prefix
        if not self.toc_path.exists():
            return "00"

        try:
            content = self.toc_path.read_text(encoding="utf-8")
            data = json.loads(content)

            clean_input_title = re.sub(r"^\d+\s*-\s*", "", lesson_title).strip()

            for number, metadata in data.items():
                title = metadata.get("title", "").strip()
                if title == clean_input_title:
                    return str(number).zfill(3)

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
                match = re.search(r"raw_(\d+)", p.name)
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
                lines = f.read_text(encoding="utf-8").splitlines()
                for i, line in enumerate(lines):
                    if len(line.strip()) < 2:
                        continue
                    all_content.append(f"[{f.name}:{i + 1}] {line}")
            except Exception as e:
                print(f"⚠️ Error reading {f.name}: {e}")

        merged_content = "\n".join(all_content)
        output_path = self.project_root / "system-workspace/text-data/full_raw_indexed.txt"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(merged_content, encoding="utf-8")

        print(f"📄 Merged {len(files)} files into {output_path}")
        return output_path

    def generate_toc(self, merged_path):
        """
        Uses Gemini to generate the TOC.json from the merged raw text.
        """
        print("🔍 Generating TOC from raw text via Gemini...")
        # Load settings
        settings_file = self.project_root / "system-workspace" / "settings.json"
        author = "أ. حنا خفيف"
        author_number = " "
        if settings_file.exists():
            try:
                with open(settings_file, encoding="utf-8") as f:
                    settings = json.load(f)
                    author = settings.get("author", author)
                    author_number = settings.get("author_number", author_number)
            except Exception as e:
                print(f"⚠️ Could not load settings: {e}")

        system_instruction = f"""You are an expert Arabic book editor.
I have a file containing transcribed Arabic grammar and literature text.
Your task is to extract the Table of Contents (TOC) from this text and output it as a JSON object.
CRITICAL RULES:
1. Identify ONLY the main, top-level lessons. Do NOT include sub-sections, author biographies (e.g. "شاعر سوري"), introductory blurbs, or comprehension question headings as separate lessons. A single Literature lesson should encompass the entire poem, its author bio, and its questions.
2. The output MUST be a JSON object where the keys are lesson numbers (e.g., "01", "02").
3. Each value must be an object with the exact following fields: 'title', 'level', 'Unit', 'author', 'author_number'.
4. You MUST logically infer an appropriate 'level' (المستوى) and 'Unit' (الوحدة) for each lesson by analyzing its topic and depth in the text (e.g., Level: 'المستوى التأسيسي', Unit: 'الأدب والنصوص' or 'علم النحو'). Do NOT leave them blank.
5. For 'author', use exactly: "{author}".
6. For 'author_number', use exactly: "{author_number}".
7. Output ONLY a valid JSON object. No explanations.

=== OUTPUT FORMAT ===
{{
  "01": {{
    "title": "Exact Arabic Title 1",
    "level": "المستوى المبتدئ",
    "Unit": "قواعد النحو",
    "author": "{author}",
    "author_number": "{author_number}"
  }}
}}
"""
        user_content = merged_path.read_text(encoding="utf-8")

        resp_text = self.client.generate_content(
            system_instruction=system_instruction, user_content=user_content
        )

        if not resp_text:
            print("❌ Failed to generate TOC.")
            return False

        try:
            cleaned_json = resp_text.replace("```json", "").replace("```", "").strip()
            match = re.search(r"\{.*\}", cleaned_json, re.DOTALL)
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
            toc_data = json.loads(self.toc_path.read_text(encoding="utf-8"))
            # Simplify TOC for the prompt: "Number - Title" list
            toc_lines = []
            sorted_keys = sorted(
                toc_data.keys(), key=lambda x: int(x) if x.isdigit() else float("inf")
            )
            for num in sorted_keys:
                meta = toc_data[num]
                toc_lines.append(f"{num} - {meta.get('title', 'Unknown')}")
            toc_content = "\n".join(toc_lines)
        except Exception as e:
            print(f"❌ Failed to process TOC.json: {e}")
            return None

        # System Prompt
        system_instruction = f"""You are an expert Arabic book editor.
I have a file containing lines from transcribed Arabic grammar and literature text (format: [filename:line] text).

Your task is to identify the EXACT START and END line markers for every lesson/topic found in that text based on the provided Table of Contents (TOC).
CRITICAL RULES:
1. You MUST use the provided Table of Contents as the definitive source for lesson titles.
2. The keys in your JSON output MUST match the exact titles from the TOC. Do not invent, paraphrase, or skip any lesson titles.
3. Find the exact `[filename:line]` where each lesson begins (usually indicated by a title heading) and where it ends (just before the next lesson begins, or at the very end of the text). A lesson's range MUST encompass all its sub-sections, author biographies, poems, explanations, and questions. Do NOT stop the end marker prematurely.
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
        user_content = merged_path.read_text(encoding="utf-8")

        # Call Gemini (Smart Client handles API Key vs CLI)
        # Using generate_content instead of forced headless mode
        resp_text = self.client.generate_content(
            system_instruction=system_instruction, user_content=user_content
        )

        if not resp_text:
            print("❌ Failed to generate index mapping.")
            return None

        try:
            # Clean potential markdown block ```json ... ```
            cleaned_json = resp_text.replace("```json", "").replace("```", "").strip()

            # Additional cleanup if needed (e.g. remove preamble text before {)
            match = re.search(r"\{.*\}", cleaned_json, re.DOTALL)
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

    def generate_auto_page_index_and_toc(self, generate_toc=True):
        """
        Automatically generates TOC.json and raw_to_lesson_index.json by slicing
        the raw text at '----- PAGE X -----' markers, bypassing AI completely.
        """
        merged_path = self.merge_raw_text()
        if not merged_path:
            return False

        print("🔍 Auto-generating TOC and Index from '----- PAGE X -----' markers...")

        # Load settings for TOC
        settings_file = self.project_root / "system-workspace" / "settings.json"
        author = "أ. حنا خفيف"
        author_number = " "
        if settings_file.exists():
            try:
                with open(settings_file, encoding="utf-8") as f:
                    settings = json.load(f)
                    author = settings.get("author", author)
                    author_number = settings.get("author_number", author_number)
            except Exception as e:
                print(f"⚠️ Could not load settings: {e}")

        toc = {}
        mapping = {}
        
        lines = merged_path.read_text(encoding="utf-8").splitlines()
        current_page_title = None
        current_start_marker = None
        prev_file_line_ref = None
        
        page_pattern = re.compile(r'^-+\s*PAGE\s+(.+?)\s*-+', re.IGNORECASE)
        
        for line in lines:
            tag_match = re.match(r'^\[(raw_[^:]+:\d+)\]\s*(.*)$', line)
            if not tag_match:
                continue
                
            file_line_ref = tag_match.group(1)
            actual_content = tag_match.group(2).strip()
            
            page_match = page_pattern.match(actual_content)
            if page_match:
                # Close the previous page block
                if current_page_title and current_start_marker and prev_file_line_ref:
                    mapping[current_page_title]["end"] = prev_file_line_ref
                
                page_id_raw = page_match.group(1).strip()
                page_key = page_id_raw
                title = f"page {page_id_raw}"
                
                if generate_toc:
                    toc[page_key] = {
                        "title": title,
                        "level": page_id_raw,
                        "Unit": page_id_raw,
                        "author": author,
                        "author_number": author_number
                    }
                
                mapping[title] = {
                    "start": file_line_ref,
                    "end": None
                }
                
                current_page_title = title
                current_start_marker = file_line_ref
                
            prev_file_line_ref = file_line_ref
            
        # Close the last page block
        if current_page_title and current_start_marker and prev_file_line_ref:
            mapping[current_page_title]["end"] = prev_file_line_ref

        # Save TOC if requested
        if generate_toc:
            self.toc_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.toc_path, "w", encoding="utf-8") as f:
                json.dump(toc, f, ensure_ascii=False, indent=2)

        # Save mapping
        self.index_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.index_file, "w", encoding="utf-8") as f:
            json.dump(mapping, f, ensure_ascii=False, indent=2)

        print(f"✅ Auto-Paginated Index generated with {len(mapping)} pages!")
        return True

    def generate_toc_and_index_from_markdown(self):
        """
        Parses input/TOC.md to generate deterministic TOC.json and raw_to_lesson_index.json
        by matching explicit page numbers to ----- PAGE X ----- markers in raw text.
        """
        md_path = self.project_root / "input/TOC.md"
        if not md_path.exists():
            print("❌ Error: input/TOC.md not found.")
            return False
            
        merged_path = self.merge_raw_text()
        if not merged_path:
            return False
            
        print("🔍 Parsing TOC from Markdown...")
        
        # Helper to convert Arabic-Indic digits to ASCII
        def arabic_to_ascii(text):
            trans = str.maketrans('٠١٢٣٤٥٦٧٨٩', '0123456789')
            return text.translate(trans)
            
        # 1. Scan raw text to build a map of Page Number -> File/Line Ref
        page_to_ref = {}
        last_ref = None
        lines = merged_path.read_text(encoding="utf-8").splitlines()
        page_pattern = re.compile(r'^-+\s*PAGE\s+(.+?)\s*-+', re.IGNORECASE)
        
        for line in lines:
            tag_match = re.match(r'^\[(raw_[^:]+:\d+)\]\s*(.*)$', line)
            if not tag_match:
                continue
                
            file_line_ref = tag_match.group(1)
            actual_content = tag_match.group(2).strip()
            last_ref = file_line_ref
            
            page_match = page_pattern.match(actual_content)
            if page_match:
                page_num_str = arabic_to_ascii(page_match.group(1).strip())
                page_to_ref[page_num_str] = file_line_ref
                
        # 2. Parse Markdown
        toc_data = {}
        lessons = [] # To keep order and compute start/end
        
        current_unit = "Unknown Unit"
        lesson_counter = 1
        
        md_lines = md_path.read_text(encoding="utf-8").splitlines()
        for line in md_lines:
            line = line.strip()
            if line.startswith("## "):
                current_unit = line[3:].strip()
            elif line.startswith("* **"):
                # Example: * **١٠١** | (القراءة التمهيدية) أدب القضايا الوطنية والقومية
                match = re.match(r'^\*\s*\*\*(.*?)\*\*\s*\|\s*(.*)$', line)
                if match:
                    page_ar = match.group(1).strip()
                    page_ascii = arabic_to_ascii(page_ar)
                    
                    # Handle ranges like 215 - 216 by taking the first number
                    page_ascii = page_ascii.split('-')[0].strip()
                    
                    title = match.group(2).strip()
                    
                    lesson_num_str = str(lesson_counter).zfill(3)
                    
                    settings_file = self.project_root / "system-workspace" / "settings.json"
                    author = "أ. حنا خفيف"
                    author_number = " "
                    
                    toc_data[lesson_num_str] = {
                        "title": title,
                        "level": current_unit, # Using Unit as level as a proxy, user can edit
                        "Unit": current_unit,
                        "author": author,
                        "author_number": author_number,
                        "page_number": page_ascii
                    }
                    
                    lessons.append({
                        "id": lesson_num_str,
                        "title": f"{lesson_num_str} - {title}",
                        "page": page_ascii
                    })
                    
                    lesson_counter += 1
                    
        # 3. Build Mapping
        mapping = {}
        for i, lesson in enumerate(lessons):
            page_str = lesson["page"]
            start_ref = page_to_ref.get(page_str)
            if not start_ref:
                print(f"⚠️ Warning: Could not find '----- PAGE {page_str} -----' in raw text for lesson '{lesson['title']}'. Mapping may fail.")
                start_ref = "UNKNOWN"
                
            # End ref is start of next lesson
            if i + 1 < len(lessons):
                next_page = lessons[i+1]["page"]
                end_ref = page_to_ref.get(next_page, "UNKNOWN")
            else:
                end_ref = last_ref
                
            mapping[lesson["title"]] = {
                "start": start_ref,
                "end": end_ref
            }
            
        # 4. Save files
        self.toc_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.toc_path, "w", encoding="utf-8") as f:
            json.dump(toc_data, f, ensure_ascii=False, indent=2)

        self.index_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.index_file, "w", encoding="utf-8") as f:
            json.dump(mapping, f, ensure_ascii=False, indent=2)
            
        print(f"✅ Successfully generated TOC and Index from Markdown ({len(lessons)} lessons).")
        return True

    def generate_nested_toc_from_semantic_maps(self):
        """
        Generates a nested TOC.json using the existing flat TOC.json 
        and the part chunks from semantic maps for the 1-part method.
        """
        if not self.toc_path.exists():
            print("❌ Base TOC.json not found. Run standard TOC generation first.")
            return False

        maps_dir = self.project_root / "system-workspace/text-data/semantic_maps"
        if not maps_dir.exists():
            print("❌ Semantic maps directory not found.")
            return False

        try:
            toc_data = json.loads(self.toc_path.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"❌ Failed to read TOC.json: {e}")
            return False

        nested_toc = {}
        
        for num, metadata in toc_data.items():
            lesson_number = num.zfill(3)
            map_path = maps_dir / f"lesson_{lesson_number}.json"
            
            # Copy base metadata
            nested_toc[num] = metadata.copy()
            nested_toc[num]["parts"] = []
            
            if map_path.exists():
                try:
                    chunks = json.loads(map_path.read_text(encoding="utf-8"))
                    for i, chunk in enumerate(chunks):
                        nested_toc[num]["parts"].append({
                            "part_index": i + 1,
                            "title": chunk.get("title", ""),
                            "start_line": chunk.get("start_line", 0),
                            "end_line": chunk.get("end_line", 0)
                        })
                except Exception as e:
                    print(f"⚠️ Failed to parse map for lesson {lesson_number}: {e}")

        # Save nested TOC
        nested_toc_path = self.project_root / "input/TOC_1part.json"
        nested_toc_path.parent.mkdir(parents=True, exist_ok=True)
        with open(nested_toc_path, "w", encoding="utf-8") as f:
            json.dump(nested_toc, f, ensure_ascii=False, indent=2)

        print(f"✅ Nested TOC generated at {nested_toc_path}")

    def merge_semantic_maps_globally(self):
        """
        Loads all lesson_XXX.json semantic maps, converts their relative bounds to absolute
        global line numbers based on raw_to_lesson_index.json, and merges contiguous chunks
        that share the same title into a unified global_semantic_map.json.
        """
        print("🌍 Merging semantic maps into global sequence...")
        index_path = self.project_root / "system-workspace/text-data/raw_to_lesson_index.json"
        maps_dir = self.project_root / "system-workspace/text-data/semantic_maps"
        full_raw_path = self.project_root / "system-workspace/text-data/full_raw_indexed.txt"
        
        if not index_path.exists() or not full_raw_path.exists():
            print("❌ Error: Missing index or raw file for global merge.")
            return False
            
        # 1. Build a marker -> absolute line number mapping
        marker_to_abs = {}
        lines = full_raw_path.read_text(encoding="utf-8").splitlines()
        for idx, line in enumerate(lines):
            match = re.match(r"^\[(.*?)\]", line)
            if match:
                marker_to_abs[match.group(1)] = idx  # 0-indexed absolute line
                
        # 2. Iterate through lessons in order
        mapping = json.loads(index_path.read_text(encoding="utf-8"))
        global_chunks = []
        
        for title, info in mapping.items():
            lesson_number = self.get_lesson_number(title)
            map_path = maps_dir / f"lesson_{lesson_number}.json"
            if not map_path.exists():
                continue
                
            start_marker = info["start"]
            if start_marker not in marker_to_abs:
                # Fallback: search forward for the next available marker
                m = re.match(r'^(raw_[^:]+):(\d+)$', start_marker)
                found = False
                if m:
                    file_name, line_num = m.group(1), int(m.group(2))
                    for offset in range(1, 50):
                        test_marker = f"{file_name}:{line_num + offset}"
                        if test_marker in marker_to_abs:
                            start_marker = test_marker
                            found = True
                            break
                if not found:
                    print(f"⚠️ Warning: Start marker {info['start']} not found in full_raw_indexed.txt (even after fallback)")
                    continue
                
            abs_start_offset = marker_to_abs[start_marker]
            
            try:
                chunks = json.loads(map_path.read_text(encoding="utf-8"))
                for chunk in chunks:
                    abs_start = abs_start_offset + chunk["start_line"] - 1
                    abs_end = abs_start_offset + chunk["end_line"] - 1
                    
                    global_chunks.append({
                        "lesson_id": str(lesson_number),
                        "title": chunk["title"],
                        "start_line": abs_start,
                        "end_line": abs_end
                    })
            except Exception as e:
                print(f"Error reading {map_path.name}: {e}")
                
        # 3. Merge contiguous chunks with the same title
        if not global_chunks:
            print("❌ No chunks found to merge.")
            return False
            
        merged_chunks = []
        current_chunk = global_chunks[0].copy()
        
        for i in range(1, len(global_chunks)):
            next_chunk = global_chunks[i]
            
            # If same title, merge them (ignore the gap)
            if next_chunk["title"] == current_chunk["title"]:
                current_chunk["end_line"] = next_chunk["end_line"]
            else:
                merged_chunks.append(current_chunk)
                current_chunk = next_chunk.copy()
                
        merged_chunks.append(current_chunk)
        
        # 4. Save
        out_path = self.project_root / "system-workspace/text-data/global_semantic_map.json"
        out_path.write_text(json.dumps(merged_chunks, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"✅ Created global_semantic_map.json with {len(merged_chunks)} unified parts!")
        return True
        return True
if __name__ == "__main__":
    tp = TextProcessor()
    tp.validate_toc()
