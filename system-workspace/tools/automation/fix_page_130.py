from bs4 import BeautifulSoup
import os

file_path = 'pages/page_130_enat1.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

merges = {
    'b00013': ['b00014', 'b00015'],
    'b00017': ['b00018'],
    'b00026': ['b00027'],
    'b00029': ['b00030']
}

for target_id, source_ids in merges.items():
    target = soup.find(id=target_id)
    if target:
        target_verses = target.find('div', class_='poem-verses')
        for sid in source_ids:
            source = soup.find(id=sid)
            if source:
                source_verses = source.find('div', class_='poem-verses')
                # append all children of source_verses to target_verses
                for child in list(source_verses.children):
                    target_verses.append(child)
                # remove the source block
                source.decompose()

# Also remove the "(تابع)" text from any other headers just in case, though they are removed by decomposing.
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Page 130 fixed.")
