# **SESSION 190**

[TASK DEFINITION]
Objective: Implement page 190.
File: `pages/page_190.html` (Note: Use the exact page number.)
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
[LESSON_NUMBER]: 190
[CHAPTER_TITLE]: page 190
[CATEGORY_HEADER]: 190
[SECTION_HEADER]: 190
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Cut Content Continuation ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[BLOCK_TITLE]: القاعدة
[CONTENT]: أ. الفَتْحَةُ، وقبلها ألف - ساءَت: هَمزة متوسطة، حركتها <span class="highlight-red">فَتَحَةٌ</span>. متوسطة، مفتوحة، وقبلها <span class="highlight-blue">مُتَطَرَفَةٌ</span>، قبلها ساكن - دابٌ هَمْرَةً ساكنة، وهي حالة شاذة - بلاء: هَمْرَةُ يأتي: )ساءت، بلاء، داب(. جِهْ عَلْ كِتَابَةَ الهَمْرَةِ على صورتها فيما

=== BLOCK 3: Poem and Bio ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: تحليل مفصل المضمون الأبيات:
[POET_NAME]:
[RIGHT_HEMISTICH]: سَاءَتْ حَيَاةٌ كُلُّهَا تَعَبُ
[LEFT_HEMISTICH]: يَبْنِي القُصُورَ وَكُوخُهُ خَرِبُ

=== BLOCK 4: Explanation for Poem 1 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الشرح
Content: يُشَيِّدُ البَنَّاءُ القُصُورَ الفَارِهَةَ، في الوقت الذي يبدو فيه بيته وَضِيعًا مُهَدَّمًا، أَلَا سُحْقًا لِحِيَاتِهِ التي لا يجني فيها إلا المتاعب والمُعَانَاةَ.

=== BLOCK 5: Core Matrix (Summary) ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: المفردات
[HEADER_2]: الفكرة
[HEADER_3]: الإعراب
[CELL_1_1]: خَرِبُ: صفةٌ مُشبهة باسم الفاعل، فعلها خرب.
[CELL_1_2]: حَيَاةُ البَنَّاءِ المُغَرَّبِ مَلِيْنَةٌ بِالتَّعَبِ والقَسْوَةِ.
[CELL_1_3]: يبني: فعل مضارع مرفوع، وعلامة رفعهِ الضَّمَّةُ المقدرة على الياء، مَعَ ظهورها النَّقَلُ. القصور: مفعول به منصوب. واو الحال: كُوحه، مبتدأ مرفوع، والهاء، ضمير متصل مَبْنِي على الضم في محل جر، مُضَافُ إِلَيْهِ. خَرِبُ: خَبَرٌ مرفوع وعلامةُ رَفْعِهِ الضَّمَّةُ الظَّاهرة. ساءَت: فعل ماض مبني على الفتح؛ لا تصالِهِ بِنَاءِ التَّانيثِ السَّاكنة. والنَّاءُ، حرف تأنيث لا محل لها مِنَ الإعراب. حياة: فاعل مرفوع وعلامة رفعهِ الضَّمَةُ الظَّاهرة. كلها: مبتدأ مرفوع، وها، ضميرٌ مُتَّصِلِّ مَبْنِي على السكون في محل جر، مُضَاف إليه. تعبُ: خَبَرٌ مرفوع.

=== BLOCK 6: Parsing Rules ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: الجمل
[IRAB_ANALYSIS]: جملة )يبني(: ابتدائية، لا محل لها مِنَ الإعراب. جملة )كُوخُهُ خَرِب(: في محل نصب، حال. جملة )ساءَتْ حياة(: استِثْنَافِيَّةٌ، لا مَحَلَّ لها مِنَ الإعراب. جملة )كلها تَعَبُ(: في محل رفع، صفة.

=== BLOCK 7: Poem 2 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]:
[RIGHT_HEMISTICH]: الشوك يزخر في مسالكها
[LEFT_HEMISTICH]: والريح ما تَنْفَكُ تَصْطَخِبُ

=== BLOCK 8: Explanation for Poem 2 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الشرح
Content: حَيَاةُ البَنَّاءُ مَلَأَتْ طُرُقَهَا وَأَنحاءها الأَشْواك، وطغى على أَجْوائِهَا عَصْفُ الريح وهُبُوهَا اللَّذين لا يَفْتُران ولا يَنْقَطعان.

