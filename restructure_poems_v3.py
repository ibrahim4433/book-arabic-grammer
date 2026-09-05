import os
from bs4 import BeautifulSoup
import re
import traceback

def find_block_bounds(raw_html, tag_name, id_value):
    start_match = re.search(f'<{tag_name}[^>]*id=[\'"]{id_value}[\'"][^>]*>', raw_html)
    if not start_match: 
        return None, None
    start_idx = start_match.start()
    
    idx = start_match.end()
    depth = 1
    
    tag_pattern = re.compile(f'</?{tag_name}(?:>|\\s[^>]*>)')
    
    while depth > 0:
        match = tag_pattern.search(raw_html, idx)
        if not match:
            break
        tag_str = match.group(0)
        if tag_str.startswith("</"):
            depth -= 1
        elif not tag_str.endswith("/>"):
            depth += 1
        idx = match.end()
        
    return start_idx, idx

def remove_slice(raw_html, start, end):
    return raw_html[:start] + (" " * (end - start)) + raw_html[end:]

def get_arabic_index(text):
    mapping = {
        "الأول": 1, "الثاني": 2, "الثالث": 3, "الرابع": 4, "الخامس": 5,
        "السادس": 6, "السابع": 7, "الثامن": 8, "التاسع": 9, "العاشر": 10,
        "الحادي عشر": 11, "الثاني عشر": 12, "الثالث عشر": 13, "الرابع عشر": 14,
        "الخامس عشر": 15, "السادس عشر": 16, "السابع عشر": 17, "الثامن عشر": 18,
        "التاسع عشر": 19, "العشرين": 20, "الأولى": 1, "الثانية": 2
    }
    for k, v in mapping.items():
        if k in text: return v
    m = re.search(r'\d+', text)
    if m: return int(m.group(0))
    return None

def build_split_grid(vocab_chunk, irab_html):
    html = ['<div class="split-grid mb-1mm">']
    
    # Vocab Column
    html.append('<div class="w-50pct">')
    html.append('<div class="content-block mb-0">')
    html.append('<div class="block-header bg-accent p-0 text-xs">')
    html.append('<span>المفردات والشرح والبلاغة</span>')
    html.append('</div>')
    html.append('<div class="block-body p-0 text-xs">')
    if vocab_chunk:
        html.append('<ul class="structured-list">')
        for text in vocab_chunk:
            # text is already formatted or we just wrap it
            # actually we extracted it as HTML text string from bs4
            html.append(f'<li>{text}</li>')
        html.append('</ul>')
    html.append('</div>')
    html.append('</div>')
    html.append('</div>')
    
    # Irab Column
    html.append('<div class="w-50pct">')
    html.append('<div class="content-block mb-0">')
    html.append('<div class="block-header p-0 text-xs">')
    html.append('<span>الإعراب</span>')
    html.append('</div>')
    html.append('<div class="block-body p-0 text-xs">')
    if irab_html:
        html.append('<ul class="structured-list">')
        html.append(f'<li><span class="marker">•</span><span>{irab_html}</span></li>')
        html.append('</ul>')
    html.append('</div>')
    html.append('</div>')
    html.append('</div>')
    
    html.append('</div>')
    return "\n".join(html)

def process_file(filepath):
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
            # We assume all vocab is in the first block due to corruption
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
                        
                    # get inner html without marker
                    marker = li.find(class_="marker")
                    if marker: marker.decompose()
                    current_chunk.append(li.decode_contents().strip())
                    if key: seen_keys.add(key)
                if current_chunk:
                    vocab_chunks.append(current_chunk)
                    
        # Truncate to num_poems
        vocab_chunks = vocab_chunks[:num_poems]
        
        # Pad if missing
        while len(vocab_chunks) < num_poems:
            vocab_chunks.append([])
            
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
        while len(irab_chunks) < num_poems:
            irab_chunks.append("")
            
        # Elements to remove
        elements_to_remove = []
        for p in poems:
            if p.get('id'): elements_to_remove.append((p.name, p.get('id')))
            
        for b in soup.find_all(class_="content-block"):
            hdr = b.find(class_="block-header")
            if not hdr: continue
            hdr_text = hdr.get_text()
            if any(x in hdr_text for x in ["دراسة", "تحليل", "المفردات", "الشرح", "تتمة التحليل", "إعراب", "الإعراب"]):
                if b.get('id'): elements_to_remove.append((b.name, b.get('id')))
                
        if irab_container:
            for box in irab_container.find_all(class_="irab-box"):
                if box.get('id'): elements_to_remove.append((box.name, box.get('id')))

        modified_html = raw_html
        insertions = []
        
        # Find insertions and remove slices
        for p in poems:
            if not p.get('id'): continue
            start, end = find_block_bounds(modified_html, p.name, p.get('id'))
            if start is not None:
                insertions.append(start)
                modified_html = remove_slice(modified_html, start, end)
                
        for tag, eid in elements_to_remove:
            # We already removed poem containers, so skip if eid is already processed
            # But the elements_to_remove has unique IDs, so it's fine.
            start, end = find_block_bounds(modified_html, tag, eid)
            if start is not None:
                modified_html = remove_slice(modified_html, start, end)
                
        modified_html = re.sub(r'<div class="w-full w-50pct"[^>]*>\s*</div>', '', modified_html)
        modified_html = re.sub(r'<div class="w-50pct"[^>]*>\s*</div>', '', modified_html)
        modified_html = re.sub(r'<div class="flex gap-2mm[^>]*>\s*</div>', '', modified_html)
        modified_html = re.sub(r'<div class="split-grid[^>]*>\s*</div>', '', modified_html)
        
        # Inject from bottom to top
        # Zip insertions with chunks
        items = list(zip(insertions, poems, vocab_chunks, irab_chunks))
        items.sort(key=lambda x: x[0], reverse=True)
        
        for pos, p_elem, v_chunk, i_chunk in items:
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
            
            sg_html = build_split_grid(v_chunk, i_chunk)
            
            full_chunk = clean_poem + "\n" + sg_html + "\n"
            modified_html = modified_html[:pos] + full_chunk + modified_html[pos:]
            
        if modified_html != raw_html:
            modified_html = re.sub(r'\n\s*\n\s*\n', '\n\n', modified_html)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(modified_html)
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
    process_file(os.path.join("pages", f))
