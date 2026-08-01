import os
import sys
import json
import subprocess
import time
from pathlib import Path

import questionary
from rich.console import Console
from rich.panel import Panel

# Add parent directory to path to import JulesClient
sys.path.append(str(Path(__file__).resolve().parent))
from jules_client import JulesClient

console = Console()

def pull_pr_branch(project_root, pr_number):
    """Fetches and checks out the PR branch locally."""
    git_env = os.environ.copy()
    git_env["GIT_TERMINAL_PROMPT"] = "0"
    local_branch = f"pr-{pr_number}"
    fetch_ref = f"pull/{pr_number}/head:{local_branch}"
    
    try:
        # Fetch PR head
        subprocess.run(
            ["git", "fetch", "origin", fetch_ref],
            check=True, cwd=project_root, capture_output=True, env=git_env
        )
        # Checkout the branch
        subprocess.run(
            ["git", "checkout", local_branch],
            check=True, cwd=project_root, capture_output=True, env=git_env
        )
        return local_branch
    except subprocess.CalledProcessError as e:
        console.print(f"[red]❌ Git pull failed: {e.stderr.decode() if e.stderr else str(e)}[/red]")
        return None

def return_to_main(project_root, delete_branch=None):
    """Returns to main branch and deletes the temporary PR branch."""
    git_env = os.environ.copy()
    try:
        subprocess.run(["git", "checkout", "main"], cwd=project_root, capture_output=True, env=git_env)
        if delete_branch:
            subprocess.run(["git", "branch", "-D", delete_branch], cwd=project_root, capture_output=True, env=git_env)
    except Exception:
        pass

def wait_for_pr_and_pull(client, session_id, project_root):
    """Waits for Jules to create a PR and pulls it."""
    console.print("[cyan]⏳ Waiting for Jules to push changes to a PR...[/cyan]")
    pr_number = None
    timeout = time.time() + 300 # 5 minutes max wait
    
    while time.time() < timeout:
        status_data = client.get_session_status(session_id)
        if status_data:
            state = status_data.get("state", "")
            
            # Extract PR number if it exists
            outputs = status_data.get("outputs", [])
            for out in outputs:
                if "pullRequest" in out:
                    url = out["pullRequest"].get("url", "")
                    if url:
                        import re
                        match = re.search(r"/pull/(\d+)", url)
                        if match: pr_number = match.group(1)
            
            # If not in outputs, check activities
            if not pr_number:
                acts = client.get_activities(session_id)
                for act in acts:
                    artifacts = act.get("artifacts", [])
                    for artifact in artifacts:
                        if "changeSet" in artifact and "gitPatch" in artifact["changeSet"]:
                            git_patch = artifact["changeSet"]["gitPatch"]
                            if "pullRequest" in git_patch:
                                pr_url = git_patch["pullRequest"].get("htmlUrl", "")
                                import re
                                match = re.search(r"/pull/(\d+)", pr_url)
                                if match:
                                    pr_number = match.group(1)
                                    break
            
            if pr_number:
                console.print(f"[green]✅ PR #{pr_number} created![/green]")
                branch = pull_pr_branch(project_root, pr_number)
                return branch, pr_number
                
            if state in ["WAITING_FOR_INPUT", "ACTION_REQUIRED"]:
                # Jules is stuck waiting for input before making a PR
                console.print("[yellow]⚠️ Agent needs input but hasn't created a PR. Prompting it to continue...[/yellow]")
                client.send_response(session_id, "Please output the modified styles/main.css and create the Pull Request.")
                time.sleep(10)
                
            if state in ["COMPLETED", "FAILED", "CANCELLED"]:
                console.print(f"[red]❌ Session ended with state {state} before PR was found.[/red]")
                return None, None
                
        time.sleep(10)
        
    console.print("[red]❌ Timed out waiting for PR.[/red]")
    return None, None

