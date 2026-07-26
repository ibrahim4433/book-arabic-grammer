# **SESSION 163**

[TASK DEFINITION]
Objective: Implement page 163.
File: `pages/page_163.html` (Note: Use the exact page number.)
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
    *   `class="w-20pct"`
    *   `class="mt-2mm"`
    *   `class="text-center"`
    *   `class="font-bold"`
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
[LESSON_NUMBER]: 163
[CHAPTER_TITLE]: page 163
[CATEGORY_HEADER]: 163
[SECTION_HEADER]: 163
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Cut Content Irab (Continuation) ===
(Component: TEMPLATE_CUT_BOX_PART_2.html -> TEMPLATE_C_IRAB.html)
Title: تتمة الإعراب
Word 1: فعل ماض. وابْتَعَدُ الواو، حَرْفُ عَطْفُ
Details 1: ابْتَعَد،ْ فعل ماضِ مَبْنِي على الفَتْحَةِ الظَّاهِرَة.ِ وسُكِّنَ لِلضَّرُورَةِ الشَّعْرِيَّة.ِ
Word 2: جملةٌ زَارَ(
Details 2: استئنافية، لا مُحَلَ ها مِنَ الإعراب
Word 3: جملة )مَا مِلْت:ُ
Details 3: مَعْطُوفة،ً لا محل لها مِنَ الإعراب
Word 4: جملة )تجافى(
Details 4: صِلَةُ المَوْصُول،ِ لا تحل لها مِنَ الإعراب.
Word 5: )على تَقْدِيْرٍ أَنْ الْمَصْدَرِيَّة الْمُضْمَرَةِ بَعْدَ حَتَّى( جملةُ ابْتَعَدْ(
Details 5: مَعْطُوفَة،ٌ لَا حَلَّ لَا مِنَ الإِعراب .

=== BLOCK 3: Introduction ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ملحق الأبيات الخارجية المتممة
Content: ملحق الأبيات الخارجية المتممة الواردة في ديوان الشاعر جورج صيدح:

=== BLOCK 4: Poem Verse 1 ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: فيهِ سَلْمَى، فيهِ جَنَّاتُ الهوى
Hemistich 2: فيه طير الأنس تدعو مَنْ شَرَدْ

=== BLOCK 5: Core Matrix (Vocabulary 1) ===
(Component: TEMPLATE_C_TABLE.html)
Header 1: المفردات
Header 2: المعنى
Row 1 Col 1: سرب
Row 1 Col 2: السَّرْبُ : الفريق مِنَ الطَّيْرِ
Row 2 Col 1: شَرَدْ
Row 2 Col 2: شَرَدَ عَنِ الطَّريق: حاد

=== BLOCK 6: Analysis Verse 1 ===
(Component: TEMPLATE_C_SPLIT.html)
Column 1 Title: الشرح والبلاغة
Column 1 Content: <span class="text-accent">الشرح:</span> تركت في وطَنِي مَحْبُوبَتِي سَلَّمَى والأماكِنَ الجَمِيلَةَ التي جمعني بها، وخَلَّقْتُ فِيهِ الطُّيُورَ التي تَدْعُونِي لِلْعَوْدَةِ إِلَيهِ. <br><br><span class="text-accent">البلاغة:</span> )طير الأنس تدعو(: استعارة مكنية.
Column 2 Title: الإعراب
Column 2 Content: سلمى، جَنَّات،ُ طير: مُبْتَداً مرفوع. الهوى، الأنس: مضاف إليه مجرورٌ. مَنْ : اسم مَوْصُول فِي مَحَلِّ نَصْبِ مَفْعُولَ بِه.ِ )شَرَدَ( : صِلَةُ الْمَوْصُولِ لا محل لها من الإعراب.

=== BLOCK 7: Poem Verse 2 ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: جَعَلَ البُرْهَةَ مِنْ أَعْمارنا
Hemistich 2: لتلاقينا، وللبَيْنِ الْأَبَد

=== BLOCK 8: Analysis Verse 2 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تحليل البيت
Content: <span class="text-accent">المفردات:</span> البُرْهَةُ المُدَّةُ مِنَ الزَّمَنِ الجَمْع:ُ بُرَه. البين البعد والانفصال. <br><span class="text-accent">الشرح:</span> جَعَلَ الدَّهْرُ أَيَّامًا قَلِيلَةً مِنْ أَعْمَارِنَا لِلقَائِنَا، وَجَعَلَ الْبُعْدَ والانفصال مُسَيْطِرين على ما تبقى منها. <br><span class="text-accent">البلاغة:</span> )تلاقينا، البين(: طباق إيجاب.

=== BLOCK 9: Poem Verse 3 ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: ضاعت النجوى وخَابَتْ كُتُبِي
Hemistich 2: لا وَيْحَ قَلْبٍ ذَابَ مِنْ قلب صلد

=== BLOCK 10: Warning Box (Analysis Verse 3) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: تحليل البيت
Content: <span class="text-accent">المفردات:</span> النجوى: إسرار الحديث. الصَّلد: صَلَدَ صَلَّدًا وصُلُودًا : صَلُبَ. الصَّلْدُ : الصَّلْب.ُ وصلد : صِفَةٌ مُشَبَّهَةٌ باسم الفاعل. <br><span class="text-accent">الشرح:</span> بَعْدَ هِجْرَتي وابتعادي عَنْ مَحْبُوبَتِي سَلْمَى لم تعد اللقاءات التي اتجاذب فيهَا أَطْرَافَ الحَدِيثِ مَعَهَا مُتاحة، والرسائل التِي أَرْسَلْتُهَا إِلَيْهَا لَم تُجْدِ نَفْعًا، فَوَيْلٌ لِقَلْبِي الذي ذَابَ حُبًا بِقَلْبِ سَلْمَى القاسي. <br><span class="text-accent">الفكرة:</span> تَصْوِيرُ قَسْوَةِ قَلْبِ الْمَحْبُوبَة. <br><span class="text-accent">الشُّعور:</span> خَيْبَةُ أَمَل. <br><span class="text-accent">الأداة:</span> التراكيب. <span class="text-accent">المثال:</span> خَابَتْ كُتُبِي. <br><span class="text-accent">الإعراب:</span> النجوى، كتبي : فاعل مرفوع. وَيْحَ: مَفْعُول مُطْلَقَ مَنْصُوبٌ. )ذَابَ(: في محل جَرِّ صِفَة. صلد: صفة مجرورة.

=== BLOCK 11: Poem Verse 4 ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: عَقَتْ ثُمَّ سَلَتْ ثُمَّ قَسَتْ
Hemistich 2: وَجَنَتْ ما ليس يَجْنِيهِ أَحَدٌ

=== BLOCK 12: Analysis Verse 4 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تحليل البيت
Content: <span class="text-accent">المفردات:</span> سَلَت:ْ نَسِيَتْ. <br><span class="text-accent">الشرح:</span> أَحَبَّتْنِي سَلْمَى، وَبَعْدَ ذَلِكَ نَسِيَتْنِي وَتَنَكُرَتْ لِي وَقَسَّتْ قَلْبَها علي، وارتكَبَتْ مَعِي ما لا يُرْتَكَب. <br><span class="text-accent">الفِكْرة:</span> تَصْوِيرُ قَسْوَةِ المَخْبُوبَةِ على الشاعر. <br><span class="text-accent">البلاغة:</span> )جَنَت،ْ ليس يجنيه(: طباق سلب. <br><span class="text-accent">الإعراب:</span> ما : اسم مَوْصُول فِي مَحَلَّ نَصْبَ مَفْعُول به. ليس : حَرْفُ نَفي. )ليسَ يَجْنِيهِ أَحَد(: صلة الموصول لا محل لها من الإعراب.

=== BLOCK 13: Poem Verse 5 ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: أَتُرَى طَيْفُ سُليمي مثلها؟
Hemistich 2: كلما رَقَّ لَهُ القَلْب استبد

=== BLOCK 14: Tip Box (Analysis Verse 5) ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Title: تحليل البيت
Content: <span class="text-accent">المفردات:</span> طَيْفُ : الطَّيْفُ الخيالُ الطَّائِف،ُ وهو ما يَرَاهُ النَّائِمُ. <br><span class="text-accent">الشرح:</span> أ يكونُ طَيْفُ سَلْمَى قاسيا مثلها، كلما تَلَطَّفَ بِهِ قَلْبِي وَرَقَّ لَهُ ازداد ظلما وتَعَسُّفًا. <br><span class="text-accent">البلاغة:</span> )استبد الطيف(: استعارة مكنية. <br><span class="text-accent">الإعراب:</span> )رَقَّ لَهُ القَلْبُ( في مَحَلِّ جَرٍّ بالإضافة. )استبد(: جُمْلَةُ جواب الشَّرْطِ لا مَحَلَّ لَهَا مِنَ الإعراب.

=== BLOCK 15: Poem Verse 6 ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: زَادَ تَعْذيبي كَأَنْ لَمْ يَكْفِنِي
Hemistich 2: أنت والدَّهْرُ وَأَجْلَافُ البَلَدْ

=== BLOCK 16: Analysis Verse 6 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تحليل البيت
Content: <span class="text-accent">المفردات:</span> أَجْلَاف: الجلف الغليظ الأحمق. <br><span class="text-accent">الشرح:</span> ازدادت معاناتي وتَعَدَّدَتْ مَصَادِرُها، فقد جلب لي هذه المعاناةُ أَنْتِ أَيَّتُهَا الْمَحْبُوبَة،ٌ وكذلك الزَّمان، وأسهم في تفاقم هذه المعاناة الحَمْقَى الَّذِينَ صَادَفْتُهُم فِي بلاد الغُرْبَةِ. <br><span class="text-accent">الفكرة:</span> الإشارة إلى أسباب معاناةِ الشَّاعِرِ فِي الْمَهْجَر. <br><span class="text-accent">الشعور:</span> ألم. <br><span class="text-accent">الأداة:</span> التراكيب. <span class="text-accent">المثال:</span> زَادَ تعذيبي.

=== BLOCK 17: Poem Verse 7 ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: وَطَنِي طَوَّحْتَ بِي فِي مَهْجَرٍ
Hemistich 2: يُرْهِقُ الحر بأنواع النكد

=== BLOCK 18: Analysis Verse 7 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تحليل البيت
Content: <span class="text-accent">المفردات:</span> طَوَّحْتَ: طَوَّحَ بِهِ بَعِيدًا : أَلْقَاهُ بَعِيدًا. طَوَّحَ بِصَاحِبِه،ِ أو طَوَّحَهُ حَمَلَهُ على ركوب المهالِكِ والأَهْوال. يُرْهِقُ : أَرْهَقَ فَلَانًا حَمَلَهُ على ما لا يُطيق. أَرْهَقَنَا السَّهَرُ : أَتْعَبَنَا. مَهْجَر: اسم مكان. الحر: صِفَةٌ مُشَبَّهَةٌ باسم الفاعل. <br><span class="text-accent">الشرح:</span> أَلْقَيْتَ بِي بَعِيدًا أَيُّهَا الوَطَنُ الْحَبِيْب،ُ وَدَفَعْتَني دَفْعًا إلى العيش في ذَلِكَ المَهْجَرِ الذي يُتْعِبُ مَنْ يأبى الذل والهوان، ويُلْحِق به ما لا يُطِيقُ مِنْ أَصْنافِ التَّعَاسَةِ التي تُكَدِّرُ صَفْوَ عَيْشِهِ وَتُنَقِّصُه.ُ <br><span class="text-accent">الفكرة:</span> تصوير معاناة الشاعر في المهجر. <br><span class="text-accent">الشعور:</span> ألم. <br><span class="text-accent">الأداة:</span> التراكيب. <span class="text-accent">المثال:</span> يُرْهِقُ الحُرَّ بأنواع النكد. <br><span class="text-accent">الإعراب:</span> )يرهق( : فِي مَحَلِّ جَرِّ صِفَة.

=== BLOCK 19: Poem Verse 8 ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: يخفض العالي مِنَ المَالِ خَلَا
Hemistich 2: وَيُقِيمُ الْمَالُ فِيهِ مَنْ قَعَدْ

=== BLOCK 20: Analysis Verse 8 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تحليل البيت
Content: <span class="text-accent">المفردات:</span> يقيم: يَنْهَضُ. <br><span class="text-accent">الشرح:</span> المَهْجَرُ يُقَلِّلُ مِنْ شَأْنِ عالي القَدْرِ بِسَبَبِ فَقْرِه،ِ وَيَرْفَعُ مِنْ شَأْنِ وَضِيعِ الْمَنْزِلَةِ بِسَبَبِ غِناه. <br><span class="text-accent">الفكرة:</span> مِعيار التفاضل بينَ النَّاسِ فِي الْمَهْجَر مادي. <br><span class="text-accent">الشعور:</span> نقمة، وسخط، وغَضَب.ُ <br><span class="text-accent">الأداة:</span> التراكيب. <span class="text-accent">المثال:</span> يخفض العالي مِنَ الْمَالِ خَلَا. <br><span class="text-accent">البلاغة:</span> )يخفض العالي، يُقِيمُ المَالُ مَنْ قَعَد(: مقابلة. <br><span class="text-accent">الإعراب:</span> العالي : مَفْعُولُ بِهِ مَنْصُوبُ . )خَلَا(: فِي مَحَلِّ نَصب حال. من: اسم مَوْصُول فِي مَحَلِّ نَصْبِ مَفْعُول بِه.ِ )قَعَد(: صِلَةُ الموصول لا محل لها من الإعراب.

=== BLOCK 21: Cut Content (Start) ===
(Component: TEMPLATE_CUT_BOX_PART_1.html -> TEMPLATE_C_BLOCK.html)
Title: تتمة النص
Content: - - ضاق

--- END STREAM ---
