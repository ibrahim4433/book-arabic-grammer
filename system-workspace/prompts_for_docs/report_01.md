### `./system-workspace/tools/new-tools/api.py`
- **Status:** Usable
- **Purpose:** A high-performance async FastAPI application that provides an API for rendering the Arabic Grammar Book PDFs on demand using WeasyPrint in a background thread.
- **Inputs:** `RenderRequest` (JSON) specifying `theme`, `watermark`, and `dry_run`. Reads `pages/*.html` and `styles/main.css` (or theme-specific CSS).
- **Outputs:** Generates a PDF file (`book.pdf`) in the specified theme directory or default export directory. Returns JSON success/error response or a downloadable file.
- **Usage:** `python api.py` (which runs `uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)`)
- **Workflow Integration:** Fits into the modern automated deployment/generation pipeline (likely integrating with the new workflow by dynamically serving the 1-Plan-Per-Page or full book PDF based on API calls).
