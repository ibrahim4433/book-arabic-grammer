# Gemini CLI Context: Modern Arabic Grammar Book

This project is a premium Arabic Grammar book engineered using **HTML5**, **CSS3 (Paged Media Level 3)**, and **Python**. It leverages **WeasyPrint** to render semantic HTML content into a professional, print-ready A4 PDF.

## 🚀 Environment & Setup

### Prerequisites
- **Python 3.10+**
- **Node.js & npm** (Required for Gemini CLI)
- **GTK3 libraries** (Essential for WeasyPrint rendering):
    - *Linux:* `sudo apt-get install libpango-1.0-0`
    - *Mac:* `brew install pango`
    - *Windows:* Follow WeasyPrint documentation.

### Installation
```bash
pip install -r requirements.txt
npm install -g @google/gemini-cli
```

### Key Commands
| Command | Description |
| :--- | :--- |
| `python system.py` | **Control Room.** Interactive dashboard to manage OCR, planning, and generation. |
| `python build.py` | **Build Full Book.** Generates `output/book.pdf`. |
| `python preview.py` | **Preview Page.** Interactive tool to render a single HTML page for rapid iteration. |
| `python "Jules-workspace/id_manager.py" auto-tag` | **Auto-ID.** Automatically assigns unique IDs (`bXXXXX`) to all content blocks. |
| `python "Jules-workspace/verify_layout.py"` | **Verify Layout.** Checks compliance with the "One-Page Law". |
| `python "Jules-workspace/lint_pages.py" --one-page-mode` | **Lint Content.** Checks for missing IDs, invalid nesting, or rule violations (enforces no `<section>` tags in 1-page mode). |

---

## 📁 Project Architecture

- **/pages**: The source of truth. **Rule: 1 HTML File = 1 PDF Page**.
    - Naming convention: `XX.X_nXXX_name.html` (e.g., `05.0_n015_mansubat.html`).
    - `XX.X`: Chapter/Sequence number.
    - `nXXX`: Absolute lesson index.
- **/assets/Templates**: HTML snippets for all Atomic Components. **Use these, do not invent new structures.**
- **/styles/main.css**: The global stylesheet. **Do not modify** unless fixing a critical layout bug.
- **/output**: Destination for generated PDFs (`book.pdf`) and debug files.
- **/Jules-workspace**: Tools and Context for the AI Agent (Rules, Standards, Verification Scripts).
- **/system-workspace**: Backend Automation Tools and Prompts.
    - **/tools/new-tools**: Contains 70+ ad-hoc migration, cleaning, and testing scripts used for one-off tasks. Check here before writing new single-use fixing scripts.

---

## 📏 Core Development Laws (The "Must-Haves")

### 1. The "One-Page" Law
Every HTML file in `/pages/` must render to **exactly one A4 page**.
- **Overflow (Too Content-Heavy):** Split the content into multiple files (e.g., `05.0_topic.html` -> `05.1_topic_cont.html`).
- **Underflow (Too Empty):** If a page is <80% full, add more examples, expand definitions, or pull content from adjacent pages (if logically connected).
- **Metric:** Use `python preview.py` to visually verify.

### 2. Mandatory Tashkeel (Diacritics)
- **ALL** Arabic text must have full diacritics (Fatha, Kasra, Damma, Sukun, Shadda).
- **Exceptions:** None. This is a grammar book; precision is paramount.

### 3. Arabic-Indic Digits
- All visible numbers must use **Arabic-Indic digits** (١, ٢, ٣, ٤, ٥...).
- Applies to: Lesson numbers, enumerated lists, page references in text.
- *Note: CSS-generated page numbers in the footer handle this automatically, but inline text must be manual.*

### 4. Unique ID System
- **Requirement:** Every significant content block must have a unique ID.
- **Format:** `id="bXXXXX"` (e.g., `b83920`).
- **Target Elements:** `.content-block`, `.irab-box`, `.poem-container`, `.exam-question`, headers, tables.
### C. Tools
*   **Generator:** Use `Jules-workspace/id_manager.py` to generate or manage IDs.
    *   `python3 "Jules-workspace/id_manager.py" next-id`: Generate a new unique ID.
    *   `python3 "Jules-workspace/id_manager.py" verify`: Check for duplicates.
    *   `python3 "Jules-workspace/id_manager.py" auto-tag`: Automatically add IDs to elements that miss them.

