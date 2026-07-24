# **SESSION 118**

[TASK DEFINITION]
Objective: Implement page 118.
File: `pages/page_118.html` (Note: Use the exact page number.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools. If it overflows, it is a catastrophic failure. Solve it by choosing denser templates or omitting optional white-space.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice. Applied "The Typo Exception" to correct obvious OCR errors.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide: NO INLINE STYLES. Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
7. Templates: Map all content using "Jules-workspace/Templates/" components. **CRITICAL 1-PAGE MODE RULE**: You MUST NOT use `<section>` tags when applying templates. Replace any `<section>` tags from the templates with `<div>` tags (keep `<header>` for page headers as is).
8. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). The ID MUST be applied to the `<div>` tag that replaced the `<section>` tag. Use "Jules-workspace/id_manager.py" to generate or verify them.
9. Do not summarize examples. Do not provide uncompleted text content using (...).
10. balanced page colors between teal and orange: make sure every page have minimum 1 element in orange (`.block-header accent`) instead of all teal.
11. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`).
12. Exam section always be in the end of the lesson (in the final page of that lesson), and without the answers! The answer must be moved to a preceding Benefit box.

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

=== BLOCK 2: تتمة الأسئلة ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تتمة الأسئلة
Content:
(Component: TEMPLATE_C_LIST.html)
- بِمَ تَسَلَّحَ كُلِّ مِنْ طَرَفِي الصَّرَاعِ فِي النَّصِ؟
- ج - الطرف الأول : الشيخ، وابنته، والجندي القديم تسلحوا بالحنين إلى الوطن، وبالإرادة الصلبة القوية التي بدت أقوى من الصخر وأصلب - الطرف الثاني: الجنود الصهاينة المحتلون تسلحوا بالبنادق والرصاص.

=== BLOCK 3: الاستيعاب والفهم والتحليل ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الاستيعاب والفهم والتحليل: المستوى الفكري
Content:
(Component: TEMPLATE_C_LIST.html)
- ۱ استعِنْ بِالمُعْجَمِ فِي تَعَرَّفِ المَعَانِي الْمُخْتَلِفَةِ لِلفِعْلِ (تلا)، ثُمَّ اخْتَر معناها السياقِي كما وَرَدَتْ فِي المَقْطَعِ الأَوَّل. ج -۱ تلا: قرأ.

=== BLOCK 4: المعجم اللغوي ===
(Component: TEMPLATE_C_TABLE.html)
Context: - ٢ كَوَنْ مُعْجَمًا لُغَوِيَّا لِكُلِّ مِنْ مَجَالَي: (العودة، الجريمة).
Table Data:
| المجال | الكلمات |
|---|---|
| مجال العودة | (مشيا، زحفا، نعود، تقود الطريق القوافل العائدين، عائدين، يصلون العائدون، الحنين، الوطن .....) |
| مجال الجريمة | (دم، مصيدة، اللحم المفتت، البنادق، مقصلة، الرصاص، الطلقة، تقتلوها، اقتلوني، القتل، يقتلوا الدم، ....) |

=== BLOCK 5: مراحل العودة ومظاهر الإصرار ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مراحل العودة ومظاهر الإصرار
Content:
(Component: TEMPLATE_C_LIST.html)
- ما مَرَاحِلُ الْعَوْدَةِ كَمَا عَرَضَهَا النَّصُ؟ ج - قرر أبطال القصة الثلاثة، الشيخ وابنته والجندي القديم، العودة إلى وطنهم فلسطين مهما كلفهم ذلك من عناء وجهد. فبدأت رحلة عودتهم قبل دخول الليل بقليل، حيث اتجهوا إلى جسر العبور، وعندما وصلوه صار الليل ستارا يمنع عيون الجنود الصهاينة المرابطين على الحدود رؤيتهم، وحينما تنبه الجنود إلى محاولة العابرين تنتهي محاولة العودة بقتل الجندي القديم فالشيخ، فتدنيس شرف الفتاة.
- أَكَدَ محمود درويش الإصْرَارَ على العَوْدَةِ بِرَغْمِ مَا يَنْتَظِرُ العَائِدِينَ مِنْ مَخَاطِر.َ اذكُرُ مَظَاهِرَ هذا الإِصْرَارِ كَمَا تَجَلَّتْ لَكَ فِي الْمَقْطَعِ الأَوَّلِ مِنَ الن.َّ ج - أصر الشيخ وابنته والجندي القديم على العودة إلى ديارهم مهما كلفهم هذا من عناء وجهد وإن تطلب الأمر الزحف على الأيدي، فقد بلغت قوة إرادتهم وصلابتها درجة تجاوزت قوة الصخر وصلابته.

=== BLOCK 6: جرائم الصهاينة والمواقف الإيمانية ===
(Component: TEMPLATE_C_BLOCK.html)
*Note: Use `.block-header accent` for Orange styling.*
Title: جرائم الصهاينة والمواقف الإيمانية
Content:
(Component: TEMPLATE_C_LIST.html)
- ه- ما الجرائم التي اقترفها الصَّهاينةٌ بِحَق العائِدِينَ كَمَا وَرَدَ فِي المَقْطَعِ الثَّالِثِ؟ ج - اقترف الصهاينة بحق العائدين جرائم القتل، فقد صار القتل عندهم عادة ومزاجا خاصا كالتدخين يصعب عليهم التخلص منه. وقد قتلوا الشيخ وانتهكوا حرمة الفتاة، ودنسوا شرفها.
- عَمَدَ الشَّيْخُ إِلى القُرْآنِ الكريم فِي مَوْقِفين في النص. حَدَدْهُمَا وَاذْكُرْ دِلالَةَ ذَلِك.َ ج - المؤقِفُ الأَوَّل:ُ (وتحسس المفتاح ثم تلا من القرآن آية). - المؤقِفُ الثاني: (والشيخ يأخذ كف ابنته ويتلو همسا من القرآن سورة). يدل ذلك على تشبث الشيخ بالإيمان؛ فهو يلجأ إلى الله في كل المواقف، وهذا يؤكد فكرة الإيمان والتدين عنده.

=== BLOCK 7: تحليل الشخصيات والسخرية ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تحليل الشخصيات والسخرية
Content:
(Component: TEMPLATE_C_LIST.html)
- تُمَثَلُ شَخْصِيَتَا الشَّيْخِ وَابْنَتِهِ جِيلَيْنَ مِنَ الفِلِسْطِينِينَ اذْكُرْهُما، وَوَضِحْ تَأْثِيرَ كُلِّ مِنْهُمَا فِي الْآخَرِ مِنَ النَّص.َ ج - الجيلُ الأَوَّل (الشيخ): يمثل الجيل القديم المفعم بأمل العودة والتفاؤل بالرجوع إلى أرض الوطن، ذلك الجيل الذي يؤكد على العودة ويصر عليها . - الجيل الثاني (الفتاة): تمثل الجيل الجديد الذي تسرب اليأس إلى نفسه وفقد أمل العودة. إنَّ الجيل الأول يحاول طرد اليأس من نفس الجيل الثاني ويجعله مفعما بالأمل، فالشيخ يحاول أن يجعل ابنته متفائلة حالمة، فعندما تشير إليه بتحطم منزلها بقولها ولكن المنازل يا أبي أطلال، يرد عليها طاردًا اليأس، راسما الأمل: (تبنيها يدان).
- بَدَتْ شَخْصِيَّةُ الجَنْدِيَ فِي النَّصَ هَامِشِيَّة،َ ذَكَرَهَا الشَّاعِرُ فِي مَوْقِفين، ولَمْ يُسْنِدْ إليها أَيَّ فِعْلٍ، اذْكُرُ هَذَينِ الْمَوْقِفين، مُبَيِّنًا غاية الشَّاعِرِ مِنْ ذَلِك.َ ج- المؤقِفُ الأَوَّل:ُ مرافقة الشيخ وابنته في طريق العودة (كانوا ثلاثة عائدين ... شيخ وابنته وجندي قديم). - المؤقِفُ الثاني: عند مقتله (والطلقة الأخرى... أصابت قلب جندي قديم). - غاية الشاعر : لم يرد الشاعر أن يعطي الجندي دورا إيجابيا في النص، ولعل الشاعر قد أراد من شخصية الجندي أن ترمز إلى عدم فاعلية الجيش العربي في إنقاذ فلسطين من براثن الصهاينة.
- تَعَمَّدَ الشَّاعِرُ السُّخْرِيةَ مِنَ الجُنُودِ الصَّهَاينة، مَثِّلْ لِذَلِكَ مِنَ المَقْطَعِ الثَّالِث،ِ واذكرِ الهَدَفَ مِنْ تِلْكَ السُّخْرِية.ِ ج -۹ المثال : ظهرت السخرية من الجنود القتلة في قول الشاعر: (لكن الجنود "الطيبين"). - الهدف مِنْ تِلْكَ السُّخْرِية:ِ إثبات النقيض من أجل التنديد بأفعال هؤلاء الجنود الذين أدمنوا على القتل والإجرام، وخلت قلوبهم من الرحمة والشفقة.

=== BLOCK 8: إضاءة: مؤشرات النمط الوصفي ===
(Component: TEMPLATE_C_BENEFIT.html)
Title: إضاءة: مؤشرات النمط الوصفي
Content:
ج -۱ مؤشراتُ النَّمَطِ الوَصْفِي :
(Component: TEMPLATE_C_LIST.html)
- استعمال الصور البيانية الخيالية الموحية: كان النهر يبصق ضفتيه، كان الجسر نعاسا، كان الليل قبعة، الطلقة الأولى أزاحت عن جبين الليل قبعة الظلام، القتل كالتدخين، النهر الذي يمتص لحم النازحين، الجسر يكبر كل يوم كالطريق ....
- استعمال الأفعال الدالة على حالة الموصوف، أو الجمل الاسمية التي تمكن من إطلاق الصفات والنعوت وبدخول (كان) على هذه الجمل ينتقل الوصف من الحاضر إلى الماضي : (وكان الصخر يضمر والمساء يدا تقود، وكان النهر يبصق ضفتيه قطعا من اللحم المفتت، كان الجسر نعاسًا وكان الليل قبعة، كان الشيخ يسقط في مياه النهر البنت التي صارت يتيمة كانت ممزقة الثياب).

=== BLOCK 9: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: المستوى الفني: - لَوْنَ الشَّاعِرُ بِينَ النَّمَطَين الوَصْفِي والسَّرِدِي في تقديم حكايته، ما المؤشرات التي تَدُلُّ على ذَلِكَ؟

--- END STREAM ---
