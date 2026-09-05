import os
import glob
import re
from bs4 import BeautifulSoup
import traceback

def process_from_backup_v2(target_file):
    try:
        m = re.search(r'page_(\d+)', target_file)
        if not m: return
        page_num = m.group(1)
        
        backups = glob.glob(f"pages/temp/lessons/page_{page_num}_*.html")
        if not backups: return
        backup_file = backups[0]
        
        with open(backup_file, "r", encoding="utf-8") as f:
            raw_html = f.read()
            
        soup = BeautifulSoup(raw_html, "html.parser")
        
        poems = soup.find_all(class_="poem-container")
        if not poems: return
            
        poems_data = []
        current_poem = None
        
        # Traverse to collect data
        for div in soup.find_all("div"):
            classes = div.get("class", [])
            if not isinstance(classes, list): classes = [classes]
                
            if "poem-container" in classes:
                current_poem = {'poem': div, 'vocab_items': [], 'irab_items': []}
                poems_data.append(current_poem)
                
            elif "content-block" in classes and current_poem:
                hdr = div.find(class_="block-header")
                if hdr and any(x in hdr.get_text() for x in ["دراسة", "تحليل", "المفردات", "الشرح"]):
                    body = div.find(class_="block-body")
                    if body:
                        for p in body.find_all("p"):
                            current_poem['vocab_items'].append(f'<li>{p.decode_contents().strip()}</li>')
                            
            elif "irab-box" in classes and current_poem:
                word = div.find(class_="irab-word")
                details = div.find(class_="irab-details")
                if word and details:
                    w_text = word.decode_contents().strip()
                    if w_text.endswith(":"): w_text = w_text[:-1].strip()
                    d_text = details.decode_contents().strip()
                    current_poem['irab_items'].append(f'<li><span class="marker">•</span><span class="text-accent font-bold">{w_text}:</span> <span>{d_text}</span></li>')

        # Generate new blocks
        new_blocks = []
        for pd in poems_data:
            p_elem = pd['poem']
            
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
            
            vocab_html = ""
            if pd['vocab_items']:
                vocab_html = '<ul class="structured-list">\n' + "\n".join(pd['vocab_items']) + '\n</ul>'
            irab_html = ""
            if pd['irab_items']:
                irab_html = '<ul class="structured-list">\n' + "\n".join(pd['irab_items']) + '\n</ul>'
                
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

        # We will reconstruct the page entirely by copying the backup file,
        # and replacing the original overarching container with our new blocks.
        first_poem = poems[0]
        container = first_poem
        
        # Determine the top-level container holding all poems.
        parent = first_poem.parent
        if parent and "w-full" in parent.get("class", []):
            if parent.parent and "split-grid" in parent.parent.get("class", []):
                container = parent.parent
            else:
                container = parent
                
        # Find exact bound in raw_html
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

        c_start, c_end = None, None
        c_id = container.get("id")
        if c_id:
            c_start, c_end = find_bound(container.name, c_id)
            
        # If the container has no ID, or we couldn't find it, we fallback to finding the first poem and the last irab block.
        if c_start is None:
            c_start, _ = find_bound(first_poem.name, first_poem.get("id"))
            
            last_pd = poems_data[-1]
            last_elem = last_pd['poem']
            
            # Find the last irab-box or content-block for the last poem
            # We can search in BS4:
            found_last = False
            for div in soup.find_all("div"):
                if div == last_elem: found_last = True
                if not found_last: continue
                # we are after the last poem
                # if we encounter another poem-container, break
                if "poem-container" in div.get("class", []) and div != last_elem: break
                if "irab-box" in div.get("class", []): last_elem = div
                
            _, c_end = find_bound(last_elem.name, last_elem.get("id"))
            
        if c_start is None or c_end is None:
            print(f"Could not find bounds for {target_file}")
            return
            
        html_before = raw_html[:c_start]
        html_after = raw_html[c_end:]
        
        final_html = html_before + "\n" + "\n".join(new_blocks) + "\n" + html_after
        final_html = re.sub(r'\n\s*\n\s*\n', '\n\n', final_html)
        
        out_path = os.path.join("pages", target_file)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(final_html)
        print(f"Successfully processed {target_file} from backup {backup_file}")
        
    except Exception as e:
        print(f"Error on {target_file}: {e}")
        traceback.print_exc()

TARGET_FILES = [
"044.0_n088_page_108.html",
"045.0_n089_page_109.html",
"108.0_n152_page_171.html"
]

for f in TARGET_FILES:
    process_from_backup_v2(f)
