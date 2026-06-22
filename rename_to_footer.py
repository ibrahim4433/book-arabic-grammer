import os, glob, re
from weasyprint import HTML

all_files = sorted(glob.glob('pages/*.html'))
pages_files = [f for f in all_files if "TEMPLATE_" not in f]

master_html_start = """<!DOCTYPE html><html lang="ar" dir="rtl"><head><meta charset="UTF-8"><link rel="stylesheet" href="styles/main.css">
<style>
    @page cover { margin: 0; size: A4; @bottom-center { content: none; } }
    .cover-page-wrapper { page: cover; width: 210mm; height: 297mm; overflow: hidden; break-after: page; position: relative; z-index: 20000; background: white; }
    .cover-page-wrapper img { width: 100%; height: 100%; object-fit: cover; }
</style></head><body>"""

has_front_cover = os.path.exists("pages/cover/front-cover.jpg")
if has_front_cover: master_html_start += f'<div class="cover-page-wrapper"><img src="pages/cover/front-cover.jpg"></div>\n'

accumulated_body_content = ""
file_ids = []
for i, page_file in enumerate(pages_files):
    with open(page_file, 'r', encoding='utf-8') as f: content = f.read()
    body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL | re.IGNORECASE)
    fragment = body_match.group(1) if body_match else content
    
    anchor_id = f"source_file_{i}"
    file_ids.append((i, page_file, anchor_id))
    accumulated_body_content += f'<div id="{anchor_id}"></div>\n' + fragment + "\n"

full_html = master_html_start + accumulated_body_content + "</body></html>"
doc = HTML(string=full_html, base_url='.').render()

anchor_to_page = {}
if hasattr(doc.pages[0], 'anchors'):
    for page_idx, page in enumerate(doc.pages):
        for anchor_name in page.anchors.keys():
            if anchor_name not in anchor_to_page:
                anchor_to_page[anchor_name] = page_idx + 1

# If the footer counter is exactly page_idx - 3 for the main content:
# Wait, let's just make sure. 
# If total pages is 159, and last page MUST BE 156, the offset is -3.
# Cover=1
# 00.0=2
# 00.1=3
# 00.2=4
# 00.3=5
# 01.0=6 -> 6 - 3 = 3? Wait! If offset is -3, then 01.0 is p003!
# But the user said "first lesson start at 6 and final lesson end on 158" before.
# If first lesson started at 6, and final was 158, total pages was 153.
# But wait, 158 - 6 = 152.
# Now if the user says 156 for final lesson, 156 - 6 = 150?
# Actually, the user says "it must be p156".

# Let's just set the offset so that the final file is exactly p156.
last_file_idx = len(pages_files) - 1
last_anchor = f"source_file_{last_file_idx}"
last_page_abs = anchor_to_page.get(last_anchor, 159)
offset = last_page_abs - 156

for i, file, anchor_id in file_ids:
    abs_page = anchor_to_page.get(anchor_id, 0)
    if abs_page > 0:
        footer_page = abs_page - offset
        basename = os.path.basename(file)
        if "TOC" not in basename and "blank" not in basename and "intro" not in basename:
            m = re.match(r'^([0-9]+\.[0-9]+)_(?:p[0-9]+_)?(.*\.html)$', basename)
            if m:
                prefix = m.group(1)
                suffix = m.group(2)
                # Ensure we don't go negative
                if footer_page < 1: footer_page = abs_page
                new_name = f"{prefix}_p{footer_page:03d}_{suffix}"
                new_path = os.path.join('pages', new_name)
                if file != new_path:
                    os.rename(file, new_path)
                    print(f"Renamed {basename} -> {new_name}")

print("Sync to footer complete.")
