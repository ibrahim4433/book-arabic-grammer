# **SESSION 116**

[TASK DEFINITION]
Objective: Implement page 116.
File: `pages/page_116.html` (Note: Use the exact page number.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
1.5 ANTI-HALLUCINATION & STRICT TYPOGRAPHER RULE (CRITICAL): Do NOT invent, hallucinate, or add new grammar rules, examples, or external text. ONLY use the exact text slices provided in the Raw Input Text. You MUST use 100% of the provided raw text. NO summarizing, NO deleting, NO adding new content. Every piece of text must map to an approved TEMPLATE.
1.6 THE TYPO EXCEPTION: You are explicitly permitted to correct obvious typos, spelling errors, or grammatical errors in the raw Arabic text during planning.
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
[UNIQUE_ID]: b00001
[LESSON_NUMBER]: 116
[CHAPTER_TITLE]: page 116
[CATEGORY_HEADER]: 116
[SECTION_HEADER]: 116
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Poem (Section 1) ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b00002
[POEM_TITLE]:
[POET_NAME]: محمود درويش
[BIO_TITLE]:
[BIO_CONTENT]:
[RIGHT_HEMISTICH]: (۱) مَشْيَا على الأَقْدَامِ أو زَحْفًا على الأَيْدِي نَعُودُ
[LEFT_HEMISTICH]: قَالُوا وكان الصَّخْرُ يَضْمُرُ والمَسَاءُ يَدًا تَقُودُ
[RIGHT_HEMISTICH]: لَمْ يَعْرِفُوا أَنَّ الطَّرِيقَ إِلَى الطَّرِيقِ دَم،ْ وَمِصْيَدَة،ً وبيد
[LEFT_HEMISTICH]: كُلُّ القَوافِلِ قَبْلَهُمْ غَاصَتْ وكانَ النَّهْرُ يَبْصُقُ ضِفَتَيْهِ
[RIGHT_HEMISTICH]: قِطَعَا مِنَ اللَّحْمِ الْمُفَتَتِ في وُجُوهِ الْعَائِدِينَ
[LEFT_HEMISTICH]: كانوا ثلاثة عائِدِين شَيْخُ وإِبْنَتُه،ُ وَجُنْدِي قَدِيمٌ
[RIGHT_HEMISTICH]: يَقِفُونَ عِنْدَ الْحِسْرِ كانَ الحِسْرُ نَعْسَانًا ،
[LEFT_HEMISTICH]: وَكَانَ اللَّيْلُ قَبَّعَةً وبَعْدَ دَقَائِقَ يَصِلُونَ
[RIGHT_HEMISTICH]: هَلْ فِي البيت ماء؟ وتَحَسَّسَ الْمِفْتَاحَ ثُمَّ تلا مِنَ القُرْآنِ آيه
[LEFT_HEMISTICH]: قالَ الشَّيخ مُنْتَعِشًا : وَكَمْ مِنْ مَنْزِلِ فِي الْأَرْضِ يَأْلَقُهُ الفَى"
[RIGHT_HEMISTICH]: قالَتْ : ولَكِنَّ المنازل يا أبي أطلال فَأَجَابَ : تبنيها يَدَان!
[LEFT_HEMISTICH]: ولَمْ يُتِمَّ حَدِينَه،ُ إِذْ صَاحَ صَوْتٌ فِي الطَّريق: تَعَالُوا
[RIGHT_HEMISTICH]: وتَلَتْهُ طَقْطَقَةُ البَنَادِقِ لَنْ يَمُرَّ الْعَائِدُونَ
[LEFT_HEMISTICH]: حَرَسُ الْحُدُودِ مُرَابِطُ يَحْمِي الحُدُودَ مِنَ الْحَنِين

=== BLOCK 3: Poem (Section 2) ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b00003
[POEM_TITLE]:
[POET_NAME]:
[BIO_TITLE]:
[BIO_CONTENT]:
[RIGHT_HEMISTICH]: (۲) أَمْر بإطلاق الرصاص على الذي يجتاز هَذَا الْجِسْرَ؛
[LEFT_HEMISTICH]: هَذَا الْحِسْرُ مِقْصَلَةُ الذِي مَا زَالَ يَحْلُمُ بالوطن
[RIGHT_HEMISTICH]: الطَّلْقَةُ الأُوْلَى أَزَاحَتْ عَنْ جَبِيْنِ الليل قبَّعَةَ الظَّلَامُ
[LEFT_HEMISTICH]: والطلقَةُ الأُخْرَى .... أَصَابَتْ قَلْبَ جُنْدِي قَدِيمٌ
[RIGHT_HEMISTICH]: والشيخ يَأْخُذُ كَلَّ إِبْنَتِهِ وَيَتْلُو هَمْسًا مِنَ الْقُرْآنِ سُورَهُ
[LEFT_HEMISTICH]: وبِلَهْجَةٍ كالحلم قال : عَيْنَا حَبِيبِتِيَ الصَّغِيرَهُ
[RIGHT_HEMISTICH]: لا تَقْتُلُوهَا، وَاقْتُلُونِ لي يا جنود، ووَجْهُهَا القَمْحِيُّ لِي
[LEFT_HEMISTICH]: وبرغم أَنَّ القَتْلَ كالتدخين الكِنَّ الجُنُودَ الطَّيبين"
[RIGHT_HEMISTICH]: الطَّالِعِينَ عَلى فَهَارِسِ دَفْتَرِ قَذَفَتْهُ أَمْعَاءُ السنين
[LEFT_HEMISTICH]: لم يَقْتُلُوا الاثنين كانَ الشَّيْحُ يَسْقُطُ فِي مِيَاهِ النَّهْرِ
[RIGHT_HEMISTICH]: والبنت التِي صَارَتْ يَتِيمَهُ كانَتْ مُمَزَّقَةَ التَّيَابِ وطار عطر الياسمين

=== BLOCK 4: Poem (Section 3) ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b00004
[POEM_TITLE]:
[POET_NAME]:
[BIO_TITLE]:
[BIO_CONTENT]:
[RIGHT_HEMISTICH]: (۳) والصَّمْتُ خَيَّمَ مَرَّةً أُخْرَى وعادَ النَّهْرُ يَبْصُقُ ضِفَتَيْهُ
[LEFT_HEMISTICH]: قِطَعًا مِنَ اللَّحْمِ الْمُفَتَتِ في وُجُوهِ العَائِدِين
[RIGHT_HEMISTICH]: لم يَعْرِفُوا أَنَّ الطَّرِيقَ إِلَى الطَّرِيقِ دم، ومصْيَدَة،ً
[LEFT_HEMISTICH]: ولم يَعْرِفُ أَحَدٌ شَيْئًا عَنِ النَّهْرِ الذي يَمْتَصُّ دَمَ النَّازِحِينَ
[RIGHT_HEMISTICH]: والحِسْرُ يَكْبُرُ كُل يوم كالطريق وهِجْرَةُ الدَّم في مِيَاهِ النَّهْرِ تَنْحِتُ
[LEFT_HEMISTICH]: مِنْ حَصَى الوادِي تَمَاثِيلًا لَهَا لَوْنُ النُّجُوم،ِ
[RIGHT_HEMISTICH]: وَلَسْعَةُ الذكرى، وطَعْمُ الحب حينَ يَصِيرُ أَكْبَرَ مِنْ عِبَادَهُ

=== BLOCK 5: Vocabulary Matrix ===
(Component: TEMPLATE_C_TABLE.html)
[UNIQUE_ID]: b00005
[TABLE_TITLE]: شرح المفردات الصعبة بحسب ورودها في النص:
[TABLE_HEADER_1]: المفردة
[TABLE_HEADER_2]: شرحها
[ROW_1_COL_1]: يَضْمُر
[ROW_1_COL_2]: هزِلَ وانكمش وانضم بعضه إلى بعض
[ROW_2_COL_1]: بيد
[ROW_2_COL_2]: جمع بيداء وهي الصحراء
[ROW_3_COL_1]: أطلال
[ROW_3_COL_2]: آثار
[ROW_4_COL_1]: مرابط
[ROW_4_COL_2]: ملازم الثغر وموضع المخافة.
[ROW_5_COL_1]: يتلو
[ROW_5_COL_2]: يقرأ
[ROW_6_COL_1]: القمحي
[ROW_6_COL_2]: ما كان لونه لون القمح.

=== BLOCK 6: Benefit Warning ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[UNIQUE_ID]: b00006
[BLOCK_TITLE]: مِقْصَلة :
[CONTENT]: اسم آلة من الفعل (فصل)، وهي آلة حادة كانوا يقطعون بها رقاب المحكوم عليهم بالقتل، جمعها مقاصل.

=== BLOCK 7: Explanation (Cut Box) ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
[UNIQUE_ID]: b00007
[BLOCK_TITLE]: شرح مقاطع النص:
[CONTENT]: <span class="text-accent">شرح المقطع الأول :</span> قال الشيخ وابنته والجندي القديم بحزم وإصرار : نحن مصرون على العودة إلى ديارنا مهما كلفتنا العودة من عناء وجهد. إن لهم إرادة صلبة عنيدة قوية أقوى من الصخر الذي بدا ضعيفا أمام صلابتهم وتمسكهم بقرار العودة.

--- END STREAM ---
