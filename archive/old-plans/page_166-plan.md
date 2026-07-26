# **SESSION 166**

[TASK DEFINITION]
Objective: Implement page 166.
File: `pages/page_166.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`.
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md` to identify the correct template to use for the continuation.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
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
[LESSON_NUMBER]: 166
[CHAPTER_TITLE]: page 166
[CATEGORY_HEADER]: 166
[SECTION_HEADER]: 166
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Vocabulary ===
(Component: TEMPLATE_C_LIST.html)
Title: عد إلى أحد المعجمات اللغوية
Content:
- عُدْ إِلَى أَحَدِ الْمُعْجَمَاتِ اللُّغَوِيَّة،ِ وابحث عن:
- المَعَانِي الْمُنوَعَةِ لِكَلِمَةِ هَائِم(، ثُمَّ مَعْنَاهَا وَفَقَ سِياقِهَا فِي البَيْتِ الأَوَّل.ِ
- ج- هائم : خَرَجَ على وجهه فِي الْأَرْضِ لا يدري أين يتوجه.
- ب الْفَرْقِ فِي مَعْنَى كَلِمَةِ الأَرْياح فيما يأتي: )هَبَّتِ الْأَرْيَاح،ُ يَمِيلُ مَعَ الْأَرْياح(.
- ج - يَمِيلُ مَعَ الأرباح الأرباح، جمع ريح(. وهي الهواء إِذَا تَحَرَّكَ .
- هَبَّتِ الأَرباح الأرباح، مِنَ الأهواء.

=== BLOCK 3: Ideas and Structure Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Title: الفكر العامة
Content:
Row 1: الفكرة العامة | تصوير المعاناة خارج الوطن والتعلق الشديد بِهِ
Row 2: فِكْرَةُ الْمُقْطَعِ الْأَوَّلِ | المعاناة من الضياع والحنين إلى الوطن والأهل
Row 3: فِكْرَةُ الْمَقْطَعِ الثَّاني | المَعَانَاةُ مِنَ التَّمَرُّقِ الرُّوحِيِّ
Row 4: فِكْرَةُ المَقْطَعِ الثَّالِثِ | الفَرَحُ بالرياح القادِمَةِ مِنَ الوَطَنِ وأثرها في الشاعر
Note: المعاناةُ مِنَ التَّمَزَّقِ الرُّوحِي، الْفَرَحْ بِالرِّيَاحِ القَادِمَةِ مِنَ الوطن وأثرها في الشاعر، تصوير المعاناة خارج الوطن والتعلق الشديد به(. المعاناةُ مِنِ الصَّيَاعِ والحنين إلى الوطن والأهل. ج- صَفِ الفكر الآتية،َ وَفُقَ الجَدُول:ِ

=== BLOCK 4: Question and Analysis ===
(Component: TEMPLATE_C_LIST.html)
Title: الفهم والتحليل
Content:
- ٢- هات مُؤَشِّرَاتِ مِنَ المَقْطَعِ الأَوَّلِ عَلَى انْتِمَاءِ الشَّاعِرِ إلى وَطَنِهِ الأم سورية، وإِلَى وَطَنِهِ العربي الأَكْبَر.ِ
- ج - مُؤْشِّرَاتُ انْتِمَاءِ الشَّاعِرِ إلى وَطَنِهِ الأُم سورية: ) حلم يومك في الميماس محتفل(.
- مُؤَشِرَاتُ انْتِمَاءِ الشَّاعِرِ إلى وَطَنِهِ العَربي الْأَكْبَرِ : )هائم في بيد قحطان(، )البيت الرابع(.

=== BLOCK 5: Question and Analysis 2 ===
(Component: TEMPLATE_C_LIST.html)
Title: قيم ومؤشرات
Content:
- عَجِزَتِ الغُرْبَةُ عَنْ زَعْزَعَةِ انْتِمَاءِ الشَّاعِرِ إِلَى قِيَمَ وَطَنِهِ الرُّوحِيَّةِ والاجِتِمَاعِيَّةِ مَثَلَ لِذَلِكَ مِنَ الْمَقْطَعِ الثَّانِي.
- ج - انتماءُ الشَّاعِرِ إِلَى قِيَمٍ وَطَنِهِ الرُّوحِيَّةِ البيتُ السَّابِع.ُ
- انتماء الشَّاعِرِ إِلَى قِيَمٍ وَطَنِهِ الاجتِمَاعِيَّة:ِ النَّاسِعُ

=== BLOCK 6: Question and Analysis 3 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: توق الشاعر
Content:
- تَبَدَّى تَوْقُ الشَّاعِرِ لِلعَوْدَةِ مِنْ خِلالِ فَرَحِهِ بِالرِّيَاحِ القَادِمَةِ مِنَ الشَّرْقِ وَضَحْ ذَلِكَ مِنْ فَهْمِكَ الْمَقْطَعَ الثَّالِث.َ
- ج - ظَهَرَ تَوْقُ الشَّاعِرِ لِلعَوْدَةِ إِلَى الوَطَنِ مِنْ خِلالِ فَرَحِهِ الكَبِيرِ بِقُدُوم رياح الشرق إلى غربتِه،ِ فهو يخاطب أصحابهُ خِطَابًا يبدو فيهِ عَاشِقًا مُغْرَمًا بِه.ِ فيطلُبُ مِنْهُم أَنْ يَتَرَكُوا النَّسَائِمَ الْمُحَمَّلَةَ برمالِ الوَطَنِ تُعَائِقُ أَنْفَاسَهُ الْمُشْتَاقَة،َ وَتَلْفَحْ مِنْ رِياح جَسَدَهُ الْمُغْتَرِبَ وَيَطْلُبُ لِوَطَبَه،ِ وَلَهَا أَنْ تزيد هُبُوهَا وَتَتَدَفَقَ إِلَيهِ لَأَنَّا تَحْمِلُ رَائِحَةَ الأَهْلِ وَالأَحِبَّة.ِ ويُؤَكِدُ لها أَنَّ قُدُومَهَا قد أعاد إليه ربيعه الذي صادرته الغُرْبَة،ُ حيثُ اهترَّتْ أَغْصَانُ قَلْبِهِ الحَامِلَةُ الجَامِدَةُ فَرِحَةً باللقاء، وراحَتْ تَتَمَايَل وترقُضُ رَقْصَ مَخْمُورٍ دَارَتِ الْخَمْرَةُ بِرَأْسِهِ وَقَدِ اكْتَسَتْ هَذِهِ الأَعْصَانُ الحَرَدَاءُ ثَمَلِ بأوراق المَحَيَّةِ والشَّوق،ِ فَبَدَتْ مُتَلَالِنَةً مُخْضَلَّة ترفل بأثواب خَضْرَاءَ سُنْدُسِيَّة،ِ فَيَفوحُ مِنْهَا عَبَقُ الربيع وعبيره، ويضوع منها نسِيمُ نَيْسان الفواح.

=== BLOCK 7: Insight Note ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: ملاحظة
Content:
- ه ثمة حقيقةً مُسْتَقِرَّةٌ فِي نَفْسِ الشَّاعِرِ حَمَتْهُ مِنَ الدَّوَبَانِ فِي بِلَادِ الْغُرْبَةِ بَدَتْ فِي الْبَيْتِ النَّاسِعِ اذْكُرُها، وبينْ رَأَيْكَ فِي قُدْرِتِهَا على صَوْنِ الإِنْسَانِ مِنْ عَوَامِلِ الصَّيَاعِ
- جه - الحقيقة التي استقرت في نَفْسِ الشاعر هي الإيمانُ بِقِيمِ الوَطَنِ الروحية، ومحَبَّتُه.ُ وهذه الحقيقةُ قَادِرَةً على صَوْنِ الْمُغْتَرَبِ مِنَ التأثر بعوامل الضياع، وحمايتِهِ مِنَ الاندماج بطبيعَةِ الْمُجْتَمَعِ الْمُتَهَتَكِ ، وَمَنْعِهِ عَنِ الْأَنْقِيَادِ وَرَاءَ المَغْريات، وإبعادِهِ مِنَ الأَنْسِياقِ لِكُلِّ مَا مِنْ شَأْنِهِ أَنْ يَجْرِفَه،ُ وَيَهبط بِهِ نَحْوَ الانحلالِ الخُلْقِي، فَيُنسِيَهُ الوَطَنَ الذِي هَاجَرَ مِنْه.ُ

=== BLOCK 8: Poetry Comparison ===
(Component: TEMPLATE_C_POEM.html)
Title: الموازنة الشعرية
Content:
- قَالَ الشَّاعِرُ المَهْجَرِي رشيد سليم الخوري )القروي(:
سَلام يا نسيم البحرِ البَلِيلَ
إِنْ تَكُنْ مَا عَرَفْتَنِي فَلَكَ العُذْ رُ فَقَدْ غَيَّرَ الْمُحبَّ السقام
زارك اليوم صَبُّكَ الْمُسْتَهَامُ
- وازِنْ بَيْنَ هَذَيْنِ الْبَيْتَين وما وَرَدَ فِي البيتِ الثَّالِثِ مِنْ حَيْثُ الْمَضْمُون.ِ

=== BLOCK 9: Comparison Result ===
(Component: TEMPLATE_C_SPLIT.html)
Title: نتيجة الموازنة
Content (Right):
ج - التشابه :
- كلا الشاعرين التجأ إلى الطَّبيعة للتعبير عَنْ مُعاناتِه.ِ
- كلا الشَّاعِرَين أَظْهَرَ ضَعْفَهُ وَوَهْنَهُ
- كلا الشاعرين استعان بالنسيم للتعبير عَنْ مُعاناته.
- كلا الشَّاعِرَينَ تَحَدَّثَ عَنِ النَّسِيم.ِ
- كلا الشاعرينَ أَظْهَرَ حُبَّهُ لِلنسيم.
Content (Left):
- الاختلاف:
- نسيب عريضة استعانَ بِنَسَمَاتِ الشيح، بينما القروي استعانَ بِنَسِيمِ البَحْر.ِ
- نسيب عريضة جعل النسيم مُؤثا،ً بينما القَرَوِيَ جَعَلَهُ مُذَكَّرًا.
- نسيب عريضة ذكَرَ النَّسِيمَ بِصِيعَةِ الجَمْع،ِ بينما القروي خاطبَ النَّسِيمَ بِصِيعَةِ الْمُفْرَد.ِ
- نسيب عريضة لم يقم بزيارة نَسَمَاتِ الشَّيْح.ِ بينما القَرَوِي قام بزيارة نسيم البحر.
- نسيب عريضة جَعَلَ النَّسيم مخاطبا، بينما القَرَوِيِّ جَعَلَهُ غائبًا.
- نسيب عريضة عَبْرَ عَنْ مَحَمَّتِهِ نَسَمَاتِ الشَّيْحِ بِشَكُلٍ مُباشَر،ٍ بينما القَرَوِيَ أَظْهَرَ حُبَّهُ نَسِيمَ البَحْرِ بِشَكُلِ غَيْرِ مُبَاشَر.ٍ

=== BLOCK 10: Cut Content Part 1 ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
Title: المستوى الفني
Content:
-  -
דדו
المستوى الفني:

--- END STREAM ---
