# **SESSION 21.0**

[TASK DEFINITION]
Objective: Implement التاء المبسوطة والتاء المربوطة.
File: `pages/21.0_nXX_التاء المبسوطة والتاء المربوطة.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/21.1_...` if page have a lot of blank space add exam elements from the lesson.
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

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER)
[LESSON_NUMBER]: 21
[CHAPTER_TITLE]: التاء المبسوطة والتاء المربوطة
[CATEGORY_HEADER]: الإملاء
[SECTION_HEADER]: المستوى اللغوي
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: [Open Ta Definition] ===
(Component: TEMPLATE_C_BLOCK)
Title: تَعْرِيفُ التَّاءِ المَبْسُوطَةِ
Content: <p class="text-accent text-justify">هِيَ التَّاءُ الَّتِي تُلفَظُ تَاءً عِنْدَ الوَقْفِ، وَتُرْسَمُ مَبْسُوطَةً (ت) فِي آخِرِ الكَلِمَةِ سَوَاءٌ كَانَتْ فِي اسْمٍ أَوْ فِعْلٍ.</p>

=== BLOCK 3: [Cases of Open Ta] ===
(Component: TEMPLATE_C_SPLIT)
[LEFT_TITLE]: فِي الأَسْمَاءِ
[LEFT_CONTENT]:
(Component: TEMPLATE_C_LIST)
List Items:
*   **مِنْ أَصْلِ الاِسْمِ:** مِثْلُ: <span class="highlight-red">بَيْت</span>، <span class="highlight-blue">حَانُوت</span>، <span class="highlight-green">كُمَيْت</span>.
*   **جَمْعُ المُؤَنَّثِ السَّالِمُ:** مِثْلُ: <span class="highlight-red">طَالِبَات</span>، <span class="highlight-blue">مُمَرِّضَات</span>.
*   **جَمْعُ التَّكْسِيرِ (مُفْرَدُهُ بِتَاءٍ):** مِثْلُ: <span class="highlight-red">بُيُوت</span> (مُفْرَدُهَا بَيْت)، <span class="highlight-blue">أَمْوَات</span>، <span class="highlight-green">أَبْيَات</span>.
[RIGHT_TITLE]: فِي الأَفْعَالِ
[RIGHT_CONTENT]:
(Component: TEMPLATE_C_LIST)
List Items:
*   **تَاءُ التَّأْنِيثِ السَّاكِنَةُ:** مِثْلُ: <span class="highlight-red">دَرَسَتْ</span>، <span class="highlight-blue">كَتَبَتْ</span>.
*   **تَاءُ الرَّفْعِ المُتَحَرِّكَةُ:** مِثْلُ: <span class="highlight-red">دَرَسْتُ</span>، <span class="highlight-blue">كَتَبْتِ</span>، <span class="highlight-green">كَتَبْتَ</span>.
*   **مِنْ أَصْلِ الفِعْلِ:** مِثْلُ: <span class="highlight-red">ثَبَتَ</span>، <span class="highlight-blue">نَبَتَ</span>، <span class="highlight-green">كَبَتَ</span>.

=== BLOCK 4: [Analysis Table: Open Ta] ===
(Component: TEMPLATE_C_TABLE)
Title: نَمَاذِجُ مُعَلَّلَةٌ (التَّاءُ المَبْسُوطَةُ)
Columns: الكَلِمَةُ | نَوْعُ التَّاءِ / سَبَبُ كِتَابَتِهَا مَبْسُوطَةً
Row 1: <span class="highlight-red">كَتَبَتْ</span> | لأَنَّهَا تَاءُ التَّأْنِيثِ السَّاكِنَةُ.
Row 2: <span class="highlight-red">كَتَبْتُ</span> | لأَنَّهَا تَاءُ الرَّفْعِ المُتَحَرِّكَةُ.
Row 3: <span class="highlight-red">نَبَتَ</span> | لأَنَّهَا مِنْ أَصْلِ الفِعْلِ.
Row 4: <span class="highlight-red">مُمَرِّضَات</span> | لأَنَّهَا جَاءَتْ فِي جَمْعِ المُؤَنَّثِ السَّالِمِ.
Row 5: <span class="highlight-red">بَيْت</span> | لأَنَّهَا مِنْ أَصْلِ الاِسْمِ (ثُلَاثِيٌّ سَاكِنُ الوَسَطِ).
Row 6: <span class="highlight-red">بُيُوت</span> | لأَنَّهَا جَاءَتْ فِي جَمْعِ تَكْسِيرٍ مُفْرَدُهُ مُنْتَهٍ بِتَاءٍ مَبْسُوطَةٍ.

