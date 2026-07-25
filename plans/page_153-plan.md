# **SESSION 153**

[TASK DEFINITION]
Objective: Implement page 153.
File: `pages/page_153.html` (Note: Use the exact page number.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools. If it overflows, it is a catastrophic failure. Do NOT try to solve overflow by deleting text (Strict Typographer Rule). Solve it by choosing denser templates or omitting optional white-space.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`. Ensure exact visual continuity (same title, same classes).
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md` to identify the correct template to use for the continuation. You are forbidden from guessing. Scan the raw text for the preceding keyword to determine the active template and apply the correct `_PART_2.html` wrapping.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`, `.highlight-green` for secondary.
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
[LESSON_NUMBER]: 153
[CHAPTER_TITLE]: page 153
[CATEGORY_HEADER]: 153
[SECTION_HEADER]: 153
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: الأسئلة العامة ===
(Component: TEMPLATE_C_LIST.html)
Item: - ماذا يُظْهِرُ النَّقْدُ بِحَسَبِ رأي الكاتب؟ (ما وظيفة النَّقْدِ كما بينها الكاتب؟) ج - النَّقْدُ يُظْهِرُ الإِيجابيَّاتِ كما يُظْهِرُ السلبيَّاتِ فِي الوقتِ نَفْسِه.ِ
Item: - متى يكون النَّاقِدُ مَوْضُوعِيَّا بِحَسَبِ رأي الكاتب؟ ج- يرى الكاتبُ أَنَّ النَّاقِدَ لا يكونُ مَوْضُوعِيًا إِلَّا إِذا كَانَ عادلا في تبيانِ الوَجْهَين معا، الإيجابي والسلبي.
Item: - ماذا لاحظ الكاتب في دراسة ظَوَاهِرِ مُجْتَمَعِنا؟ وما رأيه فيما لاحظه؟ ج - لاحظ أَنَّ أُنَاسًا يَنْظُرُونَ إِلَى ظَوَاهِرِ مُجْتَمَعِنَا بِعَيْنِ الرِّضا، فلا يجدون ثغرة ما ولا خَلَلًا ولا نقصا، ورأى أَنَّ هَذِهِ الشَّرِيحَةَ غَيْرُ مَوْضُوعِيَّةِ فِي نَظْرَتِهَا. وفي المقابل لاحظ أَنَّ أُنَاسًا آخرينَ يَنْظُرُونَ إِلَى ظَوَاهِرِ مُجْتَمَعِنَا بِعَيْنِ السُّخْط،ِ فلا يَجِدُونَ فِيهَا أَيَّ بارِقَةٍ إِيجَابِيَّة،ِ وَإِنَّما يَرَونَ أَنَّ الظَّلَامَ يَكْتَنِفُهَا، وأَنَّ الأَمَلَ فِي الخلاص مِنْ سلبياتِهَا مَعْدُومٌ فَقَدَّرَ أَنَّ هذه الشَّرِيحَةَ مِنَ النَّاسِ غَيْرُ مَوْضُوعِيَّةٍ أيضًا.
Item: ه- ما هُوَ التَّفْكِيرُ النَّقْدِيُّ السَّلِيمُ بِحَسَبِ رأي الكاتب؟ جه - رأى الكاتِبُ أَنَّ التَّفْكِيرَ النَّقْدِيَّ السَّلِيمَ هو الذي لا يَنْظُرُ إِلَى الظَّوَاهِرِ بِعَيْنِ الرضا وَحْدَهَا، ولا يَنْظُرُ إِليها بِعَيْنِ السُّخْطِ وَحْدَهَا، وَإِنَّما يَنْظُرُ إليها بِعَيْنِ الْمَوْضُوعِيَّة،ِ فَيُعْطِي لِقَيْصَرَ مَا لِقَيْصَر،َ وَلِلَّهِ مَا لله،ِ وَذَلِكَ فِي مَنْأَى عَنْ أَيِّ تَحَيُّزٍ أَو تَعَصُّبٍ أَو تَشَنُّجٍ.

=== BLOCK 3: المقطع الثاني ===
(Component: TEMPLATE_C_LIST.html)
Title: الأسئلة المُقْتَرَحَةُ فِي الْمَقْطَعِ الثَّانِي:
Item: - بماذا يرتبط التفكيرُ النَّقْدِي ارتباطا عُضويا؟ جا - يرتبط التفكيرُ النَّقْدِي ارتباطا عُضُويا بِمَاهِيَّةِ التَّفكير العلمي. فهو لا يعني مُجَرَّدَ الرَّفْضِ أو التَّفْنِيدِ أو المعارَضَةِ لِمَا هو قائم.
Item: - ما السياقات التي يَدْعُو التَّفْكِيرُ النَّقْدِي إلى الاهتمام بها عِنْدَ دراسة أي ظاهِرَةِ اجتماعِيَّةِ؟ ج ٢- السياقات الاقتصادية والاجتماعية والأبعاد التاريخية للظاهرة.
Item: - التَّفْكِيرُ النَّقْدِيُّ مَنْهَجٌ لَا يَكْتَفِي بِالأَشكالِ الظَّاهِرَةِ في واقعها المُحَدَّدِ بِالزَّمان والمكانِ الرَّاهِنَينِ وَضِّحْ ذَلِك.َ ج- التَّفْكِيرُ النَّقْدِي لا يكتفي بالأشكال الظَّاهِرَةِ في واقعهَا الرَّاهِن،ِ وَإِنَّمَا يَبْحَثُ عَنِ الجُذُورِ الْمُجْتَمَعِيةِ التِي أَدَّتْ إِلَى تَشَكُلِ هَذِهِ الظَّاهرة وعلى الصورة التي بدت عليها في أثناء فَتَرَةِ الدراسة.
Item: - ما الذي يستهْدِفُهُ التَّفْكِيرُ النَّقْدِيُّ لِمُعطيات الواقع؟ ج - ٤ يَسْتَهْدِفُ تأكيد مهمة التغيير ، ودَوْرَ التَّجديدِ فِي البَحْثِ وَالمَعْرِفَةِ بغية اكتشاف الأَبعاد الحقيقية لهذا الواقع، والسعي إلى تجاوز عقباته وصولا إلى الأَجْمَلِ وَالأَكْمَل.ِ

=== BLOCK 4: المقطع الثالث (المصفوفة) ===
(Component: TEMPLATE_C_TABLE.html)
Title: الأسئلة المقتَرَحَةُ فِي المَقْطَعِ الثَّالِثِ: - يَخْتَلِفُ الفلاسِفَةُ مَعَ عُلَمَاءِ النَّفْسِ فِي وجهات النظر حول التَّفْكِيرِ النَّقْدِي اختلافا جَوْهِرِيًّا. وَضِّحْ ذَلِك.َ
Row 1: الفلاسِفَةُ | عُلَمَاءُ النَّفْسِ
Row 2: يُؤَكِّدُونَ الحَاجَةَ إِلَى التَّفْكِيرِ النَّقْدِي. | يُفَضِّلُونَ مُصْطَلَح "مهارات التفكير".
Row 3: يَرُونَ ضَرُورَةَ التَّأْكيد على الحجج والبراهين المَوْضُوعِيَّةِ وَالمَنْطِقِيَّةِ على أنها مِحْوَرُ التَّفْكِيرِ الانتقادِي وَجَوْهَرُه.ُ | يُرَكِّزُونَ فِي عملياتِ التَّفْكِيرِ نَفْسِهَا.
Row 4: يَهْتَمُونَ بِمُمَارَسَةِ المنطق والحجج والأدلة على أنها أدوات في شرح حقائِقَ مُعَيَّنَة،ٍ وَيَرَوْنَ أَنَّ البَرَامِجَ الْمُدْرِسِيَّةَ يَنْبِغِي لها أن تركز في تصوير التفكير المنطقي أداةً مِنْ أَجَلِ صُنع قراراتٍ أَخْلَاقِيَّةٍ وَمَعْنَوِيَّةِ. | يُظْهِرُونَ اهْتِمَامًا وَاضِحًا بَعَمَلِيَّاتِ التفكير، وَكَيْفِيَّة تطويرها عِنْدَ الْمُتَعَلِّمِين غير أنهم يؤكدون، في الوقتِ نَفْسِه،ِ عَمَلِيَّةَ حَلِ الْمُشْكِلاتِ أَكْثَرَ مِنْ تأكيدهم عَمَلِيَّةَ الْمَنْطِق.ِ

=== BLOCK 5: رأي الكاتب ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: - بين رأي الكاتب في وجهات نظر الفلاسِفَةِ وَعُلَمَاءِ النَّفْسِ حَوْلَ التَّفْكِيرِ النَّقْدِي؟
Content: ج - ٢ رَأَى أَنَّ الفلاسِفَةَ مُحِقُونَ فِي تَأْكِيدِهِم التفكير الانتقادِي والتفكير التأملي والاستنتاجي. كما رأى أن عُلَمَاءَ النَّفْسِ فِي تأكيدهم المشكلات مُحِقُونَ أَيضًا، ذَلِكَ لِأَنَّ طَبيعة الحياة تستلزم أن يكونَ الْمَرْءُ مُزَوَّدًا بمهاراتِ التَّفْكِيرِ الانتقادِي.

=== BLOCK 6: المقطع الرابع ===
(Component: TEMPLATE_C_LIST.html)
Title: الأسئلة المُقْتَرَحَةُ فِي الْمُقْطَعِ الرابع:
Item: - ما الأمور التي أَوْصَانَا الكاتب أَنْ نَهْتَمَّ بها في تَرْبِيَتِنا لأَبنائنا؟ ج ۱- رأى الكاتب أَنَّا مُطَالَبُونَ فِي تَرْبِيَتِنا لأَبْنَائِنَا بَدْءًا مِنَ الْأَسْرَةِ وانتهاء بِالمُجْتَمَعِ مُرُورًا بالمدارس والمعاهد والجامعات، بالاهتمام بِالتَّفْكِيرِ النَّقْدِي مِنْ حيث طرح الأسئلة والاستفسار بـ "لماذا"، والتَّمَتُّعِ بِعُقُولٍ مُنْفَتِحَةٍ وَغَيْرِ مُتَحَيّزة، وتحديد الأسباب والاستنتاجاتِ بِرُوحِ مِنَ الْمَوْضُوعِيَّة.ِ
Item: - ماذا أَوْجَبَ الكاتب في عَمَلِيَّةِ بناء التفكير الانتقادِي؟ ج - ٢ رَأَى الكَاتِبُ أَنَّهُ فِي عَمَلِيَّةِ بِنَاءِ التَّفْكِيرِ الانتِقَادِي لَا بُدَّ مِنْ ترسيخ تقاليد مُعَيَّنَةِ تَتَمَثَلُ في احترام الرأي، وتقدير الرأي الآخَرِ والمَوْضُوعِيَّة في إصدار الأحكام، ذَلِكَ لِأَنَّ الشَّخْصِيَّة المتكاملة هي التي تَتَقَبَّلُ النَّقْدَ مِنَ الآخرين، وتسعى إلى تعديل مسارها وتطوير أدائها نحو الأَفْضَلِ فِي ضَوْءِ ما تتلقاهُ مِنْ مُلاحظات.

--- END STREAM ---
