# **SESSION 09.0**

[TASK DEFINITION]
Objective: Implement الْجُمْلَةُ الِاسْمِيَّة ( الْمُبْتَدَأِ وَالْخَبَرِ وَإِعْرَابَهُمَا.
File: `pages/09.0_nXX_الْجُمْلَةُ الِاسْمِيَّة ( الْمُبْتَدَأِ وَالْخَبَرِ وَإِعْرَابَهُمَا.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/09.1_...` if page have a lot of blank space add exam elements from the lesson.
3. text Content: 100% Arabic with full Harakat.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green`  for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   **Rule:** NO INLINE STYLES.
*   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
*   **Mapping:**
    *   inline style width: 20% -> `class="w-20pct"`
    *   inline style margin-top: 2mm -> `class="mt-2mm"`
    *   inline style text-align: center -> `class="text-center"`
    *   inline style font-weight: bold -> `class="font-bold"`
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
[LESSON_NUMBER]: 09
[CHAPTER_TITLE]: الْجُمْلَةُ الِاسْمِيَّة ( الْمُبْتَدَأِ وَالْخَبَرِ وَإِعْرَابَهُمَا
[CATEGORY_HEADER]:
[SECTION_HEADER]:
[AUTHOR_NAME]: أ. حنا خفيف
[AUTHOR_PHONE]:  

=== BLOCK 2: Introduction & Definition ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مُقَدَّمَةً
Content: <p class="text-accent">كَمَّا تَعَلُّمِنَا سَابِقًا ، الْجُمْلَةَ الِاسْمِيَّة هِي الْجُمْلَةِ الَّتِي تَبْدَأُ بـ( اِسْمَ )، وَتَتُكُّونَ مِن رُكْنَيْنِ أَسَاسِيَّيْنِ مُتَلَازِمَيْنِ هُمَا : <strong>الْمُبْتَدَأُ</strong> و <strong>الْخَبَرَ</strong>.</p>
<p>ولِكَي تَسْتَقِيمُ الْجُمْلَةُ ، يَجِبُ أَن نَعْرُفُ كَيْف نُحَدِّدُهُمَا وَنُعْرِبُهُمَا بِشَكْلِ صَحِيحِ.</p>

=== BLOCK 3: Identifying Subject and Predicate ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَحْدِيدُ الْمُبْتَدَأِ وَالْخَبَرِ
Content:
(Component: TEMPLATE_C_LIST.html inside Content)
- <strong>الْمُبْتَدَأَ :</strong> هُو الْاِسْمِ الْمُعَرَّفَةِ الَّذِي تَبْدَأُ بِه الْجُمْلَةِ ( مَوْضِعَ الْحَديثِ ). وَتَحْدِيدَهُ سَهْلُ جِدًّا لأَنّهُ الْكَلِمَةَ الْأوْلَى.
- <strong>الْخَبَرَ :</strong> هُو الْاِسْمِ الَّذِي يُخْبِرُ عَن الْمُبْتَدَأِ ، وبِه " يَكْتَمِلُ وَيَتِمُّ " مُعَنَّى الْجُمْلَةِ.

=== BLOCK 4: Tip (Benefit) ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Title: كَيْف تَكْتَشِفُ الْخَبَرُ بِسُهولَةِ ؟
Content: <p>اُمْسُكْ الْمُبْتَدَأَ وَاِسْأَلْ نَفْسكَ : <strong>( مَالُهُ ؟/ مَالَهَا ؟ )</strong>. الْكَلِمَةَ الَّتِي تُجِيبُكَ وَتُشْعِرُ عَقْلُكَ أَنّ الْمُعَنَّى اِكْتَمَلَ هِي ( الْخَبَرَ ).</p>
<p>مِثَالَ : " سَعِيدٌ الطَّالِبُ النَّشِيطُ الْمُجْتَهِدُ <span class="highlight-red">صَادِقٌ</span> فِي كِلَاَمِهِ ".</p>
<p>سَعِيدَ ( مُبْتَدَأَ ). مَالَهُ ؟ الطَّالِبَ ؟ لَم يَكْتَمِلُ. النَّشِيطُ ؟ لَم يَكْتَمِلُ. صَادِقٌ ! ( نَعَم اِكْتَمَلَ الْمُعَنَّى ، إِذَن <strong>صَادِقٌ</strong> هِي الْخَبَرِ ).</p>

=== BLOCK 5: The Core Matrix - Signs of Parsing ===
(Component: TEMPLATE_C_TABLE.html)
Title: الْإِعْرَابُ وَالْعَلَاَّمَاتُ ( قَاعِدَةَ ذَهَبِيَّةَ : الْمُبْتَدَأِ وَالْخَبَرِ دَائِمًا مَرْفُوعَانِ )
Headers: [ عُلَّامَةُ الرَّفْعِ, نَوْعُ الْعَلَامَةِ, نَوْعُ الْكَلِمَةِ, مِثَالٌ ]
Row 1: [ <span class="highlight-red">الضَّمَّةُ</span>, أَصْلِيَّةَ, مُفْرَدٌ, الشَّمْسُ <span class="highlight-red">سَاطِعَةٌ</span> ]
Row 2: [ <span class="highlight-red">الضَّمَّةُ</span>, أَصْلِيَّةَ, جَمْعُ مُؤَنَّثُ سَالِمُ, الْمُعَلِّمَاتُ <span class="highlight-red">مَحْبُوبَاتٌ</span> ]
Row 3: [ <span class="highlight-red">الضَّمَّةُ</span>, أَصْلِيَّةَ, جَمْعُ تَكْسيرِ, فَوَائِدُ الْعِلْمِ <span class="highlight-red">كَثِيرَةٌ</span> ]
Row 4: [ <span class="highlight-red">الْأَلِفُ</span>, فَرْعِيَّةَ, مُثَنَّى, الْمُعَلِّمَانِ <span class="highlight-red">مُخْلِصَانِ</span> ]
Row 5: [ <span class="highlight-red">الْوَاوُ</span>, فَرْعِيَّةَ, جَمَعَ مُذَكَّرُ سَالِمُ, الصَّادِقُونَ <span class="highlight-red">مَحْبُوبُونَ</span> ]
Row 6: [ <span class="highlight-red">الْوَاوُ</span>, فَرْعِيَّةَ, مِن الْأَسْمَاءِ الْخُمُسَةَ, أَخُوكَ <span class="highlight-red">ذُو</span> خَلْقٍ ]

=== BLOCK 6: Parsing Analysis (Deep Dive) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: نَمَاذِجُ إِعْرَابِيَّةٌ
Content: (Use TEMPLATE_C_IRAB_ROW.html)
(Box 1)
Word: الشَّمْسُ سَاطِعَةٌ
Details: الشَّمْسُ: مُبْتَدَأُ مَرْفُوعُ بِالضَّمَّةِ / سَاطِعَةٌ: خَبَرُ مَرْفُوعُ بِالضَّمَّةِ
(Box 2)
Word: فَوَائِدُ الْعِلْمِ كَثِيرَةٌ
Details: فَوَائِدُ: مُبْتَدَأُ مَرْفُوعُ بِالضَّمَّةِ / الْعِلْمَ: مُضَافٌ إِلَيْهِ / كَثِيرَةٌ: خَبَرُ مَرْفُوعُ بِالضَّمَّةِ
(Box 3)
Word: الْمُعَلِّمَانِ مُخْلِصَانِ
Details: مُبْتَدَأٍ وَخَبَرِ مَرْفُوعَانِ بِالْألْفِ لأَنّهُمَا مُثَنَّى
(Box 4)
Word: أَخَوْكَ ذُو خَلْقٍ
Details: أَخُوكَ: مُبْتَدَأُ مَرْفُوعُ بالواو ( لأَنّهُ مِن الْأَسْمَاءِ الْخُمُسَةَ ). ذُو: خَبَرُ مَرْفُوعُ بالواو ( لأَنّهُ مِن الْأَسْمَاءِ الْخُمُسَةَ ).

=== BLOCK 7: Special Cases of Predicate ===
(Component: TEMPLATE_C_SPLIT.html)
Title Left (Logical Right): حَالَاتُ خَاصَّةٍ لِلْخَبَرَ
Content Left: <p class="text-accent">الْقَاعِدَةُ الْعَامَّةُ أَنّ الْمُبْتَدَأِ يُكَوِّنُ ( مَعْرِفَةَ ) وَالْخَبَرَ يُكَوِّنُ ( نَكِرَةَ ).</p><p>لَكِنّ يَنْدُرُ أَن يَأْتِي الْخَبَرُ الْمُعَرَّفُ بـ ( الَ )، وَيَحْدُثُ ذَلِك غَالِبَا فِي الْحَالَاتِ التَّالِيَةِ.</p>
Title Right (Logical Left): الْحَالَاتُ
Content Right: (Use TEMPLATE_C_LIST.html)
- <strong>بَعْد الضَّمِيرِ الْمُنْفَصِلِ :</strong> ( أَنَا ، هُو ، نَحْن ...). مِثَالَ : <strong>( هُوَ الْعَالِمُ )</strong> هُو: ضَمِيرُ مُنْفَصِلُ مَبْنِيُّ فِي مَحَلِّ رَفْعِ مُبْتَدَأٍ. الْعَالَمُ: خَبَرُ مَرْفُوعُ بِالضَّمَّةِ.
- <strong>لِغَرَضُ التَّوْكِيدِ وَالْحَصْرِ ( بَلَاغيا ) :</strong> مِثَالٌ الْمَقُولَةُ الْمَشْهُورَةُ : <strong>( الْعِلْمُ النُّورُ )</strong> الْعِلْمَ مُبْتَدَأٌ ، النُّورَ خَبِرٌ وكِلَاهُمَا مُعَرَّفٌ بـ ( الَ ).

=== BLOCK 8: Exam 1 ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: اِسْتَخْرَجَ الْمُبْتَدَأِ وَالْخَبَرِ فِي الْجَمَلِ الْآتِيَةِ ، وَاُذْكُرْ عُلَّامَةَ الرَّفْعِ :
١. الْقُرَّاءَةُ غِذَاءُ الْعَقْلِ .
٢. الطَّالِبُ الْمُجْتَهِدُ مُتَفَوِّقٌ .
٣. أَبُوكَ رَجُلٌ كَرِيمٌ .

=== BLOCK 9: Exam 2 ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: أَعْرَبَ الْجُمْلَةُ التَّالِيَةُ إِعْرَابًا تَامًّا : ( هُوَ الْعَالِمُ )
- هُوَ :
- الْعَالِمُ :

--- END STREAM ---