# Module 3: The Control Room (`system.py` & State Management)

Welcome to Module 3. We have learned how Python uses string replacement to build HTML, and we have learned how the `system.sh` ignition script sets up the `uv` environment. 

When you run `system.sh`, its very last action is to launch this massive Python script: `system-workspace/tools/new-tools/system.py`.

This file is huge (over 80 KB). It acts as the "Control Room" for the entire repository. Instead of forcing developers to memorize 50 different command-line arguments to run scripts, `system.py` provides a beautiful, interactive graphical menu inside the terminal.

In this module, we will dive directly into the real source code of `system.py` and `project_state.py`. We will examine how it renders the UI, how it handles background logging without destroying the menu, how it safely tracks progress, and how it launches major automated workflows.

---

## Beginner Primer: Object-Oriented Programming (OOP) Crash Course

In Module 1, you learned how to use `@dataclass` to hold simple variables. But what if we need a container that holds variables AND complex functions that act on those variables?

For that, we use standard Object-Oriented Programming (OOP) Classes.

You will see things like `class ProjectState:` frequently in this module. 
**Two things beginners must know about Classes:**
1. **The `__init__` function**: This is the "constructor". Whenever you create a new instance of a class, this function runs immediately to set up the default variables.
2. **The `self` keyword**: Inside a class, a function cannot just grab a variable out of thin air. It must refer to its *own* variables using `self.`. If you see `self.project_root = ...`, it just means "assign this variable to *this specific instance* of the class."

---

## Lesson 1: The Terminal UI Engine (`rich` & `questionary`)

This project abandons standard Python `print()` statements. To create a professional dashboard, it relies heavily on two external libraries: `rich` and `questionary`.

If you open `system.py`, you will immediately see these imports near the top:

```python
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
```

*   **`rich`**: This library handles everything visual. It creates the tables, the colors, the borders (`Panel`), and the live progress bars (`Progress`, `Live`). It ensures that logs and statuses are formatted beautifully in the terminal.
*   **`questionary`**: This library handles interactivity. Instead of asking a user to type `Y/N` or `1`, Questionary allows the user to use the Up/Down arrow keys on their keyboard to select options from a list.

### Real Code: Rendering the Main Menu

Let's look at the exact code from `system.py` that renders the main interactive menu you see when you start the system:

```python
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
                "7) Quit",
            ],
            style=menu_style,
        ).ask()

        if not main_choice or main_choice.startswith("7"):
            console.print("Goodbye.")
            sys.exit(0)
```

**Line-by-Line Breakdown:**
1.  **`questionary.select(...)`**: This creates a dropdown menu in the terminal. The terminal freezes here and waits for the user.
2.  **`choices=[...]`**: This list defines the exact text the user sees on the screen.
3.  **`.ask()`**: This is the trigger. Without `.ask()`, the menu won't appear. Once the user hits Enter, `.ask()` returns the exact string they selected (e.g., `"1) book making..."`) and stores it in the variable `main_choice`.
4.  **`sys.exit(0)`**: If the user presses `CTRL+C` (which makes `main_choice` empty) or selects Option 7, the script safely exits.

---

## Lesson 2: Advanced Logging without Terminal Clutter

A major challenge when building interactive terminal UIs is dealing with `logging`. If a background process suddenly prints a 10-line error message, it will shatter the `rich` tables and the `questionary` menu, pushing them off the screen.

To solve this, `system.py` implements a custom logging handler called `UILogHandler`.

### Real Code: The `UILogHandler`

```python
# --- LOGGING SETUP ---
# Redirect logs to file so they don't break the UI
logging.basicConfig(
    filename="system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w",
)

from collections import deque

class UILogHandler(logging.Handler):
    def __init__(self, maxlen=6):
        super().__init__()
        # deque automatically pushes old messages out when it reaches maxlen
        self.log_messages = deque(maxlen=maxlen)

    def emit(self, record):
        msg = self.format(record)
        self.log_messages.append(msg)

ui_log_handler = UILogHandler(maxlen=15)
logging.getLogger().addHandler(ui_log_handler)
```

**Line-by-Line Breakdown:**
1.  **`logging.basicConfig(...)`**: The very first thing the script does is hijack the standard Python logger and forces it to write to a physical file (`system.log`) instead of printing to the terminal.
2.  **`from collections import deque`**: A `deque` (Double Ended Queue) is a highly optimized list. By setting `maxlen=6`, if you push a 7th item into the list, the 1st item is instantly and automatically deleted.
3.  **`class UILogHandler(logging.Handler)`**: We create a custom rule for the logger.
4.  **`def emit(...)`**: Every time *any* script in the entire repository calls `logging.info("...")`, it triggers this `emit` function. The message is formatted and pushed into our `deque`.
5.  **`addHandler`**: We attach this custom handler to the global Python logger.

