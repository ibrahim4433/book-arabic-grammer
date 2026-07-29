# **SESSION 147**

[TASK DEFINITION]
Objective: Implement page 147.
File: `pages/page_147.html` (Note: Use the exact page number.)
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
[LESSON_NUMBER]: 147
[CHAPTER_TITLE]: page 147
[CATEGORY_HEADER]: 147
[SECTION_HEADER]: 147
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: معاني المقطع الثاني ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b88499
[BLOCK_TITLE]: معاني المقطع الثاني:
[CONTENT]: يَبْدأ الشَّاعِرُ الْمُقْطَعَ الثاني بالتأكيد على أنَّ الدَّهْر قد تغلب عليه لأَنَّهُ غالبه بالهوى، فَلَو غالبه بغيره لا نتَصَرَ عليه انتصارا ساحقًا والنَصَبَ قِبَابَهُ بِينَ الشَّهب في أعالي السماء. ولطوف فيها لاهِيَا يَرْفل برداء الانتصار، ويُلاعِبُ وجنةَ البَدْر،ِ مظهرا حياةَ التَّرَفِ وَالرَّعْدِ فَتَرْشَهُ العيد الحسان المترفات بأنواع الطيوب، وينسج من أَشِعَةِ شَمْسِ الْغُرُوبِ ثوبًا وينقش أطرافه بحبات الندى ويطرزه بالطيوب.

=== BLOCK 3: معاني المقطع الثالث ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b32508
[BLOCK_TITLE]: معاني المقطع الثالث:
[CONTENT]: إِنَّ هؤلاء الكادِحِينَ يَصْنَعُونَ لأَنفُسِهِم الأفراح والمسرات على الرغم من المعاناة والألم اللذين يحيطان بحياتهم؛ لأهُم يَحْلِّمُونَ أَحْلَامًا بسيطة متواضعَةً؛ فهم لا يَحْلُمُونَ إِلَّا بِالحُصُولِ على لُ مَةِ عَيْشِ تُقِيتُهم وتمسك أصلاتهم.

=== BLOCK 4: مهارات الاستماع ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b29882
[BLOCK_TITLE]: مهارات الاستماع :
[CONTENT]: استمع إلى النَّص،َ ثُمَّ أَجِب:ْ

