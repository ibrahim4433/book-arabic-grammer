# **SESSION 128**

[TASK DEFINITION]
Objective: Implement page 128.
File: `pages/page_128.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`.
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md` to identify the correct template to use for the continuation.
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
6. Templates: You are forbidden from inventing new HTML tags or classes or template elements. Replace any `<section>` tags from the templates with `<div>` tags (keep `<header>`).
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). Applied to `<div>`.
8. **Self-Correction:** Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...) .
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense.
13. balanced page colors between teal and orange: make sure every page have minimum 1 element in orange.
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`).
15. Exam section always be in the end of the lesson, without answers!

[CONTENT STREAM]

--START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 128
[CHAPTER_TITLE]: page 128
[CATEGORY_HEADER]: 128
[SECTION_HEADER]: 128
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: إعراب (تتمة) ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
Title: إعراب
Content:
(Component: TEMPLATE_C_IRAB.html)
محل رفع، فَاعِلْ
يَا سَمَاءُ: يا، حَرْفُ نِدَاءٍ سَمَاءُ، مُنَادى نَكِرَةً مَقْصُودَة،ٌ مَبْنِي على الضَّمَّة،ِ في محل نصب على النداء.
جُمْلَةٌ (إِنَّهَا فَرْحَةُ الحَيَاةِ): استئنافية، لا محل لها مِنَ الإعراب
جملة (مِيدِي): اسْتئنافِيَّة،ٌ لَا مَحَلَّ لها مِنَ الإعراب
جُمْلَةً (هَلِّلِي): مَعْطُوفَة،ً لا محل لها مِنَ الإعراب.

=== BLOCK 3: الشاهد الشعري 1 ===
(Component: TEMPLATE_C_POEM.html)
وَتَغَنَّي بِأَمَّتِي إِنَّهَا عا دَتْ وَإِنَّا فِي أَرْضِنا طُلَقَاءُ

=== BLOCK 4: المفردات والشرح والفكرة 1 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح والفكرة
Content:
<span class="text-accent">المفردات:</span> تغني: أَشِيدِي طَلَقَاء: أَحْرار. وطلقاء: صِفَةٌ مُشَبَّهَةٌ باسم الفاعل، فعلها: طلق
<span class="text-accent">الشرح:</span> تباهي أيتها السَّمَاءُ بِأَمَّتِنَا العَربيَّة،ِ وأَشِيْدِي بها؛ فَقَدْ تَخَلَّصَتْ مِنْ قُيُودِ المستَعْمِرِين، واسْتَعَادَتْ إِرَادَتَهَا المصادَرَة،َ واستَرَدَتِ اسْتِقْلَالَ قَرَارِهَا المَنْهُوب،ِ فَهَا نَحْنُ نَنْعُمُ بالتَّحَرُرِ فَوْقَ ثَرَى بِلَادِنَا الْحَبيبة
<span class="text-accent">الفكرة:</span> الدَّعْوَة إلى الإِشَادَةِ بِالْأُمَّةِ العَرَبِيَّةِ لِتَحَرُرِهَا وَاسْتِقْلالها (الاعتِزَازُ بِتَحَرُّرِ الْأُمَّةِ الْعَرَبِيَّةِ).

=== BLOCK 5: الأساليب 1 ===
(Component: TEMPLATE_C_TABLE.html)
Title: الأساليب
Content:
تغني بأمتي: أسلوب أمر. صِيغَتُهُ فِعل أمر.
(إنها عادت)، (إِنَّا فِي أَرْضِنَا طَلَقَاءُ): أسلوب توكيد. المؤكد: إن. نوع التوكيد: جائز.
(Note to generator: Map this into rows/columns in the dense-table layout)

