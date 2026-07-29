# **SESSION 124**

[TASK DEFINITION]
Objective: Implement page 124.
File: `pages/page_124.html`
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
[LESSON_NUMBER]: 124
[CHAPTER_TITLE]: page 124
[CATEGORY_HEADER]: 124
[SECTION_HEADER]: 124
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: إعراب الجمل (تتمة) ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[UNIQUE_ID]: b54646
[BLOCK_TITLE]: إعراب الجمل
[CONTENT]: مُمَرَّقَةَ التياب( : مَعْطُوفَة،ٌ لا محل لها مِنَ الإعراب جملَةً كَانَتْ مُمَزَّفَةَ القياب( : خَبَرَيَّة،ٌ مَحَلُّهَا الرَّفْعُ جُمْلَةُ صَارَتْ يَتِيْمة(: صِلَهُ الْمَوْسُول،ِ لَا مَحَكَ لَهَا مِنَ الإعراب جملَةً طَارَ عِطْرُ الياسمين(: مَعْطُوفَة،ٌ مَحَلُّهَا الرَّفْع.ُ

=== BLOCK 3: عنوان الإعراب ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b02351
Title: إعراب المقطع الرابع:
Content: مفردات المقطع الرابع

=== BLOCK 4: إعراب مفردات ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b60843
[WORD_1]: والصَّمْتُ
[DETAILS_1]: الواو، حَرْفُ استنَافِ الصَّمْت،ُ مُبْتَداً مَرْفُوعٌ
[UNIQUE_ID_2]: b77069
[WORD_2]: مَرَّةٌ
[DETAILS_2]: نَائِبُ مَفْعُولِ مُطْلَقِ مَنْصُوبُ

=== BLOCK 5: إعراب مفردات ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b17384
[WORD_1]: أُخْرَى
[DETAILS_1]: صِفَةٌ مَنْصُوبَة،ٌ وعلامَةُ نَصْبِهَا الفَتْحَةُ الْمُقَدَّرَةُ على الأَلِف، مَنَعَ ظُهُورَهَا التَّعَذِّرُ
[UNIQUE_ID_2]: b38378
[WORD_2]: عَادَ
[DETAILS_2]: فِعل ماض ناقص، مَبْنِي على الفَتْحَةِ الظَّاهِرَةِ

=== BLOCK 6: إعراب مفردات ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b00329
[WORD_1]: النَّهُرُ
[DETAILS_1]: اسم )عادَ مَرْفُوع.
[UNIQUE_ID_2]: b15482
[WORD_2]: ولم يَعْرِف
[DETAILS_2]: الواو، حَرْفُ عَطْف.ِ ولم، حَرْفٌ جازم. يَعْرِف، فعل مُضَارِع مجزوم، وعلامَةُ جَزْمِهِ السُّكُونُ

=== BLOCK 7: إعراب مفردات ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b32078
[WORD_1]: أَحَد:
[DETAILS_1]: فاعِلَ مَرْفُوع، وعلامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَة.ُ وسُكِنَ لِلضَّرورة الشَّعْرِيَّةِ
[UNIQUE_ID_2]: b65959
[WORD_2]: شَيْئًا
[DETAILS_2]: مَفْعُولُ بِهِ مَنْصُوبُ

=== BLOCK 8: إعراب مفردات ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b49770
[WORD_1]: الذي
[DETAILS_1]: اسم مَوْصُلِّ مَبْنِي على السُّكُونِ فِي مَحَلِّ جَة،ٍ صُفَةٌ
[UNIQUE_ID_2]: b00169
[WORD_2]: حَمَ
[DETAILS_2]: مَفْعُولُ بِهِ مَنْصُوبُ

=== BLOCK 9: إعراب مفردات ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b23473
[WORD_1]: النَّارَحِينَ
[DETAILS_1]: مُضَافُ إِلَيْهِ مجرُوز، وعلامَةً جَرَهِ اليَاءُ لِأَنَّهُ جَمْعُ مُذَكْرٍ سالم والتون عوض عَنِ التنوين في الاسم المفرد.
[UNIQUE_ID_2]: b91372
[WORD_2]: والجِسْرُ
[DETAILS_2]: الواو، حَرْفُ اسْتِنْنَافِ الحِسْر،ُ مُبْتَداً مَرْفُو.

=== BLOCK 10: إعراب مفردات ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b19233
[WORD_1]: كُل:ِّ
[DETAILS_1]: نَائِبُ ظَرْفِ زَمَانٍ مَنْصُوبٌ
[UNIQUE_ID_2]: b86161
[WORD_2]: يوم:
[DETAILS_2]: مُضَاف إليهِ مَجْرُور.ٌ

=== BLOCK 11: إعراب مفردات ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b15597
[WORD_1]: الطريق
[DETAILS_1]: الكاف، حَرْفُ جر. الطريق، اسم تجرُور
[UNIQUE_ID_2]: b06207
[WORD_2]: وهِجْرَةُ
[DETAILS_2]: الواو، حَرْفُ عَطْفٍ . هِجْرَة،ُ مُبْتَداً مَرْفُوعَ

=== BLOCK 12: إعراب مفردات ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b10386
[WORD_1]: الدَّم:
[DETAILS_1]: مُضَافُ إليهِ يَجْرُور.ٌ
[UNIQUE_ID_2]: b01269
[WORD_2]: النَّهْرِ :
[DETAILS_2]: مُضَافُ إِلَيهِ مَجْرُورٌ

=== BLOCK 13: إعراب مفردات ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b73720
[WORD_1]: تَنْحَتْ
[DETAILS_1]: فِعْلَ مُضَارِعُ مَرْفُوعُ
[UNIQUE_ID_2]: b39546
[WORD_2]: مِنْ حَصَى
[DETAILS_2]: مِن،ْ حَرْفُ جَر.ٍ حَصَى اسم مجرور، وعلامَةُ جَرَهِ الكَسْرَةُ المُقَدَّرَةُ على الأَلِفِ مَنَعَ ظُهُورَها التَّعَذَّرُ

=== BLOCK 14: إعراب مفردات ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b55722
[WORD_1]: الوادي:
[DETAILS_1]: مُضَاف إليهِ تَجْرُور،ُ وعلامَةُ جَرِهِ الكَسْرَةُ الْمُقَدَّرِةُ على الياءِ مَنَعَ ظهورها التَّقَل.ُ
[UNIQUE_ID_2]: b66769
[WORD_2]: تماثيلًا
[DETAILS_2]: مَفْعُولٌ بِهِ مَنْسُوبٌ

=== BLOCK 15: إعراب مفردات ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b62300
[WORD_1]: لها
[DETAILS_1]: الام، حَرْفُ جر. وها، ضمير مُتَّصِلِّ مَنِي على السُّكُون في محل جر، بِحَرْفِ الجَر.ِ
[UNIQUE_ID_2]: b02889
[WORD_2]: لَوْنُ
[DETAILS_2]: مُبْتَداً مُؤَخَرُ مَرْفُوعٌ

=== BLOCK 16: إعراب مفردات ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b31201
[WORD_1]: النجوم:
[DETAILS_1]: مُضَاف إليهِ مَجْرُورٌ
[UNIQUE_ID_2]: b54032
[WORD_2]: وَلَسْعَةُ :
[DETAILS_2]: الواو، حَرْفُ عَطْفٍ لَسْعَة،ُ اسمٌ مَعْطُوفٌ مَرْفُوعُ

=== BLOCK 17: إعراب مفردات ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b13764
[WORD_1]: الذكرى:
[DETAILS_1]: مُضَاف إليهِ تَجْرُور،ٌ وعلامَةُ جَرَهِ الكَسْرَةُ المُقَدَّرَةُ على الياء، مَنَعَ ظُهُورَهَا التَّعَذَّر.ُ
[UNIQUE_ID_2]: b49531
[WORD_2]: وطَعْمُ
[DETAILS_2]: الواو، حَرْفُ عَطْفٍ طَعْم،ُ اسم مَعْطُوفٌ مَرْفُو

=== BLOCK 18: إعراب مفردات ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b48378
[WORD_1]: الحب :
[DETAILS_1]: مُضَافَ إِلَيْهِ يَجْرُور.ٌ
[UNIQUE_ID_2]: b81049
[WORD_2]: حينَ
[DETAILS_2]: مَفْعُولُ فِيهِ ظَرْفُ زَمَانٍ مَنْصُوب.ٌ

=== BLOCK 19: إعراب مفردات ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b68149
[WORD_1]: يصير :
[DETAILS_1]: فِعْلِّ مُصَارِعُ نَاقِصُ مَرْفُوعٌ
[UNIQUE_ID_2]: b43852
[WORD_2]: أَكْبَر:َ
[DETAILS_2]: خَبَرُ )يصِيرُ مَنْصُوبٌ

=== BLOCK 20: إعراب مفردات ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b78889
[WORD_1]: مِنْ عِبَادِهُ
[DETAILS_1]: مِنْ حَرْفُ جَرٍ عِبَادِه،ُ اسمٌ فَجُرُور،ٌ وعلامَةُ جَرَهِ الكَسْرَةُ الظَّاهِرَةُ وَسُكِنَ لِلضَّرُورَةِ الشَّعْرِيَّةِ
[UNIQUE_ID_2]: b93568
[WORD_2]:
[DETAILS_2]:

=== BLOCK 21: إعراب الجمل ===
(Component: TEMPLATE_C_TABLE.html)
[UNIQUE_ID]: b73274
[HEADER_1]: الجملة
[HEADER_2]: نوعها
[HEADER_3]: محلها من الإعراب

[CELL_1]: جُمْلَةُ الصَّمْتُ خَيْمَ(
[CELL_2]: استئنافية
[CELL_3]: لا محل لها مِنَ الإعراب
[CELL_4]: جملَهُ )خَيْمَ(
[CELL_5]: خَبَرَيَّة،ٌ
[CELL_6]: محَلُّهَا الرَّفْعُ
[CELL_7]: جُمَلَهُ يَبْصُقُ(
[CELL_8]: خَبَيَّة،ٌ
[CELL_9]: مَحَلَّهَا النَّصْب
[CELL_10]: جملَةً )لم يَعْرِفُوا(
[CELL_11]: استئنافية
[CELL_12]: لا محل لها من الإعراب
[CELL_13]: جُمْلَةً )لم يَعْرِفْ أَحَد(
[CELL_14]: مَعْطُوفَة،ٌ
[CELL_15]: لَا مَحَلَّ لها من الإعراب
[CELL_16]: جُمْلَةٌ يَمْتَص(
[CELL_17]: صِلَةُ المَوْصُول،ِ
[CELL_18]: لا مَحَلَّ لَهَا مِنَ الإعراب
[CELL_19]: جملة )الحِسْرُ يَكْبُرُ(
[CELL_20]: استئنافية
[CELL_21]: لا محل لها مِنَ الإعراب
[CELL_22]: ملَةً يَكْبُرُ(:
[CELL_23]: خَبَرَيَّة،ٌ
[CELL_24]: مَحَلُّهَا الرَّفْعُ
[CELL_25]: جُمْلَةً هِجْرَةُ الدَّمِ تَنْحَتْ :
[CELL_26]: مَعْطُوفَة،ً
[CELL_27]: لا محل لها مِنَ الإعراب
[CELL_28]: جُمْلَهُ تَنْحَتُ(:
[CELL_29]: خَبَيَّة،ٌ
[CELL_30]: مَحَلُّهَا الرَّفْعُ
[CELL_31]: جُمْلَةً )هَا لَوْنُ النُّجُوم(:
[CELL_32]: صفَة،ٌ
[CELL_33]: مَحَلُّهَا النَّصْبُ
[CELL_34]: جُمَلَةُ )يصِيرُ أَكْبَرَ( :
[CELL_35]: مُضَاف إليه
[CELL_36]: محلها الجر.

=== BLOCK 22: شعر محمود درويش ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b88898
[POEM_TITLE]: أَسْطُرُ النَّص المُتَ مَةُ الوَارِدَةُ فِي دِيوان الشاعر
[UNIQUE_ID_BIO]: b21388
[POET_NAME]: محمود درويش
[RIGHT_HEMISTICH_1]: .... أمر بإطلاق الرصاص على الذي يجتاز
[LEFT_HEMISTICH_1]: هَذَا الْحِسْرَ هَذَا الحِسْرُ مِقْصَلَةُ الذِي رَفَضَ
[RIGHT_HEMISTICH_2]: التَّسَلَ تَحْتَ ظِلَ وَكَالَةِ الغَوثِ الجديدة ..
[LEFT_HEMISTICH_2]: والمَوْتَ بِالمَجَانِ تَحْتَ الدُّلِّ وَالأَمْطَار،ِ مَنْ
[RIGHT_HEMISTICH_3]: يَرَفُضْهُ يُقْتَلْ عِنْدَ هذا الحِسْر،ِ هَذَا الْحِسْرُ
[LEFT_HEMISTICH_3]: مقْصَلَةُ الذي ما زالَ يَحْلُمُ بِالوَطَنْ
[RIGHT_HEMISTICH_4]: لا تَعْتُلُوها، واقْتُلُوني
[LEFT_HEMISTICH_4]: كَانَتْ مِيَاهُ النَّهْرِ أَغْزَر . . فالذينَ
[RIGHT_HEMISTICH_5]: رَفَضُوا هُنَاكَ المَوْتَ بِالمَجَانِ أَعطوا النَّهْرَ لَونًا آخَرًا.
[LEFT_HEMISTICH_5]: والحِسْر،ُ حِيْنَ يَصِيرُ تمثالا ، سَيُصْبَعُ - دُونَ
[RIGHT_HEMISTICH_6]: ريب - بالظهيرة والدِّمَاءِ وَحُضْرَةِ الْمَوْتِ
[LEFT_HEMISTICH_6]: المفاجي
[RIGHT_HEMISTICH_7]: وطَارَ عِطْرُ الياسمين
[LEFT_HEMISTICH_7]: عَنْ صَدْرها العاري الذي
[RIGHT_HEMISTICH_8]: مَلَأَتُهُ رَائِحَةُ الْحَرِيمَةِ
[LEFT_HEMISTICH_8]: - -
[RIGHT_HEMISTICH_9]: وطَعْمُ الحُبِّ حِينَ يَصِيرُ أَكثر من عِبَادَه.ُ
[LEFT_HEMISTICH_9]: في غد تزحف الجموع

--- END STREAM ---