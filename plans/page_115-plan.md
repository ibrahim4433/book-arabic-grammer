# **SESSION 115**

[TASK DEFINITION]
Objective: Implement page 115.
File: `pages/page_115.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide: NO INLINE STYLES. Irab Words inside `.irab-word` MUST be white.
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX') on the replacing `<div>` tag instead of `<section>`.
8. Self-Correction: Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...) .
11. You must preserve the exact Tashkeel provided in the input.
12. Visual Density: The page must be dense.
13. balanced page colors between teal and orange: minimum 1 element in orange.
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html`.
15. Exam section always be in the end of the lesson (in the final page of that lesson) and without the answers!

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 115
[CHAPTER_TITLE]: page 115
[CATEGORY_HEADER]: 115
[SECTION_HEADER]: 115
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Poem Continuation ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
Title: أبيات القصيدة
Content:
[TEMPLATE_C_POEM.html]
- ٣٦- لمتِ الآلام منا شملنا | وغت ما بيننا من نسب
- ۳۷- فإذا مصر أغاني جلق | وإذا بغداد نجوى يشرب
- ۳۸- ذهبت أعلامها خافقة | والتقى مشرقها بالمغرب

=== BLOCK 3: Explanation List 1 ===
(Component: TEMPLATE_C_LIST.html)
- المفردات: <span class="highlight-red">لمت</span>: جمعت. <span class="highlight-red">نسب</span>: الصلة والقرابة. <span class="highlight-red">نجوى</span>: إسرار الحديث.
- الشرح: مصائب البلاد العربية وأوجاعها وَحَدَتْ مَشَاعِرَ أَبنائها، فَبِسَبَبِ هذه المصائب والأوجاع ازدادت روابط القرابَةِ قُوَّةَ بَيْنَهُم. تَوَحْدَتِ المشاعِرُ فِي الأَقْطَارِ العَرَبِيَّة،ِ فَفَرْحَةً مِصْرَ ارتَسَمَتْ على مُحَيَّا شَعْبِ سُورية، وما يجري في العراق يَتَرَدَّد صداه في أنحاء الحجاز. حيث ارتفَعَتْ أَعْلَامُها خَفَاقَةً تُرَفْرِفُ ابتهاجًا وَفَرَحًا مِنْ شَرْقِ الوَطَنِ الْعَرَبِيِّ إِلَى غَرْبِه.ِ
- الفكرة: المصائب تُقَوّي الروابط القَوْمِيَّةَ بَيْنَ أَبناء الأُمَّةِ العربية. تصوير وِحْدَةِ المشاعِرِ فِي الأَقْطَارِ العربية.
- البلاغة: <span class="highlight-blue">(مشرقها المغرب)</span>: طباق إيجاب.

=== BLOCK 4: Irab Row 1 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
- <span class="irab-word">شملنا</span>: مَفْعُولٌ بِهِ مَنْصُوبٌ
- <span class="irab-word">ما</span>: اسمٌ مَوْصُولُ فِي مَحَلَّ نَصْبَ مَفْعُولَ بِهِ.
- <span class="irab-word">إذا</span>: فجائية.
- <span class="irab-word">مصر</span>، <span class="irab-word">بغداد</span>: مُبْتَدَاً مَرْفُوع
- <span class="irab-word">أغاني</span>، <span class="irab-word">نجوى</span>: خَبَرٌ مَرْفُوع
- <span class="irab-word">جلق</span>، <span class="irab-word">يشرب</span>: مُضَافُ إِلَيْهِ مَجْرُور.ٌ
- <span class="irab-word">أعلامها</span>، <span class="irab-word">مشرقها</span>: فاعِلٌ مَرْفُوع
- <span class="irab-word">خافقة</span>: حال منصوب.

=== BLOCK 5: Poem 2 ===
(Component: TEMPLATE_C_POEM.html)
- ٣٩- كلما انقض عليها عاصف | دفته في ضلوع السحب
- ٤٠- بورك الخطب، فكم لف على | سهمه أشتات شعب مغضب
- ٤١- عروس المجد حسبي عزة | أن أرى المجد انثنى يعتز بي

=== BLOCK 6: Explanation List 2 ===
(Component: TEMPLATE_C_LIST.html)
- المفردات: <span class="highlight-red">شت</span>: متفرق، <span class="highlight-red">أشتات</span>: شَنَّتِ الأشياء شتاتًا تَفَرَّقَتْ مفردها: الشت. <span class="highlight-red">انثنى</span>: انحنى. <span class="highlight-red">يعتز</span>: يَفْتَخِرُ.
- الشرح: كلما هاجم الأمة العربيةَ عَدُوٌّ تَخَلَّصَتْ مِنْه،ُ وَكُلَّمَا أَلَمَّتْ بِمَا مُصِيبَةٌ وَاجَهَتُها وتَخَلْصَتْ مِنْها وتفادَتْ آثارها. ليبارك الباري الْمَصَائِبَ وَالمِحَن،َ فَمَا أكثر المرات التي اجتمع فيها شمل أبناء الأُمَّةِ العربية الناقمِين على الظلم والعدوان. أَيَّتُها احرَيَّةُ يَكْفِينِي عِزَّةً وافتخارا رُؤْيَةُ الْمَجْدِ مُنحَنِيَا أَمَامَ عَظَمَةِ أَبْنَاءِ الوَطَنِ مُقَدِّرًا لَهُم.
- الفكرة: المصائب سَبَبْ فِي وَحْدَةِ الأُمَّةِ العَرَبَيَّة.ِ تَقْدِيرُ المَجْدِ لأبناء الوطن.
- الشُّعُور: افتخار واعتزاز. الأداة: التراكيب. المثال: كلما انقض عليها عاصف دفنته. أرى المجد انثنى يعتز بي.
- البلاغة: <span class="highlight-blue">(انقض السحب)</span>، <span class="highlight-blue">(ضلوع)</span>، <span class="highlight-blue">(المجد انثنى)</span>، <span class="highlight-blue">(المجد يعتز)</span>: استعارَةُ مَكْنِيّة.

