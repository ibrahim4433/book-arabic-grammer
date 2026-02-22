import time
import logging
import threading
import re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

from .jules_planner import JulesPlanner
from .jules_page_generator import JulesPageGenerator

class UnifiedProductionManager:
    """
    Manages concurrent generation of Plans and Pages using a unified task queue.
    """
    def __init__(self, project_root, state_manager, callback=None):
        self.project_root = Path(project_root)
        self.state_manager = state_manager
        self.callback = callback or (lambda t, s, m: logging.info(f"[{s}] {t}: {m}"))

        self.planner = JulesPlanner(project_root, state_manager=state_manager)
        self.generator = JulesPageGenerator(project_root)

        self.queue = [] # list of tasks: {'type': 'PLAN'|'PAGE', 'id': str, 'info': dict, 'retries': 0}
        self.active_futures = set()
        self.lock = threading.Lock()

        self.stop_event = threading.Event()
        self.max_retries = 999  # Effectively infinite as requested ("untill no remaining things")

    def _log(self, title, status, message):
        self.callback(title, status, message)

    def populate_queue(self, existing_lessons):
        """
        Scans for missing items and populates the initial queue.
        """
        self._log("System", "INFO", "Scanning for missing Plans and Pages...")

        # 1. Identify Missing Plans
        index_path = self.project_root / "system-workspace/text-data/raw_to_lesson_index.json"

        # If index missing, try to generate it via Planner's TextProcessor
        if not index_path.exists():
            self.planner.tp.generate_lesson_index()

        if index_path.exists():
            import json
            mapping = json.loads(index_path.read_text(encoding='utf-8'))

            for title, info in mapping.items():
                lesson_number = self.planner.tp.get_lesson_number(title)

                # Check if excluded (page exists already)
                if lesson_number in existing_lessons or str(int(lesson_number)) in existing_lessons:
                    continue

                clean_title = re.sub(r'^\d+\s*-\s*', '', title).strip()
                plan_filename = f"{lesson_number}-{clean_title}-plan.md"
                plan_path = self.project_root / "plans" / plan_filename

                if not plan_path.exists():
                    self.queue.append({
                        'type': 'PLAN',
                        'id': title, # Lesson Title used by planner
                        'info': info,
                        'retries': 0
                    })
                else:
                    # Plan exists, check Page
                    # Page filename usually matches plan stem
                    # But verify via generator logic if possible, or just queue it
                    # If page existed, it would be in existing_lessons
                    # So if we are here, page is missing

                    self.queue.append({
                        'type': 'PAGE',
                        'id': plan_path.stem, # Plan filename stem
                        'info': {'plan_path': plan_path},
                        'retries': 0
                    })
        else:
            self._log("System", "ERROR", "Could not load Lesson Index.")

        self._log("System", "INFO", f"Queued {len(self.queue)} initial tasks.")

    def run(self):
        max_workers = 5
        last_status_log = time.time()

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            while not self.stop_event.is_set():
                with self.lock:
                    # Periodic Status Log (Every 60s)
                    if time.time() - last_status_log > 60:
                        self._log("System", "INFO", f"Status: {len(self.queue)} tasks pending, {len(self.active_futures)} active workers.")
                        last_status_log = time.time()

                    # Check if done: No tasks in queue AND no active futures
                    if not self.queue and not self.active_futures:
                        self._log("System", "SUCCESS", "All tasks completed.")
                        break

                    # Submit tasks up to limit
                    while len(self.active_futures) < max_workers and self.queue:
                        task = self.queue.pop(0)
                        future = executor.submit(self.process_task, task)
                        self.active_futures.add(future)

                # Monitor futures
                # We copy the set to iterate safely
                current_futures = list(self.active_futures)
                for f in current_futures:
                    if f.done():
                        with self.lock:
                            self.active_futures.remove(f)

                        try:
                            result = f.result()
                            status, next_task = result

                            if status == "SUCCESS" and next_task:
                                with self.lock:
                                    self.queue.insert(0, next_task) # Prioritize next step

                            elif status == "RETRY" and next_task:
                                with self.lock:
                                    self.queue.append(next_task) # Re-queue at end

                        except Exception as e:
                            logging.error(f"Critical Task Error: {e}")

                time.sleep(1) # prevent busy loop

    def process_task(self, task):
        task_type = task['type']
        task_id = task['id']
        retries = task['retries']

        try:
            if task_type == 'PLAN':
                # Run Planner
                def plan_cb(t, s, m):
                    self._log(t, s, m)

                # Check max retries
                if retries > self.max_retries:
                    self._log(task_id, "FAILED", "Max retries exceeded.")
                    return ("FAILED", None)

                success = self.planner.process_lesson(task_id, task['info'], callback=plan_cb)

                if success:
                    # Infer plan path to create PAGE task
                    match = re.match(r'^(\d+)\s*-\s*(.*)', task_id)
                    if match:
                        num = match.group(1).zfill(2)
                        title = match.group(2).strip()
                    else:
                        title = task_id.strip()
                        num = self.planner.tp.get_lesson_number(title)

                    plan_filename = f"{num}-{title}-plan.md"
                    plan_path = self.project_root / "plans" / plan_filename

                    if plan_path.exists():
                        next_task = {
                            'type': 'PAGE',
                            'id': plan_path.stem,
                            'info': {'plan_path': plan_path},
                            'retries': 0
                        }
                        return ("SUCCESS", next_task)
                    else:
                        self._log(task_id, "ERROR", "Plan success reported but file missing.")
                        return ("FAILED", None)

                else:
                    # Failed
                    delay = 30 # wait 30s before retry
                    self._log(task_id, "WARN", f"Plan failed. Retrying in {delay}s...")
                    time.sleep(delay)
                    task['retries'] += 1
                    return ("RETRY", task)

            elif task_type == 'PAGE':
                # Run Page Generator
                plan_path = task['info']['plan_path']

                def page_cb(t, s, m):
                    self._log(t, s, m)

                if retries > self.max_retries:
                    self._log(task_id, "FAILED", "Max retries exceeded.")
                    return ("FAILED", None)

                success = self.generator.process_plan(plan_path, callback=page_cb)

                if success:
                    return ("SUCCESS", None)
                else:
                     delay = 30
                     self._log(task_id, "WARN", f"Page failed. Retrying in {delay}s...")
                     time.sleep(delay)
                     task['retries'] += 1
                     return ("RETRY", task)

        except Exception as e:
            self._log(task_id, "ERROR", f"Worker Exception: {e}")
            time.sleep(10)
            task['retries'] += 1
            return ("RETRY", task)

        return ("FAILED", None)
