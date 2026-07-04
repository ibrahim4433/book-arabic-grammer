import glob
import os
from bs4 import BeautifulSoup

def merge():
    files = sorted(glob.glob('pages/98.*_Answers.html'))
    
    all_sections = []
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            sections = soup.find_all('section', class_='content-block')
            all_sections.extend(sections)
            
    header = """<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
<meta charset="utf-8"/>
<title>مُلْحَقُ الْإِجَابَاتِ</title>
<link href="../styles/main.css" rel="stylesheet"/>
</head>
<body>
<div class="force-new-page">
<header class="page-header-strip">
<div class="header-section right">
<div class="lesson-number">٩٨</div>
<div class="lesson-details">
<div>المستوى التأسيسي</div>
<div>مُلْحَقُ الْإِجَابَاتِ</div>
</div>
</div>
<div class="header-section center">
<h1 class="header-title">حَلُّ تَدْرِيبَاتِ الْكِتَابِ</h1>
</div>
<div class="header-section left">
<div class="author-info">أ. حنا خفيف</div>
<div class="author-info"> </div>
</div>
</header>
"""
    footer = """
</div>
</body>
</html>
"""

    with open('pages/98.00_p120_Answers.html', 'w', encoding='utf-8') as f:
        f.write(header)
        for section in all_sections:
            f.write(str(section) + "\n")
        f.write(footer)
        
    print(f"Merged {len(all_sections)} sections into one file.")
    
    for file in files:
        if file != 'pages/98.00_p120_Answers.html':
            os.remove(file)
            print(f"Deleted {file}")

if __name__ == '__main__':
    merge()
