import os
from bs4 import BeautifulSoup
import re
import traceback

def find_block_bounds(raw_html, tag_name, class_value=None, text_content=None, instance_idx=0):
    """
    A more robust block bound finder.
    We just use BS4 to find the element, get a unique snippet of it, and find it in raw_html.
    But BS4 alters whitespace. So the easiest way to find a block's end is:
    Find all start tags, keep track of nesting, etc.
    Actually, we can just use the `sourceline` and `sourcepos` if we use html5lib? No, bs4 html.parser doesn't give byte offsets easily.
    """
    pass

def process_file_v5(filepath):
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
            
        # 1. Find html_before (everything up to the first poem)
        # We can find the exact match of the first poem's raw string (or parts of it)
        first_poem = poems[0]
        # Regex search for poem-container
        m_start = re.search(r'<div[^>]*class="poem-container"[^>]*>', raw_html)
        if not m_start: return
        html_before = raw_html[:m_start.start()]
        
        # 2. Find html_after (everything after the last poem analysis block)
        # What is the last block? It could be an irab block, or vocab block, or a split-grid.
        # Let's find the FIRST element that is NOT part of the poem sequence and comes AFTER the first poem.
        # Examples of after-elements: <div class="exam-question">, <div class="benefit-box">, </section>
        
        # Let's iterate all top-level children of the main container (usually inside <body> or <section>)
        # Actually, since we only want to nuke the poems+vocab+irab, we can just find the LAST element of this corrupted sequence.
        # Let's collect the IDs of all poems, vocab blocks, and irab blocks.
        ids_to_nuke = []
        for p in poems:
            if p.get("id"): ids_to_nuke.append(p.get("id"))
        for b in soup.find_all(class_="content-block"):
            hdr = b.find(class_="block-header")
            if hdr and any(x in hdr.get_text() for x in ["دراسة", "تحليل", "المفردات", "الشرح", "تتمة التحليل", "إعراب", "الإعراب"]):
                if b.get("id"): ids_to_nuke.append(b.get("id"))
        if irab_container:
            for box in irab_container.find_all(class_="irab-box"):
                if box.get("id"): ids_to_nuke.append(box.get("id"))
        
        # What if the user wrapped them in split-grids? We should nuke those too.
        for sg in soup.find_all(class_="split-grid"):
            if sg.get("id"): ids_to_nuke.append(sg.get("id"))
            
        # The end index is the end of the LAST element in ids_to_nuke.
        # We can use our find_block_bounds function.
        max_end_idx = 0
        def find_bound(tag_name, id_value):
            start_match = re.search(f'<{tag_name}[^>]*id=[\'"]{id_value}[\'"][^>]*>', raw_html)
            if not start_match: return None, None
            idx = start_match.end()
            depth = 1
            tag_pattern = re.compile(f'</?{tag_name}(?:>|\\s[^>]*>)')
            while depth > 0:
                match = tag_pattern.search(raw_html, idx)
                if not match: break
                if match.group(0).startswith("</"): depth -= 1
                elif not match.group(0).endswith("/>"): depth += 1
                idx = match.end()
            return start_match.start(), idx
            
        for tag in ["div", "section", "ul"]:
            for eid in ids_to_nuke:
                s, e = find_bound(tag, eid)
                if e and e > max_end_idx:
                    max_end_idx = e
                    
        # But wait, what if there are wrappers like <div class="w-50pct"> without IDs?
        # If they are inside a split-grid WITH an ID, they are deleted.
        # If they are NOT in a split-grid with an ID... 
        # Actually, it's safer to just find ALL tags in raw_html that are between m_start.start() and the next <div class="exam-question"> or </section>.
        
        # Another approach:
        # We use BS4 to identify ALL elements.
        # We find the element that immediately FOLLOWS the corrupted section.
        # How do we know what follows?
        # It's the first sibling of the poems/vocab blocks that is NOT a poem, vocab block, irab block, split-grid, or w-50pct.
        
        # Let's find the parent container.
        parent = poems[0].parent
        
        last_corrupted_elem = None
        for child in parent.children:
            if child.name is None: continue # text node
            is_corrupted = False
            
            if "poem-container" in child.get("class", []): is_corrupted = True
            elif "split-grid" in child.get("class", []): is_corrupted = True
            elif "w-50pct" in child.get("class", []): is_corrupted = True
            elif "flex" in child.get("class", []) and child.find(class_="irab-box"): is_corrupted = True
            elif "content-block" in child.get("class", []):
                hdr = child.find(class_="block-header")
                if hdr and any(x in hdr.get_text() for x in ["دراسة", "تحليل", "المفردات", "الشرح", "تتمة التحليل", "إعراب", "الإعراب"]):
                    is_corrupted = True
                    
            if is_corrupted:
                last_corrupted_elem = child
                
        # We know `last_corrupted_elem`. If it has an ID, we find its end index in raw_html.
        # What if it doesn't have an ID? We can give it a temporary ID in raw_html?
        # No, we can just look for the NEXT sibling that has an ID!
        
        next_sibling = last_corrupted_elem.find_next_sibling()
        html_after = ""
        if next_sibling and next_sibling.get("id"):
            s, e = find_bound(next_sibling.name, next_sibling.get("id"))
            if s: html_after = raw_html[s:]
        elif next_sibling and next_sibling.name == "section": # </section> is the parent end
            html_after = "\n</section>\n</body>\n</html>\n"
        else:
            # Fallback: just split at </section>
            s_idx = raw_html.rfind("</section>")
            if s_idx != -1:
                html_after = raw_html[s_idx:]
                
        # Now construct the new HTML
        new_blocks = []
        for p_elem, v_chunk, i_chunk in zip(poems, vocab_chunks, irab_chunks):
            # Clean poem
            temp_soup = BeautifulSoup(str(p_elem), "html.parser")
            lines = temp_soup.find_all(class_="poem-line")
            if len(lines) == 1:
                hemis = lines[0].find_all(class_="hemistich")
                if hemis:
                    for desc in hemis[0].descendants:
                        if isinstance(desc, str) and desc.strip():
                            new_text = re.sub(r'^[\s\u200B]*[\u0660-\u06690-9]+[\s\u200B]*[-ـ][\s\u200B]*', '', str(desc))
                            desc.replace_with(new_text)
                            break
            hdr = temp_soup.find(class_="poem-header")
            if hdr: hdr.decompose()
            clean_poem = str(temp_soup)
            
            # Build split grid
            sg = []
            sg.append('<div class="split-grid mb-1mm">')
            sg.append('<div class="w-50pct">')
            sg.append('<div class="content-block mb-0">')
            sg.append('<div class="block-header bg-accent p-0 text-xs">')
            sg.append('<span>المفردات والشرح والبلاغة</span>')
            sg.append('</div>')
            sg.append('<div class="block-body p-0 text-xs">')
            if v_chunk:
                sg.append('<ul class="structured-list">')
                for text in v_chunk: sg.append(f'<li>{text}</li>')
                sg.append('</ul>')
            sg.append('</div></div></div>')
            sg.append('<div class="w-50pct">')
            sg.append('<div class="content-block mb-0">')
            sg.append('<div class="block-header p-0 text-xs">')
            sg.append('<span>الإعراب</span>')
            sg.append('</div>')
            sg.append('<div class="block-body p-0 text-xs">')
            if i_chunk:
                sg.append('<ul class="structured-list">')
                sg.append(f'<li><span class="marker">•</span><span>{i_chunk}</span></li>')
                sg.append('</ul>')
            sg.append('</div></div></div></div>')
            
            new_blocks.append(clean_poem + "\n" + "\n".join(sg))
            
        final_html = html_before + "\n".join(new_blocks) + "\n" + html_after
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(final_html)
        print(f"Fixed {filepath}")
        
    except Exception as e:
        print(f"Error on {filepath}: {e}")
        traceback.print_exc()

TARGET_FILES = [
"044.0_n088_page_108.html",
"045.0_n089_page_109.html",
"108.0_n152_page_171.html"
]

for f in TARGET_FILES:
    process_file_v5(os.path.join("pages", f))
