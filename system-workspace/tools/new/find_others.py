import glob
from bs4 import BeautifulSoup

files = glob.glob("pages/*.html")
others = []

for filepath in files:
    if "_cont" in filepath: continue
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    bio_card = soup.find(class_="bio-card")
    poem_container = soup.find(class_="poem-container")
    
    if bio_card and poem_container:
        parent = bio_card.parent
        is_processed = False
        if parent and parent.name == "div":
            grandparent = parent.parent
            if grandparent and grandparent.get("class") and "split-grid" in grandparent.get("class") and "w-full" in grandparent.get("class"):
                is_processed = True
                
        if not is_processed:
            others.append(filepath)

print("Other pages with bio and poem:", others)
