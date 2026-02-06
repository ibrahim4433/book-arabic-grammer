# Gemini CLI Context: Modern Arabic Grammar Book

This project is a high-quality Arabic Grammar book built using **HTML5**, **CSS3 (Paged Media Level 3)**, and **Python**. It uses **WeasyPrint** to render semantic HTML content into a professional A4 PDF.

## 🚀 Quick Start

### Prerequisites
- **Python 3.10+**
- **GTK3 libraries** (Required by WeasyPrint for rendering).
    - *Linux:* `sudo apt-get install libpango-1.0-0`
    - *Mac:* `brew install pango`
    - *Windows:* See WeasyPrint documentation.

### Installation
```bash
pip install -r requirements.txt
```

### Key Commands
- **Build Full Book:** `python build.py` (Generates `output/book.pdf`).
- **Preview Single Page:** `python preview.py` (Allows selecting a specific page to render).
- **Manage IDs:** `python tools/id_manager.py auto-tag` (Automatically adds unique IDs to elements).
- **Verify Layout:** `python tools/verify_layout.py` (Checks compliance with the "One-Page Law").

## 📁 Project Structure

- **/pages**: Source HTML files. **Rule: 1 File = 1 PDF Page**. Naming: `XX.X_nXX_name.html`.
- **/assets/Templates**: Reference HTML snippets for Atomic Components (Headers, Blocks, Tables, etc.).
- **/styles/main.css**: The single source of truth for all styling.
- **/output**: Contains generated PDFs.
- **/tools**: Utility scripts for linting, layout verification, and ID management.

## 📏 Core Development Rules

### 1. The "One-Page" Law
Every HTML file in `/pages/` must render to **exactly one A4 page**. 
- **Overflow:** Split into multiple files (e.g., `05.0_topic.html`, `05.1_topic_cont.html`).
- **Underflow:** Add examples or adjust content to fill at least 80% of the page.

### 2. Mandatory Tashkeel & Arabic-Indic Digits
- All Arabic text **MUST** have full diacritics (Tashkeel).
- Use Arabic-Indic digits (١, ٢, ٣) for all visible numbers (lesson numbers, page numbers in text).

### 3. Unique ID System
Every significant content block (`.content-block`, `.irab-box`, `.poem-container`, etc.) must have a unique ID in the format `id="bXXXXX"` (e.g., `b83920`). Use `tools/id_manager.py` to manage these.

### 4. Color Coding (Grammar Highlights)
- `.highlight-red`: Primary focus (e.g., I'rab signs).
- `.highlight-blue`: Secondary focus (e.g., Particles/Harf).
- `.text-accent`: Used for the main explanation text inside a definition block.

### 5. Atomic Components
Always use the established HTML structures from `assets/Templates/`:
- **Headers:** `.page-header-strip` at the top of new chapters.
- **Blocks:** `.content-block` for rules and definitions.
- **Grids:** `.split-grid` for side-by-side comparisons.
- **I'rab:** `.irab-box` for grammatical parsing.
- **Exams:** Every lesson sequence must end with an `.exam-question` section.

## 🛠 Technical Constraints
- **Units:** Use `mm` or `cm` for layout, `pt` or `rem` for fonts. **NEVER use `px`, `vh`, or `vw`**.
- **Direction:** Always `<html lang="ar" dir="rtl">`.
- **Fonts:** 
    - Body: *Noto Naskh Arabic* (optimized for Tashkeel).
    - Headings: *Noto Kufi Arabic*.

## 📝 Contribution Workflow
1. Create/Edit a page in `/pages/`.
2. Run `python tools/id_manager.py auto-tag` to ensure all elements have IDs.
3. Use `python preview.py` to check the layout and page count.
4. Run `python build.py` to verify the full book integration.
