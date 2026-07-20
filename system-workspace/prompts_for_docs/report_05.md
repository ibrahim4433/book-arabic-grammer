### `./system-workspace/tools/new-tools/fix_none_title.py`
- **Status:** Usable
- **Purpose:** Iterates through HTML files in `pages/` (excluding templates and TOCs), extracts the lesson numbers and titles using BeautifulSoup, normalizes the text into Arabic-Indic numerals, and tracks page numbers. It fixes missing titles for specific sections starting with "98." and dynamically compiles this data into HTML structures for multi-column TOC pages.
- **Inputs:** `pages/*.html`
- **Outputs:** Generates TOC HTML files in `pages/` directory.
- **Usage:** `python3 system-workspace/tools/new-tools/fix_none_title.py`
- **Workflow Integration:** Central to generating the dynamic Table of Contents based on the actual parsed content rather than a static JSON file.
