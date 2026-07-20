# 🗺️ Architecture Roadmap: 1-Plan-Per-Page Generation Engine

This document outlines the technical architecture, execution steps, and system updates required to transition our automated book generation system to accept a new way of generating the book "1-Plan-Per-Page" model. This approach guarantees that generated HTML/CSS perfectly fits onto single printed A4 pages using WeasyPrint without overflowing or requiring per-page CSS hacks.

## 🎯 Core Objectives
1. **Find Golden Style Configurations:** Establish global CSS that handles the densest page perfectly.
2. **Handle Sliced/Cut Content:** Introduce smart, dynamic split elements for concepts cut between pages.
3. **Engine Update (Options M & N):** Update `system.py` and the agent prompts to strictly plan and build 1-page limits using exact text slices.
4. **Tool Tidying & Documentation:** Audit, update, and properly document the Jules agents tools.

---

## 🚀 Execution Order summary
1. **Phase 4:** Audit and document existing tools first so we have a solid baseline.
2. **Phase 1:** Build the calibration tool and determine the global CSS, as everything else depends on the physical space available.
3. **Phase 2:** Build the UI components for cut content.
4. **Phase 3:** Write the new prompts, update `system.py`, and launch the new pipeline.

---
## 🏗️ Phase 1: The Visual Global Style Calibration Tool (Option O)
**Goal:** Build a local visual tool to discover the "golden" global CSS configuration by testing the densest content block in the raw text.

### Step 1.1: Content Density Algorithm
- **Task:** Create a script (e.g., `modules/density_analyzer.py`) to parse `input/TOC.json` and the auto-paginated raw text files (e.g., `raw-text/`).
- **Logic:** Calculate the character/word density and complexity (presence of tables, poems, etc.) for each page bounded by `----- PAGE X -----`.
- **Output:** Identify the single most dense page of raw text to serve as our "stress test".

### Step 1.2: Stress-Test Plan & Page Generation
- **Task:** Add logic to temporarily bypass 1-page constraints.
- **Action:** Dispatch a standard Jules planning and generation session (using existing prompts) for the identified densest page. The result is a raw HTML file with maximum content density (no page number limits).

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
  - `TEMPLATE_CUT_BOX_PART_1.html`: (For the bottom of page N) Designed with an "open" bottom border, faded text gradient at the cut, or a suitable better design ...
  - `TEMPLATE_CUT_BOX_PART_2.html`: (For the top of page N+1) Designed with an "open" top border, or a suitable better design ...
- **CSS:** Add specific classes in `styles/main.css` to support these visuals (e.g., `.border-open-bottom`, `.border-open-top`).

### Step 2.2: Strict Component Rules
- **Task:** Create specific markdown rules enforcing visual continuity.
- **Action:** Update the design system instructions so the agent know what type of content fit what template so that the same content type will have the same template parts on deffirant pages  (preventing a scenario where `part 1` uses Element A, but `part 2` on the next page hallucinates and uses Element B) .

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

### Step 3.3: Tool Integration for Agents
- **Task:** Ensure the agent prompts explicitly guide the agent on how to use tools (like `test_weasy.py` or a new `check_page_overflow.py` or others found in the project directory as needed) to verify that the generated HTML doesn't exceed a single PDF page before finalizing its task and do the plan as perfect as it could so we got error-free perfect final results.

---

## 🛠️ Phase 4: Update and Fix Tools for the Jules Agent
**Goal:** Clean up, document, and prepare the local toolsets for the new 1-page workflow and the default current old way.

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
  - How it integrates into the new 1-Plan-Per-Page workflow when its used by the system.
- **Expert Suggestion:** *We should consider adding an `AGENTS.md` file (or updating existing ones) that the AI naturally reads to understand which tools are available and how to invoke them during the planning and generation loops.*

---


## 🗺️ **the preview of everything above:**

We are updating our generation logic to adopt a new "1-Plan-Per-Page" model for generating book pages. I have refined the strategy for how we will achieve this. We need to update system.py to include these new options:

* **M)** Plan Generation (Jules Batch - 1-to-1 Page Mapping)
* **N)** Page Generation (Jules Batch - 1-to-1 Page Mapping)
* **O)** Book Style Tuning (Semi-automatic full process)

The goal is to feed the agent exactly one page's worth of raw text (defined by ----- PAGE X ----- markers) and have it generate the HTML/CSS that perfectly fits onto a single printed A4 page when rendered via WeasyPrint.

The fundamental constraint we face is mathematical: we cannot force a varying amount of text into a fixed physical boundary using fixed global CSS if the text is physically larger than the page. Furthermore, we absolutely cannot rely on per-page CSS hacks. We need one unified, beautiful, and global style for the entire Arabic grammar book and must fix all problems related to text sections getting cut between pages.

