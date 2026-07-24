# **SESSION 134**

[TASK DEFINITION]
Objective: Implement page 134.
File: `pages/page_134.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools. If it overflows, it is a catastrophic failure. Do NOT try to solve overflow by deleting text (Strict Typographer Rule). Solve it by choosing denser templates or omitting optional white-space.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`. Ensure exact visual continuity (same title, same classes).
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md` to identify the correct template to use for the continuation. You are forbidden from guessing. Scan the raw text for the preceding keyword to determine the active template and apply the correct `_PART_2.html` wrapping.
3. Text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice. (Corrected OCR typos per the Typo Exception to reconstruct the scattered text logically).
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`, `.highlight-green` for secondary.
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
8. **Self-Correction:** Run "Jules-workspace/lint_pages.py --one-page-mode pages/page_134.html" after creating html files. If it fails, you MUST fix the errors (usually inline styles or forbidden section tags) before submitting.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...) .
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
13. Balanced page colors between teal and orange: make sure every page has minimum 1 element in orange instead of all teal.
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
15. Exam section always be in the end of the lesson (in the final page of that lesson), and without the answers! (Note: Skipped as no exam questions exist in the raw text per Strict Typographer Rule).

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 134
[CHAPTER_TITLE]: page 134
[CATEGORY_HEADER]: 134
[SECTION_HEADER]: 134
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Continuation from Previous Page ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
Content: التي هَبُّوا فِي وَجْهِ الدُّخَلَاءِ فِي غَضْبَةٍ عَارِمَةٍ، وَثَوْرَةٍ لاهِبَةٍ لِلكِفَاحِ والنِّضَالِ لِتَحْرِيرِ وَطَنِهِم وإعادةِ وَحْدَتِهِ التي مُزِّقَتْ، واسترداد حريته التي سُلِبَتْ بِرُوحِ الثَّوْرَةِ. وقد استَجَابَ الأَدَبُ العَرَبِيُّ لِهذا التطور الخلاقِ في النفسِ الْعَرَبِيَّةِ، فَوَاكَبَ مَسِيرَةِ النِّضَالِ، وَشَحَنَ النُّفُوسَ لِلكفاح لِتَحْرِيرِ الأُمَّةِ المُسْتَعْبَدَةِ وَتَوْحِيدِ الوَطَنِ المُمَزَّقِ.

=== BLOCK 3: مواكبة الأدب للنضال ===
(Component: TEMPLATE_C_BLOCK.html)
Content: فقد قام الأدباء بالتعبير عَنِ الفَرَحِ بِجَلَاءِ <span class="highlight-blue">الْمُسْتَعْمِرِ الغَرْبِيِّ</span>، ذَلِكَ أَنَّ يَوْمَ السابع عشرَ مِنْ نَيْسَان، عَامَ سِتَّةٍ وأربعين وتِسْعِمِئَةٍ وَأَلْف، يوم مجيد، وصفحة مُشْرِقَةٌ فِي تاريخ سُوْرِيَّة؛ كَتَبَ سُطُورَهَا أَبْنَاؤُهَا الْأَبَاةُ بدمائهم. فقد زَلْزَلَ السوريون الأَرْضَ تَحْتَ أَقْدَام الفرنسيين بِثَورات لاهِبَةٍ حَارِقَةٍ عَمَّتْ كُلَّ مِنْطَقَةٍ مِنْ رُبُوعِ الوَطَنِ، أَنْسَتِ <span class="highlight-red">الْمُحْتَلَّ</span> الطَّامِعَ أَطْمَاعَهُ الْخَبِيْثَةَ التي يَرُومُ مِنْ وَرَائِهَا تَدْنِيْسَ الْأَرْضِ وَسَلْبَ الكَرَامَةِ حَيْثُ تَحَوَّلَتْ كُلُّ بُقْعَةٍ مِنْ بِقَاعِ سُورِيَّة إلى مِدْفَعٍ هَادِرٍ يَرْمِي الطَّامِعِينَ الغَادِرِينَ بِقَذَائِفِ النَّارِ الملتهبة؛ لِيُطَهِّرَ بِحِمَمِهَا المنصَهِرَةِ الْأَرْضَ وَيُحَرِّرَ الإِنْسَانَ. فالجلاء ثَمَرَةٌ لِكِفاح مُرٍّ خَاضَهُ الشَّعْبُ العربي في سورية منذ وَطِئَتْ أَقْدَامُ الْمُسْتَعْمِرِينَ أَرْضَ سُورية.

