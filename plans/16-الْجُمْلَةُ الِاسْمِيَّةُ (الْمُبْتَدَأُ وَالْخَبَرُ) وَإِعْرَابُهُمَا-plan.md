# **SESSION 16.0**

[TASK DEFINITION]
Objective: Implement الْجُمْلَةُ الِاسْمِيَّةُ (الْمُبْتَدَأُ وَالْخَبَرُ) وَإِعْرَابُهُمَا.
File: `pages/16.0_nXX_الْجُمْلَةُ الِاسْمِيَّةُ (الْمُبْتَدَأُ وَالْخَبَرُ) وَإِعْرَابُهُمَا.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/16.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 16
[CHAPTER_TITLE]: الْجُمْلَةُ الِاسْمِيَّةُ (الْمُبْتَدَأُ وَالْخَبَرُ) وَإِعْرَابُهُمَا
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مُقَدِّمَةٌ وَتَحْدِيدُ الْمُبْتَدَأِ
Content:
<p class="text-accent">كَمَا تَعَلَّمْنَا سَابِقًا ، الْجُمْلَةُ الِاسْمِيَّةُ هِيَ الْجُمْلَةُ الَّتِي تَبْدَأُ بِـ (<span class="highlight-blue">اِسْمٍ</span>)، وَتَتَكَوَّنُ مِنْ رُكْنَيْنِ أَسَاسِيَّيْنِ مُتَلَازِمَيْنِ هُمَا: <span class="highlight-red">الْمُبْتَدَأُ</span> وَ <span class="highlight-red">الْخَبَرُ</span> . وَلِكَيْ تَسْتَقِيمَ الْجُمْلَةُ وَيُفْهَمَ الْمَعْنَى، يَجِبُ أَنْ نَعْرِفَ كَيْفَ نُحَدِّدُهُمَا وَنُعْرِبُهُمَا بِشَكْلٍ صَحِيحٍ.</p>
<p class="text-accent mt-2mm"><span class="font-bold highlight-red">تَحْدِيدُ الْمُبْتَدَأِ:</span> هُوَ الْاِسْمُ (وَغَالِباً يَكُونُ مَعْرِفَةً) الَّذِي تَبْدَأُ بِهِ الْجُمْلَةُ (وَهُوَ مَوْضِعُ الْحَدِيثِ الَّذِي سَنَتَكَلَّمُ عَنْهُ). وَتَحْدِيدُهُ سَهْلٌ جِدًّا لِأَنَّهُ يَكُونُ عَادَةً الْكَلِمَةُ الْأُولَى فِي الْجُمْلَةِ.</p>

=== BLOCK 3: Golden Rule ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Title: قَاعِدَةٌ ذَهَبِيَّةٌ (الْإِعْرَابُ وَالْعَلَامَاتُ)
Content:
<p>الْمُبْتَدَأُ وَالْخَبَرُ دَائِمًا (<span class="highlight-red">مَرْفُوعَانِ</span>). الْمُبْتَدَأُ لَا يَكُونُ مَنْصُوبًا وَلَا مَجْرُورًا أَبَدًا، كَذَلِكَ الْخَبَرُ. لَكِنْ تَخْتَلِفُ عَلَامَةُ الرَّفْعِ حَسَبَ نَوْعِ الْكَلِمَةِ الْمُسْتَخْدَمَةِ (مُفْرَد، مُثَنَّى، جَمْع).</p>

=== BLOCK 4: The Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Title: عَلَامَاتُ رَفْعِ الْمُبْتَدَأِ وَالْخَبَرِ
Columns: نَوْعُ الْكَلِمَةِ | عَلَامَةُ الرَّفْعِ | مِثَالٌ
Row 1: الْمُفْرَدُ | الضَّمَّةُ | السَّمَاءُ صَافِيَةٌ
Row 2: الْمُثَنَّى | الْأَلِفُ | الطَّالِبَانِ مُجْتَهِدَانِ
Row 3: جَمْعُ الْمُذَكَّرِ السَّالِمِ | الْوَاوُ | الْمُهَنْدِسُونَ بَارِعُونَ
Row 4: جَمْعُ الْمُؤَنَّثِ السَّالِمِ | الضَّمَّةُ | الْأُمَّهَاتُ رَحِيمَاتٌ

=== BLOCK 5: Deep Dive Examples ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَمْثِلَةٌ وَإِعْرَابٌ عَلَى عَلَامَاتِ الرَّفْعِ
Content:
<p>تَطْبِيقٌ لِلْقَاعِدَةِ الذَّهَبِيَّةِ عَلَى أَنْوَاعِ الْكَلِمَاتِ وَإِعْرَابِهَا بِالتَّفْصِيلِ:</p>
(Inject TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: <span class="font-bold highlight-blue">الْمُفْرَدُ</span> (يُشْرَعُ بِالضَّمَّةِ): السَّمَاءُ صَافِيَةٌ .
[LIST_ITEM_CONTENT]: <span class="font-bold highlight-blue">الْمُثَنَّى</span> (يُرْفَعُ بِالْأَلِفِ): الطَّالِبَانِ مُجْتَهِدَانِ .
[LIST_ITEM_CONTENT]: <span class="font-bold highlight-blue">جَمْعُ الْمُذَكَّرِ السَّالِمِ</span> (يُرْفَعُ بِالْوَاوِ): الْمُهَنْدِسُونَ بَارِعُونَ .
[LIST_ITEM_CONTENT]: <span class="font-bold highlight-blue">جَمْعُ الْمُؤَنَّثِ السَّالِمِ</span> (يُرْفَعُ بِالضَّمَّةِ): الْأُمَّهَاتُ رَحِيمَاتٌ .

=== BLOCK 6: Irab Parsing 1 (Mufrad) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
Box 1 (Right):
Word: السَّمَاءُ
Details: مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.
Box 2 (Left):
Word: صَافِيَةٌ
Details: خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.

=== BLOCK 7: Irab Parsing 2 (Muthanna) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
Box 1 (Right):
Word: الطَّالِبَانِ
Details: مُبْتَدَأٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنَّى.
Box 2 (Left):
Word: مُجْتَهِدَانِ
Details: خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنَّى.

=== BLOCK 8: Irab Parsing 3 (Jam Mudhakkar) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
Box 1 (Right):
Word: الْمُهَنْدِسُونَ
Details: مُبْتَدَأٌ مَرْفُوعٌ بِالْوَاوِ.
Box 2 (Left):
Word: بَارِعُونَ
Details: خَبَرٌ مَرْفُوعٌ بِالْوَاوِ.

=== BLOCK 9: Irab Parsing 4 (Jam Muannath) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
Box 1 (Right):
Word: الْأُمَّهَاتُ
Details: مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.
Box 2 (Left):
Word: رَحِيمَاتٌ
Details: خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.

=== BLOCK 10: Special Cases Warning ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: حَالَاتٌ خَاصَّةٌ لِلْخَبَرِ
Content:
<p>الْقَاعِدَةُ الْعَامَّةُ أَنَّ الْمُبْتَدَأَ يَكُونُ (<span class="highlight-blue">مَعْرِفَةً بِـ ال</span>) وَالْخَبَرَ يَكُونُ (<span class="highlight-red">نَكِرَةً بِدُونِ ال</span> لِكَيْ يُفِيدَ حُكْماً). لَكِنْ يَنْدُرُ أَنْ يَأْتِيَ الْخَبَرُ الْمُعَرَّفُ بِـ (ال)، وَيَحْدُثُ ذَلِكَ غَالِبًا فِي الْحَالَاتِ التَّالِيَةِ لِأَغْرَاضٍ بَلَاغِيَّةٍ:</p>

=== BLOCK 11: Special Cases List ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَفْصِيلُ الْحَالَاتِ الْخَاصَّةِ
Content:
(Inject TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: <span class="font-bold text-primary">بَعْدَ الضَّمِيرِ الْمُنْفَصِلِ</span> (الَّذِي يَقَعُ مُبْتَدَأً): (أَنَا ، هُوَ ، نَحْنُ ، أَنْتَ...). مِثَالٌ: (<span class="highlight-blue">هُوَ</span> <span class="highlight-red">الْعَالِمُ</span>).
[LIST_ITEM_CONTENT]: <span class="font-bold text-primary">لِغَرَضِ التَّوْكِيدِ وَالْحَصْرِ</span> (بَلَاغِيًّا): مِثَالٌ الْمَقُولَةُ الْمَشْهُورَةُ: (<span class="highlight-blue">الْعِلْمُ</span> <span class="highlight-red">النُّورُ</span>). الْعِلْمُ مُبْتَدَأٌ ، النُّورُ خَبَرٌ وَكِلَاهُمَا مُعَرَّفٌ بِـ (ال)، وَهَذَا لِلْمُبَالَغَةِ، كَأَنَّهُ لَا يُوجَدُ نُورٌ فِي الدُّنْيَا إِلَّا الْعِلْمُ.

=== BLOCK 12: Irab Parsing 5 (Special Case) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
Box 1 (Right):
Word: هُوَ
Details: ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعِ مُبْتَدَأٍ.
Box 2 (Left):
Word: الْعَالِمُ
Details: خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ (وَجَاءَ مَعْرِفَةً لِحَصْرِ الْعِلْمِ فِيهِ).

=== BLOCK 13: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: حَدِّدِ الْمُبْتَدَأَ وَالْخَبَرَ فِي الْجُمْلَةِ التَّالِيَةِ: الرَّجُلَانِ صَادِقَانِ.
Number: ٢
Question: أَعْرِبْ مَا تَحْتَهُ خَطٌّ: الْمُؤْمِنُونَ مُخْلِصُونَ.
Number: ٣
Question: هَلْ يُمْكِنُ أَنْ يَأْتِيَ الْخَبَرُ مَعْرِفَةً؟ مَتَى؟

--- END STREAM ---