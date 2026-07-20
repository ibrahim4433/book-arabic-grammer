### `./system-workspace/tools/new-tools/parse_layout_ids.py`
- **Status:** Usable
- **Purpose:** Renders HTML pages into a WeasyPrint document and walks through the generated page boxes to extract layout elements with IDs starting with `ans-lesson-` and maps them to their absolute PDF page numbers.
- **Inputs:** `pages/*.html`
- **Outputs:** Writes `answers_pagination.json`
- **Usage:** `python3 system-workspace/tools/new-tools/parse_layout_ids.py`
- **Workflow Integration:** Essential for linking specific references (like answers) to physical pages in the final compiled PDF document.
