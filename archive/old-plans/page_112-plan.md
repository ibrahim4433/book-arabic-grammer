# **SESSION 112**

[TASK DEFINITION]
Objective: Implement page 112.
File: `pages/page_112.html`
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
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal (use .block-header.accent where appropriate).
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
15. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !

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

=== BLOCK 2: Cut Content Continuation ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
(Inner Component: TEMPLATE_C_BLOCK.html)
Title: تتمة البلاغة والإعراب (Orange Accent)
Content: أَفْرَاسُنَا فِي مَلْعَب. <br> <span class="highlight-blue">البلاغة:</span> (كَمْ نَبَتْ أَسْيَافُنَا فِي مَلْعَب،ِ كَبَتْ أَفْرَاسُنَا فِي مَلْعَبِ) : كناية عن الهزيمة <br> <span class="highlight-blue">الإعراب:</span> كَمْ خَبَرَيَّةٌ مَبْبَيَّةٌ على السكون في محل نَصْبَ مَفْعُولٌ مُطْلَق.َ

=== BLOCK 3: البيت الحادي عشر ===
(Component: TEMPLATE_C_POEM.html)
Verse 1: مِنْ نِضَالِ عَائِرٍ مُصْطَخِبِ
Verse 2: لِنِضَالِ عَائِرٍ مُصْطَخِبِ

=== BLOCK 4: شرح البيت الحادي عشر ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح
Content: <span class="highlight-blue">المفردات :</span> مصطحب : صَخِبَ الجَمْعُ صَخْبًا : عَلَتْ فيه الأصوات واختلطتْ اصطحب القَوْمُ : تصايحوا وتضاربوا <br> <span class="highlight-blue">الشرح :</span> كُنَّا نَنْتَقِلُ مِنْ مَعْرَكَةِ قاسِيَةِ طَاحِنَةِ لا توفيق فيها إلى مَعْرَكَةِ أَشَد وأَعْنَف.

=== BLOCK 5: البيت الثاني عشر ===
(Component: TEMPLATE_C_POEM.html)
Verse 1: شَرَفُ الوَثْبَةِ أَنْ تُرْضي العُلَا
Verse 2: غُلِبَ الواثِبُ أَمْ لَمْ يُغْلَ ؟!

=== BLOCK 6: شرح البيت الثاني عشر ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح والبلاغة
Content: <span class="highlight-blue">المفردات:</span> الوثبَة وثبَ يَبْبُ وَثَبًا وَنُونَا قَفَر.َ وتب على فلان: غالبه. والمقصود هنا التضال والكفاح الواتب المناضل. والوايب: اسم فاعِلِ فِعْلُهُ وَتَبَ <br> <span class="highlight-blue">الشرح :</span> يَكْفِي المَنَاضِلِ فَخْرًا وَشَرَفًا أَنْ يَكُونَ نِصَالُهُ مِنْ أَجْلِ الفَاعِ عَنِ الوَطَنِ لِبُلُوعَ الْمَجْد،ِ وَلَا يَهِم بَعْدَ ذَلِكَ أَكَانَ مُنْتَصِرًا أَمْ مَهْرُومًا. <br> <span class="highlight-blue">البلاغة:</span> (الوَثْبَةِ تُرْضِي)، (تُرْضِي العلا): استعارَةً مَكْنِيَّة.ٌ (غُلِب،َ لم يقلب) طباق سلب

=== BLOCK 7: إعراب البيت الثاني عشر ===
(Component: TEMPLATE_C_IRAB.html)
Word 1: شَرَف
Role 1: مُيْتَدَاً مَرْفُوعُ
Word 2: أَنْ تُرْضِي العلا
Role 2: الْمَصْدَرُ الْمُؤْوَّلُ فِي مَحَلَّ رَفْعِ خَبَر.َ
Word 3: (تُرْضِي)
Role 3: صِلَةُ المَوْصُولِ لا تحل لها مِنَ الإغراب
Word 4: الوائِبُ
Role 4: نَائِبُ فَاعِلِ مَرْفُوع.ٌ

=== BLOCK 8: البيت الثالث عشر ===
(Component: TEMPLATE_C_POEM.html)
Verse 1: فالِتَفِتْ مِنْ كُوَّةِ الفردوس يا
Verse 2: فيصل العلياء، وانْظُرْ وَاعْجَبِ

=== BLOCK 9: شرح البيت الثالث عشر ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح
Content: <span class="highlight-blue">المفردات:</span> كوة : الكُوَّةُ خَرْقُ في الجدار، فتحة، نافذة للتَّهْوِيَة والإضاءة. الجَمْعُ : كُوى فَيُصَل: الفَيْصَل:ُ الحاكم أو القاضي. والماضي القاطع يفصل بين الحق والباطل الجمع: فياصل <br> <span class="highlight-blue">الشرح :</span> تَلَفَتْ أَيُّهَا الشَّهِيدُ مِنْ جَنَّةِ الفِرْدوس التي تَتَرَبَّعُ على عَرْشها، وانظُرْ بِغَيْنِكَ واعْجَبْ بِمَا فَعَلْناه بالمُسْتَعْمر

