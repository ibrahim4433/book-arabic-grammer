# **SESSION 65.0**

[TASK DEFINITION]
Objective: Implement عِلْمُ الْبَيَانِ التَّشْبِيهُ وَالِاسْتِعَارَةُ.
File: `pages/65.0_nXX_عِلْمُ الْبَيَانِ التَّشْبِيهُ وَالِاسْتِعَارَةُ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/65.1_...` if page have a lot of blank space add exam elements from the lesson.
3. text Content: 100% Arabic with full Harakat.
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
6. Templates: You are forbidden from inventing new HTML tags or classes or template elements. You must map all content using "Jules-workspace/Templates/" components as the STREAM says in suitable way.
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). use "Jules-workspace/id_manager.py" to generate or verify them.
8. **Self-Correction:** Run "Jules-workspace/lint_pages.py" after creating html files. If it fails, you MUST fix the errors (usually inline styles) before submitting.
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
[LESSON_NUMBER]: 65
[CHAPTER_TITLE]: عِلْمُ الْبَيَانِ التَّشْبِيهُ وَالِاسْتِعَارَةُ
[CATEGORY_HEADER]: المستوى المتقدم
[SECTION_HEADER]: علم البلاغة
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: عِلْمُ البَيَانِ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: عِلْمُ البَيَانِ
Content: <p class="text-accent mb-0">عِلْمُ البَيَانِ يَهْتَمُّ بِالصُّورَةِ الْخَيَالِيَّةِ الَّتِي يَرْسُمُهَا الْكَاتِبُ لِيُوَضِّحَ الْفِكْرَةَ وَيَجْعَلَهَا مَحْسُوسَةً.</p>

=== BLOCK 3: أَوَّلًا - التَّشْبِيهُ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَوَّلًا - التَّشْبِيهُ
Content:
<p class="text-accent">هُوَ الرَّبْطُ بَيْنَ شَيْئَيْنِ بَيْنَهُمَا صِفَةٌ مُشْتَرَكَةٌ (مَعَ الْمُبَالَغَةِ).</p>
<p class="mb-0 font-bold">أَرْكَانُهُ الْأَرْبَعَةُ: "الرَّجُلُ (<span class="highlight-blue">الْمُشَبَّهُ</span>) كَـ (<span class="highlight-red">الْأَدَاةُ</span>) الْأَسَدِ (<span class="highlight-blue">الْمُشَبَّهُ بِهِ</span>) فِي الشَّجَاعَةِ (<span class="highlight-green">وَجْهُ الشَّبَهِ</span>)".</p>

=== BLOCK 4: أَنْوَاعُ التَّشْبِيهِ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَنْوَاعُ التَّشْبِيهِ (بِحَسَبِ مَوَجُودِ الأَرْكَانِ)
Content:
(Include TEMPLATE_C_LIST.html here with the following items using [LIST_ITEM_CONTENT])
Item 1: ١. تَشْبِيهٌ تَامُّ الأَرْكَانِ: مَوْجُودَةٌ كُلُّهَا. (الرَّجُلُ كَالْأَسَدِ فِي الشَّجَاعَةِ).
Item 2: ٢. تَشْبِيهٌ مُؤَكَّدٌ: حُذِفَتْ الْأَدَاةُ. لِيَكُونَ التَّشْبِيهُ أَقْوَى كَأَنَّهُمَا شَيْءٌ وَاحِدٌ. (الرَّجُلُ أَسَدٌ فِي الشَّجَاعَةِ).
Item 3: ٣. تَشْبِيهٌ مُجْمَلٌ: حُذِفَ وَجْهُ الشَّبَهِ، فَيُتْرَكُ لِخَيَالِ السَّامِعِ. (الرَّجُلُ كَالْأَسَدِ).
Item 4: ٤. تَشْبِيهٌ بَلِيغٌ (<span class="highlight-blue">أَقْوَى وَأَجْمَلُ الْأَنْوَاعِ!</span>): حُذِفَتْ الْأَدَاةُ وَوَجْهُ الشَّبَهِ مَعًا. بَقِيَ الْمُشَبَّهُ وَالْمُشَبَّهُ بِهِ فَقَطْ، كَأَنَّ الرَّجُلَ هُوَ الْأَسَدُ عَيْنُهُ. (الرَّجُلُ أَسَدٌ). (الْعِلْمُ نُورٌ).

