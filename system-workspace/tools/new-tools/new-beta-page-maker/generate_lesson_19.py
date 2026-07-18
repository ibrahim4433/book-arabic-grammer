import os
import random
import re
import string

# Configuration
OUTPUT_FILE_19_0 = "pages/19.0_nXX_الهمزة المتطرفة.html"
OUTPUT_FILE_19_1 = "pages/19.1_nXX_الهمزة المتطرفة.html"
TEMPLATES_DIR = "Jules-workspace/Templates/"


def load_template(filename):
    with open(os.path.join(TEMPLATES_DIR, filename), encoding="utf-8") as f:
        return f.read()


def generate_id():
    return "b" + "".join(random.choices(string.digits, k=5))


def create_header(lesson_number, chapter_title, category, section, author_name, author_phone):
    template = load_template("TEMPLATE_C_HEADER.html")
    content = template.replace("[LESSON_NUMBER]", str(lesson_number))
    content = content.replace("[CHAPTER_TITLE]", chapter_title)
    content = content.replace("[CATEGORY_HEADER]", category)
    content = content.replace("[SECTION_HEADER]", section)
    content = content.replace("[AUTHOR_NAME]", author_name)
    content = content.replace("[AUTHOR_PHONE]", author_phone)
    return content


def create_block(title, content, benefit_title=None, benefit_text=None):
    template = load_template("TEMPLATE_C_BLOCK.html")
    template = template.replace("[BLOCK_ID]", generate_id())
    template = template.replace("[BLOCK_TITLE]", title)
    template = template.replace("[CONTENT_TEXT]", content)

    if benefit_title and benefit_text:
        template = template.replace("[BENEFIT_TITLE]", benefit_title)
        template = template.replace("[BENEFIT_TEXT]", benefit_text)
    else:
        # Remove benefit box if not used
        template = re.sub(r'<div class="benefit-box">.*?</div>', "", template, flags=re.DOTALL)

    return template


def create_table(title, headers, rows):
    template = load_template("TEMPLATE_C_TABLE.html")
    template = template.replace("[BLOCK_ID]", generate_id())
    template = template.replace("[TABLE_TITLE]", title)

    header_html = "".join([f"<th>{h}</th>" for h in headers])
    template = template.replace("[TABLE_HEADERS]", header_html)

    rows_html = ""
    for row in rows:
        row_html = "<tr>" + "".join([f"<td>{cell}</td>" for cell in row]) + "</tr>"
        rows_html += row_html
    template = template.replace("[TABLE_ROWS]", rows_html)

    return template


def create_chips(title, chips):
    block_template = """
    <section class="content-block" id="[BLOCK_ID]">
        <div class="block-header">
            <span>[BLOCK_TITLE]</span>
        </div>
        <div class="block-body">
            [CONTENT]
        </div>
    </section>
    """

    chips_html = ""
    for chip in chips:
        chip_html = f'<div class="bg-grey-lighter rounded p-1mm">{chip}</div>'
        chips_html += chip_html

    chips_content = load_template("TEMPLATE_C_CHIPS.html").replace("[CHIPS_CONTENT]", chips_html)

    full_block = block_template.replace("[BLOCK_ID]", generate_id())
    full_block = full_block.replace("[BLOCK_TITLE]", title)
    full_block = full_block.replace("[CONTENT]", chips_content)

    return full_block


def create_split(left_title, left_content, right_title, right_content):
    template = load_template("TEMPLATE_C_SPLIT.html")
    template = template.replace("[LEFT_TITLE]", left_title)
    template = template.replace("[LEFT_CONTENT]", left_content)
    template = template.replace("[RIGHT_TITLE]", right_title)
    template = template.replace("[RIGHT_CONTENT]", right_content)

    return template


def create_benefit(title, text):
    template = load_template("TEMPLATE_C_BENEFIT.html")
    template = template.replace("[BENEFIT_TITLE]", title)
    template = template.replace("[BENEFIT_TEXT]", text)
    return template


