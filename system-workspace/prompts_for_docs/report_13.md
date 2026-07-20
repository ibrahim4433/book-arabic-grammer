### `./Jules-workspace/lint_pages.py`
- **Status:** Usable
- **Purpose:** Lints HTML files for design constraints and allowable utility classes.
- **Inputs:** Target files (command-line arguments, defaults to all files in `pages/`) and Golden Style Configurations (dynamically read from CSS via `get_valid_utility_classes`).
- **Outputs:** Console messages showing errors, and optional JSON output. Fails fast if violations are found.
- **Usage:** `python Jules-workspace/lint_pages.py pages/01.html`
- **Workflow Integration:** Can verify new files immediately generated under the new '1-Plan-Per-Page' or legacy pipeline.
