# **SESSION 123**

[TASK DEFINITION]
Objective: Implement page 123.
File: `pages/page_123.html` (Note: Use the exact page number.)
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
[LESSON_NUMBER]: 123
[CHAPTER_TITLE]: page 123
[CATEGORY_HEADER]: 123
[SECTION_HEADER]: 123
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Continuation of I'rab (Part 2) ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[UNIQUE_ID]: b90518
[BLOCK_TITLE]: إِعْرَابُ الْمَقْطَعِ الثَّانِي
[CONTENT]:
وَسُكِّنَ لِلضَّرُورَةِ الشِّعْرِيَّةِ. وَالشَّيْخُ: الْوَاوُ، حَرْفُ اسْتِئْنَافٍ الشَّيْخُ، مُبْتَدَأٌ مَرْفُوعٌ كَابْنَتِهِ: الْكَافُ، حَرْفُ جَرٍّ. ابْنَتِهِ: اسْمٌ مَجْرُورٌ، وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ الظَّاهِرَةُ. وَالْهَاءُ، ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الْكَسْرَةِ فِي مَحَلِّ جَرٍّ، مُضَافٌ إِلَيْهِ. وَيَتْلُو: الْوَاوُ، حَرْفُ عَطْفٍ يَتْلُو، فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الْمُقَدَّرَةُ عَلَى الْوَاوِ، مَنَعَ ظُهُورَهَا الثِّقَلُ هَمْسًا: حَالٌ مَنْصُوبَةٌ سُورَةً: مَفْعُولٌ بِهِ مَنْصُوبٌ، وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ. وَسُكِّنَ لِلضَّرُورَةِ الشِّعْرِيَّةِ. وَبِلَهْجَةٍ: الْوَاوُ، حَرْفُ اسْتِئْنَافٍ وَالْبَاءُ، حَرْفُ جَرٍّ. لَهْجَةٍ، اسْمٌ مَجْرُورٌ كَالْحُلْمِ: الْكَافُ حَرْفُ جَرٍّ. الْحُلْمِ، اسْمٌ مَجْرُورٌ.

=== BLOCK 3: I'rab Details (Part 2) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b90519
[WORD_1]: عَيْنَا
[DETAILS_1]: مُبْتَدَأٌ مَرْفُوعٌ، وَعَلَامَةُ رَفْعِهِ الْأَلِفُ لِأَنَّهُ مُثَنَّى وَحُذِفَتِ النُّونُ لِلْإِضَافَةِ
[UNIQUE_ID_2]: b90520
[WORD_2]: حَبِيبَتِي
[DETAILS_2]: مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ الظَّاهِرَةُ وَالْيَاءُ، ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ، مُضَافٌ إِلَيْهِ

=== BLOCK 4: I'rab Details (Part 2) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b90521
[WORD_1]: الصَّغِيرَةِ
[DETAILS_1]: صِفَةٌ مَجْرُورَةٌ، وَعَلَامَةُ جَرِّهَا الْكَسْرَةُ الظَّاهِرَةُ. وَسُكِّنَتْ لِلضَّرُورَةِ الشِّعْرِيَّةِ.
[UNIQUE_ID_2]: b90522
[WORD_2]: يَا جُنُودُ
[DETAILS_2]: يَا، حَرْفُ نِدَاءِ جُنُودُ، مُنَادَى نَكِرَةٌ مَقْصُودَةٌ، مَبْنِيٌّ عَلَى الضَّمَّةِ، فِي مَحَلِّ نَصْبٍ عَلَى النِّدَاءِ.

=== BLOCK 5: I'rab Details (Part 2) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b90523
[WORD_1]: وَوَجْهُهَا
[DETAILS_1]: الْوَاوُ، حَرْفُ عَطْفٍ وَجْهُهَا، مُبْتَدَأٌ مَرْفُوعٌ، وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ. وَهَا، ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ، مُضَافٌ إِلَيْهِ
[UNIQUE_ID_2]: b90524
[WORD_2]: الْقَمْحِيُّ
[DETAILS_2]: صِفَةٌ مَرْفُوعَةٌ، وَعَلَامَةُ رَفْعِهَا الضَّمَّةُ الظَّاهِرَةُ

