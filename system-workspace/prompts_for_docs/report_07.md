### `system-workspace/tools/automation/modules/jules_client_plans.py`
- **Status:** Usable
- **Purpose:** Orchestrates the generation of Markdown plans by interacting with Jules and GitHub. Includes sophisticated logic for extracting PR details, pulling files via `git`, and constructing a massive 'mega prompt' for plan generation.
- **Inputs:** Takes lesson data (number, title, raw_text, metadata) and raw agent prompts.
- **Outputs:** Pulls generated plan `.md` files directly using Git checkout. Constructs the combined AI prompt string.
- **Usage:** `Used programmatically: `client = JulesPlanClient(); client.pull_plan_from_github(details, 'file.md')``
- **Workflow Integration:** Highly critical for the '1-Plan-Per-Page' workflow (Option M). The `construct_mega_prompt` function is responsible for injecting the explicit instructions (1-page fit, exact text slices, forbidden summaries) into the prompt sent to the Jules planner agent.
