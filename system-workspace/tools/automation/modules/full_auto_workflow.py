import os
import time
import shutil
import logging
import re
from pathlib import Path
from datetime import datetime

# Import modules
from modules.text_processing import TextProcessor
from modules.github_utils import GithubClient
from modules.state_manager import StateManager
from modules.jules_planner import JulesPlanner
from modules.jules_page_generator import JulesPageGenerator
from modules.jules_ocr import JulesOCR

try:
    from .unified_flow import UnifiedProductionManager
except ImportError:
    pass

# Import Jules Workspace Tools (Assuming sys.path is set by system.py)
try:
    import id_manager
    import lint_pages
    import fix_exam_blocks
    import smart_replace_haam
    import smart_color_fixer
except ImportError:
    pass # Will be handled if missing during execution

class FullAutoWorkflow:
    def __init__(self, project_root, state_manager, console_callback=None):
        self.project_root = Path(project_root)
        self.state_manager = state_manager
        self.callback = console_callback
        self.github = GithubClient(token_path=self.project_root / "secrets/Github_Token.txt")
        self.repo_name = "ibrahim4433/book-arabic-grammer" # Hardcoded based on request

        self.archive_dir = self.project_root / "Archive"
        self.raw_dir = self.project_root / "system-workspace/text-data/raw"
        self.plans_dir = self.project_root / "plans"
        self.pages_dir = self.project_root / "pages"
        self.input_dir = self.project_root / "input"

        self.tp = TextProcessor()
        if (self.input_dir / "TOC.json").exists():
            try:
                import json
                self.toc = json.loads((self.input_dir / "TOC.json").read_text(encoding='utf-8'))
            except Exception as e:
                logging.error(f"Failed to load TOC: {e}")
                self.toc = {}
        else:
            self.toc = {}

        self.stats = {
            "archived_files": 0,
            "ocr_processed": 0,
            "plans_downloaded": 0,
            "pages_downloaded": 0,
            "missing_plans": [],
            "missing_pages": []
        }

        # Internal State
        self.existing_lessons = set()
        self.skip_archive = False

        # Step Definitions
        self.steps = [
            {"id": "ARCHIVE", "func": self._step_archive, "label": "Archive Old Files"},
            {"id": "OCR", "func": self._step_ocr, "label": "OCR Processing"},
            {"id": "RAW_PROC", "func": self._step_raw_processing, "label": "Raw Text Processing"},
            {"id": "CHECK_EXIST", "func": self._step_check_existing, "label": "Check Existing Pages"},
            # {"id": "PLAN_SYNC", "func": self._step_sync_plans, "label": "Sync Missing Plans"},
            # {"id": "PAGE_SYNC", "func": self._step_sync_pages, "label": "Sync Missing Pages"},
            {"id": "UNIFIED_GEN", "func": self._step_unified_production, "label": "Unified Generation"},
            {"id": "AUDIT", "func": self._step_audit, "label": "Audit & Verify"}
        ]

        self.current_step_index = 0

        # Initialize Timings
        self.step_timings = {}
        for s in self.steps:
            self.step_timings[s['id']] = {
                "status": "PENDING",
                "start_time": None,
                "end_time": None,
                "duration": 0.0
            }

    def _log(self, step, status, message):
        if self.callback:
            self.callback(step, status, message)
        else:
            # Fallback logging if no UI
            logging.info(f"[{step}] {status}: {message}")

    def get_steps(self):
        return self.steps

    def get_current_step_name(self):
        if 0 <= self.current_step_index < len(self.steps):
            return self.steps[self.current_step_index]['label']
        return "Finished"

    def jump_to_step(self, step_id_or_label):
        """Finds step by ID or Label and sets current index."""
        target_index = -1
        for i, step in enumerate(self.steps):
            if step['id'] == step_id_or_label or step['label'] == step_id_or_label:
                target_index = i
                break

        if target_index != -1:
            self.current_step_index = target_index

            # Mark previous steps as SKIPPED
            for i in range(target_index):
                prev_step_id = self.steps[i]['id']
                # Only mark as skipped if they weren't already successful
                if self.step_timings[prev_step_id]['status'] == "PENDING":
                    self.step_timings[prev_step_id]['status'] = "SKIPPED"

            # Reset target step
            step_id = self.steps[target_index]['id']
            self.step_timings[step_id]['status'] = "PENDING"
            self.step_timings[step_id]['start_time'] = None
            self.step_timings[step_id]['end_time'] = None
            self.step_timings[step_id]['duration'] = 0.0

            return True

        return False

    def redo_previous_step(self):
        """Moves index back to the previously completed step."""
        if self.current_step_index > 0:
            self.current_step_index -= 1
            step_id = self.steps[self.current_step_index]['id']
            self.step_timings[step_id]['status'] = "PENDING"
            return True
        return False

    def run(self, skip_archive=False):
        """
        Executes the full workflow.
        Can be called repeatedly; it continues from self.current_step_index.
        """
        self.skip_archive = skip_archive

        while self.current_step_index < len(self.steps):
            step_info = self.steps[self.current_step_index]
            step_id = step_info['id']

            # Start Timing
            self.step_timings[step_id]['start_time'] = time.time()
            self.step_timings[step_id]['status'] = "RUNNING"
            self._log(step_id, "START", f"Starting {step_info['label']}...")

            try:
                # Execute Function
                step_info['func']()

                # Success
                self.step_timings[step_id]['status'] = "SUCCESS"
                self._log(step_id, "SUCCESS", f"Finished {step_info['label']}")

            except KeyboardInterrupt:
                self.step_timings[step_id]['status'] = "PAUSED"
                # Calculate partial duration
                end = time.time()
                self.step_timings[step_id]['end_time'] = end
                self.step_timings[step_id]['duration'] = end - self.step_timings[step_id]['start_time']
                raise # Re-raise to let system.py handle the menu

            except Exception as e:
                self.step_timings[step_id]['status'] = "FAILED"
                self._log(step_id, "ERROR", str(e))
                # Stop execution on error? Or raise?
                # Raising allows the UI to catch it.
                end = time.time()
                self.step_timings[step_id]['end_time'] = end
                self.step_timings[step_id]['duration'] = end - self.step_timings[step_id]['start_time']
                raise e

            # End Timing
            end = time.time()
            self.step_timings[step_id]['end_time'] = end
            self.step_timings[step_id]['duration'] = end - self.step_timings[step_id]['start_time']

            # Move to next
            self.current_step_index += 1

            # Small pause between steps for UI clarity
            time.sleep(0.5)

        return self.stats

    def _step_archive(self):
        if self.skip_archive:
            self._log("ARCHIVE", "SKIP", "Skipping Archive as requested.")
            return

        self._log("ARCHIVE", "RUNNING", "Archiving old files...")
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        target_dir = self.archive_dir / timestamp
        target_dir.mkdir(parents=True, exist_ok=True)

        # Move Raw Text
        if self.raw_dir.exists():
            for f in self.raw_dir.glob("*.txt"):
                shutil.move(str(f), str(target_dir / f.name))
                self.stats["archived_files"] += 1

        # Move Plans
        if self.plans_dir.exists():
            for f in self.plans_dir.glob("*.md"):
                shutil.move(str(f), str(target_dir / f.name))
                self.stats["archived_files"] += 1

        self._log("ARCHIVE", "SUCCESS", f"Archived {self.stats['archived_files']} files to {target_dir.name}")

    def _step_ocr(self):
        self._log("OCR", "RUNNING", "Verifying Images & Running Jules OCR...")

        # Bridge callback for JulesOCR
        def ocr_callback(status, message):
            step_status = "RUNNING"
            if status == "SUCCESS": step_status = "SUCCESS"
            elif status == "FAILED": step_status = "FAILED"
            elif status == "WARN": step_status = "WARN"
            elif status == "ERROR": step_status = "ERROR"

            self._log("OCR", step_status, message)

        try:
            ocr = JulesOCR(self.project_root)
            ocr.run_ocr_batch(update_callback=ocr_callback)
        except Exception as e:
            self._log("OCR", "ERROR", f"JulesOCR Failed: {e}")
            raise e

        # Post-Processing: Update State Manager
        self._log("OCR", "RUNNING", "Updating State Manager for OCR files...")

        images = sorted(list(self.input_dir.glob("*.jpg")) +
                        list(self.input_dir.glob("*.png")) +
                        list(self.input_dir.glob("*.jpeg")))

        processed_count = 0
        self.raw_dir.mkdir(parents=True, exist_ok=True)

        for img in images:
            raw_path = self.raw_dir / f"raw_{img.stem}.txt"
            if raw_path.exists():
                processed_count += 1
                self.state_manager.update_lesson_status(f"Image_{img.stem}", "OCR_DONE", {"raw": str(raw_path)})

        self.stats["ocr_processed"] = processed_count
        self._log("OCR", "SUCCESS", f"OCR Complete. Verified {processed_count} raw files.")

    def _step_raw_processing(self):
        self._log("RAW_PROC", "RUNNING", "Raw Processing (Merge & Index)...")
        if not self.tp.validate_toc():
             raise Exception("TOC Validation Failed")

        merged_path = self.tp.merge_raw_text()
        if merged_path:
             self._log("RAW_PROC", "MERGE", f"Merged raw text to {merged_path.name}")

        mapping = self.tp.generate_lesson_index()
        if mapping:
             self._log("RAW_PROC", "INDEX", f"Generated Lesson Index ({len(mapping)} lessons)")

        self._log("RAW_PROC", "SUCCESS", "Raw Processing Complete.")

    def _step_check_existing(self):
        self._log("CHECK_EXIST", "RUNNING", "Checking existing pages...")
        self.existing_lessons = set() # Reset

        # Check pages folder
        if self.pages_dir.exists():
            for f in self.pages_dir.glob("*.html"):
                match = re.match(r'^(\d+)', f.name)
                if match:
                    num = match.group(1)
                    normalized_num = str(int(num))
                    if normalized_num in self.toc:
                        self.existing_lessons.add(normalized_num)
                        # self._log("CHECK_EXIST", "SKIP", f"Lesson {num} exists.") # Too spammy

        self._log("CHECK_EXIST", "SUCCESS", f"Found {len(self.existing_lessons)} completed lessons.")

    def _step_unified_production(self):
        # Refresh existing lessons to account for Sync steps
        self._step_check_existing()

        self._log("UNIFIED_GEN", "RUNNING", "Starting Unified Production Manager...")

        def bridge_callback(title, status, msg):
             log_status = status
             if status == "RUNNING": log_status = "RUNNING"
             elif status == "SUCCESS": log_status = "GEN"
             elif status == "FAILED": log_status = "WARN"
             elif status == "RETRY": log_status = "WARN"

             self._log("UNIFIED_GEN", log_status, f"{title}: {msg}")

        manager = UnifiedProductionManager(self.project_root, self.state_manager, callback=bridge_callback)
        manager.populate_queue(self.existing_lessons)
        manager.run()

        self._log("UNIFIED_GEN", "SUCCESS", "Unified Production Complete.")

    def _step_plan_generation(self):
        self._log("PLAN_GEN", "RUNNING", "Generating Plans (JulesPlanner)...")
        planner = JulesPlanner(self.project_root, state_manager=self.state_manager)

        def bridge_callback(title, status, msg):
            if status in ["ERROR", "FAILED"]:
                self._log("PLAN_GEN", "WARN", f"{title}: {msg}")
            elif status == "SUCCESS":
                self._log("PLAN_GEN", "GEN", f"{title}: Plan Generated")

        try:
            planner.run_batch_planning(
                max_concurrent=5,
                update_callback=bridge_callback,
                excluded_lessons=self.existing_lessons
            )
        except Exception as e:
            self._log("PLAN_GEN", "ERROR", f"Planner crashed: {e}")
            raise e

        self._log("PLAN_GEN", "SUCCESS", "Plan Generation Phase Complete.")

    def _step_sync_plans(self):
        self._log("PLAN_SYNC", "RUNNING", "Verifying & Syncing Plans...")

        # Get open PRs
        prs = self.github.list_pull_requests(self.repo_name, author="Jules")
        if not prs:
             self._log("PLAN_SYNC", "INFO", "No open PRs from Jules found. Checking general PRs...")
             prs = self.github.list_pull_requests(self.repo_name)

        for key, data in self.toc.items():
            if key in self.existing_lessons:
                continue

            # Check Local
            local_plan = None
            if self.plans_dir.exists():
                candidates = list(self.plans_dir.glob(f"{key}-*-plan.md"))
                if not candidates:
                    candidates = list(self.plans_dir.glob(f"{int(key):02d}-*-plan.md"))

                if candidates:
                    local_plan = candidates[0]

            if local_plan:
                continue

            # Check GitHub
            self._log("PLAN_SYNC", "FETCH", f"Searching GitHub for Plan {key}...")
            found = False
            for pr in prs:
                branch = pr['head']['ref']
                files = self.github.get_file_info(self.repo_name, "plans", branch)

                if files and isinstance(files, list):
                    for f in files:
                        if f['name'].startswith(f"{key}-") or f['name'].startswith(f"{int(key):02d}-"):
                            if f['name'].endswith("-plan.md"):
                                self._log("PLAN_SYNC", "DOWN", f"Downloading {f['name']}...")
                                local_path = self.plans_dir / f['name']
                                if self.github.download_file(f['download_url'], local_path):
                                    self.stats["plans_downloaded"] += 1
                                    self.state_manager.update_lesson_status(key, "PLAN_READY", {"plan": str(local_path)})
                                    found = True
                                    break
                if found:
                    break

            if not found:
                self.stats["missing_plans"].append(key)
                self._log("PLAN_SYNC", "MISS", f"Plan for {key} not found.")

        self._log("PLAN_SYNC", "SUCCESS", "Plan Sync Complete.")

    def _step_page_generation(self):
        self._log("PAGE_GEN", "RUNNING", "Generating Pages (JulesPageGenerator)...")
        generator = JulesPageGenerator(self.project_root)

        def bridge_callback(title, status, msg):
            if status in ["ERROR", "FAILED"]:
                self._log("PAGE_GEN", "WARN", f"{title}: {msg}")
            elif status == "SUCCESS":
                self._log("PAGE_GEN", "GEN", f"{title}: Page Generated")
            elif status == "INTERACT":
                self._log("PAGE_GEN", "INFO", f"{title}: Interact - {msg}")

        try:
            generator.run_batch_generation(
                max_concurrent=5,
                update_callback=bridge_callback,
                excluded_lessons=self.existing_lessons
            )
        except Exception as e:
            self._log("PAGE_GEN", "ERROR", f"Generator crashed: {e}")
            raise e

        self._log("PAGE_GEN", "SUCCESS", "Page Generation Phase Complete.")

    def _step_sync_pages(self):
        self._log("PAGE_SYNC", "RUNNING", "Verifying & Syncing Pages...")

        # Reuse PRs
        prs = self.github.list_pull_requests(self.repo_name, author="Jules")
        if not prs:
             prs = self.github.list_pull_requests(self.repo_name)

        for key, data in self.toc.items():
            if key in self.existing_lessons:
                continue

            self._log("PAGE_SYNC", "FETCH", f"Searching GitHub for Page {key}...")

            found = False
            for pr in prs:
                branch = pr['head']['ref']
                files = self.github.get_file_info(self.repo_name, "pages", branch)

                if files and isinstance(files, list):
                    for f in files:
                        if f['name'].startswith(f"{key}.") or f['name'].startswith(f"{int(key):02d}."):
                            if f['name'].endswith(".html"):
                                self._log("PAGE_SYNC", "DOWN", f"Downloading {f['name']}...")
                                local_path = self.pages_dir / f['name']
                                if self.github.download_file(f['download_url'], local_path):
                                    self.stats["pages_downloaded"] += 1
                                    self.state_manager.update_lesson_status(key, "PAGE_GENERATED", {"html": str(local_path)})
                                    found = True
                                    break
                if found:
                    break

            if not found:
                self.stats["missing_pages"].append(key)
                self._log("PAGE_SYNC", "MISS", f"Page for {key} not found.")

        self._log("PAGE_SYNC", "SUCCESS", "Page Sync Complete.")

    def _step_audit(self):
        self._log("AUDIT", "RUNNING", "Auditing & Verifying Pages...")

        pages_dir = self.pages_dir
        if not pages_dir.exists():
            self._log("AUDIT", "WARN", "Pages directory missing.")
            return

        # Define Exclusions
        excluded_files = {
            "00.0_blank_page1.html",
            "99.0_blank_page2.html",
            "00.1_n01_toc_p1.html",
            "00.2_n02_toc_p2.html"
        }
        excluded_folders = {"cover"}

        target_files = []
        for f in sorted(list(pages_dir.glob("**/*.html"))):
            rel_path = f.relative_to(pages_dir)
            if f.name in excluded_files: continue
            if any(part in excluded_folders for part in rel_path.parts): continue
            target_files.append(str(f))

        if not target_files:
            self._log("AUDIT", "WARN", "No files to audit.")
            return

        # 1. ID Manager
        try:
            self._log("AUDIT", "AUDIT", "Running ID Manager...")
            manager = id_manager.IDManager(root_dir=str(pages_dir))
            manager.auto_tag(files=target_files)
        except Exception as e:
            self._log("AUDIT", "ERROR", f"ID Manager failed: {e}")

        # 2. Fix Exam Blocks
        try:
            self._log("AUDIT", "AUDIT", "Fixing Exam Blocks...")
            for f in target_files:
                fix_exam_blocks.fix_exam_blocks(f)
        except Exception as e:
            self._log("AUDIT", "ERROR", f"Fix Exam Blocks failed: {e}")

        # 3. Smart Replace Haam
        try:
            self._log("AUDIT", "AUDIT", "Replacing Haam...")
            for f in target_files:
                smart_replace_haam.process_file(f)
        except Exception as e:
             self._log("AUDIT", "ERROR", f"Smart Replace Haam failed: {e}")

        # 4. Smart Color Fixer
        try:
            self._log("AUDIT", "AUDIT", "Fixing Colors...")
            for f in target_files:
                smart_color_fixer.fix_colors(f)
        except Exception as e:
            self._log("AUDIT", "ERROR", f"Color Fixer failed: {e}")

        # 5. Lint Pages
        try:
            self._log("AUDIT", "AUDIT", "Linting Pages...")
            allowed_classes = None
            styles_path = self.project_root / "styles/main.css"
            if styles_path.exists():
                try:
                    allowed_classes = lint_pages.parse_allowed_classes(str(styles_path))
                except: pass

            issues = 0
            for f in target_files:
                errs, warns = lint_pages.lint_file(f, allowed_classes)
                if errs: issues += 1

            if issues > 0:
                self._log("AUDIT", "WARN", f"Linting found errors in {issues} files.")
            else:
                self._log("AUDIT", "SUCCESS", "All files passed linting.")

        except Exception as e:
            self._log("AUDIT", "ERROR", f"Linting failed: {e}")

        self._log("AUDIT", "SUCCESS", "Audit & Verify Complete.")
