def read_template(name):
    with open(f"Jules-workspace/Templates/{name}", encoding="utf-8") as f:
        return f.read()


def create_table_rows(rows):
    html = ""
    for row in rows:
        html += "<tr>"
        for cell in row:
            html += f"<td>{cell}</td>"
        html += "</tr>\n"
    return html


def create_table_headers(headers):
    html = ""
    for header in headers:
        html += f"<th>{header}</th>"
    return html


def main():
    # 1. Header
    header = read_template("TEMPLATE_C_HEADER.html")
    header = header.replace("[LESSON_NUMBER]", "١١")  # 11 in Arabic
    header = header.replace("[CHAPTER_TITLE]", "الإبدال")
    header = header.replace("[CATEGORY_HEADER]", "الصرف")
    header = header.replace("[SECTION_HEADER]", "المستوى اللغوي")
    header = header.replace("[AUTHOR_NAME]", "أ. حنا خفيف")
    header = header.replace("[AUTHOR_PHONE]", " ")

    # 2. Definition Block
    block_def = read_template("TEMPLATE_C_BLOCK.html")
    # Fix nested <p> issue: remove wrapper <p> in template
    block_def = block_def.replace(
        '<p class="mt-1mm text-accent">\n                [CONTENT_TEXT]\n            </p>',
        "[CONTENT_TEXT]",
    )

    block_def = block_def.replace("[BLOCK_TITLE]", "تَعْرِيفُ الإِبْدَالِ")
    block_def = block_def.replace(
        "[CONTENT_TEXT]",
        '<p class="text-accent text-center font-bold text-primary p-2mm">هُوَ جَعْلُ حَرْفٍ مَكَانَ حَرْفٍ، سَوَاءٌ أَكَانَ الحَرْفُ صَحِيحًا أَمْ مُعْتَلًّا.</p>',
    )

    # Remove benefit box as it's not used here
    block_def = block_def.replace(
        '<div class="benefit-box">\n                <strong> [BENEFIT_TITLE]:</strong> [BENEFIT_TEXT]\n            </div>',
        "",
    )

    # 3. Hamza Substitution Rules (Split)
    split_hamza = read_template("TEMPLATE_C_SPLIT.html")
    split_hamza = split_hamza.replace("[LEFT_TITLE]", "إِذَا تَطَرَّفَتَا بَعْدَ أَلِفٍ زَائِدَةٍ")
    split_hamza = split_hamza.replace(
        "[LEFT_CONTENT]",
        """<div class="p-2mm">
    <ul class="structured-list">
        <li class="mb-2mm">
            <span class="marker">•</span>
            <span class="font-bold highlight-red">كِسَاء</span>: أَصْلُ هَذِهِ الهَمْزَةِ <span class="highlight-blue">وَاو</span> (يَكْسُو، كِسَاو)، وتَحوَّلَتْ إِلى هَمْزَةٍ لأَنَّهَا جَاءَتْ فِي آخِرِ كَلِمَة (كِسَاء) بَعْدَ أَلِفٍ زَائِدَة.
        </li>
        <li class="mb-2mm">
            <span class="marker">•</span>
            <span class="font-bold highlight-red">بِنَاء</span>: أَصْلُ هَذِهِ الهَمْزَةِ <span class="highlight-blue">يَاء</span> (يَبْنِي، بِنَاي)، وتَحوَّلَتْ إِلى هَمْزَةٍ لأَنَّهَا جَاءَتْ فِي آخِرِ كَلِمَة (بِنَاء) بَعْدَ أَلِفٍ زَائِدَة.
        </li>
    </ul>
</div>""",
    )
    split_hamza = split_hamza.replace("[RIGHT_TITLE]", "فِي اسْمِ الفَاعِلِ مِنَ الأَجْوَفِ")
    split_hamza = split_hamza.replace(
        "[RIGHT_CONTENT]",
        """<div class="p-2mm">
    <p class="mb-2mm">إِذَا وَقَعَا عَيْنًا فِي اسْمِ الفَاعِلِ المَصُوغِ مِنَ الفِعْلِ الثُّلَاثِي الأَجْوَفِ:</p>
    <ul class="structured-list">
        <li class="mb-2mm">
            <span class="marker">•</span>
            <span class="font-bold highlight-red">عَائِد</span>: أَصْلُ هَذِهِ الهَمْزَةِ <span class="highlight-blue">وَاو</span> (يَعُودُ، عَاوِد).
        </li>
        <li class="mb-2mm">
            <span class="marker">•</span>
            <span class="font-bold highlight-red">صَائِد</span>: أَصْلُ هَذِهِ الهَمْزَةِ <span class="highlight-blue">يَاء</span> (يَصِيدُ، صَايِد).
        </li>
        <li class="mb-2mm text-grey-dark text-sm">
            <span class="marker">ℹ️</span>
            <span class="font-bold">أَمْثِلَةٌ أُخْرَى:</span> (قَالَ، قَائِل) - (بَاعَ، بَائِع).
        </li>
    </ul>
</div>""",
    )

    # 4. Plural Substitution (Block)
    block_plural = read_template("TEMPLATE_C_BLOCK.html")
    # Fix nested <p> issue
    block_plural = block_plural.replace(
        '<p class="mt-1mm text-accent">\n                [CONTENT_TEXT]\n            </p>',
        "[CONTENT_TEXT]",
    )

    block_plural = block_plural.replace("[BLOCK_TITLE]", "إِبْدَالُ حُرُوفِ المَدِّ هَمْزَةً فِي (فَعَائِل)")
    block_plural = block_plural.replace(
        "[CONTENT_TEXT]",
        """<p class="mb-2mm">يُبْدَلُ حَرْفُ المَدِّ (ي، و، ا) فِي المُفْرَدِ المُؤَنَّثِ هَمْزَةً إِذَا وَقَعَ بَعْدَ أَلِفِ صِيَغِ مُنْتَهَى الجُمُوعِ (فَعَائِل):</p>
<ul class="structured-list">
    <li class="bg-grey-lighter p-2mm rounded mb-2mm">
        <span class="marker">✅</span>
        <span class="font-bold text-primary">عَجَائِز:</span> أَصْلُهَا (عَجَاوِز) مِن (عَجَزَ). تَحَوَّلَتِ الوَاوُ إِلى هَمْزَةٍ لأَنَّهَا وَقَعَتْ بَعْدَ أَلِفِ صِيغَةِ مُنْتَهَى الجُمُوعِ.
    </li>
    <li class="bg-grey-lighter p-2mm rounded mb-2mm">
        <span class="marker">✅</span>
        <span class="font-bold text-primary">قَصَائِد:</span> أَصْلُهَا (قَصَايِد) مِن (قَصَدَ). تَحَوَّلَتِ اليَاءُ إِلى هَمْزَةٍ لأَنَّهَا وَقَعَتْ بَعْدَ أَلِفِ صِيغَةِ مُنْتَهَى الجُمُوعِ.
    </li>
    <li class="p-1mm text-sm text-grey-dark">
        <span class="marker">ℹ️</span>
        أَمْثِلَةٌ أُخْرَى: (صَحِيفَة، صَحَائِف)، (وَدِيعَة، وَدَائِع)، (قِلَادَة، قَلَائِد).
    </li>
</ul>""",
    )
    # Remove benefit box
    block_plural = block_plural.replace(
        '<div class="benefit-box">\n                <strong> [BENEFIT_TITLE]:</strong> [BENEFIT_TEXT]\n            </div>',
        "",
    )

    # 5. Ifti'āl Rules Matrix (Table)
    table_iftial = read_template("TEMPLATE_C_TABLE.html")
    table_iftial = table_iftial.replace("[TABLE_TITLE]", "قَوَاعِدُ الإِبْدَالِ فِي صِيغَةِ (افْتَعَلَ)")
    headers = ["القَاعِدَة", "المِثَال", "الأَصْل", "التَّعْلِيل"]
    rows = [
        ["تُبْدَلُ تَاءُ (افْتَعَلَ) طَاءً بَعْدَ الضَّادِ", "اضْطَرَّ", "اضْتَرَّ", "وَقَعَتِ التَّاءُ بَعْدَ حَرْفِ الضَّادِ"],
        ["تُبْدَلُ تَاءُ (افْتَعَلَ) طَاءً بَعْدَ الصَّادِ", "اصْطَحَبَ", "اصْتَحَبَ", "وَقَعَتِ التَّاءُ بَعْدَ حَرْفِ الصَّادِ"],
        ["تُبْدَلُ تَاءُ (افْتَعَلَ) دَالًا بَعْدَ الزَّايِ", "ازْدَهَرَ", "ازْتَهَرَ", "وَقَعَتِ التَّاءُ بَعْدَ حَرْفِ الزَّايِ"],
        [
            "تُبْدَلُ الوَاوُ تَاءً إِذَا وَقَعَتْ فَاءً لِـ (افْتَعَلَ)",
            "اتَّقَدَ",
            "اوتَقَدَ",
            "جَاءَتْ مُقَابِلَةً لِفَاءِ المِيزَانِ الصَّرْفِي",
        ],
    ]
    table_iftial = table_iftial.replace("[TABLE_HEADERS]", create_table_headers(headers))
    table_iftial = table_iftial.replace("[TABLE_ROWS]", create_table_rows(rows))

    # 6. Solved Applications (Table)
    # 6. Solved Applications (Table) - SPLIT
    headers_solved = ["الكَلِمَة", "العِلَّة الصَّرْفِيَّة"]
    rows_solved = [
        ["قَالَ", "إِعْلَالٌ بِالقَلْبِ، قُلِبَتِ الوَاو أَلِفًا؛ لِتَحَرُّكِهَا بَعْدَ فَتْحٍ."],
        ["عُدْ", "إِعْلَالٌ بِالحَذْفِ، حُذِفَ حَرْفُ العِلَّةِ لِوُجُودِ سَاكِنٍ بَعْدَه."],
        ["دَنَا", "إِعْلَالٌ بِالقَلْبِ، قُلِبَتِ الوَاو أَلِفًا؛ لِتَحَرُّكِهَا بَعْدَ فَتْحٍ."],
        [
            "غُزَتْ",
            "إِعْلَالٌ بِالحَذْفِ، حُذِفَ حَرْفُ العِلَّةِ لِوُقُوعِهِ فِي آخِرِ الفِعْلِ المَاضِي الَّذِي اتَّصَلَتْ بِهِ تَاءُ التَّأْنِيثِ.",
        ],
        ["يَزْدَهِي (١)", "إِبْدَالٌ، أُبْدِلَتِ التَّاءُ دَالًا لِوُقُوعِهَا بَعْدَ الزَّايِ فِي صِيغَةِ (افْتَعَلَ)."],
        ["يَزْدَهِي (٢)", "إِعْلَالٌ بِالتَّسْكِينِ، سُكِّنَتِ اليَاء لِتَطَرُّفِهَا بَعْدَ كَسْرٍ."],
        ["صَائِد", "إِبْدَال، أُبْدِلَتِ اليَاء هَمْزَةً؛ لأَنَّهَا وَقَعَتْ عَيْنًا فِي صِيغَةِ اسْمِ الفَاعِلِ مِنَ الأَجْوَفِ."],
        ["سَائِل", "إِبْدَال، أُبْدِلَتِ اليَاءُ هَمْزَةً؛ لأَنَّهَا وَقَعَتْ عَيْنًا فِي صِيغَةِ اسْمِ الفَاعِلِ مِنَ الأَجْوَفِ."],
        ["أَخْفِي", "إِعْلَالٌ بِالتَّسْكِينِ، سُكِّنَتِ اليَاءُ لأَنَّهَا تَطَرَّفَتْ بَعْدَ كَسْرٍ."],
        ["مُلْقَاة", "إِعْلَالٌ بِالقَلْبِ، قُلِبَتِ اليَاءُ أَلِفًا؛ لأَنَّهَا تَحَرَّكَتْ بَعْدَ فَتْحٍ."],
        ["كُنْتُ", "إِعْلَالٌ بِالحَذْفِ، حُذِفَ حَرْفُ العِلَّةِ لِوُجُودِ سَاكِنٍ بَعْدَه."],
        ["آتَاهُ", "إِعْلَالٌ بِالقَلْبِ: قُلِبَتِ اليَاءُ أَلِفًا؛ لأَنَّهَا جَاءَتْ مُتَحَرِّكَةً بَعْدَ فَتْحٍ."],
        ["يَصْطَلِكُ", "إِبْدَالٌ: أُبْدِلَتِ التَّاءُ طَاءً؛ لِمَجِيئِهَا بَعْدَ الصَّادِ فِي صِيغَةِ (افْتَعَلَ)."],
        ["يَضْطَرِبُ", "إِبْدَالٌ: أُبْدِلَتِ التَّاءُ طَاءً؛ لِمَجِيئِهَا بَعْدَ الضَّادِ فِي صِيغَةِ (افْتَعَلَ)."],
        ["مَعَاد", "إِعْلَالٌ بِالقَلْبِ، قُلِبَتِ الوَاو أَلِفًا؛ لِتَحَرُّكِهَا بَعْدَ فَتْحٍ."],
        ["أَعْطَتْ", "إِعْلَالٌ بِالحَذْفِ، حُذِفَ حَرفُ العِلَّةِ لوُقوعِهِ في آخِرِ الفِعْلِ الماضِي المُتَّصِلِ بِتَاءِ التَّأْنِيثِ."],
        ["تَقَاضِي", "إِعْلَالٌ بالتَّسكِينِ؛ سَكَنَتِ الياءُ لِتَطَرُّفِها بعدَ كَسرٍ."],
        ["أَسْتَزِيدُ", "إِعْلَالٌ بالتَّسكِينِ، سَكَنَتِ الياءُ؛ لتَحَرُّكِها بَعدَ حَرْفٍ صَحِيحٍ ساكِنٍ."],
    ]

    # Split: 8 rows for P1, rest for P2
    rows_p1 = rows_solved[:8]
    rows_p2 = rows_solved[8:]

    table_solved_p1 = read_template("TEMPLATE_C_TABLE.html")
    table_solved_p1 = table_solved_p1.replace("[TABLE_TITLE]", "أَمْثِلَةٌ تَطْبِيقِيَّةٌ مُجَابٌ عَنْهَا")
    table_solved_p1 = table_solved_p1.replace(
        "[TABLE_HEADERS]", create_table_headers(headers_solved)
    )
    table_solved_p1 = table_solved_p1.replace("[TABLE_ROWS]", create_table_rows(rows_p1))

    table_solved_p2 = read_template("TEMPLATE_C_TABLE.html")
    table_solved_p2 = table_solved_p2.replace("[TABLE_TITLE]", "أَمْثِلَةٌ تَطْبِيقِيَّةٌ (تَابِع)")
    table_solved_p2 = table_solved_p2.replace(
        "[TABLE_HEADERS]", create_table_headers(headers_solved)
    )
    table_solved_p2 = table_solved_p2.replace("[TABLE_ROWS]", create_table_rows(rows_p2))

    # 7. Exam
    # Construct a custom exam block based on TEMPLATE_C_EXAM or just string replace if easy
    # The template has 2 questions. We need 1.
    # I'll just manually construct the HTML for the exam block to be safe and clean, reusing the template structure.
    # Removing ID attributes so id_manager.py can auto-tag them.
    exam_content = """<section class="content-block">
    <div class="block-header bg-dark">
        <span> اخْتَبِرْ نَفْسَكَ (الإِبْدَال)</span>
    </div>
    <div class="block-body">
        <!-- Question 1 -->
        <div class="exam-question mb-0 border-none pb-0">
            <p class="m-0 mb-2mm">
                <span class="exam-number">١</span>
                بَيِّنِ العِلَّةَ الصَّرْفِيَّةَ (إِبْدَال أَوْ إِعْلَال) فِي الكَلِمَاتِ الآتِيَةِ مَعَ التَّعْلِيلِ: (سَمَاء - اصْطَبَرَ - ادَّعَى).
            </p>
            <div class="border-light h-8mm bg-grey-lighter rounded"></div>
        </div>
    </div>
</section>"""

    # 8. Assembly Page 1
    content_p1 = (
        header
        + "\n"
        + block_def
        + "\n"
        + split_hamza
        + "\n"
        + block_plural
        + "\n"
        + table_iftial
        + "\n"
        + table_solved_p1
    )

    wrapper = read_template("TEMPLATE_C_PAGE_WRAPPER.html")
    final_html_p1 = wrapper.replace("<!-- INJECT_CONTENT_HERE -->", content_p1)

    with open("pages/11.0_nXX_الإبدال.html", "w", encoding="utf-8") as f:
        f.write(final_html_p1)

    # 9. Assembly Page 2
    # Create header for p2 with  suffix
    header_p2 = read_template("TEMPLATE_C_HEADER.html")
    header_p2 = header_p2.replace("[LESSON_NUMBER]", "١١")
    header_p2 = header_p2.replace("[CHAPTER_TITLE]", "الإبدال ")
    header_p2 = header_p2.replace("[CATEGORY_HEADER]", "الصرف")
    header_p2 = header_p2.replace("[SECTION_HEADER]", "المستوى اللغوي")
    header_p2 = header_p2.replace("[AUTHOR_NAME]", "أ. حنا خفيف")
    header_p2 = header_p2.replace("[AUTHOR_PHONE]", " ")

    content_p2 = header_p2 + "\n" + table_solved_p2 + "\n" + exam_content

    final_html_p2 = wrapper.replace("<!-- INJECT_CONTENT_HERE -->", content_p2)

    with open("pages/11.1_nXX_الإبدال.html", "w", encoding="utf-8") as f:
        f.write(final_html_p2)


if __name__ == "__main__":
    main()
