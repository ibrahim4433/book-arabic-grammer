from weasyprint import HTML

print("Rendering...")
doc = HTML(filename="output/export/book.pdf")
# Wait, WeasyPrint cannot read PDF, only HTML.

html = HTML(
    string="""<!DOCTYPE html><html lang="ar" dir="rtl"><head><link rel="stylesheet" href="styles/main.css"></head><body><h1>Hello</h1></body></html>""",
    base_url=".",
)

# Let's write a script that parses the HTML like build.py does, and prints the number of pages.
import glob
import os
import re

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

all_files = sorted(glob.glob("pages/*.html"))
pages_files = [f for f in all_files if "TEMPLATE_" not in f]

accumulated_body_content = ""
for i, page_file in enumerate(pages_files):
    with open(page_file, encoding="utf-8") as f:
        content = f.read()
    body_match = re.search(r"<body[^>]*>(.*?)</body>", content, re.DOTALL | re.IGNORECASE)
    fragment = body_match.group(1) if body_match else content
    accumulated_body_content += fragment + "\n"

full_html = master_html_start + accumulated_body_content + "</body></html>"
doc = HTML(string=full_html, base_url=".").render()
print(f"TOTAL PHYSICAL PAGES IN FINAL RENDER: {len(doc.pages)}")
