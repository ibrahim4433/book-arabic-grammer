### `system-workspace/tools/automation/modules/pattern_extractor.py`
- **Status:** Usable
- **Purpose:** Analyzes existing HTML pages to extract design patterns, structural rules, and common component sequences.
- **Inputs:** Reads all HTML files located in the `pages/` directory.
- **Outputs:** Generates a rich JSON guide for Jules located at `Jules-workspace/design_patterns.json`.
- **Usage:** ``python3 system-workspace/tools/automation/modules/pattern_extractor.py``
- **Workflow Integration:** Provides essential context (Golden Flow, Component Frequencies) for the planner agents. In the '1-Plan-Per-Page' workflow, this helps the agent understand which templates to use and how they flow visually on a page, though it may need to be run against 1-page test files to extract 1-page specific patterns.