=== BLOCK 10: إعراب البيت الثالث عشر ===
(Component: TEMPLATE_C_IRAB.html)
Word 1: الفردوس، العلياء
Role 1: مُضَافُ إِلَيْهِ يَجْرُور.ٌ

=== BLOCK 11: البيت الرابع عشر ===
(Component: TEMPLATE_C_POEM.html)
Verse 1: أَتَرَى كَيْفَ اشْتَفَى النَّارُ مِن ال
Verse 2: فاتح الْمُسْتَرَقِ الْمُسْتَلِبِ

=== BLOCK 12: شرح البيت الرابع عشر ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح والبلاغة
Content: <span class="highlight-blue">المفردات:</span> اشتقى مِنْ عِلَّتِهِ بَرَى وَاشْتَفَى بكذا : شَفِي بِهِ وَاشْتَفَى من عده: بلغ ما يُذْهِبُ غَيْظَهُ مِنْهُ الفَاتِحِ الْمُسْتَرِق،ِ الْمُسْتَلِب:ِ اسم فاعل والفعل على الترتيب فتح استرق، استلب <br> <span class="highlight-blue">الشرح :</span> هل ترى كيف أخذنا بثأرنا وشَفَيْنَا غِلَّنَا حِيْنَمَا جَرَّعْنَا الْمُسْتَعْمِرَ الغَاصِبَ السارق كؤوس الهزيمة. <br> <span class="highlight-blue">الفكرة:</span> تصوير هَزِيمَةِ المُسْتَعْمِ <span class="highlight-blue">الشَّعُور:</span> اعتزاز، وافتخار، وفرح <span class="highlight-blue">الأداة:</span> التراكيب <span class="highlight-blue">المثال:</span> اشْتَفَى التَّأْرُ مِنَ الفَاتِح.ِ <br> <span class="highlight-blue">البلاغة:</span> (اشْتَفَى النَّارُ) : استعارَةً مَكْنِيَّة

=== BLOCK 13: إعراب البيت الرابع عشر ===
(Component: TEMPLATE_C_IRAB.html)
Word 1: كيف
Role 1: اسم استفهام في مَحَلَ نَصْبَ مَفْعُول مُطْلَق
Word 2: المُسْترق، الْمُسْتَلِبِ
Role 2: صِفَةٌ مَجْرُورَة.ً

=== BLOCK 14: البيت الخامس عشر ===
(Component: TEMPLATE_C_POEM.html)
Verse 1: وطوى ما طال من راياته
Verse 2: في ثنايا تجمِهِ الْمُحْتَجِب؟!

=== BLOCK 15: شرح البيت الخامس عشر ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح والفكرة
Content: <span class="highlight-blue">المفردات:</span> المختجب: حَجَبَ عَنْهُ الضَّوء: سَتَرَهُ عَنْهُ والمُخْتَجِب اسم فاعل فعله: احتجب <br> <span class="highlight-blue">الشرح :</span> بَعْدَ أَنْ جَرَّعْنَا الْعَدُ الزَيْمَةَ رَاحَ يُلَمْلِمْ أعلامهُ وَيَطُويها ويخفيها في ظُلُمَةِ نَجْمِهِ الذي أَفِلَ وانطفا.ً <br> <span class="highlight-blue">الفكرة :</span> التَّعْبِيرُ عَنِ الشمالةِ بجريمة المستَعْمر <span class="highlight-blue">الشعور :</span> اعتزاز، وافتخار، وفرح <span class="highlight-blue">الأداة:</span> التراكيب <span class="highlight-blue">المثال:</span> طوى ما طال من راياته

=== BLOCK 16: إعراب البيت الخامس عشر ===
(Component: TEMPLATE_C_IRAB.html)
Word 1: ما
Role 1: اسم مَوْصُولُ فِي مُحَلَ نَصْبَ مَفْعُول بِه.ِ
Word 2: (طَالَ)
Role 2: صِلَةُ الْمَوْسُولِ لَا مَحَلَّ لها مِنَ الإعراب
Word 3: تجمه
Role 3: مُضافُ إِلَيْهِ يَجْرُورٌ
Word 4: المُحْتَجِبِ
Role 4: صِفَةٌ مَجْرُورَة.ٌ

=== BLOCK 17: البيت السادس عشر ===
(Component: TEMPLATE_C_POEM.html)
Verse 1: ما نسينا دمعة عاصيتها
Verse 2: في وداع الأمل المرتقب

