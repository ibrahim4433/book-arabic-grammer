# **SESSION 129**

[TASK DEFINITION]
Objective: Implement page 129.
File: `pages/page_129.html`
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
[LESSON_NUMBER]: 129
[CHAPTER_TITLE]: page 129
[CATEGORY_HEADER]: 129
[SECTION_HEADER]: 129
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: البيت التاسع ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b12901
[POEM_TITLE]: البيت التاسع
[POET_NAME]:
[RIGHT_HEMISTICH]: - أَقْبِلُوا أَيُّهَا الحَيَارَى فهذا الهُ
[LEFT_HEMISTICH]: دَرْبُ طَلْقٌ مُشَوِّقُ وَضَاءُ

=== BLOCK 3: المفردات والشرح ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b12902
Title: المفردات والشرح
Content: <p><span class="text-accent">المفردات:</span> مشوق : منير. وضاء: مشرق والخيارى: صِفَةٌ مُشَبَّهَةٌ باسم الفاعل فعلها : حار. وطلق : صِفَةٌ مُشَبَّهَةٌ باسم الفاعل فعلها : طلق. ومُشَوَق: اسم فاعل، فِعْلُهُ : شوق. ووَضَاء:ُ مبالغة اسم فاعل، فِعْلُها : وَضُو.</p><p><span class="text-accent">الشرح:</span> هيا اسلكوا أَيُّهَا المَتَرَدَدُونَ سَبِيلَ الوَحْدَةِ؛ لأَنَّهُ طَرِيقٌ سَهْل مُمَهَدٌ خَلَا مِنَ الحواجز والعثرات، مُثِيرٌ لِلْإِعْجَاب،ِ شَدِيدُ الإِشْرَاقِ</p>

