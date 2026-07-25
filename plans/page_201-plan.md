# **SESSION 201**

[TASK DEFINITION]
Objective: Implement page 201.
File: `pages/page_201.html` (Note: Use the exact page number.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`.
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md`.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green`  for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide: NO INLINE STYLES. Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). The ID MUST be applied to the `<div>` tag that replaced the `<section>` tag. Use "Jules-workspace/id_manager.py" to generate or verify them.
8. Self-Correction: Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...) .
11. You must preserve the exact Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal.
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
15. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 201
[CHAPTER_TITLE]: page 201
[CATEGORY_HEADER]: 201
[SECTION_HEADER]: 201
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Poem 1 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: - تصوير آثار الغربة النفسية وسيطرة اليأس والتشاؤم على نفس المغترب:
[POET_NAME]: فوزي المعلوف:
[RIGHT_HEMISTICH]: فهو لا يَعْرِفُ التَّبَسُّمَ إِلَّا
[LEFT_HEMISTICH]: عِنْدَمَا يَسْتَعِيد حلمًا جَمِيلا

=== BLOCK 3: Poem 1 verse 2 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]:
[RIGHT_HEMISTICH]: ألف اليأْسَ قَلْبُهُ فَهو واليأس
[LEFT_HEMISTICH]: يُحاكي بُشَيْنَةً وَجَمِيلا

=== BLOCK 4: Poem 1 verse 3 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]:
[RIGHT_HEMISTICH]: وإذا اليَأْسُ صَدَّ عَنْهُ قَلِيلًا
[LEFT_HEMISTICH]: راح يبكي على نَوَاهُ طَوِيلا

=== BLOCK 5: Poem 2 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: - تصويرُ حَيْرَةِ الْمُغْتَرَبِ وَقَلَقِهِ وَضَيَاعِه:
[POET_NAME]: فوزي المعلوف
[RIGHT_HEMISTICH]: حَائِرَ الطَّرْفِ شَارِدَ الفِكْرِ يَحْكِي
[LEFT_HEMISTICH]: مُدْلِجًا في الظلامِ ضَلَّ السَّبِيلا

=== BLOCK 6: Poem 3 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: - ضَيَاعُ عُمْرِ الْمُغْتَرَبِ دُونَ تَحْقِيقٍ غَايَاتِه:
[POET_NAME]: فوزي المعلوف
[RIGHT_HEMISTICH]: تَاهَ فِي عَالَمِ الخيال فَضَاعَتْ
[LEFT_HEMISTICH]: نَفْسُهُ وهي تَنْشُدُ المستحيلا

=== BLOCK 7: Block 1 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: -١٠ تصوير مظاهر الشقاء في السَّعْي لِكَسْبِ الرِّزْق:
Content: <span class="text-accent">تَصْوِيرُ مَلامح معاناةِ البَنَّاءِ فِي فَصْلِ الشِّتَاء:</span>

=== BLOCK 8: Poem 4 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]: زكي قنصل
[RIGHT_HEMISTICH]: بالروح في كانون نظرته
[LEFT_HEMISTICH]: يَصْطَكُ مِنْ قُرِّ وَيَصْطَرِبُ

=== BLOCK 9: Poem 4 verse 2 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]:
[RIGHT_HEMISTICH]: تلهو الرِّيَاحُ بِهِ فَإِنْ سكنت
[LEFT_HEMISTICH]: فَتَحَتْ عليهِ تُقُوهَا السُّحُبُ

=== BLOCK 10: Poem 4 verse 3 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]:
[RIGHT_HEMISTICH]: جمدت على المنقار راحته
[LEFT_HEMISTICH]: فكأنها من بَعْضِهِ خَشَبُ

=== BLOCK 11: Poem 5 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: أَثَرُ كُلِّ مِنَ الأَلم والجوع في البناء:
[POET_NAME]: زكي قنصل:
[RIGHT_HEMISTICH]: دامي الفؤادِ يَمُضُهُ ألمٌ
[LEFT_HEMISTICH]: ذاوي الجفونٍ يَعَضُهُ سَغَبُ

=== BLOCK 12: Poem 6 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: حَظُ البَنَّاءِ العاثر وَخَيْبَةُ سَعْيه :
[POET_NAME]: زكي قنصل:
[RIGHT_HEMISTICH]: يسعى ولكن لا إلى أمل
[LEFT_HEMISTICH]: وَيَدِبُّ لَكِنْ حَيْتُ لَا أَرَبُ

=== BLOCK 13: Poem 7 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: مُواصَلَةُ البَنَّاءِ العَمَلَ رُغْمَ الْأَلَم وَالتَّعَب:
[POET_NAME]: زكي قنصل:
[RIGHT_HEMISTICH]: يا غَائِصا بالطين لا نصب
[LEFT_HEMISTICH]: يوهي عزيمته ولا وَصَبُ

=== BLOCK 14: Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: ۱۱- تصوير واقع حَيَاةِ الْمَغَرَّبِيْنَ القَاسِي فِي الغُرْبَة:
[HEADER_2]:
[HEADER_3]:
[CELL_1]: حَيَاةُ البَنَّاءِ المُغَرَّبِ مَلِينَةٌ بِالتَّعَبِ والقَسْوَة:
[CELL_2]: خُلُوْ حَيَاةِ البَنَّاءِ الْمُغَرَّبِ مِنَ التَّفاول والأَمَل:
[CELL_3]: افتِقَارُ البَنَّاءِ المُغَرَّبِ إلى الأصحاب:

=== BLOCK 15: Poem 8 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]: زكي قنصل
[RIGHT_HEMISTICH]: يَبْنِي القُصُورَ وَكُوحُهُ خَرِبُ
[LEFT_HEMISTICH]: سَاءَتْ حَياةٌ كُلَّهَا تَعَبُ

=== BLOCK 16: Poem 8 verse 2 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]:
[RIGHT_HEMISTICH]: الشوك يزخر في مسالكها
[LEFT_HEMISTICH]: والريح ما تَنْفَكُ تَصْطَخِبُ

=== BLOCK 17: Poem 9 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]: زكي قنصل:
[RIGHT_HEMISTICH]: لا يَزْدَهِي فِي لَيْلِهِ قَبَس
[LEFT_HEMISTICH]: إِلَّا تَوَلَّتْ طَمْسَهُ النُّوب

=== BLOCK 18: Poem 10 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]: زكي قنصل:
[RIGHT_HEMISTICH]: صَفُرَتْ مِنَ الأصحاب راحته
[LEFT_HEMISTICH]: لَمْ يُجْدِهِ سَعْيِّ ولا طلب

=== BLOCK 19: Benefit Warning ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[TITLE]: أَرْقُ البَنَّاءِ المُغَرَّبِ بِسَبَبِ الحرمانِ والتَّعَب:
[CONTENT]: زكي قنصل: يَنْبُو بِهِ فِي اللَّيْلِ مَضْجَعُهُ ويشوكهُ الحرمان والنَّصَب

=== BLOCK 20: Block 2 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: -١٢ مُحَاوَلَةُ التَّخْفِيفِ مِنْ آلام البناء الكادح:
Content: <span class="text-accent">دَعْوَةُ البَنَّاءِ الكادح إلى الصَّبر والابْتِعَادِ عَنِ الغَضَب:</span>

=== BLOCK 21: Poem 11 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]: زكي قنصل :
[RIGHT_HEMISTICH]: صَبرا على الأَيَّامِ إِنْ عَبَسَتْ
[LEFT_HEMISTICH]: هَيْهَاتَ يَفْرج ضيقها غضب

=== BLOCK 22: Poem 12 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: تَذْكِيرُ البَنَّاءِ الكَادِحَ بِكَثْرَةِ الخَائِبِين المتعبين:
[POET_NAME]: زكي قنصل:
[RIGHT_HEMISTICH]: ما أنت أَوَّلَ كَادِحِ عَثَرَتْ
[LEFT_HEMISTICH]: آمالهُ وكبا به الدَّأَبُ

=== BLOCK 23: Poem 13 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: مشاركة البَنَّاءِ فِي الشَّقَاء:
[POET_NAME]: زكي قنصل:
[RIGHT_HEMISTICH]: بَيْنِي وَبَيْنَكَ في البلاء نَسَبُ
[LEFT_HEMISTICH]: وإن كَذَبَتْ عليك ظَوَاهِرِي

=== BLOCK 24: Cut Content 1 ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
[BLOCK_TITLE]: رابعا - القومية والإنسانية
[CONTENT]:

--- END STREAM ---
