import os
import re

TEMPLATES_DIR = "Jules-workspace/Templates"
OUTPUT_FILE_1 = "pages/27.0_nXX_المحسنات_البديعية.html"
OUTPUT_FILE_2 = "pages/27.1_nXX_المحسنات_البديعية.html"

def read_template(filename):
    with open(os.path.join(TEMPLATES_DIR, filename), "r", encoding="utf-8") as f:
        return f.read()

def replace_block_content(tpl, new_content):
    pattern = r'<p class="mt-1mm text-accent">\s*\[CONTENT_TEXT\]\s*</p>'
    return re.sub(pattern, new_content, tpl, flags=re.DOTALL)

def generate_html():
    # Load Templates
    tpl_base = read_template("TEMPLATE_C_BASE.html")
    tpl_header = read_template("TEMPLATE_C_HEADER.html")
    tpl_block = read_template("TEMPLATE_C_BLOCK.html")
    tpl_table = read_template("TEMPLATE_C_TABLE.html")
    tpl_table_row = read_template("TEMPLATE_C_TABLE_ROW.html")
    tpl_chips = read_template("TEMPLATE_C_CHIPS.html")
    tpl_list = read_template("TEMPLATE_C_LIST.html")
    tpl_benefit = read_template("TEMPLATE_C_BENEFIT_TIP.html")
    tpl_poem = read_template("TEMPLATE_C_POEM.html")
    tpl_exam = read_template("TEMPLATE_C_EXAM.html")

    blocks_page_1 = []
    blocks_page_2 = []

    # --- Page 1 Content ---

    # Block 1: Header
    header = tpl_header.replace("[LESSON_NUMBER]", "27")
    header = header.replace("[CHAPTER_TITLE]", "المحسنات البديعية")
    header = header.replace("[CATEGORY_HEADER]", "فوائد")
    header = header.replace("[SECTION_HEADER]", "المستوى الفني")
    header = header.replace("[AUTHOR_NAME]", "أ. الياس خفيف")
    header = header.replace("[AUTHOR_PHONE]", "994066850 963+")
    blocks_page_1.append(header)

    # Block 2: Introduction
    intro = tpl_block.replace("[BLOCK_TITLE]", "المُحَسِّناتُ البديعيَّةُ (عِلمُ البَديعِ)")
    intro_content = '<p class="text-accent text-right mt-1mm">تُقسَمُ المُحسِّناتُ البديعيَّةُ قِسمينِ: مُحسِّناتٌ لفظيَّةٌ، ومُحسِّناتٌ معنويَّةٌ.</p>'
    intro = replace_block_content(intro, intro_content)
    intro = intro.replace("[BENEFIT_TITLE]", "فَائِدَةُ الْجِنَاسِ وَوَظِيفَتُهُ (أَثَرُهُ الْفَنِّيُّ)")
    intro = intro.replace("[BENEFIT_TEXT]", "يضفي على الكلامِ رونقًا وعذوبةً، ويمنحُه إيقاعًا موسيقيًّا، فهو منبعٌ من منابعِ الموسيقا الدّاخليَّةِ.")
    blocks_page_1.append(intro)

    # Block 3: Table
    table_rows_data = [
        ("الْجِنَاسُ التَّامُّ", "تَطَابُقُ اللَّفْظَيْنِ فِي نَوْعِ الْحُرُوفِ، وَعَدَدِهَا، وَهَيْئَتِهَا، وَتَرْتِيبِهَا مَعَ اخْتِلَافِ الْمَعْنَى.", "(حَيِّهِمْ مَا دُمْتَ فِي حَيِّهِمْ)."),
        ("الْجِنَاسُ النَّاقِصُ", "اخْتِلَافُ اللَّفْظَيْنِ فِي وَاحِدٍ مِنَ الْأُمُورِ الْأَرْبَعَةِ (النَّوْعِ، الْعَدَدِ، الْهَيْئَةِ، التَّرْتِيبِ).", "(ظَالِم، عَالِم)، (سَاق، مَسَاق)، (خَلْقِي، خُلُقِي)، (فَتْح، حَتْف)."),
        ("التَّصْرِيعُ", "تَطَابُقُ الْعَرُوضِ وَالضَّرْبِ وَزْنًا وَتَقْفِيَةً وَإِعْرَابًا (غَالِبًا فِي الْبَيْتِ الْأَوَّلِ).", "ذَخَرْتُ لِأَحْدَاثِ الزَّمَانِ يَرَاعَا ... يُجِيدُ نِضَالًا دُونَهَا وَقِرَاعَا"),
        ("السَّجْعُ", "تَوَافُقُ الْحُرُوفِ الْأَخِيرَةِ فِي نِهَايَاتِ الْجُمَلِ (فِي النَّثْرِ).", "إِنَّ حِفْظَ الْعَرَبِ لُغَتَهُمْ حِفْظُهُم، وَإِنَّ أَضَاعُوهَا أَضَاعَتْهُمْ.	"),
        ("التَّوَازُنُ", "اتِّفَاقُ الْكَلِمَتَيْنِ فِي الْوَزْنِ فِي أَوَاخِرِ الْفِقْرَتَيْنِ (دُونَ التَّقْفِيَةِ ضَرُورَةً).", "((اللَّهُمَّ أَعْطِ مُنْفِقًا خَلَفًا، وَأعْطِ مُمْسِكًا تَلَفًا))."),
        ("الطِّبَاقُ (الْإِيجَابُ)", "الْجَمْعُ بَيْنَ لَفْظَيْنِ مُتَضَادَّيْنِ وَكُلٌّ مِنْهُمَا مُثْبَتٌ.", "(نَاجِح، رَاسِب)."),
        ("الطِّبَاقُ (السَّلْبُ)", "الْجَمْعُ بَيْنَ الْكَلِمَةِ وَنَفْيِهَا، أَو الْأَمْرِ وَالنَّهْيِ.", "(يَرَى، لَمْ يَرَ)، (اقْرَأ، لَا تَقْرَأ)."),
        ("الْمُقَابَلَةُ", "الْإِتْيَانُ بِمَعْنَيَيْنِ أَو أَكْثَرَ ثُمَّ مَا يُضَادُّهَا عَلَى التَّرْتِيبِ.", "فَتًى تَمَّ فِيهِ مَا يَسُرُّ صَدِيقَهُ ... عَلَى أَنَّ فِيهِ مَا يَسُوءُ الْأَعَادِيَا"),
    ]
    rows_html = ""
    for r in table_rows_data:
        row = tpl_table_row.replace("[CELL_1]", f'<span class="font-bold text-primary">{r[0]}</span>')
        row = row.replace("[CELL_2]", r[1])
        row = row.replace("[CELL_3]", r[2])
        rows_html += row

    table = tpl_table.replace("[TABLE_TITLE]", "جَدْوَلُ خُلَاصَةِ الْمُحَسِّنَاتِ الْبَدِيعِيَّةِ")
    table = table.replace("[TABLE_HEADERS]", "<th>الْمُحَسِّنُ</th><th>التَّعْرِيفُ الْمُوجَزُ</th><th>مِثَالٌ تَوْضِيحِيٌّ</th>")
    table = table.replace("[TABLE_ROWS]", rows_html)
    blocks_page_1.append(table)

    # Block 4: Jinas Types
    jinas = tpl_block.replace("[BLOCK_TITLE]", "أَوْجُهُ الِاخْتِلَافِ فِي الْجِنَاسِ النَّاقِصِ")
    jinas_content = '<p class="text-accent text-right mt-1mm">يَكُونُ الْجِنَاسُ نَاقِصًا عِنْدَمَا يَخْتَلِفُ اللَّفْظَانِ الْمُتَجَانِسَانِ فِي وَاحِدٍ مِنَ الْوُجُوهِ الْأَرْبَعَةِ، عَلَى النَّحْوِ الْآتِي:</p>'
    jinas = replace_block_content(jinas, jinas_content)
    jinas = jinas.replace('<div class="benefit-box">\n                <strong> [BENEFIT_TITLE]:</strong> [BENEFIT_TEXT]\n            </div>', '')
    blocks_page_1.append(jinas)

    # Block 5: Conditions Chips
    chips_items = """
<div class="bg-grey-lighter p-2mm rounded text-center">نَوْعُ الْحُرُوفِ</div>
<div class="bg-grey-lighter p-2mm rounded text-center">عَدَدُ الْحُرُوفِ</div>
<div class="bg-grey-lighter p-2mm rounded text-center">هَيْئَةُ الْحُرُوفِ (الضَّبْطُ)</div>
<div class="bg-grey-lighter p-2mm rounded text-center">تَرْتِيبُ الْحُرُوفِ</div>
"""
    chips = tpl_chips.replace("[CHIPS_CONTENT]", chips_items)
    blocks_page_1.append(chips)

    # Block 6: Semantic Enhancements
    sem = tpl_block.replace("[BLOCK_TITLE]", "الْمُحَسِّنَاتُ الْبَدِيعِيَّةُ الْمَعْنَوِيَّةُ")
    sem_content = """<p class="text-accent mb-2mm text-justify mt-1mm">١- الطِّبَاقُ (الْمُطَابَقَةُ): مُحسِّنٌ معنويٌّ، يجمعُ بين لفظينِ مُتضادَّينِ في المعنى، فيولِّدُ حركةً داخليَّةً في النَّفسِ تُبرِزُ الفارقَ بينهما.</p>
<p class="text-accent mb-2mm text-justify">٢- الْمُقَابَلَةُ: مُحسِّنٌ معنويٌّ، وهو أنْ يُؤتى بمعنينِ متوافقينِ، أو عدَّةِ معانٍ مُتوافِقةٍ، ثم يُؤتَى بضِدِّها على ترتيبِها. (هي الجمعُ بين طِباقينِ، فأكثر في الكلامِ على الترتيبِ).</p>"""
    sem = replace_block_content(sem, sem_content)
    sem = sem.replace('<div class="benefit-box">\n                <strong> [BENEFIT_TITLE]:</strong> [BENEFIT_TEXT]\n            </div>', '')
    blocks_page_1.append(sem)

    # Block 7: Aesthetic Values
    aes = tpl_list.replace("[LIST_TITLE]", "الْقِيَمُ الْجَمَالِيَّةُ وَالْمَعْنَوِيَّةُ لِلطِّبَاقِ وَالْمُقَابَلَةِ (أَثَرُهُمَا الْفَنِّيُّ)")
    aes_items = """
<li><span class="font-bold text-primary">١- إِظْهَارُ الْمَعْنَى بِجَلَاءٍ وَوُضُوحٍ.</span></li>
<li><span class="font-bold text-primary">٢- إِثَارَةُ الْخَيَالِ.</span></li>
<li><span class="font-bold text-primary">٣- إِعْمَالُ الْعَقْلِ فِي الْمُتَنَاقِضَاتِ.</span></li>
<li><span class="font-bold text-primary">٤- تَحْدِيدُ الرُّؤْيَةِ (الْمَوْقِفُ).</span></li>
"""
    aes = aes.replace("[LIST_ITEMS]", aes_items)
    aes = aes.replace('<hr class="separator-dashed">\n            <div class="benefit-box">\n                <strong> [NOTE_TITLE]:</strong> [NOTE_TEXT]\n            </div>', '')
    blocks_page_1.append(aes)

    # --- Page 2 Content ---

    # Header for Page 2
    header2 = tpl_header.replace("[LESSON_NUMBER]", "27")
    header2 = header2.replace("[CHAPTER_TITLE]", "المحسنات البديعية (تابع)")
    header2 = header2.replace("[CATEGORY_HEADER]", "فوائد")
    header2 = header2.replace("[SECTION_HEADER]", "المستوى الفني")
    header2 = header2.replace("[AUTHOR_NAME]", "أ. الياس خفيف")
    header2 = header2.replace("[AUTHOR_PHONE]", "994066850 963+")
    blocks_page_2.append(header2)

    # Block 8: Tip
    tip = tpl_benefit.replace("[TIP_TITLE]", "كَيْفِيَّةُ الْإِجَابَةِ عَنْ سُؤَالِ الْقِيمَةِ الْفَنِّيَّةِ")
    tip = tip.replace("[TIP_TEXT]", """<p class="text-justify mb-2mm">إِذَا طُلِبَ مِنَ الطَّالِبِ تَوْضِيحُ الْقِيَمِ الْجَمَالِيَّةِ وَالْمَعْنَوِيَّةِ لِلطِّبَاقِ وَالْمُقَابَلَةِ بِمَقْدُورِ الطَّالِبِ إِيضَاحُهَا عَلَى النَّحْوِ الْآتِي:</p>
<p class="mb-1mm"><strong>– إِظْهَارُ الْمَعْنَى بِجَلَاءٍ وَوُضُوحٍ:</strong> أَوْضَحَ الشَّاعِرُ مِنْ خِلَالِ هَذَا الطِّبَاقِ، (أَوْ: هَذِهِ الْمُقَابَلَةِ)... [نَذْكُرُ هُنَا فِكْرَةَ الْبَيْتِ، أَوْ مَعْنَاهُ أَوْ دَلَالَتَهُ].</p>
<p class="mb-1mm"><strong>– إِثَارَةُ الْخَيَالِ:</strong> تَمَكَّنَ الشَّاعِرُ مِنْ خِلَالِ هَذَا الطِّبَاقِ، (أَوْ: هَذِهِ الْمُقَابَلَةِ) مِنْ إِثَارَةِ خَيَالِ الْمُتَلَقِّي وَجَعَلِهِ يَتَخَيَّلُ... [نَذْكُرُ هُنَا مَا يُمْكِنُ أَنْ يُثِيرَهُ الْمُحَسِّنُ مِنْ خَيَالٍ].</p>
<p class="mb-1mm"><strong>– إِعْمَالُ الْعَقْلِ فِي الْمُتَنَاقِضَاتِ:</strong> تَمَكَّنَ الشَّاعِرُ مِنْ خِلَالِ هَذَا الطِّبَاقِ، (أَوْ: هَذِهِ الْمُقَابَلَةِ) مِنْ إِعْمَالِ عَقْلِ الْمُتَلَقِّي فِي الْمُتَنَاقِضَاتِ فَجَعَلَهُ يُدْرِكُ الْفَرْقَ الشَّاسِعَ بَيْنَ حَالِ... [نَذْكُرُ هُنَا الطَّرَفَ الْأَوَّلَ مِنَ الْمُحَسِّنِ] وَحَالِ... [نَذْكُرُ هُنَا الطَّرَفَ الثَّانِي مِنَ الْمُحَسِّنِ].</p>
<p><strong>– تَحْدِيدُ الرُّؤْيَةِ (الْمَوْقِفِ):</strong> تَمَكَّنَ هَذَا الطِّبَاقُ، (أَوْ: هَذِهِ الْمُقَابَلَةُ) مِنَ الْكَشْفِ عَنْ مَوْقِفِ الشَّاعِرِ حَيْثُ أَظْهَرَ وُقُوفَهُ إِلَى جَانِبِ...</p>""")
    blocks_page_2.append(tip)

    # Block 9: Poem Verse
    poem = tpl_poem
    poem = poem.replace('<div class="block-header poem-header">\n        <span>[SECTION_TITLE]</span>\n    </div>', '<div class="block-header poem-header">\n        <span>تَطْبِيقٌ</span>\n    </div>')
    poem = poem.replace('<div class="bio-card">\n        <div class="bio-info">\n            <h4 class="m-0 text-dark">[POET_NAME]</h4>\n            <p class="mt-2mm text-sm text-grey">[POET_BIO]</p>\n        </div>\n    </div>', '')
    poem = poem.replace('<h3 class="text-center text-primary mb-4mm">[POEM_TITLE]</h3>', '')

    verse_html = """
<div class="poem-line">
    <div class="hemistich">فَتَرْفَعُ بِالْإِعْزَازِ مَنْ كَانَ جَاهِلاً</div>
    <div class="hemistich">وَتَخْفِضُ بِالْإِذْلَالِ مَنْ كَانَ يَعْقِلُ</div>
</div>
"""
    poem = poem.replace("[POEM_VERSES]", verse_html)
    blocks_page_2.append(poem)

    # Block 10: Analysis List
    anl = tpl_list.replace("[LIST_TITLE]", "تَحْلِيلُ الْبَيْتِ الشِّعْرِيِّ (جَمِيل صِدْقِي الزَّهَاوِي)")
    anl_items = """
<li><span class="font-bold text-primary">الْمُقَابَلَةُ:</span> (تَرْفَعُ، تَخْفِضُ - الْإِعْزَازُ، الْإِذْلَالُ - جَاهِلاً، يَعْقِلُ).</li>
<li><span class="font-bold text-primary">قِيمَتُهَا الْفَنِّيَّةُ:</span> اسْتَطَاعَ الشَّاعِرُ مِنْ خِلَالِ هَذِهِ الْمُقَابَلَةِ تَحْقِيقَ قِيَمٍ فَنِّيَّةٍ كَثِيرَةٍ مِنْهَا:</li>
<li><span class="font-bold text-primary">إِظْهَارُ الْمَعْنَى بِجَلَاءٍ وَوُضُوحٍ:</span> حَيْثُ أَوْضَحَ مِنْ خِلَالِ هَذِهِ الْمُقَابَلَةِ افْتِقَارَ الدَّوْلَةِ الْعُثْمَانِيَّةِ إِلَى الْإِنْصَافِ وَالْمَنْطِقِيَّةِ.</li>
<li><span class="font-bold text-primary">إِثَارَةُ الْخَيَالِ:</span> فَقَدْ تَمَكَّنَ الشَّاعِرُ مِنْ خِلَالِ هَذِهِ الْمُقَابَلَةِ مِنْ إِثَارَةِ خَيَالِ الْمُتَلَقِّي وَجَعَلَهُ يَتَخَيَّلُ حَالَةَ التَّخَبُّطِ وَالْهَمَجِيَّةِ الَّتِي اتَّصَفَتْ بِهَا سِيَاسَةُ الدَّوْلَةِ الْعُثْمَانِيَّةِ.</li>
<li><span class="font-bold text-primary">إِعْمَالُ الْعَقْلِ فِي الْمُتَنَاقِضَاتِ:</span> تَمَكَّنَ الشَّاعِرُ مِنْ خِلَالِ هَذِهِ الْمُقَابَلَةِ مِنْ إِعْمَالِ عَقْلِ الْمُتَلَقِّي فِي الْمُتَنَاقِضَاتِ فَجَعَلَهُ يُدْرِكُ الْفَرْقَ الشَّاسِعَ بَيْنَ حَالِ ارْتِفَاعِ شَأْنِ الْجَاهِلِ وَحَالِ انْخِفَاضِ شَأْنِ الْعَاقِلِ.</li>
<li><span class="font-bold text-primary">تَحْدِيدُ الرُّؤْيَةِ (الْمَوْقِفِ):</span> تَمَكَّنَتْ هَذِهِ الْمُقَابَلَةُ مِنَ الْكَشْفِ عَنْ مَوْقِفِ الشَّاعِرِ حَيْثُ أَظْهَرَتْ وُقُوفَهُ إِلَى جَانِبِ عُقَلَاءِ الْمُجْتَمَعِ الَّذِينَ هُضِمَتْ حُقُوقُهُمْ فِي ظِلِّ سِيَاسَةِ الدَّوْلَةِ الْعُثْمَانِيَّةِ.</li>
"""
    anl = anl.replace("[LIST_ITEMS]", anl_items)
    anl = anl.replace('<hr class="separator-dashed">\n            <div class="benefit-box">\n                <strong> [NOTE_TITLE]:</strong> [NOTE_TEXT]\n            </div>', '')
    blocks_page_2.append(anl)

    # Block 11: Exam
    exam_questions_data = [
        ("١", "حَدِّدِ الْبَدِيعَ فِيمَا يَأْتِي مُبَيِّنًا نَوْعَهُ، وَقِيمَتَهُ الْفَنِّيَّةَ:<br>أَنْ يَرَى فَأْرَةً فَلَمْ يَرَ شَيْئًا ... نَاكِسًا رَأْسَهُ لِطُولِ الْمَلَالَةْ<br>فَكَأَنَّ الْإِصْبَاحَ عِنْدِي لِمَا فِيـــــــهِ حَبِيبٌ رَقِيبُهُ الْإِمْسَاءُ"),
        ("٢", "أَوْرَدَ الشَّاعِرُ الطِّبَاقَ لِإِيضَاحِ الْمَعْنَى، وَإِثَارَةِ الْخَيَالِ. مَثِّلْ لِذَلِكَ مِنَ الْمَقْطَعِ الْآتِي:<br>أَبَدًا عَلَى هَذَا الطَّرِيقِ!! ... وَنَرُدُّ حَقْلاً .. شَاخَ فِيهِ الْجِذْعُ .. فِي شَرْخِ الشَّبَابِ<br>رَايَاتُنَا بَصَرُ الضَّرِيرِ .. وَصَوْتُنَا أَمَلُ الْغَرِيقْ ... وَنَصُبُّ فِي نَبْضِ الْمَصَانِعِ..<br>أَبَدًا .. جَحِيمُ عَدُوِّنَا .. أَبَدًا .. نَعِيمٌ لِلصَّدِيقْ ... لِلْمُرَبِّي .. وَالْحَقَائِبِ.. وَالثِّيَابِ"),
        ("٣", "اقْرَأ الْبَيْتَ الْآتِي ثُمَّ وَضِّحِ الْمُحَسِّنَ الْبَدِيعِيَّ (نَصَبٍ، وَصَبٍ):<br>يَا غَانِمًا بِالظَّنِّ لَا نَصَبٍ ... يُوهِي عَزِيمَتَهُ وَلَا وَصَبُ"),
        ("٤", "سُؤَالُ دَوْرَةٍ (٢٠١٤): اسْتَخْرِجْ مِنَ الْبَيْتِ مُحَسِّنًا بَدِيعِيًّا، سَمِّهِ، ثُمَّ اذْكُرْ قِيمَتَهُ الْفَنِّيَّةَ:<br>وَيُوتُوبِيَا حُلْمٌ فِي دَمِي ... أَمُوتُ وَأَحْيَا عَلَى ذِكْرِهِ"),
    ]

    exam_body = ""
    for i, (num, q_text) in enumerate(exam_questions_data):
        is_last = (i == len(exam_questions_data) - 1)
        border_class = "border-none pb-0" if is_last else ""
        margin_class = "mb-0" if is_last else ""

        q_html = f"""
        <div class="exam-question {margin_class} {border_class}">
            <p class="m-0 mb-2mm">
                <span class="exam-number">{num}</span>
                {q_text}
            </p>
            <div class="border-light h-8mm bg-grey-lighter rounded"></div>
        </div>
        """
        exam_body += q_html

    exam = tpl_exam.replace("[TOPIC]", "المحسنات البديعية")
    exam = re.sub(r'(<div class="block-body">).*?(</section>)', r'\1' + exam_body + '\n    </div>\n</section>', exam, flags=re.DOTALL)

    blocks_page_2.append(exam)

    # Generate Page 1
    full_content_1 = "\n".join(blocks_page_1)
    final_html_1 = tpl_base.replace("<!-- INJECT_CONTENT_HERE -->", full_content_1)
    # Strip IDs
    final_html_1 = final_html_1.replace('id="[BLOCK_ID]"', '')
    final_html_1 = final_html_1.replace('id="[Q1_ID]"', '')
    final_html_1 = final_html_1.replace('id="[Q2_ID]"', '')

    with open(OUTPUT_FILE_1, "w", encoding="utf-8") as f:
        f.write(final_html_1)
    print(f"Generated {OUTPUT_FILE_1}")

    # Generate Page 2
    full_content_2 = "\n".join(blocks_page_2)
    final_html_2 = tpl_base.replace("<!-- INJECT_CONTENT_HERE -->", full_content_2)
    # Strip IDs
    final_html_2 = final_html_2.replace('id="[BLOCK_ID]"', '')
    final_html_2 = final_html_2.replace('id="[Q1_ID]"', '')
    final_html_2 = final_html_2.replace('id="[Q2_ID]"', '')

    with open(OUTPUT_FILE_2, "w", encoding="utf-8") as f:
        f.write(final_html_2)
    print(f"Generated {OUTPUT_FILE_2}")

if __name__ == "__main__":
    generate_html()
