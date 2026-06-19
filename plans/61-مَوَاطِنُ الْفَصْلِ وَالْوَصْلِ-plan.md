# **SESSION 61.0**

[TASK DEFINITION]
Objective: Implement مَوَاطِنُ الْفَصْلِ وَالْوَصْلِ.
File: `pages/61.0_nXX_مَوَاطِنُ الْفَصْلِ وَالْوَصْلِ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/61.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 61
[CHAPTER_TITLE]: مَوَاطِنُ الْفَصْلِ وَالْوَصْلِ
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم الإملاء
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: أَحْكَامُ (مَا) الاِسْمِيَّةِ وَالْحَرْفِيَّةِ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَحْكَامُ (مَا) الاِسْمِيَّةِ وَالْحَرْفِيَّةِ
Content: <p class="mt-1mm text-accent">مَتَى نَكْتُبُ (<span class="highlight-blue">مَا</span>) مُتَّصِلَةً بِالْكَلِمَةِ الَّتِي قَبْلَهَا؟ وَمَتَى نَفْصِلُهَا؟</p>

=== BLOCK 3: تَفْصِيلُ أَحْكَامِ (مَا) ===
(Component: TEMPLATE_C_SPLIT.html)
Right Column:
(Component: TEMPLATE_C_BLOCK.html)
Title: ١. (مَا) مَوْصُولَةٌ (تُكْتَبُ مُتَّصِلَةً بِالْكَلِمَةِ):
Content:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: إِذَا كَانَتْ حَرْفاً يَكُفُّ (<span class="highlight-blue">إِنَّ</span>) عَنِ الْعَمَلِ: <span class="highlight-red">إِنَّمَا</span> الصِّحَّةُ كَنْزٌ. (<span class="highlight-blue">إِنَّ</span> + <span class="highlight-blue">مَا</span> = <span class="highlight-red">إِنَّمَا</span>).
[LIST_ITEM_CONTENT]: إِذَا كَانَتْ مَعَ أَدَوَاتِ الشَّرْطِ: <span class="highlight-red">أَيْنَمَا</span> تَذْهَبْ أَذْهَبْ. <span class="highlight-red">كُلَّمَا</span> حَضَرَ الْمُعَلِّمُ سَكَتُوا.

Left Column:
(Component: TEMPLATE_C_BLOCK.html)
Title: ٢. (مَا) مَفْصُولَةٌ (تُكْتَبُ لِوَحْدِهَا بَعِيدَةً):
Content:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: إِذَا كَانَتْ اسْماً مَوْصُولاً بِمَعْنَى (الَّذِي): إِنَّ <span class="highlight-red">مَا</span> تَقُولُهُ صَحِيحٌ. (أَيْ: إِنَّ الَّذِي تَقُولُهُ.. لَاحِظْ هُنَا <span class="highlight-red">مَا</span> اسْمُ إِنَّ). أُحِبُّ كُلَّ <span class="highlight-red">مَا</span> تَفْعَلُهُ.

=== BLOCK 4: أَحْكَامُ (لَا) النَّافِيَةِ مَعَ (أَنْ) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَحْكَامُ (لَا) النَّافِيَةِ مَعَ (أَنْ)
Content:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: ١. مُتَّصِلَةٌ بَعْضُهَا بِبَعْضٍ وَتُدْغَمُ النُّونُ (<span class="highlight-red">أَلَّا</span>): إِذَا جَاءَتْ (<span class="highlight-blue">أَنْ</span>) حَرْفَ نَصْبٍ لِلْمُضَارِعِ. مِثْلُ: يَجِبُ <span class="highlight-red">أَلَّا</span> تَتَأَخَّرَ. (<span class="highlight-blue">أَنْ</span> + <span class="highlight-blue">لَا</span> = <span class="highlight-red">أَلَّا</span>). لِكَيْلَا تَرْسُبَ.
[LIST_ITEM_CONTENT]: ٢. مَفْصُولَةٌ (<span class="highlight-red">أَنْ لَا</span>): إِذَا كَانَتْ (<span class="highlight-blue">أَنْ</span>) مُخَفَّفَةً مِنْ "أَنَّ" وَيَأْتِي بَعْدَهَا اسْمٌ غَالِباً. مِثْلُ: أَيْقَنْتُ <span class="highlight-red">أَنْ لَا</span> عُذْرَ لَكَ.

=== BLOCK 5: الظُّرُوفُ مَعَ (إِذْ) ===
(Component: TEMPLATE_C_BLOCK.html)
*Note: Use `.block-header.accent` for orange color balance.*
Title: الظُّرُوفُ مَعَ (إِذْ)
Content:
<p class="mt-1mm text-accent">هَلْ نَكْتُبُ (<span class="highlight-blue">يَوْمَ إِذٍ</span>) أَمْ (<span class="highlight-red">يَوْمَئِذٍ</span>)؟</p>
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: ١. مُتَّصِلَةٌ: إِذَا وَضَعْنَا تَنْوِيناً فِي آخِرِ كَلِمَةِ (<span class="highlight-blue">إِذٍ</span>). مِثْلُ: <span class="highlight-red">يَوْمَئِذٍ</span>، <span class="highlight-red">حِينَئِذٍ</span>، <span class="highlight-red">وَقْتَئِذٍ</span>.
[LIST_ITEM_CONTENT]: ٢. مَفْصُولَةٌ: إِذَا لَمْ نَضَعْ تَنْوِيناً، بَلْ بَقِيَتْ حَرَكَةُ السُّكُونِ. مِثْلُ: يَوْمَ <span class="highlight-red">إِذْ</span> حَدَثَ كَذَا. حِينَ <span class="highlight-red">إِذْ</span>.

=== BLOCK 6: الْمُصْفُوفَةُ الْأَسَاسِيَّةُ (مُلَخَّصُ الدَّرْسِ) ===
(Component: TEMPLATE_C_TABLE.html)
Table Headers: | الْكَلِمَةُ | حَالَةُ الْوَصْلِ (مُتَّصِلَةٌ) | حَالَةُ الْفَصْلِ (مَفْصُولَةٌ) |
Table Rows:
| (مَا) | إِنَّمَا، أَيْنَمَا، كُلَّمَا | إِنَّ مَا تَقُولُهُ صَحِيحٌ، كُلَّ مَا تَفْعَلُهُ |
| (لَا) مَعَ (أَنْ) | أَلَّا تَتَأَخَّرَ، لِكَيْلَا تَرْسُبَ | أَنْ لَا عُذْرَ لَكَ |
| الظُّرُوفُ مَعَ (إِذْ) | يَوْمَئِذٍ، حِينَئِذٍ، وَقْتَئِذٍ | يَوْمَ إِذْ، حِينَ إِذْ |

=== BLOCK 7: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: مَيِّزْ بَيْنَ حَالَتَيِ الْفَصْلِ وَالْوَصْلِ، مَعَ بَيَانِ السَّبَبِ فِي الْجُمَلِ التَّالِيَةِ: إِنَّمَا الصِّحَّةُ كَنْزٌ.

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: مَيِّزْ بَيْنَ حَالَتَيِ الْفَصْلِ وَالْوَصْلِ، مَعَ بَيَانِ السَّبَبِ فِي الْجُمَلِ التَّالِيَةِ: أَيْقَنْتُ أَنْ لَا عُذْرَ لَكَ.

=== BLOCK 9: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٣
Question: مَيِّزْ بَيْنَ حَالَتَيِ الْفَصْلِ وَالْوَصْلِ، مَعَ بَيَانِ السَّبَبِ فِي الْجُمَلِ التَّالِيَةِ: يَوْمَ إِذْ حَدَثَ كَذَا.

--- END STREAM ---
