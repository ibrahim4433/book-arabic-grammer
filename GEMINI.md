# Gemini CLI Context: Modern Arabic Grammar Book

This project is a premium Arabic Grammar book engineered using **HTML5**, **CSS3 (Paged Media Level 3)**, and **Python**. It leverages **WeasyPrint** to render semantic HTML content into a professional, print-ready A4 PDF.

## 🚀 Environment & Setup

### Prerequisites
- **Python 3.10+**
- **GTK3 libraries** (Essential for WeasyPrint rendering):
    - *Linux:* `sudo apt-get install libpango-1.0-0`
    - *Mac:* `brew install pango`
    - *Windows:* Follow WeasyPrint documentation.

### Installation
```bash
pip install -r requirements.txt
```

### Key Commands
| Command | Description |
| :--- | :--- |
| `python build.py` | **Build Full Book.** Generates `output/book.pdf`. |
| `python preview.py` | **Preview Page.** Interactive tool to render a single HTML page for rapid iteration. |
| `python tools/id_manager.py auto-tag` | **Auto-ID.** Automatically assigns unique IDs (`bXXXXX`) to all content blocks. |
| `python tools/verify_layout.py` | **Verify Layout.** Checks compliance with the "One-Page Law". |
| `python tools/lint_pages.py` | **Lint Content.** Checks for missing IDs, invalid nesting, or rule violations. |

---

## 📁 Project Architecture

- **/pages**: The source of truth. **Rule: 1 HTML File = 1 PDF Page**.
    - Naming convention: `XX.X_nXX_name.html` (e.g., `05.0_n15_mansubat.html`).
    - `XX.X`: Chapter/Sequence number.
    - `nXX`: Absolute lesson index.
- **/assets/Templates**: HTML snippets for all Atomic Components. **Use these, do not invent new structures.**
- **/styles/main.css**: The global stylesheet. **Do not modify** unless fixing a critical layout bug.
- **/output**: Destination for generated PDFs (`book.pdf`) and debug files.
- **/tools**: Scripts for ID management, linting, and verification.

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
- **Workflow:** Write the code -> Run `python tools/id_manager.py auto-tag`.

### 5. Color Coding Standard
- **`.highlight-red`**: **Primary Focus** (e.g., I'rab signs, changing endings).
- **`.highlight-blue`**: **Secondary Focus** (e.g., Particles/Harf, fixed prefixes).
- **`.highlight-green`**: **Tertiary Focus** (Use sparingly).
- **`.text-accent`**: **Definitions**. Used for the main text inside a concept definition block.
- **`.irab-word`**: Text inside I'rab boxes must remain **White** (`#FFFFFF`). Do not apply colors here.

---

## 🧩 Design System: Atomic Components

Always use the templates in `/assets/Templates/`.

### 1. Structure & Layout
| Component | Template File | CSS Class | Usage |
| :--- | :--- | :--- | :--- |
| **Page Base** | `TEMPLATE_C_BASE.html` | N/A | The standard HTML shell. Always starts with `<!DOCTYPE html><html dir="rtl" lang="ar">`. |
| **Page Wrapper** | `TEMPLATE_C_PAGE_WRAPPER.html` | `.force-new-page` | Wraps all content in `<body>` to enforce page breaks. |
| **Header** | `TEMPLATE_C_HEADER.html` | `.page-header-strip` | Top of every new chapter/topic. Contains Title, Lesson #, Author. |
| **Split Grid** | `TEMPLATE_C_SPLIT.html` | `.split-grid` | Side-by-side comparisons (e.g., Past vs Present). Maximize horizontal space. |

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

## 📝 Planning Protocol (The "Stream" Method)

When asked to create a plan, **DO NOT** write a generic list. You must generate a **Content Stream** that maps the lesson content directly to templates.

**Required Plan Format:**

```markdown
# SESSION [Number]

[TASK DEFINITION]
Objective: Implement [Lesson Name].
File: `pages/XX.X_nXX_name.html`

[CONTENT STREAM]

=== BLOCK 1: Header ===
(Component: TEMPLATE_C_HEADER)
Title: [Arabic Title]
Lesson: [Arabic Number]

=== BLOCK 2: Definition ===
(Component: TEMPLATE_C_BLOCK)
Title: [Block Title]
Content: [Exact Arabic Text with .text-accent class]

=== BLOCK 3: Example Table ===
(Component: TEMPLATE_C_TABLE)
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
4.  **Tag IDs:** Run `python tools/id_manager.py auto-tag`.
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
