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
    from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
    from rich import box
    import questionary
except ImportError:
    print("❌ Missing UI libraries. Please run: pip install rich questionary")
    sys.exit(1)

# --- CONFIGURATION ---
PROJECT_ROOT = Path(__file__).parent.resolve()
MODULES_PATH = PROJECT_ROOT / "system-workspace/tools/automation"
sys.path.append(str(MODULES_PATH))

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
except ImportError as e:
    logging.critical(f"Failed to import modules: {e}")
    print("❌ Critical Error: Failed to import modules. See system.log for details.")
    sys.exit(1)

console = Console()

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
    
    planner = JulesPlanner(PROJECT_ROOT)
    
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
        elif op == "F":
            run_jules_generation_ui(state_manager)
        elif op == "B":
            run_ocr(state_manager)
        elif op == "C":
            run_raw_processing(state_manager)
        elif op == "D":
            run_planning(state_manager)
        elif op == "G":
            console.clear()
            console.print("[bold]Running Audit...[/bold]")
            subprocess.run(["python3", "Jules-workspace/lint_pages.py"], check=False)
        
        if op != "Q":
            console.print(f"\n[dim]Total operation time: {format_duration(time.time() - start_op)}[/dim]")
            console.print("\n")
            questionary.press_any_key_to_continue().ask()

if __name__ == "__main__":
    main()
