# Module 20: The Data Indexer (`text_processing.py`)

## 1. Tool Definition
**What is it?** 
When the OCR Engine finishes extracting text, it leaves behind 300 messy `.txt` files on the hard drive. 
`system-workspace/tools/automation/modules/text_processing.py` cleans this mess. It parses the entire textbook, numbers every single line of text, and uses a combination of Regex and Gemini LLMs to mathematically map which lines of text belong to which grammar lesson.

## 2. I/O Mapping
*   **Inputs:** 
    *   `system-workspace/text-data/raw/` (300 OCR text files).
    *   `input/TOC.json` (The Table of Contents metadata).
*   **Processes:**
    *   **Merge & Index**: Concatenates all files into one massive string, prefixing every line with an absolute coordinate (e.g., `[raw_5.txt:42]`).
    *   **LLM Mapping**: If the book uses dynamic topic lengths, it asks Gemini to figure out exactly which coordinates bound Lesson 5 versus Lesson 6.
    *   **Strict Pagination**: If the book uses the "1-Page Law", it bypasses AI entirely and uses Regex to slice the text exactly at `----- PAGE X -----` markers.
*   **Outputs:**
    *   `full_raw_indexed.txt` (The master text file).
    *   `raw_to_lesson_index.json` (The coordinate map used by the `jules_planner.py` to extract text).

---

## 3. The Deep Dive: Codebase Analysis

Below is an exhaustive, 100% codebase breakdown of the Text Processing engine.

### Block A: Configuration & Validation
The orchestrator must first locate the data and validate the TOC JSON structure to ensure other tools won't crash when reading it.

```python
# From system-workspace/tools/automation/modules/text_processing.py

20:     def __init__(self, project_root=None, api_key=None, use_headless=False):
21:         self.project_root = (
22:             Path(project_root)
23:             if project_root
24:             else Path(__file__).parent.parent.parent.parent.parent
25:         )
26:         self.raw_dir = self.project_root / "system-workspace/text-data/raw"
27:         self.toc_path = self.project_root / "input/TOC.json"
28:         self.index_file = self.project_root / "system-workspace/text-data/raw_to_lesson_index.json"
...
36:     def validate_toc(self):
37:         """
38:         Validates the structure of TOC.json.
39:         Expected format: JSON object where keys are lesson numbers and values are metadata dicts.
40:         """
41:         if not self.toc_path.exists():
42:             print(f"❌ TOC file not found at {self.toc_path}")
43:             return False
44: 
45:         try:
46:             content = self.toc_path.read_text(encoding="utf-8").strip()
47:             data = json.loads(content)
...
57:             # Check for required fields in at least one item
58:             first_key = next(iter(data))
59:             if not isinstance(data[first_key], dict) or "title" not in data[first_key]:
60:                 print("❌ TOC items do not have 'title' field.")
61:                 return False
62: 
63:             print(f"✅ TOC Validated: {len(data)} topics found.")
64:             return True
```
#### Line-by-Line Commentary
*   **Lines 26-28:** Explicitly defines the paths. Notice how the `raw_dir` acts as the input, and `full_raw_indexed.txt` acts as the compiled output.
*   **Lines 46-47:** It strictly tests if the JSON is valid using standard Python `json.loads`.
*   **Lines 58-61:** *Schema Validation*. It doesn't just check if the JSON parses; it checks the actual data structure. It looks at the first item in the dictionary to ensure the AI actually included the mandatory `"title"` key.

### Block B: The Raw Text Merger
Before the AI can map the text, we must combine the 300 loose files into a single, highly indexable file.

```python
# From system-workspace/tools/automation/modules/text_processing.py

94:     def merge_raw_text(self):
...
100:         # Sort files numerically
101:         def sort_key(p):
102:             try:
103:                 match = re.search(r"raw_(\d+)", p.name)
104:                 return int(match.group(1)) if match else 0
105:             except ValueError:
106:                 return 0
107: 
108:         files = sorted(list(self.raw_dir.glob("raw_*.txt")), key=sort_key)
...
114:         all_content = []
115:         for f in files:
116:             try:
117:                 lines = f.read_text(encoding="utf-8").splitlines()
118:                 for i, line in enumerate(lines):
119:                     if len(line.strip()) < 2:
120:                         continue
121:                     all_content.append(f"[{f.name}:{i + 1}] {line}")
122:             except Exception as e:
123:                 print(f"⚠️ Error reading {f.name}: {e}")
124: 
125:         merged_content = "\n".join(all_content)
126:         output_path = self.project_root / "system-workspace/text-data/full_raw_indexed.txt"
127:         output_path.parent.mkdir(parents=True, exist_ok=True)
128:         output_path.write_text(merged_content, encoding="utf-8")
```
#### Line-by-Line Commentary
*   **Lines 101-106:** Standard Python string sorting is alphabetical (`raw_1`, `raw_10`, `raw_2`). That would completely break the timeline of the textbook! This `sort_key` extracts the integer using Regex, forcing a mathematical sort (`1, 2, 3... 10`).
*   **Lines 118-121:** `all_content.append(f"[{f.name}:{i + 1}] {line}")`
    *   This is the most critical line of text processing. It strips out blank lines (`< 2`) to save tokens, and dynamically injects an absolute coordinate marker (`[raw_1.txt:15]`) at the beginning of every single line. This allows the AI to say "The lesson starts at `raw_1:15` and ends at `raw_1:45`".