=== BLOCK 4: الفكرة ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[UNIQUE_ID]: b12903
Title: الفكرة
Content: الدَّعْوَة إلى الوَحْدَةِ العَرَبِيَّة )تحفيز التَرَدَدِين للالتحَاقِ بِرَكْبِ الوَحْدَةِ العربية(.

=== BLOCK 5: تحليل البيت التاسع ===
(Component: TEMPLATE_C_TABLE.html)
[UNIQUE_ID]: b12904
[TABLE_HEADER_1]: الشعور
[TABLE_HEADER_2]: الأداة
[TABLE_HEADER_3]: المثال
[TABLE_HEADER_4]: الأساليب
[ROW_1_COL_1]: حب، وغيرة
[ROW_1_COL_2]: التراكيب
[ROW_1_COL_3]: أَقْبِلُوا أَيُّهَا الحَيَارَى
[ROW_1_COL_4]: أَقْبلُوا : أسلوب أمر. صيغته: فعل أمر

=== BLOCK 6: إعراب البيت التاسع ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b12905
[WORD_1]: أَقْبَلُوا
[ROLE_1]: فِعْلُ أَمْرِ مَبْنِي على حَذْفِ النُّونِ لَأَنَّ مُضَارِعَهُ مِنَ الأَفْعَالِ الخَمْسَة.ِ والواو، ضميرٌ مُتَّصِلِّ مَبْنِي على السُّكُونِ فِي مَحَلِّ رَفْع،ِ فَاعِل.َ والأَلِفُ حَرْفُ تَفْرِيقِ
[WORD_2]: أَيُّهَا
[ROLE_2]: أَي،ُّ مُنادى نَكِرَةً مَقْصُودَةٌ مَبْنِي على الصَّمَ فِي مَحَلِّ نَصْبِ على النداء. وها، للتنبيه
[WORD_3]: الخيارى:
[ROLE_3]: صِفَةٌ مَرْفُوعَة،ٌ وعلامَةً رَفْعِهَا الصَّمَّةُ المُقَدرة على الأَلِفِ مَنَعَ ظُهُورَهَا التَّعَذُرُ
[WORD_4]: فهذا
[ROLE_4]: الفاء، حَرْفُ استثناف. والهاء للتنبيه. وذا، اسم إشارَةِ مَبْنِي على السُّكُون في حَلِ رَفْع،ِ مُبْتَدَ
[WORD_5]: الدَّرْبُ :
[ROLE_5]: بَدَلَّ مَرْفُو
[WORD_6]: طلق:
[ROLE_6]: خَبَرَ مَرْفُو
[WORD_7]: مُشَوَقَ
[ROLE_7]: خَبَرُ مَرْفُوعٌ
[WORD_8]: وَضَاء:ُ
[ROLE_8]: خَبَرَ مَرْفُوع
[WORD_9]: الجمل
[ROLE_9]: لجملة )أَقْبَلُوا(، وجُمْلَةً )هذا الدَّرْبُ طَلْقَ مُشَوَقٌ وَضَاءُ( : استئنافِيَّة،ٌ لَا مَحَلَّ لها مِنَ الإعراب.

=== BLOCK 7: البيت العاشر ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b12906
[POEM_TITLE]: البيت العاشر
[POET_NAME]:
[RIGHT_HEMISTICH]: -١٠ دَرْبُ تَوْحِيدِ أُمَّةٍ جَبَلَتْها
[LEFT_HEMISTICH]: مِنْ عَبِيرِ الْمَكَارِمِ العَلْيَاءُ

=== BLOCK 8: المفردات والشرح ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b12907
Title: المفردات والشرح
Content: <p><span class="text-accent">المفردات :</span> جَبَلَتُهَا كَوَّنَتُهَا . العلياء: الشَّرَف والرفعة.</p><p><span class="text-accent">الشرح :</span> إِنَّ هذا السَّبِيلَ الَّذِي أَدْعُوكُم لِرُوبِهِ هو الطريق الذي تَتَوَجَّدُ فِيهِ الأُمَّةُ العَرَبِيَّة.ُ تلك الأُمَّة التي جَعَلَهَا شَرَفُهَا وَرِفْعَتُهَا تَنْشَأْ على حبّ الخير، والإكثار مِنْ فِعْلِهِ</p>

=== BLOCK 9: الفكرة ===
(Component: TEMPLATE_C_BENEFIT.html)
[UNIQUE_ID]: b12908
Title: الفكرة
Content: تَمْجِيد الأُمَّةِ الْعَرَبِيَّةِ وَالتَّغَنِي بِصِفَاتِهَا .

=== BLOCK 10: تحليل البيت العاشر ===
(Component: TEMPLATE_C_TABLE.html)
[UNIQUE_ID]: b12909
[TABLE_HEADER_1]: الشعور
[TABLE_HEADER_2]: الأداة
[TABLE_HEADER_3]: المثال
[TABLE_HEADER_4]: البلاغة
[ROW_1_COL_1]: افتخار واعتزاز
[ROW_1_COL_2]: التَّراكيب
[ROW_1_COL_3]: جَبَلَ هَا مِنْ عَبِيْرِ المَكَارِمِ العلياء
[ROW_1_COL_4]: )جَبَلَتها العَلْيَاءُ(: استعارَةً مَكْنِيَّة

=== BLOCK 11: إعراب البيت العاشر ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID]: b12910
[WORD_1]: دَرْبُ :
[ROLE_1]: خَبَرٌ مَرْفُوعٌ
[WORD_2]: تَوْحِيد،ِ أَمَّة،ٍ المكارم:
[ROLE_2]: مُضَاف إليهِ مَجْرُوز
[WORD_3]: العَلْيَاء:ُ
[ROLE_3]: فَاعِلَ مَرْفُوعُ
[WORD_4]: الجمل
[ROLE_4]: جَمْلَةٌ جَبَلَ هَا مِنْ عَبِيرِ الْمَكَارِمِ الْعَلْيَاءُ(: صِفَة،ٌ مَحَلَّهَا الجَر.ُّ

=== BLOCK 12: البيت الحادي عشر ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b12911
[POEM_TITLE]: البيت الحادي عشر
[POET_NAME]:
[RIGHT_HEMISTICH]: -۱۱ في غَدٍ تَرْحَفُ الجُمُوعُ لِتَبْنِي
[LEFT_HEMISTICH]: بيَدَيْهَا مَا هَدَّمَ الأَعْدَاءُ

=== BLOCK 13: الشرح والفكرة ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b12912
Title: الشرح والفكرة
Content: <p><span class="text-accent">الشرح</span> في القَرِيبِ العَاجِلِ سَتُبَاشِرُ الجَمَاهِيرُ العَرَبِيَّةُ صِنَاعَةَ المَسْتَقْبَلِ الوَاعِدِ حَيْثُ تَقَوْمُ بِبِنَاءِ مَا فَتَتَهُ الْمُسْتَعْمِرُ الغَرْبِيُّ بِفَرْضِ التَّجْزِئَةِ على الأُمَّة،ِ وَزَرْع العُ لَةِ وَالْفُرْقَةِ بَيْنَ أَبْنَائِهَا</p><p><span class="text-accent">الفكرة :</span> التَّفَاؤُلُ بِقِيَامِ الوَحْدَةِ الإيمان بِقُدْرَةِ الجَمَاهِير العربية على بِنَاءِ مَا هَدَّمَهُ المستَعْمِ .(</p>

=== BLOCK 14: تحليل البيت الحادي عشر ===
(Component: TEMPLATE_C_TABLE.html)
[UNIQUE_ID]: b12913
[TABLE_HEADER_1]: الشعور
[TABLE_HEADER_2]: الأداة
[TABLE_HEADER_3]: المثال
[TABLE_HEADER_4]: البلاغة
[ROW_1_COL_1]: أمل وتفاؤل
[ROW_1_COL_2]: التَّراكيب
[ROW_1_COL_3]: في غَدٍ تَزْحَفُ الجمُوعُ لِتَبْنِي
[ROW_1_COL_4]: )تَبْنِي هَدَّمَ( طباق إيجاب

=== BLOCK 15: إعراب البيت الحادي عشر ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b12914
[WORD_1]: الجموع:
[ROLE_1]: فَاعِلَ مَرْفُوعُ
[WORD_2]: لِتَبْنِي:
[ROLE_2]: الام،ُ حَرْفُ جَرٍ وَتَعْلِيل. وتَيْنِي فِعْلَ مُصَارِعٌ مَنْصُوبٌ بِأَنْ الْمُضْمَرَةِ بَعْدَ لَامِ التَعْلِيل،ِ وعلامَةُ نَصْبِهِ الفَتْحَةُ المقدرة على الياء، مَنَعَ ظُهُورَهَا التَّقَل.ُ والْمَصْدَرُ الْمُوَوَّلُ مِنْ أَنَّ الْمُصْمَرَة والفِعْلَ بَعْدَهَا في محل جر بحرف الجر.
[WORD_3]: ما :
[ROLE_3]: اسم مَوْصُولُ مَبْنِي على السُّكُون، في مَحَلِّ نَصْب،ِ مَفْعُولُ بِهِ
[WORD_4]: الْأَعْدَاء:ُ
[ROLE_4]: فاعِلَ مَرْفُوةٌ
[WORD_5]: الجمل
[ROLE_5]: جُمْلَةً تَرْحَفُ الجمُوعُ اسْتِنَافِيَّة،ٌ لا محل لها مِنَ الإعراب جملَةُ تَبْنِي(: صِلَةُ المَوْصُول،ِ لا محل لها مِنَ الإعراب جُمْلَهُ هَدَّمَ الْأَعْدَاءُ(: صِلَةُ الْمَوْسُول،ِ لا مَحَلَّ لها مِنَ الإعراب.

=== BLOCK 16: التعبير الكتابي - التعبير الأدبي ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b12915
Title: التعبير الكتابي - التعبير الأدبي
Content: <p class="text-accent font-bold">مخطط موضوع الوحدة الأولى - أدب القضايا الوطنية والقومية</p><p><span class="text-primary">أولاً - مقدمة مناسبة</span><br>بمقدور الطالب أن يستوحي مقدمة مناسبة تَدُورُ حَوْلَ أَدَب القضايا الوَطَبَيَّة والقَوْمِيَّة.</p><p><span class="text-primary">ثانيا - الأدب القومي:</span><br>- الدَّعْوَةُ إِلَى التنبهِ إِلى واقع الأُمَّةِ المتردي:</p>

=== BLOCK 17: شعر إبراهيم اليازجي ومعروف الرصافي ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b12916
[POEM_TITLE]: الدَّعْوَةُ إِلَى التنبهِ
[POET_NAME]: إِبْرَاهِيمُ اليَازجي:
[RIGHT_HEMISTICH]: تَنَبَّهُوا وَاسْتَفِيقُوا أَيُّهَا الْعَرَبُ
[LEFT_HEMISTICH]: فَقَدْ طَمَى الخَطَبُ حَتَّى غَاصَتِ الرَّكَبُ

=== BLOCK 18: شعر معروف الرصافي ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b12917
[POEM_TITLE]:
[POET_NAME]: مَعْرُوفُ الرِّصَافِي:
[RIGHT_HEMISTICH]: أَمَا آنَ أَنْ يَغْشَى البلاد سعودها
[LEFT_HEMISTICH]: وَيَذْهَبَ عَنْ هَذِي النِّيَامِ هُجُودها

=== BLOCK 19: التحريض الثوري ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b12918
Title: التحريض التوري
Content: <p>- التحريض التوري للوقوف في وَجِهِ الظَّامِ مِنْ خلال :</p><p><span class="text-primary">الحت على النهوض:</span></p>

=== BLOCK 20: الحث على النهوض ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b12919
[POEM_TITLE]:
[POET_NAME]: إبراهيم اليازجي:
[RIGHT_HEMISTICH]: بالله يا قَوْمَنَا هِبُوا لِشَأْنِكُمُ
[LEFT_HEMISTICH]: فَكُمْ تُنَادِيكُمُ الأَشْعَارُ و الخُطَبُ

=== BLOCK 21: التذكير بماضي الأجداد ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b12920
Title: التذكير بالماضي
Content: <p><span class="text-primary">التذكير بِمَاضِي الْأَجْدَادِ المجيد:</span></p>

=== BLOCK 22: شعر التذكير ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b12921
[POEM_TITLE]:
[POET_NAME]: إبراهيم اليازجي:
[RIGHT_HEMISTICH]: الَسْتُم مَنْ سَطَوا فِي الْأَرْضِ وَاقْتَحَمُوا
[LEFT_HEMISTICH]: شَرْقًا وغَرْبًا، وعَزَّوا أَينما ذَهَبُوا

=== BLOCK 23: التعبير عن الفرح ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b12922
Title: مشاعر الفرح
Content: <p><span class="text-primary">التَّعْبِيرِ عَنِ مَشَاعِرِ الفَرَحِ يَامِ الوَحْدَة:ِ</span></p>

=== BLOCK 24: شعر الفرح ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b12923
[POEM_TITLE]:
[POET_NAME]: سلامة عبيد:
[RIGHT_HEMISTICH]: أَشْرَقَ الفَجْرُ فَالدُّرُوبُ ضِيَاءُ
[LEFT_HEMISTICH]: وأَنَاشِيْدُ عِزَّة وحُدَاءُ

=== BLOCK 25: استكمال شعر الفرح ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b12924
[POEM_TITLE]:
[POET_NAME]:
[RIGHT_HEMISTICH]: إِنَّهَا فَرْحَةُ الْحَيَاةِ فَمِيدِي
[LEFT_HEMISTICH]: يَا رَاوَابِي وَهَلِلِي يَا سَمَاءُ

--- END STREAM ---
