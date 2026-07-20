### `system-workspace/tools/automation/modules/jules_planner.py`
- **Status:** Usable
- **Purpose:** Orchestrates batch generation of lesson plans using Jules Sessions. It reads the text index, extracts text slices, constructs prompts, monitors remote Jules planning sessions, and pulls the resulting plan files.
- **Inputs:** System prompts and text index files.
- **Outputs:** Markdown plan files saved to `plans/` directory.
- **Usage:** Programmatically used via `JulesPlanner` class to execute batch generation.
- **Workflow Integration:** Needs minor adjustments to fit the '1-Plan-Per-Page' workflow. Currently maps texts to plans but must adapt its prompts strictly to page markers instead of broader lessons.
