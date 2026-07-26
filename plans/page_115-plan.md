# **SESSION 115**

[TASK DEFINITION]
Objective: Implement page 115.
File: `pages/page_115.html` (Note: Use the exact page number.)
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
[UNIQUE_ID]: b11501
[LESSON_NUMBER]: 115
[CHAPTER_TITLE]: page 115
[CATEGORY_HEADER]: 115
[SECTION_HEADER]: 115
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Poem 1 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b11502
[UNIQUE_ID_BIO]: b11503
[POEM_TITLE]: البيت السادس والثلاثون
[POET_NAME]: أ.الياس خفيف
[RIGHT_HEMISTICH]: لمتِ الآلام منا شملنا
[LEFT_HEMISTICH]: وغت ما بيننا من نسب

=== BLOCK 3: Explanation 1 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b11504
[BLOCK_TITLE]: الشرح والمفردات
[CONTENT]: المفردات: لمت: جمعت شملنا: بيننا نسب : الصلة والقرابة. الشرح : مصائب البلاد العربية وأوجاعها وَحَّدَتْ مَشَاعِرَ أَبنائها، فَبِسَبَبِ هذه المصائب والأوجاع ازدادت روابط القرابَةِ قُوَّةَ بَيْنَهُم.

=== BLOCK 4: Idea 1 (Orange Benefit) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[UNIQUE_ID]: b11505
[TITLE]: الفكرة
[CONTENT]: المصائب تُقَوّي الروابط القَوْمِيَّةَ بَيْنَ أَبناء الأُمَّةِ العربية.

=== BLOCK 5: Irab 1 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b11506
[UNIQUE_ID_2]: b11507
[WORD_1]: شملنا
[DETAILS_1]: مَفْعُولٌ بِهِ مَنْصُوبٌ
[WORD_2]: ما
[DETAILS_2]: اسمٌ مَوْصُولُ فِي مَحَلَّ نَصْبَ مَفْعُولَ بِهِ.

=== BLOCK 6: Poem 2 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b11508
[UNIQUE_ID_BIO]: b11509
[POEM_TITLE]: البيت السابع والثلاثون
[POET_NAME]: أ.الياس خفيف
[RIGHT_HEMISTICH]: فإذا مصر أغاني جلق
[LEFT_HEMISTICH]: وإذا بغداد نجوى يثرب

=== BLOCK 7: Explanation 2 ===
(Component: TEMPLATE_C_SPLIT.html)
[UNIQUE_ID]: b11510
[UNIQUE_ID_1]: b11511
[UNIQUE_ID_2]: b11512
[COLUMN_1_TITLE]: الشرح والمفردات
[COLUMN_1_CONTENT]: المفردات: نجوى: النجوى: إسرار الحديث. الشرح : تَوَحْدَتِ المشاعِرُ فِي الأَقْطَارِ العَرَبِيَّة،ِ فَفَرْحَةً مِصْرَ ارتَسَمَتْ على مُحَيَّا شَعْبِ سُورية، وما يجري في العراق يَتَرَدَّد صداه في أنحاء الحجاز.
[COLUMN_2_TITLE]: الفكرة والإعراب
[COLUMN_2_CONTENT]: الفكرة : تصوير وِحْدَةِ المشاعِرِ فِي الأَقْطَارِ العربية. الإعراب : إذا : فجائية. مصر، بغداد: مُبْتَدَاً مَرْفُوع. أغاني، نجوى : خَبَرٌ مَرْفُوع. جلق، يثرب : مُضَافُ إِلَيْهِ مَجْرُور.ٌ

=== BLOCK 8: Poem 3 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b11513
[UNIQUE_ID_BIO]: b11514
[POEM_TITLE]: البيت الثامن والثلاثون
[POET_NAME]: أ.الياس خفيف
[RIGHT_HEMISTICH]: ذهبت أعلامها خافقة
[LEFT_HEMISTICH]: والتقى مشرقها بالمغرب

=== BLOCK 9: Explanation 3 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b11515
[BLOCK_TITLE]: الشرح والبلاغة
[CONTENT]: الشرح : تَوَحْدَتِ المشاعِرُ فِي الأَقْطَارِ العَرَبِيَّة،ِ حيث ارتفَعَتْ أَعْلَامُها خَفَاقَةً تُرَفْرِفُ ابتهاجًا وَفَرَحًا مِنْ شَرْقِ الوَطَنِ الْعَرَبِيِّ إِلَى غَرْبِه.ِ البلاغة: (مشرقها المغرب): طباق إيجاب.

