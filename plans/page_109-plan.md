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

=== BLOCK 2: Poem Segment (Part 1) ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[RIGHT_HEMISTICH]: وأتى الدنيا فَرَفَّتْ طَرَبًا ن
[LEFT_HEMISTICH]: وانْتَشَتْ مِنْ عَبْقِهِ الْمُنْسَكِبِ

=== BLOCK 3: Explanation and Analysis (Part 1) ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: المفردات
[HEADER_2]: الشرح
[HEADER_3]: الفكرة
[CELL_1]: رفت اهتزت وتحركت طربا الطرب خفة وهزة تعتري الإنسان عند شدة الفرح انتشت سکرت عبقه الطيب المنسكب المنصب والمنسكب اسم فاعل فعله: انسكب
[CELL_2]: وحينما غشى نور الهداية والرشاد الكون وبدد سطوع وميضه الظلمات الحالكة، اهترت الدنيا لمقدمه وتمايلت فرحا وارتياحا، واعترتها نوبة من السكر بتأثير رائحة الطيب التي فاحَتْ مِنْهُ وانصبت في كل الأنحاء
[CELL_3]: الفرح بالماضي المجيد والاعتزاز به.

=== BLOCK 4: Poetic Devices (Part 1) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: الفكرة
Content: البلاغة (الدُّنيا رَفَّتْ طَرَبَا)، (الدنيا انْتَشَتْ): استعارَةُ مَكْبَيَّة.ٌ التراكيب المثال: فَرَفَّتْ طَرَبًا. الشعور الفرح الاعتزاز بالماضي المجيد الأداة التراكيب

=== BLOCK 5: I'rab Block (Part 1) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: الدنيا
[DETAILS_1]: مَفْعُولُ بِهِ مَنْصُوبٌ
[WORD_2]: طَرَبًا
[DETAILS_2]: مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ

=== BLOCK 6: I'rab Block (Part 1b) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: وانْتَشَتْ
[DETAILS_1]: الواو، حَرْفُ عَطْفٍ انْتَشَتْ فِعْلِّ مَاضِ مَبْنِي على الفَتْحَةِ المُقَدرة على الأَلِفِ المَحْدُوفَةِ؛ لا تِصَالِهِ بِتَاءِ التَّأنيث السَّاكِنَة.ِ والنَّاء،ُ حَرْفُ تَأْنيتٍ لَا مَحَلَّ لَهُ مِنَ الإِعراب
[WORD_2]: المُنْسَكِبِ
[DETAILS_2]: صِفَةً مَجْرُورِةٌ

=== BLOCK 7: I'rab Block (Part 1c) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: جُمْلَةٌ (أَتى)
[DETAILS_1]: مَعْطُوفَة،ٌ لَا حَلَ لها مِنَ الإعراب
[WORD_2]: جُمْلَةً (رَفَّتْ)
[DETAILS_2]: مَعْطُوفَة،ٌ لَا مَحَلَّ لها مِنَ الإعراب.

=== BLOCK 8: I'rab Block (Part 1d) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: جُلْلَةُ (انْتَشَتْ)
[DETAILS_1]: مَعْطُوفَة،ٌ لَا مَحَلَّ لها مِنَ الإعراب.
[WORD_2]:
[DETAILS_2]:

=== BLOCK 9: Poem Segment (Part 2) ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[RIGHT_HEMISTICH]: وتَفَنَّتْ بالمروعات التي
[LEFT_HEMISTICH]: عَرَفَغْها في فتاها العربي

=== BLOCK 10: Explanation and Analysis (Part 2) ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: المفردات
[HEADER_2]: الشرح
[HEADER_3]: الفكرة
[CELL_1]: تَغَنَّتْ : أشادت المروءات محاسن الأخلاق وجميل العادات
[CELL_2]: وقد أشادت الدنيا وتباهت بمحاسن الأخلاق وجميل العادات والقيم السامية التي أدركتها متأصلة في الإنسان العربي
[CELL_3]: الإشادة بمروءة الإنسان العربي.

=== BLOCK 11: Poetic Devices (Part 2) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: البلاغة
Content: (الدنيا تَغَنَّتْ): استعارَةً مَكْنِيَّة

=== BLOCK 12: I'rab Block (Part 2) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: وتَغَنَّتْ
[DETAILS_1]: الواو، حَرْفُ عَطْفِ تَغَنَّتْ فِعْلِّ مَاضِ مَبْنِي على الفَتْحَةِ المقدرة على الآلِفِ المَحْذُوفة؛ لاتِصَالِهِ بِتَاءِ التَّأْنيثِ السَّاكِنَةِ وَالنَّاء،ُ حَرْفُ تَأْني لا مَحَلَّ لَهُ مِنَ الإعراب
[WORD_2]: التي
[DETAILS_2]: اسم مؤصُولُ مَبْنِي على السُّكونِ فِي مَحَلِّ جَة،ٍ صِفَةٌ

=== BLOCK 13: I'rab Block (Part 2b) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: العربي
[DETAILS_1]: صِفَةً مَجْرُورَةٌ
[WORD_2]: جملة (تَفَنَّتْ)
[DETAILS_2]: مَعْطُوفة،ٌ لا محل لها مِنَ الإعراب.

