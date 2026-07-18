import json
import re

ar_to_en = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
en_to_ar = str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")

# 1. Load lesson mapping
with open("lesson_mapping.json", encoding="utf-8") as f:
    unique_lessons = json.load(f)

# unique_lessons is a list of [new_num, title, first_file]
lesson_items = []
for num, title, filepath in unique_lessons:
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    # Find the header id
    m = re.search(r'<header[^>]+id=["\']([^"\']+)["\']', content)
    header_id = m.group(1) if m else ""

    ar_num = str(num).translate(en_to_ar)
    td1 = f'<td class="text-center font-bold text-grey">{ar_num}</td>'
    td2 = f'<td class="font-bold">{title}</td>'
    td3 = f'<td class="text-center font-bold text-primary"><a class="dynamic-page" href="#{header_id}"></a></td>'
    lesson_items.append([td1, td2, td3])

# 2. Extract answer lessons from 98.00_p120_Answers.html
with open("pages/98.00_p120_Answers.html", encoding="utf-8") as f:
    ans_content = f.read()

from bs4 import BeautifulSoup

ans_soup = BeautifulSoup(ans_content, "html.parser")
headers = ans_soup.find_all("div", class_="block-header accent")

answer_items = []
for header in headers:
    span = header.find("span")
    if not span:
        continue
    text = span.get_text(strip=True)
    if text.startswith("إِجَابَاتُ:"):
        lesson_title = text.replace("إِجَابَاتُ:", "").strip()
        ans_id = header.get("id", "")
        if not ans_id:
            continue

        # We find the lesson number from the title_to_num mapping
        title_to_num = {title.strip(): num for num, title, path in unique_lessons}
        num = title_to_num.get(lesson_title, 0)

        ar_num = str(num).translate(en_to_ar) if num > 0 else "-"

        td1 = '<td class="text-center font-bold text-grey bg-grey-lighter">ج</td>'
        td2 = f'<td class="font-bold bg-grey-lighter">إِجَابَاتُ {lesson_title}</td>'
        td3 = f'<td class="text-center font-bold text-primary bg-grey-lighter"><a class="dynamic-page" href="#{ans_id}"></a></td>'
        answer_items.append([td1, td2, td3])

# 3. Chunk and create TOC pages
all_items = lesson_items + answer_items
max_rows = 24
pages = []
for i in range(0, len(all_items), max_rows * 2):
    page_items = all_items[i : i + max_rows * 2]
    num_items = len(page_items)
    rows_needed = (num_items + 1) // 2
    col1 = page_items[:rows_needed]
    col2 = page_items[rows_needed:]
    while len(col2) < rows_needed:
        col2.append(None)
    pages.append(list(zip(col1, col2)))

toc_style = """
    .toc-table { width: 100%; border-collapse: collapse; margin-top: 2mm; }
    .toc-table td, .toc-table th { padding: 2mm 1mm; font-size: 8.5pt; border-bottom: 1px solid #e0e0e0; line-height: 1.2; }
    .toc-table th { background-color: #f5f5f5; font-weight: bold; color: #333; border-bottom: 2px solid #ccc; }
    .spacer-col { width: 2%; border-bottom: none !important; }
    .dynamic-page::after { content: target-counter(attr(href), page, arabic-indic); }
"""

# Remove old TOC pages
import glob
import os

for f in glob.glob("pages/00.*_TOC.html"):
    if f not in ["pages/00.0_Cover.html", "pages/00.1_Title.html"]:
        os.remove(f)

for page_idx, page_rows in enumerate(pages):
    html = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="utf-8"/>
    <title>فِهْرِسُ الْمَوْضُوعَاتِ</title>
    <link href="../styles/main.css" rel="stylesheet"/>
    <style>{toc_style}</style>
</head>
<body>
<div class="force-new-page">
<header class="page-header-strip" id="toc-header-{page_idx}">
<div class="header-section right">
<div class="lesson-number">٠٠</div>
<div class="lesson-details"><div>المستوى التأسيسي</div><div>فِهْرِسٌ</div></div>
</div>
<div class="header-section center"><h1 class="header-title">فِهْرِسُ الْمَوْضُوعَاتِ</h1></div>
<div class="header-section left"><div class="author-info">أ. حنا خفيف</div><div class="author-info"></div></div>
</header>
<table class="toc-table">
<thead><tr>
<th class="w-5pct text-center">الدَّرْسُ</th><th class="w-35pct">الْمَوْضُوعُ</th><th class="w-5pct text-center">ص</th><th class="spacer-col"></th>
<th class="w-5pct text-center">الدَّرْسُ</th><th class="w-35pct">الْمَوْضُوعُ</th><th class="w-5pct text-center">ص</th>
</tr></thead>
<tbody>
"""
    for col1, col2 in page_rows:
        html += "<tr>\n"
        html += "".join(col1)
        html += '<td class="spacer-col"></td>\n'
        if col2:
            html += "".join(col2)
        else:
            html += '<td class="text-center font-bold text-grey"></td><td class="font-bold"></td><td class="text-center font-bold text-primary"></td>'
        html += "\n</tr>\n"

    html += """</tbody></table></div></body></html>"""

    with open(f"pages/00.{2 + page_idx}_TOC.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated 00.{2 + page_idx}_TOC.html")
