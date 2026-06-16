# **SESSION 06.0**

[TASK DEFINITION]
Objective: Implement كَيْف تُعْرِبُ ؟( خَطْوَاتِ الْإِعْرَابِ الصَّحِيحِ.
File: `pages/06_nXX_كَيْف تُعْرِبُ ؟( خَطْوَاتِ الْإِعْرَابِ الصَّحِيحِ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/06_...` if page have a lot of blank space add exam elements from the lesson.
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
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
15. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 06
[CHAPTER_TITLE]: كَيْف تُعْرِبُ ؟( خَطْوَاتِ الْإِعْرَابِ الصَّحِيحِ
[CATEGORY_HEADER]:
[SECTION_HEADER]:
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Introduction ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مُقَدَّمَةً
Content:
<p class="text-accent mb-2mm">يَسْأَلُ الْكَثِيرُ مِن الطُّلَاَّبِ كَيْف أَسْتَطِيعُ إِعْرَابَ الْكَلِمَاتِ وَتَحْدِيدِ مَوْقِعِهَا وَعُلَّامَتِهَا بِطَرِيقَةٍ صَحِيحَةٍ دُون أَخْطَاءٍ ؟</p>
<p>عَمَلِيَّةُ الْإِعْرَابِ تُشْبِهُ تَشْخِيصُ الطَّبِيبِ لِلْمَرِيضَ فِي الْمُسْتَشْفَى لِكَي نَصِفُ الْعِلَاَجَ ( الْإِعْرَابَ النِّهَائِيَّ ) بِدِقَّةٍ ، يَجِبُ أَنّ نَمِرٍ بِأَرْبَعِ خَطْوَاتٍ أَو " تحاليل " أَسَاسِيَّةً</p>

=== BLOCK 3: The 4 Steps Grid ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الْخَطْوَاتِ الْأَرْبَعَ لِلْإِعْرَابَ
Content:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEMS]:
1. <b>نَوْعُ الْكَلِمَةِ :</b> هَلٌّ هِي ( اِسْمٌ ، أَم فعَلّ ، أَم حَرْفُ )؟ وهَل هِي ( مُفْرَدٌ ، أَم مُثَنًّى ، أَم جَمْعُ )؟
2. <b>الْمَوْقِعُ الْإِعْرَابِيُّ :</b> مَا وَظِيفَةِ هَذِه الْكَلِمَةِ فِي الْجُمْلَةِ ؟( هَل هِي فَاعِلٍ ، مَفْعُولٌ بِه ، مُبْتَدَأٌ ، خَبَرٌ ...؟)
3. <b>الْحَالَةُ الْإِعْرَابِيَّةُ :</b> هَل مَوْقِعِهَا يَتَطَلَّبُ ( الرَّفْعَ ، أَم النُّصْبُ ، أَم الْجَرُّ ، أَم الجزم )؟
4. <b>الْعُلَّامَةُ الْإِعْرَابِيَّةُ :</b> بِنَاءً عَلَى نَوْعِهَا وَحَالَتِهَا ، مَا هِي الْحَرَكَةِ أَو الْحَرْفُ الَّذِي سَتَأْخُذُهُ فِي آخِرِهَا ؟( ضَمَّةً ، فَتْحَةً ، كَسِرَّةٍ ، أَلَفٌّ ، واو ، ياء ).

=== BLOCK 4: Practical App 1 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: التَّطْبِيقَ الْعَمَلِيَّ ( 1 )
Content:
<p class="font-bold mb-2mm">الْمِثَالَ :" إِِْنّ الْمُعَلِّمَ يُحِبُّ <span class="highlight-blue">الْمُجْتَهِدِينَ</span> ".</p>
<p>لِنُعْرِبُ كَلَمَّةِ <b>( الْمُجْتَهِدِينَ )</b> بِتَطْبِيقِ الْخَطْوَاتِ الْأَرْبَعَ</p>
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEMS]:
1. <b>النَّوْعُ :</b> اِسْمٌ ، جَمَعَ مُذَكَّرُ سَالِمُ
2. <b>الْمَوْقِعُ :</b> مِن الَّذِي يُحِبُّ ؟ الْمُعَلِّمَ مَاذَا يُحِبُّ ؟ الْمُجْتَهِدِينَ إِذْنُ وَقْعٍ عَلَيْهُمْ فعَلّ الْفَاعِلِ ، فهِي <b>( مَفْعُولٌ بِه )</b>.
3. <b>الْحَالَةُ :</b> الْمَفْعُولُ بِه دَائِمًا يُكَوِّنُ فِي حَالَةٍ <b>( نُصِبْ )</b>.
4. <b>الْعُلَّامَةُ :</b> عُلَّامَةُ النُّصْبِ لِجَمَعَ الْمُذَكَّرُ السَّالِمُ هِي <b>( الياء )</b>.

