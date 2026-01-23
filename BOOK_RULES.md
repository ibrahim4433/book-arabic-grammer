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

### F. Poetry & Bio
* **File:** `TEMPLATE_C_POEM.html`
* **Usage:** Literature examples.
* **Classes:** `.poem-container`, `.poem-line`, `.hemistich`, `.bio-card`.

### G. Grammar Analysis (I'rab)
* **File:** `TEMPLATE_C_IRAB.html`
* **Usage:** Parsing examples.
* **Classes:** `.irab-box`, `.irab-word`, `.irab-details`.

### H. Quizzes
* **File:** `TEMPLATE_C_EXAM.html`
* **Usage:** End of chapter tests.
* **Classes:** `.exam-question`, `.exam-number`.
