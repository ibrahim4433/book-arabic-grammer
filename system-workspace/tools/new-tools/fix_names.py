import glob
import os
import re

from weasyprint import HTML

all_files = sorted(glob.glob("pages/*.html"))
pages_files = [f for f in all_files if "TEMPLATE_" not in f]

master_html_start = """<!DOCTYPE html><html lang="ar" dir="rtl"><head><meta charset="UTF-8"><link rel="stylesheet" href="styles/main.css">
<style>
    @page cover { margin: 0; size: A4; @bottom-center { content: none; } }
    .cover-page-wrapper { page: cover; width: 210mm; height: 297mm; overflow: hidden; break-after: page; position: relative; z-index: 20000; background: white; }
    .cover-page-wrapper img { width: 100%; height: 100%; object-fit: cover; }
</style></head><body>"""

has_front_cover = os.path.exists("pages/cover/front-cover.jpg")
if has_front_cover:
    master_html_start += (
        '<div class="cover-page-wrapper"><img src="pages/cover/front-cover.jpg"></div>\n'
    )

accumulated_body_content = ""
file_ids = []
for i, page_file in enumerate(pages_files):
    with open(page_file, encoding="utf-8") as f:
        content = f.read()
    body_match = re.search(r"<body[^>]*>(.*?)</body>", content, re.DOTALL | re.IGNORECASE)
    fragment = body_match.group(1) if body_match else content

    anchor_id = f"source_file_{i}"
    file_ids.append((i, page_file, anchor_id))

    # Inject anchor INSIDE the first element to ensure it stays on the same page
    # Find the first > and insert the anchor right after it
    fragment = re.sub(r"(<[^>]+>)", r"\1" + f'<a id="{anchor_id}"></a>', fragment, count=1)

    accumulated_body_content += fragment + "\n"

full_html = master_html_start + accumulated_body_content + "</body></html>"
doc = HTML(string=full_html, base_url=".").render()

anchor_to_page = {}
if hasattr(doc.pages[0], "anchors"):
    for page_idx, page in enumerate(doc.pages):
        for anchor_name in page.anchors.keys():
            if anchor_name not in anchor_to_page:
                anchor_to_page[anchor_name] = page_idx + 1

for i, file, anchor_id in file_ids:
    abs_page = anchor_to_page.get(anchor_id, 0)
    if abs_page > 0:
        basename = os.path.basename(file)
        if "TOC" not in basename and "blank" not in basename and "intro" not in basename:
            m = re.match(r"^([0-9]+\.[0-9]+)_(?:p[0-9]+_)?(.*\.html)$", basename)
            if m:
                prefix = m.group(1)
                suffix = m.group(2)
                new_name = f"{prefix}_p{abs_page:03d}_{suffix}"
                new_path = os.path.join("pages", new_name)
                if file != new_path:
                    os.rename(file, new_path)
                    print(f"Renamed {basename} -> {new_name}")

print("Fix complete.")
