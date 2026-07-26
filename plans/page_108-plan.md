# **SESSION 108**

[TASK DEFINITION]
Objective: Implement page 108.
File: `pages/page_108.html`
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
[LESSON_NUMBER]: 108
[CHAPTER_TITLE]: page 108
[CATEGORY_HEADER]: 108
[SECTION_HEADER]: 108
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Cut Content Part 2 ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[BLOCK_TITLE]: الإعراب
[CONTENT]:
بِهِ مَنْصُوبٌ. جُمْلَةٌ (تِيهي): استئنافية، لا محل لها مِنَ الإعراب. جملَةُ (اسْحَبِي): مَعْطُوفَةٌ، لَا مَحَلَّ لها مِنَ الإعراب.

=== BLOCK 3: Poem 1 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: الشاهد الشعري
[POET_NAME]:
[RIGHT_HEMISTICH]: لَنْ تَرَيْ حَفْنَةَ رَمْلٍ فَوْقَها
[LEFT_HEMISTICH]: لَمْ تُعَطَّرْ بِدِما حُرٍّ أبي

=== BLOCK 4: Definitions and Explanation ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: المفردات
[CONTENT]:
حُرٍّ: صِفَةٌ مُشَبَّهَةٌ باسم الفاعل، فعلها: حَرَّ. أبي: صِفَةٌ مُشَبَّهَةٌ باسم الفاعل، فعلها: أَبِيَ.

=== BLOCK 5: Definitions and Explanation ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: الشرح
[CONTENT]:
<span class="text-accent">لَنْ تَجِدِي فِي ثَرَى البِلَادِ ذَرَّةً لَا يَفُوحُ مِنْهَا عَبِيرٌ مِنْ دَمِ شَهِيدٍ عَزِيزٍ.</span>

=== BLOCK 6: Core Matrix 1 ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: الفكرة
[HEADER_2]: الشعور
[HEADER_3]: التراكيب والمثال
[CELL_1]: تَمْجِيدُ التَّضْحِيَاتِ الَّتِي قَدَّمَهَا الشَّعْبُ السُّورِيُّ لِنَيْلِ اسْتِقْلَالِهِ، وَالِاعْتِزَازُ بِهَا (تَمْجِيدِ الشَّهَادَةِ وَالشُّهَدَاءِ).
[CELL_2]: اعتزاز وافتخار. الأداة: التراكيب.
[CELL_3]: لَنْ تَرَيْ حَفْنَةَ رَمْلٍ فَوْقَهَا لَمْ تُعَطَّرْ بِدِما حُرٍّ.

=== BLOCK 7: Benefit Box ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[TITLE]: الأساليب
[CONTENT]:
<span class="highlight-blue">لَنْ</span> تَرَيِ حَفْنَةَ رَمْلٍ: أسلوب نفي. الأداة: <span class="highlight-blue">لَنْ</span>. أفادت نفي وقوع الفعل المضارع في الزَّمَنِ المستقبل. ثُمَّ تُعَطَّرْ: أسلوب نفي. الأداة: <span class="highlight-blue">لَمْ</span>. أفادت نفي وقوع الفعل المضارع في الزمن الماضي.

=== BLOCK 8: Irab Header ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: الإعراب
[CONTENT]:

=== BLOCK 9: Irab Row 1 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: لَنْ تَرَي
[DETAILS_1]: لَنْ: حَرْفٌ نَاصِبٌ. تَرَي: فِعْلٌ مُضَارِعٌ مَنْصُوبٌ، وعلامَةُ نَصْبِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الخَمْسَةِ. والياء، ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ على السُّكُونِ فِي مَحَلِّ رَفْعٍ، فَاعِلٌ.
[WORD_2]: حَفْنَةَ
[DETAILS_2]: مَفْعُولٌ بِهِ مَنْصُوبٌ.

