# **SESSION 111**

[TASK DEFINITION]
Objective: Implement page 111.
File: `pages/page_111.html` (Note: Use the exact page number.)
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
[LESSON_NUMBER]: 111
[CHAPTER_TITLE]: page 111
[CATEGORY_HEADER]: 111
[SECTION_HEADER]: 111
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: [إعراب قصيدة] ===
(Component: TEMPLATE_CUT_BOX_PART_2.html -> TEMPLATE_C_IRAB.html)
Title: الإعراب
Content:
انطلاق : اسمٌ مَعْطُوفٌ مَرْفُوعٌ
حَتَّى : حَرْفُ غَايَةٍ وَجَرٍ
يَرتوي : فِعْلَ مُصَارِعٌ منصوب بأنْ الْمُضْمَرَةِ بَعْدَ حَتَّى
كُل:ُ فَاعِلَ مَرْفُوعٌ
النُّور،ِ جَفْن : مُصَافُ إِلَيْهِ تَجْرُوز
برتوي كُلُّ جَفْنِ( : صِلَةُ الْمَوْسُولِ لَا مَحَلَّ لَهَا مِنَ الإعراب .
مُخْتَضِبِ : صِفَةٌ مَجْرُورَة.ٌ

=== BLOCK 3: [بيت شعري] ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: حُلُمٌ وَلَّي، وَلَمْ يُجْرَحْ بِهِ
Hemistich 2: شَرَفُ المَسْعَى وَنُبْلُ الْمَطْلَب!

=== BLOCK 4: [الشرح والمفردات] ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح
Content:
المفردات:
المسعى: طَلَبُ المكرمة في أنواع المجد والكرم. والجمع مساع.
الشرح: مَعَ أَنَّ الحلم الذي سعينا وراءه وحاوَلْنَا بُلُوغَهُ لَم يَتَحَقَّق، إِلَّا أَنَّ هَذَا لَم يَخْدِسٌ قَدَاسَةَ الْحَدَف،َ أو يُهَوَنَ مِنْ نَزَاهَةِ الطَّلب.
الشُّعُور: خَيْبَةُ أَمَل.
الأداة: التراكيب.
المثال: حلم وَلى.

=== BLOCK 5: [إعراب البيت] ===
(Component: TEMPLATE_C_IRAB.html)
Title: الإعراب
Content:
حلم : خَبَرٌ مَرْفُو.
)وَلى( : فِي مَحَلِّ رَفْعِ صِفة.
شَرَف : نَائِبُ فَاعِلِ مَرْفُوعُ
لَمْ يُجْرَحْ بِهِ شَرَفُ الْمَسْعَى( : في محل نصب حال.
نبل : اسمٌ مَعْطُوفٌ مَرْفُوء.ٌ
المسعى، المطلب : مُضَافُ إِلَيْهِ مَجْرُور.ٌ

=== BLOCK 6: [بيت شعري] ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: سَكِرَتْ أَجيالنا في زهوها
Hemistich 2: وَغَفَتْ عَنْ كَيْدِ دَهْرٍ قُلَّبِ!

=== BLOCK 7: [الشرح والمفردات] ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح
Content:
المفردات:
زهوها: زها: تاه وتعاظم وافتخر. الزهو: الكبر. ويريد هنا الانشغال بِفَرَح النَّصْرِ على العثمانيين.
كَيْدِ: الكَيْدُ إِرَادَةُ مَضَرَّةِ الغَير خِفْيَة.ً
الشرح: انتشى أبناء الأُمَّةِ العَرَبِيَّةِ فِي أَيَّامٍ فَرَحِهِم، حِيثُ دَفَعَتْهُم لحظات الفرح والسرور إلى التيه والإعجاب بالنَّفْس،ِ فَعَفَلُوا عَنْ مَكْرِ الرَّمَانِ وَتَقَلْبَاتِهِ.
الفِكْرة: تصويرُ الغَفْلَةِ عَنْ تَقَلْبَاتِ الزمانِ.
البلاغة: )كَيْدَ دَهْرِ(: استعارَةً مَكْنِيّ.ٌ

=== BLOCK 8: [إعراب البيت] ===
(Component: TEMPLATE_C_IRAB.html)
Title: الإعراب
Content:
أجيالنا : فاعل مَرْفُوعٌ
دَهْرِ : مُضاف إِلَيْهِ مَجْرُورٌ
قَلَّبِ : صِفَةٌ فَجْرُورَة.ٌ

=== BLOCK 9: [بيت شعري] ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: وَصَحونا فَإِذَا أَعْنَاقُنَا
Hemistich 2: مُفْقَلات بقيود الأجنبي

=== BLOCK 10: [الشرح والمفردات] ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح
Content:
المفردات: مُثْقَلات: اسمُ مَفْعُول،ِ فِعْلُهُ أَنقل.
الشرح: وحِينَمَا تَخَلَصْنَا مِنْ تأثير النَّشْوَة،ِ وانجَلَتْ عَنْ أَنفُسِنَا مَعَالِمُ الفَرَحِ والزهو وَجَدْنَا نِيرَ المُسْتَعْمِرِ الفرنسي يُطَوَقُ رِقَابَنا، وأغلالَهُ تُكَبِّلُ أيدينا.
الفكرة: تصويرُ الصَّحْوَةِ مِنَ الغَفْلَةِ.
الشعور: حزن والم.
الأداة: التراكيب.
المثال: أَعْنَاقُنَا مُثْقَلَاتٌ بِقُيود الأجنبي.

=== BLOCK 11: [إعراب البيت] ===
(Component: TEMPLATE_C_IRAB.html)
Title: الإعراب
Content:
أَعْنَاقُنا : مُبْتَدَ مَرْفُوعٌ
مُثْقَلات : خَبَرٌ مَرْفُوعُ
الأَجْنَبِي : مُضَافُ إِلَيْهِ مَجْرُورٌ.

=== BLOCK 12: [بيت شعري] ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: فَدَعُونَاكِ فَلَمْ تَسْمَعُ سوى
Hemistich 2: زَفْرَةٍ مِنْ صَدْرِكَ الْمُكْتَنِبِ!

=== BLOCK 13: [الشرح والمفردات] ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح
Content:
المفردات:
زَفْرَةِ: زَفَرَ: أَخْرَجَ نَفَسَهُ بَعْدَ مَدِهِ إِيَّاهِ.
الْمُكْتَتِبِ: كَئِبَ: تَغَيَّرَتْ نَفْسُهُ وانكَسَرَتْ مِنْ شِدَّةِ الهم والحزن.
الشرح: نادَيْنَاكِ أَيَّتها الحرية، لكنكِ لم تردي على النداء، فلم يتناهي إلى أَسْمَاعِنَا إِلَّا شَهَقات الأسى والألم المنبعثَةُ مِنْ صَدْرِكِ الحزين.
الشعور: حزن.
الأداة: التراكيب.
المثال: ثُمَّ نَسْمَعُ سِوى زَفْرَةٍ مِنْ صَدْرِكِ المكتتب.
البلاغة: )صَدْرِكِ المكتب( استعارَةً مَكْنِيَّةٌ )شَبَّةَ الْحَرِّيَّة بإنسان(.

=== BLOCK 14: [إعراب البيت] ===
(Component: TEMPLATE_C_IRAB.html)
Title: الإعراب
Content:
سوى : مَفْعُولُ بِهِ مَنْصُوبُ
زَفْرَةِ : مُضَافُ إِلَيْهِ يَجْرُور.ٌ
المَكْتَتِبِ : صِفَةٌ جْرُورَة.ٌ

=== BLOCK 15: [بيت شعري] ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: فَحَمِلْنَا لك إكليل الوَفَا
Hemistich 2: وَمَشَيْنا فوق هام النُّوَبِ

=== BLOCK 16: [الشرح والمفردات] ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح
Content:
المفردات:
إكليل: تاج.
الوفا: الوفاء.
هَام: المفرد هامة، وهي الرأس.
التوبُ: التَّوَبَةُ النَّازِلَةُ والمصيبة.
الشرح: بقينا أوفياء لَكِ أَيَّتُهَا احْرِّيَةُ مُصَمِّمِينَ على النَّصْرِ مِنْ أَجْلِ الحُصُولِ عَلَيْك،ِ فَلْمَ نَكْتَرَتُ بالصعوبات، وعزمنا على تجاوز العقبات، ودسنا فوق المصائب والتكبات.
الفكرة: الوفاءُ لِلْهَدَفِ والتَّغَلُبُ على الصعاب في سَبِيلِ تَحْقِيقِهِ.
الشُّعُور: اعتزاز وافتخار.
الأداة: التراكيب.
المثال: حملنا لك إكليلَ الْوَفَا. أو : مَشَيْنا فوقَ هَامِ التَّوَبِ.
البلاغة: )إكليل الوَفَا( : تشبيةٌ بَلِيعٌ إضافي. )هَامِ التَّوَبِ( استِعَارَةٌ مَكْنِيَّة،ٌ وَيُقْبَل:ُ تشبيه بَلِيعٌ إضافي.

=== BLOCK 17: [إعراب البيت] ===
(Component: TEMPLATE_C_IRAB.html)
Title: الإعراب
Content:
الوفاء، هام، النوبِ : مُصَافُ إِلَيْهِ مَجْرُورٌ
فَوقَ : مَفْعُولُ فِيهِ ظَرْفُ مكانٍ مَنْصُوب.ُ

=== BLOCK 18: [بيت شعري] ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: وامسحي دَمْعَ اليَتَامَى وابسمي
Hemistich 2: والمسي جُرْحَ الحزاني واطربي

=== BLOCK 19: [الشرح والمفردات] ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح
Content:
المفردات: اليتامى، الخزانى : صِفَةٌ مُشَبَّهَةٌ باسم الفاعل.
الشرح: أيتها الحريَّةُ اغسلي بِدِمَاءِ الشُّهَدَاءِ التي أُرِيقَتْ مِنْ أَجِلِكِ دُمُوعَ الأَيتام وافْرَحِي وارسمي الابتسام على محياهم، وداوي بهذه الدِّمَاءِ جُرْحَ كُلِّ حَزِينِ لِتُدْخِلِي الْفَرَحَ والسرور إلى قَلْبِهِ.

=== BLOCK 20: [إعراب البيت] ===
(Component: TEMPLATE_C_IRAB.html)
Title: الإعراب
Content:
امسحي، ابسِمِي، الْمَسِي، اطْرَبِي : فعل أمر مبني على حَذْفِ النُّون؛ لأَنَّ مُصَارِعَهُ مِنَ الأفعال الخمسة.
دَمْع،َ جُرْحَ : مَفْعُولُ بِهِ مَنْصُوبُ
اليَتَامَى، الْحَزَانى : مُصَافُ إِلَيْهِ مَجْرُور.ٌ

=== BLOCK 21: [بيت شعري] ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: كَمْ لَنا مِنْ مَيُسلون نفضت
Hemistich 2: عَنْ جَنَاحَيْهَا غُبَارَ التَّعَبِ

=== BLOCK 22: [الشرح والمفردات] ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح
Content:
الشرح: حضنا معاركَ كَثِيرَةً مثل مَعْرَكَةِ مَيْسَلُون، وقد حَقَّقنا في هذه المعارك النَّصْرَ بَعْدَ الخَزِيمَة،ِ فَغَسَلْنَا الدُّلَّ والعارَ عَنْ أَنفُسِنا.
البلاغة: )ميسلون نَفَضَتْ عَنْ جَنَاحَيْهَا(: استعارَةُ مَكْنِيَّة.ٌ )عُبَارَ التَعَبِ( : تشبية بليع إضافي.

=== BLOCK 23: [إعراب البيت] ===
(Component: TEMPLATE_C_IRAB.html)
Title: الإعراب
Content:
كَمْ : خَبَرَيَّةٌ مَبْنِيَّةٌ على السكون فِي مَحَلِّ رَفْعِ مُبْتَدَا.ً
)نَفَضَتْ( : في محل نصب حال.

=== BLOCK 24: [بيت شعري] ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: ١٠- كَمْ نَبَتْ أَسْيَافُنَا فِي مَلْعَبِ
Hemistich 2: وَكَبَتْ أَفْرَاسُنَا فِي مَلْعَبِ

=== BLOCK 25: [الشرح والمفردات مقطوع] ===
(Component: TEMPLATE_CUT_BOX_PART_1.html -> TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح
Content:
المفردات:
نَبَتْ: نَهَا السَّيْفُ عَنِ الصَّرِيبَةِ نَبُوا وَنَبْوَة:ً لم يُصِبْهَا. والسَّهْمُ عَنِ الغَرَضِ جاوزَهُ.
كَبَتْ: تَعَثَرَتْ.
الشرح: خذلنا في معارك كثيرة، حَيْثُ تَعَثَرَتْ خُيُولُنَا، ولَ تُحَقِّق سُيُوفُنَا أَهدافها.
الشعور: خَيْبَة،ٌ وحزن.
الأداة: التراكيب.
المثال: نَبَتْ أَسْيَافُنَا فِي مَلْعَب.ِ أو : كَبَتْ

--- END STREAM ---
