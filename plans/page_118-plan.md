# **SESSION 118**

[TASK DEFINITION]
Objective: Implement page 118.
File: `pages/page_118.html`
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
11. You MUST preserve the EXACT Tashkeel (Harakat) from the input. Stripping diacritics is a critical failure. Do not generate bare Arabic letters without their vowels.
12. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal
14. **Page Wrappers**: The compiler will automatically wrap the final page in `TEMPLATE_C_PAGE_WRAPPER.html`. Do NOT include this template in your `[CONTENT STREAM]` blocks.
15. **Exam Section**: ONLY include the `TEMPLATE_C_EXAM.html` block if the provided raw text slice actually contains test/exam questions (e.g., keywords like "تطبيق", "امتحان"). Do NOT hallucinate an exam if it is not in the source text. **CRITICAL:** If an exam or exercise contains the answers in the raw text, you MUST use `TEMPLATE_C_EXAM_SOLVED.html` instead of `TEMPLATE_C_EXAM.html`.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 118
[CHAPTER_TITLE]: page 118
[CATEGORY_HEADER]: 118
[SECTION_HEADER]: 118
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: مقدمة الأسئلة ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b64567
Title: بِمَ تَسَلَّحَ كُلِّ مِنْ طَرَفِي الصَّرَاعِ فِي النَّصِ؟
Content: <span class="highlight-blue">ج - الطرف الأول:</span> الشيخ، وابنته، والجندي القديم تسلحوا بالحنين إلى الوطن، وبالإرادة الصلبة القوية التي بدت أقوى من الصخر وأصلب. <br> <span class="highlight-blue">- الطرف الثاني:</span> الجنود الصهاينة المحتلون تسلحوا بالبنادق والرصاص.

=== BLOCK 3: المستوى الفكري ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b29664
Title: الاستيعاب والفهم والتحليل
Content: <span class="text-accent font-bold">المستوى الفكري:</span>

=== BLOCK 4: أسئلة الفهم ===
(Component: TEMPLATE_C_LIST.html)
[UNIQUE_ID]: b58024
Item 1: - ١ استعِنْ بِالمُعْجَمِ فِي تَعَرَّفِ المَعَانِي الْمُخْتَلِفَةِ لِلفِعْلِ (تلا)، ثُمَّ اخْتَر معناها السياقِي كما وَرَدَتْ فِي المَقْطَعِ الأَوَّل. ج - ١ تلا: قرا.
Item 2: - ٢ كَوَنْ مُعْجَمًا لُغَوِيَّا لِكُلِّ مِنْ مجالَي: (العودة، الجريمة).

=== BLOCK 5: معجم لغوي ===
(Component: TEMPLATE_C_TABLE.html)
[UNIQUE_ID]: b00317
[HEADER_1]: السؤال
[HEADER_2]: مجال العودة
[HEADER_3]: مجال الجريمة
[CELL_1]: ج - ٢
[CELL_2]: (مشيا، زحفا، نعود، تقود الطريق القوافل العائدين، عائدين، يصلون العائدون، الحنين، الوطن .....)
[CELL_3]: (دم، مصيدة، اللحم المفتت، البنادق، مقصلة، الرصاص، الطلقة، تقتلوها، اقتلوني، القتل، يقتلوا الدم، ....)

=== BLOCK 6: مراحل العودة ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[UNIQUE_ID]: b67974
Title: مراحل العودة
Content: ما مَرَاحِلُ الْعَوْدَةِ كَمَا عَرَضَهَا النَّصُ؟ <br> ج - قرر أبطال القصة الثلاثة، الشيخ وابنته والجندي القديم، العودة إلى وطنهم فلسطين مهما كلفهم ذلك من عناء وجهد. فبدأت رحلة عودتهم قبل دخول الليل بقليل، حيث اتجهوا إلى جسر العبور، وعندما وصلوه صار الليل ستارا يمنع عيون الجنود الصهاينة المرابطين على الحدود رؤيتهم، وحينما تنبه الجنود إلى محاولة العابرين تنتهي محاولة العودة بقتل الجندي القديم فالشيخ، فتدنيس شرف الفتاة.

