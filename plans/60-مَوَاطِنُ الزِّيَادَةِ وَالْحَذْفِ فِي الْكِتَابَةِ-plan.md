# **SESSION 60.0**

[TASK DEFINITION]
Objective: Implement مَوَاطِنُ الزِّيَادَةِ وَالْحَذْفِ فِي الْكِتَابَةِ.
File: `pages/60.0_nXX_مَوَاطِنُ الزِّيَادَةِ وَالْحَذْفِ فِي الْكِتَابَةِ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/60.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 60
[CHAPTER_TITLE]: مَوَاطِنُ الزِّيَادَةِ وَالْحَذْفِ فِي الْكِتَابَةِ
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم الإملاء
[AUTHOR_NAME]: أ. حنا خفيف
[AUTHOR_PHONE]:  

=== BLOCK 2: Definition Split Grid ===
(Component: TEMPLATE_C_SPLIT.html)
-- RIGHT SIDE --
(Component: TEMPLATE_C_BLOCK.html)
Title: مَفْهُومُ الزِّيَادَةِ
Content: <p class="text-accent mt-1mm"><strong>الزِّيَادَةُ:</strong> هِيَ كِتَابَةُ حَرْفٍ زَائِدٍ فِي الْكَلِمَةِ يُرَى بِالْعَيْنِ وَلَا يُنْطَقُ بِاللِّسَانِ (يُكْتَبُ وَلَا يُلْفَظُ)، لِكَيْ نُفَرِّقَ بَيْنَ كَلِمَةٍ وَأُخْرَى أَوْ لِقَاعِدَةٍ إِمْلَائِيَّةٍ.</p>
-- LEFT SIDE --
(Component: TEMPLATE_C_BLOCK.html)
Title: مَفْهُومُ الْحَذْفِ
Content: <p class="text-accent mt-1mm"><strong>الْحَذْفُ:</strong> هُوَ إِسْقَاطُ حَرْفٍ مِنَ الْكَلِمَةِ فَلَا نَكْتُبُهُ، مَعَ أَنَّنَا نَنْطِقُهُ بِلِسَانِنَا (يُلْفَظُ وَلَا يُكْتَبُ)، أَوْ نَحْذِفُهُ نُطْقاً وَكِتَابَةً فِي بَعْضِ الْحَالَاتِ.</p>

=== BLOCK 3: أَوَّلًا: مَوَاطِنُ الزِّيَادَةِ (١. زِيَادَةُ الْأَلِفِ) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَوَّلًا: مَوَاطِنُ الزِّيَادَةِ (١. زِيَادَةُ الْأَلِفِ)
Content:
(Component: TEMPLATE_C_LIST.html)
- <strong>أَلِفُ التَّفْرِيقِ:</strong> تُزَادُ بَعْدَ (وَاوِ الْجَمَاعَةِ) فِي الْأَفْعَالِ لِلدَّلَالَةِ عَلَى الْجَمْعِ، وَلِلتَّفْرِيقِ بَيْنَهَا وَبَيْنَ الْوَاوِ الْأَصْلِيَّةِ لِلْفِعْلِ. مِثْل: <span class="highlight-red">سَافَرُوا</span>، <span class="highlight-red">لَمْ يَكْتُبُوا</span>، <span class="highlight-red">ادْرُسُوا</span>. (لَاحِظْ كَلِمَةَ "<span class="highlight-blue">يَرْجُو</span>" لَا نَضَعُ أَلِفاً لِأَنَّ الْوَاوَ أَصْلِيَّةٌ، وَ"<span class="highlight-blue">مُهَنْدِسُو الْمَشْرُوعِ</span>" لَا نَضَعُ أَلِفاً لِأَنَّهُ اسْمٌ وَلَيْسَ فِعْلًا!).
- <strong>أَلِفُ تَنْوِينِ النَّصْبِ:</strong> نَزِيدُ أَلِفاً بَعْدَ الْفَتْحَتَيْنِ فِي آخِرِ الِاسْمِ الْمُنَوَّنِ. مِثْل: <span class="highlight-red">رَأَيْتُ شَابًّا</span>، <span class="highlight-red">كِتَابًا</span>. (إِلَّا إِذَا كَانَتْ تَاءً مَرْبُوطَةً "<span class="highlight-blue">مَدْرَسَةً</span>"، أَوْ هَمْزَةً قَبْلَهَا أَلِفٌ "<span class="highlight-blue">سَمَاءً</span>").
- <strong>أَلِفُ الْإِطْلَاقِ:</strong> فِي نِهَايَةِ الشِّعْرِ لِتَمْدِيدِ الصَّوْتِ.

=== BLOCK 4: أَوَّلًا: مَوَاطِنُ الزِّيَادَةِ (٢. زِيَادَةُ الْوَاوِ) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَوَّلًا: مَوَاطِنُ الزِّيَادَةِ (٢. زِيَادَةُ الْوَاوِ)
Content:
(Component: TEMPLATE_C_LIST.html)
- <strong>فِي كَلِمَةِ (<span class="highlight-red">عَمْرو</span>):</strong> نَزِيدُ الْوَاوَ فِي حَالَتَي الرَّفْعِ وَالْجَرِّ لِكَيْ لَا نَخْلِطَ بَيْنَهَا وَبَيْنَ كَلِمَةِ (عُمَر). (نَقُولُ: جَاءَ <span class="highlight-red">عَمْرٌو</span>، وَمَرَرْتُ بِـ<span class="highlight-red">عَمْرٍو</span>). أَمَّا فِي النَّصْبِ فَنَحْذِفُ الْوَاوَ (<span class="highlight-blue">رَأَيْتُ عَمْرًا</span>).
- <strong>فِي الْكَلِمَاتِ:</strong> <span class="highlight-red">أُولَئِكَ</span>، <span class="highlight-red">أُولَاء</span>، <span class="highlight-red">أُولُو</span> (بِمَعْنَى أَصْحَاب)، <span class="highlight-red">أُولَات</span>، <span class="highlight-red">أُولِي</span>. (الْوَاوُ هُنَا تُكْتَبُ وَلَا تُلْفَظُ، نَنْطِقُهَا أُلَئِكَ).

=== BLOCK 5: ثَانِيًا: مَوَاطِنُ الْحَذْفِ (١. حَذْفُ الْأَلِفِ) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ثَانِيًا: مَوَاطِنُ الْحَذْفِ (١. حَذْفُ الْأَلِفِ)
Content:
(Component: TEMPLATE_C_LIST.html)
- <strong>فِي كَلِمَةِ (<span class="highlight-red">السَّمَوَات</span>):</strong> نَكْتُبُهَا السَّمَوَاتُ وَنَنْطِقُهَا (السَّمَاوَاتُ).
- <strong>مِنْ أَسْمَاءِ الْإِشَارَةِ (مُهِمَّةٌ!):</strong> <span class="highlight-red">هَذَا</span> (تُنْطَقُ هَاذَا)، <span class="highlight-red">هَذِهِ</span>، <span class="highlight-red">هَذَانِ</span>، <span class="highlight-red">هَؤُلَاءِ</span>، <span class="highlight-red">هَكَذَا</span>، <span class="highlight-red">ذَلِكَ</span>، <span class="highlight-red">أُولَئِكَ</span>.
- <strong>مِنْ بَعْضِ الْحُرُوفِ:</strong> <span class="highlight-red">لَكِنَّ</span>، <span class="highlight-red">لَكِنْ</span>. (تُنْطَقُ لَاكِن).

=== BLOCK 6: ثَانِيًا: مَوَاطِنُ الْحَذْفِ (٢. حَذْفُ النُّونِ لِلْإِدْغَامِ) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ثَانِيًا: مَوَاطِنُ الْحَذْفِ (٢. حَذْفُ النُّونِ لِلْإِدْغَامِ)
Content:
<p class="mb-2mm">إِذَا دَخَلَتْ (<span class="highlight-red">مِنْ</span>) أَوْ (<span class="highlight-red">عَنْ</span>) عَلَى (<span class="highlight-blue">مَنْ</span>) أَوْ (<span class="highlight-blue">مَا</span>)، نَحْذِفُ نُونَهَا وَنَضَعُ شَدَّةً.</p>
(Component: TEMPLATE_C_LIST.html)
- <span class="highlight-red">مِنْ</span> + <span class="highlight-blue">مَنْ</span> = <span class="highlight-green">مِمَّنْ</span>.
- <span class="highlight-red">عَنْ</span> + <span class="highlight-blue">مَنْ</span> = <span class="highlight-green">عَمَّنْ</span>.
- <span class="highlight-red">مِنْ</span> + <span class="highlight-blue">مَا</span> = <span class="highlight-green">مِمَّا</span>.
- <span class="highlight-red">عَنْ</span> + <span class="highlight-blue">مَا</span> = <span class="highlight-green">عَمَّا</span>.
- (<span class="highlight-red">إِنْ</span> / <span class="highlight-red">أَنْ</span>) + (<span class="highlight-blue">مَا</span> / <span class="highlight-blue">لَا</span>): <span class="highlight-red">إِنْ</span> + <span class="highlight-blue">لَا</span> = <span class="highlight-green">إِلَّا</span>. / <span class="highlight-red">أَنْ</span> + <span class="highlight-blue">لَا</span> = <span class="highlight-green">أَلَّا</span>. / <span class="highlight-red">إِنْ</span> + <span class="highlight-blue">مَا</span> = <span class="highlight-green">إِمَّا</span>. / <span class="highlight-red">أَنْ</span> + <span class="highlight-blue">مَا</span> = <span class="highlight-green">أَمَّا</span>.
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
<strong>⚠️ مُلَاحَظَةٌ:</strong> إِذَا كَانَتْ (مَا) لِلِاسْتِفْهَامِ، نَحْذِفُ أَلِفَهَا أَيْضاً: <span class="highlight-red">عَمَّ</span> تَبْحَثُ فِي الْكِتَابِ؟ <span class="highlight-red">لِمَ</span> تَفْعَلُ ذَلِكَ؟ <span class="highlight-red">بِمَ</span> تَفْتَخِرُ؟ <span class="highlight-red">مِمَّ</span> تَتَكَوَّنُ؟

=== BLOCK 7: The Core Matrix (Summary Table) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: جَدْوَلٌ تَلْخِيصِيٌّ لِمَوَاطِنِ الزِّيَادَةِ وَالْحَذْفِ
Content:
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: الْقَاعِدَةُ
[HEADER_2]: الْكَلِمَةُ الْمَكْتُوبَةُ
[HEADER_3]: مِثَالٌ تَطْبِيقِيٌّ
[ROW_1_COL_1]: زِيَادَةُ الْأَلِفِ
[ROW_1_COL_2]: <span class="highlight-red">سَافَرُوا</span>
[ROW_1_COL_3]: هُمْ سَافَرُوا بَاكِرًا
[ROW_2_COL_1]: زِيَادَةُ الْوَاوِ
[ROW_2_COL_2]: <span class="highlight-red">عَمْرٌو</span>
[ROW_2_COL_3]: جَاءَ عَمْرٌو
[ROW_3_COL_1]: حَذْفُ الْأَلِفِ
[ROW_3_COL_2]: <span class="highlight-red">هَذَا</span>
[ROW_3_COL_3]: هَذَا كِتَابٌ مُفِيدٌ
[ROW_4_COL_1]: حَذْفُ النُّونِ لِلْإِدْغَامِ
[ROW_4_COL_2]: <span class="highlight-red">مِمَّنْ</span>
[ROW_4_COL_3]: مِمَّنْ أَخَذْتَ الْعِلْمَ؟
[ROW_5_COL_1]: حَذْفُ أَلِفِ (مَا) الِاسْتِفْهَامِيَّةِ
[ROW_5_COL_2]: <span class="highlight-red">عَمَّ</span>
[ROW_5_COL_3]: عَمَّ تَبْحَثُ؟

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: صَوِّبِ الْخَطَأَ فِي: (هَؤُلَاءِ الرِّجَالُ يَرْجُوا نَجَاحَهُمْ).

=== BLOCK 9: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: صَوِّبِ الْخَطَأَ: (عَنْ مَاذَا تَبْحَثُ؟).

--- END STREAM ---
