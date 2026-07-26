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
[LESSON_NUMBER]: 102
[CHAPTER_TITLE]: page 102
[CATEGORY_HEADER]: 102
[SECTION_HEADER]: 102
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: مهارات الاستماع ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مهارات الاستماع
Content: استمع إلى النَّص،َ ثُمَّ أَجِب:ْ

=== BLOCK 3: أسئلة الاستماع ===
(Component: TEMPLATE_C_LIST.html)
Item 1: اختر الإِجَابَةَ الصَّحِيحَةَ مِمَا يَاتِي بَدَا الشَّاعِرُ فِي النَّصِّ: (مُحَذِّرًا، مُعْتَزًّا، مُدَافِعًا، لائِمًا)، ج -۱ بَدا الشَّاعِرُ فِي النَّصِّ مُعْتَزًّا.
Item 2: ما الجوانِبُ التِي أَسْهَمَتْ في تحقيق الجلاءِ كَمَا بَدَتْ فِي النَّصِّ؟ ج٢ - أسهمت في تحقيق الجلاء جملة من الأمور، ومن بينها التضحيات التي قدمها أبناء سورية متمثلة بالدماء الطاهرة الزكية التي روت كل ذرة من تراب الوطن، وعدم الاستكانة والانقياد للمستعمر والوقوف بثبات أمام الأسلحة الفتاكة التي استعملها، وتحويل الضعف إلى قوة فاعلة تمكنت من صناعة النصر المنشود.

=== BLOCK 4: مهارات القراءة ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مهارات القراءة
Content: * القِرَاءَةُ الصَّامِتَة:ُ

=== BLOCK 5: أسئلة القراءة ===
(Component: TEMPLATE_C_LIST.html)
Item 1: تَغَنَّى الشَّاعِرُ بِصِفَاتِ الإِنْسَانِ العَرَبِيِّ فِي النَّصِّ. هات صِفَتَيْنِ لَه.ُ ج ۱- أظهر الشاعر الإنسان العربي متصفا بالمروءة، شامخ الهامة، مزهوا بنفسه، فارسا شجاعا.
Item 2: هاتِ مُؤشِّرين على انتصارِ الشَّعْبِ العَرَبِيِّ السُّورِي فِي نِضَالِه.ِ ج -۲ البيت الثالث، والبيت الرابع، والبيت الرابع عشر.

=== BLOCK 6: الاستيعاب والفهم والتحليل ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الاستيعاب والفهم والتحليل - المستوى الفكري
Content: أسئلة المستوى الفكري:

=== BLOCK 7: أسئلة الاستيعاب ===
(Component: TEMPLATE_C_LIST.html)
Item 1: استَعِنْ بِالمُعْجَم في : تَعَرَّفِ المَعَانِي الْمُخْتَلِفَةِ لِلفِعْلِ (رَفَّ)، ثُمَّ اخْتَرْ مِنْها ما يُنَاسِبُ معناها في سياق النص. ج - رَفَّ: اهتز وتحرك. إبراز الفَرْقِ فِي الْمَعْنَى بين (المُهْر، المَهْر)، وجمع كُلِّ مِنْهُما. ج - المُهْرُ : أَوَّلُ مَا يَنْتُجُ من الخيل - جمع : أَمْهار، مِهار، مهارة. المَهْرُ : صَدَاقُ المرأة، ما يدفعه الزوج إلى زوجته بعقد الزواج - جمعه : مُهور، مُهورة.
Item 2: ٢- ما الفِكْرَةُ العامة التي بني عليها النَّصّ؟ ج -۲ التغني والاعتزاز بمنجز الجلاء، والإشادة بالتضحيات التي صنعته.
Item 3: ٣- إلامَ دَعَا الشَّاعِرُ الحَرَيَّةَ فِي المَقْطَعِ الأَوَّلِ؟ ولِمَاذا؟ - دعا الشاعر الحرية لأن تفخر وتختال كعروس مزهوة بنفسها؛ لأنها جلبت إلى ربوعنا بمهر غال نفيس، فمن أجلها تعطر تراب سورية بدماء الشهداء الأبرار.
Item 4: ٤- انطوى المقطع الثاني على تنديد ضِمْنِي بِالْمُسْتَعْمِرِ الغَرَبِي وَضِحْ ذَلِك.َ ج- ظهر التنديد بالمستعمر الغربي من خلال إظهار النقيض، حيث أظهر الشاعر الجوانب الإيجابية التي رافقت فتوحات الإنسان العربي السَّاعِي إلى نشر نور الهداية والرشاد في كل الأنحاء. فقد اهتزت الدنيا وتمايلت فرحا وارتياحا لهذه الرسالة الإنسانية التي سعى الإنسان العربي إلى نشرها. كما أنها تغنت بمحاسن الأخلاق وجميل العادات التي تحلى بها. وهذه القيم الإيجابية تعكس بشكل غير مباشر سلبيات الاستعمار الغربي الذي لا يحمل رسالة، وإنما اجتاح بلادنا طامعًا لا فاتحا، مجردًا من القيم السامية والأخلاق الحميدة؛ لذا قوبل قدومه بالرفض والتنديد.
Item 5: ٥- قامَ الشَّبَابُ السوري بمهمات جليلة في سبيل نيل الاستقلال. حَدِّدها في ضَوْءِ فَهْمِكَ المَقْطَعِ الثَّالِث.ِ ج- بذلوا التضحيات، فقد أراقوا دماءهم في سبيل تحقيق الاستقلال - لم يستسلموا للضعف ولم يرضوا به، وإنما حولوه إلى قوة تحدت أسلحة المستعمر الفتاكة. - رفضوا أشكال الوصاية والحماية والانتداب التي نادى بها المستعمر، وأصروا أن يحموا تراب بلادهم بأنفسهم.

=== BLOCK 8: سؤال القيم ===
(Component: TEMPLATE_C_BLOCK.html)
Title: استخراج القيم
Content: هاتِ دَلِيلًا مِنَ النَّص على كُلِّ مِنَ القيم الواردة في الجدول الآتي:

=== BLOCK 9: جدول القيم ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: القيمة
[HEADER_2]: الدليل
[CELL_1_1]: التضحية في سبيل الوطن
[CELL_1_2]: - أرقناها دماء حرة ..... - لن تري حفنة رمل ... أبي
[CELL_2_1]: تقدير بالماضي المجيد
[CELL_2_2]: - من هنا شق الهدى أكمامه - البيت الثامن - البيت العاشر.
[CELL_3_1]: الاعتزاز بالنصر
[CELL_3_2]: - البيت الأول - البيت الثالث - البيت الرابع.

=== BLOCK 10: الموازنة (قصيدة) ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: قالَ الشَّاعِرُ نزار قبانِي مُخَاطِبًا دِمَشْقَ فِي نَصْرِ تشرين:
[POET_NAME]: نزار قباني
[RIGHT_HEMISTICH]: وَضَعِي طَرْحَةَ العَرُوسِ لِأَجْلِي
[LEFT_HEMISTICH]: إِنَّ مَهْرَ المَنَاضِلات ثمين

=== BLOCK 11: الموازنة (سؤال وجواب) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: موازنة
Content: وازن بين هذا البيت، والبيتِ الثَّانِي عَشَرَ مِنَ النَّصِّ مِنْ حِيثُ الْمَضْمُون.ِ التَّشَابُهُ: كلا الشاعرين جعل المخاطب عروسا أو كلا الشاعرين جعل المهر غاليا.

--- END STREAM ---