def run_ai_css_tuner(project_root=None):
    if not project_root:
        project_root = Path(__file__).resolve().parent.parent.parent.parent.parent

    console.clear()
    console.print(Panel("[bold cyan]🤖 AI Book Style Tuning (Density Optimizer via Jules)[/bold cyan]"))

    try:
        client = JulesClient(project_root=project_root)
    except Exception as e:
        console.print(f"[red]Failed to initialize JulesClient: {e}[/red]")
        return

    choice = questionary.select(
        "Select target HTML page for optimization:",
        choices=[
            "1. Manually specify path",
            "2. Cancel"
        ]
    ).ask()

    if not choice or choice.startswith("2"): return

    html_path_str = questionary.text("Enter path to HTML file (e.g. pages/01.0_intro.html):").ask()
    if not html_path_str: return

    target_html = project_root / html_path_str
    if not target_html.exists():
        console.print(f"[red]❌ File not found: {target_html}[/red]")
        return

    oracle_script = project_root / "Jules-workspace" / "evaluate_css_variant.py"
    if not oracle_script.exists():
        console.print(f"[red]❌ Oracle script missing: {oracle_script}[/red]")
        return

    css_path = project_root / "styles" / "main.css"

    sys_prompt = f"""You are an expert CSS Developer for an Arabic Grammar Book.
    Your objective is to tweak the `styles/main.css` file to make the target HTML fit exactly on ONE A4 page.
    
    Constraints:
    - Never reduce body text below 13pt.
    - Never reduce line-height below 1.6em.
    - Never reduce internal padding below 1.5mm.
    
    I will run a layout verification script. If it fails, I will send you the error and you must adjust the CSS and create a new commit.
    Please start by slightly tightening the margins and grid gaps in `styles/main.css` to see if it fixes the overflow.
    """

    session_data = client.create_session(sys_prompt, title=f"CSS Tuning for {target_html.name}", automation_mode="AUTO_CREATE_PR")
    if not session_data:
        console.print("[red]❌ Failed to start Jules session.[/red]")
        return
        
    session_id = session_data.get("name")
    
    console.print("\n[yellow]Starting AI Optimization Loop...[/yellow]")
    
    max_iters = 5
    best_pr = None

    for i in range(max_iters):
        console.print(f"\n[cyan]Iteration {i+1}/{max_iters}[/cyan]")
        
        # 1. Wait for PR and Pull
        local_branch, pr_number = wait_for_pr_and_pull(client, session_id, project_root)
        
        if not local_branch:
            console.print("[red]❌ Could not pull CSS updates. Aborting loop.[/red]")
            return_to_main(project_root)
            break
            
        # 2. Run Oracle on the pulled branch (which has the updated styles/main.css)
        try:
            res = subprocess.run(
                [sys.executable, str(oracle_script), str(target_html), str(css_path)],
                capture_output=True, text=True, check=True
            )
            output = json.loads(res.stdout)
        except Exception as e:
            console.print(f"[red]Oracle failed: {e}[/red]")
            return_to_main(project_root, local_branch)
            break
            
        status = output.get("status")
        page_count = output.get("page_count")
        
        console.print(f"Status: {status} | Pages: {page_count} | Blank %: {output.get('blank_pct', 0)}")
        
        if status == "PASS":
            console.print("[green]✅ Achieved perfect 1-page fit![/green]")
            best_pr = pr_number
            # We stay on this branch so the user can verify
            console.print(f"[green]The optimized CSS is now checked out on branch: {local_branch}[/green]")
            
            # Optional: Tell Jules it succeeded
            client.send_response(session_id, "PASS! The layout is perfect. Please complete the session.")
            break
        
        # 3. Feed back to AI if failed
        feedback = f"The current CSS resulted in status: {status}, page_count: {page_count}, remaining_mm: {output.get('remaining_mm')}. Please adjust the CSS again to fix this and push a new commit."
        console.print("[yellow]Sending feedback to Jules and waiting for next commit...[/yellow]")
        
        # Go back to main while waiting
        return_to_main(project_root, local_branch)
        
        client.send_response(session_id, feedback)

    if not best_pr:
        console.print("[yellow]Optimization did not find a perfect PASS variant within the iteration limit.[/yellow]")
        return_to_main(project_root)

if __name__ == "__main__":
    run_ai_css_tuner()
