# **SESSION 10.0**

[TASK DEFINITION]
Objective: Implement الْفَاعِلُ وَأَنْوَاعُهُ وَعَلَاَّمَاتُ إِعْرَابِهِ.
File: `pages/10.0_nXX_الْفَاعِلُ وَأَنْوَاعُهُ وَعَلَاَّمَاتُ إِعْرَابِهِ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/10.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 10
[CHAPTER_TITLE]: الْفَاعِلُ وَأَنْوَاعُهُ وَعَلَاَّمَاتُ إِعْرَابِهِ
[CATEGORY_HEADER]:
[SECTION_HEADER]:
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition & Rule ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مُقَدَّمَةٌ وَتَعْرِيفُ الْفَاعِلِ
Content:
<p>تُحْدِثُنَا عَن الْجُمْلَةِ الْفِعْلِيَّةِ ، وَقُلْنَا إِنّهَا تَتُكُّونَ مِن رُكْنَيْنِ أَسَاسِيَّيْنِ <span class="font-bold">الْفِعْلُ وَالْفَاعِلُ</span> لكُلّ فعَلّ فَاعِلٍ لَا بَدَّ مِنهُ فَمَنٌّ هُو الْفَاعِلِ ؟ وكَيْف نُحَدِّدُ مَكَانَهُ بِدِقَّةٍ فِي الْجُمْلَةِ ؟</p>
<p class="text-accent mt-2mm font-bold">التَّعْرِيفَ : هُو مَن قَام بِالْفِعْلِ ، أَو اِتَّصَفَ بِه ( يَأْتِي بَعْد فعَلّ مَبْنِيٍّ لِلْمَعْلُومَ ).</p>

[Inject into Block 2]:
(Component: TEMPLATE_C_LIST.html)
List Items:
- <span class="font-bold">قَام بِالْفِعْلِ :</span> مِثْل ( تَلْعَبُ <span class="highlight-red">الطِّفْلَةُ</span> ). مَنِّ الَّتِي قَامَتْ بِاللُّعَبِ ؟ <span class="highlight-red">الطِّفْلَةَ</span> إِذَن هِي الْفَاعِلِ
- <span class="font-bold">اِتَّصَفَ بِالْفِعْلِ :</span> مِثْل ( اِنْكَسَرَ <span class="highlight-red">الْغُصْنُ</span> ) أَو ( مَاتَ <span class="highlight-red">الْعَصْفُورُ</span> ). <span class="highlight-red">الْغُصْنَ</span> لَم يَكْسِرُ نَفْسهُ ، بَل نَحْن أَلَحِقَنَا بِه صِفَةِ الْكَسْرِ وَ<span class="highlight-red">الْعَصْفُورُ</span> لَم يمُت نَفْسهُ ، بَل اِتَّصَفَ بِالْمَوْتِ إِذَن ( <span class="highlight-red">الْغُصْنَ</span> ، <span class="highlight-red">الْعَصْفُورَ</span> ) فَاعِلٌ

=== BLOCK 3: Benefit Tip ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Title: تَلْميحٌ - كَيْف تَكْتَشِفُ الْفَاعِلُ فِي الْجُمْلَةِ ؟
Text: قِفْ قَبْل الْفِعْلِ وَاِسْأَلْ : ( <span class="font-bold">مَنْ ؟</span> ). الْإِجَابَةَ هِي الْفَاعِلِ. مِثَالَ : شَرِبَ الدَّوَاءَ <span class="highlight-red">الْمَرِيضُ</span> . ( مَنُّ شَرِبَ ؟ <span class="highlight-red">الْمَرِيضَ</span> ). إِذَن ( <span class="highlight-red">الْمَرِيضَ</span> ) هُو الْفَاعِلِ ، بُغْضَ النَّظَرِ عَن تَأَخُّرِهِ فِي الْجُمْلَةِ

=== BLOCK 4: The Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Header text inside block: <p class="text-accent font-bold mb-2mm">قَاعِدَةَ ذَهَبِيَّةَ : الْفَاعِلُ دَائِمًا ( مَرْفُوعَ ). وَتَخْتَلِفُ عُلَّامَتُهُ حَسْب نَوْعِ الْاِسْمِ</p>
Table Columns: 3 columns -> الْعَلَامَةُ, نَوْعُ الْاِسْمِ, الْمِثَالُ
Rows:
- الضَّمَّةُ ( أَصِلِيَّةَ ), لِلْمُفْرَدَ, حَفِظَ <span class="highlight-red">الطَّالِبُ</span> الْقَصِيدَةَ
- الضَّمَّةُ ( أَصِلِيَّةَ ), لِجَمَعَ التَّكْسيرُ, حَفِظَ <span class="highlight-red">الطُّلَاَّبُ</span> الْقَصِيدَةَ
- الضَّمَّةُ ( أَصِلِيَّةَ ), لِجَمَعَ الْمُؤَنَّثُ السَّالِمُ, تَحْفَظُ <span class="highlight-red">الطَّالِبَاتُ</span> الْقَصِيدَةَ
- الْألْفُ ( فَرْعِيَّةَ ), لِلْمُثَنَّى, عَادَ <span class="highlight-red">الصَّدِيقَانِ</span> مِن الرِّحْلَةِ
- الواو ( فَرْعِيَّةَ ), لِجَمَعَ الْمُذَكَّرُ السَّالِمُ, نامَ <span class="highlight-red">اللَّاعِبُونَ</span> مُبَكِّرًا
- الواو ( فَرْعِيَّةَ ), لِلْأَسْمَاءَ الْخُمُسَةَ, قَابَلَ <span class="highlight-red">أَبُوكَ</span> الْمُعَلِّمَيْنِ

=== BLOCK 5: Deep Dive ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَنْوَاعُ الْفَاعِلِ
Content: <p class="mb-2mm">لَا يَقْتَصِرُ الْفَاعِلُ عَلَى كَوْنِهِ اِسْمًا ظَاهِرًا فَقَط ، بَل لَه ثَلَاثَةِ أَشْكَالٍ</p>

[Inject into Block 5]:
(Component: TEMPLATE_C_LIST.html)
List Items:
- <span class="font-bold text-accent">اِسْمُ ظَاهِرُ :</span> كَلِمَةُ وَاضِحَةُ مَكْتُوبَةُ . ( صَاحَ <span class="highlight-red">الدِّيكُ</span> ).
- <span class="font-bold text-accent">ضَمِيرُ بَارِزُ مُتَّصِلُ :</span> حَرْفُ ( ضَمِيرَ ) يَتَّصِلُ بِآخِرِ الْفِعْلِ وَيُعْرِبُ فَاعِلًا. مِثْل تَاءِ الْفَاعِلِ : ( فَهِمْ<span class="highlight-red">تُ</span> ، فَهِمْ<span class="highlight-red">تَ</span> ، فَهِمْ<span class="highlight-red">تِ</span> ). التَّاءَ ضَمِيرُ مُتَّصِلُ مَبْنِيُّ فِي مَحَلِّ رَفْعِ فَاعِلِ.
- <span class="font-bold text-accent">ضَمِيرُ مُسْتَتِرُ ( مَخْفِيَّ ) :</span> الضَّمِيرَ غَيْرَ مَكْتُوبٍ ، لَكِنّ الْعَقْلِ يُدْرِكُهُ ، ولَا يَجُوزُ خِلْوُ الْفِعْلِ مِن الْفَاعِلِ. إِذَا قُلْنَا لِلْمُخَاطِبِ : ( اِقْرَأْ الْقِصَّةَ ). الْفَاعِلَ هُنَا ضَمِيرُ مُسْتَتِرُ تَقْديرِهِ ( <span class="highlight-red">أَنْت</span> ). وَإِذَا قُلْنَا : ( الْمَرِيضُ شُرْبَ الدَّوَاءِ ). " الْمَرِيضَ " هُنَا مُبْتَدَأٍ أَيْن فَاعِلُ الْفِعْلِ ( شُرْبَ ) ؟ الْفَاعِلَ ضَمِيرُ مُسْتَتِرُ تَقْديرِهِ ( <span class="highlight-red">هُو</span> ) يَعُودُ عَلَى الْمَرِيضِ.

=== BLOCK 6: Benefit Warning ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: مُلَاحِظَةً هَامَّةً
Text: الْفِعْلُ فِي أَوَّل الْجَمَلَةِ يُكَوِّنُ دَائِمًا بِصِيغَةِ الْإِفْرَادِ ، فلَا نُقُولِ " حَفِظُوا الطُّلَاَّبُ " بَل " حَفِظَ الطُّلَاَّبُ ".

=== BLOCK 7: Evaluation (Exam) ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: اِسْتَخْرَجَ الْفَاعِلُ مِن الْجَمَلِ الْآتِيَةِ ، وَاُذْكُرْ عُلَّامَةَ إِعْرَابِهِ : ( مَاتَ الرَّجُلُ فِي الْحَادِثِ ، نامَ اللَّاعِبُونَ مُبَكِّرًا ، شَرِبَ الدَّوَاءَ الْمَرِيضُ ، قَابِلٌ أَبُوكَ الْمُعَلِّمَيْنِ )

=== BLOCK 8: Evaluation (Exam) ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: حَدَّدَ نَوْعُ الْفَاعِلِ ( اِسْمَ ظَاهِرَ ، أَم ضَمِيرُ مُتَّصِلُ ، أَم ضَمِيرُ مُسْتَتِرُ ) فِي الْآتِي : ( صَاحَ الدِّيكُ فَجَرَّا ، فَهِمْتُ الدَّرْسَ جَيِّدًا ، أَنْجِزْ الْعَمَلَ فِي وَقْتهُ )

--- END STREAM ---