import glob
import os
import re
from pathlib import Path

pages_dir = Path("pages")
all_files = sorted(glob.glob("pages/*.html"))

# Remove any old blank
if os.path.exists("pages/00.0_blank_page1.html"):
    os.remove("pages/00.0_blank_page1.html")

for file in all_files:
    if "TEMPLATE_" in file or "00." in file or "98." in file:
        continue

    basename = os.path.basename(file)

    # regex to strip (تابع) and _تابع
    clean_name = re.sub(r"\(?\s*(تابع|تتمة|تَتِمَّةٌ|تَتِمَّة|تَابِع)\s*\)?", "", basename).strip()
    clean_name = re.sub(r"_+", "_", clean_name)
    clean_name = clean_name.replace("_.html", ".html")

    # But wait, the title inside the file has "(الْجُزْءُ الثَّانِي)".
    # Should the filename have it too?
    # Yes! Let's extract the exact title from the <h1> tag.

    from bs4 import BeautifulSoup

    with open(file, encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    lt_h1 = soup.find("h1", class_="header-title")
    title = lt_h1.get_text(strip=True) if lt_h1 else None

    if title:
        # Construct the new filename: XX.X_pYY_TITLE.html
        # Extract XX.X_pYY from basename
        match = re.match(r"([0-9]+\.[0-9]+)_p([0-9]+)_", basename)
        if match:
            prefix = match.group(0)
            new_basename = f"{prefix}{title}.html"
            if new_basename != basename:
                os.rename(file, os.path.join("pages", new_basename))

# Re-generate the TOC because we might have changed the file names and the TOC needs the exact titles/numbers.
# Actually, the TOC in 00.2 and 00.3 is already generated with the cleaned titles (because the script updated them in memory).
# But let's verify if TOC has correct Arabic numerals for Page numbers!
# In the previous script I used `to_arabic_indic(current_page)`!