=== BLOCK 5: Practical App 1 Result ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Title: الْإِعْرَابَ النِّهَائِيَّ ( وَصَفَّةَ الدَّوَاءِ )
Content:
<p>مَفْعُولٌ بِه مَنْصُوبٍ ، وَعُلَّامَةَ نُصْبِهِ الياء لأَنّهُ جَمْعَ مُذَكَّرَ سَالِمَ</p>

=== BLOCK 6: Practical App 2 Summary Table ===
(Component: TEMPLATE_C_BLOCK.html)
Title: التَّطْبِيقَ الْعَمَلِيَّ الشَّامِلَ ( 2 )
Content:
<p class="font-bold text-center mb-2mm">ذَاكَرَ الطَّالِبُ الْمُجْتَهِدُ الدُّرُوسَ صَبَاحًا مُرَكَّزًا رَغْبَةً فِي النُّجَّاحِ وَالتَّفَوُّقِ .</p>
<p class="mb-2mm">فِي بِدَايَةِ الْإِعْرَابِ ، نَسْأَلُ دَائِمًا :<b> مَا نَوْعِ الْجُمْلَةِ ؟</b> بَدَأَتْ بِفِعْلِ ( ذَاكِرَ )، إِذَن هِي جُمْلَةِ فِعْلِيَّةِ نَبْدَأُ بِفَكِّ شَفْرَاتِهَا بِطَرْحِ الْأسْئِلَةِ</p>
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: الْكَلِمَةُ
[HEADER_2]: السُّؤَالُ
[HEADER_3]: الْإِعْرَابُ
Row 1: [CELL_1]: ( ذَاكِرَ ) [CELL_2]: - [CELL_3]: فعَلّ مَاضٍ مَبْنِيِّ عَلَى <span class="highlight-red">الْفَتْحِ</span> .( الْفِعْلِ الْمَاضِي دَائِمًا مَبْنِيَّ ).
Row 2: [CELL_1]: ( الطَّالِبُ ) [CELL_2]: مَنَّ ذَاكِرَ ؟( الْإِجَابَةَ عَن " مَنَّ " تُعْطِينَا الْفَاعِلُ ) [CELL_3]: فَاعِلَ مَرْفُوعَ وَعُلَّامَةَ رَفْعِهِ <span class="highlight-red">الضَّمَّةَ</span>
Row 3: [CELL_1]: ( الْمُجْتَهِدُ ) [CELL_2]: الطَّالِبَ مَنَّ ؟/ مَا صَفَّتِهِ ؟ [CELL_3]: نَعَتْ ( أَو صَفَّةُ ) مَرْفُوعٌ وَعُلَّامَةُ رَفْعِهِ <span class="highlight-red">الضَّمَّةَ</span> .( تَتْبَعُ الْمَوْصُوفُ ).
Row 4: [CELL_1]: ( الدُّرُوسَ ) [CELL_2]: مَاذَا ذَاكِرُ ؟( الْإِجَابَةَ عَن " مَاذَا " تُعْطِينَا الْمَفْعُولُ بِه ) [CELL_3]: مَفْعُولٌ بِه مَنْصُوبٍ وَعُلَّامَةِ نُصْبِهِ <span class="highlight-red">الْفَتَحَةِ</span>
Row 5: [CELL_1]: ( صَبَاحًا ) [CELL_2]: مَتَى ذَاكِرُ ؟( الْإِجَابَةَ عَن " مَتَى " تُعْطِينَا ظَرْفُ الزَّمَانِ / الْمَفْعُولَ فِيهِ ) [CELL_3]: ظَرُفَ زَمَانُ مَنْصُوبٍ وَعُلَّامَةِ نُصْبِهِ <span class="highlight-red">الْفَتَحَةِ</span>
Row 6: [CELL_1]: ( مَرْكَزًا ) [CELL_2]: كَيْف ذَاكِرُ ؟( الْإِجَابَةَ عَن " كَيْف " تُعْطِينَا الْحَالُ ) [CELL_3]: حَالَ مَنْصُوبَةَ وَعُلَّامَةَ نُصْبِهَا <span class="highlight-red">الْفَتَحَةِ</span> .( الْحَالُ دَائِمًا مَنْصُوبَةً ).
Row 7: [CELL_1]: ( رَغْبَةً ) [CELL_2]: لِمَاذَا ذَاكِرَ ؟( مِن أَجَل مَاذَا ؟)( الْإِجَابَةَ عَن " لِمَاذَا " تُعْطِينَا الْمَفْعُولُ لِأَجَّلَهُ ) [CELL_3]: مَفْعُولٌ لِأَجَّلَهُ مَنْصُوبٌ وَعُلَّامَةُ نُصْبِهِ <span class="highlight-red">الْفَتَحَةِ</span>
Row 8: [CELL_1]: ( فِي ) [CELL_2]: - [CELL_3]: حَرْفَ جَرِّ مَبْنِيِّ
Row 9: [CELL_1]: ( النُّجَّاحِ ) [CELL_2]: - [CELL_3]: اِسْمَ مَجْرُورَ ب ( فِي ) وَعُلَّامَةَ جُرِّهِ <span class="highlight-red">الْكُسَّرَةِ</span>
Row 10: [CELL_1]: ( و ) [CELL_2]: - [CELL_3]: حَرْفَ عَطْفٍ
Row 11: [CELL_1]: ( التَّفَوُّقِ ) [CELL_2]: - [CELL_3]: اِسْمَ مَعْطُوفٍ عَلَى ( النُّجَّاحَ ) مَجْرُورٌ وَعُلَّامَةُ جُرِّهِ <span class="highlight-red">الْكُسَّرَةِ</span> .( لأَنّ الْمَعْطُوفِ يَتْبَعُ الْمَعْطُوفُ عَلَيْهِ ).

