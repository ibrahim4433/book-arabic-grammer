# **SESSION 194**

[TASK DEFINITION]
Objective: Implement page 194.
File: `pages/page_194.html` (Note: Use the exact page number.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`.
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md`.
3. Text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide: NO INLINE STYLES. Irab Words inside `.irab-word` MUST be white.
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). Use "Jules-workspace/id_manager.py" to generate or verify them.
8. Self-Correction: Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...).
11. You must preserve the exact Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense.
13. balanced page colors between teal and orange: make sure every page have minimum 1 element in orange instead of all teal.
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html`.
15. Exam section always be in the end of the lesson (in the final page of that lesson), and without the answers!

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[CATEGORY_HEADER]: 194
[SECTION_HEADER]: 194
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+
[CHAPTER_TITLE]: page 194
[LESSON_NUMBER]: 194

=== BLOCK 2: تابع التدريبات ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[BLOCK_TITLE]: تابع التدريبات
[CONTENT]: - اسْتَخْرِجُ مِنَ البيت الثالث مُحَسَنَا بديعيا مَعْنويًا، وَاذْكَرْ نَوْعَه،ُ ج۱ - المُحَسَنُ البَدِيعِيَّ المَعْنَوِي:ُّ (الشباب،ُ شَيْحًا). - نَوْعُهُ طِبَاقُ إِيجاب.
- استخرج مِنَ البيت الخامس مُحَنَا بديعيًا، واذْكُرُ نَوْعَه،ُ ج -۲ الْمُحَسَنُ البَدِيعِيُّ اللَّظِيُّ : ( لا، ظليلا). - نَوْعُهُ جناس ناقص (جناس اشتقاقي).

=== BLOCK 3: تحليل الصور والموسيقا ===
(Component: TEMPLATE_C_LIST.html)
[LIST_TITLE]: تابع التدريبات
[LIST_ITEM_CONTENT_1]: سم الصُّور الآتية، ثُمَّ حَلها : (الشَّفَقُ الوردي يُغْريه - اليَأْسُ صَدَّ عَنْهُ النَّسِيمُ مَرَّ عليه). ج - الصورة : (الشَّفَقُ الوردي يُغْريه). - تَسْمِيَةُ الصورة: اسْتِعَارَةٌ مَكْنِيَّة. - تحليل الصورة: شَبَّةَ الشَّفَقَ بِحَسَاءَ تُغْرِي، حَذَفَ الْمُشَبَّةَ بِه،ِ وَأَبْقَى شَيْئًا مِنْ لَوَازِمِه،ِ وهو (يُقْرِيهِ). - الصورة: (اليَأْسُ صَدَّ عَنْهُ). - تَسْمِيَةُ الصُّورَةِ اسْتِعَارَةً مَكْنِيَّة.ٌ - تحليل الصورة: شَبَّةَ اليَأْسَ بِإِنْسَانٍ يَصُد،ُّ حَدَّفَ الْمُشَبَّهَ بِه،ِ وَأَبْقَى شَيْئًا مِنْ لَوَازِمِه،ِ وهو (صَدَّ). - الصورة: (النسيم مَرَّ عليه). - تَسْمِيَةُ السُّورَة:ِ استِعَارَةٌ مَكْنِيَّة.ٌ - تَخْلِيلُ الصُّورة : شَبَّةَ النَّسِيمَ بِإِنْسَانٍ يَمْر،ُ حَذَفَ الْمُشَبَّةَ بِه،ِ وَأَبْقَى شَيْئًا مِنْ لَوَازِمِه،ِ وهو (مَرَّ).
[LIST_ITEM_CONTENT_2]: - هات مِنَ النَّصَ مَصْدَرًا مِنْ مَصَادِرِ الموسيقا الخارجيَّة،ِ وَمَثَلْ لَهُ بِمَا يُناسِبُه.ُ ج - إِنَّ البَحْرَ الذي نُظِمَتْ عليهِ أَبْيَاتُ هَذِهِ القَصِيدَةِ هُوَ البخرُ الخفيف، أَمَّا القَافِيَةُ فَقَدِ التزَمَ الشَّاعِرُ فِيهَا اللَّامَ رَوْيًّا مَعَ الأَلِفِ المُطْلَقَةِ التي تُوْحِي بِالْأَلَم وَالتَّأْوَّه.ِ

=== BLOCK 4: إعراب النص (البيت الأول) ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: إعراب | النص:
[RIGHT_HEMISTICH_1]: -۱ غَمَرَتْهُ الأَحلامُ بِالشَّفَقِ الوَرْدِي
[LEFT_HEMISTICH_1]: يُغْرِيهِ بِالمنى تَعْلِيلا

=== BLOCK 5: المفردات والشرح ===
(Component: TEMPLATE_C_TABLE.html)
[TABLE_TITLE]: المفردات
[COL_1_HEADER]: الكلمة
[COL_2_HEADER]: المعنى
[ROW_1_COL_1]: عَمَرَتُهُ
[ROW_1_COL_2]: غَطَّتْهُ
[ROW_2_COL_1]: الشَّفَقِ
[ROW_2_COL_2]: حُمْرَةٌ تَظْهَرُ فِي الْأُفْقِ حَيْثُ تَغْرُبُ الشَّمْسُ
[ROW_3_COL_1]: الوَرْدِي
[ROW_3_COL_2]: لون أحمر يضرب إلى صُفْرَةٍ حَسَنَةٍ فِي كل شيء
[ROW_4_COL_1]: يفريه
[ROW_4_COL_2]: يُولِعُهُ

=== BLOCK 6: المفردات والشرح ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: الشَّرح
[CONTENT]: الشَّرح : فَاضَتْ عَلَيْهِ الأَحْلَام،ُ وَتَزَاحَمَتْ فِي فِكْرِهِ الأَمَانِي رَاسِمَةً لَهُ عَالَمًا مُزْدَهِرًا فَاتِنَا ، بَدَا كَحَسْنَاءِ جَمِيلَةَ نَصَبَتْ لَهُ أَشْرَاكَ العَرَام.ِ وأَمَامَ هذا الإِغْرَاءِ هَامَ على وَجْهِهِ يَحَثُ الخَطَا صَوْبَ ذَاكَ العَالَمِ الوَرْدِي الرائع

=== BLOCK 7: الفكرة والبلاغة ===
(Component: TEMPLATE_C_BENEFIT.html)
[BENEFIT_TITLE]: الفكرة
[BENEFIT_CONTENT]: الفكرة اعترار المغترب بأحلام الغربة. البلاغة: (غَمَرَتْهُ الأَحلام)، (الشفق يُغْرِيهِ): استعارَةً مِكْنِيَّة.ٌ

=== BLOCK 8: الإعراب ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD_1]: عَمَرَتْهُ
[IRAB_ANALYSIS_1]: فِعْلِّ مَاضِ مَبْنِي على الفَتْحَةِ؛ لاتِصَالِهِ بِتَاءِ التَّانيثِ السَّاكِنَة.ِ والنَّاء،ُ حَرْفُ تأني لا مَحَلَّ لَهُ مِنَ الإعراب والهاء، ضمير متصل، مَبْنِي على الصَّمَ فِي مَحَلِّ نَصْب،ِ مَفْعُولُ بِهِ
[TARGET_WORD_2]: الأَحْلامُ
[IRAB_ANALYSIS_2]: فَاعِلْ مَرْفُوعُ
[TARGET_WORD_3]: الوَرْدِي
[IRAB_ANALYSIS_3]: صِفَةٌ مَجْرُورَةٌ وَعَلَامَةً جَرَهَا الكَسْرَةُ الظَّاهِرَة.ُ
[TARGET_WORD_4]: يُغْرِيهِ
[IRAB_ANALYSIS_4]: فِعْلَ مُصَارِعٌ مَرْفُوع، وعلامَةُ رَفْعِهِ الصَّمَةُ المُقَدَّرَةُ على الياء، مَتَعَ ظُهُورَها التقل. والهاء، ضمير مُتَصِل، مبي على الكسر في حَلِّ نَصْب،ِ مَفْعُولٌ بِهِ
[TARGET_WORD_5]: تَعْلِيلا
[IRAB_ANALYSIS_5]: حال مَنْصُوبَة،ٌ وعلامَةُ نَصْبِهَا الفَتْحَةُ الظَّاهِرَةُ
[TARGET_WORD_6]: جملة (غَمَرَتْهُ الأَحلام)
[IRAB_ANALYSIS_6]: ابْتِدَانِيَّة،ٌ لا محل لها مِنَ الإعراب
[TARGET_WORD_7]: جملة (يُغْريه)
[IRAB_ANALYSIS_7]: حاليَّة،ٌ مَحَلُّهَا النَّصْب.ُ

=== BLOCK 9: البيت الثاني ===
(Component: TEMPLATE_C_POEM.html)
[RIGHT_HEMISTICH_1]: وتلاشتْ حُلمًا فَحْلَمًا إلى اللاشيء
[LEFT_HEMISTICH_1]: تمشي بِهِ قَلِيلًا قَلِيلا

=== BLOCK 10: المفردات والشرح ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: المفردات
[CONTENT]: المفردات تلاشت : زَالَتْ

=== BLOCK 11: المفردات والشرح ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: الشرح
[CONTENT]: الشرح : عُمْرُ الْمُغْتَرَبِ بَدَاً بِالتَّسَرَّبِ وَالنَّفَادِ والضَّياع دُونَ أَنْ يُحَقِّقَ حُلُمَا مِنَ الأَحْلَامِ التِي رَاوَدَتْ نَفْسَه،ُ أو يَبْلُغَ أُمْنِيَةً مِنَ الأَمَانِي التِي دَاعَبَتْ فِكْرَهُ وَبَعْدَ أَنْ أَدْرَكَ سَرَابَ الأَحْلَام،ِ وَوَعَى وَهُمَ الْأَمَانِي بَدَأَ التَّنَازُلَ عَنْ أَحْلَامِهِ الوَرْدِيَّةِ الوَاحِدَ تِلْوَ الآخر، حَتَّى تَلَاشَتْ مِن نَفْسِهِ مُخَلَفَةَ مَكَانَا أَلَمَا عَمِيفًا وَيَأْسًا رَاسِحًا

=== BLOCK 12: الفكرة ===
(Component: TEMPLATE_C_BENEFIT.html)
[BENEFIT_TITLE]: الفِكْرة
[BENEFIT_CONTENT]: الفِكْرة : تنازُلُ الْمُغْتَرَبِ وَتَخَلْبِهِ عَنْ أَحْلَامِهِ عَدَمُ قُدْرَةِ المُغْتَرَبِ عَلى تَحْقِيقِ أَحلامه( الإعراب:

=== BLOCK 13: الإعراب ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD_1]: وتلاشَتْ
[IRAB_ANALYSIS_1]: الواو ، حَرْفُ عَطْفُ لَاشَت،ْ فعل ماض، مَبْنِي على الفَتْحَةِ المُقَدَّرَةِ عَلَى الْأَلِفِ الْمَحْدُوفَةِ لا تِصَالِهِ بِتَاءِ التَّانيبُ السَّاكِنَةِ وَالنَّاء،ُ حَرْفُ تَأْنيتٍ لَا مَحَلَّ لَهُ مِنَ الإعراب
[TARGET_WORD_2]: حلما
[IRAB_ANALYSIS_2]: حالٌ مَنْصُوبَةٌ
[TARGET_WORD_3]: فَحُلمًا
[IRAB_ANALYSIS_3]: الفاء، حَرْفُ عَطْف. حلمًا، اسم مَعْطُوفٌ مَنْصُوبُ
[TARGET_WORD_4]: قَلِيلًا
[IRAB_ANALYSIS_4]: نائِبُ مَفْعُولِ مُطْلَقُ مَنْصُوب. هذا الإغراب على تَقْدِير : تَحْشِي بِهِ مَشْيًا قليلًا، وَيَصِحُ فِي إغرابها وجه آخَرُ (لا خلاف حَوْلَه)، وهو : نائِبُ مَفْعُولٍ فِيهِ ظَرْفُ زِمَانٍ مَنْصُوبٌ مُتَعَلِقٌ بِالفِعْلِ (تَمْشِي). على تَقْدِيرِ تَمَّشِي بِهِ زَمَنًا قليلا
[TARGET_WORD_5]: جمله تلاشَتْ
[IRAB_ANALYSIS_5]: مَعْطُوفَة،ٌ لا محل لها من الإعراب
[TARGET_WORD_6]: جملة (تمشي)
[IRAB_ANALYSIS_6]: حاليَّة،ٌ مَحَلُّهَا النَّصْب.ُ

=== BLOCK 14: البيت الثالث ===
(Component: TEMPLATE_C_POEM.html)
[RIGHT_HEMISTICH_1]: هو في مَيْعَةِ الشَّبَابِ ولو حَدَّقْتَ فِيهِ
[LEFT_HEMISTICH_1]: أَبْصَرْتَ شَيْحًا هَزِيْلا

=== BLOCK 15: المفردات والشرح والفكرة ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: المفردات
[CONTENT]: المفردات : بَيْعَة الشباب : الصبا، أوله ونشاطه ورَيْعَانُه.

=== BLOCK 16: المفردات والشرح والفكرة ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: الشرح
[CONTENT]: الشرح : تَرَكَتْ شِدَّةُ الْمُعَانَاةِ آثَارَهَا على ذَلِكَ الشَّاتِ الْمُغْتَرِبِ الفَيِّ الذي يَرْزَحْ تَحْتَ وَطَاةِ العَيْش،ِ فَصَيَّرَتْهُ شَيْحًا طَاعِنَا فِي السَّنَ ضَعِيفًا نَاحِلًا وَاهِنًا

=== BLOCK 17: المفردات والشرح والفكرة ===
(Component: TEMPLATE_C_BENEFIT.html)
[BENEFIT_TITLE]: الفِكْرة
[BENEFIT_CONTENT]: الفِكْرة : تصويرُ بُرُوزِ آثَارِ مُعَانَاةِ الْمُغْتَرَبِ (انعِكَاسِ عَذَابَاتِ المغترب ومعاناته على مُحَيَّاه)، (تصوير آثار الغُرْبَةِ الجَسَدِيَّة).

=== BLOCK 18: الإعراب ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD_1]: هو
[IRAB_ANALYSIS_1]: ضمير رفع منفصل، مَبْنِي على الفتح فِي حَلِّ رَفْع،ِ مُبْتَدَا.ً
[TARGET_WORD_2]: الشَّبَابِ
[IRAB_ANALYSIS_2]: مُضَافَ إِلَيْهِ مَجْرُور.ٌ
[TARGET_WORD_3]: ولو حَدَّقْتَ
[IRAB_ANALYSIS_3]: الواو، واو الحال. لو، حَرْفُ شَرْطِ غَيْرُ جَازِهِ
[TARGET_WORD_4]: شَيْخًا
[IRAB_ANALYSIS_4]: مَفْعُولُ بِهِ مَنْصُوبٌ
[TARGET_WORD_5]: هَزِيْلًا
[IRAB_ANALYSIS_5]: صِفَةٌ مَنْصُوبَةٌ
[TARGET_WORD_6]: جملة (هو فِي مَيْعَةِ الشَّبَابِ)
[IRAB_ANALYSIS_6]: اسْتنَافِيَّة،ٌ لَا مَحَلَّ لها مِنَ الإعراب
[TARGET_WORD_7]: جملة (لو حَدَّقْتَ فِيهِ أَبْصَرْتَ)
[IRAB_ANALYSIS_7]: حايَّة، محلها النصب
[TARGET_WORD_8]: جملة (حَدَّقْتَ)
[IRAB_ANALYSIS_8]: جُمْلَةُ الشَّرْطِ غير الظرفي، لا محل لها مِنَ الإعراب
[TARGET_WORD_9]: جملة (أَبْصَرْتَ)
[IRAB_ANALYSIS_9]: جَوَابُ الشَّرْطِ ، لَا مُحَلَّ لها مِنَ الإعراب.

=== BLOCK 19: البيت الرابع ===
(Component: TEMPLATE_C_POEM.html)
[RIGHT_HEMISTICH_1]: بِقَوَامِ كَأَنَّ قَاصِمَةَ الظَّهْرِ
[LEFT_HEMISTICH_1]: أَنَاخَتْ عَلَيْهِ حَمَلًا تَقِيلا

=== BLOCK 20: الشرح والفكرة ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: الشرح والفكرة
[CONTENT]: الشرح : بدا مُقَوَّسَ القَامَةِ حَانِيَ الظَّهْر،ِ يَنُوءُ بِعِمْلٍ هُمُومٍ حِسَام،ِ وَمَصَائِبَ عِظَامِ الْقِيَتْ على كاهِلِهِ الفكرة : تَصْوِيرُ بُرُوزِ آثَارِ مُعَانَاةِ المُغْتَرَبِ (انعِكَاسِ عَذَابَاتِ المغترب ومعاناته على مُحَيَّاه)، (تصوير آثار الغربة الجسدية).

=== BLOCK 21: الإعراب ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
[BLOCK_TITLE]: الإعراب
[CONTENT]: كَأَن،َّ حرف مُشَبَّهُ بِالفِعْلِ قَاصِمَة:َ

--- END STREAM ---
