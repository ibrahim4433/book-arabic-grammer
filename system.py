#!/usr/bin/env python3
import sys
import re
import subprocess
import logging
import time
import threading
from pathlib import Path

# --- RICH & UI IMPORTS ---
try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.live import Live
    from rich.layout import Layout
    from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
    from rich import box
    import questionary
except ImportError:
    print("❌ Missing UI libraries. Please run: pip install rich questionary")
    sys.exit(1)

# --- CONFIGURATION ---
PROJECT_ROOT = Path(__file__).parent.resolve()
MODULES_PATH = PROJECT_ROOT / "system-workspace/tools/automation"
JULES_WORKSPACE_PATH = PROJECT_ROOT / "Jules-workspace"
sys.path.append(str(MODULES_PATH))
sys.path.append(str(JULES_WORKSPACE_PATH))

# --- LOGGING SETUP ---
# Redirect logs to file so they don't break the UI
logging.basicConfig(
    filename='system.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w'
)

# --- MODULE IMPORTS ---
try:
    from modules.vision import VisionClient
    from modules.text_processing import TextProcessor
    from modules.planner import Planner
    from modules.jules_planner import JulesPlanner
    from modules.state_manager import StateManager
    from modules.jules_page_generator import JulesPageGenerator
    from modules.full_auto_workflow import FullAutoWorkflow
    from modules.jules_ocr import JulesOCR
except ImportError as e:
    logging.critical(f"Failed to import modules: {e}")
    print("❌ Critical Error: Failed to import modules. See system.log for details.")
    sys.exit(1)

# Import Jules Workspace Tools
try:
    import id_manager
    import lint_pages
    import fix_exam_blocks
    import smart_replace_haam
    import smart_color_fixer
except ImportError as e:
    print(f"⚠️ Warning: Could not import Jules Workspace tools: {e}")

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
    console.print(Panel.fit(
        "[bold cyan]📘 ARABIC GRAMMAR BOOK - CONTROL ROOM (V3)[/bold cyan]\n"
        f"[dim]Project Root: {PROJECT_ROOT}[/dim]",
        box=box.ROUNDED,
        border_style="cyan"
    ))

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
        if files.get("raw"): artifacts.append("📄 Raw")
        if files.get("plan"): artifacts.append("📝 Plan")
        if files.get("html"): artifacts.append("🌐 HTML")
        
        # Format timestamp
        ts = info.get("last_updated", 0)
        time_str = time.strftime('%H:%M', time.localtime(ts)) if ts else "-"

        # Try to extract title from key or original key if the key is just a number
        title = info.get('original_key', key)
        # Clean up title for display
        clean_title = re.sub(r'^\d+\s*-\s*', '', title).strip()
        if key.isdigit() and clean_title == key:
            clean_title = "Unknown Title"

        # Colorize Status
        status_style = "white"
        if "PASS" in status: status_style = "green"
        elif "READY" in status: status_style = "blue"
        elif "FAIL" in status: status_style = "red"

        table.add_row(
            key if key.isdigit() else "-",
            clean_title,
            f"[{status_style}]{status}[/{status_style}]",
            " ".join(artifacts),
            time_str
        )

    console.print(table)

# --- WORKFLOW HANDLERS ---

