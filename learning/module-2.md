# Module 2: The True Foundations, Entry Points & Architecture

Welcome to Module 2! In the previous modules, we isolated the absolute core mechanic: using Python string replacement and loops to build HTML pages. We simulated this in a 15-line sandbox script. 

But you cannot run a repository of this magnitude on a 15-line script. When you combine complex Python UI libraries, external system dependencies (like GTK3 for PDF rendering), and API connections for AI agents, you need a robust, scalable architecture. 

In this module, we will explore exactly how the real system is initialized, how dependencies are managed at blinding speed, and finally, we will map out the true, massive architecture of the backend.

---

## Beginner Primer: Demystifying Bash Scripts

If you are a Windows user moving into serious development (perhaps using WSL - Windows Subsystem for Linux), you will frequently encounter files ending in `.sh` (Shell Scripts).

**What is a Bash Script?**
A Bash script is simply a list of terminal commands saved in a text file. Instead of typing 10 setup commands one by one, you just run the script.

**Two things beginners always get stuck on:**
1. **The Shebang (`#!/bin/bash`)**: You will see this at the very top of `system.sh`. It is not a comment! It tells the operating system exactly which interpreter to use to run the file.
2. **Permission Denied (`chmod +x`)**: If you try to run `./system.sh` and get "Permission Denied", it means Linux blocked the file from executing for safety. You must run `chmod +x system.sh` to grant it "eXecutable" permissions before it will work!

---

## Lesson 1: Environment & Dependencies (Enter `uv`)

If you have worked with Python before, you are likely familiar with creating virtual environments using `python3 -m venv venv` and installing packages with `pip install -r requirements.txt`. 

While standard `pip` is perfectly valid, this repository relies heavily on a tool called **`uv`**.

### What is `uv`?
`uv` is an extremely fast Python package and project manager written in Rust. It acts as a drop-in replacement for `pip` and `venv`, but it operates exponentially faster. 

### Why is it used here?
This repository is an AI-driven rendering pipeline. It relies on massive, heavy packages:
*   **WeasyPrint:** Requires strict version matching with underlying system libraries (Pango/GTK) to calculate A4 PDF physical layout sizes accurately.
*   **Rich & Questionary:** UI libraries for rendering complex terminal dashboards.
*   **Google GenAI / Requests:** For contacting external APIs to perform OCR on images.

If the environment breaks, the entire automated vibe-coding pipeline crashes. `uv` is utilized to ensure that virtual environments are created, synced, and locked instantly and deterministically. If you look at the root directory, you'll see a massive 290KB `uv.lock` file ensuring every developer and every GitHub Action uses the exact same sub-dependency versions.

---

## Lesson 2: The Core Ignition Script (`system.sh`)

You might assume that to start a Python project, you simply run `python main.py`. However, in a complex environment that might be run on Windows (via PowerShell), macOS (via Zsh), or Linux (via Bash), hardcoding a `python` command is dangerous.

The true entry point for developers using this repository is **`system.sh`**. Let's break down this script line-by-line to see exactly how it manages cross-platform environments.

### Step 1: Safety & Cleanup
```bash
#!/bin/bash
set -e

echo "==> 🚀 Starting Arabic Grammar System..."
cd "$(dirname "$0")"
export UV_LINK_MODE=copy
```
*   **`set -e`**: A critical safety mechanism. If any command in this script fails, execution stops immediately. It prevents the script from trying to launch Python if the dependency installation failed.
*   **`cd "$(dirname "$0")"`**: Ensures that no matter where you call the script from, the working directory shifts to the project root.
*   **`export UV_LINK_MODE=copy`**: By default, `uv` tries to use hardlinks to save space. On some filesystems (like WSL - Windows Subsystem for Linux), hardlinks can cause permission issues. This forces `uv` to safely copy the files.

### Step 2: Smart OS Detection
Python virtual environments look different depending on your OS. Windows puts the Python executable in `.venv/Scripts/python.exe`, while Unix systems put it in `.venv/bin/python3`. `system.sh` intelligently detects this:

```bash
VENV_DIR=".venv"

if [ -f "$VENV_DIR/Scripts/python.exe" ]; then
    echo "    Detected Windows virtual environment (.venv/Scripts)."
    UV_CMD="uv.exe"
    PYTHON_CMD="$VENV_DIR/Scripts/python.exe"
elif [ -f "$VENV_DIR/bin/python3" ] || [ -f "$VENV_DIR/bin/python" ]; then
    echo "    Detected Linux/macOS virtual environment (.venv/bin)."
    UV_CMD="uv"
    # (Selects between python3 and python based on availability)
```
Instead of crashing when a Linux user tries to run a script hardcoded for Windows, it dynamically assigns the correct path to the `PYTHON_CMD` variable.

