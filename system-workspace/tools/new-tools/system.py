#!/usr/bin/env python3
import logging
import re
import subprocess
import sys
import threading
import time
import datetime
import string
import random
from pathlib import Path

# --- RICH & UI IMPORTS ---
try:
    import questionary
    from rich import box
    from rich.columns import Columns
    from rich.console import Console, Group
    from rich.layout import Layout
    from rich.live import Live
    from rich.panel import Panel
    from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn
    from rich.table import Table
except ImportError:
    print("❌ Missing UI libraries. Please run: pip install rich questionary")
    sys.exit(1)

try:
    import arabic_reshaper
    from bidi.algorithm import get_display
    def fix_arabic(text):
        if not text: return text
        try:
            return get_display(arabic_reshaper.reshape(str(text)))
        except:
            return text
except ImportError:
    def fix_arabic(text):
        return text

# --- CONFIGURATION ---
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
MODULES_PATH = PROJECT_ROOT / "system-workspace/tools/automation"
JULES_WORKSPACE_PATH = PROJECT_ROOT / "Jules-workspace"
sys.path.append(str(MODULES_PATH))
sys.path.append(str(JULES_WORKSPACE_PATH))

from collections import deque

# --- LOGGING SETUP ---
# Redirect logs to file so they don't break the UI
logging.basicConfig(
    filename="system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w",
)


class UILogHandler(logging.Handler):
    def __init__(self, maxlen=6):
        super().__init__()
        self.log_messages = deque(maxlen=maxlen)

    def emit(self, record):
        msg = self.format(record)
        self.log_messages.append(msg)


ui_log_handler = UILogHandler(maxlen=15)
ui_log_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%H:%M:%S")
)
logging.getLogger().addHandler(ui_log_handler)


def generate_log_panel():
    log_text = "\n".join(ui_log_handler.log_messages)
    if not log_text:
        log_text = "[dim]No logs yet...[/dim]"
    return Panel(
        log_text,
        title="[bold dim]Verbose System Logs[/bold dim]",
        style="dim",
        border_style="green",
        box=box.ROUNDED,
    )


# --- MODULE IMPORTS ---
try:
    from modules.full_auto_workflow import FullAutoWorkflow
    from modules.jules_ocr import JulesOCR
    from modules.jules_page_generator import JulesPageGenerator
    from modules.jules_planner import JulesPlanner
    from modules.planner import Planner
    from modules.state_manager import StateManager
    from modules.text_processing import TextProcessor
    from modules.vision import VisionClient
    from modules.youtube_ui import run_jules_youtube_ui
    from modules.calibration_workflow import run_calibration_ui
except ImportError as e:
    logging.critical(f"Failed to import modules: {e}")
    print("❌ Critical Error: Failed to import modules. See system.log for details.")
    sys.exit(1)

# Import Jules Workspace Tools
id_manager = None
lint_pages = None
fix_exam_blocks = None
smart_replace_haam = None
smart_color_fixer = None

try:
    import id_manager
except ImportError:
    pass
try:
    import lint_pages
except ImportError:
    pass
try:
    import fix_exam_blocks
except ImportError:
    pass
try:
    import smart_replace_haam
except ImportError:
    pass
try:
    import smart_color_fixer
except ImportError:
    pass

console = Console(file=sys.stdout)

# --- TIMING UTILS ---


def format_duration(seconds):
    """Formats seconds into a human-readable string (e.g., '2m 15s', '45.2s')."""
    if seconds >= 60:
        minutes = int(seconds // 60)
        secs = int(seconds % 60)
        return f"{minutes}m {secs}s"
    else:
        return f"{seconds:.1f}s"


class Timer:
    """Context manager to measure execution time."""

    def __init__(self):
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()

    @property
    def duration(self):
        if self.start_time is None:
            return 0
        if self.end_time is None:
            return time.time() - self.start_time
        return self.end_time - self.start_time

    @property
    def formatted_duration(self):
        return format_duration(self.duration)


# --- UI HELPERS ---


class StreamLogger:
    """Redirects writes to a logger."""

    def __init__(self, logger, level=logging.INFO):
        self.logger = logger
        self.level = level

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.logger.log(self.level, line.rstrip())

    def flush(self):
        pass


def print_header():
    console.clear()
    settings_file = PROJECT_ROOT / "system-workspace" / "settings.json"
    workspace_code = "None"
    import json
    if settings_file.exists():
        try:
            with open(settings_file, encoding="utf-8") as f:
                settings = json.load(f)
                workspace_code = settings.get("workspace_code", "None")
        except:
            pass

    console.print(
        Panel.fit(
            "[bold cyan]📘 ARABIC GRAMMAR BOOK - CONTROL ROOM (V3)[/bold cyan]\n"
            f"[dim]Project Root: {PROJECT_ROOT}[/dim]\n"
            f"[bold yellow]Workspace Code: {workspace_code}[/bold yellow]",
            box=box.ROUNDED,
            border_style="cyan",
        )
    )


def display_status_table(state_manager):
    """
    Displays a consolidated status table using rich.
    """
    table = Table(title="Project Status", box=box.SIMPLE, expand=True)
    table.add_column("ID", style="cyan", width=5)
    table.add_column("Lesson Title", style="bold white")
    table.add_column("Status", style="magenta")
    table.add_column("Artifacts", style="dim")
    table.add_column("Last Updated", style="green")

    data = state_manager.get_consolidated_state()

    # Sort by ID (numeric if possible)
    sorted_keys = sorted(data.keys(), key=lambda k: int(k) if k.isdigit() else 999)

    for key in sorted_keys:
        info = data[key]
        status = info.get("status", "UNKNOWN")
        files = info.get("files", {})

        # Determine artifacts icons
        artifacts = []
        if files.get("raw"):
            artifacts.append("📄 Raw")
        if files.get("plan"):
            artifacts.append(" Plan")
        if files.get("html"):
            artifacts.append("🌐 HTML")

        # Format timestamp
        ts = info.get("last_updated", 0)
        time_str = time.strftime("%H:%M", time.localtime(ts)) if ts else "-"

        # Try to extract title from key or original key if the key is just a number
        title = info.get("original_key", key)
        # Clean up title for display and fix RTL Arabic rendering
        clean_title = fix_arabic(re.sub(r"^\d+\s*-\s*", "", title).strip())
        if key.isdigit() and clean_title == key:
            clean_title = "Unknown Title"

        # Colorize Status
        status_style = "white"
        if "PASS" in status:
            status_style = "green"
        elif "READY" in status:
            status_style = "blue"
        elif "FAIL" in status:
            status_style = "red"

        table.add_row(
            key if key.isdigit() else "-",
            clean_title,
            f"[{status_style}]{status}[/{status_style}]",
            " ".join(artifacts),
            time_str,
        )

    console.print(table)


# --- WORKFLOW HANDLERS ---


def run_template_lint():
    console.print("\n[cyan]Running Pre-Flight Template Lint...[/cyan]")
    lint_script = PROJECT_ROOT / "Jules-workspace" / "lint_templates.py"
    if lint_script.exists():
        result = subprocess.run([sys.executable, str(lint_script)], capture_output=True, text=True)
        if result.returncode != 0:
            console.print("[red]❌ PRE-FLIGHT FAILED: Template bloat detected![/red]")
            console.print(result.stdout)
            return False
        console.print("[green]✅ Templates are clean.[/green]")
    return True


def smart_recover_hidden_plans(failed_lessons_data, project_root, console, is_pages=False):
    console.print("\n[cyan]🔍 Starting Smart Recovery Search in Local Folders...[/cyan]")
    search_dir = project_root / ("pages" if is_pages else "plans")
    extension = "*.html" if is_pages else "*.md"
    recovered = []

    for file_path in search_dir.rglob(extension):
        content = ""
        try:
            content = file_path.read_text(encoding="utf-8")
        except:
            pass

        for l_num, l_title, expected_path in failed_lessons_data:
            if l_num in recovered:
                continue

            target = project_root / expected_path
            if file_path == target:
                continue

            clean_t = re.sub(r"^\d+\s*-\s*", "", l_title).replace("-plan", "").strip()
            loose_t = re.sub(r"[^\w\s]", "", clean_t)
            loose_file = re.sub(r"[^\w\s]", "", file_path.name)

            if (
                (loose_t and loose_t in loose_file)
                or (clean_t and clean_t in file_path.name)
                or (clean_t and clean_t in content)
            ):
                console.print(
                    f"[green]✅ Found hidden plan for Lesson {l_num} at: {file_path.relative_to(project_root)}[/green]"
                )
                target = project_root / ("pages" if is_pages else "plans") / file_path.name
                import shutil

                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(file_path), str(target))
                recovered.append(l_num)
                break

    return recovered


def extract_from_pr_branches(failed_lessons_data, project_root, console, is_pages=False):
    if not failed_lessons_data:
        return []
    console.print("\n[cyan]🔍 Searching Local PR Branches...[/cyan]")
    recovered = []
    extension = ".html" if is_pages else ".md"
    try:
        branches_out = subprocess.check_output(
            ["git", "branch", "--list", "pr-*"], cwd=project_root, text=True
        )
        branches = [
            b.strip().replace("*", "").strip() for b in branches_out.splitlines() if b.strip()
        ]

        for branch in branches:
            diff_out = subprocess.check_output(
                ["git", "diff", "--name-only", f"main..{branch}"], cwd=project_root, text=True
            )
            files = [f.strip() for f in diff_out.splitlines() if f.strip().endswith(extension)]

            for f in files:
                for l_num, l_title, expected_path in failed_lessons_data:
                    if l_num in recovered:
                        continue
                    clean_t = re.sub(r"^\d+\s*-\s*", "", l_title).replace("-plan", "").strip()
                    loose_t = re.sub(r"[^\w\s]", "", clean_t)
                    loose_f = re.sub(r"[^\w\s]", "", f)

                    if (loose_t and loose_t in loose_f) or (clean_t and clean_t in f):
                        console.print(
                            f"[green]✅ Found plan for Lesson {l_num} inside hidden branch {branch}: {f}[/green]"
                        )
                        subprocess.run(
                            ["git", "checkout", branch, "--", f],
                            cwd=project_root,
                            check=True,
                            capture_output=True,
                        )
                        local_f = project_root / f
                        target = project_root / ("pages" if is_pages else "plans") / Path(f).name
                        if local_f != target:
                            target.parent.mkdir(exist_ok=True, parents=True)
                            import shutil

                            shutil.move(str(local_f), str(target))
                        recovered.append(l_num)
    except Exception as e:
        console.print(f"[red]Error searching branches: {e}[/red]")
    return recovered


