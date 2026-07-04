import glob
from bs4 import BeautifulSoup
import re
import os

ar_to_en = str.maketrans('٠١٢٣٤٥٦٧٨٩', '0123456789')
en_to_ar = str.maketrans('0123456789', '٠١٢٣٤٥٦٧٨٩')

files = sorted([f for f in glob.glob('pages/*.html') if re.match(r'pages/\d{2}\.', f)])
lesson_files = [f for f in files if not f.startswith('pages/00.') and not f.startswith('pages/98.') and not f.startswith('pages/99.')]

current_lesson_num = 0
last_seen_title = ""
unique_lessons = [] # will store (new_num, title, first_file)

for f in lesson_files:
    with open(f, encoding='utf-8') as file:
        content = file.read()
    soup = BeautifulSoup(content, 'html.parser')
    
    h1 = soup.find('h1', class_='header-title')
    num_div = soup.find('div', class_='lesson-number')
    
    if h1 and num_div:
        title = h1.get_text(strip=True)
        # Clean up weird titles if any
        title = re.sub(r'^[0-9\.]+\s*-\s*', '', title)
        title = title.replace('-', '').strip()
        
        if title != last_seen_title:
            current_lesson_num += 1
            last_seen_title = title
            unique_lessons.append((current_lesson_num, title, f))
            
        ar_num = str(current_lesson_num).translate(en_to_ar)
        
        if num_div.get_text(strip=True) != ar_num:
            num_div.string = ar_num
            # Save file
            with open(f, 'w', encoding='utf-8') as file:
                file.write(str(soup))
            print(f"Updated {f} -> Lesson {ar_num} ({title})")
            
        # Also clean up the title in the h1 if it had numbers
        if h1.get_text(strip=True) != title:
            h1.string = title
            with open(f, 'w', encoding='utf-8') as file:
                file.write(str(soup))

print(f"Total unique lessons: {current_lesson_num}")

# Save the mapping so we can build the TOC later
import json
with open('lesson_mapping.json', 'w', encoding='utf-8') as out:
    json.dump(unique_lessons, out, ensure_ascii=False, indent=2)
