### `./system-workspace/tools/new-tools/fix_metadata.py`
- **Status:** Usable
- **Purpose:** Automatically updates HTML headers, `<title>` tags, and lesson numbers in all lesson and answer HTML files to match the structural metadata inferred from their filenames.
- **Inputs:** Reads all `pages/*.html` files (excluding templates and specific prefixes).
- **Outputs:** Overwrites the modified HTML files in-place with corrected Arabic indic numerals, titles, and lesson details.
- **Usage:** `python ./system-workspace/tools/new-tools/fix_metadata.py`
- **Workflow Integration:** Heavily supports the 1-Plan-Per-Page workflow by ensuring each isolated HTML slice remains perfectly self-consistent in its metadata according to its filename before final compilation.
