import glob
import os
import re

from weasyprint import HTML


def to_arabic_indic(text):
    if text is None:
        return "-"
    english_to_arabic = {
        "0": "٠",
        "1": "١",
        "2": "٢",
        "3": "٣",
        "4": "٤",
        "5": "٥",
        "6": "٦",
        "7": "٧",
        "8": "٨",
        "9": "٩",
    }
    return "".join(english_to_arabic.get(c, c) for c in str(text))


# 1. Fetch files
all_files = sorted(glob.glob("pages/*.html"))
pages_files = [f for f in all_files if "TEMPLATE_" not in f]

master_html_start = """<!DOCTYPE html><html lang="ar" dir="rtl"><head><meta charset="UTF-8"><link rel="stylesheet" href="styles/main.css">
<style>
    @page cover { margin: 0; size: A4; @bottom-center { content: none; } }
    .cover-page-wrapper { page: cover; width: 210mm; height: 297mm; overflow: hidden; break-after: page; position: relative; z-index: 20000; background: white; }
    .cover-page-wrapper img { width: 100%; height: 100%; object-fit: cover; }
</style></head><body>"""

# Optional covers (same logic as build.py)
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

    # Inject anchor div
    anchor_id = f"source_file_{i}"
    file_ids.append((i, page_file, anchor_id))

    # Prefix fragment with anchor
    accumulated_body_content += f'<div id="{anchor_id}"></div>\n' + fragment + "\n"

full_html = master_html_start + accumulated_body_content + "</body></html>"

print("Rendering full document in memory to find exact physical pages...")
doc = HTML(string=full_html, base_url=".").render()

# 2. Extract anchors
anchor_to_page = {}
for page_idx, page in enumerate(doc.pages):
    for anchor_name in page.bookmarks:  # wait, bookmarks might be different
        pass
    # Actually anchors are in page.anchors (a dictionary mapping anchor names to (x,y) positions)
    # wait, page.anchors is available in some WeasyPrint versions.
    # Alternatively:
    if hasattr(page, "anchors"):
        for anchor_name in page.anchors.keys():
            if anchor_name not in anchor_to_page:
                anchor_to_page[anchor_name] = page_idx + 1

# If anchor_name is not in page.anchors, we can do it via bookmarks:
# Wait, let's just make them h6: <h6 id="{anchor_id}" style="display:none;"></h6>
# No, display:none removes it from layout so no anchor!
# Using <div id=".."> is standard.

print(f"Total pages rendered: {len(doc.pages)}")

# Rename files based on their actual physical page
file_to_page = {}
for i, file, anchor_id in file_ids:
    page_num = anchor_to_page.get(anchor_id)
    if not page_num:
        # Fallback if WeasyPrint doesn't populate page.anchors
        print(f"WARNING: Anchor {anchor_id} not found. Fallback to logic.")
        page_num = 0
    file_to_page[file] = page_num

    basename = os.path.basename(file)
    if "TOC" not in basename and "blank" not in basename and "intro" not in basename:
        m = re.match(r"^([0-9]+\.[0-9]+)_(?:p[0-9]+_)?(.*\.html)$", basename)
        if m and page_num > 0:
            prefix = m.group(1)
            suffix = m.group(2)
            new_name = f"{prefix}_p{page_num:03d}_{suffix}"
            new_path = os.path.join("pages", new_name)
            if file != new_path:
                os.rename(file, new_path)
                print(f"Renamed {basename} -> {new_name}")

print("Sync complete.")
