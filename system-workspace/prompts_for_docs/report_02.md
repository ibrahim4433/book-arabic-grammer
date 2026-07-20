### `./system-workspace/tools/automation/lesson_compiler.py`
- **Status:** Usable
- **Purpose:** Parses a structured markdown plan to extract blocks and fields, then compiles these into an HTML page by injecting content into base layout templates (e.g., `TEMPLATE_C_BASE.html`, `TEMPLATE_C_PAGE_WRAPPER.html`).
- **Inputs:** Markdown plan file path (`<plan_file>`) and HTML templates located in `assets/Templates`.
- **Outputs:** Compiled HTML file saved into the `pages/` directory.
- **Usage:** `python system-workspace/tools/automation/lesson_compiler.py <plan_file>`
- **Workflow Integration:** Seamlessly fits the 1-Plan-Per-Page workflow. It compiles a single HTML page based directly on the plan provided. It uses the `TEMPLATE_C_PAGE_WRAPPER.html` to ensure content respects page limits.
