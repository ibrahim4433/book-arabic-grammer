### `./system-workspace/tools/new-tools/fix_logical_pages.py`
- **Status:** Trash / Obsolete
- **Purpose:** Attempts to read all lesson files to extract lesson numbers and titles to build a logical TOC, and generates basic TOC pages. However, it hardcodes logical page numbering (incrementing by 1 per file) which doesn't reflect actual physical PDF pages.
- **Inputs:** `pages/*.html` files
- **Outputs:** Generates `pages/00.*_TOC.html` files.
- **Usage:** `python system-workspace/tools/new-tools/fix_logical_pages.py`
- **Workflow Integration:** This script appears obsolete or superseded by `rebuild_toc_final.py` which uses a more robust JSON mapping and CSS `target-counter` for accurate page referencing. Generating logical page numbers that don't match physical pages is incorrect for the final PDF.
