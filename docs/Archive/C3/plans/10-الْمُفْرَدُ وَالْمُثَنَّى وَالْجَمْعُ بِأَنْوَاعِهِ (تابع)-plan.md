# **SESSION 10.0**

[TASK DEFINITION]
Objective: Implement الْمُفْرَدُ وَالْمُثَنَّى وَالْجَمْعُ بِأَنْوَاعِهِ .
File: `pages/10.0_nXX_الْمُفْرَدُ وَالْمُثَنَّى وَالْجَمْعُ بِأَنْوَاعِهِ .html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually, instead Use `verify_layout.py` after every block.
3. text Content: 100% Arabic with full Harakat.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   **Rule:** NO INLINE STYLES.
*   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
*   **Mapping:**
    *   `style="width: 20%"` -> `class="w-20pct"`
    *   `style="margin-top: 2mm"` -> `class="mt-2mm"`
    *   `style="text-align: center"` -> `class="text-center"`
    *   `style="font-weight: bold"` -> `class="font-bold"`
7. Templates: You are forbidden from inventing new HTML tags or classes or template elements. You must map all content using "Jules-workspace/Templates/" components.
8. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). use "Jules-workspace/id_manager.py" to generate or verify them.
9. Self-Correction: Run "Jules-workspace/lint_pages.py" after creating html files. If it fails, fix the errors.
10. Do not summarize examples.
11. Do not provide uncompleted text content using (...).
12. Preserve exact Tashkeel and add any missing Tashkeel needed if any.
13. Visual Density: The page must be dense. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
14. Balanced page colors between teal and orange: minimum 1 element in orange.
15. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html`.
16. Exam section always be in the end of the lesson (without the answers!).

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 10
[CHAPTER_TITLE]: الْمُفْرَدُ وَالْمُثَنَّى وَالْجَمْعُ بِأَنْوَاعِهِ 
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. حنا خفيف
[AUTHOR_PHONE]:  

=== BLOCK 2: Definition ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ج. جَمْعُ التَّكْسِيرِ
Content: <p class="text-accent">هُوَ مَا دَلَّ عَلَى أَكْثَرِ مِنْ اِثْنَيْنِ أَوِ اثْنَتَيْنِ، مَعَ تَغَيُّرِ وَتَكَسُّرِ صُورَةِ مُفْرَدِهِ (سَوَاءً بِزِيَادَةِ حُرُوفٍ، نَقْصِ حُرُوفٍ، أَو تَغَيُّرِ حَرَكَاتٍ). وَلَا يَنْتَهِي بِنِهَايَاتٍ ثَابِتَةٍ.</p>

=== BLOCK 3: Examples Grid ===
(Component: TEMPLATE_C_SPLIT.html)
LeftSide:
(Component: TEMPLATE_C_BLOCK.html)
Title: أَمْثِلَةٌ (الْمُذَكَّرُ)
Content:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: <span class="font-bold">طَالِبٌ:</span> <span class="highlight-red">طُلَّابٌ</span>
[LIST_ITEM_CONTENT]: <span class="font-bold">طِفْلٌ:</span> <span class="highlight-red">أَطْفَالٌ</span>
[LIST_ITEM_CONTENT]: <span class="font-bold">أَسَدٌ:</span> <span class="highlight-red">أُسْدٌ</span>
[LIST_ITEM_CONTENT]: <span class="font-bold">بَابٌ:</span> <span class="highlight-red">أَبْوَابٌ</span>
[LIST_ITEM_CONTENT]: <span class="font-bold">قَلَمٌ:</span> <span class="highlight-red">أَقْلَامٌ</span>

RightSide:
(Component: TEMPLATE_C_BLOCK.html)
Title: أَمْثِلَةٌ (شَوَازّ وَغَيْرُ الْعَاقِلِ)
Content:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: <span class="font-bold">كِتَابٌ:</span> <span class="highlight-blue">كُتُبٌ</span>
[LIST_ITEM_CONTENT]: <span class="font-bold">مَدِينَةٌ:</span> <span class="highlight-blue">مُدُنٌ</span>
[LIST_ITEM_CONTENT]: <span class="font-bold">مَدْرَسَةٌ:</span> <span class="highlight-blue">مَدَارِسُ</span>
[LIST_ITEM_CONTENT]: <span class="font-bold">عَامِلٌ:</span> <span class="highlight-blue">عُمَّالٌ</span>

=== BLOCK 4: I'rab Rules ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الْإِعْرَابُ (مِثْلُ الْمُفْرَدِ تَمَامًا)
Content: <p class="mb-2mm">يُعْرَبُ جَمْعُ التَّكْسِيرِ بِالْعَلَامَاتِ الْأَصْلِيَّةِ الظَّاهِرَةِ:</p>
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: <span class="font-bold text-primary">يُرْفَعُ</span> بِـ <span class="highlight-red">الضَّمَّةِ</span>: حَضَرَ <span class="highlight-red">الطُّلَّابُ</span>.
[LIST_ITEM_CONTENT]: <span class="font-bold text-primary">يُنْصَبُ</span> بِـ <span class="highlight-red">الْفَتْحَةِ</span>: كَتَبُوا <span class="highlight-red">الدُّرُوسَ</span>.
[LIST_ITEM_CONTENT]: <span class="font-bold text-primary">يُجَرُّ</span> بِـ <span class="highlight-red">الْكَسْرَةِ</span>: قَرَأْتُ فِي <span class="highlight-red">الْكُتُبِ</span>.

