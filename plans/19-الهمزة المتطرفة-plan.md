# **SESSION 19.0**

[TASK DEFINITION]
Objective: Implement الهمزة المتطرفة.
File: `pages/19.0_nXX_الهمزة المتطرفة.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/19.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 19
[CHAPTER_TITLE]: الْهَمْزَةُ الْمُتَطَرِّفَةُ
[CATEGORY_HEADER]: الإملاء
[SECTION_HEADER]: المستوى اللغوي
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition & General Rule ===
(Component: TEMPLATE_C_BLOCK)
Title: تَعْرِيفُ الْهَمْزَةِ الْمُتَطَرِّفَةِ وَقَاعِدَتُهَا
Content:
<p class="text-justify leading-loose">
    <span class="text-accent font-bold">الْهَمْزَةُ الْمُتَطَرِّفَةُ:</span> هِيَ الَّتِي تُكْتَبُ فِي <span class="highlight-red">آخِرِ الْكَلِمَةِ</span>.
    <br><br>
    <span class="font-bold text-teal-800">الْقَاعِدَةُ الْعَامَّةُ:</span> تُكْتَبُ الْهَمْزَةُ الْمُتَطَرِّفَةُ بِحَسَبِ <span class="highlight-blue">حَرَكَةِ الْحَرْفِ الَّذِي يَسْبِقُهَا</span> (لَا يُنْظَرُ إِلَى حَرَكَةِ الْهَمْزَةِ نَفْسِهَا)، وَذَلِكَ عَلَى النَّحْوِ الآتِي:
</p>

=== BLOCK 3: The Matrix (Summary Table) ===
(Component: TEMPLATE_C_TABLE)
Title: مَوَاضِعُ كِتَابَةِ الْهَمْزَةِ الْمُتَطَرِّفَةِ
[HEADERS]: حَرَكَةُ مَا قَبْلَهَا | الْحَرْفُ الْمُنَاسِبُ | صُورَةُ الْكِتَابَةِ | أَمْثِلَةٌ تَوْضِيحِيَّةٌ
[ROW_1]: الْكَسْرَةُ (ــِـ) | الْيَاءُ غَيْرُ الْمَنْقُوطَةِ | <span class="text-2xl font-bold text-teal-600">ـئ</span> | <span class="highlight-red">يُومِئ</span>، شَاطِئ، قَارِئ
[ROW_2]: الضَّمَّةُ (ــُـ) | الْوَاوُ | <span class="text-2xl font-bold text-teal-600">ـؤ</span> | <span class="highlight-red">تَبَاطُؤ</span>، لُؤْلُؤ، تَكـَافُؤ
[ROW_3]: الْفَتْحَةُ (ــَـ) | الْأَلِفُ | <span class="text-2xl font-bold text-teal-600">ـأ</span> | <span class="highlight-red">الْمَبْدَأ</span>، قَرَأَ، نَشَأَ
[ROW_4]: السُّكُونُ (ــْـ) | السَّطْرُ (مُنْفَرِدَةً) | <span class="text-2xl font-bold text-teal-600">ء</span> | <span class="highlight-red">دِفْء</span>، عِبْء، شَيْء، هُدُوء

=== BLOCK 4: Examples with Chips ===
(Component: TEMPLATE_C_CHIPS)
Title: أَمْثِلَةٌ إِضَافِيَّةٌ لِلتَّرْسِيخِ
[CHIP_1]: <span class="font-bold">مَكْسُورٌ مَا قَبْلَهَا:</span> يُومِئ، يُكَافِئ
[CHIP_2]: <span class="font-bold">مَضْمُومٌ مَا قَبْلَهَا:</span> تَبَاطُؤ، يَجْرُؤ
[CHIP_3]: <span class="font-bold">مَفْتُوحٌ مَا قَبْلَهَا:</span> الْمَبْدَأ، يَلْجَأ
[CHIP_4]: <span class="font-bold">سَاكِنٌ مَا قَبْلَهَا:</span> دِفْء، بُطْء

=== BLOCK 5: Deep Dive - Dual Alif (Introduction) ===
(Component: TEMPLATE_C_BLOCK)
Title: تَنْبِيهَاتٌ: اجْتِمَاعُ الْهَمْزَةِ الْمُتَطَرِّفَةِ مَعَ أَلِفِ التَّثْنِيَةِ
Content:
<p class="text-justify leading-loose">
    عِنْدَ تَثْنِيَةِ الْكَلِمَةِ الْمُنْتَهِيَةِ بِهَمْزَةٍ مُتَطَرِّفَةٍ، يَجِبُ التَّمْيِيزُ بَيْنَ <span class="highlight-blue">الِاسْمِ</span> وَ <span class="highlight-blue">الْفِعْلِ</span>، وَمُرَاعَاةُ حَالَةِ الْحَرْفِ السَّابِقِ لِلْهَمْزَةِ (مِنْ حَيْثُ الِاتِّصَالُ وَالِانْفِصَالُ).
</p>

=== BLOCK 6: Dual Alif Cases (Split View) ===
(Component: TEMPLATE_C_SPLIT)
[LEFT_TITLE]: فِي الْأَفْعَالِ
[LEFT_CONTENT]:
(Component: TEMPLATE_C_LIST)
[LIST_HEADER]: حُكْمُ الْفِعْلِ
[ITEM_1]: تَبْقَى الْهَمْزَةُ الْمُتَطَرِّفَةُ الْمَرْسُومَةُ عَلَى أَلِفٍ <span class="font-bold">عَلَى حَالِهَا</span>.
[ITEM_2]: تُكْتَبُ بَعْدَهَا أَلِفُ التَّثْنِيَةِ دُونَ دَمْجٍ.
[ITEM_3]: <span class="highlight-red">مِثَالٌ:</span> بَدَأَ &#8592; <span class="font-bold text-teal-700">بَدَأَا</span>.
[ITEM_4]: <span class="font-bold text-orange-600">تَنْبِيهٌ:</span> فِي الْمُضَارِعِ، يَجِبُ الانْتِبَاهُ لِثُبُوتِ النُّونِ (يَلْجَأ &#8592; <span class="font-bold">يَلْجَأَانِ</span>).

[RIGHT_TITLE]: فِي الْأَسْمَاءِ
[RIGHT_CONTENT]:
(Component: TEMPLATE_C_LIST)
[LIST_HEADER]: حُكْمُ الاسْمِ
[ITEM_1]: إِذَا كَانَتِ الْهَمْزَةُ عَلَى أَلِفٍ، تَتَحَوَّلُ مَعَ أَلِفِ التَّثْنِيَةِ إِلَى <span class="highlight-red">مَدَّةٍ (آ)</span>.
[ITEM_2]: <span class="highlight-red">مِثَالٌ:</span> مَلْجَأ &#8592; <span class="font-bold text-teal-700">مَلْجَآنِ</span>.
[ITEM_3]: مِثَالٌ آخَرُ: مَبْدَأ &#8592; <span class="font-bold text-teal-700">مَبْدَآنِ</span>.

=== BLOCK 7: Hamza on Line with Dual Alif ===
(Component: TEMPLATE_C_TABLE)
Title: حُكْمُ الْهَمْزَةِ الْمُتَطَرِّفَةِ عَلَى السَّطْرِ مَعَ التَّثْنِيَةِ
[HEADERS]: الْحَالَةُ | الْقَاعِدَةُ | الْمِثَالُ | التَّعْلِيلُ
[ROW_1]: مَا قَبْلَهَا <span class="text-orange-600">لَا يَتَّصِلُ</span> | تَبْقَى عَلَى السَّطْرِ مُنْفَرِدَةً | <span class="font-bold">جُزْءَانِ</span>، نِدَاءَانِ | الْحَرْفُ السَّابِقُ (الزَّاي/الْأَلِف) لَا يَقْبَلُ الْوَصْلَ.
[ROW_2]: مَا قَبْلَهَا <span class="text-teal-600">يَتَّصِلُ</span> | تُكْتَبُ عَلَى نَبْرَةٍ (ـئـ) | <span class="font-bold">شَيْئَانِ</span>، فَيْئَانِ، عِبْئَانِ | الْحَرْفُ السَّابِقُ (الْيَاء/الْبَاء) يَقْبَلُ الْوَصْلَ بِمَا بَعْدَهُ.

=== BLOCK 8: Special Case (Waw/Ya) Benefit ===
(Component: TEMPLATE_C_BENEFIT)
Title: فَائِدَةٌ: الْهَمْزَةُ عَلَى الْوَاوِ وَالْيَاءِ
Content:
إِذَا كَانَتِ الْهَمْزَةُ الْمُتَطَرِّفَةُ مَرْسُومَةً عَلَى <span class="highlight-blue">الْوَاوِ</span> أَوْ عَلَى <span class="highlight-blue">يَاءٍ</span>، وَلَحِقَتْ بِهَا أَلِفُ التَّثْنِيَةِ، نُطَبِّقُ عَلَيْهَا <span class="font-bold">قَاعِدَةَ الْهَمْزَةِ الْمُتَوَسِّطَةِ</span> (أَقْوَى الْحَرَكَتَيْنِ).
<br>
<span class="highlight-red">أَمْثِلَةٌ:</span> لُؤْلُؤ &#8592; <span class="font-bold">لُؤْلُؤَانِ</span> | مُبْطِئ &#8592; <span class="font-bold">مُبْطِئَانِ</span>.

=== BLOCK 9: Tanween al-Nasb Introduction ===
(Component: TEMPLATE_C_BLOCK)
Title: الْهَمْزَةُ الْمُتَطَرِّفَةُ مَعَ تَنْوِينِ النَّصْبِ
Content:
<p class="text-justify leading-loose">
    عِنْدَ تَنْوِينِ الْكَلِمَةِ الْمُنْتَهِيَةِ بِهَمْزَةٍ مُتَطَرِّفَةٍ <span class="highlight-blue">تَنْوِينَ نَصْبٍ</span>، نَنْظُرُ إِلَى الْحَرْفِ الَّذِي يَسْبِقُ الْهَمْزَةَ، أَوْ مَوْضِعِ كِتَابَةِ الْهَمْزَةِ.
</p>

=== BLOCK 10: Tanween al-Nasb Rules (Detailed) ===
(Component: TEMPLATE_C_LIST)
Title: حَالَاتُ كِتَابَةِ تَنْوِينِ النَّصْبِ
[LIST_HEADER]: القواعد
[ITEM_1]: <span class="font-bold text-orange-600">إِذَا سُبِقَتْ بِأَلِفٍ:</span> يُرْسَمُ التَّنْوِينُ عَلَى الْهَمْزَةِ مُبَاشَرَةً دُونَ أَلِفٍ إِضَافِيَّةٍ (كَرَاهَةَ اجْتِمَاعِ أَلِفَيْنِ). <span class="highlight-red">مِثَالٌ:</span> <span class="font-bold">سَمَاءً، نِدَاءً</span>.
[ITEM_2]: <span class="font-bold text-orange-600">إِذَا كُتِبَتْ عَلَى أَلِفٍ:</span> يُرْسَمُ التَّنْوِينُ فَوْقَهَا مُبَاشَرَةً. <span class="highlight-red">مِثَالٌ:</span> <span class="font-bold">مَبْدَأً، خَطَأً</span>.
[ITEM_3]: <span class="font-bold text-teal-600">إِذَا لَمْ تُسْبَقْ بِأَلِفٍ:</span> تُرْسَمُ أَلِفُ التَّنْوِينِ بَعْدَهَا. وَلَهَا حَالَتَانِ:
    <ul class="structured-list">
        <li><span class="font-bold">غَيْرُ مُتَّصِلٍ:</span> إِذَا كَانَ مَا قَبْلَهَا لَا يَتَّصِلُ، تَبْقَى عَلَى السَّطْرِ. نَحْو: <span class="font-bold">جُزْءًا، بَدْءًا</span>.</li>
        <li><span class="font-bold">مُتَّصِلٌ:</span> إِذَا كَانَ مَا قَبْلَهَا يَتَّصِلُ، تُكْتَبُ عَلَى نَبْرَةٍ. نَحْو: <span class="font-bold">شَيْئًا، عِبْئًا</span>.</li>
    </ul>

=== BLOCK 11: Reasonings (Q&A) ===
(Component: TEMPLATE_C_SPLIT)
[LEFT_TITLE]: تَعْلِيلُ رَسْمِ الْهَمْزَةِ (1)
[LEFT_CONTENT]:
(Component: TEMPLATE_C_BLOCK)
Title: لِمَ كُتِبَتْ (شَيْئَانِ) عَلَى نَبْرَةٍ وَ(جُزْءَانِ) عَلَى السَّطْرِ؟
Content:
<p class="text-justify">
<span class="font-bold highlight-red">جُزْءَانِ:</span> هَمْزَةٌ مُتَطَرِّفَةٌ اجْتَمَعَتْ مَعَ أَلِفِ التَّثْنِيَةِ، وَالْحَرْفُ الَّذِي قَبْلَهَا (الزَّاي) <span class="text-accent">لَا يَقْبَلُ الْوَصْلَ</span> بِمَا بَعْدَهُ.<br>
<span class="font-bold highlight-red">شَيْئَانِ:</span> هَمْزَةٌ مُتَطَرِّفَةٌ اجْتَمَعَتْ مَعَ أَلِفِ التَّثْنِيَةِ، وَالْحَرْفُ الَّذِي قَبْلَهَا (الْيَاء) <span class="text-accent">يَقْبَلُ الْوَصْلَ</span> بِمَا بَعْدَهُ.
</p>

[RIGHT_TITLE]: تَعْلِيلُ رَسْمِ التَّنْوِينِ (2)
[RIGHT_CONTENT]:
(Component: TEMPLATE_C_BLOCK)
Title: لِمَ رُسِمَ التَّنْوِينُ مُخْتَلِفًا فِي (سَمَاءً) وَ(جُزْءًا)؟
Content:
<p class="text-justify">
<span class="font-bold highlight-red">سَمَاءً:</span> لِأَنَّ الْهَمْزَةَ <span class="text-accent">سُبِقَتْ بِأَلِفٍ</span>، فَلَا تُكْتَبُ أَلِفُ التَّنْوِينِ.<br>
<span class="font-bold highlight-red">جُزْءًا:</span> لِأَنَّ الْهَمْزَةَ <span class="text-accent">لَمْ تُسْبَقْ بِأَلِفٍ</span>، وَالْحَرْفُ قَبْلَهَا لَا يَتَّصِلُ، فَرُسِمَتْ عَلَى السَّطْرِ وَأُضِيفَتْ أَلِفُ التَّنْوِينِ.
</p>

=== BLOCK 12: Exam ===
(Component: TEMPLATE_C_EXAM)
Number: 1
Question: بَيِّنْ سَبَبَ كِتَابَةِ الْهَمْزَةِ عَلَى الصُّورَةِ الَّتِي تَرَاهَا فِي الْكَلِمَاتِ الآتِيَةِ: (تَبَاطُؤ - شَاطِئ - دِفْء - مَلْجَآنِ).
Number: 2
Question: أَدْخِلْ تَنْوِينَ النَّصْبِ عَلَى الْكَلِمَاتِ الآتِيَةِ مُرَاعِيًا الْقَوَاعِدَ الْإِمْلَائِيَّةَ: (جُزْء - شَيْء - سَمَاء - مَبْدَأ).

--- END STREAM ---
