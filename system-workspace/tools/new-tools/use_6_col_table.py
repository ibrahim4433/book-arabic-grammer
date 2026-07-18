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
        .toc-table {{ width: 100%; border-collapse: collapse; margin-top: 2mm; }}
        .toc-table td, .toc-table th {{ 
            padding: 2mm 1mm; 
            font-size: 8.5pt; 
            border-bottom: 1px solid #e0e0e0;
            line-height: 1.2;
        }}
        .toc-table th {{ 
            background-color: #f5f5f5; 
            font-weight: bold; 
            color: #333;
            border-bottom: 2px solid #ccc;
        }}
        .spacer-col {{ width: 2%; border-bottom: none !important; }}
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
        
        <table class="toc-table">
            <thead>
                <tr>
                    <th class="w-5pct text-center">الدَّرْسُ</th>
                    <th class="w-35pct">الْمَوْضُوعُ</th>
                    <th class="w-5pct text-center">ص</th>
                    <th class="spacer-col"></th>
                    <th class="w-5pct text-center">الدَّرْسُ</th>
                    <th class="w-35pct">الْمَوْضُوعُ</th>
                    <th class="w-5pct text-center">ص</th>
                </tr>
            </thead>
            <tbody>"""

    col_size = (len(chunk) + 1) // 2
    col1 = chunk[:col_size]
    col2 = chunk[col_size:]

    for row_idx in range(col_size):
        item1 = col1[row_idx]
        item2 = col2[row_idx] if row_idx < len(col2) else None

        bg1 = "bg-grey-lighter" if ("مُلْحَق" in item1["title"] or "حَلُّ" in item1["title"]) else ""
        bg2 = ""
        if item2:
            bg2 = "bg-grey-lighter" if ("مُلْحَق" in item2["title"] or "حَلُّ" in item2["title"]) else ""

        toc_html += f"""
                <tr>
                    <td class="text-center font-bold text-grey {bg1}">{item1["number"]}</td>
                    <td class="font-bold {bg1}">{item1["title"]}</td>
                    <td class="text-center font-bold text-primary {bg1}">{item1["arabic_page"]}</td>
                    
                    <td class="spacer-col"></td>
                    """
        if item2:
            toc_html += f"""
                    <td class="text-center font-bold text-grey {bg2}">{item2["number"]}</td>
                    <td class="font-bold {bg2}">{item2["title"]}</td>
                    <td class="text-center font-bold text-primary {bg2}">{item2["arabic_page"]}</td>
                </tr>"""
        else:
            toc_html += """
                    <td></td><td></td><td></td>
                </tr>"""

    toc_html += """
            </tbody>
        </table>
    </div>
</body>
</html>"""

    with open(f"pages/00.{page_num}_TOC.html", "w", encoding="utf-8") as f:
        f.write(toc_html)

print("TOC regenerated with 6 columns.")
