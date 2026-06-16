import os
import re

def read_template(name):
    with open(os.path.join("Jules-workspace", "Templates", name), "r", encoding="utf-8") as f:
        return f.read()

def generate_html_parts():
    # 1. Base
    base_html = read_template("TEMPLATE_C_BASE.html")

    # 2. Wrapper
    wrapper_html = read_template("TEMPLATE_C_PAGE_WRAPPER.html")

    # --- PART 1 (08.0) ---
    base_0 = base_html.replace("[PAGE_TITLE]", "حُروفُ الْجَرِّ وَعَلَاَّمَاتِ الْإِعْرَابِ الْمَجْرُورَةِ")

    # Header
    header_html = read_template("TEMPLATE_C_HEADER.html")
    header_html = header_html.replace('id="[UNIQUE_ID]"', '')
    header_html = header_html.replace("[LESSON_NUMBER]", "08")
    header_html = header_html.replace("[LEVEL_INFO]", "المستوى التأسيسي")
    header_html = header_html.replace("[TOPIC_INFO]", "علم النحو")
    header_html = header_html.replace("[MAIN_TITLE]", "حُروفُ الْجَرِّ وَعَلَاَّمَاتِ الْإِعْرَابِ الْمَجْرُورَةِ")
    header_html = header_html.replace("[AUTHOR_NAME]", "أ. الياس خفيف")
    header_html = header_html.replace("[AUTHOR_CONTACT]", "994066850 963+")

    # Block 2: Definition
    b2 = read_template("TEMPLATE_C_BLOCK.html")
    b2 = b2.replace('id="[UNIQUE_ID]"', '')
    b2 = b2.replace("[BLOCK_TITLE]", "مُقَدَّمَةً")
    b2_content = """<p class="text-accent text-center mb-2mm">"الْجَرَّ" هُو حَالَةٍ إِعْرَابِيَّةٍ خَاصَّةً بـ <span class="font-bold">الْأَسْمَاءَ فَقَط</span>؛ فلَا يُوجَدُ فعَلّ مَجْرُورٍ ولَا حَرْفِ مَجْرُورِ.</p>
<p class="text-center">مِن أَشْهُرِ مُسَبِّبَاتِ الْجَرِّ فِي اللُّغَةَ الْعَرَبِيَّةَ أَن يُسَبِّقُ الْاِسْمُ بـ (حَرْفَ جَرِّ).</p>"""
    b2 = re.sub(r'<p class="mt-1mm text-accent">\s*\[CONTENT\]\s*</p>', b2_content, b2)

    # Block 3: Table
    b3 = read_template("TEMPLATE_C_TABLE.html")
    b3 = b3.replace("[HEADER_1]", "عَلَاَّمَةُ الْجَرِّ")
    b3 = b3.replace("[HEADER_2]", "نَوْعُهَا")
    b3 = b3.replace("[HEADER_3]", "الْمَوَاضِعُ")
    b3 = b3.replace("[CELL_1]", "الْكَسْرَةَ")
    b3 = b3.replace("[CELL_2]", "أَصْلِيَّةٌ")
    b3 = b3.replace("[CELL_3]", "الْمُفْرَدُ - جَمَعَ التَّكْسيرُ - جَمَعَ الْمُؤَنَّثُ السَّالِمُ")
    b3 = b3.replace("</tr>\n        </tbody>", """</tr>
            <tr>
                <td>الياء</td>
                <td>فَرْعِيَّةٌ</td>
                <td>الْمُثَنَّى - جَمَعَ الْمُذَكَّرُ السَّالِمُ - الْأَسْمَاءُ الْخُمُسَةَ</td>
            </tr>
        </tbody>""")

    # Block 4: Deep Dive - Letters of Jar
    b4 = read_template("TEMPLATE_C_BLOCK.html")
    b4 = b4.replace('id="[UNIQUE_ID]"', '')
    b4 = b4.replace("[BLOCK_TITLE]", "مَا هِي حُروفِ الْجَرِّ ؟")
    chips_html = """<div class="flex flex-wrap gap-2mm">
    <span class="bg-grey-lighter rounded p-1mm">مِنْ</span>
    <span class="bg-grey-lighter rounded p-1mm">عَنْ</span>
    <span class="bg-grey-lighter rounded p-1mm">إِلَى</span>
    <span class="bg-grey-lighter rounded p-1mm">عَلَى</span>
    <span class="bg-grey-lighter rounded p-1mm">فِي</span>
    <span class="bg-grey-lighter rounded p-1mm">الْكَافَّ</span>
    <span class="bg-grey-lighter rounded p-1mm">اللَّاَمَ</span>
    <span class="bg-grey-lighter rounded p-1mm">الْبَاءَ</span>
</div>"""
    b4_content = f"""<p class="mb-2mm">حُروفُ الْجَرِّ سَهْلَةَ الْحِفْظِ ، وهِي:</p>
{chips_html}
<p class="mt-2mm mb-2mm">لِتَبْسِيطُ حِفْظِهَا ، قُسِّمَتْ إِلَى:</p>"""
    b4 = re.sub(r'<p class="mt-1mm text-accent">\s*\[CONTENT\]\s*</p>', b4_content, b4)

    # Block 5: Split
    b5 = read_template("TEMPLATE_C_SPLIT.html")
    b5 = b5.replace('id="[UNIQUE_ID_1]"', '')
    b5 = b5.replace('id="[UNIQUE_ID_2]"', '')
    b5 = b5.replace("[COLUMN_1_TITLE]", "حُروفَ مُنْفَصِلَةَ (تُكْتِبُ وَحْدُهَا)")
    chips1 = """<div class="flex flex-wrap gap-2mm">
    <span class="bg-grey-lighter rounded p-1mm">مِنْ</span>
    <span class="bg-grey-lighter rounded p-1mm">عَنْ</span>
    <span class="bg-grey-lighter rounded p-1mm">إِلَى</span>
    <span class="bg-grey-lighter rounded p-1mm">عَلَى</span>
    <span class="bg-grey-lighter rounded p-1mm">فِي</span>
</div>"""
    b5 = b5.replace("[COLUMN_1_CONTENT]", chips1)
    b5 = b5.replace("[COLUMN_2_TITLE]", "حُروفَ مُتَّصِلَةَ (تَتَّصِلُ بِالْاِسْمِ مُبَاشِرَةَ)")
    chips2 = """<div class="flex flex-wrap gap-2mm">
    <span class="bg-grey-lighter rounded p-1mm">الْكَافَّ</span>
    <span class="bg-grey-lighter rounded p-1mm">اللَّاَمَ</span>
    <span class="bg-grey-lighter rounded p-1mm">الْبَاءَ</span>
</div>"""
    b5 = b5.replace("[COLUMN_2_CONTENT]", chips2)

    # Block 6: Benefit Warning
    b6 = read_template("TEMPLATE_C_BENEFIT_WARNING.html")
    b6 = b6.replace('id="[UNIQUE_ID]"', '')
    b6 = b6.replace("[TITLE]", "مُلَاحِظَةَ هَامَةٍ")
    b6 = b6.replace("[CONTENT]", "اِحْذَرْ أَن تَظُنُّ أَنّ \"الواو\" أَو \"الْفَاءَ\" مِن حُروفِ الْجَرِّ ، فهِي غَالِبَا حُروفِ عَطْفِ.")

    # Block 7: Deep Dive Signs
    b7 = read_template("TEMPLATE_C_BLOCK.html")
    b7 = b7.replace('id="[UNIQUE_ID]"', '')
    b7 = b7.replace("[BLOCK_TITLE]", "عَلَاَّمَاتُ الْجَرِّ")
    b7_content = """<p class="mb-2mm">عِنْدَمَا يَأْتِي اِسْمُ بَعْد حَرْفِ الْجَرِّ ، يُعْرِبُ دَائِمَا: <span class="font-bold text-accent">(اِسْمُ مَجْرُورُ وَعُلَّامَةُ جَرِّهِ ...)</span>.</p>
<p>لُكْنٌ مَا هِي عُلَّامَةِ الْجَرِّ الْمُنَاسِبَةِ ؟ لَدَيْنَا عَلَاَّمَتَانِِ أَسَاسِيَّتَانِِ:</p>"""
    b7 = re.sub(r'<p class="mt-1mm text-accent">\s*\[CONTENT\]\s*</p>', b7_content, b7)

    # Block 8: Kasra
    b8 = read_template("TEMPLATE_C_BLOCK.html")
    b8 = b8.replace('id="[UNIQUE_ID]"', '')
    b8 = b8.replace("[BLOCK_TITLE]", "أ. الْكَسْرَةَ (وهِي الْعُلَّامَةِ الْأَصْلِيَّةِ)")
    list1_html = """<ul class="structured-list">
    <li><span class="marker">•</span> <span><span class="font-bold">الْمُفْرَدُ:</span> وَضَعَ الطَّالِبُ الْكِتَابَ <span class="highlight-blue">عَلَى</span> <span class="highlight-red">الْمَكْتَبِ</span>.</span></li>
    <li><span class="marker">•</span> <span><span class="font-bold">جَمَعَ التَّكْسيرُ:</span> يَبْحَثُ الصَّيَّادُ <span class="highlight-blue">عَن</span> <span class="highlight-red">الْأَسْمَاكِ</span>.</span></li>
    <li><span class="marker">•</span> <span><span class="font-bold">جَمَعَ الْمُؤَنَّثُ السَّالِمُ:</span> أَخَذْتُ الْأبْحَاثَ <span class="highlight-blue">مِن</span> <span class="highlight-red">الطَّالِبَاتِ</span>.</span></li>
</ul>"""
    b8_content = f"""<p class="mb-2mm">تَأْتِي الْكَسْرَةُ مَع ثَلَاثَةِ أَنْوَاعٍ مِن الْأَسْمَاءِ:</p>
{list1_html}"""
    b8 = re.sub(r'<p class="mt-1mm text-accent">\s*\[CONTENT\]\s*</p>', b8_content, b8)

    # Block 9: Irab Row 1
    b9 = read_template("TEMPLATE_C_IRAB_ROW.html")
    b9 = b9.replace('id="[UNIQUE_ID_1]"', '').replace('id="[UNIQUE_ID_2]"', '')
    b9 = b9.replace("[WORD_1]", "عَلَى الْمَكْتَبِ")
    b9 = b9.replace("[DETAILS_1]", "<span class=\"highlight-blue\">عَلَى</span>: حَرْفُ جَرٍّ. <span class=\"highlight-red\">الْمَكْتَبِ</span>: اِسْمُ مَجْرُورُ بِالْكَسْرَةِ.")
    b9 = b9.replace("[WORD_2]", "عَن الْأَسْمَاكِ")
    b9 = b9.replace("[DETAILS_2]", "<span class=\"highlight-blue\">عَنْ</span>: حَرْفُ جَرٍّ. <span class=\"highlight-red\">الْأَسْمَاكِ</span>: اِسْمُ مَجْرُورُ بِالْكَسْرَةِ.")

    # Block 10: Irab Row 2
    b10 = read_template("TEMPLATE_C_IRAB.html")
    b10 = b10.replace('id="[UNIQUE_ID]"', '')
    b10 = b10.replace("[TARGET_WORD]", "مِن الطَّالِبَاتِ")
    b10 = b10.replace("[IRAB_ANALYSIS]", "<span class=\"highlight-blue\">مِنْ</span>: حَرْفُ جَرٍّ. <span class=\"highlight-red\">الطَّالِبَاتِ</span>: اِسْمُ مَجْرُورُ بِالْكَسْرَةِ.")

    # Move Block 11, 12, 13 to Part 1 to fix UNDERFLOW in Part 1 and UNDERFLOW in Part 2.
    # Block 11: Yaa
    b11 = read_template("TEMPLATE_C_BLOCK.html")
    b11 = b11.replace('id="[UNIQUE_ID]"', '')
    b11 = b11.replace("[BLOCK_TITLE]", "ب. الياء (وهِي عُلَّامَةٍ فَرْعِيَّةٍ)")
    list2_html = """<ul class="structured-list">
    <li><span class="marker">•</span> <span><span class="font-bold">الْمُثَنَّى:</span> أَلْقَيْتُ مُحَاضَرَاتٍ <span class="highlight-blue">فِي</span> <span class="highlight-red">الْمُدَرِّسَتَيْنِ</span>.</span></li>
    <li><span class="marker">•</span> <span><span class="font-bold">جَمَعَ الْمُذَكَّرُ السَّالِمُ:</span> أَعْطَيْتُ الْهَدَايَا <span class="highlight-blue">لِـ</span><span class="highlight-red">لْمُتَمَيِّزِينَ</span>.</span></li>
    <li><span class="marker">•</span> <span><span class="font-bold">الْأَسْمَاءُ الْخُمُسَةَ:</span> ذَهَبْتُ <span class="highlight-blue">إِلَى</span> <span class="highlight-red">أَبِيكَ</span> وَأَخِيكَ.</span></li>
</ul>"""
    b11_content = f"""<p class="mb-2mm">تَأْتِي الياء مَع ثَلَاثَةِ أَنْوَاعٍ مِن الْأَسْمَاءِ أيضاً:</p>
{list2_html}"""
    b11 = re.sub(r'<p class="mt-1mm text-accent">\s*\[CONTENT\]\s*</p>', b11_content, b11)

    # Block 12: Irab Yaa Row 1
    b12 = read_template("TEMPLATE_C_IRAB_ROW.html")
    b12 = b12.replace('id="[UNIQUE_ID_1]"', '').replace('id="[UNIQUE_ID_2]"', '')
    b12 = b12.replace("[WORD_1]", "فِي الْمُدَرِّسَتَيْنِ")
    b12 = b12.replace("[DETAILS_1]", "<span class=\"highlight-blue\">فِي</span>: حَرْفُ جَرٍّ. <span class=\"highlight-red\">الْمَدْرَسَتَيْنِ</span>: مَجْرُورُ بالياء ، وَنَوَّنَهُ مَكْسُورَةُ.")
    b12 = b12.replace("[WORD_2]", "لِلْمُتَمَيِّزِينَ")
    b12 = b12.replace("[DETAILS_2]", "<span class=\"highlight-blue\">اللَّاَمُ</span> حَرْفَ جَرٍّ ، وَ<span class=\"highlight-red\">الْمُتَمَيِّزِينَ</span> مَجْرُورَ بالياء ، وَنَوَّنَهُ مَفْتُوحَةُ.")

    # Compose Part 1 (Blocks 1 to 11) - Moving 12 out due to overflow
    content_0 = "\n".join([header_html, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11])
    final_html_0 = wrapper_html.replace("<!-- Content components go here -->", content_0)
    final_html_0 = base_0.replace("<!-- Content components go here -->", final_html_0)

    # --- PART 2 (08.1) ---
    base_1 = base_html.replace("[PAGE_TITLE]", "حُروفُ الْجَرِّ وَعَلَاَّمَاتِ الْإِعْرَابِ الْمَجْرُورَةِ (تابع)")

    # Header for Part 2
    header_html_1 = read_template("TEMPLATE_C_HEADER.html")
    header_html_1 = header_html_1.replace('id="[UNIQUE_ID]"', '')
    header_html_1 = header_html_1.replace("[LESSON_NUMBER]", "08")
    header_html_1 = header_html_1.replace("[LEVEL_INFO]", "المستوى التأسيسي")
    header_html_1 = header_html_1.replace("[TOPIC_INFO]", "علم النحو")
    header_html_1 = header_html_1.replace("[MAIN_TITLE]", "حُروفُ الْجَرِّ وَعَلَاَّمَاتِ الْإِعْرَابِ الْمَجْرُورَةِ (تابع)")
    header_html_1 = header_html_1.replace("[AUTHOR_NAME]", "أ. الياس خفيف")
    header_html_1 = header_html_1.replace("[AUTHOR_CONTACT]", "994066850 963+")

    # Block 13: Irab Yaa Row 2
    b13 = read_template("TEMPLATE_C_IRAB.html")
    b13 = b13.replace('id="[UNIQUE_ID]"', '')
    b13 = b13.replace("[TARGET_WORD]", "إِلَى أَبِيكَ")
    b13 = b13.replace("[IRAB_ANALYSIS]", "<span class=\"highlight-blue\">إِلَى</span>: حَرْفُ جَرٍّ. <span class=\"highlight-red\">أَبِيكَ</span>: مَجْرُورُ بالياء لأَنّهُ مِن الْأَسْمَاءِ الْخُمُسَةَ.")

    # Exam Header
    exam_header = """<section class="content-block">
    <div class="block-header bg-dark">
        <span>اخْتَبِرْ نَفْسَكَ</span>
    </div>
    <div class="block-body">"""

    # Block 14: Exam Part 1
    b14 = read_template("TEMPLATE_C_EXAM.html")
    b14 = b14.replace('id="[UNIQUE_ID]"', '')
    b14 = b14.replace("[QUESTION_NUMBER]", "١")
    b14 = b14.replace("[QUESTION_TEXT]", "اِسْتَخْرَجَ حَرْفُ الْجَرِّ وَالْاِسْمِ الْمَجْرُورِ وَبَيِّنِ عَلَاَّمَةِ جَرِّهِ وَالسَّبَبِ فِي الْجَمَلِ الْآتِيَةِ : ١. يَبْدُو وَجْهُ الطِّفْلِ كَالْْبَدْرِ . ٢. يَفْخُرُ الْمُعَلِّمُ بِالطَّالِبَيْنِ الْمُتَفَوِّقِينَ . ٣. شَرَحْتُ الدَّرْسَ فِي الْفَصْلَيْنِ .")

    # Block 15: Exam Part 2
    b15 = read_template("TEMPLATE_C_EXAM.html")
    b15 = b15.replace('id="[UNIQUE_ID]"', '')
    b15 = b15.replace("[QUESTION_NUMBER]", "٢")
    b15 = b15.replace("[QUESTION_TEXT]", "صَحَّحَ الْخَطَأُ فِي الْجَمَلِ الْآتِيَةِ : ١. سَلَّمْتُ عَلَى الْمُهَنْدِسُونَ فِي الْمَوْقِعِ . ٢. أَخَذْتُ الْقَلَمَ مِن أَخُوكَ .")

    # We have underflow on part 2. We can add a benefit tip to take up space.
    # The rule says: "When verify_layout.py reports an UNDERFLOW status, dynamically add relevant TEMPLATE_C_BENEFIT or TEMPLATE_C_BENEFIT_TIP components to the HTML to fill the remaining height and satisfy the strict visual density constraint."
    benefit_tip = read_template("TEMPLATE_C_BENEFIT_TIP.html")
    benefit_tip = benefit_tip.replace('id="[UNIQUE_ID]"', '')
    benefit_tip = benefit_tip.replace("[TITLE]", "فَائِدَةٌ ذَهَبِيَّةٌ")
    benefit_tip = benefit_tip.replace("[CONTENT]", "حُروفُ الْجَرِّ لَا تَدْخُلُ عَلَى الْأَفْعَالِ مُطْلَقًا، فَإِذَا رَأَيْتَ حَرْفَ جَرٍّ فَاعْلَمْ أَنَّ مَا بَعْدَهُ اسْمٌ وَإِنْ لَمْ يَكُنْ فِيهِ عَلَامَةٌ مِنْ عَلَامَاتِ الِاسْمِ الْأُخْرَى كَالْأَلِفِ وَاللَّامِ أَوِ التَّنْوِينِ.")

    benefit_2 = read_template("TEMPLATE_C_BENEFIT.html")
    benefit_2 = benefit_2.replace('id="[UNIQUE_ID]"', '')
    benefit_2 = benefit_2.replace("[TITLE]", "مَعْلُومَةٌ إِضَافِيَّةٌ")
    benefit_2 = benefit_2.replace("[CONTENT]", "هُنَاكَ حُروفُ جَرٍّ أُخْرَى فِي اللُّغَةِ الْعَرَبِيَّةِ لَمْ نَذْكُرْهَا هُنَا لِلتَّبْسِيطِ، مِثْلَ: رُبَّ، وَمُذْ، وَمُنْذُ، وَحَتَّى. وَلَكِنَّ الْمَذْكُورَةَ هِيَ الْأَكْثَرُ اسْتِخْدَامًا.")

    # We can also add another exam question to take up more space.
    b16 = read_template("TEMPLATE_C_EXAM.html")
    b16 = b16.replace('id="[UNIQUE_ID]"', '')
    b16 = b16.replace("[QUESTION_NUMBER]", "٣")
    b16 = b16.replace("[QUESTION_TEXT]", "أَعْرِبْ مَا تَحْتَهُ خَطٌّ فِي الْجُمْلَةِ الْآتِيَةِ إِعْرَابًا تَامًّا: ذَهَبْتُ إِلَى <u class=\"highlight-red\">أَخِيكَ</u> الْمَرِيضِ.")

    # Let's add more questions and benefits
    b17 = read_template("TEMPLATE_C_EXAM.html")
    b17 = b17.replace('id="[UNIQUE_ID]"', '')
    b17 = b17.replace("[QUESTION_NUMBER]", "٤")
    b17 = b17.replace("[QUESTION_TEXT]", "مَثِّلْ فِي جُمَلٍ مُفِيدَةٍ لِمَا يَأْتِي: ١. اسْمٌ مَجْرُورٌ بِالْكَسْرَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ. ٢. اسْمٌ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.")

    b18 = read_template("TEMPLATE_C_EXAM.html")
    b18 = b18.replace('id="[UNIQUE_ID]"', '')
    b18 = b18.replace("[QUESTION_NUMBER]", "٥")
    b18 = b18.replace("[QUESTION_TEXT]", "اخْتَرْ الْإِجَابَةَ الصَّحِيحَةَ مِمَّا بَيْنَ الْقَوْسَيْنِ: نَظَرْتُ إِلَى (النَّجْمَتَانِ / النَّجْمَتَيْنِ) فِي السَّمَاءِ.")

    b19 = read_template("TEMPLATE_C_EXAM.html")
    b19 = b19.replace('id="[UNIQUE_ID]"', '')
    b19 = b19.replace("[QUESTION_NUMBER]", "٦")
    b19 = b19.replace("[QUESTION_TEXT]", "اقْرَأِ الْفِقْرَةَ الْآتِيَةَ ثُمَّ اسْتَخْرِجْ مِنْهَا كُلَّ حَرْفِ جَرٍّ وَالِاسْمَ الْمَجْرُورَ بَعْدَهُ: ذَهَبَ الطَّالِبُ إِلَى الْمَدْرَسَةِ مُبَكِّرًا، وَسَلَّمَ عَلَى الْمُعَلِّمِينَ، ثُمَّ جَلَسَ فِي الْفَصْلِ بِانْتِبَاهٍ يَسْتَمِعُ لِلدَّرْسِ.")

    b20 = read_template("TEMPLATE_C_EXAM.html")
    b20 = b20.replace('id="[UNIQUE_ID]"', '')
    b20 = b20.replace("[QUESTION_NUMBER]", "٧")
    b20 = b20.replace("[QUESTION_TEXT]", "أَكْمِلِ الْفَرَاغَاتِ الْآتِيَةَ بِحَرْفِ جَرٍّ مُنَاسِبٍ: عَادَ الْمُسَافِرُ ___ السَّفَرِ مُتْعَبًا. ابْتَعِدْ ___ الرِّفَاقِ السُّوءِ.")

    b21 = read_template("TEMPLATE_C_EXAM.html")
    b21 = b21.replace('id="[UNIQUE_ID]"', '')
    b21 = b21.replace("[QUESTION_NUMBER]", "٨")
    b21 = b21.replace("[QUESTION_TEXT]", "هَلْ يَجُوزُ أَنْ نَقُولَ: ذَهَبْتُ إِلَى يَلْعَبُ؟ وَلِمَاذَا؟")

    exam_footer = "</div></section>"

    # Compose Part 2 (Block 12 + Block 13 + Benefit Tip + Benefit 2 + Exam)
    content_1 = "\n".join([header_html_1, b12, b13, benefit_tip, benefit_2, exam_header, b14, b15, b16, b17, b18, b19, b20, b21, exam_footer])
    final_html_1 = wrapper_html.replace("<!-- Content components go here -->", content_1)
    final_html_1 = base_1.replace("<!-- Content components go here -->", final_html_1)

    # Write output
    with open("pages/08.0_nXX_حُروفُ الْجَرِّ وَعَلَاَّمَاتِ الْإِعْرَابِ الْمَجْرُورَةِ.html", "w", encoding="utf-8") as f:
        f.write(final_html_0)

    with open("pages/08.1_nXX_حُروفُ الْجَرِّ وَعَلَاَّمَاتِ الْإِعْرَابِ الْمَجْرُورَةِ.html", "w", encoding="utf-8") as f:
        f.write(final_html_1)

if __name__ == "__main__":
    generate_html_parts()
