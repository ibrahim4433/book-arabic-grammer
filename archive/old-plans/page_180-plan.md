# **SESSION 180**

[TASK DEFINITION]
Objective: Implement page 180.
File: `pages/page_180.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: Verify this using `verify_layout.py` or equivalent tools.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`.
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md`.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`, `.highlight-green` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide: NO INLINE STYLES. Irab Words inside `.irab-word` MUST be white.
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX') applied to the replacement `<div>`. Use "Jules-workspace/id_manager.py".
8. Self-Correction: Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...).
11. You must preserve the exact Tashkeel.
12. Visual Density: The page must be dense.
13. balanced page colors between teal and orange: minimum 1 element in orange.
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html`.
15. Exam section always be in the end of the lesson without the answers.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 180
[CHAPTER_TITLE]: page 180
[CATEGORY_HEADER]: 180
[SECTION_HEADER]: 180
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Introduction Prose ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مقدمة
Content: <p class="text-accent">ينبغي لَكُم أَنْ تُدْركوا أَنَّ بَقَاءَكُم بِينَ مَخَالِب الغُرْبَة،ِ وَأَنْيَابِ وحُشَتِهَا لِيسَ بِالأَمْرِ الحَمِيد،ِ لَأَنَّ الطَّبِيعِيَّ فِي الحَيَاةِ أَنْ يَكُونَ لِلْإِنْسَانِ وَطَنْ يَنْتَمِى إليه،ِ يَعِيسُ فِيهِ بِعِزَّة، ويموت ويُدْفَنُ فِي تُرَابِهِ فَتُرَابُ الوَطَنِ أَحَنُ مِنْ تُرَابِ الغَرْبَة،ِ وَسَمَاءُ الوَطَنِ أَكْثَرُ رَحَابَةً مِنْ سَمَائِهَا لِمَاذَا تَحْرِمُونَ أَجْسَادَكُمُ المُتَعَبَةَ مِنَ الرَّاحَةِ بِإِسْنَادِ ظُهُورِكُم على سَاقٍ نَخْلَةٍ بَاسِقَةٍ تُطَاولُ عَنَانَ السَّمَاءِ فِي وَطَنِكُم؟ لماذا تَحْرَمُونَ عُيُونَكُمْ مِنَ الاستِمْتَاعِ بِرُويَةِ سَنَابِلِ القَمْحِ الذهبيَّةِ التي اسْتَعَارَتْ لَوْهَا مِنْ لَوْنِ خُيُوطِ شَمْسِ الْوَطَنِ الدَّافِنَةِ أَلَا تَحِنُ أَرْوَاحُكُم لِذِكْرَى مَوْسِمِ الْحَصَاد،ِ ولِرَائِحَةِ خُبْرِ التَّنُّور.</p>

=== BLOCK 3: Benefit Box Orange ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: <p class="text-primary">عَلَيْكُم أَنْ تُدْرِكُوا أَنَّ الوَطَنَ الذي تركتُوهُ خَلْفَ الْأَمْوَاجِ جَنَّةً أَبْدَعَ اللَّهُ تَكُويَنَهَا، وَأَوْدَعَ فِيهَا أَرْوَعَ الْمُكَوَّنَاتِ فَطَبِيْعَةُ وَطَنِكُم تَقِفُ شَاهِدًا على عَظَمَةِ المُصَوّر الخلاق،ِ حيثُ تَتَجَلَّى آيَاتُ الجَمَالِ شَاخِصَة،ً تُزَاحِمُ أَبْدَعَ لَوْحَةٍ مُنْمَتْهَا يَدُ فَنَّانِ مُبْدِع. فيها النباتات والحيوانات والصخور والبحار والبحيرات العَذْبَةُ والأَمْوَاجُ الهَادِرَة،ُ والجِبَالُ الشَّاهِقَة،ُ والسُّهُولُ الشَّاسِعَة،ُ وَالضَابُ الصَّغِيرَة،ُ وَالأَنْهَارُ الضَّيِّقَة،ُ وَالأَمْطَارُ الغزيرة، والشلالات القَوِيَّة،ُ والشَّوَاطِئُ الجَذَابَة،ُ والأَزْهَارُ الرَّقِيقَة،ُ وَالأَشْجَارُ البَاسِقَة.ُ</p>

=== BLOCK 4: Standard Box ===
(Component: TEMPLATE_C_BLOCK.html)
Title: نداء
Content: <p>اهربوا مِنْ ضَجِيج الغُرْبَةِ وَصَخَبِهَا، وَأَقْبِلُوا على طَبِيعَةِ وَطَنِكُم فهي خَيْرُ مَلَاذ،ٍ وَأَنْجَى مَهْرَبِ لَكُم؛ ففيها الهُدُوءُ وَالرَّاحَةُ مِنْ قَسْوَةِ الحَيَاةِ تَعَالُوا لِتَلُوذُوا بالاستِمْتَاعِ بِصَوْتِ زَقْزَقَةِ العَصَافِير،ِ وَتَرَنُّمِ البلابِل،ِ وَحَفِيفِ أَوْرَاقِ الأَشْجَارِ. تعالوا لِتَهْنَؤُوا بالجلوس في سَهْل،ِ أو بارتِقَاءِ جَبَل، أو باستِنْشَاقِ هَوَاءٍ عَلِيلٍ تَعَالُوا لِتُجَدِّدُوا حَيَوِيَّتَكُم وَنَشَاطَكُم، وتَكْتَسِبُوا طَاقَةً تُخَلَّصُكُم مِنْ إِرْهَاقِ الحَيَاةِ وَضُغُوطَاتِهَا، بالسَّبَاحَةِ في البحر، أو بالجلوس على رِمَالِ شَاطِئِه.ِ إِنَّ كُلَّ هذا الخير الذي تَخْتَزِنُهُ طَبِيعَةُ وَطَنِكُم كَفِيلٌ بِمُعَالَجَةِ أَسْقَامِ أَرْوَاحِكُم، وَإِرَاحَةِ قُلُوبِكُم التِي أَتْعَبَتْهَا الْغُرْبَة.ُ</p>

=== BLOCK 5: Core Matrix (Answers) ===
(Component: TEMPLATE_C_TABLE.html)
[ROW_1_COL_1]: ج - أسلوبُ النَّفْى : (لَمْ تَجِي).
[ROW_1_COL_2]: الأَدَاةُ : لَمْ تُفِيدُ نَفْيَ وقوع الفعل المُضَارع في الزمن الماضي.
[ROW_2_COL_1]: أسلوب النفي: ليس حُزْنُ النَّفْسِ إِلَّا ظِلُّ وَهُم.
[ROW_2_COL_2]: الأداة: ليس. عاملة؛ لأَنَّهَا دَخَلَتْ على الجملة الاسمية.
[ROW_3_COL_1]: ج ۲ - الوَزْنُ الصَّرْفِي: تَجِي:
[ROW_3_COL_2]: تَفِل.
[ROW_4_COL_1]: يَفْنى:
[ROW_4_COL_2]: يَفْعَلُ
[ROW_5_COL_1]: السَّواقي:
[ROW_5_COL_2]: الفَوَاعِل.

=== BLOCK 6: Poem 1 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: تحليل مفصل المضمون الأبيات
[HEMISTICH_1]: ليس في الغَابَاتِ حُزْنٌ
[HEMISTICH_2]: لا ولا فيها الهموم

=== BLOCK 7: Poem 1 Analysis ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الشرح والفكرة
Content: <p><span class="font-bold">الشرح:</span> أَيُّهَا الإِنْسَانُ تعال إلى طَبِيْعَةِ الغَابَاتِ فَهِي عَالَمَ المَسَرَّاتِ وَالأَمَل،ِ عَالَم نَقِيَّ مِنَ الأَحْزَان،ِ فَجَرَّدٌ مِنَ الهُمُومِ لِذَا لَا يَشْعُرُ سُكَانُ الغَابِ بِأَي حُزن ولا تَنْتَابُهُم أَيَّةٌ هُمُوم،ِ فَلَيْسَ ثَمَّةٌ مَا يُعَكِّرُ صَفْوَهُمُ الْأَبَدِيَّ</p><p><span class="font-bold">الفكرة:</span> الغاب عَالَمُ المَسَرَّاتِ وَالفَرَحِ وَالْأَمَلِ (الدَّعْوَةُ للعيش في عالم الغابِ هَرَبًا مِنْ عَالَمَ المَدِينَةِ المَادِّي) (خُلُقُ الغَابِ مِنَ الهم والحزن).</p>

=== BLOCK 8: Poem 1 Irab ===
(Component: TEMPLATE_C_IRAB.html)
[IRAB_WORD_1]: ليس
[IRAB_TEXT_1]: فعل ماض ناقص، مَبْنِي عَلَى الفَتْحَةِ الظَّاهِرَة.ِ
[IRAB_WORD_2]: حزن
[IRAB_TEXT_2]: اسم (ليس) مُؤَخَرَ مَرْفُوع.
[IRAB_WORD_3]: لا
[IRAB_TEXT_3]: حَرْفُ نَفْي اسْتَعْمَلَهُ الشَّاعِرُ لِتَوْكِيْدِ نَفي (لَيْسَ)
[IRAB_WORD_4]: ولا
[IRAB_TEXT_4]: الواو، حَرْفُ عَطْفٍ لا، حَرْفُ نَفِي
[IRAB_WORD_5]: الهُمُومُ
[IRAB_TEXT_5]: مُبْتَدَا مُؤَخَرُ مَرْفُو ، وعلامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ وَسُكِنَ لِلضَّرُورَةِ الشِعْرِيَّة.ِ
[IRAB_WORD_6]: جملة (لَيْسَ فِي الغَابَاتِ حُزْنَ)
[IRAB_TEXT_6]: ابتِدَانِيَّة،ٌ لا تحل لها مِنَ الإعراب.
[IRAB_WORD_7]: جملة (لا فيها الهموم)
[IRAB_TEXT_7]: مَعْطُوفَة،ٌ لَا مَحَلَّ لها مِنَ الإعراب.

=== BLOCK 9: Poem 2 ===
(Component: TEMPLATE_C_POEM.html)
[HEMISTICH_1]: فَإِذا هَبَّ نَسِيمٌ
[HEMISTICH_2]: لَمْ تَجِيءٌ مَعَهُ السَّمُوم

=== BLOCK 10: Poem 2 Analysis ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الشرح والفكرة
Content: <p><span class="font-bold">الشرح:</span> طَبِيْعَةُ الغَابَاتِ عالم الصَّفَاءِ المِثَالِي،ِّ فَنَسَائِمُ أَثِيرِهِ وَنَفَحَاتُهُ نَقِيَّةٌ مِنَ السُّمُومِ</p><p><span class="font-bold">الفكرة:</span> الغاب عالمُ الْمَسَرَّاتِ وَالفَرَحِ وَالْأَمَلِ (الدَّعْوَةُ لِلغَيْشِ في عالم الغَابِ هَرَبًا مِنْ عَالَمَ المَدِينَةِ المادي) (خُلُو الغَابِ مِنَ الهم والحزن)</p><p><span class="font-bold">الأساليب:</span> (إذا هَبَّ نَسِيمٌ لَمَّ تَجِيءُ مَعَهُ السموم): أسلوب شرط الأداة: إذا فعل الشرط : هَب جواب الشرط : لم تجىء</p>

=== BLOCK 11: Poem 2 Irab ===
(Component: TEMPLATE_C_IRAB.html)
[IRAB_WORD_1]: فَإِذا
[IRAB_TEXT_1]: الفاء، حرف استثْنَافِ إِذَا، اسْم شَرْط غَيْرُ جازم، مَبْنِي على السُّكُون فِي مَحَلِ نَصْب،ِ مَفْعُولٌ فِيهِ ظَرْفُ زَمَانٍ
[IRAB_WORD_2]: نَسِيمٌ
[IRAB_TEXT_2]: فَاعِلَ مَرْفُوعٌ
[IRAB_WORD_3]: لَمَّ تَجِيء
[IRAB_TEXT_3]: لَم،َ حَرْفٌ جَازِمْ تَجِيءُ فِعْلَ مُصَارِع مَجْزُوم وعلامَةُ جَزْمِهِ السُّكُون
[IRAB_WORD_4]: مَعَهُ
[IRAB_TEXT_4]: مَعَ ظَرْفُ مُصَاحَبَةِ مَنْصُوب،َ وعلامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَة،ُ والهاء: ضميرٌ مُتَّصِلِّ مَبْنِي على الضم فِي مَحَلِّ جَر،ٍ مُصَافُ إليه.
[IRAB_WORD_5]: السُّمُومُ
[IRAB_TEXT_5]: فَاعِلَ مَرْفُو، وعلامَةُ رَفْعِهِ الصَّمَّةُ الظَّاهِرَة،ُ وَسُكِّنَ لِلضَّرَوَرَةِ الشَّعْرِيَّة.ِ
[IRAB_WORD_6]: جملة (إِذا هَبَّ نَسِيمٌ ثُمَّ تَجِيءٌ مَعَهُ السُّمُوم)
[IRAB_TEXT_6]: استئنافية، لا تحل لها من الإعراب.
[IRAB_WORD_7]: جملة (هَبَّ نَسِيْمٌ)
[IRAB_TEXT_7]: مُضَافُ إِلَيْه،ِ محلها الجر.
[IRAB_WORD_8]: جملة (لَمْ تَجِيءٌ مَعَهُ السُّمُومُ)
[IRAB_TEXT_8]: جَوَابُ شَرْطِ غَيْرُ جازم، لا تحل لها من الإعراب.

=== BLOCK 12: Poem 3 ===
(Component: TEMPLATE_C_POEM.html)
[HEMISTICH_1]: لَيْسَ حَزْنُ النَّفْسِ إِلَّا
[HEMISTICH_2]: ظلَ وَهُم لَا يَدُومْ

=== BLOCK 13: Poem 3 Analysis ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الشرح والفكرة
Content: <p><span class="font-bold">الشرح :</span> إِذا مَرَّتْ سَحَابَةُ حُزْنِ فِي أَنْفُسِ سُكَانِ الغَابِ فَهِيَ عَابِرَةٌ غَيْرُ مُسْتَقِرَّةِ؛ لأَنَّما حُرْنٌ وَهُمِي لَا يَلْبَثُ أَنْ يَزُوْلَ وَيَتَلَاشَى.</p><p><span class="font-bold">الفكرة:</span> الغاب عالم المَسَرَّاتِ وَالفَرَحِ وَالأَمَلِ (الدَّعْوَةُ للغَيْشِ في عالم الغابِ هَرَبًا مِنْ عالم المَدِينَةِ المادي) (خُلُو الْغَابِ مِنَ الهَمَ وَاحْرُنِ)</p>

=== BLOCK 14: Exam (التطبيقات اللغوية) ===
(Component: TEMPLATE_C_EXAM.html)
[NUMBER_1]: ١
[QUESTION_1]: التطبيقات اللغوية: ادرُسُ مَبْحَثَ النَّفي مُسْتَفِيْدًا مِنَ الحالتين الواردتين في البيتين الآتيين: (فإذا هب نسيم لم تجى معه السموم / ليس حزْنُ النَّفُسِ إِلَّا ظل وَهُم لَا يَدُوم)
[NUMBER_2]: ٢
[QUESTION_2]: هاتِ الوَزْنَ الصَّرَفِي لِلكَلِمَاتِ الآتية: (تَجِي، يَفْنَى السواقي).

--- END STREAM ---