=== BLOCK 5: List of options ===
(Component: TEMPLATE_C_LIST.html)
[UNIQUE_ID]: b71696
[LIST_ITEM_CONTENT]: - اختر الإجابة الصحيحةً فِي كُلِّ مِمَّا يأتي :
[LIST_ITEM_CONTENT]: - يتناول النَّصُلُ مَوْضُوعًا : )أ- اجتماعيا، ب وطنيا، ج ذاتيا، د- قوميًّا(. ج- ذاتيا.
[LIST_ITEM_CONTENT]: - بَدَا الشَّاعِرُ فِي النَّص:َ )أ - مُستَبْشِرًا، ب- مُنْكَسِرًا، ج- طربًا، د- مُتَمَرِّدًا( . ج- مُنْكَسِرًا .

=== BLOCK 6: مهارات القراءة ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b14613
[BLOCK_TITLE]: مهارات القراءة:
[CONTENT]: القِرَاءَةُ الصَّامِعَةُ : اقرأ النَّصَنَّ قراءَةً صَامِنَة،ً ثُمَّ أَجِبْ :

=== BLOCK 7: Questions and Answers ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b06480
[QUESTION_NUMBER]: ۱-
[QUESTION_TEXT]: ما الفِكْرَةُ العَامَّةُ التِي يَدُورُ حَوْفَهَا النَّ؟
[ANSWER_TEXT]: ج -۱ الفِكْرَةُ العامَّةُ التِي يَدُورُ حَوْهَا النَّصُ هي مُا معاناة الشَّاعِرِ مِنْ مَشَاعِرِ الْهَوَى.

=== BLOCK 8: Questions and Answers ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b65978
[QUESTION_NUMBER]: ٢-
[QUESTION_TEXT]: ما مَصْدَرُ مُعاناة الشَّاعِر؟ وما الذي مَنَعَهُ مِنْ تَجاوز هَذِهِ المُعاناة؟
[ANSWER_TEXT]: ٢- مَصْدَرُ مُعاناة الشاعر : الحفاق احب وانكسار الآمال. والمانع مِنْ تجاوز هذه العَانَاةِ تَعَلَّفُلُ احبّ فِي قَلْبِه،ِ وَتَمَكْنُهُ منه.

=== BLOCK 9: الاستيعاب والفهم والتحليل ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b81451
[BLOCK_TITLE]: الاستيعاب والفهم والتحليل:
[CONTENT]: المستوى الفكري: ☑

=== BLOCK 10: Questions and Answers ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b63358
[QUESTION_NUMBER]: -
[QUESTION_TEXT]: استعِنْ بِالمُعْجَمِ على تَعَرَّفِ مَعْنَى كَلِمَةِ )الأصيل(، في كل ما يأتي:
قال نديم محمد : وَنَسَجْتُ الأَصِيلَ تَوْبًا وَنَقَشْ ت حوافيه بِالنَّدَى وَالْمَلابِ
قال أحمد شوقي : أو دع لسانَكَ وَاللَّغَاتِ فَرُما غَنَّى الأصيل بمنطق الأجداد
[ANSWER_TEXT]: ج - الأصيل عِنْدَ نَدِيم محمد : الوَقْتُ حِينَ تَصْفَرُ الشَّمْسُ لِمَغْرِها. و عِنْدَ شَوْقِي: كريمُ النَّسَب.

=== BLOCK 11: Questions and Answers ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b66234
[QUESTION_NUMBER]: -
[QUESTION_TEXT]: كَوَنْ مُعْجَمًا لُغَوِيا لِكُلِّ مِن : )المعاناة، السعادة(، ثُمَّ حَدَدِ الْمُعْجَمَ السَّائِدَ مِنْهُما.
[ANSWER_TEXT]: ج - المعاناة: )علتي، حزي، عذابي، السم، خراب(. - السَّعَادَةِ : ) النجوم، هوي، دعايي، النعيم الأطياب(. - المُعْجَمُ السَّائِد:ُ )المعاناة(.

=== BLOCK 12: Questions and Answers ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b66356
[QUESTION_NUMBER]: -
[QUESTION_TEXT]: اذكْرِ الْفِكْرَةَ الرَّئيسةَ لِكُلِّ مِنْ مَقْطَعَي النَّصَ مُستَعِيْنَا بِالْمُعْجَمِينِ السَّابِقِين.ِ
[ANSWER_TEXT]: - المقطع الأول: معاناة الشاعر بِسَبَبٍ مَشَاعِرِ الحب، وبيان آثارها على جَسَدِه.ِ - المقطع الثاني: الرَّغْبَةُ بِالتَّخَلُصِ مِنَ الْمَعَانَاةِ وَتَجَا الألم.

=== BLOCK 13: Questions and Answers ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b57085
[QUESTION_NUMBER]: -
[QUESTION_TEXT]: وَحِ الآثار النَّفْسِيَّةَ وَالجَسَدِيَّةَ التي تركها الشُّعُورُ فِي الشَّاعِرِ كما وَرَدَ فِي المَقْطَعِ الْأَوْل.ِ
[ANSWER_TEXT]: ج - الآثارُ النَّفْسِيَّةُ نَفَتَ الشَّعُورُ السم في قلبِه،ِ فَجَعَلَ مَرَضَهُ يَسْتَفْحِلُ وَيَتَفَاقَم،ُ وَجَعَلَ حُزْنَهُ يبلغ الدُّرْوَة،َ وَأَطَالَ أَمَدَ عَذَابِه.ِ الآثارُ الحَسَدِيَّة:ُ الْتَهَمُ الشُّعُورُ عُرُوقَ جَسَدِه،ِ وَأَفْزَعَ عِظَامَه،ُ وَأَنْخَلَ جَسَدَه،ُ وَخَرَّبَ جِلْدَه.ُ

=== BLOCK 14: Questions and Answers ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b75318
[QUESTION_NUMBER]: ه-
[QUESTION_TEXT]: انْتَابَتْ فِي المَقْطَعِ الثاني الشَّاعِرَ رَغْبَةٌ عَارِمَةً في تجاوز الحرمان وإنكارِ الْأَلَم وَضَحْ ذَلِك.َ
[ANSWER_TEXT]: جه - عِنْدَمَا عَجَرَ الشَّاعِرُ عَنْ تَجاوز الحرْمَانِ والتغلب على الألم في الواقع لا إلى عالم الخيال والتأمل، فَرَسَمَ الْأَحلام التي تُشِيرُ إِلَى رَغْبَةِ جامِحَةٍ فِي التَّخَلْصِ مِنْ مُعَانَاتِه.ِ

=== BLOCK 15: Questions and Answers ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b15790
[QUESTION_NUMBER]: -
[QUESTION_TEXT]: استنتج الظَّاهِرَةَ النَّفْسِيَّةَ التِي يَطْرَحُهَا النَّص.ُّ
[ANSWER_TEXT]: ج٦ - الظَّاهِرَةُ النَّفْسِيَّةُ التِي يَطْرَحها النص هي المعاناة بِسَيِّبِ مَشَاعِرِ الْحُب.ِّ

=== BLOCK 16: المستوى الفني ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b51512
[BLOCK_TITLE]: المستوى الفني:
[CONTENT]: المستوى الفني:

=== BLOCK 17: Questions and Answers ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b33133
[QUESTION_NUMBER]: -
[QUESTION_TEXT]: بين وظيفة استعمالِ الشَّاعِرِ حَرْفَ الشَّرْطِ )لو( في التَّعْبِيرِ عَنْ أَرْمتِهِ النَّفْسِيَّة.ِ
[ANSWER_TEXT]: ج -۱ أفادة هذا الاستعمال في التَّعِبِيرِ عَنْ عَدَمِ القَدْرَةِ عَلَى تَجَاوُنِ الأَلَم، والتَّخَلُصِ مِنْ أَرْمَتِهِ النَّفْسِيَّة،ِ بَسْبَبَ عَدَمٍ مُعَالَبَةِ الدَّهْرِ لَهُ بِغَيْرِ الْهَوَى.

--- END STREAM ---
