# **SESSION 36.0**

[TASK DEFINITION]
Objective: Implement مُقَدِّمَةُ التَّوَابِعِ.
File: `pages/36.0_nXX_مُقَدِّمَةُ التَّوَابِعِ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/36.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 36
[CHAPTER_TITLE]: مُقَدِّمَةُ التَّوَابِعِ
[CATEGORY_HEADER]: المستوى المتوسط
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition of Tawabee ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَعْرِيفُ التَّابِعِ
Content:
<p class="text-accent">التَّابِعُ: هُوَ لَفْظٌ مُتَأَخِّرٌ دَائِمًا يَتْبَعُ مَا قَبْلَهُ فِي حَالَتِهِ الْإِعْرَابِيَّةِ، يَتَقَيَّدُ فِي نَوْعِ إِعْرَابِهِ بِنَوْعِ الْإِعْرَابِ فِي لَفْظٍ مُعَيَّنٍ مُتَقَدِّمٍ عَلَيْهِ (الْمَتْبُوعُ). إِذَا كَانَ الْمَتْبُوعُ مَرْفُوعاً، كَانَ التَّابِعُ مَرْفُوعاً، وَهَكَذَا.</p>
أَنْوَاعُ التَّوَابِعِ الْأَرْبَعَةِ هِيَ فَقَطْ:
(Component: TEMPLATE_C_CHIPS.html)
- الصِّفَةُ (النَّعْتُ).
- الِاسْمُ الْمَعْطُوفُ.
- التَّوْكِيدُ.
- الْبَدَلُ.

=== BLOCK 3: The Core Matrix (Summary Table) ===
(Component: TEMPLATE_C_TABLE.html)
Title: مُلَخَّصُ التَّوَابِعِ
Headers:
- [HEADER_1]: التَّابِعُ
- [HEADER_2]: التَّعْرِيفُ
- [HEADER_3]: الْفَائِدَةُ
- [HEADER_4]: مِثَالٌ

Rows:
Row 1:
- النَّعْتُ (الصِّفَةُ)
- تَابِعٌ يُذْكَرُ لِبَيَانِ صِفَةٍ فِي مَتْبُوعِهِ.
- التَّوْضِيحُ (إِذَا كَانَ مَعْرِفَةً كَالرَّجُلِ الْكَرِيمِ)، التَّخْصِيصُ (نَكِرَةٌ كَرَجُلٍ كَرِيمٍ)
- جَاءَ رَجُلٌ <span class="highlight-red">كَرِيمٌ</span> .
Row 2:
- الْعَطْفُ
- تَابِعٌ يَتَوَسَّطُ بَيْنَهُ وَبَيْنَ مَتْبُوعِهِ حَرْفُ عَطْفٍ.
- الْمُشَارَكَةُ فِي الْحُكْمِ كَالْمَجِيءِ.
- جَاءَ سَعِيدٌ <span class="highlight-blue">وَ</span><span class="highlight-red">خَالِدٌ</span> .
Row 3:
- التَّوْكِيدُ
- تَابِعٌ يُذْكَرُ لِتَقْوِيَةِ مَتْبُوعِهِ وَإِزَالَةِ الشَّكِّ عَنِ السَّامِعِ.
- تَرْسِيخُ الْمَعْنَى (إِمَّا لَفْظِيّ بِتَكْرَارِ الْكَلِمَةِ أَوْ مَعْنَوِيّ بِكَلِمَةِ "نَفْسِهِ").
- جَاءَ الْأَمِيرُ <span class="highlight-red">نَفْسُهُ</span> . أَوْ جَاءَ الْأَمِيرُ <span class="highlight-red">الْأَمِيرُ</span> .
Row 4:
- الْبَدَلُ
- تَابِعٌ مَقْصُودٌ بِالْحُكْمِ بِلَا وَاسِطَةِ حَرْفِ عَطْفٍ.
- تَوْضِيحُ الْمَقْصُودِ بِدِقَّةٍ (كَذِكْرِ اسْمِ الشَّخْصِ بَعْدَ لَقَبِهِ).
- حَضَرَ الْمُدِيرُ <span class="highlight-red">خَالِدٌ</span> .

=== BLOCK 4: Deep Dive into Sifah ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ١- الصِّفَةُ (النَّعْتُ)
Content:
الصِّفَةُ تَأْتِي بَعْدَ اسْمٍ يُدْعَى (الْمَوْصُوفَ)، وَيُعْرَبُ الْمَوْصُوفُ بِحَسَبِ مَوْقِعِهِ فِي الْجُمْلَةِ (فَاعِل، مَفْعُول...).
أَوْجُهُ الْمُطَابَقَةِ (الصِّفَةُ تَقْلِيدٌ أَعْمَى لِلْمَوْصُوفِ فِي أَرْبَعَةِ أَشْيَاءَ):
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: <span class="font-bold">الْإِفْرَادُ أَوِ التَّثْنِيَةُ أَوِ الْجَمْعُ</span> (مُفْرَدٌ مَعَ مُفْرَدٍ، جَمْعٌ مَعَ جَمْعٍ).
[LIST_ITEM_CONTENT]: <span class="font-bold">التَّذْكِيرُ أَوِ التَّأْنِيثُ</span> (ذَكَرٌ مَعَ ذَكَرٍ، مُؤَنَّثٌ مَعَ أُنْثَى).
[LIST_ITEM_CONTENT]: <span class="font-bold">التَّعْرِيفُ أَوِ التَّنْكِيرُ</span> (بِـ الـ، أَوْ بِدُونِ الـ).
[LIST_ITEM_CONTENT]: <span class="font-bold">الْعَلَامَةُ الْإِعْرَابِيَّةُ</span> (الرَّفْعُ، النَّصْبُ، الْجَرُّ).

=== BLOCK 5: Examples of Sifah ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title:  أَمْثِلَةٌ عَلَى الْمُطَابَقَةِ التَّامَّةِ
Content:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: (صَاحِبْ إِنسَانًا <span class="highlight-red">صَادِقًا</span> ) كِلَاهُمَا مُفْرَدٌ مُذَكَّرٌ نَكِرَةٌ مَنْصُوبٌ.
[LIST_ITEM_CONTENT]: (شَاهَدْتُ زَهْرَتَيْنِ <span class="highlight-red">جَمِيلَتَيْنِ</span> ) كِلَاهُمَا مُثَنَّى مُؤَنَّثٌ نَكِرَةٌ مَنْصُوبٌ بِالْيَاءِ.
[LIST_ITEM_CONTENT]: (سَلَّمْتُ عَلَى الرِّجَالِ <span class="highlight-red">الْأَبْطَالِ</span> ) كِلَاهُمَا جَمْعٌ مُذَكَّرٌ مَعْرِفَةٌ مَجْرُورٌ.

=== BLOCK 6: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: اسْتَخْرِجِ التَّابِعَ وَبَيِّنْ نَوْعَهُ فِي الْأَمْثِلَةِ السَّابِقَةِ:

--- END STREAM ---