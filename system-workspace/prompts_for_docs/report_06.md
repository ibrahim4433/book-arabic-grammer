### `system-workspace/tools/new-tools/generate_toc_from_physical.py`
- **Status:** Usable
- **Purpose:** Generates a physical TOC by rendering each HTML file using WeasyPrint to count actual PDF pages, then building a multi-column TOC HTML.
- **Inputs:** All HTML files in `pages/`
- **Outputs:** Creates/overwrites `pages/00.X_TOC.html` files.
- **Usage:** `python3 system-workspace/tools/new-tools/generate_toc_from_physical.py`
- **Workflow Integration:** General generation workflow for physical PDF pagination.
