import os
import re

# Templates Directory
TEMPLATES_DIR = 'Jules-workspace/Templates/'
OUTPUT_FILE_1 = 'pages/10.0_nXX_معاني صيغ الزيادة.html'
OUTPUT_FILE_2 = 'pages/10.1_nXX_معاني صيغ الزيادة_تابع.html'

def read_template(name):
    try:
        with open(os.path.join(TEMPLATES_DIR, name + '.html'), 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Template {name} not found.")
        return ""

def main():
    # Load Templates
    t_base = read_template('TEMPLATE_C_BASE')
    t_wrapper = read_template('TEMPLATE_C_PAGE_WRAPPER')
    t_header = read_template('TEMPLATE_C_HEADER')
    t_block = read_template('TEMPLATE_C_BLOCK')
    t_table = read_template('TEMPLATE_C_TABLE')
    t_split = read_template('TEMPLATE_C_SPLIT')
    t_list_item = read_template('TEMPLATE_C_LIST_ITEM')
    t_benefit = read_template('TEMPLATE_C_BENEFIT')
    t_poem = read_template('TEMPLATE_C_POEM')
    t_irab_row = read_template('TEMPLATE_C_IRAB_ROW')
    t_irab_box = read_template('TEMPLATE_C_IRAB_BOX')
    t_irab = read_template('TEMPLATE_C_IRAB')
    t_exam = read_template('TEMPLATE_C_EXAM')

    # ================= PAGE 1 =================
    # Block 1: Header
    header = t_header.replace('[LESSON_NUMBER]', '10')
    header = header.replace('[CHAPTER_TITLE]', 'معاني صيغ الزيادة')
    header = header.replace('[CATEGORY_HEADER]', 'الصرف')
    header = header.replace('[SECTION_HEADER]', 'المستوى اللغوي')
    header = header.replace('[AUTHOR_NAME]', 'أ. الياس خفيف')
    header = header.replace('[AUTHOR_PHONE]', '994066850 963+')

    # Block 2: Concept
    block2 = t_block.replace('[BLOCK_TITLE]', 'مَفْهُومُ الزِّيَادَةِ فِي الأَفْعَالِ')
    content_text = '<p class="text-accent text-justify">تَتَغَيَّرُ دَلَالَةُ الفِعْلِ (مَعْنَاهُ) بِحَسَبِ مَا يُزَادُ عَلَى الثُّلَاثِيِّ مِنْ حُرُوفِ الزِّيَادَةِ، وَهَذِهِ المَعَانِي الجَدِيدَةُ لَمْ تَكُنْ لِلْفِعْلِ قَبْلَ زِيَادَةِ الأَحْرُفِ عَلَى أَصْلِهِ الثُّلَاثِيِّ. فَكُلَّمَا زَادَ المَبْنَى، زَادَ المَعْنَى.</p>'
    block2 = block2.replace('[CONTENT_TEXT]', content_text)
    block2 = re.sub(r'<div class="benefit-box">.*?</div>', '', block2, flags=re.DOTALL)

    # Block 3: Table
    rows = ""
    data = [
        ('أَفْعَلَ', 'التَّحَوُّلُ، الدُّخُولُ فِي الزَّمَانِ، التَّعْدِيَةُ', '<span class="highlight-red">أَجْلَسَ</span>، <span class="highlight-blue">أَصْبَحَ</span>، <span class="highlight-green">أَفْطَرَ</span>'),
        ('افْعَلَّ', 'المُبَالَغَةُ (فِي الْأَلْوَانِ وَالْعُيُوبِ)', '<span class="highlight-red">احْمَرَّ</span> الوَجْهُ، <span class="highlight-blue">اخْضَرَّ</span> الزَّرْعُ'),
        ('اسْتَفْعَلَ', 'الطَّلَبُ وَالسُّؤَالُ، التَّحَوُّلُ', '<span class="highlight-red">اسْتَوْقَفَ</span>، <span class="highlight-blue">اسْتَحْجَرَ</span> الطِّينُ'),
        ('انْفَعَلَ', 'المُطَاوَعَةُ (لِفِعْلٍ ثُلَاثِيٍّ)', '<span class="highlight-red">انْكَسَرَ</span> الزُّجَاجُ، <span class="highlight-blue">انْطَلَقَ</span>'),
        ('افْتَعَلَ', 'المُطَاوَعَةُ، الِاتِّخَادُ، المُشَارَكَةُ', '<span class="highlight-red">اقْتَرَبَ</span>، <span class="highlight-blue">اخْتَصَمَ</span> الخَصْمَانِ'),
        ('تَفَعَّلَ', 'التَّكَلُّفُ، التَّدَرُّجُ، المُطَاوَعَةُ', '<span class="highlight-red">تَشَجَّعَ</span>، <span class="highlight-blue">تَجَرَّعَ</span>، <span class="highlight-green">تَكَسَّرَ</span>'),
        ('تَفَاعَلَ', 'المُشَارَكَةُ، التَّظَاهُرُ', '<span class="highlight-red">تَعَاوَنَ</span> القَوْمُ، <span class="highlight-blue">تَغَافَلَ</span>، <span class="highlight-green">تَمَارَضَ</span>'),
        ('فَعَّلَ', 'التَّكْثِيرُ، التَّعْدِيَةُ', '<span class="highlight-red">كَسَّرَ</span>، <span class="highlight-blue">غَلَّقَ</span> الأَبْوَابَ'),
        ('فَاعَلَ', 'المُشَارَكَةُ بَيْنَ اثْنَيْنِ', '<span class="highlight-red">قَاتَلَ</span>، <span class="highlight-blue">شَارَكَ</span>، <span class="highlight-green">جَادَلَ</span>'),
        ('تَفَعْلَلَ', 'المُطَاوَعَةُ (لِلرُّبَاعِيِّ)', '<span class="highlight-red">تَدَحْرَجَ</span> الحَجَرُ')
    ]
    for row in data:
        rows += f'<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>\n'
    block3 = t_table.replace('[TABLE_TITLE]', 'أَهَمُّ المَعَانِي المُسْتَفَادَةِ مِنْ صِيَغِ الزِّيَادَةِ')
    block3 = block3.replace('[TABLE_HEADERS]', '<th>الصِّيغَةُ الصَّرْفِيَّةُ</th><th>المَعَانِي الَّتِي تُفِيدُهَا</th><th>أَمْثِلَةٌ تَطْبِيقِيَّةٌ</th>')
    block3 = block3.replace('[TABLE_ROWS]', rows)

    # Block 4: Split
    left_list_data = [
        ('**انْفَعَلَ**: يُفِيدُ قَبُولَ أَثَرِ الفِعْلِ. مِثْلُ: كَسَرْتُهُ <span class="highlight-red">فَانْكَسَرَ</span>.', '•'),
        ('**افْتَعَلَ**: يُفِيدُ المُطَاوَعَةَ أَيْضاً. مِثْلُ: جَمَعْتُهُ <span class="highlight-red">فَاجْتَمَعَ</span>.', '•'),
        ('**تَفَعَّلَ**: مُطَاوَعَةُ (فَعَّلَ). مِثْلُ: كَسَّرْتُهُ <span class="highlight-red">فَتَكَسَّرَ</span>.', '•')
    ]
    left_items = ""
    for content, marker in left_list_data:
        content = re.sub(r'\*\*(.*?)\*\*', r'<span class="font-bold">\1</span>', content)
        item = t_list_item.replace('[CONTENT]', content).replace('[MARKER]', marker)
        left_items += item
    left_content = f'<ul class="structured-list">{left_items}</ul>'

    right_list_data = [
        ('**فَاعَلَ**: مُشَارَكَةٌ بَيْنَ طَرَفَيْنِ غَالِباً. مِثْلُ: <span class="highlight-blue">قَاتَلَ</span> الجَيْشُ العَدُوَّ.', '•'),
        ('**تَفَاعَلَ**: مُشَارَكَةٌ بَيْنَ أَكْثَرَ مِنْ طَرَفٍ، أَوْ تُفِيدُ التَّظَاهُرَ. مِثْلُ: <span class="highlight-blue">تَعَاوَنَ</span> المُوَاطِنُونَ.', '•'),
        ('**افْتَعَلَ**: قَدْ تَأْتِي لِلْمُشَارَكَةِ. مِثْلُ: <span class="highlight-blue">اخْتَصَمَ</span> الزَّيْدَانِ.', '•')
    ]
    right_items = ""
    for content, marker in right_list_data:
        content = re.sub(r'\*\*(.*?)\*\*', r'<span class="font-bold">\1</span>', content)
        item = t_list_item.replace('[CONTENT]', content).replace('[MARKER]', marker)
        right_items += item
    right_content = f'<ul class="structured-list">{right_items}</ul>'

    block4 = t_split.replace('[LEFT_TITLE]', 'صِيَغُ المُطَاوَعَةِ')
    block4 = block4.replace('[LEFT_CONTENT]', left_content)
    block4 = block4.replace('[RIGHT_TITLE]', 'صِيَغُ المُشَارَكَةِ')
    block4 = block4.replace('[RIGHT_CONTENT]', right_content)

    # Block 5: Benefit
    block5 = t_benefit.replace('[BENEFIT_TITLE]', 'قَاعِدَةٌ ذَهَبِيَّةٌ')
    content_b5 = '<p class="text-center font-bold">كُلُّ زِيَادَةٍ فِي المَبْنَى تُؤَدِّي بِالضَّرُورَةِ إِلَى زِيَادَةٍ فِي المَعْنَى.</p><p class="text-justify">فَالفِعْلُ (غَفَرَ) يَدُلُّ عَلَى مُجَرَّدِ الغُفْرَانِ، بَيْنَمَا (اسْتَغْفَرَ) يَدُلُّ عَلَى طَلَبِ ذَلِكَ الغُفْرَانِ وَالسَّعْيِ إِلَيْهِ.</p>'
    block5 = block5.replace('[BENEFIT_TEXT]', content_b5)

    # Block 6: Poem + Irab
    block6_poem = t_poem.replace('[SECTION_TITLE]', 'شَوَاهِدُ شِعْرِيَّةٌ')
    block6_poem = block6_poem.replace('[POET_NAME]', 'قَاعِدَةٌ نَحْوِيَّةٌ')
    block6_poem = block6_poem.replace('[POET_BIO]', '')
    block6_poem = block6_poem.replace('[POEM_TITLE]', '')
    block6_poem = block6_poem.replace('<h3 class="text-center text-primary mb-4mm"></h3>', '')
    block6_poem = block6_poem.replace('class="bio-info"', '')
    block6_poem = block6_poem.replace('class="bio-card"', 'class=""')

    poem_verse = "وَبِالزِّيَادَةِ المَعَانِي تَكْثُرُ ... كَمِثْلِ (اسْتَفْهَمَ) أَيْ يَسْتَفْسِرُ"
    block6_poem = block6_poem.replace('[POEM_VERSES]', f'<p class="text-center font-bold">{poem_verse}</p>')

    irab1 = t_irab_box.replace('[WORD]', 'اسْتَغْفَرَ').replace('[PARSING_DETAILS]', 'فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الفَتْحِ، وَالزِّيَادَةُ (السين والتاء) تُفِيدُ الطَّلَبَ.')
    irab2 = t_irab_box.replace('[WORD]', 'المُؤْمِنُ').replace('[PARSING_DETAILS]', 'فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ.')
    block6_irab = t_irab_row.replace('[IRAB_BOXES]', irab1 + irab2)
    block6 = block6_poem + '\n' + block6_irab

    # Combine Page 1
    content1 = header + block2 + block3 + block4 + block5 + block6
    page1 = t_base.replace('<!-- INJECT_CONTENT_HERE -->', t_wrapper.replace('<!-- INJECT_CONTENT_HERE -->', content1))

    # Clean IDs for Page 1
    page1 = page1.replace('id="[BLOCK_ID]"', '')

    with open(OUTPUT_FILE_1, 'w', encoding='utf-8') as f:
        f.write(page1)
    print(f"Generated {OUTPUT_FILE_1}")

    # ================= PAGE 2 =================
    # Header
    header2 = t_header.replace('[LESSON_NUMBER]', '10')
    header2 = header2.replace('[CHAPTER_TITLE]', 'معاني صيغ الزيادة (تابع)')
    header2 = header2.replace('[CATEGORY_HEADER]', 'الصرف')
    header2 = header2.replace('[SECTION_HEADER]', 'المستوى اللغوي')
    header2 = header2.replace('[AUTHOR_NAME]', 'أ. الياس خفيف')
    header2 = header2.replace('[AUTHOR_PHONE]', '994066850 963+')

    # Block 7: Exam
    q1_html = """
        <div class="exam-question" id="">
            <p class="m-0 mb-2mm">
                <span class="exam-number">1</span>
                اسْتَخْرِجِ الفِعْلَ المَزِيدَ وَبَيِّنْ مَعْنَى الزِّيَادَةِ فِي الجُمْلَةِ: "اسْتَمْطَرَ النَّاسُ رَبَّهُمْ".
            </p>
            <div class="border-light h-8mm bg-grey-lighter rounded"></div>
        </div>
    """
    q2_html = """
        <div class="exam-question" id="">
            <p class="m-0 mb-2mm">
                <span class="exam-number">2</span>
                صُغْ فِعْلاً عَلَى وَزْنِ (تَفَاعَلَ) مِنَ الفِعْلِ (غَفَلَ) وَضَعْهُ فِي جُمْلَةٍ مُفِيدَةٍ.
            </p>
            <div class="border-light h-8mm bg-grey-lighter rounded"></div>
        </div>
    """
    q3_html = """
        <div class="exam-question mb-0 border-none pb-0" id="">
            <p class="m-0 mb-2mm">
                <span class="exam-number">3</span>
                مَيِّزْ بَيْنَ مَعْنَى (قَطَعَ) وَ (قَطَّعَ) فِي جُمْلَتَيْنِ مِنْ إِنْشَائِكَ.
            </p>
            <div class="border-light h-8mm bg-grey-lighter rounded"></div>
        </div>
    """
    block7 = t_exam.replace('[TOPIC]', 'معاني صيغ الزيادة')
    block7 = re.sub(r'<div class="block-body">.*?</div>\s*</section>',
                    f'<div class="block-body">{q1_html}{q2_html}{q3_html}</div>\n</section>',
                    block7, flags=re.DOTALL)

    # Block 8: Extra Irab Model
    irab8_1 = t_irab_box.replace('[WORD]', 'تَعَاوَنَ').replace('[PARSING_DETAILS]', 'فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الفَتْحِ، وَوَزْنُ (تَفَاعَلَ) هُنَا يُفِيدُ الْمُشَارَكَةَ.')
    irab8_2 = t_irab_box.replace('[WORD]', 'الْمُؤْمِنُونَ').replace('[PARSING_DETAILS]', 'فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْوَاوُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.')
    block8 = t_irab.replace('[SENTENCE_TO_PARSE]', 'تَعَاوَنَ الْمُؤْمِنُونَ عَلَى الْبِرِّ')
    block8 = block8.replace('[IRAB_BOXES]', irab8_1 + irab8_2)
    block8 = block8.replace('class="irab-stack"', 'class="flex flex-col gap-2mm"')

    # Block 10: Conjugation Table (Extra)
    rows_10 = ""
    data_10 = [
        ('أَكْرَمَ', 'يُكْرِمُ', 'أَكْرِمْ', 'إِكْرَاماً'),
        ('قَاتَلَ', 'يُقَاتِلُ', 'قَاتِلْ', 'مُقَاتَلَةً / قِتَالاً'),
        ('انْكَسَرَ', 'يَنْكَسِرُ', 'انْكَسِرْ', 'انْكِسَاراً'),
        ('تَعَلَّمَ', 'يَتَعَلَّمُ', 'تَعَلَّمْ', 'تَعَلُّماً'),
        ('اسْتَغْفَرَ', 'يَسْتَغْفِرُ', 'اسْتَغْفِرْ', 'اسْتِغْفَاراً')
    ]
    for row in data_10:
        rows_10 += f'<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td></tr>\n'

    block10 = t_table.replace('[TABLE_TITLE]', 'تَصْرِيفُ نَمَاذِجَ مِنَ الأَفْعَالِ المَزِيدَةِ')
    block10 = block10.replace('[TABLE_HEADERS]', '<th>الماضي</th><th>المضارع</th><th>الأمر</th><th>المصدر</th>')
    block10 = block10.replace('[TABLE_ROWS]', rows_10)

    # Block 11: Balaagha Benefit
    block11 = t_block.replace('[BLOCK_TITLE]', 'فَائِدَةٌ بَلَاغِيَّةٌ: (اسْطَاعَ) وَ (اسْتَطَاعَ)')
    content_b11 = """
    <p class="text-justify mb-2mm">قَالَ تَعَالَى: <span class="text-primary font-bold">﴿فَمَا اسْطَاعُوا أَنْ يَظْهَرُوهُ وَمَا اسْتَطَاعُوا لَهُ نَقْبًا﴾</span> [الكهف: 97].</p>
    <p class="text-justify">لَمَّا كَانَ الظُّهُورُ (الصُّعُودُ) عَلَى السُّورِ أَسْهَلَ مِنْ نَقْبِهِ (خَرْقِهِ)، جَاءَ الفِعْلُ <b>(اسْطَاعُوا)</b> بِحَذْفِ التَّاءِ لِلتَّخْفِيفِ مُنَاسِبَةً لِخِفَّةِ الْحَدَثِ.</p>
    <p class="text-justify">وَلَمَّا كَانَ النَّقْبُ أَشَقَّ وَأَصْعَبَ وَيَحْتَاجُ إِلَى جُهْدٍ أَكْبَرَ، جَاءَ الفِعْلُ <b>(اسْتَطَاعُوا)</b> تَامًّا، فَنَاسَبَتْ زِيَادَةُ الْمَبْنَى زِيَادَةَ الْمَعْنَى (الْجُهْدِ الْمَبْذُولِ).</p>
    """
    block11 = block11.replace('[CONTENT_TEXT]', content_b11)
    block11 = re.sub(r'<div class="benefit-box">.*?</div>', '', block11, flags=re.DOTALL)

    # Block 9: Benefit Warning
    block9 = t_benefit.replace('[BENEFIT_TITLE]', 'تَنْبِيهٌ مُهِمٌّ')
    content_b9 = '<p class="text-justify">قَدْ تَأْتِي صِيغَةُ (افْتَعَلَ) وَلا تُفِيدُ المُشَارَكَةَ، بَلْ مُجَرَّدَ القِيَامِ بِالفِعْلِ، مِثْلَ: (اسْتَمَعَ) بِمَعْنَى أَصْغَى، وَلَيْسَ فِيهَا مَعْنَى المُشَارَكَةِ.</p>'
    block9 = block9.replace('[BENEFIT_TEXT]', content_b9)
    block9 = block9.replace('class="benefit-box"', 'class="benefit-box warning"')


    # Combine Page 2
    content2 = header2 + block7 + block8 + block10 + block11 + block9
    page2 = t_base.replace('<!-- INJECT_CONTENT_HERE -->', t_wrapper.replace('<!-- INJECT_CONTENT_HERE -->', content2))

    # Clean IDs for Page 2
    page2 = page2.replace('id="[BLOCK_ID]"', '')
    page2 = page2.replace('id="[Q1_ID]"', '')
    page2 = page2.replace('id="[Q2_ID]"', '')

    with open(OUTPUT_FILE_2, 'w', encoding='utf-8') as f:
        f.write(page2)
    print(f"Generated {OUTPUT_FILE_2}")

if __name__ == "__main__":
    main()
