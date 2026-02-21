# How the Arabic Grammar Automation System Works

Welcome to the **Arabic Grammar Book Automation System**. This document is your comprehensive technical guide. Whether you are a new developer, a contributor, or an AI agent, this file explains how we transform raw images of Arabic grammar lessons into structured, beautiful HTML5 pages.

---

## 1. The Big Picture

Our goal is to digitize an Arabic grammar book. We don't just want text; we want **semantic, structured HTML** that follows a strict design system. To achieve this, we use a pipeline of AI agents and Python scripts.

### The Pipeline
1.  **Ingestion (OCR):** We take photos of the book pages (`input/*.jpg`) and use Google Gemini Vision to extract the text.
2.  **Indexing:** We map the raw text to the Table of Contents (`input/TOC.json`) to know where each lesson starts and ends.
3.  **Planning (The Architect):** An AI Agent ("The Architect") reads the lesson text and creates a detailed **Markdown Plan** (`plans/*.md`).
4.  **Coding (The Developer):** Another AI Agent ("The Developer") reads the plan and writes the **HTML Code** (`pages/*.html`).
5.  **Verification (The Auditor):** We run automated scripts to check for design errors, broken layouts, and duplicate IDs.

---

## 2. Directory Structure

Understanding where things live is half the battle.

| Directory / File | Description |
| :--- | :--- |
| **`system.py`** | 🎛️ **The Control Room.** Run this script to start the interactive menu. |
| **`Jules-workspace/`** | 🛠️ **Developer Tools.** Scripts for verifying and fixing content. |
| `├── Templates/` | HTML templates (`TEMPLATE_C_BLOCK.html`, etc.) used by the generator. |
| `├── lint_pages.py` | Checks HTML for CSS violations and semantic errors. |
| `├── verify_layout.py` | Checks for content overflow (One-Page Law) using WeasyPrint. |
| `├── id_manager.py` | Manages unique IDs (`b12345`) for content blocks. |
| **`system-workspace/`** | 🧠 **The Brain.** Core automation logic. |
| `├── tools/automation/` | |
| `│   ├── modules/` | Python classes (`vision.py`, `planner.py`, `jules_page_generator.py`). |
| `│   └── project_workflow_state.json` | 🗄️ **Database.** Tracks the status of every lesson. |
| `├── text-data/` | Stores `raw_*.txt` (OCR output) and `full_raw_indexed.txt`. |
| **`input/`** | 📥 **Source Material.** Put images here. Contains `TOC.json`. |
| **`plans/`** | 📝 **Blueprints.** Generated Markdown lesson plans. |
| **`pages/`** | 🌐 **Final Output.** The HTML pages ready for the book. |
| **`styles/`** | 🎨 **Design System.** Contains `main.css`. |

---

## 3. The Workflow: Step-by-Step

To run the system, open your terminal and run:
```bash
python3 system.py
```
This opens the **Control Room**, a menu-based interface.

### Phase 1: Ingestion (OCR)
*   **Menu Option:** `B) OCR Only`
*   **What it does:**
    *   Scans `input/` for images.
    *   Uses `VisionClient` (wrapping Gemini Pro Vision) to transcribe text.
    *   Saves text files to `system-workspace/text-data/raw/raw_{filename}.txt`.
*   **Key File:** `modules/vision.py`

### Phase 2: Processing & Indexing
*   **Menu Option:** `C) Raw Processing`
*   **What it does:**
    *   **Merges:** Combines all `raw_*.txt` files into one huge file: `full_raw_indexed.txt` (with line numbers).
    *   **Indexes:** Reads `input/TOC.json` and uses Gemini to find exactly where each lesson starts and ends in the huge text file.
    *   **Outputs:** `system-workspace/text-data/raw_to_lesson_index.json`.
*   **Key File:** `modules/text_processing.py`

### Phase 3: Planning (The Architect)
*   **Menu Option:** `E) Plan Generation (Jules Batch)`
*   **What it does:**
    *   Uses `JulesPlanner` to create a "Jules Session" (Google Code Assist).
    *   Feeds the lesson text and the **Architect Persona** (`Architect_GEM_MASTER.md`).
    *   The Agent produces a structured Markdown plan describing every block (Header, Rule, Example, Exam).
    *   Saves the plan to `plans/{number}-{slug}-plan.md`.
*   **Key File:** `modules/jules_planner.py`

