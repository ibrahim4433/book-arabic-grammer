# Elements Index

This document serves as the absolute source of truth for all HTML templates (elements) available for the book. These templates have been rigorously verified and extracted from the final output pages. **Do not deviate from these templates.**

## 1. Page Wrappers & Structure

| Template File | Description | When to Use |
| :--- | :--- | :--- |
| `TEMPLATE_C_BASE.html` | The master HTML shell. | Contains `<html>`, `<head>`, `<body>`. Use as the starting point for any new page file. |
| `TEMPLATE_C_PAGE_WRAPPER.html` | The content wrapper `.force-new-page`. | Wraps **all** content inside the `<body>` of a page to enforce A4 page breaks. |
| `TEMPLATE_C_HEADER.html` | Standard Chapter Header. | At the very top of every content page (inside the wrapper). Contains Title, Lesson Number, and Author Info. |

## 2. Content Blocks (Modular Containers)

| Template File | Description | When to Use |
| :--- | :--- | :--- |
| `TEMPLATE_C_BLOCK.html` | Generic Content Card. | A generic `<section class="content-block">` container for Definitions, Rules, or Text. Do not assume it has lists or tips inside. Inject those as needed. |
| `TEMPLATE_C_SPLIT.html` | Two-Column Grid. | For side-by-side content or comparisons. Remember RTL stacks right-to-left. |

## 3. Data & Lists (Injected inside Blocks)

| Template File | Description | When to Use |
| :--- | :--- | :--- |
| `TEMPLATE_C_LIST.html` | Structured List. | Contains `<ul class="structured-list">` and list items. Inject this into a `block-body` when enumerating points. |
| `TEMPLATE_C_TABLE.html` | Dense Table. | Contains a `<div class="block-body p-0">` wrapping a `dense-table`. Use for conjugations or data grids. |
| `TEMPLATE_C_CHIPS.html` | Flex Chips Container. | For listing small items (e.g., pronouns "He, She, It") side-by-side to save vertical space. |

## 4. Benefit Boxes (Alerts & Callouts)

These components are typically injected inside a `block-body` alongside text.

| Template File | Description | When to Use |
| :--- | :--- | :--- |
| `TEMPLATE_C_BENEFIT.html` | Standard Box (Teal/Neutral). | For general notes or extra info. |
| `TEMPLATE_C_BENEFIT_TIP.html` | Tip Box (Yellow/Gold). | For mnemonic devices or golden rules. |
| `TEMPLATE_C_BENEFIT_WARNING.html` | Warning Box (Red/Orange). | For common mistakes or exceptions. |

## 5. Grammar & Parsing (I'rab)

| Template File | Description | When to Use |
| :--- | :--- | :--- |
| `TEMPLATE_C_IRAB.html` | Vertical Stack Box. | A single I'rab box in a vertical flex stack. |
| `TEMPLATE_C_IRAB_BOX.html` | Single Parsing Box. | A standard single word-analysis box. |
| `TEMPLATE_C_IRAB_ROW.html` | Horizontal Parsing Row. | A flex container to hold two `irab-box` elements side-by-side (`flex-1`). |

## 6. Literature & Drills

| Template File | Description | When to Use |
| :--- | :--- | :--- |
| `TEMPLATE_C_POEM.html` | Poem Container. | Contains poetic verses (`hemistich`) and an optional poet bio block. |
| `TEMPLATE_C_EXAM.html` | Quiz/Exam Block. | For the "Test Yourself" section at the end of a chapter sequence. |
| `TEMPLATE_C_EXAM_SOLVED.html` | Solved Quiz/Exam. | For exam questions that already contain the answer in the raw text. |

## 7. Highlighting System (Inline Classes)

Use these classes directly on text (e.g., `<span class="highlight-red">`) to highlight specific elements in examples:
- `.highlight-red`: Primary Focus (e.g., I'rab signs)
- `.highlight-blue`: Secondary Focus (e.g., Particles)
- `.highlight-green`: Tertiary Focus
- `.text-accent`: Theme text color (used for main definitions)
- `.text-primary`: Primary theme text color variant

## 8. Keyword-to-Template Deterministic Mapping (For Cut Content)

To ensure visual continuity when content is cut across two pages, you **MUST** use the following strict mapping to deduce the correct template for a given text section. Both the page ending the cut and the page starting the cut must use the same element type defined here:

| Raw Text Keyword / Pattern | Mandatory Template |
| :--- | :--- |
| **"مدخل إلى النص:" / "حياة الشاعر" / Author Names** | `TEMPLATE_C_POEM.html` (Bio block) |
| **Lines starting with `-` containing dual parts (Verses)** | `TEMPLATE_C_POEM.html` (Verses block) |
| **"مهارات الاستماع" / "مهارات القراءة" / "الاستيعاب والفهم" / "المستوى الفكري" / "القاعدة" / "الخلاصة"** | `TEMPLATE_C_BLOCK.html` (Standard Block) |
| **"ج ١-" / "س:" / Q&A structures / "أولاً:" / "ثانياً:"** | `TEMPLATE_C_LIST.html` (Numbered/Bullet List) |
| **"فائدة" / "تذكر"** | `TEMPLATE_C_BENEFIT.html` |
| **"تنبيه" / "ملاحظة"** | `TEMPLATE_C_BENEFIT_WARNING.html` |
| **"قاعدة ذهبية" / "تلميح"** | `TEMPLATE_C_BENEFIT_TIP.html` |
| **"إعراب" / "أعرب"** | `TEMPLATE_C_IRAB.html` |
| **"تطبيق" / "تدريب" / "امتحان"** (Unsolved) | `TEMPLATE_C_EXAM.html` |
| **"تدريب محلول" / "امتحان" مع جواب** | `TEMPLATE_C_EXAM_SOLVED.html` (If cut, use `TEMPLATE_CUT_EXAM_SOLVED_PART_1/2.html`) |
