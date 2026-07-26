# **SESSION 174**

[TASK DEFINITION]
Objective: Implement page 174.
File: `pages/page_174.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`.
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md` to identify the correct template to use for the continuation.
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
6. Templates: You are forbidden from inventing new HTML tags or classes or template elements. Replace any `<section>` tags from the templates with `<div>` tags (keep `<header>` for page headers as is).
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). The ID MUST be applied to the `<div>` tag that replaced the `<section>` tag. Use "Jules-workspace/id_manager.py" to generate or verify them.
8. **Self-Correction:** Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...) .
11. You must preserve the exact Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense. Do NOT leave empty space.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
15. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 174
[CHAPTER_TITLE]: page 174
[CATEGORY_HEADER]: 174
[SECTION_HEADER]: 174
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Poem Continuation ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[BLOCK_TITLE]: القصيدة
[CONTENT]:
- أ. عَلَلتها بلقاء ... رهْنِ أَزْمان - ولَوْعَةً فِي حَشَا الأحباب ما بَرَدَتْ

=== BLOCK 3: Vocabulary and Meaning Verse 8 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح
Content:

=== BLOCK 4: List for Verse 8 ===
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT_1]: المفردات: لوعة: اللوعَةُ مَصْدَرُ الفِعْلِ (لاعَ). واللوعة: حرقة في القلب والم يَجِدُهُ الإنسانُ مِنْ حُبّ أو هم. عَلَلْمُها: عَلَّلَ العَطْشَانَ سَقَاهُ سَفْيًا بَعْدَ سَفي. وعلل الطبيب المريض: عاجهُ مِنْ عِلْتِه.ِ رهن: الرَّمَان،ِ فَالْأُمُورُ مَرْهُونَةً بِاوْقَاتِهَا. يُرِيدُ أَنَّ هذا القَاءِ مَرْهُونَ بَشِيئَةِ
[LIST_ITEM_CONTENT_2]: الشرح: ولا أستطيع نسيان حرقة الألم التي استفَرَّتْ فِي قَلْبِ الأحبَّة،ِ تِلْكَ الحرقة التي أَطْفَأَنها وعالجتها بوعدي الأحِبَّةَ بِلِقَاءِ مَرْهُونِ بِمَشِينَةِ
[LIST_ITEM_CONTENT_3]: الفكرة: معاناة الأحيَّةِ مِنَ الفراق، وتَعْلِيلُهُم بالوصال. الشعور: ألم وحزن. الأداة: التراكيب. المثال: ولَوْعَةً في حَشَا الْأَحِبَابِ مَا بَرَدَت.ْ

=== BLOCK 5: Irab (Lawa'a) ===
(Component: TEMPLATE_C_IRAB.html)
[WORD_1]: ولاعة
[DETAILS_1]: الواو : حَرْفُ عَطْف. لوعَةً : اسمٌ مَعْطُوفٌ مَنْصُوبُ
[WORD_2]: الأَحباب
[DETAILS_2]: مضاقٌ إِلَيْهِ تَجْرُورٌ.
[WORD_3]: أَرْمان
[DETAILS_3]: مضاقٌ إِلَيْهِ تَجْرُورٌ.
[WORD_4]: (مَا يَرَدَتْ)
[DETAILS_4]: في محل نصب صفة.
[WORD_5]: رهن
[DETAILS_5]: صِفَةٌ مَجْرُورَة.ٌ
[WORD_6]: (عَلَلْتها)
[DETAILS_6]: في محل نصب صفة.

=== BLOCK 6: Poem Verse 9 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البيت التاسع
[RIGHT_HEMISTICH]: مَرَّتْ ثلاثون لم أنس العُهُودَ
[LEFT_HEMISTICH]: وَهَلْ تنسى مواثيق أرحام وأيمان؟!

=== BLOCK 7: Analysis Verse 9 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تحليل البيت التاسع
Content:

=== BLOCK 8: List for Verse 9 ===
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT_1]: المفردات : أَرحام : أقارب. أيمان : جمع يمين.
[LIST_ITEM_CONTENT_2]: الشرح : أَمْضَيْتُ خلال هذه المُدَّةِ الطَّوِيلَةِ فِي غُرْبَتِي ثلاثين عامًا، لم أنس العُهُودَ والمواثيق التي قطعتها الأقربائي والزَمْتُ نفسي بالإخلاص بها، ولم أنس تلك الأيمان التي حَلَفْتُها لهم.
[LIST_ITEM_CONTENT_3]: الشعور: اعتزاز، وافتخار. الأداة: التراكيب. المثال : مَرَّتْ ثلاثون.
[LIST_ITEM_CONTENT_4]: البلاغة: (لم أَنْس،َ تُنْسَى): طباق سلب.

=== BLOCK 9: Irab Verse 9 ===
(Component: TEMPLATE_C_IRAB.html)
[WORD_1]: ثلاثونَ
[DETAILS_1]: فَاعِلْ مَرْفُوعٌ وعلامَةُ رَفْعِهِ الواو؛ لأَنَّهُ مُلْحَقِّ بِجَمْعِ الْمُذَّكْرِ السَّالم.
[WORD_2]: مواثيق
[DETAILS_2]: نَائِبُ فَاعِلِ مَرْفُوع.ُ
[WORD_3]: تُنْسَى
[DETAILS_3]: فِعْلَ مُضارع مَبْنِي لِلمَجْهُولِ مَرْفُوع.

=== BLOCK 10: Poem Verse 10 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البيت العاشر
[RIGHT_HEMISTICH]: الأهل أهلي وأطلالُ الْحِمَى وَطَنِي
[LEFT_HEMISTICH]: وساكنو الربع أترابي وأفراني

=== BLOCK 11: Analysis Verse 10 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تحليل البيت العاشر
Content:

=== BLOCK 12: List for Verse 10 ===
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT_1]: المفردات: الحمى: المؤضِعُ فِيهِ كلا يُرْعَى والشَّيْءُ المَحْمِي يُحْمَى مِنَ النَّاسِ أَنْ يُرْعَى. أَترابي: المفرد، : التَّرْبُ الممائِلُ في السن. تاربه : صَاحَبَهُ. الأَقْرَان:ُ القِرْن،ُ للإنسان: مَثَلُهُ فِي الشَّجَاعَةِ والدَّة والعلم والقتال وغير ذلك. ساكنو: اسم فاعِل،ِ فِعْلُهُ سَكَنَ.
[LIST_ITEM_CONTENT_2]: الشَّرح: رُعْمَ طُولِ المَدَّةِ التِي أَمْضَيْتُها في غُرْبَتِي بَقِيتُ مُرْتَبط بأهلي، مشدودًا إِلَى وَطَي، مُتَمَسَكًا بِأَصْدِقَائِي القَاطِنِينَ فِي وَطَنِي.
[LIST_ITEM_CONTENT_3]: الفكرة: تأكيد الارتباط بالأهل والوَطَنِ. الشَّعُور: اعتزاز، وافتخار. الأداة: التراكيب. المثال: الأهل أهلي وأَطَالُ الْحِمَى وَطَنِي.

=== BLOCK 13: Irab Verse 10 ===
(Component: TEMPLATE_C_IRAB.html)
[WORD_1]: الأهل، أطلال، ساكِنُو
[DETAILS_1]: مُبْتَدَاً مَرْفُوع.
[WORD_2]: أهلي، وطني، أترابي
[DETAILS_2]: خَبَرَ مَرْفُوعُ.
[WORD_3]: الحمى، الرَّيْعِ
[DETAILS_3]: مُصَافُ إِلَيْهِ يَجْرُور.ُ

=== BLOCK 14: Poem Verse 11 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البيت الحادي عشر
[RIGHT_HEMISTICH]: يا عظم شوقي على بعد وهجران
[LEFT_HEMISTICH]: قَدْ كُنْتُ أَشتاقُهُمْ وَالْعَيْنُ تَنْظُرُهُم

=== BLOCK 15: Analysis Verse 11 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تحليل البيت الحادي عشر
Content:

=== BLOCK 16: List for Verse 11 ===
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT_1]: الشرح : كُنتُ أشتاق إلى أهلي ووطني وأصدقائي قَبْلَ أَنْ أَفَارِقَهُم، وبَعْدَ أَنْ هَاجَرْتُ وَابْتَعَدْتُ عَنِ الوَطَنِ تعاظَمَتْ أَشواقي وتفاقَمَ حَنِينِي إِلَيْهِم.
[LIST_ITEM_CONTENT_2]: الفكرة : تأكيد الشَّوْقِ والحنين إلى الأهل والوَطَنِ. الشَّعور : الشَّوْق،ُ والحنين. الأداة: التراكيب. المثال: قَدْ كُنْتُ أَشتاقُهُمْ وَالعَيْنُ تَنْظُرُهُم. أو يا عظم شوقي على بعد وهجران.

=== BLOCK 17: Irab Verse 11 ===
(Component: TEMPLATE_C_IRAB.html)
[WORD_1]: عظم
[DETAILS_1]: منادى مُضاف منصوب.
[WORD_2]: (أَشتاقهُمْ)
[DETAILS_2]: في محل نصب خَبَرَ.
[WORD_3]: العَيْنُ
[DETAILS_3]: مُبْتَدَاً مَرْفُوعٌ.
[WORD_4]: تَنْظُرُهُم
[DETAILS_4]: فِي مَحَلِّ رَفع خَبَر.َ
[WORD_5]: (العَيْنُ تَنْظُرُهُم)
[DETAILS_5]: في محل نصب حال.

=== BLOCK 18: Poem Verse 12 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البيت الثاني عشر
[RIGHT_HEMISTICH]: ١٠- إِنْ أَنْكَرُونَا فَمَا وَاللَّهِ تُنْكِرِهُم
[LEFT_HEMISTICH]: وإِنْ جَفَوا لا يُقابلهمْ بِنِسيان

=== BLOCK 19: Analysis Verse 12 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تحليل البيت الثاني عشر
Content:

=== BLOCK 20: List for Verse 12 ===
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT_1]: المفردات: جفوا : هَجَرُوا وابتَعَدُوا.
[LIST_ITEM_CONTENT_2]: الشرح: إِنْ تَنَكَّرُوا لَنَا فَنَحْنُ نُفْسِمُ إِنَّنا لن نَتَنَكُرَ لَهُم، وإِنْ هَجَرُونَا تعامِلَهُم بالمثل فَلَنْ ننساهم.
[LIST_ITEM_CONTENT_3]: البلاغة: (أَنكرونا، ما تُنْكِرُهُم) طباق سلب.

=== BLOCK 21: Irab Verse 12 ===
(Component: TEMPLATE_C_IRAB.html)
[WORD_1]: فَمَا
[DETAILS_1]: الفاء: رابطة لجواب الشَّرْط. ما : حَرْفُ نَفي.
[WORD_2]: والله
[DETAILS_2]: الواو : حَرْفُ جَرٍ وَقَسَمِ. اللهِ : لفظ الجلالة، اسم عَجْرُوز.

=== BLOCK 22: Poem Verse 13 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البيت الثالث عشر
[RIGHT_HEMISTICH]: -۱۱ تحِبُّهُمْ كَيْفَمَا كَانُوا وَإِنْ رَكِبُوا
[LEFT_HEMISTICH]: إلى آن مَرَاكِبَ الهَجْرِ مِن أن

=== BLOCK 23: Analysis Verse 13 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تحليل البيت الثالث عشر
Content:

=== BLOCK 24: List for Verse 13 ===
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT_1]: المفردات: مراكب: اسم مكان، فِعْلُه: ركب.
[LIST_ITEM_CONTENT_2]: الشرح: حبنا لهم ثابت لا يزولُ مَهما تَبَدَّلَتْ أخواهم، حتَّى وَإِنْ هَجَرُونَا مَرَّةً بَعْدَ مَرَّة.ٍ
[LIST_ITEM_CONTENT_3]: الفكرة: تأكيد حب الأهل والوَطَنِ. الشَّعور: حب. الأداة: التراكيب. المثال: تُحِبُّهُمْ كَيْفَمَا كَانُوا.

=== BLOCK 25: Irab Verse 13 ===
(Component: TEMPLATE_C_IRAB.html)
[WORD_1]: كيفما
[DETAILS_1]: اسمُ شَرْطِ جازم في محل نصب خَبَرَ كَانَ.
[WORD_2]: مَرَاكِبَ
[DETAILS_2]: مَفْعُولُ بِهِ مَنصُوب.ُ

=== BLOCK 26: Poem Verse 14 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البيت الرابع عشر
[RIGHT_HEMISTICH]: -۱۲ هيهات تطلب بالزلفي محبتهم
[LEFT_HEMISTICH]: تأبي المَحَبَّةُ أَنْ تُشْرَى بِأَثْمان

=== BLOCK 27: Analysis Verse 14 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تحليل البيت الرابع عشر
Content:

=== BLOCK 28: List for Verse 14 ===
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT_1]: المفردات: الرُّلْفي: زَلَفَ إِلَيْهِ زَلْفًا، وليفًا : دنا وتَقَرَّبَ.
[LIST_ITEM_CONTENT_2]: الشرح: لا نَدَّعِي حبهم ادعاء، ولا نَتَصَنَّعْ مَحَبَّتَهُم تَقَرُّبًا وَتَلُّ ا؛ فَالْمَحَبَّةُ الصَّادِقَةُ لا تباع أو تُشْتَرَى بأي تَنِ مِنَ الأَثْمان.
[LIST_ITEM_CONTENT_3]: الفكرة: تأكيد صدق حبّ الأهل والوَطَنِ.
[LIST_ITEM_CONTENT_4]: البلاغة: (تَأْبَ المَحَيَّةُ): استِعَارَةٌ مَكْنِيَّة.ٌ

=== BLOCK 29: Irab Verse 14 ===
(Component: TEMPLATE_C_IRAB.html)
[WORD_1]: هيهات
[DETAILS_1]: اسم فعل ماض بمعنى بعد مبني على الفتح.
[WORD_2]: محبتهم
[DETAILS_2]: مَفْعُولُ بِهِ مَنصُوبٌ.
[WORD_3]: تُشْرَى
[DETAILS_3]: فِعْلَ مُصَارِعٌ مَبْنِيَ المَجْهُولَ مَنسُوبٌ.
[WORD_4]: (تُشْرَى)
[DETAILS_4]: صِلَةً الموصول لا محل لها مِنَ الإعراب.
[WORD_5]: (تَأْبي المحيَّةُ)
[DETAILS_5]: استئنافية لا محل لها من الإعراب.

=== BLOCK 30: Warning Table ===
(Component: TEMPLATE_C_TABLE.html)
Title: جدول الخلاصة
[TABLE_HEADER_1]: البيت
[TABLE_HEADER_2]: الفكرة / الشعور
[ROW_1_COL_1]: ٩
[ROW_1_COL_2]: اعتزاز، وافتخار
[ROW_2_COL_1]: ١٠
[ROW_2_COL_2]: تأكيد الارتباط بالأهل والوَطَنِ / اعتزاز، وافتخار
[ROW_3_COL_1]: ١١
[ROW_3_COL_2]: تأكيد الشَّوْقِ والحنين إلى الأهل والوَطَنِ / الشَّوْق،ُ والحنين
[ROW_4_COL_1]: ١٣
[ROW_4_COL_2]: تأكيد حب الأهل والوَطَنِ / حب
[ROW_5_COL_1]: ١٤
[ROW_5_COL_2]: تأكيد صدق حبّ الأهل والوَطَنِ

--- END STREAM ---
