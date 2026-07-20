### `system-workspace/tools/automation/modules/unified_flow.py`
- **Status:** Usable
- **Purpose:** Manages concurrent generation of Plans and Pages using a unified task queue and thread pool. Identifies missing plans and pages, runs JulesPlanner and JulesPageGenerator, and monitors their tasks.
- **Inputs:** Reads `system-workspace/text-data/raw_to_lesson_index.json` to identify pending tasks. Also checks filesystem in `plans/` to see what is already generated.
- **Outputs:** Updates task statuses and eventually triggers creation of Plan `.md` and HTML files (via its sub-tools). Outputs logs via callbacks.
- **Usage:** ``python3 -c "from system_workspace.tools.automation.modules.unified_flow import UnifiedProductionManager; m = UnifiedProductionManager('.'); m.populate_queue([]); m.run()"``
- **Workflow Integration:** In the 'old' lesson-based workflow, it generates whole lesson plans. For the '1-Plan-Per-Page' workflow, it will need to be updated to populate tasks based on 1-page slices rather than full lessons (e.g. reading from a paginated index instead of `raw_to_lesson_index.json`).
