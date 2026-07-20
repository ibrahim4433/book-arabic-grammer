### `./system-workspace/tools/new-tools/rebuild_toc_paginated.py`
- **Status:** Usable
- **Purpose:** Rebuilds the Table of Contents (TOC) into multiple paginated HTML files by chunking TOC rows and answer references to prevent visual overflow.
- **Inputs:** `backup_answers/98.*.html` and `pages/00.3_TOC.html.bak`
- **Outputs:** Multiple paginated HTML files representing the new TOC.
- **Usage:** `python3 ./system-workspace/tools/new-tools/rebuild_toc_paginated.py`
- **Workflow Integration:** Directly aligns with the 1-Plan-Per-Page workflow by calculating and enforcing strict page item limits to prevent layout overflow in the final PDF.
