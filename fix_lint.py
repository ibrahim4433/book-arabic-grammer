import glob
import os
import re

def fix_lint_errors():
    # Fix inline styles in Unit pages
    unit_files = glob.glob("pages/*unit*.html")
    for filepath in unit_files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace inline styles with CSS classes
        content = content.replace('style="padding-top: 80mm; text-align: center; min-height: auto;"', 'class="pt-80mm text-center min-h-auto"')
        content = content.replace('style="width: 80%; margin: 0 auto;"', 'class="w-80pct mx-auto"')
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
            
    # Fix section tags in specific files
    files_with_sections = [
        "pages/14.15_n035a_الموسيقا_الشعرية_cont.html",
        "pages/14.25_n036a_الموسيقا_الشعرية_cont.html"
    ]
    for filepath in files_with_sections:
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            content = content.replace("<section", "<div").replace("</section>", "</div>")
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
                
    # Add new utility classes to styles/main.css if not added
    css_additions = """
.pt-80mm { padding-top: 80mm !important; }
.min-h-auto { min-height: auto !important; }
.w-80pct { width: 80% !important; }
.mx-auto { margin-left: auto !important; margin-right: auto !important; }
"""
    with open("styles/main.css", "a", encoding="utf-8") as f:
        f.write(css_additions)
        
    print("Lint errors fixed.")

fix_lint_errors()