=== BLOCK 7: Questions Introduction ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَدْرِيبَاتٍ وَتَطْبِيقَاتٍ عَمَلِيَّةٍ ( مُسْتَخْرَجَةً مِن الدَّرْسِ )
Content:
<p class="font-bold mb-2mm">السُّؤَالَ الْأَوَّلَ اِمْلَأْ الْفَرَاغَاتِ لِاِكْتِشَافَ الْمَوْقِعِ الْإِعْرَابِيِّ فِي الْجُمْلَةِ الْفِعْلِيَّةِ :</p>

=== BLOCK 8: Exam Question 1 ===
(Component: TEMPLATE_C_EXAM.html)
[QUESTION_NUMBER]: ١
[QUESTION_TEXT]: لِمَعْرِفَةُ الْفَاعِلِ نَسْأَلُ بِكَلِمَةٍ :.....................

=== BLOCK 9: Exam Question 2 ===
(Component: TEMPLATE_C_EXAM.html)
[QUESTION_NUMBER]: ٢
[QUESTION_TEXT]: لِمَعْرِفَةُ الْمَفْعُولِ بِه نَسْأَلُ بِكَلِمَةٍ :.....................

=== BLOCK 10: Exam Question 3 ===
(Component: TEMPLATE_C_EXAM.html)
[QUESTION_NUMBER]: ٣
[QUESTION_TEXT]: لِمَعْرِفَةُ الْمَفْعُولِ لِأَجَّلَهُ ( السَّبَبَ ) نَسْأَلُ بِكَلِمَةٍ :.....................

=== BLOCK 11: Exam Question 4 ===
(Component: TEMPLATE_C_EXAM.html)
[QUESTION_NUMBER]: ٤
[QUESTION_TEXT]: لِمَعْرِفَةُ الْحَالِ ( الْهَيْئَةَ ) نَسْأَلُ بِكَلِمَةٍ :.....................

=== BLOCK 12: Exam Question 5 ===
(Component: TEMPLATE_C_EXAM.html)
[QUESTION_NUMBER]: ٥
[QUESTION_TEXT]: لِمَعْرِفَةُ ظَرْفِ الزَّمَانِ نَسْأَلُ بِكَلِمَةٍ :.....................

=== BLOCK 13: Questions Introduction 2 ===
(Component: TEMPLATE_C_BLOCK.html)
Title:
Content:
<p class="font-bold mb-2mm">السُّؤَالَ الثَّانِي أَعْرَبَ الْكَلِمَاتُ الْمُلَوَّنَةُ بَنَّاءً عَلَى الْخَطْوَاتِ الْأَرْبَعَ :</p>
<p class="text-center mb-2mm">شَرِبَ الْمَرِيضُ الدَّوَاءَ أَمَلًا فِي الشِّفَاءِ</p>

=== BLOCK 14: Exam Question 6 ===
(Component: TEMPLATE_C_EXAM.html)
[QUESTION_NUMBER]: ١
[QUESTION_TEXT]: الْمَرِيضُ :

=== BLOCK 15: Exam Question 7 ===
(Component: TEMPLATE_C_EXAM.html)
[QUESTION_NUMBER]: ٢
[QUESTION_TEXT]: الدَّوَاءُ :

=== BLOCK 16: Exam Question 8 ===
(Component: TEMPLATE_C_EXAM.html)
[QUESTION_NUMBER]: ٣
[QUESTION_TEXT]: أَمَلًا :

--- END STREAM ---
