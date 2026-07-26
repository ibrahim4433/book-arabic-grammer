# **SESSION 184**

[TASK DEFINITION]
Objective: Implement page 184.
File: `pages/page_184.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html`.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide: NO INLINE STYLES. Irab Words inside `.irab-word` MUST be white. Replace any `<section>` tags from the templates with `<div>` tags (keep `<header>`).
7. Unique IDs: All content blocks must have a unique ID. Use "Jules-workspace/id_manager.py".
8. Self-Correction: Run "Jules-workspace/lint_pages.py --one-page-mode pages/page_184.html".
12. Visual Density: The page must be dense. Do NOT leave empty space.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html`.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 184
[CHAPTER_TITLE]: page 184
[CATEGORY_HEADER]: 184
[SECTION_HEADER]: 184
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Intro ===
(Component: TEMPLATE_C_BLOCK.html)
Title:
Content: بَعْضَ الأبيات التي نُظِمَتْ على مَجْزُوءِ الرَّمَل،ِ على النحو الآتي:

=== BLOCK 3: Matrix ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: المَقْطُوعَةُ الأولى
[HEADER_2]: (مقطوعة الخير):
[HEADER_3]: يرى جبران فيها
[CELL_1]: أَنَّ النَّاسَ مَفَطُورون على الشر،
[CELL_2]: وأنَّ الشَّرَّ متأصل في نفوسهم البَشَرَيَّةِ حَتَّى بَعْدَ الْمَمَات،ِ
[CELL_3]: وأنهم لا يقدمون الخير إلا إذا أجبروا على ذلك،

=== BLOCK 4: Topic 1 ===
(Component: TEMPLATE_C_BLOCK.html)
Title:
Content: <span class="text-accent">فالخير ليس من جبلتهم.</span> كما أشار جبران إلى أنَّ الزَّمَنَ يُعْيِّرُ نفوس النَّاسِ الضُّعْفَاءِ وَيَتَحَكْمُ بِهم ويعبث بهم كالآلات، وأكد أنه لا بد من مجيء يوم يتحرر فيه النَّاسُ مِن تَحْكُم هذا الزَّمَنِ العَابِث،ِ ودعا جبران الناس إلى التَّوَاضُعِ وَعَدَمِ الْمُبَاهَاةِ بالجاه والمجد والعلم، ووصف جبران النَّاسَ بِالقَطِيع الذي يمشي خلف راعِيهِ دونَ تَفَكَّرٍ أو تبصر في السبيل وهذا هو سَبَبُ هَلَاكِهِمْ وَضَيَاعِهِم.ْ كَمَا دَعَا أَيضًا إلى العودة إلى عالم الغَابِ؛ حيثُ الحرية المطلقة، والطبيعة الملهمة دون وجود عوائق وتَيَّارات تؤثر على البشر.

=== BLOCK 5: Poem 1 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: ومن هذه المَقْطُوعَة :
[RIGHT_HEMISTICH_1]: لَيْسَ فِي الغَابَاتِ رَاع
[LEFT_HEMISTICH_1]: لا ولا فيها القطيع
[RIGHT_HEMISTICH_2]: فالشِّتَا يَمْشِي وَلَكِنْ
[LEFT_HEMISTICH_2]: لا يُجَارِيهِ الربيع
[RIGHT_HEMISTICH_3]: خُلِقَ النَّاسُ عَبِيدًا
[LEFT_HEMISTICH_3]: لِلَّذِي يَأْبَى الخضوع
[RIGHT_HEMISTICH_4]: فإذا ما هَبَّ يومًا
[LEFT_HEMISTICH_4]: سَائِرًا سَارَ الجميع
[RIGHT_HEMISTICH_5]: أَعْطِنِي النَّايَ وَغَنِّ
[LEFT_HEMISTICH_5]: فَالْغِنَا يَرْعَى العُقُولُ
[RIGHT_HEMISTICH_6]: وأنين النَّاي أبقى
[LEFT_HEMISTICH_6]: مِنْ مَجِيدٍ وَذَليل

=== BLOCK 6: Topic 2 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المَقْطُوعَةُ الثَّالِثَةُ (مَقْطُوعَةُ العَدْلِ):
Content: <span class="text-accent">بالغ جبران في وصف منظومَةِ العَدْلِ التي أَسَّسَهَا الإنسانُ بِنَاءً على قُوَّةِ الأَفْرَاد،ِ</span> وأشار إلى أن العدل الذي يقيمه الإنسان من وجهة نَظَرِهِ هُوَ عَدْلٌ ظَالِمٌ في الوقتِ ذَاتِه،ِ فالضَعِيفُ بَيْنَ قَوْمِهِ إِذَا ارْتَكَبَ خَطَأً صغيرًا يُعاقَبُ ويُعْتَبَرُ جُرمًا، بينما القوي عِندَمَا يَرْتَكِبُ خَطَأً يُصَفَقُ له ويُعتبر بطلا،

=== BLOCK 7: Benefit Warning ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[TITLE]: وبالغ جبران في وَصَفِهِ حِينَ قَالَ :
[CONTENT]: الجِنُّ والأموات تبكي مِن عَدْلِ الإنسانِ الزَّائِف الذي وصفه بالثَّلْجِ الزائل بعد سُطُوع أَشِعَةِ الشمس، ثم عاد إلى وصف الغاب مشيرا إلى أنه لا يوجد عِقَابٌ وَثَوَابٌ في الغابة، ولا تدخل في شؤون الآخرين، أو اعتراض على أفعالهم. ثم عاد جبران وكرر أن صوت الناي وترانيمه هما صوت الخلود الحقيقي.

=== BLOCK 8: Poem 3 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: ومن هذه المقطوعة:
[RIGHT_HEMISTICH_1]: لَيْسَ فِي الغَابَاتِ عَدْلُ
[LEFT_HEMISTICH_1]: لا ولا فيها العقاب
[RIGHT_HEMISTICH_2]: فَإِذا الصَّفْصَافُ أَلقى
[LEFT_HEMISTICH_2]: ظِلَّهُ فوق التراب
[RIGHT_HEMISTICH_3]: لا يَقُولُ السَّرو هَذِي
[LEFT_HEMISTICH_3]: بِدْعَةً ضد الكِتَاب
[RIGHT_HEMISTICH_4]: إِنَّ عَدْلَ النَّاسِ ثَلْجٌ
[LEFT_HEMISTICH_4]: إِنْ رَأَتْهُ الشَّمْسُ ذَابٌ
[RIGHT_HEMISTICH_5]: أَعْطِنِي النَّايَ وَغَنِّ
[LEFT_HEMISTICH_5]: فَالْغِنَا عَدْلُ الْقُلُوبُ
[RIGHT_HEMISTICH_6]: وأنينُ النَّاي يَبْقَى
[LEFT_HEMISTICH_6]: بَعْدَ أَنْ تَفْنَى الذُّنُوبُ

=== BLOCK 9: Topic 3 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المَقْطُوعَةُ الرَّابِعَةُ (مَقْطُوعَةُ العِلْم):
Content: أشار جبران إلى فَضْلِ العلم على الإنسان وَوَضَّحَ أَنَّ بِدَايَةَ طريق العِلْمِ معروفة ووَاضِحَةً لَدَى الجميع، أَمَّا نِهَايَتُهُ فتكون بانتهاء عُمر الإنسان وَقَدَرِه،ِ وَدَعَا الإنسان إلى التعلم والعيش بطموح. كما ساوى جبران الإنسان المتعلم المُنفَرِدَ بِعِلْمِهِ بِمَنْزِلَةِ النَّبِي،ِّ فالإنسان المتعلم عِلْمُهُ يَفْصِلُهُ عن النَّاسِ الذين يعتبرونَهُ غَرِيبًا بينهم، لأنهم لا يزالون يعيشون في الماضي. ووصف جبران الإنسانَ الْمُتَعَلِمَ بِالشَّدَّةِ والقُوَّةِ بالرغم مما يُظهره من لطف ولين في التعامل، ثم عاد جبران يُقارن ذلك مع قانون الغاب الذي تَخْتَفِي فيه ثنائية العلم والجَهْلِ وَشَبَّهَ عُلوم الإنسان بالضباب الذي يَزُولُ بِسُطُوع شمس الحقيقة، وعاد وكررَ أَنَّ صوت الناي والغناء هما أفضل العلوم الخَالِدَة،ِ

=== BLOCK 10: Poem 4 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: وَمِنْ هذه المَقْطُوعَة:
[RIGHT_HEMISTICH_1]: لَيْسَ فِي الغَابَاتِ عِلْم
[LEFT_HEMISTICH_1]: لا ولا فيها الجهول
[RIGHT_HEMISTICH_2]: فَإِذَا الْأَغْصَانُ مَالَتْ
[LEFT_HEMISTICH_2]: لَمْ تَقُل هَذَا الجليل
[RIGHT_HEMISTICH_3]: إِنَّ عِلْمَ النَّاسِ طُرًّا
[LEFT_HEMISTICH_3]: كَضَبَابِ فِي الحُقُولُ
[RIGHT_HEMISTICH_4]: فَإِذا الشَّمْسُ أَطَلَّتْ
[LEFT_HEMISTICH_4]: مِنْ وَرَا الْأُفْقِ يَزُولُ
[RIGHT_HEMISTICH_5]: أَعْطِنِي النَّايَ وَغَنّ
[LEFT_HEMISTICH_5]: فَالْغِنَا خَيْرُ العُلُومُ
[RIGHT_HEMISTICH_6]: وأنينُ النَّايِ يَبْقَى
[LEFT_HEMISTICH_6]: بَعْدَ أَنْ تَطْفَا النُّجُومُ

=== BLOCK 11: Cut Content Start ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
[BLOCK_TITLE]: المَقْطُوعَةُ الخَامِسَةُ (مَقْطُوعَةُ السَّعَادَة):
[CONTENT]: اعْتَقَدَ جبران أَنَّ السعادة وهم لا يتحقَّق، فَعِنْدَمَا يُحَقِّقُ الإنسانُ هَدَفَهُ يَمَلُّ ثُمَّ يُعيد البحث عن هدف آخر، وشبه ذلك بالنهر الجاري نحوَ السَّهْل،ِ فَعِنْدَمَا يَصِلُ النَّهْرُ السَّهْلَ يُصبح النَّهْرُ كَئِيبًا بَطِيْئًا يَبحث عن مجرى آخر. كمَا اعْتَقَدَ جبران أَنَّ سعادة النَّاسِ الحقيقية هي فقط في الطموح والأمل في تحقيق الشَّيْءٍ المرجو، ولكن بعد الحصول على هذا المراد تزول هذه السَّعَادَةُ الوَهْمِيَّةُ، ورأى جبران أَنَّ الإنسان السعيد هو الذي ينشغل في تحقيق أهدافه، ثم عاد إلى قانون الغاب حيث تَخْتَفِي معادلة الطلب وَالْمَلَلِ؛ لَأَنَّهُ يَعْتَبَرُ أَنَّ

--- END STREAM ---
