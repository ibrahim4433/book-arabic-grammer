### `./system-workspace/tools/automation/modules/compiler.py`
- **Status:** Usable
- **Purpose:** Compiles Architect Plans (Markdown) into final HTML pages. It parses `=== BLOCK ===` markers, extracts component names and fields, maps them to HTML templates via `plan_to_template.json`, handles markdown-to-HTML transformations (lists, tables), and wraps the final output in the `TEMPLATE_C_PAGE_WRAPPER.html`. It can also dispatch plans to Jules.
- **Inputs:** `plan_path` (Path to a generated markdown plan file)
- **Outputs:** Saves an `.html` file inside the `pages/` directory.
- **Usage:** `python system-workspace/tools/automation/modules/compiler.py "path/to/plan.md"`
- **Workflow Integration:** This is a core translation engine. In the old workflow, it compiles lesson plans. In the new '1-Plan-Per-Page' workflow (Options M & N), it will be used to compile the strict 1-page plans into individual HTML files, relying heavily on the new Golden Style CSS wrappers to ensure perfect fit.
