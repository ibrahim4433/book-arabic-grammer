# **SESSION 59.0**

[TASK DEFINITION]
Objective: Implement كَسْرُ هَمْزَةِ (إِنَّ) وَفَتْحُ هَمْزَةِ (أَنَّ).
File: `pages/59.0_nXX_كَسْرُ هَمْزَةِ (إِنَّ) وَفَتْحُ هَمْزَةِ (أَنَّ).html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/59.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 59
[CHAPTER_TITLE]: كَسْرُ هَمْزَةِ (إِنَّ) وَفَتْحُ هَمْزَةِ (أَنَّ)
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم الإملاء
[AUTHOR_NAME]: أ. حنا خفيف
[AUTHOR_PHONE]:  

=== BLOCK 2: تَعْرِيفٌ وَمُقَدِّمَةٌ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الْفَرْقُ بَيْنَ (<span class="highlight-red">إِنَّ</span>) الْمَكْسُورَةِ وَ (<span class="highlight-blue">أَنَّ</span>) الْمَفْتُوحَةِ
Content:
<p class="text-accent mb-2mm">
هُمَا حَرْفَانِ نَاسِخَانِ (مِنْ أَخَوَاتِ إِنَّ) لِلتَّوْكِيدِ. وَلَكِنْ لَا يَجُوزُ اسْتِخْدَامُهُمَا عَشْوَائِيّاً.
</p>
(Component injected: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: (<span class="highlight-red">إِنَّ</span>) بِالْكَسْرِ: تَأْتِي لِتَبْدَأَ جُمْلَةً جَدِيدَةً مُسْتَقِلَّةً بِنَفْسِهَا (قَوِيَّةٌ).
[LIST_ITEM_CONTENT]: (<span class="highlight-blue">أَنَّ</span>) بِالْفَتْحِ: تَأْتِي لِتُكَمِّلَ جُمْلَةً قَبْلَهَا، وَيُمْكِنُ تَحْوِيلُهَا مَعَ اسْمِهَا وَخَبَرِهَا إِلَى مَصْدَرٍ صَرِيحٍ (كَلِمَةٍ وَاحِدَةٍ).

=== BLOCK 3: التَّلْخِيصُ (جَدْوَلُ الْمُقَارَنَةِ) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مُلَخَّصُ قَوَاعِدِ (إِنَّ) وَ (أَنَّ)
Content:
(Component injected: TEMPLATE_C_TABLE.html)
Headers:
- الْحَرْفُ
- حَالَةُ الْهَمْزَةِ
- السَّبَبُ الْأَسَاسِيُّ
Rows:
- <span class="highlight-red">إِنَّ</span> | كَسْرٌ وُجُوباً | فِي بَدْءِ جُمْلَةٍ مُسْتَقِلَّةٍ (لَهَا صَدَارَةُ الْكَلَامِ).
- <span class="highlight-blue">أَنَّ</span> | فَتْحٌ وُجُوباً | يُمْكِنُ تَأْوِيلُهَا مَعَ مَعْمُولَيْهَا بِمَصْدَرٍ صَرِيحٍ.

=== BLOCK 4: مَتَى يَجِبُ فَتْحُ هَمْزَةِ (أَنَّ)؟ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مَتَى يَجِبُ فَتْحُ هَمْزَةِ (<span class="highlight-blue">أَنَّ</span>)؟ (حَالَةٌ وَاحِدَةٌ فَقَطْ)
Content:
<p class="text-accent mb-2mm">
تُفْتَحُ وُجُوباً إِذَا أَمْكَنَ تَأْوِيلُهَا مَعَ اسْمِهَا وَخَبَرِهَا بِمَصْدَرٍ صَرِيحٍ يَقَعُ (فَاعِلًا، مَفْعُولًا بِهِ، مُبْتَدَأً، مَجْرُورًا).
</p>
<p class="mb-2mm font-bold">أَمْثِلَةٌ:</p>
(Component injected: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: عَلِمْتُ (<span class="highlight-blue">أَنَّكَ</span> مُسَافِرٌ). = عَلِمْتُ سَفَرَكَ. (فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ).
[LIST_ITEM_CONTENT]: يَسُرُّنِي (<span class="highlight-blue">أَنَّكَ</span> نَاجِحٌ). = يَسُرُّنِي نَجَاحُكَ. (فِي مَحَلِّ رَفْعٍ فَاعِلٌ).

=== BLOCK 5: إِعْرَابُ أَمْثِلَةِ فَتْحِ الْهَمْزَةِ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: إِعْرَابٌ وَتَحْلِيلٌ
Content:
(Component injected: TEMPLATE_C_IRAB_ROW.html)
Box 1:
- [WORD]: أَنَّكَ مُسَافِرٌ
- [DETAILS]: الْمَصْدَرُ الْمُؤَوَّلُ مِنْ (<span class="highlight-blue">أَنَّ</span>) وَاسْمِهَا وَخَبَرِهَا فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.
Box 2:
- [WORD]: أَنَّكَ نَاجِحٌ
- [DETAILS]: الْمَصْدَرُ الْمُؤَوَّلُ مِنْ (<span class="highlight-blue">أَنَّ</span>) وَاسْمِهَا وَخَبَرِهَا فِي مَحَلِّ رَفْعٍ فَاعِلٌ.

=== BLOCK 6: مَتَى يَجِبُ كَسْرُ هَمْزَةِ (إِنَّ)؟ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مَتَى يَجِبُ كَسْرُ هَمْزَةِ (<span class="highlight-red">إِنَّ</span>)؟ (حَالَاتٌ كَثِيرَةٌ)
Content:
(Component injected: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: ١. فِي بَدْءِ الْكَلَامِ (أَوَّلُ كَلِمَةٍ فِي الْجُمْلَةِ): <span class="highlight-red">إِنَّ</span> النَّجَاحَ حَلِيفُ الْمُجْتَهِدِينَ.
[LIST_ITEM_CONTENT]: ٢. بَعْدَ الْقَوْلِ (قَالَ، يَقُولُ، قُلْ، قَالُوا): قُلْتُ: <span class="highlight-red">إِنَّ</span> الْجَوَّ جَمِيلٌ. (جُمْلَةُ مَقُولِ الْقَوْلِ).
[LIST_ITEM_CONTENT]: ٣. بَعْدَ الْقَسَمِ (وَالشَّمْسِ، لَعَمْرُكَ، بِالْعَهْدِ): وَالشَّمْسِ <span class="highlight-red">إِنَّ</span> النَّصْرَ قَرِيبٌ.
[LIST_ITEM_CONTENT]: ٤. إِذَا اتَّصَلَتْ بِخَبَرِهَا اللَّامُ الْمُزَحْلَقَةُ: عَلِمْتُ <span class="highlight-red">إِنَّكَ</span> لَمُسَافِرٌ. (وُجُودُ اللَّامِ فِي "لَمُسَافِرٌ" أَجْبَرَنَا عَلَى كَسْرِ إِنَّ مَعَ أَنَّ قَبْلَهَا فِعْلَ يَقِينٍ).
[LIST_ITEM_CONTENT]: ٥. فِي بَدْءِ جُمْلَةِ صِلَةِ الْمَوْصُولِ: جَاءَ الَّذِي <span class="highlight-red">إِنَّهُ</span> نَاجِحٌ.
[LIST_ITEM_CONTENT]: ٦. بَعْدَ (أَلَا) وَ (أَمَا) الِاسْتِفْتَاحِيَّتَيْنِ: أَلَا <span class="highlight-red">إِنَّ</span> الْمُخْلِصِينَ فِي رَاحَةٍ.

=== BLOCK 7: تَنْبِيهٌ مُهِمٌّ ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: تَنْبِيهٌ
Content: لَا يَجُوزُ اسْتِخْدَامُ (<span class="highlight-red">إِنَّ</span>) وَ (<span class="highlight-blue">أَنَّ</span>) عَشْوَائِيّاً، بَلْ يَجِبُ الِالْتِزَامُ بِالْقَوَاعِدِ الْمَذْكُورَةِ! كَمَا أَنَّ وُجُودَ اللَّامِ الْمُزَحْلَقَةِ فِي الْخَبَرِ يُجْبِرُنَا عَلَى كَسْرِ هَمْزَةِ إِنَّ حَتَّى لَوْ سُبِقَتْ بِفِعْلِ يَقِينٍ.

=== BLOCK 8: اخْتَبِرْ نَفْسَكَ ===
(Component: TEMPLATE_C_EXAM.html)
Header Class: bg-dark
Number: ١
Question: بَيِّنْ سَبَبَ كَسْرِ هَمْزَةِ (<span class="highlight-red">إِنَّ</span>) فِي جُمْلَةِ: (<span class="highlight-red">إِنَّ</span> الْعَمَلَ أَسَاسُ النَّجَاحِ).
Number: ٢
Question: بَيِّنْ سَبَبَ كَسْرِ هَمْزَةِ (<span class="highlight-red">إِنَّ</span>) فِي: (قَالَ الْمُعَلِّمُ: <span class="highlight-red">إِنَّ</span> الِامْتِحَانَ سَهْلٌ).
Number: ٣
Question: عَلِّلْ فَتْحَ هَمْزَةِ (<span class="highlight-blue">أَنَّ</span>) فِي: (يُعْجِبُنِي <span class="highlight-blue">أَنَّكَ</span> مُجْتَهِدٌ).

--- END STREAM ---