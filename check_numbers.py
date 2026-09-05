import glob
from bs4 import BeautifulSoup
import re

files = glob.glob("pages/*.html")
already_numbered = []

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    for poem in soup.find_all(class_="poem-container"):
        lines = poem.find_all(class_="poem-line")
        if not lines: continue
        first_hemi = lines[0].find(class_="hemistich")
        if first_hemi:
            text = first_hemi.get_text(strip=True)
            if re.match(r'^[\u0660-\u06690-9]+', text):
                already_numbered.append((filepath, text[:15]))
                break

for f, t in already_numbered:
    print(f"{f}: {t}")
print(f"Total files with numbered poems: {len(already_numbered)}")