=== BLOCK 4: شعر بدر الدين الحامد ===
(Component: TEMPLATE_C_POEM.html)
Bio: فَمِنْ مَدِينَةِ النَّوَاعِيرِ يَقِفُ شَاعِرُ العاصي <span class="text-accent">بَدْرُ الدِّينِ الحَامِدِ</span> مُبْتَهِجًا مَزْهُوًّا فِي أَوَّلِ عِيدِ جَلَاءٍ عَنْ سُورية؛ ليتغنى بهذا المنجز العظيم، مُظْهِرًا فَرَحَهُ العَارِمَ، مُؤَكِّدًا أَنَّ الجَلَاءَ فَرْحَةٌ عَرَبِيَّةٌ، وَغَصَّةٌ عَرَبِيَّةٌ نَاشِبَةٌ لا يزيلها تعاقب السنين. يقول:
Verses:
يَوْمُ الجَلَاءِ هُوَ الدُّنْيَا وَزَهْوُهَا ... لَنَا ابْتِهَاجٌ وَلِلْبَاغِينَ إِرْغَامُ

=== BLOCK 5: شعر عمر أبو ريشة ===
(Component: TEMPLATE_C_POEM.html)
Bio: ومِنْ حَلَبَ يَنْهَضُ ابن منبج الشاعر <span class="text-accent">عُمر أبو ريشة</span> لِيُصَوَرَ فَرْحَةَ الانتصار بِجَلَاءِ <span class="highlight-red">الْمُحْتَلِّ</span> عَنْ أَرْضِ الوَطَنِ، فَيَطْلُبُ مِنَ الْحُرِّيَّةِ أَنْ تَسِيرَ بِزَهْوٍ وَفَخَارٍ فَوْقَ ثَرَى بلادنا، وأَنْ تَخْتَالَ كما تختال العروس، وتُجَرِّرَ أَذيالَ الشُّهُبِ السَّاطِعَةِ، وَتُزَيِّنَ بِهَا أَرْجَاءَ بِلَادِنَا، وَيُؤْكِّدُ أَنَّ لِقَاءَهَا قَدْ حَسُنَ وجاد بعد تلك الفرقة التي ضاقَ فِيهَا الصَّدْرُ من شِدَّة الوجد والشَّوْقِ يَقُولُ:
Verses:
يا عروس المجد تِيْهِي واسحبي ... فِي مَغَانِينا ذُيُولَ الشُّهُبِ
يا عروس المجدِ طَابَ الْمُلْتَقَى ... بَعْدَمَا طَالَ جَوَى المُغْتَرِبِ

=== BLOCK 6: تنبيه العدو الصهيوني ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: ومَعَ نَشْوةِ النَّصْرِ، وَغَمْرَةِ أَفراح الوَطَنِ بِهِ لَا يَنسَى الأَدَبَاءُ أَنَّ هَنَاكَ عَدُوًّا مُجْرِمًا ما زال يستبيحُ الأَرْضَ العَرَبِيَّةَ وَيَنْتَهِكُ حُرُمَاتِهَا ويَتَعَدَّى على مُقَدَّسَاتِها. هذا العَدُو هو <span class="highlight-red">الصَّهْيُونِيَّة</span> التي تَنْتَهِجُ مَبْدَأَ الاجْتِيَاحِ القَسْرِي، واحتلال أرض الآخرين بِقُوَّةِ السَّلَاحِ وَالنَّارِ؛ لِذَا نَجِدُ هَؤُلاء الأدباء يفضحون جرائم الصهاينة بحق أبناء <span class="highlight-blue">فلسطين</span>، حَيْثُ عَاشَ أبناء فلسطين في ظِلِّ المحتل الصهيوني وَاقِعًا صَعْبًا عَانَوْا فِيهِ مِنْ ظُلم المحتلين الطَّغَاةِ وإذلالهم،

=== BLOCK 7: ملخص الجرائم والمصير (The Core Matrix) ===
(Component: TEMPLATE_C_TABLE.html)
Header 1: ممارسات المحتل الصهيوني
Header 2: المصير الفاجع
Row 1 Col 1: فقد ظل هذا المحتل يَسُومُ الفلسطينيين ألوان الاضْطِهَادِ وَالقَهْرِ مِنْ تَشْرِيدٍ وَتَهْجِيرٍ إِلَى قَتْلٍ جَمَاعِيٍّ مُرَوِّعٍ بهدف إرْغَامِهِم على مُغَادَرَةِ البلاد،
Row 1 Col 2: فالشاعر محمود درويش يشير إلى المصير الفاجع الذي يلقاه الحالمون بالعودة إلى فلسطين حيث امتَلَأَ طريق عودتهم بجثث اختطف الصهاينة أرواحها وصادروا حياتها.

