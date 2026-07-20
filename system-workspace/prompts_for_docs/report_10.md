### `./system-workspace/tools/new-tools/index_and_toc.py`
- **Status:** Usable
- **Purpose:** Parses a raw text file to create an indexed version (adding line numbers) and extracts TOC (Table of Contents) information based on page markers, saving it as a JSON file.
- **Inputs:** `system-workspace/text-data/raw/raw_001.txt`
- **Outputs:** `system-workspace/text-data/raw_001_indexed.txt`, `input/TOC.json`
- **Usage:** `python3 system-workspace/tools/new-tools/index_and_toc.py`
- **Workflow Integration:** This tool fits into the initial stages of processing raw text and creating a TOC. It seems geared towards the general workflow rather than being specific to the 1-Plan-Per-Page approach.

### `./system-workspace/tools/new-tools/use_6_col_table.py`
- **Status:** Usable
- **Purpose:** Reads all generated HTML pages, extracts lesson numbers and titles, and generates a 6-column Table of Contents (TOC) HTML file split into chunks, updating `pages/00.X_TOC.html`.
- **Inputs:** `pages/*.html`
- **Outputs:** `pages/00.X_TOC.html` (where X starts from 2)
- **Usage:** `python3 system-workspace/tools/new-tools/use_6_col_table.py`
- **Workflow Integration:** Fits into the final assembly phase of the general workflow, gathering data from generated pages to create a comprehensive TOC.

### `./system-workspace/tools/new-tools/new-beta-page-maker/generate_lesson_11.py`
- **Status:** Usable
- **Purpose:** Generates HTML pages for Lesson 11 by hardcoding specific content, utilizing templates, and doing manual string replacements to assemble the layout into two pages (`11.0_nXX_الإبدال.html` and `11.1_nXX_الإبدال.html`).
- **Inputs:** Templates (e.g., `TEMPLATE_C_HEADER.html`, `TEMPLATE_C_TABLE.html`, `TEMPLATE_C_PAGE_WRAPPER.html`)
- **Outputs:** `pages/11.0_nXX_الإبدال.html`, `pages/11.1_nXX_الإبدال.html`
- **Usage:** `python3 system-workspace/tools/new-tools/new-beta-page-maker/generate_lesson_11.py`
- **Workflow Integration:** Represents a manual, hardcoded approach to page generation. It aligns more closely with the older workflow before dynamic plans were used, or acts as a specific beta test for a single lesson.

### `./system-workspace/tools/new-tools/new-beta-page-maker/generate_lesson_13.py`
- **Status:** Usable
- **Purpose:** Generates HTML pages for Lesson 13 using a more dynamic, data-driven approach (`BLOCKS_DATA` structure). It constructs the page block by block, verifying layout along the way, and splits into new pages when overflow occurs.
- **Inputs:** `BLOCKS_DATA` (hardcoded in the script), templates.
- **Outputs:** `pages/13.0_nXX_الإبدال.html`, `pages/13.1_nXX_الإبدال.html` (and possibly more depending on overflow).
- **Usage:** `python3 system-workspace/tools/new-tools/new-beta-page-maker/generate_lesson_13.py`
- **Workflow Integration:** This represents a transition towards a more automated approach, dynamically checking layout overflow. However, it still uses hardcoded data rather than parsing an external plan file.

### `./system-workspace/tools/new-tools/new-beta-page-maker/test_plan.py`
- **Status:** Usable
- **Purpose:** Tests a specific plan markdown file (`01-أَقْسَامُ الْكَلَاَمِ الْمُفِيدِ فِي اللُّغَةَ الْعَرَبِيَّةَ-plan.md`) to ensure it meets minimum requirements, such as having at least 4 blocks, including mandatory components, correct author metadata, and class usage.
- **Inputs:** `plans/01-أَقْسَامُ الْكَلَاَمِ الْمُفِيدِ فِي اللُّغَةَ الْعَرَبِيَّةَ-plan.md`
- **Outputs:** Console output (pass/fail assertions)
- **Usage:** `python3 system-workspace/tools/new-tools/new-beta-page-maker/test_plan.py`
- **Workflow Integration:** Fits perfectly into the 1-Plan-Per-Page workflow by acting as a validator for generated plan files before they are processed into HTML.

### `./system-workspace/tools/new-tools/new-beta-page-maker/generate_25.py`
- **Status:** Usable
- **Purpose:** Parses a plan text file (`plan.txt`), generates HTML blocks using templates, checks the layout dynamically, and splits the content across multiple pages if overflow is detected.
- **Inputs:** `plan.txt`, `Jules-workspace/Templates/*.html`
- **Outputs:** `pages/25.X_nXX_علامات الترقيم.html`
- **Usage:** `python3 system-workspace/tools/new-tools/new-beta-page-maker/generate_25.py`
- **Workflow Integration:** This script directly implements the dynamic parsing and generation envisioned in the 1-Plan-Per-Page workflow, converting a structured plan into verified HTML pages.

### `./system-workspace/tools/new-tools/new-beta-page-maker/generate_lesson_19.py`
- **Status:** Usable
- **Purpose:** Generates HTML pages for Lesson 19 using a hybrid approach, leveraging helper functions to create blocks (like chips, tables, benefits) and manually assembling them into two pages.
- **Inputs:** Helper functions, hardcoded content, templates.
- **Outputs:** `pages/19.0_nXX_الهمزة المتطرفة.html`, `pages/19.1_nXX_الهمزة المتطرفة.html` (defined by constants).
- **Usage:** `python3 system-workspace/tools/new-tools/new-beta-page-maker/generate_lesson_19.py`
- **Workflow Integration:** Similar to `generate_lesson_11.py`, this is a bespoke script for a specific lesson, using helper functions for structure but relying on hardcoded content rather than a dynamic plan file.
