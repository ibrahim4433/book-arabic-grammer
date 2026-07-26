# **SESSION 147**

[TASK DEFINITION]
Objective: Implement page 147.
File: `pages/page_147.html`
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
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
15. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 147
[CHAPTER_TITLE]: page 147
[CATEGORY_HEADER]: 147
[SECTION_HEADER]: 147
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: معاني المقاطع ===
(Component: TEMPLATE_C_BLOCK.html)
Title: معاني المقطع الثاني والثالث
Content: <span class="text-accent">معاني المقطع الثاني:</span><br>يَبْدأ الشَّاعِرُ الْمُقْطَعَ الثاني بالتأكيد على أنَّ الدَّهْر قد تغلب عليه لأَنَّهُ غالبه بالهوى، فَلَو غالبه بغيره لا نتَصَرَ عليه انتصارا ساحقًا والنَصَبَ قِبَابَهُ بِينَ الشَّهب في أعالي السماء. ولطوف فيها لاهِيَا يَرْفل برداء الانتصار، ويُلاعِبُ وجنةَ البَدْر،ِ مظهرا حياةَ التَّرَفِ وَالرَّعْدِ فَتَرْشَهُ العيد الحسان المترفات بأنواع الطيوب، وينسج من أَشِعَةِ شَمْسِ الْغُرُوبِ ثوبًا وينقش أطرافه بحبات الندى ويطرزه بالطيوب.<br><br><span class="text-accent">معاني المقطع الثالث:</span><br>إِنَّ هؤلاء الكادِحِينَ يَصْنَعُونَ لأَنفُسِهِم الأفراح والمسرات على الرغم من المعاناة والألم اللذين يحيطان بحياتهم؛ لأهُم يَحْلِّمُونَ أَحْلَامًا بسيطة متواضعَةً؛ فهم لا يَحْلُمُونَ إِلَّا بِالحُصُولِ على لُقْمَةِ عَيْشِ تُقِيتُهم وتمسك أصلاتهم.

