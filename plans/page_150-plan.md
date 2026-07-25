# **SESSION 150**

[TASK DEFINITION]
Objective: Implement page 150.
File: `pages/page_150.html`
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
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
15. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !

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

=== BLOCK 2: Cut Content Continuation ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
Title: تتمة
Content: ج -

=== BLOCK 3: The Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Table Content:
| الكلمة | الوزن الصرفي |
| الهوى: | الفعل، |
| يُطاولنِي | يُفاعِلُنِي، |
| الدَّهْر : | الفَعْل، |
| أَرْكَزَت:ُ | أَفْعَلْتُ ، |
| النجوم: | الفَعُول، |
| قبابِي: | فعالي. |
Note: A table matrix of the cut content words.

=== BLOCK 4: Introduction to Questions ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أسئلة تطبيقية
Content: أسئلة تطبيقية حول المنهج النفسي في النقد الأدبي:
Note: Use `.block-header accent` for orange color balance.

=== BLOCK 5: Question 1 ===
(Component: TEMPLATE_C_POEM.html)
Poet: نسيب عريضة
Title: - قَالَ الشَّاعِرُ نسيب عريضة:
Hemistichs:
أنا المُهَاجِرُ ذُو نَفْسَينِ وَاحِدَةً | تسير سيري، وأَخْرَى رَهُنُ أَوطاني
بَعُدْتُ عنها أَجُوبُ الأَرْضَ تَقْذِفُنِي | منى، حَشَثَتْ هَا رَكْي وأظعاني
ما إن أبالي مقامي في مغاربها | وفي مشارقها تحتي وإيماني
Followed by:
شَكَّلُ مِنْ أَلفَاظِ النَّصَيِّ السَّابِقِ مُعْجَمًا لغويا لِمُعَانَاةِ الشَّاعِر،ِ ثُمَّ ادْرُسُ تَمثيلَ ذَلِكَ الْمُعْجَمِ لِمَكُنوناتِ اللَّاشُعُورِ لَدَى الشَّاعِرِ .

=== BLOCK 6: Question 2 ===
(Component: TEMPLATE_C_POEM.html)
Poet: بَدْرُ الدين الحامد
Title: ٢- قَالَ الشَّاعِرُ بَدْرُ الدين الحامد :
Hemistichs:
يقولون لي: ما أَنْتَ إِلَّا مُخَالَطَ | بِعَقْلِك،َ كَمْ تَدْرِي الدموع سجالا !
نَعَمْ صَدَقُوا إِنِّي مُحِبُّ مُتَيَّمٌ | ولا بِدْعَ أَنْ دَمْعُ الْمُتَيَّم سالا
وذكراهم طي الحشاشة والهوى | مُقِيم وقَلْبِي لَا يَوَذُ فصالا
Followed by:
- قال الشاعر نديم محمد
- شَكِلْ مِنْ أَلفاظ النَّص السَّابِقِ مُعْجَمًا لغويا لمجال المعاناة،ِ ثُمَّ ادْرُسُ تَمْثِيلَ ذَلِكَ الْمُعْجَمِ لِمَكُنوناتِ اللَّاشُعُورِ لَدَى الشَّاعِرِ .

=== BLOCK 7: Question 3 ===
(Component: TEMPLATE_C_POEM.html)
Title: (Poem continues)
Hemistichs:
یا شُعُورِي يَا حَيَّةَ تَنْفُتُ السُّمُ | مَ فَيَجْرِي فِي القَلْبِ مِنْ أَلْفِ نَابِ
شهد الحب ما تَكْتَ لِأَنوا | بي مِنَ الحِسْمِ غَيْرَ جِلْدٍ خَرَابِ
لو بغير الهوى يُطاولي الده | ر لأَرْكَزْتُ فِي النُّجُومِ قِبَابِي
Followed by:
- شَجِّلْ مِنْ أَلفاظ النَّصَ مُعْجَمًا لغويا لِمُعاناةِ الشَّاعِر،ِ ثُمَّ ادْرُسِ الدِّلَالَةَ النَّفْسِيَّةَ لِصُورَةِ تَخْتَارُهَا مِنَ الْأَبْيَاتِ .

