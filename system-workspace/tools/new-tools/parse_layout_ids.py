import glob
import json
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
    for page_file in pages_files:
        try:
            with open(page_file, encoding="utf-8") as f:
                content = f.read()
            body_match = re.search(r"<body[^>]*>(.*?)</body>", content, re.DOTALL | re.IGNORECASE)
            if body_match:
                accumulated_body_content += body_match.group(1) + "\n"
        except:
            pass

    return master_html_start + accumulated_body_content + master_html_end


html_str = get_full_html()
doc = HTML(string=html_str, base_url=".").render()


def walk_boxes(box, page_number, results):
    if hasattr(box, "element_tag") and box.element_tag == "div":
        node = getattr(box, "node", None)
        if node is not None:
            node_id = node.get("id", "")
            if node_id.startswith("ans-lesson-"):
                results.append((page_number, node_id))

    if hasattr(box, "children"):
        for child in box.children:
            walk_boxes(child, page_number, results)


answers = []
for i, page in enumerate(doc.pages):
    walk_boxes(page._page_box, i + 1, answers)

for page_num, ans_id in answers:
    print(f"Page {page_num}: {ans_id}")

with open("answers_pagination.json", "w", encoding="utf-8") as f:
    json.dump(answers, f, ensure_ascii=False, indent=2)