def run_jules_planning_ui(state_manager, is_1_page_mode=False):
    console.clear()  # Clear screen for App-like feel
    mode_text = " (1-PAGE MODE)" if is_1_page_mode else ""
    console.print(f"[bold cyan]🚀 Starting Jules Batch Planning{mode_text}...[/bold cyan]")

    planner = JulesPlanner(PROJECT_ROOT, state_manager=state_manager, is_1_page_mode=is_1_page_mode)

    tasks = {}  # title -> {status, message, start_time, duration}
    lock = threading.Lock()

    def generate_table(full=False):
        table = Table(title="Planning Progress", box=box.ROUNDED, expand=True)
        table.add_column("Lesson", style="cyan")
        table.add_column("Status", style="bold")
        table.add_column("Message", style="dim", width=60)
        table.add_column("Duration", style="yellow", justify="right")

        def get_sort_key(item):
            title, data = item
            s = data["status"]
            if s == "RUNNING":
                return 0
            if s == "INTERACT":
                return 1
            if s in ["MERGING", "PULLING"]:
                return 2
            if s in ["ERROR", "FAILED"]:
                return 3
            return 4

        with lock:
            sorted_tasks = sorted(tasks.items(), key=get_sort_key)  # Stable sort by status

        skipped_count = 0
        success_count = 0

        for title, data in sorted_tasks:
            status = data["status"]
            status_color = "white"
            if status == "SUCCESS":
                status_color = "green"
            elif status == "FAILED":
                status_color = "red"
            elif status == "RUNNING":
                status_color = "yellow"
            elif status in ["MERGING", "PULLING"]:
                status_color = "magenta"

            # Calculate Duration
            duration_str = "-"
            if "duration" in data:
                duration_str = format_duration(data["duration"])
            elif "start_time" in data:
                duration_str = format_duration(time.time() - data["start_time"])

            if not full and status in ["SKIP", "SUCCESS"]:
                if status == "SKIP":
                    skipped_count += 1
                if status == "SUCCESS":
                    success_count += 1
                continue

            table.add_row(
                title, f"[{status_color}]{status}[/{status_color}]", data["message"], duration_str
            )

        if not full and (skipped_count > 0 or success_count > 0):
            table.add_row(
                "[dim]...[/dim]",
                "[dim]COMPLETED[/dim]",
                f"[dim]Hidden from Live View: {skipped_count} Skipped, {success_count} Success[/dim]",
                "-",
            )

        return table

    def generate_layout():
        layout = Table.grid(expand=True)
        layout.add_column(ratio=7)
        layout.add_column(ratio=3)
        layout.add_row(generate_table(), generate_log_panel())
        return layout

    # Initialize Live with the initial table
    existing_count = planner.count_existing_plans()
    force_remake = False
    if existing_count > 0:
        ans = questionary.confirm(f"Found {existing_count} existing plans. Do you want to RE-MAKE them? (No = Skip)").ask()
        force_remake = ans
        
    range_input = questionary.text("Lessons to process (e.g. '1-10', '5', '12,15' or 'ALL'):", default="ALL").ask()
    if range_input is None: return
    
    only_lessons = None
    if range_input.strip().upper() != "ALL":
        only_lessons = []
        for part in range_input.split(','):
            part = part.strip()
            if '-' in part:
                try:
                    s, e = map(int, part.split('-'))
                    only_lessons.extend([str(i).zfill(2) for i in range(s, e + 1)])
                    only_lessons.extend([str(i) for i in range(s, e + 1)]) # handle both padded and non-padded
                except:
                    pass
            elif part.isdigit():
                only_lessons.append(str(int(part)).zfill(2))
                only_lessons.append(str(int(part)))
                
    start_all = time.time()
    
    while True:
        with Live(generate_layout(), refresh_per_second=4, vertical_overflow="crop") as live:
    
            def callback(title, status, msg):
                with lock:
                    if title not in tasks:
                        tasks[title] = {}
    
                    tasks[title]["status"] = status
                    tasks[title]["message"] = msg
    
                    if status == "RUNNING":
                        if "start_time" not in tasks[title]:
                            tasks[title]["start_time"] = time.time()
                    elif status in ["SUCCESS", "FAILED", "SKIP", "WARN", "ERROR", "API_BLOCKED"]:
                        if "start_time" in tasks[title]:
                            tasks[title]["duration"] = time.time() - tasks[title]["start_time"]
                        else:
                            tasks[title]["duration"] = 0.0
    
                live.update(generate_layout())
    
            planner.run_batch_planning(max_concurrent=5, update_callback=callback, force_remake=force_remake, only_lessons=only_lessons)

        api_blocked = any(data.get("status") == "API_BLOCKED" for data in tasks.values())
        if api_blocked:
            console.print("[bold red]\n⚠️ Jules API Limit or Quota Reached![/bold red]")
            retry_choice = questionary.select(
                "API Block detected. What would you like to do?",
                choices=["1. Wait and Resume batch", "2. Stop and Exit batch"]
            ).ask()
            if retry_choice and retry_choice.startswith("1"):
                planner.abort_event.clear()
                for title, data in tasks.items():
                    if data.get("status") == "API_BLOCKED":
                        data["status"] = "PENDING"
                        data["message"] = "Retrying..."
                console.print("[yellow]Resuming batch...[/yellow]")
                time.sleep(2)
                continue
            else:
                break
        else:
            break

    total_duration = time.time() - start_all
    console.print(generate_table(full=True))
    console.print(
        f"[bold green]✅ Batch Planning Completed in {format_duration(total_duration)}![/bold green]"
    )

    # Identify Failed Tasks for Auto-Recovery
    failed_data = []
    with lock:
        for title, data in tasks.items():
            if data.get("status") in ["FAILED", "ERROR", "WARN"]:
                lesson_num = planner.tp.get_lesson_number(title)
                if lesson_num:
                    clean_t = re.sub(r"^\d+\s*-\s*", "", title).strip()
                    if getattr(planner, "is_1_page_mode", False):
                        expected_path = f"plans/page_{lesson_num}-plan.md"
                    else:
                        expected_path = f"plans/{lesson_num}-{clean_t}-plan.md"
                    failed_data.append((lesson_num, title, expected_path))

    failed_lessons = [d[0] for d in failed_data]

    if failed_data:
        console.print(
            f"\n[bold red]⚠️ {len(failed_lessons)} plans failed to generate or pull from PRs.[/bold red]"
        )
        console.print(f"Failed lessons: {', '.join(failed_lessons)}")

        choice = questionary.select(
            "How would you like to handle the failed plans?",
            choices=[
                "1. Smart Search & Auto-Recover (Search hidden folders and local PR branches)",
                "2. Regenerate them using new Jules sessions",
                "3. Show me how to check and fix them manually",
                "4. Skip for now",
            ],
        ).ask()

        if choice and choice.startswith("1"):
            rec1 = smart_recover_hidden_plans(failed_data, PROJECT_ROOT, console)
            rec2 = extract_from_pr_branches(
                [d for d in failed_data if d[0] not in rec1], PROJECT_ROOT, console
            )
            total_rec = rec1 + rec2
            if len(total_rec) == len(failed_lessons):
                console.print(
                    "[bold green]✅ All failed plans were successfully recovered![/bold green]"
                )
            else:
                console.print(
                    f"[yellow]⚠️ Recovered {len(total_rec)} out of {len(failed_lessons)} plans.[/yellow]"
                )
                still_failed = [d[0] for d in failed_data if d[0] not in total_rec]
                if still_failed:
                    console.print(f"Still missing: {', '.join(still_failed)}")
                    regen = questionary.confirm(
                        "Would you like to regenerate the remaining missing plans?"
                    ).ask()
                    if regen:
                        with lock:
                            tasks.clear()
                        if planner.state_manager:
                            for l_num, l_title, _ in failed_data:
                                if l_num in still_failed:
                                    planner.state_manager.update_lesson_data(
                                        l_title, {"session_id": None}
                                    )
                        with Live(
                            generate_layout(), refresh_per_second=4, vertical_overflow="crop"
                        ) as live:
                            planner.run_batch_planning(
                                max_concurrent=5,
                                update_callback=callback,
                                only_lessons=still_failed,
                            )

        elif choice and choice.startswith("2"):
            console.print("[cyan]Force-regenerating failed plans...[/cyan]")
            with lock:
                tasks.clear()
            if planner.state_manager:
                for l_num, l_title, _ in failed_data:
                    if l_num in failed_lessons:
                        planner.state_manager.update_lesson_data(l_title, {"session_id": None})
            with Live(generate_layout(), refresh_per_second=4, vertical_overflow="crop") as live:
                planner.run_batch_planning(
                    max_concurrent=5, update_callback=callback, only_lessons=failed_lessons
                )
            console.print("[bold green]✅ Recovery Completed![/bold green]")

        elif choice and choice.startswith("3"):
            console.print("\n[bold cyan]--- MANUAL RECOVERY GUIDE ---[/bold cyan]")
            console.print(
                "When Jules fails to merge a PR or places a file incorrectly, the files are downloaded to your local computer but hidden inside Git branches."
            )
            console.print("\n[yellow]Steps to manually recover:[/yellow]")
            console.print(
                "1. Find the PR branch name from `system.log` (e.g., [bold]pr-230[/bold])."
            )
            console.print("2. Switch to that branch in your terminal:")
            console.print("   [bold]git checkout pr-230[/bold]")
            console.print(
                "3. Look inside the [bold]plans/[/bold] folder or its subfolders (like [bold]plans/Archives/[/bold]) to find the misnamed file."
            )
            console.print(
                "4. Move or rename the file to exactly match the expected name (e.g., [bold]plans/03-عَلَاَّمَاتُ الْاِسْمِ-plan.md[/bold])."
            )
            console.print("5. Commit your changes and switch back to main:")
            console.print("   [bold]git add plans/[/bold]")
            console.print("   [bold]git commit -m 'Recovered plan'[/bold]")
            console.print("   [bold]git checkout main[/bold]")
            console.print("   [bold]git merge pr-230[/bold]")
            console.print("--------------------------------------\n")
            
    # Auto-Pull
    _settings_file = PROJECT_ROOT / "system-workspace/settings.json"
    _ws_code = None
    import json as _json
    if _settings_file.exists():
        try:
            with open(_settings_file, encoding="utf-8") as _f:
                _ws_code = _json.load(_f).get("workspace_code")
        except Exception:
            pass
    if planner.state_manager and _ws_code:
        auto_pull_jules_batch("plans", _ws_code)
    
    questionary.press_any_key_to_continue().ask()


