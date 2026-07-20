### `./system-workspace/tools/new-tools/count_pages.py`
- **Status:** Usable
- **Purpose:** Calculates the exact physical page length (number of PDF pages) each HTML file will consume by rendering them individually via WeasyPrint.
- **Inputs:** Reads all non-template HTML files in `pages/` and `styles/main.css`.
- **Outputs:** Prints out the starting page number and the length (in pages) for each HTML file, and the total expected page count.
- **Usage:** `python ./system-workspace/tools/new-tools/count_pages.py`
- **Workflow Integration:** Critical for the 1-Plan-Per-Page workflow to verify if specific HTML slices underflow or overflow their targeted page counts before full book compilation.
