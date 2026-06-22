# **SESSION 66.0**

[TASK DEFINITION]
Objective: Implement تَتِمَّةُ الصُّورَةِ الْبَيَانِيَّةِ وَالْكِنَايَةِ.
File: `pages/66.0_nXX_تَتِمَّةُ الصُّورَةِ الْبَيَانِيَّةِ وَالْكِنَايَةِ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/66.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 66
[CHAPTER_TITLE]: تَتِمَّةُ الصُّورَةِ الْبَيَانِيَّةِ وَالْكِنَايَةِ
[CATEGORY_HEADER]: المستوى المتقدم
[SECTION_HEADER]: علم البلاغة
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: تَعْرِيفُ الْكِنَايَةِ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ثَالِثًا - الكِنَايَةُ (التَّلْمِيحُ ذَكِيٌّ)
Content:
<p class="text-accent">هِيَ أَنْ تَتَكَلَّمَ بِكَلَامٍ عَادِيٍّ لَهُ مَعْنًى حَقِيقِيٌّ، وَلَكِنَّكَ لَا تَقْصِدُهُ بَلْ تَقْصِدُ مَعْنًى آخَرَ مُخْتَبِئاً خَلْفَهُ (يُلَازِمُهُ). (هِيَ التَّعْبِيرُ عَنِ الْمَعْنَى تَلْمِيحاً لَا تَصْرِيحاً).</p>

=== BLOCK 3: مُلَخَّصُ أَنْوَاعِ الْكِنَايَةِ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَنْوَاعُ الكِنَايَةِ الثَّلَاثَةِ
Content:
(Component: TEMPLATE_C_TABLE.html)
Headers: النَّوْعُ | التَّعْرِيفُ
Row 1: كِنَايَةٌ عَنْ صِفَةٍ | أَنْ تَقْصِدَ صِفَةً مَعْنَوِيَّةً (كَالْكَرَمِ، الْبُخْلِ، الشَّجَاعَةِ، الطُّولِ).
Row 2: كِنَايَةٌ عَنْ مَوْصُوفٍ | أَنْ تَقْصِدَ شَيْئاً أَوْ شَخْصاً بِعَيْنِهِ (لَقَبَهُ أَوْ مِهْنَتَهُ).
Row 3: كِنَايَةٌ عَنْ نِسْبَةٍ | أَنْ تَنْسُبَ صِفَةً إِلَى شَيْءٍ مُتَّصِلٍ بِالشَّخْصِ بَدَلَ أَنْ تَنْسُبَهَا لَهُ مُبَاشَرَةً.

=== BLOCK 4: النَّوْعُ الأَوَّلُ: كِنَايَةٌ عَنْ صِفَةٍ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ١. كِنَايَةٌ عَنْ صِفَةٍ
Content:
<p>أَنْ تَقْصِدَ صِفَةً مَعْنَوِيَّةً (كَالْكَرَمِ، الْبُخْلِ، الشَّجَاعَةِ، الطُّولِ).</p>
(Component: TEMPLATE_C_LIST.html inside Block 4 body)
List Items:
- مِثَالٌ: "<span class="highlight-red">فُلَانٌ بَابُهُ مَفْتُوحٌ دَائِماً</span>". (الْمَعْنَى الْحَقِيقِيُّ: الْبَابُ مَفْتُوحٌ. الْمَعْنَى الْخَفِيُّ الْمَقْصُودُ: كِنَايَةٌ عَنْ صِفَةِ الْكَرَمِ وَاسْتِقْبَالِ الضُّيُوفِ).
- مِثَالٌ: "<span class="highlight-red">فُلَانٌ يَدُهُ مَغْلُولَةٌ</span>". (كِنَايَةٌ عَنْ صِفَةِ الْبُخْلِ).
- مِثَالٌ: "<span class="highlight-red">طَوِيلُ النِّجَادِ رَفِيعُ الْعِمَادِ</span>". (كِنَايَةٌ عَنْ الطُّولِ وَالرِّفْعَةِ).

=== BLOCK 5: النَّوْعُ الثَّانِي: كِنَايَةٌ عَنْ مَوْصُوفٍ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٢. كِنَايَةٌ عَنْ مَوْصُوفٍ
Content:
<p>أَنْ تَقْصِدَ شَيْئاً أَوْ شَخْصاً بِعَيْنِهِ (لَقَبَهُ أَوْ مِهْنَتَهُ).</p>
(Component: TEMPLATE_C_LIST.html inside Block 5 body)
List Items:
- مِثَالٌ: "<span class="highlight-blue">يَا بِنْتَ الْيَمِّ</span>". (مَنْ هِيَ بِنْتُ الْبَحْرِ؟ كِنَايَةٌ عَنِ السَّفِينَةِ).
- مِثَالٌ: "<span class="highlight-blue">لُغَةُ الضَّادِ</span>". (كِنَايَةٌ عَنِ اللُّغَةِ الْعَرَبِيَّةِ).
- مِثَالٌ: "<span class="highlight-blue">سَفِينَةُ الصَّحْرَاءِ</span>". (كِنَايَةٌ عَنِ الْجَمَلِ).

=== BLOCK 6: النَّوْعُ الثَّالِثُ: كِنَايَةٌ عَنْ نِسْبَةٍ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٣. كِنَايَةٌ عَنْ نِسْبَةٍ
Content:
<p>أَنْ تَنْسُبَ صِفَةً (كَالْكَرَمِ) إِلَى شَيْءٍ مُتَّصِلٍ بِالشَّخْصِ بَدَلَ أَنْ تَنْسُبَهَا لَهُ مُبَاشَرَةً (مِثْلَ ثَوْبِهِ، بَيْتِهِ، ظِلِّهِ).</p>
(Component: TEMPLATE_C_LIST.html inside Block 6 body)
List Items:
- مِثَالٌ: "<span class="highlight-green">الْمَجْدُ يَمْشِي فِي ظِلِّهِ</span>". (لَمْ يَقُلْ هُوَ مَجِيدٌ، بَلْ نَسَبَ الْمَجْدَ لِظِلِّهِ، وَهِيَ كِنَايَةٌ عَنْ نِسْبَةِ الْمَجْدِ لَهُ).
- مِثَالٌ: "<span class="highlight-green">الْخَيْرُ فِي يَمِينِهِ</span>". (كِنَايَةٌ عَنْ نِسْبَةِ الْخَيْرِ إِلَيْهِ).

=== BLOCK 7: الْقِيمَةُ الْفَنِّيَّةُ لِلْكِنَايَةِ ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Content:
<strong> القِيمَةُ الفَنِّيَّةُ لِلْكِنَايَةِ:</strong> تَقْرِيبُ المَعْنَى مِنَ الذِّهْنِ، وَتَأْكِيدُهُ مَعَ الْإِتْيَانِ بِالدَّلِيلِ عَلَيْهِ فِي صُورَةٍ مَحْسُوسَةٍ جَمِيلَةٍ.

=== BLOCK 8: اِخْتَبِرْ نَفْسَكَ ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: اِسْتَخْرِجِ الْكِنَايَةَ مِنْ أَمْثِلَةِ الدَّرْسِ وَحَدِّدْ نَوْعَهَا (صِفَةٌ، مَوْصُوفٌ، نِسْبَةٌ).

--- END STREAM ---