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
        self.architect_prompt = (self.project_root / "system workspace/Architect_GEM_MASTER.md").read_text(encoding='utf-8')
        self.auditor_prompt = (self.project_root / "system workspace/Architect_AUDITOR.md").read_text(encoding='utf-8')

        # Load Raw Text Index
        self.raw_text_path = self.project_root / "system workspace/text-data/full_raw_indexed.txt"
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

    def process_lesson(self, lesson_title, range_info):
        """
        Worker function for a single lesson.
        1. Extract text.
        2. Create Session.
        3. Wait for Completion.
        4. Pull Plan.
        """
        lesson_number = self.tp.get_lesson_number(lesson_title)
        clean_title = re.sub(r'^\d+\s*-\s*', '', lesson_title).strip()
        filename = f"{lesson_number}-{clean_title}-plan.md"

        print(f"🚀 [Start] {lesson_title}...")

        # 1. Extract Text
        raw_text = self._extract_lesson_text(range_info['start'], range_info['end'])
        if not raw_text:
            print(f"❌ [Error] No text found for {lesson_title}")
            return False

        # 2. Construct Prompt
        lesson_data = {
            'number': lesson_number,
            'title': clean_title,
            'raw_text': raw_text
        }

        mega_prompt = self.client.construct_mega_prompt(
            lesson_data,
            self.architect_prompt,
            self.auditor_prompt
        )

        # 3. Create Session
        session = self.client.create_plan_session(lesson_title, mega_prompt)
        if not session:
            return False

        session_id = session.get('name')

        # 4. Monitor Session
        status = self.client.wait_for_completion(session_id, timeout_minutes=20)

        if status != "SUCCEEDED":
            print(f"❌ [Failed] Session {session_id} ended with status: {status}")
            return False

        # 5. Pull Result
        details = self.client.get_session_details(session_id)
        if not details:
            print(f"⚠️ [Warning] Could not find branch/PR for {session_id}. Manual check required.")
            return False

        success = self.client.pull_plan_from_github(details, filename)

        if success:
            print(f"✅ [Complete] Plan saved: {filename}")
            return True
        else:
            print(f"❌ [Error] Failed to pull plan for {lesson_title}")
            return False

    def run_batch_planning(self, max_concurrent=5):
        """
        Main entry point. Orchestrates the batch processing.
        """
        print(f"\n🧠 Starting Jules Batch Planning (Max Concurrent: {max_concurrent})...")

        # 1. Get Lesson Index
        index_path = self.project_root / "system workspace/text-data/raw_to_lesson_index.json"
        if not index_path.exists():
            print("⚠️ Lesson index not found. Generating...")
            mapping = self.tp.generate_lesson_index()
        else:
            mapping = json.loads(index_path.read_text(encoding='utf-8'))

        if not mapping:
            print("❌ No lessons to process.")
            return

        # 2. Filter Processed Lessons?
        # Check if plan already exists
        to_process = {}
        for title, info in mapping.items():
            lesson_number = self.tp.get_lesson_number(title)
            clean_title = re.sub(r'^\d+\s*-\s*', '', title).strip()
            plan_path = self.project_root / f"plans/{lesson_number}-{clean_title}-plan.md"

            if plan_path.exists():
                print(f"⏭️ Skipping {title} (Plan exists)")
            else:
                to_process[title] = info

        if not to_process:
            print("✅ All plans already exist!")
            return

        print(f"📋 Processing {len(to_process)} lessons...")

        # 3. Execute Batch
        with ThreadPoolExecutor(max_workers=max_concurrent) as executor:
            future_to_lesson = {
                executor.submit(self.process_lesson, title, info): title
                for title, info in to_process.items()
            }

            for future in as_completed(future_to_lesson):
                title = future_to_lesson[future]
                try:
                    success = future.result()
                    status = "✅ Success" if success else "❌ Failed"
                    print(f"🏁 {status}: {title}")
                except Exception as exc:
                    print(f"💥 Exception processing {title}: {exc}")

if __name__ == "__main__":
    planner = JulesPlanner()
    planner.run_batch_planning(max_concurrent=2)
