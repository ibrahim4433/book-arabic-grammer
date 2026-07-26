# **SESSION 108**

[TASK DEFINITION]
Objective: Implement page 108.
File: `pages/page_108.html` (Note: Use the exact page number.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools. If it overflows, it is a catastrophic failure. Do NOT try to solve overflow by deleting text (Strict Typographer Rule). Solve it by choosing denser templates or omitting optional white-space.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`. Ensure exact visual continuity (same title, same classes).
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md` to identify the correct template to use for the continuation. Scan the raw text for the preceding keyword to determine the active template and apply the correct `_PART_2.html` wrapping. For this text, it continues "الإعراب" which maps to `TEMPLATE_C_IRAB.html`.
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
7. Templates: You are forbidden from inventing new HTML tags or classes or template elements. Replace any `<section>` tags from the templates with `<div>` tags (keep `<header>` for page headers as is).
8. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). The ID MUST be applied to the `<div>` tag that replaced the `<section>` tag. Use "Jules-workspace/id_manager.py" to generate or verify them.
9. **Self-Correction:** Run "Jules-workspace/lint_pages.py --one-page-mode pages/page_108.html" after creating html files. If it fails, you MUST fix the errors (usually inline styles or forbidden section tags) before submitting.
10. Do not summarize examples.
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: Wrap all content using `TEMPLATE_C_PAGE_WRAPPER.html`. The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal (use `.block-header.accent`).
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
15. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !

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

