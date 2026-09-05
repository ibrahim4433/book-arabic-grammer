import os
import glob
import re
from bs4 import BeautifulSoup

def process_from_backup(target_file):
    # Extract page number
    m = re.search(r'page_(\d+)', target_file)
    if not m:
        print(f"Could not extract page number from {target_file}")
        return
    page_num = m.group(1)
    
    # Find backup file
    backups = glob.glob(f"pages/temp/lessons/page_{page_num}_*.html")
    if not backups:
        print(f"No backup found for {target_file}")
        return
    backup_file = backups[0]
    
    with open(backup_file, "r", encoding="utf-8") as f:
        raw_html = f.read()
        
    soup = BeautifulSoup(raw_html, "html.parser")
    
    # Find all poem containers
    poems = soup.find_all(class_="poem-container")
    if not poems:
        print(f"No poems found in {backup_file}")
        return
        
    # The backup has `<div class="poem-container">` followed by `<div class="content-block">` (vocab)
    # followed by multiple `<div class="flex">` (irab) until the next poem.
    
    new_blocks = []
    
    for i, p_elem in enumerate(poems):
        # 1. Clean poem
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
        
        # 2. Find vocab
        vocab_html = ""
        vocab_block = p_elem.find_next_sibling(class_="content-block")
        if vocab_block:
            hdr = vocab_block.find(class_="block-header")
            if hdr and any(x in hdr.get_text() for x in ["دراسة", "تحليل", "المفردات", "الشرح"]):
                # Convert the <p> tags into <li> tags for the structured-list
                body = vocab_block.find(class_="block-body")
                if body:
                    vocab_items = []
                    for p in body.find_all("p"):
                        vocab_items.append(f'<li>{p.decode_contents().strip()}</li>')
                    if vocab_items:
                        vocab_html = '<ul class="structured-list">\n' + "\n".join(vocab_items) + '\n</ul>'
                        
        # 3. Find irab
        irab_html = ""
        irab_items = []
        curr = vocab_block if vocab_block else p_elem
        while curr:
            curr = curr.find_next_sibling()
            if not curr: break
            if "poem-container" in curr.get("class", []): break
            if "content-block" in curr.get("class", []):
                # check if it's the next poem's vocab (shouldn't happen before the poem itself, but just in case)
                hdr = curr.find(class_="block-header")
                if hdr and any(x in hdr.get_text() for x in ["دراسة", "تحليل", "المفردات", "الشرح"]):
                    break
                    
            # If it's a flex container holding irab-boxes
            if "flex" in curr.get("class", []) and curr.find(class_="irab-box"):
                for box in curr.find_all(class_="irab-box"):
                    word = box.find(class_="irab-word")
                    details = box.find(class_="irab-details")
                    if word and details:
                        w_text = word.decode_contents().strip()
                        if w_text.endswith(":"): w_text = w_text[:-1].strip()
                        d_text = details.decode_contents().strip()
                        irab_items.append(f'<li><span class="marker">•</span><span class="text-accent font-bold">{w_text}:</span> <span>{d_text}</span></li>')
                        
        if irab_items:
            irab_html = '<ul class="structured-list">\n' + "\n".join(irab_items) + '\n</ul>'
            
        # 4. Build split-grid
        sg = []
        sg.append('<div class="split-grid mb-1mm">')
        sg.append('<div class="w-50pct">')
        sg.append('<div class="content-block mb-0">')
        sg.append('<div class="block-header bg-accent p-0 text-xs">')
        sg.append('<span>المفردات والشرح والبلاغة</span>')
        sg.append('</div>')
        sg.append('<div class="block-body p-0 text-xs">')
        sg.append(vocab_html)
        sg.append('</div></div></div>')
        sg.append('<div class="w-50pct">')
        sg.append('<div class="content-block mb-0">')
        sg.append('<div class="block-header p-0 text-xs">')
        sg.append('<span>الإعراب</span>')
        sg.append('</div>')
        sg.append('<div class="block-body p-0 text-xs">')
        sg.append(irab_html)
        sg.append('</div></div></div></div>')
        
        new_blocks.append(clean_poem + "\n" + "\n".join(sg))
        
    # Now inject into the file
    poem_pattern = re.compile(r'<div[^>]*class="[^"]*poem-container[^"]*"[^>]*>')
    m_start = poem_pattern.search(raw_html)
    if not m_start: return
    html_before = raw_html[:m_start.start()]
    
    # html_after is everything after the last irab block of the last poem.
    # We can find it similarly
    parent = poems[0].parent
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
            
    html_after = ""
    next_elem = last_corrupted_elem.find_next_sibling() if last_corrupted_elem else None
    
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
        if next_elem.get("id"):
            s, e = find_bound(next_elem.name, next_elem.get("id"))
            if s is not None: html_after = raw_html[s:]
        else:
            s_idx = raw_html.rfind("</section>")
            if s_idx != -1: html_after = raw_html[s_idx:]
    else:
        s_idx = raw_html.rfind("</section>")
        if s_idx != -1: html_after = raw_html[s_idx:]
        
    final_html = html_before + "\n".join(new_blocks) + "\n" + html_after
    final_html = re.sub(r'\n\s*\n\s*\n', '\n\n', final_html)
    
    out_path = os.path.join("pages", target_file)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(final_html)
    print(f"Successfully processed {target_file} from backup {backup_file}")

process_from_backup("044.0_n088_page_108.html")
