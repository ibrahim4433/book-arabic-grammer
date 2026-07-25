# **SESSION 198**

[TASK DEFINITION]
Objective: Implement page 198.
File: `pages/page_198.html`
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
[CONTENT]:

=== BLOCK 2: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 198
[CHAPTER_TITLE]: page 198
[CATEGORY_HEADER]: 198
[SECTION_HEADER]: 198
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 3: Topic Content (Cut Content Continuation) ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[BLOCK_TITLE]: الاستيعاب والفهم
[CONTENT]: يُتَاحَ لَهُ أَنْ يُبْصِرَ طريقَهُ إِلَى الهَدَفِ الأَبْعَدِ وَالأَسْمَى، ألا وهو المعرفة والقدرة، والحريَّةُ التِي مِنْ شَأْنِهَا أَنْ تَعُودَ بِالإِنْسَانِ إلى تكوينه الإلهي.

=== BLOCK 4: Warning ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[TITLE]: تنبيه
[CONTENT]: حاول الشَّرْقُ فيما مَضَى أَنْ يُطَبَقَ دِيْنَهُ على دُنْيَاه،ُ وَأَنْ يَجْعَلَ مِنَ الْأَرْضِ سُلما يرقى به إلى السَّمَاء،ِ فَهَلْ نَجَحَ فِي ذَلِكَ؟ لَمْ يَنْجَحْ مِنْ أَبْنَاءِ الشَّرْقِ غَيْرُ أَفْرَاد،ِ أَوْلَئِكَ هُمُ الأنبياء، والأَولياء، والقديسون، والمختارون،َ أَمَّا الجَمَاهِيرُ فَقَدْ أَجْهَدَهَا المحاولة وأَنفُكَتْ قُواها، فَلَاذَتْ بِالقُشُورِ وَأَهْمَلَتِ اللُّبَاب.َ

=== BLOCK 5: Block ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الأسئلة
Content: (Use TEMPLATE_C_LIST)

=== BLOCK 6: List Q&A - 1 ===
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: <span class="font-bold">ج -</span> كُلُّ دِينِ مِنْ هَذِهِ الأَدْيَانِ يَرْمِي إِلَى تَرْوِيضِ الْقَلْبِ على طريق الخيرِ كَيْمَا يُتَاحَ لَهُ أَنْ يُبْصِرَ طريقَهُ إِلَى الهَدَفِ الأَبْعَدِ وَالأَسْمَى، ألا وهو المعرفة والقدرة، والحريَّةُ التِي مِنْ شَأْنِهَا أَنْ تَعُودَ بِالإِنْسَانِ إلى تكوينه الإلهي.
[LIST_ITEM_CONTENT]: <span class="font-bold">س -</span> هَجَعَ الشَّرْقُ هَجْعَتَهُ الطَّويلة، فما الذي لاقاه على يَدِ أَخِيهِ الغَرْبِ؟
[LIST_ITEM_CONTENT]: <span class="font-bold">ج -</span> لَقَدْ سِيمَ الشَّرْقُ خِلَالَ هَجْعَتِهِ الطَّوِيلَةِ شَتَّى أَنواع الدُّلِّ وَالهَوَانِ على يَدِ أَخِيهِ الْغَرْب.ِ

