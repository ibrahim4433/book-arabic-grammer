# **SESSION 116**

[TASK DEFINITION]
Objective: Implement page 116.
File: `pages/page_116.html` (Note: Use the exact page number.)
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
[LESSON_NUMBER]: 116
[CHAPTER_TITLE]: page 116
[CATEGORY_HEADER]: 116
[SECTION_HEADER]: 116
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Poem Part 1 ===
(Component: TEMPLATE_C_POEM.html)
Title: (۱)
Verses:
مَشْيَا على الأَقْدَامِ
أو زَحْفًا على الأَيْدِي نَعُودُ
قَالُوا
وكان الصَّخْرُ يَضْمُرُ
والمَسَاءُ يَدًا تَقُودُ
- ٠٩٤٧٩٠۱۱۰۹
لَمْ يَعْرِفُوا أَنَّ الطَّرِيقَ إِلَى الطَّرِيقِ
دَم،ْ وَمِصْيَدَة،ً وبيد
كُلُّ القَوافِلِ قَبْلَهُمْ غَاصَتْ
وكانَ النَّهْرُ يَبْصُقُ ضِفَتَيْهِ
قِطَعَا مِنَ اللَّحْمِ الْمُفَتَتِ
في وُجُوهِ الْعَائِدِينَ
كانوا ثلاثة عائِدِين
شَيْخٌ وَابْنَتُهُ، وَجُنْدِي قَدِيمٌ
يَقِفُونَ عِنْدَ الجِسْرِ
كانَ الجِسْرُ نَعْسَانًا ، وَكَانَ اللَّيْلُ قَبَّعَةً
وبَعْدَ دَقَائِقَ يَصِلُونَ هَلْ فِي
البيت ماء؟
وتَحَسَّسَ الْمِفْتَاحَ ثُمَّ تلا مِنَ
القُرْآنِ آيه
قالَ الشَّيخ مُنْتَعِشًا : وَكَمْ
مِنْ مَنْزِلِ فِي الْأَرْضِ
يَأْلَفُهُ الفَتَى"
قالَتْ : ولَكِنَّ المنازل يا أبي
أطلال
فَأَجَابَ : تبنيها يَدَان!
ولَمْ يُتِمَّ حَدِيثَهُ، إِذْ صَاحَ صَوْتٌ
فِي الطَّريق: تَعَالُوا
وتَلَتْهُ طَقْطَقَةُ البَنَادِقِ
لَنْ يَمُرَّ الْعَائِدُونَ
حَرَسُ الْحُدُودِ مُرَابِطُ
يَحْمِي الحُدُودَ مِنَ الْحَنِين

=== BLOCK 3: Poem Part 2 ===
(Component: TEMPLATE_C_POEM.html)
Title: (۲)
Verses:
أَمْر بإطلاق الرصاص على الذي
يجتاز هَذَا الجِسْرَ؛ هَذَا الجِسْرُ
مِقْصَلَةُ الذِي مَا زَالَ يَحْلُمُ
بالوطن
الطَّلْقَةُ الأُوْلَى أَزَاحَتْ عَنْ جَبِيْنِ
الليل
قبَّعَةَ الظَّلَامُ
والطلقَةُ الأُخْرَى ....
أَصَابَتْ قَلْبَ جُنْدِي قَدِيمٌ
والشيخ يَأْخُذُ كَلَّ إِبْنَتِهِ وَيَتْلُو
هَمْسًا مِنَ الْقُرْآنِ سُورَهُ
وبِلَهْجَةٍ كالحلم قال :
عَيْنَا حَبِيبِتِيَ الصَّغِيرَهُ
لا تَقْتُلُوهَا، وَاقْتُلُونِ لي يا جنود، ووَجْهُهَا القَمْحِيُّ لِي
Bio Block: محمود درويش
Verses (Continued):
وبرغم أَنَّ القَتْلَ كالتدخين
لَكِنَّ الجُنُودَ الطَّيبين"
الطَّالِعِينَ عَلى فَهَارِسِ دَفْتَرِ
قَذَفَتْهُ أَمْعَاءُ السنين
لم يَقْتُلُوا الاثنين
كانَ الشَّيْخُ يَسْقُطُ فِي مِيَاهِ النَّهْرِ
والبنت التِي صَارَتْ يَتِيمَهُ
كانَتْ مُمَزَّقَةَ التَّيَابِ
وطار عطر الياسمين

=== BLOCK 4: Poem Part 3 ===
(Component: TEMPLATE_C_POEM.html)
Title: (۳)
Verses:
والصَّمْتُ خَيَّمَ مَرَّةً أُخْرَى
وعادَ النَّهْرُ يَبْصُقُ ضِفَتَيْهُ
قِطَعًا مِنَ اللَّحْمِ الْمُفَتَتِ
في وُجُوهِ العَائِدِين
لم يَعْرِفُوا أَنَّ الطَّرِيقَ إِلَى الطَّرِيقِ
دم، ومصْيَدَة،ً ولم يَعْرِفُ أَحَدٌ
شَيْئًا عَنِ النَّهْرِ الذي
يَمْتَصُّ دَمَ النَّازِحِينَ
والجِسْرُ يَكْبُرُ كُل يوم كالطريق
وهِجْرَةُ الدَّم في مِيَاهِ النَّهْرِ تَنْحِتُ
مِنْ حَصَى الوادِي تَمَاثِيلًا لَهَا لَوْنُ
النُّجُوم،ِ وَلَسْعَةُ الذكرى، وطَعْمُ
الحب حينَ يَصِيرُ أَكْبَرَ مِنْ عِبَادَهُ

=== BLOCK 5: Vocabulary Explanation (Matrix) ===
(Component: TEMPLATE_C_TABLE.html)
Title: شرح المفردات الصعبة بحسب ورودها في النص:
Note: Apply `<span class="text-accent">` to the vocabulary words in the left column.
Table Content:
- يَضْمُر | هزِلَ وانكمش وانضم بعضه إلى بعض
- بيد | جمع بيداء وهي الصحراء
- أطلال | آثار
- مرابط | ملازم التغر وموضع المخافة.
- مِقْصَلة | اسم آلة من الفعل (قصل)، وهي آلة حادة كانوا يقطعون بما رقاب المحكوم عليهم بالقتل، جمعها مقاصل،
- يتلو | يقرأ
- القمحي | ما كان لونه لون القمح.

=== BLOCK 6: Explanation of Text Sections ===
(Component: TEMPLATE_C_BLOCK.html)
Classes: .accent (To satisfy orange color balance)
Title: شرح مقاطع النص:
Content:
شرح المقطع الأول : قال الشيخ وابنته والجندي القديم بحزم وإصرار : نحن مصرون على العودة إلى ديارنا مهما كلفتنا العودة من عناء وجهد. إن لهم إرادة صلبة عنيدة قوية أقوى من الصخر الذي بدا ضعيفا أمام صلابتهم وتمسكهم بقرار العودة.
- -
مكتر.

--- END STREAM ---