=== BLOCK 5: خُلَاصَةُ أَنْوَاعِ التَّشْبِيهِ ===
(Component: TEMPLATE_C_TABLE.html)
Columns: نَوْعُ التَّشْبِيهِ | الْأَدَاةُ | وَجْهُ الشَّبَهِ | الْمِثَالُ
Row 1: تَشْبِيهٌ تَامُّ الأَرْكَانِ | مَوْجُودَةٌ | مَوْجُودٌ | الرَّجُلُ كَالْأَسَدِ فِي الشَّجَاعَةِ
Row 2: تَشْبِيهٌ مُؤَكَّدٌ | مَحْذُوفَةٌ | مَوْجُودٌ | الرَّجُلُ أَسَدٌ فِي الشَّجَاعَةِ
Row 3: تَشْبِيهٌ مُجْمَلٌ | مَوْجُودَةٌ | مَحْذُوفٌ | الرَّجُلُ كَالْأَسَدِ
Row 4: تَشْبِيهٌ بَلِيغٌ | مَحْذُوفَةٌ | مَحْذُوفٌ | الرَّجُلُ أَسَدٌ

=== BLOCK 6: ثَانِيًا - الاسْتِعَارَةُ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ثَانِيًا - الاسْتِعَارَةُ (التَّشْبِيهُ الْمُتَخَفِّي)
Content: <p class="text-accent mb-0">هِيَ فِي الْأَصْلِ تَشْبِيهٌ بَلِيغٌ، وَلَكِنَّنَا حَذَفْنَا أَحَدَ الرُّكْنَيْنِ الْأَسَاسِيَّيْنِ (الْمُشَبَّهَ أَوْ الْمُشَبَّهَ بِهِ). فَأَصْبَحَتْ خَيَالاً عَمِيقاً.</p>
<p class="mb-0 mt-2mm font-bold">أَنْوَاعُهَا الْمَشْهُورَةُ:</p>

=== BLOCK 7: أَنْوَاعُهَا الْمَشْهُورَةُ ===
(Component: TEMPLATE_C_SPLIT.html)
Side 1 (Right):
(Include TEMPLATE_C_BLOCK.html)
Title: ١. اسْتِعَارَةٌ تَصْرِيحِيَّةٌ
Content:
<p class="text-accent">نُصَرِّحُ بِمَا شَبَّهْنَا بِهِ. نَحْذِفُ الْمُشَبَّهَ الْأَصْلِيَّ، وَنَذْكُرُ الْمُشَبَّهَ بِهِ مُبَاشَرَةً.</p>
<p class="mb-0 font-bold">مِثَالٌ: يَقُولُ رَجُلٌ عَنِ ابْنَتِهِ: "<span class="highlight-red">جَاءَتْ الْقَمَرُ تَبْتَسِمُ</span>".</p>
<p class="mb-0 text-sm">(الْأَصْلُ: بِنْتِي كَالْقَمَرِ. حَذَفَ بِنْتِي (الْمُشَبَّهَ) وَصَرَّحَ بِالْقَمَرِ (الْمُشَبَّهَ بِهِ). إِذَنْ اسْتِعَارَةٌ تَصْرِيحِيَّةٌ).</p>

Side 2 (Left):
(Include TEMPLATE_C_BLOCK.html)
Title: ٢. اسْتِعَارَةٌ مَكْنِيَّةٌ (الْأَكْثَرُ شُيُوعاً)
Content:
<p class="text-accent">نَذْكُرُ الْمُشَبَّهَ، وَنَحْذِفُ الْمُشَبَّهَ بِهِ، وَنَكْنِي عَنْهُ (نَتْرُكُ دَلِيلاً أَوْ صِفَةً مِنْ صِفَاتِهِ تَدُلُّ عَلَيْهِ).</p>
<p class="mb-0 font-bold">مِثَالٌ: "<span class="highlight-blue">الْبَحْرُ يَضْحَكُ</span>".</p>
<p class="mb-0 text-sm">(شَبَّهَ الْبَحْرَ (الْمُشَبَّهَ مَوْجُودٌ) بِإِنْسَانٍ (الْمُشَبَّهُ بِهِ مَحْذُوفٌ)، وَتَرَكَ شَيْئاً مِنْ صِفَاتِهِ وَهُوَ (الضَّحِكُ) عَلَى سَبِيلِ الِاسْتِعَارَةِ الْمَكْنِيَّةِ).</p>

=== BLOCK 8: التَّشْخِيصُ ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: التَّشْخِيصُ (إِعْطَاءُ الْحَيَاةِ)
Content: <p class="mb-0">هُوَ مَنْحُ صِفَاتِ الْأَشْخَاصِ لِلْجَمَادَاتِ أَوْ لِلْمَعَانِي الْمُجَرَّدَةِ، لِتَبْدُوَ كَأَنَّهَا إِنْسَانٌ يَشْعُرُ وَيَتَكَلَّمُ. مِثْلَ السَّابِقِ (الْبَحْرُ يَضْحَكُ).</p>

=== BLOCK 9: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: حَدِّدْ نَوْعَ التَّشْبِيهِ: (الأُمُّ مَدْرَسَةٌ).

=== BLOCK 10: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: اشْرَحِ الصُّورَةَ الْبَيَانِيَّةَ: (بَكَى السَّحَابُ).

--- END STREAM ---