Because of this brilliant setup, errors and info logs don't destroy the terminal menu. Instead, they are quietly captured in the `deque`. Later in the script, `rich` pulls those strings from the `deque` and neatly displays them inside a constrained `Panel`.

---

## Lesson 3: State Management & Resumes (`project_state.py`)

Generating a 200-page book using AI takes time. API calls to Google Gemini can fail due to timeouts, rate limits, or network drops. If the script crashes on page 150, you *do not* want to start over from page 1.

This is where `system-workspace/tools/automation/project_state.py` comes in. It ensures the system always remembers exactly what it just finished.

### Real Code: `ProjectState` Class

```python
import json
import os

STATE_FILE = os.path.join(os.path.dirname(__file__), "project_state.json")

class ProjectState:
    def __init__(self):
        self.state = {
            "current_lesson_number": "",
            "current_lesson_title": "",
            "current_page_index": 0,
            "last_section_title": "",
            "last_file": "",
        }
        self.load()

    def load(self):
        if os.path.exists(STATE_FILE):
            try:
                with open(STATE_FILE, encoding="utf-8") as f:
                    self.state = json.load(f)
            except Exception as e:
                print(f"Error loading state: {e}")

    def save(self):
        try:
            with open(STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(self.state, f, indent=2, ensure_ascii=False)
            print(f"State saved to {STATE_FILE}")
        except Exception as e:
            print(f"Error saving state: {e}")
```

**Line-by-Line Breakdown:**
1.  **`STATE_FILE`**: We define exactly where the JSON file lives. Notice we use `os.path.join` to make sure the path works safely on both Windows and Linux.
2.  **`self.state = {...}`**: This acts as a default template. If `project_state.json` doesn't exist yet (e.g., a brand new run), the class initializes safely with empty strings and zeroes.
3.  **`json.load(f)`**: When the script boots up, it immediately reads the physical JSON file. If the previous run crashed at `current_page_index: 45`, the script instantly knows it needs to resume at page 46.
4.  **`json.dump(...)`**: Every time the AI finishes processing a page, the orchestrator triggers this `.save()` function. 
5.  **`ensure_ascii=False`**: This is a critical parameter when dealing with Arabic text in JSON. If you don't use this, Python will convert Arabic letters into ugly unicode escapes (like `\u0627\u0644`). This ensures the JSON file remains readable to human developers.

---

## Lesson 4: Workflow Delegation

So, the UI is running, the logger is quiet, and the state manager is tracking progress. What happens when the user actually asks `system.py` to do some heavy lifting? 

`system.py` doesn't do the work itself. It delegates.

### Real Code: Launching the Orchestrator

```python
        # (Assuming the user selected Main Menu Option 1, then Sub Menu Option A)
        if main_op == "1":
            # ... UI selections happen here ...
            
            if sub_op == "A":
                console.print("[bold green]Starting Full Auto Workflow...[/bold green]")
                workflow = FullAutoWorkflow(PROJECT_ROOT)
                workflow.run()
                op_ran = True
```

**Line-by-Line Breakdown:**
1.  **`if sub_op == "A":`**: We capture the user's choice from the questionary menu.
2.  **`FullAutoWorkflow(PROJECT_ROOT)`**: `system.py` instantiates a massive, separate class from the `automation/` folder. It passes `PROJECT_ROOT` to it so the workflow knows exactly where all the files are located on the hard drive.
3.  **`workflow.run()`**: This one line of code triggers hundreds of internal functions. It boots up the Gemini AI, triggers the OCR engine to read images, writes markdown plans, and injects HTML templates. `system.py` just sits and waits for `.run()` to finish.

### Review
You now understand the architecture of the Control Room. 
*   You know how `questionary` allows keyboard interactivity.
*   You understand how `UILogHandler` intercepts logs to protect the `rich` UI using a `deque`.
*   You understand how `project_state.json` acts as the persistent memory of the system.
*   You know that `system.py` is a delegator, passing massive tasks off to classes like `FullAutoWorkflow`.

In **Module 4: AI, OCR & Automation Pipelines**, we will follow the delegation path! We will jump into the `automation/` folder and look at `orchestrator.py` to see exactly how this repository talks to Google Gemini to extract Arabic text.
