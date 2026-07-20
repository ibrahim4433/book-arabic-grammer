### `./system-workspace/tools/new-tools/merge_answers.py`
- **Status:** Usable / Needs fixing
- **Purpose:** Merges the content of two HTML answer files (`98.00_p120_Answers.html` and `98.43_p163_Answers.html`) into one, by appending the content of the second file (excluding headers) into the first file's container, and then deletes the second file.
- **Inputs:** `pages/98.00_p120_Answers.html`, `pages/98.43_p163_Answers.html`
- **Outputs:** Modifies `pages/98.00_p120_Answers.html`, deletes `pages/98.43_p163_Answers.html`
- **Usage:** `python system-workspace/tools/new-tools/merge_answers.py`
- **Workflow Integration:** This script appears to be a one-off or transitional tool used to consolidate split answer pages into a single logical file, possibly prior to rebuilding TOC or fixing physical pages. It may conflict with the 1-Plan-Per-Page workflow if it dynamically alters layout structures across multiple physical pages without verifying layout constraints.
