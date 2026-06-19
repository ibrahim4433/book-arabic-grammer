# **SESSION 58.0**

[TASK DEFINITION]
Objective: Implement التَّاءُ الْمَبْسُوطَةُ وَالتَّاءُ الْمَرْبُوطَةُ.
File: `pages/58.0_nXX_التَّاءُ الْمَبْسُوطَةُ وَالتَّاءُ الْمَرْبُوطَةُ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/58.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 58
[CHAPTER_TITLE]: التَّاءُ الْمَبْسُوطَةُ وَالتَّاءُ الْمَرْبُوطَةُ
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم الإملاء
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: تَعْرِيفُ التَّاءِ الْمَبْسُوطَةِ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَوَّلًا: التَّاءُ الْمَبْسُوطَةُ (ت)
Content:
<div class="mt-1mm text-accent">هِيَ التَّاءُ الَّتِي تُلفَظُ (تَاءً تْ) عِنْدَ الوَقْفِ عَلَيْهَا بِالسُّكُونِ (نَقُولُ: بَيْتْ). تُرْسَمُ مَفْتُوحَةً (ت) فِي آخِرِ الاسْمِ أَوِ الفِعْلِ أَوِ الْحَرْفِ.</div>

=== BLOCK 3: مَوَاضِعُ التَّاءِ الْمَبْسُوطَةِ الرَّئِيسِيَّةُ ===
(Component: TEMPLATE_C_SPLIT.html)
LeftSide:
  (Component: TEMPLATE_C_BLOCK.html)
  Title: ١- فِي الأَفْعَالِ دَائِماً:
  Content:
  (Component: TEMPLATE_C_LIST.html)
  [LIST_ITEM_CONTENT]: <span class="font-bold">تَاءُ التَّأْنِيثِ السَّاكِنَةُ:</span> <span class="highlight-red">ذَهَبَتْ</span>، <span class="highlight-red">كَتَبَتْ</span>، <span class="highlight-red">رَسَمَتْ</span>.
  [LIST_ITEM_CONTENT]: <span class="font-bold">تَاءُ الْفَاعِلِ الْمُتَحَرِّكَةُ:</span> <span class="highlight-red">ذَهَبْتُ</span>، <span class="highlight-red">ذَهَبْتَ</span>، <span class="highlight-red">ذَهَبْتِ</span>.
  [LIST_ITEM_CONTENT]: <span class="font-bold">التَّاءُ الْأَصْلِيَّةُ فِي الْفِعْلِ:</span> <span class="highlight-red">مَاتَ</span>، <span class="highlight-red">نَبَتَ</span>، <span class="highlight-red">صَمَتَ</span>، <span class="highlight-red">فَاتَ</span>.
RightSide:
  (Component: TEMPLATE_C_BLOCK.html)
  Title: ٢- فِي الأَسْمَاءِ:
  Content:
  (Component: TEMPLATE_C_LIST.html)
  [LIST_ITEM_CONTENT]: <span class="font-bold">التَّاءُ الْأَصْلِيَّةُ فِي الِاسْمِ الثُّلَاثِيِّ السَّاكِنِ الْوَسَطِ:</span> <span class="highlight-red">بَيْت</span> ، <span class="highlight-red">وَقْت</span> ، <span class="highlight-red">زَيْت</span> ، <span class="highlight-red">مَوْت</span>.
  [LIST_ITEM_CONTENT]: <span class="font-bold">جَمْعُ المُؤَنَّثِ السَّالِمُ:</span> <span class="highlight-red">طَالِبَات</span> ، <span class="highlight-red">مُمَرِّضَات</span> ، <span class="highlight-red">مُعَلِّمَات</span>.
  [LIST_ITEM_CONTENT]: <span class="font-bold">جَمْعُ التَّكْسِيرِ (الَّذِي يَنْتَهِي مُفْرَدُهُ بِتَاءٍ مَبْسُوطَةٍ):</span> <span class="highlight-red">أَوْقَات</span> (مِنْ <span class="highlight-blue">وَقْت</span>)، <span class="highlight-red">بُيُوت</span> (<span class="highlight-blue">بَيْت</span>)، <span class="highlight-red">أَمْوَات</span> (<span class="highlight-blue">مَيْت</span>).

=== BLOCK 4: تَعْرِيفُ التَّاءِ الْمَرْبُوطَةِ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ثَانِياً: التَّاءُ الْمَرْبُوطَةُ (ة / ـة)
Content:
<div class="mt-1mm text-accent">هِيَ التَّاءُ الَّتِي تُلفَظُ (هَاءً هْ) عِنْدَ الوَقْفِ عَلَيْهَا بِالسُّكُونِ (نَقُولُ: مَدْرَسَهْ)، وَلَكِنَّهَا تُنْطَقُ (تَاءً) عِنْدَ الْوَصْلِ بِالْحَرَكَاتِ (مَدْرَسَةُ الْعِلْمِ).</div>

=== BLOCK 5: مَوَاضِعُ التَّاءِ الْمَرْبُوطَةِ الرَّئِيسِيَّةُ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مَوَاضِعُهَا الرَّئِيسِيَّةُ:
Content:
(Component: TEMPLATE_C_LIST.html)
  [LIST_ITEM_CONTENT]: <span class="font-bold">١- الِاسْمُ المُفْرَدُ المُؤَنَّثُ:</span> دَائِماً مَرْبُوطَةٌ فِي الْأَسْمَاءِ الصِّفَاتِ وَالْجَوَامِدِ. حَقِيقِيٌّ: <span class="highlight-red">عَالِيَة</span>، <span class="highlight-red">فَاتِنَة</span>، <span class="highlight-red">طَالِبَة</span>، <span class="highlight-red">مُعَلِّمَة</span>. مَجَازِيٌّ: <span class="highlight-red">مَدْرَسَة</span>، <span class="highlight-red">شَجَرَة</span>، <span class="highlight-red">مَكْتَبَة</span>، <span class="highlight-red">لَوْحَة</span>، <span class="highlight-red">كُرَة</span>.
  [LIST_ITEM_CONTENT]: <span class="font-bold">٢- جَمْعُ التَّكْسِيرِ (الَّذِي لَا يَنْتَهِي مُفْرَدُهُ بِتَاءٍ مَبْسُوطَةٍ):</span> <span class="highlight-red">قُضَاة</span> (مُفْرَدُهُ قَاضِي). عُظَمَا... لَا! <span class="highlight-red">حُمَاة</span> (مُفْرَدُهُ حَامِي)، <span class="highlight-red">أُبَاة</span> (آبِي)، <span class="highlight-red">رُمَاة</span> (مُفْرَدُهُ رَامِي).
  [LIST_ITEM_CONTENT]: <span class="font-bold">٣- ثَمَّةَ الظَّرْفِيَّةُ (بِمَعْنَى هُنَاكَ):</span> ثَمَّةَ رَجُلٌ عَلَى الْبَابِ.

=== BLOCK 6: تَنْبِيهٌ هَامٌّ بَيْنَ (ثَمَّةَ) وَ(ثُمَّتَ) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: <span class="font-bold">تَنْبِيهٌ:</span> لِلتَّمْيِيزِ عَنْ <span class="highlight-red">ثُمَّتَ</span> حَرْفِ الْعَطْفِ الَّذِي يُكْتَبُ مَبْسُوطاً، نَكْتُبُ <span class="highlight-blue">ثَمَّةَ</span> الظَّرْفِيَّةُ بِتَاءٍ مَرْبُوطَةٍ. مِثَالٌ: ثَمَّةَ رَجُلٌ عَلَى الْبَابِ.

=== BLOCK 7: جَدْوَلٌ تَلْخِيصِيٌّ (Matrix) ===
(Component: TEMPLATE_C_TABLE.html)
Headers: النَّوْعُ | كَيْفِيَّةُ اللَّفْظِ عِنْدَ الْوَقْفِ | أَمْثِلَةٌ
Rows:
- التَّاءُ الْمَبْسُوطَةُ | تُلفَظُ (تَاءً تْ) عِنْدَ الوَقْفِ بِالسُّكُونِ | ذَهَبَتْ، بَيْت، مُعَلِّمَات
- التَّاءُ الْمَرْبُوطَةُ | تُلفَظُ (هَاءً هْ) عِنْدَ الوَقْفِ بِالسُّكُونِ وَ(تَاءً) عِنْدَ الْوَصْلِ | مَدْرَسَة، قُضَاة، حُمَاة

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: بَيِّنْ نَوْعَ التَّاءِ فِي الْكَلِمَاتِ التَّالِيَةِ مَعَ ذِكْرِ السَّبَبِ: كَتَبَتْ، مَدْرَسَةٌ، قُضَاةٌ، أَوْقَاتٌ.
Number: ٢
Question: ضَعْ كَلِمَةَ (ثَمَّةَ) وَ(ثُمَّتَ) فِي جُمْلَتَيْنِ مُفِيدَتَيْنِ لِتَوْضِيحِ الْفَرْقِ بَيْنَهُمَا.

--- END STREAM ---