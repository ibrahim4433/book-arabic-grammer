# **SESSION 53.0**

[TASK DEFINITION]
Objective: Implement الْهَمْزَةُ الْأَوَّلِيَّةُ (وَصْلٌ وَقَطْعٌ).
File: `pages/53.0_nXX_الْهَمْزَةُ الْأَوَّلِيَّةُ (وَصْلٌ وَقَطْعٌ).html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/53.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 53
[CHAPTER_TITLE]: الْهَمْزَةُ الْأَوَّلِيَّةُ (وَصْلٌ وَقَطْعٌ)
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم الإملاء
[AUTHOR_NAME]: أ. حنا خفيف
[AUTHOR_PHONE]:  

=== BLOCK 2: Definition of Hamzat al-Wasl ===
(Component: TEMPLATE_C_BLOCK.html)
Title: هَمْزَةُ الْوَصْلِ (<span class="highlight-red">ا</span>)
Content: <p class="text-accent font-bold">هِيَ هَمْزَةٌ تُكْتَبُ أَلِفاً بِدُونِ (<span class="highlight-blue">ء</span>). تُنْطَقُ فِي أَوَّلِ الْكَلَامِ، وَلَا تُنْطَقُ إِذَا سَبَقَهَا كَلَامٌ آخَرُ. تُسْتَخْدَمُ لِكَيْ لَا نَبْدَأَ بِحَرْفٍ سَاكِنٍ لِأَنَّ الْعَرَبَ لَا تَبْدَأُ بِسَاكِنٍ.</p>
(Component: TEMPLATE_C_BENEFIT.html)
Title: أَمْثِلَةٌ
Content:
(Component: TEMPLATE_C_LIST.html)
- [LIST_ITEM_CONTENT]: <span class="highlight-red">اِ</span>نْطَلَقَ (تُنْطَقُ فِي أَوَّلِ الْكَلَامِ)
- [LIST_ITEM_CONTENT]: وَ<span class="highlight-blue">ا</span>نْطَلَقَ (لَا تُنْطَقُ إِذَا سَبَقَهَا كَلَامٌ آخَرُ)

=== BLOCK 3: Positions of Hamzat al-Wasl (Split View) ===
(Component: TEMPLATE_C_SPLIT.html)
LeftSide:
(Component: TEMPLATE_C_BLOCK.html)
Title: ١- فِي الْأَفْعَالِ
Content:
(Component: TEMPLATE_C_LIST.html)
- [LIST_ITEM_CONTENT]: أَمْرُ الْفِعْلِ الثُّلَاثِيِّ: <span class="highlight-red">اِ</span>شْرَبْ، <span class="highlight-red">اُ</span>كْتُبْ، <span class="highlight-red">اِ</span>قْرَأْ، <span class="highlight-red">اِ</span>لْعَبْ.
- [LIST_ITEM_CONTENT]: الْخُمَاسِيُّ (مَاضِيهِ، وَأَمْرُهُ، وَمَصْدَرُهُ): <span class="highlight-red">اِ</span>نْطَلَقَ، <span class="highlight-red">اِ</span>نْطَلِقْ، <span class="highlight-red">اِ</span>نْطِلَاق. <span class="highlight-red">اِ</span>سْتَمَعَ، <span class="highlight-red">اِ</span>سْتَمِعْ، <span class="highlight-red">اِ</span>سْتِمَاع.
- [LIST_ITEM_CONTENT]: السُّدَاسِيُّ (مَاضِيهِ، وَأَمْرُهُ، وَمَصْدَرُهُ): <span class="highlight-red">اِ</span>سْتَقْبَلَ، <span class="highlight-red">اِ</span>سْتَقْبِلْ، <span class="highlight-red">اِ</span>سْتِقْبَال. <span class="highlight-red">اِ</span>سْتَخْرَجَ، <span class="highlight-red">اِ</span>سْتَخْرِجْ، <span class="highlight-red">اِ</span>سْتِخْرَاج.
RightSide:
(Component: TEMPLATE_C_BLOCK.html)
Title: ٢- فِي الْأَسْمَاءِ وَالْحُرُوفِ
Content:
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Title: الْأَسْمَاءُ الثَّمَانِيَةُ الْمَحْفُوظَةُ
Content: <span class="highlight-red">اِ</span>سْم، <span class="highlight-red">اِ</span>بْن، <span class="highlight-red">اِ</span>بْنَة، <span class="highlight-red">اِ</span>ثْنَان، <span class="highlight-red">اِ</span>ثْنَتَان، <span class="highlight-red">اِ</span>مْرُؤ، <span class="highlight-red">اِ</span>مْرَأَة، <span class="highlight-red">اِ</span>سْت (أَيِ الْأَسَاسُ).
(Component: TEMPLATE_C_BLOCK.html)
Title: ٣- فِي الْحُرُوفِ
Content: فِي أَدَاةِ التَّعْرِيفِ فَقَطْ (<span class="highlight-blue">الـ</span>): <span class="highlight-red">اَ</span>لْكِتَاب، <span class="highlight-red">اَ</span>لْمَدْرَسَة.

=== BLOCK 4: Definition of Hamzat al-Qat' ===
(Component: TEMPLATE_C_BLOCK.html)
Title: هَمْزَةُ الْقَطْعِ (<span class="highlight-red">أَ</span>، <span class="highlight-red">أُ</span>، <span class="highlight-red">إِ</span>)
Content: <p class="text-accent font-bold">هِيَ هَمْزَةٌ تُكْتَبُ مَعَ (<span class="highlight-blue">ء</span>)، وَتُنْطَقُ دَائِماً فِي جَمِيعِ الْأَحْوَالِ. وَتَكُونُ (<span class="highlight-red">أَ</span> / <span class="highlight-red">أُ</span>) إِذَا كَانَتْ مَفْتُوحَةً أَوْ مَضْمُومَةً، وَ(<span class="highlight-red">إِ</span>) إِذَا كَانَتْ مَكْسُورَةً.</p>
(Component: TEMPLATE_C_BENEFIT.html)
Title: أَمْثِلَةٌ
Content:
(Component: TEMPLATE_C_LIST.html)
- [LIST_ITEM_CONTENT]: مَفْتُوحَةً: <span class="highlight-red">أَ</span>كَلَ
- [LIST_ITEM_CONTENT]: مَضْمُومَةً: <span class="highlight-red">أُ</span>سْتَاذ
- [LIST_ITEM_CONTENT]: مَكْسُورَةً: <span class="highlight-red">إِ</span>نْسَان

=== BLOCK 5: Positions of Hamzat al-Qat' (Split View) ===
(Component: TEMPLATE_C_SPLIT.html)
LeftSide:
(Component: TEMPLATE_C_BLOCK.html)
Title: ١- فِي الْأَفْعَالِ
Content:
(Component: TEMPLATE_C_LIST.html)
- [LIST_ITEM_CONTENT]: مَاضِي الثُّلَاثِيِّ وَمَصْدَرُهُ: <span class="highlight-red">أَ</span>كَلَ - <span class="highlight-red">أَ</span>كْلاً، <span class="highlight-red">أَ</span>خَذَ - <span class="highlight-red">أَ</span>خْذاً.
- [LIST_ITEM_CONTENT]: الرُّبَاعِيُّ (مَاضِيهِ وَأَمْرُهُ وَمَصْدَرُهُ): <span class="highlight-red">أَ</span>قْبَلَ، <span class="highlight-red">أَ</span>قْبِلْ، <span class="highlight-red">إِ</span>قْبَال. <span class="highlight-red">أَ</span>كْرَمَ، <span class="highlight-red">أَ</span>كْرِمْ، <span class="highlight-red">إِ</span>كْرَام.
- [LIST_ITEM_CONTENT]: كُلُّ فِعْلٍ مُضَارِعٍ يَبْدَأُ بِالْهَمْزَةِ (<span class="highlight-blue">أَنَا</span>): <span class="highlight-red">أَ</span>شْرَبُ، <span class="highlight-red">أَ</span>نْطَلِقُ، <span class="highlight-red">أَ</span>سْتَقْبِلُ، <span class="highlight-red">أَ</span>لْعَبُ.
RightSide:
(Component: TEMPLATE_C_BLOCK.html)
Title: ٢- فِي الْأَسْمَاءِ وَالْحُرُوفِ
Content:
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: فِي الْأَسْمَاءِ
Content: جَمِيعُ الْأَسْمَاءِ فِي اللُّغَةِ مَا عَدَا الثَّمَانِيَةَ: <span class="highlight-red">أَ</span>مْجَد، <span class="highlight-red">إِ</span>سْعَاد، <span class="highlight-red">أَ</span>سَد، <span class="highlight-red">إِ</span>نْسَان، <span class="highlight-red">أَ</span>ب، <span class="highlight-red">أُ</span>خْت.
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: ٣- فِي الْحُرُوفِ
Content: جَمِيعُ الْحُرُوفِ مَا عَدَا (<span class="highlight-blue">الـ</span>): <span class="highlight-red">إِ</span>لَى، <span class="highlight-red">إِ</span>نَّ، <span class="highlight-red">أَ</span>نْ، <span class="highlight-red">أَ</span>وْ، <span class="highlight-red">أَ</span>مْ.

=== BLOCK 6: Summary Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Headers: النَّوْعُ | مَوَاضِعُ الْأَفْعَالِ | مَوَاضِعُ الْأَسْمَاءِ | مَوَاضِعُ الْحُرُوفِ
Row 1: هَمْزَةُ الْوَصْلِ (<span class="highlight-red">ا</span>) | أَمْرُ الثُّلَاثِيِّ، الْخُمَاسِيُّ، السُّدَاسِيُّ | الْأَسْمَاءُ الثَّمَانِيَةُ فَقَطْ | أَدَاةُ التَّعْرِيفِ (<span class="highlight-blue">الـ</span>) فَقَطْ
Row 2: هَمْزَةُ الْقَطْعِ (<span class="highlight-red">أَ</span>، <span class="highlight-red">إِ</span>، <span class="highlight-red">أُ</span>) | مَاضِي ومَصْدَرُ الثُّلَاثِيِّ، الرُّبَاعِيُّ، الْمُضَارِعُ كُلُّهُ | جَمِيعُ الْأَسْمَاءِ (مَا عَدَا الثَّمَانِيَةَ) | جَمِيعُ الْحُرُوفِ (مَا عَدَا <span class="highlight-blue">الـ</span>)

=== BLOCK 7: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: حَدِّدْ نَوْعَ الْهَمْزَةِ وَالسَّبَبَ فِي الْكَلِمَاتِ التَّالِيَةِ: (اِسْتِغْفَار، أَحْسَنَ، اِبْن).
Number: ٢
Question: صَوِّبِ الْخَطَأَ الْإِمْلَائِيَّ فِي الْجُمْلَةِ التَّالِيَةِ: (إِنْطَلَقَ أَلْقِطَارُ مُسْرِعاً).
Number: ٣
Question: اِئْتِ بِفِعْلٍ خُمَاسِيٍّ وَحَدِّدْ نَوْعَ هَمْزَتِهِ.

--- END STREAM ---