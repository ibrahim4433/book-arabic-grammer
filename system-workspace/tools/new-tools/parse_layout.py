import glob
import os
import re

from weasyprint import HTML


def get_full_html():
    output_dir = "output/export"
    all_files = sorted(glob.glob("pages/*.html"))
    pages_files = [f for f in all_files if "TEMPLATE_" not in f]

    master_html_start = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="styles/main.css">
    <style>
        @page cover { margin: 0; size: A4; @bottom-center { content: none; } }
        .cover-page-wrapper { page: cover; width: 210mm; height: 297mm; overflow: hidden; break-after: page; position: relative; z-index: 20000; background: white; }
        .cover-page-wrapper img { width: 100%; height: 100%; object-fit: cover; }
    </style>
</head>
<body>
    <div class="global-background-layer"></div>
    <div class="global-watermark-layer"><span class="watermark-text">أ. حنا خفيف</span></div>
"""
    master_html_end = "</body></html>"

    accumulated_body_content = ""
    if os.path.exists("pages/cover/front-cover.jpg"):
        accumulated_body_content += '<div class="cover-page-wrapper"><img src="pages/cover/front-cover.jpg" alt="Front Cover"></div>'

    for page_file in pages_files:
        try:
            with open(page_file, encoding="utf-8") as f:
                content = f.read()
            body_match = re.search(r"<body[^>]*>(.*?)</body>", content, re.DOTALL | re.IGNORECASE)
            if body_match:
                accumulated_body_content += body_match.group(1) + "\n"
        except:
            pass

    if os.path.exists("pages/cover/back-cover.jpg"):
        accumulated_body_content += '<div class="cover-page-wrapper" style="break-after: auto;"><img src="pages/cover/back-cover.jpg" alt="Back Cover"></div>'

    return master_html_start + accumulated_body_content + master_html_end


html_str = get_full_html()
doc = HTML(string=html_str, base_url=".").render()

print(f"Total PDF pages: {len(doc.pages)}")


# We want to find the pages that contain "إجابات الدرس" headers.
# We will recursively walk the layout boxes.
def walk_boxes(box, page_number, results):
    # Check if this box is a heading for the answer section
    # The answer headers are <h3> with text like "إجابات الدرس..."
    if hasattr(box, "element_tag") and box.element_tag == "h3":
        text = ""
        # The text is in the children
        if hasattr(box, "text"):
            text += box.text
        # Sometimes text is in inline children
        if hasattr(box, "children"):
            for child in box.children:
                if hasattr(child, "text"):
                    text += child.text
        if "إِجَابَاتُ الدَّرْسِ" in text or "إجابات الدرس" in text:
            m = re.search(r"الدَّرْسِ?\s*([٠-٩0-9]+)", text)
            if m:
                results.append((page_number, text.strip()))

    if hasattr(box, "children"):
        for child in box.children:
            walk_boxes(child, page_number, results)


answers = []
for i, page in enumerate(doc.pages):
    walk_boxes(page._page_box, i + 1, answers)

for page_num, text in answers:
    print(f"Page {page_num}: {text}")

import json

with open("answers_pagination.json", "w", encoding="utf-8") as f:
    json.dump(answers, f, ensure_ascii=False, indent=2)
