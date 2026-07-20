### `./system-workspace/tools/extra/verify_lesson_28.py`
- **Status:** Trash/Obsolete
- **Purpose:** Uses Playwright to take a full-page screenshot of a single, hardcoded lesson file (lesson 28).
- **Inputs:** `pages/09.0_n28_sarf_mizan.html`
- **Outputs:** `verification/lesson_28.png`
- **Usage:** `python3 ./system-workspace/tools/extra/verify_lesson_28.py`
- **Workflow Integration:** Old workflow. It relies on a hardcoded file path, making it unscalable for an automated pipeline like the 1-Plan-Per-Page model which requires dynamic or parameterized verification.
