import os, glob, re
from pathlib import Path
from bs4 import BeautifulSoup

def to_arabic_indic(text):
    english_to_arabic = {'0':'٠','1':'١','2':'٢','3':'٣','4':'٤','5':'٥','6':'٦','7':'٧','8':'٨','9':'٩'}
    return ''.join(english_to_arabic.get(c, c) for c in str(text))

pages_dir = Path('pages')

all_files = sorted(glob.glob('pages/*.html'))
lesson_files = [f for f in all_files if "TEMPLATE_" not in f and not os.path.basename(f).startswith('00.') and not os.path.basename(f).startswith('98.')]

for file in lesson_files:
    basename = os.path.basename(file)
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    # Extract info from filename: XX.X_pYY_TITLE.html
    match = re.match(r'([0-9]+)\.[0-9]+_p([0-9]+)_(.*)\.html', basename)
    if not match:
        continue
        
    base_lesson_number = match.group(1) # e.g. "01"
    title_from_filename = match.group(3)
    
    changed = False
    
    # 1. Fix lesson number in the header
    ln_div = soup.find('div', class_='lesson-number')
    if ln_div:
        current_ln = ln_div.get_text(strip=True)
        new_ln = to_arabic_indic(base_lesson_number)
        if current_ln != new_ln:
            ln_div.string = new_ln
            changed = True
            
    # 2. Fix the header title
    h1_title = soup.find('h1', class_='header-title')
    if h1_title:
        current_title = h1_title.get_text(strip=True)
        if current_title != title_from_filename:
            h1_title.string = title_from_filename
            changed = True
            
    # 3. Fix the <title> tag
    title_tag = soup.find('title')
    if title_tag:
        if title_tag.get_text(strip=True) != title_from_filename:
            title_tag.string = title_from_filename
            changed = True
            
    # 4. Fix the lesson details level (usually "المستوى التأسيسي")
    header_right = soup.find('div', class_='header-section right')
    if header_right:
        details_div = header_right.find('div', class_='lesson-details')
        if details_div:
            divs = details_div.find_all('div')
            if len(divs) >= 2:
                # Level
                if divs[0].get_text(strip=True) != "المستوى التأسيسي":
                    divs[0].string = "المستوى التأسيسي"
                    changed = True
                
                # We can put a short subject name in the second div.
                # Usually it's "النَّحْوُ" or similar. Let's extract the main topic.
                topic = re.sub(r'\(الْجُزْءُ.*\)', '', title_from_filename).strip()
                if divs[1].get_text(strip=True) != topic:
                    divs[1].string = topic
                    changed = True

    if changed:
        with open(file, 'w', encoding='utf-8') as out:
            out.write(str(soup))
            
# Do the same for 98.* answers
answer_files = sorted(glob.glob('pages/98.*.html'))
for file in answer_files:
    basename = os.path.basename(file)
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    changed = False
    
    ln_div = soup.find('div', class_='lesson-number')
    if ln_div:
        new_ln = "٩٨"
        if ln_div.get_text(strip=True) != new_ln:
            ln_div.string = new_ln
            changed = True
            
    header_right = soup.find('div', class_='header-section right')
    if header_right:
        details_div = header_right.find('div', class_='lesson-details')
        if details_div:
            divs = details_div.find_all('div')
            if len(divs) >= 2:
                if divs[0].get_text(strip=True) != "المستوى التأسيسي":
                    divs[0].string = "المستوى التأسيسي"
                    changed = True
                if divs[1].get_text(strip=True) != "مُلْحَقُ الْإِجَابَاتِ":
                    divs[1].string = "مُلْحَقُ الْإِجَابَاتِ"
                    changed = True
                    
    if changed:
        with open(file, 'w', encoding='utf-8') as out:
            out.write(str(soup))

print("Metadata fixed.")