=== BLOCK 10: Irab Row 2 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: رَمْلٍ
[DETAILS_1]: مُضَافٌ إليهِ مَجْرُورٌ.
[WORD_2]: فوقها
[DETAILS_2]: مَفْعُولٌ فِيهِ ظَرْفُ مَكَانٍ مَنْصُوبٌ.

=== BLOCK 11: Irab Row 3 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: لَمْ تُعَطَّرْ
[DETAILS_1]: لَمْ: حَرْفٌ جازمٌ. تُعَطَّرْ: فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلمَجْهُولِ مَجْزُومٌ، وعلامةُ جَزْمِهِ السُّكُونُ.
[WORD_2]: بِدِما
[DETAILS_2]: الباء: حَرْفُ جَرٍّ. دِما: اسمٌ مَجْرُورٌ، وعلامَةُ جَرِّهِ الكَسْرَةُ المُقَدَّرَةُ على الأَلِفِ، مَنَعَ ظُهُورَهَا التَّعَذُّرُ (عُومِلَ المَمْدُودُ مُعَامَلَةَ الْمَقْصُورِ لِلضَّرُورَةِ الشِّعْرِيَّةِ).

=== BLOCK 12: Irab Row 4 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: حُرٍّ
[DETAILS_1]: صِفَةٌ مَجْرُورَةٌ وعلامَةُ جَرِّهَا الكَسْرَةُ الظَّاهِرَةُ، وَسُكِّنَ لِلضَّرُورَةِ الشِّعْرِيَّةِ.
[WORD_2]: أبي
[DETAILS_2]: صِفَةٌ مَجْرُورَةٌ وعلامَةُ جَرِّهَا الكَسْرَةُ المُقَدَّرَةُ على الأَلِفِ، مَنَعَ ظُهُورَهَا التَّعَذُّرُ.

=== BLOCK 13: Irab Row 5 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: جملَةُ (لَمْ تَعَطَّرْ)
[DETAILS_1]: صِفَةٌ، مَحَلَّهَا النَّصْبُ.
[WORD_2]: جُمْلَةُ (لَنْ تَرَي)
[DETAILS_2]: استئنافية، لا محل لها من الإعراب.

=== BLOCK 14: Poem 2 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: الشاهد الشعري
[POET_NAME]:
[RIGHT_HEMISTICH]: دَرَجَ البَغْيُ عَلَيْهَا حِقْبَةً
[LEFT_HEMISTICH]: وَهَوى دُونَ بُلوغِ الأَرَبِ

=== BLOCK 15: Definitions and Explanation 2 ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: المفردات والشرح
[CONTENT]:
<span class="text-accent">المفردات:</span> دَرَجَ: مَشَى. البَغْيُ: العُدْوَانُ وَالظُّلْمُ. حِقْبَةً: مُدَّةً (الجَمْعُ: حُقُبٌ وَحُقُوبٌ). هَوَى: سَقَطَ وَهَلَكَ. الأَرَبِ: البُغْيَةُ وَالْأُمْنِيَةُ.
<span class="text-accent">الشرح:</span> مَشَى الظُّلْمُ فِي رُبُوعِ البِلَادِ مُدَّةً مِنَ الزَّمَنِ، وَهَلَكَ قَبْلَ أَنْ يُحَقِّقَ غَايَتَهُ.

=== BLOCK 16: Core Matrix 2 ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: الفكرة
[HEADER_2]: الشعور والأداة
[HEADER_3]: البلاغة
[CELL_1]: تَصْوِيرُ هَزِيمَةِ المُسْتَعْمِرِ وَخَيْبَتِهِ فِي تَوْطِيدِ وُجُودِهِ على أَرْضِنَا (السُّخْرِيَةُ مِنَ المُسْتَعْمِرِ وَالشَّمَاتَةُ بِهَزِيمَتِهِ).
[CELL_2]: الشُّعُورُ: الفَرَحُ. الأداة: التراكيب. المثال: هَوَى دُونَ بُلُوغِ الأَرَبِ.
[CELL_3]: (دَرَجَ البَغْيُ): استعارَةٌ مَكْنِيَّةٌ.