### Phase 4: Page Generation (The Developer)
*   **Menu Option:** `F) Page Generation (Jules Batch)`
*   **What it does:**
    *   Uses `JulesPageGenerator` to read the Markdown Plan.
    *   Starts a new Jules Session with the **Developer Persona**.
    *   Instructs the agent to map every plan block to a specific HTML template in `Jules-workspace/Templates/`.
    *   The Agent writes the code and commits it (or we pull it).
    *   Saves the HTML to `pages/{number}-{slug}.html`.
*   **Key File:** `modules/jules_page_generator.py`

### Phase 5: Verification & Audit
*   **Menu Option:** `G) Audit & Verify Pages`
*   **What it does:** Runs a suite of checks to ensure quality.

#### 1. Linter (`lint_pages.py`)
Checks for:
*   **Inline Styles:** Forbidden (e.g., `style="color: red"`).
*   **Undefined Classes:** Must be in `styles/main.css`.
*   **Semantic Rules:** e.g., "Exam" headers must be `.bg-dark` and questions must have an answer box.

#### 2. Layout Verifier (`verify_layout.py`)
*   Uses `WeasyPrint` to render the page virtually.
*   **One-Page Law:** Checks if content spills onto a second page. If it does, it reports **OVERFLOW**.
*   **Underflow:** Checks if there is too much whitespace (>10%).

#### 3. ID Manager (`id_manager.py`)
*   Every content block needs a unique ID (e.g., `id="b49210"`).
*   Run `python3 Jules\ workspace/id_manager.py auto-tag` to automatically assign IDs to new elements.

---

## 4. Key Components Deep Dive

### The Controller: `system.py`
This is your dashboard. It uses the `rich` library to display a beautiful status table. It tracks which lessons are `OCR_DONE`, `PLAN_READY`, or `CODED`.

### State Management: `state_manager.py`
The system needs to remember its brain. It stores the state of every lesson in `project_workflow_state.json`.
*   **Schema:**
    ```json
    "01": {
      "status": "CODED",
      "files": {
        "raw": "...",
        "plan": "...",
        "html": "..."
      },
      "last_updated": 1715000000
    }
    ```

### Templates: `Jules-workspace/Templates/`
We do not hardcode HTML. We use templates.
*   `TEMPLATE_C_HEADER.html`: Standard lesson header.
*   `TEMPLATE_C_BLOCK.html`: Generic content block with title.
*   `TEMPLATE_C_EXAM.html`: The "Test Yourself" section.
*   `TEMPLATE_C_SPLIT.html`: Two-column layout (Right: Rule, Left: Examples).

**Rule:** Always use `TEMPLATE_C_SPLIT` for Arabic grammar rules to ensure the text flows correctly (Right-to-Left).

### Workflow Manager: `workflow_manager.py`
(Advanced) This is a headless version of the system designed for CI/CD or fully automated runs. It can listen for GitHub Pull Requests and trigger Jules agents automatically.

---

## 5. Developer Guide: How to Contribute

### Setup & Prerequisites
Before you start, ensure you have the following:
1.  **Python 3.10+** installed.
2.  **Dependencies:** Run `pip install -r requirements.txt`.
3.  **API Keys:**
    *   You need a Google Cloud API Key with access to **Gemini 3.1 Pro** and **Google Code Assist**.
    *   Save it to `secrets/Jules_API.txt` or set the `JULES_API_KEY` environment variable.

### Adding a New Feature
1.  **Modify the Module:** Edit the Python file in `system-workspace/tools/automation/modules/`.
2.  **Update `system.py`:** If you added a new capability, add a menu option for it.

### Debugging
*   **Logs:** Check the console output. `system.py` uses color-coded logs (Red = Error, Green = Success).
*   **Intermediate Files:** Check `system-workspace/text-data/` to see exactly what text the AI is seeing.
*   **Plan Files:** If the HTML is wrong, check the `plans/*.md` file first. The Agent follows the plan strictly.

### Common Issues & Fixes
*   **"TOC file not found":** Ensure `input/TOC.json` exists and is valid JSON.
*   **"ModuleNotFoundError":** You might be missing dependencies. Run `pip install -r requirements.txt`.
*   **"Layout Overflow":** The content is too long for one page.
    *   **Fix:** Edit the HTML to remove non-essential examples.
    *   **Fix:** Split the lesson into `09.0` and `09.1`.
*   **"Duplicate ID":** Run `python3 Jules\ workspace/id_manager.py auto-tag` to fix it.

---

**Happy Automating!** 🚀
