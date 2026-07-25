# **SESSION 155**

[TASK DEFINITION]
Objective: Implement page 155.
File: `pages/page_155.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`.
2.6 Cut Content Determinism: Scan the raw text for the preceding keyword to determine the active template and apply the correct `_PART_2.html` wrapping.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide: NO INLINE STYLES. Irab Words inside `.irab-word` MUST be white.
7. Templates: Map all content using "Jules-workspace/Templates/" components. Replace any `<section>` tags from the templates with `<div>` tags (keep `<header>`).
8. Unique IDs: All content blocks must have a unique ID (id='bXXXXX') applied to the `<div>` tag that replaced the `<section>` tag. Use "Jules-workspace/id_manager.py".
9. Self-Correction: Run "Jules-workspace/lint_pages.py --one-page-mode <filename>".
10. Do not summarize examples. Do not provide uncompleted text content using (...).
11. You must preserve the exact Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense.
13. balanced page colors between teal and orange: minimum 1 element in orange.
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`).
15. Exam section always be in the end of the lesson (without the answers!). Strict Typographer Rule overrides this if no exam questions exist.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 155
[CHAPTER_TITLE]: page 155
[CATEGORY_HEADER]: 155
[SECTION_HEADER]: 155
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: حياة الشاعر (تتمة) ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
Title: حياة الشاعر
Content:
- ولِدَ فِي دِمَشْق،َ وَانْتَقَلَ إِلَى لُبْنَانَ طالبًا، ثُمَّ ارتحل إلى مصر، ومنها إلى أوربا، ثم إلى فنزويلا، واستقر في الجنوبي )الأرجنتين( فَاسْتَحَقِّ لَقَبَ )الشاعر الرَّحَالة(.

=== BLOCK 3: المؤلفات ===
(Component: TEMPLATE_C_TABLE.html)
Title: لَهُ مَجْمُوعَةٌ مِنَ المُؤَلَّفَات،ِ منها :
Headers: المؤلف | ملاحظات
Row 1: أَدَبُنا وأدباؤنا في المهاجر الأمريكية( | -
Row 2: ديوان: )نَبَضَات( | -
Row 3: ديوان )النوافل(. | -

=== BLOCK 4: ملاحظة هامة ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: رَصَدَ رَيْعَهُ لِلجَانِ الدفاع عَنْ فِلِسْطِين،َ وَمِنْهُ نَصُنَا الْمُخْتَار.ُ

=== BLOCK 5: القصيدة ===
(Component: TEMPLATE_C_POEM.html)
Title: وطني
Poet: جورج صيدح
Hemistich 1 Right: - وَطَنِي أَيْنَ أَنَا مِمَّنْ أَهْوَى ؟
Hemistich 1 Left: أَوَ مَا لِلْحَظِّ بَعْدَ الجَزْرِ مَدْ؟
Hemistich 2 Right: - ما رَسَتْ حَيْثُ رَسَتْ فُلْكُ النَّوى
Hemistich 2 Left: لو أباحوا لِي فِي الدَّفَّةِ يَدْ!
Hemistich 3 Right: غابَ خَلْفَ البَحْرِ عَنِّي شَاطِئٌ
Hemistich 3 Left: كل ما أَرَّقَنِي فِيهِ رَقَدْ
Hemistich 4 Right: - فيهِ رَبْعِي، فيهِ جَنَّاتٌ جَرَتْ
Hemistich 4 Left: تَحْتَهَا الأَنْهَارُ والرِّزْقُ جَمَدْ
Hemistich 5 Right: - فيهِ مُرُ العَيْشِ يَحْلُو وأَرَى
Hemistich 5 Left: في سواهُ زُبْدَةَ العَيْشِ زَبَدْ
Hemistich 6 Right: وطني، ما زِلْتُ أَدْعُوكَ أَبِي
Hemistich 6 Left: وجراح اليُتْمِ فِي قَلْبِ الوَلَدْ
Hemistich 7 Right: - ما رَضِيتُ البَيْنَ لولا شِدَّةٌ
Hemistich 7 Left: وَجَدَتْنِي سَاعَةَ البَيْنِ أَشَدْ
Hemistich 8 Right: - فَتَجَشَمْتُ العَنَا نَحْوَ الْمُنَى
Hemistich 8 Left: وتقاضاني الغِنَى عُمْرًا نَفَدْ
Hemistich 9 Right: - هَلْ دَرَى الدَّهْرُ الذي فَرَّقَنَا
Hemistich 9 Left: أَنَّهُ فَرَّقَ رُوْحًا عَنْ جَسَدْ ؟
Hemistich 10 Right: -١٠ وطني حَتَّامَ تَرْتَدُ الصَّبَا
Hemistich 10 Left: دُونَ أَنْ تَحْمِلَ مِنْ سَلْمَايَ رَدْ؟
Hemistich 11 Right: -۱۱ قسما لولا أَنِيْنِي ما اهْتَدَى
Hemistich 11 Left: لِسَرِيرِي طَيْفُهَا لَمَّا وَفَدْ
Hemistich 12 Right: -١٢ زَارَ إِلْمَامًا فَمَا مِلْتُ إِلى
Hemistich 12 Left: ضَمِّهِ حَتَّى تَجَافَى وَابْتَعَدْ

=== BLOCK 6: مدخل إلى النص ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مدخل إلى النص:
Content:
- غَادَرَ الشَّاعِرُ جورج صَيْدَحٍ وَطَنَهُ وَتَرَكَ خَلْفَ الشَّوَاطِي بَيْتَهُ وَأَهْلَهُ وَصَحْبَه،ُ فَأَمَّ جَاهِلَ الغُرْبَة،ِ وَلَمْ يَكُنْ يدري أَيَّ وحْشَةٍ سَتَلْقَاهُ بها الأَمْكِنَةُ الجديدة، وأي عالم غريب سَتُفْتَحْ أَبوابُهُ لِيَخْلَهُ الْمُغَرب، وَتَبْدَارِحْلَتُهُ القاسية حيث الحياةٌ لَا تُشْبِهُ فِي وَجْهِ مِنْ وُجُوهِهَا مَا أَلِفَهُ وَخَبِرَهُ فِي بِلادِه.ِ
- تَعَمَّقَ الشَّعُورُ بِالغُرْبَةِ المَكَانِيَّة،ِ حيثُ أَلْفَى نَفْسَهُ أَمَامَ مَكَانٍ قَاتَ مُظْلِمِ تَعْصِفُ فيهِ الرِّيَاحُ وَتَغْمُرُهُ الظَّلْمَة،ُ فَلَمْ يَجِدْ مَفَرًا مِنْ فَتْحِ نَوَافِذِ الدَّاكِرَةِ لِيرِمِي نَفْسَهُ فِي أكنافِ جَنَّتِهِ الْمَفْقُودَةِ حِيثُ يَنفَتِحُ المكان على الأُلْفَةِ وَالجَمَالِ والمُنْعَة.ِ

=== BLOCK 7: مهارات الاستماع ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
Title: مهارات الاستماع
Content: مهارات الاستماع :

--- END STREAM ---