=== BLOCK 5: I'rab Example ===
(Component: TEMPLATE_C_IRAB_ROW.html)
Left_Irab_Word: الطُّلَّابُ
Left_Irab_Details: فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ <span class="highlight-red">الضَّمَّةُ</span> الظَّاهِرَةُ عَلَى آخِرِهِ (لِأَنَّهُ جَمْعُ تَكْسِيرٍ).
Right_Irab_Word: الْكُتُبِ
Right_Irab_Details: اِسْمٌ مَجْرُورٌ بـ (فِي) وَعَلَامَةُ جَرِّهِ <span class="highlight-red">الْكَسْرَةُ</span> الظَّاهِرَةُ تَحْتَ آخِرِهِ (لِأَنَّهُ جَمْعُ تَكْسِيرٍ).

=== BLOCK 6: The Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Title: جَدْوَلُ إِعْرَابِ الْأَسْمَاءِ الْمُبَسَّطِ
Columns: النَّوْعُ | حَالَةُ الرَّفْعِ | حَالَةُ النَّصْبِ | حَالَةُ الْجَرِّ
Row 1: الْمُفْرَدُ | الضَّمَّةُ | الْفَتْحَةُ | الْكَسْرَةُ
Row 2: الْمُثَنَّى | الْأَلِفُ | الْيَاءُ | الْيَاءُ
Row 3: جَمْعُ الْمُذَكَّرِ السَّالِمِ | الْوَاوُ | الْيَاءُ | الْيَاءُ
Row 4: جَمْعُ الْمُؤَنَّثِ السَّالِمِ | الضَّمَّةُ | الْكَسْرَةُ | الْكَسْرَةُ
Row 5: جَمْعُ التَّكْسِيرِ | الضَّمَّةُ | الْفَتْحَةُ | الْكَسْرَةُ

=== BLOCK 7: Warning Notes ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: تَنْبِيهَاتٌ مُهِمَّةٌ جِدًّا
Content:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: <span class="font-bold">النُّونُ</span> فِي <span class="highlight-red">الْمُثَنَّى</span> مَكْسُورَةٌ دَائِمًا (قَلَمَانِ، وَلَدَيْنِ)، وَفِي <span class="highlight-blue">جَمْعِ الْمُذَكَّرِ السَّالِمِ</span> مَفْتُوحَةٌ دَائِمًا (مُعَلِّمُونَ، فَائِزِينَ). وَهَذَا لِلتَّفْرِيقِ بَيْنَهُمَا فِي الْقِرَاءَةِ.
[LIST_ITEM_CONTENT]: عِنْدَ إِضَافَةِ الْمُثَنَّى أَو جَمْعِ الْمُذَكَّرِ السَّالِمِ إِلَى اِسْمٍ بَعْدَهُ (مُضَافٌ وَمُضَافٌ إِلَيْهِ)، <span class="highlight-red">تُحْذَفُ النُّونُ</span> لِلتَّخْفِيفِ. (مِثْلُ: مُعَلِّمُو الْمَدْرَسَةِ بَدَلًا مِنْ مُعَلِّمُونَ الْمَدْرَسَةِ، طَالِبَا الْعِلْمِ بَدَلًا مِنْ طَالِبَانِ الْعِلْمِ).

=== BLOCK 8: Tip Notes ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Title: مُلَاحَظَةٌ إِعْرَابِيَّةٌ
Content: يُعْرَبُ جَمْعُ التَّكْسِيرِ بِالْحَرَكَاتِ الظَّاهِرَةِ كَالْمُفْرَدِ تَمَامًا (<span class="highlight-green">ضَمَّةٌ</span>، <span class="highlight-green">فَتْحَةٌ</span>، <span class="highlight-green">كَسْرَةٌ</span>).

=== BLOCK 9: Exam Question 1 ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: ثَنِّ وَاِجْمَعِ الْكَلِمَاتِ التَّالِيَةَ جَمْعًا مُنَاسِبًا: <br> ١. عَامِلٌ <br> ٢. طَالِبَةٌ

=== BLOCK 10: Exam Question 2 ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: حَدِّدْ نَوْعَ الْجَمْعِ فِي الْكَلِمَاتِ الْمُلَوَّنَةِ: <br> ١. تَجَوَّلْتُ فِي <span class="highlight-red">الْبَسَاتِينِ</span>. <br> ٢. <span class="highlight-red">الْمُهَنْدِسُونَ</span> مَاهِرُونَ. <br> ٣. سَمِعْتُ <span class="highlight-red">أَصْوَاتًا</span> عَالِيَةً.

=== BLOCK 11: Exam Question 3 ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٣
Question: أَعْرِبِ الْكَلِمَةَ الْمُلَوَّنَةَ فِي الْجُمَلِ الْآتِيَةِ: <br> ١. قَابَلْتُ <span class="highlight-blue">صَدِيقَيْنِ</span> فِي الْمَكْتَبَةِ. <br> ٢. <span class="highlight-blue">التِّلْمِيذَانِ</span> حَاضِرَانِ. <br> ٣. كَرَّمَتِ الْمُدِيرَةُ <span class="highlight-blue">الْمُعَلِّمَاتِ</span>.

--- END STREAM ---
