### `./system-workspace/tools/new-tools/rebuild_toc_final.py`
- **Status:** Usable
- **Purpose:** Rebuilds the Table of Contents (TOC) HTML pages. It reads a `lesson_mapping.json` to generate TOC entries for lessons, extracts answer sections from `98.00_p120_Answers.html`, assigns dynamic page links using CSS `target-counter`, chunks the entries into multiple pages, and generates new `00.*_TOC.html` files.
- **Inputs:** `lesson_mapping.json`, mapped lesson HTML files, `pages/98.00_p120_Answers.html`
- **Outputs:** Generates multiple `pages/00.*_TOC.html` files and deletes old ones.
- **Usage:** `python system-workspace/tools/new-tools/rebuild_toc_final.py`
- **Workflow Integration:** Integrates with the workflow by automating the creation of the TOC based on the final generated HTML files and their assigned IDs. It relies on CSS `target-counter` to resolve physical page numbers during PDF generation, bypassing the need to hardcode physical page numbers in the HTML.