=== BLOCK 7: Irab Row 2 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
- <span class="irab-word">الخطب</span>: نائب فاعِلِ مَرْفُوعٌ
- <span class="irab-word">كَمْ</span>: خَبَرَيَّةٌ مَبْنِيَّةٌ على السكون في محل نَصْبَ مَفْعُولُ مُطْلَق
- <span class="irab-word">أشتات</span>: مَفْعُولُ بِهِ مَنْصُوب.ٌ
- <span class="irab-word">مغضب</span>: صِفَةٌ مَجْرُورَة.ٌ
- <span class="irab-word">حسبي</span>: مبتداً مَرْفُوعُ
- <span class="irab-word">عَزة</span>: تمييز مَنْصُوب
- <span class="irab-word">أن أرى المجد انثنى</span>: الْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ رَفْعِ خبر.
- <span class="irab-word">(أرى)</span>: صِلَةُ المَوْصُولِ الحرفي لَا مَحَلَّ لَهَا مِنَ الإعراب.
- <span class="irab-word">(انثنى)</span>: في مَحَلِّ نَصْبَ مَفْعُولُ به ثان.
- <span class="irab-word">(يعتز)</span>: في محل نصب حال.
- <span class="irab-word">(عروس المجد)</span>: استثنافِيَّةٌ لا محل لها مِنَ الإعراب.
- <span class="irab-word">جملة (عليها عاصف)</span>: في محل جر بالإضافة. <span class="irab-word">(انقض عليها عاصف دفنته)</span>: لا محل لها مِنَ الإعراب. جُمْلَةُ جَوابِ الشَّرْطِ.

=== BLOCK 8: Poem 3 ===
(Component: TEMPLATE_C_POEM.html)
- ٤٢- أنا لولاه لما طوفت في | كل قفر مترام مجدب
- ٤٣- رب لحن سال عن قيثارتي | هز أعطاف الجهاد الأشيب
- ٤٤- لبلادي ولرواد السنا | كل ما ألهمتني من أدب

=== BLOCK 9: Explanation List 3 ===
(Component: TEMPLATE_C_LIST.html)
- المفردات: <span class="highlight-red">قفر</span>: القَفْرُ الخلاءُ مِنَ الأَرْضِ لا ماء فيه ولا ناس ولا كلا. <span class="highlight-red">مجدب</span>: جَدَبَ المكان: يَبِسَ لاحتباس الماء فيه. الأَراضي الخالية القاحِلَة.ِ
- الشرح: لولا رَغْبَتِي بِبُلُوعُ الْمَجْدِ لِمَا طَوَيْتُ الْمَسَافَاتِ الشَّاسِعَة،َ وجُبْتُ. كَثِيرٌ مِنَ القصائد التي جادَتْ بِمَا قَرِيحَتِي الشَّعْرِيَّةِ بَثَتْ روح الكفاح المُوَقَّر والتضالِ المُشَرَفِ فِي نُفُوس أبناء الأمة. أُهْدِي شِعْرِي وَكُلَّ أَدَبٍ أَلْهَمْتِنِي إِيَّاهُ أَيَّتُهَا احرَيَّةُ لوطني ولأبنائه الذين ارتقوا إلى ذرا الْمَجْد.ِ
- البلاغة: <span class="highlight-blue">(لحن سال)</span>، <span class="highlight-blue">(الجهاد الأشيب)</span>: استعارَةً مَكْنِيَّة.ٌ

=== BLOCK 10: Irab Row 3 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
- <span class="irab-word">لما</span>: اللام واقعة في جواب لولا.
- <span class="irab-word">ما</span>: حَرْفَ نَفي.
- <span class="irab-word">قفر</span>: مُضاف إليه مجرور
- <span class="irab-word">مترام</span>، <span class="irab-word">مجدب</span>: صفة مجرورة.
- <span class="irab-word">رَبَّ</span>: حَرْفُ جَرّ شَبِيه بِالزَّائِد.
- <span class="irab-word">لحن</span>: اسمٌ مَجْرُورٌ لَفَظًا مَرْفُوعٌ مَحَلَّا على أَنَّهُ مُبْتَدَا.ً
- <span class="irab-word">(سال)</span>: في محل رفع صفة.
- <span class="irab-word">(هز)</span>: في محل رفع خبر.
- <span class="irab-word">أعطاف</span>: مَفْعُولُ بِهِ مَنْصُوبٌ.
- <span class="irab-word">الجهاد</span>: مُضاف إلَيْهِ مَجْرُورُ.
- <span class="irab-word">الأشيب</span>: صِفَةً مَجْرُورَة.ُ
- <span class="irab-word">كل</span>: مُبْتَدَاً مَرْفُوع
- <span class="irab-word">ما</span>: اسمٌ مَوْصُولُ فِي مَحَلِّ جَرّ بالإضافة.
- <span class="irab-word">(ألهمتني)</span>: صِلَةُ المَوْصُولِ لَا مَحَلَّ لها مِنَ الإغراب.

=== BLOCK 11: الفوائد العامة ===
(Component: TEMPLATE_C_TABLE.html)
Columns: <span class="text-accent">المفهوم</span> | <span class="text-accent">التوضيح</span>
Row 1: الشُّعُور | افتخار واعتزاز
Row 2: الفكرة | المصائب تُقَوّي الروابط القَوْمِيَّةَ
Row 3: البلاغة | استعارة مكنية، طباق إيجاب

--- END STREAM ---
