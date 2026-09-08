import json
import logging
import random
import re
import sys
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# Ensure modules are importable
sys.path.append(str(Path(__file__).parent))

from jules_client_plans import JulesPlanClient
from jules_client import APIBlockError
from text_processing import TextProcessor
from repoless_jules import RepolessJulesClient


class JulesPlanner:
    """
    Orchestrates the batch generation of plans using Jules Sessions.
    """

    def __init__(self, project_root, state_manager=None, is_1_page_mode=False, is_1_part_mode=False, part_instruction='', part_number=''):
        self.project_root = Path(project_root)
        self.state_manager = state_manager
        self.client = JulesPlanClient(project_root=self.project_root)
        self.tp = TextProcessor(project_root=self.project_root)
        self.is_1_page_mode = is_1_page_mode
        self.is_1_part_mode = is_1_part_mode
        self.part_instruction = part_instruction
        self.part_number = part_number

        self.abort_event = threading.Event()
        self._first_task_done = False
        self._delay_lock = threading.Lock()

        # Load Prompts
        if self.is_1_part_mode:
            master_prompt_name = "Architect_GEM_MASTER_1_PART.md"
        else:
            master_prompt_name = "Architect_GEM_MASTER_1_PAGE.md" if self.is_1_page_mode else "Architect_GEM_MASTER.md"
            
        self.architect_prompt = (
            self.project_root / f"system-workspace/{master_prompt_name}"
        ).read_text(encoding="utf-8")

        # Inject elements_index.md to prevent Context Starvation
        elements_index_path = self.project_root / "Jules-workspace/elements_index.md"
        if elements_index_path.exists():
            elements_text = elements_index_path.read_text(encoding="utf-8")
            self.architect_prompt += f"\n\n--- ELEMENTS INDEX DICTIONARY ---\n{elements_text}\n"

        if self.is_1_part_mode:
            part_mapping_path = self.project_root / "system-workspace/part_mapping.json"
            if part_mapping_path.exists():
                mapping_text = part_mapping_path.read_text(encoding="utf-8")
                self.architect_prompt += f"\n\n--- PART MAPPING JSON ---\n{mapping_text}\n"

        if self.is_1_part_mode:
            auditor_prompt_name = "Architect_AUDITOR_1_PART.md"
        else:
            auditor_prompt_name = "Architect_AUDITOR_1_PAGE.md" if is_1_page_mode else "Architect_AUDITOR.md"
            
        self.auditor_prompt = (
            self.project_root / f"system-workspace/{auditor_prompt_name}"
        ).read_text(encoding="utf-8")
        
        if self.is_1_part_mode and self.part_instruction:
            custom_inst = f"\n\n--- CUSTOM PART INSTRUCTION ---\n{self.part_instruction}\n"
            self.architect_prompt += custom_inst
            self.auditor_prompt += custom_inst

        # Load Raw Text Index
        self.raw_text_path = self.project_root / "system-workspace/text-data/full_raw_indexed.txt"
        if not self.raw_text_path.exists():
            logging.warning("⚠️ Raw text index missing. Generating...")
            self.tp.merge_raw_text()

        self.raw_lines = self.raw_text_path.read_text(encoding="utf-8").splitlines()

    def _extract_lesson_text(self, start_marker, end_marker):
        """
        Extracts lines from full_raw_indexed.txt between start and end markers.
        Markers format: "raw_filename.txt:line_number"
        """
        extracted = []
        capturing = False

        # Parse markers to match format [filename:line]
        # TextProcessor index format: "raw_1.txt:5"
        # File format: "[raw_1.txt:5] Content..."

        start_pattern = f"[{start_marker}]"
        end_pattern = f"[{end_marker}]"

        for line in self.raw_lines:
            if start_pattern in line:
                capturing = True

            if capturing:
                # Remove the [marker] prefix for cleaner prompt
                clean_line = re.sub(r"^\[.*?\]\s*", "", line)
                extracted.append(clean_line)

            if end_pattern in line:
                capturing = False
                break

        return "\n".join(extracted)

    def count_existing_plans(self, excluded_lessons=None, only_lessons=None):
        """Counts how many plans already exist for the current index."""
        index_path = self.project_root / "system-workspace/text-data/raw_to_lesson_index.json"
        if not index_path.exists(): return 0
        mapping = json.loads(index_path.read_text(encoding="utf-8"))
        count = 0
        
        for title, info in mapping.items():
            lesson_number = self.tp.get_lesson_number(title)
            if excluded_lessons:
                if lesson_number and (lesson_number in excluded_lessons or str(int(lesson_number)) in excluded_lessons): continue
            if only_lessons:
                if not lesson_number or (lesson_number not in only_lessons and str(int(lesson_number)) not in only_lessons): continue
            
            clean_title = re.sub(r"^\d+\s*-\s*", "", title).strip()
            clean_title = re.sub(r'[<>:"/\|?*]', '', clean_title)
            if getattr(self, "is_1_page_mode", False):
                existing = list((self.project_root / "plans").glob(f"page_{lesson_number}-plan*.md"))
            elif getattr(self, "is_1_part_mode", False):
                existing = list((self.project_root / "plans").glob(f"{lesson_number}.*_nXXX_{clean_title}-plan*.md"))
            else:
                existing = list((self.project_root / "plans").glob(f"{lesson_number}-{clean_title}-plan*.md"))
            count += len(existing)
        return count

    def _get_semantic_chunks(self, raw_text):
        try:
            client = RepolessJulesClient()
            lines = raw_text.splitlines()
            total_lines = len(lines)
            
            window_size = 800
            all_chunks = []
            
            current_start = 0
            
            while current_start < total_lines:
                # Extract the next window
                window_lines = lines[current_start:current_start+window_size]
                
                # Use local 1-based indexing for the LLM to avoid confusion with massive line numbers
                numbered_text = "\n".join([f"{j+1}: {line}" for j, line in enumerate(window_lines)])
                
                sys_prompt = """You are a smart text chunker for an Arabic grammar textbook.
Analyze the following raw OCR text and segment it into logical parts for lesson planning.
Each part should represent a distinct, cohesive section (e.g. a poem, a grammar rule explanation, a set of exercises, an author biography).
You MUST output ONLY a JSON array, with no markdown formatting and no extra text.
For each part, provide a descriptive title in Arabic and the start and end line numbers exactly as they appear in the text.

Schema:
[
  {
    "title": "Descriptive title of the part in Arabic",
    "start_line": 1,
    "end_line": 40
  }
]
"""
                logging.info(f"Sending window from line {current_start+1} (up to {current_start+len(window_lines)}) for semantic chunking...")
                response_json = client.generate_content(prompt=f"TEXT TO ANALYZE:\n{numbered_text}", system_instruction=sys_prompt)
                window_chunks = json.loads(response_json)
                
                if not window_chunks:
                    raise Exception("Jules returned empty chunks.")
                
                # Mathematically shift the bounds to match original global absolute index
                for chunk in window_chunks:
                    chunk["start_line"] += current_start
                    chunk["end_line"] += current_start
                    
                # If this is the final window, append all chunks and exit
                if current_start + window_size >= total_lines:
                    all_chunks.extend(window_chunks)
                    break
                    
                # If this is a middle window, we discard the final chunk as it may be cut randomly.
                # We start the next window perfectly at the end of the last safe chunk!
                if len(window_chunks) > 1:
                    last_safe_chunk = window_chunks[-2]
                    all_chunks.extend(window_chunks[:-1])
                    current_start = last_safe_chunk["end_line"]
                else:
                    # Rare edge case: the LLM returned exactly 1 massive chunk for the whole 800 lines.
                    all_chunks.extend(window_chunks)
                    current_start += window_size
                
            return all_chunks
        except Exception as e:
            logging.error(f"Semantic chunking failed: {e}")
            return None

    def run_batch_planning(
        self, max_concurrent=10, update_callback=None, excluded_lessons=None, only_lessons=None, force_remake=False
    ):
        """
        Main entry point. Orchestrates the batch processing.
        Args:
            update_callback (callable): Function(lesson_title, status, message)
            excluded_lessons (set): Set of lesson numbers (str) to skip.
        """
        if not update_callback:

            def default_callback(title, status, msg):
                logging.info(f"[{status}] {title}: {msg}")

            update_callback = default_callback

        if excluded_lessons is None:
            excluded_lessons = set()

        logging.info(f"\n🧠 Starting Jules Batch Planning (Max Concurrent: {max_concurrent})...")

        # 1. Get Lesson Index
        index_path = self.project_root / "system-workspace/text-data/raw_to_lesson_index.json"
        if not index_path.exists():
            update_callback("System", "WARN", "Lesson index missing. Generating...")
            mapping = self.tp.generate_lesson_index()
        else:
            mapping = json.loads(index_path.read_text(encoding="utf-8"))

        if not mapping:
            update_callback("System", "ERROR", "No lessons to process.")
            return

        # 2. Filter Processed Lessons?
        to_process = []
        
        for title, info in mapping.items():
            lesson_number = self.tp.get_lesson_number(title)
            
            # Check Exclusions
            if excluded_lessons:
                if lesson_number and (lesson_number in excluded_lessons or str(int(lesson_number)) in excluded_lessons):
                    update_callback(title, "SKIP", f"Lesson {lesson_number} excluded (Page exists)")
                    continue

            if only_lessons:
                if not lesson_number or (lesson_number not in only_lessons and str(int(lesson_number)) not in only_lessons):
                    continue  # Skip if we only want specific lessons

            raw_text = self._extract_lesson_text(info["start"], info["end"])
            if not raw_text:
                continue

            lines = raw_text.splitlines()
            # Semantic Chunking
            semantic_chunks = None
            if getattr(self, "is_1_part_mode", False):
                map_path = self.project_root / f"system-workspace/text-data/semantic_maps/lesson_{lesson_number}.json"
                if map_path.exists():
                    update_callback(title, "RUNNING", "Loading local Semantic Map...")
                    try:
                        semantic_chunks = json.loads(map_path.read_text(encoding="utf-8"))
                    except Exception as e:
                        logging.error(f"Failed to load local map {map_path}: {e}")
                        semantic_chunks = None
                        
                if not semantic_chunks:
                    update_callback(title, "RUNNING", "Generating Smart Semantic Chunks...")
                    semantic_chunks = self._get_semantic_chunks(raw_text)

            if semantic_chunks:
                num_chunks = len(semantic_chunks)
                chunk_parts = [str(i) for i in range(1, num_chunks + 1)]
                
                if getattr(self, "is_1_part_mode", False):
                    if isinstance(self.part_number, list) and self.part_number == ['1', '2', '3', '4']:
                        part_list = chunk_parts
                    elif isinstance(self.part_number, list):
                        part_list = [p for p in self.part_number if p in chunk_parts]
                    else:
                        part_list = [str(self.part_number)] if str(self.part_number) in chunk_parts else []
                else:
                    part_list = chunk_parts
            else:
                CHUNK_SIZE = 50
                num_chunks = max(1, (len(lines) + CHUNK_SIZE - 1) // CHUNK_SIZE)
                
                if getattr(self, "is_1_part_mode", False):
                    if isinstance(self.part_number, list) and self.part_number == ['1', '2', '3', '4']:
                        part_list = [str(i) for i in range(1, num_chunks + 1)]
                    elif isinstance(self.part_number, list):
                        part_list = self.part_number
                    else:
                        part_list = [str(self.part_number)]
                else:
                    part_list = [None]
                
            clean_title = re.sub(r"^\d+\s*-\s*", "", title).strip()
            clean_title = re.sub(r'[<>:"/\|?*]', '', clean_title)
            
            for p_num in part_list:
                display_title = f"[Part {p_num}/{num_chunks}] {title}" if p_num else title
                
                if getattr(self, "is_1_page_mode", False):
                    base_name = f"page_{lesson_number}-plan"
                elif getattr(self, "is_1_part_mode", False):
                    base_name = f"{lesson_number}.{p_num}_nXXX_{clean_title}-plan"
                else:
                    base_name = f"{lesson_number}-{clean_title}-plan"

                existing = list((self.project_root / "plans").glob(f"{base_name}*.md"))
                if existing and not force_remake:
                    update_callback(display_title, "SKIP", "Plan exists")
                else:
                    if force_remake and existing:
                        for f in existing:
                            try:
                                f.unlink()
                            except:
                                pass
                                
                    chunk_text = raw_text
                    if getattr(self, "is_1_part_mode", False) and p_num:
                        p_idx = int(p_num) - 1
                        if semantic_chunks and p_idx < len(semantic_chunks):
                            chunk_info = semantic_chunks[p_idx]
                            s_line = max(1, chunk_info["start_line"]) - 1
                            e_line = min(len(lines), chunk_info["end_line"])
                            chunk_lines = lines[s_line:e_line]
                            chunk_text = "\n".join(chunk_lines)
                            display_title = f"[Part {p_num}/{num_chunks}] {chunk_info['title']}"
                        elif not semantic_chunks and p_idx < num_chunks:
                            chunk_lines = lines[p_idx * CHUNK_SIZE : (p_idx + 1) * CHUNK_SIZE]
                            chunk_text = "\n".join(chunk_lines)
                        else:
                            continue # Skip out of bounds parts

                    to_process.append({
                        "title": title,
                        "display_title": display_title,
                        "info": info,
                        "p_num": p_num,
                        "chunk_text": chunk_text
                    })
                    update_callback(display_title, "PENDING", "Queued")

        if not to_process:
            update_callback("System", "DONE", "All plans exist.")
            return

        # 3. Execute Batch
        def _get_num(item):
            import re
            m = re.match(r"^(\d+)", item["title"])
            return int(m.group(1)) if m else 999
            
        sorted_items = sorted(to_process, key=_get_num)
        
        with ThreadPoolExecutor(max_workers=max_concurrent) as executor:
            future_to_lesson = {
                executor.submit(
                    self.process_lesson_with_callback, item["display_title"], item["title"], item["info"], update_callback, item.get("p_num"), item.get("chunk_text")
                ): item["display_title"]
                for item in sorted_items
            }

            for future in as_completed(future_to_lesson):
                pass  # The callback handles updates inside the future

        if hasattr(self, "pull_threads"):
            for t in self.pull_threads:
                t.join()

    def process_lesson_with_callback(self, display_title, original_title, range_info, callback, p_num=None, chunk_text=None):
        """Wrapper for process_lesson that uses callback."""
        callback(display_title, "RUNNING", "Starting...")
        try:
            # We wrap the inner callback so it always emits display_title
            self.process_lesson(original_title, range_info, lambda t, s, m, **kwargs: callback(display_title, s, m, **kwargs), force_remake=False, p_num=p_num, chunk_text=chunk_text)
        except Exception as e:
            callback(display_title, "ERROR", str(e))

    def process_lesson(self, lesson_title, range_info, callback=None, force_remake=False, p_num=None, chunk_text=None):
        """
        Worker function for a single lesson.
        """
        if self.abort_event.is_set():
            return

        if not callback:
            def default_callback(t, s, m, **kwargs):
                logging.info(f"[{s}] {t}: {m}")
            callback = default_callback

        # API Safety Delay (5-15s) to prevent burst
        with self._delay_lock:
            if not self._first_task_done:
                self._first_task_done = True
                delay = 0
            else:
                delay = random.uniform(5, 15)

        if delay > 0:
            callback(lesson_title, "RUNNING", f"Safety Delay ({delay:.1f}s)...")
            time.sleep(delay)

        # Attempt to parse number and title from the lesson_title (which is a key from index)
        match = re.match(r"^(\d+)\s*-\s*(.*)", lesson_title)
        if match:
            # Found "9 - Title"
            inferred_number = match.group(1).zfill(3)
            clean_title = match.group(2).strip()
            lesson_number = inferred_number
        else:
            # Fallback for "Title" only
            clean_title = lesson_title.strip()
            lesson_number = self.tp.get_lesson_number(clean_title)

        clean_title = re.sub(r'[<>:"/\\|?*]', '', clean_title)

        # Determine filename based on mode
        if getattr(self, "is_1_page_mode", False):
            base_filename = f"page_{lesson_number}-plan"
        elif getattr(self, "is_1_part_mode", False):
            p_num = p_num or getattr(self, "part_number", "1")
            base_filename = f"{lesson_number}.{p_num}_nXXX_{clean_title}-plan"
        else:
            base_filename = f"{lesson_number}-{clean_title}-plan"
            
        settings_file = self.project_root / "system-workspace/settings.json"
        workspace_code = None

        if settings_file.exists():
            try:
                with open(settings_file, encoding="utf-8") as f:
                    workspace_code = json.load(f).get("workspace_code")
            except:
                pass

        if workspace_code and workspace_code != "None":
            filename = f"{base_filename}_{workspace_code}.md"
        else:
            filename = f"{base_filename}.md"
            
        expected_path = f"plans/{filename}"

        # 0. Check if Plan Exists (Early Exit)
        existing_files = list((self.project_root / "plans").glob(f"{base_filename}*.md"))
        if existing_files and not force_remake:
            callback(lesson_title, "SUCCESS", f"Plan exists: {existing_files[0].name}", lesson_num=lesson_number, expected_path=expected_path)
            return True

        callback(lesson_title, "RUNNING", "Extracting Text...", lesson_num=lesson_number, expected_path=expected_path)

        # 1. Extract Text
        if chunk_text is not None:
            raw_text = chunk_text
        else:
            raw_text = self._extract_lesson_text(range_info["start"], range_info["end"])
            
        if not raw_text:
            callback(lesson_title, "ERROR", "No text found")
            return False

        # 2. Get Metadata from TOC.json
        lesson_metadata = {}
        if self.tp.toc_path.exists():
            try:
                toc_data = json.loads(self.tp.toc_path.read_text(encoding="utf-8"))
                # Try to find by number (stripping leading zeros if key is integer-like string)
                key = str(int(lesson_number)) if lesson_number.isdigit() else lesson_number
                if key in toc_data:
                    lesson_metadata = toc_data[key]
                else:
                    # Fallback: search by title
                    for k, v in toc_data.items():
                        if v.get("title", "").strip() == clean_title:
                            lesson_metadata = v
                            break
            except Exception:
                pass

        # 3. Construct Prompt
        lesson_data = {
            "number": lesson_number,
            "title": clean_title,
            "raw_text": raw_text,
            "level": lesson_metadata.get("level", ""),
            "unit": lesson_metadata.get("Unit", ""),
            "author": lesson_metadata.get("author", ""),
            "author_number": lesson_metadata.get("author_number", ""),
        }
        mega_prompt = self.client.construct_mega_prompt(
            lesson_data, self.architect_prompt, self.auditor_prompt, getattr(self, "is_1_page_mode", False)
        )
        
        if workspace_code and workspace_code != "None":
            filename = f"{base_filename}_{workspace_code}.md"
        else:
            filename = f"{base_filename}.md"
        mega_prompt += f"\n\nCRITICAL FILENAME INSTRUCTION: You MUST name the generated plan EXACTLY: `{filename}`. Do NOT deviate from this filename."

        mega_prompt += f"\n\nCRITICAL PATH INSTRUCTION: Do NOT place the generated plan inside `Jules-workspace/plans/`. You MUST place the generated plan in the root `plans/` directory."
        
        # Inject chunking critical rule
        mega_prompt += f"\n\nCRITICAL RULE (ZERO CONTENT LOSS): YOU MUST PROCESS 100% OF THE RAW TEXT SLICE PROVIDED ABOVE. Do NOT summarize. Do NOT filter by topic. Convert every single sentence of the provided text into the HTML plan, even if it seems unrelated to the lesson title '{clean_title}'! You are acting as a perfect transcriber/typesetter mapping physical chunks of text to HTML components."


        # 4. Check or Create Session
        session_id = None
        session_key = f"session_id_{base_filename}"

        if force_remake:
            if self.state_manager:
                self.state_manager.update_lesson_data(lesson_title, {session_key: None})
        elif self.state_manager:
            session_id = self.state_manager.get_lesson_data(lesson_title, session_key)
            if session_id:
                callback(lesson_title, "RUNNING", f"Checking Existing Session ({session_id})...")
                status_data = self.client.get_session_status(session_id)
                if status_data:
                    state = status_data.get("state", "UNKNOWN")
                    if state in ["SUCCEEDED", "COMPLETED"]:
                        callback(lesson_title, "RUNNING", f"Existing Session Completed: {state}")
                        # Skip creation, jump to pull
                    elif state in ["FAILED", "CANCELLED", "ERROR"]:
                        callback(
                            lesson_title,
                            "WARN",
                            f"Previous Session Failed ({state}). Creating New...",
                        )
                        session_id = None  # Force new session
                    else:
                        # RUNNING or UNKNOWN
                        callback(lesson_title, "RUNNING", f"Resuming Monitoring ({state})...")
                        # Keep session_id, proceed to wait
                else:
                    callback(lesson_title, "WARN", "Existing Session ID invalid. Creating New...")
                    session_id = None

        if not session_id:
            callback(lesson_title, "RUNNING", "Creating Session...")
            session = None
            for _attempt in range(10):
                try:
                    session = self.client.create_plan_session(base_filename, mega_prompt)
                    if session:
                        break
                    callback(lesson_title, "WARN", "Network error during create. Retrying in 10s...")
                    time.sleep(10)
                except APIBlockError as e:
                    self.abort_event.set()
                    callback(lesson_title, "API_BLOCKED", "API Quota/Limit Reached")
                    return False
                except Exception as e:
                    callback(lesson_title, "WARN", f"Error during create: {e}. Retrying in 10s...")
                    time.sleep(10)

            if not session:
                callback(lesson_title, "ERROR", "Session Creation Failed after retries")
                return False

            session_id = session.get("name")
            if self.state_manager:
                self.state_manager.update_lesson_data(lesson_title, {session_key: session_id})

        callback(lesson_title, "RUNNING", f"Monitoring Session ({session_id})...")

        # 5. Monitor Session
        # Define status callback for wait_for_completion
        def status_update(state):
            callback(lesson_title, "RUNNING", f"Status: {state}")

        status = self.client.wait_for_completion(
            session_id, timeout_minutes=45, status_callback=status_update
        )

        if status not in ["SUCCEEDED", "COMPLETED"]:
            callback(lesson_title, "FAILED", f"Session ended: {status}")
            return False

        # 6. Pull Result asynchronously to free up the thread for a new session immediately
        def bg_pull():
            callback(lesson_title, "PULLING", "Pulling Plan in background...")
            details = self.client.get_session_details(session_id)
            if not details:
                callback(lesson_title, "WARN", "No PR found. Manual check needed.")
                return

            target_path = f"plans/{filename}"

            def pr_callback(ignored_path, state, msg):
                callback(lesson_title, state, msg)

            success = self.client.finalize_pr_and_pull(details, target_path, callback=pr_callback)
            if success:
                callback(lesson_title, "SUCCESS", f"Plan saved: {filename}")
            else:
                callback(lesson_title, "ERROR", "Pull Failed")

        import threading
        t = threading.Thread(target=bg_pull, daemon=False)
        if not hasattr(self, "pull_threads"):
            self.pull_threads = []
        self.pull_threads.append(t)
        t.start()
        
        # We don't wait for bg_pull here to free the executor slot, 
        # but we will join it at the end of run_batch_planning.
        return True


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    planner = JulesPlanner()
    planner.run_batch_planning(max_concurrent=2)