def run_jules_generation_ui(state_manager, is_1_page_mode=False):
    console.clear()  # Clear screen for App-like feel

    if not run_template_lint():
        return

    mode_text = " (1-PAGE MODE)" if is_1_page_mode else ""
    console.print(f"[bold cyan]🚀 Starting Jules Page Generation{mode_text}...[/bold cyan]")

    generator = JulesPageGenerator(PROJECT_ROOT, state_manager=state_manager, is_1_page_mode=is_1_page_mode)

    tasks = {}
    lock = threading.Lock()

    def generate_table(full=False):
        table = Table(title="Generation Progress", box=box.ROUNDED, expand=True)
        table.add_column("Lesson", style="cyan")
        table.add_column("Status", style="bold")
        table.add_column("Details", style="dim", width=60)
        table.add_column("Duration", style="yellow", justify="right")

        with lock:
            sorted_tasks = sorted(tasks.items())

        skipped_count = 0
        success_count = 0

        for title, data in sorted_tasks:
            s = data["status"]
            color = "white"
            if s == "RUNNING":
                color = "yellow"
            elif s == "SUCCESS":
                color = "green"
            elif s == "FAILED":
                color = "red"
            elif s == "INTERACT":
                color = "magenta"
            elif s in ["MERGING", "PULLING"]:
                color = "cyan"

            # Calculate Duration
            duration_str = "-"
            if "duration" in data:
                duration_str = format_duration(data["duration"])
            elif "start_time" in data:
                duration_str = format_duration(time.time() - data["start_time"])

            if not full and s in ["SKIP", "SUCCESS"]:
                if s == "SKIP":
                    skipped_count += 1
                if s == "SUCCESS":
                    success_count += 1
                continue

            table.add_row(title, f"[{color}]{s}[/{color}]", data["message"], duration_str)

        if not full and (skipped_count > 0 or success_count > 0):
            table.add_row(
                "[dim]...[/dim]",
                "[dim]COMPLETED[/dim]",
                f"[dim]Hidden from Live View: {skipped_count} Skipped, {success_count} Success[/dim]",
                "-",
            )

        return table

    def generate_layout():
        layout = Table.grid(expand=True)
        layout.add_column(ratio=7)
        layout.add_column(ratio=3)
        layout.add_row(generate_table(), generate_log_panel())
        return layout

    # --- RESUME LAST FAILED BATCH ---
    _failed_cache_path = PROJECT_ROOT / "system-workspace" / ".last_failed_pages.json"
    import json as _json_resume
    _last_failed = None
    if _failed_cache_path.exists():
        try:
            _last_failed = _json_resume.loads(_failed_cache_path.read_text(encoding="utf-8"))
        except Exception:
            _last_failed = None

    if _last_failed and _last_failed.get("failed_lessons"):
        _prev_count = len(_last_failed["failed_lessons"])
        console.print(f"\n[bold yellow]⚠️  Found {_prev_count} lessons that failed in your last batch run![/bold yellow]")
        console.print(f"[dim]Lessons: {', '.join(_last_failed['failed_lessons'])}[/dim]")
        _resume_choice = questionary.select(
            "What would you like to do?",
            choices=[
                f"1. Resume & retry the {_prev_count} failed lessons from last time",
                "2. Start a new batch (full or custom range)",
            ]
        ).ask()
        if _resume_choice and _resume_choice.startswith("1"):
            only_lessons = _last_failed["failed_lessons"]
            force_remake = False
            # Clear the cache now that we're retrying
            try:
                _failed_cache_path.unlink()
            except Exception:
                pass
            console.print(f"[cyan]Resuming with {len(only_lessons)} failed lessons...[/cyan]")
            start_all = time.time()
            # Skip straight to batch run
            with Live(generate_layout(), refresh_per_second=4, vertical_overflow="crop") as live:
                def callback(title, status, msg):
                    with lock:
                        if title not in tasks:
                            tasks[title] = {}
                        tasks[title]["status"] = status
                        tasks[title]["message"] = msg
                        if status == "RUNNING":
                            if "start_time" not in tasks[title]:
                                tasks[title]["start_time"] = time.time()
                        elif status in ["SUCCESS", "FAILED", "SKIP", "WARN", "ERROR", "API_BLOCKED"]:
                            if "start_time" in tasks[title]:
                                tasks[title]["duration"] = time.time() - tasks[title]["start_time"]
                            else:
                                tasks[title]["duration"] = 0.0
                    live.update(generate_layout())
                generator.run_batch_generation(max_concurrent=5, update_callback=callback, only_lessons=only_lessons)
            # Fall through to failure-handling logic below
            total_duration = time.time() - start_all
            console.print(generate_table(full=True))
            console.print(f"[bold green]✅ Resume Batch Completed in {format_duration(total_duration)}![/bold green]")
            # Re-check failures (same logic below)
            failed_data = []
            with lock:
                for title, data in tasks.items():
                    if data.get("status") in ["FAILED", "ERROR", "WARN"]:
                        match = re.search(r"(?:^|page[_\s]*)(\d+)", title, re.IGNORECASE)
                        lesson_num = match.group(1) if match else None
                        if lesson_num:
                            clean_t = re.sub(r"^\d+\s*-\s*", "", title).replace("-plan", "").strip()
                            if getattr(generator, "is_1_page_mode", False):
                                expected_path = f"pages/page_{lesson_num}.html"
                            else:
                                expected_path = f"pages/{lesson_num}.0_nXX_{clean_t.replace(' ', '_')}.html"
                            failed_data.append((lesson_num, title, expected_path))
            failed_lessons = [d[0] for d in failed_data]
            if failed_data:
                try:
                    _failed_cache_path.write_text(
                        _json_resume.dumps({"failed_lessons": failed_lessons, "failed_data": [[a, b, c] for a, b, c in failed_data]}, ensure_ascii=False, indent=2),
                        encoding="utf-8"
                    )
                except Exception:
                    pass
                console.print(f"\n[bold red]⚠️ {len(failed_lessons)} pages still failed.[/bold red]")
                console.print(f"[dim]Run generation again to resume these {len(failed_lessons)} lessons.[/dim]")
            questionary.press_any_key_to_continue().ask()
            return

    # Initialize Live with the initial table
    existing_count = generator.count_existing_pages()
    force_remake = False
    if existing_count > 0:
        ans = questionary.confirm(f"Found {existing_count} existing pages. Do you want to RE-MAKE them? (No = Skip)").ask()
        force_remake = ans
        
    range_input = questionary.text("Lessons to process (e.g. '1-10', '5', '12,15' or 'ALL'):", default="ALL").ask()
    if range_input is None: return
    
    only_lessons = None
    if range_input.strip().upper() != "ALL":
        only_lessons = []
        for part in range_input.split(','):
            part = part.strip()
            if '-' in part:
                try:
                    s, e = map(int, part.split('-'))
                    only_lessons.extend([str(i).zfill(2) for i in range(s, e + 1)])
                    only_lessons.extend([str(i) for i in range(s, e + 1)])
                except:
                    pass
            elif part.isdigit():
                only_lessons.append(str(int(part)).zfill(2))
                only_lessons.append(str(int(part)))

    start_all = time.time()
    
    while True:
        with Live(generate_layout(), refresh_per_second=4, vertical_overflow="crop") as live:
    
            def callback(title, status, msg):
                with lock:
                    if title not in tasks:
                        tasks[title] = {}
    
                    tasks[title]["status"] = status
                    tasks[title]["message"] = msg
    
                    if status == "RUNNING":
                        if "start_time" not in tasks[title]:
                            tasks[title]["start_time"] = time.time()
                    elif status in ["SUCCESS", "FAILED", "SKIP", "WARN", "ERROR", "API_BLOCKED"]:
                        if "start_time" in tasks[title]:
                            tasks[title]["duration"] = time.time() - tasks[title]["start_time"]
                        else:
                            tasks[title]["duration"] = 0.0
    
                live.update(generate_layout())
    
            generator.run_batch_generation(max_concurrent=5, update_callback=callback, force_remake=force_remake, only_lessons=only_lessons)

        api_blocked = any(data.get("status") == "API_BLOCKED" for data in tasks.values())
        if api_blocked:
            console.print("[bold red]\n⚠️ Jules API Limit or Quota Reached![/bold red]")
            retry_choice = questionary.select(
                "API Block detected. What would you like to do?",
                choices=["1. Wait and Resume batch", "2. Stop and Exit batch"]
            ).ask()
            if retry_choice and retry_choice.startswith("1"):
                generator.abort_event.clear()
                for title, data in tasks.items():
                    if data.get("status") == "API_BLOCKED":
                        data["status"] = "PENDING"
                        data["message"] = "Retrying..."
                console.print("[yellow]Resuming batch...[/yellow]")
                time.sleep(2)
                continue
            else:
                break
        else:
            break

    total_duration = time.time() - start_all
    console.print(generate_table(full=True))
    console.print(
        f"[bold green]✅ Batch Generation Completed in {format_duration(total_duration)}![/bold green]"
    )

    # Identify Failed Tasks for Auto-Recovery
    failed_data = []
    with lock:
        for title, data in tasks.items():
            if data.get("status") in ["FAILED", "ERROR", "WARN"]:
                match = re.search(r"(?:^|page[_\s]*)(\d+)", title, re.IGNORECASE)
                lesson_num = match.group(1) if match else None
                if lesson_num:
                    clean_t = re.sub(r"^\d+\s*-\s*", "", title).replace("-plan", "").strip()
                    if getattr(generator, "is_1_page_mode", False):
                        expected_path = f"pages/page_{lesson_num}.html"
                    else:
                        expected_path = f"pages/{lesson_num}.0_nXX_{clean_t.replace(' ', '_')}.html"
                    failed_data.append((lesson_num, title, expected_path))

    failed_lessons = [d[0] for d in failed_data]

    # Persist failed lessons list to disk so it can be resumed later
    _failed_cache_path = PROJECT_ROOT / "system-workspace" / ".last_failed_pages.json"
    import json as _json_fl
    if failed_data:
        try:
            _failed_cache_path.write_text(
                _json_fl.dumps({"failed_lessons": failed_lessons, "failed_data": [[a, b, c] for a, b, c in failed_data]}, ensure_ascii=False, indent=2),
                encoding="utf-8"
            )
        except Exception:
            pass

    if failed_data:
        console.print(
            f"\n[bold red]⚠️ {len(failed_lessons)} pages failed to generate or pull from PRs.[/bold red]"
        )
        console.print(f"Failed lessons: {', '.join(failed_lessons)}")

        choice = questionary.select(
            "How would you like to handle the failed pages?",
            choices=[
                "1. Smart Search & Auto-Recover (Search hidden folders and local PR branches)",
                "2. Regenerate them using new Jules sessions",
                "3. Show me how to check and fix them manually",
                "4. Skip for now",
                "5. Auto-Retry failed lessons now (resume batch)",
            ],
        ).ask()

        if choice and choice.startswith("1"):
            rec1 = smart_recover_hidden_plans(failed_data, PROJECT_ROOT, console, is_pages=True)
            rec2 = extract_from_pr_branches(
                [d for d in failed_data if d[0] not in rec1], PROJECT_ROOT, console, is_pages=True
            )
            total_rec = rec1 + rec2
            if len(total_rec) == len(failed_lessons):
                console.print(
                    "[bold green]✅ All failed pages were successfully recovered![/bold green]"
                )
            else:
                console.print(
                    f"[yellow]⚠️ Recovered {len(total_rec)} out of {len(failed_lessons)} pages.[/yellow]"
                )
                still_failed = [d[0] for d in failed_data if d[0] not in total_rec]
                if still_failed:
                    console.print(f"Still missing: {', '.join(still_failed)}")
                    regen = questionary.confirm(
                        "Would you like to regenerate the remaining missing pages?"
                    ).ask()
                    if regen:
                        console.print("[cyan]Force-regenerating remaining missing pages...[/cyan]")
                        with lock:
                            tasks.clear()
                        if state_manager:
                            for l_num, l_title, _ in failed_data:
                                if l_num in still_failed:
                                    state_manager.update_lesson_data(
                                        l_title, {"page_session_id": None}
                                    )
                        with Live(
                            generate_layout(), refresh_per_second=4, vertical_overflow="crop"
                        ) as live:
                            generator.run_batch_generation(
                                max_concurrent=5,
                                update_callback=callback,
                                only_lessons=still_failed,
                            )
                        console.print("[bold green]✅ Recovery Completed![/bold green]")

        elif choice and choice.startswith("2"):
            console.print("[cyan]Force-regenerating failed pages...[/cyan]")
            with lock:
                tasks.clear()
            if state_manager:
                for l_num, l_title, _ in failed_data:
                    if l_num in failed_lessons:
                        state_manager.update_lesson_data(l_title, {"page_session_id": None})
            with Live(generate_layout(), refresh_per_second=4, vertical_overflow="crop") as live:
                generator.run_batch_generation(
                    max_concurrent=5, update_callback=callback, only_lessons=failed_lessons
                )
            console.print("[bold green]✅ Recovery Completed![/bold green]")

        elif choice and choice.startswith("3"):
            console.print("\n[bold cyan]--- MANUAL RECOVERY GUIDE ---[/bold cyan]")
            console.print(
                "When Jules fails to merge a PR or places a file incorrectly, the files are downloaded to your local computer but hidden inside Git branches."
            )
            console.print("\n[yellow]Steps to manually recover:[/yellow]")
            console.print(
                "1. Find the PR branch name from `system.log` (e.g., [bold]pr-230[/bold])."
            )
            console.print("2. Switch to that branch in your terminal:")
            console.print("   [bold]git checkout pr-230[/bold]")
            console.print(
                "3. Look for the file in the `pages/` or `Jules-workspace/pages/` folder."
            )
            console.print("4. Move the file into the `pages/` folder:")
            console.print("   [bold]mv Jules-workspace/pages/07.0_nXX_title.html pages/[/bold]")
            console.print("5. Switch back to the main branch:")
            console.print("   [bold]git checkout main[/bold]")
            console.print("6. Your file will now be successfully recovered!\n")

        elif choice and choice.startswith("4"):
            console.print("[dim]Skipping recovery for now.[/dim]")
            console.print(f"[dim]💡 Tip: Run generation again and choose option 5 to resume the {len(failed_lessons)} failed lessons.[/dim]")

        elif choice and choice.startswith("5"):
            console.print("[cyan]⏳ Auto-retrying all failed lessons with new Jules sessions...[/cyan]")
            with lock:
                tasks.clear()
            if state_manager:
                for l_num, l_title, _ in failed_data:
                    state_manager.update_lesson_data(l_title, {"page_session_id": None})
            generator.abort_event.clear()
            with Live(generate_layout(), refresh_per_second=4, vertical_overflow="crop") as live:
                generator.run_batch_generation(
                    max_concurrent=5, update_callback=callback, only_lessons=failed_lessons
                )
            console.print("[bold green]✅ Auto-Retry Completed![/bold green]")

    # Auto-Pull
    _settings_file_gen = PROJECT_ROOT / "system-workspace/settings.json"
    _ws_code_gen = None
    import json as _json_gen
    if _settings_file_gen.exists():
        try:
            with open(_settings_file_gen, encoding="utf-8") as _fg:
                _ws_code_gen = _json_gen.load(_fg).get("workspace_code")
        except Exception:
            pass
    if _ws_code_gen:
        auto_pull_jules_batch("pages", _ws_code_gen)

    questionary.press_any_key_to_continue().ask()
    console.print("\n[cyan]Running Post-Flight Page Lint...[/cyan]")
    try:
        import lint_pages

        # Define allowed classes to avoid parsing css multiple times
        allowed_classes = None
        styles_path = PROJECT_ROOT / "styles/main.css"
        if styles_path.exists():
            try:
                allowed_classes = lint_pages.parse_allowed_classes(str(styles_path))
            except:
                pass

        target_files = []
        pages_dir = PROJECT_ROOT / "pages"
        if pages_dir.exists():
            for f in pages_dir.glob("*.html"):
                target_files.append(str(f))

        issues = 0
        for f in target_files:
            errs, warns = lint_pages.lint_file(f, allowed_classes)
            if errs:
                issues += 1

        if issues > 0:
            console.print(
                f"[red]⚠️ POST-FLIGHT WARNING: {issues} pages have bloat/errors. Run Audit & Verify (G) for details.[/red]"
            )
        else:
            console.print("[green]✅ Post-Flight Success: All generated pages are clean.[/green]")
    except Exception as e:
        console.print(f"[red]Error running post-flight lint: {e}[/red]")


