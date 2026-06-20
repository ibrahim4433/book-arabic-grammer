# **SESSION 04.0**

[TASK DEFINITION]
Objective: Implement الْحَرْفُ وَعَلَاَّمَاتُهُ وَأَنْوَاعُهُ.
File: `pages/04.0_nXX_الْحَرْفُ وَعَلَاَّمَاتُهُ وَأَنْوَاعُهُ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/04.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 04
[CHAPTER_TITLE]: الْحَرْفُ وَعَلَاَّمَاتُهُ وَأَنْوَاعُهُ
[CATEGORY_HEADER]:
[SECTION_HEADER]:
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: مُقَدَّمَةً ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مُقَدَّمَةً
Content:
<p class="text-accent">الْقِسْمُ الثَّالِثُ وَالْأَخِيرُ مِن أَقْسَامِ الْكَلَاَمِ فِي اللُّغَةَ الْعَرَبِيَّةَ هُو <span class="highlight-red">الْحَرْفَ</span>.</p>
<p>وقَد دَرَسَنَا سَابِقَا الْاِسْمِ وَعَلَاَّمَاتِهِ ، وَالْفِعْلَ وَعَلَاَّمَاتِهِ ، وَالْيَوْمَ نَتَعَرَّفُ عَلَى الْقِسْمِ الَّذِي يَرْبُطُ بَيْن الْأَسْمَاءِ وَالْأَفْعَالِ لِيُكَوِّنُ لَنَا جَمَلًا مُفِيدَةً.</p>

=== BLOCK 3: تَعْرِيفُ الْحَرْفِ ===
(Component: TEMPLATE_C_SPLIT.html)
Left Column (TEMPLATE_C_BLOCK.html):
Title: 1. تَعْرِيفُ الْحَرْفِ
Content:
<p class="text-accent">هُو : كَلِمَةُ دَلَّتْ عَلَى مُعَنًّى فِي غَيْرِهَا.</p>
<p>أي أَنّ الْحَرْفِ لَه مُعَنًّى ، ولَكِنّ هَذَا الْمُعَنَّى لَا يَظْهَرُ مُسْتَقِلًّا أَو وَاضِحًا بِمُفْرَدِهِ ، بَل يَظْهَرُ مُعَنَّاُهُ وَتَتَّضِحُ وَظِيفَتُهُ فقَطّ عِنْدَمَا يُوضَعُ فِي سِيَاقِ جُمْلَةِ مُفِيدَةِ.</p>

Right Column (TEMPLATE_C_BLOCK.html):
Title: مِثَالَ
Content:
<p>حَرْفُ الْجَرِّ <span class="highlight-red">( إِلَى )</span>.</p>
<p>إِذَا قُلْتُهُ بِمُفْرَدِهِ لَا يُفِيدُ مُعَنَّى كَامِلًا ، ولَكِنّ عِنْدَمَا نَضَعُهُ فِي الْمِثَالِ :" ثُمَّ أَتِمُّوا الْعَمَلَ <span class="highlight-red">إِِْلََى</span> اللَّيْلِ "، يَظْهَرُ مُعَنَّاُهُ بِوُضُوحٍ وهُو :" اِنْتِهَاءُ الْغَايَةِ الزَّمَانِيَّةِ ".</p>

=== BLOCK 4: عَلَاَّمَاتُ الْحَرْفِ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: 2. عَلَاَّمَاتُ الْحَرْفِ
Content:
<p>كَيْف نَعْرُفُ أَنّ هَذِه الْكَلِمَةِ حَرْفٌ ؟</p>
<p class="text-accent">لِلْحَرْفُ عَلَاَّمَةُ عَدَمِيَّةُ ( أَيَّ تُعْرَفُ بِالنَّفْي ): فهُو لَا يَقْبَلُ شَيْئًا مِن عَلَاَّمَاتِ الْاِسْمِ ، ولَا يَقْبَلُ شَيْئًا مِن عَلَاَّمَاتِ الْفِعْلِ .</p>
(Component: TEMPLATE_C_LIST.html)
- لَا يَقْبَلُ ( الً ، التَّنْوِينَ ، التَّاءَ الْمَرْبُوطَةَ ...) فهُو لَيْس اِسْمًا
- لَا يَقْبَلُ ( تَاءَ التَّأْنِيثِ ، تَاءَ الْفَاعِلِ ، لَم ، لَن ، قَد ، السِّينَ ...) فهُو لَيْس فِعْلًا

=== BLOCK 5: تَلْميحٌ ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Title: تَلْميحٌ
Content:
<p><strong>قَاعِدَةَ ثَابتةِ :</strong> جَمِيعُ الْحُروفِ <span class="highlight-red">مَبْنِيَّةَ</span> دَائِمًا .( أي لَا يَتَغَيَّرُ شَكْلُ آخِرِهَا بِاِخْتِلَاَفِ مَوْقِعِهَا فِي الْجُمْلَةِ ).</p>

=== BLOCK 6: أَنْوَاعُ الْحُروفِ فِي اللُّغَةَ الْعَرَبِيَّةَ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: 3. أَنْوَاعُ الْحُروفِ فِي اللُّغَةَ الْعَرَبِيَّةَ
Content:
<p>لِلْحُروفُ فِي لُغَتِنَا الْعَرَبِيَّةِ وَظَائِفَ وَأَنْوَاعَ كَثِيرَةَ ، نَذْكُرُ مِن أَهَمَّهَا</p>
(Component: TEMPLATE_C_TABLE.html)
Row 1: 1 . حُروفُ الْجَرِّ | ( مِنْ ، عَن ، إِلَى ، عَلَى ، فِي ، الْكَافَّ ، اللَّاَمَ ، الْبَاءَ )
Row 2: 2 . حُروفُ الْعَطْفِ | ( الواو ، الْفَاءَ ، ثُمَّ ، أَو ، أَم ...)
Row 3: 3 . حُروفُ النِّدَاءِ | ( يَا ، أَيَا ، هَيَا ، الْهَمْزَةَ ، أَيَّ )
Row 4: 4 . حُروفُ الْجَوَابِ | ( نَعَمٌ ، بَلَى ، أَجَلٌ ، لَا ، كَلًّا )
Row 5: 5 . حَرْفَا الْاِسْتِفْهَامِ | ( هَلٌّ ، وَالْهَمْزَةَ " أَْ " )
Row 6: 6 . حُروفُ النُّصْبِ ( لِلْفِعْلَ الْمُضَارِعَ ) | ( أَْنْ ، لَنْ ، كَيْ ، حَتَّى ، لَامَ التَّعْلِيلُ )
Row 7: 7 . حُروفُ الجزم ( لِلْفِعْلَ الْمُضَارِعَ ) | ( لَمْ ، لَمَّا ، لَامَ الْأَمْرُ ، لَا النَّاهِيَةِ )
Row 8: 8 . الْحُروفُ النَّاسِخَةُ ( إِنّْ وَأُخُوَّاتِهَا ) | ( إِنّْ ، أنّْ ، كأنّْ ، لِكَنَّ ، لَيْت ، لَعَلّ )

=== BLOCK 7: مُلَاحِظَةً ===
(Component: TEMPLATE_C_BENEFIT.html)
Title: مُلَاحِظَةً
Content:
<p>فِي الدُّرُوسِ الْقَادِمَةِ سَيَتِمُّ تَفْصِيلٌ كُلّ نَوْعٍ مِن هَذِه الْحُروفِ وَإِعْرَابِهَا فِي جُمْلَةِ .</p>

=== BLOCK 8: Exam Question 1 ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: اِخْتَرْ الْإِجَابَةَ الصَّحِيحَةَ مِمَّا بَيْن الْقَوْسَيْنِ :
- 1. الْحَرْفُ هُو كَلِمَةِ ( تَدُلُّ عَلَى مُعَنًّى فِي نَفْسهَا / تَدُلُّ عَلَى مُعَنًّى فِي غَيْرِهَا / لَيْس لَهَا أَيِّ مُعَنَّى مُطْلَقًا ).
- 2. جَمِيعُ الْحُروفِ فِي اللُّغَةَ الْعَرَبِيَّةَ ( مُعَرِّبَةَ / مَبْنِيَّةَ / بَعْضَهَا مُعَرِّبَ وبَعْضَهَا مَبْنِيَّ ).
- 3. عُلَّامَةُ الْحَرْفِ أَنّهُ ( يَقْبَلُ التَّنْوِينُ / يَقْبَلُ تَاءُ الْفَاعِلِ / لَا يَقْبَلُ عَلَاَّمَاتُ الْاِسْمِ ولَا الْفِعْلِ ).

=== BLOCK 9: Exam Question 2 ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: اِسْتَخْرَجَ الْحُروفُ مِن الْجُمْلَةِ التَّالِيَةِ وَصِنْفِ نَوْعِهَا بِنَاءً عَلَى مَا دَرَسَتْ : " ثُمَّ أَتِمُّوا الْعَمَلَ إِِْلََى اللَّيْلِ "
- الْحَرْفَ الْأَوَّلَ :.....................( نَوَّعَهُ :................)
- الْحَرْفَ الثَّانِي :.....................( نَوَّعَهُ :................)

=== BLOCK 10: Exam Question 3 ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٣
Question: اِقْرَأْ الْجُمْلَةَ التَّالِيَةَ وَصِنْفَ كَلِمَاتِهَا إِلَى ( اِسْمٌ ، فعَلّ ، حَرْفَ ) لِتَرَاجُعٍ مَا دَرْسَتِهِ فِي الدُّرُوسِ الثَّلَاثَةَ الْمَاضِيَةَ : ( لَنْ يَنْجَحَ الْكَسُولُ فِِي الِامْتِحَانِ )
- لَنْ :.....................
- يَنْجَحَ :.....................
- الْكَسُولُ :.....................
- فِِي :.....................
- الِامْتِحَانِ :.....................

--- END STREAM ---