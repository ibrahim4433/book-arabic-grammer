# **SESSION 199**

[TASK DEFINITION]
Objective: Implement page 199.
File: `pages/page_199.html`
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

=== BLOCK 1: Page Wrapper ===
(Component: TEMPLATE_C_PAGE_WRAPPER.html)

=== BLOCK 2: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 199
[CHAPTER_TITLE]: page 199
[CATEGORY_HEADER]: 199
[SECTION_HEADER]: 199
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 3: Topic Block ===
(Component: TEMPLATE_C_BLOCK.html)
Title: التعبير الكتابي - التعبير الأدبي
Content: مخطط موضوع الوحدة الثالثة - الغربة والاغتراب في الأدب المهجري<br>أولا - مقدمة مناسبة بمقدور الطالب أن يستوحي مُقدمةً مُناسِبَةً تَدُورُ حَوْلَ أَدب المُهْجَر.

=== BLOCK 4: List Item 1 ===
(Component: TEMPLATE_C_LIST.html)
[LIST_TITLE]: ثانيا - الشوق والحنين
[LIST_ITEM_CONTENT]: - تصوير شَوْقِ أُمهات المهاجرينَ وَحَنِينَهُنَّ إِلَى أَبْنَائِهِن:َّ

=== BLOCK 5: Poem 1 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b00001
[POEM_TITLE]:
[UNIQUE_ID_BIO]: b00002
[POET_NAME]: شفيق معلوف
[RIGHT_HEMISTICH]: دار العروبة دار الحب والغزل
[LEFT_HEMISTICH]: ترى هل آب مِنْ سَفَرِ شِرَاعٌ