=== BLOCK 6: I'rab Details (Part 2) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b90525
[WORD_1]: لِي
[DETAILS_1]: اللَّامُ، حَرْفُ جَرٍّ. وَالْيَاءُ، ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِحَرْفِ الْجَرِّ. مُتَعَلِّقَانِ بِخَبَرٍ مَحْذُوفٍ.
[UNIQUE_ID_2]: b90526
[WORD_2]: لَا تَقْتُلُوهَا
[DETAILS_2]: لَا، حَرْفٌ جَازِمٌ تَقْتُلُوهَا، فِعْلٌ مُضَارِعٌ مَجْزُومٌ، وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ. وَالْوَاوُ، ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ، فَاعِلٌ. وَهَا، ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مَفْعُولٌ بِهِ.

=== BLOCK 7: I'rab Details (Part 2) ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b90527
[TARGET_WORD]: وَاقْتُلُونِي
[IRAB_ANALYSIS]: الْوَاوُ، حَرْفُ عَطْفٍ اقْتُلُونِي، فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، لِأَنَّ مُضَارِعَهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ. وَالْوَاوُ، ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ، فَاعِلٌ وَالنُّونُ، حَرْفُ وِقَايَةٍ. وَالْيَاءُ، ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مَفْعُولٌ بِهِ

=== BLOCK 8: Sentence Parsing ===
(Component: TEMPLATE_C_TABLE.html)
[UNIQUE_ID]: b90528
[HEADER_1]: الجملة
[HEADER_2]: إعرابها
[HEADER_3]: محلها
[CELL_1]: جُمْلَةُ (أَمَرَ بِإِطْلَاقِ الرَّصَاصِ)
[CELL_2]: استئنافية
[CELL_3]: لا محل لها مِنَ الإعراب.
[CELL_4]: جُمْلَةُ (يَجْتَازُ)
[CELL_5]: صِلَةُ المَوْسُولِ
[CELL_6]: لا محل لها مِنَ الإعراب
[CELL_7]: جُمْلَةُ (هَذَا الحِسْرُ مِقْصَلَةُ الذي ما زالَ يَحْلُمُ)
[CELL_8]: استئنافية
[CELL_9]: لا محل لها من الإعراب
[CELL_10]: جملة (مَا زَالَ يَحْلُمُ)
[CELL_11]: صِلَةُ المَوْسُولِ
[CELL_12]: لا مَحَلَّ لَهَا مِنَ الإعراب.
[CELL_13]: جُمْلَةُ (يَحْلُمُ)
[CELL_14]: خَبَرِيَّةٌ
[CELL_15]: مَحَلُّهَا النَّصْبُ
[CELL_16]: جُمْلَةُ (الطَّلقةُ الأُولَى أَزَاحَتْ)
[CELL_17]: استئنافية
[CELL_18]: لا مَحَلَّ لها مِنَ الإعراب.
[CELL_19]: جُمْلَةُ (أَرَاحَتْ)
[CELL_20]: خَبَرِيَّةٌ
[CELL_21]: مَحَلُّهَا الرَّفْعُ.
[CELL_22]: جملة (الطلقةُ الأُخْرَى أَصَابَتْ)
[CELL_23]: مَعْطُوفَةٌ
[CELL_24]: لَا مَحَلَّ لها مِنَ الإعراب
[CELL_25]: جُمْلَةُ (أَصَابَتْ)
[CELL_26]: خَبَرِيَّةٌ
[CELL_27]: مَحَلَّهَا الرَّفْعُ.
[CELL_28]: جملة (الشيخ يَأْخُذُ)
[CELL_29]: استئنافية
[CELL_30]: لا محل لها من الإعراب
[CELL_31]: جُمْلَةُ (يَأْخُذُ)
[CELL_32]: خَبَرِيَّةٌ
[CELL_33]: مَحَلُّها الرفع.
[CELL_34]: جُمْلَةُ (يَتْلُو)
[CELL_35]: مَعْطُوفَةٌ
[CELL_36]: مَحَلُّهَا الرَّفْعُ
[CELL_37]: جُمْلَةُ (قَالَ)
[CELL_38]: خَبَرِيَّةٌ
[CELL_39]: مَحَلَّهَا النَّصْبُ.
[CELL_40]: جملة (عَيْنَا حبيبتي الصغيرة لي يا جنود، ووَجْهُهَا القَمْحِيُّ لِي لا تَقْتُلُوهَا وَاقْتُلُونِي)
[CELL_41]: مَقُولُ القَوْلِ
[CELL_42]: مَفْعُولُ بِهِ.
[CELL_43]: جُمْلَةُ (عَيْنَا حبيبتي الصغيرة لي)
[CELL_44]: ابتدائية
[CELL_45]: لا محل لها مِنَ الإعراب
[CELL_46]: جملة (وجهها القَمْحِيُّ لِي)
[CELL_47]: مَعْطُوفَةٌ
[CELL_48]: لَا مَحَل لها مِنَ الإعراب.
[CELL_49]: جملة (لا تَقْتُلوها)
[CELL_50]: استئنافية
[CELL_51]: لا محل لها مِنَ الإعراب .
[CELL_52]: جُمْلَةُ (اقْتُلُونِي)
[CELL_53]: مَعْطُوفَةٌ
[CELL_54]: لا محل لها مِنَ الإعراب.

