# 📏 BOOK_RULES: The Arabic Grammar Design System

## 1. Core Philosophy
* **Modular:** Every chapter is built from standard "Atomic Components".
* **Dense:** Maximize A4 space. Use `split-grid` for comparisons. Avoid vertical stacking if horizontal works.
* **Visual:** Every rule needs an example. Every definition needs a colored header, and the definition text must be colored using `.text-accent`.
* **Tashkeel:** MANDATORY. All Arabic text must have full diacritics.
* **Highlighting:** Lesson-focused words in examples MUST be colored to aid learning.

## 2. The Atomic Components (CSS Class Reference)

### A. Headers & Layout
* **File:** `TEMPLATE_C_HEADER.html`
* **Usage:** Top of every new chapter.
* **Classes:** `.page-header-strip`, `.lesson-number`, `.header-title`, `.author-info`.

### B. Content Blocks (The Standard Card)
* **File:** `TEMPLATE_C_BLOCK.html`
* **Usage:** Definitions, General Rules.
* **Classes:** `.content-block`, `.block-header` (Teal), `.block-body`.
* **Variant:** `.block-header.accent` (Orange) for warnings or secondary info.
* **Rule:** If the block contains a **Definition** or **Concept Explanation**, the main explanatory paragraph must have the class `.text-accent`.

### C. Comparison Grids (Split View)
* **File:** `TEMPLATE_C_SPLIT.html`
* **Usage:** Comparing Noun vs. Verb, Past vs. Present.
* **Classes:** `.split-grid`, `.content-block`.

### D. Structured Lists
* **File:** `TEMPLATE_C_LIST.html`
* **Usage:** Listing rules or conditions.
* **Classes:** `.structured-list`, `.marker` (Checkmarks/Crosses).

### E. Data Tables
* **File:** `TEMPLATE_C_TABLE.html`
* **Usage:** Conjugations, Examples.
* **Classes:** `.dense-table`.

### F. Chips & Horizontal Lists
* **File:** `TEMPLATE_C_CHIPS.html`
* **Usage:** Listing small items side-by-side (e.g., pronouns "He, She, It") without vertical stacking.
* **Classes:** `.chips-container` (or inline flex style).

### G. Poetry & Bio
* **File:** `TEMPLATE_C_POEM.html`
* **Usage:** Literature examples.
* **Classes:** `.poem-container`, `.poem-line`, `.hemistich`, `.bio-card`.

### H. Grammar Analysis (I'rab)
* **File:** `TEMPLATE_C_IRAB.html`
* **Usage:** Parsing examples (Full Block).
* **Classes:** `.irab-box`, `.irab-word`, `.irab-details`.
* **Variants:**
    * `TEMPLATE_C_IRAB_ROW.html`: Horizontal container for multiple boxes.
    * `TEMPLATE_C_IRAB_BOX_COMPACT.html`: Compact box for tight spaces.

### I. Quizzes
* **File:** `TEMPLATE_C_EXAM.html`
* **Usage:** End of chapter tests.
* **Classes:** `.exam-question`, `.exam-number`.

### J. Table of Contents
* **Files:** `TEMPLATE_C_TOC_PAGE.html`, `TEMPLATE_C_TOC_LEVEL.html`, etc.
* **Usage:** Specialized templates for constructing the TOC pages.

### K. Text Highlighting (Focus Words)
* **Usage:** Apply to the specific word illustrating the grammatical rule in every example sentence.
* **Classes:**
    *   `.highlight-red`: **Primary Focus**. Use for the main concept of the section.
    *   `.highlight-blue`: **Secondary Focus**. Use for contrasting elements (e.g., Subject vs Object).
    *   `.highlight-green`: **Tertiary Focus**. Use sparingly if a third distinct category is needed.

## 3. Strict Layout Rules (The "One-Page" Law)
A. **Language:** content must be 100% Arabic (except for file codes/IDs).
B. **Numerals:** Visible numbers (page numbers, lesson numbers) must use Arabic-Indic digits (e.g., ١, ٢, ٣). Lesson numbers must be included in TOC pages for cross-reference.
C. **Atomic Pages:** Every HTML file in `pages/` must render to EXACTLY ONE PDF Page (A4).
D. **Splitting:** If content exceeds one page, split it into multiple HTML files (e.g., `01_topic.html`, `02_topic_cont.html`).
E. **Whitespace Optimization:**
   - **Overflow (Too big):** Split the file or condense the text/padding.
   - **Underflow (Too empty):** If a page has >20% whitespace at the bottom, pull content from the next page ( if it from the same lesson ) or expand diagrams/examples/text content to fill it.
F. **Stability:** Do not edit the CSS/Templates unless absolutely necessary to fix a layout break.

## 4. Unique Identification System (The ID Rule)
Every distinct content unit must have a permanent, unique identifier (ID) to facilitate precise referencing and updates.

### A. ID Format
*   **Format:** `bXXXXX` (The letter 'b' followed by 5 random digits).
*   **Example:** `id="b83920"`
*   **Uniqueness:** IDs must be globally unique across all pages.

### B. Target Elements
The following elements must always have an ID:
*   `<header>` (Page Header)
*   `.content-block` (Main Sections)
*   `.benefit-box` (Tips/Warnings)
*   `.irab-box` (Parsing Blocks)
*   `.poem-container` (Poetry)
*   `.bio-card` (Author/Bio)
*   `.exam-question` (Quiz Questions)
*   Direct children of `.split-grid`

### C. Tools
*   **Generator:** Use `tools/id_manager.py` to generate or manage IDs.
    *   `python3 tools/id_manager.py next-id`: Generate a new unique ID.
    *   `python3 tools/id_manager.py verify`: Check for duplicates.
    *   `python3 tools/id_manager.py auto-tag`: Automatically add IDs to elements that miss them.
