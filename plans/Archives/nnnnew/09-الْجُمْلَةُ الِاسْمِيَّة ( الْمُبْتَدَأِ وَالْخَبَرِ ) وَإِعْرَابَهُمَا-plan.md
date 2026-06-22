# **SESSION 09.0**

[TASK DEFINITION]
Objective: Implement الْجُمْلَةُ الِاسْمِيَّة ( الْمُبْتَدَأِ وَالْخَبَرِ ) وَإِعْرَابَهُمَا.
File: `pages/09.0_nXX_الْجُمْلَةُ الِاسْمِيَّة ( الْمُبْتَدَأِ وَالْخَبَرِ ) وَإِعْرَابَهُمَا.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
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
[LESSON_NUMBER]: 09
[CHAPTER_TITLE]: الْجُمْلَةُ الِاسْمِيَّةُ (الْمُبْتَدَأُ وَالْخَبَرُ) وَإِعْرَابُهُمَا
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. حنا خفيف
[AUTHOR_PHONE]:  

=== BLOCK 2: Definition Block ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مُقَدِّمَةٌ
Content:
`<p class="text-accent">كَمَا تَعَلَّمْنَا سَابِقًا ، الْجُمْلَةُ الِاسْمِيَّةُ هِيَ الْجُمْلَةُ الَّتِي تَبْدَأُ بِـ (اِسْمٍ)، وَتَتَكَوَّنُ مِنْ رُكْنَيْنِ أَسَاسِيَّيْنِ مُتَلَازِمَيْنِ هُمَا: <span class="highlight-blue">الْمُبْتَدَأُ</span> وَ <span class="highlight-blue">الْخَبَرُ</span>.</p><p>وَلِكَيْ تَسْتَقِيمَ الْجُمْلَةُ ، يَجِبُ أَنْ نَعْرِفَ كَيْفَ نُحَدِّدُهُمَا وَنُعْرِبُهُمَا بِشَكْلٍ صَحِيحٍ.</p>`

=== BLOCK 3: Split Block - Defining Subject and Predicate ===
(Component: TEMPLATE_C_SPLIT.html)
LeftSide:
(Component: TEMPLATE_C_BLOCK.html)
Title: تَحْدِيدُ الْمُبْتَدَأِ
Content: `<p>هُوَ الْاِسْمُ الْمَعْرِفَةُ الَّذِي تَبْدَأُ بِهِ الْجُمْلَةُ (مَوْضِعُ الْحَدِيثِ). وَتَحْدِيدُهُ سَهْلٌ جِدًّا لِأَنَّهُ الْكَلِمَةُ الْأُولَى.</p>`

RightSide:
(Component: TEMPLATE_C_BLOCK.html)
Title: تَحْدِيدُ الْخَبَرِ
Content: `<p>هُوَ الْاِسْمُ الَّذِي يُخْبِرُ عَنِ الْمُبْتَدَأِ ، وَبِهِ " يَكْتَمِلُ وَيَتِمُّ " مَعْنَى الْجُمْلَةِ.</p>`

=== BLOCK 4: Benefit Tip - How to find the Predicate ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Content:
`<p class="font-bold text-primary">كَيْفَ تَكْتَشِفُ الْخَبَرَ بِسُهُولَةٍ ؟</p>
<p>اُمْسُكِ الْمُبْتَدَأَ وَاسْأَلْ نَفْسَكَ: <span class="highlight-red">(مَالُهُ ؟ / مَالَهَا ؟)</span>. الْكَلِمَةُ الَّتِي تُجِيبُكَ وَتُشْعِرُ عَقْلَكَ أَنَّ الْمَعْنَى اكْتَمَلَ هِيَ (الْخَبَرُ).</p>
<p>مِثَالٌ: "سَعِيدٌ الطَّالِبُ النَّشِيطُ الْمُجْتَهِدُ <span class="highlight-red">صَادِقٌ</span> فِي كَلَامِهِ".</p>
<p>سَعِيدٌ (مُبْتَدَأٌ)... مَالُهُ ؟ الطَّالِبُ ؟ لَمْ يَكْتَمِلْ. النَّشِيطُ ؟ لَمْ يَكْتَمِلْ. صَادِقٌ! (نَعَمْ اكْتَمَلَ الْمَعْنَى ، إِذَنْ <span class="highlight-red">صَادِقٌ</span> هِيَ الْخَبَرُ).</p>`

=== BLOCK 5: Block for Rule ===
(Component: TEMPLATE_C_BLOCK.html)
Title: قَاعِدَةٌ ذَهَبِيَّةٌ (الْإِعْرَابُ وَالْعَلَامَاتُ)
Content: `<p class="text-accent">الْمُبْتَدَأُ وَالْخَبَرُ دَائِمًا (<span class="highlight-red">مَرْفُوعَانِ</span>). لَكِنْ تَخْتَلِفُ عَلَامَةُ الرَّفْعِ حَسَبَ نَوْعِ الْكَلِمَةِ.</p>`

=== BLOCK 6: The Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Headers: عَلَامَةُ الرَّفْعِ | نَوْعُ الْكَلِمَةِ | مِثَالٌ
Row 1: الضَّمَّةُ (عَلَامَةٌ أَصْلِيَّةٌ) | مُفْرَدٌ ، جَمْعُ مُؤَنَّثٍ سَالِمٌ ، جَمْعُ تَكْسِيرٍ | الشَّمْسُ سَاطِعَةٌ
Row 2: الْأَلِفُ (عَلَامَةٌ فَرْعِيَّةٌ) | مُثَنَّى | الْمُعَلِّمَانِ مُخْلِصَانِ
Row 3: الْوَاوُ (عَلَامَةٌ فَرْعِيَّةٌ) | جَمْعُ مُذَكَّرٍ سَالِمٌ ، الْأَسْمَاءُ الْخَمْسَةُ | الصَّادِقُونَ مَحْبُوبُونَ

=== BLOCK 7: Extra Explanation Block ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَمْثِلَةٌ وَإِعْرَابٌ عَلَى عَلَامَاتِ الرَّفْعِ
Content: `<p>تَطْبِيقٌ لِلْقَاعِدَةِ الذَّهَبِيَّةِ عَلَى أَنْوَاعِ الْكَلِمَاتِ وَإِعْرَابِهَا:</p>`

=== BLOCK 8: Irab Row (Damma) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
RightSide:
(Component: TEMPLATE_C_IRAB_BOX.html)
Word: الشَّمْسُ
Details: مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.
LeftSide:
(Component: TEMPLATE_C_IRAB_BOX.html)
Word: سَاطِعَةٌ
Details: خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.

=== BLOCK 9: Benefit General Info (More Damma examples) ===
(Component: TEMPLATE_C_BENEFIT.html)
Content:
`<p><b>الْمُعَلِّمَاتُ مَحْبُوبَاتٌ:</b> (مُبْتَدَأٌ وَخَبَرٌ مَرْفُوعَانِ بِالضَّمَّةِ لِأَنَّهُمَا جَمْعُ مُؤَنَّثٍ سَالِمٌ).</p>
<p><b>فَوَائِدُ الْعِلْمِ كَثِيرَةٌ:</b> (فَوَائِدُ: مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ لِأَنَّهُ جَمْعُ تَكْسِيرٍ / الْعِلْمِ: مُضَافٌ إِلَيْهِ / كَثِيرَةٌ: خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ).</p>`

=== BLOCK 10: Irab Row (Alif and Waw) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
RightSide:
(Component: TEMPLATE_C_IRAB_BOX.html)
Word: الْمُعَلِّمَانِ
Details: مُبْتَدَأٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنَّى. (وَ: مُخْلِصَانِ خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ).
LeftSide:
(Component: TEMPLATE_C_IRAB_BOX.html)
Word: أَخُوكَ
Details: مُبْتَدَأٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ. (وَ: ذُو خَبَرٌ مَرْفُوعٌ بِالْوَاوِ).

=== BLOCK 11: Block for Special Cases ===
(Component: TEMPLATE_C_BLOCK.html)
Title: حَالَاتٌ خَاصَّةٌ لِلْخَبَرِ
Content: `<p>الْقَاعِدَةُ الْعَامَّةُ أَنَّ الْمُبْتَدَأَ يَكُونُ (مَعْرِفَةً) وَالْخَبَرَ يَكُونُ (نَكِرَةً). لَكِنْ يَنْدُرُ أَنْ يَأْتِيَ الْخَبَرُ الْمُعَرَّفُ بِـ (ال)، وَيَحْدُثُ ذَلِكَ غَالِبًا فِي الْحَالَاتِ التَّالِيَةِ:</p>`

=== BLOCK 12: List for Special Cases ===
(Component: TEMPLATE_C_LIST.html)
Items:
- **بَعْدَ الضَّمِيرِ الْمُنْفَصِلِ:** (أَنَا ، هُوَ ، نَحْنُ ...). مِثَالٌ: (<span class="highlight-blue">هُوَ</span> <span class="highlight-red">الْعَالِمُ</span>). هُوَ: ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعِ مُبْتَدَأٍ. الْعَالِمُ: خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.
- **لِغَرَضِ التَّوْكِيدِ وَالْحَصْرِ (بَلَاغِيًّا):** مِثَالٌ الْمَقُولَةُ الْمَشْهُورَةُ: (<span class="highlight-blue">الْعِلْمُ</span> <span class="highlight-red">النُّورُ</span>). الْعِلْمُ مُبْتَدَأٌ ، النُّورُ خَبَرٌ وَكِلَاهُمَا مُعَرَّفٌ بِـ (ال).

=== BLOCK 13: Exam Section 1 ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: اسْتَخْرِجِ الْمُبْتَدَأَ وَالْخَبَرَ فِي الْجُمَلِ الْآتِيَةِ، وَاذْكُرْ عَلَامَةَ الرَّفْعِ: (١. الْقِرَاءَةُ غِذَاءُ الْعَقْلِ) (٢. الطَّالِبُ الْمُجْتَهِدُ مُتَفَوِّقٌ) (٣. أَبُوكَ رَجُلٌ كَرِيمٌ).

=== BLOCK 14: Exam Section 2 ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: أَعْرِبِ الْجُمْلَةَ التَّالِيَةَ إِعْرَابًا تَامًّا: ( هُوَ الْعَالِمُ ).

--- END STREAM ---
