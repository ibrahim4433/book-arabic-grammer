### `./scripts/preview.py`
- **Status:** Usable
- **Purpose:** Renders individual HTML pages or templates from the pages directory into PDF format using WeasyPrint. It wraps the selected page in a master HTML template (injecting a global watermark text) to provide an accurate representation of how a single page will look when printed.
- **Inputs:**
  - Reads `.html` files from the pages directory.
  - Takes user input via CLI to select the file to render (by number or 't' for template).
- **Outputs:**
  - Writes a `.pdf` file to the generated output path.
- **Usage:** `python3 ./scripts/preview.py`
- **Workflow Integration:** In the new 1-Plan-Per-Page workflow (Options M & N), this tool is essential for the agent to verify that the generated HTML doesn't exceed a single PDF page before finalizing its task. It allows quick rendering of a single generated page into a PDF to check for layout issues without needing to compile the entire book.
