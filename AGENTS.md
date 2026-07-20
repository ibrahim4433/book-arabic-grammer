# AGENTS INSTRUCTIONS

Welcome! This file contains programmatic checks, rules, and guidance for all AI agents working in this repository.
The scope of this file is the entire directory tree.

## Book Generation Rules (The 1-Plan-Per-Page Model)

We use a "1-Plan-Per-Page" workflow to generate a modern, beautifully typeset instructional textbook on Arabic grammar.
The goal is to fit content exactly on a single A4 page for rendering via WeasyPrint. The older workflow (lesson-based) may still be referenced or used in some legacy contexts or "old ways when selected".

1. **Exact Text Slices:** Only process the text strictly bound within the provided slice (typically bounded by `----- PAGE X -----`).
2. **Strict 1-Page Fit:** The output must visually fit on exactly one A4 page.
3. **The Strict Typographer Rule:** Use 100% of the provided raw text. NO summarizing, NO deleting, NO adding new content.
4. **The Typo Exception:** Explicit permission to correct obvious typos or grammatical errors in the raw Arabic text.
5. **Sliced Content:** For elements cut between pages, use specific dynamic split HTML templates (`TEMPLATE_C_SPLIT.html`, `TEMPLATE_CUT_BOX_PART_1.html` etc).

## Tools

You have access to several specialized tools, particularly in the `Jules-workspace/` directory.

### Key Validation Tools
- **`verify_layout.py`**: Verifies that the generated HTML correctly renders onto a single A4 page without underflow/overflow.
  - Usage: `python3 Jules-workspace/verify_layout.py pages/01.html`
- **`lint_pages.py`**: Lints HTML files to ensure they conform to Atomic Design compliance and golden styles.
  - Usage: `python3 Jules-workspace/lint_pages.py pages/`
- **`id_manager.py`**: Auto-tags block elements with unique IDs for layout tracing. Must be run before linting.
  - Usage: `python3 Jules-workspace/id_manager.py auto-tag`

Refer to `JULES_TOOLS.md` (in `Jules-workspace/`) or `TOOLS_DOCUMENTATION.md` (in the project root) for the full list of tools. A dedicated list of tools documentation is available in `Jules-workspace/JULES_TOOLS.md` for AI agent usage.

Always run the available checks when making code changes.
