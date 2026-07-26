# **SESSION 146**

[TASK DEFINITION]
Objective: Implement page 146.
File: `pages/page_146.html` (Note: Use the exact page number.)
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
[LESSON_NUMBER]: 146
[CHAPTER_TITLE]: page 146
[CATEGORY_HEADER]: 146
[SECTION_HEADER]: 146
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Poem Block ===
(Component: TEMPLATE_C_POEM.html)
Poet Name: أ. نديم محمد
Bio: شاعر سُوري، ولِدَ في قرية (عين شقاق) بمحافظة اللاذِقِيَّة، وتَمَيَّزَ مِنْ أبناء جِيْلِهِ بِطْفُولَةٍ قَلِقَةٍ مُشَاكِسَة،ٍ ولكنه كان أليفا صافيًا صفاء الطبيعة التي احْتَضَنَتْهُ بِأَبُوَّةِ وحنانٍ. تَعَلَّمَ القراءة والقرآن في القرية على يَدِ شَيْخ الكتاب، ثُمَّ أُرْسِلَ إلى بانياس لِيتَعَلَّمَ قواعد اللغة العربية، ومنها إلى مدرسة (الفرير) في اللاذقية. وفي عام ١٩٢٦م أُرْسِلَ إِلَى مَدْرَسَةِ اللابيك في بيروت، ومنها إلى فرنسا لإتمام الدراسة في جامِعَةِ مُونبلييه، حَصَلَ على الإجازة في الأَدَبِ العَرَبِي،ِّ ثُمَّ انْتَقَلَ إلى سويسرا لدراسة الحقوق، ولَكِنَّهُ عاد عام ١٩٣٠م لأسبابِ خَاصَّةٍ مِنْ دُونِ أَنْ يُكْمِلَ دِرَاسَتَه.ُ اتَّسَمَ بِحِسِهِ الْمُرْهَفِ وَمُعَانَاتِهِ الذَّاتِيَّةِ العَمِيقَةِ. لَهُ عِدَّةُ مَجْمُوعَاتٍ مِنْهَا: (فراشات وعناكِب)، (فُرُوعَ مِنْ أُصُولِ)، ومَجْمُوعَةُ (آلام) التي أُخِذَ مِنْها هَذَا النَّص.ُ
Title: يا شُعُورِي
Verse 1 Hemistich 1: يا شُعُورِي يَا حَيَّةٌ تَنْفُثُ السُّمْ
Verse 1 Hemistich 2: مِنْ أَلْفِ نَابِ فَيَجْرِي فِي القَلْبِ
Verse 2 Hemistich 1: كبرت فِيكَ عِلْتِي وَتَنَاهَى
Verse 2 Hemistich 2: فيك حزني، وطالَ فِيكَ عَذَابِي
Verse 3 Hemistich 1: أَيُّ عِرْقٍ لَمْ تَلْتَهِمْه،ُ وَعَظْمِ
Verse 3 Hemistich 2: لَم تَرْعُهُ بِعَاصِف أو شهاب؟
Verse 4 Hemistich 1: شهد الحُبُّ مَا تَرَكْتَ لِأَثْوابِي
Verse 4 Hemistich 2: مِنَ الجِسْمِ غَيْرَ جِلْدٍ خَرَابِ
Verse 5 Hemistich 1: لو بغير الهوى يُطَاوِلني الدَّهْرُ
Verse 5 Hemistich 2: لأَرْكَزْتُ فِي النُّجُومِ قِبَابِي
Verse 6 Hemistich 1: وَجَرَّرْتُ بُرْدَ لَهْوِي على البَدْرِ
Verse 6 Hemistich 2: ولَطَّمْتُ خَدَّهُ بِدُعابي
Verse 7 Hemistich 1: وَلَطَوَّفْتُ بِالنَّعِيمِ فَرَشَّتْنِي
Verse 7 Hemistich 2: حِسَانُ النَّعِيم بالأطياب
Verse 8 Hemistich 1: وَنَسَجْتُ الأَصِيلَ ثَوْبًا وَنَقَشْتُ
Verse 8 Hemistich 2: حوافِيهِ بِالنَّدى والملاب

