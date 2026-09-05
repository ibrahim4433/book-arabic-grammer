import glob
import re
from bs4 import BeautifulSoup

def process_all():
    files = sorted(glob.glob("pages/*.html"))
    for filepath in files:
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                raw = f.read()
                
            soup = BeautifulSoup(raw, "html.parser")
            modified = False
            
            # 1. Remove numbering from single-verse poem containers
            poems = soup.find_all(class_="poem-container")
            for p in poems:
                lines = p.find_all(class_="poem-line")
                if len(lines) == 1:
                    hemis = lines[0].find_all(class_="hemistich")
                    if hemis:
                        hemi1 = hemis[0]
                        # Find first text node
                        first_text = None
                        for desc in hemi1.descendants:
                            if isinstance(desc, str) and desc.strip():
                                first_text = desc
                                break
                        if first_text:
                            # Strip standard verse numbers like ١- 
                            new_text = re.sub(r'^[\s\u200B]*[\u0660-\u06690-9]+[\s\u200B]*[-ـ][\s\u200B]*', '', str(first_text))
                            if new_text != str(first_text):
                                first_text.replace_with(new_text)
                                modified = True
            
            # 2. Smash any remaining I'rab tables inside split-grids
            split_grids = soup.find_all(class_="split-grid")
            for sg in split_grids:
                irab_blocks = sg.find_all(class_="content-block")
                for block in irab_blocks:
                    header = block.find(class_="block-header")
                    if header and ("إعراب" in header.get_text() or "الإعراب" in header.get_text()):
                        table = block.find("table", class_="dense-table")
                        if table:
                            # Smasher logic
                            smashed_text = []
                            rows = table.find_all('tr')
                            for row in rows:
                                cells = row.find_all(['td', 'th'])
                                if len(cells) == 2:
                                    first_col_html = cells[0].decode_contents().strip()
                                    second_col_text = cells[1].get_text(separator=' ', strip=True)
                                    # Since we fix double colons later, we just use one colon here if we think it's needed
                                    # Actually we can just add no colon and let the text handle it, or add one and clean it up.
                                    smashed_text.append(f"{first_col_html} : {second_col_text}")
                            
                            if smashed_text:
                                ul_tag = soup.new_tag("ul")
                                ul_tag['class'] = "structured-list"
                                li_tag = soup.new_tag("li")
                                marker_span = soup.new_tag("span")
                                marker_span['class'] = "marker"
                                marker_span.string = "•"
                                li_tag.append(marker_span)
                                text_span = soup.new_tag("span")
                                combined_html = " ".join(smashed_text)
                                temp_soup = BeautifulSoup(combined_html, "html.parser")
                                for child in temp_soup.contents:
                                    text_span.append(child)
                                li_tag.append(text_span)
                                ul_tag.append(li_tag)
                                table.replace_with(ul_tag)
                                modified = True
                                
            # 3. Clean up double colons
            if modified or True:
                # To be safe, we just convert the soup to string and do a global regex replace for the double colons
                # Since we don't want to parse again unless modified, actually let's just do it on raw string.
                html_out = str(soup)
                
                # Fix double colons in highlighting
                # For example: <span class="highlight-red">حَسِبْتَهَا:</span> : فِعْلٌ
                html_out = html_out.replace('</span>: :', '</span>:')
                html_out = html_out.replace('</span> : :', '</span> :')
                html_out = html_out.replace('</span>:  :', '</span>:')
                # Also just general:
                html_out = html_out.replace(': :', ':')
                html_out = html_out.replace(':  :', ':')
                
                # Re-apply the newlines formatting in case it was missed
                html_out = html_out.replace('<div class="split-grid mb-1mm"><div class="w-50pct"', '<div class="split-grid mb-1mm">\n<div class="w-50pct"')
                html_out = re.sub(r'(<div class="w-50pct"[^>]*>)<div class="content-block"', r'\1\n<div class="content-block"', html_out)
                html_out = re.sub(r'</div></div><div class="w-50pct"', r'</div>\n</div>\n<div class="w-50pct"', html_out)
                html_out = html_out.replace('</div></div></div>', '</div>\n</div>\n</div>')
                
                # Check if it actually changed
                if html_out != raw:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(html_out)
                    print(f"Fixed {filepath}")
                    
        except Exception as e:
            print(f"Error on {filepath}: {e}")

if __name__ == "__main__":
    process_all()
