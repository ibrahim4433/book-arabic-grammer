# **SESSION 146**

[TASK DEFINITION]
Objective: Implement page 146.
File: `pages/page_146.html` (Note: Use the exact page number.)
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
[LESSON_NUMBER]: 146
[CHAPTER_TITLE]: page 146
[CATEGORY_HEADER]: 146
[SECTION_HEADER]: 146
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Poem & Author Bio ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b41301
[UNIQUE_ID_BIO]: b23615
[POEM_TITLE]: شعوري
[POET_NAME]: نديم محمد
أ. شاعر سُوري، ولِدَ في قرية )عين شقاق بمحافظة اللاذِقِيَّة، وتَيْرَ مِنْ أبناء جِيْلِهِ بِطْفُولَةٍ فَلِقَةٍ مُشَاكِسَة،ٍ ولكنه كان أليفا صافيًا صفاء الطبيعة التي اختَضَنَتْهُ بِأَبُوَّةِ وحنانٍ تَعَلَّمَ القراءة والقرآن في القرية على يَدِ شَيْخ الكتاب، ثُمَّ أُرْسِلَ إلى بانياس لِيتَعَلَّمَ قواعد اللغة العربية، ومنها إلى مدرسة الفرير( في اللاذقية. وفي عام ٦٢٩١م أُرْسِلَ إِلَى مَدْرَسَةِ اللابيك في بيروت، ومنها إلى فرنسا لإتمام الدراسة في جامِعَةِ مُونبلييه، حَصَلَ على الإجازة في الأَدَبِ العَرَبِي،ِّ ثُمَّ انْتَقَلَ إلى سويسرا لدراسة الحقوق، ولَكِنَّهُ عاد عام ٠٣٩١م لأسبابِ خَامَّةٍ مِنْ دُونِ أَنْ يُكْمِلَ دِرَاسَتَه.ُ اتَّسَمَ بِحِسِهِ الْمُرْهَفِ وَمُعَانَاتِهِ التَّا لِيَّةِ العَمِيقَةِ لَهُ عِدَّةُ مَجْمُوعَاتٍ مِنْهَا : فراشات وعناكِب(، )فُرُوعَ مِنْ أُصُولِ(، وتَجْمُوعَةُ )آلام( التي أُخِذَ مِنْها هَذَا النَّص.ُ
[RIGHT_HEMISTICH_1]: يا شُعُورِي يَا حَيَّةٌ تَنْفُةُ السُّمْ
[LEFT_HEMISTICH_1]: مِنْ أَلْفِ نَابِ مَ فَيَجْرِي فِي القَلْبِ
[RIGHT_HEMISTICH_2]: كبرت فِيكَ عِلْتِي وَتَناهي
[LEFT_HEMISTICH_2]: فيك حزني، وطالَ فِيكَ عَذَابِي
[RIGHT_HEMISTICH_3]: أَيُّ عِرْقٍ لَمْ تَلْتَهِمْه،ُ وَعَظْمِ
[LEFT_HEMISTICH_3]: لَم تَرْعُهُ بِعَاصِف أو شهاب؟
[RIGHT_HEMISTICH_4]: - شهد الحُبُّ مَا تَرَكْتَ لِأَثْوا
[LEFT_HEMISTICH_4]: جِلْدٍ خَرَابِ فِي مِنَ الحِسْمِ غَيْرَ
[RIGHT_HEMISTICH_5]: الده ه- لو بغير الهوى يُطَاوِلني
[LEFT_HEMISTICH_5]: ر لأَرْكَزْتُ فِي النُّجُومِ قبايي
[RIGHT_HEMISTICH_6]: وَجَرَّرْتُ بُرْدَ هَوِي على البَدْ
[LEFT_HEMISTICH_6]: ر ولَطَّمْتُ خَدَّهُ بِدُعابي
[RIGHT_HEMISTICH_7]: وَلَطَوَّفُتُ بِالنَّعِيمِ فَرَشَّتْ
[LEFT_HEMISTICH_7]: نِي حِسَانُ النَّعِيم بالأطياب
[RIGHT_HEMISTICH_8]: وَتَسَجْتُ الأَصِيلَ تَوْبًا وَنَقَتْ
[LEFT_HEMISTICH_8]: ت حوافِيهِ بِالنَّدى والملاب

=== BLOCK 3: Introduction to Text ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[UNIQUE_ID]: b65161
[TITLE]: مدخل إلى النص:
[CONTENT]:
دَابَ الرومانسيون على مجيد الألم، بوصفه باعِنا على الكتابة والتوهج الإبداعي، لِذَلِكَ نَرَاهُم يُعْطُونَ قِيادَ نُفُوسِهِمْ لِلشَّعُور،ِ فَتَنْسَابُ أَسْعَارُهُم مُخْصَلَّةٌ بالدموع، متوجة بالآهات والأحزان والشكوى، مُستَبْطِنَةً خَزَائِنَ اللَّاشُعُور،ِ كَاشِفَةً عَمَّا تَوَارَى فيها مِنْ حُبّ مُخْفِق،ِ وآمال مُنْكَسِرَة،ِ وأمنياتٍ خَائِبَة،ٍ وهذا ما سَعَى الشَّاعِرُ إلى بَبِّهِ في تضاعِيفِ هَذِهِ الْأَبِيَات.ِ

=== BLOCK 4: Vocabulary Matrix ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b37746
Title: شرح المفردات الصعبة بحسب ورودها في النص:
Content:
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: الكلمة
[HEADER_2]: المعنى
[HEADER_3]: كلمات أخرى
[CELL_1_1]: شهاب
[CELL_1_2]: الشَّعْلَةُ السَّاطِعَةُ مِنَ النَّار.ِ
[CELL_1_3]: يُطاولني: يُعَالِبُني
[CELL_2_1]: أزگرت
[CELL_2_2]: ثَبَّتُ
[CELL_2_3]: دُعاي: المداعَبَةُ والملاعبة
[CELL_3_1]: الملاب
[CELL_3_2]: صَرْبٌ مِنَ الطِيبِ
[CELL_3_3]: تَرْعَهُ: تُفْزِعُهُ وَتَحِيْفُهُ
[CELL_4_1]: الأصيل
[CELL_4_2]: الوَقْتُ حِينَ تَصْفَرُ الشَّمْسُ لِمَغْرِيهَا .
[CELL_4_3]:

=== BLOCK 5: Text Meanings (Cut Box Part 1) ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
[UNIQUE_ID]: b13031
[BLOCK_TITLE]: معاني النص: معاني المقطع الأول
[CONTENT]:
يَبْدأ الشَّاعِرُ المَقْطَعَ الأَوَّلَ بنداءِ شُعُوره، ونَعْتِهِ بِالحَيَّةِ التِي تَنْفُتُ السَّمَّ، وكأنها امتلكت ألف ناب يضُحُ فِي قَلْبِهِ بِغَزارة وكثافة، السَّم،َّ ثم لا يلبث أن يجعله السبب في تفاقم مرضه واستفحاله، فيؤكد أن شعوره قد جعل حزنه يبلغ الذروة، وجعل عذابه يمتد ويَطُول.ُ ويده في قلبه. ثم يتوجه إلى شُعُورِه،ِ مَرَّةً أُخْرَى ليسأَلَهُ سُؤال العارِفِ المُسْتَنْكِر،ِ فيؤكد له من خلال هذا السؤال أنه لم يُبْقِ فِي جَسَدِهِ عِرْفًا سَلِيمًا ناجيا مِنْ أَذَاه،ُ ولا عَظْمًا مُطْمَتِنَّا لَم يُفْزِعْهُ بِعَصْفِهِ وَيُخِفْهُ بِلَهِيبٍ شِهَابِه،ِ ويُنْهِي الشَّاعِرُ هذا المَقْطَعَ بِالنَّاكِيدِ على أنَّ الْحُبَّ يَشْهَدُ أَنَّ شُعُورَهُ لَمْ يَتْرَك جِسْمَا سَلِيمًا مُعافى، إِذْ لم يترك للشباب التي يَرْتَدِيهَا إِلَّا جِلْدًا شَاحِبًا خَرِبًا.

--- END STREAM ---
