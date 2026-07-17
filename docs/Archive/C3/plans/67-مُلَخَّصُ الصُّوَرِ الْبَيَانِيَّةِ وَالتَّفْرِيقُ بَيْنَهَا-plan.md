# **SESSION 67.0**

[TASK DEFINITION]
Objective: Implement مُلَخَّصُ الصُّوَرِ الْبَيَانِيَّةِ وَالتَّفْرِيقُ بَيْنَهَا.
File: `pages/67.0_nXX_مُلَخَّصُ الصُّوَرِ الْبَيَانِيَّةِ وَالتَّفْرِيقُ بَيْنَهَا.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/67.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 67
[CHAPTER_TITLE]: مُلَخَّصُ الصُّوَرِ الْبَيَانِيَّةِ وَالتَّفْرِيقُ بَيْنَهَا
[CATEGORY_HEADER]: المستوى المتقدم
[SECTION_HEADER]: علم البلاغة
[AUTHOR_NAME]: أ. حنا خفيف
[AUTHOR_PHONE]:  

=== BLOCK 2: [Topic] ===
(Component: TEMPLATE_C_BLOCK.html)
Title: كَيْفَ نُفَرِّقُ بَيْنَ أَنْوَاعِ الصُّوَرِ بِسُهُولَةٍ؟
Content:
<span class="text-accent">١. هَلْ يُمْكِنُ أَنْ يَحْدُثَ هَذَا فِي الْوَاقِعِ؟</span>

=== BLOCK 3: [Topic] ===
(Component: TEMPLATE_C_LIST.html)
List Item 1:
[LIST_ITEM_CONTENT]: نَعَمْ يُمْكِنُ: (فُلَانٌ كَثِيرُ الرَّمَادِ). إِذَنْ هِيَ كِنَايَةٌ (عَنْ صِفَةِ الْكَرَمِ لِكَثْرَةِ الطَّبْخِ).
List Item 2:
[LIST_ITEM_CONTENT]: لَا، خَيَالٌ مُسْتَحِيلٌ: (ضَحِكَ الزَّمَانُ). إِذَنْ نَنْتَقِلُ لِلسُّؤَالِ الثَّانِي.

=== BLOCK 4: [Topic] ===
(Component: TEMPLATE_C_BLOCK.html)
Title: كَيْفَ نُفَرِّقُ بَيْنَ أَنْوَاعِ الصُّوَرِ بِسُهُولَةٍ؟
Content:
<span class="text-accent">٢. هَلْ الطَّرَفَانِ (الْمُشَبَّهُ وَالْمُشَبَّهُ بِهِ) مَذْكُورَانِ مَعًا؟</span>

=== BLOCK 5: [Topic] ===
(Component: TEMPLATE_C_LIST.html)
List Item 1:
[LIST_ITEM_CONTENT]: نَعَمْ كِلَاهُمَا مَوْجُودٌ: (الْفَارِسُ أَسَدٌ). إِذَنْ هُوَ تَشْبِيهٌ بَلِيغٌ . (الْفَارِسُ كَالْأَسَدِ تَشْبِيهٌ تَامٌّ).
List Item 2:
[LIST_ITEM_CONTENT]: لَا، أَحَدُهُمَا مَحْذُوفٌ: (زَأَرَ الْفَارِسُ فِي الْمَعْرَكَةِ). حَذَفْنَا الْأَسَدَ. إِذَنْ هِيَ اسْتِعَارَةٌ (وَلِأَنَّنَا تَرَكْنَا صِفَةَ الزَّئِيرِ فَهِيَ مَكْنِيَّةٌ ).

=== BLOCK 6: [Topic] ===
(Component: TEMPLATE_C_TABLE.html)
Title: كَيْفَ نُفَرِّقُ بَيْنَ أَنْوَاعِ الصُّوَرِ بِسُهُولَةٍ؟
Row 1: هَلْ يُمْكِنُ أَنْ يَحْدُثَ هَذَا فِي الْوَاقِعِ؟ | نَعَمْ يُمْكِنُ | فُلَانٌ كَثِيرُ الرَّمَادِ | كِنَايَةٌ (عَنْ صِفَةِ الْكَرَمِ لِكَثْرَةِ الطَّبْخِ)
Row 2: هَلْ يُمْكِنُ أَنْ يَحْدُثَ هَذَا فِي الْوَاقِعِ؟ | لَا، خَيَالٌ مُسْتَحِيلٌ | ضَحِكَ الزَّمَانُ | نَنْتَقِلُ لِلسُّؤَالِ الثَّانِي
Row 3: هَلْ الطَّرَفَانِ (الْمُشَبَّهُ وَالْمُشَبَّهُ بِهِ) مَذْكُورَانِ مَعًا؟ | نَعَمْ كِلَاهُمَا مَوْجُودٌ | الْفَارِسُ أَسَدٌ | تَشْبِيهٌ بَلِيغٌ . (الْفَارِسُ كَالْأَسَدِ تَشْبِيهٌ تَامٌّ)
Row 4: هَلْ الطَّرَفَانِ (الْمُشَبَّهُ وَالْمُشَبَّهُ بِهِ) مَذْكُورَانِ مَعًا؟ | لَا، أَحَدُهُمَا مَحْذُوفٌ | زَأَرَ الْفَارِسُ فِي الْمَعْرَكَةِ | اسْتِعَارَةٌ (وَلِأَنَّنَا تَرَكْنَا صِفَةَ الزَّئِيرِ فَهِيَ مَكْنِيَّةٌ )

=== BLOCK 7: [Topic] ===
(Component: TEMPLATE_C_BENEFIT.html)
Content:
<span class="text-accent">كَيْفَ نُفَرِّقُ بَيْنَ أَنْوَاعِ الصُّوَرِ بِسُهُولَةٍ؟</span>

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: حَدِّدِ الصُّورَةَ الْبَيَانِيَّةَ فِي: "بَكَى الْيَتِيمُ دَماً".

=== BLOCK 9: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: حَدِّدْ نَوْعَ الْكِنَايَةِ فِي: "هُوَ نَظِيفُ الْيَدِ".

=== BLOCK 10: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٣
Question: حَدِّدِ الصُّورَةَ فِي: "أَبْنَاءُ النِّيلِ".

--- END STREAM ---