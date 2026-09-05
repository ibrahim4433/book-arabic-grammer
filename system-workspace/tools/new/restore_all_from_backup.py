import os
import glob
import re
from bs4 import BeautifulSoup
import traceback

def process_from_backup_v2(target_file):
    try:
        m = re.search(r'_n(\d+[a-z]?)_', target_file)
        if not m:
            print(f"Could not extract nXXX from {target_file}")
            return
        n_num = m.group(1)
        
        # We need to find the backup file. The backup files are in `pages/temp/lessons/`.
        # They are usually named `page_{num}_*.html`.
        # But `target_file` might not have `page_`. E.g., `016.1_n039_munada.html`.
        # How do we map it? The page number is what?
        # The user's backups have `page_{page_num}`.
        # Let's extract page num if it exists.
        m_page = re.search(r'page_(\d+)', target_file)
        if m_page:
            page_num = m_page.group(1)
            backups = glob.glob(f"pages/temp/lessons/page_{page_num}_*.html")
            # If not found, try matching by `nXXX` instead? No, backup files don't have nXXX.
            # Some backups might be in `archive/` or other dirs?
        else:
            # If there is no page number in the target file, how do we find the backup?
            # We can search ALL backups for one that contains the content of this file?
            # Or we can just try to find the backup by searching for a file in `pages/temp/lessons/` that has the same text?
            print(f"No page number in {target_file}, skipping for now")
            return
            
        if not backups:
            print(f"No backup found for {target_file}")
            return
        backup_file = backups[0]
        
        with open(backup_file, "r", encoding="utf-8") as f:
            raw_html = f.read()
            
        soup = BeautifulSoup(raw_html, "html.parser")
        
        poems = soup.find_all(class_="poem-container")
        if not poems:
            print(f"No poems found in {backup_file}")
            return
            
        poems_data = []
        current_poem = None
        
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

        new_blocks = []
        for pd in poems_data:
            p_elem = pd['poem']
            
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

        first_poem = poems[0]
        container = first_poem
        
        parent = first_poem.parent
        if parent and "w-full" in parent.get("class", []):
            if parent.parent and "split-grid" in parent.parent.get("class", []):
                container = parent.parent
            else:
                container = parent
                
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
            
        if c_start is None:
            c_start, _ = find_bound(first_poem.name, first_poem.get("id"))
            
            last_pd = poems_data[-1]
            last_elem = last_pd['poem']
            
            found_last = False
            for div in soup.find_all("div"):
                if div == last_elem: found_last = True
                if not found_last: continue
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
        print(f"Successfully restored {target_file} from {backup_file}")
        
    except Exception as e:
        print(f"Error on {target_file}: {e}")
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
    process_from_backup_v2(f)
