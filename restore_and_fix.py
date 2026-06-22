import os, glob, re
from pathlib import Path
from bs4 import BeautifulSoup

def to_arabic_indic(text):
    english_to_arabic = {'0':'٠','1':'١','2':'٢','3':'٣','4':'٤','5':'٥','6':'٦','7':'٧','8':'٨','9':'٩'}
    return ''.join(english_to_arabic.get(c, c) for c in str(text))

arabic_parts = ["الْأَوَّلُ", "الثَّانِي", "الثَّالِثُ", "الرَّابِعُ", "الْخَامِسُ", "السَّادِسُ", "السَّابِعُ", "الثَّامِنُ", "التَّاسِعُ", "الْعَاشِرُ", "الْحَادِيَ عَشَرَ", "الثَّانِيَ عَشَرَ"]

pages_dir = Path('pages')

if os.path.exists('pages/99.0_blank_page2.html'):
    os.remove('pages/99.0_blank_page2.html')

all_files = sorted(glob.glob('pages/*.html'))
lesson_files = [f for f in all_files if "TEMPLATE_" not in f and not os.path.basename(f).startswith('00.') and not os.path.basename(f).startswith('98.')]

groups = {}
file_info = []

for file in lesson_files:
    basename = os.path.basename(file)
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # Authoritative title comes from <title> tag because it exists everywhere
    title_tag = soup.find('title')
    title = title_tag.get_text(strip=True) if title_tag else ""
    
    # Strip any leading numbers "16 - "
    title = re.sub(r'^[0-9]+\s*-\s*', '', title)
    
    base_title = title
    base_title = re.sub(r'\(.*?\)', '', base_title)
    base_title = re.sub(r'_(تابع|تتمة|تَتِمَّة|تَابِع|تَتِمَّةٌ)', '', base_title)
    base_title = re.sub(r'(تابع|تتمة|تَتِمَّة|تَابِع|تَتِمَّةٌ)', '', base_title)
    base_title = re.sub(r'الجزء\s+.*', '', base_title)
    base_title = re.sub(r'الْجُزْءُ\s+.*', '', base_title)
    base_title = base_title.replace('؟', '؟ ')
    base_title = re.sub(r'\s+', ' ', base_title).strip()
    
    if not base_title:
        # Fallback to filename prefix if somehow completely empty
        match = re.match(r'([0-9]+\.[0-9]+)', basename)
        base_title = match.group(1) if match else "بدون عنوان"
        
    group_key = re.sub(r'[\u064B-\u065F\u0670]', '', base_title).strip()
    
    if group_key not in groups:
        groups[group_key] = {
            'display_title': base_title,
            'files': []
        }
    groups[group_key]['files'].append(file)
    
    file_info.append({
        'file': file,
        'group_key': group_key,
        'soup': soup,
        'basename': basename,
        'title_tag': title_tag
    })

new_titles = {}
for group_key, group_data in groups.items():
    display_title = group_data['display_title']
    files_in_group = sorted(group_data['files'])
    if len(files_in_group) == 1:
        new_titles[files_in_group[0]] = display_title
    else:
        for idx, f in enumerate(files_in_group):
            part_name = arabic_parts[idx] if idx < len(arabic_parts) else str(idx+1)
            new_titles[f] = f"{display_title} (الْجُزْءُ {part_name})"

print("Updating lesson files and filenames...")
for info in file_info:
    f = info['file']
    new_title = new_titles[f]
    soup = info['soup']
    basename = info['basename']
    
    changed = False
    
    # 1. Update <title>
    title_tag = soup.find('title')
    if title_tag and title_tag.get_text(strip=True) != new_title:
        title_tag.string = new_title
        changed = True
        
    # 2. Update <h1> if exists
    lt_h1 = soup.find('h1', class_='header-title')
    if lt_h1 and lt_h1.get_text(strip=True) != new_title:
        lt_h1.string = new_title
        changed = True
        
    if changed:
        with open(f, 'w', encoding='utf-8') as out:
            out.write(str(soup))
            
    # 3. Rename file
    match = re.match(r'([0-9]+\.[0-9]+)_(p[0-9]+|n[0-9X]+)_', basename)
    if match:
        prefix = match.group(0)
        new_basename = f"{prefix}{new_title}.html"
        new_basename = new_basename.replace('/', '-').replace('?', '')
        
        if new_basename != basename:
            new_file = os.path.join(pages_dir, new_basename)
            os.rename(f, new_file)

# We also need to map the answer blocks to the exact correct lesson names
# Since the answers files use lesson number, we can remap it.
print("Updating answers HTML files...")
answer_files = sorted(glob.glob('pages/98.*.html'))
lesson_num_to_title = {}
lesson_files_updated = [f for f in glob.glob('pages/*.html') if "TEMPLATE_" not in f and not os.path.basename(f).startswith('00.') and not os.path.basename(f).startswith('98.')]

for f in lesson_files_updated:
    with open(f, 'r', encoding='utf-8') as html_f:
        soup = BeautifulSoup(html_f.read(), 'html.parser')
        
    ln_div = soup.find('div', class_='lesson-number')
    title_tag = soup.find('title')
    
    if ln_div and title_tag:
        ln = ln_div.get_text(strip=True)
        title = title_tag.get_text(strip=True)
        lesson_num_to_title[to_arabic_indic(ln)] = title
        lesson_num_to_title[ln] = title

