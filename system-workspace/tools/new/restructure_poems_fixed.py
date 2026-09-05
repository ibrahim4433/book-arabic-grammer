import os
import glob
import re
from bs4 import BeautifulSoup

def remove_tashkeel(text):
    return re.sub(r'[\u064B-\u065F\u0670]', '', text)

def process_file(filepath):
    # Only process files that don't have _cont in them
    if "_cont" in filepath: return
        
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    bio_card = soup.find(class_="bio-card")
    poem_container = soup.find(class_="poem-container")
    
    # We also need to find "مدخل الى النص"
    intro_block = None
    for block in soup.find_all(class_="content-block"):
        header = block.find(class_="block-header")
        if header:
            clean_header = remove_tashkeel(header.get_text())
            if "مدخل" in clean_header:
                intro_block = block
                break
                
    if not (bio_card and poem_container and intro_block):
        return # Not a target page
        
    # Check if already processed (has split-grid containing bio-card)
    parent = bio_card.parent
    if parent and parent.name == "div":
        grandparent = parent.parent
        if grandparent and grandparent.get("class") and "split-grid" in grandparent.get("class"):
            return # Already processed
            
    print(f"Processing {filepath}...")
    
    main_container = soup.find(class_="force-new-page")
    if not main_container:
        main_container = soup.body
        
    split_grid = soup.new_tag("div", attrs={"class": "split-grid mb-1mm w-full"})
    
    col1 = soup.new_tag("div") # Right in RTL (bio_card)
    col2 = soup.new_tag("div") # Left in RTL (intro_block)
    
    bio_card_parent = bio_card.parent
    bio_card.extract()
    col1.append(bio_card)
    
    intro_block_parent = intro_block.parent
    intro_block.extract()
    col2.append(intro_block)
    
    split_grid.append(col1)
    split_grid.append(col2)
    
    poem_container.extract()
    
    children = list(main_container.children)
    header_block = soup.find(class_="page-header-strip")
    if header_block:
        header_block.extract()
        
    remaining_elements = []
    for child in children:
        if child.name and child != header_block and child != bio_card and child != intro_block and child != poem_container:
            if child.get('class') and 'split-grid' in child.get('class'):
                 if not child.find_all(recursive=False):
                     continue
            remaining_elements.append(child)
            
    main_container.clear()
    if header_block:
         main_container.append(header_block)
    main_container.append(split_grid)
    main_container.append(poem_container)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(str(soup))
        
    if remaining_elements:
        dirname = os.path.dirname(filepath)
        basename = os.path.basename(filepath)
        
        parts = basename.split('_')
        if len(parts) >= 3:
            num1 = parts[0]
            num2 = parts[1]
            try:
                f_num1 = float(num1)
                new_num1 = f"{f_num1 + 0.05:.2f}".rstrip('0').rstrip('.')
            except:
                new_num1 = num1 + "5"
                
            new_num2 = num2 + "a"
            
            rest = "_".join(parts[2:]).replace(".html", "")
            new_basename = f"{new_num1}_{new_num2}_{rest}_cont.html"
        else:
            new_basename = basename.replace(".html", "_cont.html")
            
        new_filepath = os.path.join(dirname, new_basename)
        print(f"  Moving extra content to {new_filepath}")
        
        new_soup = BeautifulSoup('<!DOCTYPE html><html dir="rtl" lang="ar"><head><meta charset="utf-8"/><title>Continuation</title><link href="../styles/main.css" rel="stylesheet"/></head><body><div class="force-new-page"></div></body></html>', "html.parser")
        new_main = new_soup.find(class_="force-new-page")
        
        if header_block:
            new_header = BeautifulSoup(str(header_block), "html.parser").header
            new_main.append(new_header)
            
        for el in remaining_elements:
            new_main.append(el)
            
        with open(new_filepath, "w", encoding="utf-8") as f:
            f.write(str(new_soup))

files = glob.glob("pages/*.html")
for f in files:
    process_file(f)

print("Done restructuring poem pages.")