=== BLOCK 7: الإصرار والجرائم ===
(Component: TEMPLATE_C_LIST.html)
[UNIQUE_ID]: b53139
Item 1: - أَكَدَ محمود درويش الإصْرَارَ على العَوْدَةِ بِرَغْمِ مَا يَنْتَظِرُ العَائِدِينَ مِنْ مَخَاطِر.َ اذكُرُ مَظَاهِرَ هذا الإِصْرَارِ كَمَا تَجَلَّتْ لَكَ فِي الْمَقْطَعِ الأَوَّلِ مِنَ الن.َّ <br> <span class="highlight-blue">ج -</span> أصر الشيخ وابنته والجندي القديم على العودة إلى ديارهم مهما كلفهم هذا من عناء وجهد وإن تطلب الأمر الزحف على الأيدي، فقد بلغت قوة إرادتهم وصلابتها درجة تجاوزت قوة الصخر وصلابته.
Item 2: ه - ما الجرائم التي اقترفها الصَّهاينةٌ بِحَق العائِدِينَ كَمَا وَرَدَ فِي المَقْطَعِ الثَّالِثِ؟ <br> <span class="highlight-blue">ج -</span> اقترف الصهاينة بحق العائدين جرائم القتل، فقد صار القتل عندهم عادة ومزاجا خاصا كالتدخين يصعب عليهم التخلص منه. وقد قتلوا الشيخ وانتهكوا حرمة الفتاة، ودنسوا شرفها.

=== BLOCK 8: الموقف من القرآن ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b15251
Title: الموقف من القرآن الكريم
Content: - عَمَدَ الشَّيْخُ إِلى القُرْآنِ الكريم فِي مَوْقِفين في النص. حَدَدْهُمَا وَاذْكُرْ دِلالَةَ ذَلِك.َ <br> <span class="highlight-blue">ج - المؤقِفُ الأَوَّل:ُ</span> (وتحسس المفتاح ثم تلا من القرآن آية). <br> <span class="highlight-blue">- المؤقِفُ الثاني:</span> (والشيخ يأخذ كف ابنته ويتلو همسا من القرآن سورة). <br> يدل ذلك على تشبث الشيخ بالإيمان؛ فهو يلجأ إلى الله في كل المواقف، وهذا يؤكد فكرة الإيمان والتدين عنده.

=== BLOCK 9: تمثيل الأجيال ===
(Component: TEMPLATE_C_BENEFIT.html)
[UNIQUE_ID]: b25176
Title: تمثيل الأجيال في النص
Content: - تُمَثِّلُ شَخْصِيَّتَا الشَّيْخِ وَابْنَتِهِ جِيلَيْنَ مِنَ الفِلِسْطِينِينَ اذْكُرْهُما، وَوَضِحْ تَأْثِيرَ كُلِّ مِنْهُمَا فِي الْآخَرِ مِنَ النَّص.َ <br> <span class="highlight-blue">ج - الجيلُ الأَوَّل (الشيخ):</span> يمثل الجيل القديم المفعم بأمل العودة والتفاؤل بالرجوع إلى أرض الوطن، ذلك الجيل الذي يؤكد على العودة ويصر عليها. <br> <span class="highlight-blue">- الجيل الثاني (الفتاة):</span> تمثل الجيل الجديد الذي تسرب اليأس إلى نفسه وفقد أمل العودة. <br> إنَّ الجيل الأول يحاول طرد اليأس من نفس الجيل الثاني ويجعله مفعما بالأمل، فالشيخ يحاول أن يجعل ابنته متفائلة حالمة، فعندما تشير إليه بتحطم منزلها بقولها ولكن المنازل يا أبي أطلال، يرد عليها طاردًا اليأس، راسما الأمل: (تبنيها يدان).

