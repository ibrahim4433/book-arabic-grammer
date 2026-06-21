import os
import bs4

with open("Jules-workspace/pages/11.0_nXX_الْمَفْعُولُ بِه وَأَنْوَاعَهُ وَعَلَاَّمَاتِ إِعْرَابِهِ.html", "r") as f:
    html_content = f.read()

soup = bs4.BeautifulSoup(html_content, "html.parser")

exam_block = soup.find('section', class_='content-block')
all_sections = soup.find_all('section', class_='content-block')
exam_block = all_sections[-1]

exam_block.extract()

with open("Jules-workspace/pages/11.0_nXX_الْمَفْعُولُ بِه وَأَنْوَاعَهُ وَعَلَاَّمَاتِ إِعْرَابِهِ.html", "w") as f:
    f.write(str(soup))


html_1 = """<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="utf-8"/>
    <title>الْمَفْعُولُ بِه وَأَنْوَاعَهُ وَعَلَاَّمَاتِ إِعْرَابِهِ - 2</title>
    <link href="../styles/main.css" rel="stylesheet"/>
</head>
<body>
    <div class="force-new-page">

        <header class="page-header-strip">
            <div class="header-section right">
                <div class="lesson-number">11</div>
                <div class="lesson-details">
                    <div></div>
                    <div></div>
                </div>
            </div>
            <div class="header-section center">
                <h1 class="header-title">الْمَفْعُولُ بِه وَأَنْوَاعَهُ وَعَلَاَّمَاتِ إِعْرَابِهِ (تَتِمَّةٌ)</h1>
            </div>
            <div class="header-section left">
                <div class="author-info">أ. الياس خفيف</div>
                <div class="author-info">994066850 963+</div>
            </div>
        </header>

        <div class="benefit-box warning mb-2mm">
            <strong>⚠️ تَنْبِيهٌ:</strong> رَاجِعِ الْقَوَاعِدَ السَّابِقَةَ قَبْلَ الْبَدْءِ فِي حَلِّ هَذَا الِاخْتِبَارِ لِضَمَانِ الْإِجَابَةِ الصَّحِيحَةِ.
        </div>

    </div>
</body>
</html>"""

soup1 = bs4.BeautifulSoup(html_1, "html.parser")
force_new_page1 = soup1.find('div', class_='force-new-page')
force_new_page1.append(exam_block)

with open("Jules-workspace/pages/11.1_nXX_الْمَفْعُولُ بِه وَأَنْوَاعَهُ وَعَلَاَّمَاتِ إِعْرَابِهِ.html", "w") as f:
    f.write(str(soup1))