def create_list(title, items, note_title=None, note_text=None):
    template = load_template("TEMPLATE_C_LIST.html")
    template = template.replace("[LIST_TITLE]", title)

    list_items_html = ""
    for item in items:
        item_html = load_template("TEMPLATE_C_LIST_ITEM.html")
        item_html = item_html.replace("[CONTENT]", item)
        item_html = item_html.replace("[MARKER]", ".")
        list_items_html += item_html

    template = template.replace("[LIST_ITEMS]", list_items_html)

    if note_title and note_text:
        template = template.replace("[NOTE_TITLE]", note_title)
        template = template.replace("[NOTE_TEXT]", note_text)
    else:
        template = re.sub(r'<div class="benefit-box">.*?</div>', "", template, flags=re.DOTALL)
        template = template.replace('<hr class="separator-dashed">', "")

    return template


def create_exam(number_1, question_1, number_2, question_2, topic):
    template = load_template("TEMPLATE_C_EXAM.html")
    template = template.replace("[BLOCK_ID]", generate_id())
    template = template.replace("[TOPIC]", topic)
    template = template.replace("[Q1_ID]", generate_id())
    template = template.replace("[Q2_ID]", generate_id())

    parts = template.split("[QUESTION_TEXT]")
    if len(parts) == 3:
        template = parts[0] + question_1 + parts[1] + question_2 + parts[2]
    else:
        template = template.replace("[QUESTION_TEXT]", question_1, 1)
        template = template.replace("[QUESTION_TEXT]", question_2, 1)

    return template


def create_irab(sentence, word_analysis_list):
    template = load_template("TEMPLATE_C_IRAB.html")
    # Remove irab-stack if not in CSS
    template = template.replace('class="irab-stack"', 'class="flex flex-col gap-2mm"')

    template = template.replace("[SENTENCE_TO_PARSE]", sentence)

    boxes_html = ""
    for word, analysis in word_analysis_list:
        box_template = load_template("TEMPLATE_C_IRAB_BOX.html")
        box_template = box_template.replace("[WORD]", word)
        box_template = box_template.replace("[PARSING_DETAILS]", analysis)
        boxes_html += box_template

    template = template.replace("[IRAB_BOXES]", boxes_html)
    return template