def run_jules_planning_ui(state_manager):
    console.clear() # Clear screen for App-like feel
    console.print("[bold cyan]🚀 Starting Jules Batch Planning...[/bold cyan]")
    
    planner = JulesPlanner(PROJECT_ROOT, state_manager=state_manager)
    
    tasks = {} # title -> {status, message, start_time, duration}
    lock = threading.Lock()

    def generate_table():
        table = Table(title="Planning Progress", box=box.ROUNDED, expand=True)
        table.add_column("Lesson", style="cyan")
        table.add_column("Status", style="bold")
        table.add_column("Message", style="dim", width=60)
        table.add_column("Duration", style="yellow", justify="right")

        with lock:
            sorted_tasks = sorted(tasks.items()) # Stable sort

        for title, data in sorted_tasks:
            status = data['status']
            status_color = "white"
            if status == "SUCCESS": status_color = "green"
            elif status == "FAILED": status_color = "red"
            elif status == "RUNNING": status_color = "yellow"
            elif status in ["MERGING", "PULLING"]: status_color = "magenta"

            # Calculate Duration
            duration_str = "-"
            if 'duration' in data:
                duration_str = format_duration(data['duration'])
            elif 'start_time' in data:
                duration_str = format_duration(time.time() - data['start_time'])

            table.add_row(
                title,
                f"[{status_color}]{status}[/{status_color}]",
                data['message'],
                duration_str
            )

        return table

    # Initialize Live with the initial table
    start_all = time.time()
    with Live(generate_table(), refresh_per_second=4) as live:

        def callback(title, status, msg):
            with lock:
                if title not in tasks:
                    tasks[title] = {}

                tasks[title]['status'] = status
                tasks[title]['message'] = msg

                if status == "RUNNING":
                    if 'start_time' not in tasks[title]:
                        tasks[title]['start_time'] = time.time()
                elif status in ["SUCCESS", "FAILED", "SKIP", "WARN", "ERROR"]:
                    if 'start_time' in tasks[title]:
                        tasks[title]['duration'] = time.time() - tasks[title]['start_time']
                    else:
                        tasks[title]['duration'] = 0.0

            live.update(generate_table())

        planner.run_batch_planning(max_concurrent=5, update_callback=callback)
    
    total_duration = time.time() - start_all
    console.print(f"[bold green]✅ Batch Planning Completed in {format_duration(total_duration)}![/bold green]")

def run_jules_generation_ui(state_manager):
    console.clear() # Clear screen for App-like feel
    console.print("[bold cyan]🚀 Starting Jules Page Generation...[/bold cyan]")
    
    generator = JulesPageGenerator(PROJECT_ROOT)
    
    tasks = {}
    lock = threading.Lock()

    def generate_table():
        table = Table(title="Generation Progress", box=box.ROUNDED, expand=True)
        table.add_column("Lesson", style="cyan")
        table.add_column("Status", style="bold")
        table.add_column("Details", style="dim", width=60)
        table.add_column("Duration", style="yellow", justify="right")
        
        with lock:
            sorted_tasks = sorted(tasks.items())

        for title, data in sorted_tasks:
            s = data['status']
            color = "white"
            if s == "RUNNING": color = "yellow"
            elif s == "SUCCESS": color = "green"
            elif s == "FAILED": color = "red"
            elif s == "INTERACT": color = "magenta"
            elif s in ["MERGING", "PULLING"]: color = "cyan"
            
            # Calculate Duration
            duration_str = "-"
            if 'duration' in data:
                duration_str = format_duration(data['duration'])
            elif 'start_time' in data:
                duration_str = format_duration(time.time() - data['start_time'])

            table.add_row(title, f"[{color}]{s}[/{color}]", data['message'], duration_str)
        return table

    # Initialize Live with the initial table
    start_all = time.time()
    with Live(generate_table(), refresh_per_second=4) as live:

        def callback(title, status, msg):
            with lock:
                if title not in tasks:
                    tasks[title] = {}

                tasks[title]['status'] = status
                tasks[title]['message'] = msg

                if status == "RUNNING":
                    if 'start_time' not in tasks[title]:
                        tasks[title]['start_time'] = time.time()
                elif status in ["SUCCESS", "FAILED", "SKIP", "WARN", "ERROR"]:
                    if 'start_time' in tasks[title]:
                        tasks[title]['duration'] = time.time() - tasks[title]['start_time']
                    else:
                        tasks[title]['duration'] = 0.0

            live.update(generate_table())

        generator.run_batch_generation(max_concurrent=5, update_callback=callback)

    total_duration = time.time() - start_all
    console.print(f"[bold green]✅ Batch Generation Completed in {format_duration(total_duration)}![/bold green]")

def run_jules_ocr_ui(state_manager):
    console.clear()
    console.print("[bold cyan]🚀 Starting Jules Batch OCR (One Session)...[/bold cyan]")

    ocr = JulesOCR(PROJECT_ROOT)

    ui_state = {
        "status": "INIT",
        "message": "Initializing..."
    }
    lock = threading.Lock()

    def generate_display():
        with lock:
            s = ui_state["status"]
            m = ui_state["message"]

        color = "white"
        if s == "RUNNING": color = "yellow"
        elif s == "SUCCESS": color = "green"
        elif s == "FAILED": color = "red"
        elif s == "ERROR": color = "red"

        return Panel(
            f"[bold {color}]Status: {s}[/bold {color}]\n{m}",
            title="Jules OCR Progress",
            box=box.ROUNDED,
            border_style=color
        )

    start_time = time.time()
    with Live(generate_display(), refresh_per_second=4) as live:

        def callback(status, msg):
            with lock:
                ui_state["status"] = status
                ui_state["message"] = msg
            live.update(generate_display())

        ocr.run_ocr_batch(update_callback=callback)

    console.print(f"[bold green]✅ OCR Batch Completed in {format_duration(time.time() - start_time)}![/bold green]")

