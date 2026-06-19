# **SESSION 70.0**

[TASK DEFINITION]
Objective: Implement الْمُوسِيقَا الشِّعْرِيَّةُ (نَبْضُ الْقَصِيدَةِ).
File: `pages/70.0_nXX_الْمُوسِيقَا الشِّعْرِيَّةُ (نَبْضُ الْقَصِيدَةِ).html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/70.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 70
[CHAPTER_TITLE]: الْمُوسِيقَا الشِّعْرِيَّةُ (نَبْضُ الْقَصِيدَةِ)
[CATEGORY_HEADER]: المستوى المتقدم
[SECTION_HEADER]: علم البلاغة
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: أقسام الموسيقا الشعرية ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَقْسَامُ الْمُوسِيقَا الشِّعْرِيَّةِ
Content:
<p class="text-accent">تَنْقَسِمُ الْمُوسِيقَا فِي أَيِّ قَصِيدَةٍ إِلَى قِسْمَيْنِ لِيَكْتَمِلَ الْجَمَالُ الصَّوْتِيُّ:</p>
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: <span class="highlight-blue">الْمُوسِيقَا الْخَارِجِيَّةُ</span> (الْهَيْكَلُ الْعَامُّ الْوَاضِحُ).
[LIST_ITEM_CONTENT]: <span class="highlight-blue">الْمُوسِيقَا الدَّاخِلِيَّةُ</span> (الْإِيقَاعُ الْخَفِيُّ فِي الدَّاخِلِ).

=== BLOCK 3: أولاً: الموسيقا الخارجية ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَوَّلًا: الْمُوسِيقَا الْخَارِجِيَّةُ (أَسَاسُ الشِّعْرِ)
Content:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: <span class="highlight-blue">الْوَزْنُ الْعَرُوضِيُّ (الْبَحْرُ):</span> هُوَ الْإِيقَاعُ الْعَامُّ الَّذِي يَمْشِي عَلَيْهِ الشَّاعِرُ (كَأَنَّهُ لَحْنُ الْأُغْنِيَةِ).
[LIST_ITEM_CONTENT]: <span class="highlight-blue">الْقَافِيَةُ:</span> هِيَ الْمَقْطَعُ الصَّوْتِيُّ الْأَخِيرُ الَّذِي تَنْتَهِي بِهِ الْأَبْيَاتُ (مِنْ آخِرِ سَاكِنٍ إِلَى السَّاكِنِ الَّذِي قَبْلَهُ).
[LIST_ITEM_CONTENT]: <span class="highlight-blue">حَرْفُ الرَّوِيِّ:</span> هُوَ الْحَرْفُ النِّهَائِيُّ الَّذِي تُبْنَى عَلَيْهِ الْقَصِيدَةُ وَتُسَمَّى بِاسْمِهِ (إِذَا كَانَ "بَاء" سُمِّيَتْ <span class="highlight-green">بَائِيَّةً</span>).

=== BLOCK 4: مثال على الموسيقا الخارجية ===
(Component: TEMPLATE_C_POEM.html)
Line 1 Hemistich 1: عَلَى قَدْرِ أَهْلِ الْعَزْمِ تَأْتِي الْعَزَائِمُ
Line 1 Hemistich 2: وَتَأْتِي عَلَى قَدْرِ الْكِرَامِ الْمَكَارِ<span class="highlight-red">مُ</span>
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: تَنْبِيهٌ هَامٌّ
Content: لَا تَنْسَ أَنَّ حَرْفَ الرَّوِيِّ فِي هَذَا الْبَيْتِ هُوَ (<span class="highlight-red">الْمِيمُ الْمَضْمُومَةُ</span>)، وَتُسَمَّى الْقَصِيدَةُ مِيمِيَّةً.
(Component: TEMPLATE_C_IRAB_ROW.html)
Word 1: الْمَكَارِمُ
Details 1: الْمِيمُ الْمَضْمُومَةُ هِيَ حَرْفُ الرَّوِيِّ الَّذِي تُبْنَى عَلَيْهِ الْقَصِيدَةُ.

=== BLOCK 5: أنواع القافية ===
(Component: TEMPLATE_C_SPLIT.html)
Split 1:
    (Component: TEMPLATE_C_BLOCK.html)
    Title: الْقَافِيَةُ الْمُطْلَقَةُ
    Content: <p class="text-accent">حَرْفُ الرَّوِيِّ مُتَحَرِّكٌ (بِفَتْحَةٍ، ضَمَّةٍ، كَسْرَةٍ) وَيَتَوَلَّدُ مِنْهُ حَرْفُ مَدٍّ (يُسَمَّى الْوَصْلَ).</p> مِثْل: (الْمَكَارِ<span class="highlight-red">مُ</span>).
Split 2:
    (Component: TEMPLATE_C_BLOCK.html)
    Title: الْقَافِيَةُ الْمُقَيَّدَةُ
    Content: <p class="text-accent">حَرْفُ الرَّوِيِّ عَلَيْهِ سُكُونٌ (مُقَيَّدٌ لَا يَتَحَرَّكُ).</p> مِثْل: (يَضِيقُ عَنْهَا الْفَضَا<span class="highlight-red">ءْ</span>).

=== BLOCK 6: ثانياً: الموسيقا الداخلية ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ثَانِياً: الْمُوسِيقَا الدَّاخِلِيَّةُ (التَّنَاغُمُ السِّرِّيُّ)
Content:
<p class="text-accent">هِيَ أَصْوَاتٌ خَفِيَّةٌ تَأْتِي مِنْ اخْتِيَارِ الْكَلِمَاتِ وَتَرْتِيبِهَا:</p>
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: <span class="highlight-blue">التَّكْرَارُ (أَهَمُّ شَيْءٍ):</span> تَكْرَارُ حَرْفٍ مُعَيَّنٍ، أَوْ كَلِمَةٍ، أَوْ حَتَّى كَثْرَةُ التَّنْوِينِ (<span class="highlight-green">شَوْقاً</span>، <span class="highlight-green">جُنُوناً</span>). يَمْنَحُ الْكَلَامَ رَنِيناً.
[LIST_ITEM_CONTENT]: <span class="highlight-blue">التَّنَاغُمُ بَيْنَ الْحُرُوفِ:</span> الْمُزَاوَجَةُ بَيْنَ حُرُوفِ الْهَمْسِ (الرَّقِيقَةِ مِثْلَ: س، ك، ت، ف، ح، ث، هـ، ش، خ، ص) وَحُرُوفِ الْجَهْرِ (الْقَوِيَّةِ).
[LIST_ITEM_CONTENT]: <span class="highlight-blue">الْمُحَسِّنَاتُ اللَّفْظِيَّةُ:</span> كَالْجِنَاسِ (<span class="highlight-green">رَبِيع</span> - <span class="highlight-green">رَبِيعًا</span>)، وَالتَّصْرِيعِ.
[LIST_ITEM_CONTENT]: <span class="highlight-blue">التَّقْفِيَةُ الدَّاخِلِيَّةُ:</span> جَعْلُ كَلِمَاتٍ دَاخِلَ الْبَيْتِ تَنْتَهِي بِنَفْسِ الْوَزْنِ أَوْ الْحَرْفِ لِزِيَادَةِ الْمُوسِيقَا. (<span class="highlight-green">حَارَ فِكْرِي</span>، <span class="highlight-green">وَضَاقَ صَدْرِي</span>).

=== BLOCK 7: Matrix Summary ===
(Component: TEMPLATE_C_TABLE.html)
Table Content:
Row 1: | نَوْعُ الْمُوسِيقَا | التَّعْرِيفُ | الْعَنَاصِرُ |
Row 2: | الْمُوسِيقَا الْخَارِجِيَّةُ | الْهَيْكَلُ الْعَامُّ وَالْإِيقَاعُ الْوَاضِحُ | الْوَزْنُ، الْقَافِيَةُ، حَرْفُ الرَّوِيِّ |
Row 3: | الْمُوسِيقَا الدَّاخِلِيَّةُ | الْأَصْوَاتُ الْخَفِيَّةُ مِنَ الْكَلِمَاتِ | التَّكْرَارُ، التَّنَاغُمُ، الْمُحَسِّنَاتُ، التَّقْفِيَةُ الدَّاخِلِيَّةُ |

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: مَا هِيَ أَنْوَاعُ الْقَافِيَةِ، وَمَا الْفَرْقُ بَيْنَهُمَا مَعَ التَّمْثِيلِ؟
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: اشْرَحْ كَيْفَ تُسَاهِمُ الْمُوسِيقَا الدَّاخِلِيَّةُ فِي جَمَالِ الْقَصِيدَةِ مَعَ ذِكْرِ عُنْصُرَيْنِ مِنْ عَنَاصِرِهَا؟

--- END STREAM ---