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
Content: الْقِسْمُ الثَّالِثُ وَالْأَخِيرُ مِن أَقْسَامِ الْكَلَاَمِ فِي اللُّغَةَ الْعَرَبِيَّةَ هُو <span class="highlight-red">الْحَرْفَ</span>. وقَد دَرَسَنَا سَابِقَا الْاِسْمِ وَعَلَاَّمَاتِهِ ، وَالْفِعْلَ وَعَلَاَّمَاتِهِ ، وَالْيَوْمَ نَتَعَرَّفُ عَلَى الْقِسْمِ الَّذِي يَرْبُطُ بَيْن الْأَسْمَاءِ وَالْأَفْعَالِ لِيُكَوِّنُ لَنَا جَمَلًا مُفِيدَةً.

=== BLOCK 3: تَعْرِيفُ الْحَرْفِ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ١. تَعْرِيفُ الْحَرْفِ
Content: هُو : <span class="text-accent">كَلِمَةُ دَلَّتْ عَلَى مُعَنًّى فِي غَيْرِهَا</span>. أي أَنّ الْحَرْفِ لَه مُعَنًّى ، ولَكِنّ هَذَا الْمُعَنَّى لَا يَظْهَرُ مُسْتَقِلًّا أَو وَاضِحًا بِمُفْرَدِهِ ، بَل يَظْهَرُ مُعَنَّاُهُ وَتَتَّضِحُ وَظِيفَتُهُ فقَطّ عِنْدَمَا يُوضَعُ فِي سِيَاقِ جُمْلَةِ مُفِيدَةِ.

=== BLOCK 4: مِثَالَ ===
(Component: TEMPLATE_C_BENEFIT.html)
Title: مِثَالَ
Content: حَرْفُ الْجَرِّ (<span class="highlight-blue">إِلَى</span>). إِذَا قُلْتُهُ بِمُفْرَدِهِ لَا يُفِيدُ مُعَنَّى كَامِلًا ، ولَكِنّ عِنْدَمَا نَضَعُهُ فِي الْمِثَالِ : "ثُمَّ أَتِمُّوا الْعَمَلَ <span class="highlight-red">إِِْلََى</span> اللَّيْلِ" ، يَظْهَرُ مُعَنَّاُهُ بِوُضُوحٍ وهُو : "اِنْتِهَاءُ الْغَايَةِ الزَّمَانِيَّةِ".

=== BLOCK 5: عَلَاَّمَاتُ الْحَرْفِ ===
(Component: TEMPLATE_C_SPLIT.html)
Left-Side (Logical Left / Visual Right):
  (Component: TEMPLATE_C_BLOCK.html)
  Title: ٢. عَلَاَّمَاتُ الْحَرْفِ
  Content: كَيْف نَعْرُفُ أَنّ هَذِه الْكَلِمَةِ حَرْفٌ ؟ لِلْحَرْفُ عَلَاَّمَةُ عَدَمِيَّةُ ( أَيَّ تُعْرَفُ بِالنَّفْي ): <span class="text-accent font-bold">فهُو لَا يَقْبَلُ شَيْئًا مِن عَلَاَّمَاتِ الْاِسْمِ ، ولَا يَقْبَلُ شَيْئًا مِن عَلَاَّمَاتِ الْفِعْلِ .</span>
Right-Side (Logical Right / Visual Left):
  (Component: TEMPLATE_C_LIST.html)
  Items:
  - لَا يَقْبَلُ (<span class="highlight-blue">الً ، التَّنْوِينَ ، التَّاءَ الْمَرْبُوطَةَ</span>) فهُو لَيْس اِسْمًا.
  - لَا يَقْبَلُ (<span class="highlight-green">تَاءَ التَّأْنِيثِ ، تَاءَ الْفَاعِلِ ، لَم ، لَن ، قَد ، السِّينَ</span>) فهُو لَيْس فِعْلًا.

=== BLOCK 6: تَلْميحٌ ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Title: تَلْميحٌ - قَاعِدَةَ ثَابتةِ
Content: <span class="highlight-red font-bold">جَمِيعُ الْحُروفِ مَبْنِيَّةَ</span> دَائِمًا . ( أي لَا يَتَغَيَّرُ شَكْلُ آخِرِهَا بِاِخْتِلَاَفِ مَوْقِعِهَا فِي الْجُمْلَةِ ).

