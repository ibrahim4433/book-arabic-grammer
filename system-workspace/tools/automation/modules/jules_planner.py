import sys
import json
import time
import re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# Ensure modules are importable
sys.path.append(str(Path(__file__).parent))

from jules_client_plans import JulesPlanClient
from text_processing import TextProcessor

class JulesPlanner:
    """
    Orchestrates the batch generation of plans using Jules Sessions.
    """

    def __init__(self, project_root=None):
        self.project_root = Path(project_root) if project_root else Path(__file__).parent.parent.parent.parent.parent
        self.client = JulesPlanClient(project_root=self.project_root)
        self.tp = TextProcessor(project_root=self.project_root)

        # Load Prompts
        self.architect_prompt = (self.project_root / "system-workspace/Architect_GEM_MASTER.md").read_text(encoding='utf-8')
        self.auditor_prompt = (self.project_root / "system-workspace/Architect_AUDITOR.md").read_text(encoding='utf-8')

        # Load Raw Text Index
        self.raw_text_path = self.project_root / "system-workspace/text-data/full_raw_indexed.txt"
        if not self.raw_text_path.exists():
            print("⚠️ Raw text index missing. Generating...")
            self.tp.merge_raw_text()

        self.raw_lines = self.raw_text_path.read_text(encoding='utf-8').splitlines()

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
                clean_line = re.sub(r'^\[.*?\]\s*', '', line)
                extracted.append(clean_line)

            if end_pattern in line:
                capturing = False
                break

        return "\n".join(extracted)

    def run_batch_planning(self, max_concurrent=5, update_callback=None):
        """
        Main entry point. Orchestrates the batch processing.
        Args:
            update_callback (callable): Function(lesson_title, status, message)
        """
        if not update_callback:
            def update_callback(title, status, msg): print(f"[{status}] {title}: {msg}")

        print(f"\n🧠 Starting Jules Batch Planning (Max Concurrent: {max_concurrent})...")

        # 1. Get Lesson Index
        index_path = self.project_root / "system-workspace/text-data/raw_to_lesson_index.json"
        if not index_path.exists():
            update_callback("System", "WARN", "Lesson index missing. Generating...")
            mapping = self.tp.generate_lesson_index()
        else:
            mapping = json.loads(index_path.read_text(encoding='utf-8'))

        if not mapping:
            update_callback("System", "ERROR", "No lessons to process.")
            return

        # 2. Filter Processed Lessons?
        to_process = {}
        for title, info in mapping.items():
            lesson_number = self.tp.get_lesson_number(title)
            clean_title = re.sub(r'^\d+\s*-\s*', '', title).strip()
            plan_path = self.project_root / f"plans/{lesson_number}-{clean_title}-plan.md"

            if plan_path.exists():
                update_callback(title, "SKIP", "Plan exists")
            else:
                to_process[title] = info
                update_callback(title, "PENDING", "Queued")

        if not to_process:
            update_callback("System", "DONE", "All plans exist.")
            return

        # 3. Execute Batch
        with ThreadPoolExecutor(max_workers=max_concurrent) as executor:
            future_to_lesson = {
                executor.submit(self.process_lesson_with_callback, title, info, update_callback): title
                for title, info in to_process.items()
            }
            
            for future in as_completed(future_to_lesson):
                pass # The callback handles updates inside the future

    def process_lesson_with_callback(self, lesson_title, range_info, callback):
        """Wrapper for process_lesson that uses callback."""
        callback(lesson_title, "RUNNING", "Starting...")
        try:
            # Re-implement process_lesson logic here but with callbacks?
            # Or just call self.process_lesson and modify it to accept callback?
            # Better to modify process_lesson signature.
            self.process_lesson(lesson_title, range_info, callback)
        except Exception as e:
            callback(lesson_title, "ERROR", str(e))

    def process_lesson(self, lesson_title, range_info, callback=None):
        """
        Worker function for a single lesson.
        """
        if not callback: callback = lambda t, s, m: print(f"[{s}] {t}: {m}")
        
        # Attempt to parse number and title from the lesson_title (which is a key from index)
        match = re.match(r'^(\d+)\s*-\s*(.*)', lesson_title)
        if match:
            # Found "9 - Title"
            inferred_number = match.group(1).zfill(2)
            clean_title = match.group(2).strip()
            lesson_number = inferred_number
        else:
            # Fallback for "Title" only
            clean_title = lesson_title.strip()
            lesson_number = self.tp.get_lesson_number(clean_title)

        filename = f"{lesson_number}-{clean_title}-plan.md"

        callback(lesson_title, "RUNNING", "Extracting Text...")

        # 1. Extract Text
        raw_text = self._extract_lesson_text(range_info['start'], range_info['end'])
        if not raw_text:
            callback(lesson_title, "ERROR", "No text found")
            return False

        # 2. Get Metadata from TOC.json
        lesson_metadata = {}
        if self.tp.toc_path.exists():
            try:
                toc_data = json.loads(self.tp.toc_path.read_text(encoding='utf-8'))
                # Try to find by number (stripping leading zeros if key is integer-like string)
                key = str(int(lesson_number)) if lesson_number.isdigit() else lesson_number
                if key in toc_data:
                    lesson_metadata = toc_data[key]
                else:
                    # Fallback: search by title
                    for k, v in toc_data.items():
                         if v.get('title', '').strip() == clean_title:
                             lesson_metadata = v
                             break
            except Exception:
                pass

        # 3. Construct Prompt
        lesson_data = {
            'number': lesson_number,
            'title': clean_title,
            'raw_text': raw_text,
            'level': lesson_metadata.get('level', ''),
            'unit': lesson_metadata.get('Unit', ''),
            'author': lesson_metadata.get('author', ''),
            'author_number': lesson_metadata.get('author_number', '')
        }
        mega_prompt = self.client.construct_mega_prompt(
            lesson_data, self.architect_prompt, self.auditor_prompt
        )

        # 4. Create Session
        callback(lesson_title, "RUNNING", "Creating Session...")
        session = self.client.create_plan_session(lesson_title, mega_prompt)
        if not session:
            callback(lesson_title, "ERROR", "Session Creation Failed")
            return False

        session_id = session.get('name')
        callback(lesson_title, "RUNNING", f"Monitoring Session ({session_id})...")

        # 5. Monitor Session
        # We need to poll inside here and update callback occasionally
        # But wait_for_completion blocks. Let's modify wait_for_completion to accept callback?
        # Or just wait.
        status = self.client.wait_for_completion(session_id, timeout_minutes=20)

        if status != "SUCCEEDED":
            callback(lesson_title, "FAILED", f"Session ended: {status}")
            return False

        # 6. Pull Result
        callback(lesson_title, "RUNNING", "Pulling Plan...")
        details = self.client.get_session_details(session_id)
        if not details:
            callback(lesson_title, "WARN", "No PR found. Manual check needed.")
            return False

        success = self.client.pull_plan_from_github(details, filename)

        if success:
            callback(lesson_title, "SUCCESS", f"Plan saved: {filename}")
            return True
        else:
            callback(lesson_title, "ERROR", "Pull Failed")
            return False


if __name__ == "__main__":
    planner = JulesPlanner()
    planner.run_batch_planning(max_concurrent=2)
