import glob
import re
from bs4 import BeautifulSoup, Tag
import sys

def strip_tashkeel(text):
    tashkeel = re.compile(r'[\u0617-\u061A\u064B-\u0652]')
    return re.sub(tashkeel, '', text)

def is_vocab_block(block):
    if not isinstance(block, Tag) or 'content-block' not in block.get('class', []):
        return False
    header = block.find(class_='block-header')
    if header:
        text = strip_tashkeel(header.get_text())
        return any(word in text for word in ['الشرح', 'المفردات', 'الفكرة', 'البلاغة', 'الشعور', 'تحليل'])
    return False

def is_irab_block(block):
    if not isinstance(block, Tag) or 'content-block' not in block.get('class', []):
        return False
    header = block.find(class_='block-header')
    if header:
        text = strip_tashkeel(header.get_text())
        return 'إعراب' in text or 'الإعراب' in text
    return False

def find_next_element_sibling(element):
    sibling = element.next_sibling
    while sibling and not isinstance(sibling, Tag):
        sibling = sibling.next_sibling
    return sibling

def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    modified = False
    
    # 1. Fix poem-containers inside split-grids (like page 171)
    poem_containers = soup.find_all(class_="poem-container")
    for poem in poem_containers:
        # Check if poem is inside a split-grid
        parent_col = poem.parent
        if parent_col and parent_col.parent and 'split-grid' in parent_col.parent.get('class', []):
            split_grid = parent_col.parent
            # Extract poem and put it BEFORE the split-grid
            poem.extract()
            split_grid.insert_before(poem)
            modified = True
            
            # Since we moved the poem, we also need to ensure the remaining blocks in the split-grid are just Vocab and Irab.
            # Page 171 has: split-grid -> col1(Vocab, Irab of sentences) & col2(Irab of vocab).
            # If there are multiple Irab blocks, they should probably all be in the left column (col2).
            # The structure of page 171 split-grid is already Vocab in col1 and Irab in col2, but we just needed the poem out!
            # Let's enforce that the columns are w-50pct
            for col in split_grid.find_all(recursive=False):
                if isinstance(col, Tag):
                    classes = col.get('class', [])
                    if 'w-50pct' not in classes:
                        classes.append('w-50pct')
                        col['class'] = classes

    # 2. Fix sequentially stacked blocks (like page 170)
    # Re-fetch poem containers since DOM changed
    poem_containers = soup.find_all(class_="poem-container")
    for poem in poem_containers:
        sibling1 = find_next_element_sibling(poem)
        if not sibling1: continue
        
        # Sibling1 might be a block, or it might be a split-grid!
        if 'split-grid' in sibling1.get('class', []):
            continue # already in a split grid
            
        sibling2 = find_next_element_sibling(sibling1)
        if not sibling2: continue
        
        vocab_block = None
        irab_block = None
        
        if is_vocab_block(sibling1) and is_irab_block(sibling2):
            vocab_block = sibling1
            irab_block = sibling2
        elif is_irab_block(sibling1) and is_vocab_block(sibling2):
            irab_block = sibling1
            vocab_block = sibling2
            
        if vocab_block and irab_block:
            split_grid = soup.new_tag("div")
            split_grid["class"] = "split-grid mb-1mm"
            
            col1 = soup.new_tag("div")
            col1["class"] = "w-50pct"
            col2 = soup.new_tag("div")
            col2["class"] = "w-50pct"
            
            vocab_block.extract()
            irab_block.extract()
            
            col1.append(vocab_block)
            col2.append(irab_block)
            
            split_grid.append(col1)
            split_grid.append(col2)
            
            poem.insert_after(split_grid)
            modified = True
            
    # 3. Ensure any split-grid that directly follows a poem-container has w-50pct columns
    poem_containers = soup.find_all(class_="poem-container")
    for poem in poem_containers:
        sibling1 = find_next_element_sibling(poem)
        if sibling1 and 'split-grid' in sibling1.get('class', []):
            cols = sibling1.find_all(recursive=False)
            if len(cols) == 2:
                for col in cols:
                    if isinstance(col, Tag):
                        classes = col.get('class', [])
                        if 'w-50pct' not in classes:
                            classes.append('w-50pct')
                            col['class'] = classes
                            modified = True

    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(str(soup))
        print(f"Restructured {filepath}")

def main():
    files = glob.glob("pages/*.html")
    for f in files:
        process_file(f)

if __name__ == "__main__":
    main()
