from bs4 import BeautifulSoup
import glob
import re

ar_to_en = str.maketrans('٠١٢٣٤٥٦٧٨٩', '0123456789')
en_to_ar = str.maketrans('0123456789', '٠١٢٣٤٥٦٧٨٩')

# Step 1: Collect and sort all 34 Answer entries from the backup files
entries = []
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
        entries.append((lessons, page))

# Sort by first lesson number
entries.sort(key=lambda x: x[0][0])

answer_blocks = []
for lessons, page in entries:
    if len(lessons) > 2:
        lessons_str = " وَ ".join(str(l) for l in lessons)
        title = f"إِجَابَاتُ الدُّرُوسِ {lessons_str}".translate(en_to_ar)
    elif len(lessons) == 2:
        title = f"إِجَابَاتُ الدَّرْسِ {lessons[0]} وَ {lessons[1]}".translate(en_to_ar)
    else:
        title = f"إِجَابَاتُ الدَّرْسِ {lessons[0]}".translate(en_to_ar)
    ar_page = str(page).translate(en_to_ar)
    answer_blocks.append((title, ar_page))

# Step 2: Read the current 00.3_TOC.html
with open('pages/00.3_TOC.html.bak', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')
tbody = soup.find('tbody')

# Collect actual lessons from the left side
left_lessons = []
for tr in tbody.find_all('tr'):
    tds = tr.find_all('td')
    if len(tds) >= 3:
        # Check if the left column is an answer (98) or a real lesson
        lesson_num = tds[0].get_text(strip=True)
        if lesson_num.translate(ar_to_en) != '98':
            # Store the 3 elements of the left column
            left_lessons.append([str(tds[0]), str(tds[1]), str(tds[2])])

# Create an empty tbody to rebuild
tbody.clear()

# Step 3: Rebuild the table rows
# We need max(len(left_lessons), len(answer_blocks)) rows.
# But wait! If we just put them all on the right, we will have 34 rows. 24 will have left lessons, 10 will have empty left sides.
# Wait, if we want to save space and keep it neat, we could put the remaining answers on the LEFT side of the extra rows!
# Let's see: left_lessons has 24 items. answer_blocks has 34 items.
# Row 1-24: Left = lesson, Right = Answer (1-24)
# Row 25-29: Left = Answer (25-29), Right = Answer (30-34)
# That's exactly 5 rows! 
# Let's do that to save vertical space and match the style!

# Let's build the rows
num_rows = 24 + 5 # 29 rows total
ans_idx = 0

for i in range(29):
    tr = soup.new_tag('tr')
    
    # --- LEFT SIDE ---
    if i < len(left_lessons):
        # Add actual lesson
        for td_str in left_lessons[i]:
            tr.append(BeautifulSoup(td_str, 'html.parser'))
    else:
        # Add an answer block on the left
        if ans_idx < len(answer_blocks):
            title, ar_page = answer_blocks[ans_idx]
            ans_idx += 1
            td1 = soup.new_tag('td', attrs={'class': 'text-center font-bold text-grey bg-grey-lighter'})
            td1.string = '٩٨'
            td2 = soup.new_tag('td', attrs={'class': 'font-bold bg-grey-lighter'})
            td2.string = title
            td3 = soup.new_tag('td', attrs={'class': 'text-center font-bold text-primary bg-grey-lighter'})
            td3.string = ar_page
            tr.append(td1)
            tr.append(td2)
            tr.append(td3)
        else:
            # Empty left block just in case
            td1 = soup.new_tag('td', attrs={'class': 'text-center font-bold text-grey'})
            td2 = soup.new_tag('td', attrs={'class': 'font-bold'})
            td3 = soup.new_tag('td', attrs={'class': 'text-center font-bold text-primary'})
            tr.append(td1); tr.append(td2); tr.append(td3)
            
    # --- SPACER ---
    spacer = soup.new_tag('td', attrs={'class': 'spacer-col'})
    tr.append(spacer)
    
    # --- RIGHT SIDE ---
    if ans_idx < len(answer_blocks):
        title, ar_page = answer_blocks[ans_idx]
        ans_idx += 1
        td1 = soup.new_tag('td', attrs={'class': 'text-center font-bold text-grey bg-grey-lighter'})
        td1.string = '٩٨'
        td2 = soup.new_tag('td', attrs={'class': 'font-bold bg-grey-lighter'})
        td2.string = title
        td3 = soup.new_tag('td', attrs={'class': 'text-center font-bold text-primary bg-grey-lighter'})
        td3.string = ar_page
        tr.append(td1)
        tr.append(td2)
        tr.append(td3)
    else:
        # Empty right block
        td1 = soup.new_tag('td', attrs={'class': 'text-center font-bold text-grey bg-grey-lighter'})
        td2 = soup.new_tag('td', attrs={'class': 'font-bold bg-grey-lighter'})
        td3 = soup.new_tag('td', attrs={'class': 'text-center font-bold text-primary bg-grey-lighter'})
        tr.append(td1); tr.append(td2); tr.append(td3)
        
    tbody.append(tr)

# Write back to file
with open('pages/00.3_TOC.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Successfully rebuilt 00.3_TOC.html")
