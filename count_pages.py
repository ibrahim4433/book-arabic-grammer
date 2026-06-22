from weasyprint import HTML
import glob, os, re

def to_arabic_indic(text):
    if text is None: return '-'
    english_to_arabic = {'0':'٠','1':'١','2':'٢','3':'٣','4':'٤','5':'٥','6':'٦','7':'٧','8':'٨','9':'٩'}
    return ''.join(english_to_arabic.get(c, c) for c in str(text))

all_files = sorted(glob.glob('pages/*.html'))
pages_files = [f for f in all_files if "TEMPLATE_" not in f]

master_html_start = """<!DOCTYPE html><html lang="ar" dir="rtl"><head><meta charset="UTF-8"><link rel="stylesheet" href="styles/main.css"></head><body>"""
master_html_end = """</body></html>"""

current_page = 2 # Front cover is 1, so the loop starts calculating from page 2.
file_pages_mapping = {}

for file in pages_files:
    basename = os.path.basename(file)
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract body
    body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL | re.IGNORECASE)
    if body_match:
        fragment = body_match.group(1)
    else:
        fragment = content
        
    full_html = master_html_start + fragment + master_html_end
    
    doc = HTML(string=full_html, base_url='.').render()
    num_pages = len(doc.pages)
    
    file_pages_mapping[file] = current_page
    print(f"{basename}: starts at {current_page}, takes {num_pages} pages")
    
    current_page += num_pages

print(f"Total expected pages without back cover: {current_page - 1}")