=== BLOCK 6: Benefit Warning ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: - الحنينُ الدَّائِمُ لِلدِّيارِ :
Content: المعاناةُ بِسَبَبِ تَرْكِ الوَطَنِ وَالأَهْلِ قَسْرًا )الحَنِينُ الدَّائِمُ لِلدِّيارِ(:

=== BLOCK 7: Poem 2 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b00003
[POEM_TITLE]:
[UNIQUE_ID_BIO]: b00004
[POET_NAME]: إلياس فرحات:
[RIGHT_HEMISTICH]: شراعٌ مَدَّ فَوْقَ الْمُوْجِ عنقا
[LEFT_HEMISTICH]: تَذُوب إليهِ تَحْنانا وشوقا
[RIGHT_HEMISTICH_2]: يُقِلُ فَتَى تَبَدَّى الشَّطَ جَهْمَا
[LEFT_HEMISTICH_2]: ولم تشبعهُ تَقْبِيلًا وَنَشْقا
[RIGHT_HEMISTICH_3]: وعَادَرَ عِنْدَ صَخْرِ الشَّطِ أَمَّا
[LEFT_HEMISTICH_3]: لَهُ فَأَشَاحَ عَنْهُ الوَجْةَ طَلْقا

=== BLOCK 8: Poem 3 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b00005
[POEM_TITLE]:
[UNIQUE_ID_BIO]: b00006
[POET_NAME]: جورج صيدح
[RIGHT_HEMISTICH]: وطني، أين أنا لِمُّنْ أَود؟
[LEFT_HEMISTICH]: أو ما لِلحَ بَعْدَ الجَزْرِ مَدْ؟
[RIGHT_HEMISTICH_2]: غابَ خَلْفَ البَحْرِ عَنِّي شَاطِي
[LEFT_HEMISTICH_2]: هَا جَرْتُ مِنْكِ وقلبي فيك لم يزل
[RIGHT_HEMISTICH_3]: وراحَ يَرُودُ خَلْفَ الأَفْقِ أَفْقا
[LEFT_HEMISTICH_3]: كل ما أَرَّقَنِي فِيهِ رَقَدْ

=== BLOCK 9: List Item 2 ===
(Component: TEMPLATE_C_LIST.html)
[LIST_TITLE]: استعذاب ضَنْكِ العيش وضِيْقِهِ فِي الوَطَن، وتَفْضِيْلِه على العيش الرَّغِيدِ فِي الغُرْبَة:ِ
[LIST_ITEM_CONTENT]: ه- تصوير قُوَّة الانتماء إلى الوطن:

=== BLOCK 10: Poem 4 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b00007
[POEM_TITLE]:
[UNIQUE_ID_BIO]: b00008
[POET_NAME]: جورج صيدح
[RIGHT_HEMISTICH]: فيهِ مُر العيش يحلو وأرى
[LEFT_HEMISTICH]: في سواهُ زُبْدَةَ العَيْشِ زَبَدْ
[RIGHT_HEMISTICH_2]: وطني، ما زِلْتُ أَدْعُوكَ أَبِي
[LEFT_HEMISTICH_2]: وجراح اليُنمِ فِي قَلْبِ الوَلَدْ
[RIGHT_HEMISTICH_3]: هَلْ دَرَى الدَّهْرُ الذي فَرَّقَنا
[LEFT_HEMISTICH_3]: أَنَّهُ فَرَّقَ رُوحًا عَنْ جَسَ ؟

=== BLOCK 11: Info Block ===
(Component: TEMPLATE_C_BLOCK.html)
Title: - إبْرَازُ الانتماء إلى قيم الوَطَنِ الرُّوحِيَّةِ تَأْكِيدُ عُمْقِ الأَنْتِمَاء إلى
Content: الوَطَنِ(، )تَفْضِيلُ الوَطَنِ على الغُرْبَة(:

=== BLOCK 12: Matrix Overview ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]:
[HEADER_2]:
[HEADER_3]:
[CELL_1]: نسيب عريضة:
[CELL_2]: ما إِنْ أُبَالِي مُقَامِي في مغاربها
[CELL_3]: وفي مشارقها حتي وإيماني

=== BLOCK 13: Sub Info ===
(Component: TEMPLATE_C_BLOCK.html)
Title: التَّعْبِيرُ عَنِ الغُرْبَةِ القَسْرِيَّة:ِ
Content: بَيَانُ الدَّوَافِعِ الكَامِنَةِ وراء الاغتراب الإِشَارَةُ إلى سَبَبِ الْهِجْرَةِ مِنَ الْوَطَنِ(:

=== BLOCK 14: Poem 6 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b00011
[POEM_TITLE]:
[UNIQUE_ID_BIO]: b00012
[POET_NAME]: جورج صيدح
[RIGHT_HEMISTICH]: مارست حيثُ رَسَتْ فلك النوى
[LEFT_HEMISTICH]: لو أَبَاحُوا لِي فِي الدَّفَّةِ يَدْ
[RIGHT_HEMISTICH_2]: ما رَضِيتُ البَيْنَ لولا شِدَّةٌ
[LEFT_HEMISTICH_2]: وَجَدَتْنِي سَاعَةَ البَيْنِ أَشَدَّ

=== BLOCK 15: Info List ===
(Component: TEMPLATE_C_LIST.html)
[LIST_TITLE]:
[LIST_ITEM_CONTENT]: - انقطاع الرِّزْقِ في الوَطَنِ رِعْمَ وَفْرَةِ خَيْرَاتِهِ :

=== BLOCK 16: Poem 7 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b00013
[POEM_TITLE]:
[UNIQUE_ID_BIO]: b00014
[POET_NAME]: جورج صيدح
[RIGHT_HEMISTICH]: فيه ربعي فيهِ جَنَّاتُ جَرَتْ
[LEFT_HEMISTICH]: تَحْتَهَا الأَهَارُ والرَزْقُ جَمَدْ

=== BLOCK 17: Info List 2 ===
(Component: TEMPLATE_C_LIST.html)
[LIST_TITLE]:
[LIST_ITEM_CONTENT]: - هَجْرِ الوَطَنِ بِسَبْبٍ شَظَفِ العَيْشِ وَضِيْقِه:ِ

=== BLOCK 18: Poem 8 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b00015
[POEM_TITLE]:
[UNIQUE_ID_BIO]: b00016
[POET_NAME]: جورج صيدح
[RIGHT_HEMISTICH]: لولا شِدَّةٌ وَجَدَتْنِي سَاعَةَ البَيْنِ أَشَدْ
[LEFT_HEMISTICH]: ما رَضِيتُ البَيْنَ

=== BLOCK 19: Poem 9 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b00017
[POEM_TITLE]:
[UNIQUE_ID_BIO]: b00018
[POET_NAME]:
[RIGHT_HEMISTICH]: بَعُدْتُ عَنْهَا أَجُوبُ الْأَرْضَ تَقْذِفْنِي
[LEFT_HEMISTICH]: منى، حَتَقْتُ لَهَا رَكْبِي وأضعَانِي

=== BLOCK 20: Info List 3 ===
(Component: TEMPLATE_C_LIST.html)
[LIST_TITLE]:
[LIST_ITEM_CONTENT]: - السَّعْي لِتَحْقِيقِ الأماني والأحلام:

=== BLOCK 21: Info List 4 ===
(Component: TEMPLATE_C_LIST.html)
[LIST_TITLE]:
[LIST_ITEM_CONTENT]: نسيب عريضة:
[LIST_ITEM_CONTENT]: - اغترار المغترب بأحلام الغربة:

=== BLOCK 22: Cut Box Part 1 ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
[BLOCK_TITLE]: فوزي المعلوف
[CONTENT]: غَمَرَتْهُ الأَحلامُ بِالشَّفَقِ الوَرْدِي يُغْرِيهِ بِالمنى تَعْلِيلا<br>-  -

--- END STREAM ---
