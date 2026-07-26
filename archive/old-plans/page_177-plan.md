# **SESSION 177**

[TASK DEFINITION]
Objective: Implement page 177.
File: `pages/page_177.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. Verify layout using `verify_layout.py`.
3. Text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice. Typo exception applied to fix obvious OCR issues (e.g., القريا to الثريا, removing stray page numbers).
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`, `.highlight-green` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide: NO INLINE STYLES. Irab Words inside `.irab-word` MUST be white.
7. Templates: Use `Jules-workspace/Templates/` components. Replace any `<section>` tags from the templates with `<div>` tags (keep `<header>` for page headers as is).
8. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). The ID MUST be applied to the `<div>` tag that replaced the `<section>` tag. Use `id_manager.py` to generate or verify them.
9. Visual Density: At least 4 substantial content blocks, and ensuring balanced page colors by including an orange Warning box.
10. Wrapping: Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (`.force-new-page`).
11. Evaluation: Exam section always be in the end of the lesson, without the answers. The answer is placed in a preceding Benefit block.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 177
[CHAPTER_TITLE]: page 177
[CATEGORY_HEADER]: 177
[SECTION_HEADER]: 177
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: مناقشة النص ===
(Component: TEMPLATE_C_LIST.html)
Title: -
List Items:
- <span class="text-accent">وضح ارتباط النَّصَ بِعُنُوانِه،ِ</span> ج۱ - عُنُوانُ النَّصِ يرتبط بِمَضْمُونِهِ ارْتِبَاطًا ظاهِرًا، فَمَضْمُونُ النَّصِّ يَنْطَوِي على رَغْبَةٍ عَارِمَةٍ لَدَى جبران لِدَفْعِ الْإِنْسَانِ إِلَى رَفْضِ العالم المادي الفاني، واللجوء إلى عالم الطَّبِيْعَةِ الطَّاهِرِ؛ فهو يُؤْكَدُ أَنَّ الغَابَ عَالَمُ الْمَسَرَّاتِ وَالْأَمَل،ِ وَيَدْعُو إلى العيش في الغاب والاستمتاع بِسِحْرِه.ِ كما يَدْعُو إلى تَأْمُلِ طَبِيْعَةِ الغَابِ والاستمتاع بها.
- <span class="text-accent">٢- اذْكُرْ بَعْضَ صِفَاتِ عَالَمِ الشَّاعِرِ البَدِيلِ مِنَ الْغُرْبَةِ القَاسِيَة.ِ</span> ج ٢- هذا العالم البَدِيلُ يَخْلُو مِنَ الهم والحزن، ويمتلك طبيعة ساحِرَةً مُمْتِعَة،َ تَسْتَحِقُ مِنَ الإِنْسَانِ أَنْ يَنْصَرِفَ عَنِ الدنيا ويُدِيمَ التَّامل فيها.

=== BLOCK 3: مهارات القراءة ===
(Component: TEMPLATE_C_LIST.html)
Title: مهارات القراءة : القِرَاءَةُ الصَّامِمَةُ
List Items:
- بِمَ اسْتَعَانَ الشَّاعِرُ فِي نَصِهِ لِرَسْمِ مَلامِحٍ عَالَمِهِ المَتَخَيَّلِ ؟ ولم؟ ج -۱ استعان باللجوء إلى الطبيعة، ولا سيما طبيعة لبنانَ السَّاحِرَة التي حفظ مَنَاظِرَهَا الخلابة في مُخَيِّلَتِهِ.ِ كما استعان بالجنوح إلى الخيال؛ لأَنَّ كثيرًا مِمَا رَسَمَهُ مِنْ مَلامِحَ لِعَالَمِهِ المَتَحَيَّلِ غَيْرُ مَوْجُودَةٍ فِي الواقع الذي يحياه. لذا لَجَأَ إِلَى الخَيَالِ لِيَتَمَكَّنَ مِنْ رَسُمِهَا . وهَذِهِ الاستعانة تَنْسَجِمُ مَعَ مُيُولِ الإبداعيين والرومانسِيِّين،َ وَجُبران واحِدٌ مِنْهُم. فالجنوح إلى الخيال، وتمجيد الطبيعة والتغني بمَشَاهِدِهَا الأَخَاذَةِ أَهَمُ خَصِيْصَتِينَ مِنْ خَصَائِصِ الْمَذْهَبِ الْإِبْدَاعِي.
- اذْكُرْ مِنَ النَّص ثلاثةَ مُؤشِّرَاتٍ على سَعَادَةِ الشَّاعِرِ فِي عَالَمِهِ الْمُتَخْيَل.ِ ج -٢ خُلُو عالَمِهِ المُتَخَيَّلِ مِنَ الهم والحزن - امتلاك عالَمِهِ المُتَخَيَّلِ طبيعة ساحِرَةً تَزْخَرُ بِمَشَاهِدِهَا الأَخَاذَة،ِ وَمَنَاظِرِهَا الخَلَابَة.ِ - استعانته بالفن والغناء؛ لِمَحْو المِحَنِ وَنِسْيَانِ الدَّاءِ والدواء.

