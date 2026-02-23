# **SESSION 11.0**

[TASK DEFINITION]
Objective: Implement الإبدال.
File: `pages/11.0_nXX_الإبدال.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/[LESSON_NUMBER].1_...` if page have a lot of blank space add exam elements from the lesson.
3. text Content: 100% Arabic with full Harakat.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green`  for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   **Rule:** NO INLINE STYLES.
*   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
*   **Mapping:**
    *   `style="width: 20%"` -> `class="w-20pct"`
    *   `style="margin-top: 2mm"` -> `class="mt-2mm"`
    *   `style="text-align: center"` -> `class="text-center"`
    *   `style="font-weight: bold"` -> `class="font-bold"`
6. Templates: You are forbidden from inventing new HTML tags or classes or template elements. You must map all content using "Jules-workspace/Templates/" components as the STREAM says in suitable way.
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). use "Jules-workspace/id_manager.py" to generate or verify them.
8. **Self-Correction:** Run "Jules-workspace/lint_pages.py" after creating html files. If it fails, you MUST fix the errors (usually inline styles) before submitting.
9. Do not summarize examples. 
10. Do not provide uncompleted text content using (...) .
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.  
12. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal 

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER)
[LESSON_NUMBER]: 11
[CHAPTER_TITLE]: الإبدال
[CATEGORY_HEADER]: الصرف
[SECTION_HEADER]: المستوى اللغوي
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition ===
(Component: TEMPLATE_C_BLOCK)
Title: تَعْرِيفُ الإِبْدَالِ
Content: <p class="text-accent text-center font-bold text-primary p-2mm">هُوَ جَعْلُ حَرْفٍ مَكَانَ حَرْفٍ، سَوَاءٌ أَكَانَ الحَرْفُ صَحِيحًا أَمْ مُعْتَلًّا.</p>

=== BLOCK 3: Hamza Substitution Rules ===
(Component: TEMPLATE_C_SPLIT)
[LEFT_TITLE]: إِذَا تَطَرَّفَتَا بَعْدَ أَلِفٍ زَائِدَةٍ
[LEFT_CONTENT]:
<div class="p-2mm">
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
</div>

[RIGHT_TITLE]: فِي اسْمِ الفَاعِلِ مِنَ الأَجْوَفِ
[RIGHT_CONTENT]:
<div class="p-2mm">
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
</div>

=== BLOCK 4: Plural Substitution ===
(Component: TEMPLATE_C_BLOCK)
Title: إِبْدَالُ حُرُوفِ المَدِّ هَمْزَةً فِي (فَعَائِل)
Content:
<p class="mb-2mm">يُبْدَلُ حَرْفُ المَدِّ (ي، و، ا) فِي المُفْرَدِ المُؤَنَّثِ هَمْزَةً إِذَا وَقَعَ بَعْدَ أَلِفِ صِيَغِ مُنْتَهَى الجُمُوعِ (فَعَائِل):</p>
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
</ul>

=== BLOCK 5: Ifti'āl Rules Matrix ===
(Component: TEMPLATE_C_TABLE)
Title: قَوَاعِدُ الإِبْدَالِ فِي صِيغَةِ (افْتَعَلَ)
Columns: [القَاعِدَة, المِثَال, الأَصْل, التَّعْلِيل]
Rows:
[
    ["تُبْدَلُ تَاءُ (افْتَعَلَ) طَاءً بَعْدَ الضَّادِ", "اضْطَرَّ", "اضْتَرَّ", "وَقَعَتِ التَّاءُ بَعْدَ حَرْفِ الضَّادِ"],
    ["تُبْدَلُ تَاءُ (افْتَعَلَ) طَاءً بَعْدَ الصَّادِ", "اصْطَحَبَ", "اصْتَحَبَ", "وَقَعَتِ التَّاءُ بَعْدَ حَرْفِ الصَّادِ"],
    ["تُبْدَلُ تَاءُ (افْتَعَلَ) دَالًا بَعْدَ الزَّايِ", "ازْدَهَرَ", "ازْتَهَرَ", "وَقَعَتِ التَّاءُ بَعْدَ حَرْفِ الزَّايِ"],
    ["تُبْدَلُ الوَاوُ تَاءً إِذَا وَقَعَتْ فَاءً لِـ (افْتَعَلَ)", "اتَّقَدَ", "اوتَقَدَ", "جَاءَتْ مُقَابِلَةً لِفَاءِ المِيزَانِ الصَّرْفِي"]
]

=== BLOCK 6: Solved Applications ===
(Component: TEMPLATE_C_TABLE)
Title: أَمْثِلَةٌ تَطْبِيقِيَّةٌ مُجَابٌ عَنْهَا
Columns: [الكَلِمَة, العِلَّة الصَّرْفِيَّة]
Rows:
[
    ["قَالَ", "إِعْلَالٌ بِالقَلْبِ، قُلِبَتِ الوَاو أَلِفًا؛ لِتَحَرُّكِهَا بَعْدَ فَتْحٍ."],
    ["عُدْ", "إِعْلَالٌ بِالحَذْفِ، حُذِفَ حَرْفُ العِلَّةِ لِوُجُودِ سَاكِنٍ بَعْدَه."],
    ["دَنَا", "إِعْلَالٌ بِالقَلْبِ، قُلِبَتِ الوَاو أَلِفًا؛ لِتَحَرُّكِهَا بَعْدَ فَتْحٍ."],
    ["غُزَتْ", "إِعْلَالٌ بِالحَذْفِ، حُذِفَ حَرْفُ العِلَّةِ لِوُقُوعِهِ فِي آخِرِ الفِعْلِ المَاضِي الَّذِي اتَّصَلَتْ بِهِ تَاءُ التَّأْنِيثِ."],
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
    ["أَسْتَزِيدُ", "إِعْلَالٌ بالتَّسكِينِ، سَكَنَتِ الياءُ؛ لتَحَرُّكِها بَعدَ حَرْفٍ صَحِيحٍ ساكِنٍ."]
]

=== BLOCK 7: Exam ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: بَيِّنِ العِلَّةَ الصَّرْفِيَّةَ (إِبْدَال أَوْ إِعْلَال) فِي الكَلِمَاتِ الآتِيَةِ مَعَ التَّعْلِيلِ: (سَمَاء - اصْطَبَرَ - ادَّعَى).

--- END STREAM ---
