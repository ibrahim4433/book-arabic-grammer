### `system-workspace/tools/new-tools/parse_layout.py`
- **Status:** Usable
- **Purpose:** Analyzes the generated HTML to PDF layout using WeasyPrint to find which physical pages contain the "إجابات الدرس" headers.
- **Inputs:** All HTML files in `pages/` directory.
- **Outputs:** Generates `answers_pagination.json` mapping page numbers to answer section headers.
- **Usage:** `python system-workspace/tools/new-tools/parse_layout.py`
- **Workflow Integration:** Useful for generating accurate Tables of Contents or cross-referencing answer locations after rendering.
