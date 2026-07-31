# AGENTS INSTRUCTIONS

Welcome! This file contains programmatic checks, rules, and guidance for all AI agents working in this repository.
The scope of this file is the entire directory tree. This repository uses two distinct workflows: **1-Page Mode** (for printing single A4 pages) and **Standard Lesson Mode** (for logical lesson flow). You must adhere to the rules of the specific mode you are tasked with.

## Universal Book Generation Rules (Applies to ALL Modes)

1. **The Strict Typographer Rule:** Use 100% of the provided raw text slice. NO summarizing, NO deleting, NO adding new content.
2. **Mandatory OCR Restoration (CRITICAL):** The raw text is raw OCR output. It is full of missing dots, garbled letters, broken Arabic-Indic numbers, and missing Harakat (diacritics). You MUST NOT blindly copy-paste this text into the plan. You are strictly REQUIRED to act as an expert Arabic proofreader: fix all spelling mistakes, restore missing dots and letters, correct garbled numbers, and perfectly reconstruct missing Harakat (diacritics) while preserving the exact original pedagogical meaning. NO raw OCR mistakes must reach the page maker agent.
3. **Template Mapping:** Every piece of content must be mapped to an approved HTML component in `Jules-workspace/Templates/`. Do NOT invent raw HTML structures.
4. **Content Integrity:** Preserve ALL Arabic Diacritics (Harakat) exactly as provided.
5. **Unique IDs:** Every content block must have a unique ID (`id="bXXXXX"`).

## Mode-Specific Rules

### A. 1-Page Mode (1-Plan-Per-Page)
The goal is to fit content exactly on a single A4 page for rendering via WeasyPrint.
1. **Exact Text Slices:** Only process the text strictly bound within the provided slice (typically bounded by `----- PAGE X -----`).
2. **Strict 1-Page Fit:** The output MUST visually fit on exactly one A4 page without underflow/overflow.
3. **Sliced Content:** For elements cut between pages, use specific dynamic split HTML templates (`TEMPLATE_C_SPLIT.html`, `TEMPLATE_CUT_BOX_PART_1.html` etc).
4. **Div Tags Only:** When mapping templates to content, `<section>` tags are strictly forbidden. You MUST replace any `<section>` tags in the template with `<div>` tags (keeping their IDs). `<header>` tags for page headers should remain as is.

### B. Standard Lesson Mode
The goal is to map entire logical lessons into HTML, allowing content to naturally flow across multiple pages.
1. **Semantic Sections:** Maintain the default `<section>` tags provided in the templates (unlike 1-Page mode).
2. **Logical Flow:** Map the content sequentially following the pedagogical flow of the lesson. 

## Tools

You have access to several specialized tools, particularly in the `Jules-workspace/` directory.

### Key Validation Tools
- **`verify_layout.py`**: Verifies that the generated HTML correctly renders onto a single A4 page without underflow/overflow. (Primarily used in 1-Page Mode).
  - Usage: `python3 Jules-workspace/verify_layout.py pages/file.html`
- **`lint_pages.py`**: Lints HTML files to ensure they conform to Atomic Design compliance and golden styles.
  - Usage (1-Page Mode): `python3 Jules-workspace/lint_pages.py pages/ --one-page-mode`
  - Usage (Standard Mode): `python3 Jules-workspace/lint_pages.py pages/`
- **`id_manager.py`**: Auto-tags block elements with unique IDs for layout tracing. Must be run before linting.
  - Usage: `python3 Jules-workspace/id_manager.py auto-tag`

### Dynamic Image Generation
- **Dummy Images**: Whenever a plan dictates the use of the `TEMPLATE_C_POET_BIO.html` element (for a poet's biography), you MUST create a dummy picture file at `input/integrated-pictures/pic_[IDENTIFIER].jpg` (where IDENTIFIER is the page or lesson number, e.g., `01` or `163`) during your page generation process using a bash command like `touch` or `cp`.

Refer to `JULES_TOOLS.md` (in `Jules-workspace/`) or `TOOLS_DOCUMENTATION.md` (in the project root) for the full list of tools. A dedicated list of tools documentation is available in `Jules-workspace/JULES_TOOLS.md` for AI agent usage.

Always run the available checks when making code changes.