=== BLOCK 9: Core Matrix 2 (Summary) ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: المفردات
[HEADER_2]: الفكرة
[HEADER_3]: الإعراب
[CELL_1_1]: يزخر: زخر النبات، طال. والمراد هنا يملأ. مسالكها: المفرد المسلك، وهو الطريق.
[CELL_1_2]: حَيَاةُ البَنَّاءِ المُغَرَّبِ مَلِيْنَةً بِالتَعَبِ والقَسْوَةِ.
[CELL_1_3]: الشوك: مبتدأ مرفوع. يزخر: فِعْلَ مُصَارِعٌ مَرْفُوعٌ. في: حَرْفُ جَرِّ. مسالكها: اسم مجرور، وعلامَةُ جَرِهِ الكَسْرَةُ الظَّاهِرَةُ. وها، ضَمِيرٌ مُتَّصِلِّ مَبْنِي على السُّكُونِ فِي مَحَلِّ جَرِّ، مُضاف إليه. والريح: الواو، حرف عطف. الريح، مبتداً مرفوع. ما تَنْفَكُ: ما، حَرْفُ نَفِي. تَنْفَك، فِعْلَ مُصَارِعُ نَاقِصَ مَرْفُوع. تَصْطَخِبُ: فِعْلَ مُضَارِعَ مَرْفُو.

=== BLOCK 10: Parsing Rules 2 ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: الجمل
[IRAB_ANALYSIS]: جملة )الشوك يحر في مسالكها(: معطوفة، حَلَّهَا الرَّفْعُ. جملة )يزخر(: خَبَرَيَّةٌ، محلها الرفع. جملة )الريحُ مَا تَنَفَكَ تَصْطَخِبَ(: مَعْطُوفَةٌ، مَحَلَّهَا الرَّفْعُ. جملة )مَا تَنْفَكُ تَصْطَخِبُ(: خَبَرَيَّةٌ، مَحَلَّهَا الرَّفْعُ. جملة )تَصْطَخِبُ(: خَبَرَيَّةٌ، حَلُّهَا النَّصْبُ.

=== BLOCK 11: Poem 3 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]:
[RIGHT_HEMISTICH]: لا يَزْدَهِي في لَيْلِهِ قَبَسٌ
[LEFT_HEMISTICH]: إِلَّا تَوَلَّتْ طَمْسَهُ النُّوب

=== BLOCK 12: Explanation for Poem 3 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الشرح
Content: هذا البائس الكادح لا يُشْرِقُ فِي لَيْلِهِ نُورٌ مِنَ التَّفَاؤُلِ وَالأَمَلِ إِلَّا تَكَفَّلَتْ بِحَجْبِهِ وَمَحْوِهِ المصائب والمِحَنُ.

=== BLOCK 13: Benefit / Core Matrix 3 (Summary) ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: المفردات
[HEADER_2]: الفكرة
[HEADER_3]: الإعراب
[CELL_1_1]: يردهي: يُضيء. قَبَس: شعلة من النار. طمْسَهُ: طَمَسَهُ حَجَبَ ضوه. التوب: مفردها: نوبة، وهي المصيبة.
[CELL_1_2]: خُلُ حَيَاةِ الْبَنَّاءِ الْمُغَرَّبِ مِنَ التَّفَاؤُلِ وَالأَمَلِ.
[CELL_1_3]: لا يَزْدَهِي: لا، حَرْفُ نَفْي. يَزْدَهِي: فِعْلَ مُصَارِ مَرْفُوعٌ. قَبَسٌ: فَاعِلَ مَرْفُوعُ. إِلَّا: أداةُ حَصْرٍ. تَوَلَّتْ: فعل ماض، مبني على الفَتْحَةِ المُقَدَّرَةِ على الأَلِفِ المَحْذُوفة؛ لا تصالِهِ بتاءِ التَّأنيث السَّاكِنَةِ. والنَّاءُ، حَرْفُ تَأْني لا مُحَلَّ لَهُ مِنَ الإِعرابِ. طَمْسَهُ: مَفْعُولُ بِهِ مَنْصُوب، وعلامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَةُ، والهاء، ضَمِيرٌ مُتَّصِلِّ مَبْنِي على الضَّمَّةِ فِي مَحَلَ جَرٍّ، مُضاف إليه. التوب: فَاعِلْ مَرْفُوعُ.

=== BLOCK 14: Parsing Rules 3 ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: الجمل
[IRAB_ANALYSIS]: جملة )لا يَزْدَهِي في لَيْلِهِ قَبَسٌ(: استئنافية، لا محل لها مِنَ الإعراب. جملة )تَوَلَّتْ طَمْسَهُ التوب(: في محل نَصْبٍ، حال [الجملَةُ بَعْدَ حَرْفِ الحَصْرِ حَالِيَّةٌ].

=== BLOCK 15: Poem 4 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]:
[RIGHT_HEMISTICH]: صفرَتْ مِنَ الأصحاب راحته
[LEFT_HEMISTICH]: لَمْ يُجْدِهِ سَعْي ولا طلب

