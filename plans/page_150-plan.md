# **SESSION 150**

[TASK DEFINITION]
Objective: Implement page 150.
File: `pages/page_150.html` (Note: Use the exact page number.)
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
[LESSON_NUMBER]: 150
[CHAPTER_TITLE]: page 150
[CATEGORY_HEADER]: 150
[SECTION_HEADER]: 150
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Cut Content Continued ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[UNIQUE_ID]: b83760
[BLOCK_TITLE]: أوزان الأفعال
[CONTENT]: ج - الهوى: الفعل، يُطاولنِي يُفاعِلُنِي، الدَّهْر : الفَعْل، أَرْكَزَت:ُ أَفْعَلْتُ ، النجوم: الفَعُول، قبابِي: فعالي.

=== BLOCK 3: Application Questions Header ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b28696
[BLOCK_TITLE]: أسئلة تطبيقية
[CONTENT]: أسئلة تطبيقية حول المنهج النفسي في النقد الأدبي:

=== BLOCK 4: Question 1 Poem ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b65382
[POET_NAME]: - قَالَ الشَّاعِرُ نسيب عريضة:
[POET_BIO]:
[RIGHT_HEMISTICH]: أنا المُهَاجِرُ ذُو نَفْسَينِ وَاحِدَةً
[LEFT_HEMISTICH]: تسير سيري، وأَخْرَى رَهُنُ أَوطاني
[RIGHT_HEMISTICH]: بَعُدْتُ عنها أَجُوبُ الأَرْضَ تَقْذِفُنِي
[LEFT_HEMISTICH]: منى، حَشَثَتْ هَا رَكْي وأظعاني
[RIGHT_HEMISTICH]: ما إن أبالي مقامي في مغاربها
[LEFT_HEMISTICH]: وفي مشارقها تحتي وإيماني

=== BLOCK 5: Question 1 ===
(Component: TEMPLATE_C_EXAM.html)
[UNIQUE_ID]: b87985
[QUESTION_NUMBER]: ١-
[QUESTION_TEXT]: شَكَّلُ مِنْ أَلفَاظِ النَّصَيِّ السَّابِقِ مُعْجَمًا لغويا لِمُعَانَاةِ الشَّاعِر،ِ ثُمَّ ادْرُسُ تَمثيلَ ذَلِكَ الْمُعْجَمِ لِمَكُنوناتِ اللَّاشُعُورِ لَدَى الشَّاعِرِ .

=== BLOCK 6: Question 2 Poem ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b76243
[POET_NAME]: ٢- قَالَ الشَّاعِرُ بَدْرُ الدين الحامد :
[POET_BIO]:
[RIGHT_HEMISTICH]: يقولون لي: ما أَنْتَ إِلَّا مُخَالَطَ
[LEFT_HEMISTICH]: بِعَقْلِك،َ كَمْ تَدْرِي الدموع سجالا !
[RIGHT_HEMISTICH]: نَعَمْ صَدَقُوا إِنِّي مُحِبُّ مُتَيَّمٌ
[LEFT_HEMISTICH]: ولا بِدْعَ أَنْ دَمْعُ الْمُتَيَّم سالا
[RIGHT_HEMISTICH]: وذكراهم طي الحشاشة والهوى
[LEFT_HEMISTICH]: مُقِيم وقَلْبِي لَا يَوَذُ فصالا

=== BLOCK 7: Question 2 ===
(Component: TEMPLATE_C_EXAM.html)
[UNIQUE_ID]: b82009
[QUESTION_NUMBER]: -
[QUESTION_TEXT]: - شَكِلْ مِنْ أَلفاظ النَّص السَّابِقِ مُعْجَمًا لغويا لمجال المعاناة،ِ ثُمَّ ادْرُسُ تَمْثِيلَ ذَلِكَ الْمُعْجَمِ لِمَكُنوناتِ اللَّاشُعُورِ لَدَى الشَّاعِرِ .

=== BLOCK 8: Question 3 Poem ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b02081
[POET_NAME]: - قال الشاعر نديم محمد
[POET_BIO]:
[RIGHT_HEMISTICH]: یا شُعُورِي يَا حَيَّةَ تَنْفُتُ السُّمُ
[LEFT_HEMISTICH]: مَ فَيَجْرِي فِي القَلْبِ مِنْ أَلْفِ نَابِ
[RIGHT_HEMISTICH]: شهد الحب ما تَكْتَ لِأَنوا
[LEFT_HEMISTICH]: بي مِنَ الحِسْمِ غَيْرَ جِلْدٍ خَرَابِ
[RIGHT_HEMISTICH]: لو بغير الهوى يُطاولي الده
[LEFT_HEMISTICH]: ر لأَرْكَزْتُ فِي النُّجُومِ قِبَابِي

=== BLOCK 9: Question 3 ===
(Component: TEMPLATE_C_EXAM.html)
[UNIQUE_ID]: b28671
[QUESTION_NUMBER]: -
[QUESTION_TEXT]: - شَجِّلْ مِنْ أَلفاظ النَّصَ مُعْجَمًا لغويا لِمُعاناةِ الشَّاعِر،ِ ثُمَّ ادْرُسِ الدِّلَالَةَ النَّفْسِيَّةَ لِصُورَةِ تَخْتَارُهَا مِنَ الْأَبْيَاتِ .

