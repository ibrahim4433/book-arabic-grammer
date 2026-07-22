import os
import sys
import time
import threading
import subprocess
import shutil
from pathlib import Path
import questionary
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
import uvicorn

# Ensure modules are importable
sys.path.append(str(Path(__file__).parent))
from density_analyzer import DensityAnalyzer
from jules_client_plans import JulesPlanClient
from jules_page_generator import JulesPageGenerator

console = Console()

def start_calibration_server(html_path, project_root):
    """Starts the FastAPI calibration app in a separate thread."""
    os.environ["CALIBRATION_HTML_PATH"] = str(html_path)

    # We need to run the uvicorn server.
    # To pass state safely, we can import the app and set it before running,
    from calibration_app import app
    app.state.target_html_path = html_path
    
    config = uvicorn.Config(app, host="127.0.0.1", port=8000, log_level="error")
    server = uvicorn.Server(config)

    server_thread = threading.Thread(target=server.run, daemon=True)
    server_thread.start()

    target_name = html_path.name if html_path else "None (Select in web app)"
    console.print(Panel(
        f"[bold green]✅ Calibration Tool Started![/bold green]\n"
        f"Target HTML: {target_name}\n"
        f"Open in your browser: [bold cyan]http://127.0.0.1:8000[/bold cyan]\n"
        f"Press Ctrl+C here to stop the server and return.",
        style="green"
    ))

    try:
        while server_thread.is_alive():
            time.sleep(1)
    except KeyboardInterrupt:
        console.print("\n[yellow]Stopping calibration server...[/yellow]")
        server.should_exit = True
        server_thread.join(timeout=3)

def wait_for_session_pr(client, session_id, step_name="PR"):
    """Waits for PR and handles manual override/interrupts."""
    pr_number = None

    while True:
        try:
            status = client.get_session_status(session_id)
            details = client.get_session_details(session_id)

            if details and details.get('pr_number'):
                pr_number = details.get('pr_number')
                console.print(f"[green]✅ {step_name} #{pr_number} created![/green]")
                return pr_number, False

            if status and status.get('state') == 'COMPLETED':
                console.print(f"[yellow]Session completed. Checking for {step_name}...[/yellow]")
                time.sleep(2)
                details = client.get_session_details(session_id)
                if details and details.get('pr_number'):
                    pr_number = details.get('pr_number')
                    console.print(f"[green]✅ {step_name} #{pr_number} found![/green]")
                    return pr_number, False
                else:
                    console.print(f"[yellow]No {step_name} found automatically.[/yellow]")
                    choice = questionary.select(
                        "How would you like to proceed?",
                        choices=[
                            "1. Wait longer (check again)",
                            "2. Enter PR number manually",
                            "3. File is already in place locally (skip pull)",
                            "4. Cancel"
                        ]
                    ).ask()
                    if not choice or choice.startswith("4"):
                        return None, False
                    if choice.startswith("1"):
                        continue
                    elif choice.startswith("2"):
                        pr_num_str = questionary.text("Enter PR number:").ask()
                        if pr_num_str and pr_num_str.isdigit():
                            return pr_num_str, False
                    elif choice.startswith("3"):
                        return None, True

            time.sleep(5)
        except KeyboardInterrupt:
            console.print("\n[yellow]Interrupted![/yellow]")
            choice = questionary.select(
                "How would you like to proceed?",
                choices=[
                    "1. Resume waiting",
                    "2. Enter PR number manually",
                    "3. File is already in place locally (skip pull)",
                    "4. Cancel"
                ]
            ).ask()
            if not choice or choice.startswith("4"):
                return None, False
            if choice.startswith("2"):
                pr_num_str = questionary.text("Enter PR number:").ask()
                if pr_num_str and pr_num_str.isdigit():
                    return pr_num_str, False
            elif choice.startswith("3"):
                return None, True

def extract_from_pr_branches(project_root, expected_filename):
    console.print(f"\n[cyan]🔍 Searching Local PR Branches for {expected_filename}...[/cyan]")
    try:
        branches_out = subprocess.check_output(
            ["git", "branch", "--list", "pr-*"], cwd=project_root, text=True
        )
        branches = [
            b.strip().replace("*", "").strip() for b in branches_out.splitlines() if b.strip()
        ]
        
        expected_name = Path(expected_filename).name
        
        for branch in branches:
            diff_out = subprocess.check_output(
                ["git", "diff", "--name-only", f"main..{branch}"], cwd=project_root, text=True
            )
            files = [f.strip() for f in diff_out.splitlines() if f.strip()]
            
            for f in files:
                if expected_name in f:
                    console.print(f"[green]✅ Found {expected_name} inside hidden branch {branch}: {f}[/green]")
                    subprocess.run(
                        ["git", "checkout", branch, "--", f],
                        cwd=project_root,
                        check=True,
                        capture_output=True,
                    )
                    local_f = project_root / f
                    target = project_root / expected_filename
                    if local_f != target:
                        target.parent.mkdir(exist_ok=True, parents=True)
                        shutil.move(str(local_f), str(target))
                    return True
    except Exception as e:
        console.print(f"[red]Error searching branches: {e}[/red]")
    return False