=== BLOCK 14: I'rab Block (Part 2c) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: جملة (عَرَفَتْها)
[DETAILS_1]: صِلَةُ المَوْصُول،ِ لا محل لها مِنَ الإعراب.
[WORD_2]:
[DETAILS_2]:

=== BLOCK 15: Poem Segment (Part 3) ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[RIGHT_HEMISTICH]: أَصْيَدٌ صَاقَتْ بِهِ صَحْرَاؤُهُ
[LEFT_HEMISTICH]: فَأَعَدَّنَهُ لِأَفُقِ أَرْحَبِ

=== BLOCK 16: Explanation and Analysis (Part 3) ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: المفردات
[HEADER_2]: الشرح
[HEADER_3]: الفكرة
[CELL_1]: أصيد: يرفع رأسه كبرًا، وهو المزهو المعتد بنفسه. الجمع: صيد أرحب أوسع. وأرحب اسم تفضيل، فعله: رحب
[CELL_2]: الإنسان العربي جعلته العظمة مرفوع الرأس شامخ الهامة مزهوا بنفسه رافضا أن يحصر فتوحاته في نطاق الأرض العربية، ضيق الأرض العربية، فقد أراد لهذه الفتوحات أن تتجاوز حدود الأرض العربية وتبلغ أرضا رحبةً ومدى واسعا
[CELL_3]: امتداد فتوحات العربي خارج نطاق الأرض العربية

=== BLOCK 17: I'rab Block (Part 3) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: أَصْيَدٌ
[DETAILS_1]: خَبَرٌ لِمُبْتَدا تَحْذُوفِ مَرْفُوعٌ
[WORD_2]: صَحْرَاؤُهُ
[DETAILS_2]: فَاعِلَ مَرْفُوعٌ

=== BLOCK 18: I'rab Block (Part 3b) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: أَرْحَبِ
[DETAILS_1]: صِفَةً مجرورةٌ
[WORD_2]: جُمْلَةٌ (ضَاقَتْ بِهِ صَحْرَاؤُهُ)
[DETAILS_2]: صِفَة،ً مَحَلُّهَا الرَّفْعُ

=== BLOCK 19: I'rab Block (Part 3c) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: جُمْلَهُ (أَعَدَّتْهُ)
[DETAILS_1]: مَعْطُوفَة،ٌ مَحَلَّهَا الرَّفْع.ُ
[WORD_2]:
[DETAILS_2]:

=== BLOCK 20: Poem Segment (Part 4) ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: ۱۰-
[RIGHT_HEMISTICH]: هَبَّ لِلْفَتَح،َ فَأَدْمَى تَحْتَهُ
[LEFT_HEMISTICH]: حَافِرُ الْمُهْرِ جَيِينَ الكوكب

=== BLOCK 21: Explanation and Analysis (Part 4) ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: المفردات
[HEADER_2]: الشرح
[HEADER_3]: الفكرة
[CELL_1]: هب نهض اندفع
[CELL_2]: الإنسان العربي يجوب مشارق الأرض ومغاربها حتى بلغ بفتوحاته عنان السماء
[CELL_3]: امتداد فتوحات العربي خارج نِطَاقِ الأرض العربية

