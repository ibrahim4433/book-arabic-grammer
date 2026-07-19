# 🗺️ Architecture Roadmap: 1-Plan-Per-Page Generation Engine

This document outlines the technical architecture, execution steps, and system updates required to transition our automated book generation system to a "1-Plan-Per-Page" model. This approach guarantees that generated HTML/CSS perfectly fits onto single printed A4 pages using WeasyPrint without overflowing or requiring per-page CSS hacks.

## 🎯 Core Objectives
1. **Find Golden Style Configurations:** Establish global CSS that handles the densest page perfectly.
2. **Handle Sliced/Cut Content:** Introduce smart, dynamic split elements for concepts cut between pages.
3. **Engine Update (Options M & N):** Update `system.py` and the agent prompts to strictly plan and build 1-page limits using exact text slices.
4. **Tool Tidying & Documentation:** Audit, update, and properly document the Jules agents tools.

---

## 🏗️ Phase 1: The Visual Global Style Calibration Tool (Option O)
**Goal:** Build a local visual tool to discover the "golden" global CSS configuration by testing the densest content block in the raw text.

### Step 1.1: Content Density Algorithm
- **Task:** Create a script (e.g., `modules/density_analyzer.py`) to parse `input/TOC.json` and the auto-paginated raw text files (e.g., `raw-text/`).
- **Logic:** Calculate the character/word density and complexity (presence of tables, poems, etc.) for each page bounded by `----- PAGE X -----`.
- **Output:** Identify the single most dense page of raw text to serve as our "stress test".

### Step 1.2: Stress-Test Plan & Page Generation
- **Task:** Add logic to temporarily bypass 1-page constraints.
- **Action:** Dispatch a standard Jules planning and generation session (using existing prompts) for the identified densest page. The result is a raw HTML file with maximum content density.

### Step 1.3: Interactive Local Calibration Tool (New Web App)
- **Task:** Build a local Python web app (e.g., using Flask or FastAPI + Jinja2) and integrate it into `system.py` as **Option O**.
- **Features:**
  - **Live Preview:** A side-by-side or split pane view rendering the HTML file exactly as WeasyPrint would (A4 dimensions).
  - **Control Panel:** UI sliders for root CSS variables (e.g., `--font-size-base`, `--line-height`, `--element-padding`, `--scale-factor`).
  - **Dynamic Injection:** Update the preview pane's CSS in real-time via WebSocket or JS.
- **Expert Note:** *Since WeasyPrint has specific quirks (like how it handles `@page` rules and fragmentation), the live preview should use a JS library like Paged.js to closely mimic WeasyPrint's behavior in the browser, reducing surprises when generating the final PDF.*

### Step 1.4: WeasyPrint Verification
- **Task:** Add a "Generate Test PDF" button to the web app.
- **Action:** Upon clicking, the tool runs WeasyPrint on the current configuration, generating a PDF. This confirms that the web preview matches the final engine output.

### Step 1.5: Save Golden Values
- **Task:** Once the "sweet spot" is found manually, save the values back to `styles/main.css` (or a dedicated `variables.css` file imported globally).

---

## ✂️ Phase 2: Smart Sliced/Cut Content Architecture
**Goal:** Develop dynamic UI components that gracefully handle content sliced violently by a `----- PAGE X -----` marker.

### Step 2.1: Design "Split" Template Variants
- **Task:** In `Jules-workspace/Templates/`, create split variants of existing structural elements (e.g., definitions, example blocks, poems).
- **Files Needed:**
  - `TEMPLATE_CUT_BOX_PART_1.html`: (For the bottom of page N) Designed with an "open" bottom border, faded text gradient at the cut, or a "continued on next page" indicator.
  - `TEMPLATE_CUT_BOX_PART_2.html`: (For the top of page N+1) Designed with an "open" top border, or a "continued from previous page" indicator.
- **CSS:** Add specific classes in `styles/main.css` to support these visuals (e.g., `.border-open-bottom`, `.border-open-top`).

