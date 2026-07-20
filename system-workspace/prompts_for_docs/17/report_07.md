### `./system-workspace/tools/new-tools/fix_names.py`
- **Status:** Usable
- **Purpose:** Prepares a master HTML document with global headers/covers, injects dynamic anchor tags into the first element of each page fragment, maps these anchors to absolute PDF page numbers via WeasyPrint, and renames the source HTML files to embed the page number (`prefix_p{abs_page:03d}_suffix`).
- **Inputs:** `pages/*.html`, optional `pages/cover/front-cover.jpg`.
- **Outputs:** Renames HTML files in `pages/` directory.
- **Usage:** `python3 system-workspace/tools/new-tools/fix_names.py`
- **Workflow Integration:** Synchronizes the file naming convention with the actual rendered PDF layout to ensure correct chronological order during final processing.