=== BLOCK 5: [Closed Ta Definition] ===
(Component: TEMPLATE_C_BLOCK)
Title: تَعْرِيفُ التَّاءِ المَرْبُوطَةِ
Content: <p class="text-accent text-justify">هِيَ التَّاءُ الَّتِي تُلفَظُ هَاءً عِنْدَ الوَقْفِ، وَتُرْسَمُ مَرْبُوطَةً (ة / ـة) فِي آخِرِ الكَلِمَةِ.</p>

=== BLOCK 6: [Cases of Closed Ta] ===
(Component: TEMPLATE_C_LIST)
Title: مَوَاضِعُ التَّاءِ المَرْبُوطَةِ
List Items:
*   **الِاسْمُ المُفْرَدُ المُؤَنَّثُ:** سَوَاءٌ كَانَ حَقِيقِيًّا أَوْ مَجَازِيًّا. مِثْلُ: <span class="highlight-red">شَجَرَة</span>، <span class="highlight-blue">مَكْتَبَة</span>، <span class="highlight-green">فَاطِمَة</span>، <span class="highlight-red">امْرَأَة</span>.
*   **جَمْعُ التَّكْسِيرِ (مُفْرَدُهُ لَيْسَ بِتَاءٍ):** مِثْلُ: <span class="highlight-red">قُضَاة</span>، <span class="highlight-blue">أُبَاة</span>، <span class="highlight-green">حُمَاة</span>.
*   **(ثَمَّةَ) الظَّرْفِيَّةُ:** وَهِيَ اسْمُ إِشَارَةٍ يُشَارُ بِهِ إِلَى المَكَانِ البَعِيدِ.

=== BLOCK 7: [Analysis Table: Closed Ta] ===
(Component: TEMPLATE_C_TABLE)
Title: نَمَاذِجُ مُعَلَّلَةٌ (التَّاءُ المَرْبُوطَةُ)
Columns: الكَلِمَةُ | سَبَبُ كِتَابَتِهَا مَرْبُوطَةً
Row 1: <span class="highlight-red">مَكْتَبَة</span> | لأَنَّهَا جَاءَتْ فِي آخِرِ اسْمٍ مُفْرَدٍ مُؤَنَّثٍ.
Row 2: <span class="highlight-red">قُضَاة</span> | لأَنَّهَا جَاءَتْ فِي جَمْعِ تَكْسِيرٍ مُفْرَدُهُ غَيْرُ مُنْتَهٍ بِتَاءٍ مَبْسُوطَةٍ.

=== BLOCK 8: [Summary Matrix] ===
(Component: TEMPLATE_C_TABLE)
Title: الخُلَاصَةُ (الفَرْقُ بَيْنَ التَّاءَيْنِ)
Columns: وَجْهُ المُقَارَنَةِ | التَّاءُ المَبْسُوطَةُ | التَّاءُ المَرْبُوطَةُ
Row 1: النُّطْقُ عِنْدَ الوَقْفِ | تُلفَظُ تَاءً (تْ) | تُلفَظُ هَاءً (هْ)
Row 2: الرَّسْمُ الكِتَابِيُّ | تَكُونُ مَفْتُوحَةً (ت) | تَكُونُ مَرْبُوطَةً (ة / ـة)
Row 3: مِثَالٌ | <span class="highlight-red">بَيْت</span> | <span class="highlight-blue">مَدْرَسَة</span>

=== BLOCK 9: [Evaluation] ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: عَلِّلْ كِتَابَةَ التَّاءِ مَبْسُوطَةً فِي كَلِمَةِ "أَمْوَات".
Number: ٢
Question: عَلِّلْ كِتَابَةَ التَّاءِ مَرْبُوطَةً فِي كَلِمَةِ "حُمَاة".
Number: ٣
Question: اخْتَرْ الإِجَابَةَ الصَّحِيحَةَ: كُتِبَتِ التَّاءُ فِي "رَعَاة" مَرْبُوطَةً لأَنَّهَا...

--- END STREAM ---
