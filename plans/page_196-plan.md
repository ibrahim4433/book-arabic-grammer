# **SESSION 196**

[TASK DEFINITION]
Objective: Implement page 196.
File: `pages/page_196.html` (Note: Use the exact page number.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools. If it overflows, it is a catastrophic failure. Do NOT try to solve overflow by deleting text (Strict Typographer Rule). Solve it by choosing denser templates or omitting optional white-space.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`. Ensure exact visual continuity (same title, same classes).
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md` to identify the correct template to use for the continuation. You are forbidden from guessing. Scan the raw text for the preceding keyword to determine the active template and apply the correct `_PART_2.html` wrapping.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
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
6. Templates: You are forbidden from inventing new HTML tags or classes or template elements. You must map all content using "Jules-workspace/Templates/" components as the STREAM says in suitable way. **CRITICAL 1-PAGE MODE RULE**: You MUST NOT use `<section>` tags when applying templates. Replace any `<section>` tags from the templates with `<div>` tags (keep `<header>` for page headers as is).
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). The ID MUST be applied to the `<div>` tag that replaced the `<section>` tag. Use "Jules-workspace/id_manager.py" to generate or verify them.
8. **Self-Correction:** Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files. If it fails, you MUST fix the errors (usually inline styles or forbidden section tags) before submitting.
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
[LESSON_NUMBER]: 196
[CHAPTER_TITLE]: page 196
[CATEGORY_HEADER]: 196
[SECTION_HEADER]: 196
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Poem Continuation ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[BLOCK_TITLE]: القصيدة (تتمة)
[CONTENT]: -١٠ <span class="highlight-red">حَائِرَ</span> <span class="highlight-blue">الطَّرْفِ</span> <span class="highlight-red">شَارِدَ</span> <span class="highlight-blue">الْفِكْرِ</span> <span class="highlight-green">يَحْكِي</span> مُدْجِاً فِي الظَّلَامِ ضَلَّ السَّبِيلا

=== BLOCK 3: Explanation 10 ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: الشرح
[CONTENT]: المفردات: مدي: الذي يسير في الليل. ضل: تاه وأضاع الطريق<br>الشرح: يُعاني هذا المَغْتَرَبُ فِي غُرْبَتِهِ مِنَ الخَيْرَةِ والضياع، فَيَبْدُو مُضْطَرَبًا، قَلِقًا، حائِرَ الطَّرْف، شارِدَ الْفِكْرِ كالنَّائِهِ الذي ضَل الطريق في ليلة بَهِيمَةٍ مُظْلِمَةِ حَالِكَةِ الظُّلُمَةِ لَا يُرَى فِيهَا مَعْلَمًا يُهْتَدَى به.

=== BLOCK 4: Idea 10 ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[CONTENT]: الفكرة: تصوير حَيْرَةِ الْمُغْتَرَبِ وَقَلَقِهِ وَضَيَاعِهِ.

=== BLOCK 5: Irab Row 1 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b1001
[TARGET_WORD_1]: حائر
[IRAB_ANALYSIS_1]: حالٌ مَنْصُوبَة.ٌ
[UNIQUE_ID_2]: b1002
[TARGET_WORD_2]: الطَّرْفِ
[IRAB_ANALYSIS_2]: مُضَاف إليهِ مَجْرُورٌ

=== BLOCK 6: Irab Row 2 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b1003
[TARGET_WORD_1]: شَارِدَ
[IRAB_ANALYSIS_1]: حالٌ مَنْصُوبَةٌ
[UNIQUE_ID_2]: b1004
[TARGET_WORD_2]: الفِكْرِ
[IRAB_ANALYSIS_2]: مُضَافُ إِلَيهِ مَجْرُورٌ

=== BLOCK 7: Irab Row 3 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b1005
[TARGET_WORD_1]: يَحْكِي
[IRAB_ANALYSIS_1]: فِعْلَ مُضَارِعٌ مَرْفُوعٌ
[UNIQUE_ID_2]: b1006
[TARGET_WORD_2]: مُدْجًا
[IRAB_ANALYSIS_2]: مَفْعُولُ بِهِ مَنْصُوبُ

