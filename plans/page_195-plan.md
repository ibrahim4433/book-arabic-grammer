# **SESSION 195**

[TASK DEFINITION]
Objective: Implement page 195.
File: `pages/page_195.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`.
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md`.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   **Rule:** NO INLINE STYLES.
*   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). Use "Jules-workspace/id_manager.py".
8. **Self-Correction:** Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...) .
11. You must preserve the exact Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense. Do NOT leave empty space.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal.
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`).
15. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers!

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Page Wrapper ===
(Component: TEMPLATE_C_PAGE_WRAPPER.html)

=== BLOCK 2: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 195
[CHAPTER_TITLE]: page 195
[CATEGORY_HEADER]: 195
[SECTION_HEADER]: 195
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 3: Cut Content - Irab (Continuation) ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[BLOCK_TITLE]: الإعراب
[CONTENT]: <span class="highlight-red">اسم إِنَّ</span> مَنْصُوبُ <span class="highlight-red">الظَّهْرِ :</span> مُضَاف إليهِ مَجْرُورٌ. <span class="highlight-red">حملا:</span> مَفْعُولُ بِهِ مَنْصُوب، وعلامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَةُ. <span class="highlight-red">ثَقِيلا :</span> صِفَةٌ مَنْصُوبَة،ٌ وعلامَةً نَصْبِها الفَتْحَةُ الظَّاهِرَة.ُ <span class="highlight-red">جملة )كَأَنَّ قَاصِمَةَ الظَّهْرِ أَنَاخَتْ( :</span> صِفَة،ٌ مَحَلُها الجر. <span class="highlight-red">جملة )أَنَاخَتْ(:</span> خَبَرَيَّة،ٌ مَحَلَّهَا الرَّفْع.ُ

=== BLOCK 4: Poem Verse 5 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البيت الخامس
[RIGHT_HEMISTICH]: ه- وَجَبِيْنِ أَلْقَتْ عَلَيْهِ شُجُونُ النَّفْسِ
[LEFT_HEMISTICH]: ظِلًّا مِنَ العُبُوسِ ظَلِيْلا

=== BLOCK 5: Explanation and Idea 5 ===
(Component: TEMPLATE_C_SPLIT.html)
[COLUMN_1_TITLE]: الشرح
[COLUMN_1_CONTENT]: <p class="text-accent">إِنَّ ذَلِكَ الجَبِينَ المُقَطَّبَ الْمُغَضَنَ الَّذِي لَفَعَتْهُ أَحْزَانُ النَّفْسِ وَشُجُونُهَا بِظِلٍّ قَاتِمٍ كَتِيْب،ِ قَدْ بَاتَ مَحْرُومًا مِنَ السَّعَادَة.ِ</p>
[COLUMN_2_TITLE]: الفكرة
[COLUMN_2_CONTENT]: <p class="text-accent">تصوير بُرُوز آثارِ مُعَانَاةِ الْمُغْتَرَبِ انعِكَاسَ عَذَابَاتِ المغترب ومعاناته على محياه(، )تصوير آثار الغُرْبَةِ الجَسَدِيَّة(.</p>

=== BLOCK 6: Irab 5 ===
(Component: TEMPLATE_C_IRAB.html)
Title: الإعراب
Content:
<div class="irab-box"><span class="irab-word">وَجَبين</span> الواو، حَرْفُ عَطْفٍ وَجَبِيْن،ِ اسمٌ مَعْطُوفٌ جْرُورٌ</div>
<div class="irab-box"><span class="irab-word">أَلْقَتْ</span> : فعل ماض، مَبْنِي على الفَتْحَةِ المُقَدَّرَةِ على الآلِفِ المَحْذُوِفَةِ؛ لَا تِصَالِهِ بنَاءِ التَّأْنِيثِ السَّاكِنَةِ وَالنَّاء،ُ حَرْفُ تَأْنِيثٍ لَا مَحَلَّ لَهُ مِنَ الإعراب.</div>
<div class="irab-box"><span class="irab-word">شُجُونُ</span> : فَاعِلَ مَرْفُوعُ</div>
<div class="irab-box"><span class="irab-word">النَّفْسِ</span> : مُضَافُ إِلِيهِ مَجْرُورٌ</div>
<div class="irab-box"><span class="irab-word">ظِلًا:</span> مَفْعُولُ بِهِ مَنْصُوب.ُ</div>
<div class="irab-box"><span class="irab-word">ظليلا :</span> صفَةٌ مَنْصُوبَة،ً وعلامَةُ نَصْبِهَا الفَتْحَةُ الظَّاهِرَة.ُ</div>
<div class="irab-box"><span class="irab-word">جملة )أَلْقَتْ عَلَيْهِ شُجُونُ النَّفْسِ(:</span> صِفَة،ٌ مَحَلَّها الجر.</div>

=== BLOCK 7: Poem Verse 6 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البيت السادس
[RIGHT_HEMISTICH]: فهو لا يَعْرِفُ التَّبَسُّمَ
[LEFT_HEMISTICH]: إِلَّا عِنْدَمَا يَسْتَعِيدُ حُلمًا جَمِيلا

=== BLOCK 8: Explanation and Idea 6 ===
(Component: TEMPLATE_C_SPLIT.html)
[COLUMN_1_TITLE]: الشرح
[COLUMN_1_CONTENT]: <p class="text-accent">لا تَرْتَسِمُ الابْتِسَامَةُ على مُحَيَّاهُ العَابِسِ إِلَّا إِذَا اسْتَعَادَ يَوْمَ سَعْدٍ غَابِر،ٍ أو لَاحَ لَهُ طَيْفُ ذِكْرَى جَمِيلَةٍ سَالِفَةِ</p>
[COLUMN_2_TITLE]: الفكرة
[COLUMN_2_CONTENT]: <p class="text-accent">تَصْوِير آثار الغُرْبَةِ النَّفْسِيَّةِ )سَيْطَرَةُ اليَأْسِ وَالتَّشَاؤمِ عَلى نَفْسِ المغترب(.</p>

=== BLOCK 9: Irab 6 ===
(Component: TEMPLATE_C_IRAB.html)
Title: الإعراب
Content:
<div class="irab-box"><span class="irab-word">فهو</span> الفاء، حَرْفُ اسْتِئناف هو، ضميرُ رَفْعِ مُنْفَصِلٌ مَبْنِيَّ على الفتح فِي مَحَلِّ رَفْع،ِ مُبْتَدَا.</div>
<div class="irab-box"><span class="irab-word">لا يَعْرِفُ :</span> لا، حَرْفُ نَفي. يَعْرِفُ فِعْلَ مُضَارِعُ مَرْفُوعُ</div>
<div class="irab-box"><span class="irab-word">التَّبَسُّمَ</span> مَفْعُولُ بِهِ مَنْصُوبُ</div>
<div class="irab-box"><span class="irab-word">إِلَّا</span> أداةً حَصْرٍ .</div>
<div class="irab-box"><span class="irab-word">عِنْدَمَا</span> عِنْدَ مَفْعُولُ فِيهِ ظَرْفٌ زَمَانٍ مَنْصُوبٌ ما، حَرْفٌ مَصْدَرِي وَالْمَصْدَرُ الْمُؤَوَّلُ )ما يَسْتَعِيدُ( فِي مُحَلِّ جَر،ِّ مُضافُ إِلَيْهُ</div>
<div class="irab-box"><span class="irab-word">حُلمًا :</span> مَفْعُولُ بِهِ مَنْصُوب.ُ</div>
<div class="irab-box"><span class="irab-word">جَمِيلًا:</span> صِفَةٌ مَنْصُوبَةً</div>
<div class="irab-box"><span class="irab-word">جملة )هو لَا يَعْرِفُ(:</span> اسْتِثْنَافِيَّة،ٌ لَا مَحَلَّ لَهَا مِنَ الإعراب</div>
<div class="irab-box"><span class="irab-word">جملة )لا يعرف(:</span> خَبَرَيَّة،ٌ مَحَلَّهَا الرَّفْع.ُ</div>
<div class="irab-box"><span class="irab-word">جملة )يَسْتَعِيدُ( :</span> صِلَةٌ المَوْصُول،ِ لا محل لها مِنَ الإعراب.</div>

=== BLOCK 10: Poem Verse 7 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البيت السابع
[RIGHT_HEMISTICH]: ٧- أَلِفَ اليَأْسَ قَلْبُهُ فَهو واليأس
[LEFT_HEMISTICH]: يحاكي بُثَيْنَةً وَجَمِيلا

=== BLOCK 11: Explanation and Idea 7 ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: الشرح والفكرة
Content: <p class="text-accent"><span class="font-bold">الشرح :</span> لِأَنَّ اليَأْسَ قَدِ اتَّخَذَ قَلْبَهُ سَكَنَا دَائِمًا وحُضْنَا دَافِنَا انْعَقَدَتْ بِينَهُمَا أَوَاصِرُ مَوَدَّة وطِيدَةٍ مَاثَلَتْ بِمَتَانَتِهَا مَتَانَةَ عُرَى عَلَاقَةِ العِشْقِ التِي جَمَعَتْ جَمِيلًا بِمَحْبُوبَتِهِ بُثَيْنَةَ <br><span class="font-bold">الفِكْرة :</span> تَصْوِيرُ آثَارِ الغُرْبَةِ النَّفْسِيَّةِ سَيْطَرَةُ اليَأْسِ وَالتَّشَاؤُمِ على نَفْسِ الْمُغْتَرَبِ(.</p>

=== BLOCK 12: Irab 7 ===
(Component: TEMPLATE_C_IRAB.html)
Title: الإعراب
Content:
<div class="irab-box"><span class="irab-word">ألف :</span> فعل ماض، مَبْنِي على الفَتْحَةِ الظَّاهِرَةِ</div>
<div class="irab-box"><span class="irab-word">اليَأْسَ</span> مَفْعُولُ بِهِ مَنْصُوبٌ</div>
<div class="irab-box"><span class="irab-word">قَلْبُه:ُ</span> فَاعِلَ مَرْفوع، وعلامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَة،ُ وَالهَاء،ُ ضمير متصل مبني على الضم في محل جر، مضافُ إِلَيْه.ِ</div>
<div class="irab-box"><span class="irab-word">فهو</span> الفاء، حَرْفُ اسْتِثْنَافٍ هو، ضميرُ رَفْعِ مُنْفَصِلٌ مَبْنِي على الفَتْحِ فِي مَحَلِّ رَفْع،ِ مُبْتَدَا.ً</div>
<div class="irab-box"><span class="irab-word">واليأس</span> الواو، حَرْفُ عَطْفٍ والياس، اسم مَعْطُوفٌ مَرْفُوعٌ</div>
<div class="irab-box"><span class="irab-word">يُحَاكِي:</span> فِعْلَ مُضَارِعٌ مَرْفُوع، وعلامَةُ رَفْعِهِ الضَّمَةُ المُقَدَّرَةُ على الياء، مَنَعَ ظُهُورَهَا الثِّقَلُ</div>
<div class="irab-box"><span class="irab-word">بُثَيْنَةَ</span> مَفْعُولُ بِهِ مَنْصُوب.</div>
<div class="irab-box"><span class="irab-word">وجميلا :</span> الواو ، حَرْفُ عَطْفٍ وجَمِيلا، اسمٌ مَعْطُوفٌ مَنْصُوب.</div>
<div class="irab-box"><span class="irab-word">جملة )أَلِفَ اليَأْسَ قَلْبُهُ(:</span> اسْتِثْنَافِيَّة،ٌ لا محل لها من الإعراب</div>
<div class="irab-box"><span class="irab-word">جملة )هو والياس يُحاكي( :</span> اسْتِثْنَافِيَّة،ٌ لَا محل لها من الإعراب</div>
<div class="irab-box"><span class="irab-word">جملة )يُحَاكِي( :</span> خَبَرَيَّة،ٌ مَحَلُّهَا الرَّفْع.ُ</div>

=== BLOCK 13: Poem Verse 8 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البيت الثامن
[RIGHT_HEMISTICH]: وإذا اليَأْسُ صَدَّ عَنْهُ قَلِيلَا
[LEFT_HEMISTICH]: رَاحَ يَبْكي على نَوَاهُ طَوِيلا

=== BLOCK 14: Vocab, Explanation and Idea 8 ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: المفردات
[HEADER_2]: الشرح
[HEADER_3]: الفكرة
[CELL_1]: نواه: بُعْدَهُ
[CELL_2]: لِشِدَّةِ تَعَلَّقِ الْمُغْتَرِبِ بِاليَأْسِ وَلِلْحَمِيمِيَّةِ والأُلَفَةِ التِي تَمَتْ بَيْنَهُما، فَإِنَّهُ يَحْزَنُ وَيَتَالَمْ إِذَا مَا جَافَاهُ اليَأْسُ وفَتَرَ عَنْهُ لَحْظَة،ً بل يبكي فراقه ومجافاته وصدودة بكاء عاشق متيم انفصل عن محبُوبَتِهِ
[CELL_3]: تَصْوِيرُ آثَارِ الْغُرْبَةِ النَّفْسِيَّةِ )سَيُطَرَةُ اليَأْسِ والتَّشَاؤُم على نَفْفس المُغْتَرب(

=== BLOCK 15: Irab 8 ===
(Component: TEMPLATE_C_IRAB.html)
Title: الإعراب
Content:
<div class="irab-box"><span class="irab-word">وإذا :</span> الواو، حرف اسْتِئْنَاف. وإذا، اسمُ شَرْطِ غَيْرُ جازم، مَبْنِي على السُّكُون، فِي مَحَلِ نَصْب،ِ مَفْعُولٌ فِيهِ ظَرْفُ زَمَانِ</div>
<div class="irab-box"><span class="irab-word">اليَأْس:ُ</span> فَاعِلْ لِفِعْلِ مَحْذُوفِ يُفْسِرُهُ الْمَذْكُورُ بَعْدَهُ مَرْفُوعٌ</div>
<div class="irab-box"><span class="irab-word">قَلِيلًا :</span> نَائِبُ مَفْعُولٍ فِيهِ ظَرْفُ زَمَانٍ مَنْصُوب. هذا الإعْرَاب على تَقْدِير : صَدَّ عَنْهُ زَمَنَا قَلِيلًا، وَيَصِحُ فِي إعْرَابِها وجة آخر )لا خلاف حَوْلَهُ(، وهو نائِبُ مَفْعُولِ مُطْلَقَ مَنْصُوب، وعلامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَةُ على تَقْدِيرِ : صَدَّ عَنْهُ صُدُودًا قليلا [.</div>
<div class="irab-box"><span class="irab-word">راح :</span> فعل ماض ناقص، مَبْنِي على الفَتْحَةِ الظَّاهِرَةِ</div>
<div class="irab-box"><span class="irab-word">طَوِيل :</span> نَائِبُ مَفْعُولٍ فِيهِ ظَرُفُ رَمَانٍ مَنْصُوب.ٌ هذا الإعراب على تَقْدِير : يَبْكي على نَوَاهُ زَمَنَا طَوِيْلًا، وَيَصِحُ فِي إعْرَابِها وجه آخر لا خلاف حَوْلَهُ(، وهو : نائِبُ مَفْعُولٍ مُطْلَقَ مَنْصُوب.ٌ على تَقْدِيرِ : يبكي على نَوَاهُ بُكاء طويلا .</div>
<div class="irab-box"><span class="irab-word">جمله )إذا اليَأْسُ صَدَّ عَنْهُ قَلِيْلًا رَاحَ يَبْكي( :</span> اسْتِثْنَافِيَّة،ُ لَا مَحَلَّ لها مِنَ الإعراب.</div>
<div class="irab-box"><span class="irab-word">جملة )صد(:</span> تَفْسِيرية، لا محل لها مِنَ الإعراب</div>
<div class="irab-box"><span class="irab-word">جملة )راح يبكي( :</span> جَوَابُ الشَّرْط،ِ لا مُحَلَّ لها مِنَ الإعراب</div>
<div class="irab-box"><span class="irab-word">جملة )يبكي( :</span> خَبَرَيَّة،ٌ مَحَلَّهَا النَّصْب.ُ</div>

=== BLOCK 16: Poem Verse 9 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البيت التاسع
[RIGHT_HEMISTICH]: وإذا ما النَّسِيمُ مَرَّ عَلَيْهِ
[LEFT_HEMISTICH]: فَعَلِيلٌ أَتَى يَعُودُ عَلِيلا

=== BLOCK 17: Vocab, Explanation and Idea 9 ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: المفردات
[HEADER_2]: الشرح
[HEADER_3]: الفكرة
[CELL_1]: عليل : مريض. يعود : يَزُور
[CELL_2]: إِنَّ النَّسَمَاتِ الرَّقِيقَةَ الواهِنَةَ الضَّعِيفَة،َ حِينَمَا تَلْفَحْ ذَلِكَ الْمُغْتَرَب،َ وتُدَاعِبُ وَجْهَهُ تَجِدْهُ مَرِيضًا سَقِيمًا مَهْمُومًا، فَتَبْدُو كَمَرَيْضِ وَاهِنِ أَتَى يَعُودُ مَرِيضًا وَاهِنَا ضَعِيفًا .
[CELL_3]: مشاركةُ الطَّبِيعَةِ الشَّاعِرَ آلامَه.ُ

=== BLOCK 18: Irab 9 ===
(Component: TEMPLATE_C_IRAB.html)
Title: الإعراب
Content:
<div class="irab-box"><span class="irab-word">وإذا :</span> الواو ، حَرْفُ عَطْف. وإذا ، اسمُ شَرْطٍ غَيْرُ جازم، مَبْنِي على السُّكُون، في مَحَلِّ نَصْب،ِ مَفْعُولُ فِيهِ ظَرْفُ زَمَانٍ</div>
<div class="irab-box"><span class="irab-word">مَا النَّسِيم:ُ</span> ما، حَرْفٌ زَائِدُ النَّسِيم،ُ فَاعِلْ لِفِعْلِ مَحْذُوفِ يُفَسِرُهُ الْمَذْكُورُ بَعْدَهُ مَرْفُوعٌ</div>
<div class="irab-box"><span class="irab-word">فَعَلِيْل :</span> الفَاء،ُ حَرْفٌ رابط جَوَابِ الشَّرْطِ . عَلِيلٌ خَبَرٌ لِمُبْتَدَا مَخْذُوفِ مرفوع</div>
<div class="irab-box"><span class="irab-word">أتى:</span> فعل ماض، مَبْنِي على الفَتْحَةِ المُقَدَّرَةُ على الأَلِفِ مَنَعَ ظُهُورَهَا التَّعَذِّرُ</div>
<div class="irab-box"><span class="irab-word">عَلِيلا :</span> مَفْعُولُ بِهِ مَنْصُوبٌ</div>
<div class="irab-box"><span class="irab-word">جملة )إذا ما النَّسِيمُ مَرَّ عَلَيْهِ فَعَلِيلٌ أَتَى( :</span> مَعْطُوفَة،ٌ لَا مَحَلَّ لَا مِنَ الإعراب</div>
<div class="irab-box"><span class="irab-word">جملة ) مَرَ النَّسِيمُ(:</span> مُضَافُ إِلَيْه،ِ مَحَلَّها الجر.</div>
<div class="irab-box"><span class="irab-word">جمله )مَرَّ( :</span> تَفْسِيرِيَّة،ٌ لَا مَحَلَّ لَهَا مِنَ الإعراب</div>
<div class="irab-box"><span class="irab-word">جملة )فَعَلِيل أَتَى( :</span> جَوَابُ الشَّرْط،ِ لا محل لها من الإعراب</div>
<div class="irab-box"><span class="irab-word">جملة )أَتَى(:</span> صِفَة،ً محلها الرفع</div>
<div class="irab-box"><span class="irab-word">جمله )يَعُودُ(:</span> حالِيَّة،ٌ حَلَّهَا النَّصْبُ . ] حالٌ مِنَ الضَّمِيرِ الْمُسْتَتِرِ في الفعل )أتى([.</div>

--- END STREAM ---