=== BLOCK 18: شرح البيت السادس عشر ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح
Content: <span class="highlight-blue">المفردات:</span> عاصيتها حاولت مَنْعَ نُزولها . المرتقب : اسمُ مَفْعُولٍ فِعْلُهُ : ارتقب <br> <span class="highlight-blue">الشرح :</span> أَيَّتها الحريَّةُ لم نَنْسَ تلك الدُّمُوعَ التِي كَفَكَفْتِهَا، وحاولتِ مَنْعَ نُرُوهَا حِينَمَا سَيُطَرَ اليَاسُ عَلَيْك،ِ وتلاشى أَمَلُ النَّصْرِ والتَّحَرُرُ فِي نَفْسِكِ <span class="highlight-blue">الشعور :</span> حزن <span class="highlight-blue">الأداة :</span> التَّراكيب <span class="highlight-blue">المثال:</span> ما نسينا دمعة عاصيتها.

=== BLOCK 19: إعراب البيت السادس عشر ===
(Component: TEMPLATE_C_IRAB.html)
Word 1: (عاصيتها)
Role 1: في محل نصب صفة
Word 2: الأمل
Role 2: مضاف إلَيْهِ يَجْرُورٌ
Word 3: المرتقب
Role 3: صِفَةٌ مَجْرُورَة.ٌ

=== BLOCK 20: البيت السابع عشر ===
(Component: TEMPLATE_C_POEM.html)
Verse 1: رجفت بالأمس سكرى ألم
Verse 2: فاسلها اليوم سکری طرب

=== BLOCK 21: شرح البيت السابع عشر ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الشرح
Content: <span class="highlight-blue">الشرح :</span> ارتَعَشَتْ تِلْكَ الدَّمْعَةُ وَارْتَجَفَتْ قَبْلَ تَحْقِيقِ النَّصْرِ مِنْ شِدَّةِ الأسى والألم، أما اليومَ فَأَسَالَ تِلْكَ الدَّمْعَةَ الفَرْحُ بِتَحْقِيقِ النَّصْرِ على المستمر

=== BLOCK 22: إعراب البيت السابع عشر ===
(Component: TEMPLATE_C_IRAB.html)
Word 1: سكرى
Role 1: حال منصوب
Word 2: الم، طرب
Role 2: مضاف إلَيْهِ يَجْرُورٌ
Word 3: اليوم
Role 3: مَفْعُولُ فِيهِ ظَرْفُ زَمَانٍ مَنْصُوب.َ

=== BLOCK 23: البيت الثامن عشر ===
(Component: TEMPLATE_C_POEM.html)
Verse 1: یا لنعمى خف في أظلالها
Verse 2: ما حملنا في ركاب الحقب

=== BLOCK 24: شرح البيت الثامن عشر ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح
Content: <span class="highlight-blue">المفردات:</span> نعمى: النِّعْمى الرفاهِيَةُ وطيب العيش، والدعة ركاب : الركاب الإبل المركوبة، أو الحامِلَةُ شَيْئًا، أو التي يُرادُ الحَمْلُ عَلَيْهَا الحَمْع:ُ ركب، وركايب الحقب: الحِقْبَةُ مِنَ الدَّهْرِ : الْمُدَّةُ لَا وَقت لها، الجَمْعُ حِقَب وحقوب <br> <span class="highlight-blue">الشرح :</span> ما أطيب الحياة التي بَلَغَنَاهَا بَعْدَ تَخْقِيقِ النَّصْرِ على المُسْتَعْمر؛ حيثُ صِرْنَا نَعِيش فيها بِدِعَةٍ وَرَفَاهِيَة،ٍ وخف علينا في ظلها ثقل ذلك الحمل الذي أَنهُكَ كَاهِلَنَا طَوال مُدَّةِ الاستعمار.

=== BLOCK 25: إعراب البيت الثامن عشر ===
(Component: TEMPLATE_C_IRAB.html)
Word 1: خف
Role 1: فعل ماض مبني على الفتح
Word 2: ما
Role 2: اسم مَوْصُولُ فِي مَحَلِ رَفْعِ فَاعِل.
Word 3: (حملنا)
Role 3: صِلَةُ المَوْصُولِ لا محل لها من الإعراب.

=== BLOCK 26: Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Col 1: البيت
Col 2: الفكرة الرئيسية
Row 1: ١١ - ١٢
Row 1: الانتقال لمعركة أشد، وشرف النضال
Row 2: ١٣ - ١٥
Row 2: التلفت للفردوس، والشماتة بهزيمة المستعمر
Row 3: ١٦ - ١٨
Row 3: دمعة الحزن تتحول لفرح، والرفاهية بعد النصر

--- END STREAM ---
