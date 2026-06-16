# **SESSION 11.0**

[TASK DEFINITION]
Objective: Implement الْمَفْعُولُ بِه وَأَنْوَاعَهُ وَعَلَاَّمَاتِ إِعْرَابِهِ.
File: `pages/11.0_nXX_الْمَفْعُولُ بِه وَأَنْوَاعَهُ وَعَلَاَّمَاتِ إِعْرَابِهِ.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually, instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/11.1_...` if page have a lot of blank space add exam elements from the lesson.
3. text Content: 100% Arabic with full Harakat.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green` for secondary.
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
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
15. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 11
[CHAPTER_TITLE]: الْمَفْعُولُ بِه وَأَنْوَاعَهُ وَعَلَاَّمَاتِ إِعْرَابِهِ
[CATEGORY_HEADER]:
[SECTION_HEADER]:
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Introduction & Definition ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مُقَدَّمَةٌ وَتَعْرِيفٌ
Content:
<p>فِي الْجُمْلَةِ الْفِعْلِيَّةِ (الَّتِي تَتَكَوَّنُ مِنْ فِعْلٍ وَفَاعِلٍ)، قَدْ لَا يَكْتَمِلُ الْمَعْنَى إِلَّا بِذِكْرِ مَنْ أَوْ مَا وَقَعَ عَلَيْهِ هَذَا الْحَدَثِ. هَذَا الرُّكْنُ الْمُكَمِّلُ (فِي الْأَفْعَالِ الْمُتَعَدِّيَةِ) يُسَمَّى <span class="highlight-red">الْمَفْعُولَ بِهِ</span>.</p>
<p class="text-accent"><strong>التَّعْرِيفُ:</strong> هُوَ الِاسْمُ الْمَنْصُوبُ الَّذِي وَقَعَ عَلَيْهِ فِعْلُ الْفَاعِلِ.</p>
<p><strong>مِثَالٌ:</strong> يَشْرَبُ الْمَرِيضُ الدَّوَاءَ. (مَنْ يَشْرَبُ؟ الْمَرِيضُ الْفَاعِلُ. مَاذَا يَشْرَبُ؟ <span class="highlight-red">الدَّوَاءَ</span> الْمَفْعُولُ بِهِ).</p>

=== BLOCK 3: Tip ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
[TIP_TITLE]: تَلْمِيحٌ كَيْفَ تَكْتَشِفُ الْمَفْعُولَ بِهِ فِي الْجُمْلَةِ؟
[TIP_TEXT]: قِفْ قَبْلَ الْفِعْلِ وَاسْأَلْ: <strong>(مَاذَا؟)</strong>. الْإِجَابَةُ هِيَ الْمَفْعُولُ بِهِ.

=== BLOCK 4: Block For Table ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الْإِعْرَابُ وَالْعَلَامَاتُ
Content:
<p><strong>قَاعِدَةٌ ذَهَبِيَّةٌ:</strong> الْمَفْعُولُ بِهِ دَائِمًا <strong>(مَنْصُوبٌ)</strong>. وَتَخْتَلِفُ عَلَامَةُ نَصْبِهِ حَسَبَ نَوْعِ الْكَلِمَةِ.</p>

=== BLOCK 5: Summary Table of Accusative Signs ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: عَلَامَةُ النَّصْبِ
[HEADER_2]: نَوْعُ الْكَلِمَةِ
[HEADER_3]: مِثَالٌ
[ROW_1_COL_1]: الْفَتْحَةُ (أَصْلِيَّةٌ)
[ROW_1_COL_2]: لِلْمُفْرَدِ وَلِجَمْعِ التَّكْسِيرِ
[ROW_1_COL_3]: غَرَسَ الْفَلَّاحُ <span class="highlight-red">الشَّجَرَةَ</span>، يَحْمِلُ الطَّالِبُ <span class="highlight-red">الْكُتُبَ</span>
[ROW_2_COL_1]: الْكَسْرَةُ (نِيَابَةً عَنِ الْفَتْحَةِ)
[ROW_2_COL_2]: لِجَمْعِ الْمُؤَنَّثِ السَّالِمِ فَقَطْ
[ROW_2_COL_3]: عَلَّقَ سَعِيدٌ <span class="highlight-red">اللَّوْحَاتِ</span> (مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْكَسْرَةِ)
[ROW_3_COL_1]: الْيَاءُ (فَرْعِيَّةٌ)
[ROW_3_COL_2]: لِلْمُثَنَّى وَلِجَمْعِ الْمُذَكَّرِ السَّالِمِ
[ROW_3_COL_3]: حَفِظَ الطَّالِبُ <span class="highlight-red">الْقَصِيدَتَيْنِ</span>، كَافَأْتُ <span class="highlight-red">الْمُتَفَوِّقِينَ</span>
[ROW_4_COL_1]: الْأَلِفُ (فَرْعِيَّةٌ)
[ROW_4_COL_2]: لِلْأَسْمَاءِ الْخَمْسَةِ
[ROW_4_COL_3]: أَطِعْ <span class="highlight-red">أَبَاكَ</span> (مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْأَلِفِ)

=== BLOCK 6: Extra Info Note ===
(Component: TEMPLATE_C_BENEFIT.html)
[BENEFIT_TITLE]: مُلَاحَظَةٌ حَوْلَ فِعْلِ الْأَمْرِ
[BENEFIT_TEXT]: إِذَا جَاءَ فِعْلُ أَمْرٍ مُوَجَّهٍ لِلْمُخَاطَبِ الْمُفْرَدِ كَقَوْلِنَا (اكْتُبِ الْوَاجِبَ، قُلِ الْحَقَّ)، يَكُونُ الْفَاعِلُ دَائِمًا مُسْتَتِرًا تَقْدِيرُهُ "أَنْتَ"، وَمَا بَعْدَ الْفِعْلِ يُعْرَبُ مَفْعُولًا بِهِ.

=== BLOCK 7: Types of Object Section ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَنْوَاعُ الْمَفْعُولِ بِهِ
Content:
<p>الْمَفْعُولُ بِهِ لَا يَكُونُ دَائِمًا اسْمًا صَرِيحًا مَفْصُولًا (اسْمًا ظَاهِرًا)، بَلْ يَأْتِي كَثِيرًا عَلَى شَكْلِ <strong>ضَمِيرٍ مُتَّصِلٍ</strong> يَلْتَصِقُ بِآخِرِ الْفِعْلِ.</p>
<p>إِذَا رَأَيْتَ أَحَدَ هَذِهِ الضَّمَائِرِ مُلْتَصِقًا بِـ <strong>فِعْلٍ</strong>، فَقُمْ بِإِعْرَابِهَا فَوْرًا: (ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبِ مَفْعُولٍ بِهِ).</p>

=== BLOCK 8: Pronouns List ===
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEMS]:
- <strong>كَافُ الْخِطَابِ (كَ):</strong> مِثْلُ (يُسْعِدُ<span class="highlight-red">كَ</span> النَّجَاحُ، شَكَرَ<span class="highlight-red">كَ</span> النَّاسُ).
- <strong>هَاءُ الْغَائِبِ (هُ):</strong> مِثْلُ (الدَّرْسُ شَرَحَ<span class="highlight-red">هُ</span> الْمُعَلِّمُ).
- <strong>يَاءُ الْمُتَكَلِّمِ (نِي):</strong> مِثْلُ (عَالَجَ<span class="highlight-red">نِي</span> الطَّبِيبُ). <em>(تُسْبَقُ يَاءُ الْمُتَكَلِّمِ دَائِمًا بِنُونٍ تُسَمَّى "نُونَ الْوِقَايَةِ" لِتَحْمِيَ الْفِعْلَ مِنَ الْكَسْرِ).</em>
- <strong>نَا الْمُتَكَلِّمَيْنِ الدَّالَّةُ عَلَى الْمَفْعُولَيْنِ (نَا):</strong> مِثْلُ (كَافَأَ<span class="highlight-red">نَا</span> الْمُدِيرُ). الْمُدِيرُ هُوَ الْمُكَافِئُ (الْفَاعِلُ)، وَنَحْنُ الْمُكَافَأُونَ (الْمَفْعُولُ بِهِ).

=== BLOCK 9: Warning Note ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[WARNING_TITLE]: تَنْبِيهٌ هَامٌّ حَوْلَ (نَا)
[WARNING_TEXT]: "نَا" قَدْ تَأْتِي فَاعِلًا مِثْلُ: كَتَبْ<span class="highlight-blue">نَا</span> الدَّرْسَ. نُفَرِّقُ بَيْنَهُمَا بِالْمَعْنَى وَحَرَكَةِ الْحَرْفِ الْأَخِيرِ مِنَ الْفِعْلِ الْمَاضِي؛ فَإِذَا كَانَ الْفِعْلُ الْمَاضِي مَبْنِيًّا عَلَى الْفَتْحِ "كَافَأَ<span class="highlight-red">نَا</span>"، كَانَتِ النَّا مَفْعُولًا بِهِ، وَإِذَا كَانَ مَبْنِيًّا عَلَى السُّكُونِ "كَتَبْ<span class="highlight-blue">نَا</span>"، كَانَتْ فَاعِلًا.

=== BLOCK 10: Parsing Evidence ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: الشَّجَرَةَ
[DETAILS_1]: مَفْعُولٌ بِهِ مَنْصُوبٌ، وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ عَلَى آخِرِهِ.
[WORD_2]: يُسْعِدُكَ
[DETAILS_2]: فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْكَافُ: ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبِ مَفْعُولٍ بِهِ مُقَدَّمٍ.

=== BLOCK 11: Exam 1 ===
(Component: TEMPLATE_C_EXAM.html)
[QUESTION_NUMBER]: ١
[QUESTION_TEXT]: اسْتَخْرِجِ الْمَفْعُولَ بِهِ مِنَ الْجُمَلِ الْآتِيَةِ وَاذْكُرْ عَلَامَةَ نَصْبِهِ:
- غَرَسَ الْفَلَّاحُ الشَّجَرَةَ.
- يَحْمِلُ الطَّالِبُ الْكُتُبَ.
- أَطِعْ أَبَاكَ.
- حَفِظَ الطَّالِبُ الْقَصِيدَتَيْنِ.
- كَافَأْتُ الْمُتَفَوِّقِينَ.
- عَلَّقَ سَعِيدٌ اللَّوْحَاتِ.

=== BLOCK 12: Exam 2 ===
(Component: TEMPLATE_C_EXAM.html)
[QUESTION_NUMBER]: ٢
[QUESTION_TEXT]: أَعْرِبِ الضَّمَائِرَ الْمُتَّصِلَةَ بِالْأَفْعَالِ فِي الْجُمَلِ الْآتِيَةِ:
- يُسْعِدُكَ النَّجَاحُ.
- الدَّرْسُ شَرَحَهُ الْمُعَلِّمُ.
- عَالَجَنِي الطَّبِيبُ.

--- END STREAM ---