=== BLOCK 22: Poetic Devices (Part 4) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: البلاغة
Content: (جبين الكوكب استعارَةً مَكْنِيَّة

=== BLOCK 23: I'rab Block (Part 4) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: تَحْتَهُ
[DETAILS_1]: مَفْعُولُ فِيهِ ظَرْفُ مَكَانٍ مَنْصُوب.ٌ
[WORD_2]: حَافِرُ
[DETAILS_2]: فَاعِلَ مَرْفُوع

=== BLOCK 24: I'rab Block (Part 4b) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: المهر
[DETAILS_1]: مُضَاف إليه تجرُورٌ
[WORD_2]: جَبِيْنَ
[DETAILS_2]: مَفْعُولُ بِهِ مَنْصُوبٌ

=== BLOCK 25: I'rab Block (Part 4c) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: الكوكب
[DETAILS_1]: مُضَاف إليه مَجْرُورٌ
[WORD_2]: جملة (هَبَّ لِلفَتْح)
[DETAILS_2]: صِفَة،ٌ مَحَلُّهَا الرَّفْعُ

=== BLOCK 26: I'rab Block (Part 4d) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: جُمَلَةً (أَدْمَى تَحْتَهُ حَافِرُ الْمُهْرِ)
[DETAILS_1]: مَعْطُوفَة،ٌ مَحَلَّهَا الرَّفْع.ُ
[WORD_2]:
[DETAILS_2]:

=== BLOCK 27: Poem Segment (Part 5) ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: ۱۱-
[RIGHT_HEMISTICH]: يَا عَرُوسَ الْمَجْد،ِ طَابَ الْمُلْتَقَى
[LEFT_HEMISTICH]: بعدما طالَ جَوَى الْمُغْتَرَبِ

=== BLOCK 28: Explanation and Analysis (Part 5) ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: المفردات
[HEADER_2]: الشرح
[HEADER_3]: الفكرة
[CELL_1]: طاب جاد وحسن جوى شدة الوجد
[CELL_2]: أيتها الحرية لقد حسن البقاء وجاد بعد أن ضاق صدر المغترب من شدة الوجد التي عانى منها طويلا.
[CELL_3]: التَّعْبِير عَنْ مَشَاعِرِ الفَرَحِ وَالزَّهو بِتَحْقِيقِ الجلاء الفرح بِجَلاء المستعمر الغربي(.

=== BLOCK 29: Poetic Devices (Part 5) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: البلاغة والتراكيب
Content: البلاغة: )طَاب، طال( جناس ناقص التراكيب المثال: طَابَ الملتقى الشعور : الفرح الأداة: الجلاء

=== BLOCK 30: I'rab Block (Part 5) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: يا
[DETAILS_1]: حَرْفُ نِدَاءٍ
[WORD_2]: عروس،َ
[DETAILS_2]: مُنَادى مُضَافَ مَنْصُوب.ُ

=== BLOCK 31: I'rab Block (Part 5b) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: المَجْدِ
[DETAILS_1]: مُضَافَ إِلِيهِ مَجْرُورٌ
[WORD_2]: المُلْتَقَى
[DETAILS_2]: فَاعِلَ مَرْفُوعٌ

=== BLOCK 32: I'rab Block (Part 5c) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: بَعْدَمَا
[DETAILS_1]: مَفْعُولُ فِيهِ ظَرْفُ زَمَانٍ مَنْصُوب. وما، حَرْفٌ مَصْدَرِيُّ
[WORD_2]: طَالَ
[DETAILS_2]: فِعْلَ مَاض،ٍ مَنْصُوب. مبي على الفَتْحَةِ الظَّاهِرَة،ِ وَالمَصْدَرُ المَ وَّل )ما طال( في محل جر، مُضَاف إليه.

=== BLOCK 33: I'rab Block (Part 5d) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: جَوَى
[DETAILS_1]: فَاعِ مَرْفُوعٌ
[WORD_2]: الْمُغْتَرَبِ
[DETAILS_2]: مُضَافَ إِلِيهِ مَجْرُورٌ

=== BLOCK 34: I'rab Block (Part 5e) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: جُمْلَةً )طَابَ الْمُلْتَقَى(
[DETAILS_1]: استئنافية، لا تحل لها مِنَ الإعراب.
[WORD_2]: جملَهُ طَالَ جَوَى الْمُغْتَرِبِ(
[DETAILS_2]: صِلَةُ المَوْصُولِ الحري، لا محل لها مِنَ الإعراب.

=== BLOCK 35: Poem Segment (Part 6) ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: ١٢-
[RIGHT_HEMISTICH]: قَدْ عَرَفْنَا مَهْرَكِ الغالي فَلَمْ نُرْخص
[LEFT_HEMISTICH]: المَهْر،َ وَلَمْ تَحْتَسِبِ

=== BLOCK 36: Explanation and Analysis (Part 6) ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: المفردات
[HEADER_2]: الشرح
[HEADER_3]: الفكرة
[CELL_1]: مهرك صداق المرأة، ما يدفعه الزوج ولم دفع صَدَاقِ مكلف لم نبال بذلك
[CELL_2]: مع أنا أدركنا أن الظفر بك أيتها الحرية يتطلب نساوم لنبخسَكِ حقك المشروع
[CELL_3]: تمجِيدُ التَّضْحِياتِ الَّتِي قَدَّمَهَا الشَّعْبُ السُّورِي والاعتزاز بِهَا تَعْجِيدِ الشَّهَادِة لِنَيْلِ استقلاله،

=== BLOCK 37: Poetic Devices (Part 6) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الأساليب والبلاغة
Content: الأساليب : قَدْ عَرَفنا أسلوب توكيد المؤكد: قد. حُكْمُ التَّوكيد : جائز . )لَمْ نُرْخص(، )م تَحْتَسِب(: أسلوب نفي الأداة: لم. أفادت نفي وقوع الفعل المضارع في الزمن الماضي. البلاغة: )الغالي، نرخص(: طباق إيجاب والشُّهَدَاء(.

=== BLOCK 38: I'rab Block (Part 6) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: مَهْرَك،ِ
[DETAILS_1]: مَفْعُولُ بِهِ مَنْصُوبٌ
[WORD_2]: الغالي
[DETAILS_2]: صِفَةٌ مَنْصُوبَة،ٌ

=== BLOCK 39: I'rab Block (Part 6b) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: فَلَمْ
[DETAILS_1]: الفَاء،ُ حَرْفُ عَطْفِ لَم،ْ حَرْفٌ جارَمٌ
[WORD_2]: نُرْخِص:ِ
[DETAILS_2]: فِعْلَ مُضَارِعٌ مَجْزُوم، وعلامَةُ جَزْمِهِ السُّكُون.ُ وحُرَكَ بِالكَسْرَةِ لِمَنْعِ الْتِقَاءِ السَّاكَنَين.

--- END STREAM ---
