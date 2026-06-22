# **SESSION 02.0**

[TASK DEFINITION]
Objective: Implement أَقْسَامُ الْكَلَاَمِ .
File: `pages/02.0_nXX_أَقْسَامُ الْكَلَاَمِ .html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/02.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 02
[CHAPTER_TITLE]: أَقْسَامُ الْكَلَاَمِ 
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. حنا خفيف
[AUTHOR_PHONE]:  

=== BLOCK 2: Definition of الْقَوْل ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٤. الْقَوْلُ
Content:
<p class="text-accent">كَلٌّ مَا يَتَلَفَّظُ بِهِ الْإِنْسَانُ وَيَدُلُّ عَلَى مُعَنًّى ، سَوَاءً كَانَ مُفْرَدًا أَوْ مُرَكَّبًا ، مُفِيدًا أَوْ غَيْرَ مُفِيدٍ.</p>
(Component: TEMPLATE_C_BENEFIT.html)
Content: وَهُوَ أَعَمُّ مِنَ الْكَلِمَةِ وَالْكَلَامِ وَالْكَلِمِ. كُلُّ شَيْءٍ لَهُ مَعْنًى هُوَ "قَوْلٌ".

=== BLOCK 3: Detailed Breakdown of Examples (Deep Dive) ===
(Component: TEMPLATE_C_SPLIT.html)
Left Side:
(Component: TEMPLATE_C_BLOCK.html)
Title: أَمِثْلَةٌ عَلَى الْمُفْرَدِ وَالْمُرَكَّبِ النَّاقِصِ
Content:
(Component: TEMPLATE_C_LIST.html)
- <span class="highlight-red">أَسَدٌ</span> (مُفْرَدٌ يَدُلُّ عَلَى مُعَنًّى، قَوْلٌ وَكَلِمَةٌ).
- <span class="highlight-blue">طَالِبُ الْعِلْمِ</span> (مُرَكَّبٌ يَدُلُّ عَلَى مُعَنًّى، لَكِنَّهُ لَا يَحْسُنُ السُّكُوتُ عَلَيْهِ، قَوْلٌ).
- <span class="highlight-green">قَلَمُ الرَّصَاصِ</span>. (قَوْلٌ).

Right Side:
(Component: TEMPLATE_C_BLOCK.html)
Title: أَمِثْلَةٌ عَلَى الْمُرَكَّبِ التَّامِّ (الْمُفِيدِ)
Content:
(Component: TEMPLATE_C_LIST.html)
- <span class="highlight-red">الْعِلْمُ نُورٌ</span> (مُرَكَّبٌ يَدُلُّ عَلَى مُعَنًّى تَامٍّ، قَوْلٌ وَكَلَامٌ).
- <span class="highlight-blue">قَرَأَ خَالِدٌ الْكِتَابَ</span>. (قَوْلٌ، وَكَلِمٌ، وَكَلَامٌ).

=== BLOCK 4: The Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Header: مُلَخَّصُ الْعِلَاقَةِ بَيْنَ أَقْسَامِ الْكَلَامِ وَالْقَوْلِ
Content:
Row 1: أَسَدٌ | مُفْرَدٌ يَدُلُّ عَلَى مُعَنًّى | قَوْلٌ وَكَلِمَةٌ
Row 2: طَالِبُ الْعِلْمِ / قَلَمُ الرَّصَاصِ | مُرَكَّبٌ نَاقِصٌ | قَوْلٌ فَقَطْ
Row 3: الْعِلْمُ نُورٌ | مُرَكَّبٌ تَامٌّ | قَوْلٌ وَكَلَامٌ
Row 4: قَرَأَ خَالِدٌ الْكِتَابَ | مُرَكَّبٌ تَامٌّ مِنْ ثَلَاثِ كَلِمَاتٍ | قَوْلٌ وَكَلِمٌ وَكَلَامٌ

=== BLOCK 5: Warning Box ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: تَنْبِيهٌ هَامٌّ!
Content: لَيْسَ كُلُّ لَفْظٍ قَوْلًا. اللَّفْظُ الْمُهْمَلُ الَّذِي لَيْسَ لَهُ مَعْنًى (مِثْلُ: لُزِّنَّ) يُسَمَّى لَفْظًا فَقَطْ وَلَا يُسَمَّى قَوْلًا.

=== BLOCK 6: Evaluation (Exam) ===
(Component: TEMPLATE_C_EXAM.html)
Title: اِخْتَبِرْ نَفْسَكَ

Question 1:
Number: ١
Question: حَدَّدَ نَوْعُ الْعِبَارَاتِ التَّالِيَةِ بِنَاءً عَلَى مَا دَرَسَتْ ( الْكَلِمَةَ ، الْكِلَاَمَ ، الْكَلْمَ ، الْقَوْلَ ، اللَّفْظَ ). مُلَاحِظَةً: قَد تَقْبَلُ الْعِبَارَةُ أَكْثَرَ مِن إِجَابَةِ:
1. شَجَرَةُ
2. السَّفَرُ مُفِيدٌ
3. اِذْهَبْ
4. كَتَبَ الطَّالِبُ الدَّرْسَ
5. ضَعْ إِلَى نَحْفَظُ
6. أَسَدُّ
7. طَالِبُ الْعِلْمِ
8. سَيَّارَةُ
9. لُزِّنَّ (ليس لها معنى، فهي لفظ مهمل فقط).

Question 2:
Number: ٢
Question: اِقْرَأْ الْمَقُولَاتِ وَالْأَشْعَارِ التَّالِيَةِ ، ثُمَّ أَجِبُ:
أ) يَقُولُ الشَّاعِرُ: "أَقُولُ لهُ وقَد طَارَتْ شَعَاعًا ... مِنَ الْأَبْطَالِ وَيْحَكَ لَنْ تُرَاعِي". مَا الْمَقْصُودِ بـ "كَلِمَةَ" (وَيَحْكِ لَن تُرَاعِي) فِي هَذَا السِّيَاقِ، وهَل هِي لَفْظَةٍ مُفْرَدَةٍ أَم جُمْلَةٌ؟
ب) الْمَقُولَةَ الْمَشْهُورَةَ: "كَلِمَةُ وَاحِدَةُ أَقُولُهَا لَكُم: اِتَّحَدُوا تَسُودُوا". لِمَاذَا أُطْلِقُ عَلَى عِبَارَةِ "اِتَّحَدُوا تَسُودُوا" بأَنّهَا "كَلِمَةَ" رَغْمٌ أَنّهَا جُمْلَةَ كَامِلَةَ؟

Question 3:
Number: ٣
Question: ضَعْ عُلَّامَةَ (صَحَّ) أَو (خَطَأَ) مَع تَصْحِيحِ الْخَطَأِ:
1. ( ) كُلّ كَلِمٍ هُو كَلَاَمِ مُفِيدِ يُحْسِنُ السُّكُوتُ عَلَيْهِ.
2. ( ) "الْعِلْمُ نُورٌ" تُعْتَبَرُ كَلَاَمًا لأَنّهَا تَتُكُّونَ مِن كَلْمَتَيْنِ وَتُفِيدُ مُعَنَّى تَامًّا.
3. ( ) أَيَّ صَوْتٍ يَخْرُجُ مِن فَمِ الْإِنْسَانِ يَحْتَوِي عَلَى حُروفِ يُسَمَّى "قَوْلًا" حَتَّى لَو لَم يَكُنُّ لَه مُعَنًّى.
4. ( ) جُمْلَةُ "اِذْهَبْ" هِي كَلِمَةِ وَاحِدَةِ ولَيْسَت كَلَاَمًا.

--- END STREAM ---
