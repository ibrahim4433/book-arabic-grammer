# **SESSION 15.0**

[TASK DEFINITION]
Objective: Implement أَنْوَاعُ الْجَمَلِ وَكَيْفِيَّةِ التَّمْييزِ بَيْنهَا .
File: `pages/15.0_nXX_أَنْوَاعُ الْجَمَلِ وَكَيْفِيَّةِ التَّمْييزِ بَيْنهَا .html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/15.1_...` if page have a lot of blank space add exam elements from the lesson.
3. text Content: 100% Arabic with full Harakat.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`, `.highlight-green` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   **Rule:** NO INLINE STYLES.
*   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
*   **Mapping:**
    *   inline style width: 20% -> `class="w-20pct"`
    *   inline style margin-top: 2mm -> `class="mt-2mm"`
    *   inline style text-align: center -> `class="text-center"`
    *   inline style font-weight: bold -> `class="font-bold"`
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
[LESSON_NUMBER]: 15
[CHAPTER_TITLE]: أَنْوَاعُ الْجَمَلِ وَكَيْفِيَّةِ التَّمْييزِ بَيْنهَا 
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. حنا خفيف
[AUTHOR_PHONE]:  

=== BLOCK 2: Definition & Rule ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَعْرِيفُ أَنْوَاعِ الْجُمَلِ
Content: <p class="text-accent text-center mb-2mm">تَنْقَسِمُ الْجُمَلُ فِي اللُّغَةِ الْعَرَبِيَّةِ إِلَى قِسْمَيْنِ أَسَاسِيَّيْنِ، وَهُمَا <span class="font-bold">الْجُمْلَةُ الِاسْمِيَّةُ</span> وَ<span class="font-bold">الْجُمْلَةُ الْفِعْلِيَّةُ</span>، وَيَتِمُّ التَّمْيِيزُ بَيْنَهُمَا مِنْ خِلَالِ الْكَلِمَةِ الَّتِي تَبْدَأُ بِهَا الْجُمْلَةُ.</p>

=== BLOCK 3: The Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Table Headers: نَوْعُ الْجُمْلَةِ | تَبْدَأُ بـ | أَرْكَانُهَا الْأَسَاسِيَّةُ | مِثَالٌ
Row 1: اِسْمِيَّة | اِسْم | الْمُبْتَدَأُ + الْخَبَرُ | الْعِلْمُ نُورٌ
Row 2: فِعْلِيَّة | فِعْل | الْفِعْلُ + الْفَاعِلُ | نَامَ الطِّفْلُ

=== BLOCK 4: Deep Dive - Nominal Sentence ===
(Component: TEMPLATE_C_SPLIT.html)

[LeftSide]
(Component: TEMPLATE_C_BLOCK.html)
Title: 1. الْجُمْلَةُ الِاسْمِيَّةُ
Content: هِيَ الْجُمْلَةُ الَّتِي تَبْدَأُ بِـ <span class="highlight-blue">اِسْمٍ</span>. وَتَتَكَوَّنُ مِنْ رُكْنَيْنِ أَسَاسِيَّيْنِ هُمَا الْمُبْتَدَأُ وَالْخَبَرُ. مِثَالٌ عَلَى ذَلِكَ: <span class="highlight-red font-bold">الْعِلْمُ نُورٌ</span>.

[RightSide]
(Component: TEMPLATE_C_IRAB_ROW.html)
Word 1: الْعِلْمُ
Details 1: مُبْتَدَأٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ عَلَى آخِرِهِ.
Word 2: نُورٌ
Details 2: خَبَرُ الْمُبْتَدَإِ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ عَلَى آخِرِهِ.

=== BLOCK 5: Deep Dive - Verbal Sentence ===
(Component: TEMPLATE_C_SPLIT.html)

[LeftSide]
(Component: TEMPLATE_C_BLOCK.html)
Title: 2. الْجُمْلَةُ الْفِعْلِيَّةُ
Content: هِيَ الْجُمْلَةُ الَّتِي تَبْدَأُ بِـ <span class="highlight-blue">فِعْلٍ</span>. وَتَتَكَوَّنُ مِنْ رُكْنَيْنِ أَسَاسِيَّيْنِ هُمَا الْفِعْلُ وَالْفَاعِلُ. مِثَالٌ عَلَى ذَلِكَ: <span class="highlight-red font-bold">نَامَ الطِّفْلُ</span>.

[RightSide]
(Component: TEMPLATE_C_IRAB_ROW.html)
Word 1: نَامَ
Details 1: فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ الظَّاهِرِ عَلَى آخِرِهِ.
Word 2: الطِّفْلُ
Details 2: فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ عَلَى آخِرِهِ.

=== BLOCK 6: Benefit Warning ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: تَنْبِيهٌ هَامٌّ!
Content: لِلتَّمْيِيزِ بَيْنَ الْجُمْلَةِ الِاسْمِيَّةِ وَالْفِعْلِيَّةِ، انْظُرْ دَائِماً إِلَى <span class="highlight-red font-bold">الْكَلِمَةِ الْأُولَى</span> فِي الْجُمْلَةِ. إِذَا كَانَتْ اِسْماً فَالْجُمْلَةُ اِسْمِيَّةٌ، وَإِذَا كَانَتْ فِعْلاً فَالْجُمْلَةُ فِعْلِيَّةٌ.

=== BLOCK 7: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: حَدِّدْ نَوْعَ الْجُمْلَةِ فِيمَا يَلِي (اِسْمِيَّةٌ أَمْ فِعْلِيَّةٌ): الشَّمْسُ مُشْرِقَةٌ.
Number: ٢
Question: حَدِّدْ نَوْعَ الْجُمْلَةِ فِيمَا يَلِي (اِسْمِيَّةٌ أَمْ فِعْلِيَّةٌ): يَقْرَأُ الطَّالِبُ الدَّرْسَ.
Number: ٣
Question: أَعْرِبْ الْجُمْلَةَ التَّالِيَةَ إِعْرَاباً تَامّاً: الْعِلْمُ نُورٌ.

--- END STREAM ---