=== BLOCK 16: Explanation for Poem 4 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الشرح
Content: زاد معاناة البناءِ تَفَرُّقُ الأَصْدِقَاءِ مِنْ حَوْلِهِ، وابتعادهم عَنْهُ، فَكُلما سعى وَجَدَّ فِي طَلَبِهِم عَادَ صِفْرَ اليَدَيْن،َ وَبَاءَتْ جُهُودُهُ بالفَشَلِ.

=== BLOCK 17: Core Matrix 4 (Summary) ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: الفكرة
[HEADER_2]: الإعراب
[HEADER_3]: الإعراب (تتمة)
[CELL_1_1]: افتقارُ البَنَّاءِ المُغَرَّبِ إلى الأَصْحاب.
[CELL_1_2]: صفرَتْ: فِعل ماض مَبْنِي على الفَنْحَةِ الظَّاهِرَةِ؛ لاتِصَالِهِ بِنَاءِ التَّأْنِيثِ السَّاكِنَةِ. والنَّاءُ، حَرْفُ تَأْني لا مَحَلَ لَهُ مِنَ الإعراب. راحته: فَاعِلَ مَرْفُوع، وعلامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ، والهاء، ضَمِيرٌ مُتَصِلٌ مَبْنِي على الضَّمَّةِ في محَلَ جَةٍ، مُضاف إليهِ.
[CELL_1_3]: لَمْ يُجْدِهِ: لَمْ، حَرْفٌ جازم. يُجْدِه،ِ فَعْلِّ مُصَارِعٌ مَجْزُوم، وعلامَةُ جَزْمِهِ حَذْفُ حَرْفِ العِلَّةِ. والهاء، ضَمِيرٌ مُتَّصِلِّ مَبْنِي على الكَسْرَةِ فِي مَحَلِّ نَصْبٍ، مَفْعُولُ بِهِ. سَعْي: فَاعِلَ مَرْفُوع. ولا طَلَبُ: الواو، حَرْفُ عَطْف. لا، زائِدَةً لِتَوْكِيدِ النَّفْي. طَلَبُ، اسمٌ مَعْطُوفٌ مَرْفُوع.

=== BLOCK 18: Parsing Rules 4 ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: الجمل
[IRAB_ANALYSIS]: جملة )صَفُرَتْ مِنَ الأَصحاب راحته(: استئنافية، لا محل لها مِنَ الإعراب. جملة )لَمْ يُجْدِهِ سَعْي(: استئنافية، لا مَحَلَّ لها مِنَ الإعراب.

=== BLOCK 19: Poem 5 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]:
[RIGHT_HEMISTICH]: يَنْبُو بِهِ فِي اللَّيْلِ مَضْجَعُهُ
[LEFT_HEMISTICH]: وَيَشوكُهُ الحرمان والنصب ه

=== BLOCK 20: Explanation for Poem 5 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الشرح
Content: إِنَّ هذا الكادح الشَّقِيَ لَا يَهْنَا بِالرَّاحَةِ حَتَّى فِي خَظَاتِ هُجُوعِهِ، فَعِندما يَأْوِي إلى فراشِهِ يَمْضِي لَيْلَهُ مُتَقَلَبًا لَا يَطْمَئِنُ بِهِ مَضْجَعٌ ، ولا يَسْتَقِر في فراش، حِيثُ يَخِرُهُ الْحِرْمَانُ وتَلْسَعُهُ الحَاجَةُ، ويُؤْلِمُهُ التَّعَبُ.

=== BLOCK 21: Idea (Warning for orange color balance) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[CONTENT]: الفِكْرة: أَرَقُ البَنَّاءِ الْمُغَرَّبِ بِسَبَبِ الحرمان والتعب.

=== BLOCK 22: Core Matrix 5 (Summary) ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: المفردات
[HEADER_2]: الإعراب
[CELL_1_1]: ينبو: تَبَا جَنْبُهُ عن الفراش: لم يطمئن به ولم يستقر فيه. النصب: التعب.
[CELL_1_2]: يَنْبُو: فِعْلِّ مُضَارِعٌ مَرْفُوعٌ. مَضْجَعُهُ: فَاعِلَ مَرْفُوعٌ.

--- END STREAM ---