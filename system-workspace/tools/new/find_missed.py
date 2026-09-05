import glob
from bs4 import BeautifulSoup
import re

def has_madkhal(text):
    clean = re.sub(r'[\u064B-\u065F\u0670]', '', text)
    return 'مدخل' in clean

files = glob.glob("pages/*.html")
missed = []

for filepath in files:
    if "_cont" in filepath: continue
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    bio_card = soup.find(class_="bio-card")
    poem_container = soup.find(class_="poem-container")
    
    intro_block = None
    for block in soup.find_all(class_="content-block"):
        header = block.find(class_="block-header")
        if header and has_madkhal(header.get_text()):
            intro_block = block
            break
            
    if bio_card and poem_container and intro_block:
        parent = bio_card.parent
        is_processed = False
        if parent and parent.name == "div":
            grandparent = parent.parent
            if grandparent and grandparent.get("class") and "split-grid" in grandparent.get("class") and "w-full" in grandparent.get("class"):
                is_processed = True
                
        if not is_processed:
            missed.append(filepath)

print("Missed pages:", missed)
