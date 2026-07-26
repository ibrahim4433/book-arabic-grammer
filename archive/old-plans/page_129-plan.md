# **SESSION 129**

[TASK DEFINITION]
Objective: Implement page 129.
File: `pages/page_129.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools. If it overflows, it is a catastrophic failure. Do NOT try to solve overflow by deleting text (Strict Typographer Rule). Solve it by choosing denser templates or omitting optional white-space.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`.
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md`.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide: NO INLINE STYLES. Irab Words inside `.irab-word` MUST be white.
7. Templates: Map all content using "Jules-workspace/Templates/" components. Replace `<section>` tags with `<div>`.
8. Unique IDs: All content blocks must have a unique ID (id='bXXXXX') applied to the `<div>`. Use "Jules-workspace/id_manager.py".
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...).
11. Preserve exact Tashkeel and add missing if any.
12. Visual Density: The page must be dense.
13. balanced page colors between teal and orange: minimum 1 element in orange.
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html`.
15. No Exam fabricated since it does not exist in the raw text, following the Strict Typographer Rule override.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 129
[CHAPTER_TITLE]: page 129
[CATEGORY_HEADER]: 129
[SECTION_HEADER]: 129
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: الشاهد الأول ===
(Component: TEMPLATE_C_POEM.html)
Verse: - <span class="highlight-red">أَقْبِلُوا</span> أَيُّهَا الحَيَارَى فهذا الهُ دَرْبُ طَلْقٌ مُشَوِّقُ وَضَاءُ

