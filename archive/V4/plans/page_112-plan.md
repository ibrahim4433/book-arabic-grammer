# **SESSION 112**

[TASK DEFINITION]
Objective: Implement page 112.
File: `pages/page_112.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
1.5 ANTI-HALLUCINATION & STRICT TYPOGRAPHER RULE (CRITICAL): Do NOT invent, hallucinate, or add new grammar rules, examples, or external text. ONLY use the exact text slices provided in the Raw Input Text. You MUST use 100% of the provided raw text. NO summarizing, NO deleting, NO adding new content. Every piece of text must map to an approved TEMPLATE.
1.6 THE TYPO EXCEPTION: You are explicitly permitted to correct obvious typos, spelling errors, or grammatical errors in the raw Arabic text during planning.
2. Metadata:
    * Page Number: 112
    * Title: page 112
    * Header Data (MANDATORY): You must populate the `TEMPLATE_C_HEADER.html` component with the specific metadata provided in the prompt:
        * `[CATEGORY_HEADER]` <- Use `112`
        * `[SECTION_HEADER]` <- Use `112`
        * `[AUTHOR_NAME]` <- Use `أ.الياس خفيف`
        * `[AUTHOR_PHONE]` <- Use `994066850 963+`
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
[LESSON_NUMBER]: 112
[CHAPTER_TITLE]: page 112
[CATEGORY_HEADER]: 112
[SECTION_HEADER]: 112
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Cut Content Block ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[UNIQUE_ID]: b82044
[BLOCK_TITLE]: تحليل القصيدة
[CONTENT]: أَفْرَاسُنَا فِي مَلْعَب. البلاغة: (كَمْ نَبَتْ أَسْيَافُنَا فِي مَلْعَب،ِ كَبَتْ أَفْرَاسُنَا فِي مَلْعَبِ) : كناية عن الهزيمة الإعراب: كَمْ خَبَرَيَّةٌ مَبْنِيَّةٌ على السكون في محل نَصْبَ مَفْعُولٌ مُطْلَق.َ

=== BLOCK 3: Poem Verse 11 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b73324
[POEM_TITLE]: البيت الحادي عشر
[UNIQUE_ID_BIO]: b04803
[POET_NAME]: ١١-
[RIGHT_HEMISTICH]: مِنْ نِضَالِ عَائِرٍ مُصْطَخِبِ
[LEFT_HEMISTICH]: لِنِضَالِ عَائِرٍ مُصْطَخِبِ

=== BLOCK 4: Poem 11 Explanation ===
(Component: TEMPLATE_C_SPLIT.html)
[UNIQUE_ID_1]: b21934
[COLUMN_1_TITLE]: المفردات
[COLUMN_1_CONTENT]: مصطحب : صَخِبَ الجَمْعُ صَخْبًا : عَلَتْ فيه الأصوات واختلطتْ اصطحب القَوْمُ : تصايحوا وتضاربوا
[UNIQUE_ID_2]: b62133
[COLUMN_2_TITLE]: الشرح
[COLUMN_2_CONTENT]: كُنَّا نَنْتَقِلُ مِنْ مَعْرَكَةِ قاسِيَةِ طَاحِنَةِ لا توفيق فيها إلى مَعْرَكَةِ أَشَد وأَعْنَف.

=== BLOCK 5: Poem Verse 12 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b53504
[POEM_TITLE]: البيت الثاني عشر
[UNIQUE_ID_BIO]: b11543
[POET_NAME]: -۱۲
[RIGHT_HEMISTICH]: شَرَفُ الوَثْبَةِ أَنْ تُرْضي العُلَا
[LEFT_HEMISTICH]: غُلِبَ الواثِبُ أَمْ لَمْ يُغْلَ ؟!

=== BLOCK 6: Poem 12 Explanation ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b46227
Title: المفردات والشرح
Content: <span class="text-accent">المفردات الوثبَة وثبَ يَبْبُ وَثَبًا وَنُونَا قَفَر.َ وتب على فلان: غالبه. والمقصود هنا التضال والكفاح الواتب المناضل. والوايب: اسم فاعِلِ فِعْلُهُ وَتَبَ</span><br><br>الشَّرح : يَكْفِي المَنَاضِلِ فَخْرًا وَشَرَفًا أَنْ يَكُونَ نِصَالُهُ مِنْ أَجْلِ الفَاعِ عَنِ الوَطَنِ لِبُلُوعَ الْمَجْد،ِ وَلَا يَهِم بَعْدَ ذَلِكَ أَكَانَ مُنْتَصِرًا أَمْ مَهْرُومًا.

=== BLOCK 7: Poem 12 Balagha & Irab ===
(Component: TEMPLATE_C_SPLIT.html)
[UNIQUE_ID_1]: b97339
[COLUMN_1_TITLE]: البلاغة
[COLUMN_1_CONTENT]: (الوَثْبَةِ تُرْضِي)، (تُرْضِي العلا): استعارَةً مَكْنِيَّة.ٌ (غُلِب،َ لم يقلب) طباق سلب
[UNIQUE_ID_2]: b49307
[COLUMN_2_TITLE]: الإعراب
[COLUMN_2_CONTENT]: شَرَف: مُيْتَدَاً مَرْفُوعُ أَنْ تُرْضِي العلا: الْمَصْدَرُ الْمُؤْوَّلُ فِي مَحَلَّ رَفْعِ خَبَر.َ (تُرْضِي): صِلَةُ المَوْصُولِ لا تحل لها مِنَ الإغراب الوائِبُ : نَائِبُ فَاعِلِ مَرْفُوع.ٌ

=== BLOCK 8: Poem Verse 13 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b02668
[POEM_TITLE]: البيت الثالث عشر
[UNIQUE_ID_BIO]: b39314
[POET_NAME]: -۱۳
[RIGHT_HEMISTICH]: فالِتَفِتْ مِنْ كُوَّةِ الفردوس يا فيصل العلياء،
[LEFT_HEMISTICH]: وانْظُرْ وَاعْجَبِ

=== BLOCK 9: Poem 13 Explanation ===
(Component: TEMPLATE_C_SPLIT.html)
[UNIQUE_ID_1]: b05212
[COLUMN_1_TITLE]: المفردات
[COLUMN_1_CONTENT]: كوة : الكُوَّةُ خَرْقُ في الجدار، فتحة، نافذة للتَّهْوِيَة والإضاءة. الجَمْعُ : كُوى فَيُصَل: الفَيْصَل:ُ الحاكم أو القاضي. والماضي القاطع يفصل بين الحق والباطل الجمع: فياصل
[UNIQUE_ID_2]: b36411
[COLUMN_2_TITLE]: الشرح والإعراب
[COLUMN_2_CONTENT]: الشرح : تَلَفَتْ أَيُّهَا الشَّهِيدُ مِنْ جَنَّةِ الفِرْدوس التي تَتَرَبَّعُ على عَرْشها، وانظُرْ بِغَيْنِكَ واعْجَبْ بِمَا فَعَلْناه بالمُسْتَعْمر<br><br><span class="font-bold">الإعراب:</span> الفردوس، العلياء : مُضَافُ إِلَيْهِ يَجْرُور.ٌ

=== BLOCK 10: Poem Verse 14 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b57023
[POEM_TITLE]: البيت الرابع عشر
[UNIQUE_ID_BIO]: b15660
[POET_NAME]: ١٤-
[RIGHT_HEMISTICH]: أَتَرَى كَيْفَ اشْتَفَى النَّارُ مِن ال
[LEFT_HEMISTICH]: فاتح الْمُسْتَرَقِ الْمُسْتَلِبِ

=== BLOCK 11: Poem 14 Explanation ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b00466
Title: المفردات والشرح
Content: <span class="text-accent">المفردات اشتقى مِنْ عِلَّتِهِ بَرَى وَاشْتَفَى بكذا : شَفِي بِهِ وَاشْتَفَى من عده: بلغ ما يُذْهِبُ غَيْظَهُ مِنْهُ الفَاتِحِ الْمُسْتَرِق،ِ الْمُسْتَلِب:ِ اسم فاعل والفعل على الترتيب فتح استرق، استلب</span><br><br>الشرح هل ترى كيف أخذنا بثأرنا وشَفَيْنَا غِلَّنَا حِيْنَمَا جَرَّعْنَا الْمُسْتَعْمِرَ الغَاصِبَ السارق كؤوس الهزيمة.

=== BLOCK 12: Poem 14 Table ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: الفكرة
[HEADER_2]: الشَّعُور
[HEADER_3]: الأداة
[CELL_1]: تصوير هَزِيمَةِ المُسْتَعْمِ
[CELL_2]: اعتزاز، وافتخار، وفرح
[CELL_3]: التراكيب المثال: اشْتَفَى التَّأْرُ مِنَ الفَاتِح.ِ

=== BLOCK 13: Poem 14 Balagha & Irab ===
(Component: TEMPLATE_C_SPLIT.html)
[UNIQUE_ID_1]: b57977
[COLUMN_1_TITLE]: البلاغة
[COLUMN_1_CONTENT]: (اشْتَفَى النَّارُ) : استعارَةً مَكْنِيَّة
[UNIQUE_ID_2]: b81911
[COLUMN_2_TITLE]: الإعراب
[COLUMN_2_CONTENT]: كيف : اسم استفهام في مَحَلَ نَصْبَ مَفْعُول مُطْلَق المُسْترق، الْمُسْتَلِبِ : صِفَةٌ مَجْرُورَة.ً

=== BLOCK 14: Poem Verse 15 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b47547
[POEM_TITLE]: البيت الخامس عشر
[UNIQUE_ID_BIO]: b43269
[POET_NAME]: ١٥-
[RIGHT_HEMISTICH]: وطوى ما طال من راياته
[LEFT_HEMISTICH]: في ثنايا تجمِهِ الْمُحْتَجِب؟!

=== BLOCK 15: Poem 15 Explanation ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b67241
Title: المفردات والشرح
Content: <span class="text-accent">المفردات المختجب: حَجَبَ عَنْهُ الضَّوء: سَتَرَهُ عَنْهُ والمُخْتَجِب اسم فاعل فعله: احتجب</span><br><br>الشرح : بَعْدَ أَنْ جَرَّعْنَا الْعَدُ الزَيْمَةَ رَاحَ يُلَمْلِمْ أعلامهُ وَيَطُويها ويخفيها في ظُلُمَةِ نَجْمِهِ الذي أَفِلَ وانطفا.ً

=== BLOCK 16: Poem 15 Table ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: الفكرة
[HEADER_2]: الشعور
[HEADER_3]: الأداة
[CELL_1]: التَّعْبِيرُ عَنِ الشمالةِ بجريمة المستَعْمر
[CELL_2]: اعتزاز، وافتخار، وفرح
[CELL_3]: التراكيب المثال: طوى ما طال من راياته

=== BLOCK 17: Poem 15 Irab ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[UNIQUE_ID]: b48223
[TITLE]: الإعراب
[CONTENT]: ما : اسم مَوْصُولُ فِي مُحَلَ نَصْبَ مَفْعُول بِه.ِ (طَالَ : صِلَةُ الْمَوْسُولِ لَا مَحَلَّ لها مِنَ الإعراب تجمه: مُضافُ إِلَيْهِ يَجْرُورٌ المُحْتَجِبِ : صِفَةٌ مَجْرُورَة.ٌ

=== BLOCK 18: Poem Verse 16 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b31653
[POEM_TITLE]: البيت السادس عشر
[UNIQUE_ID_BIO]: b51840
[POET_NAME]: -١٦
[RIGHT_HEMISTICH]: ما نسينا دمعة عاصيتها
[LEFT_HEMISTICH]: في وداع الأمل المرتقب

=== BLOCK 19: Poem 16 Explanation ===
(Component: TEMPLATE_C_SPLIT.html)
[UNIQUE_ID_1]: b31033
[COLUMN_1_TITLE]: المفردات
[COLUMN_1_CONTENT]: عاصيتها حاولت مَنْعَ نُزولها . المرتقب : اسمُ مَفْعُولٍ فِعْلُهُ : ارتقب
[UNIQUE_ID_2]: b43963
[COLUMN_2_TITLE]: الشرح
[COLUMN_2_CONTENT]: أَيَّتها الحريَّةُ لم نَنْسَ تلك الدُّمُوعَ التِي كَفَكَفْتِهَا، وحاولتِ مَنْعَ نُرُوهَا حِينَمَا سَيُطَرَ اليَاسُ عَلَيْك،ِ وتلاشى أَمَلُ النَّصْرِ والتَّحَرُرُ فِي نَفْسِكِ

=== BLOCK 20: Poem 16 Table ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: الشعور
[HEADER_2]: الأداة
[HEADER_3]: المثال
[CELL_1]: حزن
[CELL_2]: التَّراكيب
[CELL_3]: ما نسينا دمعة عاصيتها.

=== BLOCK 21: Poem 16 Irab ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b95536
Title: الإعراب
Content: عاصيتها( في محل نصب صفة الأمل : مضاف إلَيْهِ يَجْرُورٌ المرتقب : صِفَةٌ مَجْرُورَة.ٌ

=== BLOCK 22: Poem Verse 17 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b54152
[POEM_TITLE]: البيت السابع عشر
[UNIQUE_ID_BIO]: b11179
[POET_NAME]: -۱۷
[RIGHT_HEMISTICH]: رجفت بالأمس سكرى ألم
[LEFT_HEMISTICH]: فاسلها اليوم سکری طرب

=== BLOCK 23: Poem 17 Explanation & Irab ===
(Component: TEMPLATE_C_SPLIT.html)
[UNIQUE_ID_1]: b58742
[COLUMN_1_TITLE]: الشرح
[COLUMN_1_CONTENT]: ارتَعَشَتْ تِلْكَ الدَّمْعَةُ وَارْتَجَفَتْ قَبْلَ تَحْقِيقِ النَّصْرِ مِنْ شِدَّةِ الأسى والألم، أما اليومَ فَأَسَالَ تِلْكَ الدَّمْعَةَ الفَرْحُ بِتَحْقِيقِ النَّصْرِ على المستعمر
[UNIQUE_ID_2]: b75497
[COLUMN_2_TITLE]: الإعراب
[COLUMN_2_CONTENT]: سكرى حال منصوب الم، طرب : مضاف إلَيْهِ يَجْرُورٌ اليوم : مَفْعُولُ فِيهِ ظَرْفُ زَمَانٍ مَنْصُوب.َ

=== BLOCK 24: Poem Verse 18 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b98632
[POEM_TITLE]: البيت الثامن عشر
[UNIQUE_ID_BIO]: b81802
[POET_NAME]: ۱۸-
[RIGHT_HEMISTICH]: یا لنعمى خف في أظلالها
[LEFT_HEMISTICH]: ما حملنا في ركاب الحقب

=== BLOCK 25: Poem 18 Explanation ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b85955
Title: المفردات والشرح
Content: <span class="text-accent">المفردات: نعمى: النِّعْمى الرفاهِيَةُ وطيب العيش، والدعة ركاب : الركاب الإبل المركوبة، أو الحامِلَةُ شَيْئًا، أو التي يُرادُ الحَمْلُ عَلَيْهَا الحَمْع:ُ ركب، وركايب الحقب: الحِقْبَةُ مِنَ الدَّهْرِ : الْمُدَّةُ لَا وَقت لها، الجَمْعُ حِقَب وحقوب</span><br><br>الشرح ما أطيب الحياة التي بَلَغَنَاهَا بَعْدَ تَخْقِيقِ النَّصْرِ على المُسْتَعْمر؛ حيثُ صِرْنَا نَعِيش فيها بِدِعَةٍ وَرَفَاهِيَة،ٍ وخف علينا في ظلها ثقل ذلك الحمل الذي أَنهُكَ كَاهِلَنَا طَوال مُدَّةِ الاستعمار.

=== BLOCK 26: Poem 18 Irab ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b18620
Title: الإعراب
Content: خف : فعل ماض مبني على الفتح ما : اسم مَوْصُولُ فِي مَحَلِ رَفْعِ فَاعِل. (ملنا(: صِلَةُ المَوْصُولِ لا محل لها من الإعراب.

--- END STREAM ---
