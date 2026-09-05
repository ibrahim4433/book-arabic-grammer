import glob
import os

def fix_unit_pages():
    unit_files = glob.glob("pages/*unit*.html")
    for filepath in unit_files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace the class
        content = content.replace('class="force-new-page"', 'class="unit-page-wrapper"')
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed {filepath}")

fix_unit_pages()