=== BLOCK 3: Introduction to Text ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مدخل إلى النص:
Classes: `block-header` (Teal)
Content: دَأَبَ الرومانسيون على تمجيد الألم، بوصفه باعثاً على الكتابة والتوهج الإبداعي، لِذَلِكَ نَرَاهُم يُعْطُونَ قِيادَ نُفُوسِهِمْ لِلشَّعُور،ِ فَتَنْسَابُ أَسْعَارُهُم مُبَلَّلَةً بالدموع، متوجة بالآهات والأحزان والشكوى، مُستَبْطِنَةً خَزَائِنَ اللَّاشُعُور،ِ كَاشِفَةً عَمَّا تَوَارَى فيها مِنْ حُبّ مُخْفِق،ِ وآمال مُنْكَسِرَة،ِ وأمنياتٍ خَائِبَة،ٍ وهذا ما سَعَى الشَّاعِرُ إلى بَثِّهِ في تضاعِيفِ هَذِهِ الْأَبِيَات.ِ

=== BLOCK 4: Vocabulary ===
(Component: TEMPLATE_C_TABLE.html)
Title: شرح المفردات الصعبة بحسب ورودها في النص:
Header Row: الكلمة | معناها
Row 1: شهاب | الشَّعْلَةُ السَّاطِعَةُ مِنَ النَّارِ.
Row 2: يُطاولني | يُغَالِبُني
Row 3: أرْكَزْتُ | ثَبَّتُ
Row 4: دُعابي | المداعَبَةُ والملاعبة
Row 5: الملاب | ضَرْبٌ مِنَ الطِيبِ
Row 6: تَرْعَهُ | تُفْزِعُهُ وَتُخِيفُهُ
Row 7: الأصيل | الوَقْتُ حِينَ تَصْفَرُ الشَّمْسُ لِمَغْرِيهَا.

=== BLOCK 5: Meaning of the Text ===
(Component: TEMPLATE_C_BLOCK.html)
Title: معاني النص - معاني المقطع الأول:
Classes: `block-header accent` (Orange for color balance)
Content: <p class="text-accent text-justify">يَبْدأ الشَّاعِرُ المَقْطَعَ الأَوَّلَ بنداءِ شُعُوره، ونَعْتِهِ بِالحَيَّةِ التِي تَنْفُثُ السَّم،َّ امتلكت ألف ناب يضُخُ فِي قَلْبِهِ بِغَزارة وكثافة، وكأنها السبب في تفاقم مرضه واستفحاله، فيؤكد أن شعوره قد جعل حزنه يبلغ الذروة، وجعل عذابه يمتد ويَطُول.ُ ثم لا يلبث أن يتوجه إلى شُعُورِه،ِ مَرَّةً أُخْرَى ليسأَلَهُ سُؤال العارِفِ المُسْتَنْكِر،ِ فيؤكد له من خلال هذا السؤال أنه لم يُبْقِ فِي جَسَدِهِ عِرْقًا سَلِيمًا ناجيا مِنْ أَذَاه،ُ ولا عَظْمًا مُطْمَئِنَّا لَم يُفْزِعْهُ بِعَصْفِهِ وَيُخِفْهُ بِلَهِيبٍ شِهَابِه،ِ ويُنْهِي الشَّاعِرُ هذا المَقْطَعَ بِالتَّأْكِيدِ على أنَّ الْحُبَّ يَشْهَدُ أَنَّ شُعُورَهُ لَمْ يَتْرَكَ لَهُ جِسْمَا سَلِيمًا مُعافى، إِذْ لم يترك للثياب التي يَرْتَدِيهَا إِلَّا جِلْدًا شَاحِبًا خَرِبًا.</p>

--- END STREAM ---
