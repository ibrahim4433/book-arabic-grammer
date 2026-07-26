# **SESSION 133**

[TASK DEFINITION]
Objective: Implement page 133.
File: `pages/page_133.html` (Note: Use the exact page number.)
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
[LESSON_NUMBER]: 133
[CHAPTER_TITLE]: page 133
[CATEGORY_HEADER]: 133
[SECTION_HEADER]: 133
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: الشواهد الشعرية ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
Mapped Component: TEMPLATE_C_POEM.html
Title: ه- الإشارة إلى غَفْلَةِ العالم عَنِ الجَرَائِمِ التِي تَرْتَكِبُهَا الصُّهْيُونِيَّةُ بِحَقِ العَائِدِين :
Poet: محمود درويش
Hemistich 1: لَمْ يَعْرِفُوا أَنَّ الطَّرِيقَ إِلَى الطَّرِيقِ
Hemistich 2: دَمْ وَمِصْيَدَة،ٌ وَلَمْ يَعْرِفُ أَحَدٌ

=== BLOCK 3: صُعُوبَاتِ العَوْدَةِ ===
(Component: TEMPLATE_C_POEM.html)
Title: إِبْرَازُ صُعُوبَاتِ العَوْدَةِ وَتَحَدِّياتها :
Poet: محمود درويش
Hemistich 1: لَمْ يَعْرِفُوا أَنَّ الطَّرِيقَ إِلَى الطَّرِيقِ
Hemistich 2: دَمْ وَمِصْيَدَةٌ وَبِيدُ

=== BLOCK 4: حُلم الفلسطينيين ===
(Component: TEMPLATE_C_POEM.html)
Title: - تَعَاظم حُلم الفلسطينيين بِالعَوْدَة:ِ
Hemistich 1: شَيْئًا عَنِ النَّهْرِ الذي
Hemistich 2: يمتص لَخَمَ النازحِين

=== BLOCK 5: تابع الشواهد ===
(Component: TEMPLATE_C_POEM.html)
Title:
Poet: محمود درويش
Hemistich 1: والحِسْرُ يَكْبُرُ كُلَّ يَوْمِ الطَّريق
Hemistich 2: وَهِجْرَةُ الدَّمِ فِي مِيَاهِ النَّهْرِ تَنْحَتُ
Hemistich 3: النُّجُوم،ِ وَلَسْعَةُ الذِّكْرَى، وطَعْمُ
Hemistich 4: الْحُبِّ حِينَ يَصِيرُ أَكْبَرَ مِنْ عِبَادَهُ
Hemistich 5: من حصى الوادِي تَمَاثِيلًا لَهَا لَوْنُ

=== BLOCK 6: الحنين إلى الديار ===
(Component: TEMPLATE_C_POEM.html)
Title: حَنِينُ الفلسطينيين إلى الديار، والحلم بالعَوْدَةِ إِلَيْهَا :
Poet: محمود درويش:
Hemistich 1: وَبَعْدَ دَقَائِقِ يَصِلُونَ هَلِ فِي
Hemistich 2: البَيْتِ ماء؟
Hemistich 3: وَتَحْسَّسَ الْمِفْتَاحَ ثُمَّ تَلَا مِنَ
Hemistich 4: القُرْآنِ آيَهُ

=== BLOCK 7: إيمَانِ العَائِدِينِ ===
(Component: TEMPLATE_C_POEM.html)
Title: الإشارة إلى إيمَانِ العَائِدِينِ وَتَدَيَّنُهُم :
Poet: محمود درويش
Hemistich 1: والشَّيْحُ يَأْخُذُ كَ إِبْنَتِهِ وَيَتْلُو
Hemistich 2: هَمْسًا مِنَ القُرْآنِ سُوْرَهُ
Hemistich 3: قَالَ الشَّيْحُ مُنْتَعِشَا : وَكَمْ
Hemistich 4: مِنْ مَنْزِلٍ فِي الْأَرْضِ
Hemistich 5: يَأْلَفُهُ الْفَتَى

=== BLOCK 8: تَسَرُّبُ اليَأْسِ ===
(Component: TEMPLATE_C_POEM.html)
Title: -۱۰ تَسَرُّبُ اليَأْسِ إِلى نُفُوس الحالِمِين بِالعَوْدَة:ِ
Poet: محمود درويش:
Hemistich 1: قَالَتْ وَلَكِنَّ الْمَنَازِلَ يَا أَبِي
Hemistich 2: أطلال

=== BLOCK 9: الموضوعات المقترحة ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: الموضوعات المقترحة
Content: هذه الموضوعات لا تَشْتَمِلُ على أَفكار مُخَطَّطِ الوَحْدَةِ الأولى جميعها، وَإِنَّا تَتَضَمْنُ بَعْضًا مِن هَذِهِ الْأَفكار

=== BLOCK 10: الموضوعات المكتوبة ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أولا: الموضوعات المقترحة المكتوبة:
Content: الموضوع المقترح المكتوب الأول: قيل: (شَغَلَتِ القضايا الوَطَنِيَّةُ وَالقَوْمِيَّةُ اهْتِمَامَ الْأُدَبَاءِ العَرَبِ فِي العَصْرِ الحَدِيث،ِ فَعَبَّرُوا عَنْ فَرْحَتِهِم بِجَلَاءِ المُسْتَعْمِرِ الغربي، وفضحوا جرائم الصهاينة بحق أبناء فلسطين، مُبْرِزِينَ تَمَسُّكَ الفَلَسْطِينيين بِفِكْرَةِ النضالِ فِي سَبِيلِ الوُجُودِ حِينَا ، وَإِصْرَارَ المُهَجْرِينَ مِنْهُم على العَوْدَةِ إِلَى أَرْضِهِمْ حِيْنًا آخَرَ). ناقش الموضوع السَّابِقَ وَأَيِّدْ مَا تَذْهَبُ إِلَيْهِ بِالشَّوَاهِدِ المَنَاسِبَة،ِ مُوَظِّفاً الشَّاهِدَ الآتي: قَالَ تَوْفِيقِ زَيَّاد :

=== BLOCK 11: شاهد الموضوع ===
(Component: TEMPLATE_C_POEM.html)
Title:
Hemistich 1: أَهْوَنُ أَلْفَ مَرَّهُ
Hemistich 2: أَنْ تُدْخِلُوا الفِيلَ بِثَقْبِ إِبْرَهُ
Hemistich 3: مِنْ أَنْ تُمِيتُوا بِاضْطِهَادِكُمْ وَمِيضَ فِكْرَهُ
Hemistich 4: وَتَحْرِفُونَا عَنْ طَرِيقِنَا الذي اخْتَرْنَاهُ
Hemistich 5: قَيْدَ شَعْرَهُ

=== BLOCK 12: إجابة الموضوع ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
Mapped Component: TEMPLATE_C_TABLE.html
Title: إجابة الموضوع المقترح المكتوب الأول :
Row 1: وَقَعَتِ الأُمَّةُ العَرَبِيَّةُ بَينَ مَخَالِبِ الدول الاستعمارية، والكيانِ الصُّهْيُونِي الذين اندَفَعُوا نَحْوَ رُبُوع بلادنا كالوحوش الضارِيَةِ التي تَنْقَضُ على الفريسة لِتَفْتِكَ بِهَا، إِلَّا أَنَّ أَبْنَاءَ الوَطَنِ العربي، بما فطروا عليه من إباء للظلم وتَعَشقِ للحريَّة،ِ لَم يَكُونُوا صَيْدًا سَهْلَا؛ فقد

--- END STREAM ---
