# **SESSION 20.0**

[TASK DEFINITION]
Objective: Implement الْمُبْتَدَأُ وَالْخَبَرُ (مُتَقَدِّمٌ).
File: `pages/20.0_nXX_الْمُبْتَدَأُ وَالْخَبَرُ (مُتَقَدِّمٌ).html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/20.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 20
[CHAPTER_TITLE]: الْمُبْتَدَأُ وَالْخَبَرُ (مُتَقَدِّمٌ)
[CATEGORY_HEADER]: المستوى المتقدم
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition & Rule - Introduction ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مَرْتَبَةُ الْمُبْتَدَأِ وَالْخَبَرِ (وُجُوبُ التَّقْدِيمِ لِلْخَبَرِ)
Content: <p class="text-accent">الْأَصْلُ فِي الْمُبْتَدَأِ أَنْ يَتَقَدَّمَ عَلَى الْخَبَرِ، وَيَجُوزُ الْعَكْسُ (مِثْلَ: مَمْنُوعٌ التَّدْخِينُ). وَلَكِنْ هُنَاكَ حَالَاتٌ يَتَقَدَّمُ فِيهَا الْخَبَرُ عَلَى الْمُبْتَدَأِ وُجُوبًا (أَيْ لَا خِيَارَ لَكَ):</p>

=== BLOCK 3: The Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Title: مُلَخَّصُ وُجُوبِ تَقْدِيمِ وَحَذْفِ الْخَبَرِ
Content:
Headers: <th>الْقَاعِدَةُ</th> <th>الْحَالَةُ</th> <th>الْمِثَالُ</th>
Rows:
- وُجُوبُ تَقْدِيمِ الْخَبَرِ | الْخَبَرُ شِبْهُ جُمْلَةٍ وَالْمُبْتَدَأُ نَكِرَةٌ | فِي الْقَفَصِ عُصْفُورٌ
- وُجُوبُ تَقْدِيمِ الْخَبَرِ | فِي الْمُبْتَدَأِ ضَمِيرٌ يَعُودُ عَلَى بَعْضِ الْخَبَرِ | لِلتَّفَوُّقِ ثَمَنُهُ
- وُجُوبُ تَقْدِيمِ الْخَبَرِ | الْخَبَرُ مِنْ أَسْمَاءِ الِاسْتِفْهَامِ | مَنْ أَنْتَ؟
- وُجُوبُ حَذْفِ الْخَبَرِ | بَعْدَ لَوْلَا الشَّرْطِيَّةِ | لَوْلَا الْكِتَابَةُ لَضَاعَ الْعِلْمُ
- وُجُوبُ حَذْفِ الْخَبَرِ | بَعْدَ الْقَسَمِ الصَّرِيحِ | لَعَمْرُكَ لَأَقُولَنَّ الْحَقَّ

=== BLOCK 4: Deep Dive - حالات التقديم ===
(Component: TEMPLATE_C_BLOCK.html)
Title: حَالَاتُ وُجُوبِ تَقْدِيمِ الْخَبَرِ
Content:
[TEMPLATE_C_LIST.html injected here]
Items:
- ١ إِذَا كَانَ الْخَبَرُ شِبْهَ جُمْلَةٍ (جَارٌّ وَمَجْرُورٌ، أَوْ ظَرْفٌ) وَالْمُبْتَدَأُ نَكِرَةٌ ، نَحْوُ: ( <span class="highlight-blue">فِي الْقَفَصِ</span> عُصْفُورٌ )، ( <span class="highlight-blue">عِنْدَكَ</span> كِتَابٌ ).
- ٢ إِذَا كَانَ فِي الْمُبْتَدَأِ ضَمِيرٌ يَعُودُ عَلَى بَعْضِ الْخَبَرِ ، نَحْوُ: ( <span class="highlight-blue">لِلتَّفَوُّقِ</span> ثَمَنُهُ ).
- ٣ إِذَا كَانَ الْخَبَرُ مِنْ أَسْمَاءِ الِاسْتِفْهَامِ الَّتِي لَهَا الصَّدَارَةُ فِي الْكَلَامِ دَائِماً، نَحْوُ: ( <span class="highlight-blue">مَنْ</span> أَنْتَ ؟ ) أَوْ ( <span class="highlight-blue">أَيْنَ</span> الطَّرِيقُ ؟ ). "<span class="highlight-blue">أَيْنَ</span>" خَبَرٌ مُقَدَّمٌ.

=== BLOCK 5: Extra Info - Warning ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: تَنْبِيهٌ هَامٌّ
Content: لَا يُمْكِنُ أَنْ نَقُولَ (ثَمَنُهُ لِلتَّفَوُّقِ) حَتَّى لَا يَعُودَ الضَّمِيرُ عَلَى مُتَأَخِّرٍ.

=== BLOCK 6: Definition & Rule - مواطن حذف الخبر ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَشْهَرُ مَوَاطِنِ حَذْفِ الْخَبَرِ (الْخَبَرُ غَيْرُ مَوْجُودٍ فِي الْجُمْلَةِ)
Content: <p class="text-accent">يُحْذَفُ خَبَرُ الْمُبْتَدَأِ وُجُوبًا (يَفْهَمُهُ السَّامِعُ وَلَا يُذْكَرُ) فِي مَوَاضِعَ، مِنْهَا:</p>

=== BLOCK 7: Deep Dive - مواضع الحذف ===
(Component: TEMPLATE_C_SPLIT.html)
LeftSide:
  (Component: TEMPLATE_C_BLOCK.html)
  Title: ١ بَعْدَ لَوْلَا الشَّرْطِيَّةِ
  Content: مِثَالُ: ( <span class="highlight-blue">لَوْلَا</span> الْكِتَابَةُ لَضَاعَ الْعِلْمُ ). التَّقْدِيرُ: لَوْلَا الْكِتَابَةُ <span class="highlight-red">مَوْجُودَةٌ</span> لَضَاعَ الْعِلْمُ. فَالْخَبَرُ مَحْذُوفٌ تَقْدِيرُهُ "<span class="highlight-red">مَوْجُودٌ</span>".
RightSide:
  (Component: TEMPLATE_C_BLOCK.html)
  Title: ٢ بَعْدَ الْقَسَمِ الصَّرِيحِ
  Content: مِثَالُ: ( <span class="highlight-blue">لَعَمْرُكَ</span> لَأَقُولَنَّ الْحَقَّ ). التَّقْدِيرُ: لَعَمْرُكَ <span class="highlight-red">قَسَمِي</span> . فَالْخَبَرُ مَحْذُوفٌ تَقْدِيرُهُ "<span class="highlight-red">قَسَمِي</span>".

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: عَيِّنِ الْخَبَرَ الْمُقَدَّمَ وُجُوبًا فِي الْجُمْلَةِ الْآتِيَةِ: (فِي الْقَفَصِ عُصْفُورٌ).
Number: ٢
Question: قَدِّرِ الْخَبَرَ الْمَحْذُوفَ وُجُوبًا فِي: (لَوْلَا الْكِتَابَةُ لَضَاعَ الْعِلْمُ).
Number: ٣
Question: مَا السَّبَبُ فِي وُجُوبِ تَقْدِيمِ الْخَبَرِ فِي جُمْلَةِ: (مَنْ أَنْتَ ؟) ؟

--- END STREAM ---