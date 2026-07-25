# **SESSION 152**

[TASK DEFINITION]
Objective: Implement page 152.
File: `pages/page_152.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
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
[LESSON_NUMBER]: 152
[CHAPTER_TITLE]: page 152
[CATEGORY_HEADER]: 152
[SECTION_HEADER]: 152
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: النص ===
(Component: TEMPLATE_C_BLOCK.html)
Content: (۱) <span class="text-accent font-bold">الدكتور محمود السيد ۱۹۳۹) م(</span> طالما يتبادر إلى الدِّهْنِ عندما نُطْلِقُ مَفْهُومَ النَّقْدِ أَنَّ الكلام ينصب على تبيان الأُمُورِ السَّلبَيَّة،ِ وهذا غَيْرُ صَحِيح، فالتَّقْدُ يُظْهِرُ الإيجابيات كما يُظْهِرُ السَّليَّاتِ في الوقتِ نَفْسِه،ِ فَإِذا كانَ فِي المَوْضُوعِ أُمُورُ إِيجَابَيَّةٌ فَالنَّاقِدُ يَكْشِفُ النقاب عنها، ولا يكونُ مَوْضُوعِيا إِلَّا إِذا كان عادلا في تبيان الوجهين معا الإيجابي والسَّلْبِي. وفي دِرَاسَةِ ظَاهِرِ مُجْتَمَعِنَا خُلاصَةُ أَنَّ ثُمَّةَ أَناسا ينظُرُونَ إليها بِعَيْنِ الرِّضَا، فلا يَجِدُونَ تَعْرَةً ما ولا خَلَلًا ولا نَقْصا، وأَرَى أَنَّ هَذِهِ الشَّرِيحَةَ غَيْرُ مَوْضُوعِيَّةِ فِي نَظْرَتها وبالمقابلِ نَرَى أناسًا آخرينَ يَنْظُرُونَ إِلَى ظَوَاهِرِ مُجْتَمَعِنَا بِعَيْنِ السُّخْطِ ، فلا يَجِدُونَ فِيهَا أَيَّ بارقة إيجابية، وإِنَّا يَرَونَ أَنَّ الظَّلَامَ يَكْتَنِفها ، وأَنَّ الأَمَل في الخلاص مِنْ سلبياتِهَا مَعْدُوم، وفي تقديرِي أَنَّ هَذِهِ الشَّرِيحَةَ مِنَ النَّاسِ غَيْرُ مَوْضُوعِيَّةِ أيضًا وَرَحِمَ اللَّهُ شَاعِرَنَا العَرَبِيَّ إِذْ يقول:

=== BLOCK 3: شعر ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: وَعَيْنُ الرضا عَنْ كُلِّ عَيْبٍ كليلةً
Hemistich 2: ولَكِنَّ عَيْنَ السُّخْطِ تُبدي المساويا

=== BLOCK 4: تابع النص ===
(Component: TEMPLATE_C_BLOCK.html)
Content: إِنَّ التَّفْكِيرَ النَّقْدِيَّ السَّليم هو الذي لا يَنْظُرُ إلى الظواهر بِعَيْنِ الرضا وَحْدَها، ولا ينظر إليها بِعَيْنِ السُّخْطِ وَحْدَهَا، وَإِنَّمَا يَنْظُرُ إِليها بغَيْنِ المَوْضُوعِيَّة،ِ فَيُعْطِي لِقَيْصَرَ مَا لِقَيْصَر،َ وَللَّهِ مَا لله،ِ وَذَلِكَ فِي مَنْأَى عَنْ أَي تَخَيْرٍ أَو تَعَصُّبِ أو تَشَنُج.ِ

=== BLOCK 5: القسم الثاني ===
(Component: TEMPLATE_C_BLOCK.html)
Content: (۲) يرتبط التفكير التَّقْدِي ارتباطا عضويا بِمَناهج التفكير العلمي، وهو لا يعني مُجَرَّدَ الرَّفْضِ أو التَّفْنِيدِ أو المعارَضَةِ لِمَا هو قَائِم،ُ وَإِنَّمَا يدعو في دراسة أي ظاهرة اجتماعية إلى الاهتمام بالسياقات الاقتصادية والاجتماعِيَّةِ وَالأَبْعَادِ التَّاريخية لها. وهو منهج لا يكتفي بالأشكال الظَّاهِرَةِ فِي واقعها المُحَدَّدِ بِالزَّمَانِ والمكان الرَّاهِتَيْن،ِ وَإِنَّمَا يَبْحَثُ عَنِ الجُدُورِ المُجْتَمَعِيَّةِ التي أَدَّتْ إِلَى تَشَكُلِ هَذِهِ الظَّاهِرَةِ وعلى الصورة التي بدت عليها في أثناء فترة الدراسة. والتَّفْكِيرُ التَّقْدِيُّ لِمُعْطيات الواقع يَسْتَهَدِفُ تأكيد مهمة التغيير، ودَوْرَ التجديد في البَحْثِ وَالمَعْرِفَةِ بغية اكتشاف الأبعاد الحقيقية لهذا الواقع، والسَّعي إلى تجاوز عقباته وصولا إلى الأَجْمَلِ والأكمل.

=== BLOCK 6: الجدول الأساسي ===
(Component: TEMPLATE_C_TABLE.html)
Header 1: (۳) ويَخْتَلِفُ الفلاسِفَةُ مَعَ عَلَمَاءُ النَّفْسِ فِي وجهاتِ النَّظَرِ حول التَّفْكِيرِ النَّقْدِي اختلافًا جَوْهِرِيا:
Row 1 Col 1: إِذْ إِنَّ الفلاسِفَةَ يُؤْكِّدُونَ الحَاجَةَ إِلَى التَّفْكِيرِ النَّقْدِي،
Row 1 Col 2: في الوقت الذي يُفَصِلُ فِيهِ عَلَمَاءُ النَّفْسِ مُصْطلح مهارات التفكير".
Row 2 Col 1: ويرى الفلاسِفَةُ ضَرُورَةَ التأكيد على الحجج والبراهين الموضوعية والمنطقية على أَنَّها مِجُورُ التفكير الانتقادي وجَوْهَرُه،ُ
Row 2 Col 2: في الوقت الذي يركز فِيهِ عَلَمَاءُ النَّفْسِ في عمليات التَّفْكِيرِ نَفْسِهَا،
Row 3 Col 1: وَيَهْتَمُ الفلاسِفَةُ بِمُمَارِسَةِ المنطق والحجج والأدلة على أنها أدوات في شرح حقائِقَ مُعَيِّنَة،ِ
Row 3 Col 2: وَيَرَونَ أَنَّ البَرَامِ الْمُدْرِسِيَّةَ يَنْبغي لها أَنْ تُرَكَز في تصوير التفكير المَنْطِقِي أداة مِنْ أَجْلِ صُنع قراراتٍ أَخْلَاقِيَّةٍ وَمَعْنَوِيَّة.ٍ
Row 4 Col 1: وإذا كانَ عَلَمَاءُ النَّفْسِ يُظْهرون اهتمامًا واضحا بَعَمَلِيَّاتِ التَّفْكِير،ِ وَكَيْفِيَّة تطويرها عِنْدَ المَتَعَلِمِين،َ فَإِنَّهُم يُؤكدون، في الوقتِ نَفْسِه، عَمَلِيَّةَ حَلَ الْمُشْكِلاتِ أَكْثَرَ مِنْ تأكيدهم عَمَلِيَّةَ المَنْطِق.ِ
Row 4 Col 2: والفلاسِفَةُ مُحِقُون في تأكيدهم التفكير الانتقادِي والتفكير التأملي والاستنتاجي، كما أَنَّ عُلَمَاءَ النَّفْسِ في تأكيدهم المشكلات مُحِقُونَ أَيضًا، ذَلِكَ لِأَنَّ طبيعة الحياة تستلزم أن يكونَ المَرْءُ مُزَوَّدًا بمهاراتِ التَّفْكِيرِ الانتِقَادِي.

=== BLOCK 7: القسم الرابع ===
(Component: TEMPLATE_C_BLOCK.html)
Content: (٤) ونحن في تربيتِنَا لِأَبْنَائِنَا بِدءًا مِنَ الأُسْرَةِ وانتهاء بالمجتمع، مُرُورًا بالمدارس والمعاهد والجامعات، مطالبون بالاهتمامِ بِالتَّفْكِيرِ النَّقْدِي من حيث طرح الأسئلة والاستفسار بـ "لماذا"، والتَّمَتَّعِ بِعْقُولِ مُنْفَتِحَةٍ وَغَيْرِ مُتَحَيَّزة، وتحديد الأسباب والاستنتاجاتِ بِرُوحِ مِنَ الْمَوْضُوعِيَّة،ِ وَفِي عملية بناء التفكير الانتقادي لا بُدَّ مِنْ ترسيخ تقاليد مُعَيَّنَةٍ تَمَثَل في احترام الرأي، وتقدير الرأي الآخر والمُوْضُوعِيَّةِ في إصدار الأحكام، ذَلِكَ لأَنَّ الشَّخْصِيَّةَ المتكاملة هي التي تَتَقَبْلُ التَّقْدَ مِنَ الآخرين، وتسعى إلى تعديل مسارها وتطوير أدائها نحو الأفضل فِي ضَوْءِ ما تتلقاهُ مِنْ ملاحظات. ولَقَد جاء في تراثنا : رحم الله امراً أَهْدَى إلينا عيوبنا".

=== BLOCK 8: إجابة مقترحة ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: الأسئلة المُقْتَرَحَةُ فِي الْمَقْطَعِ الأَوَّل:ِ
Content: ج - يَتَبَادِرُ إِلَى اللَّهْنِ أَنَّ الكلام يَنْصَبُّ على تبيان الأُمُورِ السَّلبية. والكاتب يرى أَنَّ ذَلِكَ غَيْرُ صَحِيح.

=== BLOCK 9: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: ماذا يتبادر إلى الذِّهْنِ عندما نُطْلِقُ مَفْهُومَ النَّقْدِ؟ وما رأي الكاتب في ذلك ؟

--- END STREAM ---
