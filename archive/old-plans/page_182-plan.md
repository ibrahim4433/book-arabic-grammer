# **SESSION 182**

[TASK DEFINITION]
Objective: Implement page 182.
File: `pages/page_182.html` (Note: Use the exact page number.)
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
[LESSON_NUMBER]: 182
[CHAPTER_TITLE]: page 182
[CATEGORY_HEADER]: 182
[SECTION_HEADER]: 182
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Cut Content Continuation ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[BLOCK_TITLE]: تتمة
[CONTENT]: فَتَتَبَّعْت السواقي
الشرح : سَتَجِدُ فِي طَبِيعَةِ الغَابِ الجَمِيلَةِ جَنَّةَ حَقِيقِيَّةً تَنْعُمُ بِمَبَاهِجِهَا الفَرِيدَة،ِ حَيْثُ التَمَتَّعُ بِمَنَاظِرِ سَوَاقِيهَا الخلابة، والتَّسَلْقُ على صُحُورها البَهِيجَةِ

=== BLOCK 3: Benefit Warning (Orange) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[TITLE]: الفِكْرة
[CONTENT]: مطالبة الإنسان بالعودة إلى رحاب الطبيعة الدعوة إلى العيش في الغاب والاستمتاع بسخره(

=== BLOCK 4: Irab Analysis ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: فَتَتَبَّعْت:َ السَّوَاقِي وتَسَلَّقْتَ الصُّخور
[IRAB_ANALYSIS]: فَتَتَبَّعْت:َ الفاء، حَرْفُ عَطْفِ السَّوَاقِي: <span class="highlight-red">مَفْعُولُ بِهِ مَنْصُوبٌ</span> وَتَسَلَّقْتَ : الواو ، حَرْفُ عَطْفٍ الصُّخور : مَفْعُولُ بِهِ مَنْصُوب،ٌ وعلامَةً نَصْبِهِ الفَتْحَةُ الظَّاهِرَةُ وَسُكِّنَ لِلضَّرُورَةِ الشَّعْرِيَّة.ِ جملةٌ )تَبَّعْتَ( : مَعْطُوفَة،ٌ لَا مَحَلَّ لها مِنَ الإعراب جملة )تَسَلَّقْتَ( : مَعْطُوفَة،ً لا مُحَلَّ لها مِنَ الإعراب.

=== BLOCK 5: Poem Verse 9 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البيت التاسع
[RIGHT_HEMISTICH]: - هَلْ تَحْمَّمْتَ بِعِطْرِ
[LEFT_HEMISTICH]: وتَنَشَفْتَ بِنُور؟

=== BLOCK 6: Explanation ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: الشرح
[CONTENT]: ستنعم في طَبِيعَةِ الغَابِ بِالعَيْشِ بَيْنَ عَبِيرِ أَزْهَارِهَا الفَوَّاحَة،ِ والاسْتِمْتَاعِ بِأَنْوارِهَا السَّاطِعَةِ التِي تَبْعَثُ الدِفْءَ فِي نَفْسِك.َ

=== BLOCK 7: Benefit ===
(Component: TEMPLATE_C_BENEFIT.html)
[TITLE]: الفكرة
[CONTENT]: مطالبة الإنسان بالعودة إلى رحاب الطبيعة )الدعوة إلى العيش في الغاب والاستمتاع بسخره(

=== BLOCK 8: Irab Analysis ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: وتَنَشفت بِنُور
[IRAB_ANALYSIS]: وتَنَشفت : الواو، حَرْفُ عَطْفٍ بِنُور: الباء، حَرْفُ جر. نور، اسمٌ مَجْرُور،ُ وعلامةُ جَرَهِ الكَسْرَةُ الظَّاهِرَة.ُ وسُكِنَ لِلضَّرُورَةِ الشَّعْرِيَّة.ِ مُتَعَلّقان بالفعل )تَنَشَفْتَ(. جمله )تَحَمَّمْتَ(: استئنافية، لا محل لها مِنَ الإعراب جملة )تَنَشَفْتَ( : مَعْطُوفَة،ٌ لَا مَحَلَّ لها مِنَ الإعراب.

=== BLOCK 9: Poem Verse 10 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البيت العاشر
[RIGHT_HEMISTICH]: ۱۰- وشربتَ الفَجْرَ خَمرا
[LEFT_HEMISTICH]: في كؤوس مِنْ أَثِيرٌ

=== BLOCK 10: Explanation ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: الشرح
[CONTENT]: اهْجُرْ أَيُّها الإِنْسَانُ السُّكْرَ بِالخَمْر،ِ وَاسْكَرْ بِبَهَاءِ مَنْظَرِ بُزُوغِ الفَجْرِ وَجَمَالِ طُلُوعِ الشَّمْسِ حَيْثُ النَّسَمَاتُ الْأَثِيرَيَّةُ الهَادِئَةُ التي تُدَاعِبُكَ بِكُلِّ لَطْفٍ وَنُعُومَة.ِ

=== BLOCK 11: Benefit ===
(Component: TEMPLATE_C_BENEFIT.html)
[TITLE]: الفكرة والبلاغة
[CONTENT]: الفكرة: مطالبة الإنسان بالعودة إلى رحاب الطبيعة )الدعوة إلى الاستِمْتَاعِ بِفَجْرِ الغابِ وَنُوره( البلاغة: )الفجر خمر( تشبية بليغ

=== BLOCK 12: Irab Analysis ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: وَشَرِبْتَ الفَجْرَ خَمْرًا مِنْ أَثِير
[IRAB_ANALYSIS]: وَشَرِبْتَ الواو، حَرْفُ عَطْفٍ الفَجْرَ : <span class="highlight-red">مَفْعُولُ بِهِ مَنْصُوبُ</span> خَمْرًا حال مَنْصُوبَةٌ مِنْ أَثِير: مِنْ حَرْفُ جَرٍ أَثِير، اسم مَجْرُور، وعلامةُ جَرَهِ الكَسْرَةُ الظَّاهِرَة.ُ وسُكِنَ لِلضَّرُورَةِ الشَّعْرِيَّةِ مُتَعَلِقان بِصِفَةٍ مَحْذُوفة. جمله )شَرِبْتَ( : مَعْطُوفَة،َ لَا محل لها مِنَ الإعراب.

=== BLOCK 13: Poem Verse 11 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البيت الحادي عشر
[RIGHT_HEMISTICH]: ۱۱- هَلْ جَلَسْتَ العَصْرَ مِثْلِي
[LEFT_HEMISTICH]: بَيْنَ جَفْنَاتِ العِنَب؟

=== BLOCK 14: Table ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: المفردات
[HEADER_2]: الشرح
[HEADER_3]: الفكرة
[CELL_1]: جفنات: المُفْرَدُ جَفْنَة،ً وهي القَصْعَة،ُ وَأَرَادَ بها هنا العناقِيدَ الْمُعَلَّقَة،َ وَلَمْ تُقْطَف
[CELL_2]: في سَاعَاتِ العَصْرِ مَتِّعْ نَفْسَكَ بالجلُوسِ بَيْنَ كُرُومِ العِتَبِ
[CELL_3]: مطالبة الإنسان بالعودة إلى رحاب الطبيعة )الدعوة إلى العيش في الغاب والاستمتاع يسخره(

=== BLOCK 15: Irab Analysis ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: العَصْرَ مِثْلِي بَيْنَ جَفْنَاتِ العِنَب
[IRAB_ANALYSIS]: العَصْرَ مَفْعُولٌ فِيهِ ظَرْفُ زَمَانٍ مَنْصُوبُ مِثْلِي : <span class="highlight-red">نَائِبُ مَفْعُولٍ مُطْلَقٍ مَنْصُوب،ُ</span> وعلامَةُ نَصْبِهِ الفَتْحَةُ المُقَدَّرَةُ على ما قَبْلِ يَاءِ المُتَكَلِّم،ِ مَنَعَ ظُهُورَهَا اشْتِعَالُ الْمَحَل بالحركة المناسبة. والياء، ضميرٌ مُتَّصِلِّ مَبْنِي على السكون في محل جر، مُضَاف إليه. )التَّقْدِيرُ : هَلْ جَلَسْتَ العَصْرَ مِثْلَ جُلُوسي (... بَيْنَ : مَفْعُولٌ فِيهِ ظَرْفُ مَكَانٍ مَنْصُوبٌ جَفْنَاتِ : مُضَاف إليهِ مَجْرُورُ العِنَب:ْ مُضَاف إليهِ مَجْرُور،ٌ وعلامَةُ جَوَهِ الكَسْرَةُ الظَّاهِرَة.ُ وسُكِنَ لِلضَّرُورَةِ الشَّعْرِيَّةِ جملة )جَلَسْت( استئنافية، لا محل لها مِنَ الإعراب.

=== BLOCK 16: Poem Verse 12 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البيت الثاني عشر
[RIGHT_HEMISTICH]: -۱۲ والعَنَاقِيدُ تَدَلَّتْ
[LEFT_HEMISTICH]: كَثُرَيَّاتِ الذَّهَب

=== BLOCK 17: Explanation ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: الشرح
[CONTENT]: مَتِّعْ نَفْسَكَ بِإِمْعَانِ النَّظَرِ إِلَى العَنَاقِيدِ المَتَدَلَيةِ مِنْ عَرَائِشِ العِنَبِ التِي شَابَهَ تَدَلَيْهَا تَدَلَّي الثُّرَيَّاتِ الذَّهَبِيَّةِ فِي أَسْقُفِ القُصُور.ِ

=== BLOCK 18: Benefit ===
(Component: TEMPLATE_C_BENEFIT.html)
[TITLE]: الفكرة والبلاغة
[CONTENT]: الفكرة : مطالبة الإنسان بالعودة إلى رحاب الطبيعة )الدعوة إلى العيش في الغاب والاستمتاع بسخره( البلاغة : )العَنَاقِيدُ تَدَلَّتْ كَثُرَيَّاتِ الذَّهَبَ( تشبية تام الأركان

=== BLOCK 19: Irab Analysis ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: والعناقيد تَدَلَّتْ كَثُرَيَّاتِ الذَّهَب
[IRAB_ANALYSIS]: والعناقيد الواو، واو الحالِ العَنَاقِيد،ُ مُبْتَدَاً مَرْفُوعٌ تَدَلَّتْ فِعْل ماض مَبْنِيَّ على الفَتْحَةِ المُقَدَّرَةُ على الآلِفِ المَحْذُوفَةِ؛ لاتِصَالِهِ بِتَاءِ التَّأْنيثِ والنَّاء،ُ حَرْفٌ لَا مَحَلَّ لَهُ مِنَ الإعراب كَثُرَيَّات:ِ الكاف، حَرْفُ جر. ثُرَيَّات،ِ اسمٌ مَجْرُورُ الذَّهَبْ : مُضَافُ إليهِ مَجْرُور،ٌ وعلامَةُ جَرَهِ الكَسْرَةُ الظَّاهِرَةُ وَسُكِّنَ لِلضَّرُورَةِ الشَّعْرِيَّة.ِ جملة )العَنَاقِيدُ تَدَلَّتْ(: حاليَّة،ٌ مَحَلَّها النصب جملة )تَدَلَّتْ( : خَبَرَيَّة،ٌ مَحَلُّهَا الرَّفْع.ُ

=== BLOCK 20: Poem Verse 13 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البيت الثالث عشر
[RIGHT_HEMISTICH]: -۱۳ هَلَ فَرَشْتَ العُشْبَ لَيْلًا
[LEFT_HEMISTICH]: وَتَلَخَفْتَ الفضا؟

=== BLOCK 21: Explanation ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: الشرح
[CONTENT]: أَيُّهَا الإِنْسَانُ انْصَرِفْ عَنِ الدُّنيا وتأمَّلِ الغَابَ وَاسْتَمْتِعْ بِطبيعتِهِ السَّاحِرَة،ِ فَإِنْ أَسْدَلَ اللَّيْلُ سِتَارَهُ الأَسْوَدَ وَخَيَّمَ عَلَى الغَاب،ِ فَاسْتَمْتِعْ بالاستلقَاءِ فَوْقَ بِسَاطِ العُشْبِ الأَخْضَر،ِ وَالتَّخِذْهُ فِرَاشًا تَحْتَ قُبَّةِ السَّمَاءِ المَتَرَصَعَةِ بَآيَاتِ الجَمَالِ

=== BLOCK 22: Benefit ===
(Component: TEMPLATE_C_BENEFIT.html)
[TITLE]: الفِكرة
[CONTENT]: الدَّعُوةُ إلى الحياةِ الفِطْرِيَّةِ النَّقِيَّة.ِ )الدعوة إلى تأمل الطبيعة، والانصرافِ عَنِ الدنيا(

=== BLOCK 23: Irab Analysis ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: العُشْبَ لَيْلًا وَتَلَخَفْتَ الفضا
[IRAB_ANALYSIS]: العُشْبَ <span class="highlight-red">مَفْعُولُ بِهِ مَنْصُوبُ</span> لَيْلًا مَفْعُولُ فِيهِ ظَرْفُ زَمَانٍ مَنْصُوب.ٌ وَتَلَخَفْتَ الواو، حَرْفُ عَطْفِ الفَضَا : مَفْعُولُ بِهِ مَنْصُوب، وعلامَةُ نَصْبِهِ الفَتْحَةُ المُقَدَّرَةُ على الآلِفِ مَنَعَ ظُهُورَهَا التَّعَذُرُ )عُومِلَ الْمَمْدُودُ مُعَامَلَةِ المَقْصُورِ لِلضَّرَوَرَةِ السَّعْرِيَّةِ(. جملة )فَرَشْتَ( : استئنافية، لا محل لها مِنَ الإعراب جملة )تَلَخَفْتَ(: مَعْطُوفَة،ً لا محل لها مِنَ الإعراب.

=== BLOCK 24: Poem Verse 14 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البيت الرابع عشر
[RIGHT_HEMISTICH]: -١٤ زاهدا فِيمَا سَيَأْتِي
[LEFT_HEMISTICH]: ناسيا ما قَدْ مَضَى

=== BLOCK 25: Table ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: المفردات
[HEADER_2]: الشرح
[HEADER_3]: الفكرة
[CELL_1]: زاهدًا زَهِدَ فِي الشَّيْءٍ أَعْرَضَ عَنْهُ وَتَرَكَهُ
[CELL_2]: ازْهَدْ فِيمَا يُمْكِنُ أَنْ تَجْنِيهِ مِنْ منافع مادِيةٍ فِي الْمُسْتَفْبَل،ِ وَانْسَ الْمَاضِي ومَا فِيهِ مِنْ إِحْفَاقَات،ِ وَانْزَعْ مِنْ نَفْسِكَ ما تركَاهُ فِيهَا مِنْ أَثَرِ لِتَتَفَرْ لِل مَتُّعِ بِسُكُونِ اللَّيْلِ العَمِيقِ وَسِحْرِه.ِ
[CELL_3]: الدَّعوة إلى الرُّهْدِ بِالْمُسْتَقْبَلِ ونسيان الماضي. )الدعوة إلى تأمل الطبيعة، والأَنْصِرَافِ عَنِ الدنيا(

--- END STREAM ---
