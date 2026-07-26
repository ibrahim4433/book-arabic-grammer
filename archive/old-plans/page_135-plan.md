# **SESSION 135**

[TASK DEFINITION]
Objective: Implement page 135.
File: `pages/page_135.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools. If it overflows, it is a catastrophic failure. Do NOT try to solve overflow by deleting text (Strict Typographer Rule). Solve it by choosing denser templates or omitting optional white-space.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`. Ensure exact visual continuity (same title, same classes).
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md` to identify the correct template to use for the continuation. You are forbidden from guessing. Scan the raw text for the preceding keyword to determine the active template and apply the correct `_PART_2.html` wrapping.
3. Text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
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
[LESSON_NUMBER]: 135
[CHAPTER_TITLE]: page 135
[CATEGORY_HEADER]: 135
[SECTION_HEADER]: 135
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Continuation of Previous Section ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[BLOCK_TITLE]: الموضوع المقترح المكتوب
[CONTENT]:
سُلِخَ عَنْهَا، فَأَعَادَ لِرُوحِهِ التَّوَازُنَ النَّفْسِيِّ بِتَشَبُّثِهِ بِالأَمَلِ، وَتَطَلُّعِهِ لِلعَوْدَةِ وَهَذَا مَا دَعَا الْأَدَبَاءَ إِلَى إِبْرَازِ إِصْرَارِ الْمُهَجَّرِينَ الفَلَسْطِينِيِّينَ على العَوْدَةِ إِلَى أَرْضِهم، فقد طرح الأدباء الهم جانبًا وارتفع في أعْمَاقِهِم صَوْتُ التَّمَرُّدِ والاحتجاج على الواقع، فَتَرَفَّعُوا عَنِ البُكَاءِ واللطم والعويل، فَظَهَرُوا فِي أَدَبِهِمْ مُتَجَاوِزِينَ المِحْنَةَ مُتَخَطِّينَ الفَجِيعَةَ، يَرْسُمُ لَهُمْ تَمَسُّكُهُم بِأَمَلِ العَوْدَةِ الظَّافِرَةِ، صُورَةَ الْمُسْتَقْبَلِ الوَاعِدِ.
فالشَّاعِرُ الفَلَسْطِينِي محمود درويش لا يَتَخَلَّى عَنْ حُلُمِ العَوْدَةِ إِلَى أَحْضَانِ الوَطَنِ الدَّافِئَةِ، ويُؤَكِّدُ أَنَّ قَرَارَ العَوْدَةِ إِلَى الْأَرْضِ الفَلَسْطِينِيَّةِ قرارٌ قَطْعِي لا رَجُوعِ عَنْهُ، فَيُبْدِي إِرَادَةً صُلْبَةً قَوِيَّةً أَقْوَى مِنَ الصَّخْرِ، وَيُظْهِرُ إِصْرَارَهُ على تنفيذ هذا القرار مهما تَطَلَّبَ تَنْفِيذُهُ مِنْ عَنَاءٍ وَجُهْدٍ. يَقُولُ :

=== BLOCK 3: Poem ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: شعر
[POET_NAME]: محمود درويش
[RIGHT_HEMISTICH]: مَشْيًا على الأقدامِ
[LEFT_HEMISTICH]: أَوْ زَحْفًا على الأيدي نَعُودُ

=== BLOCK 4: Al-Karmi Block ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: استمرار الشواهد
[CONTENT]:
أَمَّا الشَّاعِرُ عَبد الكريم الكَرْمِي فقد ظَلَ حَلْمُ العَوْدَةِ مَائِلًا أَمَامَ عَيْنَيْهِ لَا يَغِيْبُ عَنْهُ لَحْظَةً، فهو يُؤَكِّدُ أَنَّ العَوْدَةَ إِلَى الْأَرْضِ الفَلَسْطِينِيَّةِ قَادِمَةٌ لَا مَحَالَةَ، يَقُولُ :

=== BLOCK 5: Poem 2 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: شعر
[POET_NAME]: عبد الكريم الكرمي
[RIGHT_HEMISTICH]: غَدًا سَنَعُودُ وَالأَجْيَالُ تُصْغِي
[LEFT_HEMISTICH]: إلى وقع الخطا عِنْدَ الإِيَابِ

=== BLOCK 6: Conclusion ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: خلاصة
[CONTENT]:
هَكَذَا نَجِدُ أَنَّ الأدب العَرَبِيَّ ظَلَ مُلازِمَا لِلقَضَايا الوَطَنِيَّةِ والقومية التي تبرز في الساحة العربية، فقد وَجَدَ الأدباء في هذه القَضَايا مادَّةً غزيرةً غَمَسُوا فيها أقلامَهُمْ، فَصَاغُوا منها أَدَبًا تَجَلَّتْ فيه الفَرْحَةُ الصَّاخِبَةُ بجلاء المستعمر الفرنسي عَنْ البلاد، وَبَرَزَتْ فِيهِ جرائم العَدُوِّ الصهيوني المرتكبة بحق أبناء فلسطين، كما ظهر فيه تشبث الفلسطينيين بِفِكْرَةِ النضالِ والكِفَاحِ مِنْ أَجْلِ الوُجُودِ. كذلك تبدى في صَفَحَاتِ هذا الأدب إصرار الفلسطيني المهجر على العودة إلى أَرْضِ الوَطَنِ الْحَبِيبِ.

=== BLOCK 7: The Core Matrix - Essay Prompt ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: الموضوع
[HEADER_2]: المناقشة
[HEADER_3]: الشواهد
[CELL_1]: الموضوع المقترح المكتوب الثاني: قيل: (تناول الأُدَبَاءُ العَرَبُ القَضَايَا الوَطَنِيَّةَ وَالقَوْمِيَّةَ، فَأَكدوا إصْرَارَ المهجرين الفلسطينيين على العَوْدَةِ إِلَى أَرْضِهِم، واستنكرُوا خِداعَ الفَرَنْسِيِّين الشُّعُوبَ العَرَبِيَّةَ، وَمَجَدُوا التَّضْحِيَاتِ الْمُشْرِّفَةَ التي حَقَقَتِ الْجَلَاء).
[CELL_2]: ناقش المَوْضُوعَ السَّابِقَ وَأَيَدْ مَا تَذْهَبُ إِلَيْهِ بِالشَّوَاهِدِ المُنَاسِبَةِ، مُوَظِّفًا الشَّاهِدَ الآتي : قَالَ خَيْرُ الدِّينِ الرَّزَكْلِي:
[CELL_3]: جَهَرُوا بِتَحْرِيرِ الشَّعُوبِ وَأَثْقَلَتْ مَتْنَ الشَّعُوبِ سَلَاسِلٌ وَقُيُودُ<br>خَدَعُوكِ يَا أُمَّ الْحَضَارَةِ فَارْتَمَتْ تَجْنِي عَلَيْكِ فَيَالِقٌ وَجُنُودُ

=== BLOCK 8: Essay Answer Start ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: إجابة الموضوع المقترح المكتوب الثاني
[CONTENT]:
سَالَتْ إِلَى رُبُوعِ وَطَنِنَا العَرَبِي جَحَافِلُ المحتلِّينِ الطَّامِعين عبر تاريخه، نظرًا لما يتمتَّعُ بِهِ مِنْ مَوْقِعِ جُغْرَافِي مُتَمَيِّزٍ وَمَا يمتلِكُهُ مِنْ إِرْثٍ حَضَارِي نَادِرٍ، وهذا ما جَلَبَ لَهُ الوَيْلَاتِ، وَأَوْقَعَهُ فَرِيسَةً لأَطْمَاعِ المحتلين الطَّامِعِين، الذين عَاثُوا بِهِ فَسَادًا، وَسَامُوا أَبْنَاءَهُ أَلْوَانَ الْعَذَابِ.
فقد عانى الإنْسَانُ العربي وهو يَرْزَحُ تَحْتَ قَبْضَةِ المحتلينَ مِنَ الظُّلْمِ والقَهْرِ وَالبَطْشِ ذلك أَنَّ المُغْتَصِبَ كَانَ بَاطِشًا لَا يَرْحَمُ وظالما لا يَعْدِلُ. وأقض هذا الواقع المُرُّ مَضَاجِعَ الأَدَبَاءِ، فَهَبُّوا مِن أَجْلِ الذَّوْدِ عَنْ كَرَامَةِ الأَمَّةِ، وَحِيَاضِ الْأَوْطَانِ. فَمَعَ أَنَّ انتزاع الفِلَسْطِينِي مِنْ أَرْضِهِ قد باتَ أَمْرًا واقعا لا مجال لعدم الاعترافِ بِهِ، وَمَعَ أَنَّ هِجْرَةَ الفَلَسْطِينين قد أَمْسَتْ حَقِيقَةً مَرَّةً لَا مَنَاصَ مِنْ تَجَرُّعِ عَلْقَمِها، إِلَّا أَنَّ الفَلَسْطِينِي قَد سَيْطَرَ على أَشْوَاقِهِ العَمِيْقَةِ، وَرَوَّضَ حَنِيْنَهُ الوَثَّابَ لِأَرْضِ الوَطَنِ التي سُلِخَ عَنْهَا، فَأَعَادَ لِرُوحِهِ التَّوَازُنَ النَّفْسِي بِتَشَبُّثِهِ بِالْأَمَلِ، وَتَطَلُّعِهِ لِلعَوْدَةِ وَهَذَا مَا دَعَا الأُدَبَاءَ إِلَى إِبْرَازِ إِصْرَارِ الْمُهَجَّرِينَ الفلسطينيين على العَوْدَةِ إِلَى أَرْضِهِم، فقد طرح الأدباء الهم جانبا وارتفع في أعمَاقِهِم صَوْتُ التَّمَرُّدِ والاحتجاج على الواقع، فَتَرَفَّعُوا عَنِ البُكَاءِ وَاللَّطْمِ والعَوِيْل، فَظَهَرُوا في أَدَبِهِمْ مُتَجَاوزين المِحْنَةَ مُتَخَطِّينَ الفَجِيعَةَ، يَرْسُمُ لَهُم تَمَسُّكُهُم بِأَمَلِ العَوْدَةِ الظَّافِرَة، صُورَةَ الْمُسْتَقْبَلِ الوَاعِدِ.
فالشَّاعِرُ الفَلَسْطِينِي محمود درويش لا يَتَخَلَّى عَنْ حُلُمِ العَوْدَةِ إِلَى أَحْضَانِ الوَطَنِ الدَّافِئَةِ، ويُؤَكِّدُ أَنَّ قَرَارَ العَوْدَةِ إِلَى الأَرْضِ الفَلَسْطِينِيَّةِ قَرَارٌ قَطْعِي لا رجوع عَنْهُ، فَيُبْدِي إِرَادَةً صُلْبَةً قَوِيَّةً أَقْوَى مِنَ الصَّخْرِ، وَيُظْهِرُ إِصْرَارَهُ على تَنْفِيذِ هذا القرار مهما تَطَلَّبَ تَنْفِيدُهُ مِنْ عَنَاءٍ وَجُهْدٍ. يَقُولُ :

=== BLOCK 9: Poem inside Answer ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: شعر
[POET_NAME]: محمود درويش
[RIGHT_HEMISTICH]: مَشْيًا على الأقدامِ
[LEFT_HEMISTICH]: أَوْ زَحْفًا على الأيدي نَعُودُ

=== BLOCK 10: Essay Answer Cut Content ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
[BLOCK_TITLE]: إجابة الموضوع المقترح المكتوب الثاني
[CONTENT]:
أَمَّا الشَّاعِرُ عَبد الكريم الكرمي فقد ظل حلمُ العَوْدَةِ مَائِلًا أَمَامَ عَيْنَيْهِ لَا يَغِيْبُ عَنْهُ لَحْظَةً، فهو يُؤَكِّدُ أَنَّ العَوْدَةَ إِلَى الْأَرْضِ الفَلَسْطِينِيَّةِ قَادِمَةٌ لَا مَحَالَةَ. يَقُولُ :

--- END STREAM ---