=== BLOCK 8: شعر محمود درويش ===
(Component: TEMPLATE_C_POEM.html)
Bio: يَقُولُ:
Verses:
كُلُّ القَوَافِلِ قَبْلَهُم غَاصَتْ ... وَكَانَ النَّهْرُ يَبْصُقُ ضِفَتَيْهِ
قِطَعًا مِنَ اللَّحْمِ الْمُفَتَّتِ ... في وُجُوهِ الْعَائِدِينَ

=== BLOCK 9: ملحمة الكفاح الفلسطيني ===
(Component: TEMPLATE_C_BLOCK.html)
Content: وحينما يُذكر اسم <span class="highlight-blue">فَلَسْطِينَ</span> يلوح في الأفق أغصان زيتون، وأشجار ليمون، وحجر يروي ملحمة الكفاح الدامي والثورة اللاهبة على أرض الرسالات السماوية. إنها مأساة فلسطين التي دخلت ميدان الأدب مانحة الكلمة معنى خاصا، والحَرْفَ طَعْمًا خاصا والأدب نكهة خاصة. فقد عاشَتِ القَضِيَّةُ الفلسطينية مع الأدباء، ولا سيما الأدباء الفلسْطِينيين، الذينَ تَنَفَّسُوا هواءَهَا وَرَافَقُوها في أَشَدِّ أَزْمَاتِهَا، وَأَعْظم انتصاراتها، فها هم يبرزون تمسك الفلسطينيين بِفِكْرَةِ النِّضَالِ فِي سَبِيلِ الوُجُودِ، فرغم كُلِّ مَا اقْتَرَفَتْهُ الصَّهْيُونِيَّةُ مِنْ جرائم وحشية، بحقِّ أَبْنَاءِ فِلَسْطِينِ إِلَّا أَنَّهُم لَم يَسْتَسْلِمُوا لَهَا، أو يهابُوا فَتْكَهَا، بل ظل الإصرار على النِّضَالِ حَادِيهِم، والتَّمَسُّكُ بالكِفَاحِ رَائِدَهُم فَقَدْ نَذَرُوا أَنْفُسَهُم للمطالبة بالحقوق والدفاع عَنِ الْأَرْضِ وَالكَرَامَةِ والعرض، فالتحمُوا بِتُرَابِ الوطن التحامًا عضويا متماسكا، فأصبحوا جزءًا لا يَتَجَزَّأُ مِنْهُ، حَتَى غدا الإنسان الفلسطيني عضوا مِن أَعْضَاء هَذِهِ الأَرْضِ، مُتَوَحِّدًا بِترابها.

=== BLOCK 10: شعر توفيق زياد ===
(Component: TEMPLATE_C_POEM.html)
Bio: فها هُوَ كَبِير شُعَرَاءِ الأَرْضِ الْمُحْتَلَّةِ الشَّاعِرِ <span class="text-accent">تَوْفِيقِ زَيَّادٍ</span> يَضَعُ نَفْسَهُ فِي مُوَاجَهَةٍ سَافِرَةٍ مَعَ عَدُوٍّ مُغْتَصِبٍ يُشَارِكُهُ أَرْضَهُ، فَيُعْلِنُ التَّحَدِّي بِنَبْرَةِ وَاثِقَةٍ لَا تعرف الاستسلام أو تُقِرُّ بِالإِذْعَان، مؤكدًا متابعة السَّيْرِ في طريق الكفاح والنِّضَالِ والْمُقَاوَمَةِ، والثبات في الأَرْضِ والتَّمَسُّكَ بها. يَقُولُ:
Verses:
أَهْوَنُ أَلْفَ مَرَّهُ ... أَنْ تُدْخِلُوا الْفِيلَ بِثَقُبِ إِبْرَهُ
مِنْ أَنْ تُمِيتُوا بِاضْطِهَادِكُم وَمِيضَ فِكْرَهُ ... وتَحْرِفُونَا عَنْ طَرِيْقِنَا الذي اخْتَرْنَاهُ
قَيْدَ شَعْرَهُ

=== BLOCK 11: الانقطاع للورقة القادمة ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
Content: وَمَعَ أَنَّ هِجْرَة الفلسطينين قد أَمْسَتْ حقيقة مرة لا مَنَاصَ مِن تَجَرُّعِ عَلْقَمِها، وَمَعَ أَنَّ اقْتِلَاعِ الفَلَسْطِينِي مِنْ أَرْضِهِ قَد بَاتَ أَمْرًا واقعا لا مَجَالَ لَعَدَمِ الاعتراف بِهِ، إِلَّا أَنَّ الفَلَسْطِينِي قَد سَيْطَرَ على أَشْوَاقِهِ العَمِيْقَةِ، وَرَوَّضَ حَنِيْنَهُ الوَثَّابَ لِأَرْضِ الْوَطَنِ التي

--- END STREAM ---