=== BLOCK 10: Irab 3 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b11516
[UNIQUE_ID_2]: b11517
[WORD_1]: أعلامها، مشرقها
[DETAILS_1]: فاعِلِّ مَرْفُوع
[WORD_2]: خافقة
[DETAILS_2]: حال منصوب.

=== BLOCK 11: Poem 4 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b11518
[UNIQUE_ID_BIO]: b11519
[POEM_TITLE]: البيت التاسع والثلاثون
[POET_NAME]: أ.الياس خفيف
[RIGHT_HEMISTICH]: كلما انقض عليها عاصف
[LEFT_HEMISTICH]: دفنته في ضلوع السحب

=== BLOCK 12: Explanation 4 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b11520
[BLOCK_TITLE]: الشرح
[CONTENT]: الشرح: كلما هاجم الأمة العربيةَ عَدُوٌّ تَخَلَّصَتْ مِنْهُ، وتفادَتْ آثارها. وَكُلَّمَا أَلَمَّتْ بِمَا مُصِيبَةٌ وَاجَهَتُها وتَخَلْصَتْ مِنْها. البلاغة: (ضلوع السحب)، (انقض): استعارَةُ مَكْنِيّة.

=== BLOCK 13: Core Matrix (Table) ===
(Component: TEMPLATE_C_TABLE.html)
[UNIQUE_ID]: b11521
[HEADER_1]: الشَّعُور
[HEADER_2]: الأداة (التراكيب)
[HEADER_3]: المثال
[CELL_1]: افتخار واعتزاز
[CELL_2]: التراكيب
[CELL_3]: كلما انقض عليها عاصف دفنته. أرى المجد انثنى يعتز بي.

=== BLOCK 14: Irab 4 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b11522
[UNIQUE_ID_2]: b11523
[WORD_1]: (عليها عاصف)
[DETAILS_1]: في محل جر بالإضافة.
[WORD_2]: (دفنته)
[DETAILS_2]: جُمْلَةُ جَوابِ الشَّرْطِ لا محل لها مِنَ الإعراب.

=== BLOCK 15: Poem 5 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b11524
[UNIQUE_ID_BIO]: b11525
[POEM_TITLE]: البيت الأربعون
[POET_NAME]: أ.الياس خفيف
[RIGHT_HEMISTICH]: بورك الخطب، فكم لف على
[LEFT_HEMISTICH]: سهمه أشتات شعب مغضب

=== BLOCK 16: Explanation 5 ===
(Component: TEMPLATE_C_SPLIT.html)
[UNIQUE_ID]: b11526
[UNIQUE_ID_1]: b11527
[UNIQUE_ID_2]: b11528
[COLUMN_1_TITLE]: المفردات والشرح
[COLUMN_1_CONTENT]: المفردات: أشتات : شَتَّتِ الأشياء شتاتًا تَفَرَّقَتْ مفردها : الشَّتُّ: متفرق. الشرح : ليبارك الباري الْمَصَائِبَ وَالمِحَن،َ فَمَا أكثر المرات التي اجتمع فيها شمل أبناء الأُمَّةِ العربية الناقمِين على الظلم والعدوان.
[COLUMN_2_TITLE]: الفكرة والإعراب
[COLUMN_2_CONTENT]: الفكرة: المصائب سَبَبْ فِي وَحْدَةِ الأُمَّةِ العَرَبَيَّة.ِ الإعراب: الخطب: نائب فاعِلِ مَرْفُوعٌ. كَمْ: خَبَرَيَّةٌ مَبْنِيَّةٌ على السكون في محل نَصْبَ مَفْعُولُ مُطْلَق. أشتات : مَفْعُولُ بِهِ مَنْصُوب.ٌ مغضب : صِفَةٌ مَجْرُورَة.ٌ

=== BLOCK 17: Poem 6 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b11529
[UNIQUE_ID_BIO]: b11530
[POEM_TITLE]: البيت الحادي والأربعون
[POET_NAME]: أ.الياس خفيف
[RIGHT_HEMISTICH]: عروس المجد حسبي عزة
[LEFT_HEMISTICH]: أن أرى المجد انثنى يعتز بي

=== BLOCK 18: Explanation 6 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b11531
[BLOCK_TITLE]: الشرح والمفردات
[CONTENT]: المفردات: انثنى: انحنى. يعتز : يَفْتَخِرُ. الشرح : أَيَّتُها الحُرَيَّةُ يَكْفِينِي عِزَّةً وافتخارا رُؤْيَةُ الْمَجْدِ مُنحَنِيَا أَمَامَ عَظَمَةِ أَبْنَاءِ الوَطَنِ مُقَدِّرًا لَهُم. الفِكرة : تَقْدِيرُ المَجْدِ لأبناء الوطن. البلاغة: (المجد انثنى)، (المجد يعتز): استعارة مكنية.