=== BLOCK 17: Irab Header 2 ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: الإعراب
[CONTENT]:

=== BLOCK 18: Irab Row 6 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: البَغْيُ
[DETAILS_1]: فَاعِلٌ مَرْفُوعٌ، وعلامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ.
[WORD_2]: حِقْبَةً
[DETAILS_2]: مَفْعُولٌ فِيهِ ظَرْفُ زَمَانٍ مَنْصُوبٌ.

=== BLOCK 19: Irab Row 7 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: دُوْنَ
[DETAILS_1]: مَفْعُولٌ فِيهِ ظَرْفُ زَمَانٍ مَنْصُوبٌ مُتَعَلِّقٌ بِالْفِعْلِ (هَوى).
[WORD_2]: بُلوغِ الأَرَبِ
[DETAILS_2]: مُضَافٌ إِلَيْهِ مَجْرُورٌ.

=== BLOCK 20: Irab Row 8 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: جُمْلَهُ (دَرَجَ البَغْيُ)
[DETAILS_1]: استئنافية، لا محل لها مِنَ الإعراب.
[WORD_2]: جُمْلَةُ (هَوَى)
[DETAILS_2]: مَعْطُوفَةٌ، لَا مَحَلَّ لها مِنَ الإعراب.

=== BLOCK 21: Poem 3 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: الشاهد الشعري
[POET_NAME]:
[RIGHT_HEMISTICH]: وارْتَمَى كِبْرُ اللّيالي دُونَهَا
[LEFT_HEMISTICH]: لَيِّنَ النّابِ، كَلِيْلَ المِخْلَبِ

=== BLOCK 22: Definitions and Explanation 3 ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: المفردات والشرح
[CONTENT]:
<span class="text-accent">المفردات:</span> كِبْرُ: العَظَمَةُ وَالتَّجَبُّرُ. لَيِّنَ: سَهْلٌ، مُنْقَادٌ (الجَمْعُ: أَلْيِنَاءُ). كَلِيْلَ: ضَعِيفٌ. المِخْلَبِ: اسم آلة، فعله: خَلَبَ.
<span class="text-accent">الشرح:</span> وَخَضَعَ لِلْبِلَادِ جَبَرُوتُ الزَّمَانِ مُنْهَكَ القُوَى، إِذْ تَهَاوَى أَمَامَ صُمُودِ أَبْنَائِنَا جَبَرُوتُ المُسْتَعْمِرِينَ بَعْدَ أَنْ أُنْهِكَتْ قُوَاهُمْ.

=== BLOCK 23: Core Matrix 3 ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: الفكرة
[HEADER_2]: الشعور
[HEADER_3]: التراكيب والمثال
[CELL_1]: تَصْوِيرُ هَزِيمَةِ المُسْتَعْمِرِ وَخَيْبَتِهِ فِي تَوْطِيدِ وُجُودِهِ على أَرْضِنَا (السُّخْرِيَةُ مِنَ المُسْتَعْمِرِ وَالشَّمَاتَةُ بِهَزِيمَتِهِ).
[CELL_2]: الشُّعُورُ: الفَرَحُ. الأداة: التراكيب.
[CELL_3]: ارْتَمَى كِبْرُ اللّيالي.

=== BLOCK 24: Irab Header 3 ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: الإعراب
[CONTENT]:

=== BLOCK 25: Irab Row 9 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: كِبْرُ
[DETAILS_1]: فَاعِلٌ مَرْفُوعٌ.
[WORD_2]: اللّيالي
[DETAILS_2]: مُضَافٌ إِلَيْهِ مَجْرُورٌ، وعلامَةُ جَرِّهِ الكَسْرَةُ المُقَدَّرَةُ على الياء، مَنَعَ ظُهُورَهَا الثِّقَلُ.