def run_retry_planning_and_generation_ui(state_manager):
    console.clear()
    console.print("[bold cyan]🔄 Retry Batch Jules Planning / Page Making[/bold cyan]")

    lesson_input = questionary.text(
        "Enter lesson numbers to re-make (comma separated, e.g. 3, 5, 6):"
    ).ask()
    if not lesson_input:
        return

    # Parse inputs to padded string format used in TOC
    only_lessons = []
    for item in lesson_input.split(","):
        item = item.strip()
        if item.isdigit():
            only_lessons.append(f"{int(item):02d}")
        else:
            only_lessons.append(item)

    if not only_lessons:
        return

    console.print(f"[yellow]Will re-make lessons: {', '.join(only_lessons)}[/yellow]")
    confirm = questionary.confirm(
        "This will delete old plans and pages for these lessons. Continue?"
    ).ask()
    if not confirm:
        return

    # Delete old plans and pages
    plans_dir = PROJECT_ROOT / "plans"
    pages_dir = PROJECT_ROOT / "pages"

    deleted = 0
    if plans_dir.exists():
        for plan in plans_dir.glob("*.md"):
            match = re.search(r"(?:^|page[_\s]*)(\d+)", plan.name, re.IGNORECASE)
            if match and match.group(1) in only_lessons:
                plan.unlink()
                deleted += 1
                console.print(f"[dim]Deleted {plan.name}[/dim]")

    if pages_dir.exists():
        for page in pages_dir.glob("*.html"):
            match = re.search(r"(?:^|page[_\s]*)(\d+)", page.name, re.IGNORECASE)
            if match and match.group(1) in only_lessons:
                page.unlink()
                deleted += 1
                console.print(f"[dim]Deleted {page.name}[/dim]")

    console.print(f"[green]Deleted {deleted} old files.[/green]")

    # Run Planning
    console.print("\n[bold cyan]Step 1: Planning[/bold cyan]")
    planner = JulesPlanner(PROJECT_ROOT, state_manager=state_manager)
    tasks = {}
    lock = threading.Lock()

    def callback_plan(title, status, msg):
        with lock:
            if title not in tasks:
                tasks[title] = {"status": status, "message": msg}
            else:
                tasks[title]["status"] = status
                tasks[title]["message"] = msg
        if status in ["ERROR", "FAILED", "WARN"]:
            console.print(f"[red][{status}] {title}: {msg}[/red]")
        elif status == "SUCCESS":
            console.print(f"[green]✅ {title} planned![/green]")

    planner.run_batch_planning(
        max_concurrent=5, update_callback=callback_plan, only_lessons=only_lessons
    )

    # Run Generation
    console.print("\n[bold cyan]Step 2: Generation[/bold cyan]")
    generator = JulesPageGenerator(PROJECT_ROOT)

    def callback_gen(title, status, msg):
        with lock:
            if title not in tasks:
                tasks[title] = {"status": status, "message": msg}
            else:
                tasks[title]["status"] = status
                tasks[title]["message"] = msg
        if status in ["ERROR", "FAILED", "WARN"]:
            console.print(f"[red][{status}] {title}: {msg}[/red]")
        elif status == "SUCCESS":
            console.print(f"[green]✅ {title} generated![/green]")

    generator.run_batch_generation(
        max_concurrent=5, update_callback=callback_gen, only_lessons=only_lessons
    )

    console.print("\n[bold green]✅ Retry Workflow Completed![/bold green]")


def run_jules_ocr_ui(state_manager):
    console.clear()
    console.print("[bold cyan]🚀 Starting Jules Batch OCR (One Session)...[/bold cyan]")

    ocr = JulesOCR(PROJECT_ROOT)

    ui_state = {"status": "INIT", "message": "Initializing..."}
    lock = threading.Lock()

    def generate_display():
        with lock:
            s = ui_state["status"]
            m = ui_state["message"]

        color = "white"
        if s == "RUNNING":
            color = "yellow"
        elif s == "SUCCESS":
            color = "green"
        elif s == "FAILED" or s == "ERROR":
            color = "red"

        return Panel(
            f"[bold {color}]Status: {s}[/bold {color}]\n{m}",
            title="Jules OCR Progress",
            box=box.ROUNDED,
            border_style=color,
        )

    start_time = time.time()

    with Live(
        Group(generate_display(), generate_log_panel()),
        refresh_per_second=4,
        vertical_overflow="visible",
    ) as live:

        def callback(status, msg):
            with lock:
                msg_type, msg_text = msg
                status_messages.append(f"[{msg_type}]{msg_text}[/{msg_type}]")
                ui_state["status"] = status
                ui_state["message"] = msg_text
            live.update(Group(generate_display(), generate_log_panel()))

        ocr.run_ocr_batch(update_callback=callback)

    console.print(
        f"[bold green]✅ OCR Batch Completed in {format_duration(time.time() - start_time)}![/bold green]"
    )


def run_full_auto_ui(state_manager, is_1_page_mode=False):
    console.clear()
    mode_text = " (1-Page Mode)" if is_1_page_mode else ""
    console.print(f"[bold cyan]🚀 Starting Full Auto Workflow{mode_text}...[/bold cyan]")
    console.print("[dim]Press Ctrl+C to Pause/Stop[/dim]")

    # Init workflow
    workflow = FullAutoWorkflow(PROJECT_ROOT, state_manager, is_1_page_mode=is_1_page_mode)

    # Ask for starting point
    start_choice = questionary.select(
        "Select Starting Point:",
        choices=["1. Start normally", "Start from Raw Processing", "Start from Unified Generation"],
        style=questionary.Style(
            [
                ("qmark", "fg:#673ab7 bold"),
                ("question", "bold"),
                ("answer", "fg:#f44336 bold"),
                ("pointer", "fg:#673ab7 bold"),
                ("highlighted", "fg:#673ab7 bold"),
                ("selected", "fg:#cc5454"),
                ("separator", "fg:#cc5454"),
                ("instruction", ""),
                ("text", ""),
                ("disabled", "fg:#858585 italic"),
            ]
        ),
    ).ask()

    if not start_choice:
        return

    if start_choice == "Start from Raw Processing":
        workflow.jump_to_step("RAW_PROC")
    elif start_choice == "Start from Unified Generation":
        # Start from CHECK_EXIST to ensure we sync existing plans/pages before generating
        workflow.jump_to_step("CHECK_EXIST")

    # Shared state for UI
    ui_state = {"history": [], "last_update": time.time()}
    lock = threading.Lock()

    # Display Class for Rich Live
    class WorkflowStatusDisplay:
        def __init__(self, workflow, ui_state, lock):
            self.workflow = workflow
            self.ui_state = ui_state
            self.lock = lock

        def __rich__(self):
            layout = Layout()
            layout.split(
                Layout(name="header", size=3),
                Layout(name="main", ratio=1),
                Layout(name="footer", size=10),
                Layout(name="verbose_logs", size=8),
            )

            current_step = self.workflow.get_current_step_name()
            layout["header"].update(
                Panel(
                    f"[bold cyan]Full Auto Workflow - {current_step}[/bold cyan]",
                    style="bold white",
                    box=box.ROUNDED,
                )
            )

            layout["main"].update(Panel(self.generate_timeline(), box=box.ROUNDED))

            with self.lock:
                hist = list(self.ui_state["history"])

            log_text = ""
            for ts, s, st, m in hist:
                c = "white"
                if st == "SUCCESS":
                    c = "green"
                elif st == "WARN":
                    c = "yellow"
                elif st == "ERROR":
                    c = "red"
                elif st == "DOWN":
                    c = "cyan"
                elif st == "MISS":
                    c = "magenta"
                elif st == "START":
                    c = "blue"
                elif st == "INFO":
                    c = "dim"
                elif st == "RUNNING":
                    c = "yellow"
                log_text += f"[{c}]{ts} [{s}] {st}: {m}[/{c}]\n"

            layout["footer"].update(Panel(log_text, title="Log History", box=box.SIMPLE))
            layout["verbose_logs"].update(generate_log_panel())
            return layout

        def generate_timeline(self):
            table = Table(title="Workflow Timeline", box=box.SIMPLE, expand=True)
            table.add_column("Step", style="bold white")
            table.add_column("Status", width=12)
            table.add_column("Start", style="dim")
            table.add_column("End", style="dim")
            table.add_column("Timer", justify="right", style="yellow")

            steps = self.workflow.get_steps()
            for step in steps:
                s_id = step["id"]
                if s_id in self.workflow.step_timings:
                    meta = self.workflow.step_timings[s_id]
                    status = meta["status"]
                else:
                    meta = {
                        "status": "PENDING",
                        "start_time": None,
                        "end_time": None,
                        "duration": 0,
                    }
                    status = "PENDING"

                s_color = "white"
                if status == "SUCCESS":
                    s_color = "green"
                elif status == "RUNNING":
                    s_color = "yellow"
                elif status == "FAILED":
                    s_color = "red"
                elif status == "PAUSED":
                    s_color = "magenta"
                elif status == "PENDING":
                    s_color = "dim"
                elif status == "SKIPPED":
                    s_color = "dim green"

                start_s = (
                    time.strftime("%H:%M:%S", time.localtime(meta["start_time"]))
                    if meta["start_time"]
                    else "-"
                )
                end_s = (
                    time.strftime("%H:%M:%S", time.localtime(meta["end_time"]))
                    if meta["end_time"]
                    else "-"
                )

                if status == "RUNNING" and meta.get("start_time"):
                    dur_s = format_duration(time.time() - meta["start_time"])
                else:
                    dur_s = (
                        format_duration(meta["duration"]) if meta.get("duration", 0) > 0 else "-"
                    )

                table.add_row(
                    step["label"], f"[{s_color}]{status}[/{s_color}]", start_s, end_s, dur_s
                )
            return table

    def callback(step, status, message):
        with lock:
            if status in [
                "SUCCESS",
                "WARN",
                "ERROR",
                "MISS",
                "DOWN",
                "START",
                "MERGE",
                "INDEX",
                "GEN",
                "AUDIT",
                "INFO",
                "RUNNING",
            ]:
                ui_state["history"].append((time.strftime("%H:%M:%S"), step, status, message))
                if len(ui_state["history"]) > 8:
                    ui_state["history"].pop(0)

    workflow.callback = callback

    # Run Loop with Pause Handling
    skip_archive = False

    # Save original stdout to restore later and for console to use
    original_stdout = sys.stdout

    try:
        # Redirect stdout to log to prevent flickering from modules
        sys.stdout = StreamLogger(logging.getLogger(), logging.INFO)

        while True:
            # Ensure display instance has the CURRENT workflow object (important for restarts)
            display_instance = WorkflowStatusDisplay(workflow, ui_state, lock)

            try:
                # Pass console explicitly to ensure Live uses the terminal (original stdout)
                with Live(
                    display_instance,
                    refresh_per_second=4,
                    console=console,
                    vertical_overflow="visible",
                ) as live:
                    # Start workflow
                    stats = workflow.run(skip_archive=skip_archive)

                # If we get here, it finished successfully
                # We need to temporarily restore stdout to print the final report to screen
                sys.stdout = original_stdout
                console.print(
                    "[bold green]✅ Full Auto Workflow Completed Successfully![/bold green]"
                )

                # Show Final Report
                table = Table(title="Final Workflow Report", box=box.ROUNDED)
                table.add_column("Metric", style="cyan")
                table.add_column("Value", style="bold white")
                for k, v in stats.items():
                    if isinstance(v, list):
                        v = f"{len(v)} ({', '.join(map(str, v[:5]))}...)"
                    table.add_row(k, str(v))
                console.print(table)
                break

            except KeyboardInterrupt:
                # Restore stdout for interaction
                sys.stdout = original_stdout

                # Pause Menu
                console.print("\n[bold yellow]⏸️ Workflow Paused by User[/bold yellow]")

                # Determine options
                current_step_name = workflow.get_current_step_name()

                choices = [
                    f"Resume (Continue {current_step_name})",
                    "Re-do Previous Step",
                    "Jump to Step...",
                    "Restart (Full Reset)",
                    "Quit",
                ]

                action = questionary.select(
                    "Paused. What would you like to do?", choices=choices
                ).ask()

                if not action or action.startswith("Quit"):
                    return

                elif action.startswith("Resume"):
                    skip_archive = True  # Usually we don't want to archive again if we resume
                    console.print("[dim]Resuming...[/dim]")
                    # Go back to redirecting stdout
                    sys.stdout = StreamLogger(logging.getLogger(), logging.INFO)

                elif action.startswith("Restart"):
                    skip_archive = False
                    workflow = FullAutoWorkflow(PROJECT_ROOT, state_manager)  # Reset
                    workflow.callback = callback
                    ui_state["history"] = []
                    console.print("[dim]Restarting...[/dim]")
                    # Go back to redirecting stdout
                    sys.stdout = StreamLogger(logging.getLogger(), logging.INFO)

                elif action.startswith("Re-do Previous"):
                    if workflow.redo_previous_step():
                        console.print("[green]Rewound to previous step.[/green]")
                        skip_archive = True  # Don't archive again if jumping back inside
                    else:
                        console.print("[red]Cannot go back (already at start).[/red]")
                        time.sleep(1)
                    # Go back to redirecting stdout
                    sys.stdout = StreamLogger(logging.getLogger(), logging.INFO)

                elif action.startswith("Jump to Step"):
                    steps = [s["label"] for s in workflow.get_steps()]
                    target = questionary.select("Select Step to Jump to:", choices=steps).ask()
                    if target:
                        workflow.jump_to_step(target)
                        skip_archive = True  # Assume skip archive if jumping around
                        console.print(f"[green]Jumped to {target}.[/green]")
                    # Go back to redirecting stdout
                    sys.stdout = StreamLogger(logging.getLogger(), logging.INFO)

    except Exception as e:
        sys.stdout = original_stdout
        console.print(f"[bold red]❌ Critical Error: {e}[/bold red]")
        import traceback

        console.print(traceback.format_exc())
    finally:
        sys.stdout = original_stdout