### Step 2.2: Strict Component Rules
- **Task:** Create specific markdown rules enforcing visual continuity.
- **Action:** Update the design system instructions so the agent understands that if a definition block starts with `TEMPLATE_CUT_BOX_PART_1` on page 3, the exact matching `TEMPLATE_CUT_BOX_PART_2` MUST be the first element on page 4.

---

## ⚙️ Phase 3: The "1-Plan-Per-Page" Engine Update (Options M & N)
**Goal:** Update `system.py` and the agent prompts to execute generation strictly based on pre-sliced page markers.

### Step 3.1: Update `system.py`
- **Task:** Introduce new options to the main menu.
- **Option M (Plan Generation - Jules Batch 1-to-1):** Iterate through the text blocks divided by `----- PAGE X -----` rather than logical lessons. Generate a unique markdown plan for every single page.
- **Option N (Page Generation - Jules Batch 1-to-1):** Iterate through the generated 1-page plans and produce exactly one `.html` file per page.

### Step 3.2: Create Dedicated Agent Prompts
- **Task:** Clone the existing master prompts to create specialized versions tailored to 1-page generation.
- **Files:** Create `system-workspace/Architect_GEM_MASTER_1_PAGE.md` and `system-workspace/Architect_AUDITOR_1_PAGE.md`.
- **New Prompt Instructions:**
  - **Exact Text Slices:** Only process the text strictly bound within the provided slice.
  - **Strict 1-Page Fit:** The output must visually fit on exactly one A4 page. Use available local workspace tools to verify overloading.
  - **The Strict Typographer Rule:** Must use 100% of the provided raw text. NO summarizing, NO deleting, NO adding new content.
  - **The Typo Exception:** Explicit permission to correct obvious typos or grammatical errors in the raw Arabic text during planning.
- **Expert Question:** *Should the Jules Agent be allowed to automatically move a single hanging word or orphan line to the next page's raw text file if it fails to fit, or should it strictly adhere to the provided page boundary no matter what? Strict adherence implies the bounds must be perfectly calculated before the prompt.*

### Step 3.3: Tool Integration for Agents
- **Task:** Ensure the agent prompts explicitly guide the agent on how to use tools (like `test_weasy.py` or a new `check_page_overflow.py`) to verify that the generated HTML doesn't exceed a single PDF page before finalizing its task.

---

## 🛠️ Phase 4: Update and Fix Tools for the Jules Agent
**Goal:** Clean up, document, and prepare the local toolsets for the new 1-page workflow.

### Step 4.1: Audit Existing Tools
- **Task:** Review all scripts in `Jules-workspace/` and `system-workspace/`. Ensure scripts (like `verify_layout.py`, `lint_pages.py`) can handle 1-page files effectively and don't assume lesson-level file structures.

### Step 4.2: Inline Code Documentation
- **Task:** Update docstrings and inline comments for every Python tool, clearly explaining their arguments, return values, and side effects.

### Step 4.3: Create Master Tool Index
- **Task:** Create `TOOLS_DOCUMENTATION.md` in the root (or `Jules-workspace/`).
- **Content:**
  - A catalog of every tool.
  - Its exact purpose.
  - Expected inputs/outputs.
  - Usage examples (e.g., `python3 Jules-workspace/verify_layout.py pages/01.html`).
  - How it integrates into the new 1-Plan-Per-Page workflow.
- **Expert Suggestion:** *We should consider adding an `AGENTS.md` file (or updating existing ones) that the AI naturally reads to understand which tools are available and how to invoke them during the planning and generation loops.*

---

## 🚀 Execution Order summary
1. **Phase 4:** Audit and document existing tools first so we have a solid baseline.
2. **Phase 1:** Build the calibration tool and determine the global CSS, as everything else depends on the physical space available.
3. **Phase 2:** Build the UI components for cut content.
4. **Phase 3:** Write the new prompts, update `system.py`, and launch the new pipeline.