=== BLOCK 6: الإعراب 1 ===
(Component: TEMPLATE_C_IRAB.html)
Title: الإعراب
Content:
وَتَغَنَّي: الوَاو،ِ حَرْفُ عَطْفٍ تَغَنَّي، فِعْلُ أَمْرٍ مَبْنِي على حَذْفِ النُّون،ِ لَأَنَّ مُضَارِعَهُ مِنَ الْأَفْعَالِ الخَمْسَة.ِ والياء، ضَمِيرٌ مُتَّصِلٌّ مبني على السكون فِي مَحَلِ رَفْع،ِ فاعل
بأمتي: الباء، حَرْفُ جَر. أمتي، اسم مجرور، وعلامَةُ جَرِهِ الكَسْرَةُ الظَّاهِرَة،ُ والياء، ضَمِيرٌ مُتَصِلُّ مَبْنِيٌّ على السكون فِي مَحَلِّ جَر، مضاف إِلَيْهِ
إِنَّهَا: إِن،َّ حَرْفٌ مُشَبَّهُ بِالفِعْل.ِ وها، ضَمِيرٌ مُتَصِلٌّ مَبْنِي على السُّكُونِ فِي مَحَلَّ نَصْب،ِ اسمُ إِنَّ
عَادَتْ: فعل ماض، مَبْنِي على الفَتْحَةِ؛ لاتِصَالِهِ بِتَاءِ التَّأْنِيثِ السَّاكِنَةِ وَالتَّاء،ُ حَرْفُ تَأْنِيث لا مَحَلَّ لَهُ مِنَ الإعراب.
وإِنَّا: الواو، حَرْفُ عَطْفٍ إِن،َّ حَرْفٌ مُشَبَّهٌ بالفعل. ونا، ضَمِيرٌ مُتَّصِلٌّ مَبْنِي على السكون في محل نَصْب،ٍ اسم إِنَّ
طَلَقَاءُ: خَبَرٌ مَرْفُوع
جُمْلَةُ (تَغَنَّي): مَعْطُوفَة،ً لا محل لها مِنَ الإعراب.
جُمْلَةُ (عَادَتْ): اسْتَئنافِيَّة،ٌ لا محل لها مِنَ الإعراب
جُمْلَهُ (إِنَّا فِي أَرْضِنَا طَلَقَاءُ): مَعْطُوفَة،ٌ لَا مَحَل لها مِنَ الإعراب.

=== BLOCK 7: الشاهد الشعري 2 ===
(Component: TEMPLATE_C_POEM.html)
أَيُّهَا النَّائِهُونَ فِي مَهْمَهِ الْأَمْسِ سَرَابٌ دُرُوبُكُمْ وَشَقَاءُ

=== BLOCK 8: المفردات والشرح والفكرة 2 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح والفكرة
Content:
<span class="text-accent">المفردات:</span> النَّائِهُونَ: المُتَخَلِّفُونَ عَنْ رَكْبِ الوَحْدَةِ مَهْمَه: المفازة البعيدة، وهي الصَّحراء الواسعة، أو البَلَدَ القَفْر. سراب: وَهْم، وهو ما يرى في نِصْفِ النَّهَارِ عِنْدَ اشْتِدَادِ الحر كالماء في الصَّحَارَى يَلْصَقُ بِالأَرْضِ والنَّائِهُونَ: اسم فاعل، فعله: تاه.
<span class="text-accent">الشرح:</span> أَيُّهَا المُتَخَلِّفُونَ عَنْ رَكْبِ الوَحْدَة،ِ يَا مَنْ تَتَشَبَّثُونَ بِأَوْهَامِ الْمَاضِي، وَتَتَخَبَّطُونَ بِمَتَاهَاتِهِ المُضِلَّة،ِ إِنَّ سَبِيلَ الفُرْقَةِ وَالتَّجْزِيَّةِ الذي اخْتَرْتُمُوهُ طريق مَفْرُوش بِالأَوْهَام،ِ مُعَبَّد بِالمَشَقَة،ِ مَرْصُوف بِالعَذَاب
<span class="text-accent">الفكرة:</span> الدَّعْوَة إلى الوَحْدَةِ العَرَبِيَّةِ (تَحْفِيز المترددين للالتحاق بِرَكْبِ الوَحْدَةِ العَرَبِيَّةِ، التَّحْذِيرَ مِنَ التَّجْزِنَةِ وَنَبْذ الْفُرْقَةِ). الشُّعُور: حب، وغيرة

