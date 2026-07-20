### `./system-workspace/tools/new-tools/fix_parts.py`
- **Status:** Trash/Obsolete
- **Purpose:** Fixes HTML files by removing "(الْجُزْءُ ...)" from titles, cleaning up TOC elements using BeautifulSoup, and reformatting/rebuilding answer files into a merged layout.
- **Inputs:** `pages/*.html`, `pages/*TOC*.html`, `pages/98.00_p120_Answers.html`
- **Outputs:** Modifies and renames HTML files in `pages/`
- **Usage:** `python3 system-workspace/tools/new-tools/fix_parts.py`
- **Workflow Integration:** This belongs to an older bulk-processing or migration workflow that modified multiple files simultaneously. It does not fit the new '1-Plan-Per-Page' workflow which forbids modifying arbitrary multiple files per plan.

### `./system-workspace/tools/new-tools/fix_toc.py`
- **Status:** Trash/Obsolete
- **Purpose:** Cleans up Table of Contents HTML files by removing "(الْجُزْءُ ...)" text from Table rows (`<td>`) and headers (`<h1>`), deleting duplicate entries.
- **Inputs:** `pages/*TOC*.html`
- **Outputs:** Modifies the TOC HTML files in `pages/`
- **Usage:** `python3 system-workspace/tools/new-tools/fix_toc.py`
- **Workflow Integration:** Obsolete bulk processor for TOC files. Under the '1-Plan-Per-Page' workflow, TOCs are either dynamically generated or managed explicitly, avoiding regex-based sweeping changes over globbed files.

### `./system-workspace/tools/new-tools/renumber_lessons.py`
- **Status:** Trash/Obsolete
- **Purpose:** Iterates over all lesson HTML files, cleans up their titles (removing numbers), sequentially renumbers the lesson numbers in the HTML (converting to Arabic numerals), and creates a `lesson_mapping.json`.
- **Inputs:** `pages/*.html`
- **Outputs:** Modifies `pages/*.html` and creates `lesson_mapping.json`
- **Usage:** `python3 system-workspace/tools/new-tools/renumber_lessons.py`
- **Workflow Integration:** This tool mass-edits all pages and alters global sequential state, heavily violating the '1-Plan-Per-Page' isolated constraints.

### `./system-workspace/tools/new-tools/fix_book.py`
- **Status:** Trash/Obsolete
- **Purpose:** Reorganizes lesson titles by grouping parts, renames files to contain correct page numbers (pXX), updates answers pages, generates a blank page and builds exactly two TOC pages spanning 2 columns.
- **Inputs:** `pages/*.html`
- **Outputs:** Modifies `pages/*.html`, creates `pages/00.0_blank.html`, `pages/00.2_TOC.html`, `pages/00.3_TOC.html`, and renames multiple files.
- **Usage:** `python3 system-workspace/tools/new-tools/fix_book.py`
- **Workflow Integration:** Obsolete monolithic script that manages the entire book layout, pagination, and TOC generation. This completely contradicts the '1-Plan-Per-Page' paradigm where each plan is strictly limited to rendering and validating a single page slice.

### `./system-workspace/tools/new-tools/merge_all_prs.py`
- **Status:** Usable
- **Purpose:** Fetches all open Pull Requests for the repo `ibrahim4433/book-arabic-grammer` using a GitHub token, attempts to squash-merge them, and deletes the PR branches.
- **Inputs:** GitHub Token from `secrets/Github_Token.txt`
- **Outputs:** Merges PRs on GitHub and deletes branches. Logs output to stdout.
- **Usage:** `python3 system-workspace/tools/new-tools/merge_all_prs.py`
- **Workflow Integration:** Independent maintenance/automation script. Useful for repository management, distinct from the page generation workflow, but relies on API tokens.

### `./system-workspace/tools/new-tools/rebuild_toc.py`
- **Status:** Trash/Obsolete
- **Purpose:** Rebuilds `pages/00.3_TOC.html` by extracting answer entries from `backup_answers/98.*.html`, combining them with actual lesson entries on the left side, and generating a side-by-side (2-column) TOC table.
- **Inputs:** `backup_answers/98.*.html`, `pages/00.3_TOC.html.bak`
- **Outputs:** Modifies/rebuilds `pages/00.3_TOC.html`
- **Usage:** `python3 system-workspace/tools/new-tools/rebuild_toc.py`
- **Workflow Integration:** Outdated TOC builder for specific page requirements and backup files. It performs multi-file gathering which is obsolete under the '1-Plan-Per-Page' structure.

### `./system-workspace/tools/new-tools/test_weasy.py`
- **Status:** Usable
- **Purpose:** A small test script to verify WeasyPrint's rendering capabilities, specifically testing the `target-counter` CSS functionality for cross-referencing pages and `arabic-indic` numeral styles.
- **Inputs:** None (embedded HTML)
- **Outputs:** Prints WeasyPrint page objects to stdout.
- **Usage:** `python3 system-workspace/tools/new-tools/test_weasy.py`
- **Workflow Integration:** General test utility. Doesn't interfere with the 1-Page plans directly, but can be useful during debugging of WeasyPrint rendering or Golden CSS adjustments.
