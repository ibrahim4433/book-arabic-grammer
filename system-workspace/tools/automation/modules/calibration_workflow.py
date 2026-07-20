import os
import sys
import time
import threading
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
    # but uvicorn.run blocks. So we run it in a thread.
    def run_server():
        from calibration_app import app
        app.state.target_html_path = html_path
        uvicorn.run(app, host="127.0.0.1", port=8000, log_level="error")

    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()

    console.print(Panel(
        f"[bold green]✅ Calibration Tool Started![/bold green]\n"
        f"Target HTML: {html_path.name}\n"
        f"Open in your browser: [bold cyan]http://127.0.0.1:8000[/bold cyan]\n"
        f"Press Ctrl+C here to stop the server and return.",
        style="green"
    ))

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        console.print("\n[yellow]Stopping calibration server...[/yellow]")
        # Daemon thread will die when we return

def run_calibration_ui(state_manager=None, project_root=None):
    console.clear()
    console.print(Panel("[bold cyan]O) Book Style Tuning (Semi-automatic)[/bold cyan]", box=None))

    project_root = Path(project_root) if project_root else Path(__file__).resolve().parent.parent.parent.parent.parent

    choice = questionary.select(
        "How do you want to select the test page?",
        choices=[
            "1. Automatically fetch and generate the densest page (via Jules API)",
            "2. Manually select an existing HTML file",
            "3. Cancel"
        ]
    ).ask()

    if not choice or choice.startswith("3"):
        return

    html_target_path = None

    if choice.startswith("2"):
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
        console.print("\n[bold yellow]--- Step 1: Planning ---[/bold yellow]")
        plan_client = JulesPlanClient(project_root=project_root)

        # Override prompt for stress test
        plan_prompt = (
            f"You are the Lead Architect. Generate a Markdown plan for the following raw text.\n\n"
            f"**CRITICAL INSTRUCTION**: This is a density stress test. DO NOT attempt to fit this into a single page. "
            f"Bypass any 1-page limits. Plan it fully.\n\n"
            f"Raw Text:\n{page_text}\n"
        )

        title = f"Stress Test Plan - Page {page_num}"
        session = plan_client.create_session(plan_prompt, title=title)

        if not session:
            console.print("[red]❌ Failed to create Jules planning session.[/red]")
            return

        console.print(f"Waiting for PR for session {session.get('name')}...")
        session_id = session.get('name')

        # Wait for PR
        pr_number = None
        while True:
            status = plan_client.get_session_status(session_id)
            if status and status.get('state') == 'COMPLETED':
                if 'pr_number' not in status:
                    console.print("[yellow]PR creation takes a moment...[/yellow]")
                    time.sleep(10)
                    # For now, let's just break if it says completed but no PR (means interactive mode maybe, which we aren't using)
                else:
                    pr_number = status.get('pr_number')
                    console.print(f"[green]✅ PR #{pr_number} created![/green]")
                    break
            time.sleep(5)

        # Fake details for merge_pr
        details = {"pr_number": pr_number}
        plan_file = f"plans/{page_num}.md"
        plan_client.finalize_pr_and_pull(details, plan_file)

        # 2. Dispatch Generation
        console.print("\n[bold yellow]--- Step 2: Page Generation ---[/bold yellow]")
        # We need the plan content
        plan_path = project_root / plan_file
        if not plan_path.exists():
            console.print(f"[red]❌ Plan file {plan_path} not found after pull![/red]")
            return

        # Use a simple generic generation logic or the JulesClient directly
        gen_prompt = (
            f"You are the Lead UI Developer. Generate an HTML page based on the following plan.\n"
            f"**CRITICAL INSTRUCTION**: This is a stress test. Ignore 1-page limits. Generate the full HTML.\n\n"
            f"Plan:\n{plan_path.read_text(encoding='utf-8')}\n"
        )

        gen_session = plan_client.create_session(gen_prompt, title=f"Stress Test Gen - Page {page_num}")
        if not gen_session: return

        console.print("Waiting for generation PR...")
        gen_session_id = gen_session.get('name')

        gen_pr_number = None
        while True:
            status = plan_client.get_session_status(gen_session_id)
            if status and status.get('state') == 'COMPLETED':
                if 'pr_number' in status:
                    gen_pr_number = status.get('pr_number')
                    console.print(f"[green]✅ Generation PR #{gen_pr_number} created![/green]")
                    break
            time.sleep(5)

        details_gen = {"pr_number": gen_pr_number}
        html_file = f"pages/{page_num}.html"
        plan_client.finalize_pr_and_pull(details_gen, html_file)

        html_target_path = project_root / html_file
        if not html_target_path.exists():
            console.print(f"[red]❌ HTML file {html_target_path} not found after pull![/red]")
            return

    # Start the server with the target HTML
    start_calibration_server(html_target_path, project_root)