=== BLOCK 19: Irab 6 ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b11532
[TARGET_WORD]: إعراب
[IRAB_ANALYSIS]: حسبي: مبتدأ مَرْفُوع. عزة: تمييز مَنْصُوب. أن أرى المجد انثنى: الْمَصْدَرُ الْمَوَوَّلُ فِي مَحَلِّ رَفْعِ خبر. (أرى): صِلَةُ المَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الإعراب. (انثنى): في مَحَلِّ نَصْبَ مَفْعُولُ به ثان. (يعتز): في محل نصب حال. (أن أرى المجد انثنى): استئنافِيَّةٌ لا محل لها مِنَ الإعراب.

=== BLOCK 20: Poem 7 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b11533
[UNIQUE_ID_BIO]: b11534
[POEM_TITLE]: البيت الثاني والأربعون
[POET_NAME]: أ.الياس خفيف
[RIGHT_HEMISTICH]: أنا لولاه لما طوفت في كل
[LEFT_HEMISTICH]: قفر مترام مجدب

=== BLOCK 21: Explanation 7 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b11535
[BLOCK_TITLE]: الشرح والمفردات
[CONTENT]: المفردات: قفر : القَفْرُ الخلاءُ مِنَ الأَرْضِ لا ماء فيه ولا ناس ولا كلأ. مجدب : جَدَبَ المكان: يَبِسَ لاحتباس الماء فيه. الشرح : لولا رَغْبَتِي بِبُلُوغُ الْمَجْدِ لِمَا طَوَيْتُ الْمَسَافَاتِ الشَّاسِعَة،َ وجُبْتُ الأَراضي الخالية القاحِلَة.ِ الإعراب : لما: اللام واقعة في جواب لولا. ما : حَرْفَ نَفي. قفر : مُضاف إليه مجرور. مترام، مجدب: صفة مجرورة.

=== BLOCK 22: Poem 8 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b11536
[UNIQUE_ID_BIO]: b11537
[POEM_TITLE]: البيت الثالث والأربعون
[POET_NAME]: أ.الياس خفيف
[RIGHT_HEMISTICH]: رب لحن سال عن قيثارتي
[LEFT_HEMISTICH]: هز أعطاف الجهاد الأشيب

=== BLOCK 23: Explanation 8 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b11538
[BLOCK_TITLE]: الشرح والبلاغة
[CONTENT]: الشرح : كَثِيرٌ مِنَ القصائد التي جادَتْ بِهَا قَرِيحَتِي الشَّعْرِيَّةِ بَثَتْ روح الكفاح المُظَفَّر والنضال المُشَرَفِ فِي نُفُوس أبناء الأمة. البلاغة: (لحن سال)، (الجهاد الأشيب): استعارَةً مَكْنَيَّة.ٌ الإعراب : ربَّ: حَرْفُ جَرَّ شَبِيهِ بِالزَّائِد. لحن : اسمٌ مَجْرُورٌ لَفَظًا مَرْفُوعٌ مَحَلَّا على أَنَّهُ مُبْتَدَا.ً (سال): في محل رفع صفة. (هز) : في محل رفع خبر. أعطاف : مَفْعُولُ بِهِ مَنْصُوبٌ. الجهاد : مُضاف إلَيْهِ مَجْرُور. الأشيب : صِفَةً مَجْرُورَة.ُ

=== BLOCK 24: Poem 9 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b11539
[UNIQUE_ID_BIO]: b11540
[POEM_TITLE]: البيت الرابع والأربعون
[POET_NAME]: أ.الياس خفيف
[RIGHT_HEMISTICH]: لبلادي ولرواد السنا كل
[LEFT_HEMISTICH]: ما ألهمتني من أدب

=== BLOCK 25: Explanation 9 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b11541
[BLOCK_TITLE]: الشرح والإعراب
[CONTENT]: الشرح: أُهْدِي شِعْرِي وَكُلَّ أَدَبٍ أَلْهَمْتِنِي إِيَّاهُ أَيَّتُهَا الحُرَيَّةُ لوطني ولأبنائه الذين ارتقوا إلى ذرا الْمَجْد.ِ الإعراب : كل: مُبْتَدَاً مَرْفُوع. ما : اسمٌ مَوْصُولُ فِي مَحَلِّ جَرٍّ بالإضافة. (ألهمتني) : صِلَةُ المَوْصُولِ لَا مَحَلَّ لها مِنَ الإعراب.

--- END STREAM ---
