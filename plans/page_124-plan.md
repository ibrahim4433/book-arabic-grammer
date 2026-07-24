# **SESSION 124**

[TASK DEFINITION]
Objective: Implement page 124.
File: `pages/page_124.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. Verify with `verify_layout.py` or equivalent tools.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`.
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md` to identify the correct template to use for the continuation. You are forbidden from guessing.
3. Text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice. (The Typo Exception is applied for obvious OCR errors).
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`, `.highlight-green` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide: NO INLINE STYLES. Irab Words inside `.irab-word` MUST be white. Replace `<section>` tags from the templates with `<div>` tags (keep `<header>`). Apply `id='bXXXXX'` to replacement `<div>`.
7. Unique IDs: All content blocks must have a unique ID.
8. Self-Correction: Run `lint_pages.py --one-page-mode <filename>` after creating html files.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...).
11. You must preserve the exact Tashkeel provided in the input and add any missing Tashkeel needed.
12. Visual Density: The page must be dense.
13. Balanced page colors between teal and orange: make sure every page have minimum 1 element in orange.
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html`.
15. Exam section always be in the end of the lesson (in the final page of that lesson), and without the answers! No exam is included here as it does not exist in the raw text.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 124
[CHAPTER_TITLE]: page 124
[CATEGORY_HEADER]: 124
[SECTION_HEADER]: 124
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Cut Content Part 2 (Sentence Irab Continuation) ===
(Component: TEMPLATE_CUT_BOX_PART_2.html wrapping TEMPLATE_C_IRAB.html)
Title: إعراب الجمل (تتمة)
- جُمْلَةُ (مُمَزَّقَةَ الثِّيَابِ): مَعْطُوفَةٌ، لا مَحَلَّ لها مِنَ الإعرابِ.
- جُمْلَةُ (كَانَتْ مُمَزَّقَةَ الثِّيَابِ): خَبَرَيَّةٌ، مَحَلُّهَا الرَّفْعُ.
- جُمْلَةُ (صَارَتْ يَتِيْمةً): صِلَةُ الْمَوْصُولِ، لَا مَحَلَّ لَهَا مِنَ الإعرابِ.
- جُمْلَةُ (طَارَ عِطْرُ الياسمين): مَعْطُوفَةٌ، مَحَلُّهَا الرَّفْعُ.

=== BLOCK 3: Detailed Irab (Words) ===
(Component: TEMPLATE_C_BLOCK.html wrapping TEMPLATE_C_IRAB.html)
Title: إعْرابُ المَقْطَعِ الرابع:
- والصَّمْتُ: الواو: حَرْفُ استئنافٍ. الصَّمْتُ: مُبْتَدَأٌ مَرْفُوعٌ.
- مَرَّةً: نَائِبُ مَفْعُولٍ مُطْلَقٍ مَنْصُوبٌ.
- أُخْرَى: صِفَةٌ مَنْصُوبَةٌ، وعلامَةُ نَصْبِهَا الفَتْحَةُ الْمُقَدَّرَةُ على الأَلِفِ، مَنَعَ ظُهُورَهَا التَّعَذُّرُ.
- عَادَ: فِعْلٌ مَاضٍ ناقصٌ، مَبْنِيٌّ على الفَتْحَةِ الظَّاهِرَةِ.
- النَّهْرُ: اسمُ (عادَ) مَرْفُوعٌ.
- ولم يَعْرِفْ: الواو: حَرْفُ عَطْفٍ. لم: حَرْفٌ جازمٌ. يَعْرِفْ: فعلٌ مُضَارِعٌ مجزومٌ، وعلامَةُ جَزْمِهِ السُّكُونُ.
- أَحَدٌ: فاعِلٌ مَرْفُوعٌ، وعلامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ. وسُكِّنَ لِلضَّرورةِ الشِّعْرِيَّةِ.
- شَيْئًا: مَفْعُولٌ بِهِ مَنْصُوبٌ.
- الذي: اسمٌ مَوْصُولٌ مَبْنِيٌّ على السُّكُونِ فِي مَحَلِّ جَرٍّ، صِفَةٌ.
- خِيَمَ: مَفْعُولٌ بِهِ مَنْصُوبٌ.
- النَّازِحِينَ: مُضَافٌ إِلَيْهِ مجرورٌ، وعلامَةُ جَرِّهِ اليَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سالمٌ والنونُ عوضٌ عَنِ التنوينِ في الاسمِ المفردِ.
- والجِسْرُ: الواو: حَرْفُ اسْتِئْنَافٍ. الجِسْرُ: مُبْتَدَأٌ مَرْفُوعٌ.
- كُلَّ: نَائِبُ ظَرْفِ زَمَانٍ مَنْصُوبٌ.
- يومٍ: مُضَافٌ إليهِ مَجْرُورٌ.
- كَالطَّريقِ: الكاف: حَرْفُ جرٍّ. الطريقِ: اسمٌ مجرُورٌ.
- وهِجْرَةُ: الواو: حَرْفُ عَطْفٍ. هِجْرَةُ: مُبْتَدَأٌ مَرْفُوعٌ.
- الدَّمِ: مُضَافٌ إليهِ مَجْرُورٌ.
- النَّهْرِ: مُضَافٌ إِلَيهِ مَجْرُورٌ.
- تَنْحَتُ: فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.
- مِنْ حَصَى: مِنْ: حَرْفُ جَرٍّ. حَصَى: اسمٌ مجرورٌ، وعلامَةُ جَرِّهِ الكَسْرَةُ المُقَدَّرَةُ على الأَلِفِ مَنَعَ ظُهُورَها التَّعَذَّرُ.
- الوادي: مُضَافٌ إليهِ مَجْرُورٌ، وعلامَةُ جَرِّهِ الكَسْرَةُ الْمُقَدَّرِةُ على الياءِ مَنَعَ ظهورها الثِّقَلُ.
- تماثيلًا: مَفْعُولٌ بِهِ مَنْصُوبٌ.
- لها: اللام: حَرْفُ جرٍّ. وها: ضميرٌ مُتَّصِلٌ مَبْنِيٌّ على السُّكُونِ في محلِّ جرٍّ، بِحَرْفِ الجَرِّ.
- لَوْنُ: مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.
- النجومِ: مُضَافٌ إليهِ مَجْرُورٌ.
- وَلَسْعَةُ: الواو: حَرْفُ عَطْفٍ. لَسْعَةُ: اسمٌ مَعْطُوفٌ مَرْفُوعٌ.
- الذكرى: مُضَافٌ إليهِ مَجْرُورٌ، وعلامَةُ جَرِّهِ الكَسْرَةُ المُقَدَّرَةُ على الياءِ، مَنَعَ ظُهُورَهَا التَّعَذُّرُ.
- وطَعْمُ: الواو: حَرْفُ عَطْفٍ. طَعْمُ: اسمٌ مَعْطُوفٌ مَرْفُوعٌ.
- الحبِّ: مُضَافٌ إِلَيْهِ مَجْرُورٌ.
- حينَ: مَفْعُولٌ فِيهِ ظَرْفُ زَمَانٍ مَنْصُوبٌ.
- يصيرُ: فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ.
- أَكْبَرَ: خَبَرُ (يصِيرُ) مَنْصُوبٌ.
- مِنْ عِبَادِهِ: مِنْ: حَرْفُ جَرٍّ. عِبَادِهِ: اسمٌ مَجْرُورٌ، وعلامَةُ جَرِّهِ الكَسْرَةُ الظَّاهِرَةُ وَسُكِّنَ لِلضَّرُورَةِ الشِّعْرِيَّةِ.

=== BLOCK 4: Summary Table of Sentence Irab (The Core Matrix) ===
(Component: TEMPLATE_C_TABLE.html)
Title: إعراب الجمل (خلاصة)
Columns: | الجملة | إعرابها |
Rows:
| جُمْلَةُ (الصَّمْتُ خَيَّمَ) | استئنافية، لا محل لها مِنَ الإعراب |
| جُمْلَةُ (خَيَّمَ) | خَبَرَيَّةٌ، محَلُّهَا الرَّفْعُ |
| جُمْلَةُ (يَبْصُقُ) | خَبَرَيَّةٌ، مَحَلَّهَا النَّصْبُ |
| جُمْلَةُ (لم يَعْرِفُوا) | استئنافية، لا محل لها من الإعراب |
| جُمْلَةُ (لم يَعْرِفْ أَحَدٌ) | مَعْطُوفَةٌ، لَا مَحَلَّ لها من الإعراب |
| جُمْلَةُ (يَمْتَصُّ) | صِلَةُ المَوْصُولِ، لا مَحَلَّ لَهَا مِنَ الإعراب |
| جُمْلَةُ (الجِسْرُ يَكْبُرُ) | استئنافية، لا محل لها مِنَ الإعراب |
| جُمْلَةُ (يَكْبُرُ) | خَبَرَيَّةٌ، مَحَلُّهَا الرَّفْعُ |
| جُمْلَةُ (هِجْرَةُ الدَّمِ تَنْحَتُ) | مَعْطُوفَةٌ، لا محل لها مِنَ الإعراب |
| جُمْلَةُ (تَنْحَتُ) | خَبَرَيَّةٌ، مَحَلُّهَا الرَّفْعُ |
| جُمْلَةُ (لَهَا لَوْنُ النُّجُومِ) | صفَةٌ، مَحَلُّهَا النَّصْبُ |
| جُمْلَةُ (يصِيرُ أَكْبَرَ) | مُضَافٌ إليه، محلها الجر |

=== BLOCK 5: Poem Text ===
(Component: TEMPLATE_C_POEM.html)
Title: أَسْطُرُ النَّصِّ المُتَمِّمَةُ الوَارِدَةُ فِي دِيوانِ الشاعر محمود درويش
Poem Lines:
.... أمر بإطلاق الرصاص على الذي يجتاز
هَذَا الْحِسْرَ هَذَا الحِسْرُ مِقْصَلَةُ الذِي رَفَضَ
التَّسَلُّلَ تَحْتَ ظِلِّ وَكَالَةِ الغَوثِ الجديدة ..
والمَوْتَ بِالمَجَانِ تَحْتَ الذُّلِّ وَالأَمْطَارِ، مَنْ
يَرْفُضْهُ يُقْتَلْ عِنْدَ هذا الحِسْرِ، هَذَا الْحِسْرُ
مقْصَلَةُ الذي ما زالَ يَحْلُمُ بِالوَطَنْ
لا تَعْتَقِلُوها، واقْتُلُوني
كَانَتْ مِيَاهُ النَّهْرِ أَغْزَرَ . . فالذينَ
رَفَضُوا هُنَاكَ المَوْتَ بِالمَجَانِ أَعطوا النَّهْرَ لَونًا آخَرَ.
والحِسْرُ، حِيْنَ يَصِيرُ تمثالًا ، سَيُصْبَغُ - دُونَ
ريبٍ - بالظهيرةِ والدِّمَاءِ وَخُضْرَةِ الْمَوْتِ
المفاجئ
وطَارَ عِطْرُ الياسمين
عَنْ صَدْرها العاري الذي
مَلَأَتُهُ رَائِحَةُ الْجَرِيمَةِ
-  -
وطَعْمُ الحُبِّ حِينَ يَصِيرُ أَكثرَ من عِبَادِهِ.
في غدٍ تزحف الجموع

--- END STREAM ---