=== BLOCK 26: Irab Row 10 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: دُونَهَا
[DETAILS_1]: مَفْعُولٌ فِيهِ ظَرْفُ مَكَانٍ مَنْصُوبٌ، وعلامة نَصْبِهِ الفَتْحَةُ الظَّاهِرَةُ. وها: ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ على السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إليهِ.
[WORD_2]: لَيِّنَ، كَلِيْلَ
[DETAILS_2]: حَالٌ مَنْصُوبَةٌ.

=== BLOCK 27: Irab Row 11 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: النّابِ، المِخْلَبِ
[DETAILS_1]: مُضَافٌ إِلَيْهِ مَجْرُورٌ.
[WORD_2]: جُمْلَهُ (ارْتَمَى)
[DETAILS_2]: مَعْطُوفَةٌ، لا محل لها مِنَ الإعراب.

=== BLOCK 28: Poem 4 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: الشاهد الشعري
[POET_NAME]:
[RIGHT_HEMISTICH]: لا يموتُ الحَقُّ مَهْمَا لَطَمَتْ
[LEFT_HEMISTICH]: عارضيْهِ قَبْضَةُ الْمُغْتَصِبِ

=== BLOCK 29: Definitions and Explanation 4 ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: المفردات، الشرح والبلاغة
[CONTENT]:
<span class="text-accent">المفردات:</span> عارضيه: المفرد: عَارِضٌ وَهُوَ جَانِبُ الوَجْهِ أَوْ صَفْحَةُ الخَدِّ.
<span class="text-accent">الشرح:</span> كِفَّةُ الحَقِّ هِيَ الرَّاجِحَةُ دَائِماً فَهُوَ الغَالِبُ مَهْمَا حَاوَلَ المُسْتَعْمِرُ تَغْطِيَتَهُ وَطَمْسَهُ. الفكرة: ثَبَاتُ الحَقِّ فِي وَجْهِ المُغْتَصِبِ.
<span class="text-accent">البلاغة:</span> (الحَقُّ لَطَمَتْ عَارِضَيْهِ قَبْضَةُ الْمُغْتَصِبِ) استعارَةٌ مَكْنِيَّةٌ.

=== BLOCK 30: Irab Header 4 ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: الإعراب
[CONTENT]:

=== BLOCK 31: Irab Row 12 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: لا يموت
[DETAILS_1]: لا: حَرْفُ نَفي. يموت: فعل مُضَارِعٌ مَرْفُوعٌ.
[WORD_2]: الحقُّ
[DETAILS_2]: فَاعِلٌ مَرْفُوعٌ.

=== BLOCK 32: Irab Row 13 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: مَهْمَا
[DETAILS_1]: اسمُ شَرْطٍ جازم، مَبْنِيٌّ على السُّكُونِ، فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.
[WORD_2]: لَطَمَتْ
[DETAILS_2]: فِعْلٌ ماضٍ، مَبْنِيٌّ على الفَتْحَةِ؛ لاتِّصَالِهِ بِتَاءِ التَّأنيث السَّاكِنَةِ، وهو في محل جزم. والتَّاءُ: حَرْفُ تَأْنِيثٍ لَا مَحَلَّ لَهُ مِنَ الإِعراب.

=== BLOCK 33: Irab Row 14 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: عَارِضَيْهِ
[DETAILS_1]: مَفْعُولٌ بِهِ مَنْصُوبٌ، وعلامَةُ نَصْبِهِ اليَاءُ؛ لأَنَّهُ مُثَنَّى، وحُذِفَتِ النُّونُ لِلإِضَافَةِ. والهاء: ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ على الكَسْرَةِ في محل جر، مُضَافٌ إِلَيْهِ.
[WORD_2]: قَبْضَةُ
[DETAILS_2]: فَاعِلٌ مَرْفُوعٌ. الْمُغْتَصِبِ: مُضَافٌ إِلَيْهِ مَجْرُورٌ.

