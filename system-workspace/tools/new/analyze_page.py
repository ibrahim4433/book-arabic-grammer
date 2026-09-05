import os
import re
from bs4 import BeautifulSoup, Tag

def convert_to_arabic_index(index_str):
    mapping = {
        "الأول": 1, "الثاني": 2, "الثالث": 3, "الرابع": 4, "الخامس": 5,
        "السادس": 6, "السابع": 7, "الثامن": 8, "التاسع": 9, "العاشر": 10,
        "الحادي عشر": 11, "الثاني عشر": 12, "الثالث عشر": 13, "الرابع عشر": 14,
        "الخامس عشر": 15, "السادس عشر": 16, "السابع عشر": 17, "الثامن عشر": 18,
        "التاسع عشر": 19, "العشرين": 20, "الأولى": 1, "الثانية": 2
    }
    for k, v in mapping.items():
        if k in index_str:
            return v
    return None

def extract_vocab_items(block):
    # block could have <p><strong>المفردات:</strong> ...</p>
    # or <ul><li><span class="text-accent font-bold">المفردات:</span> ...</li></ul>
    items = []
    # Try <p> tags
    for p in block.find_all("p"):
        strong = p.find("strong")
        if strong:
            key = strong.get_text(strip=True)
            strong.extract()
            val = p.decode_contents().strip()
            # Remove any leading colons from val if strong didn't have it
            if val.startswith(":"): val = val[1:].strip()
            items.append((key, val))
            continue
        
        # Try finding spans with bold/accent
        span = p.find("span", class_=re.compile("text-accent|font-bold"))
        if span:
            key = span.get_text(strip=True)
            span.extract()
            val = p.decode_contents().strip()
            if val.startswith(":"): val = val[1:].strip()
            items.append((key, val))
            continue
            
    # Try <li> tags
    for li in block.find_all("li"):
        # find the title, usually in strong or text-accent
        title_tag = li.find(["strong", "b"]) or li.find("span", class_=re.compile("text-accent|font-bold|highlight"))
        if title_tag:
            key = title_tag.get_text(strip=True)
            title_tag.extract()
            # remove marker if exists
            marker = li.find(class_="marker")
            if marker: marker.extract()
            val = li.decode_contents().strip()
            if val.startswith(":"): val = val[1:].strip()
            items.append((key, val))
        else:
            # If no clear title, it might be just text
            marker = li.find(class_="marker")
            if marker: marker.extract()
            val = li.decode_contents().strip()
            items.append(("", val))
            
    return items

def extract_irab_items(container):
    # container could be a block with a dense-table, or a list of irab-box divs
    items = []
    
    # 1. Look for irab-boxes
    boxes = container.find_all(class_="irab-box")
    for box in boxes:
        word_tag = box.find(class_="irab-word")
        details_tag = box.find(class_="irab-details")
        if word_tag and details_tag:
            word = word_tag.decode_contents().strip()
            details = details_tag.decode_contents().strip()
            items.append((word, details))
            
    # 2. Look for dense-tables
    tables = container.find_all("table", class_="dense-table")
    for table in tables:
        for row in table.find_all("tr"):
            cells = row.find_all(["td", "th"])
            if len(cells) >= 2:
                word = cells[0].decode_contents().strip()
                details = cells[1].decode_contents().strip()
                items.append((word, details))
                
    # 3. Look for already smashed <li> elements
    if not boxes and not tables:
        ul = container.find("ul", class_="structured-list")
        if ul:
            for li in ul.find_all("li"):
                marker = li.find(class_="marker")
                if marker: marker.extract()
                text = li.decode_contents().strip()
                # we don't try to re-split, just treat as one item
                items.append(("", text))
                
    return items

# First, let's just inspect page 108 to see how we can extract
soup = BeautifulSoup(open("pages/044.0_n088_page_108.html", encoding="utf-8").read(), "html.parser")
print("Found poems:", len(soup.find_all(class_="poem-container")))
# Check headers for "دراسة البيت" or similar
blocks = soup.find_all(class_="content-block")
for b in blocks:
    hdr = b.find(class_="block-header")
    if hdr:
        print("Block:", hdr.get_text(strip=True))

