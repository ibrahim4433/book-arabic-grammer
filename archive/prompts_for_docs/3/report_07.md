### `./system-workspace/tools/automation/modules/state_manager.py`
- **Status:** Usable
- **Purpose:** Manages and persists the workflow state across the system by reading and writing to `project_workflow_state.json`. It tracks the progression status (e.g., OCR_DONE, PLAN_READY, PAGE_GENERATED) of lessons/pages, cleans up state for deleted files, and provides consolidated views.
- **Inputs:** State modifications (via class methods), internal JSON file.
- **Outputs:** Updates `system-workspace/tools/automation/project_workflow_state.json`.
- **Usage:** `python -c "from modules.state_manager import StateManager; sm = StateManager(); sm.update_lesson_status('Lesson 1', 'PLAN_READY')"`
- **Workflow Integration:** Acts as the central nervous system tracking progress. For the new '1-Plan-Per-Page' workflow, it will be critical to track the status of individual sliced pages rather than monolithic lessons to guarantee no pages are skipped during batch generation.
