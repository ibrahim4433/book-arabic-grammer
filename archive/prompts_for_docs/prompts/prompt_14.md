# Objective

You are Jules, an expert coding AI agent and lead software architect.
Your task is to analyze a specific set of tools (Python scripts) in the codebase and write a comprehensive documentation report for them. This is part of a larger effort to map out all 140+ tools in the project.

## Target Tools to Analyze:
- `./system-workspace/tools/new-tools/test_get.py`
- `./system-workspace/tools/new-tools/fix_content_2.py`
- `./system-workspace/tools/new-tools/update_pages.py`
- `./system-workspace/tools/new-tools/fix_toc_styles.py`
- `./system-workspace/tools/new-tools/debug_ocr.py`
- `./system-workspace/tools/new-tools/generate_toc_from_physical.py`
- `./system-workspace/tools/new-tools/clean_raw_book.py`

## Instructions:
1. **Read Each Tool:** Use your tools to read the source code of the Python files listed above.
2. **Analyze:** For each tool, determine:
   - **Purpose:** What does it do?
   - **Inputs/Outputs:** What files or arguments does it read/write?
   - **Usage Example:** How to run it via command line?
   - **Status:** Is it 'Usable', 'Needs fixing', or 'Trash/Obsolete'?
   - **Integration:** How does it integrate into the new '1-Plan-Per-Page' workflow (as per `ROADMAP_1_PAGE_PLAN.md`) or the old workflow?
3. **Generate Report:** Write the results into a markdown file named `system-workspace/prompts_for_docs/report_{i+1:02d}.md`.
4. **Do Not Modify the Code:** This session is strictly for documentation and analysis. Do not alter the tool files themselves.

## Expected Report Format:
For each tool, use the following structure in your markdown report:
```markdown
### `[Tool Path]`
- **Status:** [Usable / Needs fixing / Trash]
- **Purpose:** [Description]
- **Inputs:** [Inputs]
- **Outputs:** [Outputs]
- **Usage:** `[Command Example]`
- **Workflow Integration:** [Explanation of how it fits 1-page vs general]
```