=== BLOCK 9: إعراب المقطع الثالث ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b90529
[BLOCK_TITLE]: إِعْرَابُ الْمَقْطَعِ الثَّالِثِ
[CONTENT]:
وَبِرَغْمِ الْوَاوُ، حَرْفُ اسْتِئْنَافٍ الْبَاءُ، حَرْفُ جَرٍّ. رَغْمِ اسْمٌ مَجْرُورٌ أَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ الْقَتْلَ: اسْمُ (أَنَّ). كَالتَّدْخِينِ: الْكَافُ، حَرْفُ جَرٍّ. التَّدْخِينِ، اسْمٌ مَجْرُورٌ، وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ الظَّاهِرَةُ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِخَبَرٍ مَحْذُوفٍ. وَالْمَصْدَرُ الْمُؤَوَّلُ (أَنَّ الْقَتْلَ التَّدْخِينِ)، فِي مَحَلِّ جَرٍّ، مُضَافٌ إِلَيْهِ.

=== BLOCK 10: I'rab Details (Part 3) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b90530
[WORD_1]: لَكِنَّ
[DETAILS_1]: حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ
[UNIQUE_ID_2]: b90531
[WORD_2]: الْجُنُودَ
[DETAILS_2]: اسْمُ لَكِنَّ مَنْصُوبٌ

=== BLOCK 11: I'rab Details (Part 3) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b90532
[WORD_1]: الطَّيِّبِينَ
[DETAILS_1]: صِفَةٌ مَنْصُوبَةٌ، وَعَلَامَةُ نَصْبِهَا الْيَاءُ؛ لِأَنَّهَا جَمْعُ مُذَكَّرٍ سَالِمٌ. وَالنُّونُ، عِوَضٌ عَنِ التَّنْوِينِ فِي الِاسْمِ الْمُفْرَدِ
[UNIQUE_ID_2]: b90533
[WORD_2]: الطَّالِعِينَ
[DETAILS_2]: صِفَةٌ مَنْصُوبَةٌ، وَعَلَامَةُ نَصْبِهَا الْيَاءُ؛ لِأَنَّهَا جَمْعُ مُذَكَّرٍ سَالِمٌ وَالتُّونُ، عِوَضٌ عَنِ التَّنْوِينِ فِي الِاسْمِ الْمُفْرَدِ

=== BLOCK 12: I'rab Details (Part 3) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b90534
[WORD_1]: دَفْتَرِ
[DETAILS_1]: مُضَافٌ إِلَيْهِ مَجْرُورٌ
[UNIQUE_ID_2]: b90535
[WORD_2]: قَذَفَتْهُ
[DETAILS_2]: فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحَةِ؛ لِاتِّصَالِهِ بِتَاءِ التَّأْنِيثِ السَّاكِنَةِ. وَالتَّاءُ، حَرْفُ تَأْنِيثٍ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ وَالْهَاءُ، ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمَّةِ فِي مَحَلِّ نَصْبٍ، مَفْعُولٌ بِهِ

=== BLOCK 13: I'rab Details (Part 3) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b90536
[WORD_1]: أَمْعَاءُ
[DETAILS_1]: فَاعِلٌ مَرْفُوعٌ
[UNIQUE_ID_2]: b90537
[WORD_2]: السِّنِينَ
[DETAILS_2]: مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَعَلَامَةُ جَرِّهِ الْيَاءُ؛ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.

=== BLOCK 14: I'rab Details (Part 3) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b90538
[WORD_1]: لَمْ يَقْتُلُوا
[DETAILS_1]: لَمْ حَرْفٌ جَازِمٌ يَقْتُلُوا فِعْلٌ مُضَارِعٌ مَجْزُومٌ، وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ. وَالْوَاوُ، ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ، فِي مَحَلِّ رَفْعٍ، فَاعِلٌ وَالْأَلِفُ حَرْفُ تَفْرِيقٍ
[UNIQUE_ID_2]: b90539
[WORD_2]: الِاثْنَيْنِ
[DETAILS_2]: مَفْعُولٌ بِهِ مَنْصُوبٌ، وَعَلَامَةُ نَصْبِهِ الْيَاءُ لِأَنَّهُ مُلْحَقٌ بِالْمُثَنَّى

