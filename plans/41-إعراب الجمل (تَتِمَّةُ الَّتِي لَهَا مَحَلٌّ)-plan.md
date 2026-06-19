# **SESSION 41.0**

[TASK DEFINITION]
Objective: Implement إعراب الجمل (تَتِمَّةُ الَّتِي لَهَا مَحَلٌّ).
File: `pages/41.0_nXX_إعراب الجمل (تَتِمَّةُ الَّتِي لَهَا مَحَلٌّ).html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/41.1_...` if page have a lot of blank space add exam elements from the lesson.
3. text Content: 100% Arabic with full Harakat.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green`  for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   **Rule:** NO INLINE STYLES.
*   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
*   **Mapping:**
    *   inline style width: 20% -> `class="w-20pct"`
    *   inline style margin-top: 2mm -> `class="mt-2mm"`
    *   inline style text-align: center -> `class="text-center"`
    *   inline style font-weight: bold -> `class="font-bold"`
7. Templates: You are forbidden from inventing new HTML tags or classes or template elements. You must map all content using "Jules-workspace/Templates/" components as the STREAM says in suitable way.
8. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). use "Jules-workspace/id_manager.py" to generate or verify them.
9. **Self-Correction:** Run "Jules-workspace/lint_pages.py" after creating html files. If it fails, you MUST fix the errors (usually inline styles) before submitting.
10. Do not summarize examples.
11. Do not provide uncompleted text content using (...) .
12. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
13. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
14. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal
15. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
16. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !
17. Exam questions must be nested inside a content-block and block-body container.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 41
[CHAPTER_TITLE]: إعراب الجمل (تَتِمَّةُ الَّتِي لَهَا مَحَلٌّ)
[CATEGORY_HEADER]: المستوى المتقدم
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: الجدول الجامع ===
(Component: TEMPLATE_C_TABLE.html)
Headers: [نوع الجملة, المحل الإعرابي, مثال]
Row 1: [الجملة المضاف إليها, مَحَلُّهَا الْجَرُّ, سَأَلْتَقِيكَ يَوْمَ (نَنْجَحُ)]
Row 2: [جملة المفعول به, مَحَلُّهَا النَّصْبُ, قَالَ الْمُعَلِّمُ: (الِامْتِحَانُ سَهْلٌ)]
Row 3: [جملة جواب الشرط الجازم, مَحَلُّهَا الْجَزْمُ, مَنْ يَجْتَهِدْ (فَالنَّجَاحُ حَلِيفُهُ)]
Row 4: [الجملة المعطوفة, تَتْبَعُ السَّابِقَةَ لَهَا, كَانَ الطَّالِبُ (يَدْرُسُ) وَ(يَجْتَهِدُ)]

=== BLOCK 3: ٤- الجملة المضاف إليها ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٤- الْجُمْلَةُ الْمُضَافُ إِلَيْهَا (مَحَلُّهَا الْجَرُّ)
Content:
<span class="text-accent">تَأْتِي دَائِماً بَعْدَ الظُّرُوفِ كَـ <span class="highlight-blue">(يَوْمَ، حِينَ، حَيْثُ، إِذَا، لَمَّا، مُذْ)</span>.</span>
مِثَالٌ: سَأَلْتَقِيكَ يَوْمَ <span class="highlight-red">(نَنْجَحُ)</span>.
جُمْلَةُ (نَنْجَحُ) فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ.
هُنَالِكَ حَيْثُ <span class="highlight-red">(تَذُوبُ الْقُيُودُ)</span>.

=== BLOCK 4: ٥- جملة المفعول به ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٥- جُمْلَةُ الْمَفْعُولِ بِهِ (مَحَلُّهَا النَّصْبُ دَائِماً - جُمْلَةُ مَقُولِ الْقَوْلِ)
Content:
<span class="text-accent">تَأْتِي بَعْدَ الْقَوْلِ <span class="highlight-blue">(قَالَ، يَقُولُ، قُلْ)</span>.</span>
مِثَالٌ: قَالَ الْمُعَلِّمُ: <span class="highlight-red">(الِامْتِحَانُ سَهْلٌ)</span>.
جُمْلَةُ (الِامْتِحَانُ سَهْلٌ) فِي مَحَلِّ نَصْبِ مَفْعُولٍ بِهِ، أَوْ مَقُولِ الْقَوْلِ.

=== BLOCK 5: ٦- جملة جواب الشرط الجازم ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٦- جُمْلَةُ جَوَابِ الشَّرْطِ الْجَازِمِ (مَحَلُّهَا الْجَزْمُ)
Content:
<span class="text-accent">لَهَا شَرْطَانِ أَسَاسِيَّانِ لِاجْتِمَاعِهِمَا مَعاً:</span>

=== BLOCK 6: شروط جملة جواب الشرط ===
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: ١- الْأَدَاةُ جَازِمَةٌ <span class="highlight-blue">(إِنْ، مَنْ، مَتَى)</span>.
[LIST_ITEM_CONTENT]: ٢- الْجَوَابُ مُقْتَرِنٌ <span class="highlight-blue">بِالْفَاءِ</span>.

=== BLOCK 7: مثال جملة جواب الشرط الجازم ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مِثَالٌ عَلَى جُمْلَةِ جَوَابِ الشَّرْطِ
Content:
مَنْ يَجْتَهِدْ <span class="highlight-red">(فَالنَّجَاحُ حَلِيفُهُ)</span>.
الْجُمْلَةُ فِي مَحَلِّ جَزْمِ جَوَابِ الشَّرْطِ.

=== BLOCK 8: ملاحظة ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: مُلَاحَظَةٌ: إِذَا اخْتَلَّ أَحَدُ الشَّرْطَيْنِ، فَلَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.

=== BLOCK 9: ٧- الجملة المعطوفة ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٧- الْجُمْلَةُ الْمَعْطُوفَةُ (تَتْبَعُ الْجُمْلَةَ السَّابِقَةَ لَهَا)
Content:
<span class="text-accent">تَأْتِي بَعْدَ حَرْفِ عَطْفٍ. إِذَا كَانَتْ مَعْطُوفَةً عَلَى جُمْلَةٍ فِي مَحَلِّ نَصْبٍ، تَكُونُ مِثْلَهَا فِي مَحَلِّ نَصْبٍ.</span>
مِثَالٌ: كَانَ الطَّالِبُ <span class="highlight-blue">(يَدْرُسُ)</span> وَ<span class="highlight-red">(يَجْتَهِدُ)</span>.

=== BLOCK 10: إعراب أمثلة الجملة المعطوفة ===
(Component: TEMPLATE_C_IRAB_ROW.html)
Word 1: (يَدْرُسُ)
Details 1: خَبَرُ كَانَ فِي مَحَلِّ نَصْبٍ.
Word 2: (يَجْتَهِدُ)
Details 2: مَعْطُوفَةٌ عَلَيْهَا فِي مَحَلِّ نَصْبٍ.

=== BLOCK 11: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: حَدِّدِ الْجُمْلَةَ الَّتِي لَهَا مَحَلٌّ مِنَ الْإِعْرَابِ فِي الْأَمْثِلَةِ التَّالِيَةِ مَعَ ذِكْرِ مَحَلِّهَا: سَأَلْتَقِيكَ يَوْمَ نَنْجَحُ، قَالَ الْمُعَلِّمُ: الِامْتِحَانُ سَهْلٌ.
Number: ٢
Question: بَيِّنْ شُرُوطَ جُمْلَةِ جَوَابِ الشَّرْطِ لِتَكُونَ فِي مَحَلِّ جَزْمٍ.

--- END STREAM ---