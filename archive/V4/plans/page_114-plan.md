# **SESSION 114**

[TASK DEFINITION]
Objective: Implement page 114.
File: `pages/page_114.html` (Note: Use the exact page number.)
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
[LESSON_NUMBER]: 114
[CHAPTER_TITLE]: page 114
[CATEGORY_HEADER]: 114
[SECTION_HEADER]: 114
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Poem Verse 27 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b10001
[POEM_TITLE]: - أ.
[UNIQUE_ID_BIO]: b10002
[POET_NAME]:
[RIGHT_HEMISTICH]: ٢٧- أي أنشودة خزي غص في
[LEFT_HEMISTICH]: بنها بين الأسى والكرب

=== BLOCK 3: Vocabulary Verse 27 ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: الكلمة
[HEADER_2]: المعنى
[HEADER_3]:
[CELL_1]: الكرب
[CELL_2]: مفردها الكُرْبَة،ُ )الكَرْبُ(: الحزن والغَم.
[CELL_3]:
[CELL_1]: خزي
[CELL_2]: خَزِي الرَّجُلُ ما أبقى مِنْ نَفْسِه،ِ استحيا، وخَجِلَ مِنها.
[CELL_3]:

=== BLOCK 4: Explanation Verse 27 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b10004
Title: الشرح
Content: إلا رواها وكشفها الصَّهَابِنَةً بِحَقِّ الفلسطينيين وجَلَبَتْ لَهُم احزن والهموم، التاريخ جريمة مُخْزِيَةً مُخْجِلَةً مِنَ الجَرَائِمِ التِي اقْتَرَفَهَا للعالم.

=== BLOCK 5: Warning Verse 27 ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[UNIQUE_ID]: b10005
[TITLE]: البلاغة
[CONTENT]: )أنشودة خزي(: تشبية بيع إضافي

=== BLOCK 6: Irab Verse 27 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b10006
[WORD_1]: أي :
[DETAILS_1]: اسم استفهام، مُبْتَدَاً مَرْفُوع
[UNIQUE_ID_2]: b10007
[WORD_2]: أنشودة، خزي، الأسى:
[DETAILS_2]: مُضَافَ إِلَيْهِ تَجْرُور.ٌ

=== BLOCK 7: Poem Verse 28 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b10008
[POEM_TITLE]:
[UNIQUE_ID_BIO]: b10009
[POET_NAME]:
[RIGHT_HEMISTICH]: ٢٨- ما لأبناء السبايا ركبوا
[LEFT_HEMISTICH]: للأماني البيض أشهى مركــــــــب

=== BLOCK 8: Analysis Verse 28 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b10010
Title: الشرح والمفردات
Content: المفردات: السبايا المفرد: الشبيَّة والسي: المأسور. ويريد هنا بأبناء السبايا: اليهود مِن أبناء سبايا الأمم البيض: صِفَةٌ مُشَبَّهَةٌ باسم الفاعل أشهى: اسم تفضيل. الشرح: ما بال اليهود قد بالعُوا في أحلامهم، وتمادوا في أُمْنِياتِهِم وَطَمَحُوا لِيلُوغِ مُسْتَقْبَلٍ عَظِيمٍ فَوْقَ تَرِى بلادنا العربية

=== BLOCK 9: Irab Verse 28 - Row 1 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b10011
[WORD_1]: ما
[DETAILS_1]: اسم استفهام فِي مَحَلِ رَفْع مُبْتَدَا.
[UNIQUE_ID_2]: b10012
[WORD_2]: الشايا، مركب :
[DETAILS_2]: مضاف إليهِ يَجْرُورٌ

=== BLOCK 10: Irab Verse 28 - Row 2 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b10013
[WORD_1]: )رَكَبُوا( :
[DETAILS_1]: في مَحَلَّ نَصْب حال
[UNIQUE_ID_2]: b10014
[WORD_2]: الْبِيض:ِ
[DETAILS_2]: صِفَةً مَجْرُورَةٌ

=== BLOCK 11: Irab Verse 28 - Row 3 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b10015
[WORD_1]: أَشهى :
[DETAILS_1]: مَفْعُولُ بِهِ مَنْصُوب.ٌ
[UNIQUE_ID_2]: b10015b
[WORD_2]:
[DETAILS_2]:

=== BLOCK 12: Poem Verse 29 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b10016
[POEM_TITLE]:
[UNIQUE_ID_BIO]: b10017
[POET_NAME]:
[RIGHT_HEMISTICH]: ٢٩- ومتى هروا علينا رايةً
[LEFT_HEMISTICH]: ما انطوت بين رخيص السَّلَبِ؟

=== BLOCK 13: Analysis Verse 29 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b10018
Title: الشرح والمفردات
Content: المفردات: رخيص: صِفَةٌ مُشَبَّهَةٌ باسم الفاعل. الشرح: مَا سَبَقَ لِلْيَهُودِ أن غارُوا عَلينا وخاضوا ضِدَّنَا حَرْبًا، عَلَيْهِم وَطَوَيْنَا أَعْلَامَهِم إِلَّا هَزَمْنَاهُم وَانْتَصَرْنَا مَعَ مَا غَنِمْنَاهُ مِنْهُم.

=== BLOCK 14: Irab Verse 29 - Row 1 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b10019
[WORD_1]: متى :
[DETAILS_1]: اسم استفهام مَفْعُول فيه ظرف زمان
[UNIQUE_ID_2]: b10020
[WORD_2]: راية :
[DETAILS_2]: مَفْعُولٌ بِهِ مَنْصُوبُ

=== BLOCK 15: Irab Verse 29 - Row 2 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b10021
[WORD_1]: )ما انطوت(:
[DETAILS_1]: في محل : نصب صفة
[UNIQUE_ID_2]: b10022
[WORD_2]: رخيص السلب:
[DETAILS_2]: مُضَافُ إِلَيْهِ يَجْرُور.ٌ

=== BLOCK 16: Poem Verse 30 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b10023
[POEM_TITLE]:
[UNIQUE_ID_BIO]: b10024
[POET_NAME]:
[RIGHT_HEMISTICH]: ٣٠- ومن الطاعي الذي مد لهم
[LEFT_HEMISTICH]: من سراب الحق أوهی سبب؟

=== BLOCK 17: Analysis Verse 30 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b10025
Title: الشرح والمفردات
Content: المفردات: الطَّاعِي: الظَّالِم، والطَّاغِيَةُ: العَظِيم الظُّلْم، الكثير الطغيان. أوهى أضعف. والطَّاعِي: اسم فاعل وأوهى اسم تفضيل. الشرح: من هذا الظَّام الذي أَبَاحَ لِلْيَهُودِ أَنْ يَحْتَلُوا أَرْضَنا دونَ وَجْهِ حَق، وَسَوَّعَ لَهُم هذا الاحتلال، وأهمهم بِشَرْعِيَّتِهِ. البلاغة: )سراب الحق(: تشبية بليغ إضافي.

=== BLOCK 18: Irab Verse 30 - Row 1 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b10026
[WORD_1]: من
[DETAILS_1]: اسم استفهام فِي مَحَلَّ مُبْتَدَةٌ مَرْفُوعٌ
[UNIQUE_ID_2]: b10027
[WORD_2]: الطَّاعِي:
[DETAILS_2]: فِي مَحَلِّ رَفْعِ خَبَرَ

=== BLOCK 19: Irab Verse 30 - Row 2 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b10028
[WORD_1]: الذي:
[DETAILS_1]: اسمٌ مَوْسُولٌ فِي حَلِّ رَفْعِ صفة.
[UNIQUE_ID_2]: b10029
[WORD_2]: )مد( :
[DETAILS_2]: صِلَةُ المَوْصُولِ لَا مَحَلَّ لَا مِنَ الإعراب

=== BLOCK 20: Irab Verse 30 - Row 3 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b10030
[WORD_1]: الحق، سبب :
[DETAILS_1]: مُضَافُ إِلَيْهِ تَجْرُورٌ
[UNIQUE_ID_2]: b10031
[WORD_2]: أوهى :
[DETAILS_2]: مَفْعُولُ بِهِ مَنْصُوب.ٌ

=== BLOCK 21: Poem Verse 31 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b10032
[POEM_TITLE]:
[UNIQUE_ID_BIO]: b10033
[POET_NAME]:
[RIGHT_HEMISTICH]: ٣١- أو ما كنا له في خطبه
[LEFT_HEMISTICH]: مَعُقل الأمن وجسر الهرب؟

=== BLOCK 22: Analysis Verse 31 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b10034
Title: الشرح والمفردات
Content: المفردات: خطيه الخطب المكروه. معقل: اسم مكان. الشرح: ألم نَكُنْ لَهُ فِي شِدَّتِهِ وَكَرْبِهِ مَلَاذَا آمِنَا يَأْوِي إِلَيْهِ لِيَنْعَمَ بِالْأَمْن،ِ وَطَرِيقًا يَسْلُكَهُ لِيَنْجُو مِنَ الأَخْطَارِ المحدِقَةِ به.

=== BLOCK 23: Irab Verse 31 - Row 1 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b10035
[WORD_1]: أ:
[DETAILS_1]: الهَمْرَةُ : حَرْفُ استفهام و الواو حرف زائد. ما حَرْفُ نَفي.
[UNIQUE_ID_2]: b10036
[WORD_2]: مَعْقَل:َ
[DETAILS_2]: خَبَرَ كَانَ مَنْصُوب.ٌ

=== BLOCK 24: Irab Verse 31 - Row 2 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b10037
[WORD_1]: الأمن الهرب :
[DETAILS_1]: مُضَافُ إِلَيْهِ تَجْرُورٌ .
[UNIQUE_ID_2]: b10037b
[WORD_2]:
[DETAILS_2]:

=== BLOCK 25: Poem Verse 32 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b10038
[POEM_TITLE]:
[UNIQUE_ID_BIO]: b10039
[POET_NAME]:
[RIGHT_HEMISTICH]: ٣٢- ما لنا لمح في مشيته
[LEFT_HEMISTICH]: مجلب الذئب وجلد التَّغْلب؟

=== BLOCK 26: Analysis Verse 32 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b10040
Title: الشرح والمفردات
Content: المفردات: مجلب اسم آلة. الشرح: تبدو لنا فِي هَيْنَتِهِ حِينَمَا نُبْصِرُهُ مَاشِيَا مَلامِحُ الوَحْشِيَّة،ِ ومعالم المكر والحمل والخداع. البلاغة: )مجلب الذَّئب( : كنايَةً عَنِ الوَحْشِيَّة.ِ )جلد التَّعْلَبِ( : كِنَايَةً عَنِ المكر والخداع.

=== BLOCK 27: Irab Verse 32 - Row 1 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b10041
[WORD_1]: ما
[DETAILS_1]: اسم استفهام فِي حَلِّ رَفْعِ مُبْتَدَا.
[UNIQUE_ID_2]: b10042
[WORD_2]: المخ( :
[DETAILS_2]: في محل نصب حال

=== BLOCK 28: Irab Verse 32 - Row 2 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b10043
[WORD_1]: مِخْلَب :
[DETAILS_1]: مَفْعُولُ بِهِ مَنْصُوبُ
[UNIQUE_ID_2]: b10044
[WORD_2]: الذَّنب التَّعْلَبِ :
[DETAILS_2]: مُضَافُ إِلَيْهِ تَجْرُور.ٌ

=== BLOCK 29: Poem Verse 33 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b10045
[POEM_TITLE]:
[UNIQUE_ID_BIO]: b10046
[POET_NAME]:
[RIGHT_HEMISTICH]: ٣٣- يا لذل العهد إن أغضى أس
[LEFT_HEMISTICH]: فوق صَدْرِ الشَّرف المنتحب

=== BLOCK 30: Analysis Verse 33 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b10047
Title: الشرح والمفردات
Content: المفردات: أغضى: أغضى فلان: قارب بينَ أَجْفَانِهِ وأَعْضَى عَيْنَهُ وَطَرْفَهُ عَنْهُ حَوَّلَهُ عَنْهُ المنتحب اسم فاعل. الشرح: يا للعار ويا للذل الذي سَيُلَطَخُهُ إِنْ تناسى سَيُكَلِّلُ جَبِينَ الإنسان العربي، وتنصَّلَ مِنَ العَهْدَ الذي قَطَعَهُ لِفِلَسْطِينَ وَغَضَ الطَّرْفَ عَنْه،ُ الدفاع وعَنْ شَرَفها. البلاغة: العهد أغضي(، )صَدْرِ الشَّرْفِ(، )الشرف المنتحب( استعارةً مَكْنِية.

=== BLOCK 31: Irab Verse 33 - Row 1 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b10048
[WORD_1]: العَهْد،ِ صَدْرِ الشَّرْف:ِ
[DETAILS_1]: مضافُ إِلَيْهِ مَجْرُورٌ
[UNIQUE_ID_2]: b10049
[WORD_2]: المنتحب :
[DETAILS_2]: صفة مجرُورَة.ٌ

=== BLOCK 32: Irab Verse 33 - Row 2 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b10050
[WORD_1]: فوق :
[DETAILS_1]: مَفْعُولٌ فِيهِ ظَرْفُ مكان منصوب
[UNIQUE_ID_2]: b10051
[WORD_2]: اسي :
[DETAILS_2]: مَفْعُولٌ لأَجْلِهِ مَنْصُوبٌ

=== BLOCK 33: Poem Verse 34 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b10052
[POEM_TITLE]:
[UNIQUE_ID_BIO]: b10053
[POET_NAME]:
[RIGHT_HEMISTICH]: ٣٤- يا روابي القدس يا مجلى السنا
[LEFT_HEMISTICH]: يا رؤى عيسى على جفن النبي

=== BLOCK 34: Analysis Verse 34 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b10054
Title: الشرح والمفردات
Content: المفردات: السنا: الضوء السَّاطِعُ. الشرح: يا مرتفعات فلسطين الحبيبة، يا مَنْ كُنْتِ مَهْبَطَ الرسالات السماوية يَا مَنْ أَشْرَقَتْ على تراك الأنوارُ الإِهْيَّة،ٌ.

=== BLOCK 35: Irab Verse 34 - Row 1 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b10055
[WORD_1]: روايي، مجلى، رؤى
[DETAILS_1]: منادى منصوب
[UNIQUE_ID_2]: b10056
[WORD_2]: القدس، السنا، عيسى الني:
[DETAILS_2]: مضاف إِلَيْهِ مَجْرُور.ٌ

=== BLOCK 36: Poem Verse 35 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b10057
[POEM_TITLE]:
[UNIQUE_ID_BIO]: b10058
[POET_NAME]:
[RIGHT_HEMISTICH]: ٣٥- دون عليائك في الرحب المدى
[LEFT_HEMISTICH]: صهلة الخيل ووهج القضب

=== BLOCK 37: Analysis Verse 35 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b10059
Title: الشرح والمفردات
Content: المفردات: القضب: السُّيُوفُ القَطَاعَةُ. الشرح: انتظري تَجْدَتَنَا سَتَجْعَلُ خُيُولَنَا وَأَسْلِحَتَنَا دِرْعًا حاميًا لك،ِ ومُخَصًا لَكِ مِنْ بَرَائِنِ العدوان.

=== BLOCK 38: Irab Verse 35 - Row 1 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b10060
[WORD_1]: دونَ
[DETAILS_1]: مَفْعُولُ فِيهِ ظَرْفُ مكانٍ مَنْصُوب
[UNIQUE_ID_2]: b10061
[WORD_2]: عليانك الخيل، القضب:
[DETAILS_2]: مُضافُ إِلَيْهِ تَجْرُور

=== BLOCK 39: Irab Verse 35 - Row 2 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b10062
[WORD_1]: المدى:
[DETAILS_1]: صِفَةً مَجْرُورَة.ٌ
[UNIQUE_ID_2]: b10063
[WORD_2]: صهلة :
[DETAILS_2]: مُبْتَدَاً مرفوع.

=== BLOCK 40: Irab Verse 35 - Row 3 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b10064
[WORD_1]: وهج:
[DETAILS_1]: اسمٌ مَعْطُوفٌ مَرْفُوع.ُ
[UNIQUE_ID_2]: b10064b
[WORD_2]:
[DETAILS_2]:

--- END STREAM ---