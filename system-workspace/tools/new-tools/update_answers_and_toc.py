import glob
import re

from bs4 import BeautifulSoup

ar_to_en = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
en_to_ar = str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")

# Create a mapping from old lesson number (extracted from original header or filename) to new lesson number
# Wait, let's just parse the old files again. Since we OVERWROTE the lesson-number div, we can use the filename `XX.x`!
old_to_new = {}

files = sorted([f for f in glob.glob("pages/*.html") if re.match(r"pages/\d{2}\.", f)])
lesson_files = [
    f
    for f in files
    if not f.startswith("pages/00.")
    and not f.startswith("pages/98.")
    and not f.startswith("pages/99.")
]

for f in lesson_files:
    # Filename like pages/05.0_p006_....html
    m = re.match(r"pages/(\d{2})\.", f)
    if not m:
        continue
    old_num = int(m.group(1))

    # Read the NEW lesson number we just wrote
    soup = BeautifulSoup(open(f, encoding="utf-8").read(), "html.parser")
    num_div = soup.find("div", class_="lesson-number")
    if num_div:
        new_num = int(num_div.get_text(strip=True).translate(ar_to_en))
        old_to_new[old_num] = new_num

# Wait! The old answer files (backup_answers/98.*.html) used the old numbers!
# Let's update the headers in 98.00_p120_Answers.html and the TOC.
with open("pages/98.00_p120_Answers.html", encoding="utf-8") as file:
    ans_content = file.read()

ans_soup = BeautifulSoup(ans_content, "html.parser")
headers = ans_soup.find_all("h3", class_="header-title")

for h3 in headers:
    text = h3.get_text(strip=True)
    m = re.search(r"الدَّرْسُ\s*([٠-٩0-9]+)", text)
    if m:
        old_ans_num = int(m.group(1).translate(ar_to_en))
        new_ans_num = old_to_new.get(old_ans_num, old_ans_num)
        new_text = re.sub(
            r"الدَّرْسُ\s*[٠-٩0-9]+", f"الدَّرْسُ {str(new_ans_num).translate(en_to_ar)}", text
        )
        h3.string = new_text

with open("pages/98.00_p120_Answers.html", "w", encoding="utf-8") as f:
    f.write(str(ans_soup))
print("Updated 98.00_p120_Answers.html with new lesson numbers")

# Now, we need to rebuild the TOC completely!
# The user asked:
# 1. Unique lesson titles in TOC.
# 2. Map every page of the answers section in the TOC and name it after the selected lessons in that page.
# BUT we combined the answers into ONE page! How can we map every page?
# The user says: "the answers section must every page of it mapped in the toc starting from answers to lesson 1 ,... into the end every page of it must be in the toc and named after the selected lessons in the page"
# This implies the user DOES NOT want them combined anymore?
# Wait! "every page of it must be in the toc" - the answers originally spanned 34 pages!
# If we keep them in ONE file, WeasyPrint paginates them.
# The only way to know the page numbers of the PDF is to run WeasyPrint, extract the page numbers, and put them in the TOC.
# BUT, we can use CSS `target-counter`!
# Let's write a python script to modify the TOC to use `target-counter` so WeasyPrint handles the page numbers dynamically!
