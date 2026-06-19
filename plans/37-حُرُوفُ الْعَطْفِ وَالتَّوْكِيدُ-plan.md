# **SESSION 37.0**

[TASK DEFINITION]
Objective: Implement حُرُوفُ الْعَطْفِ وَالتَّوْكِيدُ.
File: `pages/37.0_nXX_حُرُوفُ الْعَطْفِ وَالتَّوْكِيدُ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/37.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 37
[CHAPTER_TITLE]: حُرُوفُ الْعَطْفِ وَالتَّوْكِيدُ
[CATEGORY_HEADER]: المستوى المتوسط
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition & Rule ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٢- الِاسْمُ الْمَعْطُوفُ
Content:
<p class="text-accent">الِاسْمُ الْمَعْطُوفُ تَابِعٌ يَتَوَسَّطُ بَيْنَهُ وَبَيْنَ مَتْبُوعِهِ أَحَدُ حُرُوفِ الْعَطْفِ، وَيَأْخُذُ نَفْسَ حَرَكَةِ مَا قَبْلَهُ. أَهَمُّ حُرُوفِهِ:</p>

=== BLOCK 3: The Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Columns: الْحَرْفُ | مَعْنَاهُ | مِثَالٌ
Rows:
- <span class="highlight-blue font-bold">الْوَاوُ</span> | تُفِيدُ الْجَمْعَ بَيْنَ الْمُتَعَاطِفَيْنِ مُطْلَقاً. | نَجَحَ <span class="highlight-green">سَعِيدٌ</span> <span class="highlight-blue">وَ</span><span class="highlight-red">طَارِقٌ</span> (طَارِقٌ مَرْفُوعٌ مِثْلَ سَعِيدٍ).
- <span class="highlight-blue font-bold">الْفَاءُ</span> | تُفِيدُ التَّرْتِيبَ وَالتَّعْقِيبَ (السُّرْعَةَ دُونَ تَأْخِيرٍ). | دَخَلَ <span class="highlight-blue">فَ</span><span class="highlight-red">سَلَّمَ</span> أَيْ دَخَلَ وَفَوْرًا سَلَّمَ. (قَامَ طَارِقٌ <span class="highlight-blue">فَ</span><span class="highlight-red">سَعِيدٌ</span>).
- <span class="highlight-blue font-bold">ثُمَّ</span> | تُفِيدُ التَّرْتِيبَ مَعَ التَّرَاخِي (التَّأْخِيرِ) فِي الزَّمَنِ. | زَرَعَ <span class="highlight-blue">ثُمَّ</span> <span class="highlight-red">حَصَدَ</span>. (الزِّرَاعَةُ تَتَطَلَّبُ أَشْهُراً لِلْحَصَادِ).
- <span class="highlight-blue font-bold">أَوْ</span> | تُفِيدُ التَّخْيِيرَ (تَخْتَارُ وَاحِداً) أَوِ التَّقْسِيمَ. | اشْرَبْ مَاءً <span class="highlight-blue">أَوْ</span> <span class="highlight-red">عَصِيرًا</span>.
- <span class="highlight-blue font-bold">أَمْ</span> | (الْمُعَادَلَةُ) لِطَلَبِ التَّعْيِينِ وَتَأْتِي بَعْدَ سُؤَالٍ. | أَطَلَبْتَ مَاءً <span class="highlight-blue">أَمْ</span> <span class="highlight-red">عَصِيرًا</span>؟

=== BLOCK 4: Deep Dive - التوكيد ===
(Component: TEMPLATE_C_BLOCK.html)
Title: 💠 ثَالِثاً: التَّوْكِيدُ (اللَّفْظِيُّ وَالْمَعْنَوِيُّ)
Content:
<p class="text-accent">يَنْقَسِمُ التَّوْكِيدُ الَّذِي نَسْتَخْدِمُهُ لِتَثْبِيتِ الْكَلَامِ إِلَى قِسْمَيْنِ:</p>

=== BLOCK 5: Deep Dive - Split Grid ===
(Component: TEMPLATE_C_SPLIT.html)
RightSide:
(Component: TEMPLATE_C_BLOCK.html)
Title: ١- التَّوْكِيدُ اللَّفْظِيُّ
Content:
يَكُونُ بِإِعَادَةِ اللَّفْظِ نَفْسِهِ (تَكْرَارِهِ مَرَّتَيْنِ):
(Component: TEMPLATE_C_LIST.html)
List Items:
- <span class="font-bold">تَكْرَارُ الْحَرْفِ:</span> نَحْوُ: (<span class="highlight-red">لَا لَا</span> أُخْذِلُ وَالِدِي).
- <span class="font-bold">تَكْرَارُ الِاسْمِ:</span> نَحْوُ: (<span class="highlight-green">طَارِقٌ</span> <span class="highlight-red">طَارِقٌ</span> مُجْتَهِدٌ).
- <span class="font-bold">تَكْرَارُ الْجُمْلَةِ:</span> نَحْوُ: (<span class="highlight-green">أَنْتَ الْأَمَلُ</span> <span class="highlight-red">أَنْتَ الْأَمَلُ</span>). الْجُمْلَةُ الثَّانِيَةُ تُعْرَبُ: تَوْكِيدٌ لَفْظِيٌّ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ.

LeftSide:
(Component: TEMPLATE_C_BLOCK.html)
Title: ٢- التَّوْكِيدُ الْمَعْنَوِيُّ
Content:
تُذْكَرُ بَعْدَ الْمُؤَكَّدِ إِحْدَى الْكَلِمَاتِ الْمُحَدَّدَةِ:
(Component: TEMPLATE_C_CHIPS.html)
Chips: نَفْس | عَيْن | كِلَا | كِلْتَا | جَمِيع | كُلّ

=== BLOCK 6: Extra Info - Warning ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: شَرْطُ التَّوْكِيدِ الْمَعْنَوِيِّ
Content:
بِشَرْطِ أَنْ تَتَّصِلَ بِضَمِيرٍ يَعُودُ عَلَى الْمُؤَكَّدِ، وَإِذَا حُذِفَتْ لَا يَتَأَثَّرُ الْمَعْنَى.

=== BLOCK 7: Evidence - Parsing (I'rab) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: 💡 أَمْثِلَةٌ تَطْبِيقِيَّةٌ
Content:
(Component: TEMPLATE_C_IRAB_ROW.html)
Row 1:
- Word: عَيْنُهُ | Details: تَوْكِيدٌ مَرْفُوعٌ بِالضَّمَّةِ لِأَنَّ الرَّجُلَ مَرْفُوعٌ. فِي جُمْلَةِ: (جَاءَ الرَّجُلُ <span class="highlight-red">عَيْنُهُ</span>)
- Word: نَفْسَهَا | Details: تَوْكِيدٌ مَنْصُوبٌ بِالْفَتْحَةِ. فِي جُمْلَةِ: (رَأَيْتُ الْفَتَاةَ <span class="highlight-red">نَفْسَهَا</span>)
(Component: TEMPLATE_C_IRAB_ROW.html)
Row 2:
- Word: كِلَاهُمَا | Details: تَوْكِيدٌ مَرْفُوعٌ بِالْأَلِفِ (يُعَامَلُ مُعَامَلَةَ الْمُثَنَّى). فِي جُمْلَةِ: (جَاءَ الطَّالِبَانِ <span class="highlight-red">كِلَاهُمَا</span>)
- Word: كُلَّهَا | Details: تَوْكِيدٌ مَنْصُوبٌ بِالْفَتْحَةِ. فِي جُمْلَةِ: (قَرَأْتُ الْأَمْثِلَةَ <span class="highlight-red">كُلَّهَا</span>)

=== BLOCK 8: Evaluation (Exam) ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: عَيِّنْ حَرْفَ الْعَطْفِ وَالْمَعْطُوفَ فِي الْجُمْلَةِ التَّالِيَةِ: أَكَلْتُ تُفَّاحَةً ثُمَّ بُرْتُقَالَةً.
Number: ٢
Question: حَدِّدْ نَوْعَ التَّوْكِيدِ وَأَعْرِبْهُ: النَّجَاحُ النَّجَاحُ هَدَفِي.

--- END STREAM ---
