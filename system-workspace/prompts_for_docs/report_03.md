### `./system-workspace/tools/new-tools/rename_to_absolute.py`
- **Status:** Usable
- **Purpose:** Determines the absolute page number in the final compiled PDF for each source HTML file by injecting anchors and rendering a virtual PDF using WeasyPrint.
- **Inputs:** Reads all HTML files in the `pages/` directory (excluding templates), `styles/main.css`, and a front cover image if present.
- **Outputs:** Prints out the mapping of HTML filenames to their absolute page numbers in the resulting PDF. Does not directly modify files.
- **Usage:** `python ./system-workspace/tools/new-tools/rename_to_absolute.py`
- **Workflow Integration:** Useful for aligning the logical 1-Plan-Per-Page HTML files with the final continuous physical PDF layout, helping trace where a specific HTML snippet lands in the final book.
