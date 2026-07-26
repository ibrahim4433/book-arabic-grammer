# **SESSION 144**

[TASK DEFINITION]
Objective: Implement page 144.
File: `pages/page_144.html` (Note: Use the exact page number.)
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
[UNIQUE_ID]: b51685
[LESSON_NUMBER]: 144
[CHAPTER_TITLE]: page 144
[CATEGORY_HEADER]: 144
[SECTION_HEADER]: 144
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: تحليل النص ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b98930
[BLOCK_TITLE]: تحليل النص
[CONTENT]:
<div class="text-accent mb-4">والنص الذي أمامنا لوحة فنية استوحاها البياتي من واقع مجتمعه فعلى مستوى معاني النَّصَ نَجِدُ أَنَّ الشَّاعِرَ قَدِ افْتَتَحَهُ بِإِبراز النزوع الإنساني لدى الكادِحِين، وإظهار تمنيهم الخير لجميع الكائنات ، وَبَيَانٍ عَدَمِ حُلْمِهِم بأحلام مثالية. فالكادِحُونَ لَا يَحْلَمُونَ بِمَوتِ فَرَاشَة،ٍ ولا بِخَزْنِ وَرْدَة،ٍ ولا يَحْلُمُونَ أَحْلَامًا عَظِيمَةً كَبِيرَةَ. وَصَوَّرَ فِي المقطع الثاني معاناة الكادِحِينَ وَبَيَّنَ دَوْرَهُم في إسعاد الآخرين، وَأَظْهَرَ قَنَاعَتَهُم بِوَاقِعِهِم. فالكادِحُونَ يَتَجَرَّعُونَ مَرَارَةَ الْمَعَانَاةِ وَعَلْقَمَ الحرمان وعذابَ الفَقْرِ وَالعَوْز،ِ وَمَعَ كُلِّ ذَلِكَ يَكْدَحُونَ لِيَصْنَعُوا السَّعَادَةَ لِغَيْرِهِمْ إِنَّهُم يَتَحَدَّونَ جَحِيمَ المعاناة،ِ وَيَقْهَرُونَ قَسْوَةَ الْأَلَم،ِ فَيَصْنَعُونَ لَأَنْفُسِهِمُ الْمَسَرَّاتِ؛ لأنهم يَحْلُمُونَ بِأَحْلَامٍ مُتَوَاضِعَةٍ قَابِلَةٍ للتحقق. وفي المَقْطَعِ الثَّالِثِ أَبْرَزَ مُعاناة الكادِحِينَ وَبَساطة أحلامهم، وأكد أهم لا يَخْلُمُونَ إِلَّا بالحصول على لُ مَةِ عَيْشِ تُمْسِكُ أَصْلاتهم.</div>
وعلى مستوى تَحْدِيدِ الظَّاهِرَةِ الاجتماعِيَّةِ نَجِدُ أَنَّ المعاني السَّابِقَةَ قَد كَشَفَتْ مُعاناةَ الكَادِحِينَ مِنَ القَقْر،ِ وَبَسَاطَةَ أَحْلامِهِم، كما وَضَّحَتِ المعاني العلاقة بين الأدب والمُجْتَمَعِ إِذْ غَدا الأخيرُ مَصْدَرًا يستَمِدُ مِنْهُ الأَديب مادته الإبداعية.

