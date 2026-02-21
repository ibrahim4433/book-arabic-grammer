import os
import json
import re
from bs4 import BeautifulSoup

PAGES_DIR = "pages/"
TOC_FILE = "system-workspace/TOC.json"

ARABIC_NUMERALS = {
    '0': '٠', '1': '١', '2': '٢', '3': '٣', '4': '٤',
    '5': '٥', '6': '٦', '7': '٧', '8': '٨', '9': '٩'
}

def to_arabic_num(n):
    return "".join(ARABIC_NUMERALS.get(d, d) for d in str(int(n)))

def fix_header(filepath, toc_data):
    # Determine lesson number and part from filename
    filename = os.path.basename(filepath)
    # Pattern: XX.Y_...
    match = re.match(r"(\d+)\.(\d+)", filename)
    if not match:
        print(f"Skipping {filepath}: Filename pattern mismatch.")
        return

    lesson_key = str(int(match.group(1))) # "09" -> "9"
    part_num = int(match.group(2))

    metadata = toc_data.get(lesson_key)
    if not metadata:
        print(f"Skipping {filepath}: No metadata found for lesson {lesson_key}")
        return

    # Retrieve Metadata
    title = metadata.get("title", "Unknown Lesson")
    level = metadata.get("level", "Unknown Level")
    author = metadata.get("author", "Unknown Author")
    author_num = metadata.get("author_number", "")

    # Suffix for continued parts
    # e.g., Lesson 9 Part 1 (File 09.1) -> " (تابع)"
    # Lesson 9 Part 0 (File 09.0) -> ""
    title_suffix = " (تابع)" if part_num > 0 else ""
    full_title = f"{title}{title_suffix}"

    lesson_ar = to_arabic_num(lesson_key)

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")
    header = soup.find("header", class_="page-header-strip")

    if not header:
        print(f"Skipping {filepath}: No header found.")
        return

    # Create new inner HTML structure
    new_inner_html = f"""
<div class="header-section right">
<div class="lesson-number">{lesson_ar}</div>
<div class="lesson-details">
<div>المستوى اللغوي</div>
<div>{level}</div>
</div>
</div>
<div class="header-section center">
<h1 class="header-title">{full_title}</h1>
</div>
<div class="header-section left">
<div class="author-info">{author}</div>
<div class="author-info">{author_num}</div>
</div>
"""

    # Parse the new inner HTML
    new_soup = BeautifulSoup(new_inner_html, "html.parser")

    # Clear old header content
    header.clear()

    # Append new content, handling potential parser wrapping
    if new_soup.body:
        for child in list(new_soup.body.contents):
            header.append(child)
    else:
        for child in list(new_soup.contents):
            header.append(child)

    # Save
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print(f"Updated header for {filepath}")

def main():
    if not os.path.exists(TOC_FILE):
        print("TOC.json not found.")
        return

    with open(TOC_FILE, "r", encoding="utf-8") as f:
        toc_data = json.load(f)

    files = sorted([f for f in os.listdir(PAGES_DIR) if f.endswith(".html")])

    for filename in files:
        filepath = os.path.join(PAGES_DIR, filename)
        try:
            fix_header(filepath, toc_data)
        except Exception as e:
            print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    main()
