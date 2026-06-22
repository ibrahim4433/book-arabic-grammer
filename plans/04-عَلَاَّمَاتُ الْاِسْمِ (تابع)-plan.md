# **SESSION 04.0**

[TASK DEFINITION]
Objective: Implement عَلَاَّمَاتُ الْاِسْمِ .
File: `pages/04.0_nXX_عَلَاَّمَاتُ الْاِسْمِ .html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/04.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 04
[CHAPTER_TITLE]: عَلَاَّمَاتُ الْاِسْمِ 
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: ثَالِثًا أَسَمَاءُ مَبْنِيَّةُ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ثَالِثًا أَسَمَاءُ مَبْنِيَّةُ (أَنْوَاعَ خَاصَّةٍ مِن الْأَسْمَاءِ)
Content: <p class="text-accent">هُنَاك كَلِمَاتٍ فِي اللُّغَةَ الْعَرَبِيَّةَ هِي مِن الْأَسْمَاءِ بِالرَّغْمِ مِن أَنّهَا لَا تَتَغَيَّرُ حَرَكَتُهَا. وتُعرف بـ "الأسماء المبنية".</p>

=== BLOCK 3: تنبيه هام ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: <p>لَا يُمْكِنُ أَنْ نَضَعَ عَلَيْهَا ضَمَّةً أَوْ فَتْحَةً أَوْ كَسْرَةً حَسَبَ الْإِعْرَابِ بَلْ تَلْزَمُ حَالَةً وَاحِدَةً.</p>

=== BLOCK 4: أَسَمَاءَ الْإشَارَةِ و الْأَسْمَاءَ الْمَوْصُولَةَ ===
(Component: TEMPLATE_C_SPLIT.html)
[RIGHT_SIDE_CONTENT]:
(Component: TEMPLATE_C_BLOCK.html)
Title: ١. أَسَمَاءَ الْإشَارَةِ
Content:
(Component: TEMPLATE_C_CHIPS.html)
هَذَا، هَذِه، هَذَان، هَاتَان، هَؤُلَاء، ذَلِكَ، تِلْكَ
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: <span class="highlight-blue">هَذَا</span> طَالِبٌ مُجْتَهِدٌ.
[LIST_ITEM_CONTENT]: <span class="highlight-blue">هَذِه</span> شَجَرَةٌ مُثْمِرَةٌ.

[LEFT_SIDE_CONTENT]:
(Component: TEMPLATE_C_BLOCK.html)
Title: ٢. الْأَسْمَاءَ الْمَوْصُولَةَ
Content:
(Component: TEMPLATE_C_CHIPS.html)
الَّذِي، الَّتِي، الْلَذَان، الْلَتَان، الَّذِين، الْلَاتِي، الْلَائِي، مَنْ، مَا
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: جَاءَ <span class="highlight-blue">الَّذِي</span> نَجَحَ.
[LIST_ITEM_CONTENT]: قَرَأْتُ الْقِصَّةَ <span class="highlight-blue">الَّتِي</span> اشْتَرَيْتُهَا.

=== BLOCK 5: الضَّمَائِرَ و أَسَمَاءَ الْاِسْتِفْمُهِمِّ ===
(Component: TEMPLATE_C_SPLIT.html)
[RIGHT_SIDE_CONTENT]:
(Component: TEMPLATE_C_BLOCK.html)
Title: ٣. الضَّمَائِرَ
Content:
<p>(وَهِي كَثِيرَة جِدّاً، تُمَثِّل أَسْمَاء مُسْتَتِرَة أَوْ ظَاهِرَة)</p>
(Component: TEMPLATE_C_CHIPS.html)
هُو، هِي، أَنْتُم، هُم، نَحْن، أَنْتُمَا، أَنَا، أَنْتِ
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: <span class="highlight-blue">أَنَا</span> أُحِبُّ الْقِرَاءَةَ.
[LIST_ITEM_CONTENT]: <span class="highlight-blue">هُم</span> يَلْعَبُونَ.

[LEFT_SIDE_CONTENT]:
(Component: TEMPLATE_C_BLOCK.html)
Title: ٤. أَسَمَاءَ الْاِسْتِفْمُهِمِّ (الاستفهام)
Content:
(Component: TEMPLATE_C_CHIPS.html)
مَنٌّ، مَاذَا، لِمَاذَا، مَتَى، أَيْن، كَيْف، كَمْ، أَيُّ
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: <span class="highlight-blue">أَيْن</span> تَسْكُنُ؟
[LIST_ITEM_CONTENT]: <span class="highlight-blue">مَتَى</span> تَسْتَيْقِظُ؟

=== BLOCK 6: خُلَاصَةُ الْأَسْمَاءِ الْمَبْنِيَّةِ ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: نَوْعُ الِاسْمِ
[HEADER_2]: أَمْثِلَةٌ عَلَيْهِ
[ROW_1_COL_1]: أَسَمَاءَ الْإشَارَةِ
[ROW_1_COL_2]: هَذَا، هَذِه، هَذَان، هَاتَان، هَؤُلَاء، ذَلِكَ، تِلْكَ
[ROW_2_COL_1]: الْأَسْمَاءَ الْمَوْصُولَةَ
[ROW_2_COL_2]: الَّذِي، الَّتِي، الْلَذَان، الْلَتَان، الَّذِين، الْلَاتِي، الْلَائِي، مَنْ، مَا
[ROW_3_COL_1]: الضَّمَائِرَ
[ROW_3_COL_2]: هُو، هِي، أَنْتُم، هُم، نَحْن، أَنْتُمَا، أَنَا، أَنْتِ
[ROW_4_COL_1]: أَسَمَاءَ الْاِسْتِفْمُهِمِّ
[ROW_4_COL_2]: مَنٌّ، مَاذَا، لِمَاذَا، مَتَى، أَيْن، كَيْف، كَمْ، أَيُّ

=== BLOCK 7: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: اِسْتَخْرَجَ الْأَسْمَاءُ مِن بَيْن الْكَلِمَاتِ التَّالِيَةِ وَضَعَ خَطًّا تَحْتهَا : ( مُعَلِّمًا - إِلَى - شَجَرَةً - كَيْف - كَتَبٍّ - هَذِه )
Number: ٢
Question: اُذْكُرْ عُلَّامَةَ الْاِسْمِ فِي الْكَلِمَاتِ الْمُلَوَّنَةِ فِي الْجَمَلِ التَّالِيَةِ : ١. ذَهَبْتُ إِلَى الْحَديقَةِ الْعَظِيمَةَ . (الحَديقَةِ، العَظِيمَةَ). ٢. يَا طَالِبُ الْعِلْمِ . (طَالِبُ، الْعِلْمِ). ٣. رَأَيْتُ عَصْفُورًا يَطِيرُ . (عَصْفُورًا). ٤. الْقَلَمُ جَدِيدٌ . (الْقَلَمُ، جَدِيدٌ).
Number: ٣
Question: صَنَّفَ الْأَسْمَاءُ التَّالِيَةُ حَسْب دَلَالَتِهَا ( إِنْسَانٌ ، حَيَوَانَ / طَيْرٌ ، نَبَاتٌ ، جَمَادٌ ، صَفَّةً ، مَصْدَرٌ ، اِسْمَ إشَارَةٍ ، ضَمِيرٌ ، اِسْمَ اِسْتِفْمُهِمِّ ) : ١. هِنْدٌ ٢. خُرُوجٌ ٣. طَوِيلٌ ٤. نَحْن ٥. مَاذَا ٦. هَؤُلَاء ٧. فَرَاشَةٌ
Number: ٤
Question: هَلِ الْكَلِمَةُ ( الَّذِي ) مُعْرَبَةٌ أَمْ مَبْنِيَّةٌ ؟ وَمَا نَوْعُهَا مِنَ الْأَسْمَاءِ ؟

--- END STREAM ---