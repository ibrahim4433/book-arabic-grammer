### `./Jules-workspace/batch_refactor.py`
- **Status:** Usable
- **Purpose:** A batch refactoring tool that performs regex-based search and replace operations across all HTML files in the `pages/` directory.
- **Inputs:** Requires `--pattern` (regex) and `--replace` (replacement string) arguments. Can accept an optional `--dry-run` flag.
- **Outputs:** Modifies HTML files in-place or prints potential changes to the console (if in dry-run mode).
- **Usage:** `python Jules-workspace/batch_refactor.py --pattern "old-class" --replace "new-class"`
- **Workflow Integration:** Useful for bulk updates to styling or element IDs when migrating from legacy designs to the new Golden Style Configurations in the 1-page workflow.
