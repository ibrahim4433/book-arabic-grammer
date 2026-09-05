import os
import re
from bs4 import BeautifulSoup

def has_madkhal(text):
    if not text: return False
    clean = re.sub(r'[\u064B-\u065F\u0670]', '', text)
    return 'مدخل' in clean

files = [
    'pages/014.1_n035_الموسيقا_الشعرية.html', 'pages/014.2_n036_الموسيقا_الشعرية.html', 'pages/028.0_n058_اسلوب_الشرط.html', 
    'pages/088.0_n132_page_152.html', 'pages/100.0_n144_page_164.html', 'pages/102.0_n146_page_165.html', 'pages/110.0_n154_page_173.html', 
    'pages/120.0_n164_page_183.html', 'pages/144.0_n188_page_207.html', 'pages/175.0_n219_page_238.html', 'pages/196.0_n240_page_259.html', 
    'pages/202.0_n246_page_265.html', 'pages/204.0_n248_page_267.html', 'pages/207.0_n251_page_270.html', 'pages/227.0_n271_page_290.html', 
    'pages/234.0_n278_page_297.html', 'pages/245.0_n289_page_308.html'
]

for filepath in files:
    if not os.path.exists(filepath): continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    bio_card = soup.find(class_="bio-card")
    poem_container = soup.find(class_="poem-container")
    
    if not (bio_card and poem_container):
        continue
        
    intro_block = None
    for block in soup.find_all(class_="content-block"):
        header = block.find(class_="block-header")
        if header and has_madkhal(header.get_text()):
            intro_block = block
            break
            
    print(f"Processing {filepath}...")
    
    main_container = soup.find(class_="force-new-page")
    if not main_container:
        main_container = soup.body
        
    split_grid = soup.new_tag("div", attrs={"class": "split-grid mb-1mm w-full"})
    
    col1 = soup.new_tag("div")
    col2 = soup.new_tag("div")
    
    bio_card.extract()
    col1.append(bio_card)
    
    if intro_block:
        intro_block.extract()
        col2.append(intro_block)
    
    split_grid.append(col1)
    split_grid.append(col2)
    
    poem_container.extract()
    
    header_block = soup.find(class_="page-header-strip")
    if header_block:
        header_block.extract()
        
    children = list(main_container.children)
    remaining_elements = []
    for child in children:
        if child.name and child != header_block and child != bio_card and child != intro_block and child != poem_container:
            if child.get('class') and 'split-grid' in child.get('class') and not child.get_text(strip=True):
                 continue
            if child.name == 'div' and not child.get_text(strip=True):
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

print("Done structuring remaining pages")