=== BLOCK 8: Irab Row 4 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b1007
[TARGET_WORD_1]: السَّبِيلا
[IRAB_ANALYSIS_1]: مَفْعُولٌ بِهِ مَنْصُوب، وعلامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَة،ُ وَالأَلِف،ُ الإطلاق القافية.
[UNIQUE_ID_2]: b1008
[TARGET_WORD_2]: جملة )تحكي(
[IRAB_ANALYSIS_2]: حالِيَّة،ٌ مَحَلَّهَا النَّصْب.

=== BLOCK 9: Irab Row 5 ===
(Component: TEMPLATE_C_IRAB_BOX.html)
[UNIQUE_ID]: b1009
[TARGET_WORD]: جمله )ضَلَ(
[IRAB_ANALYSIS]: صِفَة،ٌ مَحَلَّهَا النَّصْب.ِ

=== BLOCK 10: Poem 11 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البيت الحادي عشر
[POET_NAME]:
[RIGHT_HEMISTICH]: -۱۱ تاة في عَالَمَ الْخَيَالِ فَضَاعَتْ
[LEFT_HEMISTICH]: نَفْسُهُ وهي تَنْشُد المستحيلا

=== BLOCK 11: Explanation 11 ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: الشرح
[CONTENT]: المفردات: تنشد: تطلب<br>الشرح: راوَدَتْ نَفْسَهُ الأَحلام، وواكَبَتْ فِكْرَهُ الْأُمْنِيات، فَتَاهَ فِي عالم الحَيَالِ مُحَاوِلَا بَلُوعَهَا، لَكِنَّهُ أَضَاعَ عُمْرَهُ وهو يبحَثُ عَنْ غايَاتِهِ.

=== BLOCK 12: Idea 11 ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[CONTENT]: الفكرة : ضَيَاعُ عُمْرِ الْمُغْتَرَبِ دُونَ تَحْقِيقٍ غَايَاتِهِ.

=== BLOCK 13: Irab Row 6 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b1010
[TARGET_WORD_1]: تاه
[IRAB_ANALYSIS_1]: فعل ماض، مَبْنِي على الفَتْحَةِ الظَّاهِرَةِ
[UNIQUE_ID_2]: b1011
[TARGET_WORD_2]: الْحَيَالِ
[IRAB_ANALYSIS_2]: مُضَافُ إِلَيهِ مَجْرُورٌ

=== BLOCK 14: Irab Row 7 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b1012
[TARGET_WORD_1]: فَضَاعَتْ
[IRAB_ANALYSIS_1]: الفَاء،ُ حَرْفُ عَطْفٍ
[UNIQUE_ID_2]: b1013
[TARGET_WORD_2]: نَفْسُهُ
[IRAB_ANALYSIS_2]: فَاعِلْ مَرْفوع، وعلامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَة،ُ والهاء، ضميرٌ مُتَّصِلِّ مَبْنِي على الضم في محل جر، مُضَافَ إِلَيْه.ِ

=== BLOCK 15: Irab Row 8 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b1014
[TARGET_WORD_1]: وهي
[IRAB_ANALYSIS_1]: الواو، واو الحال هي، ضميرُ رَفْعِ مُنْفَصِلٌ مَبْنِي على الفَتْحِ في محل رَفْع،ِ مُبْتَدَا
[UNIQUE_ID_2]: b1015
[TARGET_WORD_2]: المستَحِيلا
[IRAB_ANALYSIS_2]: مَفْعُولَ بِهِ مَنْصُوب،ٌ وعلامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَة،ُ والأَلِف،ُ لإطلاق القافية.

=== BLOCK 16: Irab Row 9 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b1016
[TARGET_WORD_1]: جملة )تاة(
[IRAB_ANALYSIS_1]: اسْتِنْنَافِيَّة،ٌ لَا مَحَلَّ لَهَا مِنَ الإعراب
[UNIQUE_ID_2]: b1017
[TARGET_WORD_2]: جملة )ضاعت(
[IRAB_ANALYSIS_2]: مَعْطُوفَة،ٌ لَا مَحَلَّ لها من الإعراب

=== BLOCK 17: Irab Row 10 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b1018
[TARGET_WORD_1]: جملة )هيَ تَنْشُدُ(
[IRAB_ANALYSIS_1]: حالِيَّة،ٌ مَحَلُّها النَّصْبِ
[UNIQUE_ID_2]: b1019
[TARGET_WORD_2]: جملةً تَنْشُدُ(
[IRAB_ANALYSIS_2]: خَبَرَيَّة،ٌ مَحَلُها الرَّفْع.

=== BLOCK 18: New Section Header ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: المطالعة
[CONTENT]: رسالة الشرق المتجدد<br>ميخائيل نعيمة (۱۸۸۹ - ۸۸۹۱م)

=== BLOCK 19: Reading 1 ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: (۱)
[CONTENT]: إِنَّ المَدَنِيَّة الغربية المُسَيْطِرة على العالم مُنْذُ أجيال وأجيال تَتَخَبَّطُ اليوم في شِبَاكِ مِنَ الْمُشْكِلاتِ المُعَقَّدَةِ التِي خَلَقَتْهَا مِنْ نَفْسِهَا لِنَفْسِهَا، وتُفَتِسُ عَنْ بَابِ للخلاص فلا تدي إليه ذَلِكَ أَنَّهَا صَرَفَتْ جُلَّ اهتمامها إلى العقل وترويضِهِ وَتَنْظِيمِهِ فَكَانَتْ هَذِهِ الطَّفْرَةُ البَاهِرَةُ فِي دُنيا العلوم النظرية والتطبيقية، وكانَ هَذَا الْفَيْضُ العَارِمُ مِنَ الاختراعات العجيبة والاكتشافاتِ المُذْهِشَة،ِ أَمَّا القَلْبُ الذِي تَصْطَرِعُ فِيهِ سُودُ الشَّهواتِ وبِيْضُهَا فَمَا أَحْسَنَتْ ترويضه وتنظيمه. فكان هذا الطَّغيانُ الذي نَشْهَدُهُ اليومَ مِنْ أَنانيةٍ وَحِقْدٍ وَبُغْضِ وَتَنَائِذٍ وَجَشَعِ وَمَكْرٍ وَدَهَاءٍ وَغَيْرِهَا مِنَ الشَّهَوَاتِ السُّودِ وَمِنْ شَأْنِ هَذِهِ الشَّهَوَات،ِ إذا اسْتَفْحَلَ أَمْرُهَا، أَنْ تَعْبَثَ بِنِتاج العَقْلِ فَتَجْعَلَهُ أَدَاةَ تَخْرِيبِ بَدَلَ التَّعْمير،ٍ وَمَصْدَرَ شَقَاءِ لا هناء، ونُقْطَةَ انزلاق لا انطلاق. وها هي تُقَوّضُ اليومَ أَرْكَانَ هَذِهِ المَدَنَيَّةِ مِثْلَمَا قَوَّضَتْ أَركانَ مَا سَبَقَهَا مِن مَدَنِيَّاتٍ.<br>وإنِّي لَأَسْأَل:ُ إِذَا انْهَارَتِ الْمَدَنِيَّةُ الحَاضِرَةُ - وَلَسَوْفَ تَنْهَارُ - فَمَنْ ذَا الذي سَيَرِفَعْ لِلبَشَرِيَّةِ مِشْعَلَ الحِدَايَة،ِ وَيُقِيلَهَا مِنْ عَشْرِهَا، ثُمَّ يقودها في الطريق السَّوي إلى الهَدَفِ السَّمِي الْمُعَدِّ لها مُنْدُ الأَزَلِ؟

=== BLOCK 20: Reading 2 ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: (Y)
[CONTENT]: إِنَّ لِلأَرْمِنَةِ دَلَائِلَهَا، وَدَلَائِلُ زمان نَحْنُ فِيهِ لا تترك فِي ذِهْنِي أَقَلَ الشَّكَ فِي أَنَّ الشَّرْقَ مَدْعُوٌّ لِلقِيَامِ بِهَذِهِ المَهَمَّةِ الخطرةِ مِن جديد، فهو الذي انْبَرَى لها مرة بعدَ مَرَّةٍ مُنْدُ فَجْرِ التَّاريخ، فَمَا أَفْلَحَ الإِفْلَاحَ كَلَّه،ُ ولا أَخْفَقَ الإِخْفَاقَ كُلَّه.ُ وما الديانات التي نشرها في الأَرْض،ِ على اختلاف أَسْمَائِهَا وَمَسَالِكِها، سوى مناهج ترمي إلى ترويض القلب على طريق الخير كي ما يتاحَ لَهُ أَنْ يبصر طريقه إلى الهَدَفِ الأَبْعَدِ وَالأَسْمَى، ألا وهو المعرفة والقدرة، والحرية التي مِنْ شَأْنِهَا أَنْ تعود بالإِنْسَان إلى تكوينه الإلهي.<br>تلك في خطوطها الواسعة، هي رسالةُ كُلِّ دِينِ مِنَ الأَدْيَانِ التي جاء بها المَشْرِقُ وَلَقَدْ حاول الشَّرْقُ فيما مَضَى أَنْ يُطَيِّقَ دِيْنَهُ عَلَى دنياه، وأن يجعل مِنَ الأَرْضِ سَلَّما يرقى به إلى السَّمَاء،ِ فَمَا نَجَحَ مِن بنيه غير أَفْرَاد،ٍ أُولَئِكَ هُمُ الأنبياء، والأولياء، والقديسون، والمختارون، أما الجماهير فَقَدْ أَجْهَدَتْهَا الْمُحَاولةُ وَأَفْكَتْ قواها، فَلَاذَتْ بِالْقُشُورِ وَأَهْمَلَتِ اللُّبَابَ.

=== BLOCK 21: Reading 3 ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: (۳)
[CONTENT]: وهكذا هَجَعَ الشَّرْقُ هَجْعَتَهُ الطويلة، وقد سيم في خلالها شَتَّى أَنواع الدُّل والهَوَانِ على يد أخيه الغرب، ولكنهُ اليومَ يَنْتَفِضُ انتِفَاضَةَ الجبار،ِ فَيَنْزَعُ عَنْهُ مَعْلَمًا تِلْوَ مَعْلَمٍ مِنْ مَعَالم الاستثمار والاستِعْمَار،ِ وَيَكْشَحُ ظُلُمَاتِ الدُّ والهوان، ويعمل بنشاط والدفاع على ترميم ما انهار مِنْ عَزِيمَتِه،ِ وَاسْتِرْدَادِ مَا ضَاعَ مِنْ حَقِّهِ،ِ وَتَلْيينِ مَا تَصَلَّبَ مِنْ شَرايينه، فهو كالنَّسْرِ يُحَدِّدُ شَبَابَهُ وَيَتَطَلَعُ إِلَى عَالَم أَرْحَبَ وَأَفْضَلَ وَأَجْمَلَ مِن عَالَمَ هو فيه.

=== BLOCK 22: Cut Content 1 ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
[BLOCK_TITLE]: المطالعة (يتبع)
[CONTENT]: وما العالم الذي نَعِيشُ فِيهِ اليومَ وَكَأَنَّنا نعيش على فوهة بركان، إِنَّهُ لَعَالَمَ انْشَطَرَ إِلَى مُعَسْكَرَيْنَ مُدَجَّجَيْن بالسلاح، وكلاهما يرتقِبُ الفُرْصَةَ الموانِيةَ لينقض على الآخر فلا يُبْقِي ولا يَدَر.ُ وليس يعنيهُمَا مِنَ الإِنْسَانِ سوى أَنَّهُ مُنْتِج ومُسْتَهْلِك،َ وصاحِبُ عَمَلٍ أَو عامِلٌ وَأَنَّهُ - - مكت

=== BLOCK 23: The Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
[TABLE_TITLE]: خلاصة الأفكار
[TABLE_HEADER_1]: البيت
[TABLE_HEADER_2]: الفكرة
[ROW_1_COL_1]: البيت العاشر
[ROW_1_COL_2]: تصوير حَيْرَةِ الْمُغْتَرَبِ وَقَلَقِهِ وَضَيَاعِهِ.
[ROW_2_COL_1]: البيت الحادي عشر
[ROW_2_COL_2]: ضَيَاعُ عُمْرِ الْمُغْتَرَبِ دُونَ تَحْقِيقٍ غَايَاتِهِ.

--- END STREAM ---
