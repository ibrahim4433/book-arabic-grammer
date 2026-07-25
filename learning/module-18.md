# Module 18: The Content Stream Orchestrator (`jules_planner.py`)

## 1. Tool Definition
**What is it?** 
The AI cannot simply read the raw Arabic OCR text and spit out a perfect HTML page. The cognitive load is too high. 
Instead, the process is split into two phases. Phase 1 is **Planning**. 

`system-workspace/tools/automation/modules/jules_planner.py` orchestrates this planning phase. It takes the raw Arabic OCR text, injects the `elements_index.md` so the AI knows what UI components exist, and commands the AI to generate a "Content Stream" plan (a Markdown file detailing exactly which text goes into which UI box).

## 2. I/O Mapping
*   **Inputs:** 
    *   The massive `full_raw_indexed.txt` (the raw book text).
    *   The `raw_to_lesson_index.json` (maps text ranges to specific lessons).
    *   `Architect_GEM_MASTER.md` (The primary System Prompt).
*   **Processes:**
    *   Uses Regex to surgically extract just the raw text needed for a specific lesson.
    *   Concatenates the System Prompt, the Elements Index, the Raw Text, and the TOC JSON metadata into one gigantic "Mega Prompt".
    *   Launches 5 concurrent API threads to process multiple plans simultaneously.
    *   Updates `project_workflow_state.json` with the Google Cloud Session IDs.
*   **Outputs:**
    *   Markdown files saved into the `plans/` directory (e.g., `plans/page_05-plan.md`).

---

## 3. The Deep Dive: Codebase Analysis

Below is an exhaustive, 100% codebase breakdown of the Planning Orchestrator.

### Block A: State Initialization & Context Injection
Before launching any threads, the orchestrator must gather its cognitive resources.

```python
# From system-workspace/tools/automation/modules/jules_planner.py

36:         # Load Prompts
37:         master_prompt_name = "Architect_GEM_MASTER_1_PAGE.md" if is_1_page_mode else "Architect_GEM_MASTER.md"
38:         self.architect_prompt = (
39:             self.project_root / f"system-workspace/{master_prompt_name}"
40:         ).read_text(encoding="utf-8")
41: 
42:         # Inject elements_index.md to prevent Context Starvation
43:         elements_index_path = self.project_root / "Jules-workspace/elements_index.md"
44:         if elements_index_path.exists():
45:             elements_text = elements_index_path.read_text(encoding="utf-8")
46:             self.architect_prompt += f"\n\n--- ELEMENTS INDEX DICTIONARY ---\n{elements_text}\n"
47: 
48:         auditor_prompt_name = "Architect_AUDITOR_1_PAGE.md" if is_1_page_mode else "Architect_AUDITOR.md"
49:         self.auditor_prompt = (
50:             self.project_root / f"system-workspace/{auditor_prompt_name}"
51:         ).read_text(encoding="utf-8")
52: 
53:         # Load Raw Text Index
54:         self.raw_text_path = self.project_root / "system-workspace/text-data/full_raw_indexed.txt"
55:         if not self.raw_text_path.exists():
56:             logging.warning("⚠️ Raw text index missing. Generating...")
57:             self.tp.merge_raw_text()
58: 
59:         self.raw_lines = self.raw_text_path.read_text(encoding="utf-8").splitlines()
```
#### Line-by-Line Commentary
*   **Lines 37-40:** It dynamically selects the correct system prompt depending on whether the system is running in standard mode or `is_1_page_mode` (The 1-Page Law enforcer).
*   **Lines 42-46:** *Context Starvation Prevention*. The AI cannot use Atomic Design elements if it doesn't know they exist. This reads the `elements_index.md` (which documents all the CSS classes and templates) and directly appends it to the bottom of the System Prompt.
*   **Lines 54-59:** It loads the entirety of the raw OCR text into memory (`self.raw_lines`), automatically calling the TextProcessor (`self.tp.merge_raw_text()`) to generate it if it's missing.

### Block B: The Raw Text Extractor
We have 300 pages of text in memory. We only want to send 1 page to the AI.

```python
# From system-workspace/tools/automation/modules/jules_planner.py

61:     def _extract_lesson_text(self, start_marker, end_marker):
62:         """
63:         Extracts lines from full_raw_indexed.txt between start and end markers.
64:         Markers format: "raw_filename.txt:line_number"
65:         """
66:         extracted = []
67:         capturing = False
68: 
69:         # Parse markers to match format [filename:line]
70:         # TextProcessor index format: "raw_1.txt:5"
71:         # File format: "[raw_1.txt:5] Content..."
72: 
73:         start_pattern = f"[{start_marker}]"
74:         end_pattern = f"[{end_marker}]"
75: 
76:         for line in self.raw_lines:
77:             if start_pattern in line:
78:                 capturing = True
79: 
80:             if capturing:
81:                 # Remove the [marker] prefix for cleaner prompt
82:                 clean_line = re.sub(r"^\[.*?\]\s*", "", line)
83:                 extracted.append(clean_line)
84: 
85:             if end_pattern in line:
86:                 capturing = False
87:                 break
88: 
89:         return "\n".join(extracted)
```
#### Line-by-Line Commentary
*   **Lines 73-74:** The JSON index maps lessons to markers like `raw_5.txt:42`. This formats them into the bracket notation used inside the text file.
*   **Lines 76-88:** A highly efficient `O(n)` linear scan. It reads through the 10,000 lines of text. As soon as it hits the start marker, it flips `capturing = True` and begins saving the lines to memory. As soon as it hits the end marker, it physically `break`s the loop to save CPU cycles.
*   **Line 82:** `re.sub(r"^\[.*?\]\s*", "", line)`
    *   We don't want the AI to read the internal tracking markers (`[raw_5.txt:42]`). This regex cleanly strips them out before sending the text to the cloud.

