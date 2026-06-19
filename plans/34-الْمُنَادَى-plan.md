# **SESSION 34.0**

[TASK DEFINITION]
Objective: Implement الْمُنَادَى.
File: `pages/34.0_nXX_الْمُنَادَى.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/34.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 34
[CHAPTER_TITLE]: الْمُنَادَى
[CATEGORY_HEADER]: المستوى المتوسط
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَعْرِيفُ الْمُنَادَى
Content: <p class="text-accent mb-0">النِّدَاءُ أُسْلُوبٌ لِطَلَبِ إِقْبَالِ الشَّخْصِ إِلَيْكَ. وَ<span class="font-bold">الْمُنَادَى</span> هُوَ اسْمٌ وَقَعَ بَعْدَ حَرْفٍ مِنْ أَحْرُفِ النِّدَاءِ.</p>

=== BLOCK 3: Particles of Calling (أدوات النداء) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَدَوَاتُ النِّدَاءِ
Content:
(Component: TEMPLATE_C_LIST.html)
- (<span class="highlight-blue">يَا</span>): لِنِدَاءِ كُلِّ مُنَادَى (الْقَرِيبِ وَالْبَعِيدِ)، وَهِيَ الْأَشْهَرُ.
- (<span class="highlight-blue">أ</span>، <span class="highlight-blue">أَيْ</span>): لِنِدَاءِ الْقَرِيبِ (<span class="highlight-blue">أَ</span><span class="highlight-red">سَعِيدُ</span> أَقْبِلْ).
- (<span class="highlight-blue">أَيَا</span>، <span class="highlight-blue">هَيَا</span>): لِنِدَاءِ الْبَعِيدِ (<span class="highlight-blue">أَيَا</span> <span class="highlight-red">سَامِعاً</span> كَلَامِي).
- (<span class="highlight-blue">وَا</span>): لِلنُّدْبَةِ وَالِاسْتِغَاثَةِ لِلتَّعَجُّبِ وَالتَّفَجُّعِ (<span class="highlight-blue">وَا</span>أَسَفَاه).

=== BLOCK 4: Important Rule ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: <span class="font-bold">قَاعِدَةٌ هَامَّةٌ:</span> الْمُنَادَى فِي الْأَصْلِ مِنَ الْمَنْصُوبَاتِ؛ لِأَنَّهُ كَالْمَفْعُولِ بِهِ لِأَدَاةِ النِّدَاءِ، فَأَدَاةُ النِّدَاءِ تَقُومُ مَقَامَ الْفِعْلِ (<span class="highlight-blue">أُنَادِي</span> <span class="highlight-red">سَعِيداً</span> = <span class="highlight-blue">يَا</span> <span class="highlight-red">سَعِيدُ</span>).

=== BLOCK 5: Core Matrix (Summary Table) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مُلَخَّصُ أَحْوَالِ الْمُنَادَى الْخَمْسَةِ (الْمُعْرَبِ وَالْمَبْنِيِّ)
Content:
يَنْقَسِمُ الْمُنَادَى إِلَى قِسْمَيْنِ: مُعْرَبٌ (مَنْصُوبٌ بِالْفَتْحَةِ مُبَاشَرَةً)، وَمَبْنِيٌّ (يُبْنَى عَلَى مَا يُرْفَعُ بِهِ فِي مَحَلِّ نَصْبٍ).
(Component: TEMPLATE_C_TABLE.html)
Headers: الْقِسْمُ | الْحَالَةُ | مِثَالٌ
Rows:
- الْمُعْرَبُ (يَكُونُ كَلِمَتَيْنِ عَادَةً أَوْ مُنَوَّناً) | ١. الْمُضَافُ | يَا طَالِبَ الْعِلْمِ . يَا حَارِسَ الْمَصْنَعِ
- الْمُعْرَبُ | ٢. الشَّبِيهُ بِالْمُضَافِ | يَا طَالِباً الْعِلْمَ . يَا رَغِيباً فِي النَّجَاحِ
- الْمُعْرَبُ | ٣. نَكِرَةٌ غَيْرُ مَقْصُودَةٍ | يَا رَجُلاً خُذْ بِيَدِي . يَا مُهْمِلاً احْذَرْ
- الْمَبْنِيُّ (يَكُونُ كَلِمَةً وَاحِدَةً بِدُونِ تَنْوِينٍ بَلْ بِضَمَّةٍ) | ١. مُفْرَدٌ عَلَمٌ | يَا سَعِيدُ . يَا دِمَشْقُ . يَا سَعِيدَانِ
- الْمَبْنِيُّ | ٢. نَكِرَةٌ مَقْصُودَةٌ | يَا رَجُلُ . يَا طَالِبُ اجْلِسْ

=== BLOCK 6: Deep Dive (Split View for Types) ===
(Component: TEMPLATE_C_SPLIT.html)
LeftSide:
(Component: TEMPLATE_C_BLOCK.html)
Title: أَوَّلاً: الْمُنَادَى الْمُعْرَبُ (الْمَنْصُوبُ مُبَاشَرَةً)
Content:
وَيَأْتِي فِي ٣ حَالَاتٍ (يَكُونُ كَلِمَتَيْنِ عَادَةً أَوْ مُنَوَّناً):
(Component: TEMPLATE_C_LIST.html)
- <span class="font-bold">١. الْمُضَافُ:</span> (كَلِمَتَانِ، الْأُولَى بِدُونِ تَنْوِينٍ وَالثَّانِيَةُ مُضَافٌ إِلَيْهِ). مِثَالٌ: يَا <span class="highlight-red">طَالِبَ</span> الْعِلْمِ . يَا <span class="highlight-red">حَارِسَ</span> الْمَصْنَعِ. (<span class="font-bold">طَالِبَ:</span> مُنَادَى مَنْصُوبٌ بِالْفَتْحَةِ).
- <span class="font-bold">٢. الشَّبِيهُ بِالْمُضَافِ:</span> (يَأْتِي مُنَوَّناً وَيَحْتَاجُ كَلِمَةً تُكَمِّلُ مَعْنَاهُ كَالْمَفْعُولِ بِهِ أَوِ الْجَارِّ وَالْمَجْرُورِ). مِثَالٌ: يَا <span class="highlight-red">طَالِباً</span> الْعِلْمَ . يَا <span class="highlight-red">رَغِيباً</span> فِي النَّجَاحِ. (<span class="font-bold">طَالِباً:</span> مُنَادَى مَنْصُوبٌ بِالْفَتْحَةِ).
- <span class="font-bold">٣. نَكِرَةٌ غَيْرُ مَقْصُودَةٍ:</span> (كَلِمَةٌ وَاحِدَةٌ مُنَوَّنَةٌ بِالنَّصْبِ وَلَا تَقْصِدُ شَخْصاً مُعَيَّناً أَمَامَكَ). مِثَالٌ لِلْأَعْمَى يَقُولُ: يَا <span class="highlight-red">رَجُلاً</span> خُذْ بِيَدِي (أَيْ رَجُلٍ). يَا <span class="highlight-red">مُهْمِلاً</span> احْذَرْ (أَيْ مُهْمِلٍ بِشَكْلٍ عَامٍّ).

RightSide:
(Component: TEMPLATE_C_BLOCK.html)
Title: ثَانِياً: الْمُنَادَى الْمَبْنِيُّ (فِي مَحَلِّ نَصْبٍ)
Content:
وَيَأْتِي فِي حَالَتَيْنِ (يَكُونُ كَلِمَةً وَاحِدَةً بِدُونِ تَنْوِينٍ بَلْ بِضَمَّةٍ):
(Component: TEMPLATE_C_LIST.html)
- <span class="font-bold">١. مُفْرَدٌ عَلَمٌ:</span> (اسْمُ شَخْصٍ أَوْ مَدِينَةٍ): مِثَالٌ: يَا <span class="highlight-red">سَعِيدُ</span> . يَا <span class="highlight-red">دِمَشْقُ</span> . (مُنَادَى مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ). يَا <span class="highlight-red">سَعِيدَانِ</span> (مَبْنِيٌّ عَلَى الْأَلِفِ).
- <span class="font-bold">٢. نَكِرَةٌ مَقْصُودَةٌ:</span> (قُصِدَ بِهِ مُعَيَّنٌ أَمَامَكَ، كَلِمَةٌ وَاحِدَةٌ بِضَمَّةٍ): مِثَالٌ: يَا <span class="highlight-red">رَجُلُ</span> (تَقُولُهَا لِشَخْصٍ يَقِفُ أَمَامَكَ تَقْصِدُهُ). يَا <span class="highlight-red">طَالِبُ</span> اجْلِسْ. (مُنَادَى مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ).

=== BLOCK 7: Analysis Example (نَمُوذَجٌ إِعْرَابِيٌّ) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: نَمُوذَجٌ إِعْرَابِيٌّ (إِضَافِيٌّ لِلتَّوْضِيحِ)
Content:
(Component: TEMPLATE_C_IRAB_ROW.html)
Box 1:
Word: يَا طَالِبَ
Details: <span class="font-bold">يَا:</span> حَرْفُ نِدَاءٍ. <span class="font-bold">طَالِبَ:</span> مُنَادَى مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ.
Box 2:
Word: يَا سَعِيدُ
Details: <span class="font-bold">يَا:</span> حَرْفُ نِدَاءٍ. <span class="font-bold">سَعِيدُ:</span> مُنَادَى مَفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: اسْتَخْرِجِ الْمُنَادَى وَبَيِّنْ نَوْعَهُ وَحُكْمَهُ الْإِعْرَابِيَّ فِي الجملة: (يَا صَانِعَ الْمَعْرُوفِ).
Number: ٢
Question: حَوِّلِ الْمُنَادَى الْمَبْنِيَّ إِلَى مُعْرَبٍ فِي الْجُمْلَةِ التَّالِيَةِ: (يَا رَجُلُ، سَاعِدْنِي).
Number: ٣
Question: أَعْرِبْ مَا تَحْتَهُ خَطٌّ: يَا غَافِلاً انْتَبِهْ.

--- END STREAM ---
