### `./system-workspace/tools/extra/verify_changes.py`
- **Status:** Needs fixing
- **Purpose:** Uses Playwright to iterate over a hardcoded list of HTML pages and generate full-page screenshots for visual verification.
- **Inputs:** Specific HTML files like `pages/03.2_n10_mubtada.html`
- **Outputs:** `verification/*.png`
- **Usage:** `python3 ./system-workspace/tools/extra/verify_changes.py`
- **Workflow Integration:** Partially fits the old workflow for mass visual verification. To integrate into the 1-Plan-Per-Page workflow, it needs to be updated to accept dynamic inputs (like arguments or directories) instead of a hardcoded list.