### Step 3: Fallback & Creation
What if the virtual environment doesn't exist yet?

```bash
else
    echo "    Virtual environment not found. Setting up..."
    # (Logic checking if uv or uv.exe is installed)
    $UV_CMD venv "$VENV_DIR"
```
If `.venv` is missing, the script automatically builds it for you using `uv venv`.

### Step 4: Syncing Dependencies
Once the environment is confirmed, it syncs the dependencies.
```bash
echo "==> 📦 Syncing dependencies via $UV_CMD..."
export VIRTUAL_ENV="$PWD/$VENV_DIR"
$UV_CMD pip install -e ".[dev,api]"
```
*   **`-e ".[dev,api]"`**: Instead of a simple `requirements.txt`, this project uses a `pyproject.toml` file (a modern Python standard). This command tells `uv` to install the project in "editable" mode (`-e`) and specifically install the optional dependency groups `dev` (for linters/formatters) and `api` (for AI orchestration).

### Step 5: Ignition
Finally, we hand control over to the Python engine.
```bash
echo "==> ✅ Dependencies synced! Running system.py..."
"$PYTHON_CMD" system-workspace/tools/new-tools/system.py
```
Notice where it points! It does *not* point to `generate.py` or `build.py`. It points deep into the architecture at `system-workspace/tools/new-tools/system.py`.

---

## Lesson 3: The True Architecture Map

If you look at the root directory of the repository, you see folders like `pages/`, `styles/`, and `.github/`. That is only the surface. The real engines that power this repository are buried in specific backend directories. 

Here is the mental map you need to navigate this repository successfully.

### 1. The Core Engines (`Jules-workspace/`)
This directory contains the strict parsers and structural tools. If the HTML structure is failing, the problem is usually here.
*   **`generate.py`**: The script that loops through raw data and injects it into HTML templates (as we learned in Module 1).
*   **`id_manager.py`**: A vital script that uses the `@dataclass` structure we learned about to auto-tag every single HTML `<section>` or `<div>` with a unique ID (e.g., `id="b49281"`).
*   **`verify_layout.py` & `lint_pages.py`**: The quality gates. They enforce the 1-Page Law and ensure no forbidden HTML tags are used.
*   **`Templates/`**: The folder containing the atomic HTML snippets (`TEMPLATE_C_BASE.html`, `TEMPLATE_C_BLOCK.html`).

### 2. The AI Orchestration (`system-workspace/tools/automation/`)
This folder is the "Brain" of the repository. When you need the AI to parse an image of an Arabic textbook and convert it to structured JSON, these scripts handle it.
*   **`orchestrator.py`**: The main hub for making REST API calls to Google Gemini. It handles prompting the AI to extract Arabic text while preserving strict diacritics (Tashkeel).
*   **`project_state.py`**: A massive state manager that saves progress to `project_state.json`. It ensures that if the OCR process crashes halfway through a 200-page book, the pipeline can resume exactly where it left off.

### 3. The Debugging & Fixer Arsenal (`system-workspace/tools/new-tools/`)
This is the largest and most complex folder in the repository. It contains over 80 specific Python scripts. Why? Because when you use AI "vibe coding" to generate thousands of lines of HTML, errors happen. IDs collide. Tags are left unclosed. Titles are misspelled.

Instead of fixing these manually, developers wrote single-purpose scripts to clean up the tech debt programmatically.
*   **`system.py`**: The 82-kilobyte script that `system.sh` launches. It is a massive interactive terminal dashboard that controls all the other scripts.
*   **`fix_book.py` / `sync_pages.py` / `rebuild_toc.py`**: Highly specific scripts designed to manipulate the generated HTML files, clean up duplicate IDs, or automatically generate a Table of Contents based on the `<title>` tags in the `/pages/` folder.

### 4. The Output Pipeline (`scripts/` and `/pages/`)
*   **`/pages/`**: The ultimate destination for all HTML files generated by Python. 
*   **`/output/`**: The destination for the final `book.pdf`.
*   **`scripts/build-with-id.sh` & `build.py`**: The scripts that take the hundreds of individual HTML files in `/pages/`, stitch them together, link the CSS, and feed them into WeasyPrint to generate the final PDF.

---

### Review
You now have a complete mental map of the repository. You know how the environment is instantly standardized using `uv` via `system.sh`, and you know exactly which directories hold the HTML templates versus the AI orchestrators.

In **Module 3: The Control Room (`system.py`)**, we will follow the path of `system.sh` and dive directly into the massive 82KB dashboard script to see how it manages this entire sprawling architecture using interactive UIs and State Management.