# --- LEGACY WRAPPERS ---


def run_ocr(state_manager):
    console.clear()  # Clear screen
    console.print(Panel("[bold]Running OCR Module...[/bold]", style="blue"))
    input_dir = PROJECT_ROOT / "input"
    images = sorted(list(input_dir.glob("*.jpg")) + list(input_dir.glob("*.png")))

    if not images:
        console.print("[yellow]⚠️ No images found in input/.[/yellow]")
        return

    vision = VisionClient()
    output_dir = PROJECT_ROOT / "system-workspace/text-data/raw"
    output_dir.mkdir(parents=True, exist_ok=True)

    start_time = time.time()
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("{task.percentage:>3.0f}%"),
    ) as progress:
        task = progress.add_task("[cyan]Processing Images...", total=len(images))

        for img in images:
            out_file = output_dir / f"raw_{img.stem}.txt"
            if out_file.exists():
                progress.console.print(f"[dim]⏭️ Skipping {img.name} (exists)[/dim]")
                progress.advance(task)
                continue

            text = vision.extract_text([img])
            if text:
                out_file.write_text(text, encoding="utf-8")
                progress.console.print(f"[green]✅ Saved: {out_file.name}[/green]")
                state_manager.update_lesson_status(
                    f"Image_{img.stem}", "OCR_DONE", {"raw": str(out_file)}
                )
            else:
                progress.console.print(f"[red]❌ Failed: {img.name}[/red]")

            progress.advance(task)

    console.print(
        f"[bold green]✅ OCR Completed in {format_duration(time.time() - start_time)}![/bold green]"
    )


def run_raw_processing(state_manager):
    console.clear()
    console.print(Panel("[bold]Running Raw Processing...[/bold]", style="blue"))
    tp = TextProcessor()

    toc_choice = questionary.select(
        "How would you like to provide the TOC.json?",
        choices=[
            "1. Manually select/use existing input/TOC.json",
            "2. Auto-generate new TOC.json using AI from raw text",
        ],
    ).ask()

    if not toc_choice:
        return

    start_time = time.time()

    from rich.spinner import Spinner
    from rich.text import Text

    def generate_raw_view(status_text):
        return Group(
            Panel(Spinner("dots", text=Text(status_text, style="bold green")), border_style="blue"),
            generate_log_panel(),
        )

    original_stdout = sys.stdout
    original_stderr = sys.stderr
    sys.stdout = StreamLogger(logging.getLogger(), logging.INFO)
    sys.stderr = StreamLogger(logging.getLogger(), logging.ERROR)

    try:
        with Live(
            generate_raw_view("Processing..."),
            console=console,
            refresh_per_second=4,
            redirect_stdout=False,
            redirect_stderr=False,
            vertical_overflow="visible",
        ) as live:

            def log_step(text):
                logging.info(text)
                live.update(generate_raw_view(text))

            log_step("1. Merging Raw Text...")
            merged_path = tp.merge_raw_text()
            if not merged_path:
                return

            if toc_choice.startswith("2"):
                log_step("2. Generating TOC.json via AI...")
                toc_success = tp.generate_toc(merged_path)
                if not toc_success:
                    logging.info(
                        "[yellow]⚠️ Gemini API and CLI failed to generate TOC. Falling back to Antigravity CLI Headless Agent...[/yellow]"
                    )
                    try:
                        import json

                        settings_file = PROJECT_ROOT / "system-workspace" / "settings.json"
                        author = "أ. حنا خفيف"
                        author_number = " "
                        if settings_file.exists():
                            try:
                                with open(settings_file, encoding="utf-8") as f:
                                    settings = json.load(f)
                                    author = settings.get("author", author)
                                    author_number = settings.get("author_number", author_number)
                            except Exception as e:
                                logging.info(f"⚠️ Could not load settings: {e}")

                        prompt = (
                            "Please read system-workspace/text-data/full_raw_indexed.txt. "
                            "Act as an expert Arabic book editor to extract the Table of Contents (TOC) from this text and output it as a JSON object. "
                            "The output MUST be a JSON object where the keys are lesson numbers (e.g., '01', '02'). "
                            f"Each value must be an object with exactly these fields: 'title', 'level', 'Unit', 'author' (set to '{author}'), and 'author_number' (set to '{author_number}'). "
                            "You MUST logically infer an appropriate 'level' (المستوى) and 'Unit' (الوحدة) for each lesson by analyzing its topic and depth in the text (e.g., Level: 'المستوى التأسيسي', Unit: 'علم النحو'). Do NOT leave them blank. "
                            "Save this EXACT JSON structure to input/TOC.json."
                        )
                        cmd = ["agy", "-p", prompt, "--dangerously-skip-permissions"]
                        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
                        if result.returncode != 0:
                            logging.info(f"[red]❌ Antigravity CLI Error:[/red] {result.stderr}")
                        if tp.toc_path.exists():
                            logging.info(
                                "[green]✅ Antigravity CLI successfully generated the TOC![/green]"
                            )
                        else:
                            logging.info(
                                "[red]❌ Antigravity CLI ran, but TOC was not created.[/red]"
                            )
                    except Exception as e:
                        logging.info(f"[red]❌ Antigravity CLI Fallback failed: {e}[/red]")

            if not tp.validate_toc():
                return

            log_step("3. Generating Lesson Index...")
            mapping = tp.generate_lesson_index()

            if not mapping:
                logging.info(
                    "[yellow]⚠️ Gemini API and CLI failed. Falling back to Antigravity CLI Headless Agent...[/yellow]"
                )
                try:
                    import json

                    prompt = (
                        "Please read input/TOC.json and system-workspace/text-data/full_raw_indexed.txt. "
                        "Then, act as an expert Arabic book editor to identify the exact start and end line markers "
                        "for every lesson/topic found in that text based on the TOC. "
                        "Create a JSON mapping where keys are the exact TOC titles and values are objects "
                        "with 'start' and 'end' line indicators (e.g., 'raw_1.txt:5'). "
                        "Save this EXACT JSON structure to system-workspace/text-data/raw_to_lesson_index.json."
                    )
                    cmd = ["agy", "-p", prompt, "--dangerously-skip-permissions"]
                    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
                    if result.returncode != 0:
                        logging.info(f"[red]❌ Antigravity CLI Error:[/red] {result.stderr}")

                    if tp.index_file.exists():
                        with open(tp.index_file, encoding="utf-8") as f:
                            mapping = json.load(f)
                        logging.info(
                            "[green]✅ Antigravity CLI successfully generated the index mapping![/green]"
                        )
                    else:
                        logging.info(
                            "[red]❌ Antigravity CLI ran, but the index file was not created.[/red]"
                        )
                except Exception as e:
                    logging.info(f"[red]❌ Antigravity CLI Fallback failed: {e}[/red]")

        if mapping:
            console.print(
                f"[bold green]✅ Raw Processing Complete in {format_duration(time.time() - start_time)}![/bold green]"
            )
    finally:
        sys.stdout = original_stdout
        sys.stderr = original_stderr