for f in answer_files:
    with open(f, 'r', encoding='utf-8') as ans_f:
        content = ans_f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    changed = False
    for section in soup.find_all('section', class_='content-block'):
        header_span = section.find('div', class_='block-header').find('span')
        if header_span:
            text = header_span.get_text(strip=True)
            match = re.search(r'إِجَابَاتُ: (.*?) \(الدَّرْسُ (.*?)\)', text)
            if match:
                num = match.group(2)
                if num in lesson_num_to_title:
                    correct_title = lesson_num_to_title[num]
                    # Also map the lesson title (strip "(الجزء الأول)" if it's there)
                    # For answers, let's keep the full title.
                    new_text = f'إِجَابَاتُ: {correct_title} (الدَّرْسُ {num})'
                    if text != new_text:
                        header_span.string = new_text
                        changed = True
    
    if changed:
        with open(f, 'w', encoding='utf-8') as out:
            out.write(str(soup))

# Finally, Generate exactly 2 TOC pages (00.2 and 00.3)
print("Generating TOC...")
all_files = sorted(glob.glob('pages/*.html'))
toc_entries = []
current_page = 2

for f in all_files:
    if "TEMPLATE_" in f or "TOC" in f:
        continue
    
    basename = os.path.basename(f)
    if basename == "00.0_blank.html" or basename == "00.1_intro.html":
        current_page += 1
        continue
        
    with open(f, 'r', encoding='utf-8') as html_f:
        soup = BeautifulSoup(html_f.read(), 'html.parser')
        
    lesson_number = None
    ln_div = soup.find('div', class_='lesson-number')
    if ln_div:
        lesson_number = ln_div.get_text(strip=True)
        
    lesson_title = None
    title_tag = soup.find('title')
    if title_tag:
        lesson_title = title_tag.get_text(strip=True)
        
    if basename.startswith('98.'):
        if not lesson_title.startswith('حَلُّ تَدْرِيبَاتِ الْكِتَابِ'):
            lesson_title = 'مُلْحَقُ الْإِجَابَاتِ - ' + lesson_title
            
    toc_entries.append({
        'title': lesson_title,
        'number': to_arabic_indic(lesson_number) if lesson_number else '-',
        'arabic_page': to_arabic_indic(current_page)
    })
    
    current_page += 1

mid_point = len(toc_entries) // 2
chunks = [toc_entries[:mid_point], toc_entries[mid_point:]]

for idx, chunk in enumerate(chunks):
    page_num = idx + 2
    
    toc_html = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="utf-8">
    <title>فِهْرِسُ الْمَوْضُوعَاتِ</title>
    <link href="../styles/main.css" rel="stylesheet">
    <style>
        .toc-table td, .toc-table th {{ padding: 2px; font-size: 11pt; border-bottom: 1px solid #ddd; }}
        .toc-table {{ width: 48%; float: right; margin-left: 2%; }}
        .toc-table.left-col {{ margin-left: 0; }}
        .toc-container {{ display: flex; justify-content: space-between; }}
    </style>
</head>
<body>
    <div class="force-new-page">
        <header class="page-header-strip">
            <div class="header-section right">
                <div class="lesson-number">00</div>
                <div class="lesson-details">
                    <div>المستوى التأسيسي</div>
                    <div>فِهْرِسٌ</div>
                </div>
            </div>
            <div class="header-section center">
                <h1 class="header-title">فِهْرِسُ الْمَوْضُوعَاتِ (الْجُزْءُ {to_arabic_indic(idx+1)})</h1>
            </div>
            <div class="header-section left">
                <div class="author-info">أ. الياس خفيف</div>
                <div class="author-info">994066850 963+</div>
            </div>
        </header>
        
        <div class="toc-container mt-2mm">
"""
    col_size = (len(chunk) + 1) // 2
    col1 = chunk[:col_size]
    col2 = chunk[col_size:]
    
    for c_idx, col_data in enumerate([col1, col2]):
        extra_class = "left-col" if c_idx == 1 else ""
        toc_html += f"""
            <table class="toc-table {extra_class}">
                <thead>
                    <tr style="background-color: #f5f5f5;">
                        <th style="width: 15%; text-align: center;">الدَّرْسُ</th>
                        <th style="width: 70%;">الْمَوْضُوعُ</th>
                        <th style="width: 15%; text-align: center;">الصَّفْحَةُ</th>
                    </tr>
                </thead>
                <tbody>"""
                
        for item in col_data:
            title = item['title']
            num = item['number']
            page = item['arabic_page']
            
            bg = "background-color: rgba(0, 121, 107, 0.05);" if ('مُلْحَق' in title or 'حَلُّ' in title) else ""
            
            toc_html += f"""
                    <tr style="{bg}">
                        <td style="text-align: center; font-weight: bold;">{num}</td>
                        <td style="font-weight: bold; font-size: 10pt;">{title}</td>
                        <td style="text-align: center; font-weight: bold; color: #00796b;">{page}</td>
                    </tr>"""
                    
        toc_html += """
                </tbody>
            </table>"""
            
    toc_html += """
        </div>
    </div>
</body>
</html>"""

    with open(f'pages/00.{page_num}_TOC.html', 'w', encoding='utf-8') as f:
        f.write(toc_html)

print("Done restoring and fixing!")
