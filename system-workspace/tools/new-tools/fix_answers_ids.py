import json

from bs4 import BeautifulSoup

with open("lesson_mapping.json", encoding="utf-8") as f:
    unique_lessons = json.load(f)

# Create a mapping from title to new lesson number
title_to_num = {title.strip(): num for num, title, path in unique_lessons}

with open("pages/98.00_p120_Answers.html", encoding="utf-8") as f:
    content = f.read()

soup = BeautifulSoup(content, "html.parser")
headers = soup.find_all("div", class_="block-header accent")

for header in headers:
    span = header.find("span")
    if not span:
        continue
    text = span.get_text(strip=True)
    if text.startswith("إِجَابَاتُ:"):
        lesson_title = text.replace("إِجَابَاتُ:", "").strip()
        if lesson_title in title_to_num:
            num = title_to_num[lesson_title]
            header["id"] = f"ans-lesson-{num}"
            print(f"Assigned id 'ans-lesson-{num}' to '{lesson_title}'")
        else:
            print(f"Warning: '{lesson_title}' not found in mapping!")

with open("pages/98.00_p120_Answers.html", "w", encoding="utf-8") as f:
    f.write(str(soup))
