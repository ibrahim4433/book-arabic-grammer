import glob
import os

from bs4 import BeautifulSoup


def to_arabic_indic(text):
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


all_files = sorted(glob.glob("pages/*.html"))
toc_entries = []
current_page = 2

for f in all_files:
    if "TEMPLATE_" in f or "TOC" in f:
        continue

    basename = os.path.basename(f)
    if basename == "00.0_blank.html" or basename == "00.1_intro.html":
        current_page += 1
        continue

    with open(f, encoding="utf-8") as html_f:
        soup = BeautifulSoup(html_f.read(), "html.parser")

    lesson_number = None
    ln_div = soup.find("div", class_="lesson-number")
    if ln_div:
        lesson_number = ln_div.get_text(strip=True)

    lesson_title = None
    title_tag = soup.find("title")
    if title_tag:
        lesson_title = title_tag.get_text(strip=True)

    if basename.startswith("98."):
        if not lesson_title.startswith("حَلُّ تَدْرِيبَاتِ الْكِتَابِ"):
            lesson_title = "مُلْحَقُ الْإِجَابَاتِ - " + lesson_title

    toc_entries.append(
        {
            "title": lesson_title,
            "number": to_arabic_indic(lesson_number) if lesson_number else "-",
            "arabic_page": to_arabic_indic(current_page),
        }
    )

    current_page += 1

mid_point = (len(toc_entries) + 1) // 2
chunks = [toc_entries[:mid_point], toc_entries[mid_point:]]

for idx, chunk in enumerate(chunks):
    page_num = idx + 2

    toc_html = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="utf-8">
    <title>فِهْرِسُ الْمَوْضُوعَاتِ</title>
    <link href="../styles/main.css" rel="stylesheet">
    <style>
        .toc-table {{ width: 48%; float: right; margin-left: 2%; border-collapse: collapse; margin-top: 0; }}
        .toc-table.left-col {{ margin-left: 0; }}
        .toc-table td, .toc-table th {{ 
            padding: 1px 3px; 
            font-size: 8.5pt; 
            border-bottom: 1px solid #e0e0e0;
            line-height: 1.1;
        }}
        .toc-table th {{ 
            background-color: #f5f5f5; 
            font-weight: bold; 
            color: #333;
            border-bottom: 2px solid #ccc;
        }}
        .toc-container {{ 
            display: flex; 
            justify-content: space-between; 
            align-items: flex-start;
            margin-top: 1mm; 
        }}
    </style>
</head>
<body>
    <div class="force-new-page">
        <header class="page-header-strip">
            <div class="header-section right">
                <div class="lesson-number">٠٠</div>
                <div class="lesson-details">
                    <div>المستوى التأسيسي</div>
                    <div>فِهْرِسٌ</div>
                </div>
            </div>
            <div class="header-section center">
                <h1 class="header-title">فِهْرِسُ الْمَوْضُوعَاتِ (الْجُزْءُ {to_arabic_indic(idx + 1)})</h1>
            </div>
            <div class="header-section left">
                <div class="author-info">أ. حنا خفيف</div>
                <div class="author-info"> </div>
            </div>
        </header>
        
        <div class="toc-container">
"""
    col_size = (len(chunk) + 1) // 2
    col1 = chunk[:col_size]
    col2 = chunk[col_size:]

    for c_idx, col_data in enumerate([col1, col2]):
        extra_class = "left-col" if c_idx == 1 else ""
        toc_html += f"""
            <table class="toc-table {extra_class}">
                <thead>
                    <tr>
                        <th class="w-10pct text-center">الدَّرْسُ</th>
                        <th class="w-75pct">الْمَوْضُوعُ</th>
                        <th class="w-15pct text-center">الصَّفْحَةُ</th>
                    </tr>
                </thead>
                <tbody>"""

        for item in col_data:
            title = item["title"]
            num = item["number"]
            page = item["arabic_page"]

            row_class = "bg-grey-lighter" if ("مُلْحَق" in title or "حَلُّ" in title) else ""

            toc_html += f"""
                    <tr class="{row_class}">
                        <td class="text-center font-bold text-grey">{num}</td>
                        <td class="font-bold">{title}</td>
                        <td class="text-center font-bold text-primary">{page}</td>
                    </tr>"""

        toc_html += """
                </tbody>
            </table>"""

    toc_html += """
        </div>
    </div>
</body>
</html>"""

    with open(f"pages/00.{page_num}_TOC.html", "w", encoding="utf-8") as f:
        f.write(toc_html)

print("TOC generated cleanly.")
