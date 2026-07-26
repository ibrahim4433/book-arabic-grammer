# **SESSION 158**

[TASK DEFINITION]
Objective: Implement page 158.
File: `pages/page_158.html`
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
[LESSON_NUMBER]: 158
[CHAPTER_TITLE]: page 158
[CATEGORY_HEADER]: 158
[SECTION_HEADER]: 158
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: الاستيعاب والفهم (تتمة) ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[BLOCK_TITLE]: الاستيعاب والفهم
[CONTENT]: كانَ فِي نَصَهِ ركنا مميزا، ووسيلة يُحْدِثُ التاثير في المتلقي؛ ذَلِكَ أَنَّ التَّصوير ج - تمكن الشاعر باستعمال الخيال مِنَ النجاح في جَعْلِ الشَّعْرِ البَدِيعِيَّةِ عَلَلْ إِجَابَتَك.َ الشعر باستعمال الخيال والمُحَسَاتِ - أَنجَحَ الشَّاعِرُ أَمْ أَخْفَقَ فِي خَلْقِ التَّأْثير في
أَنَّ الشَّاعِرَ جَعَلَ الوَطَنَ إِنْسَانَا يُنَادَى وَيُخَاطَب،ُ والرِّزْقَ شَيْئًا تَعْبِيرِيَّةً فَمَّالةً نَقَلَ مِنْ خلالها الأحاسيس والمشاعر التي تجيش بها نَفْسُهُ مِنْ ذلكَ
العُمَرُ أَجْرًا يُدْفَعُ وَيَنفَدُ أَمَّا الدَّهْرُ حسوسا يحمد وينكمش، والطَّيْفَ زائرًا يزور ويتجافى ويبتعد . كذلك صار الغِنَ إِنْسَانًا يتقاضَى الأَجْر،َ وَأَمْسَى
جَسَد( مُعَ رَةٌ عَنْ مِنَ الجَسَد.ِ وتَتَجَلَّى على هذا الصَّعِيدِ صُورَةُ فَرَّقَ رُوْحًا عَن فغدا ذا دِرَايَةٍ يمتلك طاقة قادرة على تفريق الشَّمْل،ِ وَنَزْعِ الرُّوح
الشَّاعِرِ ) جراح اليْتُم(، فهذه الصورةُ تُكَ فُ مَأْسَاةَ مِنَ الصور التي ابتدعَهَا خَيَالُ الشَّاعِرِ صُورة متانة وشائج العلاقة بين الشاعر والوَطَن.ِ كذلك
أَنَّهَا تَبْعَتُ فِي النَّفْسِ ما المعاناة التي يُصارعها. وبما يزيد هذه الصُّورةَ جَمَالًا وَتَأْلُقَا في الغربة،ِ وَتَكْشِفُ ما يُكابدُهُ مِن وَطَاةِ العَيْش،ِ وتَخْتَزِلُ شِدَّةَ
الْمُحَسَنَاتِ البديعيَّةِ بِابَيها إِلى التأثيرِ فِي الْمُتَلَفِي تَكْنُهُ مِنْ تَوظيف طاقَةِ ينم على عمق الانتماء إلى الوطن والانتساب إليه. وما أَوْصَلَ الشَّاعِرَ

=== BLOCK 3: الجانب المعنوي والجانب اللفظي ===
(Component: TEMPLATE_C_SPLIT.html)
[RIGHT_TITLE]: الجانب المعنوي
[RIGHT_CONTENT]: المعاني المتقابلة يفيد مِنْ طَاقَةِ النَّصَاةِ بينَ الأَلْفَاظ،ِ فَيُبْرِزُ عنها. ففي الجانب المغنوِيَ نَجِدُهُ المَعْنَوِي والفَ يِّ فِي خِدْمَةِ المعاني التي أراد الإِفْصَاحَ
المزرية التي كان يحياها خيال المتلقي ويمنحه الفُرْصَةَ لِتَخَيل الحالة الإيجاب: )الجزر المد(، يثير ويُكسبها مزيدًا مِنَ التَّأْثير فحينما يعمد إلى طباق
الفَرْقِ الشَّاسِعِ بِينَ الحالتين المتناقضتين، تَرَقُبِ العَوْدَةِ وَتَمَتِي الرُّجُوعِ فَيُمَكِّنُهُ مِنْ إِدراك الشَّاعِرُ وهو يُبْحِرُ مُرْعَمَا مِنْ شَوَاطِي وَطَنِه،ِ وحالةِ
فِي وَطَنِه،ِ وَانْقِطَاعِ رِزْقِه.ِ فهذا الاستعمال يُبْرِزُ التناقض الحاد بينَ وَفْرَةِ الخَيْراتِ ويصبَعُ مِثْل ذلك حين يستعمل طباق الإيجاب: )جَرَتْ جمد(،
فِي أَحْضَانِ الوَطَن،ِ مهما كانَ ضَنَكًا صَيِّقًا، وَمَرَارِتِهِ فِي وعندما يلجأ إلى طباق الإيجاب: )مر، يحلو(، فَإِنَّهُ يُفْصِحُ لِلْمُتَلَقِي عَنْ عُدُوبَةِ العَيْشِ
عَقْلِهِ بِينَهُمَا لِيُدْرِكَ الْفَرْقَ هَاتَين الحالتين المتناقضتين، ويُمكنهُ مِنْ إِعمالِ الغربة مهما كانَ رَغِيدًا. وهذا يُثير خيال المتلقي ويُحَقِّرُهُ لِلْمُقارنة بينَ
لِلعَوْدَةِ إِلَى رُبُوعِ الوَطَن.ِ الشَّاسِعَ بِينَهُما. فَضْلَا عَنْ إِبرازِ مَوْقِفِ الشَّاعِرِ الرَّافِضِ لِلغَرْبَةِ الطَّامِحِ
[LEFT_TITLE]: الجانب اللفظي
[LEFT_CONTENT]: عنها. شِعْرِهِ جَوا مُوسِيقِيَّا مُتَنَاغِمًا مَعَ المعاني التي يُنصح أما في الجانِبِ اللَّفَطْيِّ فَنَجِدُ أَنَّ الْمُحَسنات البديعية اللَّفْظِيةَ قَد أَصْفَتْ على
ورَوْعَةِ الإيقاع الموسيقيين عن طريق وجود دالين ساكنين في شطرين فالتصريع في بداية النص بينَ كَلِمَتَي )أَوَدْ مَدْ( مَنَحَهُ مَزِيدًا مِنْ حَلَاوَ الجَرْس،ِ
في أَبيات النَّصَ جَرْسًا موسيقيا قويا يَقْرَعُ الأسماع ويلفِتُهَا لِتَتَفَكَّر متناظرين مُتناغمين. والجناسُ النَّاقِلُ زبدة، زبد(، أو الغناء المنى( أَكْسَبَ
لِبُلوغ الأماني والأحلام. صفو العيش وهنائِهِ فِي الوَطَن،ِ وَكَدَرِهِ فِي الغُرْبَة،ِ وتُعِنَ فِي تحمل المتَاعِبِ والمشاق
الحالة الوجدانية التي يُعَبِّرُ عَنْهَا الشَّاعِر.ُ - استَعْمَلَ الشَّاعِرُ رَوِيَّ الدَّالِ السَّاكِنَةِ بَيِّنِ الملاءَمَةَ الإيقاعِيَّةَ لِذَلِكَ مَعَ
مَعَ الْأَفكار التي طَرَحَهَا، وَمُتَلَائِمَا مَعَ الحَالَةِ الوجدَانِيَّةِ - حَدَّدَ الشَّاعِرُ نَصَّهُ بِإِطار موسيقي خارجي أضفى عليه إيقاعا موسيقيا مُنْسَجِمَا
في القافِيَةِ المُقَيَّدَةِ الخارجية باحث بأسرار الشاعر الداخلية، فما الانقباض التي يعبر عنها مُتَناغمًا مَعَ الحَالَةِ الشُّعُوريَّة التي يعيشها؛ فَمُوسيقا النَّص
الشَّاعِرِ وَتَقَطَّعِ أَنْفَاسِه،ِ خَلَّفَهُمَا تَفْبِيدُ حَرْفِ الرَّوي إِلَّا ترجمة لانجباس زفراتِ إِلَّا صَدَى لانقباضات الداخل، وما الانحباس والتَّقَطْعُ اللَّذانِ
رُوحِهِ وَأَنْفَاسِه.ِ الدَّالِ يُشْعِرُ بِالْكِسَارِ نَفْسِهِ وَالْقِبَاضِ ودَلِيلٌ على ضِيْقٍ صَدْرِهِ بِسَبَبِ المعاناة التي يُعانيها . فَتَسْكِينُ

=== BLOCK 4: عناصر الموسيقا الداخلية ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: الظاهرة
[HEADER_2]: المثال
[HEADER_3]: الموضع
[CELL_1_1]: استعمال حُرُوفِ الهَمْسِ
[CELL_1_2]: س، ت، ح، ف، ك
[CELL_1_3]: في البيت الثاني
[CELL_2_1]: التكرار (تكرار الكَلِمَات)
[CELL_2_2]: رَسَتْ رَسَتْ
[CELL_2_3]: في البيت الثاني
[CELL_3_1]: التكرار (تكرار الكَلِمَات)
[CELL_3_2]: البين، البين
[CELL_3_3]: في البيت السابع

=== BLOCK 5: تنبيه هام ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[TITLE]: ملاحظة حول الإجابة
[CONTENT]: الإجابة حول نثر أبيات المقطع الأول: وطني الحبيب لقد أصبحت بعيدا عن بيتي وأهلي وصحبي، بعد أن أخذني جَزْرُ البَحْرِ مِنْ شَاطِئِكَ إِلَى شاطئ العربة، فهل من حسن طالع يُعْقِبُ هذا الجزر بمد يُعيدني إليك؟!. لو امتلكت ناصية أمري وكانَ مِقْوَدُ سَفِينَةِ البُعْدِ بِيَدي لما جَعَلْتُهَا تُبْعِدُنِي عَنْكَ وَتُلْقِي بي في شاطئ العزية. فقد صار البحر الذي سَلَكُتُهُ لأبلغ غَرْبَتِي، فاصلًا غَيَّبَ عن ناظري ذلك الشاطئ الذي اسْتَقَرَّ فيه كلُّ مَنْ حَرَمَنِي فَرْقَتُهُم نومَ لَيْلِي. ففيه منزلي الذي نَشَأْت فيه، وفيهِ بِقَاعٌ غَنَّاءُ خَضْرَاءُ جَمِيلَةً وَارِفَةُ الظَّلَال،ِ فَقَدْ حَبَا الهُ آيَاتٍ مِنَ الْجُمَالِ وَزَانَهُ بِأَخَارِ رَقْراقة عذبة، ومع كل هذا يطل الخير العميم، قد ضاق العيش فيه، وامتنع تحصيل الرزق وصَعُبَ فيه تَسْتَحِيلُ مَرَارَةُ العيش عذوبَة،ٌ وَيَعْدُو كَدَرُهُ صَفْوا، وفي أي بقعة سواه رغَدُ العيش مُنَغَصًا عكرًا، فلا تلد الحياة بعيدا عنه؛ لأَنَّ معالمها مصبوغة بجراح الغربة. (اغْتَنَى النَّرُّ بِعَنَاصِرِ الْمُوسيقا الدَّاخِلِيَّةِ مَثَلْ لِكُلِّ من : استعمال حُرُوفِ الهَمْسِ التكرار). ٧٥١

=== BLOCK 6: تقطيع البيت الأول ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: تقطيع البيت الأول
[POET_NAME]:
[RIGHT_HEMISTICH]: حَظ بَعْدَ الْ جَزْرِ مَدْ
[LEFT_HEMISTICH]: من أنا هم مَنْ أَوَدُ
[RIGHT_HEMISTICH]: أَوَمَا لِلْ وَطَنِي أَيْ
[LEFT_HEMISTICH]: 이 이이이 이 이 이 이
[RIGHT_HEMISTICH]: فاعلن فاعلن فعلاتن
[LEFT_HEMISTICH]: فاعلاتن فعلاتن فعلاتن
[RIGHT_HEMISTICH]: = /٥//.
[LEFT_HEMISTICH]: القافية : جزر مد الرمل.

=== BLOCK 7: Exam ===
(Component: TEMPLATE_C_EXAM.html)
[QUESTION_NUMBER]: ١
[QUESTION_TEXT]: قَطَعْ مِنَ الأَبيات البيت الأوَّلَ مِنَ النَّص، ثُمَّ سَمَ بِحْرَه،ُ وَحَدّد قافيته. -۹ تقطيع البيت الأوَّلِ مِنَ النَّص، وتسمية بحرِه،ِ وَتَحْدِيدٌ قَافِيتِه:ِ المستوى الإبداعي: انثر أبيات المقطع الأول. التعبير الكتابي:

--- END STREAM ---
