# **Project Architecture**

## **Documentation Map**

*   **`BOOK_RULES.md`**: The central Design System and content rules (The "One-Page Law", Atomic Components).
*   **`CODING_STANDARDS.md`**: Technical guidelines for HTML structure, CSS conventions, and Python scripts.
*   **`TECH_STACK.md`**: Defined technologies, constraints, and dependencies.
*   **`elements_index.md`**: The catalog of all available HTML templates and atomic components.
*   **`ARCHITECTURE.md`** (This File): High-level overview of file structure, data flow, and build logic.

## **Directory Structure**

```text
Root/  
│  
├── **pages/**                  # Content Source
│   ├── **cover/**              # Container for full-bleed cover images
│   │   ├── front-cover.jpg     # The Book Front Cover (A4)
│   │   └── back-cover.jpg      # The Book Back Cover (A4)
│   ├── 01.0_n01_toc_p1.html    # Table of Contents (Part 1)
│   ├── 01.1_n02_toc_p2.html    # Table of Contents (Part 2)
│   ├── 02.0_n03_verbs_past.html # Lesson Content
│   └── ...                     # (Follows naming: XX.X_nXX_name.html)
│
├── **assets/**                 # Static Assets
│   ├── **Templates/**          # Atomic HTML Component Patterns (Reference Only)
│   │   └── (See elements_index.md for full catalog)
│   ├── **page-background/**    # Assets for global background layers
│   ├── images/                 # High-res images (300dpi preferred)
│   └── fonts/                  # Local font files
│  
├── **styles/**                 # Styling Source
│   └── main.css                # **Single Source of Truth** for all book styling.
│  
├── **tools/**                  # Utility Scripts
│   └── verify_layout.py        # CLI tool to verify "One-Page Law" compliance.
│  
├── **output/**                 # Build Artifacts
│   └── book.pdf                # The final generated PDF.
│  
├── build.py                    # **The Builder**: Merges content and generates the PDF.
├── preview.py                  # **The Viewer**: Renders individual pages for quick previewing.
├── elements_index.md           # **The Catalog**: Index of all templates and components.
└── requirements.txt            # Python dependencies (includes `weasyprint`).
```

## **Data Flow & Build Logic**

1.  **Content Authoring:**
    *   Content is written in individual HTML files in `pages/`.
    *   Each file represents **exactly one A4 page**.
    *   Cover images are placed in `pages/cover/`.

2.  **The Build Process (`build.py`):**
    *   **Cover Detection:** Checks for `front-cover.jpg` and `back-cover.jpg` in `pages/cover/`.
    *   **File Scanning:** Scans `pages/` for `*.html` files (excluding templates).
    *   **Sorting:** Sorts files alphabetically (e.g., `01_` before `02_`).
    *   **Body Extraction:**
        *   Uses Regex (`<body[^>]*>(.*?)</body>`) to extract the *inner HTML* of the `<body>` tag.
        *   If no `<body>` tag is found, treats the entire file as a content fragment.
    *   **Injection:**
        *   Injects `front-cover.jpg` (if exists) as the first page (with zero margins).
        *   Concatenates all extracted body content.
        *   Injects `back-cover.jpg` (if exists) as the last page.
        *   Wraps the result in a Master HTML Shell (containing `<head>`, styles, and global fixed layers).
    *   **Rendering:** Uses `WeasyPrint` to generate `output/book.pdf`.

3.  **Validation (`tools/verify_layout.py`):**
    *   Renders a single HTML file to checking page count.
    *   **Fail:** If Page Count > 1.
    *   **Warn:** If empty space > 20% (Underflow).

## **Key Architectural Decisions**

*   **Atomic Design:** The book is built from "Atomic Components" (Templates) to ensure consistency.
*   **One-Page Law:** Strict constraint where 1 HTML File = 1 PDF Page.
*   **Zero-Margin Covers:** Cover images are handled specially to allow full-bleed printing, bypassing the standard 5mm margins defined in `main.css`.
*   **Global Layers:** Watermarks and Background Art are injected globally by the build script, not included in individual page files.
