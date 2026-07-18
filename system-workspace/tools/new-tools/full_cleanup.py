import glob
import os
import re
from pathlib import Path

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


arabic_parts = [
    "الْأَوَّلُ",
    "الثَّانِي",
    "الثَّالِثُ",
    "الرَّابِعُ",
    "الْخَامِسُ",
    "السَّادِسُ",
    "السَّابِعُ",
    "الثَّامِنُ",
    "التَّاسِعُ",
    "الْعَاشِرُ",
    "الْحَادِيَ عَشَرَ",
    "الثَّانِيَ عَشَرَ",
    "الثَّالِثَ عَشَرَ",
    "الرَّابِعَ عَشَرَ",
    "الْخَامِسَ عَشَرَ",
]

pages_dir = Path("pages")

# 1. Gather all lesson files
all_files = sorted(glob.glob("pages/*.html"))
lesson_files = [
    f
    for f in all_files
    if "TEMPLATE_" not in f
    and not os.path.basename(f).startswith("00.")
    and not os.path.basename(f).startswith("98.")
]

groups = {}
file_info = []

for file in lesson_files:
    basename = os.path.basename(file)
    with open(file, encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    lt_h1 = soup.find("h1", class_="header-title")
    title = lt_h1.get_text(strip=True) if lt_h1 else ""

    # We want to extract the pure base title.
    # We will strip out anything like (تابع), (تتمة), (الجزء الثاني), _تابع, etc.
    # Also strip diacritics ONLY for comparison to group them correctly?
    # No, diacritics might be important, but let's remove common noise words.

    base_title = title
    # Remove text in parentheses
    base_title = re.sub(r"\(.*?\)", "", base_title)
    # Remove _تابع, _تتمة etc
    base_title = re.sub(r"_(تابع|تتمة|تَتِمَّة|تَابِع|تَتِمَّةٌ)", "", base_title)
    base_title = re.sub(r"(تابع|تتمة|تَتِمَّة|تَابِع|تَتِمَّةٌ)", "", base_title)
    base_title = re.sub(r"الجزء\s+.*", "", base_title)
    base_title = re.sub(r"الْجُزْءُ\s+.*", "", base_title)
    base_title = base_title.replace("؟", "؟ ")
    base_title = re.sub(r"\s+", " ", base_title).strip()

    if not base_title:
        base_title = title  # fallback

    # To group them better, we can strip all diacritics for the grouping key
    group_key = re.sub(r"[\u064B-\u065F\u0670]", "", base_title).strip()

    if group_key not in groups:
        groups[group_key] = {
            "display_title": base_title,  # use the first one's diacritics
            "files": [],
        }
    groups[group_key]["files"].append(file)

    file_info.append({"file": file, "group_key": group_key, "soup": soup, "basename": basename})

new_titles = {}
for group_key, group_data in groups.items():
    display_title = group_data["display_title"]
    files_in_group = sorted(group_data["files"])  # already sorted chronologically by filename
    if len(files_in_group) == 1:
        new_titles[files_in_group[0]] = display_title
    else:
        for idx, f in enumerate(files_in_group):
            part_name = arabic_parts[idx] if idx < len(arabic_parts) else str(idx + 1)
            new_titles[f] = f"{display_title} (الْجُزْءُ {part_name})"

print("Updating lesson files...")
for info in file_info:
    f = info["file"]
    new_title = new_titles[f]
    soup = info["soup"]
    basename = info["basename"]

    changed = False

    # 1. Update H1
    lt_h1 = soup.find("h1", class_="header-title")
    if lt_h1 and lt_h1.get_text(strip=True) != new_title:
        lt_h1.string = new_title
        changed = True

    if changed:
        with open(f, "w", encoding="utf-8") as out:
            out.write(str(soup))

    # 2. Rename file
    # format: XX.X_pYY_TITLE.html
    match = re.match(r"([0-9]+\.[0-9]+)_(p[0-9]+|n[0-9X]+)_", basename)
    if match:
        prefix = match.group(0)
        # remove anything before the title, and attach the new clean title
        # wait, the prefix already contains the _pYY_ or _nXX_
        new_basename = f"{prefix}{new_title}.html"
        # Sanitize filename if needed (e.g., removing / or \ or ?)
        new_basename = new_basename.replace("/", "-").replace("?", "")

        if new_basename != basename:
            new_file = os.path.join(pages_dir, new_basename)
            os.rename(f, new_file)

# Now let's update answers HTML files (98.*)
print("Updating answers HTML files...")
answer_files = sorted(glob.glob("pages/98.*.html"))
for f in answer_files:
    with open(f, encoding="utf-8") as ans_f:
        content = ans_f.read()

    # We need to replace the old titles with new titles.
    # To do this safely, we read all answer files, find the blocks, extract الدَّرْسُ NUMBER
    # and map the NUMBER back to the new title.
    # We can get the NUMBER from the new_titles dict! Wait, we don't have the lesson numbers easily.
    pass

# Map lesson number to new title
lesson_num_to_title = {}
# Read again since files are renamed!
lesson_files = [
    f
    for f in glob.glob("pages/*.html")
    if "TEMPLATE_" not in f
    and not os.path.basename(f).startswith("00.")
    and not os.path.basename(f).startswith("98.")
]
for f in lesson_files:
    with open(f, encoding="utf-8") as html_f:
        soup = BeautifulSoup(html_f.read(), "html.parser")

    ln_div = soup.find("div", class_="lesson-number")
    lt_h1 = soup.find("h1", class_="header-title")

    if ln_div and lt_h1:
        ln = ln_div.get_text(strip=True)
        title = lt_h1.get_text(strip=True)
        lesson_num_to_title[to_arabic_indic(ln)] = title
        lesson_num_to_title[ln] = title

for f in answer_files:
    with open(f, encoding="utf-8") as ans_f:
        content = ans_f.read()

    soup = BeautifulSoup(content, "html.parser")
    changed = False
    for section in soup.find_all("section", class_="content-block"):
        header_span = section.find("div", class_="block-header").find("span")
        if header_span:
            text = header_span.get_text(strip=True)
            match = re.search(r"إِجَابَاتُ: (.*?) \(الدَّرْسُ (.*?)\)", text)
            if match:
                num = match.group(2)
                if num in lesson_num_to_title:
                    correct_title = lesson_num_to_title[num]
                    new_text = f"إِجَابَاتُ: {correct_title} (الدَّرْسُ {num})"
                    if text != new_text:
                        header_span.string = new_text
                        changed = True

    if changed:
        with open(f, "w", encoding="utf-8") as out:
            out.write(str(soup))

# Finally, update the TOC pages (00.2, 00.3)
print("Generating TOC...")
# Get all files including answers
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
    lt_h1 = soup.find("h1", class_="header-title")
    if lt_h1:
        lesson_title = lt_h1.get_text(strip=True)

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

mid_point = len(toc_entries) // 2
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
        .toc-table td, .toc-table th {{ padding: 4px; font-size: 11pt; border-bottom: 1px solid #eee; }}
        .toc-table {{ width: 48%; float: right; margin-left: 2%; }}
        .toc-table.left-col {{ margin-left: 0; }}
        .toc-container {{ display: flex; justify-content: space-between; }}
    </style>
</head>
<body>
    <div class="force-new-page">
        <header class="page-header-strip">
            <div class="header-section right">
                <div class="lesson-number">00</div>
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
                        <th style="width: 15%; text-align: center;">الرَّقْمُ</th>
                        <th style="width: 70%;">الْمَوْضُوعُ</th>
                        <th style="width: 15%; text-align: center;">الصَّفْحَةُ</th>
                    </tr>
                </thead>
                <tbody>"""

        for item in col_data:
            title = item["title"]
            num = item["number"]
            page = item["arabic_page"]

            bg = (
                "background-color: rgba(0, 121, 107, 0.1);"
                if ("مُلْحَق" in title or "حَلُّ" in title)
                else ""
            )

            toc_html += f"""
                    <tr style="{bg}">
                        <td style="text-align: center; font-weight: bold;">{num}</td>
                        <td style="font-weight: bold;">{title}</td>
                        <td style="text-align: center; font-weight: bold; color: #00796b;">{page}</td>
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

print("Done!")