=== BLOCK 7: Matrix / Table of Q&A ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: السؤال
[HEADER_2]: الجواب
[CELL_1_1]: ماذا فَعَلَ الشَّرْقُ بَعْدَ أَنِ انْتَفَضَ اليومَ مِنْ هَجْعَتِهِ الطويلة؟
[CELL_1_2]: إِنَّ الشَّرْقَ اليومَ يَنْتَفِضُ انتِقَاضَةَ الجَبَار،ِ فَيَنْزِعْ عَنْهُ وَيَكْشَحْ ظُلُمَاتِ الدُّلِّ والهوان مَعْلَمًا تِلْوَ مَعْلَمٍ مِنْ مَعَالم الاستِثْمَارِ والاستِعْمَار،ِ وَيَعْمَلُ بِنَشَاطِ واندِفاع على ترميم ما انهارَ مِنْ شَانِه،ِ وَاستردادِ مَا ضَاعَ مِنْ حَقِه،ِ وَتَلْينِ مَا تَصَلَّبَ مِنْ عزيمته.
[CELL_2_1]: بِمَاذَا شَبَّهُ الكَاتِبُ الشَّرْقَ بَعْدَ أَنِ انْتَفَضَ اليومَ مِنْ هَجْعَتِهِ الطَّوِيلِةِ؟
[CELL_2_2]: شَبَّهَهُ بِالنَّسْرِ الذي يُجَدِّدُ شَبَابَه،ُ وَيَتَطَلَّعُ إِلَى عَالَم أَرْحَبَ وَأَفْضَلَ وَأَجْمَلَ مِنْ عَالَ هُوَ فِيه.ِ
[CELL_3_1]: كيف نظر الكاتب إلى العالم الذي نعيش فيه اليوم؟
[CELL_3_2]: رأى الكاتِبُ أَنَّنَا نَعِيش اليوم على فُوهَةٍ بُركانٍ فَالْعَالَمُ الذِي نَعِيشُ فِيهِ انْشَطَرَ إِلَى مُعَسْكَرَين مُدَجَجَين بالسلاح، وكلاهما يَرْتَقِبُ الفُرْصَةَ المواتية لينقض على الآخر فلا يُبْقِي ولا يَذَر.ُ
[CELL_4_1]: لماذا حكم الكاتب على مُحَاوَلَةِ الوُصُولِ إِلَى الحَرِّيَّةِ والسَّعَادَةِ بِالفَشَلِ وَالإِخْفَاقِ؟
[CELL_4_2]: لأَنَّ الْمُسْكَرَيْنِ المُدَجَجَين بالسلاح ليسَ يَعْنِيهما مِنَ الإِنْسَانِ سوى أَنَّهُ مُنْتِج ومُسْتَهْلِك،َ وَصَاحِبُ عَمَلِ أو عامِل،ٌ وَأَنَّهُ أَبيض أو أَسْمَر،ُ وَأَنَّهُ وطني فِي هَذِهِ البَفْعَة،ِ وَأَجْنَبِيَّ فِي كُلِّ مَا عَذَاهَا مِنْ بِقَاعِ الأَرْض،ِ فكلا المُعَسْكَرَيْنِ لَا يُبْصِرُ مِنَ الإِنْسَانِ غَيْرَ لِّهِ وَقُسُورِه.ِ

=== BLOCK 8: Block ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الأسئلة المقترحةُ فِي المَقْطَعِ الثالث
Content: (Use TEMPLATE_C_LIST)

