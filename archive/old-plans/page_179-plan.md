# **SESSION 179**

[TASK DEFINITION]
Objective: Implement page 179.
File: `pages/page_179.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
2.5 Cut Content: Not applicable here.
2.6 Cut Content Determinism: Not applicable here.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide: NO INLINE STYLES.
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). Use "Jules-workspace/id_manager.py".
8. Self-Correction: Run "Jules-workspace/lint_pages.py --one-page-mode <filename>".
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...) .
11. You must preserve the exact Tashkeel provided in the input and add any missing Tashkeel needed.
12. Visual Density: The page must be dense.
13. balanced page colors between teal and orange: make sure every page have minimum 1 element in orange.
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (`.force-new-page`).
15. Exam section always be in the end of the lesson without answers.
16. The Strict Typographer Rule overrides the mandatory Exam section rule. If the raw text does not contain exam questions, do not fabricate an Exam block. However, if the text contains an exam prompt and its answer, place the answer text in a preceding 'Benefit' block, or a `TEMPLATE_C_TABLE.html` to satisfy the 'Must have a Matrix' rule without violating the exam format.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 179
[CHAPTER_TITLE]: page 179
[CATEGORY_HEADER]: 179
[SECTION_HEADER]: 179
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Question 1 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: - استَخْرِجُ مِنَ المَقْطَعِ الثَّالِثِ أُسلُوبَ قَصْر،ِ وَبَيِّنْ أَثَرَهُ فِي خِدْمَةِ الْمَعْنى
Content: <span class="text-accent">ج۳ - أُسلُوبُ القَصْرِ : إِنَّهَا النَّاسُ سُطُور.ٌ </span><br>أَثَرُهُ فِي خِذَمَةِ المغنى : وَضَحَ هذا الأسلُوبُ المَعْنَى وَأَكَدَه،ُ فَقَدْ كَشَفَ حَقِيقَةَ النَّاسِ كما يراها جبران، عندَمَا قَصَرَهُمْ عَلَى سُطُورِ مَكُتُوبَةٍ بِمَاء،ٍ فَدَفَعَ بِذَلِكَ التَّوَهُمَ بِأَيَّ صِفَةٍ أُخْرَى يَتَصِفُونَ بها.

=== BLOCK 3: The Core Matrix (Table) ===
(Component: TEMPLATE_C_TABLE.html)
Title: ادْكُرْ دِلالَةَ كُلِّ رَمْرٍ مِمَّا يَأْتِي وَفْقَ الجَدُولِ :
[TABLE_HEADER_1]: الرمز
[TABLE_HEADER_2]: دلالته
[ROW_1_COL_1]: غُيُومُ النَّفْسِ
[ROW_1_COL_2]: سوداويةُ النَّفْسِ وَتَشَاؤُمِها
[ROW_2_COL_1]: الغاب
[ROW_2_COL_2]: الحياة المثالية المتحررةُ مِنَ الوَهُم والنِّفَاقِ
[ROW_3_COL_1]: النور
[ROW_3_COL_2]: دِفْءُ الشَّمْسِ في العالم المثالي
[ROW_4_COL_1]: الناي
[ROW_4_COL_2]: الفن

=== BLOCK 4: Question 5 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ه- استَخْرِجُ مِنَ الْمُقْطَعِ الْأَوَّلِ : )تَشْبِيْهَا بَلِيْفًا، استِعَارَةُ مَكْنِيَّة،ٌ وَبَين وظيفةً لِكُلِّ مِنْهُما :
Content:

=== BLOCK 5: Q5 List ===
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: <span class="highlight-red">جه التشبيه البليغ:</span> )حُزْنُ النَّفْسِ ظِلُ وَهُم(. - الوظيفة الشرح والتَّوضِيحُ شَرَحَتِ الصُّورَةُ مَعْنَى : )خُلَوَ عَالَمِ الغَابِ مِنَ الْأَحْرَانِ وتَجَرَّدِهِ مِنَ الهُمُوم( ، وَوَ حَتْ ذَلِكَ الْمَعْنَى مِنْ خِلالِ تَشْبِيهِ حُزْنِ النَّفْسِ بِ لَ وَهُم،ْ فَأَقْنَعَتِ الْمُتَلَقِيَ بِمَضْمُونِ الْمَعْنَى وَصِدْقِه.ِ
[LIST_ITEM_CONTENT]: <span class="highlight-red">الاستعارة المكنية :</span> )أَنِينُ النَّايِ يَبْقَى(. - الوظيفة : الشَّرْحُ والتَّوضِيحُ شَرَحَتِ الصُّورَةُ مَعْنَى : )خُلُودِ الفَنِّ وبقائِهِ واستمراره(، وَوَضَحَتْ ذَلِكَ الْمَعْنَى مِنْ خِلَالٍ تَشْبِيهِ النَّاي بكائِنِ يَنُ فَأَقْنَعَتِ الْمُتَلَقِيَ بِمَضْمُونِ الْمَعْنَى وَصِدْقِه.ِ

=== BLOCK 6: Question 7 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: - استَخْرِجُ مِنَ البَيْتِ السَّابِعِ عَشَرَ طِبَاقًا، وَادْكُرْ قِيمَةً مِنْ قِيَمِهِ الفَنِّيَّةِ مَعَ التَّوْضِيح.
Content: ج - الطباق : )داء، دواء(. - القِيمَةُ الفَنِّيَّة:ُ اسْتَطَاعَ الشَّاعِرُ مِنْ خلال هذا الطباق تحقيق قيم فنية كثيرة منها :

=== BLOCK 7: Q7 List ===
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: - إظْهَارُ المَعْنَى بِجَلَاءٍ وَوُصُوحٍ : حيثُ أَوضَحَ الشَّاعِرُ مِنْ خِلال هذا الطَّبَاقِ انتفَاءَ المَوْتِ أَمَامَ تَرَاتِيلِ الغناء وَتَرَانِيمَ الْمُؤْسِيقَى فِي عَالَمِ الغاب المثالي.
[LIST_ITEM_CONTENT]: -٢ إثارة الخَيَالِ : تَمَكْنَ الشَّاعِرُ مِنْ خلال هذا الطباق مِنْ إِثارة خيالِ الْمُتَلي، وَجَعْلِهِ يَتَخَيَّلُ ذَلِكَ العالم المثالي الذي يَنْتَفِي فِيهِ الْمَوْتُ أَمَامَ تَرَاتيل الغناء، وترانيم المُؤْسِيقَى.
[LIST_ITEM_CONTENT]: ٣- إِعْمَالُ العقل في المتناقضات : تَمَكُنَ الشَّاعِرُ مِنْ خِلالِ هذا الطَّبَاقِ مِنْ إِعْمَالِ عَقْلِ الْمُتَلَقِي فِي الْمُتَنَاقِضَات،ِ فَجَعَلَهُ يُدْرِكُ الفَرْقَ الشَّاسِعَ بِينَ عَالَ الغَابِ التَابِي والواقع.
[LIST_ITEM_CONTENT]: - ٤ تَحْدِيدُ الرُّوْيَةِ الْمَوْقِف( : تَمَكَّنَ هذا الطَّبَاقُ مِنَ الكُشْفِ عَنْ مَوْقِفِ الشَّاعِر،ِ حيثُ أَظْهَرَ مَيْلَهُ الشَّدِيد،َ ونُرُوعَهُ إِلَى عَالَمِ الغَابِ الْمِثَالِي.ِّ

=== BLOCK 8: Feelings ===
(Component: TEMPLATE_C_BLOCK.html)
Title: - سَرَى فِي النَّ شُعُورانِ عَاطِفِيَّانِ خَفِيَّانِ الحَنِينُ إِلَى الوَطَن،ِ وَالْأَمَّ مِنْ غُرْبَةٍ قَاسِيَةٍ دُلِّ على مَوْطَنِ كُلِّ مِنْهُمَا فِي الن.َّ
Content: ج - شُعُورُ الحنين إلى الوطن: في المقطع الثاني. - شُعُورُ الأَلَمِ مِنْ غُرْبَةٍ قَاسِيَة:ِ فِي المَقْطَعِ الأَوَّل.ِ

=== BLOCK 9: External Music ===
(Component: TEMPLATE_C_BLOCK.html)
Title: هات مَصْدَرًا مِنْ مَصَادِرِ الموسيقا الخارجيَّةِ فِي النَّص، وَمَثَلْ لَهُ بِمَا يُنَاسِب.ُ
Content: ج- لجَنَّ الشَّاعِرُ إِلى وَزْنِ قَصِيرٍ هُوَ تَجْرُوءُ الرَّمَلِ بِمَا فِيهِ مِنْ حَفَةٍ تَتَوَاءَمُ مَعَ شَفَافِيَّةِ التعبير واللوحات الطبيعية المُتَخَيَّلَةِ المُتَتَابِعَة،ِ كما لجأ إلى تنويع القوافي وتوزيعها توزيعًا مُتَنَا مَا مِنْ خِلال القطع بالتسكين.

=== BLOCK 10: Internal Music ===
(Component: TEMPLATE_C_BLOCK.html)
Title: - في النص موسيقا داخِلِيَّةٌ ثَرَّةٌ مَثَلْ لِثَلاثةِ مَصَادِرَ مِثَالِ وَاحِدٍ مُنَاسِبٍ لِكُلِّ مِنْهَا.
Content: ج - ۹ مِنْ مَصَادِرِ الموسيقا الداخلية البارزة في النَّص:

=== BLOCK 11: Internal Music List ===
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: -١ التَّنَاغُمُ والانْسجامُ بَينَ حُرُوفِ الهَمْس،ِ وحُرُوفِ الجَهْرِ فِي الكَلِمَاتِ المتعاقبة في البَيْتِ الثَّالِثَ عَشَرَ : )هَلَ فَرَشْتَ المُشْب،ِ تَلَحْفْتَ الفَضَا(.
[LIST_ITEM_CONTENT]: -٢ التَّنَاغُمُ والأنْسِجَامُ بَيْنَ حُرُوفِ المَدِ الطويل، وحُرُوفِ المَدِ القَصِيرِ فِي البَيْتِ السَّابِع: الغاب، مِثْلِي، دُونَ القُصُور(.
[LIST_ITEM_CONTENT]: ٣- التَّقَابُلُ بَيْنَ الكَلِمَاتِ كِ بَاقِ الإيجاب )دَاء،ً دواء(.

=== BLOCK 12: Verse Cutting ===
(Component: TEMPLATE_C_BLOCK.html)
Title: -۱۰ قطع البيت الأَوَّلَ مِنَ النَّصْي،ِّ وَسَمَ بِحْرَه.ُ
Content: ج -۱۰ تقطيع البيت الأَوَّلِ مِنَ النَّص،َ وتسميةُ بَحْرِهِ بَحْرُ الرَّمَلِ تجزوء(.<br><br>لَيْسَ فِي الغَا بَاتِ حُزْنٌ / لا ولا في ها الهموم<br>이 이이이  이<br>فاعلاتن / فاعلاتن فاعلاتن فاعلن

=== BLOCK 13: Orange Benefit Answer ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: المستوى الإبداعي:
Content: الإجابة : أَيُّهَا النَّائِهُونَ فِي مَتَاهَاتِ الغُرْبَةِ المُشَرَّدُونَ فِي أَصْقَاعِهَا النَّائِيَةِ الْمَحْرُومُونَ مِنْ نَعِيمٍ وَطَيْكُم إِنَّ وَطَنَكُم مَنْجَاً لأَفْئِدَتِكُم وَمَهْوى الأرواحكُم فَالْوَطَنُ مَلَادٌ آمِنْ يَضُمُ أَبْنَاءَه،ُ وَيَصُونُ كَرَامَتَهُم وَعِزَّهُم وَيَنَعُهُم مِنْ كُلِّ التَّشَرُّدِ والحاجة؛ فهو المكان الذي تَسْكُنُ إِلَيهِ النَّفْس،ُ وتَرْتَاحُ وقدَا،ً ولأَجْلِ ذَلِكَ اسْتَحَقِّ أَنْ يَكُونَ أَجْدَرَ الأَمَاكِنِ بِالسَّكَنِ وَالإِقَامَةِ والحب، فلا عَيْشَ لِإِنْسَانٍ دُوْنَ وَطَنِ يَحْفَظُ لَهُ كَرَامَتَهُ وَهَيْبَتَه،ُ وَيَقِيهِ مِنَ الهَوَانِ والضَّيَاع.ِ

=== BLOCK 14: Final Exam Q ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: حَوْلِ الْمَقْطَعَ الأَوَّلَ مِنَ النَّصَ إلى رسالةٍ تُوَجَهها إلى مَوَاكِبِ الصَّائِعِينَ فِي مَتَاهَاتِ الغُرْبَةِ تُقْنِعُهُمْ فِيهَا بِالعَوْدَةِ إِلَى جِنَانِ الوَطَن.

--- END STREAM ---