=== BLOCK 3: مهارات الاستماع والقراءة ===
(Component: TEMPLATE_C_SPLIT.html)
Title: مهارات الاستماع والقراءة
RightContent:
<span class="text-accent font-bold">مهارات الاستماع :</span><br>استمع إلى النَّص،َ ثُمَّ أَجِب:ْ<br>- اختر الإجابة الصحيحةً فِي كُلِّ مِمَّا يأتي :<br>- يتناول النَّصُ مَوْضُوعًا : )أ- اجتماعيا، ب وطنيا، ج ذاتيا، د- قوميًّا(. ج- ذاتيا.<br>- بَدَا الشَّاعِرُ فِي النَّص:َ )أ - مُستَبْشِرًا، ب- مُنْكَسِرًا، ج- طربًا، د- مُتَمَرِّدًا( . ج- مُنْكَسِرًا .
LeftContent:
<span class="text-accent font-bold">مهارات القراءة: القِرَاءَةُ الصَّامِتَةُ :</span><br>اقرأ النَّصَّ قراءَةً صَامِتَة،ً ثُمَّ أَجِبْ :<br>۱- ما الفِكْرَةُ العَامَّةُ التِي يَدُورُ حَوْلَهَا النَّصُ؟ ج -۱ الفِكْرَةُ العامَّةُ التِي يَدُورُ حَوْلَهَا النَّصُ هي ما معاناة الشَّاعِرِ مِنْ مَشَاعِرِ الْهَوَى.<br>٢- ما مَصْدَرُ مُعاناة الشَّاعِر؟ وما الذي مَنَعَهُ مِنْ تَجاوز هَذِهِ المُعاناة؟ ٢- مَصْدَرُ مُعاناة الشاعر : إخفاق الحب وانكسار الآمال. والمانع مِنْ تجاوز هذه المُعَانَاةِ تَغَلْغُلُ الحبّ فِي قَلْبِه،ِ وَتَمَكْنُهُ منه.

=== BLOCK 4: الاستيعاب والفهم والتحليل ===
(Component: TEMPLATE_C_TABLE.html)
Title: الاستيعاب والفهم والتحليل - المستوى الفكري
Headers: الاستيعاب | الفهم والتحليل
Row 1: استعِنْ بِالمُعْجَمِ على تَعَرَّفِ مَعْنَى كَلِمَةِ )الأصيل(، في كل ما يأتي: قال نديم محمد : وَنَسَجْتُ الأَصِيلَ تَوْبًا وَنَقَشْ ت حوافيه بِالنَّدَى وَالْمَلابِ. وقال أحمد شوقي : أو دع لسانَكَ وَاللَّغَاتِ فَرُما غَنَّى الأصيل بمنطق الأجداد | ج - الأصيل عِنْدَ نَدِيم محمد : الوَقْتُ حِينَ تَصْفَرُ الشَّمْسُ لِمَغْرِها. و عِنْدَ شَوْقِي: كريمُ النَّسَب.
Row 2: كَوَنْ مُعْجَمًا لُغَوِيا لِكُلِّ مِن : )المعاناة، السعادة(، ثُمَّ حَدَدِ الْمُعْجَمَ السَّائِدَ مِنْهُما. | ج - المعاناة: )علتي، حزني، عذابي، السم، خراب(. - السَّعَادَةِ : ) النجوم، هوى، دعائي، النعيم الأطياب(. - المُعْجَمُ السَّائِد:ُ )المعاناة(.
Row 3: اذكْرِ الْفِكْرَةَ الرَّئيسةَ لِكُلِّ مِنْ مَقْطَعَي النَّصَ مُستَعِيْنَا بِالْمُعْجَمِينِ السَّابِقِين.ِ | - المقطع الأول: معاناة الشاعر بِسَبَبٍ مَشَاعِرِ الحب، وبيان آثارها على جَسَدِه.ِ - المقطع الثاني: الرَّغْبَةُ بِالتَّخَلُصِ مِنَ الْمَعَانَاةِ وَتَجَاوُزِ الألم.
Row 4: وَضِّحِ الآثار النَّفْسِيَّةَ وَالجَسَدِيَّةَ التي تركها الشُّعُورُ فِي الشَّاعِرِ كما وَرَدَ فِي المَقْطَعِ الْأَوْل.ِ | ج - الآثارُ النَّفْسِيَّةُ نَفَتَ الشَّعُورُ السم في قلبِه،ِ فَجَعَلَ مَرَضَهُ يَسْتَفْحِلُ وَيَتَفَاقَم،ُ وَجَعَلَ حُزْنَهُ يبلغ الدُّرْوَة،َ وَأَطَالَ أَمَدَ عَذَابِه.ِ الآثارُ الجَسَدِيَّة:ُ الْتَهَمُ الشُّعُورُ عُرُوقَ جَسَدِه،ِ وَأَفْزَعَ عِظَامَه،ُ وَأَنْخَلَ جَسَدَه،ُ وَخَرَّبَ جِلْدَه.ُ

=== BLOCK 5: رغبة الشاعر وتجاوز الحرمان ===
(Component: TEMPLATE_C_BLOCK.html)
Title: رغبة الشاعر وتجاوز الحرمان
Content: ه- انْتَابَتْ فِي المَقْطَعِ الثاني الشَّاعِرَ رَغْبَةٌ عَارِمَةً في تجاوز الحرمان وإنكارِ الْأَلَم وَضَحْ ذَلِك.َ
جه - عِنْدَمَا عَجَرَ الشَّاعِرُ عَنْ تَجاوز الحرْمَانِ والتغلب على الألم في الواقع لجأ إلى عالم الخيال والتأمل، فَرَسَمَ الْأَحلام التي تُشِيرُ إِلَى رَغْبَةِ جامِحَةٍ فِي التَّخَلْصِ مِنْ مُعَانَاتِه.ِ

=== BLOCK 6: ملاحظة هامة ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: ملاحظة هامة حول الظاهرة النفسية والمستوى الفني
Content: إجابة ج٦: الظَّاهِرَةُ النَّفْسِيَّةُ التِي يَطْرَحها النص هي المعاناة بِسَبَبِ مَشَاعِرِ الْحُب.ِّ
إجابة ج -۱: أفاد هذا الاستعمال في التَّعْبِيرِ عَنْ عَدَمِ القُدْرَةِ عَلَى تَجَاوُزِ الأَلَم، والتَّخَلُصِ مِنْ أَرْمَتِهِ النَّفْسِيَّة،ِ بِسَبَبِ عَدَمٍ مُغَالَبَةِ الدَّهْرِ لَهُ بِغَيْرِ الْهَوَى.

=== BLOCK 7: الامتحان ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: استنتج الظَّاهِرَةَ النَّفْسِيَّةَ التِي يَطْرَحُهَا النَّص.ُّ
Number: ٢
Question: المستوى الفني: بين وظيفة استعمالِ الشَّاعِرِ حَرْفَ الشَّرْطِ )لو( في التَّعْبِيرِ عَنْ أَرْمتِهِ النَّفْسِيَّة.ِ

--- END STREAM ---