### Block C: Batch Processing Filter
Before launching threads, the orchestrator checks which files actually need to be generated to prevent wasting API credits.

```python
# From system-workspace/tools/automation/modules/jules_planner.py

143:         # 2. Filter Processed Lessons?
144:         to_process = {}
145:         for title, info in mapping.items():
146:             lesson_number = self.tp.get_lesson_number(title)
147: 
148:             # Check Exclusions
149:             if excluded_lessons and (
150:                 lesson_number in excluded_lessons or str(int(lesson_number)) in excluded_lessons
151:             ):
152:                 update_callback(title, "SKIP", f"Lesson {lesson_number} excluded (Page exists)")
153:                 continue
154: 
155:             if only_lessons and (
156:                 lesson_number not in only_lessons and str(int(lesson_number)) not in only_lessons
157:             ):
158:                 continue  # Skip if we only want specific lessons
159: 
160:             clean_title = re.sub(r"^\d+\s*-\s*", "", title).strip()
161:             
162:             if getattr(self, "is_1_page_mode", False):
163:                 plan_path = self.project_root / f"plans/page_{lesson_number}-plan.md"
164:             else:
165:                 plan_path = self.project_root / f"plans/{lesson_number}-{clean_title}-plan.md"
166: 
167:             if plan_path.exists() and not force_remake:
168:                 update_callback(title, "SKIP", "Plan exists")
169:             else:
170:                 to_process[title] = info
171:                 update_callback(title, "PENDING", "Queued")
172: 
173:         if not to_process:
174:             update_callback("System", "DONE", "All plans exist.")
175:             return
```
#### Line-by-Line Commentary
*   **Lines 149-158:** It handles the CLI arguments `--exclude` or `--only`. If a developer only wants to test Lesson 5, this skips all other entries in the dictionary.
*   **Lines 162-167:** It calculates the expected final filepath. If the file already exists on the hard drive, and the developer didn't pass the `force_remake` override, it safely `SKIP`s the API call.

### Block D: Resilient Session Creation & State Management
When the threads finally execute, they must be extremely fault-tolerant.

```python
# From system-workspace/tools/automation/modules/jules_planner.py

282:         # 4. Check or Create Session
283:         session_id = None
284: 
285:         # Check State Manager for existing session
286:         if self.state_manager:
287:             session_id = self.state_manager.get_lesson_data(lesson_title, "session_id")
288:             if session_id:
289:                 callback(lesson_title, "RUNNING", f"Checking Existing Session ({session_id})...")
290:                 status_data = self.client.get_session_status(session_id)
291:                 if status_data:
292:                     state = status_data.get("state", "UNKNOWN")
293:                     if state in ["SUCCEEDED", "COMPLETED"]:
294:                         callback(lesson_title, "RUNNING", f"Existing Session Completed: {state}")
295:                         # Skip creation, jump to pull
296:                     elif state in ["FAILED", "CANCELLED", "ERROR"]:
297:                         callback(
298:                             lesson_title,
299:                             "WARN",
300:                             f"Previous Session Failed ({state}). Creating New...",
301:                         )
302:                         session_id = None  # Force new session
303:                     else:
304:                         # RUNNING or UNKNOWN
305:                         callback(lesson_title, "RUNNING", f"Resuming Monitoring ({state})...")
306:                         # Keep session_id, proceed to wait
307:                 else:
308:                     callback(lesson_title, "WARN", "Existing Session ID invalid. Creating New...")
309:                     session_id = None
310: 
311:         if not session_id:
312:             callback(lesson_title, "RUNNING", "Creating Session...")
313:             try:
314:                 session = self.client.create_plan_session(lesson_title, mega_prompt)
315:             except APIBlockError as e:
316:                 self.abort_event.set()
317:                 callback(lesson_title, "API_BLOCKED", "API Quota/Limit Reached")
318:                 return
```
#### Line-by-Line Commentary
*   **Line 287:** `session_id = self.state_manager.get_lesson_data(lesson_title, "session_id")`
    *   *Resume-on-Failure Logic*. Before starting a new Cloud Session, it checks the local state database. Did this script crash 5 minutes ago? Was there already a session running for this lesson?
*   **Lines 290-302:** If a session ID was found in the database, it queries Google Cloud for the status. 
    *   If it `SUCCEEDED`, it bypasses the entire generation pipeline and jumps straight to downloading the results!
    *   If it `FAILED` (e.g., the AI hit a content safety filter), it wipes the session ID and prepares to create a new one.
*   **Lines 315-318:** `except APIBlockError:`
    *   If the AI provider cuts off access completely, it catches the error and crucially calls `self.abort_event.set()`. This instantly broadcasts a kill-signal to all other concurrent threads, shutting down the entire ThreadPool immediately instead of letting them all violently crash.

### Review
You have successfully dissected `jules_planner.py`. You now understand context injection, efficient text parsing, idempotent batch filtering, and resilient state-driven API monitoring!
