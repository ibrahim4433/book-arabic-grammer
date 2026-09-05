import os
from bs4 import BeautifulSoup
import re

def test_chunking(filepath):
    print(f"\n--- Testing {filepath} ---")
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    poems = soup.find_all(class_="poem-container")
    num_poems = len(poems)
    print(f"Found {num_poems} poems.")
    
    # Find the single big vocab list
    vocab_blocks = []
    blocks = soup.find_all(class_="content-block")
    for b in blocks:
        hdr = b.find(class_="block-header")
        if hdr and "المفردات" in hdr.get_text():
            vocab_blocks.append(b)
            
    if not vocab_blocks:
        print("No vocab block found.")
        return
        
    print(f"Found {len(vocab_blocks)} vocab blocks (should be 1 if corrupted)")
    
    ul = vocab_blocks[0].find("ul", class_="structured-list")
    if not ul:
        print("No UL in vocab block.")
        return
        
    lis = ul.find_all("li")
    chunks = []
    current_chunk = []
    
    for li in lis:
        text = li.get_text()
        if "المفردات" in text and current_chunk:
            chunks.append(current_chunk)
            current_chunk = []
        current_chunk.append(text)
        
    if current_chunk:
        chunks.append(current_chunk)
        
    print(f"Chunked into {len(chunks)} groups. (Should match num_poems = {num_poems})")
    for i, c in enumerate(chunks):
        print(f"  Chunk {i+1} has {len(c)} items. First item: {c[0][:50]}")

if __name__ == "__main__":
    test_chunking("pages/044.0_n088_page_108.html")
    test_chunking("pages/045.0_n089_page_109.html")
