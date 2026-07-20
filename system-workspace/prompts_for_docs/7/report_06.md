### `./system-workspace/tools/new-tools/rename_to_physical.py`
- **Status:** Usable / Needs fixing
- **Purpose:** Renames HTML files in the `pages/` directory to include the physical page number they will start on in the final PDF. It does this by rendering each HTML file using WeasyPrint to determine how many physical pages it spans, maintaining a running total to calculate the starting page of the next file.
- **Inputs:** `pages/*.html`
- **Outputs:** Renames `pages/*.html` files (modifies filenames, not contents).
- **Usage:** `python system-workspace/tools/new-tools/rename_to_physical.py`
- **Workflow Integration:** Useful for syncing filenames with physical page numbers, but it requires running WeasyPrint on every file sequentially which is slow. In the strict 1-Plan-Per-Page workflow, files should ideally map 1:1 to physical pages, making this tool potentially redundant or indicating that files are still spanning multiple pages.
