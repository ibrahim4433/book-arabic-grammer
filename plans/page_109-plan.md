# **SESSION 109**

[TASK DEFINITION]
Objective: Implement page 109.
File: `pages/page_109.html`
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
[LESSON_NUMBER]: 109
[CHAPTER_TITLE]: page 109
[CATEGORY_HEADER]: 109
[SECTION_HEADER]: 109
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Poem 1 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: شعر
[RIGHT_HEMISTICH]: وأتى الدنيا فَرَفَّتْ طَرَبًا ن
[LEFT_HEMISTICH]: وانْتَشَتْ مِنْ عَبْقِهِ الْمُنْسَكِبِ

=== BLOCK 3: Vocabulary 1 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات
Content: المنسكب: عند شدة الفرح انتشت سکرت عبقه الطيب : الطرب خفة وهزة تعتري الإنسان المفردات رفت اهتزت وتحركت طربا

=== BLOCK 4: Explanation 1 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الشرح
Content: <span class="text-accent">الشرح وحينما المنصب والمنسكب اسم فاعل فعله: انسكب الظلمات الحالكة، الكون وبدد سطوع وميضه غشى نور الهداية والرشاد الفكرة: مِنْهُ وانصبت في كل الأنحاء بتأثير رائحة الطيب التي فاحَتْ وارتياحا، واعترتها نوبة من السكر اهترت الدنيا لمقدمه وتمايلت فرحا</span>

=== BLOCK 5: Balagha 1 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: البلاغة
Content: <span class="text-accent">طَرَبَا(، )الدنيا انْتَشَتْ(: استعارَةُ مَكْبَيَّة.ٌ طَرَبًا. البلاغة: )الدُّنيا رَفَّتْ الأداة التراكيب المثال: فَرَفَّتْ الاعتزاز بالماضي المجيد الشعور الفرح</span>

=== BLOCK 6: Irab 1 ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: الدنيا :
[IRAB_ANALYSIS]: مَفْعُولُ بِهِ مَنْصُوبٌ طَرَبًا مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ وانْتَشَتْ : الواو، حَرْفُ عَطْفٍ انْتَشَتْ فِعْلِّ مَاضِ مَبْنِي على الفَتْحَةِ المُقَدرة على الأَلِفِ المَحْدُوفَةِ؛ لا تِصَالِهِ بِتَاءِ التَّأنيث السَّاكِنَة.ِ والنَّاء،ُ حَرْفُ تَأْنيتٍ لَا مَحَلَّ لَهُ مِنَ الإِعراب المُنْسَكِبِ : صِفَةً مَجْرُورِةٌ جُمْلَةٌ الإعراب :

