# **SESSION 102**

[TASK DEFINITION]
Objective: Implement page 102.
File: `pages/page_102.html` (Note: Use the exact page number.)
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
7. Templates: You are forbidden from inventing new HTML tags or classes or template elements. You must map all content using "Jules-workspace/Templates/" components as the STREAM says in suitable way. **CRITICAL 1-PAGE MODE RULE**: You MUST NOT use `<section>` tags when applying templates. Replace any `<section>` tags from the templates with `<div>` tags (keep `<header>` for page headers as is).
8. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). The ID MUST be applied to the `<div>` tag that replaced the `<section>` tag. Use "Jules-workspace/id_manager.py" to generate or verify them.
9. **Self-Correction:** Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files. If it fails, you MUST fix the errors (usually inline styles or forbidden section tags) before submitting.
10. Do not summarize examples.
11. Do not provide uncompleted text content using (...) unless strictly matching raw text.
12. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
13. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
14. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal. Use `.block-header accent` for Orange blocks.
15. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
16. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 102
[CHAPTER_TITLE]: page 102
[CATEGORY_HEADER]: 102
[SECTION_HEADER]: 102
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition (مهارات الاستماع) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مهارات الاستماع
Classes: .text-accent
Content: استمع إلى النَّص،َ ثُمَّ أَجِب:ْ
[TEMPLATE_C_LIST.html]
- اختر الإِجَابَةَ الصَّحِيحَةَ مِمَا يَاتِي بَدَا الشَّاعِرُ فِي النَّص:ّ )مُحَدِّرًا، مُعْتَنَّا، مُدَافِعًا، لائِمًا( ، ج -۱ بَدا الشَّاعِرُ فِي النَّ مُعْتَنَّا.
- ما الجوانِبُ التِي أَسْهَمَتْ في تحقيق الجلاءِ كَمَا بَدَتْ فِي النَّصَ؟ ج٢ - أسهمت في تحقيق الجلاء جملة من الأمور، ومن بينها التضحيات التي قدمها أبناء سورية متمثلة بالدماء الطاهرة الزكية التي روت كل ذرة من تراب الوطن، وعدم الاستكانة والانقياد للمستعمر والوقوف بثبات أمام الأسلحة الفتاكة التي استعملها، وتحويل الضعف إلى قوة فاعلة تمكنت من صناعة النصر المنشود.

=== BLOCK 3: Detailed Breakdown (مهارات القراءة) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مهارات القراءة
Classes: .block-header accent
Content: * القِرَاءَةُ الصَّامِعَة:ُ
[TEMPLATE_C_LIST.html]
- تَغَنَّى الشَّاعِرُ بِصِفَاتِ الإِنْسَانِ العَرَبِيِّ فِي النَّص.َ هات صِفَتَيْنِ لَه.ُ ج ۱- أظهر الشاعر الإنسان العربي متصفا بالمروءة، شامخ الهامة، مزهوا بنفسه، فارسا شجاعا.
- هاتِ مُؤشِّرين على انتصارِ الشَّعْبِ العَرَبِيِّ السُّورِي فِي نِضَالِه.ِ ج -۲ البيت الثالث، والبيت الرابع، والبيت الرابع عشر.

=== BLOCK 4: Detailed Breakdown Part 2 (الاستيعاب والفهم - المعجم) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الاستيعاب والفهم والتحليل
Content: المستوى الفكري:
[TEMPLATE_C_LIST.html]
- استَعِنْ بِالمُعْجَم في :
- تَعَرَّفِ المَعَانِي الْمُخْتَلِفَةِ لِلفِعْلِ رَةً(، ثُمَّ اخْتَرْ مِنْها ما يُنَاسِبُ معناها في سياق النص. ج - رف: اهتر وتحرك.
- إبراز الفَرْقِ فِي الْمَعْنَى بين المهر، المهر(، وجمع كُلِّ مِنْهُما. ج - المُهْرُ : أَوَّلُ مَا يَنْتُجُ من الخيل - جمع : أَمْهار، مِهار، مهارة.
- المَهْرُ : صَدَاقُ المرأة، ما يدفعه الزوج إلى زوجته بعقد الزواج - جمعه : مهور، مهورة.

=== BLOCK 5: Detailed Breakdown Part 3 (الاستيعاب والفهم - التحليل) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الاستيعاب والفهم والتحليل (تابع)
Content:
[TEMPLATE_C_LIST.html]
- ٢- ما الفِكْرَةُ العامة التي بني عليها النَّ؟ ج -۲ التغني والاعتزاز بمنجز الجلاء، والإشادة بالتضحيات التي صنعته.
- إلامَ دَعَا الشَّاعِرُ الحَرَيَّةَ فِي المَقْطَعِ الأَوَّلِ؟ ولِمَاذا؟ - دعا الشاعر الحرية لأن تفخر وتختال كعروس مزهوة بنفسها؛ لأنها جلبت إلى ربوعنا بمهر غال نفيس، فمن أجلها تعطر تراب سورية بدماء الشهداء الأبرار.
- انطوى المقطع الثاني على تنديد ضِمْنِي بِالْمُسْتَعْمِرِ الغَرَبِي وَضِحْ ذَلِك.َ ج- ظهر التنديد بالمستعمر الغربي من خلال إظهار النقيض، حيث أظهر الشاعر الجوانب الإيجابية التي رافقت فتوحات الإنسان العربي السَّاعِي إلى نشر نور الهداية والرشاد في كل الأنحاء. فقد اهتزت الدنيا وتمايلت فرحا وارتياحا لهذه الرسالة الإنسانية التي سعى الإنسان العربي إلى نشرها. كما أنها تعنت بمحاسن الأخلاق وجميل العادات التي تحلى بها. وهذه القيم الإيجابية تعكس بشكل غير مباشر سلبيات الاستعمار الغربي الذي لا يحمل رسالة، وإنما اجتاح بلادنا طامعًا لا فاتحا، مجردًا من القيم السامية والأخلاق الحميدة؛ لذا قوبل قدومه بالرفض والتنديد.
- ه- قامَ الشَّبَابُ السوري بمهمات جليلة في سبيل نيل الاستقلال. حَدِّدها في ضَوْءٍ قهمكَ المَقْطَعِ النَّالِث.ِ ج- بذلوا التضحيات، فقد أراقوا دماءهم في سبيل تحقيق الاستقلال - لم يستسلموا للضعف ولم يرضوا به، وإنما حولوه إلى قوة تحدت أسلحة المستعمر الفتاكة. - رفضوا أشكال الوصاية والحماية والانتداب التي نادى بها المستعمر، وأصروا على أن يحموا تراب بلادهم بأنفسهم.

=== BLOCK 6: Matrix (القيم) ===
(Component: TEMPLATE_C_TABLE.html)
Title: هاتِ دَلِيلًا مِنَ النَّص على كُلِّ مِنَ القيم الواردة في الجدول الآتي:
Headers: القيمة | الدليل
Row 1: التضحية في سبيل الوطن | - لن تري حفنة رمل ... أبي - أرقناها دماء حرة .....
Row 2: تقدير بالماضي المجيد | - من هنا شق الهدى أكمامه - البيت الثامن - البيت العاشر.
Row 3: الاعتزاز بالنصر | - البيت الأول - البيت الثالث - البيت الرابع.

=== BLOCK 7: Exam (الموازنة) ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: - قالَ الشَّاعِرُ نزار قبانِي مُخَاطِبًا دِمَشْقَ فِي نَصْرِ تشرين:
[TEMPLATE_C_POEM.html]
إِنَّ مَهْرَ المَنَاضِلات ثمين | وَضَعِي طَرْحَةَ العَرُوسِ لِأَجْلِي
وازن بين هذا البيت، والبيتِ الثَّانِي عَشَرَ مِنَ النَّضِ مِنْ حِيثُ الْمَضْمُون.ِ التَّشَابُهُ : كلا الشاعرين جعل المخاطب عروسا أو كلا الشاعرين جعل المهر غاليا.

--- END STREAM ---
