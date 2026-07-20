### `./system-workspace/tools/new-tools/rename_final.py`
- **Status:** Usable
- **Purpose:** Renders HTML pages (excluding templates) into a single WeasyPrint document and determines the absolute PDF page number for each file by injecting anchors. It calculates an offset based on a target file containing '98.34' (with a fallback) and renames the source HTML files using a regex-based pattern to include their calculated pagination.
- **Inputs:** `pages/*.html`, optional `pages/cover/front-cover.jpg`.
- **Outputs:** Renames HTML files in the `pages/` directory.
- **Usage:** `python3 system-workspace/tools/new-tools/rename_final.py`
- **Workflow Integration:** Syncs file names with actual PDF page numbers. Useful for the old workflow; for the 1-Plan-Per-Page workflow, it might need adjustments if the page mapping is already strict.
