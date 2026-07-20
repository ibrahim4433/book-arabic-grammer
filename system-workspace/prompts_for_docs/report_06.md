### `./system-workspace/tools/automation/workflow_state.py`
- **Status:** Usable
- **Purpose:** Tracks the high-level workflow status (e.g., RAW, PLANNED, CODED, VERIFIED) and history of lessons, storing this information in a JSON file.
- **Inputs:** `tools/automation/project_workflow_state.json`
- **Outputs:** Updates and saves to `tools/automation/project_workflow_state.json`
- **Usage:** Used as an imported module, or executed directly to print state: `python system-workspace/tools/automation/workflow_state.py`
- **Workflow Integration:** Geared towards tracking progress per lesson. For the 1-Plan-Per-Page workflow, this would need adjusting to track state per *page* rather than per *lesson*, since pages are processed independently.
