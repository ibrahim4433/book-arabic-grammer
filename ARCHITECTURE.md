Project ArchitectureDirectory StructureRoot/
│
├── pages/                  # Content Source
│   ├── 00_frontmatter.html # Title page, Copyright, TOC
│   ├── 01_chapter1.html    # Chapter 1 content
│   ├── 02_chapter2.html    # Chapter 2 content
│   └── ... (sequential)
│
├── styles/                 # Styling Source
│   ├── main.css            # The Single Source of Truth for styles. Imports fonts/vars.
│   └── (Optional) theme.css 
│
├── assets/                 # Static Assets
│   ├── images/             # High-res images (300dpi preferred)
│   └── fonts/              # Local font files (if not using Google Fonts)
│
├── output/                 # Build Artifacts
│   └── book.pdf            # The final generated book
│
├── build.py                # The Build Script (WeasyPrint logic)
└── requirements.txt        # Python dependencies
Data FlowAuthoring: Content is written into individual HTML files in /pages/.Styling: All pages link to ../styles/main.css.Building: The build.py script:Scans /pages/ for all .html files.Sorts them alphabetically.Merges them into a single WeasyPrint document.Renders output/book.pdf.Key ConventionsImage Paths: Must be relative: ../assets/images/image.png.Page Breaks: Use CSS classes .page-break manually where needed, but rely on break-inside: avoid for components.