To achieve this, we need to solve 3 core problems:

1. **Finding the Golden Style Configurations:** Finding the exact CSS values (font sizes, element scales, line heights/widths, etc.) that ensure the largest, densest page text content fits nicely onto one generated PDF page without becoming unreadable, poorly designed, or corrupted. If we find this golden ratio, we ensure all other pages will also fit.
2. **Handling Sliced/Cut Content:** When a component (e.g., a definition, poem, etc.) is violently cut in half by a ----- PAGE X ----- marker, we cannot just dump broken HTML. We need to give the Jules agent specialized tools and dynamic elements that support splitting into two parts in a dynamic way, accompanied by good documentation on how, where, why, and for what content to use them.
3. **Special Instructions \& Rules:** Creating specific documentation and rules for the new "one plan for one page" method. These must affect the plan-making and page-generating processes so the Jules agent knows how to do it right and achieve the best possible results.

# **The Logic and Strategy**

## ** 1: The New Visual Global Style Calibration Tool (New Option O in system.py)**

To find the "golden" CSS values that guarantee our densest page fits on a single A4 sheet without overflowing, we will build a local visual calibration workflow:

* **Step A:** Algorithmically select the largest/densest text content block from the raw text. Send this to the Jules planner agent with instructions to generate a standard plan *without* any 1-page limits.
* **Step B:** Once the pre-step plan is detected, send it to the Jules page maker to generate a standard HTML test page, again *without* 1-page limits.
* **Step C:** Once the test-page HTML is ready, build a local visual tool with a real-time accurate preview (matching exactly how the WeasyPrint PDF will render). This tool must feature manual slider controls for scaling values, font sizes, padding, split-page views, and any other styling configs that affect page fitting.
* **Step D:** I will use this tool to manually trial configurations until I find the "sweet spot" where all text fits perfectly on one page without breaking the design or ruining readability.
* **Step E:** The tool must have a feature to build the test page into a final PDF to verify that the real-time preview matches the actual PDF output perfectly.
* **Step F:** Once reviewed and confirmed, we save these golden CSS values globally for the entire book.

## ** 2: Smart Sliced/Cut Content Architecture**

When a concept, definition, or poem is violently cut in half, the Jules agent must use special elements that support cutting into parts in a suitable way.

* **The Logic:** We will create specifically crafted, duplicate copies of our current structural elements tailored explicitly for cut text.
* **Dynamic States:** These custom elements will feature two dynamic states: part 1 (for the bottom of the first page) and part 2 (for the top of the next page).
* **Strict Component Rules:** We must establish smart logic and strict instructions for the planner/maker agents to ensure visual continuity. The agent must use the *exact same* element style for both parts of the cut text across the page break (e.g., preventing a hallucination where part 1 uses Element A, but part 2 on the next page uses Element B).

## ** 3: The "1-Plan-Per-Page" Engine Update (New Options M and N in system.py)**

Add the new options to start the planning/page-making process for specially prepared raw text via option "L) Raw Processing (Auto-Paginated Index \& TOC)". This will function similarly to current options E and F, but tailored for the new 1-plan-per-page logic (rather than 1 plan per lesson).

This includes editing the text prompt sent to the Jules agent to achieve these goals:

1. **Exact Text Slices:** Feed the planner agent the exact text slices between page markers, rather than broad topics/lessons.
2. **Strict 1-Page Fit:** The plan must instruct the Jules agent (the page maker) to fit the content entirely and smartly onto *one page only*. It must use the tools available in the @\[Jules-workspace] folder to test overloading and page numbers generated from turning the HTML into a PDF. At the same time, it must ensure the readability of the text and proper design (so it isn't smashed, corrupted, or unprintable).
3. **The Strict Typographer Rule:** Fix the system prompts to enforce that the agent uses 100% of the provided raw text. It is strictly forbidden from summarizing, deleting content, or adding new content to make it fit. It must rely on the golden CSS values and the smart use of elements to ensure it fits on one page.
4. **The Typo Exception:** If the agent detects an obvious typo, spelling error, or grammatical mistake in the raw Arabic text, it is explicitly permitted to fix it suitably during the planning phase.

*Note: To get a better understanding, you can find a raw text example with page breaking (where I ran option L from system.py) in /system-workspace/raw-text/, and a TOC in /input/TOC.json.*

## ** 4: Update and Fix Tools for the Jules Agent**

We need to tidy up and document every current tool in this project, including its accurate definition, usage, and purpose.

* You can find all tools in these directories: /Jules-workspace/ and /system-workspace/.
* We need to update the tools to be better suited for this project, write good documentation for them, and implement them into the workflow of the Jules agent in a seamless way.

