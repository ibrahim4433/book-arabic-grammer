# **SESSION 197**

[TASK DEFINITION]
Objective: Implement page 197.
File: `pages/page_197.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`. Ensure exact visual continuity (same title, same classes).
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md` to identify the correct template to use for the continuation. You are forbidden from guessing. Scan the raw text for the preceding keyword to determine the active template and apply the correct `_PART_2.html` wrapping.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   **Rule:** NO INLINE STYLES.
*   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
*   **Mapping:**
    *   `style="width: 20%"` -> `class="w-20pct"`
    *   `style="margin-top: 2mm"` -> `class="mt-2mm"`
    *   `style="text-align: center"` -> `class="text-center"`
    *   `style="font-weight: bold"` -> `class="font-bold"`
6. Templates: You are forbidden from inventing new HTML tags or classes or template elements. You must map all content using "Jules-workspace/Templates/" components as the STREAM says in a suitable way. **CRITICAL 1-PAGE MODE RULE**: You MUST NOT use `<section>` tags when applying templates. Replace any `<section>` tags from the templates with `<div>` tags (keep `<header>` for page headers as is).
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
[LESSON_NUMBER]: 197
[CHAPTER_TITLE]: page 197
[CATEGORY_HEADER]: 197
[SECTION_HEADER]: 197
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 3: Cut Content Part 2 ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[BLOCK_TITLE]: النص
[CONTENT]: إِنَّ كِلا المُعَسكرين لَا يُبْصِرُ مِنَ الإِنْسَانِ مَا عَدَاهَا مِنْ بِقَاعِ الأَرْضِ وَبِكَلِمَةٍ أُخْرَى أبيض أو أَسْمَر،ُ وَأَنَّهُ وطَيَّ فِي هَذِهِ البُقْعَة،ِ وَأَجْنَبِيَّ فِي كُلِّ حَتْمَا إِلى بِهِ إِلَى الحَرِّيَّةِ وَالسَّعَادَةِ لَمُحَاوِلَةً مَصْيرُهَا في هذا الطريق أو ذَاكَ بِقَصْدِ الوُصُولِ غيرَ لِهِ وَقُشُورِه.ِ ولِذَلِكَ فَكُلُّ مُحاولة يُبديها لتوجيهه الإخْفَاق.ِ () مِنْ رِبَّقَةِ التَّقُوسِ الْمَتَحَجَرَة،ِ وكيفَ يَسْتَمِدُّ مِنَ الكارثةِ إِذا هو عَرَفَ كِيفَ يَتَحَرَّرُ ويقيني أَنَّ الشَّرْقَ المتجدد يستطيع أَنْ يُنجي العالم وطريقهُمْ إلى الهدف واحد، وأَنَّ عليهم أَنْ ذَاكَ هي تذكير الناس في كل مكان بِأَنَّ هَدَفَهُمْ واحد، القُوَّةَ والهداية من مُعلميه العظام فرسالتُهُ إِذْ أَصْبَحَتْ مَتَى أَدركوا سمو الهدف الذي إِلَيْهِ يسيرونَ الفكر والوجدان والخيال والإرادة، وأَهُمْ يَسْلُكُوا ذَلِكَ الطَّريق مُتَعَاونِينَ لَا مُتَنابذِين،َ وزادُهُمُ أَنْ تُسْتَغَلَ خَيْرِ وَأَنَّ الأَرْضَ هي ميراث الجميع ونَجِبُ فِي سَيْرِهِمْ بَدَلَا مِنْ أَنْ تكونَ حَجَرَ عَنْرَة،ِ فوارق الجنس واللون واللَّغَةِ وَالْمَذْهَبِ عَوْنَا لَهُمْ جَارَهُ بَدَلًا مِنْ أَنْ يُبْغِضَه.ُ الجميع. إِنَّهُ لَمِنْ أَكبرِ الخَيْرِ لِلإِنْسَانِ أَنْ يُحِبَّ تُلَقِحَهَا من جديد كثيرة التقطتها من هنا وهناك، وأَنْ أَنْ تُطَهَرَ أَفْكَارَهَا وَقُلُوبَهَا مِنْ ترهات وعلى الأجيال الحاضرة والأَجْيَالِ الطَّالِعَةِ فِي الشَّرْقِ ذَلِكَ الإيمانِ لَأَمْنَعُ مِنْ أَنْ تَنَالَ منها أَفْضَعُ الأَسْلحَةِ الله فِي الأَرْضِ إِنَّ قُلُوبًا وَأَفكارا عامرةً مِثْلِ بإيمانِ الشَّرْقِ بالإنسان الذي هو خليفة الزَّمَانَ لَروح لا يقهر ولا يموت. الجَهَنَّمِيَّةِ مَنَالًا . وإِنَّ روح الشَّرْقِ الذي فَهَرَ

=== BLOCK 4: Warning for Color Balance ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[TITLE]: الأسئلة المقتَرَحَةُ فِي المَقْطَعِ الأَوَّل :
[CONTENT]: - كيف رأى الكاتب المدنية العربية المُسَيْطِرَةَ على العالم؟ التِي خَلَقَتْهَا مِنْ نَفْسِهَا لِنَفْسِها، ج - رأى الكاتب المدنية العربية المُسَيْطِرَةَ على العالم تَتَخَبَّطُ اليومَ فِي شِبَاكِ مِنَ الْمُشْكِلاتِ المُعَقَدَةِ ورأى أَنَّها ما زالَتْ تُفَتِ عَنْ بَابِ لِلخَلاص فلا تحتدي إليه.

=== BLOCK 5: Core Matrix (Summary Table) ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: السؤال
[HEADER_2]: الجواب
[HEADER_3]: توضيح
[CELL_1]: - لماذا لَمْ تَسْتَطِعِ الْمَدَنِيَّةُ الغَرْبِيَّةُ الخلاص مِنْ شِبَاكِ الْمُشْكِلَاتِ المُعَقْدَةِ التِي خَلَقَتْهَا مِنْ نَفْسِهَا لِنَفْسِهَا؟
[CELL_2]: ج ٢- لِأَنَّهَا صَرَفَتْ جُل اهتمامِها إلى العَقْلِ وترويضِهِ وتَنْظِيمِه،ِ أَحْسَنَتْ ترويضَهُ وتنظيمه.
[CELL_3]: الشَّهَوَاتُ فَمَا أَمَّا القَلْبُ الذي تَصْطَرِعُ فِيهِ رَكْزَتْ جُل اهتمامِها على العقل وترويضه؟

=== BLOCK 6: Question List 1 ===
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: ما هي النَّتَائِجُ التي أَفْرَزَقْهَا المَدَنِيَّةُ الغَرْبِيَّةُ عِنْدَمَا الْمُدْهِشَة.ِ والاكِتِشَافَاتِ الاختراعات العجيبة والتَطْبِيقِيَّة،ِ فَكَانَ هَذَا الْفَيْضُ العَارِمُ مِنَ ج -۳ نَتَجَ عَنْ ذلك طَفْرَةً باهِرَةٌ فِي دُنْيَا العُلُومِ النَّظَرِيَّةِ نَتَجَ عَنْ ذَلِكَ؟
[LIST_ITEM_CONTENT]: لَمْ تُحْسِنِ الْمَدَنِيَّةُ الغَرْبِيَّةُ تَرْوِيضَ القَلْبِ وَتَنْظِيمَهُ مَاذَا السُّود.ِ وَدَهَاءِ وَغَيْرِهَا مِنَ الشَّهَوَاتِ ج - نَتَجَ عَنْ ذلك هذا الطَّغْيانُ اللَّذِي نَشْهَدُهُ اليومَ مِنْ أَنَانِيَّةِ وَحِقْدٍ وَبُغْضِ وَتَنَائِذٍ وَجَشَعٍ وَمَكْرٍ والتَّنَائِذٍ والجشع والمكر والدهاء؟
[LIST_ITEM_CONTENT]: ه - ما سَبَبُ الطَّغيان الذي نَشْهَدُهُ اليوم مِنَ الأنانية والحِقْدِ والبُغْضِ القَلْبَ الذي تَصْطَرَعُ فِيهِ الشَّهَوَات.ُ العقل وترويضه وتنظيمه، وأَهْمَلَتِ لأَنَّ المَدَنِيَّةَ الغَرْبِيَّةَ صَرَفَتْ جُلَّ اهتمامها إلى
[LIST_ITEM_CONTENT]: - أَشَارَ الشَّاعِرُ إِلَى أَثَرِ الشَّهَوَاتِ فِي الْمَدَنِيَّةِ اذْكُرُ هَذَا الْأَثَر.َ ج - رأى أَنَّ الشَّهَوَاتِ تُقَوِّضُ اليومَ أَرْكَانَ هَذِهِ المَدَنِيَّةِ مِثَلَمَا قَوْضَتْ أَرَكَانَ مَا سَبَقَهَا مِنْ مَدَنِيَّات.
[LIST_ITEM_CONTENT]: - ما الأَثَرُ الذي تَتْرَكُهُ سِيطَرَةُ الشَّهَواتِ إِذَا اسْتَفْحَلَ أَمْرُها؟ ج - إِنَّا تَعْبَتْ بِنِتَاج العَقْل،ِ فَتَجْعَلَهُ أَدَاةً تَخْرِي بَدَلَ النَّعْمِير،ِ وَمَصْدَرَ شَقَاءِ لَا هَنَاء،ٍ ونقطة انزلاق لا انطلاق.
[LIST_ITEM_CONTENT]: الكاتب؟ - إذا انهَارَتِ المَدَنِيَّةُ الحَاضِرَة،ُ فَمَنِ الذي سَيَفَعُ لِلبَشَرَيَّةِ مِشْعَلَ الهداية، ويُقِيلُها مِنْ عَفْرتها في رأي مَرَّةٍ مُنْذَ فَجْرِ التَّاريخ. - يرى الكاتب أَنَّ الشَّرْقَ سَيَقُومُ بِهَذِهِ الْمَهَمَّةِ الخَطِرَةِ مِنْ جَدِيد،ٍ فهو الذي انْبَرَى لها مَرَّةً بعد

=== BLOCK 7: Questions Block 2 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الأسئلة المقترحةُ فِي المَقْطَعِ الثاني:
Content: - يرى الكاتِبُ أَنَّ لِلأَرْمِنَةِ دَلائلها، فما دلالة الزَّمَانِ الَّذِي نَحْنُ فِيهِ؟ الْحِدَايَةِ إِذَا انْكَارَتِ الْمَدَنَيَّةُ الحَاضِرَة،ً فهو الذي انترى لها ج - دلالة الزمانِ الَّذِي نَحْنُ فِيهِ أَنَّ الشَّرْقَ مَدْعُ لِلقِيَامِ بِمَهَمَّةِ رَفْعِ مِشْعَلِ ولا أَخْفَقَ الإِخْفَاقَ كَلَّه.ُ مَرَّةً بعدَ مَرَّةٍ مُنْدُ فَجْرِ التَّاريخ، فَمَا أَفْلَحَ الإِفْلاح كُلَّه،ُ - كيف نظر الكاتب إلى الديانات التي نَشَرَهَا الشَّرْقُ فِي الْأَرْضِ؟ ألا وهو ج - رأى أَنَّا مَنَاهِ تَحْدِفُ إلى ترويض القلب على طريق الخَيْرِ كي ما يُتَاحَ لَهُ أَنْ يُبْصِرَ طَريقة إلى الهُدَفِ الأَبْعَدِ والأسمى، المعرفة والقُدْرَة،ُ والحرية التي مِنْ شَأْنِهَا أَنْ تعودَ بِالإِنْسَانِ إلى تكوينه الإلهي.

=== BLOCK 8: Exam Section ===
(Component: TEMPLATE_C_EXAM.html)
[QUESTION_NUMBER]: ١
[QUESTION_TEXT]: ما هي رسَالَهُ كُلِّ دِينِ مِنَ الْأَدْيَانِ التِي جَاءَ بِمَا الْمَشْرِقُ؟ - - ۱۹۷ الأحكمة

--- END STREAM ---