=== BLOCK 3: المحتوى الواقعي الجديد ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[UNIQUE_ID]: b64191
[TITLE]: المحتوى الواقعي الجديد
[CONTENT]:
وفيما يتصل بالمحتوى الواقعي الجدِيدَ لاحِظُ أَنَّ النَّ قَدِ اسْتَطَاعَ أَنْ يُجَسَدَ وَعْيَ طَبَقَةِ الكَادِحِينِ الفَقِيرَةِ لِوَاقِعِها بما فيهِ مِنْ فَقْرِ وحِرْمَانٍ وَمُعاناة، وَأَنْ يُظْهَرَ تَأَقْلُمَهَا مَعَ واقعها المر، وقناعتها به، ورضاها بأحلام بسيطة مُتَوَاضِعَةٍ قَابِلَةٍ لِلتَّحَقَّق. ويُحْكِنَا مَا سَبَقَ أَنْ نُوَكَدَ العلاقَةَ التَّبَادُلِيَّة بين الشَّاعِرِ وَالْمُجْتَمَع، إِذْ أَخَذَ مِنْهُ مَادَّتَهُ ثُمَّ أَعادها إليهِ فَنَّا طليعيًّا يُثْبِتُ أَنَّ الأَدَبَ لِيسَ مِرْآةٌ تَعكسُ الْمُجْتَمَعَ كما هُو،َ بَلْ تُضِيفُ إِلى عَنَاصِرِهِ رُؤْيَةً جَدِيدَةً لَا تَكْتَفِي بتصوير الواقع القائم، بَلْ تَمتد إلى ما يمكن أَنْ يُنْجِرَهُ الكَادِحُونَ مِنْ نَقْلِ الوَاقِعِ مِنْ طَوْرٍ إِلَى آخَرَ أَكْثَرَ عدالة وإنسانية. وقد تَجَلَّى ذَلِكَ مِنْ خلال إظهار الكادحين متجاوزين المعاناة، وإحباطات الواقع إِذْ صَنَعُوا لَأَنْفُسِهِمُ الْمَسَرَّات،ِ وأَسْهَمُوا في إسعاد الآخرين. وهذا ما جَعَلَ النَّصَ تَرِيا بالعناصر الجديدَةِ التي تُخْرِجُهُ مِنْ كَوْنِهِ انْعِكَاسًا حَرْفِيا الواقع.

=== BLOCK 4: الوسائل الفنية ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b15746
[BLOCK_TITLE]: الوسائل الفنية المُجَسِّدة للمحتوى
[CONTENT]:
وعلى مستوى الوسائل الفَيِّةِ المُجَسَدَةِ لِلْمُحتوى نَجِدُ أَنَّ الشَّاعِرَ قَدْ حَقَّقَ رُؤْيَتَهُ بِوَسَائِلَ فَنِّيَّةٍ عَبْرَتْ عَنِ المحتوى الجديد للأدب الواقعي، فحرص على وَحْدَةِ الشَّكُلِ وَالْمَضَمُونِ؛ إِذْ كَانَ الْمَضْمُون واضحا، انطلاقا مِنْ أَنَّ الأَدَبَ يَتَوَجُهُ إِلَى جُمْهُور،ٍ وَيَنْبَغِي أَن يكونَ مَفْهُومًا، كما حافظ على رقي الشكل الفتي وسموه، باعتماده على الصورة المعَبَرَةِ النَّابِضة: (الملاين التي تكدحُ لَا تَخْلُمُ بِمَوْتِ فَرَاشَه،ُ أزهار البَنَفْسَج، قَضَعُ قُرْضَ الشَّمْسِ). وليسَتْ هَذِهِ صُورًا لِلتَّرْبِين،ِ بَلْ هِيَ صُورٌ تخدمُ الْمَعْنَى بما أَوْحَتْ بِهِ مِن إبراز النزوع الإنساني لدى الكادحين، وبما أسْهَمَتْ به مِنْ تَصوير معاناة الكادحين. كما اهتم النص بالجزئيات الصغيرة، وكذلك بالحوادث اليومية والمُشَاهِدِ الْمُعَبَرَةِ كما في المقطع الثاني. ويعُودُ ذَلِكَ الاهتمامُ إِلَى أَنَّ الشَّاعِرَ لَا يَعْرِضُ الأفكار والقضايا عرضا مُباشرًا، بَلْ يَعْرِضُهَا بِلَّغَةِ الشَّعْرِ وَرُويَاهُ الإبداعِيَّة.ُ<br>وبِمَا سَبَقَ نَجِدُ أَنَّ عملية الإبداع الفتي في المنهج الواقعي هي اتصال وجداني واع بين ذاتِ الأَديب المبدع والواقع المَوْضُوعِي، تحكمها علاقة تبادلية تأثرِيَّةُ تَعْكِسُ وَعَيَين؛ وَعْيَا بما هو قائم، وآخر بما يمكن أن يكون.

