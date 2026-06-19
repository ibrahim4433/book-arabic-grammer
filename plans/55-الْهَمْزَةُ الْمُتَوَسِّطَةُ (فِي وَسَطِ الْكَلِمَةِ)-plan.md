# **SESSION 55.0**

[TASK DEFINITION]
Objective: Implement الْهَمْزَةُ الْمُتَوَسِّطَةُ (فِي وَسَطِ الْكَلِمَةِ).
File: `pages/55.0_nXX_الْهَمْزَةُ الْمُتَوَسِّطَةُ (فِي وَسَطِ الْكَلِمَةِ).html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/55.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 55
[CHAPTER_TITLE]: الْهَمْزَةُ الْمُتَوَسِّطَةُ (فِي وَسَطِ الْكَلِمَةِ)
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم الإملاء
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَعْرِيفُ الْهَمْزَةِ الْمُتَوَسِّطَةِ
Content: <p class="text-accent mb-2mm">هِيَ الْهَمْزَةُ الَّتِي تَقَعُ فِي وَسَطِ الْكَلِمَةِ (مِثْل: <span class="highlight-red">سَأَلَ</span>، <span class="highlight-red">فَأْس</span>، <span class="highlight-red">بِئْر</span>، <span class="highlight-red">سُؤَال</span>).</p>
Child Component: TEMPLATE_C_BENEFIT_TIP.html
Tip Content: <p class="font-bold">الْقَاعِدَةُ الذَّهَبِيَّةُ كَمَا سُمِّيَتْ (قَاعِدَةُ أَقْوَى الْحَرَكَتَيْنِ):</p><p>لِكِتَابَتِهَا، نَنْظُرُ إِلَى حَرَكَةِ الْهَمْزَةِ نَفْسِهَا، وَحَرَكَةِ الْحَرْفِ الَّذِي قَبْلَهَا، وَنُجْرِي مُبَارَزَةً بَيْنَهُمَا، وَالْحَرَكَةُ الْأَقْوَى هِيَ الَّتِي تَفُوزُ وَتَخْتَارُ الْحَرْفَ الَّذِي تُكْتَبُ عَلَيْهِ.</p>

=== BLOCK 3: The Core Matrix ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَسَلْسُلُ قُوَّةِ الْحَرَكَاتِ
Child Component: TEMPLATE_C_TABLE.html
Table Headers: | الْحَرَكَة | قُوَّتُهَا | الْحَرْفُ الْمُنَاسِبُ |
Row 1: | <span class="highlight-red font-bold">١. الْكَسْرَةُ</span> | أَقْوَى شَيْءٍ تَقْهَرُ الْجَمِيعَ | النَّبْرَةُ (الْيَاءُ بِلَا نُقَطٍ) (<span class="highlight-blue">ـئـ</span> / <span class="highlight-blue">ئ</span>) |
Row 2: | <span class="highlight-red font-bold">٢. الضَّمَّةُ</span> | أَقْوَى مِنَ الْفَتْحَةِ وَالسُّكُونِ | الْوَاوُ (<span class="highlight-blue">ـؤـ</span> / <span class="highlight-blue">ؤ</span>) |
Row 3: | <span class="highlight-red font-bold">٣. الْفَتْحَةُ</span> | أَقْوَى مِنَ السُّكُونِ فَقَطْ | الْأَلِفُ (<span class="highlight-blue">ـأـ</span> / <span class="highlight-blue">أ</span>) |
Row 4: | <span class="highlight-red font-bold">٤. السُّكُونُ</span> | أَضْعَفُ شَيْءٍ دَائِماً خَاسِرٌ | (لَا شَيْءَ لَهُ، إِلَّا حَالَةَ التَّطَرُّفِ تُكْتَبُ عَلَى السَّطْرِ) |

=== BLOCK 4: Deep Dive - Applications ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَمْثِلَةٌ تَطْبِيقِيَّةٌ مُفَصَّلَةٌ عَلَى الْقَاعِدَةِ الْعَامَّةِ
Child Component: TEMPLATE_C_LIST.html
Item 1: <span class="highlight-red font-bold">١. بِئْر:</span> الْهَمْزَةُ سَاكِنَةٌ، وَمَا قَبْلَهَا مَكْسُورٌ (بِـ). الْكَسْرَةُ أَقْوَى مِنَ السُّكُونِ، لِذَلِكَ كُتِبَتْ عَلَى <span class="highlight-blue">نَبْرَةٍ</span>. (<span class="highlight-green">سُئِلَ</span>، <span class="highlight-green">تَئِنُّ</span>، <span class="highlight-green">مُطْمَئِنّ</span>).
Item 2: <span class="highlight-red font-bold">٢. سُؤَال:</span> الْهَمْزَةُ مَفْتُوحَةٌ، وَمَا قَبْلَهَا مَضْمُومٌ (سُـ). الضَّمَّةُ أَقْوَى مِنَ الْفَتْحَةِ، لِذَلِكَ كُتِبَتْ عَلَى <span class="highlight-blue">وَاوٍ</span>. (<span class="highlight-green">يُؤَدِّي</span>، <span class="highlight-green">رُؤْيَة</span>، <span class="highlight-green">مُؤْتَمَر</span>).
Item 3: <span class="highlight-red font-bold">٣. سَأَلَ:</span> الْهَمْزَةُ مَفْتُوحَةٌ، وَمَا قَبْلَهَا مَفْتُوحٌ (سَـ). تَعَادُلٌ، إِذَنْ تُكْتَبُ عَلَى <span class="highlight-blue">أَلِفٍ</span>. (<span class="highlight-green">فَأْس</span>، <span class="highlight-green">رَأْس</span>، <span class="highlight-green">مَسْأَلَة</span>).

=== BLOCK 5: Exceptions ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الْحَالَاتُ الشَّاذَّةُ (الِاسْتِثْنَاءَاتُ)
Content: <p class="text-accent mb-2mm">فِي بَعْضِ الْحَالَاتِ، نَكْسِرُ الْقَاعِدَةَ وَلَا نَنْظُرُ لِلْقُوَّةِ أَبَداً: تُكْتَبُ الْهَمْزَةُ الْمُتَوَسِّطَةُ عَلَى السَّطْرِ (ء) فِي حَالَتَيْنِ:</p>
Child Component: TEMPLATE_C_LIST.html
Item 1: <span class="font-bold">١. إِذَا كَانَتْ الْهَمْزَةُ مَفْتُوحَةً وَجَاءَتْ بَعْدَ أَلِفٍ مَدٍّ سَاكِنَةٍ.</span> مِثْلُ: <span class="highlight-red">عَبَاءَة</span> ، <span class="highlight-red">قِرَاءَة</span> ، <span class="highlight-red">بَرَاءَة</span> ، <span class="highlight-red">تَفَاءَلَ</span>.
Item 2: <span class="font-bold">٢. إِذَا كَانَتْ الْهَمْزَةُ مَفْتُوحَةً أَوْ مَضْمُومَةً وَجَاءَتْ بَعْدَ وَاوٍ مَدٍّ سَاكِنَةٍ.</span> مِثْلُ: <span class="highlight-red">مُرُوءَة</span> ، <span class="highlight-red">مَقْرُوءَة</span> ، <span class="highlight-red">السَّمَوْءَل</span> ، <span class="highlight-red">ضَوْءُهَا</span> (إِذَا نُصِبَتْ <span class="highlight-blue">ضَوْءَهَا</span>).

=== BLOCK 6: Benefit Warning ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: <p class="font-bold">⚠️ تَنْبِيهٌ:</p><p>أَمَّا إِذَا جَاءَتْ بَعْدَ (يَاءٍ) سَاكِنَةٍ، فَتُكْتَبُ دَائِماً عَلَى (<span class="highlight-red">نَبْرَةٍ</span>) شُذُوذًا! مِثْلُ: <span class="highlight-blue">بِيئَة</span>، <span class="highlight-blue">هَيْئَة</span>، <span class="highlight-blue">رَدِيئَة</span>.</p>

=== BLOCK 7: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: عَلِّلْ كِتَابَةَ الْهَمْزَةِ فِي الْكَلِمَاتِ الْآتِيَةِ بِنَاءً عَلَى قَاعِدَةِ أَقْوَى الْحَرَكَتَيْنِ: (بِئْر، سُؤَال، سَأَلَ).

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: بَيِّنْ سَبَبَ كِتَابَةِ الْهَمْزَةِ عَلَى السَّطْرِ أَوِ النَّبْرَةِ فِي الْحَالَاتِ الشَّاذَّةِ الْآتِيَةِ: (قِرَاءَة، مُرُوءَة، بِيئَة).

--- END STREAM ---