def run_raw_processing_auto(state_manager):
    console.clear()
    console.print(Panel("[bold]Running Auto-Paginated Raw Processing...[/bold]", style="blue"))
    tp = TextProcessor()
    
    toc_choice = questionary.select(
        "How would you like to provide the TOC.json?",
        choices=[
            "1. Manually select/use existing input/TOC.json",
            "2. Auto-generate new TOC.json from PAGE markers",
        ],
    ).ask()

    if not toc_choice:
        return
        
    generate_toc_flag = toc_choice.startswith("2")

    start_time = time.time()
    
    from rich.spinner import Spinner
    from rich.text import Text

    def generate_raw_view(status_text):
        return Group(
            Panel(Spinner("dots", text=Text(status_text, style="bold green")), border_style="blue"),
            generate_log_panel(),
        )

    original_stdout = sys.stdout
    original_stderr = sys.stderr
    sys.stdout = StreamLogger(logging.getLogger(), logging.INFO)
    sys.stderr = StreamLogger(logging.getLogger(), logging.ERROR)

    try:
        with Live(
            generate_raw_view("Processing Auto-Pagination..."),
            console=console,
            refresh_per_second=4,
            redirect_stdout=False,
            redirect_stderr=False,
            vertical_overflow="visible",
        ) as live:

            def log_step(text):
                logging.info(text)
                live.update(generate_raw_view(text))

            log_step("Auto-generating Index (and TOC if requested) from PAGE markers...")
            success = tp.generate_auto_page_index_and_toc(generate_toc=generate_toc_flag)
            
            if success:
                console.print(
                    f"[bold green]✅ Auto-Paginated Raw Processing Complete in {format_duration(time.time() - start_time)}![/bold green]"
                )
            else:
                console.print("[bold red]❌ Failed to generate auto-paginated index.[/bold red]")
    finally:
        sys.stdout = original_stdout
        sys.stderr = original_stderr



def run_planning(state_manager):
    console.clear()
    console.print(Panel("[bold]Running Standard Planner...[/bold]", style="blue"))

    start_time = time.time()
    with console.status("[bold green]Initializing...[/bold green]", spinner="dots"):
        tp = TextProcessor(use_headless=True)
        if not tp.validate_toc():
            return

        console.print("1. Merging Raw Text...")
        merged_path = tp.merge_raw_text()
        if not merged_path:
            return

        console.print("2. Generating Lesson Index...")
        mapping = tp.generate_lesson_index()
        if not mapping:
            return

    planner = Planner()

    with Progress() as progress:
        task = progress.add_task("[cyan]Generating Plans...", total=len(mapping))

        for lesson_title, range_info in mapping.items():
            lesson_number = tp.get_lesson_number(lesson_title)
            clean_title = re.sub(r"^\d+\s*-\s*", "", lesson_title).strip()

            plan_filename = f"{lesson_number}-{clean_title}-plan.md"
            plan_path = planner.generate_plan(
                raw_lesson_text=merged_path.read_text(encoding="utf-8"),
                output_filename=plan_filename,
                lesson_number=lesson_number,
                lesson_title=clean_title,
            )

            if plan_path:
                state_manager.update_lesson_status(
                    lesson_number, "PLAN_READY", {"plan": str(plan_path)}
                )
                progress.console.print(f"[green]✅ Plan: {plan_filename}[/green]")

            progress.advance(task)

    console.print(
        f"[bold green]✅ Standard Planning Completed in {format_duration(time.time() - start_time)}![/bold green]"
    )


def run_audit_and_verify(state_manager):
    console.clear()
    console.print(Panel("[bold]Running Audit & Verify Pages...[/bold]", style="blue"))

    # Define paths
    pages_dir = PROJECT_ROOT / "pages"
    if not pages_dir.exists():
        console.print("[red]❌ Pages directory not found![/red]")
        return

    # Define Exclusions
    excluded_files = {
        "00.0_blank_page1.html",
        "99.0_blank_page2.html",
        "00.1_n01_toc_p1.html",
        "00.2_n02_toc_p2.html",
    }
    excluded_folders = {"cover"}

    # Gather Files
    target_files = []

    # We use glob to find all HTML files recursively
    all_html_files = sorted(list(pages_dir.glob("**/*.html")))

    for f in all_html_files:
        rel_path = f.relative_to(pages_dir)

        # Check specific file exclusion
        if f.name in excluded_files:
            continue

        # Check folder exclusion (check parts of the relative path)
        if any(part in excluded_folders for part in rel_path.parts):
            continue

        target_files.append(str(f))

    if not target_files:
        console.print("[yellow]No files to process.[/yellow]")
        return

    console.print(f"[bold]Processing {len(target_files)} files...[/bold]")

    # 1. ID Manager
    console.print("\n[cyan]1. Running ID Manager (auto-tag)...[/cyan]")
    if id_manager:
        try:
            # Initialize IDManager with root_dir so it scans ALL files for uniqueness
            manager = id_manager.IDManager(root_dir=str(pages_dir))
            # But only auto-tag the target files
            manager.auto_tag(files=target_files)
        except Exception as e:
            console.print(f"[red]Error in ID Manager: {e}[/red]")
    else:
        console.print("[yellow]Skipping ID Manager (module not found)[/yellow]")

    # 2. Fix Exam Blocks
    console.print("\n[cyan]2. Running Fix Exam Blocks...[/cyan]")
    if fix_exam_blocks:
        for f in target_files:
            try:
                fix_exam_blocks.fix_exam_blocks(f)
            except Exception as e:
                console.print(f"[red]Error fixing exams in {Path(f).name}: {e}[/red]")
    else:
        console.print("[yellow]Skipping Fix Exam Blocks (module not found)[/yellow]")

    # 3. Smart Replace Haam
    console.print("\n[cyan]3. Running Smart Replace Haam...[/cyan]")
    if smart_replace_haam:
        for f in target_files:
            try:
                if smart_replace_haam.process_file(f):
                    console.print(f"  [green]Modified:[/green] {Path(f).name}")
            except Exception as e:
                console.print(f"[red]Error replacing Haam in {Path(f).name}: {e}[/red]")
    else:
        console.print("[yellow]Skipping Smart Replace Haam (module not found)[/yellow]")

    # 4. Smart Color Fixer
    console.print("\n[cyan]4. Running Smart Color Fixer...[/cyan]")
    if smart_color_fixer:
        for f in target_files:
            try:
                smart_color_fixer.fix_colors(f)
            except Exception as e:
                console.print(f"[red]Error fixing colors in {Path(f).name}: {e}[/red]")
    else:
        console.print("[yellow]Skipping Smart Color Fixer (module not found)[/yellow]")

    # 5. Lint Pages
    console.print("\n[cyan]5. Running Lint Pages...[/cyan]")
    if lint_pages:
        # Pre-load allowed classes once
        allowed_classes = None
        styles_path = PROJECT_ROOT / "styles/main.css"
        if styles_path.exists():
            try:
                allowed_classes = lint_pages.parse_allowed_classes(str(styles_path))
            except Exception:
                pass

        # We'll use a table to show results
        table = Table(title="Lint Report", box=box.SIMPLE, show_lines=True)
        table.add_column("File", style="cyan")
        table.add_column("Errors", style="red")
        table.add_column("Warnings", style="yellow")

        files_with_issues = 0
        total_errors = 0

        for f in target_files:
            try:
                errs, warns = lint_pages.lint_file(f, allowed_classes)
                if errs:
                    files_with_issues += 1
                    total_errors += len(errs)

                    # Format for table
                    err_text = "\n".join([f"• {e}" for e in errs])
                    warn_text = "\n".join([f"• {w}" for w in warns]) if warns else "-"

                    table.add_row(Path(f).name, err_text, warn_text)
            except Exception as e:
                console.print(f"[red]Error linting {Path(f).name}: {e}[/red]")

        if files_with_issues > 0:
            console.print(table)
            console.print(
                f"\n[bold red]❌ Found {total_errors} errors in {files_with_issues} files.[/bold red]"
            )
        else:
            console.print("\n[bold green]✅ All checks passed! No lint errors.[/bold green]")
    else:
        console.print("[yellow]Skipping Lint Pages (module not found)[/yellow]")


def run_youtube_to_text():
    console.clear()
    console.print(
        Panel("[bold]📺 YouTube-to-Text Pipeline (Jules Dispatcher)[/bold]", style="blue")
    )

    url = questionary.text("Enter YouTube Video or Playlist URL:").ask()
    if not url:
        return

    from modules.jules_youtube_dispatcher import JulesYouTubeDispatcher

    try:
        dispatcher = JulesYouTubeDispatcher(PROJECT_ROOT)
    except Exception as e:
        console.print(f"[red]❌ Error initializing dispatcher: {e}[/red]")
        return

    with console.status("[bold cyan]Resolving YouTube URL...[/bold cyan]") as status:
        try:
            urls_to_process, is_playlist = dispatcher.resolve_urls(url)
        except Exception as e:
            console.print(f"[red]❌ Error resolving YouTube URL: {e}[/red]")
            return

    if not urls_to_process:
        console.print("[yellow]⚠️ No videos found or resolved from URL.[/yellow]")
        return

    console.print(f"[green]✓ Resolved {len(urls_to_process)} video(s) to process.[/green]")

    # Process sequentially
    total_videos = len(urls_to_process)

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("{task.percentage:>3.0f}%"),
        console=console,
    ) as progress:
        overall_task = progress.add_task("[cyan]Dispatching Jules Sessions...", total=total_videos)

        for idx, (video_url, video_title) in enumerate(urls_to_process):
            seq_n = (idx + 1) if is_playlist else None
            clean_title = video_title[:50] + "..." if len(video_title) > 53 else video_title

            progress.console.print(
                f"\n[bold yellow]({idx + 1}/{total_videos}) Dispatching: {clean_title}[/bold yellow]"
            )
            progress.console.print(f"[dim]{video_url}[/dim]")

            def update_status(msg):
                progress.update(overall_task, description=f"[cyan]{msg} ({clean_title})[/cyan]")

            try:
                session_name = dispatcher.dispatch_session(
                    video_url=video_url,
                    video_title=video_title,
                    seq_num=seq_n,
                    progress_callback=update_status,
                )
                progress.console.print(
                    f"[green]✅ Successfully dispatched Jules Session: {session_name}[/green]"
                )
            except Exception as e:
                progress.console.print(f"[red]❌ Failed to dispatch '{video_title}': {e}[/red]")

            progress.advance(overall_task)

    console.print("\n[bold green]🏁 YouTube-to-Text Pipeline Dispatch Completed![/bold green]")
    console.print(
        "[italic]You can monitor the sessions in the 'B) Monitor PR Auto-Merges' menu.[/italic]"
    )


# --- MAIN MENU ---


def run_local_pdf_ocr():
    console.clear()
    console.print(Panel("[bold cyan]J) Scanned PDF to Raw Text (Local OCR)[/bold cyan]", box=box.ROUNDED))
    
    pdf_path = questionary.text("Absolute path to the scanned PDF file:").ask()
    if not pdf_path or not pdf_path.strip():
        return
        
    output_path = questionary.text("Absolute path to save the extracted text (.txt):", default=str(PROJECT_ROOT / "output.txt")).ask()
    if not output_path or not output_path.strip():
        return
        
    languages = questionary.text("Languages (e.g. ara for Arabic only):", default="ara").ask()
    if not languages:
        languages = "ara"

    try:
        from modules.pdf_ocr_local import LocalPDFOCR
        ocr = LocalPDFOCR(languages=languages)
        ocr.process_pdf(pdf_path, output_path)
    except Exception as e:
        console.print(f"[red]❌ Critical Error running Local OCR: {e}[/red]")

def run_network_ai_ocr():
    console.clear()
    console.print(Panel("[bold cyan]K) Advanced Network AI OCR (Surya)[/bold cyan]", box=box.ROUNDED))
    
    pdf_path = questionary.text("Absolute path to the scanned PDF file:").ask()
    if not pdf_path or not pdf_path.strip():
        return
        
    output_path = questionary.text("Absolute path to save the extracted text (.txt):", default=str(PROJECT_ROOT / "output.txt")).ask()
    if not output_path or not output_path.strip():
        return
        
    server_ip = questionary.text("IP address of the AI Server (e.g. 192.168.1.100 or localhost):", default="localhost").ask()
    if not server_ip:
        return

    try:
        from modules.pdf_ocr_network import NetworkPDFOCR
        ocr = NetworkPDFOCR(server_ip=server_ip)
        ocr.process_pdf(pdf_path, output_path)
    except Exception as e:
        console.print(f"[red]❌ Critical Error running Network AI OCR: {e}[/red]")

