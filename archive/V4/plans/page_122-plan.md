# **SESSION 122**

[TASK DEFINITION]
Objective: Implement page 122.
File: `pages/page_122.html`
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
11. You MUST preserve the EXACT Tashkeel (Harakat) from the input. Stripping diacritics is a critical failure. Do not generate bare Arabic letters without their vowels.
12. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal
14. **Page Wrappers**: The compiler will automatically wrap the final page in `TEMPLATE_C_PAGE_WRAPPER.html`. Do NOT include this template in your `[CONTENT STREAM]` blocks.
15. **Exam Section**: ONLY include the `TEMPLATE_C_EXAM.html` block if the provided raw text slice actually contains test/exam questions (e.g., keywords like "تطبيق", "امتحان"). Do NOT hallucinate an exam if it is not in the source text. **CRITICAL:** If an exam or exercise contains the answers in the raw text, you MUST use `TEMPLATE_C_EXAM_SOLVED.html` instead of `TEMPLATE_C_EXAM.html`.

[CONTENT STREAM]

--- START STREAM ---
=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 122
[CHAPTER_TITLE]: page 122
[CATEGORY_HEADER]: 122
[SECTION_HEADER]: 122
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+
=== BLOCK 2: Warning Header ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[UNIQUE_ID]: b65461
[CONTENT]: مَبْنِي الشَّعْرِيَّةِ

=== BLOCK 3: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65462
[WORD_1]: تلا
[DETAILS_1]: فعل ماض، <span class="highlight-red">مَبْنِي</span> على الفَتْحَةِ المُقَدَّرة على الأَلِف،ِ مَنَعَ ظُهُورَهَا التَّعَذِّر.ُ
[UNIQUE_ID_2]: b65463
[WORD_2]: هَلْ
[DETAILS_2]: حَرْفُ استفهام. ثُمَّ حَرْفُ عَطْف.

=== BLOCK 4: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65464
[WORD_1]: مَاءً
[DETAILS_1]: مُبْتَداً مُؤَخَرٌ <span class="highlight-red">مَرْفُوع</span>، وعلامةُ رَفْعِهِ الصَّمَّةُ الظَّاهِرَة.ُ وسُكِنَ لِلضَّرُورَةِ الشَّعْرِيَّةِ في
[UNIQUE_ID_2]: b65465
[WORD_2]: الشَّيخ
[DETAILS_2]: فاعِلَ <span class="highlight-red">مَرْفُوع</span>ُ وعلامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَة،ُ

