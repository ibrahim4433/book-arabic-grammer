# **SESSION 186**

[TASK DEFINITION]
Objective: Implement page 186.
File: `pages/page_186.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green`  for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide: NO INLINE STYLES. Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). Use "Jules-workspace/id_manager.py" to generate or verify them.
8. Self-Correction: Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...) .
11. You must preserve the exact Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense. Do NOT leave empty space.
13. balanced page colors between teal and orange: make sure every page have minimum 1 element in orange.
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`).
15. Exam section always be in the end of the lesson (without the answers!).

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 186
[CHAPTER_TITLE]: page 186
[CATEGORY_HEADER]: 186
[SECTION_HEADER]: 186
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Poet Biography ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: أ. زكي قنصل (١٩١٩ م)
[CONTENT]: شاعِرٌ سُورِي، ولد في يبرود، وتلقى تعليمه الابتدائي فيها. فتعلم مبادئ العربية والفرنسية. هاجر إلى الأرجنتين وعمل فيها بائعا مُتَجَوْلًا، ثُمَّ اقْتَتَحَ متجرًا صغيرا. وقد كانَ شَغُوفًا بِالْقِرَاءَة والتحصيل المعرفي، فَدَرَسَ الْعَرَبِيَّةَ والإسبانِيَّةَ بِنَفْسِهِ حَتَّى تَمَكَنَّ مِنْهُما. وأَخَذَ يَنْظِمُ الشَّعْر،َ وَتَفَتَّحَتْ مواهِبُهُ مع الأيام ليصبح مِنَ الشَّعراء المجيدين. وقد تَوَلَّتْ وزارة الثقافة في الجمهورية العربية السوريةِ طَبْعَ ديوانِهِ المُوَلَّفِ مِنْ جُزاين، ومِنَ الجزء الثاني أُخِذَ هذا النَّصُن.ُ

=== BLOCK 3: Introduction Matrix ===
(Component: TEMPLATE_C_TABLE.html)
[TABLE_TITLE]: مدخل إلى النص :
[ROW_1_COL_1]: اصطدمت حياة المُغْتَرَبِينَ فِي المَهْجَرِ بواقع قاس،
[ROW_1_COL_2]: وتُخَطَّمَتْ أحلامهم على صخوره،
[ROW_2_COL_1]: وأدركوا بعد فوات الآوانِ أَنَّ السعادة التي طالما حلموا بها ما هي إلا سراب،
[ROW_2_COL_2]: وأَنَّ اللُّقْمَةَ دُونَهَا الكَدُّ والتعب والأعمال التي تستَنْزِفُ العافية،
[ROW_3_COL_1]: فسماء الغربةِ
[ROW_3_COL_2]: لَا تُمْطِرُ ذَهَبًا.

=== BLOCK 4: Warning Box ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[TITLE]: والبناء شاهد على الشقاء والعناء
[CONTENT]: والمَشَفَّةِ فِي غُرْبَةٍ رَمَتْهُ فِي دروبها الموحشة، فأضحى ضائعا يعيش في عُزْلَةٍ مُؤْلِمَة،ٍ لا أَحَدَ يُصغي إلى أوجاعه، والنَّوائِبُ تُحْدِقُ بِهِ مِنْ كُلِّ جانب، فيعمل مِنْ دُونِ كَلَلٍ أو مَلَل،ٍ ولكن لا يستطيع بكل ما يبذل أَنْ يُضيء في حياته شعلة تطردُ عَنْهُ ظُلُمَةَ الأَيَّام.

=== BLOCK 5: The Poem ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البناء
[RIGHT_HEMISTICH_1]: ١- يَبْنِي القُصُورَ وَكُوخُهُ خَرِبُ
[LEFT_HEMISTICH_1]: سَاءَتْ حَياةٌ كُلِّهَا تَعَبُ
[RIGHT_HEMISTICH_2]: ٢- الشوك يزخر في مسالكها
[LEFT_HEMISTICH_2]: والريح ما تَنْفَكُ تَصْطَخِبُ
[RIGHT_HEMISTICH_3]: ٣- لا يَزْدَهِي فِي لَيْلِهِ قَبَسٌ
[LEFT_HEMISTICH_3]: إِلَّا تَوَلَّتْ طَمْسَهُ النُّوبُ
[RIGHT_HEMISTICH_4]: ٤- صَفُرَتْ مِنَ الأصحاب راحته
[LEFT_HEMISTICH_4]: لَمْ يُجْدِهِ سَعْيٌ ولا طلب
[RIGHT_HEMISTICH_5]: ٥- يَنْبُو بِهِ فِي اللَّيْلِ مَضْجَعُهُ
[LEFT_HEMISTICH_5]: ويَشُوكُهُ الحرمانُ وَالنَّصَبُ
[RIGHT_HEMISTICH_6]: ٦- يسعى ولَكِنْ لَا إِلَى أَمَلٍ
[LEFT_HEMISTICH_6]: ويَدِبُّ لَكِنْ حَيْتُ لَا أَرَبُ
[RIGHT_HEMISTICH_7]: ٧- دامي الفُوَادِ يَمُضُهُ أَلَمٌ
[LEFT_HEMISTICH_7]: ذاوي الجفونِ يَعَضُّهُ سَغَبُ
[RIGHT_HEMISTICH_8]: ٨- بالروح في کانون نَفْضَتُهُ
[LEFT_HEMISTICH_8]: يَصْطَكُ مِنْ قُرِّ وَيَضْطَرِبُ
[RIGHT_HEMISTICH_9]: ٩- جَمَدَتْ على المنقار راحته
[LEFT_HEMISTICH_9]: فكأنها من بَعْضِهِ خَشَبُ
[RIGHT_HEMISTICH_10]: ١٠- تَلْهُو الرياحُ بِهِ فَإِنْ سَكَنَتْ
[LEFT_HEMISTICH_10]: فَتَحَتْ عليهِ تُقُوبَهَا السُّحُبُ
[RIGHT_HEMISTICH_11]: ١١- يا غَائِصًا بالطِينِ لَا نَصَبٌ
[LEFT_HEMISTICH_11]: يوهي عزيمته ولا وَصَبٌ
[RIGHT_HEMISTICH_12]: ١٢- صَبْرًا على الأَيَّامِ إِنْ عَبَسَتْ
[LEFT_HEMISTICH_12]: هَيْهَاتَ يَفْرِجُ ضيقها غضب
[RIGHT_HEMISTICH_13]: ١٣- ما أنتَ أَوَّلَ كَادِحٍ عَثَرَتْ
[LEFT_HEMISTICH_13]: آمالُهُ وَكَبَا بِهِ الدَّأَبُ
[RIGHT_HEMISTICH_14]: ١٤- بَيْنِي وَبَيْنَكَ فِي البَلاء وإن
[LEFT_HEMISTICH_14]: كَذَبَت عليك ظَوَاهِرِي نَسَبُ

--- END STREAM ---
