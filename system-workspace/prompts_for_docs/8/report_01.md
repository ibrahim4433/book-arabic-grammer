### `./system-workspace/tools/new-tools/fix_6_answers.py`
- **Status:** Trash/Obsolete
- **Purpose:** Hardcodes 6 specific string replacements for missing or incorrect answers in a specific answers page (`98.00_p120_Answers.html`).
- **Inputs:** `pages/98.00_p120_Answers.html`
- **Outputs:** Modified `pages/98.00_p120_Answers.html`
- **Usage:** `python3 ./system-workspace/tools/new-tools/fix_6_answers.py`
- **Workflow Integration:** Part of the old batch workflow, patching hardcoded text in a monolithic answers file. Obsolete under the new 1-Plan-Per-Page workflow.

### `./system-workspace/tools/new-tools/regenerate_answers.py`
- **Status:** Trash/Obsolete
- **Purpose:** Unifies recovered AI answers from JSON chunks and old backup HTML answers, matches them to questions found across all lesson HTML files, and regenerates a single massive answers file.
- **Inputs:** `chunks/answers_*.json`, `backup_answers/*.html`, `pages/*.html`
- **Outputs:** Modified `pages/98.00_p120_Answers.html`
- **Usage:** `python3 ./system-workspace/tools/new-tools/regenerate_answers.py`
- **Workflow Integration:** Highly tied to the old monolithic book-building workflow. Incompatible with the 1-Plan-Per-Page system where lessons and answers are processed individually.

### `./system-workspace/tools/new-tools/restore_and_fix.py`
- **Status:** Trash/Obsolete
- **Purpose:** Normalizes lesson titles in HTML files, adds "(الْجُزْءُ ...)" suffixes for multi-part lessons, renames files, syncs answer headers, and generates exactly 2 Table of Contents pages.
- **Inputs:** `pages/*.html`, `pages/98.*.html`
- **Outputs:** Modified and renamed `pages/*.html` files, `pages/00.2_TOC.html`, `pages/00.3_TOC.html`
- **Usage:** `python3 ./system-workspace/tools/new-tools/restore_and_fix.py`
- **Workflow Integration:** Batch-processes all HTML files simultaneously and relies on old file naming conventions. This violates the isolated nature of the 1-Plan-Per-Page workflow.

### `./system-workspace/tools/new-tools/fill_missing.py`
- **Status:** Trash/Obsolete
- **Purpose:** Replaces specific missing answers (identified by `إجابة غير متوفرة.`) in the global answers file by using a hardcoded python dictionary and a JSON list of missing questions.
- **Inputs:** `pages/98.00_p120_Answers.html`, `missing_qs.json`
- **Outputs:** Modified `pages/98.00_p120_Answers.html`
- **Usage:** `python3 ./system-workspace/tools/new-tools/fill_missing.py`
- **Workflow Integration:** Operates strictly on a legacy combined answers file. It does not align with the 1-Plan-Per-Page model.

### `./system-workspace/tools/new-tools/update_all_css_bg.py`
- **Status:** Usable
- **Purpose:** Recursively searches the codebase for all `.css` files and updates any `background-image` property to point to a standard background image path (`'../assets/page-background/background.jpg'`).
- **Inputs:** All `*.css` files within the repository.
- **Outputs:** Updated `*.css` files.
- **Usage:** `python3 ./system-workspace/tools/new-tools/update_all_css_bg.py`
- **Workflow Integration:** This is a general utility script. While it can be run in any workflow, it affects global styling across the project.

### `./system-workspace/tools/new-tools/rename_to_footer.py`
- **Status:** Needs fixing / Obsolete
- **Purpose:** Merges all HTML files into a single master document, uses WeasyPrint to parse it and determine absolute page numbers, then renames each source HTML file to include its physical page number (footer) with a calculated offset.
- **Inputs:** `pages/*.html`, `pages/cover/front-cover.jpg`
- **Outputs:** Renamed `pages/*.html` files.
- **Usage:** `python3 ./system-workspace/tools/new-tools/rename_to_footer.py`
- **Workflow Integration:** Operates on the entire set of pages at once and requires rendering the entire book via WeasyPrint. This contradicts the 1-Plan-Per-Page workflow.

### `./system-workspace/tools/new-tools/test_next.py`
- **Status:** Trash / Needs fixing
- **Purpose:** A development test script that tests the `TextProcessor` module by looking up the topic corresponding to lesson number "07" in a JSON index map.
- **Inputs:** `system-workspace/text-data/raw_to_lesson_index.json`
- **Outputs:** Console printout (Standard output)
- **Usage:** `python3 ./system-workspace/tools/new-tools/test_next.py`
- **Workflow Integration:** A standalone testing script, not used for production processing.
