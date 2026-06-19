# **SESSION 39.0**

[TASK DEFINITION]
Objective: Implement الْمَمْنُوعُ مِنَ الصَّرْفِ.
File: `pages/39_nXX_الْمَمْنُوعُ مِنَ الصَّرْفِ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/39.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 39
[CHAPTER_TITLE]: الْمَمْنُوعُ مِنَ الصَّرْفِ
[CATEGORY_HEADER]: المستوى المتقدم
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition & Rule ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَعْرِيفُ الْمَمْنُوعِ مِنَ الصَّرْفِ
Content: <p class="text-accent mb-2mm">الْأَصْلُ فِي الْأَسْمَاءِ فِي اللُّغَةِ الْعَرَبِيَّةِ أَنْ تَقْبَلَ التَّنْوِينَ (<span class="highlight-blue">خَالِدٌ</span>، <span class="highlight-blue">خَالِداً</span>، <span class="highlight-blue">خَالِدٍ</span>)، وَتُجَرَّ بِالْكَسْرَةِ.</p><p class="text-accent mb-2mm">وَلَكِنْ هُنَاكَ أَسْمَاءٌ مَرِيضَةٌ (لِعِلَّةٍ أَوْ سَبَبٍ نَحْوِيٍّ) لَا تَتَحَمَّلُ التَّنْوِينَ أَبَدًا، وَتُسَمَّى <span class="font-bold highlight-red">الْمَمْنُوعَ مِنَ الصَّرْفِ</span>.</p>

=== BLOCK 3: Golden Rule Benefit ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Content: الْقَاعِدَةُ الذَّهَبِيَّةُ لِلْمَمْنُوعِ مِنَ الصَّرْفِ: يُرْفَعُ بِالضَّمَّةِ بِدُونِ تَنْوِينٍ (<span class="highlight-blue">أَسْعَدُ</span>)، يُنْصَبُ بِالْفَتْحَةِ بِدُونِ تَنْوِينٍ (<span class="highlight-blue">أَسْعَدَ</span>)، ويُجَرُّ بِالْفَتْحَةِ أيضاً نِيَابَةً عَنِ الْكَسْرَةِ! (سَلَّمْتُ عَلَى <span class="highlight-red">أَسْعَدَ</span>).

=== BLOCK 4: The Core Matrix (Summary Table) ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: النَّوْعُ
[HEADER_2]: التَّفْصِيلُ
[HEADER_3]: الْأَمْثِلَةُ
[ROW_1_COL_1]: لِعِلَّتَيْنِ (الْعَلَمُ)
[ROW_1_COL_2]: الْمُؤَنَّثُ، الْأَعْجَمِيُّ، الْمُرَكَّبُ، الْمَزِيدُ، وَزْنُ الْفِعْلِ، الْمَعْدُولُ
[ROW_1_COL_3]: بَغْدَادُ، وَاشِنْطُنُ، بَعْلَبَكُّ، مَرْوَانُ، أَسْعَدُ، مُضَرُ
[ROW_2_COL_1]: لِعِلَّتَيْنِ (الصِّفَةُ)
[ROW_2_COL_2]: وَزْنُ أَفْعَلَ، وَزْنُ فَعْلَانَ، وَزْنُ فُعَالٍ/مَفْعَلٍ، أُخَرُ
[ROW_2_COL_3]: أَحْمَرُ، عَطْشَانُ، ثُلَاثُ، أُخَرُ
[ROW_3_COL_1]: لِعِلَّةٍ وَاحِدَةٍ
[ROW_3_COL_2]: أَلِفُ التَّأْنِيثِ الْمَقْصُورَةُ/الْمَمْدُودَةُ، صِيغَةُ مُنْتَهَى الْجُمُوعِ
[ROW_3_COL_3]: ذِكْرَى، صَحْرَاءُ، مَصَانِعُ، مَصَابِيحُ

=== BLOCK 5: Deep Dive Split (Mamnūʿ for Two Causes) ===
(Component: TEMPLATE_C_SPLIT.html)
[LEFT_SIDE_COMPONENTS]:
(Component: TEMPLATE_C_BLOCK.html)
Title: ثَانِيًا: الصِّفَاتُ الْمَمْنُوعَةُ
Content:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: عَلَى وَزْنِ <span class="highlight-blue">أَفْعَلَ</span> (وَمُؤَنَّثُهُ فَعْلَاءُ/فُعْلَى): <span class="highlight-red">أَحْمَرُ</span> حَمْرَاءُ، <span class="highlight-red">أَكْبَرُ</span> كُبْرَى، <span class="highlight-red">أَفْضَلُ</span>، <span class="highlight-red">أَسْوَدُ</span>.
[LIST_ITEM_CONTENT]: عَلَى وَزْنِ <span class="highlight-blue">فَعْلَانَ</span> (وَمُؤَنَّثُهُ فَعْلَى): <span class="highlight-red">عَطْشَانُ</span> عَطْشَى، <span class="highlight-red">غَضْبَانُ</span>، <span class="highlight-red">جَوْعَانُ</span>.
[LIST_ITEM_CONTENT]: الْأَعْدَادُ عَلَى وَزْنِ <span class="highlight-blue">فُعَالٍ</span> أَوْ <span class="highlight-blue">مَفْعَلٍ</span>: <span class="highlight-red">ثُلَاثُ</span>، <span class="highlight-red">مَثْنَى</span>.
[LIST_ITEM_CONTENT]: كَلِمَةُ <span class="highlight-red">أُخَرَ</span> (جَمْعُ أُخْرَى).

[RIGHT_SIDE_COMPONENTS]:
(Component: TEMPLATE_C_BLOCK.html)
Title: أَوَّلًا: الْمَمْنُوعُ مِنْ الصَّرْفِ لِعِلَّتَيْنِ (الْعَلَمُ)
Content:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: الْعَلَمُ الْمُؤَنَّثُ: <span class="highlight-red">بَغْدَادُ</span>، <span class="highlight-red">كَامِلَةُ</span>، <span class="highlight-red">عَفَافُ</span>، <span class="highlight-red">سُعَادُ</span>، <span class="highlight-red">عَنْتَرَةُ</span>. يُصْرَفُ إِذَا كَانَ ثُلَاثِيًّا سَاكِنَ الْوَسَطِ مِثْلُ: هِنْدٌ، دَعْدٌ.
[LIST_ITEM_CONTENT]: الْعَلَمُ الْأَعْجَمِيُّ (زَائِدٌ عَنْ ٣ أَحْرُفٍ): <span class="highlight-red">وَاشِنْطُنُ</span>، <span class="highlight-red">مَايْكِلُ</span>، <span class="highlight-red">لُنْدُنُ</span>، <span class="highlight-red">جُورْجُ</span>. يُصْرَفُ إِذَا كَانَ ثُلَاثِيًّا سَاكِنَ الْوَسَطِ مِثْلُ: جُونٌ، بُولٌ، نِيلٌ.
[LIST_ITEM_CONTENT]: الْعَلَمُ الْمُرَكَّبُ مَزْجِيًّا: <span class="highlight-red">بَعْلَبَكُّ</span>، <span class="highlight-red">حَضْرَمَوْتُ</span>، <span class="highlight-red">بُورْسَعِيدُ</span>.
[LIST_ITEM_CONTENT]: الْعَلَمُ الْمُنْتَهِي بِأَلِفٍ وَنُونٍ زَائِدَتَيْنِ: <span class="highlight-red">مَرْوَانُ</span>، <span class="highlight-red">كَهْلَانُ</span>، <span class="highlight-red">غَسَّانُ</span>، <span class="highlight-red">عَدْنَانُ</span>.
[LIST_ITEM_CONTENT]: الْعَلَمُ عَلَى وَزْنِ الْفِعْلِ: <span class="highlight-red">أَسْعَدُ</span>، <span class="highlight-red">يَزِيدُ</span>، <span class="highlight-red">يَشْكُرُ</span>.
[LIST_ITEM_CONTENT]: الْعَلَمُ الْمَعْدُولُ (عَلَى وَزْنِ فُعَلَ): <span class="highlight-red">مُضَرُ</span>، <span class="highlight-red">زُحَلُ</span>، <span class="highlight-red">قُزَحُ</span>.

=== BLOCK 6: Deep Dive (Mamnūʿ for One Cause) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ثَالِثًا: الْمَمْنُوعُ مِنَ الصَّرْفِ لِعِلَّةٍ وَاحِدَةٍ
Content:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: أَلِفُ التَّأْنِيثِ الْمَقْصُورَةُ الزَّائِدَةُ: <span class="highlight-red">ذِكْرَى</span>، <span class="highlight-red">سَلْوَى</span>، <span class="highlight-red">مَرْضَى</span>. (أَمَّا فَتًى فَمَصْرُوفٌ لِأَنَّ الْأَلِفَ أَصْلِيَّةٌ).
[LIST_ITEM_CONTENT]: أَلِفُ التَّأْنِيثِ الْمَمْدُودَةُ: <span class="highlight-red">صَحْرَاءُ</span>، <span class="highlight-red">عُلَمَاءُ</span>، <span class="highlight-red">أُدَبَاءُ</span>، <span class="highlight-red">حَمْرَاءُ</span>. (أَمَّا سَمَاءٌ وَمَاءٌ فَمَصْرُوفٌ لِأَنَّ الْهَمْزَةَ أَصْلِيَّةٌ أَوْ مُنْقَلِبَةٌ).
[LIST_ITEM_CONTENT]: صِيغَةُ مُنْتَهَى الْجُمُوعِ (أَهَمُّ نَوْعٍ!): كُلُّ جَمْعِ تَكْسِيرٍ فِيهِ أَلِفٌ فِي النِّصْفِ، بَعْدَهَا حَرْفَانِ أَوْ ثَلَاثَةُ أَحْرُفٍ أَوْسَطُهَا سَاكِنٌ. مِثَالُ حَرْفَيْنِ: <span class="highlight-red">مَصَانِعُ</span>، <span class="highlight-red">مَكَاتِبُ</span>، <span class="highlight-red">مَدَارِسُ</span>، <span class="highlight-red">قَنَابِلُ</span>. مِثَالُ ثَلَاثَةِ أَحْرُفٍ أَوْسَطُهَا سَاكِنٌ: <span class="highlight-red">مَصَابِيحُ</span>، <span class="highlight-red">تَلَامِيذُ</span>، <span class="highlight-red">مَفَاتِيحُ</span>.

=== BLOCK 7: Benefit Warning ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: يُصْرَفُ جَمْعُ التَّكْسِيرِ إِذَا كَانَ بَعْدَ الْأَلِفِ ٣ أَحْرُفٍ مُتَحَرِّكَةِ الْوَسَطِ مِثْلُ: <span class="highlight-blue">تَلَامِذَةٌ</span>، <span class="highlight-blue">فَلَاسِفَةٌ</span>.

=== BLOCK 8: Exceptions (When is it Declined?) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مَتَى يُصْرَفُ الْمَمْنُوعُ مِنَ الصَّرْفِ؟ (الْجَرُّ بِالْكَسْرَةِ بَدَلَ الْفَتْحَةِ)
Content: يُصْرَفُ الْمَمْنُوعُ مِنَ الصَّرْفِ (أَيْ نُعِيدُ إِلَيْهِ الْكَسْرَةَ فِي حَالَةِ الْجَرِّ) فِي حَالَتَيْنِ فَقَطْ:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: إِذَا دَخَلَتْ عَلَيْهِ (ال) التَّعْرِيفِ: تَجَوَّلْتُ فِي <span class="highlight-red">مَصَانِعَ</span> كَثِيرَةٍ. (مَمْنُوعٌ مِنَ الصَّرْفِ: مَجْرُورٌ بِالْفَتْحَةِ). تَجَوَّلْتُ فِي <span class="highlight-blue">الْمَصَانِعِ</span> الْكَثِيرَةِ. (فِيهَا الـ: مَجْرُورٌ بِالْكَسْرَةِ).
[LIST_ITEM_CONTENT]: إِذَا أُضِيفَ (أَتَى بَعْدَهُ مُضَافٌ إِلَيْهِ): تَجَوَّلْتُ فِي <span class="highlight-blue">مَصَانِعِ</span> الْمَدِينَةِ. (مُضَافٌ: مَجْرُورٌ بِالْكَسْرَةِ).

=== BLOCK 9: I'rab Details ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[BOX_1_WORD]: مِصْرَ
[BOX_1_DETAILS]: اسْمٌ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِعِلَّتَيْنِ الْعَلَمِيَّةِ وَالتَّأْنِيثِ. (سَافَرْتُ إِلَى مِصْرَ)
[BOX_2_WORD]: مَتَاحِفَ
[BOX_2_DETAILS]: اسْمٌ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ صِيغَةُ مُنْتَهَى الْجُمُوعِ. (تَجَوَّلْتُ فِي مَتَاحِفَ أَثَرِيَّةٍ)

=== BLOCK 10: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: اسْتَخْرِجِ الِاسْمَ الْمَمْنُوعَ مِنَ الصَّرْفِ وَبَيِّنْ سَبَبَ الْمَنْعِ: (سَافَرْتُ إِلَى مِصْرَ).

=== BLOCK 11: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: أَعْرِبْ كَلِمَةَ (مَتَاحِفَ) فِي الْجُمْلَةِ: (تَجَوَّلْتُ فِي مَتَاحِفَ أَثَرِيَّةٍ).

--- END STREAM ---
