# ⚙️ Functional Requirements

This document defines the core behaviors and features of the Automation System.

## 👤 User Stories

### As an Author (Content Creator)
1.  **Ingest:** I want to drop a folder of images (`input/*.jpg`) and have the system extract accurate Arabic text with diacritics automatically.
2.  **Structure:** I want the system to automatically map raw text to my Table of Contents (`TOC.txt`), creating a structured index.
3.  **Plan:** I want an AI "Architect" to propose a layout plan for each lesson before generating code, ensuring the pedagogical flow makes sense.
4.  **Build:** I want to run a single command (`workflow_manager.py`) to transform a raw lesson into a finished HTML page.
5.  **Verify:** I want the system to alert me *immediately* if a lesson exceeds one page (Overflow), so I can fix it.

### As a Developer (Maintainer)
1.  **Templates:** I want to add new HTML templates (`Jules-workspace/Templates/`) and have the system automatically start using them in new plans.
2.  **Styling:** I want to modify `styles/main.css` and see the changes reflected across the entire book instantly.
3.  **ID Management:** I want a tool to automatically assign unique IDs to every new content block for digital indexing.

---

## ✅ Core Features

### 1. Optical Character Recognition (OCR) Pipeline
*   **Input:** Images (`.jpg`, `.png`).
*   **Processing:** Google Gemini Vision API.
*   **Output:** UTF-8 Text files with full Tashkeel.
*   **Constraint:** Must preserve poetic verses and table structures as distinct blocks.

### 2. Intelligent Planning Engine
*   **Input:** Raw Text + Design Patterns.
*   **Logic:**
    *   Identify Definitions, Examples, Rules, and Exceptions.
    *   Map content to specific HTML Templates (Block, Table, Split-Grid).
*   **Output:** A Markdown Plan (`plans/plan_X.md`) validated by an AI Auditor.

### 3. Code Generation (The Compiler)
*   **Input:** Lesson Plan (`.md`).
*   **Logic:**
    *   Load HTML Templates.
    *   Inject content into placeholders.
    *   Assemble the page structure.
*   **Output:** Valid HTML5 file in `pages/`.

### 4. Layout Verification (The "One-Page Law" Enforcer)
*   **Input:** HTML Page.
*   **Logic:** Headless rendering via WeasyPrint.
*   **Criteria:** Page Count == 1.
*   **Action:** Return PASS/FAIL status.

### 5. Book Assembly
*   **Input:** All valid HTML pages in `pages/`.
*   **Logic:**
    *   Sort alphanumerically.
    *   Inject Cover, TOC, and Global Assets.
    *   Render to PDF.
*   **Output:** High-resolution PDF (`book.pdf`).

---

## ⚡ Edge Cases & Error Handling

*   **Text Overflow:** If content > 1 page, the system must FLAG the file and optionally suggest splitting it.
*   **Missing Diacritics:** The system should warn if the percentage of vocalized text drops below a threshold (future feature).
*   **Template Mismatch:** If a plan requests a non-existent template, fallback to a generic `TEMPLATE_C_BLOCK`.
*   **API Failure:** Graceful retry logic for Gemini API calls.
