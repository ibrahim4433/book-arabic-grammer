# 🛠️ Tools & Scripts Definition Index

This document provides a comprehensive index of all tools available in the **Modern Arabic Grammar Book** project. It explains *what* each tool does, *why* it exists, and *how* it fits into the automation workflow.

---

## 🏗️ Core Build System

### 1. `system.py`
*   **Location:** Root
*   **Purpose:** The central "Control Room" for the entire project.
*   **What it does:**
    1.  Provides an interactive menu for all workflow steps (OCR, Planning, Generation, Auditing).
    2.  Wraps all underlying automation modules (`modules/`).
    3.  Manages project state.
*   **Why:** Simplifies the workflow into a single entry point.

### 2. `build.py`
*   **Location:** Root
*   **Purpose:** The master builder.
*   **What it does:**
    1.  Scans `pages/` for all HTML files.
    2.  Sorts them alphanumerically.
    3.  Extracts the `<body>` content from each.
    4.  Injects global assets (Watermarks, Backgrounds).
    5.  Merges everything into a single Master HTML.
    6.  Uses `WeasyPrint` to render the final `output/export/book.pdf`.
*   **Why:** Ensures the "One-Page Law" (1 HTML file = 1 PDF page) is respected while generating a unified book artifact.

### 3. `preview.py`
*   **Location:** Root
*   **Purpose:** Rapid iteration viewer.
*   **What it does:** Allows the user to select a single HTML page from `pages/` and renders it immediately to `output/debug/preview.pdf`.
*   **Why:** Speed. Building the whole book takes time. This tool lets developers tweak CSS or content and see results in seconds.

---

## 🤖 Automation Suite (`system-workspace/tools/automation/`)

(Note: These are now primarily accessed via `system.py`)

### 4. `all_pics_to_text.py` / `modules.vision`
*   **Purpose:** Batch OCR (Optical Character Recognition).
*   **What it does:**
    1.  Scans `input/` for images (`.jpg`, `.png`).
    2.  Sends each image to **Gemini Flash/Pro** with a prompt to "Extract all Arabic text with full Tashkeel".
    3.  Saves the raw text to `system-workspace/text-data/raw/raw_X.txt`.
*   **Why:** The starting point of the pipeline. Converts physical book scans into digital raw data.

### 5. `create_lesson_index.py` / `modules.text_processing`
*   **Purpose:** Structural Mapping.
*   **What it does:**
    1.  Reads all raw text files.
    2.  Reads `system-workspace/text-data/TOC.txt` (Table of Contents).
    3.  Asks Gemini to map "Which lesson is in which file/lines?".
    4.  Generates `assets/data/raw_to_lesson_index.json`.
*   **Why:** Raw text is unstructured. We need to know that "The Verb" lesson starts at `raw_1.txt:Line 5` and ends at `raw_2.txt:Line 10` to process it effectively.

### 6. `plan_refiner.py` (The Architect) / `modules.planner`
*   **Purpose:** AI Planning & Pedagogical Design.
*   **What it does:**
    1.  Takes raw text for a specific lesson.
    2.  Consults `system-workspace/Architect_GEM_MASTER.md` (The Persona) and `assets/design_patterns.json`.
    3.  Generates a **Markdown Plan** that maps the content to specific HTML Templates (e.g., "Use `TEMPLATE_C_BLOCK` for this definition").
    4.  **Audits** the plan using `system-workspace/Architect_AUDITOR.md` to ensure quality.
    5.  Saves the approved plan to `plans/plan_LESSON_NAME.md`.
*   **Why:** Ensures consistency. Instead of writing HTML directly, we first design the *structure* of the page.

### 7. `lesson_compiler.py` (The Builder) / `modules.compiler`
*   **Purpose:** Code Generation.
*   **What it does:**
    1.  Reads a `.md` Lesson Plan.
    2.  Parses the "Blocks" (Header, Definition, Table, etc.).
    3.  Loads the corresponding HTML Templates from `assets/Templates/`.
    4.  Fills in the content (Title, Body, Fields).
    5.  Assembles the final HTML file in `pages/`.
*   **Why:** Automates the tedious HTML writing process. Ensures every page uses the correct classes and structure.

---

## 🛠️ Utility Tools (`Jules-workspace/`)

### 8. `verify_layout.py`
*   **Purpose:** Quality Assurance (QA).
*   **What it does:**
    1.  Renders a specific HTML page using WeasyPrint (headless).
    2.  Checks the Page Count.
    3.  **PASS:** If Page Count == 1.
    4.  **FAIL:** If Page Count > 1 (Overflow).
*   **Why:** Enforces the "One-Page Law" automatically.

### 9. `id_manager.py`
*   **Purpose:** Unique Identification.
*   **What it does:**
    1.  Scans all HTML files.
    2.  Finds content blocks (headers, boxes, questions) missing an `id`.
    3.  Assigns a unique `bXXXXX` ID to them.
*   **Why:** Essential for cross-referencing, digital indexing, and ensuring every piece of content is addressable.

---

## 📂 Documentation & Configuration

*   **`system-workspace/Architect_GEM_MASTER.md`**: The system prompt for the AI Architect. Defines *how* to think about layout.
*   **`system-workspace/Architect_AUDITOR.md`**: The system prompt for the AI Auditor. Defines the "Quality Gates".
*   **`Jules-workspace/elements_index.md`**: A catalog of all available HTML templates.

---

## 📊 Data & Assets

*   **`assets/Templates/`**: The "Lego Bricks" of the project. Reusable HTML components.
*   **`assets/design_patterns.json`**: Statistics on which components are used most often, helping the AI mimic existing style.
*   **`assets/data/raw_to_lesson_index.json`**: The map connecting Lesson Titles to Raw Text locations.
