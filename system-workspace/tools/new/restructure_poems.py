import os
import glob
from bs4 import BeautifulSoup

def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    bio_card = soup.find(class_="bio-card")
    poem_container = soup.find(class_="poem-container")
    
    # We also need to find "مدخل الى النص"
    intro_block = None
    for block in soup.find_all(class_="content-block"):
        header = block.find(class_="block-header")
        if header and "مدخل" in header.get_text():
            intro_block = block
            break
            
    if not (bio_card and poem_container and intro_block):
        return # Not a target page
        
    print(f"Processing {filepath}...")
    
    # Find the main container (usually body or force-new-page)
    main_container = soup.find(class_="force-new-page")
    if not main_container:
        main_container = soup.body
        
    # Create the split grid
    split_grid = soup.new_tag("div", attrs={"class": "split-grid mb-1mm"})
    
    col1 = soup.new_tag("div") # Right in RTL (bio_card)
    col2 = soup.new_tag("div") # Left in RTL (intro_block)
    
    # Extract them from their current location and put them in columns
    bio_card_parent = bio_card.parent
    bio_card.extract()
    col1.append(bio_card)
    
    intro_block_parent = intro_block.parent
    intro_block.extract()
    col2.append(intro_block)
    
    split_grid.append(col1)
    split_grid.append(col2)
    
    # We need to assemble the new layout.
    # 1. header
    # 2. split-grid
    # 3. poem-container
    
    # Extract poem container
    poem_container.extract()
    
    # Get all direct children of main_container
    children = list(main_container.children)
    
    # We want to keep the header (page-header-strip) in place.
    # So we'll clear the main container, append header, append split-grid, append poem,
    # and collect anything else to move to a new page.
    
    header_block = soup.find(class_="page-header-strip")
    if header_block:
        header_block.extract()
        
    # Collect all other blocks that were in the main container (ignoring empty text/spaces)
    remaining_elements = []
    for child in children:
        if child.name and child != header_block and child != bio_card and child != intro_block and child != poem_container:
            # Check if this child contains only empty space or the wrapper for bio_card/intro
            if child.get('class') and 'split-grid' in child.get('class'):
                 # It was the old split grid, ignore if it's empty now
                 if not child.find_all(recursive=False):
                     continue
            remaining_elements.append(child)
            
    # Rebuild main page
    main_container.clear()
    if header_block:
         main_container.append(header_block)
    main_container.append(split_grid)
    main_container.append(poem_container)
    
    # Write the modified main page back
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(str(soup))
        
    # Process remaining elements
    if remaining_elements:
        # Generate new filename
        # e.g., 123.0_n167_page_186.html -> 123.05_n167a_page_186_cont.html
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
        
        # Create a new document for the extra content
        new_soup = BeautifulSoup('<!DOCTYPE html><html dir="rtl" lang="ar"><head><meta charset="utf-8"/><title>Continuation</title><link href="../styles/main.css" rel="stylesheet"/></head><body><div class="force-new-page"></div></body></html>', "html.parser")
        new_main = new_soup.find(class_="force-new-page")
        
        # Optionally add a simple header
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