=== BLOCK 9: البلاغة والتراكيب 2 ===
(Component: TEMPLATE_C_TABLE.html)
Title: البلاغة والتراكيب
Content:
الأداة التراكيب المثال: سَرَابٌ دُرُوبُكُمْ وَشَقَاءُ.
البلاغة: (سَرَابٌ دُرُوبُكُمُ): تشبيه بليغ
(Note to generator: Map this into rows/columns in the dense-table layout)

=== BLOCK 10: الإعراب 2 ===
(Component: TEMPLATE_C_IRAB.html)
Title: الإعراب
Content:
أَيُّهَا: أَيُّ، مُنادى نَكِرَةٌ مَقْصُودَةٌ مَبْنِي على الضَّمِ فِي مَحَلِّ نَصْبِ على النداء. وها، للتنبيه.
النَّائِهُونَ: صِفَةٌ مَرْفُوعَة،ٌ وعلامَةُ رَفْعِهَا الواو؛ لأَنَّهَا جَمْعُ مُذَكّر سالم، والنون، عِوَضُ عَنِ التَّنْوِينِ فِي الاسم المفرد.
في مهمه: في، حَرْفُ جَرٍ مَهْمَه،ِ اسم مجرور، وعلامةُ جَرَهِ الكَسْرَةُ الظَّاهِرَةُ
الأَمْسِ: مُضَافُ إِلِيهِ مَجْرُورٌ
سَرَابٌ: خَبَرٌ مُقَدَّمَ مَرْفُوعٌ
دُرُوبُكُمْ: مُبْتَدَأٌ مُؤَخَرُ مَرْفُوعٌ
وَشَقَاءُ: الواو، حَرْفُ عَطْفٍ شَقَاء،ُ اسمٌ مَعْطُوفٌ مَرْفُوعٌ
جَمْلَهُ (سَرَابٌ دُرُوبُكُمْ): اسْتِتَنَافِيَّة،ٌ لَا مَحَل لها مِنَ الإعراب.

=== BLOCK 11: الشاهد الشعري 3 ===
(Component: TEMPLATE_C_POEM.html)
أَزْهَرَتْ وَاحَةُ العُرُوبَةِ وَافْتَرَّتْ وَماسَتْ جِنَانُهَا الْخَضْرَاءُ

=== BLOCK 12: المفردات والشرح والفكرة 3 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح والفكرة
Content:
<span class="text-accent">المفردات:</span> واحة: ساحة. افْتَرَّت: بَدَا عَلَيْهَا الابتِسَامِ مَاسَتْ: تَبَخْتَرَتْ وَاخْتَالَتْ . جنانها: المفرد: جَنَّة، وهي الحديقة ذات الشجر، أو البُسْتَان. والخضراء: صِفَةٌ مُشَبَّهَةٌ باسم الفاعل فعلها: خضر
<span class="text-accent">الشرح:</span> بِقِيَامِ الوَحْدَةِ اكْتَسَتْ سَاحَةُ العُرُوبَةِ رَبِّيْعًا، بَعْدَ أَنْ أَجْدَبَتْهَا التَّجْزِنَة،ُ حَيْثُ تَفَتَّحَتْ فِيهَا أَكْمَامُ الزُّهُورِ فَبَدَتْ بَاسِمَةَ الثَّغْرِ مِنْ شِدَّةِ حُسْنِهَا، وَرَاحَتْ حَدَائِقُهَا الغَنَّاءُ تَخْتَالُ وَتَتَبَخْتَرُ تِيْهًا مِنْ رَوْعَةِ جَمَالها.
<span class="text-accent">الفكرة:</span> الإشارة إلى ثمارِ الوَحْدَةِ (وَصْفِ جَمَالِ الحَيَاةِ بَعْدَ قِيَامِ الوَحْدَةِ).
البلاغة: (ماسَتْ جِنَانُهَا): استِعَارَةُ مَكْنِيَّة.

