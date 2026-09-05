import os
import re
from bs4 import BeautifulSoup

unit_files = {
    "1": ("pages/037.0_n081_page_101.html", "pages/036.9_n081a_unit_1.html"),
    "2": ("pages/076.0_n120_page_140.html", "pages/075.9_n120a_unit_2.html"),
    "3": ("pages/090.0_n134_page_154.html", "pages/089.9_n134a_unit_3.html"),
    "4": ("pages/146.0_n190_page_209.html", "pages/145.9_n190a_unit_4.html"),
    "5": ("pages/164.0_n208_page_227.html", "pages/163.9_n208a_unit_5.html"),
    "6": ("pages/206.0_n250_page_269.html", "pages/205.9_n250a_unit_6.html")
}

template = """<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="utf-8"/>
    <title>Unit {unit_num}</title>
    <link href="../styles/main.css" rel="stylesheet"/>
</head>
<body>
<div class="force-new-page" style="display: flex; align-items: center; justify-content: center; height: 100vh;">
    <div class="text-center" style="width: 80%;">
        {content}
    </div>
</div>
</body>
</html>
"""

def extract_unit(unit_num, src_path, dst_path):
    print(f"Processing Unit {unit_num} from {src_path}")
    with open(src_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    
    # Try to find the block containing the unit title
    target_block = None
    for block in soup.find_all(class_="content-block"):
        if re.search(r'الوحدة|الوَحْدَة', block.get_text()):
            target_block = block
            break
            
    if not target_block:
        # Sometimes it's just a div or span, find the first parent block or just the element
        for elem in soup.find_all(['span', 'div', 'p']):
            if re.search(r'الوحدة|الوَحْدَة', elem.get_text()):
                if len(elem.get_text().strip()) < 100: # Not a huge block of text
                    target_block = elem.find_parent(class_="content-block")
                    if not target_block:
                        target_block = elem.find_parent("div")
                    break

    if target_block:
        # Increase font sizes and make it centered
        for tag in target_block.find_all(['span', 'p']):
            tag['class'] = tag.get('class', []) + ['text-title', 'font-bold']
            
        target_block['class'] = target_block.get('class', []) + ['border-none', 'bg-transparent', 'shadow-none']
        
        # Remove from source
        target_block.extract()
        
        # Write to dest
        html_out = template.format(unit_num=unit_num, content=str(target_block))
        with open(dst_path, "w", encoding="utf-8") as f:
            f.write(html_out)
            
        # Write back source
        with open(src_path, "w", encoding="utf-8") as f:
            f.write(str(soup))
            
        print(f"  Success: Extracted to {dst_path}")
    else:
        print(f"  Failed: Could not find Unit {unit_num} block")

for u, (src, dst) in unit_files.items():
    extract_unit(u, src, dst)
