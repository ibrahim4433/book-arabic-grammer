import glob
import re

from bs4 import BeautifulSoup

ar_to_en = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
en_to_ar = str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")

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
    m = re.match(r"pages/(\d{2})\.", f)
    if not m:
        continue
    old_num = int(m.group(1))
    soup = BeautifulSoup(open(f, encoding="utf-8").read(), "html.parser")
    num_div = soup.find("div", class_="lesson-number")
    if num_div:
        new_num = int(num_div.get_text(strip=True).translate(ar_to_en))
        old_to_new[old_num] = new_num

with open("pages/98.00_p120_Answers.html", encoding="utf-8") as file:
    ans_content = file.read()

ans_soup = BeautifulSoup(ans_content, "html.parser")
headers = ans_soup.find_all("h3", class_="header-title")

for h3 in headers:
    text = h3.get_text(strip=True)
    m = re.search(r"الدَّرْسِ?\s*([٠-٩0-9]+)", text)
    if m:
        old_ans_num = int(m.group(1).translate(ar_to_en))
        new_ans_num = old_to_new.get(old_ans_num, old_ans_num)
        new_text = re.sub(
            r"الدَّرْسِ?\s*[٠-٩0-9]+", f"الدَّرْسِ {str(new_ans_num).translate(en_to_ar)}", text
        )
        h3.string = new_text
        h3["id"] = f"ans-lesson-{new_ans_num}"

with open("pages/98.00_p120_Answers.html", "w", encoding="utf-8") as f:
    f.write(str(ans_soup))

print("Updated 98.00_p120_Answers.html with new lesson numbers and IDs")