=== BLOCK 13: الإعراب 3 ===
(Component: TEMPLATE_C_IRAB.html)
Title: الإعراب
Content:
وَاحَةٌ: فَاعِلَ مَرْفُوعٌ
العُرُوبَةِ: مُضَافُ إليهِ مَجْرُورٌ
جِنَاتُها: فَاعِلٌ مَرْفُوعُ
الخَضْرَاءُ: صِفَةٌ مَرْفُوعَةٌ
جُمْلَهُ (أَزْهَرَتْ وَاحَةُ العُرُوبَةِ): اسْتِنَافِيَّة،ٌ لا محل لها مِنَ الإعراب .
جُمَلَةُ (افْتَرَتْ)، وجُمْلَةً (ماسَتْ جِنَانُهَا): مَعْطُوفَة،ٌ لَا مَحَلَّ لها مِنَ الإعراب.

=== BLOCK 14: الشاهد الشعري 4 ===
(Component: TEMPLATE_C_POEM.html)
وَتَثَنَّتْ فِيهَا الْجَدَاوِلُ سَكْرَى وَتَرَامَتْ فِي رَبِّعِهَا الْأَفْيَاءُ

=== BLOCK 15: المفردات والشرح والفكرة 4 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح والفكرة
Content:
<span class="text-accent">المفردات:</span> تَثَنَّتْ: تَمَايَلَتْ وَتَبَخْتَرَتْ الجداول: السَّوَاقِي ربعها: الجمع: ربوع، وهو المنزل والمسكن الأفياء: المفرد: فيء، وهو الظل. وسكرى: صفَةٌ مُشَبَّهَةٌ باسم الفاعل فعلها: سكر
<span class="text-accent">الشرح:</span> بِقِيَامِ الوَحْدَةِ بَدَتْ فِي سَاحَةِ العُرُوبَةِ جَدَاوِلُ المَاءِ الرَّقْرَاقَةِ تَتَمَايَلُ مُنْتَشِيَةً كَمَخْمُورٍ ثَمِلٍ دَارَتْ الخَمْرَةُ بِرَأْسِه،ِ وَرَاحَتْ رُبُوعُهَا تَضِجُّ مِنْ تَزَاحُمِ الظِّلَالِ الوَارِفَةِ التِي تَرَاكَمَتْ فيها
<span class="text-accent">الفكرة:</span> الإشارة إلى ثمارِ الوَحْدَةِ (وَصْفَ جَمَالِ الْحَيَاةِ بَعْدَ قِيَامٍ الوَحْدَة). الشُّعُور: فرح
الأداة: التَّراكيب المثال: تَثَنَّتْ فِيهَا الجَدَاوِلُ سَكْرَى
البلاغة: (تَثَنَّتُ الجَدَاوِلُ)، (الجَدَاوِلُ سَكْرَى): استعارَةً مَكْنِيَّة.

=== BLOCK 16: الإعراب 4 ===
(Component: TEMPLATE_C_IRAB.html)
Title: الإعراب
Content:
وَتَثَنَّتْ وَتَرَامَتْ: الواو، حَرْفُ عَطْفٍ تَشَنَّتْ تَرَامَتْ فِعل ماض، مَبْنِي على الفَتْحَةِ المُقَدَّرَةِ على الأَلِفِ الْمَحْذُوفَةِ لَاتِصَالِهِ بِتَاءِ التانيثِ السَّاكِنَة.ِ والتَّاء،ُ حَرْفُ تَأْنيث لا مَحَلَّ لَهُ مِنَ الإعراب
فيها: في، حَرْفُ جَر.ٍ وها، ضَمِيرٌ مُتَّصِلٌّ مَبْنِي على السُّكُونِ فِي مَحَلِّ جَر،ٍ بِحَرْفِ الجَر. والجار والمَجْرُورُ مُتَعَلقان بِالفِعْلِ (تَشَنَّتْ).
الجَدَاوِلُ الأَفْيَاءُ: فَاعِلْ مَرْفُوعٌ
سَكْرَى: حالٌ مَنْصُوبَة،ٌ وعلامَةُ نَصْبِهَا الفَتْحَةُ المُقَدَّرَةُ على الأَلِف،ِ مَنَعَ ظُهُورَهَا التَّعَذُّرُ
جُمْلَةُ (تَشَنَّتْ فِيهَا الْجَدَاوِلُ) وجُمَلَهُ (تَرَامَتْ فِي رَبِّعِهَا الأَفْيَاءُ): مَعْطُوفَة،ٌ لَا مَحَلَّ لها مِنَ الإعراب.


--- END STREAM ---
