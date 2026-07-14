import re
import glob

# Arabic to English numerals
ar_to_en = str.maketrans('٠١٢٣٤٥٦٧٨٩', '0123456789')
en_to_ar = str.maketrans('0123456789', '٠١٢٣٤٥٦٧٨٩')

# Map page numbers to lesson numbers
page_to_lessons = {}
for f in glob.glob('backup_answers/98.*.html'):
    m = re.search(r'_p([0-9]+)_', f)
    if not m: continue
    page = int(m.group(1))
    
    text = open(f, encoding='utf-8').read()
    headers = re.findall(r'إِجَابَاتُ[^<]+', text)
    lessons = []
    for h in headers:
        m2 = re.search(r'الدَّرْسُ\s*([0-9]+)', h)
        if m2: lessons.append(int(m2.group(1)))
    
    if lessons:
        lessons = sorted(list(set(lessons)))
        page_to_lessons[page] = lessons

# Read TOC
with open('pages/00.3_TOC.html', encoding='utf-8') as f:
    content = f.read()

# Find all answer parts
def replacer(match):
    full_match = match.group(0)
    old_title = match.group(1)
    ar_page = match.group(3) # Group 3 is the page number
    
    en_page = int(ar_page.translate(ar_to_en))
    lessons = page_to_lessons.get(en_page, [])
    
    if not lessons:
        return full_match
    
    # Generate Arabic representation of lessons
    # User example: اجابات الدرس 6 و 7
    if len(lessons) > 2:
        # e.g. 16 و 17 و 18
        lessons_str = " وَ ".join(str(l) for l in lessons)
        new_title = f"إِجَابَاتُ الدُّرُوسِ {lessons_str}".translate(en_to_ar)
    elif len(lessons) == 2:
        new_title = f"إِجَابَاتُ الدَّرْسِ {lessons[0]} وَ {lessons[1]}".translate(en_to_ar)
    else:
        new_title = f"إِجَابَاتُ الدَّرْسِ {lessons[0]}".translate(en_to_ar)
        
    return full_match.replace(old_title, new_title)

pattern = re.compile(r'(مُلْحَقُ الْإِجَابَاتِ\s*-\s*مُلْحَقُ الْإِجَابَاتِ\s*-\s*جُزْءٌ\s*[0-9]+)(</td>\s*<td[^>]*>)([٠-٩]+)</td>')

new_content = pattern.sub(replacer, content)

with open('pages/00.3_TOC.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated 00.3_TOC.html")