=== BLOCK 34: Irab Row 15 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: جملة (لا يَمُوتُ الحقُّ)
[DETAILS_1]: استئنافية، لا مَحَلَّ لها مِنَ الإعراب.
[WORD_2]: جُمْلَةُ (مَهْمَا لَطَمَتْ عَارِضَيْهِ قَبْضَةُ الْمُغْتَصِبِ)
[DETAILS_2]: استئنافية، لا محل لها مِنَ الإعراب.

=== BLOCK 35: Irab Single ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: جُمْلَةُ (لَطَمَتْ عَارِضَيْهِ قَبْضَةُ الْمُغْتَصِبِ)
[IRAB_ANALYSIS]: جُمْلَةُ الشَّرْطِ غَيْرِ الظَّرفي، لَا مَحَلَّ لها مِنَ الإِعراب.

=== BLOCK 36: Poem 5 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: الشاهد الشعري
[POET_NAME]:
[RIGHT_HEMISTICH]: وَتَهَادَى مَوْكِبًا في مَوْكِبٍ
[LEFT_HEMISTICH]: من هُنَا شَقَّ الهُدَى أَكْمَامَهُ

=== BLOCK 37: Definitions and Explanation 5 ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: المفردات والشرح
[CONTENT]:
<span class="text-accent">المفردات:</span> الهُدَى: الهِدَايَةُ وَالرَّشَادُ. أَكْمَامَهُ: أَغْطِيَتُهُ (المُفْرَدُ: كُمٌّ).
<span class="text-accent">الشرح:</span> مِنْ أَرْضِنَا بَزَغَ نُورُ الهِدَايَةِ وَالرَّشَادِ، وَفَوْقَ تُرَابِهَا تَقَاطَرَتْ جَحَافِلُ الفَاتِحِينَ تَتَدَاوَلُ نَشْرَ ضِيَائِهِ وَبَسْطَ وَهَجِهِ فِي كُلِّ الأَرْجَاءِ. الفكرة: الاعْتِزَازُ بِالْمَاضِي الْمَجِيدِ. الشعور: الاعْتِزَازُ وَالِافْتِخَارُ. الأداة: التَّرَاكِيبُ. المثال: مِنْ هُنَا شَقَّ الهُدَى أَكْمَامَهُ.

=== BLOCK 38: Irab Header 5 ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: الإعراب
[CONTENT]:

=== BLOCK 39: Irab Row 16 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: مِنْ هُنَا
[DETAILS_1]: مِنْ: حَرْفُ جَرٍّ. هُنَا: اسمُ إشارةٍ مبنيٌّ على السُّكُونِ في محلِّ جَرٍّ بِحَرْفِ الجَرِّ.
[WORD_2]: الهُدَى
[DETAILS_2]: فَاعِلٌ مَرْفُوعٌ.

=== BLOCK 40: Irab Row 17 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: أَكْمَامَهُ
[DETAILS_1]: مَفْعُولٌ بِهِ مَنْصُوبٌ.
[WORD_2]: وَتَهَادَى
[DETAILS_2]: الواو: حَرْفُ عَطْفٍ. تَهَادَى: فعلٌ ماضٍ، مَبْنِيٌّ على الفتحةِ المقدرةِ على الأَلِفِ، مَنَعَ ظُهُورَها التَعَذُّرُ.

=== BLOCK 41: Irab Row 18 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: مَوْكِبًا
[DETAILS_1]: حَالٌ مَنْصُوبَةٌ.
[WORD_2]: جُمْلَهُ (شَقَّ الهُدَى أَكْمَامَهُ)
[DETAILS_2]: استئنافية، لا محل لها مِنَ الإعراب.

=== BLOCK 42: Irab Single 2 ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: جُمْلَةُ (تَهَادَى)
[IRAB_ANALYSIS]: مَعْطُوفَةٌ، لا محل لها مِنَ الإعراب.

--- END STREAM ---