def run_full_auto_ui(state_manager):
    console.clear()
    console.print("[bold cyan]🚀 Starting Full Auto Workflow...[/bold cyan]")
    console.print("[dim]Press Ctrl+C to Pause/Stop[/dim]")

    # Init workflow
    workflow = FullAutoWorkflow(PROJECT_ROOT, state_manager)

    # Ask for starting point
    start_choice = questionary.select(
        "Select Starting Point:",
        choices=[
            "1. Start normally",
            "Start from Raw Processing",
            "Start from Unified Generation"
        ],
        style=questionary.Style([
            ('qmark', 'fg:#673ab7 bold'),
            ('question', 'bold'),
            ('answer', 'fg:#f44336 bold'),
            ('pointer', 'fg:#673ab7 bold'),
            ('highlighted', 'fg:#673ab7 bold'),
            ('selected', 'fg:#cc5454'),
            ('separator', 'fg:#cc5454'),
            ('instruction', ''),
            ('text', ''),
            ('disabled', 'fg:#858585 italic')
        ])
    ).ask()

    if not start_choice:
        return

    if start_choice == "Start from Raw Processing":
        workflow.jump_to_step("RAW_PROC")
    elif start_choice == "Start from Unified Generation":
        workflow.jump_to_step("UNIFIED_GEN")

    # Shared state for UI
    ui_state = {
        "history": [],
        "last_update": time.time()
    }
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
                Layout(name="footer", size=10)
            )

            current_step = self.workflow.get_current_step_name()
            layout["header"].update(Panel(
                f"[bold cyan]Full Auto Workflow - {current_step}[/bold cyan]",
                style="bold white",
                box=box.ROUNDED
            ))

            layout["main"].update(Panel(self.generate_timeline(), box=box.ROUNDED))

            with self.lock:
                hist = list(self.ui_state["history"])

            log_text = ""
            for ts, s, st, m in hist:
                c = "white"
                if st == "SUCCESS": c = "green"
                elif st == "WARN": c = "yellow"
                elif st == "ERROR": c = "red"
                elif st == "DOWN": c = "cyan"
                elif st == "MISS": c = "magenta"
                elif st == "START": c = "blue"
                log_text += f"[{c}]{ts} [{s}] {st}: {m}[/{c}]\n"

            layout["footer"].update(Panel(log_text, title="Log History", box=box.SIMPLE))
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
                s_id = step['id']
                if s_id in self.workflow.step_timings:
                    meta = self.workflow.step_timings[s_id]
                    status = meta['status']
                else:
                    meta = {"status": "PENDING", "start_time": None, "end_time": None, "duration": 0}
                    status = "PENDING"

                s_color = "white"
                if status == "SUCCESS": s_color = "green"
                elif status == "RUNNING": s_color = "yellow"
                elif status == "FAILED": s_color = "red"
                elif status == "PAUSED": s_color = "magenta"
                elif status == "PENDING": s_color = "dim"

                start_s = time.strftime('%H:%M:%S', time.localtime(meta['start_time'])) if meta['start_time'] else "-"
                end_s = time.strftime('%H:%M:%S', time.localtime(meta['end_time'])) if meta['end_time'] else "-"

                if status == "RUNNING" and meta.get('start_time'):
                    dur_s = format_duration(time.time() - meta['start_time'])
                else:
                    dur_s = format_duration(meta['duration']) if meta.get('duration', 0) > 0 else "-"

                table.add_row(step['label'], f"[{s_color}]{status}[/{s_color}]", start_s, end_s, dur_s)
            return table

    def callback(step, status, message):
        with lock:
            if status in ["SUCCESS", "WARN", "ERROR", "MISS", "DOWN", "START", "MERGE", "INDEX", "GEN", "AUDIT"]:
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
                with Live(display_instance, refresh_per_second=4, console=console) as live:
                    # Start workflow
                    stats = workflow.run(skip_archive=skip_archive)

                # If we get here, it finished successfully
                # We need to temporarily restore stdout to print the final report to screen
                sys.stdout = original_stdout
                console.print("[bold green]✅ Full Auto Workflow Completed Successfully![/bold green]")

                # Show Final Report
                table = Table(title="Final Workflow Report", box=box.ROUNDED)
                table.add_column("Metric", style="cyan")
                table.add_column("Value", style="bold white")
                for k, v in stats.items():
                    if isinstance(v, list): v = f"{len(v)} ({', '.join(map(str, v[:5]))}...)"
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
                    "Quit"
                ]

                action = questionary.select(
                    "Paused. What would you like to do?",
                    choices=choices
                ).ask()

                if not action or action.startswith("Quit"):
                    return

                elif action.startswith("Resume"):
                    skip_archive = True # Usually we don't want to archive again if we resume
                    console.print("[dim]Resuming...[/dim]")
                    # Go back to redirecting stdout
                    sys.stdout = StreamLogger(logging.getLogger(), logging.INFO)

                elif action.startswith("Restart"):
                    skip_archive = False
                    workflow = FullAutoWorkflow(PROJECT_ROOT, state_manager) # Reset
                    workflow.callback = callback
                    ui_state["history"] = []
                    console.print("[dim]Restarting...[/dim]")
                    # Go back to redirecting stdout
                    sys.stdout = StreamLogger(logging.getLogger(), logging.INFO)

                elif action.startswith("Re-do Previous"):
                    if workflow.redo_previous_step():
                        console.print("[green]Rewound to previous step.[/green]")
                        skip_archive = True # Don't archive again if jumping back inside
                    else:
                        console.print("[red]Cannot go back (already at start).[/red]")
                        time.sleep(1)
                    # Go back to redirecting stdout
                    sys.stdout = StreamLogger(logging.getLogger(), logging.INFO)

                elif action.startswith("Jump to Step"):
                    steps = [s['label'] for s in workflow.get_steps()]
                    target = questionary.select("Select Step to Jump to:", choices=steps).ask()
                    if target:
                        workflow.jump_to_step(target)
                        skip_archive = True # Assume skip archive if jumping around
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
    console.clear() # Clear screen
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
                out_file.write_text(text, encoding='utf-8')
                progress.console.print(f"[green]✅ Saved: {out_file.name}[/green]")
                state_manager.update_lesson_status(f"Image_{img.stem}", "OCR_DONE", {"raw": str(out_file)})
            else:
                progress.console.print(f"[red]❌ Failed: {img.name}[/red]")
            
            progress.advance(task)

    console.print(f"[bold green]✅ OCR Completed in {format_duration(time.time() - start_time)}![/bold green]")

