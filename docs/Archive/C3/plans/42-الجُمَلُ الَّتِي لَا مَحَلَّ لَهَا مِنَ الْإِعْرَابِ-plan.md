# **SESSION 42.0**

[TASK DEFINITION]
Objective: Implement الجُمَلُ الَّتِي لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.
File: `pages/42.0_nXX_الجُمَلُ الَّتِي لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/42.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 42
[CHAPTER_TITLE]: الجُمَلُ الَّتِي لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ
[CATEGORY_HEADER]: المستوى المتقدم
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. حنا خفيف
[AUTHOR_PHONE]:  

=== BLOCK 2: Definition & Rule ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَعْرِيفُ الْجُمَلِ الَّتِي لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ
Content: <p class="text-accent mb-2mm">هِيَ جُمَلٌ تُعْرَبُ كَلِمَاتُهَا إِعْرَابًا عَادِيًّا، لَكِنَّ الْجُمْلَةَ كَكُلٍّ لَا مَوْقِعَ لَهَا مِنَ الْإِعْرَابِ (أَيْ: لَيْسَتْ خَبَرًا، وَلَا صِفَةً، وَلَا حَالًا...). وَلَا يُمْكِنُ اسْتِبْدَالُهَا بِكَلِمَةٍ مُفْرَدَةٍ.</p>

=== BLOCK 3: The Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Table Content:
| النَّوْعُ | تَعْرِيفُهَا | مِثَالٌ |
|---|---|---|
| الْجُمْلَةُ الِابْتِدَائِيَّةُ | الَّتِي نَبْدَأُ بِهَا الْكَلَامَ فِي أَوَّلِ السَّطْرِ. | (<span class="highlight-red">الْعِلْمُ نُورٌ</span>) |
| الْجُمْلَةُ الِاسْتِئْنَافِيَّةُ | الَّتِي نَسْتَأْنِفُ (نُتَابِعُ) بِهَا الْكَلَامَ بَعْدَ فِكْرَةٍ مُسْتَقِلَّةٍ (أَوْ بَعْدَ فَاصِلَةٍ). | نَامَ الطِّفْلُ، (<span class="highlight-red">وَالْأُمُّ تَسْهَرُ</span>) |
| جُمْلَةُ صِلَةِ الْمَوْصُولِ | هِيَ الْجُمْلَةُ الَّتِي تَأْتِي بَعْدَ الِاسْمِ الْمَوْصُولِ لِتُوَضِّحَهُ. | جَاءَ الَّذِي (<span class="highlight-red">يُحِبُّكَ</span>) |
| الْجُمْلَةُ الِاعْتِرَاضِيَّةُ | الَّتِي تَعْتَرِضُ بَيْنَ الْمُبْتَدَأِ وَالْخَبَرِ، أَوْ بَيْنَ الْفِعْلِ وَالْفَاعِلِ. | الطَّبِيبُ - (<span class="highlight-red">وَالْحَقُّ يُقَالُ</span>) - أَنْقَذَ الْمَرِيضَ |
| جُمْلَةُ جَوَابِ الشَّرْطِ | الَّتِي تَأْتِي بَعْدَ أَدَوَاتٍ غَيْرِ جَازِمَةٍ. | إِذَا جِئْتَنِي (<span class="highlight-red">أَكْرَمْتُكَ</span>) |
| جُمْلَةُ جَوَابِ الْقَسَمِ | الَّتِي تَأْتِي بَعْدَ الْقَسَمِ (وَحَيَاتِكَ، لَعَمْرُكَ). | لَعَمْرُكَ (<span class="highlight-red">لَأَدْرُسَنَّ</span>) |
| الْجُمْلَةُ الْمَعْطُوفَةُ | الْمَعْطُوفَةُ عَلَى جُمْلَةٍ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ. | (<span class="highlight-red">الْعِلْمُ نُورٌ</span>) وَ(<span class="highlight-blue">الْجَهْلُ ظَلَامٌ</span>) |

=== BLOCK 4: Deep Dive - Part 1 ===
(Component: TEMPLATE_C_SPLIT.html)
LeftSide Component: TEMPLATE_C_BLOCK.html
LeftSide Title: ١- الْجُمْلَةُ الِابْتِدَائِيَّةُ وَالِاسْتِئْنَافِيَّةُ
LeftSide Content:
[TEMPLATE_C_LIST.html]
- **الِابْتِدَائِيَّةُ:** هِيَ الَّتِي نَبْدَأُ بِهَا الْكَلَامَ. مِثَالٌ: (<span class="highlight-red">الْعِلْمُ نُورٌ</span>). الْجُمْلَةُ الِابْتِدَائِيَّةُ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.
- **الِاسْتِئْنَافِيَّةُ:** هِيَ الَّتِي نَسْتَأْنِفُ (نُتَابِعُ) بِهَا الْكَلَامَ بَعْدَ فِكْرَةٍ مُسْتَقِلَّةٍ (أَوْ بَعْدَ فَاصِلَةٍ). مِثَالٌ: انْتَهَى الدَّرْسُ، (<span class="highlight-red">وَالطُّلَّابُ يَسْتَعِدُّونَ</span>).

RightSide Component: TEMPLATE_C_BLOCK.html
RightSide Title: ٢- جُمْلَةُ صِلَةِ الْمَوْصُولِ وَالِاعْتِرَاضِيَّةُ
RightSide Content:
[TEMPLATE_C_LIST.html]
- **صِلَةُ الْمَوْصُولِ:** هِيَ الْجُمْلَةُ الَّتِي تَأْتِي بَعْدَ الِاسْمِ الْمَوْصُولِ (الَّذِي، الَّتِي، الَّذِينَ، مَا، مَنْ) لِتُوَضِّحَهُ. مِثَالٌ: جَاءَ الَّذِي (<span class="highlight-red">يُحِبُّكَ</span>). جُمْلَةُ (يُحِبُّكَ) صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ دَائِمًا.
- **الِاعْتِرَاضِيَّةُ:** هِيَ الَّتِي تَعْتَرِضُ بَيْنَ الْمُبْتَدَأِ وَالْخَبَرِ، أَوْ بَيْنَ الْفِعْلِ وَالْفَاعِلِ (تُوضَعُ بَيْنَ شَرْطَتَيْنِ كَالتَّوْضِيحِ). مِثَالٌ: الطَّبِيبُ - (<span class="highlight-red">وَالْحَقُّ يُقَالُ</span>) - أَنْقَذَ الْمَرِيضَ. جُمْلَةُ (وَالْحَقُّ يُقَالُ) اعْتِرَاضِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.

=== BLOCK 5: Deep Dive - Part 2 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٣- جَوَابُ الشَّرْطِ، جَوَابُ الْقَسَمِ، وَالْمَعْطُوفَةُ
Content:
[TEMPLATE_C_LIST.html]
- **جُمْلَةُ جَوَابِ الشَّرْطِ (غَيْرِ الْجَازِمِ):** الَّتِي تَأْتِي بَعْدَ أَدَوَاتٍ غَيْرِ جَازِمَةٍ (إِذَا، لَوْ، لَوْلَا، كُلَّمَا). مِثَالٌ: إِذَا جِئْتَنِي (<span class="highlight-red">أَكْرَمْتُكَ</span>). جُمْلَةُ أَكْرَمْتُكَ لَا مَحَلَّ لَهَا. (وَكَذَلِكَ جَوَابُ الشَّرْطِ الْجَازِمِ الَّذِي لَيْسَ فِيهِ فَاءٌ).
- **جُمْلَةُ جَوَابِ الْقَسَمِ:** الَّتِي تَأْتِي بَعْدَ الْقَسَمِ (وَحَيَاتِكَ، لَعَمْرُكَ). مِثَالٌ: لَعَمْرُكَ (<span class="highlight-red">لَأَدْرُسَنَّ</span>). لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.
- **الْجُمْلَةُ الْمَعْطُوفَةُ عَلَى جُمْلَةٍ لَا مَحَلَّ لَهَا:** مِثَالٌ: (<span class="highlight-red">الْعِلْمُ نُورٌ</span>) وَ(<span class="highlight-blue">الْجَهْلُ ظَلَامٌ</span>). الْجُمْلَةُ الْأُولَى ابْتِدَائِيَّةٌ لَا مَحَلَّ لَهَا، وَالثَّانِيَةُ مَعْطُوفَةٌ عَلَيْهَا، فَهِيَ مِثْلُهَا لَا مَحَلَّ لَهَا.

=== BLOCK 6: Extra Info - Important Note ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: هَامَّةٌ جِدًّا!
Content: جُمْلَةُ صِلَةِ الْمَوْصُولِ هَامَّةٌ جِدًّا! تَأْتِي دَائِمًا بَعْدَ الِاسْمِ الْمَوْصُولِ (الَّذِي، الَّتِي، الَّذِينَ، مَا، مَنْ) وَلَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ دَائِمًا.

=== BLOCK 7: Extra Info - Rule Explanation ===
(Component: TEMPLATE_C_BENEFIT.html)
Title: فَائِدَةٌ إِعْرَابِيَّةٌ
Content: الْجُمَلُ الَّتِي لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ (لَا يُمْكِنُ اسْتِبْدَالُهَا بِكَلِمَةٍ مُفْرَدَةٍ)، وَلَيْسَتْ فِي مَحَلِّ رَفْعٍ أَوْ نَصْبٍ أَوْ جَرٍّ أَوْ جَزْمٍ كَخَبَرٍ أَوْ صِفَةٍ أَوْ حَالٍ.

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: بَيِّنِ الْمَحَلَّ الْإِعْرَابِيَّ لِلْجُمْلَةِ: "قَالَ الْمُعَلِّمُ: (<span class="highlight-red">الْعِلْمُ نُورٌ</span>)".

=== BLOCK 9: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: بَيِّنِ الْمَحَلَّ الْإِعْرَابِيَّ لِلْجُمْلَةِ: "جَاءَ الطَّالِبُ (<span class="highlight-red">وَهُوَ يَبْتَسِمُ</span>)".

=== BLOCK 10: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٣
Question: بَيِّنِ الْمَحَلَّ الْإِعْرَابِيَّ لِلْجُمْلَةِ: "هَذَا كِتَابٌ (<span class="highlight-red">أُسْلُوبُهُ رَائِعٌ</span>)".

=== BLOCK 11: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٤
Question: بَيِّنِ الْمَحَلَّ الْإِعْرَابِيَّ لِلْجُمْلَةِ: "جَاءَ الَّذِي (<span class="highlight-red">تَفَوَّقَ</span>)".

--- END STREAM ---