=== BLOCK 4: الاستيعاب والفهم والتحليل ===
(Component: TEMPLATE_C_LIST.html)
Title: الاستيعاب والفهم والتحليل: المستوى الفكري:
List Items:
- اسْتَعِنْ بِأَحَدِ المَعَاجِمِ اللَّغَوِيَّةِ فِي تَنْفِيدِ مَا يَأْتِي:
- ما جمع كُلِّ مِن:ْ (دواء، داء)؟ ج- دواء: أدوية. - داء: أدواء.
- ما الفَرْقُ بَيْنَ مَعْنَى : (مَسْمَع، مِسْمَعِ) ج- مَسْمَع : اسم مَكَان،ٍ وهو المكان الذي يُسْمَعُ مِنْهُ الصَّوت،ُ حيث يُقَالُ : هُوَ مِنِي بِمَرْأَى ومَسْمَع - مِسْمَع الأذن، وهو اسم آلة.

=== BLOCK 5: معاني المفردات - شوقي ===
(Component: TEMPLATE_C_POEM.html)
Title: حَدِّدْ مَعْنَى (الثُّرَيَّا) في كُلِّ مِنَ البَيْتَين الآتيين :
Poet: قَالَ أَحْمَدُ شوقي :
Hemistich 1: فإذا جَازَ الثُّرَيَّا لِلثَّرَى
Hemistich 2: جَرَّ كَالطَّاوُوسِ ذَيْلَ الْخُيَلاء

=== BLOCK 6: معاني المفردات - جبران ===
(Component: TEMPLATE_C_POEM.html)
Title: -
Poet: قال جبران خليل :
Hemistich 1: والعَنَاقِيدُ تَدَلَّتْ
Hemistich 2: كَثُرَيَّاتِ الذَّهَبِ

=== BLOCK 7: تلميح حول المعنى ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: تلميح
Content: ج- معنى الثُّرَيَّا عِنْدَ أحمد شوقي: مجموعةً مِنَ النُّجُومِ فِي صُورَةِ الثَّوْرِ. - عند جبران خليل جبران: جمع، ومُفْرَدُهُ (ثريا)، وهي النَّجَفَة.ُ

=== BLOCK 8: الفكرة العامة والمقاطع ===
(Component: TEMPLATE_C_TABLE.html)
Title: الفكر الرئيسة
Headers: الفكرة | الجواب / المقطع
Row 1: اخْتَرْ مِمَا بَيْنَ القَوْسَين الفِكْرَةَ العامة لِلنَّص: (الدَّعُوةُ إِلَى الحَيَاةِ الفِطْرِيَّةِ النَّقِيَّة،ِ خُلُو الغَابِ مِنَ الهم والحُزْنِ الدَّعوة إلى الاستِمْتَاعِ بِفَجْرِ الغَابِ وَنُورِه،ِ الدعوة إلى الزُّهْدِ بِالمُسْتَقْبَلِ وَنِسْيَانِ الماضي). | ج - الدعوة إلى الحَيَاةِ الفِطْرِيَّةِ النَّقِيَّة.ِ
Row 2: انْسُبْ كَلَّا مِنَ الفِكْرِ الرَّيْسَةِ الْآتية إلى المقطع المناسب لها : الدعوة إلى العيش في الغَاب،ِ والاستمتاع بِسِحْرِه.ِ | (المقطع الثاني).
Row 3: الدعوة إلى تَأْمل الطبيعة، والانْصِرَافِ عَنِ الدُّنيا. | (الْمَقْطَعُ الثالث).
Row 4: الغابُ عَالَمَ الْمَسَرَّاتِ وَالْأَمَلِ. | (المقطع الْأَوَّلُ).

=== BLOCK 9: إجابة التقويم ===
(Component: TEMPLATE_C_BENEFIT.html)
Title: إجابة نموذجية
Content: ج - يَرَى جبران أَنَّ حياة الإِنْسَانِ فِي المُجْتَمَعِ الذي يعيش فيهِ تَطْفَحُ بِالْأَحْزان، وتَعِجُّ بِالهُمُوم،ِ فَصِرَاعُ الإِنْسَانِ مَعَ نَفْسِهِ أَو مَعَ أفْرَادِ مُحِيطِهِ الاجتماعي يُوَلَدُ الكآبة والتعاسة والألم والحرمان والكراهية. وتَوْقُ جبران إلى الغَابِ يَشِي بِنُفُورِهِ الشَّدِيدِ مِنْ وَاقِعِ الْغُرْبَة،ِ ويُصَوِّرُ مَدَى رَغْبَتِهِ بِتَحْطِيمِ أَسْوَارِ هذا الواقع البغيضِ وَتَخَطِّيهِ إِلَى عَالَمٍ مِثَالِي نَقِيَ مِنَ الْأَحْرَانِ مُجَرَّدٍ مِنَ الهُمُومِ وَالْأَوْهَامِ فَوَجَدَ ضَالَّتَهُ فِي الغَابِ لِأَنَّ طَبِيعَةَ الغَابِ بَرِيئَةً نَقِيَّةٌ مِنَ آثَامِ الوَهْم،ِ وَأَدْرَانِ الشَّرُورِ التي تُخَلِّفُ الْأَحْزَانَ وَالهُمُوم.َ

=== BLOCK 10: تقويم ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: مَثَّلَ النَّصُّ فِي تَوْقِ الشَّاعِرِ إِلَى الغَابِ نُفُورًا مِنْ عَالَمَ بَغِيْضِ عَاشَهُ فِي غُرْبَتِهِ، ادْكُرْ بَعْضَ مَلامِحٍ ذَلِكَ العَالَمِ كما أَوْحَى بِهِ الْمَقْطَعُ الْأَوَّل.ُ

--- END STREAM ---
