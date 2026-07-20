### `./system-workspace/tools/new-tools/update_answers.py`
- **Status:** Usable
- **Purpose:** Synchronizes lesson numbers in the master answers file (`98.00_p120_Answers.html`) based on the current sequential numbering of the main lesson HTML files.
- **Inputs:** Reads `pages/*.html` lesson files to build a mapping, and reads `pages/98.00_p120_Answers.html`.
- **Outputs:** Overwrites `pages/98.00_p120_Answers.html` with updated Arabic lesson numbers and corresponding HTML `id` attributes.
- **Usage:** `python ./system-workspace/tools/new-tools/update_answers.py`
- **Workflow Integration:** Part of the maintenance for the new workflow, ensuring the consolidated answers index stays in sync when 1-Plan-Per-Page lesson files are added, removed, or renumbered.