def run_raw_processing(state_manager):
    console.clear()
    console.print(Panel("[bold]Running Raw Processing...[/bold]", style="blue"))
    
    start_time = time.time()
    with console.status("[bold green]Processing...[/bold green]", spinner="dots"):
        tp = TextProcessor()
        if not tp.validate_toc(): return

        console.print("1. Merging Raw Text...")
        merged_path = tp.merge_raw_text()
        if not merged_path: return

        console.print("2. Generating Lesson Index...")
        mapping = tp.generate_lesson_index()
        if mapping:
            console.print(f"[bold green]✅ Raw Processing Complete in {format_duration(time.time() - start_time)}![/bold green]")

def run_planning(state_manager):
    console.clear()
    console.print(Panel("[bold]Running Standard Planner...[/bold]", style="blue"))
    
    start_time = time.time()
    with console.status("[bold green]Initializing...[/bold green]", spinner="dots"):
        tp = TextProcessor(use_headless=True)
        if not tp.validate_toc(): return

        console.print("1. Merging Raw Text...")
        merged_path = tp.merge_raw_text()
        if not merged_path: return
        
        console.print("2. Generating Lesson Index...")
        mapping = tp.generate_lesson_index()
        if not mapping: return
    
    planner = Planner()
    
    with Progress() as progress:
        task = progress.add_task("[cyan]Generating Plans...", total=len(mapping))
        
        for lesson_title, range_info in mapping.items():
            lesson_number = tp.get_lesson_number(lesson_title)
            clean_title = re.sub(r'^\d+\s*-\s*', '', lesson_title).strip()
            
            plan_filename = f"{lesson_number}-{clean_title}-plan.md"
            plan_path = planner.generate_plan(
                raw_lesson_text=merged_path.read_text(encoding='utf-8'),
                output_filename=plan_filename,
                lesson_number=lesson_number,
                lesson_title=clean_title
            )
            
            if plan_path:
                state_manager.update_lesson_status(lesson_number, "PLAN_READY", {"plan": str(plan_path)})
                progress.console.print(f"[green]✅ Plan: {plan_filename}[/green]")
            
            progress.advance(task)

    console.print(f"[bold green]✅ Standard Planning Completed in {format_duration(time.time() - start_time)}![/bold green]")

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
        "00.2_n02_toc_p2.html"
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
    try:
        # Initialize IDManager with root_dir so it scans ALL files for uniqueness
        manager = id_manager.IDManager(root_dir=str(pages_dir))
        # But only auto-tag the target files
        manager.auto_tag(files=target_files)
    except Exception as e:
        console.print(f"[red]Error in ID Manager: {e}[/red]")

    # 2. Fix Exam Blocks
    console.print("\n[cyan]2. Running Fix Exam Blocks...[/cyan]")
    for f in target_files:
        try:
            fix_exam_blocks.fix_exam_blocks(f)
        except Exception as e:
            console.print(f"[red]Error fixing exams in {Path(f).name}: {e}[/red]")

    # 3. Smart Replace Haam
    console.print("\n[cyan]3. Running Smart Replace Haam...[/cyan]")
    for f in target_files:
        try:
            if smart_replace_haam.process_file(f):
                console.print(f"  [green]Modified:[/green] {Path(f).name}")
        except Exception as e:
            console.print(f"[red]Error replacing Haam in {Path(f).name}: {e}[/red]")

    # 4. Smart Color Fixer
    console.print("\n[cyan]4. Running Smart Color Fixer...[/cyan]")
    for f in target_files:
        try:
            smart_color_fixer.fix_colors(f)
        except Exception as e:
            console.print(f"[red]Error fixing colors in {Path(f).name}: {e}[/red]")

    # 5. Lint Pages
    console.print("\n[cyan]5. Running Lint Pages...[/cyan]")

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
        console.print(f"\n[bold red]❌ Found {total_errors} errors in {files_with_issues} files.[/bold red]")
    else:
        console.print("\n[bold green]✅ All checks passed! No lint errors.[/bold green]")