=== BLOCK 5: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65466
[WORD_1]: آية
[DETAILS_1]: مَفْعُولُ بِهِ <span class="highlight-red">مَنْصُوب</span>، وعلامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَة،ُ وَسُكِّنَ لِلضَّرُورَةِ الشَّعْرِيَّةِ
[UNIQUE_ID_2]: b65467
[WORD_2]: مَنْزِل
[DETAILS_2]: اسم مجرور، وعلامَةُ جَرَهِ الكَسْرَةُ الظَّاهِرَة.ُ والجار والمَجْرُورُ مُتَعَلِّقان بحالِ مَحْدُوفَةٍ لـ )كم( ]التَّقْدِير : عَدَدٌ كَثِير مِنَ المنازِلِ كَائِنٌ[

=== BLOCK 6: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65468
[WORD_1]: مُنْتَعِشا
[DETAILS_1]: حال منصوبة.
[UNIQUE_ID_2]: b65469
[WORD_2]: وكَمْ
[DETAILS_2]: الواو: زائدَةً كَمْ خَبَرَيَّةٌ مَبْنِيَّةٌ على السُّكُونِ فِي مَحَلِ رَفْع،ِ مُبْتَدا.ً مِنْ حَرْفُ جَةٍ مَنْزِل،ِ

=== BLOCK 7: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65470
[WORD_1]: الفَتَى
[DETAILS_1]: فاعِلْ <span class="highlight-red">مَرْفُوع</span>، وعلامَةً رَفْعِهِ الضَّمَّةُ المُقَدَّرَةُ على الأَلِفِ مَنَعَ ظُهُورَهَا التَّعَذِّر.ُ
[UNIQUE_ID_2]: b65471
[WORD_2]: يَأْلَهُ
[DETAILS_2]: فِعْلَ مُضَارِعٌ <span class="highlight-red">مَرْفُوع</span>، وعلامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَة،ُ وَالهاء، ضمير متصل مَبْنِي على السكون فِي مَحَلَّ نَصْب،ِ مَفْعُولُ بِهِ الأَرْضِ[ .

=== BLOCK 8: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65472
[WORD_1]: الْمَنَازِلَ
[DETAILS_1]: اسم )لَكِنَّ( منصوب وعلامَةُ نَصْبِهِ الفَتْحَةُ المُقَدَّرَةُ على ما قَبْلَ ياءِ الْمُتَكَلِم،ِ مَنَعَ ظُهُورَهَا اسْتِقَالُ الْمَحَلِّ بالحركة المناسبة. والياء، ضمير متصل مَبْنِي على السكون في محل جر، مُضَاف إليه.
[UNIQUE_ID_2]: b65473
[WORD_2]: ولَكِنَّ
[DETAILS_2]: الواو : زائدةً لَكِنَّ حَرْفٌ مُشَبَّهُ بِالفِعِلِ

=== BLOCK 9: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65474
[WORD_1]: يا أبي
[DETAILS_1]: يا، أَدَاةُ نِدَاء.ِ أبي، مُنَادى مُضَافُ <span class="highlight-red">مَنْصُوب</span>،
[UNIQUE_ID_2]: b65475
[WORD_2]: اطلال
[DETAILS_2]: خَبَرَ <span class="highlight-red">مَرْفُوع</span>ٌ وعلامَةُ رَفْعِهِ الصَّمَّةُ الظَّاهِرَة.ُ

=== BLOCK 10: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65476
[WORD_1]: فَأَجَابَ
[DETAILS_1]: الفَاء،ُ حَرْفُ اسْتِثْنَافِ أَجاب، فعل ماض، مَبْنِي على الفَنْحَةِ الظَّاهِرَة.ِ
[UNIQUE_ID_2]: b65477
[WORD_2]: تبنيها
[DETAILS_2]: فِعْلَ مُصَارِعٌ <span class="highlight-red">مَرْفُوع</span>، وعلامَةُ رَفْعِهِ الضَّمَّةُ المُقَدَّرَةُ على الياء، مَنَعَ ظُهُورها التقل. وها، ضمير مُتَّصِلِّ مَبْنِي على السكون في مَحَلَ نَصْب،ِ مَفْعُولُ بِهِ

=== BLOCK 11: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65478
[WORD_1]: يَدَان
[DETAILS_1]: فاعل <span class="highlight-red">مَرْفُوع</span>، وعلامَةُ رَفْعِهِ الأَلِفُ؛ لأَنَّهُ مُتَتَّى، والنُّون عوض عَنِ التنوين في الاسم المفرد.
[UNIQUE_ID_2]: b65479
[WORD_2]: حديثة
[DETAILS_2]: مَفْعُولُ به منصوب، وعلامةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَةُ

=== BLOCK 12: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65480
[WORD_1]: ولم يتم
[DETAILS_1]: الواو، حَرْفُ استناف. لم، حَرْفٌ جازم. يُتِم،َّ فعل مُضَارِعٌ تجزوم، وعلامَةُ جَزْمِهِ السُّكُونُ الْمُقَدَّرُ بِسَبَبِ التَّضْعيف. والهاء، ضميرٌ مُتَصِلِّ مَبْنِي على الضَّمَّة في محل جر، مُضَاف إليه.
[UNIQUE_ID_2]: b65481
[WORD_2]: إِذ:ْ
[DETAILS_2]: اسمٌ مَبْنِي على السُّكُون في مَحَلَ نَصْب،ِ مَفْعُولُ فِيهِ ظَرْفُ زَمَانِ بمعنى حِينَ(.

=== BLOCK 13: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65482
[WORD_1]: صَوْت:ُ
[DETAILS_1]: فَاعِلَ <span class="highlight-red">مَرْفُوع</span>ٌ
[UNIQUE_ID_2]: b65483
[WORD_2]: تَعَالوا
[DETAILS_2]: فِعْلُ أَمْرٍ مَبْنِي على حَذْفِ النُّونِ لَأَنَّ مُصَارِعَهُ مِنَ الْأَفْعَالِ الخمسة. والواو، ضمير مُتَصِلِّ مَبْنِي على السُّكُون فِي مَحَلِ رَفْع،ِ فَاعِلٌ والآلِفُ حَرْفُ تفريق.

=== BLOCK 14: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65484
[WORD_1]: وتَلَتْهُ
[DETAILS_1]: الواو، حَرْفُ عَطْفٍ تَلَتْه،ُ فِعْلَ مَاض،ِ مَبْنِي على الفَتْحَةِ المُقَدَّرة على الألف الْمَحْذُوفَةِ؛ لِاتِصَالِهِ بِتَاءِ التَّأْنيثِ السَّاكِنَة.ِ والنَّاء،ُ حَرْفُ تَأْني لا مَحَنَّ لَهُ مِنَ الإعراب.
[UNIQUE_ID_2]: b65485
[WORD_2]: طَقَطَقَةً
[DETAILS_2]: فَاعِلَ <span class="highlight-red">مَرْفُوع</span>ُ

=== BLOCK 15: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65486
[WORD_1]: الْبَنَادِق
[DETAILS_1]: مُضَافُ إِلَيهِ يَجْرُورٌ
[UNIQUE_ID_2]: b65487
[WORD_2]: لَنْ يَمُر
[DETAILS_2]: لَنْ حَرْفٌ نَاصِب.ُ يمر، فِعْلَ مُضَارِعٌ <span class="highlight-red">مَنْصُوب</span>ُ

=== BLOCK 16: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65488
[WORD_1]: العَاندون
[DETAILS_1]: فاعل <span class="highlight-red">مَرْفُوع</span>، وعلامَةُ رَفْعِهِ الواو؛ لِأَنَّهُ جَمع مذكر سالم والتون عوض عَنِ التنوين في الاسم المفرد.
[UNIQUE_ID_2]: b65489
[WORD_2]: حَرَسُ
[DETAILS_2]: مُبْتَداً مَرْفُو وعلامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَة.ُ

=== BLOCK 17: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65490
[WORD_1]: الحُدُودِ
[DETAILS_1]: مُضَافَ إِلَيهِ مَجْرُورٌ
[UNIQUE_ID_2]: b65491
[WORD_2]: مُرَابِ
[DETAILS_2]: خَبَرٌ <span class="highlight-red">مَرْفُوع</span>.ٌ

=== BLOCK 18: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65492
[WORD_1]: يحمي
[DETAILS_1]: فِعْلَ مُضارع <span class="highlight-red">مَرْفُوع</span>، وعلامَةُ رَفْعِهِ الضَّمَةُ المُقَدرة على الياء، مَنَعَ ظُهُورَهَا التَّقَلُ
[UNIQUE_ID_2]: b65493
[WORD_2]: الحُدُودَ
[DETAILS_2]: مَفْعُولُ بِهِ <span class="highlight-red">مَنْصُوب</span>ٌ

=== BLOCK 19: Sentences Block ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b65494
[BLOCK_TITLE]: إعراب الجمل
[CONTENT]:
=== BLOCK 20: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65495
[WORD_1]: جُمْلَهُ مَشْيَّا على الأَقْدَام أو رَحْفًا على الأَيْدِي نَعُود(
[DETAILS_1]: مَفْعُولُ بِه،ِ مَحَلُّهَا النَّصْبُ مَقُولُ القَوْلِ(. جملة كَانَ الصَّحْرُ )قالُوا(: ابتدائية، لا محل لها مِنَ الإعراب.
[UNIQUE_ID_2]: b65496
[WORD_2]: جُمْلَةً )مْ يَعْرِفُوا
[DETAILS_2]: استئنافية، لا محل لها

=== BLOCK 21: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65497
[WORD_1]: جملة )تقود(
[DETAILS_1]: صِفَة،ٌ مَحَلُّهَا النَّصْبُ
[UNIQUE_ID_2]: b65498
[WORD_2]: جُمْلَةً يَضْمُرُ(
[DETAILS_2]: حاليَّة،ٌ مَحَلُّهَا النَّصْبُ

=== BLOCK 22: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65499
[WORD_1]: يُمْلَهُ يَضْمُرُ(
[DETAILS_1]: خَبَريَّة،ٌ مَحَلُّهَا الرَّفْع.ُ
[UNIQUE_ID_2]: b65500
[WORD_2]: جملة كَانَ النَّهْرُ
[DETAILS_2]: استئنافية، لا محل لها مِنَ الإعراب

=== BLOCK 23: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65501
[WORD_1]: جملة )غاصَتْ(
[DETAILS_1]: مِنَ الإعراب جملة )كُلُّ القَوافِلِ قَبْلَهُم غَاصَتْ( لا محل لها مِنَ الإعراب.
[UNIQUE_ID_2]: b65502
[WORD_2]: جُلْلَةً كَانَ مَحَلُّهَا النَّصْبُ
[DETAILS_2]: جُمْلَةً )كانُوا ثلاثة عائدين(: استئنافية،

=== BLOCK 24: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65503
[WORD_1]: يَبْصُق(
[DETAILS_1]: حاليَّة،ٌ مَحَلُّهَا النَّصْبُ
[UNIQUE_ID_2]: b65504
[WORD_2]: جُمْلَهُ يَبْصُقُ(
[DETAILS_2]: خَرَيَّة،ٌ لا لها مِنَ الإعراب

=== BLOCK 25: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65505
[WORD_1]: جملة يصلونَ(
[DETAILS_1]: استثْنَافِيَّة،ٌ لجملة )كانَ اللَّيْلُ قَبَّعَةٌ( : مَعْطُوفَة،ٌ لَا مَحَلَّ
[UNIQUE_ID_2]: b65506
[WORD_2]: الجِسْرُ نَعْسَانًا(
[DETAILS_2]: استئنافية، لا محل لها مِنَ الإعراب

=== BLOCK 26: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65507
[WORD_1]: تَحَسَّسَ(
[DETAILS_1]: النَّصْبُ جُمْلَةً تَحَسَّسَ( : استِثْنَافِيَّة،ٌ لا تحل لها مِنَ الإعراب جُمْلَةٌ محل لها مِنَ الإعراب
[UNIQUE_ID_2]: b65508
[WORD_2]: جملة هل في البيت ماء
[DETAILS_2]: مَفْعُولُ بِه،ِ مَحَلَّهَا النَّصْبُ مَقُولُ القَوْلِ(.

=== BLOCK 27: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65509
[WORD_1]: جُمْلَةُ قَالَ الشَّيْخ
[DETAILS_1]: استئنافية، لا محل لَهَا مِنَ الإعراب استئنافية، لا محل لها مِنَ الإعراب . جُمْلَةً
[UNIQUE_ID_2]: b65510
[WORD_2]: جملة )تلا(
[DETAILS_2]: مَعْطُوفَة،ٌ لَا مَحَكَ لها مِنَ الإعراب

=== BLOCK 28: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65511
[WORD_1]: يألَفُهُ الفتى(
[DETAILS_1]: مَفْعُولُ بِه،ِ مَحَلُّهَا النَّصْبُ مَقُولُ لها مِنَ الإعراب
[UNIQUE_ID_2]: b65512
[WORD_2]: جملة )وَكَمْ مِنْ مَنْزِلِ فِي الْأَرْضِ وكَمْ مِنْ مَنْزِلٍ فِي الأَرْضِ
[DETAILS_2]: ابتدائية، لا محل لها مِنَ الإعراب

=== BLOCK 29: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65513
[WORD_1]: يَا أَبِي أَطَلَالٌ
[DETAILS_1]: مَفْعُول بِه،ِ حَلَّهَا النَّصْبُ مَقُولُ القول(.
[UNIQUE_ID_2]: b65514
[WORD_2]: جملة ولكن المنازِلَ
[DETAILS_2]: استنافية، لا محل لها مِنَ الإعراب

=== BLOCK 30: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65515
[WORD_1]: جُمْلَةً يَأْلُفُهُ الفَتَى(
[DETAILS_1]: صِفَة،ٌ مَحَلَّها الجر. قَالَتْ( : لا محل لها مِنَ الإعراب
[UNIQUE_ID_2]: b65516
[WORD_2]: جملة تبنيها يَدَانِ(
[DETAILS_2]: مَفْعُولُ بِه،ِ مَحَلُّهَا النَّصْبُ مَقُولُ القَوْلِ(.

=== BLOCK 31: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65517
[WORD_1]: جُجْلَةُ أَجَابَ(
[DETAILS_1]: استئنافية، لا محل لها مِنَ الإعراب
[UNIQUE_ID_2]: b65518
[WORD_2]: صَوْت(
[DETAILS_2]: إضافِيَّة،ٌ مَحَلَّها الجر.

=== BLOCK 32: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65519
[WORD_1]: جملَةً تَعَالوا
[DETAILS_1]: مَفْعُولُ بِه،ِ مَحَلَّهَا النَّصْبُ مَقُولُ القول(.
[UNIQUE_ID_2]: b65520
[WORD_2]: جملة لم يتم(
[DETAILS_2]: استئنافية، لا محل لها مِنَ الإعراب

=== BLOCK 33: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65521
[WORD_1]: جُمْلَةُ صَاحَ
[DETAILS_1]: مَقُولُ القَوْلِ(.
[UNIQUE_ID_2]: b65522
[WORD_2]: جُلَةً )لَتْهُ طَقْطَقَةُ البَنَادِقِ(
[DETAILS_2]: مَعْطُوفَة،ٌ مَحَلُّها الجر.

=== BLOCK 34: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65523
[WORD_1]: لَمْلَةً لَنْ يَمر العاندونَ(
[DETAILS_1]: استئنافية، لا محل لها مِنَ الإِعراب
[UNIQUE_ID_2]: b65524
[WORD_2]: جُمْلَةٌ حَرَسُ الحدُودِ مُرَابِ
[DETAILS_2]: استئنافية، لا محل لها مِنَ الإعراب

=== BLOCK 35: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65525
[WORD_1]: جُمْلَةُ يَحْمِي(
[DETAILS_1]: خَبَرَيَّة،ٌ مَحَلَّهَا الرَّفْع.ُ
[UNIQUE_ID_2]: b65526
[WORD_2]: &nbsp;
[DETAILS_2]: &nbsp;

=== BLOCK 36: Part 2 Header ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b65527
[BLOCK_TITLE]: إعراب المقطع الثاني
[CONTENT]:
=== BLOCK 37: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65528
[WORD_1]: أَمْرُ
[DETAILS_1]: خَيْرٌ لِمُبْتَنَا مَحْذُوفٌ <span class="highlight-red">مَرْفُوع</span>َ
[UNIQUE_ID_2]: b65529
[WORD_2]: الرَّصَاصِ
[DETAILS_2]: مُضاف إليهِ مَجْرُور على حرف جر.

=== BLOCK 38: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65530
[WORD_1]: الذي
[DETAILS_1]: اسمٌ مَوْصُولُ مَبْنِي على السُّكُون، فِي مَحَلِّ جَرٍ بِحَرْفِ الجر.
[UNIQUE_ID_2]: b65531
[WORD_2]: هَذَا
[DETAILS_2]: الهَاء،ُ حرف تنبيه. ذا، اسم إشارةٍ مَبْنِي على السُّكُونِ فِي مَحَلَ نَصْب،ِ مَفْعُولُ بِهِ

=== BLOCK 39: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65532
[WORD_1]: الْجِسْرَ
[DETAILS_1]: بَدَلَّ مِنِ اسم الإِشَارَةِ <span class="highlight-red">مَنْصُوب</span>ُ
[UNIQUE_ID_2]: b65533
[WORD_2]: هَذَا
[DETAILS_2]: الهَاء،ُ حَرْفُ تنبيه ذا، اسم إشارة مَبْنِي على السكون فِي مَحَلِ رَفْع، مبتداً

=== BLOCK 40: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65534
[WORD_1]: الجسر
[DETAILS_1]: بَدَلَّ مِنِ اسم الإشارةِ <span class="highlight-red">مَرْفُوع</span>ُ
[UNIQUE_ID_2]: b65535
[WORD_2]: مِقْصَلَهُ
[DETAILS_2]: خَبَرَ <span class="highlight-red">مَرْفُوع</span>ٌ

=== BLOCK 41: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65536
[WORD_1]: الذي
[DETAILS_1]: اسم مَبْنِي على الفَتْحَةِ الظَّاهِرَةِ
[UNIQUE_ID_2]: b65537
[WORD_2]: الطلقة
[DETAILS_2]: مُبْتَداً <span class="highlight-red">مَرْفُوع</span>

=== BLOCK 42: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65538
[WORD_1]: الأولى
[DETAILS_1]: مَوْصُولُ مَبْنِي على السكون، في حل جة،ٍ مُضَاف إليه.
[UNIQUE_ID_2]: b65539
[WORD_2]: ما زال
[DETAILS_2]: فعل ماض ناقص : إليهِ يَجْرُورٌ

=== BLOCK 43: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65540
[WORD_1]: فَبَّعَةَ
[DETAILS_1]: مَفْعُولُ بِهِ <span class="highlight-red">مَنْصُوب</span>ُ
[UNIQUE_ID_2]: b65541
[WORD_2]: الظَّلَامُ
[DETAILS_2]: الأَلِفِ مَنَعَ ظُهُورَهَا التَّعَذُرُ

=== BLOCK 44: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65542
[WORD_1]: اللَّيل
[DETAILS_1]: مُضَاف صفَةٌ <span class="highlight-red">مَرْفُوع</span>َة،ٌ وعلامَةُ رَفْعِهَا الضَّمَّةُ المُقَدرة على الْأُخْرَى صِفَةٌ حَرْفُ عَطْفٍ
[UNIQUE_ID_2]: b65543
[WORD_2]: الطَّلقَة،ُ
[DETAILS_2]: مُبْتَداً <span class="highlight-red">مَرْفُوع</span>ُ وسُكْنَ لِلضَّرورة الشَّعْرِيَّة.ِ

=== BLOCK 45: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65544
[WORD_1]: والطلقة
[DETAILS_1]: الواو، مُضَاف إليهِ مَجْرُور، وعلامَةُ جَرَهِ الكَسْرَةُ الظَّاهِرَة.ُ الظَّاهِرَةُ
[UNIQUE_ID_2]: b65545
[WORD_2]: قَديم
[DETAILS_2]: صفة تجزورة، وعلامة جَرِّهَا الكَسْرَةُ مُصَافَ إِلَيهِ يَجْرُور،ٌ وعلامَةُ جَبِّهِ الكَسْرَةُ الظَّاهِرَةُ <span class="highlight-red">مَرْفُوع</span>َةٌ

=== BLOCK 46: Irab Row ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b65546
[WORD_1]: قَلْبَ
[DETAILS_1]: مَفْعُولُ بِهِ <span class="highlight-red">مَنْصُوب</span>ُ
[UNIQUE_ID_2]: b65547
[WORD_2]: جُنْدِي
[DETAILS_2]: مُصَافَ إِلَيهِ يَجْرُور،ٌ وعلامَةُ جَبِّهِ الكَسْرَةُ الظَّاهِرَةُ

=== BLOCK 47: Summary Matrix ===
(Component: TEMPLATE_C_TABLE.html)
[UNIQUE_ID]: b65548
[CONTENT]: AAL مكتة

--- END STREAM ---
