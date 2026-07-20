### `system-workspace/tools/automation/modules/jules_page_generator.py`
- **Status:** Usable
- **Purpose:** Submits generated Markdown plans to a Jules AI session, monitors the session, answers questions via Gemini, and pulls the finalized HTML file via PR.
- **Inputs:** Reads Markdown plans from the `plans/` directory.
- **Outputs:** Produces the final `.html` file, downloading it to `pages/` or `Jules-workspace/pages/`. Saves session IDs to the state manager.
- **Usage:** ``python3 -c "from system_workspace.tools.automation.modules.jules_page_generator import JulesPageGenerator; g = JulesPageGenerator('.'); g.run_batch_generation()"``
- **Workflow Integration:** Currently geared towards full lessons. For the '1-Plan-Per-Page' update (Option N), this module needs to handle the specialized 1-page agent prompts and enforce the strict file naming (`nXX` instead of lesson-based names). It executes the final step of turning a 1-page plan into a physical 1-page HTML.
