import glob
import re
from bs4 import BeautifulSoup, Tag

def smash_irab_table(table_tag):
    # This function converts an I'rab <table class="dense-table"> to smashed text
    smashed_text = []
    rows = table_tag.find_all('tr')
    for row in rows:
        cells = row.find_all(['td', 'th'])
        if len(cells) == 2:
            # Preserve the highlight classes inside the first cell if any
            first_col_html = cells[0].decode_contents().strip()
            # If the first cell has a span with highlight, we keep it
            # But we might need to make sure there's no block elements.
            second_col_text = cells[1].get_text(separator=' ', strip=True)
            # Combine them
            # Check if first_col_html already has a colon
            colon = "" if ":" in first_col_html or "：" in first_col_html else ": "
            smashed_text.append(f"{first_col_html}{colon}{second_col_text}")
    
    if not smashed_text:
        return None
        
    ul_tag = soup.new_tag("ul")
    ul_tag['class'] = "structured-list"
    li_tag = soup.new_tag("li")
    
    # Create the marker
    marker_span = soup.new_tag("span")
    marker_span['class'] = "marker"
    marker_span.string = "•"
    li_tag.append(marker_span)
    
    # Create the text span
    # Since we have HTML in first_col_html, we can't just use .string
    text_span = soup.new_tag("span")
    # We join them with a space
    combined_html = " ".join(smashed_text)
    
    # We need to parse this combined_html to append it to text_span
    temp_soup = BeautifulSoup(combined_html, "html.parser")
    for child in temp_soup.contents:
        text_span.append(child)
        
    li_tag.append(text_span)
    ul_tag.append(li_tag)
    return ul_tag

# Let's fix the 88 files directly!
with open("files_to_revert.txt", "r") as f:
    files = [line.strip() for line in f if line.strip()]

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
                        # Strip standard verse numbers
                        new_text = re.sub(r'^[\s\u200B]*[\u0660-\u06690-9]+[\s\u200B]*[-ـ][\s\u200B]*', '', str(first_text))
                        if new_text != str(first_text):
                            first_text.replace_with(new_text)
                            modified = True
                            
        # 2. Find ALL split grids, and if they contain an I'rab block with a table, smash the table!
        split_grids = soup.find_all(class_="split-grid")
        for sg in split_grids:
            irab_blocks = sg.find_all(class_="content-block")
            for block in irab_blocks:
                header = block.find(class_="block-header")
                if header and ("إعراب" in header.get_text() or "الإعراب" in header.get_text()):
                    # Find the table
                    table = block.find("table", class_="dense-table")
                    if table:
                        new_ul = smash_irab_table(table)
                        if new_ul:
                            table.replace_with(new_ul)
                            modified = True
                            
        # Now, we need to prettify ONLY the ugly single-line split-grids we injected.
        # It's hard to selectively prettify in BeautifulSoup.
        # We will write the file, then use a regex replacement to add newlines to our specific tags.
        if modified:
            html_out = str(soup)
            
            # Format our injected tags:
            # <div class="split-grid mb-1mm"><div class="w-50pct" id="b93579"><div class="content-block mb-1mm" id="b30784">
            # We want:
            # <div class="split-grid mb-1mm">
            # <div class="w-50pct" ...>
            # <div class="content-block ...>
            html_out = html_out.replace('<div class="split-grid mb-1mm"><div class="w-50pct"', '<div class="split-grid mb-1mm">\n<div class="w-50pct"')
            html_out = re.sub(r'(<div class="w-50pct"[^>]*>)<div class="content-block"', r'\1\n<div class="content-block"', html_out)
            html_out = re.sub(r'</div></div><div class="w-50pct"', r'</div>\n</div>\n<div class="w-50pct"', html_out)
            html_out = html_out.replace('</div></div></div>', '</div>\n</div>\n</div>')
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html_out)
            print(f"Fixed {filepath}")
            
    except Exception as e:
        print(f"Error on {filepath}: {e}")