=== BLOCK 7: Irab details 1 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: إعراب جمل
Content: <span class="text-accent">)أَتى( : مَعْطُوفَة،ٌ لَا حَلَ لها مِنَ الإعراب رَفَّتْ( : مَعْطُوفَة،ٌ لَا مَحَلَّ لها مِنَ الإعراب جُلْلَةُ انْتَشَتْ( جُمْلَةً : مَعْطُوفَة،ٌ لَا مَحَلَّ لها مِنَ الإعراب.</span>

=== BLOCK 8: Poem 2 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: شعر
[RIGHT_HEMISTICH]: وتَفَنَّتْ بالمروعات التي
[LEFT_HEMISTICH]: عَرَفَغْها في فتاها العربي

=== BLOCK 9: Vocabulary 2 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات
Content: المفردات : تَغَنَّتْ : أشادت المروءات محاسن الأخلاق وجميل العادات

=== BLOCK 10: Explanation 2 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الشرح
Content: <span class="text-accent">الشرح وقد أشادت الدنيا وتباهت بمحاسن الأخلاق وجميل العادات والقيم السامية التي أدركتها متأصلة في الإنسان العربي الفكرة الإشادة بمروءة الإنسان العربي البلاغة الدنيا تَغَنَّتْ(: استعارَةً مَكْنِيَّة العربي.</span>

=== BLOCK 11: Irab 2 ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: وتَغَنَّتْ
[IRAB_ANALYSIS]: الإعراب : وتَغَنَّتْ : الواو، حَرْفُ عَطْفِ تَغَنَّتْ فِعْلِّ مَاضِ مَبْنِي على الفَتْحَةِ المقدرة على الآلِفِ المَحْذُوفة؛ لاتِصَالِهِ بِتَاءِ التَّأْنيثِ السَّاكِنَةِ وَالنَّاء،ُ حَرْفُ تَأْني لا مَحَلَّ لَهُ مِنَ الإعراب التي: اسم مؤصُولُ مَبْنِي على السُّكونِ فِي مَحَلِّ جَة،ٍ صِفَةٌ العربي: صِفَةً مَجْرُورَةٌ جُمْلَةً )عَرَفَتْها( : صِلَةُ المَوْصُول،ِ لا محل لها مِنَ الإعراب. تَفَنَّتْ(: مَعْطُوفة،ٌ لا محل لها مِنَ الإعراب. جملة

=== BLOCK 12: Poem 3 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: شعر
[RIGHT_HEMISTICH]: صَاقَتْ بِهِ صَحْرَاؤُهُ فَأَعَدَّنَهُ
[LEFT_HEMISTICH]: لِأَفُقِ أَرْحَبِ أَصْيَدٌ

=== BLOCK 13: Vocabulary 3 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات
Content: المفردات: أصيد: يرفع رأسه كبرًا، وهو المزهو المعتد بنفسه. الجمع: صيد أرحب أوسع. وأرحب اسم تفضيل، فعله: رحب

=== BLOCK 14: Explanation 3 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الشرح
Content: <span class="text-accent">الشرح: الإنسان العربي جعلته العظمة مرفوع الرأس شامخ الهامة مزهوا بنفسه رافضا أن يحصر يقتصر على فتوحاته في نطاق ضيق الأرض العربية، الفكرة امتداد فتوحات حدود الأرض العربية وتبلغ أرضا رحبةً فقد أراد لهذه الفتوحات أن تتجاوز ومدى واسعا خارج نطاق العربي</span>

=== BLOCK 15: Irab 3 ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: أَصْيَدٌ :
[IRAB_ANALYSIS]: الإعراب : أَصْيَدٌ : خَبَرٌ لِمُبْتَدا تَحْذُوفِ مَرْفُوعٌ صَحْرَاؤُهُ : فَاعِلَ مَرْفُوعٌ الأرض العربية. أَرْحَبِ صِفَةً مجرورةٌ صِفَة،ً جُمْلَةٌ ضَاقَتْ بِهِ صَحْرَاؤُهُ( أَعَدَّتْهُ(: مَعْطُوفَة،ٌ مَحَلَّهَا الرَّفْع.ُ جُمْلَهُ حَلُّهَا الرَّفْعُ

=== BLOCK 16: Poem 4 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: شعر
[RIGHT_HEMISTICH]: ۱۰- هَبَّ لِلْفَتَح،َ فَأَدْمَى تَحْتَهُ
[LEFT_HEMISTICH]: حَافِرُ الْمُهْرِ جَيِينَ الكوكب

=== BLOCK 17: Benefit 4 ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[BENEFIT_TEXT]: المفردات هب نهض الشرح اندفع الإنسان العربي يجوب مشارق الأرض ومغاربها حتى بلغ بفتوحاته عنان السماء الفكرة: امتداد فتوحات العربي خارج نِطَاقِ الأرض العربية البلاغة: )جبين الكوكب استعارَةً مَكْنِيَّة

=== BLOCK 18: Irab 4 ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: تَحْتَهُ
[IRAB_ANALYSIS]: الإعراب : تَحْتَهُ مَفْعُولُ فِيهِ ظَرْفُ مَكَانٍ مَنْصُوب.ٌ الكوكب: مُضَاف إليه تجرُورٌ جَبِيْنَ مَفْعُولُ بِهِ مَنْصُوبٌ حَافِرُ فَاعِلَ مَرْفُوع المهر جملة )هَبَّ لِلفَتْح(: صِفَة،ٌ مَحَلُّهَا الرَّفْعُ جُمَلَةً )أَدْمَى حَافِرُ الْمُهْرِ( : مَعْطُوفَة،ٌ مَحَلَّهَا الرَّفْع.ُ

=== BLOCK 19: Poem 5 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: شعر
[RIGHT_HEMISTICH]: ۱۱- يَا عَرُوسَ الْمَجْد،ِ طَابَ الْمُلْتَقَى
[LEFT_HEMISTICH]: بعدما طالَ جَوَى الْمُغْتَرَبِ

=== BLOCK 20: Explanation 5 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الشرح
Content: <span class="text-accent">المفردات طاب جاد وحسن جوى شدة الوجد الشرح أيتها الحرية لقد حسن البقاء وجاد بعد أن ضاق صدر المغترب من شدة الوجد التي عانى منها طويلا. الفكرة : التَّعْبِير عَنْ مَشَاعِرِ الفَرَحِ وَالزَّهو بِتَحْقِيقِ الجلاء الفرح بِجَلاء المستعمر الغربي(. الأداة: الفرح : الشعور البلاغة: )طَاب، طال( جناس ناقص المثال: طَابَ الملتقى التراكيب</span>

=== BLOCK 21: Irab 5 ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: يا
[IRAB_ANALYSIS]: الإعراب : يا، حَرْفُ نِدَاءٍ عَرُوس،َ مُنَادى مُضَافَ مَنْصُوب.ُ عروس المَجْدِ مُضَافَ إِلِيهِ مَجْرُورٌ الْمُغْتَرَبِ : المُلْتَقَى: فَاعِلَ مَرْفُوعٌ بَعْدَمَا مَفْعُولُ فِيهِ ظَرْفُ زَمَانٍ وما، حَرْفٌ مَصْدَرِيُّ طَالَ : فِعْلَ مَاض،ٍ مَنْصُوب. وَالمَصْدَرُ المَ وَّل )ما طال( في محل جر، مبي على الفَتْحَةِ الظَّاهِرَة،ِ استئنافية، جُمْلَةً )طَابَ الْمُلْتَقَى(: جَوَى فَاعِ مَرْفُوعٌ مُضَاف إليه. تحل لا جملَهُ طَالَ جَوَى الْمُغْتَرِبِ(: صِلَةُ المَوْصُولِ الحري، لا محل لها مِنَ الإعراب. لها مِنَ الإعراب

=== BLOCK 22: Poem 6 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: شعر
[RIGHT_HEMISTICH]: ١٢- قَدْ عَرَفْنَا مَهْرَكِ الغالي فَلَمْ نُرْخص
[LEFT_HEMISTICH]: المَهْر،َ وَلَمْ تَحْتَسِبِ

=== BLOCK 23: Explanation 6 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الشرح
Content: <span class="text-accent">المفردات: مهرك صداق المرأة، ما يدفعه الزوج الشرح مع أنا أدركنا أن الظفر بك أيتها الحرية يتطلب دفع صَدَاقِ مكلف لم نبال بذلك ولم نساوم لنبخسَكِ حقك المشروع الفكرة تَعْجِيدِ تمجِيدُ التَّضْحِياتِ الَّتِي قَدَّمَهَا الشَّعْبُ السُّورِي والاعتزاز بِهَا لِنَيْلِ استقلاله، الشَّهَادِة الأساليب : قَدْ عَرَفنا أسلوب توكيد المؤكد: قد. حُكْمُ التَّوكيد : جائز . )لَمْ نُرْخص(، )م البلاغة: )الغالي، نرخص(: طباق إيجاب والشُّهَدَاء(.</span>

=== BLOCK 24: Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: الإعراب
[HEADER_2]: الكلمة
[HEADER_3]: إعراب
[CELL_1]: الإعراب : مَهْرَك،ِ الغالي: صِفَةٌ الْمَهْرَ : مَفْعُولُ بِهِ مَنْصُوبٌ
[CELL_2]: تَحْتَسِب(: أسلوب نفي الأداة: لم. أفادت نفي وقوع الفعل المضارع في الماضي. الزمن
[CELL_3]: فَلَمْ : الفَاء،ُ حَرْفُ عَطْفِ نُرْخِص:ِ فِعْلَ مُضَارِعٌ مَجْزُوم، لَم،ْ حَرْفٌ جارَمٌ مَنْصُوبَة،ٌ وعلامَةُ جَزْمِهِ السُّكُون.ُ وحُرَكَ بِالكَسْرَةِ لِمَنْعِ الْتِقَاءِ السَّاكَنَين. - - الحجمة

--- END STREAM ---
