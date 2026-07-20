### `./Jules-workspace/verify_layout.py`
- **Status:** Usable
- **Purpose:** Verifies that a generated HTML page renders exactly to one A4 page without overflowing or significantly underflowing. Uses WeasyPrint to simulate PDF rendering. Also runs `lint_pages.py` internally unless skipped.
- **Inputs:** The target HTML page file.
- **Outputs:** Console output or JSON output with a layout status (`PASS`, `FAIL`, `OVERFLOW`, `UNDERFLOW`) and recommendations for fixing.
- **Usage:** `python Jules-workspace/verify_layout.py pages/01.0_intro.html`
- **Workflow Integration:** Critical for the new 1-Plan-Per-Page workflow to verify that generated pages satisfy layout constraints before finalization.
