def run_retry_planning_and_generation_ui(state_manager):
    console.clear()
    console.print("[bold cyan]🔄 Retry Batch Jules Planning / Page Making[/bold cyan]")
    
    lesson_input = questionary.text("Enter lesson numbers to re-make (comma separated, e.g. 3, 5, 6):").ask()
    if not lesson_input: return

    # Parse inputs to padded string format used in TOC
    only_lessons = []
    for item in lesson_input.split(","):
        item = item.strip()
        if item.isdigit():
            only_lessons.append(f"{int(item):02d}")
        else:
            only_lessons.append(item)

    if not only_lessons: return

    console.print(f"[yellow]Will re-make lessons: {', '.join(only_lessons)}[/yellow]")
    confirm = questionary.confirm("This will delete old plans and pages for these lessons. Continue?").ask()
    if not confirm: return

    # Delete old plans and pages
    plans_dir = PROJECT_ROOT / "plans"
    pages_dir = PROJECT_ROOT / "pages"
    
    deleted = 0
    if plans_dir.exists():
        for plan in plans_dir.glob("*.md"):
            match = re.match(r'^(\d+)', plan.name)
            if match and match.group(1) in only_lessons:
                plan.unlink()
                deleted += 1
                console.print(f"[dim]Deleted {plan.name}[/dim]")
                
    if pages_dir.exists():
        for page in pages_dir.glob("*.html"):
            match = re.match(r'^(\d+)', page.name)
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
            if title not in tasks: tasks[title] = {'status': status, 'message': msg}
            else:
                tasks[title]['status'] = status
                tasks[title]['message'] = msg
        if status in ["ERROR", "FAILED", "WARN"]:
            console.print(f"[red][{status}] {title}: {msg}[/red]")
        elif status == "SUCCESS":
            console.print(f"[green]✅ {title} planned![/green]")

    planner.run_batch_planning(max_concurrent=5, update_callback=callback_plan, only_lessons=only_lessons)

    # Run Generation
    console.print("\n[bold cyan]Step 2: Generation[/bold cyan]")
    generator = JulesPageGenerator(PROJECT_ROOT)
    
    def callback_gen(title, status, msg):
        with lock:
            if title not in tasks: tasks[title] = {'status': status, 'message': msg}
            else:
                tasks[title]['status'] = status
                tasks[title]['message'] = msg
        if status in ["ERROR", "FAILED", "WARN"]:
            console.print(f"[red][{status}] {title}: {msg}[/red]")
        elif status == "SUCCESS":
            console.print(f"[green]✅ {title} generated![/green]")

    generator.run_batch_generation(max_concurrent=5, update_callback=callback_gen, only_lessons=only_lessons)
    
    console.print("\n[bold green]✅ Retry Workflow Completed![/bold green]")
