# **SESSION 17.0**

[TASK DEFINITION]
Objective: Implement الْجُمْلَةُ الِاسْمِيَّةُ (الْمُبْتَدَأُ وَالْخَبَرُ) وَإِعْرَابُهُمَا .
File: `pages/17.0_nXX_الْجُمْلَةُ الِاسْمِيَّةُ (الْمُبْتَدَأُ وَالْخَبَرُ) وَإِعْرَابُهُمَا .html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/17.1_...` if page have a lot of blank space add exam elements from the lesson.
3. text Content: 100% Arabic with full Harakat.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green`  for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   **Rule:** NO INLINE STYLES.
*   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
*   **Mapping:**
    *   inline style width: 20% -> class="w-20pct"
    *   inline style margin-top: 2mm -> class="mt-2mm"
    *   inline style text-align: center -> class="text-center"
    *   inline style font-weight: bold -> class="font-bold"
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

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 17
[CHAPTER_TITLE]: الْجُمْلَةُ الِاسْمِيَّةُ (الْمُبْتَدَأُ وَالْخَبَرُ) وَإِعْرَابُهُمَا 
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition & Rule ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَطْبِيقٌ إِضَافِيٌّ
Content:
<p class="text-accent mb-2mm">حَاوِلْ دَائِمًا تَقْسِيمَ الْجُمْلَةِ إِلَى كَلِمَاتٍ، ثُمَّ اسْأَلْ نَفْسَكَ: مَنِ الَّذِي نَتَحَدَّثُ عَنْهُ؟ هُوَ (<span class="highlight-blue font-bold">الْمُبْتَدَأُ</span>). وَمَاذَا نَقُولُ عَنْهُ؟ الْمَعْلُومَةُ هِيَ (<span class="highlight-red font-bold">الْخَبَرُ</span>).</p>
<p class="mb-0">لَوْ قُلْنَا: "<span class="highlight-blue">طَالِبُ</span> الْعِلْمِ الْمُجْتَهِدُ فِي دُرُوسِهِ <span class="highlight-red">نَاجِحٌ</span>".</p>

=== BLOCK 3: Deep Dive ===
(Component: TEMPLATE_C_SPLIT.html)
LeftSide:
(Component: TEMPLATE_C_BLOCK.html)
Title: اسْتِخْرَاجُ الْمُبْتَدَإِ
Content: مَنِ الَّذِي نَتَحَدَّثُ عَنْهُ؟ <span class="highlight-blue font-bold">طَالِبُ</span> (مُبْتَدَأٌ).
RightSide:
(Component: TEMPLATE_C_BLOCK.html)
Title: اسْتِخْرَاجُ الْخَبَرِ
Content: مَا بِهِ طَالِبُ الْعِلْمِ الْمُجْتَهِدُ فِي دُرُوسِهِ؟ الْجَوَابُ: (<span class="highlight-red font-bold">نَاجِحٌ</span>). إِذَنْ <span class="highlight-red">نَاجِحٌ</span> هُوَ الْخَبَرُ رَغْمَ تَأَخُّرِهِ فِي الْجُمْلَةِ.

=== BLOCK 4: Extra Info (Orange Alert) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content:
<p class="font-bold text-center mb-2mm">تَدْرِيبٌ سَرِيعٌ عَلَى تَعَدُّدِ الْخَبَرِ</p>
<p class="text-center mb-0">هَلْ يُمْكِنُ أَنْ يَكُونَ لِلْمُبْتَدَأِ الْوَاحِدِ أَكْثَرُ مِنْ خَبَرٍ؟ نَعَمْ، يَجُوزُ ذَلِكَ إِذَا كُنَّا نُخْبِرُ عَنْهُ بِعِدَّةِ صِفَاتٍ. تَأَمَّلِ الْجُمْلَةَ التَّالِيَةَ: (<span class="highlight-blue">الرُّمَّانُ</span> <span class="highlight-red">حُلْوٌ</span> <span class="highlight-red">حَامِضٌ</span> <span class="highlight-red">لَذِيذٌ</span>).</p>

=== BLOCK 5: Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Table Headers: [ الْكَلِمَةُ , إِعْرَابُهَا ]
Row 1: [ الرُّمَّانُ , مُبْتَدَأٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ. ]
Row 2: [ حُلْوٌ , خَبَرٌ أَوَّلُ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ. ]
Row 3: [ حَامِضٌ , خَبَرٌ ثَانٍ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ. ]
Row 4: [ لَذِيذٌ , خَبَرٌ ثَالِثٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ. ]

=== BLOCK 6: I'rab Details (Row 1) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
Box 1: (Component: TEMPLATE_C_IRAB_BOX.html)
Word: الرُّمَّانُ
Details: مُبْتَدَأٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ.
Box 2: (Component: TEMPLATE_C_IRAB_BOX.html)
Word: حُلْوٌ
Details: خَبَرٌ أَوَّلُ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ.

=== BLOCK 7: I'rab Details (Row 2) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
Box 1: (Component: TEMPLATE_C_IRAB_BOX.html)
Word: حَامِضٌ
Details: خَبَرٌ ثَانٍ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ.
Box 2: (Component: TEMPLATE_C_IRAB_BOX.html)
Word: لَذِيذٌ
Details: خَبَرٌ ثَالِثٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ.

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: اسْتَخْرِجِ الْمُبْتَدَأَ وَالْخَبَرَ مِنَ الْجُمْلَةِ التَّالِيَةِ: "طَالِبُ الْعِلْمِ الْمُجْتَهِدُ فِي دُرُوسِهِ نَاجِحٌ" وَبَيِّنْ إِعْرَابَهُمَا.

--- END STREAM ---