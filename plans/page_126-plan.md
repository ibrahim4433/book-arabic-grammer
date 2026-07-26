# **SESSION 126**

[TASK DEFINITION]
Objective: Implement page 126.
File: `pages/page_126.html` (Note: Use the exact page number.)
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
[UNIQUE_ID]: b09248
[LESSON_NUMBER]: 126
[CHAPTER_TITLE]: page 126
[CATEGORY_HEADER]: 126
[SECTION_HEADER]: 126
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Cut Answer from Previous Page ===
(Component: TEMPLATE_CUT_EXAM_SOLVED_PART_2.html)
[UNIQUE_ID]: b74444
[ANSWER_TEXT_CONTINUED]: ج - الشَّاعِرُ رَافِضَ لهذه الحُدُودِ غَيْرُ مُعْتَرِفِ بِهَا، وقد تَجَلَّى ذلك مِنْ خلالِ وَصْفِهِ لِلْأَحَادِيثِ التِي تَدُورُ حَوْلَ هذه الحُدُودِ بِالْأَسَاطِيرِ والأَبَاطِيلِ الزَّائِفَة.ِ

=== BLOCK 3: Solved Question ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b94942
[QUESTION_NUMBER]: -
[QUESTION_TEXT]: تجلَّتْ في النص قِيَمْ كثيرة ، اذكرْ بَعْضًا منها. مُحَدِّدًا مِنَ النَّص مُؤَشِّرًا لكل منها.
[ANSWER_TEXT]: مبين في الجدول الآتي:

=== BLOCK 4: Values and Indicators Table ===
(Component: TEMPLATE_C_TABLE.html)
[UNIQUE_ID]: b05922
Headers:
[HEADER_1]: القيمة
[HEADER_2]: مُؤشِّرُها
Rows:
Row 1: [CELL_1]: رَفْضُ التَّجْزِيَّةِ وإنكار الحدود التي رسمها المُسْتَعْمرون | [CELL_2]: تلاشتْ مَعَ الْقُيُودِ أَسَاطِيرُ حَدُودٍ رَهِيبَةٌ نَكْرَاءُ
Row 2: [CELL_1]: التَّفَاوُلُ بِمُسْتَقْبَلِ مُشْرِقٍ وَاعِدِ | [CELL_2]: هَادَى الغَدُ الضَّحُوكَ طَلِيْقًا وبِهِ مِنْ سَنَا الرَّجَاءِ سَنَاءُ
Row 3: [CELL_1]: الاعتزاز بِتَحَرُّرِ الْأُمَّةِ الْعَرَبِيَّةِ | [CELL_2]: تَغَنَّى بِأُمَّتِي إِنَّمَا عَادَتْ وَإِنَّا فِي أَرْضِنَا طَلَقَاءُ
Row 4: [CELL_1]: تَمْجِيدُ الأَمَّةِ العَرَبِيَّةِ وَالتَّغَنِي بِصِفَاتِهَا | [CELL_2]: أُمَّة جَبَلَتْهَا مِنْ عَبِيرِ الْمَكَارِمِ العَلْيَاءُ
Row 5: [CELL_1]: تَحْفِيزُ الْمُتَرَدَدِين للالتحاقِ بِرَكْبِ الوَحْدَةِ العَرَبِيَّةِ | [CELL_2]: أَقْبِلُوا أَيُّهَا الحَيَارِي فَهَذا الدَّرْبُ طَلْق،َ مُشَوَقٌ وَضَاءُ
Row 6: [CELL_1]: الإيمانُ بِقُدْرَةِ الجَمَاهِيرِ العَرَبِيَّةِ على بِنَاءِ مَا هَدَّمَهُ المُسْتَعْمِرُ | [CELL_2]: فِي غَدِ تَزْحَفُ الْجُمُوعُ لِتَبْنِي بِيَدَيْهَا مَا هَدَّمَ الْأَعْدَاءُ

=== BLOCK 5: Introduction to Poem ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b31426
[BLOCK_TITLE]: ه- قَالَ الشَّاعِرُ سُلَيْمَان العيسى:
[CONTENT]: القصيدة:

=== BLOCK 6: Poem Evidence ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b40382
Verse 1:
[RIGHT_HEMISTICH]: يا ليالي الضياع والقيد زولي
[LEFT_HEMISTICH]: نَحْنُ بَاقُونَ وَحْدَةً لَن تَزُولَا