=== BLOCK 2: Cut Content (Irab Continuation) ===
(Component: TEMPLATE_CUT_BOX_PART_2.html wrapping TEMPLATE_C_IRAB.html)
Title: تابع الإعراب
Word 1: بِهِ
Details 1: مَنْصُوبٌ
Word 2: جُمْلَةٌ )تيهي(
Details 2: استئنافية، لا محل لها مِنَ الإعراب
Word 3: جملَةُ )اسْحَبِي(
Details 3: مَعْطُوفَة،ٌ لَا مَحَلَّ لها مِنَ الإعراب.

=== BLOCK 3: Poem Verse 1 ===
(Component: TEMPLATE_C_POEM.html)
Line 1 Hemistich 1: لَنْ تَرَى حَفْنَةَ رَمْلٍ فَوْقَها
Line 1 Hemistich 2: لم تُعَطَرْ بِدِما حُرٍّ أَبي

=== BLOCK 4: Analysis Verse 1 ===
(Component: TEMPLATE_C_TABLE.html)
Col 1: العنصر
Col 2: التفاصيل
Row 1 Col 1: المفردات
Row 1 Col 2: حر: صِفَةٌ مُشَبَّهَةٌ باسم الفاعل فعلها : حر. أَبي : صِفَةٌ مُشَبَّهَة باسم الفاعل فعلها أبي
Row 2 Col 1: الشرح
Row 2 Col 2: لن تجدي في تراب البلاد ذرة لا يفوح منها عبير من دم شهيد عزيز
Row 3 Col 1: الفكرة
Row 3 Col 2: تمجِيدُ التَّصْحِياتِ الَّتِي قَدَّمَهَا الشَّعْبُ السُّورِي لِنَيْلِ استقلاله، والاعتزاز بها )تَمْجِيدِ الشَّهَادِة والشهداء(
Row 4 Col 1: الشعور
Row 4 Col 2: اعتزاز وافتخار
Row 5 Col 1: الأداة التراكيب المثال
Row 5 Col 2: لَنْ تَرَى حَفْنَةَ رَمْلٍ فَوْقَهَا لَمْ تُعَطَّرْ بِدِما حُر.ِّ
Row 6 Col 1: الأساليب
Row 6 Col 2: لَنْ تَرَيِ حَفْنَةَ رمل: أسلوب نفي الأداة: لن أفادت نفي وقوع الفعل المضارع في الزَّمَن المستقبل. ثُمَّ تعطر : أسلوب نفي الأداة: لَمْ أفادت نفي وقوع الفعل المضارع في الزمن الماضي

=== BLOCK 5: Irab Verse 1 ===
(Component: TEMPLATE_C_IRAB.html)
Word 1: لَنْ
Details 1: حَرْفٌ نَاصِبٌ
Word 2: تَرَي
Details 2: فِعْلَ مُضَارِعٌ مَنْصُوب، وعلامَةُ نَصْبِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الخَمْسَة.ِ والياء، ضمير مُتَّصِلِّ مَبْنِي على السكون فِي مَحَلِّ رَفْع، فَاعِلٌ
Word 3: حَفْنَةَ
Details 3: مَفْعُولُ بِهِ مَنْصُوبٌ
Word 4: رَمْلٍ
Details 4: مُضَاف إليهِ مَجْرُور.ٌ
Word 5: فَوْقَها
Details 5: مَفْعُولٌ فِيهِ ظَرْفُ مَكَانِ مَنْصُوبُ
Word 6: لَمْ
Details 6: حَرْفٌ جازمٌ
Word 7: تُعَطَرْ
Details 7: فِعْلَ مُصَارِعٌ مَبْنِي لِلمَجْهُولِ مَجْرُوم، وعلامةُ جَزْمِهِ السُّكُونُ
Word 8: بِدِمَا
Details 8: الباء، حَرْفَ جَرٍ دِمَا، اسمٌ مَجْرُور، وعلامَةُ جَرَهِ الكَسْرَةُ المُقَدَّرَةُ على الأَلِف،ِ مَنَعَ ظُهُورَهَا التَّعَذُرُ عُومِلَ المَمْدُودُ مُعَامَلَةَ الْمَقْصُورِ لِلضَّرُورَةِ الشَّعْرِيَّة.ِ
Word 9: حُرٍّ
Details 9: مُضَاف إليهِ مَجْرُور.ٌ وعلامَةُ جَرَهِ الكَسْرَةُ الظَّاهِرَة،ُ
Word 10: أبي
Details 10: صِفَةً مَجْرُورَةً وعلامَةُ جَرَهَا الكَسْرَةُ المُقَدَّرَةُ وَسُكِّنَ للضرورة الشعْرِيَّة.ِ
Word 11: جُمْلَةً )لَنْ تَرَي(
Details 11: استئنافية، لا محل لها من الإعراب
Word 12: جملَةً )لَمْ تُعَطَّر(
Details 12: صِفَة،ٌ مَحَلَّهَا النَّصْب.ُ

=== BLOCK 6: Poem Verse 2 ===
(Component: TEMPLATE_C_POEM.html)
Line 1 Hemistich 1: دَرَجَ البَغْيُ عَلَيْهَا حِقْبَةً
Line 1 Hemistich 2: وَهَوى دُونَ بُلوغ الأرب

=== BLOCK 7: Analysis Verse 2 ===
(Component: TEMPLATE_C_BLOCK.html with `.block-header.accent`)
Title: دراسة البيت
Body:
المفردات: درج مشى البغي العدوان والظلم حقبة مدة الجمع: حقب وحقوب. هوى سقط وهلك الأرب: البغية والأمنية.
الشرح مشى الظلم في ربوع البلاد مدة من الزمن، وهلك قبل أن يحقق غايته.
الفكرة تصوير هَزِيمَةِ المُستَعْمِر وَخَيْبَتِهِ فِي تَوْطِيدِ وُجُودِه على أَرْضِنا )السُّخْرِيَةِ مِنَ المُسْتَعْمِر والشَّمَاتَةَ بِهَزِيمَتِهِ(.
الشُّعُور: الفرح
الأداة التراكيب المثال: هوى دُونَ بُلُوع الأرب.
البلاغة: )درج البغْي(: استعارَةُ مَكْنِيَّة

=== BLOCK 8: Irab Verse 2 ===
(Component: TEMPLATE_C_IRAB.html)
Word 1: البَغْي
Details 1: فَاعِلَ مَرْفُوع، وعلامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ
Word 2: حِقْبَةٌ
Details 2: مَفْعُولُ فِيهِ ظَرْفُ زَمَانٍ مَنْصُوبٌ
Word 3: دُوْنَ
Details 3: مَفْعُولٌ فِيهِ ظَرْفُ زَمَانٍ مَنْصُوبُ مُتَعَلَّقُ بِالْفِعْلِ )هَوى(.
Word 4: بلوغ
Details 4: مُضَافُ إِلِيهِ مَجْرُورٌ
Word 5: الأَرَبِ
Details 5: مُضَافُ إِلِيهِ مَجْرُورٌ
Word 6: جُمْلَهُ )دَرَجَ البَغْي(
Details 6: استئنافية، لا محل لها مِنَ الإعراب .
Word 7: يُمْلَةٌ )هوى(
Details 7: مَعْطُوفَة،ٌ لَا مَحَلَّ لها مِنَ الإعراب.

=== BLOCK 9: Poem Verse 3 ===
(Component: TEMPLATE_C_POEM.html)
Line 1 Hemistich 1: وَارْتَمَى كِيرُ اللَّيَالِي دُونَهَا
Line 1 Hemistich 2: لَيْنَ النَّابِ، كَلِيلَ الْمِخْلَبِ

=== BLOCK 10: Analysis Verse 3 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: دراسة البيت
Body:
المفردات كير العظمة والتجبر لين : سهل، منقاد. الجمع أليناء. كليل: ضعيف المِخْلَب اسم آلة، فعله: خلب
الشرح وخضع للبلاد جبروت الزمان منهك القوى، إذ تهاوى أمام صمود أبنائنا جبروت المستعمرين بعد أن أنهكت قواهم
الفكرة تصوير هَزِيمَةِ المُستَعْمر وَخَيْبَتِهِ فِي تَوْطِيدِ وُجُودِه على أَرْضِنا )السُّخْرِيَةِ مِنَ المُسْتَعْمِر والشَّمَاتَةَ بِهَزِيمَتِهِ(
الشَّعُور : الفَرَح
الأداة التراكيب المثال: ارْتَمَى كير الليالي.

=== BLOCK 11: Irab Verse 3 ===
(Component: TEMPLATE_C_IRAB.html)
Word 1: كير
Details 1: فَاعِلَ مَرْفُوع
Word 2: الليالي
Details 2: مُضَافَ إِلَيْهِ مَجْرُوز، وعلامَةُ جَرَهِ الكَسْرَةُ المُقَدَّرَةُ على الياء، مَنَعَ ظُهُورَهَا التَّقَلُ
Word 3: دُونَهَا
Details 3: مَفْعُولٌ فِيهِ ظَرْفُ مَكَانِ مَنْصُوب، وعلامة نَصْبِهِ الفَتْحَةُ الظَّاهِرَة.ُ وها، ضميرٌ مُتَصِلِّ مَبْنِي على السُّكُونِ فِي مَحَلٍ جَر،ٍ مُضَاف إليهِ
Word 4: لَيْنَ
Details 4: حَالَ مَنْصُوبَة.ٌ
Word 5: النَّابِ
Details 5: مُضَافُ إِلَيْهِ مَجْرُورٌ
Word 6: كَلِيْلَ
Details 6: حَالَ مَنْصُوبَة ثانية.ٌ
Word 7: الْمِخْلَبِ
Details 7: مُضَافُ إِلَيْهِ مَجْرُورٌ
Word 8: جُمْلَهُ )ارْتَمَى(
Details 8: مَعْطُوفَة،ٌ لا محل لها مِنَ الإعراب.

=== BLOCK 12: Poem Verse 4 ===
(Component: TEMPLATE_C_POEM.html)
Line 1 Hemistich 1: لا يموتُ الحَقُّ مَهْمَا لَطَمَتْ
Line 1 Hemistich 2: عارضيْهِ قَبْضَةُ الْمُغْتَصِبِ

=== BLOCK 13: Analysis Verse 4 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: دراسة البيت
Body:
المفردات عارضيه المفرد عارض وهو جانب الوجه أو صفحة الخد.
الشرح كفة الحق هي الراجحة دائما فهو الغالب مهما حاول المستعمر تغطيته وطمسه
الفكرة: ثبات الحق في وجه المغتصب
البلاغة : )الحَقُّ(، )لَطَمَتْ عَارِضَيْهِ قَبْضَةُ الْمُغْتَصِب(: استعارَةٌ مَكْنِيَّة.ٌ

=== BLOCK 14: Irab Verse 4 ===
(Component: TEMPLATE_C_IRAB.html)
Word 1: لا
Details 1: حَرْفُ نَفي.
Word 2: يموت
Details 2: فعل مُصَارِعٌ مَرْفُوع
Word 3: الحقُّ
Details 3: فَاعِلَ مَرْفُوعٌ
Word 4: مَهْمَا
Details 4: اسمُ شَرْطِ جازم، مَبْنِي على السُّكُون، فِي مَحَلِّ رَفْع،ِ مُبْتَدَا.
Word 5: لَطَمَتْ
Details 5: فِعْل ماض، مَبْنِي على الفَتْحَةِ؛ لاتِصَالِهِ بِنَاءِ التَّأنيث السَّاكِنَة،ِ وهو في محل جزم والنَّاء،ُ حَرْفُ تَأْنِي لَا مَحَلَّ لَهُ مِنَ الإِعراب .
Word 6: عَارِضَيْه
Details 6: مَفْعُولُ بِهِ مَنْصُوب، وعلامَةُ نَصْبِهِ اليَاءُ؛ لأَنَّهُ مُتَتَّى، وذفَتِ النُّونُ لِلإِضَافَة.ِ والهاء، ضمير متصل مَبْنِي على الكُسْرَةِ في محل جر، مُضَافُ إِلَيْهِ
Word 7: قَبْضَةُ
Details 7: فَاعِلَ مَرْفُوعُ
Word 8: الْمُغْتَصِبِ
Details 8: مُضَافَ إِلِيهِ مَجْرُورٌ
Word 9: جملة )لا يوت الحق(
Details 9: استئنافية، لا تحل لها مِنَ الإعراب
Word 10: جُمْلَةٌ )مَهُمَا لَطَمَتْ عَارِضَيْهِ قَبْضَةُ الْمُعْتَصِبِ(
Details 10: استئنافية، لا محل لها مِنَ الإعراب
Word 11: جُمْلَةً )لَطَمَتْ عَارِضَيْهِ قَبْضَةُ المُنْتَصِبِ(
Details 11: جُمْلَةُ الشَّرْطِ غَيْرِ الظَّرفي، لَا مَحَلَّ لها مِنَ الإِعراب.

=== BLOCK 15: Poem Verse 5 ===
(Component: TEMPLATE_C_POEM.html)
Line 1 Hemistich 1: مِنْ هُنا شَقَ الهُدَى أَكْمَامَهُ
Line 1 Hemistich 2: وَتَهَادَى مَوْكِبًا في مَوْكِبِ

=== BLOCK 16: Analysis Verse 5 ===
(Component: TEMPLATE_C_BLOCK.html with `.block-header.accent`)
Title: دراسة البيت
Body:
المفردات الهدى الهداية والرشاد. أكمامه: أغطيته المفرد : كم
الشرح من أرضنا برغ نُورُ الهداية والرشاد، وفوق ترابها تقاطرت جحافل الفاتحين تتداول نشر ضيائه وبسط وهجه في كل الأرجاء
الفكرة الاعتزاز بالماضي المجيد.
الشعور الاعتزاز والافتخار.
الأداة: التراكيب. المثال: من هنا شَقَّ الهُدَى أَكْمَامَهُ

=== BLOCK 17: Irab Verse 5 ===
(Component: TEMPLATE_C_IRAB.html)
Word 1: من
Details 1: مِنْ حَرْفُ جر.
Word 2: هنا
Details 2: اسم إشارة مبني على السُّكون في محل جرٍ بِحَرْفِ الجَر.ِ
Word 3: الهدى
Details 3: فَاعِلِّ مَرْفُو
Word 4: أَكْمَامَهُ
Details 4: مَفْعُولُ بِهِ مَنْصُوبُ
Word 5: وَقَادَى
Details 5: الواو، حَرْفُ عَطْفٍ تَقَادَى، فعل ماض، مَبْنِي على الفتحة المقدرة على الأَلِف،ِ مَنَعَ ظَهُورَها التَعَذِّر،ُ
Word 6: مؤكبًا
Details 6: حَالُ مَنْصُوبَة.ٌ
Word 7: يُمْلَهُ )شَقَ الهُدَى أكمامه(
Details 7: استئنافية، لا محل لها مِنَ الإعراب
Word 8: جُمْلَةً )قَادَى(
Details 8: مَعْطُوفَة،ٌ لا محل لها مِنَ الإعراب.

--- END STREAM ---
