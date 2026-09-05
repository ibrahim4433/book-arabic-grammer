import os
import re
from bs4 import BeautifulSoup, Comment
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

def extract_vocab_items(block):
    items = []
    for p in block.find_all("p"):
        strong = p.find(["strong", "b"])
        if strong:
            key = strong.decode_contents().strip()
            if key.endswith(":"): key = key[:-1].strip()
            strong.extract()
            val = p.decode_contents().strip()
            if val.startswith(":"): val = val[1:].strip()
            items.append((key, val))
            continue
            
        span = p.find("span", class_=re.compile(r"text-accent|font-bold"))
        if span:
            key = span.decode_contents().strip()
            if key.endswith(":"): key = key[:-1].strip()
            span.extract()
            val = p.decode_contents().strip()
            if val.startswith(":"): val = val[1:].strip()
            items.append((key, val))
            continue
            
        text = p.decode_contents().strip()
        if text:
            items.append(("", text))
            
    for li in block.find_all("li"):
        title_tag = li.find(["strong", "b"]) or li.find("span", class_=re.compile("text-accent|font-bold|highlight"))
        if title_tag:
            key = title_tag.decode_contents().strip()
            if key.endswith(":"): key = key[:-1].strip()
            title_tag.extract()
            marker = li.find(class_="marker")
            if marker: marker.extract()
            val = li.decode_contents().strip()
            if val.startswith(":"): val = val[1:].strip()
            items.append((key, val))
        else:
            marker = li.find(class_="marker")
            if marker: marker.extract()
            val = li.decode_contents().strip()
            if val:
                items.append(("", val))
                
    return items

def extract_irab_items(container):
    items = []
    boxes = container.find_all(class_="irab-box")
    if boxes:
        for box in boxes:
            word_tag = box.find(class_="irab-word")
            details_tag = box.find(class_="irab-details")
            if word_tag and details_tag:
                word = word_tag.decode_contents().strip()
                details = details_tag.decode_contents().strip()
                if word.endswith(":"): word = word[:-1].strip()
                items.append((word, details))
        return items
            
    tables = container.find_all("table", class_="dense-table")
    if tables:
        for table in tables:
            for row in table.find_all("tr"):
                cells = row.find_all(["td", "th"])
                if len(cells) >= 2:
                    word = cells[0].decode_contents().strip()
                    details = cells[1].decode_contents().strip()
                    if word.endswith(":"): word = word[:-1].strip()
                    items.append((word, details))
        return items
                
    ul = container.find("ul", class_="structured-list")
    if ul:
        for li in ul.find_all("li"):
            marker = li.find(class_="marker")
            if marker: marker.extract()
            text = li.decode_contents().strip()
            if text:
                items.append(("", text))
                
    return items

def get_index(text):
    mapping = {
        "الأول": 1, "الثاني": 2, "الثالث": 3, "الرابع": 4, "الخامس": 5,
        "السادس": 6, "السابع": 7, "الثامن": 8, "التاسع": 9, "العاشر": 10,
        "الحادي عشر": 11, "الثاني عشر": 12, "الثالث عشر": 13, "الرابع عشر": 14,
        "الخامس عشر": 15, "السادس عشر": 16, "السابع عشر": 17, "الثامن عشر": 18,
        "التاسع عشر": 19, "العشرين": 20, "الأولى": 1, "الثانية": 2
    }
    for k, v in mapping.items():
        if k in text:
            return v
    # Try digits
    m = re.search(r'\d+', text)
    if m:
        return int(m.group(0))
    return None

