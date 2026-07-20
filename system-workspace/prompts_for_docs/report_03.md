### `system-workspace/tools/automation/modules/auditor.py`
- **Status:** Usable
- **Purpose:** Acts as a Quality Assurance module. It runs verification scripts on generated HTML pages to check for layout overflows and linting errors.
- **Inputs:** Takes the path to an HTML file (e.g. `pages/01.html`). Uses internal tools like `Jules-workspace/verify_layout.py` and `Jules-workspace/lint_pages.py`.
- **Outputs:** Returns a status dictionary (`PASS` or `FAIL`) with details about layout and lint checks.
- **Usage:** ``python3 -c "from system_workspace.tools.automation.modules.auditor import Auditor; a = Auditor(); print(a.audit_page('pages/01.html'))"``
- **Workflow Integration:** Crucial for the '1-Plan-Per-Page' workflow. It validates that the generated HTML strictly adheres to the 'One-Page Law' (fits visually without overflow) and conforms to structural/linting rules before finalizing the page.