### Block C: AI-Driven TOC & Index Generation
If the book lacks clear visual "PAGE" markers, the orchestrator asks Gemini to read the textbook and figure out where the lessons begin and end.

```python
# From system-workspace/tools/automation/modules/text_processing.py

204:     def generate_lesson_index(self):
...
233:         # System Prompt
234:         system_instruction = f"""You are an expert Arabic book editor.
235: I have a file containing lines from transcribed Arabic grammar images (format: [filename:line] text).
236: 
237: Your task is to identify the EXACT START and END line markers for every lesson/topic found in that text based on the provided Table of Contents (TOC).
238: CRITICAL RULES:
239: 1. You MUST use the provided Table of Contents as the definitive source for lesson titles.
240: 2. The keys in your JSON output MUST match the exact titles from the TOC. Do not invent, paraphrase, or skip any lesson titles.
241: 3. Find the exact `[filename:line]` where each lesson begins (usually indicated by a title heading) and where it ends (just before the next lesson begins, or at the end of the text).
242: 4. Output ONLY a valid JSON object. No explanations.
243: 
244: === TABLE OF CONTENTS ===
245: {toc_content}
246: 
247: === OUTPUT FORMAT ===
248: {{
249:   "Exact Lesson Title 1": {{
250:     "start": "raw_1.txt:5",
251:     "end": "raw_2.txt:10"
252:   }}
253: }}
254: """
255: 
256:         # User Content (The merged raw text)
257:         user_content = merged_path.read_text(encoding="utf-8")
258: 
259:         # Call Gemini (Smart Client handles API Key vs CLI)
260:         resp_text = self.client.generate_content(
261:             system_instruction=system_instruction, user_content=user_content
262:         )
```
#### Line-by-Line Commentary
*   **Lines 237-241:** The system prompt explains the exact syntax of the injected markers from Block B, instructing the AI to use them as boundaries. 
*   **Line 257:** It dumps the entire 300-page indexed textbook file directly into the `user_content` prompt. Gemini 1.5 Pro has a 1-million token context window, so it easily handles this task in a single API call.

### Block D: The "1-Page Law" Hardware Auto-Paginator
AI is prone to hallucination. If we are running the strict 1-Page Layout mode (which requires absolute millimeter perfection), we cannot trust the AI to slice the text. We use Regex.

```python
# From system-workspace/tools/automation/modules/text_processing.py

289:     def generate_auto_page_index_and_toc(self, generate_toc=True):
290:         """
291:         Automatically generates TOC.json and raw_to_lesson_index.json by slicing
292:         the raw text at '----- PAGE X -----' markers, bypassing AI completely.
293:         """
...
321:         page_pattern = re.compile(r'^-+\s*PAGE\s+(.+?)\s*-+', re.IGNORECASE)
322:         
323:         for line in lines:
324:             tag_match = re.match(r'^\[(raw_[^:]+:\d+)\]\s*(.*)$', line)
325:             if not tag_match:
326:                 continue
327:                 
328:             file_line_ref = tag_match.group(1)
329:             actual_content = tag_match.group(2).strip()
330:             
331:             page_match = page_pattern.match(actual_content)
332:             if page_match:
333:                 # Close the previous page block
334:                 if current_page_title and current_start_marker and prev_file_line_ref:
335:                     mapping[current_page_title]["end"] = prev_file_line_ref
336:                 
337:                 page_id_raw = page_match.group(1).strip()
338:                 page_key = page_id_raw
339:                 title = f"page {page_id_raw}"
...                
350:                 mapping[title] = {
351:                     "start": file_line_ref,
352:                     "end": None
353:                 }
...                
358:             prev_file_line_ref = file_line_ref
```
#### Line-by-Line Commentary
*   **Line 321:** `re.compile(r'^-+\s*PAGE\s+(.+?)\s*-+')`
    *   This targets physical separators written in the raw OCR files (e.g., `----- PAGE 5 -----`).
*   **Lines 324-331:** As it loops through the massive file, it strips the coordinate marker off (`[raw_1.txt:10]`) just long enough to check if the underlying Arabic text is actually a PAGE marker.
*   **Lines 334-353:** *The Tracking Logic*. When it hits a PAGE marker, it immediately takes the `prev_file_line_ref` (e.g., the coordinate of the line just before this one) and sets it as the `end` coordinate for the previous page in the JSON object! Then, it initializes a new mapping object for the current page.

### Review
You have successfully dissected `text_processing.py`. You now understand custom string sorting, absolute coordinate injection, AI Context Mapping, and deterministic Regex pagination!