# --- MAIN MENU ---

def main():
    state_manager = StateManager(PROJECT_ROOT)

    while True:
        print_header()
        
        # 1. Show Status Dashboard
        display_status_table(state_manager)
        console.print("")

        # 2. Questionary Menu
        choice = questionary.select(
            "Select Operation:",
            choices=[
                "A) Full Auto Workflow",
                "B) OCR Only (Images -> Raw)",
                "C) Raw Processing (Merge & Index)",
                "D) Plan Generation (Standard)",
                "E) Plan Generation (Jules Batch)",
                "F) Page Generation (Jules Batch)",
                "G) Audit & Verify Pages",
                "H) OCR Only by Jules (Images -> Raw)",
                "Q) Quit"
            ],
            style=questionary.Style([
                ('qmark', 'fg:#673ab7 bold'),
                ('question', 'bold'),
                ('answer', 'fg:#f44336 bold'),
                ('pointer', 'fg:#673ab7 bold'),
                ('highlighted', 'fg:#673ab7 bold'),
                ('selected', 'fg:#cc5454'),
                ('separator', 'fg:#cc5454'),
                ('instruction', ''),
                ('text', ''),
                ('disabled', 'fg:#858585 italic')
            ])
        ).ask()

        if not choice or choice.startswith("Q"):
            console.print("Goodbye.")
            sys.exit(0)

        op = choice[0]

        start_op = time.time()

        if op == "E":
            run_jules_planning_ui(state_manager)
        elif op == "A":
            run_full_auto_ui(state_manager)
        elif op == "F":
            run_jules_generation_ui(state_manager)
        elif op == "B":
            run_ocr(state_manager)
        elif op == "C":
            run_raw_processing(state_manager)
        elif op == "D":
            run_planning(state_manager)
        elif op == "G":
            run_audit_and_verify(state_manager)
        elif op == "H":
            run_jules_ocr_ui(state_manager)
        
        if op != "Q":
            console.print(f"\n[dim]Total operation time: {format_duration(time.time() - start_op)}[/dim]")
            console.print("\n")
            questionary.press_any_key_to_continue().ask()

if __name__ == "__main__":
    main()
