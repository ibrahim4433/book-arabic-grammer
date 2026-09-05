import glob
from bs4 import BeautifulSoup
import re

files = glob.glob("pages/*.html")
fixed_count = 0

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
        
    soup = BeautifulSoup(html, "html.parser")
    modified = False
    
    # 1. Remove poem dividers containing dots
    for divider in soup.find_all(class_="poem-divider"):
        if "..." in divider.get_text() or ".." in divider.get_text():
            divider.extract()
            modified = True
            
    # 2. Look for standalone dots between hemistichs
    for line in soup.find_all(class_="poem-line"):
        for child in list(line.children):
            if child.name is None and ("..." in child or ".." in child):
                child.extract()
                modified = True
                
        # Some dots might be inside spans
        for span in line.find_all("span"):
            if "..." in span.get_text() or ".." in span.get_text():
                if "hemistich" not in span.parent.get("class", []): # don't delete text inside the poem verse itself if they are part of the verse, wait, actually let's just be careful not to delete legitimate ellipses in poetry. But the user said "between the verses". So they mean between the hemistichs.
                    span.extract()
                    modified = True

    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(str(soup))
        fixed_count += 1
        
print(f"Removed dots in {fixed_count} files.")