=== BLOCK 15: I'rab Details (Part 3) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b90540
[WORD_1]: كَانَ
[DETAILS_1]: فِعْلٌ مَاضٍ نَاقِصٌ، مَبْنِيٌّ عَلَى الْفَتْحَةِ الظَّاهِرَةِ
[UNIQUE_ID_2]: b90541
[WORD_2]: الشَّيْخُ
[DETAILS_2]: اسْمُ (كَانَ) مَرْفُوعٌ

=== BLOCK 16: I'rab Details (Part 3) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b90542
[WORD_1]: النَّهْرِ
[DETAILS_1]: مُضَافٌ إِلَيْهِ مَجْرُورٌ.
[UNIQUE_ID_2]: b90543
[WORD_2]: وَالْبِنْتُ
[DETAILS_2]: الْوَاوُ، حَرْفُ عَطْفٍ . الْبِنْتُ، مُبْتَدَأٌ مَرْفُوعٌ

=== BLOCK 17: I'rab Details (Part 3) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b90544
[WORD_1]: الَّتِي
[DETAILS_1]: اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ، صِفَةٌ،
[UNIQUE_ID_2]: b90545
[WORD_2]: صَارَتْ
[DETAILS_2]: فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحَةِ لِاتِّصَالِهِ بِتَاءِ التَّأْنِيثِ السَّاكِنَةِ. وَالتَّاءُ، حَرْفُ تَأْنِيثٍ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ.

=== BLOCK 18: I'rab Details (Part 3) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b90546
[WORD_1]: يَتِيمَةً
[DETAILS_1]: خَبَرُ (صَارَ) مَنْصُوبٌ، وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ. وَسُكِّنَ لِلضَّرُورَةِ الشِّعْرِيَّةِ.
[UNIQUE_ID_2]: b90547
[WORD_2]: كَانَتْ
[DETAILS_2]: فِعْلٌ مَاضٍ نَاقِصٌ، مَبْنِيٌّ عَلَى الْفَتْحَةِ؛ لِاتِّصَالِهِ بِتَاءِ التَّأْنِيثِ السَّاكِنَةِ وَالتَّاءُ، حَرْفُ تَأْنِيثٍ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ.

=== BLOCK 19: I'rab Details (Part 3) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b90548
[WORD_1]: مُمَزَّقَةَ
[DETAILS_1]: خَبَرُ (كَانَ) مَنْصُوبٌ
[UNIQUE_ID_2]: b90549
[WORD_2]: الثِّيَابِ
[DETAILS_2]: مُضَافٌ إِلَيْهِ مَجْرُورٌ

=== BLOCK 20: I'rab Details (Part 3) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b90550
[WORD_1]: عِطْرُ
[DETAILS_1]: فَاعِلٌ مَرْفُوعٌ
[UNIQUE_ID_2]: b90551
[WORD_2]: الْيَاسَمِينِ
[DETAILS_2]: مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ الظَّاهِرَةُ. وَسُكِّنَ لِلضَّرُورَةِ الشِّعْرِيَّةِ

=== BLOCK 21: Sentence Parsing (Part 3) ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
[UNIQUE_ID]: b90552
[BLOCK_TITLE]: إعراب الجمل (يتبع)
[CONTENT]:
جُمْلَةُ (لَكِنَّ الْجُنُودَ ... لَمْ يَقْتُلُوا) اسْتِئْنَافِيَّةٌ، لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ جُمْلَةُ (لَمْ يَقْتُلُوا) : خَبَرِيَّةٌ، مَحَلُّهَا الرَّفْعُ جُمْلَةُ (قَذَفَتْهُ أَمْعَاءُ السِّنِينَ): صِفَةٌ، مَحَلُّهَا الْجَرُّ. جُمْلَةُ (كَانَ الشَّيْخُ يَسْقُطُ) اسْتِئْنَافِيَّةٌ، لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ . جُمْلَةُ (يَسْقُطُ) : خَبَرِيَّةٌ، مَحَلُّهَا النَّصْبُ. جُمْلَةُ (الْبِنْتُ ... كَانَتْ)

--- END STREAM ---