=== BLOCK 10: Question 4 Poem ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b02482
[POET_NAME]: - قال الشاعر نديم محمد :
[POET_BIO]:
[RIGHT_HEMISTICH]: یا شعُورِي يَا حَيَّةً تَنْفُتُ السُّمْ
[LEFT_HEMISTICH]: م فَيَجْرِي فِي القَلْبِ مِنْ أَلْفِ نَابِ
[RIGHT_HEMISTICH]: شهد الحب ما تَرَكْتَ لأنوا
[LEFT_HEMISTICH]: في مِنَ الحِسْمِ غَيْرَ جِلَدٍ خَرَابِ
[RIGHT_HEMISTICH]: لو بِغَيْرِ الهوى يطاولي الدَّه
[LEFT_HEMISTICH]: ر لأَرْكَزْتُ فِي النُّجُومِ قِبايي

=== BLOCK 11: Question 4 ===
(Component: TEMPLATE_C_EXAM.html)
[UNIQUE_ID]: b62526
[QUESTION_NUMBER]: -
[QUESTION_TEXT]: - شَكِّلُ مِنْ أَلَفَاظِ النَّصَ مُعْجَمًا لغويا لمجال (الألم)، ثُمَّ ادْرُسُ تَمثيل ذَلِكَ الْمُعْجَمِ لِمَكُنُونَاتِ اللاشُعُورِ لَدَى الشَّاعِر.ِ

=== BLOCK 12: Question 5 Poem ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b62878
[POET_NAME]: ه- قَالَ الشَّاعِرُ بَدْرُ الدِّين الحامد:
[POET_BIO]:
[RIGHT_HEMISTICH]: أكان التلاقي يا فُوَّادُ خَيَالا ؟!
[LEFT_HEMISTICH]: نَعِمْنَا بِهِ ثُمَّ اضْمَحَلَّ وزالا
[RIGHT_HEMISTICH]: وليلاتنا ما بَاهُن،َ وَنَحْنُ
[LEFT_HEMISTICH]: تم وصالا، قَدْ شَدَدْنَ رِحَالا ؟!
[RIGHT_HEMISTICH]: حرام علينا أَنْ نَنَالَ البَانَةً
[LEFT_HEMISTICH]: وَهَذَا الزمان النكد صالَ وَجَالا

=== BLOCK 13: Question 5 ===
(Component: TEMPLATE_C_EXAM.html)
[UNIQUE_ID]: b15760
[QUESTION_NUMBER]: -
[QUESTION_TEXT]: - شَكَّلْ مِنْ أَلفَاظِ النَّصَ السَّابِقِ مُعْجَمًا لغويا لمجال (الفراق)، ثُمَّ ادْرُسُ تَمْثِيلَ ذَلِكَ الْمُعْجَمِ لِمَكُنونَاتِ اللَّاشُعُورِ لَدَى الشَّاعِرِ .

=== BLOCK 14: Question 6 Poem ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b58041
[POET_NAME]: - قَالَ الشَّاعِرُ بَدْرُ الدين الحامد:
[POET_BIO]:
[RIGHT_HEMISTICH]: أكانَ التَّلاقي يا فُوَّادُ خَيَالا ؟!
[LEFT_HEMISTICH]: نَعِمْنَا بِهِ ثُمَّ اصْمَحَل وزالا
[RIGHT_HEMISTICH]: وليلاتنا ما بالهن،َّ وَنَحْنُ لَم
[LEFT_HEMISTICH]: نتم وصالا ، قَدْ شَدَدْنَ رِحَالا ؟!
[RIGHT_HEMISTICH]: حَرَامٌ علينا أَنْ تَنَالَ لُبَانَةً
[LEFT_HEMISTICH]: وَهَذَا الزمان النكد صالَ وَجَالا

=== BLOCK 15: Question 7 Poem ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b02683
[POET_NAME]: - قَالَ الشَّاعِرُ نسيب عريضة:
[POET_BIO]:
[RIGHT_HEMISTICH]: مَنْ أَنْتَ؟ ما أَنْتَ؟ قد وَزَعْتَ رُوحَكَ فِي
[LEFT_HEMISTICH]: عَهْدَيْنِ مِنْ شَاسِع ماض ومن داني
[RIGHT_HEMISTICH]: أنا المُهَاجِرُ ذُو نَفْسَينِ وَاحِدَةٌ
[LEFT_HEMISTICH]: تسير سيري، وأُخْرَى رَهْنُ أَوْطَانِي
[RIGHT_HEMISTICH]: بَعُدْتُ عنها أَجُوبُ الأَرْضَ تَقْذِفُنِي
[LEFT_HEMISTICH]: منى، حَثَثَتُ لها ركبي وأَظْعاني

=== BLOCK 16: Question 7 ===
(Component: TEMPLATE_C_EXAM.html)
[UNIQUE_ID]: b30989
[QUESTION_NUMBER]: -
[QUESTION_TEXT]: شَكِلْ مِنْ أَلفاظ النَّصَ السَّابِقِ مُعْجَمًا لغويًّا (لِمعاناة الشاعر)، ثُمَّ ادْرُسُ تَمْثِيلَ ذَلِكَ الْمُعْجَمِ لِمَكُنُونَاتِ اللاشُعُورِ لَدَيه.

=== BLOCK 17: Question 8 ===
(Component: TEMPLATE_C_EXAM.html)
[UNIQUE_ID]: b00531
[QUESTION_NUMBER]: -
[QUESTION_TEXT]: شَكِلْ مِنْ أَلفَاظِ النَّصَ السَّابِقِ مُعْجَمًا لغويا (لمعاناة الشاعر)، ثُمَّ ادْرُسُ تَمْشِيلَ ذَلِكَ الْمُعْجَمِ لِمَكُنُونَاتِ اللَّاشُعُورِ لَدَيه.

=== BLOCK 18: Cut Part 1 ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
[UNIQUE_ID]: b09415
[BLOCK_TITLE]: قصيدة
[CONTENT]: - - مكتر -- - - قَالَ الشاعر نسيب عريضة:

--- END STREAM ---
