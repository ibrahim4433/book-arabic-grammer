# 📏 BOOK_RULES: The Arabic Grammar Design System

## 1. Core Philosophy
* **Modular:** Every chapter is built from standard "Atomic Components".
* **Dense:** Maximize A4 space. Use `split-grid` for comparisons. Avoid vertical stacking if horizontal works.
* **Visual:** Every rule needs an example. Every definition needs a colored header.
* **Tashkeel:** MANDATORY. All Arabic text must have full diacritics.

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

## 3. Strict Layout Rules (The "One-Page" Law)
A. **Language:** content must be 100% Arabic (except for file codes/IDs).
B. **Numerals:** Visible numbers (page numbers, lesson numbers) must use Arabic-Indic digits (e.g., ١, ٢, ٣). Lesson numbers must be included in TOC pages for cross-reference.
C. **Atomic Pages:** Every HTML file in `pages/` must render to EXACTLY ONE PDF Page (A4).
D. **Splitting:** If content exceeds one page, split it into multiple HTML files (e.g., `01_topic.html`, `02_topic_cont.html`).
E. **Whitespace Optimization:**
   - **Overflow (Too big):** Split the file or condense the text/padding.
   - **Underflow (Too empty):** If a page has >20% whitespace at the bottom, pull content from the next page ( if it from the same lesson ) or expand diagrams/examples/text content to fill it.
F. **Stability:** Do not edit the CSS/Templates unless absolutely necessary to fix a layout break.