def run_settings():
    console.clear()
    console.print(Panel("[bold]System Settings[/bold]", style="magenta"))
    settings_file = PROJECT_ROOT / "system-workspace" / "settings.json"

    settings = {"author": "أ. حنا خفيف", "author_number": " "}

    import json

    if settings_file.exists():
        try:
            with open(settings_file, encoding="utf-8") as f:
                settings.update(json.load(f))
        except Exception as e:
            console.print(f"[red]Failed to load settings: {e}[/red]")

    new_author = questionary.text(
        "Author Name:", default=settings.get("author", "أ. حنا خفيف")
    ).ask()
    if new_author is None:
        return

    new_author_number = questionary.text(
        "Author Number:", default=settings.get("author_number", " ")
    ).ask()
    if new_author_number is None:
        return

    settings["author"] = new_author
    settings["author_number"] = new_author_number

    try:
        with open(settings_file, "w", encoding="utf-8") as f:
            json.dump(settings, f, ensure_ascii=False, indent=4)
        console.print("[green]✅ Settings saved successfully![/green]")
    except Exception as e:
        console.print(f"[red]❌ Failed to save settings: {e}[/red]")


def run_refresh_workspace_code():
    console.clear()
    console.print(Panel("[bold]Workspace Code Settings[/bold]", style="magenta"))
    settings_file = PROJECT_ROOT / "system-workspace" / "settings.json"
    
    settings = {}
    import json
    if settings_file.exists():
        try:
            with open(settings_file, encoding="utf-8") as f:
                settings.update(json.load(f))
        except Exception as e:
            console.print(f"[red]Failed to load settings: {e}[/red]")
            
    current_code = settings.get("workspace_code", "None")
    console.print(f"Current Workspace Code: [bold cyan]{current_code}[/bold cyan]")
    
    generate_new = questionary.confirm("Do you want to generate a new 5-character workspace code?").ask()
    if generate_new:
        new_code = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
        manual_override = questionary.text("Enter a custom code or press enter to use generated:", default=new_code).ask()
        if manual_override:
            new_code = manual_override
            
        settings["workspace_code"] = new_code
        if "workspace_code_history" not in settings:
            settings["workspace_code_history"] = []
            
        settings["workspace_code_history"].append({
            "code": new_code,
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        try:
            with open(settings_file, "w", encoding="utf-8") as f:
                json.dump(settings, f, ensure_ascii=False, indent=4)
            console.print(f"[green]✅ Workspace code updated to {new_code}![/green]")
        except Exception as e:
            console.print(f"[red]❌ Failed to save settings: {e}[/red]")
            
    questionary.press_any_key_to_continue().ask()

def auto_pull_jules_batch(file_type, workspace_code):
    """Automatically pulls files for a specific Jules batch from GitHub API."""
    if not workspace_code:
        return
        
    console.print(f"\n[bold cyan]🔄 Auto-Pulling Generated Files for Workspace Code: '{workspace_code}'[/bold cyan]")
    
    token_path = PROJECT_ROOT / "secrets/Github_Token.txt"
    if not token_path.exists():
        console.print("[red]❌ secrets/Github_Token.txt not found! Cannot auto-pull.[/red]")
        return
        
    token = token_path.read_text().strip()
    import urllib.request, json, subprocess
    
    try:
        repo_url = subprocess.check_output(["git", "config", "--get", "remote.origin.url"], cwd=PROJECT_ROOT, text=True).strip()
        repo_name = repo_url.split("github.com/")[-1].replace(".git", "")
    except Exception as e:
        console.print("[red]❌ Could not detect repo name for auto-pull.[/red]")
        return
        
    console.print(f"[dim]Fetching open PRs from API for {repo_name}...[/dim]")
    url = f"https://api.github.com/repos/{repo_name}/pulls?state=open&per_page=100"
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"token {token}")
    req.add_header("Accept", "application/vnd.github.v3+json")
    
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            prs = json.loads(response.read())
    except Exception as e:
        console.print(f"[red]❌ API Request failed: {e}[/red]")
        return
        
    if not prs:
        console.print("[yellow]⚠️ No open PRs found to pull.[/yellow]")
        return
        
    found_files = []
    with console.status("Scanning PR branches for generated files...") as status:
        for pr in prs:
            branch_ref = pr['head']['ref']
            try:
                subprocess.run(["git", "fetch", "origin", f"pull/{pr['number']}/head:{branch_ref}"], cwd=PROJECT_ROOT, check=True, capture_output=True)
                diff_out = subprocess.check_output(
                    ["git", "diff", "--name-only", f"main...{branch_ref}"], 
                    cwd=PROJECT_ROOT, text=True, stderr=subprocess.DEVNULL
                )
                for f in diff_out.splitlines():
                    if not f.strip(): continue
                    if file_type == "plans" and not f.startswith("plans/"): continue
                    if file_type == "pages" and not f.startswith("pages/"): continue
                    if workspace_code.lower() not in f.lower(): continue
                    
                    found_files.append((branch_ref, f))
            except Exception as e:
                console.print(f"[dim red]DEBUG fetch PR #{pr['number']}: {e}[/dim red]")
                
    if not found_files:
        console.print("[green]✨ No generated files found waiting in PRs.[/green]")
        return
        
    console.print(f"[green]✅ Found {len(found_files)} files to auto-pull.[/green]")
    
    success = 0
    failures = []
    
    for branch, f in found_files:
        console.print(f"[dim]Pulling {f} from {branch}...[/dim]")
        try:
            subprocess.run(["git", "checkout", branch, "--", f], cwd=PROJECT_ROOT, check=True, capture_output=True)
            success += 1
        except subprocess.CalledProcessError as e:
            failures.append((branch, f))
            
    console.print(f"[bold green]Successfully pulled {success} files![/bold green]")
    
    if failures:
        fallback_dir = PROJECT_ROOT / "temp_recovered"
        fallback_dir.mkdir(exist_ok=True)
        console.print(f"[bold red]Failed to merge {len(failures)} files (Conflict/Error). Auto-recovering to temp_recovered/ ...[/bold red]")
        for branch, f in failures:
            try:
                content = subprocess.check_output(["git", "show", f"{branch}:{f}"], cwd=PROJECT_ROOT)
                out_path = fallback_dir / Path(f).name
                out_path.write_bytes(content)
                console.print(f"[green]Recovered {f} -> {out_path}[/green]")
            except Exception as e:
                console.print(f"[red]Could not recover {f}: {e}[/red]")
                
    console.print("[bold cyan]✅ Auto-Pull Complete![/bold cyan]")
    
def run_auto_smart_merging():
    console.clear()
    console.print(Panel("[bold]Auto Smart Merging/Pulling Tool[/bold]", style="cyan"))
    
    file_type = questionary.select("What are the file types?", choices=["plans", "pages"]).ask()
    if not file_type: return
    
    settings_file = PROJECT_ROOT / "system-workspace" / "settings.json"
    settings = {}
    import json
    if settings_file.exists():
        try:
            with open(settings_file, encoding="utf-8") as f:
                settings.update(json.load(f))
        except:
            pass
            
    default_code = settings.get("workspace_code", "")
    workspace_code = questionary.text("What is the workspace code? (leave empty to ignore)", default=default_code).ask()
    if workspace_code is None: return
    
    days_input = questionary.text("Fetch PRs from the last X days (leave empty for All Time):").ask()
    if days_input is None: return
    
    import datetime
    now = datetime.datetime.now(datetime.timezone.utc)
    cutoff = None
    if days_input.strip():
        try:
            days = float(days_input.strip())
            cutoff = now - datetime.timedelta(days=days)
        except ValueError:
            console.print("[yellow]Invalid number of days. Defaulting to All Time.[/yellow]")
    
    fetch_method = questionary.select(
        "Select fetch method:", 
        choices=[
            "1) Fetch OPEN PRs directly from GitHub (API)", 
            "2) Scan local branches (Old Method)"
        ]
    ).ask()
    
    if not fetch_method: return

    import subprocess
    found_files = []
    
    if fetch_method.startswith("1"):
        import urllib.request
        
        token_path = PROJECT_ROOT / "secrets/Github_Token.txt"
        if not token_path.exists():
            console.print("[red]❌ secrets/Github_Token.txt not found![/red]")
            return
            
        token = token_path.read_text().strip()
        
        try:
            repo_url = subprocess.check_output(["git", "config", "--get", "remote.origin.url"], cwd=PROJECT_ROOT, text=True).strip()
            # Handle standard https URL like https://github.com/ibrahim4433/book-arabic-grammer.git
            repo_name = repo_url.split("github.com/")[-1].replace(".git", "")
        except Exception as e:
            console.print(f"[dim red]DEBUG repo parsing: {e}[/dim red]")
            repo_name = questionary.text("Could not detect repo name. Please enter it (e.g. ibrahim4433/book-arabic-grammer):").ask()
            if not repo_name: return
            
        console.print(f"[dim]Fetching open PRs from API for {repo_name}...[/dim]")
        url = f"https://api.github.com/repos/{repo_name}/pulls?state=open&per_page=100"
        req = urllib.request.Request(url)
        req.add_header("Authorization", f"token {token}")
        req.add_header("Accept", "application/vnd.github.v3+json")
        
        try:
            with urllib.request.urlopen(req, timeout=15) as response:
                prs = json.loads(response.read())
        except Exception as e:
            console.print(f"[red]❌ API Request failed:[/red] [dim red]{e}[/dim red]")
            return
            
        if not prs:
            console.print("[yellow]⚠️ No open PRs found![/yellow]")
            return
            
        if cutoff:
            filtered_prs = []
            for pr in prs:
                try:
                    pr_date = datetime.datetime.strptime(pr['created_at'], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.timezone.utc)
                    if pr_date >= cutoff:
                        filtered_prs.append(pr)
                except Exception:
                    filtered_prs.append(pr)
            prs = filtered_prs
            
        if not prs:
            console.print("[yellow]⚠️ No PRs match the selected time filter![/yellow]")
            return
            
        pr_choices = []
        for pr in prs:
            try:
                pr_date = datetime.datetime.strptime(pr['created_at'], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.timezone.utc)
                delta = now - pr_date
                if delta.days == 0:
                    time_str = "Today"
                elif delta.days == 1:
                    time_str = "Yesterday"
                else:
                    time_str = f"{delta.days} days ago"
            except Exception:
                time_str = "Unknown time"
                
            pr_choices.append(questionary.Choice(f"[{time_str}] PR #{pr['number']}: {pr['title']} ({pr['head']['ref']})", value=pr))
            
        selected_prs = questionary.checkbox("Select PRs to process:", choices=pr_choices).ask()
        
        if not selected_prs: return
        
        with console.status("Fetching selected PR branches...") as status:
            for i, pr in enumerate(selected_prs, 1):
                status.update(f"Fetching PR #{pr['number']} ({i}/{len(selected_prs)})...")
                branch_ref = pr['head']['ref']
                try:
                    subprocess.run(["git", "fetch", "origin", f"pull/{pr['number']}/head:{branch_ref}"], cwd=PROJECT_ROOT, check=True, capture_output=True)
                    diff_out = subprocess.check_output(
                        ["git", "diff", "--name-only", f"main...{branch_ref}"], 
                        cwd=PROJECT_ROOT, text=True, stderr=subprocess.DEVNULL
                    )
                    for f in diff_out.splitlines():
                        if not f.strip(): continue
                        if file_type == "plans" and not f.startswith("plans/"): continue
                        if file_type == "pages" and not f.startswith("pages/"): continue
                        if workspace_code and workspace_code.lower() not in f.lower(): continue
                        
                        found_files.append((branch_ref, f))
                except Exception as e:
                    console.print(f"[dim red]DEBUG fetch/diff PR #{pr['number']}: {e}[/dim red]")
                    
    else:
        console.print(f"\n[cyan]🔍 Searching branches for workspace code: '{workspace_code}'[/cyan]")
        console.print("[dim]Fetching latest remote branches and PRs...[/dim]")
        try:
            subprocess.run(["git", "fetch", "--all"], cwd=PROJECT_ROOT, check=False, capture_output=True)
            subprocess.run(["git", "fetch", "origin", "+refs/pull/*/head:refs/remotes/origin/pr/*"], cwd=PROJECT_ROOT, check=False, capture_output=True)
        except Exception as e:
            console.print(f"[dim red]DEBUG fetch: {e}[/dim red]")
            
        try:
            branches_out = subprocess.check_output(["git", "branch", "-a"], cwd=PROJECT_ROOT, text=True)
            branches = []
            for b in branches_out.splitlines():
                b = b.strip().replace("* ", "")
                if "->" in b: continue
                branches.append(b)
                
            target_branches = [b for b in branches if "pr-" in b.lower() or "pr/" in b.lower() or "jules" in b.lower()]
            if not target_branches:
                target_branches = branches
                
            if cutoff:
                filtered_branches = []
                with console.status("Filtering branches by date..."):
                    for b in target_branches:
                        try:
                            d_out = subprocess.check_output(["git", "log", "-1", "--format=%cI", b], cwd=PROJECT_ROOT, text=True, stderr=subprocess.DEVNULL).strip()
                            if d_out:
                                b_date = datetime.datetime.fromisoformat(d_out)
                                # b_date may be offset-aware. cutoff is utc-aware.
                                if b_date >= cutoff:
                                    filtered_branches.append(b)
                        except Exception:
                            filtered_branches.append(b)
                target_branches = filtered_branches
                
            with console.status("Scanning branches..."):
                for branch in target_branches:
                    try:
                        diff_out = subprocess.check_output(
                            ["git", "diff", "--name-only", f"main...{branch}"], 
                            cwd=PROJECT_ROOT, text=True, stderr=subprocess.DEVNULL
                        )
                        for f in diff_out.splitlines():
                            if not f.strip(): continue
                            if file_type == "plans" and not f.startswith("plans/"): continue
                            if file_type == "pages" and not f.startswith("pages/"): continue
                            if workspace_code and workspace_code.lower() not in f.lower(): continue
                            
                            found_files.append((branch, f))
                    except Exception as e:
                        console.print(f"[dim red]DEBUG diff branch {branch}: {e}[/dim red]")
        except Exception as e:
            console.print(f"[dim red]DEBUG branch parsing: {e}[/dim red]")
            
    if not found_files:
        console.print(f"[yellow]⚠️ No files found matching filters.[/yellow]")
    else:
        # Filter found_files based on existence
        filter_type = questionary.select(
            "Filter findings:",
            choices=[
                "1) Show ALL files",
                "2) Only show NEW files (Do not exist locally)",
                "3) Only show EXISTING files (Already exist locally)"
            ]
        ).ask()
        
        if not filter_type: return
        
        filtered_files = []
        for branch, f in found_files:
            exists = (PROJECT_ROOT / f).exists()
            if filter_type.startswith("2") and exists:
                continue
            if filter_type.startswith("3") and not exists:
                continue
            filtered_files.append((branch, f))
            
        if not filtered_files:
            console.print("[yellow]⚠️ No files left after filtering.[/yellow]")
            return
            
        console.print(f"[green]✅ Found {len(filtered_files)} candidate files.[/green]")
        file_choices = [questionary.Choice(f"{f} (from {b})", value=(b, f)) for b, f in filtered_files]
        
        selected_files = questionary.checkbox("Select files to merge/pull:", choices=file_choices).ask()
        if not selected_files:
            console.print("[yellow]Aborted by user.[/yellow]")
            return
            
        dest_choice = questionary.select(
            "Where to save selected files?",
            choices=[
                "1) Pull to their actual places (Standard Git Checkout)",
                "2) Extract to temp folder (temp_recovered/)",
                "3) Extract to custom path..."
            ]
        ).ask()
        if not dest_choice: return
        
        target_dir = None
        if dest_choice.startswith("2"):
            target_dir = PROJECT_ROOT / "temp_recovered"
        elif dest_choice.startswith("3"):
            custom_path = questionary.text("Enter custom path (relative to project root):").ask()
            if not custom_path: return
            target_dir = PROJECT_ROOT / custom_path
            
        if target_dir:
            target_dir.mkdir(parents=True, exist_ok=True)
            
        success = 0
        failures = []
        
        for branch, f in selected_files:
            console.print(f"[dim]Processing {f} from {branch}...[/dim]")
            if target_dir:
                try:
                    content = subprocess.check_output(["git", "show", f"{branch}:{f}"], cwd=PROJECT_ROOT)
                    out_path = target_dir / Path(f).name
                    out_path.write_bytes(content)
                    console.print(f"[green]Saved to {out_path}[/green]")
                    success += 1
                except Exception as e:
                    console.print(f"[dim red]DEBUG extract {f}: {e}[/dim red]")
                    failures.append((branch, f))
            else:
                try:
                    subprocess.run(["git", "checkout", branch, "--", f], cwd=PROJECT_ROOT, check=True, capture_output=True)
                    success += 1
                except subprocess.CalledProcessError as e:
                    console.print(f"[dim red]DEBUG checkout {f}: {e.stderr if hasattr(e, 'stderr') else e}[/dim red]")
                    failures.append((branch, f))
                
        console.print(f"\n[bold green]Successfully processed {success} files![/bold green]")
        if failures:
            console.print(f"[bold red]Failed to process {len(failures)} files:[/bold red]")
            for _, f in failures:
                console.print(f" - {f}")
            if not target_dir:
                force = questionary.confirm("Force download problematic files to a temp folder?").ask()
                if force:
                    fallback_dir = PROJECT_ROOT / "temp_recovered"
                    fallback_dir.mkdir(exist_ok=True)
                    for branch, f in failures:
                        try:
                            content = subprocess.check_output(["git", "show", f"{branch}:{f}"], cwd=PROJECT_ROOT)
                            out_path = fallback_dir / Path(f).name
                            out_path.write_bytes(content)
                            console.print(f"[green]Recovered to {out_path}[/green]")
                        except Exception as e:
                            console.print(f"[red]Could not recover {f}: {e}[/red]")
        
    questionary.press_any_key_to_continue().ask()


def main():
    state_manager = StateManager(PROJECT_ROOT)

    menu_style = questionary.Style(
        [
            ("qmark", "fg:#673ab7 bold"),
            ("question", "bold"),
            ("answer", "fg:#f44336 bold"),
            ("pointer", "fg:#673ab7 bold"),
            ("highlighted", "fg:#673ab7 bold"),
            ("selected", "fg:#cc5454"),
            ("separator", "fg:#cc5454"),
            ("instruction", ""),
            ("text", ""),
            ("disabled", "fg:#858585 italic"),
        ]
    )

    while True:
        print_header()

        # 1. Show Status Dashboard
        display_status_table(state_manager)
        console.print("")

        # 2. Main Menu
        main_choice = questionary.select(
            "Select Category:",
            choices=[
                "1) book making by 1-lesson-1-plan method",
                "2) book making by 1-page-1-plan method",
                "3) OCR tools",
                "4) Book Style Tuning",
                "5) Settings",
                "6) Clear History",
                "7) auto smart merging/pulling tool",
                "8) refresh workspace code",
                "9) Quit",
            ],
            style=menu_style,
        ).ask()

        if not main_choice or main_choice.startswith("9"):
            console.print("Goodbye.")
            sys.exit(0)

        start_op = time.time()
        op_ran = False
        
        main_op = main_choice[0]

        if main_op == "1":
            sub_choice = questionary.select(
                "Select Operation (1-lesson-1-plan):",
                choices=[
                    "A) Full Auto Workflow",
                    "B) Raw Processing (Merge & Index)",
                    "C) Plan Generation (Jules Batch)",
                    "D) Plan Generation (Standard)",
                    "E) Page Generation (Jules Batch)",
                    "F) Audit & Verify Pages",
                    "G) Retry batch planning / generation to selected lessons",
                    "X) Back to Main Menu",
                ],
                style=menu_style,
            ).ask()
            
            if sub_choice and not sub_choice.startswith("X"):
                sub_op = sub_choice[0]
                op_ran = True
                if sub_op == "A":
                    run_full_auto_ui(state_manager)
                elif sub_op == "B":
                    run_raw_processing(state_manager)
                elif sub_op == "C":
                    run_jules_planning_ui(state_manager)
                elif sub_op == "D":
                    run_planning(state_manager)
                elif sub_op == "E":
                    run_jules_generation_ui(state_manager)
                elif sub_op == "F":
                    run_audit_and_verify(state_manager)
                elif sub_op == "G":
                    run_retry_planning_and_generation_ui(state_manager)
                
        elif main_op == "2":
            sub_choice = questionary.select(
                "Select Operation (1-page-1-plan):",
                choices=[
                    "A) Full Auto Workflow",
                    "B) Raw Processing (Auto-Paginated Index & TOC)",
                    "C) Plan Generation (Jules Batch - 1-to-1 Page Mapping)",
                    "D) Page Generation (Jules Batch - 1-to-1 Page Mapping)",
                    "E) Audit & Verify Pages",
                    "F) Retry batch planning / generation to selected lessons",
                    "X) Back to Main Menu",
                ],
                style=menu_style,
            ).ask()
            
            if sub_choice and not sub_choice.startswith("X"):
                sub_op = sub_choice[0]
                op_ran = True
                if sub_op == "A":
                    run_full_auto_ui(state_manager, is_1_page_mode=True)
                elif sub_op == "B":
                    run_raw_processing_auto(state_manager)
                elif sub_op == "C":
                    run_jules_planning_ui(state_manager, is_1_page_mode=True)
                elif sub_op == "D":
                    run_jules_generation_ui(state_manager, is_1_page_mode=True)
                elif sub_op == "E":
                    run_audit_and_verify(state_manager)
                elif sub_op == "F":
                    run_retry_planning_and_generation_ui(state_manager)

        elif main_op == "3":
            sub_choice = questionary.select(
                "Select Operation (OCR tools):",
                choices=[
                    "A) Images -> Raw ( JULES )",
                    "B) Images -> Raw ( API/CLI )",
                    "C) Images -> Raw ( Local-utilities )",
                    "D) Images -> Raw ( Local-AI-network )",
                    "E) Video / Youtube -> Raw",
                    "X) Back to Main Menu",
                ],
                style=menu_style,
            ).ask()
            
            if sub_choice and not sub_choice.startswith("X"):
                sub_op = sub_choice[0]
                op_ran = True
                if sub_op == "A":
                    run_jules_ocr_ui(state_manager)
                elif sub_op == "B":
                    run_ocr(state_manager)
                elif sub_op == "C":
                    run_local_pdf_ocr()
                elif sub_op == "D":
                    run_network_ai_ocr()
                elif sub_op == "E":
                    run_jules_youtube_ui(state_manager)

        elif main_op == "4":
            op_ran = True
            run_calibration_ui(state_manager, PROJECT_ROOT)
            
        elif main_op == "5":
            op_ran = True
            run_settings()
            
        elif main_op == "6":
            if questionary.confirm("Are you sure you want to completely clear the project state history?").ask():
                state_manager.state = {"lessons": {}}
                state_manager.save_state()
                console.print("[green]✅ History database cleared successfully![/green]")
            op_ran = True

        elif main_op == "7":
            op_ran = True
            run_auto_smart_merging()
            
        elif main_op == "8":
            op_ran = True
            run_refresh_workspace_code()

        if op_ran:
            console.print(
                f"\n[dim]Total operation time: {format_duration(time.time() - start_op)}[/dim]"
            )
            console.print("\n")
            questionary.press_any_key_to_continue().ask()


if __name__ == "__main__":
    main()