=== BLOCK 3: تحليل الشاهد الأول ===
(Component: TEMPLATE_C_TABLE.html)
Row 1: المفردات: | مشوق : منير. وضاء: مشرق والخيارى: صِفَةٌ مُشَبَّهَةٌ باسم الفاعل فعلها : حار. وطلق : صِفَةٌ مُشَبَّهَةٌ باسم الفاعل فعلها : طلق. ومُشَوَق: اسم فاعل، فِعْلُهُ : شوق. ووَضَاء:ُ مبالغة اسم فاعل، فِعْلُها : وَضُو.
Row 2: الشرح | <span class="text-accent">هيا اسلكوا أَيُّهَا المَتَرَدَدُونَ سَبِيلَ الوَحْدَةِ؛ لأَنَّهُ طَرِيقٌ سَهْل مُمَهَدٌ خَلَا مِنَ الحواجز والعثرات، مُثِيرٌ لِلْإِعْجَاب،ِ شَدِيدُ الإِشْرَاقِ</span>
Row 3: الفكرة : | الدَّعْوَة إلى الوَحْدَةِ العَرَبِيَّة )تحفيز التَرَدَدِين للالتحَاقِ بِرَكْبِ الوَحْدَةِ العربية(.
Row 4: الشهور : | حب، وغيرة
Row 5: الأداة التراكيب المثال: | <span class="highlight-red">أَقْبِلُوا</span> أَيُّهَا الحَيَارَى
Row 6: الأساليب : | أَقْبلُوا : أسلوب أمر. صيغته: فعل أمر

=== BLOCK 4: الإعراب ===
(Component: TEMPLATE_C_IRAB.html)
الإعراب:
أَقْبَلُوا : فِعْلُ أَمْرِ مَبْنِي على حَذْفِ النُّونِ لَأَنَّ مُضَارِعَهُ مِنَ الأَفْعَالِ الخَمْسَة.ِ والواو، ضميرٌ مُتَّصِلِّ مَبْنِي على السُّكُونِ فِي مَحَلِّ رَفْع،ِ فَاعِل.َ والأَلِفُ حَرْفُ تَفْرِيقِ
أَيُّهَا : أَي،ُّ مُنادى نَكِرَةً مَقْصُودَةٌ مَبْنِي على الصَّمَ فِي مَحَلِّ نَصْبِ على النداء. وها، للتنبيه
الخيارى: : صِفَةٌ مَرْفُوعَة،ٌ وعلامَةً رَفْعِهَا الصَّمَّةُ المُقَدرة على الأَلِفِ مَنَعَ ظُهُورَهَا التَّعَذُرُ
فهذا : الفاء، حَرْفُ استثناف. والهاء للتنبيه. وذا، اسم إشارَةِ مَبْنِي على السُّكُون في حَلِ رَفْع،ِ مُبْتَدَ
الدَّرْبُ : : بَدَلَّ مَرْفُو
طلق: : خَبَرَ مَرْفُو
مُشَوَقَ : خَبَرُ مَرْفُوعٌ
وَضَاء:ُ : خَبَرَ مَرْفُوع لجملة )أَقْبَلُوا(، وجُمْلَةً )هذا الدَّرْبُ طَلْقَ مُشَوَقٌ وَضَاءُ( : استئنافِيَّة،ٌ لَا مَحَلَّ لها مِنَ الإعراب.

=== BLOCK 5: الشاهد الثاني ===
(Component: TEMPLATE_C_POEM.html)
Verse: -١٠ دَرْبُ تَوْحِيدِ أُمَّةٍ <span class="highlight-red">جَبَلَتْها</span> مِنْ عَبِيرِ الْمَكَارِمِ العَلْيَاءُ

=== BLOCK 6: تحليل الشاهد الثاني ===
(Component: TEMPLATE_C_TABLE.html)
Row 1: المفردات : | جَبَلَتُهَا كَوَّنَتُهَا . العلياء: الشَّرَف والرفعة.
Row 2: الشرح : | <span class="text-accent">إِنَّ هذا السَّبِيلَ الَّذِي أَدْعُوكُم لِرُوبِهِ هو الطريق الذي تَتَوَجَّدُ فِيهِ الأُمَّةُ العَرَبِيَّة.ُ تلك الأُمَّة التي جَعَلَهَا شَرَفُهَا وَرِفْعَتُهَا تَنْشَأْ على حبّ الخير، والإكثار مِنْ فِعْلِهِ</span>
Row 3: الفكرة : | تَمْجِيد الأُمَّةِ الْعَرَبِيَّةِ وَالتَّغَنِي بِصِفَاتِهَا .
Row 4: الشعور | افتخار واعتزاز
Row 5: الأداة : التَّراكيب المثال: | <span class="highlight-red">جَبَلَ هَا</span> مِنْ عَبِيْرِ المَكَارِمِ العلياء
Row 6: البلاغة : | )جَبَلَتها العَلْيَاءُ(: استعارَةً مَكْنِيَّة

=== BLOCK 7: إعراب الشاهد الثاني ===
(Component: TEMPLATE_C_IRAB.html)
الإعراب :
دَرْبُ : : خَبَرٌ مَرْفُوعٌ
تَوْحِيد،ِ : أَمَّة،ٍ
المكارم: : مُضَاف إليهِ مَجْرُوز
العَلْيَاء:ُ : فَاعِلَ مَرْفُوعُ
جَمْلَةٌ جَبَلَ هَا مِنْ عَبِيرِ الْمَكَارِمِ الْعَلْيَاءُ(: : صِفَة،ٌ مَحَلَّهَا الجَر.ُّ

=== BLOCK 8: الشاهد الثالث ===
(Component: TEMPLATE_C_POEM.html)
Verse: -۱۱ في غَدٍ تَرْحَفُ الجُمُوعُ <span class="highlight-red">لِتَبْنِي</span> بيَدَيْهَا مَا هَدَّمَ الأَعْدَاءُ

=== BLOCK 9: تحليل الشاهد الثالث ===
(Component: TEMPLATE_C_TABLE.html)
Row 1: الشرح | <span class="text-accent">في القَرِيبِ العَاجِلِ سَتُبَاشِرُ الجَمَاهِيرُ العَرَبِيَّةُ صِنَاعَةَ المَسْتَقْبَلِ الوَاعِدِ حَيْثُ تَقَوْمُ بِبِنَاءِ مَا فَتَتَهُ الْمُسْتَعْمِرُ الغَرْبِيُّ بِفَرْضِ التَّجْزِئَةِ على الأُمَّة،ِ وَزَرْع العُ لَةِ وَالْفُرْقَةِ بَيْنَ أَبْنَائِهَا</span>
Row 2: الفكرة : | التَّفَاؤُلُ بِقِيَامِ الوَحْدَةِ الإيمان بِقُدْرَةِ الجَمَاهِير العربية على بِنَاءِ مَا هَدَّمَهُ المستَعْمِ .(
Row 3: الشعور : | أمل وتفاؤل
Row 4: الأداة : التَّراكيب المثال: | في غَدٍ تَزْحَفُ الجمُوعُ <span class="highlight-red">لِتَبْنِي</span>
Row 5: البلاغة : | )تَبْنِي هَدَّمَ( طباق إيجاب

=== BLOCK 10: إعراب الشاهد الثالث ===
(Component: TEMPLATE_C_IRAB.html)
الإعراب
الجموع: : فَاعِلَ مَرْفُوعُ
لِتَبْنِي: : الام،ُ حَرْفُ جَرٍ وَتَعْلِيل. وتَيْنِي فِعْلَ مُصَارِعٌ مَنْصُوبٌ بِأَنْ الْمُضْمَرَةِ بَعْدَ لَامِ التَعْلِيل،ِ وعلامَةُ نَصْبِهِ الفَتْحَةُ المقدرة على الياء، مَنَعَ ظُهُورَهَا التَّقَل.ُ والْمَصْدَرُ الْمُوَوَّلُ مِنْ أَنَّ الْمُصْمَرَة والفِعْلَ بَعْدَهَا في محل جر بحرف الجر.
ما : : اسم مَوْصُولُ مَبْنِي على السُّكُون، في مَحَلِّ نَصْب،ِ مَفْعُولُ بِهِ
الْأَعْدَاء:ُ : فاعِلَ مَرْفُوةٌ
جُمْلَةً تَرْحَفُ الجمُوعُ : اسْتِنَافِيَّة،ٌ لا محل لها مِنَ الإعراب
جملَةُ تَبْنِي(: : صِلَةُ المَوْصُول،ِ لا محل لها مِنَ الإعراب
جُمْلَهُ هَدَّمَ الْأَعْدَاءُ(: : صِلَةُ الْمَوْسُول،ِ لا مَحَلَّ لها مِنَ الإعراب.

=== BLOCK 11: التعبير الكتابي - التعبير الأدبي ===
(Component: TEMPLATE_C_BLOCK.html)
Title: التعبير الكتابي - التعبير الأدبي
Content: مخطط موضوع الوحدة الأولى - أدب القضايا الوطنية والقومية
أولاً - مقدمة مناسبة بمقدور الطالب أن يستوحي مقدمة مناسبة تَدُورُ حَوْلَ أَدَب القضايا الوَطَبَيَّة والقَوْمِيَّة.
ثانيا - الأدب القومي:
- الدَّعْوَةُ إِلَى التنبهِ إِلى واقع الأُمَّةِ المتردي:

=== BLOCK 12: شواهد الأدب القومي 1 ===
(Component: TEMPLATE_C_POEM.html)
Bio: إِبْرَاهِيمُ اليَازجي:
Verse: تَنَبَّهُوا وَاسْتَفِيقُوا أَيُّهَا الْعَرَبُ   فَقَدْ طَمَى الخَطَبُ حَتَّى غَاصَتِ الرَّكَبُ
Bio: مَعْرُوفُ الرِّصَافِي:
Verse: أَمَا آنَ أَنْ يَغْشَى البلاد سعودها  وَيَذْهَبَ عَنْ هَذِي النِّيَامِ هُجُودها

=== BLOCK 13: التحريض الثوري ===
(Component: TEMPLATE_C_BLOCK.html)
Content: - التحريض التوري للوقوف في وَجِهِ الظَّامِ مِنْ خلال :
الحت على النهوض:

=== BLOCK 14: شواهد التحريض الثوري ===
(Component: TEMPLATE_C_POEM.html)
Bio: إبراهيم اليازجي:
Verse: بالله يا قَوْمَنَا هِبُوا لِشَأْنِكُمُ    فَكُمْ تُنَادِيكُمُ الأَشْعَارُ و الخُطَبُ

=== BLOCK 15: التذكير بماضي الأجداد ===
(Component: TEMPLATE_C_BLOCK.html)
Content: التذكير بِمَاضِي الْأَجْدَادِ

=== BLOCK 16: شواهد التذكير ===
(Component: TEMPLATE_C_POEM.html)
Bio: إبراهيم اليازجي:
Verse: الَسْتُم مَنْ سَطَوا فِي الْأَرْضِ وَاقْتَحَمُوا  شَرْقًا وغَرْبًا، وعَزَّوا أَينما ذَهَبُوا

=== BLOCK 17: التعبير عن مشاعر الفرح ===
(Component: TEMPLATE_C_BLOCK.html)
Content: التَّعْبِيرِ عَنِ مَشَاعِرِ الفَرَحِ يَامِ الوَحْدَة:ِ

=== BLOCK 18: شواهد الفرح ===
(Component: TEMPLATE_C_POEM.html)
Bio: سلامة عبيد:
Verse: أَشْرَقَ الفَجْرُ فَالدُّرُوبُ ضِيَاءُ   وأَنَاشِيْدُ عِزَّة وحُدَاءُ
Verse: إِنَّهَا فَرْحَةُ الْحَيَاةِ فَمِيدِي       يَا رَاوَابِي وَهَلِلِي يَا سَمَاءُ
۱۲۹

--- END STREAM ---
