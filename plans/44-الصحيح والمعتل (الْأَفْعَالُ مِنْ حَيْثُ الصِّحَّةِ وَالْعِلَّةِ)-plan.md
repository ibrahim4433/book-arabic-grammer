# **SESSION 44.0**

[TASK DEFINITION]
Objective: Implement الصحيح والمعتل (الْأَفْعَالُ مِنْ حَيْثُ الصِّحَّةِ وَالْعِلَّةِ).
File: `pages/44.0_nXX_الصحيح والمعتل (الْأَفْعَالُ مِنْ حَيْثُ الصِّحَّةِ وَالْعِلَّةِ).html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/44.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 44
[CHAPTER_TITLE]: الصحيح والمعتل (الْأَفْعَالُ مِنْ حَيْثُ الصِّحَّةِ وَالْعِلَّةِ)
[CATEGORY_HEADER]: المستوى المتوسط
[SECTION_HEADER]: علم الصرف
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition of Verbs based on Soundness and Illness ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مَفْهُومُ الْفِعْلِ الصَّحِيحِ وَالْفِعْلِ الْمُعْتَلِّ
Content:
<p class="text-accent">تَنْقَسِمُ الْأَفْعَالُ فِي اللُّغَةِ الْعَرَبِيَّةِ حَسَبَ حُرُوفِهَا الْأَصْلِيَّةِ (فِي الْمَاضِي الثُّلَاثِيِّ) إِلَى نَوْعَيْنِ أَسَاسِيَّيْنِ:</p>
(Component: TEMPLATE_C_LIST.html)
Item 1: <span class="font-bold highlight-blue">١- الْفِعْلُ الصَّحِيحُ:</span> هُوَ مَا كَانَتْ حُرُوفُهُ الْأَصْلِيَّةُ خَالِيَةً سَلِيمَةً مِنْ حُرُوفِ الْعِلَّةِ الثَّلَاثَةِ (<span class="highlight-red">الْأَلِف</span>، <span class="highlight-red">الْوَاو</span>، <span class="highlight-red">الْيَاء</span>). مِثْل: كَتَبَ، دَرَسَ، فَهِمَ.
Item 2: <span class="font-bold highlight-blue">٢- الْفِعْلُ الْمُعْتَلُّ:</span> هُوَ مَا كَانَ أَحَدُ (أَوْ أَكْثَرُ مِنْ) حُرُوفِهِ الْأَصْلِيَّةِ حَرْفَ عِلَّةٍ كَالْمَرِيضِ. مِثْل: وَجَدَ، قَالَ، رَمَى.

=== BLOCK 3: Detailed Breakdown of Correct Verb Types ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَقْسَامُ الْفِعْلِ الصَّحِيحِ (ثَلَاثَةُ أَنْوَاعٍ)
Content:
(Component: TEMPLATE_C_LIST.html)
Item 1: <span class="font-bold">السَّالِمُ:</span> مَا سَلِمَتْ (خَلَتْ) أُصُولُهُ مِنَ الْهَمْزَةِ (<span class="highlight-red">أ</span>) وَالتَّضْعِيفِ (الشَّدَّةِ).
Item 2: <span class="font-bold">الْمَهْمُوزُ:</span> مَا كَانَ أَحَدُ أُصُولِهِ هَمْزَةً (فِي الْأَوَّلِ أَوْ الْوَسَطِ أَوْ الْأَخِيرِ).
Item 3: <span class="font-bold">الْمُضَعَّفُ:</span> مَا كَانَ أَحَدُ أُصُولِهِ مُشَدَّدًا (أَيْ فِيهِ حَرْفَانِ مُتَمَاثِلَانِ أُدْغِمَا مَعًا).

=== BLOCK 4: EXTRA INFO (Warning on Quadruplet) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: تَنْبِيهٌ
Content: هُنَاكَ مُضَعَّفٌ رُبَاعِيٌّ كَـ (زَلْزَلَ).

=== BLOCK 5: Matrix of Correct Verbs ===
(Component: TEMPLATE_C_TABLE.html)
Table Content:
Row 1 (Header): النَّوْع | التَّعْرِيف | أَمْثِلَة
Row 2: السَّالِم | مَا سَلِمَتْ (خَلَتْ) أُصُولُهُ مِنَ الْهَمْزَةِ (أ) وَالتَّضْعِيفِ (الشَّدَّةِ). | <span class="highlight-green">كَتَبَ</span> ، <span class="highlight-green">جَلَسَ</span> ، <span class="highlight-green">فَهِمَ</span> ، <span class="highlight-green">سَمِعَ</span>.
Row 3: الْمَهْمُوز | مَا كَانَ أَحَدُ أُصُولِهِ هَمْزَةً (فِي الْأَوَّلِ أَوْ الْوَسَطِ أَوْ الْأَخِيرِ). | <span class="highlight-red">أَ</span>كَلَ، <span class="highlight-red">أَ</span>مَرَ ، سَ<span class="highlight-red">أَ</span>لَ ، قَرَ<span class="highlight-red">أَ</span>، لَجَ<span class="highlight-red">أَ</span>.
Row 4: الْمُضَعَّف | مَا كَانَ أَحَدُ أُصُولِهِ مُشَدَّدًا (أَيْ فِيهِ حَرْفَانِ مُتَمَاثِلَانِ أُدْغِمَا مَعًا). | صَ<span class="highlight-red">دَّ</span> (أَصْلُهَا صَدَدَ)، مَ<span class="highlight-red">دَّ</span>، عَ<span class="highlight-red">دَّ</span>، جَ<span class="highlight-red">دَّ</span>.

=== BLOCK 6: Detailed Breakdown of Ill Verb Types ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَقْسَامُ الْفِعْلِ الْمُعْتَلِّ (خَمْسَةُ أَنْوَاعٍ)
Content:
(Component: TEMPLATE_C_LIST.html)
Item 1: <span class="font-bold">الْمِثَالُ:</span> أَوَّلُهُ حَرْفُ عِلَّةٍ (<span class="highlight-red">وَاوٌ</span> أَوْ <span class="highlight-red">يَاءٌ</span>، وَلَا يَكُونُ أَلِفًا).
Item 2: <span class="font-bold">الْأَجْوَفُ:</span> أَوْسَطُهُ (عَيْنُهُ فِي جَوْفِهِ) حَرْفُ عِلَّةٍ.
Item 3: <span class="font-bold">النَّاقِصُ:</span> آخِرُهُ (لَامُهُ) حَرْفُ عِلَّةٍ.
Item 4: <span class="font-bold">اللَّفِيفُ الْمَفْرُوقُ:</span> فِيهِ حَرْفَا عِلَّةٍ، بَيْنَهُمَا فَاصِلٌ مُفَرِّقٌ (حَرْفٌ صَحِيحٌ فِي الْوَسَطِ).
Item 5: <span class="font-bold">اللَّفِيفُ الْمَقْرُونُ:</span> فِيهِ حَرْفَا عِلَّةٍ مُتَتَالِيَانِ مَقْرُونَانِ بِبَعْضِهِمَا (دُونَ فَاصِلٍ).

=== BLOCK 7: Matrix of Ill Verbs ===
(Component: TEMPLATE_C_TABLE.html)
Table Content:
Row 1 (Header): النَّوْع | مَوْضِعُ الْعِلَّةِ (أَيْنَ يُوجَدُ الْمَرَضُ؟) | أَمْثِلَة
Row 2: الْمِثَال | أَوَّلُهُ حَرْفُ عِلَّةٍ (وَاوٌ أَوْ يَاءٌ، وَلَا يَكُونُ أَلِفًا). | <span class="highlight-red">وَ</span>صَلَ ، <span class="highlight-red">وَ</span>جَدَ ، <span class="highlight-red">وَ</span>عَدَ، <span class="highlight-red">يَ</span>ئِسَ، <span class="highlight-red">يَ</span>قِظَ.
Row 3: الْأَجْوَف | أَوْسَطُهُ (عَيْنُهُ فِي جَوْفِهِ) حَرْفُ عِلَّةٍ. | قَ<span class="highlight-red">ا</span>لَ ، سَ<span class="highlight-red">ا</span>رَ ، بَ<span class="highlight-red">ا</span>عَ، نَ<span class="highlight-red">ا</span>مَ، خَ<span class="highlight-red">ا</span>فَ.
Row 4: النَّاقِص | آخِرُهُ (لَامُهُ) حَرْفُ عِلَّةٍ. | مَشَ<span class="highlight-red">ى</span> ، دَنَ<span class="highlight-red">ا</span> ، رَمَ<span class="highlight-red">ى</span>، سَعَ<span class="highlight-red">ى</span>، دَعَ<span class="highlight-red">ا</span>.
Row 5: اللَّفِيفُ الْمَفْرُوق | فِيهِ حَرْفَا عِلَّةٍ، بَيْنَهُمَا فَاصِلٌ مُفَرِّقٌ (حَرْفٌ صَحِيحٌ فِي الْوَسَطِ). | <span class="highlight-red">وَ</span>عَ<span class="highlight-red">ى</span> (وَاوٌ وَيَاءٌ بَيْنَهُمَا عَيْنٌ)، <span class="highlight-red">وَ</span>شَ<span class="highlight-red">ى</span>، <span class="highlight-red">وَ</span>قَ<span class="highlight-red">ى</span>، <span class="highlight-red">وَ</span>لِ<span class="highlight-red">يَ</span>.
Row 6: اللَّفِيفُ الْمَقْرُون | فِيهِ حَرْفَا عِلَّةٍ مُتَتَالِيَانِ مَقْرُونَانِ بِبَعْضِهِمَا (دُونَ فَاصِلٍ). | رَ<span class="highlight-red">وَى</span> (وَاوٌ وَيَاءٌ مُتَتَالِيَتَانِ)، طَ<span class="highlight-red">وَى</span>، شَ<span class="highlight-red">وَى</span>، نَ<span class="highlight-red">وَى</span>.

=== BLOCK 8: DEEP DIVE (أَمْثِلَةٌ إِضَافِيَّةٌ لِلْإِعْرَابِ) ===
(Component: TEMPLATE_C_SPLIT.html)
Description: Side-by-side parsing example of verbs.
LeftSide:
(Component: TEMPLATE_C_IRAB_ROW.html)
Word1: شَكَرَ
Details1: فِعْلٌ مَاضٍ صَحِيحٌ سَالِمٌ.
Word2: قَرَأَ
Details2: فِعْلٌ مَاضٍ صَحِيحٌ مَهْمُوزٌ.
RightSide:
(Component: TEMPLATE_C_IRAB_ROW.html)
Word1: نَامَ
Details1: فِعْلٌ مَاضٍ مُعْتَلٌّ أَجْوَفٌ.
Word2: سَعَى
Details2: فِعْلٌ مَاضٍ مُعْتَلٌّ نَاقِصٌ.

=== BLOCK 9: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: صَنِّفِ الْأَفْعَالَ الْآتِيَةَ إِلَى صَحِيحٍ وَمُعْتَلٍّ مَعَ بَيَانِ النَّوْعِ: (نَامَ، شَدَّ، وَعَدَ، قَرَأَ، رَضِيَ، طَوَى).
Number: ٢
Question: اسْتَخْرِجِ الْأَفْعَالَ مِنَ الْجُمْلَةِ الْآتِيَةِ وَبَيِّنْ نَوْعَهَا: (سَعَى الرَّجُلُ فِي الْعَمَلِ، وَوَجَدَ النَّجَاحَ، وَشَكَرَ مُدِيرَهُ).

--- END STREAM ---