import os, glob, re
from pathlib import Path
from bs4 import BeautifulSoup

def to_arabic_indic(text):
    english_to_arabic = {'0':'٠','1':'١','2':'٢','3':'٣','4':'٤','5':'٥','6':'٦','7':'٧','8':'٨','9':'٩'}
    return ''.join(english_to_arabic.get(c, c) for c in str(text))

pages_dir = Path('pages')

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
    lt_h1 = soup.find('h1', class_='header-title')
    if lt_h1:
        lesson_title = lt_h1.get_text(strip=True)
        
    if not lesson_title:
        lesson_title = ""
        
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
        .toc-table td, .toc-table th {{ padding: 4px; font-size: 11pt; border-bottom: 1px solid #eee; }}
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
        
        <div class="toc-container">
"""
    col_size = (len(chunk) + 1) // 2
    col1 = chunk[:col_size]
    col2 = chunk[col_size:]
    
    for c_idx, col_data in enumerate([col1, col2]):
        extra_class = "left-col" if c_idx == 1 else ""
        toc_html += f"""
            <table class="toc-table {extra_class}">
                <thead>
                    <tr>
                        <th style="width: 15%; text-align: center;">الرَّقْمُ</th>
                        <th style="width: 70%;">الْمَوْضُوعُ</th>
                        <th style="width: 15%; text-align: center;">الصَّفْحَةُ</th>
                    </tr>
                </thead>
                <tbody>"""
                
        for item in col_data:
            title = item['title']
            num = item['number']
            page = item['arabic_page']
            
            bg = "background-color: rgba(0, 121, 107, 0.1);" if ('مُلْحَق' in title or 'حَلُّ' in title) else ""
            
            toc_html += f"""
                    <tr style="{bg}">
                        <td style="text-align: center; font-weight: bold;">{num}</td>
                        <td style="font-weight: bold;">{title}</td>
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

print("Done!")