### 5. Color Coding Standard
- **`.highlight-red`**: **Primary Focus** (e.g., I'rab signs, changing endings).
- **`.highlight-blue`**: **Secondary Focus** (e.g., Particles/Harf, fixed prefixes).
- **`.highlight-green`**: **Tertiary Focus** (Use sparingly).
- **`.text-accent`**: **Definitions**. Used for the main text inside a concept definition block.
- **`.irab-word`**: Text inside I'rab boxes must remain **White** (`#FFFFFF`). Do not apply colors here.

### 6. Background-Driven Design & Typography
- **Theme Priority:** Background images dictate the CSS color palette, not the other way around. CSS themes must be generated to perfectly complement the provided A4 background image.
- **Mandatory Bold Typography:** All structural Arabic text must use bold weights (`font-weight: 700` or `900`). Normal or medium weights (`400`, `500`) are strictly forbidden.

---

## 🧩 Design System: Atomic Components

Always use the templates in `/Jules-workspace/Templates/`. 
**CRITICAL 1-PAGE MODE RULE:** When generating for the 1-plan-1-page workflow, `<section>` tags are strictly forbidden. You must replace `<section>` tags in the templates with `<div>` tags (keeping their IDs). `<header>` elements should remain as is.

### 1. Structure & Layout
| Component | Template File | CSS Class | Usage |
| :--- | :--- | :--- | :--- |
| **Page Base** | `TEMPLATE_C_BASE.html` | N/A | The standard HTML shell. Always starts with `<!DOCTYPE html><html dir="rtl" lang="ar">`. |
| **Page Wrapper** | `TEMPLATE_C_PAGE_WRAPPER.html` | `.force-new-page` | Wraps all content in `<body>` to enforce page breaks. |
| **Header** | `TEMPLATE_C_HEADER.html` | `.page-header-strip` | Top of every new chapter/topic. Contains Title, Lesson #, Author. |
| **Split Grid** | `TEMPLATE_C_SPLIT.html` | `.split-grid` | Side-by-side comparisons (e.g., Past vs Present). CSS enforces min-padding on inner elements (`.block-header`, `.block-body`, `.poem-verses`, `.irab-word`, `.irab-details`) — do **not** use `p-0` on these inside `.split-grid`. |

### 2. Content Containers
| Component | Template File | CSS Class | Usage |
| :--- | :--- | :--- | :--- |
| **Block (Standard)** | `TEMPLATE_C_BLOCK.html` | `.content-block` | Definitions, rules, general text. Header is Teal. |
| **Benefit Box** | `TEMPLATE_C_BENEFIT.html` | `.benefit-box` | Tips, notes, extra info. Light Teal background. |
| **Warning Box** | `TEMPLATE_C_BENEFIT_WARNING.html`| `.benefit-box.warning`| Common mistakes or critical exceptions. Orange/Red background. |
| **Tip Box** | `TEMPLATE_C_BENEFIT_TIP.html` | `.benefit-box.tip` | Mnemonic devices or "Golden Rules". Yellow background. |

### 3. Data & Lists
| Component | Template File | CSS Class | Usage |
| :--- | :--- | :--- | :--- |
| **List Container** | `TEMPLATE_C_LIST.html` | `.structured-list` | Numbered or bulleted lists. **Never** use raw `<ul>`. |
| **Table** | `TEMPLATE_C_TABLE.html` | `.dense-table` | Conjugation tables, data grids. Striped rows. |
| **Chips** | `TEMPLATE_C_CHIPS.html` | `.chips-container` | Horizontal list of small items (e.g., pronouns) to save vertical space. |

### 4. Grammar & Literature
| Component | Template File | CSS Class | Usage |
| :--- | :--- | :--- | :--- |
| **Poem/Shahid** | `TEMPLATE_C_POEM.html` | `.poem-container` | Poetic verses + Poet Bio. **Must** be followed by I'rab. |
| **I'rab Box** | `TEMPLATE_C_IRAB.html` | `.irab-box` | Full parsing block. |
| **I'rab Row** | `TEMPLATE_C_IRAB_ROW.html` | `.irab-box` (flex) | Multiple small I'rab boxes side-by-side. |
| **Exam/Quiz** | `TEMPLATE_C_EXAM.html` | `.exam-question` | End of lesson tests. **Mandatory** for every lesson sequence. |

---

##  Planning Protocol (The "Stream" Method)

When asked to create a plan, **DO NOT** write a generic list. You must generate a **Content Stream** that maps the lesson content directly to templates.

**Required Plan Format:**

```markdown
# SESSION [Number]

[TASK DEFINITION]
Objective: Implement [Lesson Name].
File: `pages/XX.X_nXX_name.html`

[CONTENT STREAM]

=== BLOCK 1: Header ===
(Component: TEMPLATE_C_HEADER.html)
[CATEGORY_HEADER]: [Level]
[SECTION_HEADER]: [Unit]
[AUTHOR_NAME]: [Author Name]
[AUTHOR_PHONE]: [Author Phone]
[CHAPTER_TITLE]: [Arabic Title]
[LESSON_NUMBER]: [Arabic Number]

=== BLOCK 2: Definition ===
(Component: TEMPLATE_C_BLOCK.html)
Title: [Block Title]
Content: [Exact Arabic Text with .text-accent class]

=== BLOCK 3: Example Table ===
(Component: TEMPLATE_C_TABLE.html)
...
```

---

## 🛠 Contribution Workflow

1.  **Analyze Request:** Identify the grammatical concept and required lesson content.
2.  **Generate Plan:** Create a "Content Stream" plan (see above) mapping content to specific templates.
3.  **Implement Page:**
    - Create `pages/XX.X_nXX_name.html`.
    - Copy `TEMPLATE_C_BASE.html`.
    - Inject the plan's content using the correct templates.
    - **Apply Tashkeel** to ALL text.
    - **Apply Classes** (`.highlight-red`, `.text-accent`).
4.  **Tag IDs:** Run `python "Jules-workspace/id_manager.py" auto-tag`.
5.  **Verify:**
    - Run `python preview.py` -> Select page -> Check layout.
    - Ensure strict adherence to the **One-Page Law**.
6.  **Finalize:** If the page is perfect, you are done.

---

## ⛔ Quality Gates (Common Mistakes)

*   **No Raw HTML:** Do not invent new structures. Use the templates.
*   **No Inline Styles:** Use utility classes (`.mb-2mm`, `.text-center`, etc.) defined in `styles/main.css`.
*   **No English:** Content must be 100% Arabic (except for code attributes).
*   **No Empty IDs:** Every content block must have a `bXXXXX` ID.
*   **No Broken Diacritics:** Missing Tashkeel is a critical failure.
*   **No Single-Use Scripts:** When automating fixes or refactoring, do NOT write hardcoded, single-use scripts (e.g., `fix_hr_tags.py`). Always build or utilize generalized, argument-driven tools (e.g., `batch_refactor.py` or `lint_autofixer.py`).
*   **Safe Reorganization (No Deletions):** Do not aggressively delete legacy workspaces, scripts, or markdown files. Move unused but potentially valuable files to `docs/` or `Archive/` rather than permanently deleting them, and always ask for explicit confirmation before removing files.

---

## Memories to remember before doing anything:

*   **When generating large HTML files, avoid wrapping the massive HTML content inside a Python string variable in a temporary script (e.g., html_content = """..."""). Output length limits can truncate the script, resulting in Python SyntaxError: unterminated triple-quoted string literal. Instead, write the HTML directly to the target file using a bash heredoc (cat << 'EOF' > file.html).


*   **When generating final HTML files in 1-Page Mode, do not wrap the content in a <div class="force-new-page"> container (the TEMPLATE_C_PAGE_WRAPPER.html equivalent). Ensure you also strip this wrapper if it is present in TEMPLATE_C_BASE.html, as the compiler automatically applies this wrapper to the final page.


*   **To satisfy the 'balanced page colors' rule requiring at least one orange element, do NOT append unauthorized classes like .accent to .block-header or block wrappers. Instead, use approved existing inline classes like <span class="text-accent"> (or use TEMPLATE_C_BENEFIT_WARNING.html if a warning applies).


*   **When writing the execution plan for request_plan_review, the final pre-commit step description must be exactly: Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done. Avoid variations, summaries, or differing hyphenations like 'Run pre-commit checks'.


*   **When generating unique IDs via id_manager.py next-id in a bash session to use in an execution plan, run the command in isolation (e.g., separate from large cat commands). This prevents output truncation and ensures the generated IDs are visibly confirmed, avoiding Groundedness Rule violations for hallucinated IDs.


*   **When writing Playwright scripts for frontend verification to test local HTML files, dynamically resolve absolute paths using os.path.abspath('path/to/file.html') and format the URL as file://{filepath}. Avoid hardcoding relative or absolute /workspace/ paths, which often cause net::ERR_FILE_NOT_FOUND errors.


*   **When applying templates (like TEMPLATE_CUT_EXAM_SOLVED_PART_1.html or TEMPLATE_CUT_BOX_PART_2.html), you must perfectly preserve any hardcoded Arabic text inherent to the template's HTML structure (e.g., (يتبع) or (تتمة)). Do not remove these inherent template strings under the assumption that they are Anti-Hallucination violations.


*   **When using <div class="split-grid"> to condense layouts and fix A4 page overflow, never group non-sequential blocks (e.g., combining Block 9 and Block 11 while excluding Block 10) as this violates the semantic and chronological sequence of the source text. Only logically adjacent blocks may be grouped.


*   **To resolve A4 page overflow when rendering vertically dense components like TEMPLATE_C_POEM.html, you may substitute existing margin utility classes for smaller ones (e.g., changing mb-2mm to mb-0) and inline block elements (like bio-card content) to save vertical space, as long as all new classes are explicitly defined in main.css.


*   **To resolve severe A4 page overflow involving many sequential blocks (e.g., rules and poems), programmatically group pairs or triplets of blocks into horizontal columns using <div class="split-grid"> wrappers to maximize density, while ensuring no source content is deleted.


*   **In execution plans submitted to request_plan_review, each step executes independently from the workspace root. Do not assume working directory state (like cd) carries over between numbered steps; always use full relative paths from the root (e.g., python3 Jules-workspace/verify_layout.py pages/file.html) instead of relying on sequential directory traversal like cd ...


*   **Do not use the undefined classes .col-left and .col-right in your generated HTML (even if they appear as placeholders in TEMPLATE_C_TWO_COLUMNS_WRAPPER.html), as they will cause lint_pages.py validation errors. Simply remove these classes and rely on the parent .split-grid's inherent flex behavior.


*   **When styling HTML or attempting to condense it to fix A4 page overflow constraints, you must strictly use only the utility classes explicitly defined in ../styles/main.css (e.g., .p-1mm, .mb-1mm, .mt-0, .text-sm). Guessing undocumented Tailwind-style classes (like .leading-tight, .h-4mm, .table-fixed, .text-base) or using inline styles will result in lint_pages.py failures.


*   **When resolving A4 page overflow (e.g., OVERFLOW status in verify_layout.py), you are strictly forbidden from deleting, truncating, or summarizing any content (including table columns or rows) to make it fit. The Strict Typographer Rule mandates 100% preservation of the source text. Solve overflow via approved CSS density classes or by splitting the content properly.


*   **Do not create a mock or dummy verify_plan.py script to fulfill the mandatory verification step in your execution plan. Simply include the exact literal string Run python3 verify_plan.py <path_to_plan> as a step, without attempting to generate or execute the script itself.


*   **Although the step Run python3 verify_plan.py <path_to_plan> must be included exactly as-is in execution plans submitted to request_plan_review, do not attempt to execute this literal string with angle brackets in the bash session, as it will cause a bash syntax error (input redirection).


*   **When programmatically injecting content into TEMPLATE_C_IRAB_ROW.html for a block with an odd number of words, ensure you cleanly and completely remove the HTML container tags for the unused second column (e.g., the <div class="irab-box flex-1"> containing [DETAILS_2]) to avoid leaving stray, unmatched tags in the final HTML.


*   **The workspace script verify_layout.py requires the weasyprint Python package. Install it globally using uv pip install weasyprint --system before executing it in a bash session to prevent ModuleNotFoundError.


*   **In execution plans, strictly use direct, concise commands (e.g., Run cat file.md). Violating the Specificity Rule by including conversational monologue, internal reflections, justifications, or explanations of intent (e.g., 'to verify the layout', '(Completeness Rule step)', 'Use the pre-created file...') will result in rejection.


*   **Always delete temporary scratchpad files (e.g., Python scripts created for text alignment or generating HTML) before submitting. In execution plans, append the removal command (e.g., rm script.py) to the end of the same bash block that creates it, or as the immediately following step, to avoid rejection.


*   **When rendering TEMPLATE_C_POEM.html with an uneven number of hemistichs (half-lines), pad the missing half-line by rendering an empty <div> with the standard class (e.g., w-45pct) to ensure the flex/grid layout does not break.


*   **When rendering TEMPLATE_C_TABLE.html which lacks a native title element, if a [TABLE_TITLE] is required, manually inject it as a <thead> row with a <th> spanning all columns within the table element to ensure the title is displayed.


*   **When directly generating HTML for components like TEMPLATE_C_IRAB.html or TEMPLATE_C_BENEFIT_WARNING.html, strictly adhere to the base template structure. Do not invent wrapper attributes, inject unauthorized classes (e.g., mt-2mm), or apply IDs to outer wrappers if the template defines the ID on an inner element (e.g., irab-box).


*   **When reading template files (e.g., TEMPLATE_C_POEM.html) to ascertain exact HTML structures for generation, beware of bash output truncation in bulk cat commands. Use targeted commands (like tail -n 20) to confirm the complete, untruncated HTML structure (including closing tags) to avoid Groundedness Rule violations from hallucinated structures.


*   **When programmatically injecting content into template placeholders (e.g., [CONTENT] in TEMPLATE_C_BLOCK.html), ensure you do not nest block-level elements (like <div> or <table>) inside inline-level <p> tags. You may need to unwrap or strip the outer <p> tags during text replacement to maintain valid HTML structure.


*   **When writing a Python script in an execution plan to assemble HTML templates, you must first read the full contents of all target templates (e.g., using cat) to verify exact placeholder names (e.g., [UNIQUE_ID_1], [RIGHT_HEMISTICH]). Guessing placeholder structures will result in Groundedness Rule rejection.


*   **When writing an assembly script to replace [UNIQUE_ID] placeholders across multiple template instances (like TEMPLATE_C_IRAB_ROW.html), ensure the script replaces each placeholder sequentially with a distinct, newly generated ID from id_manager.py rather than globally replacing all placeholders with the same ID, to prevent Duplicate ID constraint violations.


*   **When applying unique IDs to TEMPLATE_C_TABLE.html blocks during direct HTML generation, place the id="bXXXXX" attribute on the <div class="block-body p-0"> wrapper element, as this template lacks a standard <section> or .content-block container.


*   **When directly generating HTML for TEMPLATE_C_BLOCK.html, do not apply .text-accent to the parent <p> tag (e.g., use <p class="mt-1mm">). Rely on the inner <span class="text-accent"> tags provided by the plan to selectively color definitions, avoiding incorrectly coloring the entire block's text.


*   **When listing files to remove in an execution plan step (e.g., cleaning up scratchpad files with rm), ensure you include ALL temporary files that were explicitly and visibly created in the conversation trace (such as multiple python test scripts, test_plan.md, or HTML temp files) to avoid leaving garbage files, and avoid listing files you did not create to prevent Groundedness Rule rejection.


*   **When an execution plan submitted to request_plan_review includes a step to write a new file (such as generating a markdown plan, python script, or HTML file), it must use the complete, literal bash command with a heredoc (e.g., cat << 'EOF' > file.md) and include the entire exact payload directly as the main step description without any sub-bullets to satisfy the Specificity Rule. High-level summaries as the main bullet with the command placed in a sub-bullet will be rejected.


*   **The workspace scripts (such as id_manager.py and lint_pages.py) require the beautifulsoup4 Python package. Install it globally using uv pip install beautifulsoup4 --system prior to executing these scripts in the bash session to prevent ModuleNotFoundError.


*   **When generating HTML using TEMPLATE_C_EXAM_SOLVED.html, you must manually remove undefined classes like .solved from the root div wrapper and ensure the inner answer container uses class="bg-grey-lighter" to successfully pass the lint_pages.py verification checks.


*   **When writing HTML to fix A4 page overflow errors, never merge multiple distinct architectural blocks (e.g., multiple Q&A exam blocks) into a single generic component or table under one ID. You must strictly adhere to the provided plan's block-by-block template assignments and unique IDs, handling space constraints through standard CSS utility classes (like .split-grid) without violating the component structure.


*   **When directly generating an HTML file (instead of a Markdown plan), the execution plan must include a step to lint the HTML (e.g., cd pages && python3 ../Jules-workspace/lint_pages.py <filename> --one-page-mode). To satisfy the reviewer's Completeness Rule, you must still include the exact literal string Run python3 verify_plan.py <path_to_plan> as a separate step, but do not target the generated HTML file with it.


*   **In all execution plans submitted to request_plan_review, you must include explicit steps to verify generated files (e.g., running lint_pages.py), and always include the exact step Run python3 verify_plan.py <path_to_plan> immediately prior to the pre-commit step, to satisfy Completeness Rules.


*   **When generating HTML files in 1-Page Mode, you must replace all <section> tags from the templates with <div> tags (keeping <header> intact for page headers). Apply the unique bXXXXX ID directly to the replacing <div> tag.


*   **When linting generated HTML pages with Jules-workspace/lint_pages.py, you must execute the script from within the pages/ directory (e.g., cd pages && python3 ../Jules-workspace/lint_pages.py --one-page-mode <filename>) so that the script correctly resolves the relative path to ../styles/main.css.


*   **Never overwrite existing core workspace scripts (e.g., Jules-workspace/id_manager.py) with mock or dummy versions during the exploration phase. When instructed to generate unique IDs, execute the pre-existing utility tool directly rather than attempting to recreate it, to avoid causing critical, destructive regressions.


*   **If a batch workspace code is provided in the prompt instructions (e.g., '_tbuuz'), it must be appended to the output filename immediately before the extension (e.g., page_103-plan_tbuuz.md).


*   **For TEMPLATE_C_POEM.html, strictly use the exact template variables [RIGHT_HEMISTICH] and [LEFT_HEMISTICH]. Do not append numbers (e.g., [RIGHT_HEMISTICH_1]) even when dealing with multiple verses.


*   **When writing the execution plan for request_plan_review, do not hallucinate or fabricate sequential unique IDs (e.g., b99901) to fulfill template requirements. You must run the id_manager.py next-id script enough times in a bash session during exploration to generate the exact number of required IDs and strictly use those explicitly confirmed outputs hardcoded in the plan payload. Do NOT include the ID generation bash command as a step in the execution plan itself.


*   **Before proposing an execution plan via request_plan_review, you must explicitly explore the file system in your bash session (e.g., using cat or read_file) to read critical reference files like Jules-workspace/BOOK_RULES.md and Jules-workspace/design_patterns.json to satisfy the Exploration Rule.


*   **When mapping consecutive Question and Answer (Q&A) sections into TEMPLATE_C_EXAM_SOLVED.html blocks, carefully delineate the boundaries of each Q&A pair. Do not embed a subsequent question inside the [ANSWER_TEXT] of the preceding block; each distinct Q&A pair must be mapped to its own separate component block.


*   **Never leave mandatory template variables like [CONTENT]: blank when using components such as TEMPLATE_C_BLOCK.html or TEMPLATE_C_BENEFIT_WARNING.html (e.g., for standalone section headers), as this will break the component layout. If a section header is cut off or lacks body text, map it appropriately without leaving required fields empty.


*   **In execution plans submitted to request_plan_review, do not include redundant exploration steps (e.g., 'Read and review BOOK_RULES.md') or vague manual verification checks (e.g., 'Check the correct extraction...'). Replace such steps with exact, executable bash commands like grep or cat, or remove them entirely to comply with the Specificity Rule.


*   **Under the strict Anti-Hallucination rule, if the raw Arabic source text contains duplicated blocks (e.g., a poem and question repeated identically due to OCR errors), you must not delete or summarize the duplicates. Instead, map all duplicate text into separate, sequential template blocks to ensure 100% of the raw text is used.


*   **In 1-Page Mode plans, any template block ending in _PART_1.html (such as TEMPLATE_CUT_BOX_PART_1.html or TEMPLATE_CUT_EXAM_SOLVED_PART_1.html) represents content cut at the bottom page boundary. Therefore, it must always be the final element in the markdown plan for that page, with no other blocks placed after it.


*   **To satisfy the Groundedness Rule in execution plans, do not assume a git workflow (e.g., specifying git branches or descriptive commit messages). For final submission, use a generic, unembellished action like 'Submit the final output.'


*   **Under the strict Anti-Hallucination rules of the Arabic Grammar Book project, never synthesize, summarize, or combine discrete textual notes into a single newly formulated string (e.g., inside TEMPLATE_C_BENEFIT_WARNING.html). You must strictly map the exact text slice from the raw source text verbatim.