=== BLOCK 8: Question 4 (Duplicate of Ndime's Poem from Raw Text) ===
(Component: TEMPLATE_C_POEM.html)
Poet: نديم محمد
Title: - قال الشاعر نديم محمد :
Hemistichs:
یا شعُورِي يَا حَيَّةً تَنْفُتُ السُّمْ | م فَيَجْرِي فِي القَلْبِ مِنْ أَلْفِ نَابِ
شهد الحب ما تَرَكْتَ لأنوا | في مِنَ الحِسْمِ غَيْرَ جِلَدٍ خَرَابِ
لو بِغَيْرِ الهوى يطاولي الدَّه | ر لأَرْكَزْتُ فِي النُّجُومِ قِبايي
Followed by:
- شَكِّلُ مِنْ أَلَفَاظِ النَّصَ مُعْجَمًا لغويا لمجال )الألم(، ثُمَّ ادْرُسُ تَمثيل ذَلِكَ الْمُعْجَمِ لِمَكُنُونَاتِ اللاشُعُورِ لَدَى الشَّاعِر.ِ

=== BLOCK 9: Question 5 ===
(Component: TEMPLATE_C_POEM.html)
Poet: بَدْرُ الدِّين الحامد
Title: ه- قَالَ الشَّاعِرُ بَدْرُ الدِّين الحامد:
Hemistichs:
أكان التلاقي يا فُوَّادُ خَيَالا ؟! | نَعِمْنَا بِهِ ثُمَّ اضْمَحَلَّ وزالا
وليلاتنا ما بَاهُن،َ وَنَحْنُ | تم وصالا، قَدْ شَدَدْنَ رِحَالا ؟!
حرام علينا أَنْ نَنَالَ البَانَةً | وَهَذَا الزمان النكد صالَ وَجَالا
Followed by:
- شَكَّلْ مِنْ أَلفَاظِ النَّصَ السَّابِقِ مُعْجَمًا لغويا لمجال )الفراق(، ثُمَّ ادْرُسُ تَمْثِيلَ ذَلِكَ الْمُعْجَمِ لِمَكُنونَاتِ اللَّاشُعُورِ لَدَى الشَّاعِرِ .

=== BLOCK 10: Question 6 (Duplicate of Hamaid's Poem from Raw Text) ===
(Component: TEMPLATE_C_POEM.html)
Poet: بَدْرُ الدين الحامد
Title: - قَالَ الشَّاعِرُ بَدْرُ الدين الحامد:
Hemistichs:
أكانَ التَّلاقي يا فُوَّادُ خَيَالا ؟! | نَعِمْنَا بِهِ ثُمَّ اصْمَحَل وزالا
وليلاتنا ما بالهن،َّ وَنَحْنُ لَم | نتم وصالا ، قَدْ شَدَدْنَ رِحَالا ؟!
حَرَامٌ علينا أَنْ تَنَالَ لُبَانَةً | وَهَذَا الزمان النكد صالَ وَجَالا

=== BLOCK 11: Question 7 ===
(Component: TEMPLATE_C_POEM.html)
Poet: نسيب عريضة
Title: - قَالَ الشَّاعِرُ نسيب عريضة:
Hemistichs:
مَنْ أَنْتَ؟ ما أَنْتَ؟ قد وَزَعْتَ رُوحَكَ فِي | عَهْدَيْنِ مِنْ شَاسِع ماض ومن داني
أنا المُهَاجِرُ ذُو نَفْسَينِ وَاحِدَةٌ | تسير سيري، وأُخْرَى رَهْنُ أَوْطَانِي
بَعُدْتُ عنها أَجُوبُ الأَرْضَ تَقْذِفُنِي | منى، حَثَثَتُ لها ركبي وأَظْعاني

=== BLOCK 12: Exam Section ===
(Component: TEMPLATE_C_EXAM.html)
Number: -
Question: شَكِلْ مِنْ أَلفاظ النَّصَ السَّابِقِ مُعْجَمًا لغويًّا )لِمعاناة الشاعر(، ثُمَّ ادْرُسُ تَمْثِيلَ ذَلِكَ الْمُعْجَمِ لِمَكُنُونَاتِ اللاشُعُورِ لَدَيه.
Content: شَكِلْ مِنْ أَلفَاظِ النَّصَ السَّابِقِ مُعْجَمًا لغويا )لمعاناة الشاعر(، ثُمَّ ادْرُسُ تَمْشِيلَ ذَلِكَ الْمُعْجَمِ لِمَكُنُونَاتِ اللَّاشُعُورِ لَدَيه.

=== BLOCK 13: Extra symbols ===
(Component: TEMPLATE_C_BLOCK.html)
Title: - -
Content: مكتر -- -

=== BLOCK 14: Cut Content Part 1 ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
Title: يتبع
Content: - قَالَ الشاعر نسيب عريضة:

--- END STREAM ---
