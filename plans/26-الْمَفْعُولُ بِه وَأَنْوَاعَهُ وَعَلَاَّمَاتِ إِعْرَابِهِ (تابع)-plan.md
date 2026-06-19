# **SESSION 26.0**

[TASK DEFINITION]
Objective: Implement الْمَفْعُولُ بِه وَأَنْوَاعَهُ وَعَلَاَّمَاتِ إِعْرَابِهِ (تابع).
File: `pages/26.0_nXX_الْمَفْعُولُ بِه وَأَنْوَاعَهُ وَعَلَاَّمَاتِ إِعْرَابِهِ (تابع).html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/26.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 26
[CHAPTER_TITLE]: الْمَفْعُولُ بِه وَأَنْوَاعَهُ وَعَلَاَّمَاتِ إِعْرَابِهِ (تابع)
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition and Rule ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَعْرِيفُ الْمَفْعُولِ بِهِ وَحُكْمُهُ
Content: <p class="text-accent">الْمَفْعُولُ بِهِ هُوَ الاسْمُ الَّذِي يَقَعُ عَلَيْهِ فِعْلُ الْفَاعِلِ، وَيَكُونُ دَائِمًا <span class="highlight-red">مَنْصُوبًا</span>.</p>
مثال: غَرَسَ الْفَلَّاحُ <span class="highlight-blue">الشَّجَرَةَ</span>.

=== BLOCK 3: Core Matrix - Accusative Signs ===
(Component: TEMPLATE_C_TABLE.html)
Headers: النَّوْع | عَلَامَةُ النَّصْبِ | الْمِثَال
Row 1: الْمُفْرَدُ وَجَمْعُ التَّكْسِيرِ | الْفَتْحَةُ | يَحْمِلُ الطَّالِبُ <span class="highlight-red">الْكُتُبَ</span>.
Row 2: الْمُثَنَّى وَجَمْعُ الْمُذَكَّرِ السَّالِمِ | الْيَاءُ | حَفِظَ الطَّالِبُ <span class="highlight-red">الْقَصِيدَتَيْنِ</span>. / كَافَأْتُ <span class="highlight-red">الْمُتَفَوِّقِينَ</span>.
Row 3: الْأَسْمَاءُ الْخَمْسَةُ | الْأَلِفُ | أَطِعْ <span class="highlight-red">أَبَاكَ</span>.
Row 4: جَمْعُ الْمُؤَنَّثِ السَّالِمِ | الْكَسْرَةُ | عَلَّقَ سَعِيدٌ <span class="highlight-red">اللَّوْحَاتِ</span>.

=== BLOCK 4: Deep Dive - Types of Maf'ul Bihi ===
(Component: TEMPLATE_C_SPLIT.html)
LeftSide:
(Component: TEMPLATE_C_BLOCK.html)
Title: اسْمٌ ظَاهِرٌ
Content: <p class="text-accent">يَكُونُ الْمَفْعُولُ بِهِ اسْمًا ظَاهِرًا يُذْكَرُ بَعْدَ الْفِعْلِ وَالْفَاعِلِ.</p>
List (Component: TEMPLATE_C_LIST.html):
- قَرَأْتُ الْكِتَابَ.
RightSide:
(Component: TEMPLATE_C_BLOCK.html)
Title: ضَمِيرٌ مُتَّصِلٌ
Content: <p class="text-accent">وَيَكُونُ ضَمِيرًا يَتَّصِلُ بِالْفِعْلِ الْمُتَعَدِّي فِي مَحَلِّ نَصْبٍ.</p>
List (Component: TEMPLATE_C_LIST.html):
- يُسْعِدُ<span class="highlight-red">كَ</span> النَّجَاحُ.
- الدَّرْسُ شَرَحَ<span class="highlight-red">هُ</span> الْمُعَلِّمُ.
- عَالَجَنِ<span class="highlight-red">ي</span> الطَّبِيبُ.

=== BLOCK 5: Extra Info - Warning ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: تَنْبِيهٌ: <span class="highlight-blue">"نَا"</span> فِي جُمْلَةِ (كَتَبْنَا الدَّرْسَ) تُعْرَبُ فَاعِلًا لِأَنَّنَا مَنْ قُمْنَا بِالْكِتَابَةِ، وَلَيْسَ مَفْعُولًا بِهِ.

=== BLOCK 6: Parsing Models ===
(Component: TEMPLATE_C_IRAB_ROW.html)
Word 1: أَبَاكَ
Details: مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ <span class="highlight-red">الْأَلِفُ</span> لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ.
Word 2: اللَّوْحَاتِ
Details: مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ <span class="highlight-red">الْكَسْرَةُ</span> عِوَضًا عَنِ الْفَتْحَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ.

=== BLOCK 7: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: اسْتَخْرِجِ الْمَفْعُولَ بِهِ مِنَ الْجُمَلِ الْآتِيَةِ وَاذْكُرْ عَلَامَةَ نَصْبِهِ:
(Component: TEMPLATE_C_LIST.html)
- غَرَسَ الْفَلَّاحُ الشَّجَرَةَ.
- يَحْمِلُ الطَّالِبُ الْكُتُبَ.
- أَطِعْ أَبَاكَ.
- حَفِظَ الطَّالِبُ الْقَصِيدَتَيْنِ.
- كَافَأْتُ الْمُتَفَوِّقِينَ.
- عَلَّقَ سَعِيدٌ اللَّوْحَاتِ.

(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: أَعْرِبِ الضَّمَائِرَ الْمُتَّصِلَةَ بِالْأَفْعَالِ فِي الْجُمَلِ الْآتِيَةِ:
(Component: TEMPLATE_C_LIST.html)
- يُسْعِدُكَ النَّجَاحُ.
- الدَّرْسُ شَرَحَهُ الْمُعَلِّمُ.
- عَالَجَنِي الطَّبِيبُ.

(Component: TEMPLATE_C_EXAM.html)
Number: ٣
Question: صِلِ الْكَلِمَةَ بِالْإِعْرَابِ الصَّحِيحِ لَهَا (كَافَأْتُ الْمُتَفَوِّقِينَ):
(Component: TEMPLATE_C_LIST.html)
- الْمُتَفَوِّقِينَ

(Component: TEMPLATE_C_EXAM.html)
Number: ٤
Question: أَكْمِلِ الْفَرَاغَ بِالْمَفْعُولِ بِهِ الْمُنَاسِبِ لِلْعَلَامَةِ:
(Component: TEMPLATE_C_LIST.html)
- (كَسْرَةٌ) عَلَّقَ سَعِيدٌ ..........
- (أَلِفٌ) أَطِعْ ..........

(Component: TEMPLATE_C_EXAM.html)
Number: ٥
Question: ضَعْ إِشَارَةَ (صَحّ) أَوْ (خَطَأ) أَمَامَ الْعِبَارَاتِ الْآتِيَةِ، وَصَحِّحِ الْخَطَأَ:
(Component: TEMPLATE_C_LIST.html)
- الْمَفْعُولُ بِهِ مَرْفُوعٌ دَائِمًا. (   )
- يُنْصَبُ الْمَفْعُولُ بِهِ بِالْكَسْرَةِ إِذَا كَانَ جَمْعَ مُؤَنَّثٍ سَالِمًا. (   )
- "نَا" فِي جُمْلَةِ (كَتَبْنَا الدَّرْسَ) تُعْرَبُ مَفْعُولًا بِهِ. (   )

(Component: TEMPLATE_C_EXAM.html)
Number: ٦
Question: هَاتِ جُمْلَةً مُفِيدَةً مِنْ إِنْشَائِكَ تَحْتَوِي عَلَى مَفْعُولٍ بِهِ مَنْصُوبٍ بِالْفَتْحَةِ، وَأُخْرَى تَحْتَوِي عَلَى مَفْعُولٍ بِهِ (ضَمِيرٌ مُتَّصِلٌ).

--- END STREAM ---
