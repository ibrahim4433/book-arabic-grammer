# **SESSION 160**

[TASK DEFINITION]
Objective: Implement page 160.
File: `pages/page_160.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules.
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md`.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   **Rule:** NO INLINE STYLES.
*   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
*   **Mapping:**
    *   `style="width: 20%"` -> `class="w-20pct"`
    *   `style="margin-top: 2mm"` -> `class="mt-2mm"`
    *   `style="text-align: center"` -> `class="text-center"`
    *   `style="font-weight: bold"` -> `class="font-bold"`
6. Templates: You are forbidden from inventing new HTML tags or classes or template elements. You must map all content using "Jules-workspace/Templates/" components. **CRITICAL 1-PAGE MODE RULE**: You MUST NOT use `<section>` tags when applying templates. Replace any `<section>` tags from the templates with `<div>` tags (keep `<header>` for page headers as is).
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). The ID MUST be applied to the `<div>` tag that replaced the `<section>` tag. Use "Jules-workspace/id_manager.py" to generate or verify them.
8. **Self-Correction:** Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...) .
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense. Do NOT leave empty space.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`).
15. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 160
[CHAPTER_TITLE]: page 160
[CATEGORY_HEADER]: 160
[SECTION_HEADER]: 160
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Exercises ===
(Component: TEMPLATE_C_LIST.html)
Item 1: حَوَلِ الفِعْلَ الوارد في الجملة الآتية إلى صِيعَةِ الْمَبْنِي لِلمَجْهُول،ِ ثُمَّ ا بْطِ الجُمْلَةَ بِالشَّكْل:ِ )فَرَّقَ رُوْحًا عَنْ جَسَ .( ج فَرَقَتْ رُوْحٌ عَنْ جَسَد.ٍ
Item 2: - اذْكُرُ مَصْدَرَ كُلِّ مِمَّا يَاتِي: )تَجَافَى، تَرْتَدُّ أَبَاحُوا، رَسَتْ(. ج - تَجَافى : تَجَافِي. - تَرْتَد: ارتداد - أباحوا: إِبَاحَة. - رَسَتْ رُسُو.
Item 3: ه - عَلِلْ كِتَابِةَ الهَمْرَةِ الأَوَّلِيَّةِ على صورتها فيما يأتي: الْمَامًا، أدعوك، اهتدي(. ه - الْمَامًا : هَمْرَةً قَطع جاءَتْ فِي مَصْدَرِ الفِعْلِ الرباعي. - أدعوك : هَمْرَةُ قَطْع،ِ زائدةً لِلْمُضَارَعَة. - اهتدى هَمْرَةُ وَضْلِ جَاءَتْ فِي فِعْلِ مَاضٍ خُمَاسِي.
Item 4: - اكْتُبْ كَلِمَةً )شَاطِي في صِيعَةِ المُتَتَّى، ثُمَّ الجمع، وعلل كتابة الهمزة في كلنا الحالتين. - صيغة المنى: شاطِنَانِ هَمْرَةً مُتوسطة،ٌ مَفْتُوحَةٌ سُبِقَتْ بِكُسْر - صيغة الجمع: شواطئ؛ هَمَةً مُتَطَرَفَة،ٌ مَسْبُوقَةٌ بِكُسْر.ِ

=== BLOCK 3: Detailed Analysis ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تحليل مفصل لمضمون الأبيات:
Content: تحليل مفصل لمضمون الأبيات:

=== BLOCK 4: Verse 1 ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: وطني، أَيْنَ أَنَا بِمَّنْ أَوَدُ؟
Hemistich 2: أو ما لِلحَظِّ بَعْدَ الجَزْرِ مَدٌ؟

=== BLOCK 5: Verse 1 Explanation ===
(Component: TEMPLATE_C_LIST.html)
Item 1: <span class="text-accent">المفردات:</span> أود: أَرْغَبُ وأُحِبُّ. الجزر: انحِسَارُ الماء. مد: انبساط الماء وامتِدَادُهُ.
Item 2: <span class="text-accent">الشرح:</span> وَطَنِي الحبيب لقد أصبحت بعيدا عن بيتي وأهلي وصحبي، بعد أن أخذنِي جَزْرُ البَحْرِ مِنْ شَاطِئِكَ إِلى شاطئ الغربة، فهل من حسن طالع يُعْقِبُ هذا الجزر بم يعيدني إليك؟!
Item 3: <span class="text-accent">الفكرة:</span> المعاناةُ بِسَبَبٍ تَرْكِ الوَطَنِ وَالأَهْلِ قَسْرًا )الحنينُ الدَّائِمُ لِلدِّيا (.
Item 4: <span class="text-accent">الشعور:</span> الشوق والحنين
Item 5: <span class="text-accent">الأداة:</span> التراكيب
Item 6: <span class="text-accent">المثال:</span> أَوَ مَا لِلحَظ بَعْدَ الجَزْرِ مد. البلاغة: أسلوب إنشاء طلبي نداء(: )وَطني(. أسلوب إنشاء طلبي )استفهام(: )أَيْنَ أَنا مِمَّنْ أَوَدُ ،( )أَوَ مَا لِلحَقِّ بَعْدَ الجَزْرِ مَنْ؟(.
Item 7: <span class="text-accent">الأساليب:</span> )أَيْنَ أنا(: تَقَدَّمَ الخبر على المبتدا؛ لأنَّهُ مِنْ أسماء الصَّدارة )اسم استفهام(. )الحظ بَعْدَ الجَزْرِ مَن(: تَقَدَّمَ الخَبَرُ على المبتدا؛ لأنه شبه جملة والمبتدأ نكرة. الإعراب

=== BLOCK 6: Verse 1 Parsing ===
(Component: TEMPLATE_C_IRAB.html)
Word 1: وطني
Analysis 1: مُنَادَى مُضَافُ مَنْصُوب، وعلامَةُ نَصْبِهِ الفَتْحَةُ المُقَدَّرَةُ على ما قَبْلَ يَاءِ المَتَكَلِم،َ مَنَعَ ظُهُورَهَا اشْتِغَالُ المحل بالحركَةِ المُنَاسِبَة.ِ فِي مَحَلِّ نَصْب،ِ والياء، ضمير متصل مبني على السكون في محل جر، مُضَاف إليه.
Word 2: أَيْنَ
Analysis 2: اسم استفهام، مَبْنِي على الفَتْحَةِ مَفْعُولُ فِيهِ ظَرْفُ مَكَان.ٍ مُتَعَلِقٌ بِخَبَرَ مُقَدَّم مخذُوفٍ
Word 3: أنا
Analysis 3: ضميرُ رَفْعِ مُنْفَصِل،ٌ مَبْنِي على السُّكُونِ فِي مَحَلِّ رَفْع،ِ مُبْتَدَا،ً
Word 4: مِنْ
Analysis 4: مِنْ حَرْفُ جَرٍ
Word 5: مَنْ
Analysis 5: اسم مَوْصُولُ مَبْنِي على السُّكُونِ فِي محل جرٍ بِحَرْفِ الجَرِ
Word 6: أَوَدُ
Analysis 6: فِعْلَ مُصَارِعٌ مَرْفُوع، وعلامَةُ رَفْعِهِ الصَّمَّةُ الظَّاهِرَةُ
Word 7: أَوَ
Analysis 7: ها الحمزة، حرف استفهام والواو، زائِدَة،ٌ
Word 8: مَا
Analysis 8: حَرْفُ نَفي.
Word 9: بَعْدَ
Analysis 9: مَفْعُولُ فِيهِ ظَرْفُ زَمَانٍ مَنْصُوبُ
Word 10: الجزر
Analysis 10: مُضَاف إليهِ مَجْرُورٌ
Word 11: مَدْ
Analysis 11: مُبْتَدَأٌ مُوَخَّرٌ مرفوع، وعلامةُ رَفْعِهِ الصَّمَةُ الظَّاهِرَة،ُ وسُكِنَ لِلضَّرُورَةِ الشَّعْرِيَّةِ وَسُكِّنَ لِلضَّرَورَةِ الشَّعْرِيَّةِ
Word 12: جملة )أَيْنَ أنا(
Analysis 12: استئنافية، لا محل لها من الإعراب
Word 13: جملة )أَوَ (
Analysis 13: صِلَةَ الْمَوْصُول،ِ مِنَ الإعراب. لا محل لها من الإعراب
Word 14: جمله )أَ وَمَا لِلحَظ ... مد(
Analysis 14: استئنافية، لا محل لها

=== BLOCK 7: Verse 2 ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: ما رَسَتْ حَيْثُ رَسَتْ فُلْكَ النَّوى
Hemistich 2: لو أباحوا لِي فِي الدَّفْةِ يَد!

=== BLOCK 8: Verse 2 Explanation ===
(Component: TEMPLATE_C_LIST.html)
Item 1: <span class="text-accent">المفردات:</span> رَسَتْ تَوَفَّفَتْ عَنِ الْمَسِير فلك: سفينة النوى البعد الدفة السكان، وهو آلَةً فِي مُؤَخَرَةِ السَّفِيْنَةِ حَرِّكُهَا بَعَيْنَا أَو يَسَارًا.
Item 2: <span class="text-accent">الشرح:</span> لو امتلكت ناصية أمري وَكَانَ مِقْوَدُ سَفِينَةِ البُعْدِ بِيَدي لما جَعَلْتُهَا تُبْعِدُنِي عَنْكَ وَتُلْقِي بي في شاطئ الغُرْبَةِ
Item 3: <span class="text-accent">الفِكْرَةِ:</span> التَّعْبِيرُ عَنِ الغربة القسرية.
Item 4: <span class="text-accent">البلاغة:</span> )مَا رَسَتْ رَسَتَ(: طباق سَلْب الإعراب:

=== BLOCK 9: Verse 2 Parsing ===
(Component: TEMPLATE_C_IRAB.html)
Word 1: ما رَسَتْ
Analysis 1: ما، حَرْفُ نَفْي. رَسَت،ْ فعل ماضِ مَبْنِي على الفَتْحَةِ الْمُقَدَّرَةِ على الألف الْمَحْدُوفَةِ؛ لاتِصَالِهِ بِنَاءِ التَّأْنِيثِ السَّاكِيَة.ِ والنَّاء،ُ حَرْفُ تَأْنيث لا مَحَلَّ لَهُ مِنَ الإعراب.
Word 2: حيث
Analysis 2: اسم مبني على الصَّمَةِ فِي مَحَلَ نَصْب،ِ مَفْعُولُ فِيهِ ظَرْفُ مَكَانٍ
Word 3: فَلْكَ
Analysis 3: فَاعِلَ مَرْفُوعُ
Word 4: النوى
Analysis 4: مُضَاف إليهِ مَجْرُورٌ
Word 5: لو
Analysis 5: حَرْفُ شَرْطٍ غَيْرُ جَازِم.
Word 6: أَبَاحُوا
Analysis 6: فعل ماض، مَبْنِي على الصَّمَّةِ لاتصاله واو الجماعة والواو، ضميرٌ مُتَصِلَ مَبْنِي على السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ والآلِفُ حَرْفُ تَفْرِيقِ
Word 7: يَدْ
Analysis 7: مَفْعُولُ بِهِ مَنْصُوب،ُ وعلامَةً نَصْبِهِ الفَفْحَةُ الظَّاهِرَة.ُ وسُكِنَ لِلضَّرُورَةِ البَعْرِيَّةِ
Word 8: جملة )ما رَسَتْ ... فلك النوى(
Analysis 8: استئنافية، لا تحل لها مِنَ الإعراب
Word 9: جمله )رَسَتْ(
Analysis 9: مُضَاف إليه، محلها الجر.
Word 10: جملة )أباحوا(
Analysis 10: جملة الشَّرْطِ غَيْرِ الظَّرْي،َ لا محل لها مِنَ الإعراب.

=== BLOCK 10: Verse 3 ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: غابَ خَلْفَ البَحْرِ عَنِّي شَاطِي
Hemistich 2: كُلُّ مَا أَرَّقَنِي فِيهِ رَقَدْ

=== BLOCK 11: Verse 3 Explanation ===
(Component: TEMPLATE_C_LIST.html)
Item 1: <span class="text-accent">المفردات:</span> أَرْقَنِي جَعَلَ النَّوْمَ يَمْتَنِعُ عليَّ لَيْلًا، فالأرق الامتناع عَنِ النَّوْمِ لَيْلًا رَقَد : استقر
Item 2: <span class="text-accent">الشرح:</span> صار البحر الذي سَلَكْتُهُ لأَبْلُغَ غُرْبَتِي، فاصلا غيب عن ناظري ذلك الشاطئ الذي استقر فيه كلُّ مَنْ حَرَمَتْنِي فُرْقَتُهُم نومَ لَيْلِي
Item 3: <span class="text-accent">الفكرة:</span> المعاناةُ بِسَبَبِ تَرْكِ الوَطَنِ وَالْأَهْلِ قَسْرًا )الحنين الدائم للديار(. الإعراب:

=== BLOCK 12: Verse 3 Parsing ===
(Component: TEMPLATE_C_IRAB.html)
Word 1: خَلْفَ
Analysis 1: مَفْعُول فيهِ ظَرَّفُ مَكَانٍ مَنْصُوبُ
Word 2: الْبَحْرِ
Analysis 2: مُضَافَ إِلَيْهِ يَجْرُورُ
Word 3: شَاطِي
Analysis 3: فَاعِلَ مَرْفُوعَ
Word 4: كُلُّ
Analysis 4: مُبْتَدَاً مرفوع
Word 5: ما
Analysis 5: اسم مَوْصُولُ مَبْنِي على السكون فِي مَحَلَ جَر،ٍ مُضَاف إليه.
Word 6: أَرْقَنِي
Analysis 6: فِعْلَ مَاضِ مَبْنِي على الفَنْحَةِ الظَّاهِرَة.ِ والنون،ُ حَرْفُ وَقَايَة.ٍ والياء، ضميرٌ مُتَصِلِّ مَبْنِي على السُّكُونِ فِي مَحَلِ نَصْب،ِ مَفْعُولُ بِهِ
Word 7: رَقَدْ
Analysis 7: فِعْلَ مَاضِ مَبْنِي على الفَتْحَةِ الظَّاهِرَة.ِ وسُكْنَ لِلضرورة الشَّعْرِيَّة.ِ
Word 8: جملة )غاب ... شاطئ(
Analysis 8: استئنافية، لا تحل لها مِنَ الإعراب
Word 9: جملة )أَرْقَنِي(
Analysis 9: صِلَةُ الْمَوْصُول،ِ لَا مَحَلَّ لَهَا مِنَ الإعراب
Word 10: جملة )كُلُّ مَا أَرْقَنِي فِيهِ رَقَد(
Analysis 10: صِفَة،ٌ مَحَلَّهَا الرَّفْعُ
Word 11: جملة )رَقَدْ(
Analysis 11: خَبَرَيَّة،ٌ مَحَلَّهَا الرَّفْع.ُ

=== BLOCK 13: Core Matrix of Exercises ===
(Component: TEMPLATE_C_TABLE.html)
Col 1 Header: السؤال
Col 2 Header: الإجابة
Row 1 Col 1: حَوَلِ الفِعْلَ الوارد في الجملة الآتية إلى صِيعَةِ الْمَبْنِي لِلمَجْهُول،ِ ثُمَّ ا بْطِ الجُمْلَةَ بِالشَّكْل:ِ )فَرَّقَ رُوْحًا عَنْ جَسَ .(
Row 1 Col 2: ج فَرَقَتْ رُوْحٌ عَنْ جَسَد.ٍ
Row 2 Col 1: - اذْكُرُ مَصْدَرَ كُلِّ مِمَّا يَاتِي: )تَجَافَى، تَرْتَدُّ أَبَاحُوا، رَسَتْ(.
Row 2 Col 2: ج - تَجَافى : تَجَافِي. - تَرْتَد: ارتداد - أباحوا: إِبَاحَة. - رَسَتْ رُسُو.
Row 3 Col 1: ه - عَلِلْ كِتَابِةَ الهَمْرَةِ الأَوَّلِيَّةِ على صورتها فيما يأتي: الْمَامًا، أدعوك، اهتدي(.
Row 3 Col 2: ه - الْمَامًا : هَمْرَةً قَطع جاءَتْ فِي مَصْدَرِ الفِعْلِ الرباعي. - أدعوك : هَمْرَةُ قَطْع،ِ زائدةً لِلْمُضَارَعَة. - اهتدى هَمْرَةُ وَضْلِ جَاءَتْ فِي فِعْلِ مَاضٍ خُمَاسِي.
Row 4 Col 1: - اكْتُبْ كَلِمَةً )شَاطِي في صِيعَةِ المُتَتَّى، ثُمَّ الجمع، وعلل كتابة الهمزة في كلنا الحالتين.
Row 4 Col 2: - صيغة المنى: شاطِنَانِ هَمْرَةً مُتوسطة،ٌ مَفْتُوحَةٌ سُبِقَتْ بِكُسْر - صيغة الجمع: شواطئ؛ هَمَةً مُتَطَرَفَة،ٌ مَسْبُوقَةٌ بِكُسْر.ِ

--- END STREAM ---
