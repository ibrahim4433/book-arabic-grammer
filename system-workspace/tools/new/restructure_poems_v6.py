import os
from bs4 import BeautifulSoup
import re
import traceback

def process_file_v6(filepath):
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
            
        # Find exactly where the first poem starts in raw HTML
        poem_pattern = re.compile(r'<div[^>]*class="[^"]*poem-container[^"]*"[^>]*>')
        m_start = poem_pattern.search(raw_html)
        if not m_start: 
            print(f"Regex failed for {filepath}")
            return
            
        html_before = raw_html[:m_start.start()]
        
        # We need to find everything that comes AFTER the corrupted blocks.
        # Find the parent containing the poems
        parent = poems[0].parent
        
        # Find the last element in the sequence that is corrupted.
        last_corrupted_elem = None
        for child in parent.children:
            if child.name is None: continue
            
            classes = child.get("class", [])
            if not isinstance(classes, list): classes = [classes]
                
            is_corrupted = False
            if "poem-container" in classes: is_corrupted = True
            elif "split-grid" in classes: is_corrupted = True
            elif "w-50pct" in classes: is_corrupted = True
            elif "flex" in classes and child.find(class_="irab-box"): is_corrupted = True
            elif "content-block" in classes:
                hdr = child.find(class_="block-header")
                if hdr and any(x in hdr.get_text() for x in ["دراسة", "تحليل", "المفردات", "الشرح", "تتمة التحليل", "إعراب", "الإعراب"]):
                    is_corrupted = True
                    
            if is_corrupted:
                last_corrupted_elem = child
                
        # Now find the NEXT element that is NOT corrupted
        html_after = ""
        next_elem = last_corrupted_elem.find_next_sibling()
        
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

        if next_elem:
            # Usually the next element is an exam question or a benefit-box
            if next_elem.get("id"):
                s, e = find_bound(next_elem.name, next_elem.get("id"))
                if s is not None: html_after = raw_html[s:]
            else:
                # If it doesn't have an ID, we can just split at </section>
                s_idx = raw_html.rfind("</section>")
                if s_idx != -1: html_after = raw_html[s_idx:]
        else:
            s_idx = raw_html.rfind("</section>")
            if s_idx != -1: html_after = raw_html[s_idx:]
            
        # Build new blocks
        new_blocks = []
        for p_elem, v_chunk, i_chunk in zip(poems, vocab_chunks, irab_chunks):
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
        final_html = re.sub(r'\n\s*\n\s*\n', '\n\n', final_html)
        
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
    process_file_v6(os.path.join("pages", f))