def build_split_grid(vocab_items, irab_items):
    html = ['<div class="split-grid mb-1mm">']
    
    html.append('<div class="w-50pct">')
    html.append('<div class="content-block mb-0">')
    html.append('<div class="block-header bg-accent p-0 text-xs">')
    html.append('<span>المفردات والشرح والبلاغة</span>')
    html.append('</div>')
    html.append('<div class="block-body p-0 text-xs">')
    if vocab_items:
        html.append('<ul class="structured-list">')
        for key, val in vocab_items:
            if key:
                html.append(f'<li><span class="marker">•</span><span class="text-accent font-bold">{key}:</span> <span>{val}</span></li>')
            else:
                html.append(f'<li><span class="marker">•</span><span>{val}</span></li>')
        html.append('</ul>')
    html.append('</div>')
    html.append('</div>')
    html.append('</div>')
    
    html.append('<div class="w-50pct">')
    html.append('<div class="content-block mb-0">')
    html.append('<div class="block-header p-0 text-xs">')
    html.append('<span>الإعراب</span>')
    html.append('</div>')
    html.append('<div class="block-body p-0 text-xs">')
    if irab_items:
        html.append('<ul class="structured-list">')
        smashed_parts = []
        for key, val in irab_items:
            if key:
                smashed_parts.append(f"{key}: {val}")
            else:
                smashed_parts.append(val)
        full_text = " ".join(smashed_parts)
        if full_text.strip():
            html.append(f'<li><span class="marker">•</span><span>{full_text}</span></li>')
        html.append('</ul>')
    html.append('</div>')
    html.append('</div>')
    html.append('</div>')
    
    html.append('</div>')
    return "\n".join(html)

def remove_slice(raw_html, start, end):
    return raw_html[:start] + (" " * (end - start)) + raw_html[end:]

