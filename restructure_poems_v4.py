import os
from bs4 import BeautifulSoup
import re
import traceback

def process_file_v4(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            raw_html = f.read()
            
        soup = BeautifulSoup(raw_html, "html.parser")
        
        poems = soup.find_all(class_="poem-container")
        num_poems = len(poems)
        if num_poems == 0:
            return
            
        # Extract vocab chunks
        vocab_blocks = []
        for b in soup.find_all(class_="content-block"):
            hdr = b.find(class_="block-header")
            if hdr and any(x in hdr.get_text() for x in ["المفردات", "الشرح", "تحليل", "دراسة", "فهم", "تذوق"]):
                vocab_blocks.append(b)
                
        vocab_chunks = []
        if vocab_blocks:
            # We assume all vocab is in the first block
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
                    
        vocab_chunks = vocab_chunks[:num_poems]
        while len(vocab_chunks) < num_poems: vocab_chunks.append([])
            
        # Extract irab chunks
        irab_chunks = []
        irab_container = None
        for flex in soup.find_all("div", class_="flex"):
            if not flex.find_parents(class_="content-block") and flex.find(class_="irab-box"):
                irab_container = flex
                break
                
        if irab_container:
            boxes = irab_container.find_all(class_="irab-box")
            for box in boxes:
                word = box.find(class_="irab-word")
                details = box.find(class_="irab-details")
                if word and details:
                    w_text = word.decode_contents().strip()
                    if w_text.endswith(":"): w_text = w_text[:-1].strip()
                    d_text = details.decode_contents().strip()
                    irab_chunks.append(f"{w_text}: {d_text}")
        else:
            for b in soup.find_all(class_="content-block"):
                hdr = b.find(class_="block-header")
                if hdr and ("إعراب" in hdr.get_text() or "الإعراب" in hdr.get_text()):
                    ul = b.find("ul", class_="structured-list")
                    if ul:
                        for li in ul.find_all("li"):
                            marker = li.find(class_="marker")
                            if marker: marker.decompose()
                            irab_chunks.append(li.decode_contents().strip())
                            
        irab_chunks = irab_chunks[:num_poems]
        while len(irab_chunks) < num_poems: irab_chunks.append("")
            
        # Now, REBUILD THE ENTIRE PAGE 
        # We will keep the header, and any content that is NOT part of the poem/vocab/irab sequence.
        # It's safer to extract everything before the FIRST poem, and everything after the LAST irab/vocab block.
        
        # But wait, there might be exams or other things AFTER the poems!
        # Find the first poem's index in the raw_html
        first_poem_match = re.search(r'<div class="poem-container"[^>]*>', raw_html)
        if not first_poem_match: return
        first_poem_idx = first_poem_match.start()
        
        # Everything before the first poem
        header_html = raw_html[:first_poem_idx]
        
        # Now find what comes AFTER the poems. Usually exams, or `</section></body></html>`
        # Let's find all poem containers, split-grids, irab-boxes, and content-blocks (with vocab/irab)
        # Instead of manual slicing, let's use BS4 to decompose the bad elements, 
        # BUT we can't write out BS4 directly because it destroys formatting.
        
        # Actually, let's just use BS4 to get the HTML of the bad elements, and then string-replace them with empty string.
        elements_to_remove = []
        for p in poems:
            elements_to_remove.append(str(p))
            
        for split in soup.find_all(class_="split-grid"):
            elements_to_remove.append(str(split))
            
        for b in soup.find_all(class_="content-block"):
            hdr = b.find(class_="block-header")
            if hdr and any(x in hdr.get_text() for x in ["دراسة", "تحليل", "المفردات", "الشرح", "تتمة التحليل", "إعراب", "الإعراب"]):
                elements_to_remove.append(str(b))
                
        if irab_container:
            elements_to_remove.append(str(irab_container))
            
        # For any lingering w-50pct wrappers
        for w in soup.find_all(class_="w-50pct"):
            if not w.find_parents(class_="split-grid"): # if it wasn't already in a removed split-grid
                elements_to_remove.append(str(w))
        
        # But str(element) might not exactly match raw_html due to attribute ordering.
        # That's why find_block_bounds was better!
        pass
        
    except Exception as e:
        print(f"Error on {filepath}: {e}")
        traceback.print_exc()
