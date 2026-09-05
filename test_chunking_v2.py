import os
from bs4 import BeautifulSoup, Comment
import re

def test_chunking_v2(filepath):
    print(f"\n--- Testing {filepath} ---")
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    poems = soup.find_all(class_="poem-container")
    num_poems = len(poems)
    print(f"Found {num_poems} poems.")
    
    vocab_blocks = []
    for b in soup.find_all(class_="content-block"):
        hdr = b.find(class_="block-header")
        if hdr and any(x in hdr.get_text() for x in ["المفردات", "الشرح", "تحليل", "دراسة"]):
            vocab_blocks.append(b)
            
    if not vocab_blocks:
        print("No vocab block found.")
        return
        
    ul = vocab_blocks[0].find("ul", class_="structured-list")
    if not ul:
        print("No UL found in vocab block.")
        return
        
    chunks = []
    current_chunk = []
    seen_keys = set()
    
    for li in ul.find_all("li"):
        # extract key
        key = ""
        strong = li.find(["strong", "b"]) or li.find("span", class_=re.compile("text-accent|font-bold|highlight"))
        if strong:
            key = strong.get_text().strip(" :\t\n")
            
        text = li.get_text()
        
        # Start new chunk condition:
        if current_chunk and (key == "المفردات" or key in seen_keys):
            chunks.append(current_chunk)
            current_chunk = []
            seen_keys = set()
            
        current_chunk.append(text)
        if key:
            seen_keys.add(key)
            
    if current_chunk:
        chunks.append(current_chunk)
        
    print(f"Chunked into {len(chunks)} groups. (Expected {num_poems})")
    
    # Also test I'rab extraction
    irab_chunks = []
    irab_container = None
    for flex in soup.find_all("div", class_="flex"):
        if not flex.find_parents(class_="content-block") and flex.find(class_="irab-box"):
            irab_container = flex
            break
            
    if irab_container:
        boxes = irab_container.find_all(class_="irab-box")
        print(f"Found {len(boxes)} Irab boxes. (Expected {num_poems})")
    else:
        # Check if irab is in a content-block
        for b in soup.find_all(class_="content-block"):
            hdr = b.find(class_="block-header")
            if hdr and ("إعراب" in hdr.get_text() or "الإعراب" in hdr.get_text()):
                ul = b.find("ul", class_="structured-list")
                if ul:
                    lis = ul.find_all("li")
                    print(f"Found {len(lis)} Irab items in list. (Expected {num_poems})")

if __name__ == "__main__":
    test_chunking_v2("pages/044.0_n088_page_108.html")
    test_chunking_v2("pages/045.0_n089_page_109.html")