def process_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            raw_html = f.read()
            
        soup = BeautifulSoup(raw_html, "html.parser")
        
        poems = []
        poem_idx = 1
        for pc in soup.find_all(class_="poem-container"):
            idx = None
            hdr = pc.find(class_="poem-header")
            if hdr:
                idx = get_index(hdr.get_text())
            else:
                prev = pc.previous_sibling
                while prev:
                    if isinstance(prev, Comment):
                        idx = get_index(str(prev))
                        if idx: break
                    prev = prev.previous_sibling
            
            if not idx:
                idx = poem_idx
            
            # ensure no duplicates
            while idx in [p['index'] for p in poems]:
                idx += 1
            poem_idx = idx + 1
                
            poems.append({'index': idx, 'element': pc, 'id': pc.get('id')})

        vocab_blocks = {}
        irab_blocks = {}
        elements_to_remove = []
        
        last_idx = 1
        blocks = soup.find_all(class_="content-block")
        for b in blocks:
            hdr = b.find(class_="block-header")
            if not hdr: continue
            hdr_text = hdr.get_text()
            
            is_vocab = any(x in hdr_text for x in ["دراسة", "تحليل", "المفردات", "الشرح", "تتمة التحليل", "إعراب مفردات"])
            is_irab = "إعراب" in hdr_text or "الإعراب" in hdr_text
            
            if not is_vocab and not is_irab:
                continue
                
            b_clone = BeautifulSoup(str(b), "html.parser").div
            for pc in b_clone.find_all(class_="poem-container"):
                pc.decompose()
                
            idx = get_index(hdr_text)
            if not idx:
                prev = b.parent if b.parent.name == 'div' and ('w-50pct' in b.parent.get('class', []) or 'split-grid' in b.parent.get('class', [])) else b
                prv = prev.previous_sibling
                while prv:
                    if isinstance(prv, Comment):
                        idx = get_index(str(prv))
                        if idx: break
                    prv = prv.previous_sibling
            if not idx:
                # find closest poem before it in document order
                # We can just increment last_idx for stacked stuff if we detect it
                idx = last_idx
            
            if is_vocab:
                if idx not in vocab_blocks: vocab_blocks[idx] = []
                vocab_blocks[idx].extend(extract_vocab_items(b_clone))
                last_idx = idx # update last seen
            if is_irab:
                if idx not in irab_blocks: irab_blocks[idx] = []
                irab_blocks[idx].extend(extract_irab_items(b_clone))
                # don't update last_idx for irab since it usually follows vocab
                
            if b.get('id'):
                elements_to_remove.append((b.name, b.get('id')))
                
        flexes = soup.find_all("div", class_="flex")
        last_flex_idx = 1
        for flex in flexes:
            if not flex.find_parents(class_="content-block") and flex.find(class_="irab-box"):
                idx = None
                prev = flex.previous_sibling
                while prev:
                    if isinstance(prev, Comment):
                        idx = get_index(str(prev))
                        if idx: break
                    if hasattr(prev, 'get') and prev.get('class') and 'content-block' in prev.get('class'):
                        hdr = prev.find(class_='block-header')
                        if hdr:
                            idx = get_index(hdr.get_text())
                            if idx: break
                    prev = prev.previous_sibling
                
                if not idx: 
                    idx = last_flex_idx
                else:
                    last_flex_idx = idx
                    
                for box in flex.find_all(class_="irab-box"):
                    if box.get('id'):
                        elements_to_remove.append((box.name, box.get('id')))
                        if idx not in irab_blocks: irab_blocks[idx] = []
                        irab_blocks[idx].extend(extract_irab_items(box))
                
                # if the flex itself has an id, we can remove it entirely, but if not we remove the boxes
                # Actually, the boxes are already added to elements_to_remove
                        
        if not poems:
            return

        modified_html = raw_html
        
        insertions = {}
        for p in poems:
            if not p['id']: continue
            start, end = find_block_bounds(modified_html, p['element'].name, p['id'])
            if start is not None:
                insertions[p['index']] = start
                modified_html = remove_slice(modified_html, start, end)
                
        for tag, eid in elements_to_remove:
            start, end = find_block_bounds(modified_html, tag, eid)
            if start is not None:
                modified_html = remove_slice(modified_html, start, end)
                
        modified_html = re.sub(r'<div class="w-full w-50pct"[^>]*>\s*</div>', '', modified_html)
        modified_html = re.sub(r'<div class="w-50pct"[^>]*>\s*</div>', '', modified_html)
        modified_html = re.sub(r'<div class="flex gap-2mm[^>]*>\s*</div>', '', modified_html)
        modified_html = re.sub(r'<div class="split-grid[^>]*>\s*</div>', '', modified_html)
        
        sorted_insertions = sorted(insertions.items(), key=lambda x: x[1], reverse=True)
        for idx, pos in sorted_insertions:
            p_elem = next(p['element'] for p in poems if p['index'] == idx)
            
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
            
            v_items = vocab_blocks.get(idx, [])
            i_items = irab_blocks.get(idx, [])
            sg_html = build_split_grid(v_items, i_items)
            
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
"011.2_n028_الصورة_البيانية.html",
"016.1_n039_munada.html",
"018.0_n041_irab_jumal.html",
"018.1_n042_irab_jumal.html",
"018.2_n043_irab_jumal.html",
"022.2_n051_mubtada.html",
"022.3_n052_mubtada.html",
"026.0_n056_التوكيد.html",
"029.1_n060_follow.html",
"029.2_n061_follow.html",
"030.0_n062_mansubat.html",
"030.1_n063_mansubat.html",
"030.3_n065_mansubat.html",
"030.4_n066_mansubat.html",
"035.2_n078_المصادر.html",
"044.0_n088_page_108.html",
"045.0_n089_page_109.html",
"046.0_n090_page_110.html",
"047.0_n091_page_111.html",
"048.0_n092_page_112.html",
"049.0_n093_page_113.html",
"051.0_n095_page_115.html",
"057.0_n101_page_121.html",
"063.0_n107_page_127.html",
"064.0_n108_page_128.html",
"065.0_n109_page_129.html",
"085.0_n129_page_149.html",
"096.0_n140_page_160.html",
"108.0_n152_page_171.html",
"110.05_n154a_page_173_cont.html",
"118.0_n162_page_181.html",
"120.05_n164a_page_183_cont.html",
"129.0_n173_page_192.html",
"133.0_n177_page_196.html",
"170.0_n214_page_233.html",
"171.0_n215_page_234.html",
"172.0_n216_page_235.html",
"178.0_n222_page_241.html",
"181.0_n225_page_244.html",
"189.0_n233_page_252.html",
"194.0_n238_page_257.html",
"195.0_n239_page_258.html",
"196.05_n240a_page_259_cont.html",
"211.0_n255_page_274.html",
"212.0_n256_page_275.html",
"213.0_n257_page_276.html",
"221.0_n265_page_284.html",
"222.0_n266_page_285.html",
"223.0_n267_page_286.html",
"224.0_n268_page_287.html",
"225.0_n269_page_288.html",
"226.0_n270_page_289.html",
"227.05_n271a_page_290_cont.html",
"233.0_n277_page_296.html",
"236.0_n280_page_299.html",
"237.0_n281_page_300.html",
"238.0_n282_page_301.html"
]

for f in TARGET_FILES:
    process_file(os.path.join("pages", f))
