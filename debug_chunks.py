import os
from bs4 import BeautifulSoup
import re

filepath = "pages/044.0_n088_page_108.html"
with open(filepath, "r", encoding="utf-8") as f:
    raw_html = f.read()
    
soup = BeautifulSoup(raw_html, "html.parser")
poems = soup.find_all(class_="poem-container")
num_poems = len(poems)
print("Num poems:", num_poems)

vocab_blocks = []
for b in soup.find_all(class_="content-block"):
    hdr = b.find(class_="block-header")
    if hdr and any(x in hdr.get_text() for x in ["المفردات", "الشرح", "تحليل", "دراسة", "فهم", "تذوق"]):
        vocab_blocks.append(b)
        
vocab_chunks = []
if vocab_blocks:
    ul = vocab_blocks[0].find("ul", class_="structured-list")
    if ul:
        current_chunk = []
        seen_keys = set()
        for li in ul.find_all("li"):
            key = ""
            strong = li.find(["strong", "b"]) or li.find("span", class_=re.compile("text-accent|font-bold|highlight"))
            if strong: key = strong.get_text().strip(" :\t\n")
            
            if current_chunk and (key == "المفردات" or key in seen_keys):
                vocab_chunks.append(current_chunk)
                current_chunk = []
                seen_keys = set()
                
            marker = li.find(class_="marker")
            if marker: marker.decompose()
            current_chunk.append(li.decode_contents().strip())
            if key: seen_keys.add(key)
        if current_chunk:
            vocab_chunks.append(current_chunk)
            
print("Vocab chunks length before truncation:", len(vocab_chunks))
for i, c in enumerate(vocab_chunks):
    print(f" Chunk {i}: {len(c)} items")
    
vocab_chunks = vocab_chunks[:num_poems]
while len(vocab_chunks) < num_poems: vocab_chunks.append([])

print("Vocab chunks length after truncation:", len(vocab_chunks))
for i, c in enumerate(vocab_chunks):
    print(f" Chunk {i}: {len(c)} items")