=== BLOCK 9: List Q&A - 4 ===
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: <span class="font-bold">س -</span> متى يستطيع الشَّرْقُ المُتَجَدِدُ أَنْ يُنْجِيَ العَالَمَ مِنَ الكَارِثَةِ التِي حَلَّتْ بِهِ بِحَسَبِ رأي الكَاتِبِ؟
[LIST_ITEM_CONTENT]: <span class="font-bold">ج -</span> إذا عَرَفَ كِيفَ يَتَحَرَّرُ مِنْ رِبَّقَةِ الطقوس المتحجرة، وكيف يَسْتَمِدُّ القُوَّةَ والحِدَايَةَ مِن مُعَلَّمِيهِ العِظَام.ِ
[LIST_ITEM_CONTENT]: <span class="font-bold">س -</span> ما هي رسالة الشرقِ المُتَجَدِّدِ بَعْدَ أَنْ يَتَحَرَّرَ مِنَ الطَّقْوسِ الْمُتَحَجَرَة،ِ وَبَعْدَ أَنْ يَسْتَمِدَّ القُوَّةَ وَالهُدَايَةَ مِنْ مُعَلَّمِيهِ العِظام؟
[LIST_ITEM_CONTENT]: <span class="font-bold">ج ٢-</span> رسَالَةُ الشَّرْقِ المُتَجَدِدِ هي تذكير النَّاسِ في كل مكان بِأَنَّ هَدَفَهُم واحد، وطريقهم إلى الهدف واحد، وَأَنَّ عَلَيْهِم أَنْ يَسلكوا ذلك الطريق مُتَعاونينَ لَا مُتنابذين، وزادُهُمُ الفكر والوجدان والخيال والإرادة، وأَنهُمْ مَتَى أَدْرَكُوا سُمُو الهَدَفِ الذي إليه يسيرونَ أَصْبَحَتْ فوارق الجنس واللون واللغة والمَنْهَبِ عَوْنَا لَهُم فِي سَيْرِهِم بَدَلَا مِنْ أَنْ تكونَ حَجَرَ عَفْرَة،ِ وَأَنَّ الأَرْضَ هي ميرات الجميع، ونَجِبُ أَنْ تُسْتَغَلَّ خَيْرِ الجميع، إِنَّهُ لَمِنْ أَكبرِ الخَيْرِ لِلإِنْسَانِ أَنْ يُحِبَّ جَارَهُ بَدَلَا مِنْ أَنْ يَبْغَضَهُ.
[LIST_ITEM_CONTENT]: <span class="font-bold">س -</span> ما هي نتيجة إداك النَّاسِ سُمو الهدف الذي يسيرون إليه؟
[LIST_ITEM_CONTENT]: <span class="font-bold">ج-٣</span> تُصْبِحُ فَوَارِقُ الجنسِ وَاللَّوْنِ وَاللَّغَةِ وَالْمَذْهَبِ عَوْنَا لَهُمْ فِي سَيْرِهِم،ْ بَدَلَا مِنْ أَنْ تكونَ حَجَرَ عَنْرَة،ِ وَسَيُدْرِكُونَ أَنَّ الأَرْضَ هي ميرات الجميع، ويجب أَنْ تُسْتَغَلَّ لِخَيْرِ الجَمِيع.ِ
[LIST_ITEM_CONTENT]: <span class="font-bold">س -</span> متي يُمكنُ أَنْ يُذَلِلَ الشَّرْقُ فَوارِقَ الجنس واللوْنِ وَاللَّغَةِ والمَذْهَبِ؟
[LIST_ITEM_CONTENT]: <span class="font-bold">ج -</span> عِنْدَمَا يَسْلكَ أَبْنَاؤُهُ الطَّرِيقَ مُتَعَاوَنِينَ لَا مُتَنَابِذِين،َ ويكون زادُهُمُ الفِكْرُ والوجدان والخيال والإرادة، ويُدْرِكُونَ سمو الهَدَفِ الذي يسيرون إليه.
[LIST_ITEM_CONTENT]: <span class="font-bold">س -</span> ماذا أَوْجَبَ الكاتب على الأجيال الحاضرة والأجيال الطَّالِعَةِ فِي الشَّرْقِ؟
[LIST_ITEM_CONTENT]: <span class="font-bold">ج -</span> أَوْجَبَ الكاتب على الأجيال الحاضِرَةِ وَالأَجْيَالِ الطَّالِعَةِ فِي الشَّرْقِ أَنْ تُطَهْرَ أَفْكَارَهَا وَقُلُوبَهَا مِنْ تُرَهَاتِ كثيرةِ التَقَطَتها مِنْ هُنا وهناك، وأَنْ تُلَقِحَهَا مِنْ جديد بإيمانِ الشَّرْقِ بالإنْسَانِ الذي هو خليفة اللهِ فِي الأَرْض.ِ
[LIST_ITEM_CONTENT]: <span class="font-bold">س -</span> ما سَبَبُ صُمُودِ الشَّرْقِ فِي وَجْهِ الأَسْلِحَةِ الجِهَنَّمِيَّةِ التي صَنَعَتْها المَدَنِيَّةُ الغَرْبِيَّةُ وَوَجَّهَتْهَا نَحْوَهُ؟
[LIST_ITEM_CONTENT]: <span class="font-bold">ج -</span> الإيمان بالإنْسَانِ الذي هو خليفة اللهِ فِي الأَرْض،ِ فالقُلُوبُ والأفكار العامرة بهذا الإيمان تمتلك مَنَاعَةً عظيمة وكبيرة ضد أَي سلاح.
[LIST_ITEM_CONTENT]: <span class="font-bold">س -</span> كَيْفَ نَظَرَ الكَاتِبُ إِلى روح الشَّرْقِ؟
[LIST_ITEM_CONTENT]: <span class="font-bold">ج -</span> رأى أَنَّهُ رُوْحٌ قَهَرَ الزَّمَان،َ وَبَدَا وَائِقًا مِنْ أَنَّهُ رُوح لا يُقْهَرُ ولا يموت.

=== BLOCK 10: Exam Block ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: ما سَبَبُ ثِقَةِ الشَّاعِرِ بِعَدَمِ نَيْلِ أفظعِ الأَسْلِحَةِ الجَهَنَّمِيَّةَ مِنْ أَبْنَاءِ الشَّرْقِ؟

--- END STREAM ---
