# **SESSION 71.0**

[TASK DEFINITION]
Objective: Implement مَلْحَقٌ خَاصٌّ الْبَحْثُ فِي الْمَعَاجِمِ الْعَرَبِيَّةِ.
File: `pages/71.0_nXX_مَلْحَقٌ خَاصٌّ الْبَحْثُ فِي الْمَعَاجِمِ الْعَرَبِيَّةِ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/71.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 71
[CHAPTER_TITLE]: مَلْحَقٌ خَاصٌّ الْبَحْثُ فِي الْمَعَاجِمِ الْعَرَبِيَّةِ
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم المعاجم
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: مُقَدِّمَةُ الْبَحْثِ وَالتَّجْرِيدِ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: كَيْفَ نَبْحَثُ عَنْ كَلِمَةٍ فِي الْقَامُوسِ (الْمُعْجَمِ)؟
Content:
<p class="mt-1mm text-accent">الْقَاعِدَةُ الْأُولَى وَالْأَهَمُّ: (<span class="highlight-red">التَّجْرِيدُ</span>).</p>
<p>لَا نَبْحَثُ عَنِ الْكَلِمَةِ بِشَكْلِهَا الْمُعَقَّدِ، بَلْ نُجَرِّدُهَا مِنْ حُرُوفِ الزِّيَادَةِ (<span class="highlight-blue">سَأَلْتُمُونِيهَا</span>) لِنُخْرِجَ الْجَذْرَ الثُّلَاثِيَّ الْأَصْلِيَّ (الْمَاضِي).</p>

=== BLOCK 3: أَمْثِلَةٌ عَلَى التَّجْرِيدِ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَمْثِلَةٌ عَمَلِيَّةٌ
Content:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: <span class="highlight-blue">اسْتِعْمَال</span> -> نَذْهَبُ إِلَى الْمَاضِي ثُمَّ نَحْذِفُ الزِّيَادَةَ -> <span class="highlight-red">عَمِلَ</span>. (ثَلَاثَةُ أَحْرُفٍ: ع، م، ل).
[LIST_ITEM_CONTENT]: <span class="highlight-blue">مُسَافِرُونَ</span> -> <span class="highlight-red">سَفَرَ</span>. (س، ف، ر).
[LIST_ITEM_CONTENT]: <span class="highlight-blue">مُسْتَشْفَى</span> -> <span class="highlight-red">شَفَيَ</span>. (ش، ف، ي).

=== BLOCK 4: طَرِيقَتَا الْمَعَاجِمِ فِي التَّرْتِيبِ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مَدْرَسَتَا الْمَعَاجِمِ
Content:
<p class="text-accent mt-1mm">بَعْدَ أَنْ حَصَلْنَا عَلَى الْجَذْرِ الثُّلَاثِيِّ (مِثْلًا: <span class="highlight-red">عَمِلَ</span>)، أَيْنَ نَبْحَثُ فِي الْكِتَابِ؟ يُوجَدُ مَدْرَسَتَانِ لِلْمَعَاجِمِ.</p>
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
<strong>تَنْبِيهٌ:</strong> <p class="m-0">الطَّرِيقَةُ الْقَدِيمَةُ السِّرِّيَّةُ الْعَجِيبَةُ! الْعَرَبُ قَدِيمًا رَتَّبُوا الْكُتُبَ حَسَبَ الْحَرْفِ الْأَخِيرِ (عَلَى الْقَافِيَةِ!).</p>

=== BLOCK 5: الْمُقَارَنَةُ بَيْنَ الْمَدْرَسَتَيْنِ ===
(Component: TEMPLATE_C_SPLIT.html)
[RIGHT_COLUMN]:
(Component: TEMPLATE_C_BLOCK.html)
Title: ١- مَعَاجِمُ الْأَوَائِلِ
Content:
<p class="mt-1mm font-bold text-primary">الطَّرِيقَةُ الْحَدِيثَةُ السَّهْلَةُ:</p>
<p>نَبْحَثُ فِي (بَابِ) الْحَرْفِ الْأَوَّلِ، ثُمَّ (فَصْلِ) الْحَرْفِ الثَّانِي، فَمَا بَعْدَهُ.</p>
<p>- (<span class="highlight-red">عَمِلَ</span>): نَبْحَثُ فِي بَابِ الْعَيْنِ (ع)، ثُمَّ الْمِيمِ (م)، ثُمَّ اللَّامِ (ل).</p>
<p class="mt-2mm font-bold text-accent">مِنْ أَشْهَرِهَا:</p>
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: الْمُعْجَمُ الْمَدْرَسِيُّ، الْمُعْجَمُ الْوَسِيطُ، الْمُنْجِدُ.
[LIST_ITEM_CONTENT]: مُخْتَارُ الصِّحَاحِ، الْمِصْبَاحُ الْمُنِيرُ.

[LEFT_COLUMN]:
(Component: TEMPLATE_C_BLOCK.html)
Title: ٢- مَعَاجِمُ الْأَوَاخِرِ
Content:
<p class="mt-1mm font-bold text-primary">الطَّرِيقَةُ الْقَدِيمَةُ:</p>
<p>فَنَبْحَثُ فِي (بَابِ) الْحَرْفِ الْأَخِيرِ، ثُمَّ نَرْجِعُ إِلَى (فَصْلِ) الْحَرْفِ الْأَوَّلِ، ثُمَّ الْحَرْفِ الْوَسَطِ.</p>
<p>- (<span class="highlight-red">عَمِلَ</span>): نَبْحَثُ فِي بَابِ الْحَرْفِ الْأَخِيرِ وَهُوَ اللَّامُ (ل)، ثُمَّ فَصْلِ الْحَرْفِ الْأَوَّلِ الْعَيْنِ (ع)، مَعَ مُرَاعَاةِ الثَّانِي الْمِيمِ (م).</p>
<p class="mt-2mm font-bold text-accent">مِنْ أَشْهَرِهَا:</p>
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: الْقَامُوسُ الْمُحِيطُ (لِلْفَيْرُوزْآبَادِي).
[LIST_ITEM_CONTENT]: لِسَانُ الْعَرَبِ (لِابْنِ مَنْظُورٍ)، تَاجُ الْعَرُوسِ.

=== BLOCK 6: مُلَخَّصُ قَوَاعِدِ الْبَحْثِ فِي الْمَعَاجِمِ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: خُلَاصَةُ الدَّرْسِ
Content:
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1] الْمَدْرَسَةُ
[HEADER_2] طَرِيقَةُ الْبَحْثِ
[HEADER_3] أَشْهَرُ الْمَعَاجِمِ
[CELL_1] مَعَاجِمُ الْأَوَائِلِ
[CELL_2] بَابُ الْأَوَّلِ، ثُمَّ فَصْلُ الثَّانِي
[CELL_3] الْمُعْجَمُ الْوَسِيطُ، مُخْتَارُ الصِّحَاحِ
[CELL_1] مَعَاجِمُ الْأَوَاخِرِ
[CELL_2] بَابُ الْأَخِيرِ، فَصْلُ الْأَوَّلِ
[CELL_3] لِسَانُ الْعَرَبِ، الْقَامُوسُ الْمُحِيطُ

=== BLOCK 7: Exam Section ===
(Component: TEMPLATE_C_BLOCK.html)
Header Classes: `block-header bg-dark`
Title:  اخْتِبِرْ نَفْسَكَ
Content:
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: كَيْفَ نَبْحَثُ عَنْ كَلِمَةِ (<span class="highlight-red">اسْتِعْمَال</span>) فِي مَعَاجِمِ الْأَوَاخِرِ؟
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: كَيْفَ نَبْحَثُ عَنْ كَلِمَةِ (<span class="highlight-red">مُسْتَشْفَى</span>) فِي مَعَاجِمِ الْأَوَائِلِ؟

--- END STREAM ---
