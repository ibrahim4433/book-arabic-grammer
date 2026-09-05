import os
from bs4 import BeautifulSoup

target_files = []
directory = "pages"

for filename in os.listdir(directory):
    if not filename.endswith(".html"):
        continue
        
    filepath = os.path.join(directory, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
        
    # We are looking for pages that have a poem-container
    if "poem-container" not in html:
        continue
        
    soup = BeautifulSoup(html, "html.parser")
    poems = soup.find_all(class_="poem-container")
    if not poems:
        continue
        
    # Check if they have I'rab or Vocab blocks that aren't already perfectly structured like page 162
    # Page 162 structure: split-grid -> w-50pct -> block-header "المفردات والشرح والبلاغة"
    # and w-50pct -> block-header "الإعراب"
    
    needs_restructure = False
    for poem in poems:
        # Check the next siblings or look at the whole file's blocks
        pass
        
    # A simpler way: If the file has 'دراسة البيت' or 'تحليل البيت' or 'إعراب مفردات'
    # or it has flex I'rab boxes outside a split-grid.
    headers = soup.find_all(class_="block-header")
    header_texts = [h.get_text(strip=True) for h in headers]
    
    has_bad_structure = False
    for text in header_texts:
        if "دراسة البيت" in text or "تحليل البيت" in text or "إعراب مفردات" in text or "إعراب جمل" in text:
            has_bad_structure = True
            break
            
    # Also check if it has stacked I'rab boxes (not in a single list)
    irab_boxes = soup.find_all(class_="irab-box")
    if irab_boxes:
        has_bad_structure = True

    if has_bad_structure:
        target_files.append(filename)

print(f"Found {len(target_files)} files needing restructure:")
for f in sorted(target_files):
    print(f)
