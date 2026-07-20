### `system-workspace/tools/automation/modules/planner.py`
- **Status:** Usable
- **Purpose:** Generates structured lesson plans using the Architect (Gemini) Persona by calling the Gemini API with raw Arabic text, metadata, and design patterns.
- **Inputs:** Reads from `system-workspace/Architect_GEM_MASTER.md`, `system-workspace/tools/automation/project_state.json`, `input/TOC.json`.
- **Outputs:** Markdown plan file in `plans/` directory.
- **Usage:** Used programmatically to generate lesson plans from raw text.
- **Workflow Integration:** This tool fits into both workflows but is primarily designed for the older lesson-based planning where it uses TOC data. To fully support the new '1-Plan-Per-Page' workflow (`ROADMAP_1_PAGE_PLAN.md`), it would need to strictly focus on the single page's text slice without relying heavily on whole-lesson metadata.
