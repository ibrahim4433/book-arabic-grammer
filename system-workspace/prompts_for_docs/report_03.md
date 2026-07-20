### `./system-workspace/tools/new-tools/clean_toc_duplicates.py`
- **Status:** Usable
- **Purpose:** Cleans duplicate entries from generated Table of Contents HTML files by parsing the tables using BeautifulSoup and removing duplicate rows based on title text.
- **Inputs:** `pages/00.*_TOC.html`
- **Outputs:** Modifies TOC files in-place.
- **Usage:** `python3 system-workspace/tools/new-tools/clean_toc_duplicates.py`
- **Workflow Integration:** A clean-up utility that ensures TOC integrity, applicable to both workflows after TOC generation.
