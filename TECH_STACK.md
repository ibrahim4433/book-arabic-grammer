Tech Stack & Constraints
Core Frameworks
Runtime: Python 3.10+ (for build scripts)
Frontend: Standard HTML5 (Semantic)
Styling: CSS3 (Paged Media Level 3 specific)
Language: Arabic (Modern Standard Arabic - MSA) with mandatory full Diacritics (Tashkeel).
Build Engine
PDF Generator: WeasyPrint (Python library).
Automation: build.py script merges HTML files and renders the PDF.
Dependencies: Listed in requirements.txt (must include weasyprint).
Strict Project Constraints
Dimensions: Standard A4 Paper (210mm x 297mm).
Units: - Layout: mm or cm.
Fonts: pt or rem.
FORBIDDEN: Do NOT use px, vh, or vw for layout (causes print scaling issues).
Direction: ALWAYS set <html dir="rtl" lang="ar">.
Fonts: - Body: Noto Naskh Arabic (optimized for legibility of Tashkeel).
Headings: Noto Kufi Arabic.
File Architecture: Modular. One HTML file per chapter. NEVER a single index.html for the whole book.