=== BLOCK 10: الجندي والسخرية ===
(Component: TEMPLATE_C_LIST.html)
[UNIQUE_ID]: b11507
Item 1: - بَدَتْ شَخْصِيَّةُ الجَنْدِيَ فِي النَّصَ هَامِشِيَّة،َ ذَكَرَهَا الشَّاعِرُ فِي مَوْقِفين، ولَمْ يُسْنِدْ إليها أَيَّ فِعْلِ اذْكُرُ هَذَينِ الْمَوْقِفين، مُبَيِّنًا غاية الشَّاعِرِ مِنْ ذَلِك.َ <br> <span class="highlight-blue">ج - المؤقِفُ الأَوَّل:ُ</span> مرافقة الشيخ وابنته في طريق العودة كانوا ثلاثة عائدين ... شيخ وابنته وجندي قديم(. <br> <span class="highlight-blue">- المؤقِفُ الثاني:</span> عند مقتله والطلقة الأخرى... أصابت قلب جندي قديم(. <br> <span class="highlight-blue">- غاية الشاعر:</span> لم يرد الشاعر أن يعطي الجندي دورا إيجابيا في النص، ولعل الشاعر قد أراد من شخصية الجندي أن ترمز إلى عدم فاعلية الجيش العربي في إنقاذ فلسطين من براثن الصهاينة.
Item 2: - تَعَمَّدَ الشَّاعِرُ السُّخْرِيَةَ مِنَ الجُنُودِ الصَّهَاينة، مَثِّلْ لِذَلِكَ مِنَ المَقْطَعِ الثَّالِث،ِ واذكرِ الهَدَفَ مِنْ تِلْكَ السُّخْرِية.ِ <br> <span class="highlight-blue">ج - ٩ المثال:</span> ظهرت السخرية من الجنود القتلة في قول الشاعر: لكن الجنود "الطيبين"(. <br> <span class="highlight-blue">- الهدف مِنْ تِلْكَ السُّخْرِية:ِ</span> إثبات النقيض من أجل التنديد بأفعال هؤلاء الجنود الذين أدمنوا على القتل والإجرام، وخلت قلوبهم من الرحمة والشفقة.

=== BLOCK 11: المستوى الفني ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b02452
Title: المستوى الفني
Content: <span class="text-accent font-bold">المستوى الفني:</span> <br> - لَوْنَ الشَّاعِرُ بِينَ النَّمَطَين الوَصْفِي والسَّرِدِي في تقديم حكايته، ما المؤشرات التي تَدُلُّ على ذَلِكَ؟ <br> <span class="highlight-blue">ج - ١ مؤشراتُ النَّمَطِ الوَصْفِي:</span>

=== BLOCK 12: مؤشرات النمط الوصفي ===
(Component: TEMPLATE_C_LIST.html)
[UNIQUE_ID]: b97657
Item 1: استعمال الصور البيانية الخيالية الموحية: كان النهر يبصق ضفتيه، كان الجسر نعاسا، كان الليل قبعة، الطلقة الأولى أزاحت عن جبين الليل قبعة الظلام، القتل كالتدخين، النهر الذي يمتص لحم النازحين، الجسر يكبر كل يوم كالطريق ....
Item 2: استعمال الأفعال الدالة على حالة الموصوف، أو الجمل الاسمية التي تمكن من إطلاق الصفات والنعوت وبدخول (كان) على هذه الجمل ينتقل الوصف من الحاضر إلى الماضي : (وكان الصخر يضمر والمساء يدا تقود، وكان النهر يبصق ضفتيه قطعا من اللحم المفتت، كان الجسر نعاسًا وكان الليل قبعة، كان الشيخ يسقط في مياه النهر البنت التي صارت يتيمة كانت ممزقة الثياب(.

--- END STREAM ---
