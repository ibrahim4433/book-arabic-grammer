# **SESSION 173**

[TASK DEFINITION]
Objective: Implement page 173.
File: `pages/page_173.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`.
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md` to identify the correct template to use for the continuation.
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
12. Visual Density: The page must be dense. Do NOT leave empty space.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
15. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 173
[CHAPTER_TITLE]: page 173
[CATEGORY_HEADER]: 173
[SECTION_HEADER]: 173
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: إعراب (تتمة) ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
Title: إعراب
Content: مُضَاف إليه مَجْرُورٌ. جملة (هَزَزْتِ): استئنافية، لا محل لها مِنَ الإعراب. جملة (خَلَعَتْ): صَلَةُ المَوْصُولِ، لا محل لها مِنَ الإعراب. جملة (مَاسَتْ): مَعْطُوفَةٌ، لا محل لها مِنَ الإعراب.

=== BLOCK 3: البيت الثالث عشر ===
(Component: TEMPLATE_C_POEM.html)
Poet:
Title:
Hemistich 1: كَسَوْتِهَا وَرَقَ الأَشْواقِ فَازْدَهَرَتْ
Hemistich 2: خَضْرَاءَ يَعْبَقُ مِنْهَا رَوْحُ نَيْسان

=== BLOCK 4: دراسة البيت الثالث عشر ===
(Component: TEMPLATE_C_TABLE.html)
Header 1: العنصر
Header 2: التفصيل
Row 1 Col 1: المفردات
Row 1 Col 2: ازدهرت : تَلالاتْ، يَعْبُقُ : يَفُوحُ، رَوْحُ: نَسِيم. خَضْرَاءَ: صفة مشبهة باسم الفاعل فعلها خضر.
Row 2 Col 1: الشرح
Row 2 Col 2: أَلْبَسْتِ أَيَّتُها الرياحُ القَادِمَةُ مِنَ الشَّرْقِ هَذِهِ الأَغْصَانَ الجرداء أوراق المَحَبَّةِ والشَّوقِ، فَبَدَتْ مُتَلَالِئَةً مُخْضَلَّةً تَرْفِلُ بِثياب خضراء سُندسِيَّةِ، يَفوح منها عَبَقَ الربيع وعبيرة، ويَضُوعُ مِنْهَا نَسِيمُ نَيْسَانَ الفَوَّاحُ.
Row 3 Col 1: الفكرة والبلاغة
Row 3 Col 2: الفكرة: التَّعْبِيرِ عَنْ إِثَارَةِ مَشَاعر الشَّوْقِ وتجددها. البلاغة: (وَرَقَ الأَشواقِ): تشبيه بليغ إضافي.
Row 4 Col 1: الإعراب
Row 4 Col 2: كَسَوْتِهَا: فِعْلٌ مَاضِ مَبْنِي على السُّكُونِ؛ لاتِصَالِهِ بِتَاءِ الرَّفْعِ الْمُتَحَرِّكَةِ. والنَّاءُ، ضميرٌ مُتَصِلٌ مَبْنِي على الكَسْرَةِ في محل رفع، فاعل. وها، ضمير متصل مبني على السُّكُونِ فِي مَحَلِّ نَصْبِ، مَفْعُولُ بِهِ أَول. وَرَقَ: مَفْعُولُ بِهِ ثَانٍ مَنْصُوبُ. الأَشْوَاقِ: مُضَافُ إليه مجْرُورُ. فَازْدَهَرَتْ: الفَاءُ، حَرْفُ عَطْفٍ. خَضْرَاءَ: حالٌ مَنْصُوبَةٌ. رَوْحُ: فَاعِلَ مَرْفُوعُ. نَيْسَانِ: مُضَاف إليهِ مَجْرُورٌ. جملة (كَسَوْها): استئنافية، لا محل لها مِنَ الإعراب. جملة (فازْدَهَرَتْ): مَعْطُوفَةٌ، لَا مَحَلَّ لها من الإعراب. جملة (يَعْبَقُ مِنْهَا رَوْحُ نَيْسان): حاليَّةٌ، مَحَلُّها النَّصْب.

=== BLOCK 5: ملحق الأبيات الخارجية ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: ملحق الأبيات الخارجية المتممة الواردة في ديوان الشاعر نسيب عريضة:

=== BLOCK 6: البيت الأول من الملحق ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: حَبَّ فِي الغَرْبِ ذكرى الأرز والبان
Hemistich 2: ما هَذَبَتْكَ ليالي البعد يا عاني

=== BLOCK 7: دراسة البيت الأول من الملحق ===
(Component: TEMPLATE_C_TABLE.html)
Header 1: العنصر
Header 2: التفصيل
Row 1 Col 1: المفردات
Row 1 Col 2: البان: ضَرْبٌ مِنَ الشَّجَرِ سَبْطُ القوام، لين، ورقة كورق الصفصاف ويُشَبَّهُ بِهِ الحسان في الطول واللين. عاني: العاني: الدليل. الجمع: عوان.
Row 2 Col 1: الشرح
Row 2 Col 2: أَيُّها المهاجر المعاني لم تستطع الليالي التي أمضيتها في بلادِ الغُرْبَةِ بَعِيدًا عَنْ وَطَنِكَ، أَنْ تُنْسِيكَ ذِكْرَيَاتِ الوَطَنِ.
Row 3 Col 1: الفكرة والشعور
Row 3 Col 2: الفكرة: الاحتفاظ بذكريات الوَطَنِ في بلاد الغُرْبَةِ. الشُّعُور: الشَّوْقُ والحنين. الأداة: التراكيب. المثال: حَبَّ في الغرب ذكرى الأرز والبان.
Row 4 Col 1: البلاغة
Row 4 Col 2: (حَبَّ ذكرى، هَذَبَتْكَ ليالي): استعارَةُ مَكْنِيَّةٌ. (البان، عاني): تصريع.
Row 5 Col 1: الإعراب
Row 5 Col 2: (حَبَّ في الغَرْبِ ذكرى الأَرز): ابتدائية لا محل لها مِنَ الإعراب. (ما هَذَبَتُكَ ليالي البعد): استئنافية لا محل لها من الإعراب. ذكرى، ليالي: فاعل مَرْفُوعٌ. الأَرْزِ، البَعْدِ: مُضَافُ إِلَيْهِ مَجْرُورٌ.

=== BLOCK 8: البيت الثاني من الملحق ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: ابن العروبة لا أَسْلُو الرُّبُوعَ وَلَو
Hemistich 2: كانت مثيرة أوصابي وأشجاني

=== BLOCK 9: دراسة البيت الثاني من الملحق ===
(Component: TEMPLATE_C_TABLE.html)
Header 1: العنصر
Header 2: التفصيل
Row 1 Col 1: المفردات
Row 1 Col 2: أوصابي: الوَصَبُ الوَجَعُ والمرض، والتَّعَبُ وَالفُتُورُ فِي البَدَنِ. أَشجانِ: الشَّجَنُ: الهم والحزن. مثيرة: اسم فاعل، فِعْلُه: أثار.
Row 2 Col 1: الشرح
Row 2 Col 2: أنا العربي لا أنسى رُبُوعَ الوَطَنِ مَعَ أَنَّهَا السَّبَبُ الْمُبَاشَرُ في إثارة أوجاعي وأمراضي، والمحرك هُمُومي وأحزاني.
Row 3 Col 1: الفكرة والشعور
Row 3 Col 2: الفكرة: الانتماء إلى الوَطَنِ رُغْم المعاناةِ بِسَبَبِهِ. الشَّعور: ألم. الأداة: التراكيب. المثال: كانت مثيرة أوصابي.
Row 4 Col 1: الإعراب
Row 4 Col 2: ابن: خبر مَرْفُوع (المبتَدَأ محذوف تَقْدِيرُهُ "أنا"). العُرُوبَةِ، أوصابي: مُضاف إِلَيْهِ مَجْرُورٌ. (لا أَسْلُو): في مَحَلِّ رَفْعِ خَبَر. (للمبتدأ المحذوف "أنا"). الرَّبُوعَ: مَفْعُولُ بِهِ مَنصُوبٌ. لَو: حَرْفُ شَرْطِ غَيْرِ جَازِم. مثيرة: خَبَرٌ مَنْصُوبٌ.

=== BLOCK 10: البيت الثالث من الملحق ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: تَغَلْغَلِي بينَ أَضْلاعي إلى كَبِدِي
Hemistich 2: وَخَفَّفِي مِنْ حَرُورِ السائل القاني

=== BLOCK 11: دراسة البيت الثالث من الملحق ===
(Component: TEMPLATE_C_TABLE.html)
Header 1: العنصر
Header 2: التفصيل
Row 1 Col 1: الشرح
Row 1 Col 2: اخترقي أيتها الرياح الشَّرْقِيَّةُ أضلاعي واللجي أحشائي لتخففي مِنْ حرارَةِ نَارِ الشَّوْقِ الْمُسْتَعِرَةِ في داخلي.
Row 2 Col 1: الفكرة
Row 2 Col 2: تَصْوِيرُ شِدَّةِ الشَّوْقِ والحنين إلى الوطن.
Row 3 Col 1: الإعراب
Row 3 Col 2: تَغَلْغَلِي، خَفَّفِي: فِعْلُ أَمْرِ مَبْنِي على حذف النُّونِ. بَيْنَ: مَفْعُولُ فِيهِ ظَرْفُ مَكانٍ مَنصُوبٌ. أَضْلاعي، السَّائِلِ: مُضافُ إِلَيْهِ مَجْرُورٌ. القاني: صِفَةٌ مَجْرُورَةٌ.

=== BLOCK 12: البيت الرابع من الملحق ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: وذكريني بِمَا أُنسيْتُ مِنْ أَمَل
Hemistich 2: وجَنِّحِينِي أُرَفْرِف فوق أوطاني

=== BLOCK 13: دراسة البيت الرابع من الملحق ===
(Component: TEMPLATE_C_TABLE.html)
Header 1: العنصر
Header 2: التفصيل
Row 1 Col 1: الشرح
Row 1 Col 2: جَدِّدِي أَيَّتُها الرياحُ الشَّرْقِيَّةُ أَمَلَ العودة إلى الوَطَنِ فِي نَفْسِي، وامنحيني جناحين؛ لأطير بهما إلى الوطن.
Row 2 Col 1: الشعور والبلاغة
Row 2 Col 2: الشعور: الشَّوْقُ، والحَنِين. الأداة: التراكيب. المثال: جَنِّحِينِي أُرَفْرِفُ فوق أوطاني. البلاغة: (ذكرينِي)، (أَرَفْرِف): استعارَةُ مَكْنِيَّة.
Row 3 Col 1: الإعراب
Row 3 Col 2: ذكريني، جَنِّحِينِي: فِعْلُ أَمْرِ مَبْنِي على حذف النون. بِمَا: الباءُ حَرْفُ جَرِّ. ما: اسمٌ مَوْصُولُ فِي مَحَلِّ جَرِّ بِحَرْفِ الجَرِّ. أُنسِيتُ: فِعْلُ مَاضِ مَبْنِي لِلْمَجْهُول. (أُنسَيْتُ): صِلَةُ الموصول لا محل لها من الإعراب. أرفرف: فعل مُضارع مَجْزُوم؛ لأنَّهُ جواب الطلب. فوق: مَفْعُولُ فِيهِ ظَرْفُ مكان منصوب. أوطاني: مُضافُ إِلَيْهِ مَجْرُورٌ.

=== BLOCK 14: البيت الخامس من الملحق ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: أنا المهاجر لا أنسى الوداع وما
Hemistich 2: جَرَى مِنَ الدمع في أَجْفان غزلان

=== BLOCK 15: دراسة البيت الخامس من الملحق ===
(Component: TEMPLATE_C_TABLE.html)
Header 1: العنصر
Header 2: التفصيل
Row 1 Col 1: المفردات
Row 1 Col 2: أجفان غزلان: يعني هنا عيون الأحبة. المهاجر: اسم فاعِلِ فِعْلُه هاجر.
Row 2 Col 1: الشرح
Row 2 Col 2: أنا القاطِنُ في بلاد الغُرْبَةِ، لا أستطيع نسيان لحظات الفراق المؤثرة، ولا سيما تلك الدموع السَّخِيَّة التي جادَتْ بها عُيُونُ الأَحِبَّةِ.
Row 3 Col 1: الفكرة والشعور
Row 3 Col 2: الفكرة: تأكيد عدم نسيانِ مَشْهَدِ فِرَاقِ الأحبة. الشعور: الشَّوْقُ، والحنين. الأداة: التراكيب. المثال: لا أنسى الوداع.
Row 4 Col 1: البلاغة
Row 4 Col 2: (أجفان غزلان): استعارَةُ تَصْرِيحِيَّةٌ. (شَبَّهَ الْأَحِبَّة بالغزلان).
Row 5 Col 1: الإعراب
Row 5 Col 2: أنا: ضمير رفع مُنْفَصِلُ فِي مَحَلِّ رَفْعِ مُبْتَدَأ. المهاجر: خَبَرَ مَرْفُوع. (لا أنسى): في محل رفع خبر. الوداع: مَفْعُولُ بِهِ مَنصوب. ما: اسم مَوْصُول في محل نصب اسم مَعْطُوف. (جَرَى): صِلَةُ الموصول لا محل لها من الإعراب. غزلان: مُضَافُ إِلَيْهِ مَجْرُورٌ.

--- END STREAM ---
