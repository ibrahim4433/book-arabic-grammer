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
]

pages_dir = Path("pages")

# 1. Gather all lesson files except 00.* and 98.*
all_files = sorted(glob.glob("pages/*.html"))
lesson_files = [
    f
    for f in all_files
    if "TEMPLATE_" not in f
    and not os.path.basename(f).startswith("00.")
    and not os.path.basename(f).startswith("98.")
]

# Analyze titles to group duplicates
groups = {}
file_info = []

for file in lesson_files:
    basename = os.path.basename(file)
    with open(file, encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    lt_h1 = soup.find("h1", class_="header-title")
    title = lt_h1.get_text(strip=True) if lt_h1 else ""

    # Clean up (تابع), (تتمة), etc.
    # regex to remove (تابع) or (تتمة) or تابع or تتمة at the end
    clean_title = re.sub(r"\(?\s*(تابع|تتمة|تَتِمَّةٌ|تَتِمَّة|تَابِع)\s*\)?", "", title).strip()
    clean_title = re.sub(r"\s+", " ", clean_title)  # normalize spaces

    if clean_title not in groups:
        groups[clean_title] = []
    groups[clean_title].append(file)

    file_info.append({"file": file, "clean_title": clean_title, "soup": soup, "basename": basename})

# Assign new titles
new_titles = {}  # file -> new_title
for title, files_in_group in groups.items():
    if len(files_in_group) == 1:
        new_titles[files_in_group[0]] = title
    else:
        for idx, f in enumerate(files_in_group):
            part_name = arabic_parts[idx] if idx < len(arabic_parts) else str(idx + 1)
            new_titles[f] = f"{title} (الْجُزْءُ {part_name})"

# Update the HTML files with new titles
print("Updating lesson titles in HTML files...")
for info in file_info:
    f = info["file"]
    new_title = new_titles[f]
    soup = info["soup"]

    lt_h1 = soup.find("h1", class_="header-title")
    if lt_h1 and lt_h1.get_text(strip=True) != new_title:
        lt_h1.string = new_title
        with open(f, "w", encoding="utf-8") as out:
            out.write(str(soup))

print("Updating answers HTML files with new titles...")
answer_files = sorted(glob.glob("pages/98.*.html"))
for f in answer_files:
    with open(f, encoding="utf-8") as ans_f:
        content = ans_f.read()

    # We need to replace the old titles with new titles.
    # Since we don't know exactly what was written, we can use regex to find
    # إِجَابَاتُ: {old_title} (الدَّرْسُ {number})
    # Wait, the titles in the answers might have had (تتمة) etc.
    # Let's iterate over ALL new_titles, but we need the old title that was in the answer file.
    pass

# A better way to update answer files:
# Since we know the lesson numbers (from the header span), we can map lesson_number -> new_title
lesson_num_to_title = {}
for info in file_info:
    ln_div = info["soup"].find("div", class_="lesson-number")
    if ln_div:
        ln = ln_div.get_text(strip=True)
        lesson_num_to_title[to_arabic_indic(ln)] = new_titles[info["file"]]
        lesson_num_to_title[ln] = new_titles[info["file"]]

for f in answer_files:
    with open(f, encoding="utf-8") as ans_f:
        content = ans_f.read()

    soup = BeautifulSoup(content, "html.parser")
    changed = False
    for section in soup.find_all("section", class_="content-block"):
        header_span = section.find("div", class_="block-header").find("span")
        if header_span:
            text = header_span.get_text(strip=True)
            # format is إِجَابَاتُ: TITLE (الدَّرْسُ NUMBER)
            match = re.search(r"إِجَابَاتُ: (.*?) \(الدَّرْسُ (.*?)\)", text)
            if match:
                old_title = match.group(1)
                num = match.group(2)

                # normalize num (might be arabic-indic or ascii)
                if num in lesson_num_to_title:
                    correct_title = lesson_num_to_title[num]
                    new_text = f"إِجَابَاتُ: {correct_title} (الدَّرْسُ {num})"
                    if text != new_text:
                        header_span.string = new_text
                        changed = True

    if changed:
        with open(f, "w", encoding="utf-8") as out:
            out.write(str(soup))

# Now create blank page
blank_html = """<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head><meta charset="utf-8"><title>Blank Page</title><link href="../styles/main.css" rel="stylesheet"></head>
<body><div class="force-new-page" style="display:flex; align-items:center; justify-content:center; height:100%;">
</div></body></html>"""
with open("pages/00.0_blank.html", "w", encoding="utf-8") as out:
    out.write(blank_html)

# Calculate correct page numbers
# Order:
# Page 1: Cover (handled by build.py)
# Page 2: 00.0_blank.html
# Page 3: 00.1_intro.html
# Page 4: 00.2_TOC.html
# Page 5: 00.3_TOC.html
# Then lesson files
# Then answer files

all_files = sorted(glob.glob("pages/*.html"))
current_page = 2  # since blank is first html file, it gets page 2. Cover is 1.

toc_entries = []

for file in all_files:
    if "TEMPLATE_" in file or "TOC" in file:
        continue  # TOC doesn't go in TOC

    basename = os.path.basename(file)

    if basename == "00.0_blank.html" or basename == "00.1_intro.html":
        current_page += 1
        continue

    with open(file, encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    lesson_number = None
    ln_div = soup.find("div", class_="lesson-number")
    if ln_div:
        lesson_number = ln_div.get_text(strip=True)

    lesson_title = None
    lt_h1 = soup.find("h1", class_="header-title")
    if lt_h1:
        lesson_title = lt_h1.get_text(strip=True)

    # fallback
    if not lesson_title:
        lesson_title = basename

    if basename.startswith("98."):
        if not lesson_title.startswith("حَلُّ تَدْرِيبَاتِ الْكِتَابِ"):
            lesson_title = "مُلْحَقُ الْإِجَابَاتِ - " + lesson_title

    toc_entries.append(
        {
            "title": lesson_title,
            "number": to_arabic_indic(lesson_number) if lesson_number else "-",
            "page": current_page,
            "arabic_page": to_arabic_indic(current_page),
            "file": file,
            "basename": basename,
        }
    )

    # We rename the file replacing nXX with pXX
    # example: 02.0_nXX_أَقْسَامُ الْكَلَاَمِ (تابع).html
    # wait, the file name might already be changed? Let's check regex.
    new_basename = re.sub(r"_n[0-9X]+_", f"_p{current_page:02d}_", basename)
    if new_basename == basename:
        # if it didn't have _nXX_, try _pXX_ in case we already renamed it
        new_basename = re.sub(r"_p[0-9]+_", f"_p{current_page:02d}_", basename)

    if new_basename != basename:
        new_file = os.path.join(pages_dir, new_basename)
        os.rename(file, new_file)
        # update file path in our list
        toc_entries[-1]["file"] = new_file

    current_page += 1

# Generate exactly 2 TOC pages
# 00.2_TOC.html and 00.3_TOC.html
# They will be pages 4 and 5.
# Total items: len(toc_entries). Approx 100.
# So 50 items per TOC page.
# To fit 50 items, we can use 2 columns! Or just dense-table with very small margins.
# Let's use two columns in a single table, or two side-by-side tables.
# Using 2 columns:
# <tr> <td>1</td> <td>Title</td> <td>10</td>  <td>2</td> <td>Title2</td> <td>11</td> </tr>

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
        .toc-table td, .toc-table th {{ padding: 2px 4px; font-size: 10pt; }}
        .toc-table {{ width: 48%; float: right; margin-left: 2%; }}
        .toc-table.left-col {{ margin-left: 0; }}
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
        
        <div style="display: flex; justify-content: space-between;">
"""
    # split chunk into 2 columns for this page
    col_size = (len(chunk) + 1) // 2
    col1 = chunk[:col_size]
    col2 = chunk[col_size:]

    for c_idx, col_data in enumerate([col1, col2]):
        extra_class = "left-col" if c_idx == 1 else ""
        toc_html += f"""
            <table class="dense-table toc-table {extra_class}">
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
                        <td style="text-align: center; font-weight: bold;">{page}</td>
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

# Remove any extra TOC pages if they exist
for f in glob.glob("pages/00.*_TOC.html"):
    if f not in ["pages/00.2_TOC.html", "pages/00.3_TOC.html"]:
        os.remove(f)
