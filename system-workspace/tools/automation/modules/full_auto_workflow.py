import os
import time
import shutil
import logging
import re
from pathlib import Path
from datetime import datetime

# Import modules
from modules.vision import VisionClient
from modules.text_processing import TextProcessor
from modules.github_utils import GithubClient
from modules.state_manager import StateManager

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

    def _log(self, step, status, message):
        if self.callback:
            self.callback(step, status, message)
        else:
            print(f"[{step}] {status}: {message}")

    def run(self, skip_archive=False):
        """
        Executes the full workflow: Archive -> OCR -> Check Local -> Sync Plans -> Sync Pages -> Report.
        Raises KeyboardInterrupt for pause handling in the main loop.
        """
        try:
            # Step A: Archive
            if not skip_archive:
                self._step_archive()

            # Step B: OCR
            self._step_ocr()

            # Step C: Raw Processing (Merge & Index)
            self._step_raw_processing()

            # Step Check: Exclude existing pages (User logic)
            existing_lessons = self._step_check_existing()

            # Step E: Verify/Sync Plans
            self._step_sync_plans(existing_lessons)

            # Step F: Verify/Sync Pages
            self._step_sync_pages(existing_lessons)

            # Step G: Audit & Verify
            self._step_audit()

            # Report handled by caller or returned here
            return self.stats

        except KeyboardInterrupt:
            raise
        except Exception as e:
            logging.error(f"Workflow Error: {e}")
            self._log("ERROR", "FAILED", str(e))
            raise

    def _step_archive(self):
        self._log("Step A", "RUNNING", "Archiving old files...")
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

        self._log("Step A", "SUCCESS", f"Archived {self.stats['archived_files']} files to {target_dir.name}")
        time.sleep(1) # Visual pause

    def _step_ocr(self):
        self._log("Step B", "RUNNING", "Verifying Images & Running OCR...")
        vision = VisionClient()
        images = sorted(list(self.input_dir.glob("*.jpg")) + list(self.input_dir.glob("*.png")))

        self.raw_dir.mkdir(parents=True, exist_ok=True)

        for img in images:
            raw_path = self.raw_dir / f"raw_{img.stem}.txt"
            if not raw_path.exists():
                self._log("Step B", "OCR", f"Processing {img.name}...")
                text = vision.extract_text([img])
                if text:
                    raw_path.write_text(text, encoding='utf-8')
                    self.stats["ocr_processed"] += 1
                    self.state_manager.update_lesson_status(f"Image_{img.stem}", "OCR_DONE", {"raw": str(raw_path)})
                else:
                    self._log("Step B", "WARN", f"Failed to OCR {img.name}")
            else:
                 # Already exists (should not happen if archived, unless OCR failed before)
                 pass

        self._log("Step B", "SUCCESS", f"OCR Complete. Processed {self.stats['ocr_processed']} images.")
        time.sleep(1)

    def _step_raw_processing(self):
        self._log("Step C", "RUNNING", "Raw Processing (Merge & Index)...")
        if not self.tp.validate_toc():
             self._log("Step C", "ERROR", "TOC Validation Failed")
             return

        merged_path = self.tp.merge_raw_text()
        if merged_path:
             self._log("Step C", "MERGE", f"Merged raw text to {merged_path.name}")

        mapping = self.tp.generate_lesson_index()
        if mapping:
             self._log("Step C", "INDEX", f"Generated Lesson Index ({len(mapping)} lessons)")

        self._log("Step C", "SUCCESS", "Raw Processing Complete.")
        time.sleep(1)

    def _step_check_existing(self):
        self._log("Step Check", "RUNNING", "Checking existing pages...")
        existing_lessons = set()

        # Map TOC to lesson numbers
        lesson_map = {} # number -> title
        for key, data in self.toc.items():
            lesson_map[key] = data['title']

        # Check pages folder
        if self.pages_dir.exists():
            for f in self.pages_dir.glob("*.html"):
                # Extract number from filename (e.g., "09.0_Title.html")
                match = re.match(r'^(\d+)', f.name)
                if match:
                    num = match.group(1)
                    # Use str(int(num)) to normalize "09" -> "9" to match TOC keys
                    normalized_num = str(int(num))
                    if normalized_num in self.toc:
                        existing_lessons.add(normalized_num)
                        self._log("Step C", "SKIP", f"Lesson {num} exists (Page found).")

        self._log("Step C", "SUCCESS", f"Found {len(existing_lessons)} completed lessons.")
        time.sleep(1)
        return existing_lessons

    def _step_sync_plans(self, existing_lessons):
        self._log("Step E", "RUNNING", "Verifying & Syncing Plans...")

        # Get open PRs once
        prs = self.github.list_pull_requests(self.repo_name, author="Jules")
        if not prs:
             self._log("Step E", "INFO", "No open PRs from Jules found. Checking general PRs...")
             prs = self.github.list_pull_requests(self.repo_name) # Fallback to all PRs

        for key, data in self.toc.items():
            if key in existing_lessons:
                continue

            lesson_title = data['title']
            # Expected filename pattern: "{key}-{title}-plan.md" or similar
            # Since title might vary in cleaning, we look for "{key}-*-plan.md"

            # Check Local
            local_plan = None
            if self.plans_dir.exists():
                candidates = list(self.plans_dir.glob(f"{key}-*-plan.md"))
                # Also try 0 padded
                if not candidates:
                    candidates = list(self.plans_dir.glob(f"{int(key):02d}-*-plan.md"))

                if candidates:
                    local_plan = candidates[0]

            if local_plan:
                self._log("Step E", "EXIST", f"Plan for {key} exists.")
                continue

            # Check GitHub
            self._log("Step E", "FETCH", f"Searching GitHub for Plan {key}...")

            # We search for a file starting with the lesson number in "plans/" directory
            # Since we don't know the exact title, we might need to list files in PRs?
            # find_file_in_prs expects a filename.
            # I need a way to find by pattern.
            # But github_utils.find_file_in_prs takes exact filename.
            # I will iterate PRs and list files in "plans/" folder to match pattern.

            found = False
            for pr in prs:
                branch = pr['head']['ref']
                files = self.github.get_file_info(self.repo_name, "plans", branch)

                if files and isinstance(files, list):
                    for f in files:
                        if f['name'].startswith(f"{key}-") or f['name'].startswith(f"{int(key):02d}-"):
                            if f['name'].endswith("-plan.md"):
                                # Found match
                                self._log("Step E", "DOWN", f"Downloading {f['name']}...")
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
                self._log("Step E", "MISS", f"Plan for {key} not found.")

        self._log("Step E", "SUCCESS", "Plan Sync Complete.")

    def _step_sync_pages(self, existing_lessons):
        self._log("Step F", "RUNNING", "Verifying & Syncing Pages...")

        # Reuse PRs (should optimize to not fetch again, but for now simple call)
        prs = self.github.list_pull_requests(self.repo_name, author="Jules")
        if not prs:
             prs = self.github.list_pull_requests(self.repo_name)

        for key, data in self.toc.items():
            if key in existing_lessons:
                continue

            # If we are here, page is missing locally (checked in Step C).

            self._log("Step F", "FETCH", f"Searching GitHub for Page {key}...")

            found = False
            for pr in prs:
                branch = pr['head']['ref']
                files = self.github.get_file_info(self.repo_name, "pages", branch)

                if files and isinstance(files, list):
                    for f in files:
                        if f['name'].startswith(f"{key}.") or f['name'].startswith(f"{int(key):02d}."):
                            if f['name'].endswith(".html"):
                                # Found match
                                self._log("Step F", "DOWN", f"Downloading {f['name']}...")
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
                self._log("Step F", "MISS", f"Page for {key} not found.")

        self._log("Step F", "SUCCESS", "Page Sync Complete.")

    def _step_audit(self):
        self._log("Step G", "RUNNING", "Auditing & Verifying Pages...")

        pages_dir = self.pages_dir
        if not pages_dir.exists():
            self._log("Step G", "WARN", "Pages directory missing.")
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
            self._log("Step G", "WARN", "No files to audit.")
            return

        # 1. ID Manager
        try:
            self._log("Step G", "AUDIT", "Running ID Manager...")
            manager = id_manager.IDManager(root_dir=str(pages_dir))
            manager.auto_tag(files=target_files)
        except Exception as e:
            self._log("Step G", "ERROR", f"ID Manager failed: {e}")

        # 2. Fix Exam Blocks
        try:
            self._log("Step G", "AUDIT", "Fixing Exam Blocks...")
            for f in target_files:
                fix_exam_blocks.fix_exam_blocks(f)
        except Exception as e:
            self._log("Step G", "ERROR", f"Fix Exam Blocks failed: {e}")

        # 3. Smart Replace Haam
        try:
            self._log("Step G", "AUDIT", "Replacing Haam...")
            for f in target_files:
                smart_replace_haam.process_file(f)
        except Exception as e:
             self._log("Step G", "ERROR", f"Smart Replace Haam failed: {e}")

        # 4. Smart Color Fixer
        try:
            self._log("Step G", "AUDIT", "Fixing Colors...")
            for f in target_files:
                smart_color_fixer.fix_colors(f)
        except Exception as e:
            self._log("Step G", "ERROR", f"Color Fixer failed: {e}")

        # 5. Lint Pages
        try:
            self._log("Step G", "AUDIT", "Linting Pages...")
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
                self._log("Step G", "WARN", f"Linting found errors in {issues} files.")
            else:
                self._log("Step G", "SUCCESS", "All files passed linting.")

        except Exception as e:
            self._log("Step G", "ERROR", f"Linting failed: {e}")

        self._log("Step G", "SUCCESS", "Audit & Verify Complete.")
