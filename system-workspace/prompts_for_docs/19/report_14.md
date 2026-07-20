### `./Jules-workspace/id_manager.py`
- **Status:** Usable
- **Purpose:** Manages the generation and assignment of cryptographically unique `bXXXXX` IDs across significant structural elements in HTML files. Prevents ID collisions.
- **Inputs:** Scans target HTML files in `pages/` directory (or specified via `--files`).
- **Outputs:** Injects missing `id="bXXXXX"` properties to elements defined in `TARGET_SELECTORS` directly within the file (unless `--dry-run` is used). Can also print new IDs or verify duplicates.
- **Usage:** `python Jules-workspace/id_manager.py auto-tag --files pages/01.html`
- **Workflow Integration:** Plays a critical role in mapping specific content blocks. Should be run after a new 1-page HTML generation or refactoring, but strictly before `verify_layout.py` or linting processes.
