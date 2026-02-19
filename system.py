#!/usr/bin/env python3
import sys
import os
import json
import re
import subprocess
from pathlib import Path
import time

# --- RICH & UI IMPORTS ---
try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.layout import Layout
    from rich.live import Live
    from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
    from rich import box
    import questionary
except ImportError:
    print("❌ Missing UI libraries. Please run: pip install rich questionary")
    sys.exit(1)

# --- CONFIGURATION ---
PROJECT_ROOT = Path(__file__).parent.resolve()
MODULES_PATH = PROJECT_ROOT / "system workspace/tools/automation"
sys.path.append(str(MODULES_PATH))

# --- MODULE IMPORTS ---
try:
    from modules.vision import VisionClient
    from modules.text_processing import TextProcessor
    from modules.planner import Planner
    from modules.jules_planner import JulesPlanner
    from modules.compiler import Compiler
    from modules.auditor import Auditor
    from modules.state_manager import StateManager
    from modules.jules_page_generator import JulesPageGenerator
except ImportError as e:
    print(f"❌ Critical Error: Failed to import modules. Details: {e}")
    sys.exit(1)

console = Console()

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
    console.print("[bold cyan]🚀 Starting Jules Batch Planning...[/bold cyan]")
    
    planner = JulesPlanner(PROJECT_ROOT)
    
    # Live Table for Status
    progress_table = Table(title="Planning Progress", box=box.ROUNDED)
    progress_table.add_column("Lesson", style="cyan")
    progress_table.add_column("Status", style="bold")
    progress_table.add_column("Message", style="dim", width=50)
    
    # Store dynamic state
    tasks = {} # title -> {status, message}

    def update_ui():
        # Rebuild table rows
        progress_table.rows = [] # Clear rows
        for title, data in tasks.items():
            status_color = "yellow"
            if data['status'] == "SUCCESS": status_color = "green"
            elif data['status'] == "FAILED": status_color = "red"
            
            progress_table.add_row(title, f"[{status_color}]{data['status']}[/{status_color}]", data['message'])

    def callback(title, status, msg):
        tasks[title] = {"status": status, "message": msg}
        # Note: In a real async loop we'd await, but here threads update 'tasks' dict
        # and 'Live' context refreshes automatically.

    with Live(progress_table, refresh_per_second=4):
        planner.run_batch_planning(max_concurrent=5, update_callback=callback)
    
    console.print("[bold green]✅ Batch Planning Completed![/bold green]")

def run_jules_generation_ui(state_manager):
    console.print("[bold cyan]🚀 Starting Jules Page Generation...[/bold cyan]")
    
    generator = JulesPageGenerator(PROJECT_ROOT)
    
    progress_table = Table(title="Generation Progress", box=box.ROUNDED)
    progress_table.add_column("Lesson", style="cyan")
    progress_table.add_column("Status", style="bold")
    progress_table.add_column("Details", style="dim", width=60)
    
    tasks = {}

    def callback(title, status, msg):
        tasks[title] = {"status": status, "message": msg}

    # Custom loop to update table from 'tasks' dict
    # Since 'Live' calls the renderable, we need a wrapper or just update the table object
    # But table rows are static once added. We need to generate a NEW table each refresh
    # or use a Layout.
    # Simpler approach: A function that returns the table.
    
    def generate_table():
        table = Table(title="Generation Progress", box=box.ROUNDED)
        table.add_column("Lesson", style="cyan")
        table.add_column("Status", style="bold")
        table.add_column("Details", style="dim", width=60)
        
        for title, data in tasks.items():
            s = data['status']
            color = "white"
            if s == "RUNNING": color = "yellow"
            elif s == "SUCCESS": color = "green"
            elif s == "FAILED": color = "red"
            elif s == "INTERACT": color = "magenta"
            
            table.add_row(title, f"[{color}]{s}[/{color}]", data['message'])
        return table

    with Live(generate_table, refresh_per_second=4) as live:
        # We need to hook the callback to force a refresh?
        # Live polls 'generate_table' automatically.
        generator.run_batch_generation(max_concurrent=5, update_callback=callback)

    console.print("[bold green]✅ Batch Generation Completed![/bold green]")

# --- LEGACY WRAPPERS ---

def run_ocr(state_manager):
    console.print(Panel("[bold]Running OCR Module...[/bold]", style="blue"))
    input_dir = PROJECT_ROOT / "input"
    images = sorted(list(input_dir.glob("*.jpg")) + list(input_dir.glob("*.png")))
    
    if not images:
        console.print("[yellow]⚠️ No images found in input/.[/yellow]")
        return

    vision = VisionClient()
    output_dir = PROJECT_ROOT / "system workspace/text-data/raw"
    output_dir.mkdir(parents=True, exist_ok=True)
    
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

def run_planning(state_manager):
    console.print(Panel("[bold]Running Standard Planner...[/bold]", style="blue"))
    
    tp = TextProcessor()
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
            
            # Simplified: Pass full text (context window limited, but standard planner might handle it)
            # Actually, standard planner expects 'raw_lesson_text'
            # We should slice it.
            # For V3 UI, let's just use the merged text as placeholder logic if slicing isn't robust
            # But we can try to use the same logic as JulesPlanner if available
            # Or just pass the whole thing.
            
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
                "C) Plan Generation (Standard)",
                "D) Plan Generation (Jules Batch)",
                "E) Page Generation (Jules Batch)",
                "F) Audit & Verify Pages",
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

        if op == "D":
            run_jules_planning_ui(state_manager)
        elif op == "E":
            run_jules_generation_ui(state_manager)
        elif op == "B":
            # Call existing run_ocr but maybe wrap output?
            # For now, just call it, it prints to stdout.
            # We can capture it or leave it.
            from system import run_ocr
            run_ocr(state_manager)
        elif op == "C":
            from system import run_planning
            run_planning(state_manager)
        elif op == "F":
             # New option for Audit/Status refresh if needed
             # or maybe call verify_layout
             console.print("Running Audit...")
             subprocess.run(["python3", "Jules workspace/lint_pages.py"])
        
        if op != "Q":
            questionary.press_any_key_to_continue().ask()

if __name__ == "__main__":
    main()