=== BLOCK 7: أَنْوَاعُ الْحُروفِ فِي اللُّغَةَ الْعَرَبِيَّةَ ===
(Component: TEMPLATE_C_TABLE.html)
Title: ٣. أَنْوَاعُ الْحُروفِ فِي اللُّغَةَ الْعَرَبِيَّةَ
Content: لِلْحُروفُ فِي لُغَتِنَا الْعَرَبِيَّةِ وَظَائِفَ وَأَنْوَاعَ كَثِيرَةَ ، نَذْكُرُ مِن أَهَمَّهَا:
Table Data:
| النَّوْعُ | الْحُروفُ |
| --- | --- |
| حُروفُ الْجَرِّ | (مِنْ ، عَن ، إِلَى ، عَلَى ، فِي ، الْكَافَّ ، اللَّاَمَ ، الْبَاءَ) |
| حُروفُ الْعَطْفِ | (الواو ، الْفَاءَ ، ثُمَّ ، أَو ، أَم) |
| حُروفُ النِّدَاءِ | (يَا ، أَيَا ، هَيَا ، الْهَمْزَةَ ، أَيَّ) |
| حُروفُ الْجَوَابِ | (نَعَمٌ ، بَلَى ، أَجَلٌ ، لَا ، كَلًّا) |
| حَرْفَا الْاِسْتِفْهَامِ | (هَلٌّ ، وَالْهَمْزَةَ "أَْ") |
| حُروفُ النُّصْبِ (لِلْفِعْلَ الْمُضَارِعَ) | (أَْنْ ، لَنْ ، كَيْ ، حَتَّى ، لَامَ التَّعْلِيلُ) |
| حُروفُ الجزم (لِلْفِعْلَ الْمُضَارِعَ) | (لَمْ ، لَمَّا ، لَامَ الْأَمْرُ ، لَا النَّاهِيَةِ) |
| الْحُروفُ النَّاسِخَةُ (إِنّْ وَأُخُوَّاتِهَا) | (إِنّْ ، أنّْ ، كأنّْ ، لِكَنَّ ، لَيْت ، لَعَلّ) |

=== BLOCK 8: مُلَاحِظَةً ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: مُلَاحِظَةً
Content: فِي الدُّرُوسِ الْقَادِمَةِ سَيَتِمُّ تَفْصِيلٌ كُلّ نَوْعٍ مِن هَذِه الْحُروفِ وَإِعْرَابِهَا فِي جُمْلَةِ.

=== BLOCK 9: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Title: تَدْرِيبَاتٍ وَتَطْبِيقَاتٍ عَمَلِيَّةٍ (مُسْتَخْرَجَةً مِن الدَّرْسِ)
Number: ١
Question: السُّؤَالَ الْأَوَّلَ: اِخْتَرْ الْإِجَابَةَ الصَّحِيحَةَ مِمَّا بَيْن الْقَوْسَيْنِ:<br>١- الْحَرْفُ هُو كَلِمَةِ (تَدُلُّ عَلَى مُعَنًّى فِي نَفْسهَا / تَدُلُّ عَلَى مُعَنًّى فِي غَيْرِهَا / لَيْس لَهَا أَيِّ مُعَنَّى مُطْلَقًا).<br>٢- جَمِيعُ الْحُروفِ فِي اللُّغَةَ الْعَرَبِيَّةَ (مُعَرِّبَةَ / مَبْنِيَّةَ / بَعْضَهَا مُعَرِّبَ وبَعْضَهَا مَبْنِيَّ).<br>٣- عُلَّامَةُ الْحَرْفِ أَنّهُ (يَقْبَلُ التَّنْوِينُ / يَقْبَلُ تَاءُ الْفَاعِلِ / لَا يَقْبَلُ عَلَاَّمَاتُ الْاِسْمِ ولَا الْفِعْلِ).

=== BLOCK 10: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Title:
Number: ٢
Question: السُّؤَالَ الثَّانِي: اِسْتَخْرَجَ الْحُروفُ مِن الْجُمْلَةِ التَّالِيَةِ وَصِنْفِ نَوْعِهَا بِنَاءً عَلَى مَا دَرَسَتْ: "ثُمَّ أَتِمُّوا الْعَمَلَ إِِْلََى اللَّيْلِ" <br> - الْحَرْفَ الْأَوَّلَ : ..................... (نَوَّعَهُ: .................)<br> - الْحَرْفَ الثَّانِي : ..................... (نَوَّعَهُ: .................)

=== BLOCK 11: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Title:
Number: ٣
Question: السُّؤَالَ الثَّالِثَ: اِقْرَأْ الْجُمْلَةَ التَّالِيَةَ وَصِنْفَ كَلِمَاتِهَا إِلَى ( اِسْمٌ ، فعَلّ ، حَرْفَ ) لِتَرَاجُعٍ مَا دَرْسَتِهِ فِي الدُّرُوسِ الثَّلَاثَةَ الْمَاضِيَةَ: (لَنْ يَنْجَحَ الْكَسُولُ فِِي الِامْتِحَانِ)<br> - لَنْ : .....................<br> - يَنْجَحَ : .....................<br> - الْكَسُولُ : .....................<br> - فِِي : .....................<br> - الِامْتِحَانِ : .....................

--- END STREAM ---
