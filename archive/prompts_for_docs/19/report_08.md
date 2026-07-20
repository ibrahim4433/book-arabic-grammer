### `./Jules-workspace/lint_templates.py`
- **Status:** Usable
- **Purpose:** An Anti-Bloat Pre-Flight check for HTML templates to ensure they do not contain forbidden tags (`<hr>`), inline styles, or generic `<ul>` tags without required classes. Ensures templates are clean shells.
- **Inputs:** Reads all HTML template files in `Templates/` or `Jules-workspace/Templates/` (skipping `TEMPLATE_CHAPTER*`).
- **Outputs:** Console output indicating success or listing rule violations. Fails with exit code 1 if violations exist.
- **Usage:** `python Jules-workspace/lint_templates.py`
- **Workflow Integration:** Can be run during testing or before generation to ensure base templates adhere to global styling rules for the 1-page workflow.
