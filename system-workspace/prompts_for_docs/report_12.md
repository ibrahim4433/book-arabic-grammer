### `system-workspace/tools/new-tools/full_cleanup.py`
- **Status:** Usable
- **Purpose:** Cleans up lesson titles by removing noise (like "تابع", "الجزء"), groups related lessons, updates H1 tags in HTML files, renames files, updates titles in answer files, and regenerates the TOC.
- **Inputs:** All HTML files in `pages/`
- **Outputs:** Modified HTML files with clean titles, renamed files, and updated TOC pages.
- **Usage:** `python system-workspace/tools/new-tools/full_cleanup.py`
- **Workflow Integration:** Important for ensuring consistent and clean titles across all generated lessons, answers, and the TOC.