=== BLOCK 7: Solved Comparison Question ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b34869
[QUESTION_NUMBER]: -
[QUESTION_TEXT]: وازن بَيْنَ هَذَا الْبَيْت،ِ وَالبَيْتِ الثَّانِي مِنْ أَبْيَاتِ النَّصِّ، وَبَيَنْ أَيُّهَمَا أَفْضَلِ فِي التَّعْبِيرِ عَنِ الْمَعْنَى مَعَ التَّعْلِيل.ِ
[ANSWER_TEXT]: ج - التشابه - كلا الشَّاعِرَيْنِ يَتَحَدَّثُ عَنِ القُيُودِ والخلاص مِنْهَا. أو -: كلا الشَّاعِرَين يَتَغَنَّى بِالوَحْدَة.ِ أو : - كِلا الشَّاعِرَيْنِ يُعَبِّرُ عَنْ فَرَحِهُ بِالوَحْدَة.ِ الاختلاف : - سلامة عبيد أَكَّدَ أَنَّ القُيُودَ تَلَاشَت،ْ بينما سُلَيْمَانَ العِيسَى يَطْلُبُ مِنَ القُيُودِ أَنْ تَزُول.َ - سلامة عبيد يُؤَكِّدُ أَنَّ أَسَاطِيرَ الحُدُودِ تَلَاشَتْ مَعَ القيود، بينما سُلَيْمَان العِيسَى يَطْلُبُ أَنْ تَزُولَ لَيَالِي الضَّيَاعِ مَعَ القُيُود.ِ

=== BLOCK 8: Note on Comparison ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[UNIQUE_ID]: b17087
[TITLE]: ملاحظة
[CONTENT]: يُكتفى بوجه واحد للتشابه، وبوجه واحد للاختلاف.

=== BLOCK 9: Artistic Level Block ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b22812
[BLOCK_TITLE]: المستوى الفني:
[CONTENT]: اختر الإجابة الصَّحِيْحَةَ فيما يَأْتِي:

=== BLOCK 10: Unsolved Exam Question 1 ===
(Component: TEMPLATE_C_EXAM.html)
[UNIQUE_ID]: b05277
[QUESTION_NUMBER]: ١
[QUESTION_TEXT]: في البَيْتِ الثَّالِثِ مُحَسَن بديعي، نوعُه:ُ (جناس تام، جناس ناقص، طِبَاقُ إِيجَاب،ٍ طِبَاقُ سَلْبٍ).

=== BLOCK 11: Unsolved Exam Question 2 ===
(Component: TEMPLATE_C_EXAM.html)
[UNIQUE_ID]: b00225
[QUESTION_NUMBER]: ٢
[QUESTION_TEXT]: في قول الشاعر : (سَرَابٌ دروبكم) تقديم وتأخير غَرَضُهُ : (أ- التوكيد، ب- التشويق للمتأخر، ج- إبراز أهمية المتقدم، د- ب + ج).

=== BLOCK 12: Solved Exam Question 3 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b30781
[QUESTION_NUMBER]: -
[QUESTION_TEXT]: في البَيْتِ الأَخِيرِ مُحَسَنُ بديعي استخرجه وسمه، وَادْكُرْ قِيْمَةً مِنْ قِيَمِهِ الفَنِيَّةِ مَعَ التَّوْضِيح.
[ANSWER_TEXT]: المحسن البديعي: (تبني، هَدَّمَ). - تَسْمِيةُ المحسن البديعي: طباق إيجاب. - القيمة الفنية وتوضيحها: إعمالُ العَقْلِ في المتناقضات حيث استطاع الشاعر من خلال هذا الطباق أن يعمل عقل المتلقي في المتناقضات فجعله يدرك الفرق الشاسع بين حالة البناء، وَحَالَةِ الهَدْم.

=== BLOCK 13: Solved Exam Question 4 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b54954
[QUESTION_NUMBER]: -
[QUESTION_TEXT]: في البَيْتِ الأَوَّلِ مُحَسَنْ بَدِيعِي، اسْتَخْرِجْهُ وَسَمَه،ِ وَادْكُرْ قِيمَتَهُ الفَنِيَّة.َ
[ANSWER_TEXT]: ج - (ضِيَاء،ُ حُدَاءُ). - تَسْمِيَةُ المحسن البديعي: تصريع. - قِيمَتُهُ الفَنِيَّةُ : يضفي على الكلام رونقًا وعذوبة، ويمنحه إيقاعا موسيقيا جميلا. ويعمد الشعراء إلى استخدامه في المطالع غالبا من أجل الإعلام عن القافية قبل الوصول إليها.

=== BLOCK 14: Solved Exam Question 5 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b36407
[QUESTION_NUMBER]: -
[QUESTION_TEXT]: في قول الشاعر : الغَدُ الضَّحوك صورة بلاغيَّة،ٌ اشرَحْهَا، وَوَضَحْ وظيفتها في الإيحاء، والشرح والتوضيح.
[ANSWER_TEXT]: ج - الصورة: (الغَدُ الضَّحُوك). - تسمية الصورة: استعارة مكنية. - تحليل الصورة: شبه الغد بإنسان يضحك، فحذف المشبه به، وأبقى شيئًا من لوازمه وهو : "الضحوك". توضيح وَظِيفَةِ الإِيحَاءِ : جَعَلَ الشَّاعِرُ الصُّورَةَ موحِيَةً بتشبيهه الغد بإنسان يضحك، فهذا أوحى بالمستقبل المشرق والخير الوفير وتحقق الأحلام، وأثار مشاعر الفرح والبَهْجَةِ وَالتَّفَاول.

--- END STREAM ---
