# **SESSION 165**

[TASK DEFINITION]
Objective: Implement page 165.
File: `pages/page_165.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`.
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md` to identify the correct template to use for the continuation.
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
8. **Self-Correction:** Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files. If it fails, you MUST fix the errors.
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
[LESSON_NUMBER]: 165
[CHAPTER_TITLE]: page 165
[CATEGORY_HEADER]: 165
[SECTION_HEADER]: 165
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Poem ===
(Component: TEMPLATE_C_POEM.html)
Title: المهاجر
Poet: نسيب عريضة
Verse 1 Right: - أحاضرٌ أَنَّتَ أَمْ بَادٍ أَمُهْتَجِرٌ
Verse 1 Left: في الغرب؟ أو هاتم فِي بِيْدِ فَحْطَانِ؟
Verse 2 Right: أَكُلَّمَا هَيَّتِ الأَرْيَاحُ حَافِقَةً
Verse 2 Left: تجُرُّ فِي ذَيْلِهَا أَنْفَاسَ رَيْحَانِ
Verse 3 Right: - حَسِبْتَهَا نَسَمَاتِ الشَّيْحِ فَانْطَلَقَتْ
Verse 3 Left: مِنْ أَسْرِهَا زَفَرَاتُ العاجز الواني
Verse 4 Right: - وليس يرويكَ إِلَّا نَلَةً بَعْدَتْ
Verse 4 Left: مِنْ مَاءٍ دِجْلَةَ أو سَلْسَالِ لُبْنَانِ
Verse 5 Right: ه وحُلْمُ يَوْمِكَ في الميماس محتفل
Verse 5 Left: بالغيدِ والصيد في أَعْرَاسِ نُدمان
Verse 6 Right: - مَنْ أَنْتَ؟ ما أَنْتَ؟ قد وَزَعْتَ رُوْحَكَ فِي
Verse 6 Left: عَهْدَيْنِ مِنْ شَاسِع ماض ومن داني
Verse 7 Right: أنا الْمُهَاجِرُ ذُو نَفْسَينِ وَاحِدَةً
Verse 7 Left: تسير سيري، وأُخْرَى رَهْنُ أَوْطَانِي
Verse 8 Right: بَعُدْتُ عنها أَجُوبُ الأَرْضَ تَقْذِفُنِي
Verse 8 Left: مُنَى حَتَقْتُ لها ركبي وأظعاني
Verse 9 Right: - ما إِنْ أُبالي مُقَامِي فِي مَغَارِها
Verse 9 Left: وفِي مَشَارِقها حتي وإيماني
Verse 10 Right: -۱۰ صَحْبِي دَعُوا النَّسَمَاتِ الْمُيْسَ تَلْمِسُنِي
Verse 10 Left: فَقَدْ عَرَقْتُ بِمَا أَنْفَاسَ كُثْبَانِي
Verse 11 Right: -۱۱ تدفقي يا رياحَ الشَّرْقِ هَائِجَةً
Verse 11 Left: فَأَنْتِ لَا شَكَ مِنْ أَهْلِي وَإِخْوَانِي
Verse 12 Right: ۱۲- هَزَزْتِ أَغْصَانَ قَلْبِي بَعْدَمَا خَلَعَتْ
Verse 12 Left: تَوْبَ الرَّبِيعِ فَمَا سَتْ رَقْصَ نَشْوانِ
Verse 13 Right: -۱۳ كَسَويهَا وَرَقَ الأَشْواقِ فَازْدَهَرَتْ
Verse 13 Left: خضراء يَعْبَقُ مِنْهَا رَوْحُ نَيْسَانِ

=== BLOCK 3: Bio ===
(Component: TEMPLATE_C_POEM.html)
Title: مدخل إلى النص:
Content: لَمْ تَسْتَطِعِ الْهِجْرَةُ أَنْ تَنْتَزِعَ الشَّاعِرَ مِنْ وَطَنِهِ الأُم،ْ لَكِنَّهَا شَطَرَتْهُ نِصْقِين،َ وَوَزَعَتْهُ بِينَ حاضِرٍ يُنْهِكَ جَسَدَه،ُ وماضِ تَحَوَّلَ إلى ذكريات تقضُ مَضْجَعَه،ُ ولَوْعَتُهُ نَدَمًا على الرَّحِيل،ِ ولَكِنَّ الفَرَحَ أَخيرًا يَنْسَرِبُ إِلَيهِ فَيُضِيء نَفْسَه،ُ فَتَقُصُ مُرَحِبَةً بِرياحِ قَادِمَةٍ مِنَ الشَّرْقِ حَيْثُ الفردوس الآسر.

=== BLOCK 4: Listening Skills ===
(Component: TEMPLATE_C_TABLE.html)
Title: مهارات الاستماع :
Row 1 Col 1: - بَدًا الشَّاعِرُ فِي النَّصَ السَّابِق:ِ )مُتَنَاسِيا الآلام - مُكْتَوبًا بِنَارٍ شَوْقِهِ - مُنْدَمِجا مَعَ وَاقِعِ الغُرْبَةِ(.
Row 1 Col 2: ج -۱ مُكْتَوبًا بِنَارِ شَوْقِه.ِ
Row 2 Col 1: - عَجْزَتِ الغُرْبَةُ فِي النَّصَ عَنْ : )أ - تَخْبِيبِ أَمَلِ الشَّاعِرِ فِي تَحقيق مطالبه ب - زرع الانكِسَارِ وَالحَيْبَةِ فِي نَفْسِه.ِ ج- انْتِرَاعِ التَّلَهُفِ والحَسْرَةِ مِنْ قَلْبِه،ِ
Row 2 Col 2: ج -۲ ج- انتزاع التَّلَغْفِ وَالْحَسْرَةِ مِنْ قَلْبِه.ِ

=== BLOCK 5: Reading Skills ===
(Component: TEMPLATE_C_LIST.html)
Title: * القِرَاءَةُ الصَّامِعَة:ُ
Item 1: - ما الذي حَمَلَهُ الشَّاعِرُ مِنْ وَطَنِه،ِ وَظَلَ حَاضِرًا فِي ذَاكِرِتِهِ؟ ج - اخْتَزَنَ الشَّاعِرُ فِي ذاكرتِهِ مَا أَلِقَهُ فِي وَطَيْه،ِ فَقَدْ حَمَلَ فِي ذاكرتِهِ رائِحَةَ الريحان والشيح وعُذُوبةَ مِيَاهِ دِجَلَةَ ومياه لبنان، وذكرياته في حي الميماس الحمصي.....
Item 2: - ما الذي أَثَارَ مَشَاعِرَ الشَّوْقِ فِي نَفْسِ الشاعِرِ ؟ ج ۲ - النسماتُ القَادِمَةُ مِنْ قِبَلِ الشَّرْق،ِ مِنْ جِهَةٍ وَطَنِه.ِ

=== BLOCK 6: Cut Box Part 1 ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
Title: الاستيعاب والفهم والتحليل:
Content: ☑ المستوى الفكري:

--- END STREAM ---