=== BLOCK 5: التطبيقات اللغوية ١ ===
(Component: TEMPLATE_C_TABLE.html)
[UNIQUE_ID]: b47708
[HEADER_1]: الجملة
[HEADER_2]: نوعها
[HEADER_3]: إعرابها
[CELL_1_1]: الملايين التي تَكْدَح،ُ لَا تَحْلَمُ فِي مَوْتِ فَرَاشَهُ وَبِأَحْرَانِ البَنَفْسَ / أو شِرَاعِ يَتَوَهَّجُ
[CELL_1_2]: التطبيقات اللغوية: ادرس مَبْحَثَ الجُمَلِ التي لها مَحَلَّ مِنَ الإعراب، والتي لا محل لها مِنَ الإعراب مُستفيدًا مَا وَرَدَ فِي الأَسْطُرِ الشَّعْرِيَّةِ الآتية:
[CELL_1_3]: ج -۱
[CELL_2_1]: (الملايين التِي تَكْدَح،ُ لَا تَحْلِّم)
[CELL_2_2]: ابتدائية
[CELL_2_3]: لا تحل لها مِنَ الإِغْراب.
[CELL_3_1]: (تَكْدَحُ)
[CELL_3_2]: صِلَةُ المَوْصُولِ
[CELL_3_3]: لَا مَحَلَّ لَهَا مِنَ الإِغراب.
[CELL_4_1]: (لا تَحْلُمُ)
[CELL_4_2]: خَبَرَيَّةٌ
[CELL_4_3]: مَحَلَّهَا الرَّفْع.ُ
[CELL_5_1]: (يَتَوَهَج)
[CELL_5_2]: صِفَةً
[CELL_5_3]: مَحَلَّهَا اجْر.ُّ

=== BLOCK 6: التطبيقات اللغوية ٢ ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b28531
[NUMBER]: ٢
[QUESTION]: هات المصدر واسم الفاعل مِنَ الفعل (يبكي).
[ANSWER]: ج -۲ المصدر : بكاء. - اسم الفاعل: الباكي.

=== BLOCK 7: التطبيقات اللغوية ٣ ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b89292
[NUMBER]: ٣
[QUESTION]: ادرس مَبْحَثَ الهُمْرَةِ لمتطرفةا. : مستفيدا مِنَ الحالة الواردة في السَّطْرِ الآتي: تَحْتَ صَوْءِ القَمَرِ الأَخْضَرِ فِي لَيْلَةٍ صَيْفٍ .
[ANSWER]: ج -۲ ضوء : هَمْرَةٌ مُتَطَرِّفَة،ٌ سُبْقَتْ بِسَاكِنٍ.

=== BLOCK 8: مقدمة القصيدة ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b35101
[BLOCK_TITLE]: أسئلة تطبيقية حول المنهج الاجتماعي في النقد الأدبي:
[CONTENT]:

=== BLOCK 9: قصيدة الزركلي ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b34364
[POET_NAME]: - قَالَ الشَّاعِرُ خَيْرُ الدِّينِ الزَّرْكُلِي:
[POEM_CONTENT]:
رَنَتْ سُعدى إليه، وَقَدْ أَلَمَّتْ
بها الأحزان واشتد البلاء
بُنَيَّ رُوَيْدَ عَذْلِكَ إِنَّ شَجْوي
لَمِمَّا قَدْ أَحَلَّ بنا القضاء
تَرَى أَخَوَيْكَ قَدْ بانا ويتنا
جياعا، لا شراب ولا غذاء

=== BLOCK 10: سؤال تطبيقي ===
(Component: TEMPLATE_C_EXAM.html)
[UNIQUE_ID]: b07676
[NUMBER]: ١
[QUESTION]: شَكَّلْ مِنْ أَلفَاظِ النَّصّ السَّابِقِ مُعْجَمًا لغويا للمعاناة ثُمَّ حَدِدٌ مِنْ خلال ذلك المعجم الظاهرة الاجتماعية التي تدور حولها الأبيات السابقة.

=== BLOCK 11: قصيدة حافظ إبراهيم ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b09909
[POET_NAME]: - قَالَ الشَّاعِرُ حافظ إبراهيم:
[POEM_CONTENT]:
لا مِلُوا فِي الصَّالِحَاتِ فَإِنَّكُم
لا تَجْهَلُونَ عَوَاقِبَ الإِثْمَالِ
إنِّي أَرَى فَقَرَاءَكُم في حاجة
لوْ تَعْلَمُونَ لِقَائِلِ فَعَالِ
فَتَسَابَقُوا الْخَيْرَاتِ فَهْيِ أَمَامَكُم
مَيْدَانُ سَيِّ لِلْجَوَادِ النَّالِ

=== BLOCK 12: قصيدة يتبع ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
[UNIQUE_ID]: b28287
[BLOCK_TITLE]: قصيدة يتبع
[CONTENT]: مكت

--- END STREAM ---