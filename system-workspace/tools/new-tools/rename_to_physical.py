import glob, os, re
from weasyprint import HTML

all_files = sorted(glob.glob('pages/*.html'))
pages_files = [f for f in all_files if "TEMPLATE_" not in f]

master_html_start = """<!DOCTYPE html><html lang="ar" dir="rtl"><head><meta charset="UTF-8"><link rel="stylesheet" href="styles/main.css"></head><body>"""
master_html_end = """</body></html>"""

current_page = 2

for file in pages_files:
    basename = os.path.basename(file)
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL | re.IGNORECASE)
    fragment = body_match.group(1) if body_match else content
    full_html = master_html_start + fragment + master_html_end
    
    doc = HTML(string=full_html, base_url='.').render()
    num_pages = len(doc.pages)
    
    # rename
    if "TOC" not in basename and "blank" not in basename and "intro" not in basename:
        # Match XX.X_pYYY_TITLE.html or XX.X_TITLE.html
        m = re.match(r'^([0-9]+\.[0-9]+)_(?:p[0-9]+_)?(.*\.html)$', basename)
        if m:
            prefix = m.group(1)
            suffix = m.group(2)
            new_name = f"{prefix}_p{current_page:03d}_{suffix}"
            new_path = os.path.join('pages', new_name)
            if file != new_path:
                os.rename(file, new_path)
                print(f"Renamed {basename} -> {new_name}")

    current_page += num_pages

print("Renaming complete.")
