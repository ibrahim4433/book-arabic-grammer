### `./system-workspace/tools/automation/project_state.py`
- **Status:** Usable (May need fixing for 1-Page Workflow)
- **Purpose:** Manages, reads, updates, and verifies the current state of project generation (e.g., current lesson number, title, page index) by saving to a `project_state.json` file and parsing metadata from compiled HTML headers.
- **Inputs:** HTML files (for extracting metadata like page index and lesson number) and `project_state.json`.
- **Outputs:** `project_state.json` file and console outputs with state/verification results.
- **Usage:** `python system-workspace/tools/automation/project_state.py [init|read|update <filepath>|verify <filepath>]`
- **Workflow Integration:** Primarily designed for the old workflow where files and lessons track continuous progression. Needs to be adapted for the 1-Plan-Per-Page workflow to verify page indexes and handle page breaks within a single lesson properly, rather than relying solely on lesson titles.
