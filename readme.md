# 📘 Modern Arabic Grammar Book

A modern, high-quality Arabic Grammar book project built with **HTML**, **CSS Paged Media**, and **Python**.

## 🚀 Quick Start

### Prerequisites
* Python 3.10 or higher
* **GTK3 libraries** (CRITICAL: Required for WeasyPrint rendering).
    * *Linux:* `sudo apt-get install libpango-1.0-0`
    * *Mac:* `brew install pango`
   * *Windows:* Install the GTK/Pango runtime from the WeasyPrint docs; `pip install weasyprint` is not enough by itself.

### Installation
1. Clone the repository.
2. Install Python dependencies:
   `pip install -r requirements.txt`

### Building the Book
Run the central control room to manage OCR, generation, and building the book:
`python system.py`

If you see `libgobject-2.0-0` / `libpango` errors on Windows, the Python package is installed but the native GTK runtime is missing.

## **📂 Project Structure**

* **/pages**: Contains the source content. Each chapter is a separate .html file (e.g., 01\_intro.html).  
* **/styles**: Contains the CSS files. main.css controls the global layout and A4 dimensions.  
* **/assets**: Stores images and fonts.  
* **build.py**: The Python automation script that merges pages and renders the PDF.

## **✍️ Contribution Guidelines**

**Adding a New Chapter:**

1. Create a new file in /pages/ following the naming convention: XX\_topic\_name.html.  
2. Ensure the file starts with:  
   \<\!DOCTYPE html\>  
   \<html lang="ar" dir="rtl"\>

3. Link the stylesheet:  
   \<link rel="stylesheet" href="../styles/main.css"\>

4. Write your content using the approved semantic HTML tags (\<article\>, \<h1\>, .grammar-box).

**Design Rules:**

* **No Inline Styles:** Use classes defined in CODING\_STANDARDS.md.  
* **A4 Layout:** Do not change the global @page settings in main.css.  
* **Diacritics:** All Arabic text must include full Tashkeel.

## **🛠️ Technical Documentation**

For detailed technical constraints, rules, and tool documentation, please refer to:

* [GEMINI.md](GEMINI.md) \- Context and core rules for the AI coding assistant.
* [AGENTS.md](AGENTS.md) \- System rules, validation steps, and 1-page generation constraints.
* [TOOLS_DOCUMENTATION.md](TOOLS_DOCUMENTATION.md) \- Master index of all project tools and scripts.
* [ROADMAP_1_PAGE_PLAN.md](ROADMAP_1_PAGE_PLAN.md) \- Roadmap for the 1-Plan-Per-Page architecture.