def run_calibration_ui(state_manager=None, project_root=None):
    console.clear()
    console.print(Panel("[bold cyan]O) Book Style Tuning (Semi-automatic)[/bold cyan]"))

    project_root = Path(project_root) if project_root else Path(__file__).resolve().parent.parent.parent.parent.parent

    choice = questionary.select(
        "How do you want to select the test page?",
        choices=[
            "1. Automatically fetch and generate the densest page (via Jules API)",
            "2. Generate HTML from an existing Plan (Markdown)",
            "3. Manually select an existing HTML file",
            "4. Open Web UI without selecting a page",
            "5. Cancel"
        ]
    ).ask()

    if not choice or choice.startswith("5"):
        return

    html_target_path = None

    if choice.startswith("4"):
        pass # html_target_path remains None
    elif choice.startswith("3"):
        html_path_str = questionary.text("Enter path to the HTML file (relative to project root):", default="pages/test.html").ask()
        if not html_path_str:
            return

        target = project_root / html_path_str
        if not target.exists():
            console.print(f"[red]❌ File not found: {target}[/red]")
            return

        html_target_path = target

    elif choice.startswith("1"):
        console.print("[cyan]🔍 Analyzing raw text to find the densest page...[/cyan]")
        analyzer = DensityAnalyzer(project_root)
        page_num, page_text, density = analyzer.get_densest_page()

        if not page_text:
            console.print("[red]❌ Failed to find any pages in raw text.[/red]")
            return

        console.print(f"[green]✅ Found densest page: Page {page_num} (Density: {density} chars)[/green]")

        if not questionary.confirm(f"Do you want to dispatch Jules to plan and generate this page now?").ask():
            return

        # 1. Dispatch Planning
        if choice.startswith("1"):
            console.print("\n[bold yellow]--- Step 1: Planning ---[/bold yellow]")
            plan_client = JulesPlanClient(project_root=project_root)

            plan_file = f"plans/{page_num}.md"
            master_prompt_path = project_root / "system-workspace" / "Architect_GEM_MASTER.md"
            master_prompt = master_prompt_path.read_text(encoding="utf-8") if master_prompt_path.exists() else ""

            # Override prompt for stress test
            plan_prompt = (
                f"{master_prompt}\n\n"
                f"You are the Lead Architect. Generate a Markdown plan for the following raw text.\n\n"
                f"**CRITICAL INSTRUCTION**: This is a density stress test. DO NOT attempt to fit this into a single page. "
                f"Bypass any 1-page limits. Plan it fully.\n"
                f"**OUTPUT FORMAT**: You MUST output your plan to the EXACT file path: {plan_file}\n\n"
                f"Raw Text:\n{page_text}\n"
            )

            title = f"Stress Test Plan - Page {page_num}"
            session = plan_client.create_session(plan_prompt, title=title)

            if not session:
                console.print("[red]❌ Failed to create Jules planning session.[/red]")
                return

            console.print(f"Waiting for PR for session {session.get('name')}...")
            session_id = session.get('name')

            pr_number, skip_pull = wait_for_session_pr(plan_client, session_id, "Planning PR")

            if not pr_number and not skip_pull:
                console.print("[red]❌ Planning cancelled or failed.[/red]")
                return

            plan_file = f"plans/{page_num}.md"
            if not skip_pull:
                details = {"pr_number": pr_number}
                plan_client.finalize_pr_and_pull(details, plan_file)
            
            # Check if file exists and recover if necessary
            if not (project_root / plan_file).exists():
                console.print(f"[yellow]⚠️ {plan_file} not found at expected path. Searching PR branches...[/yellow]")
                if not extract_from_pr_branches(project_root, plan_file):
                    console.print(f"[red]❌ Failed to recover {plan_file}. Please check git branches manually.[/red]")
                    return
        else:
            plan_file_str = questionary.text("Enter path to the Markdown Plan file (relative to project root):", default="plans/test.md").ask()
            if not plan_file_str:
                return
            plan_file = plan_file_str
            plan_client = JulesPlanClient(project_root=project_root)
            page_num = "manual_test" # Dummy page_num for manual test

        # 2. Dispatch Generation
        console.print("\n[bold yellow]--- Step 2: Page Generation ---[/bold yellow]")
        # We need the plan content
        plan_path = project_root / plan_file
        if not plan_path.exists():
            console.print(f"[red]❌ Plan file {plan_path} not found after pull![/red]")
            return

        # Use a simple generic generation logic or the JulesClient directly
        html_file = f"pages/{page_num}.html"
        auditor_prompt_path = project_root / "system-workspace" / "Architect_AUDITOR.md"
        auditor_prompt = auditor_prompt_path.read_text(encoding="utf-8") if auditor_prompt_path.exists() else ""

        gen_prompt = (
            f"{auditor_prompt}\n\n"
            f"You are the Lead UI Developer. Generate an HTML page based on the following plan.\n"
            f"**CRITICAL INSTRUCTION**: This is a stress test. Ignore 1-page limits. Generate the full HTML.\n"
            f"**OUTPUT FORMAT**: You MUST output the HTML to the EXACT file path: {html_file}\n\n"
            f"Plan:\n{plan_path.read_text(encoding='utf-8')}\n"
        )

        gen_session = plan_client.create_session(gen_prompt, title=f"Stress Test Gen - Page {page_num}")
        if not gen_session: return

        console.print("Waiting for generation PR...")
        gen_session_id = gen_session.get('name')

        gen_pr_number, skip_pull_gen = wait_for_session_pr(plan_client, gen_session_id, "Generation PR")

        if not gen_pr_number and not skip_pull_gen:
            console.print("[red]❌ Generation cancelled or failed.[/red]")
            return

        if not skip_pull_gen:
            details_gen = {"pr_number": gen_pr_number}
            plan_client.finalize_pr_and_pull(details_gen, html_file)
            
        html_target_path = project_root / html_file

        if not html_target_path.exists():
            console.print(f"[yellow]⚠️ {html_file} not found at expected path. Searching PR branches...[/yellow]")
            if not extract_from_pr_branches(project_root, html_file):
                console.print(f"[red]❌ HTML file {html_target_path} not found after pull and branch search![/red]")
                return

    # Start the server with the target HTML
    start_calibration_server(html_target_path, project_root)