def main():
    # --- PAGE 1 CONTENT ---
    blocks_p1 = []

    # Block 1: Header
    blocks_p1.append(
        create_header(19, "الْهَمْزَةُ الْمُتَطَرِّفَةُ", "الإملاء", "المستوى اللغوي", "أ. حنا خفيف", " ")
    )

    # Block 2: Definition
    content_b2 = """
<p class="text-justify">
    <span class="text-accent font-bold">الْهَمْزَةُ الْمُتَطَرِّفَةُ:</span> هِيَ الَّتِي تُكْتَبُ فِي <span class="highlight-red">آخِرِ الْكَلِمَةِ</span>.
    <br><br>
    <span class="font-bold text-primary">الْقَاعِدَةُ الْعَامَّةُ:</span> تُكْتَبُ الْهَمْزَةُ الْمُتَطَرِّفَةُ بِحَسَبِ <span class="highlight-blue">حَرَكَةِ الْحَرْفِ الَّذِي يَسْبِقُهَا</span> (لَا يُنْظَرُ إِلَى حَرَكَةِ الْهَمْزَةِ نَفْسِهَا)، وَذَلِكَ عَلَى النَّحْوِ الآتِي:
</p>
"""
    blocks_p1.append(create_block("تَعْرِيفُ الْهَمْزَةِ الْمُتَطَرِّفَةِ وَقَاعِدَتُهَا", content_b2))

    # Block 3: Matrix
    headers_b3 = ["حَرَكَةُ مَا قَبْلَهَا", "الْحَرْفُ الْمُنَاسِبُ", "صُورَةُ الْكِتَابَةِ", "أَمْثِلَةٌ تَوْضِيحِيَّةٌ"]
    rows_b3 = [
        [
            "الْكَسْرَةُ (ــِـ)",
            "الْيَاءُ غَيْرُ الْمَنْقُوطَةِ",
            '<span class="font-bold text-primary">ـئ</span>',
            '<span class="highlight-red">يُومِئ</span>، شَاطِئ، قَارِئ',
        ],
        [
            "الضَّمَّةُ (ــُـ)",
            "الْوَاوُ",
            '<span class="font-bold text-primary">ـؤ</span>',
            '<span class="highlight-red">تَبَاطُؤ</span>، لُؤْلُؤ، تَكـَافُؤ',
        ],
        [
            "الْفَتْحَةُ (ــَـ)",
            "الْأَلِفُ",
            '<span class="font-bold text-primary">ـأ</span>',
            '<span class="highlight-red">الْمَبْدَأ</span>، قَرَأَ، نَشَأَ',
        ],
        [
            "السُّكُونُ (ــْـ)",
            "السَّطْرُ (مُنْفَرِدَةً)",
            '<span class="font-bold text-primary">ء</span>',
            '<span class="highlight-red">دِفْء</span>، عِبْء، شَيْء، هُدُوء',
        ],
    ]
    blocks_p1.append(create_table("مَوَاضِعُ كِتَابَةِ الْهَمْزَةِ الْمُتَطَرِّفَةِ", headers_b3, rows_b3))

    # Block 4: Examples with Chips
    chips_b4 = [
        '<span class="font-bold">مَكْسُورٌ مَا قَبْلَهَا:</span> يُومِئ، يُكَافِئ',
        '<span class="font-bold">مَضْمُومٌ مَا قَبْلَهَا:</span> تَبَاطُؤ، يَجْرُؤ',
        '<span class="font-bold">مَفْتُوحٌ مَا قَبْلَهَا:</span> الْمَبْدَأ، يَلْجَأ',
        '<span class="font-bold">سَاكِنٌ مَا قَبْلَهَا:</span> دِفْء، بُطْء',
    ]
    blocks_p1.append(create_chips("أَمْثِلَةٌ إِضَافِيَّةٌ لِلتَّرْسِيخِ", chips_b4))

    # Block 5: Deep Dive
    content_b5 = """
<p class="text-justify">
    عِنْدَ تَثْنِيَةِ الْكَلِمَةِ الْمُنْتَهِيَةِ بِهَمْزَةٍ مُتَطَرِّفَةٍ، يَجِبُ التَّمْيِيزُ بَيْنَ <span class="highlight-blue">الِاسْمِ</span> وَ <span class="highlight-blue">الْفِعْلِ</span>، وَمُرَاعَاةُ حَالَةِ الْحَرْفِ السَّابِقِ لِلْهَمْزَةِ (مِنْ حَيْثُ الِاتِّصَالُ وَالِانْفِصَالُ).
</p>
"""
    blocks_p1.append(create_block("تَنْبِيهَاتٌ: اجْتِمَاعُ الْهَمْزَةِ الْمُتَطَرِّفَةِ مَعَ أَلِفِ التَّثْنِيَةِ", content_b5))

    # Block 6: Dual Alif Cases (Split View)
    left_content_b6 = """
    <ul class="structured-list">
        <li><span class="marker">.</span><span>تَبْقَى الْهَمْزَةُ الْمُتَطَرِّفَةُ الْمَرْسُومَةُ عَلَى أَلِفٍ <span class="font-bold">عَلَى حَالِهَا</span>.</span></li>
        <li><span class="marker">.</span><span>تُكْتَبُ بَعْدَهَا أَلِفُ التَّثْنِيَةِ دُونَ دَمْجٍ.</span></li>
        <li><span class="marker">.</span><span><span class="highlight-red">مِثَالٌ:</span> بَدَأَ &#8592; <span class="font-bold text-primary">بَدَأَا</span>.</span></li>
        <li><span class="marker">.</span><span><span class="font-bold text-accent">تَنْبِيهٌ:</span> فِي الْمُضَارِعِ، يَجِبُ الانْتِبَاهُ لِثُبُوتِ النُّونِ (يَلْجَأ &#8592; <span class="font-bold">يَلْجَأَانِ</span>).</span></li>
    </ul>
    """

    right_content_b6 = """
    <ul class="structured-list">
        <li><span class="marker">.</span><span>إِذَا كَانَتِ الْهَمْزَةُ عَلَى أَلِفٍ، تَتَحَوَّلُ مَعَ أَلِفِ التَّثْنِيَةِ إِلَى <span class="highlight-red">مَدَّةٍ (آ)</span>.</span></li>
        <li><span class="marker">.</span><span><span class="highlight-red">مِثَالٌ:</span> مَلْجَأ &#8592; <span class="font-bold text-primary">مَلْجَآنِ</span>.</span></li>
        <li><span class="marker">.</span><span>مِثَالٌ آخَرُ: مَبْدَأ &#8592; <span class="font-bold text-primary">مَبْدَآنِ</span>.</span></li>
    </ul>
    """

    blocks_p1.append(create_split("فِي الْأَفْعَالِ", left_content_b6, "فِي الْأَسْمَاءِ", right_content_b6))

    # Block 7: Hamza on Line with Dual Alif
    headers_b7 = ["الْحَالَةُ", "الْقَاعِدَةُ", "الْمِثَالُ", "التَّعْلِيلُ"]
    rows_b7 = [
        [
            'مَا قَبْلَهَا <span class="text-accent">لَا يَتَّصِلُ</span>',
            "تَبْقَى عَلَى السَّطْرِ مُنْفَرِدَةً",
            '<span class="font-bold">جُزْءَانِ</span>، نِدَاءَانِ',
            "الْحَرْفُ السَّابِقُ (الزَّاي/الْأَلِف) لَا يَقْبَلُ الْوَصْلَ.",
        ],
        [
            'مَا قَبْلَهَا <span class="text-primary">يَتَّصِلُ</span>',
            "تُكْتَبُ عَلَى نَبْرَةٍ (ـئـ)",
            '<span class="font-bold">شَيْئَانِ</span>، فَيْئَانِ، عِبْئَانِ',
            "الْحَرْفُ السَّابِقُ (الْيَاء/الْبَاء) يَقْبَلُ الْوَصْلَ بِمَا بَعْدَهُ.",
        ],
    ]
    blocks_p1.append(create_table("حُكْمُ الْهَمْزَةِ الْمُتَطَرِّفَةِ عَلَى السَّطْرِ مَعَ التَّثْنِيَةِ", headers_b7, rows_b7))

    # Block 8: Benefit
    benefit_text_b8 = """
إِذَا كَانَتِ الْهَمْزَةُ الْمُتَطَرِّفَةُ مَرْسُومَةً عَلَى <span class="highlight-blue">الْوَاوِ</span> أَوْ عَلَى <span class="highlight-blue">يَاءٍ</span>، وَلَحِقَتْ بِهَا أَلِفُ التَّثْنِيَةِ، نُطَبِّقُ عَلَيْهَا <span class="font-bold">قَاعِدَةَ الْهَمْزَةِ الْمُتَوَسِّطَةِ</span> (أَقْوَى الْحَرَكَتَيْنِ).
<br>
<span class="highlight-red">أَمْثِلَةٌ:</span> لُؤْلُؤ &#8592; <span class="font-bold">لُؤْلُؤَانِ</span> | مُبْطِئ &#8592; <span class="font-bold">مُبْطِئَانِ</span>.
"""
    blocks_p1.append(create_benefit("فَائِدَةٌ: الْهَمْزَةُ عَلَى الْوَاوِ وَالْيَاءِ", benefit_text_b8))

    # Extra Chips to fill Page 1
    chips_extra_p1 = [
        '<span class="font-bold">بَدْء &#8592; بَدْءَانِ</span> (تَبْقَى عَلَى السَّطْرِ)',
        '<span class="font-bold">عِبْء &#8592; عِبْئَانِ</span> (تُوصَلُ بِمَا قَبْلَهَا)',
        '<span class="font-bold">مِلْء &#8592; مِلْءَانِ</span> (مِثْلُ عِبْء)',
        '<span class="font-bold">دِفْء &#8592; دِفْءَانِ</span> (مِثْلُ شَيْء)',
    ]
    blocks_p1.append(create_chips("تَدْرِيبَاتٌ إِضَافِيَّةٌ عَلَى التَّثْنِيَةِ", chips_extra_p1))

    # Irab (Page 1)
    irab_p1 = [
        ("يَلْجَأُ", "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ عَلَى آخِرِهِ (الْهَمْزَة)."),
        ("الْمُؤْمِنُ", "فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ عَلَى آخِرِهِ."),
    ]
    blocks_p1.append(create_irab("يَلْجَأُ الْمُؤْمِنُ إِلَى رَبِّهِ.", irab_p1))

    # --- PAGE 2 CONTENT ---
    blocks_p2 = []

    # Block 9: Header (Continuation)
    blocks_p2.append(
        create_header(19, "الْهَمْزَةُ الْمُتَطَرِّفَةُ ", "الإملاء", "المستوى اللغوي", "أ. حنا خفيف", " ")
    )

    # Block 9: Tanween al-Nasb Introduction
    content_b9 = """
<p class="text-justify">
    عِنْدَ تَنْوِينِ الْكَلِمَةِ الْمُنْتَهِيَةِ بِهَمْزَةٍ مُتَطَرِّفَةٍ <span class="highlight-blue">تَنْوِينَ نَصْبٍ</span>، نَنْظُرُ إِلَى الْحَرْفِ الَّذِي يَسْبِقُ الْهَمْزَةَ، أَوْ مَوْضِعِ كِتَابَةِ الْهَمْزَةِ.
</p>
"""
    blocks_p2.append(create_block("الْهَمْزَةُ الْمُتَطَرِّفَةُ مَعَ تَنْوِينِ النَّصْبِ", content_b9))

    # Block 10: Tanween Rules (Detailed)
    items_b10 = [
        '<span class="font-bold text-accent">إِذَا سُبِقَتْ بِأَلِفٍ:</span> يُرْسَمُ التَّنْوِينُ عَلَى الْهَمْزَةِ مُبَاشَرَةً دُونَ أَلِفٍ إِضَافِيَّةٍ (كَرَاهَةَ اجْتِمَاعِ أَلِفَيْنِ). <span class="highlight-red">مِثَالٌ:</span> <span class="font-bold">سَمَاءً، نِدَاءً</span>.',
        '<span class="font-bold text-accent">إِذَا كُتِبَتْ عَلَى أَلِفٍ:</span> يُرْسَمُ التَّنْوِينُ فَوْقَهَا مُبَاشَرَةً. <span class="highlight-red">مِثَالٌ:</span> <span class="font-bold">مَبْدَأً، خَطَأً</span>.',
        '<span class="font-bold text-primary">إِذَا لَمْ تُسْبَقْ بِأَلِفٍ:</span> تُرْسَمُ أَلِفُ التَّنْوِينِ بَعْدَهَا. وَلَهَا حَالَتَانِ:</span><ul class="structured-list"><li><span class="marker">.</span><span><span class="font-bold">غَيْرُ مُتَّصِلٍ:</span> إِذَا كَانَ مَا قَبْلَهَا لَا يَتَّصِلُ، تَبْقَى عَلَى السَّطْرِ. نَحْو: <span class="font-bold">جُزْءًا، بَدْءًا</span>.</span></li><li><span class="marker">.</span><span><span class="font-bold">مُتَّصِلٌ:</span> إِذَا كَانَ مَا قَبْلَهَا يَتَّصِلُ، تُكْتَبُ عَلَى نَبْرَةٍ. نَحْو: <span class="font-bold">شَيْئًا، عِبْئًا</span>.</span></li></ul><span>',
    ]
    blocks_p2.append(create_list("حَالَاتُ كِتَابَةِ تَنْوِينِ النَّصْبِ", items_b10))

    # Block 11: Reasonings (Q&A)
    left_content_b11 = """
<div class="block-body">
    <p class="text-justify">
    <strong>لِمَ كُتِبَتْ (شَيْئَانِ) عَلَى نَبْرَةٍ وَ(جُزْءَانِ) عَلَى السَّطْرِ؟</strong><br><br>
    <span class="font-bold highlight-red">جُزْءَانِ:</span> هَمْزَةٌ مُتَطَرِّفَةٌ اجْتَمَعَتْ مَعَ أَلِفِ التَّثْنِيَةِ، وَالْحَرْفُ الَّذِي قَبْلَهَا (الزَّاي) <span class="text-accent">لَا يَقْبَلُ الْوَصْلَ</span> بِمَا بَعْدَهُ.<br>
    <span class="font-bold highlight-red">شَيْئَانِ:</span> هَمْزَةٌ مُتَطَرِّفَةٌ اجْتَمَعَتْ مَعَ أَلِفِ التَّثْنِيَةِ، وَالْحَرْفُ الَّذِي قَبْلَهَا (الْيَاء) <span class="text-accent">يَقْبَلُ الْوَصْلَ</span> بِمَا بَعْدَهُ.
    </p>
</div>
"""
    right_content_b11 = """
<div class="block-body">
    <p class="text-justify">
    <strong>لِمَ رُسِمَ التَّنْوِينُ مُخْتَلِفًا فِي (سَمَاءً) وَ(جُزْءًا)؟</strong><br><br>
    <span class="font-bold highlight-red">سَمَاءً:</span> لِأَنَّ الْهَمْزَةَ <span class="text-accent">سُبِقَتْ بِأَلِفٍ</span>، فَلَا تُكْتَبُ أَلِفُ التَّنْوِينِ.<br>
    <span class="font-bold highlight-red">جُزْءًا:</span> لِأَنَّ الْهَمْزَةَ <span class="text-accent">لَمْ تُسْبَقْ بِأَلِفٍ</span>، وَالْحَرْفُ قَبْلَهَا لَا يَتَّصِلُ، فَرُسِمَتْ عَلَى السَّطْرِ وَأُضِيفَتْ أَلِفُ التَّنْوِينِ.
    </p>
</div>
"""
    blocks_p2.append(
        create_split(
            "تَعْلِيلُ رَسْمِ الْهَمْزَةِ (1)", left_content_b11, "تَعْلِيلُ رَسْمِ التَّنْوِينِ (2)", right_content_b11
        )
    )

    # Block 12: Exam (Expanded for Page 2)
    blocks_p2.append(
        create_exam(
            "1",
            "بَيِّنْ سَبَبَ كِتَابَةِ الْهَمْزَةِ عَلَى الصُّورَةِ الَّتِي تَرَاهَا فِي الْكَلِمَاتِ الآتِيَةِ: (تَبَاطُؤ - شَاطِئ - دِفْء - مَلْجَآنِ).",
            "2",
            "أَدْخِلْ تَنْوِينَ النَّصْبِ عَلَى الْكَلِمَاتِ الآتِيَةِ مُرَاعِيًا الْقَوَاعِدَ الْإِمْلَائِيَّةَ: (جُزْء - شَيْء - سَمَاء - مَبْدَأ).",
            "الْهَمْزَةُ الْمُتَطَرِّفَةُ",
        )
    )

    # Add extra exam question to fill space if needed
    blocks_p2.append(
        create_exam(
            "3",
            "هَاتِ مُثَنَّى كُلٍّ مِنَ الْكَلِمَاتِ الآتِيَةِ: (مَلْجَأ - بَدَأَ - قَارِئ - لُؤْلُؤ).",
            "4",
            "صَوِّبِ الْخَطَأَ فِي الْكَلِمَاتِ الآتِيَةِ: (شَيْءًا - سَمَاءًا - جُزْءًا - مَبْدَءًا).",
            "تَدْرِيبَاتٌ إِضَافِيَّةٌ",
        )
    )

    # Irab (Page 2) - Tanween
    irab_p2 = [
        ("قَرَأْتُ", "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ."),
        ("شَيْئًا", "مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ عَلَى آخِرِهِ (الْهَمْزَة)."),
    ]
    blocks_p2.append(create_irab("قَرَأْتُ شَيْئًا مُفِيدًا.", irab_p2))

    # Write Page 1
    full_content_p1 = "\n".join(blocks_p1)
    page_template = load_template("TEMPLATE_C_PAGE_WRAPPER.html")
    final_html_p1 = page_template.replace("<!-- INJECT_CONTENT_HERE -->", full_content_p1)
    with open(OUTPUT_FILE_19_0, "w", encoding="utf-8") as f:
        f.write(final_html_p1)
    print(f"Generated {OUTPUT_FILE_19_0}")

    # Write Page 2
    full_content_p2 = "\n".join(blocks_p2)
    final_html_p2 = page_template.replace("<!-- INJECT_CONTENT_HERE -->", full_content_p2)
    with open(OUTPUT_FILE_19_1, "w", encoding="utf-8") as f:
        f.write(final_html_p2)
    print(f"Generated {OUTPUT_FILE_19_1}")


if __name__ == "__main__":
    main()
