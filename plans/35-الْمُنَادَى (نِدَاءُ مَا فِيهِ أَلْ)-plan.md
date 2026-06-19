# **SESSION 35.0**

[TASK DEFINITION]
Objective: Implement الْمُنَادَى (نِدَاءُ مَا فِيهِ أَلْ).
File: `pages/35.0_nXX_الْمُنَادَى (نِدَاءُ مَا فِيهِ أَلْ).html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/35.1_...` if page have a lot of blank space add exam elements from the lesson.
3. text Content: 100% Arabic with full Harakat.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green`  for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   **Rule:** NO INLINE STYLES.
*   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
7. Templates: You are forbidden from inventing new HTML tags or classes or template elements. You must map all content using "Jules-workspace/Templates/" components as the STREAM says in suitable way.
8. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). use "Jules-workspace/id_manager.py" to generate or verify them.
9. **Self-Correction:** Run "Jules-workspace/lint_pages.py" after creating html files. If it fails, you MUST fix the errors (usually inline styles) before submitting.
10. Do not summarize examples.
11. Do not provide uncompleted text content using (...) .
12. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
13. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits. Use `Jules-workspace/whitespace_filler.py` if needed.
14. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal
15. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
16. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 35
[CHAPTER_TITLE]: الْمُنَادَى (نِدَاءُ مَا فِيهِ أَلْ)
[CATEGORY_HEADER]: المستوى المتوسط
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition & Rule ===
(Component: TEMPLATE_C_BLOCK.html)
Title: نِدَاءُ الْمُعَرَّفِ بِـ (أَلْ)
Content:
<p class="text-accent font-bold">
الْعَرَبُ لَا تَقُولُ <span class="highlight-red">(يَا الرَّجُلُ)</span>، فَلَا يَجْتَمِعُ حَرْفُ النِّدَاءِ مَعَ (الـ) التَّعْرِيفِ!
</p>
<p>
إِذَنْ كَيْفَ نُنَادِي الْكَلِمَةَ الَّتِي بِهَا <span class="highlight-blue">(الـ)</span> كَـ "الطَّالِب"؟<br>
نَسْتَعِينُ بِكَلِمَةِ <span class="highlight-green">(أَيُّهَا)</span> لِلْمُذَكَّرِ، أَوْ <span class="highlight-green">(أَيَّتُهَا)</span> لِلْمُؤَنَّثِ. فَنَقُولُ: <span class="highlight-red">(يَا أَيُّهَا الطَّالِبُ)</span> وَ<span class="highlight-red">(يَا أَيَّتُهَا الطَّالِبَةُ)</span>.
</p>

=== BLOCK 3: Deep Dive - Irab ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الْإِعْرَابُ هَامٌّ جِدّاً
Content:
(TEMPLATE_C_IRAB_ROW.html)
Word 1: يَا
Details 1: حَرْفُ نِدَاءٍ.
Word 2: أَيُّ/أَيَّةُ
Details 2: هُوَ الْمُنَادَى هُنَا نَوْعُهُ (نَكِرَةٌ مَقْصُودَةٌ)، فَنُعْرِبُهُ: <span class="highlight-red">مُنَادَى مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.</span>
(TEMPLATE_C_IRAB_ROW.html)
Word 3: هَا
Details 3: لِلتَّنْبِيهِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.
Word 4: الِاسْمُ الْمَرْفُوعُ
Details 4: بَعْدَهُمَا (الطَّالِبُ/الرَّجُلُ) لَهُ حَالَتَانِ مُهِمَّتَانِ.

=== BLOCK 4: The Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
(Make sure to inject it into TEMPLATE_C_BLOCK if necessary, or just use it directly if supported by generator script)
Headers: النَّوْعُ | الْمِثَالُ | الْإِعْرَابُ
Row 1: مُشْتَقٌّ (مَأْخُوذٌ مِنْ فِعْلٍ) | الطَّالِبُ (مِنْ طَلَبَ)، الْمُعَلِّمُ (مِنْ عَلِمَ) | يُعْرَبُ <span class="highlight-red">صِفَةً (نَعْتاً) مَرْفُوعَةً بِالضَّمَّةِ</span>.
Row 2: جَامِدٌ (لَا فِعْلَ لَهُ) | الرَّجُلُ، الْمَرْأَةُ، الْفَتَاةُ | يُعْرَبُ <span class="highlight-blue">بَدَلًا مَرْفُوعًا بِالضَّمَّةِ</span>.

=== BLOCK 5: Extra Info - Warning ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: تَنْبِيهٌ هَامٌّ
Content: تَذَكَّرْ أَنَّ الْمُنَادَى الْحَقِيقِيَّ هُوَ (أَيُّ/أَيَّةُ) وَلَيْسَ الِاسْمَ الْمُعَرَّفَ بِـ (أَلْ) الَّذِي يَلِيهِ.

=== BLOCK 6: Exam ===
(Component: TEMPLATE_C_EXAM.html)
(Wrap inside a TEMPLATE_C_BLOCK with bg-dark header as shown in elements index)
Number: ١
Question: مَيِّزِ الْمُنَادَى الْمُعْرَبَ مِنَ الْمَبْنِيِّ: (يَا طَالِعاً جَبَلاً - يَا طَارِقُ).
Number: ٢
Question: حَوِّلِ الْمُنَادَى الْمُضَافَ إِلَى شَبِيهٍ بِالْمُضَافِ: (يَا طَالِبَ الْعِلْمِ اجْتَهِدْ).
Number: ٣
Question: أَعْرِبْ: (يَا أَيُّهَا الْمُوَاطِنُونَ).

--- END STREAM ---
