### `./Jules-workspace/lint_autofixer.py`
- **Status:** Usable
- **Purpose:** Automatically scans all HTML files in `pages/` and replaces known bad/forbidden CSS classes with approved Golden Style equivalents (e.g., `border-dashed` to `border-light`). It also removes `<hr>` tags.
- **Inputs:** Scans all `.html` files in the `pages/` directory.
- **Outputs:** In-place modifications to HTML files, followed by automatically running `lint_pages.py` to verify the fixes.
- **Usage:** `python Jules-workspace/lint_autofixer.py`
- **Workflow Integration:** Can be run immediately after an agent generates a page to automatically correct minor styling hallucinations before the final layout verification is performed.
