# Elements Index

This document serves as a catalog of all available HTML templates (elements) for the book. Use these templates to ensure consistency and adherence to the design system.

## 1. Page Wrappers & Structure

| Template File | Description | When to Use |
| :--- | :--- | :--- |
| `TEMPLATE_C_BASE.html` | The master HTML shell. | Contains `<html>`, `<head>`, `<body>`. Use as the starting point for any new page file. |
| `TEMPLATE_C_PAGE_WRAPPER.html` | The content wrapper `.force-new-page`. | Wraps **all** content inside the `<body>` of a page to enforce page breaks and layout rules. |
| `TEMPLATE_C_HEADER.html` | Standard Chapter Header. | At the very top of every content page (inside the wrapper). Contains Title, Lesson Number, and Author Info. |

## 2. Content Blocks

| Template File | Description | When to Use |
| :--- | :--- | :--- |
| `TEMPLATE_C_BLOCK.html` | Standard Content Card. | For Definitions, Rules, or General Text. Contains a teal header and a body. |
| `TEMPLATE_C_SPLIT.html` | Two-Column Grid. | For side-by-side comparisons (e.g., Past vs Present). Handles RTL stacking automatically. |
| `TEMPLATE_C_LIST.html` | List Block Wrapper. | A content block specifically designed to hold a `structured-list`. |
| `TEMPLATE_C_TABLE.html` | Table Block Wrapper. | A content block specifically designed to hold a `dense-table`. |
| `TEMPLATE_C_POEM.html` | Poem & Bio Container. | For literature sections. Includes a Bio Card for the poet and the Poem verses. |
| `TEMPLATE_C_EXAM.html` | Quiz/Exam Block. | For the "Test Yourself" section at the end of a chapter. |

## 3. Atomic Components (Injectable)

These components are typically injected *inside* the blocks above.

### A. Benefit Boxes (Tips & Warnings)
| Template File | Description | When to Use |
| :--- | :--- | :--- |
| `TEMPLATE_C_BENEFIT.html` | Standard Benefit Box (Teal/Neutral). | For general notes, rules, or extra info inside a text block. |
| `TEMPLATE_C_BENEFIT_WARNING.html` | Warning Box (Red/Orange). | For common mistakes (e.g., "Don't say X"). |
| `TEMPLATE_C_BENEFIT_TIP.html` | Tip Box (Yellow/Gold). | For mnemonic devices (e.g., "Remember Tawanina") or golden rules. |

### B. Lists & Tables
| Template File | Description | When to Use |
| :--- | :--- | :--- |
| `TEMPLATE_C_LIST_ITEM.html` | Single List Item (`<li>`). | Inside a `structured-list`. Use `[MARKER]` for bullets (`•`, `✅`, `❌`). |
| `TEMPLATE_C_TABLE_ROW.html` | Single Table Row (`<tr>`). | Inside a `dense-table`. |
| `TEMPLATE_C_CHIPS.html` | Horizontal Flex Container. | For listing small items side-by-side (e.g., pronouns "He, She, It") without vertical stacking. |

### C. Parsing (Irab)
| Template File | Description | When to Use |
| :--- | :--- | :--- |
| `TEMPLATE_C_IRAB.html` | Full Parsing Block. | A complete block containing a stack of parsing boxes. |
| `TEMPLATE_C_IRAB_BOX.html` | Single Parsing Box. | A single word-analysis box. Can be used standalone. |
| `TEMPLATE_C_IRAB_ROW.html` | Horizontal Parsing Row. | A flex container to hold multiple `IRAB_BOX`es side-by-side. |
| `TEMPLATE_C_IRAB_BOX_COMPACT.html`| Compact Parsing Box. | A version of the parsing box optimized for tight spaces or rows (smaller font/padding). |

## 4. Table of Contents (TOC)

Specialized templates for constructing the TOC pages.

| Template File | Description | When to Use |
| :--- | :--- | :--- |
| `TEMPLATE_C_TOC_PAGE.html` | TOC Page Wrapper. | The specific shell for TOC pages (distinct from standard pages). |
| `TEMPLATE_C_TOC_LEVEL.html` | Level 1 Header (`<h3>`). | For main sections (e.g., "First: Linguistic Level"). |
| `TEMPLATE_C_TOC_CATEGORY.html` | Level 2 Header (`<h4>`). | For subsections (e.g., "1- Grammar"). |
| `TEMPLATE_C_TOC_LIST.html` | List Container (`<ul>`). | Wraps the list of chapters. |
| `TEMPLATE_C_TOC_ITEM.html` | TOC Entry (`<li>`). | A single chapter row with dots and page number. |

## 5. Reference Templates

These files are full-page examples and should not be used for injection, but as a guide.
- `TEMPLATE_CHAPTER.html`
- `TEMPLATE_CHAPTER1_EXAMPLE.html`
- `TEMPLATE_CHAPTER2_EXAMPLE.html.html`
