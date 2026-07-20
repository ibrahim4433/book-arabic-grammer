# Objective

You are Jules, an expert coding AI agent and lead software architect.
You are tasked with executing the final step of **Phase 4** of the `ROADMAP_1_PAGE_PLAN.md` for this project.

Earlier, other Jules sessions analyzed 140+ tools in this project and generated detailed markdown reports located in `system-workspace/prompts_for_docs/report_*.md`.

## Your Instructions

1. **Aggregate the Data:** Read all the `report_*.md` files in `system-workspace/prompts_for_docs/`.
2. **Review & Compile:** Synthesize all the findings to understand the full tool landscape of the project. Pay special attention to tools marked "Usable" and those explicitly needed for the `1-Plan-Per-Page` workflow.
3. **Execute Phase 4.3 (Master Tool Index):**
   - Create a master catalog file named `TOOLS_DOCUMENTATION.md` in the root of the project. This file must contain the aggregated documentation of every usable/fixable tool, organized logically (e.g. grouped by directory).
4. **Create `Jules-workspace/JULES_TOOLS.md`:**
   - Extract the subset of tools located inside `Jules-workspace/` and create a dedicated documentation file for the agent named `JULES_TOOLS.md` inside `Jules-workspace/`.
5. **Create/Update `AGENTS.md`:**
   - Ensure an `AGENTS.md` file exists in the root directory. It must provide clear instructions to the Jules agent on the rules of the "1-Plan-Per-Page" model, emphasizing that it cannot summarize or delete text, must ensure A4 PDF compliance, and must run tools like `verify_layout.py` and `lint_pages.py`. Include a reference indicating that tools documentation is available in `Jules-workspace/JULES_TOOLS.md`.
6. **Code Updates (Optional but Recommended):**
   - Based on the reports, if any critical tools inside `Jules-workspace/` require minor inline documentation fixes (like missing docstrings), you may use your search-and-replace tools to add docstrings to them. Do not break any tool logic.
7. **Clean Up:**
   - You may delete the intermediate `report_*.md` files and `ALL_TOOLS.txt` once they have been successfully aggregated into `TOOLS_DOCUMENTATION.md`.

Be thorough, precise, and ensure your final documents are beautifully formatted using markdown tables or clear sections.

Good luck!
