# **SESSION 12.0**

[TASK DEFINITION]
Objective: Implement الضَّمَائِرُ (الجزء الثاني).
File: `pages/12.0_nXX_الضَّمَائِرُ (الجزء الثاني).html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/12.1_nXX_الضَّمَائِرُ (الجزء الثاني)_تابع.html` if page have a lot of blank space add exam elements from the lesson.
3. text Content: 100% Arabic with full Harakat.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green` for secondary.
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
[LESSON_NUMBER]: 12
[CHAPTER_TITLE]: الضَّمَائِرُ (الجزء الثاني)
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition & Rule ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَفْصِيلُ ضَمَائِرِ النَّصْبِ وَالْجَرِّ الْمُتَّصِلَةِ (نَاهِيكَ)
Content: <p class="text-accent mb-2mm">هَذِهِ الضَّمَائِرُ (نَا، هَاءٌ، يَاءٌ، كَافٌ) لَهَا ثَلَاثَةُ أَحْوَالٍ حَسَبَ الْكَلِمَةِ الَّتِي تَلْتَصِقُ بِهَا:</p>

=== BLOCK 3: The Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Header 1: الْحَالَةُ
Header 2: الْمَحَلُّ الْإِعْرَابِيُّ
Header 3: مِثَالٌ
Row 1 Col 1: مَعَ الْأَفْعَالِ
Row 1 Col 2: نَصْبٌ مَفْعُولٌ بِهِ
Row 1 Col 3: أَكْرَمَنَا الْمُعَلِّمُ
Row 2 Col 1: مَعَ الْأَسْمَاءِ
Row 2 Col 2: جَرٌّ بِالْإِضَافَةِ
Row 2 Col 3: مُعَلِّمُهُ
Row 3 Col 1: مَعَ حُرُوفِ الْجَرِّ
Row 3 Col 2: جَرٌّ بِحَرْفِ الْجَرِّ
Row 3 Col 3: فِيهِ
Row 4 Col 1: مَعَ كَانَ وَأَخَوَاتِهَا
Row 4 Col 2: رَفْعٌ اسْمُ كَانَ
Row 4 Col 3: كُنْتُ أَدْرُسُ

=== BLOCK 4: Deep Dive 1 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ١. مَعَ الْأَفْعَالِ (نَصْبٌ)
Content: <p class="text-accent mb-2mm">تَكُونُ فِي مَحَلِّ نَصْبٍ مَفْعُولٍ بِهِ إِذَا اتَّصَلَتْ بِالْفِعْلِ (لِأَنَّهَا لَا تَفْعَلُ، بَلْ يَقَعُ عَلَيْهَا الْفِعْلُ)، وَهِيَ:</p>
(Inject TEMPLATE_C_LIST.html inside content)
[LIST_ITEM_CONTENT]: نَا الْمَفْعُولِينَ (أَكْرَمَ<span class="highlight-red">نَا</span> الْمُعَلِّمُ).
[LIST_ITEM_CONTENT]: هَاءُ الْغَائِبِ (أَكَلَ<span class="highlight-red">هُ</span> الْقِطُّ، شَرَحَ<span class="highlight-red">هُ</span> الْمُعَلِّمُ).
[LIST_ITEM_CONTENT]: يَاءُ الْمُتَكَلِّمِ (أَكْرَمَنِ<span class="highlight-red">ي</span> صَدِيقِي، ضَرَبَنِ<span class="highlight-red">ي</span> الشَّخْصُ).
[LIST_ITEM_CONTENT]: كَافُ الْخِطَابِ (رَأَيْتُ<span class="highlight-red">كَ</span> فِي السُّوقِ، أَحَبَّ<span class="highlight-red">كَ</span> النَّاسُ).

=== BLOCK 5: Deep Dive 2 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٢. مَعَ الْأَسْمَاءِ (جَرٌّ بِالْإِضَافَةِ)
Content: <p class="text-accent mb-2mm font-bold">قَاعِدَةٌ ذَهَبِيَّةٌ: أَيُّ ضَمِيرٍ يَتَّصِلُ بِالِاسْمِ يُعْرَبُ دَائِماً: ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.</p>
<p class="mb-0">مِثَالٌ: مُعَلِّمُ<span class="highlight-red">هُ</span> / بَيْتُ<span class="highlight-red">كَ</span> / كِتَابِ<span class="highlight-red">ي</span> / مَدْرَسَتُ<span class="highlight-red">نَا</span>. (الْهَاءُ، الْكَافُ، الْيَاءُ، النَّا: مُضَافٌ إِلَيْهِ).</p>

=== BLOCK 6: Deep Dive 3 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٣. مَعَ حُرُوفِ الْجَرِّ (جَرٌّ بِحَرْفِ الْجَرِّ)
Content: <p class="text-accent mb-2mm">إِذَا اتَّصَلَتْ هَذِهِ الضَّمَائِرُ بِحَرْفِ الْجَرِّ تُعْرَبُ: فِي مَحَلِّ جَرٍّ اسْمٌ مَجْرُورٌ.</p>
<p class="mb-0">مِثْلٌ: فِي<span class="highlight-red">هِ</span> (فِي + هـ)، عَلَيْ<span class="highlight-red">كَ</span> (عَلَى + ك)، لَ<span class="highlight-red">نَا</span> (لـ + نَا)، بِ<span class="highlight-red">ي</span> (بِـ + ي).</p>

=== BLOCK 7: Deep Dive 4 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٤. مَعَ كَانَ وَأَخَوَاتِهَا (رَفْعٌ اسْتِثْنَائِيٌّ)
Content: <p class="text-accent mb-2mm">إِذَا اتَّصَلَ الضَّمِيرُ بِكَانَ وَأَخَوَاتِهَا يُعْرَبُ: فِي مَحَلِّ رَفْعٍ اسْمُ كَانَ.</p>
<p class="mb-0">مِثَالٌ: كُنْ<span class="highlight-red">تُ</span> أَدْرُسُ (التَّاءُ اسْمُ كَانَ). كَانُ<span class="highlight-red">وا</span> نَائِمِينَ (الْوَاوُ اسْمُ كَانَ). كُنَّ<span class="highlight-red">ا</span> أَطْفَالاً (النَّا اسْمُ كَانَ).</p>

=== BLOCK 8: Benefit Tip ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Title:  فَائِدَةٌ: يَاءُ الْمُتَكَلِّمِ وَنُونُ الْوِقَايَةِ
Content: <p class="mb-2mm">هَلْ لَاحَظْتَ أَنَّكَ تَقُولُ (كِتَابِي) بِدُونِ نُونٍ، وَلَكِنْ تَقُولُ فِي الْفِعْلِ (أَعْطَانِي) بِنُونٍ قَبْلَ الْيَاءِ؟ هَذِهِ النُّونُ تُسَمَّى <span class="font-bold">"نُونَ الْوِقَايَةِ"</span>.</p>
(Inject TEMPLATE_C_LIST.html inside content)
[LIST_ITEM_CONTENT]: <span class="font-bold">١. مَعَ الْفِعْلِ (تَجِبُ نُونُ الْوِقَايَةِ):</span> لِتَقِيَ الْفِعْلَ مِنَ الْكَسْرِ (لِأَنَّ الْفِعْلَ لَا يُكْسَرُ). مِثَالٌ: هَجَرَنِي (النُّونُ لِلْوِقَايَةِ لَا مَحَلَّ لَهَا، الْيَاءُ مَفْعُولٌ بِهِ).
[LIST_ITEM_CONTENT]: <span class="font-bold">٢. مَعَ الِاسْمِ (لَا نُونَ وِقَايَةٍ):</span> الِاسْمُ يُكْسَرُ عَادِيّاً، وَيُعْرَبُ مَا قَبْلَهُ بِحَرَكَةٍ مُقَدَّرَةٍ. مِثَالٌ: صَدِيقِي (الْيَاءُ مُضَافٌ إِلَيْهِ، الْقَافُ مَكْسُورَةٌ لِتُنَاسِبَ الْيَاءَ).

=== BLOCK 9: Benefit Warning ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: ⚠️ تَنْبِيهٌ: الْأَسْمَاءُ الْخَمْسَةُ وَيَاءُ الْمُتَكَلِّمِ
Content: <p class="text-accent mb-2mm">الْأَسْمَاءُ الْخَمْسَةُ (أَبٌ، أَخٌ، حَمٌ، فُو، ذُو) تُرْفَعُ بِالْوَاوِ، تُنْصَبُ بِالْأَلِفِ، وَتُجَرُّ بِالْيَاءِ، بِشَرْطِ إِضَافَتِهَا لِأَيِّ ضَمِيرٍ غَيْرِ يَاءِ الْمُتَكَلِّمِ.</p>
<p class="text-accent mb-2mm">إِذَا اتَّصَلَتِ الْأَسْمَاءُ الْخَمْسَةُ بِيَاءِ الْمُتَكَلِّمِ خَاصَّةً، تُعْرَبُ بِالْحَرَكَاتِ الْمُقَدَّرَةِ وَتَفْقِدُ مِيزَتَهَا الْإِعْرَابِيَّةَ.</p>
(Inject TEMPLATE_C_LIST.html inside content)
[LIST_ITEM_CONTENT]: <span class="font-bold">مَعَ غَيْرِ الْيَاءِ (تُعْرَبُ بِالْحُرُوفِ):</span> جَاءَ أَبُوكَ (مَرْفُوعٌ بِالْوَاوِ). رَأَيْتُ أَخَاهُ (مَنْصُوبٌ بِالْأَلِفِ).
[LIST_ITEM_CONTENT]: <span class="font-bold">مَعَ يَاءِ الْمُتَكَلِّمِ (تُعْرَبُ بِحَرَكَاتٍ مُقَدَّرَةٍ):</span> جَاءَ أَبِي (مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ). رَأَيْتُ أَخِي (مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ).

=== BLOCK 10: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number 1: ١
Question 1: حَدِّدِ الضَّمِيرَ الْمُتَّصِلَ وَأَعْرِبْهُ فِي جُمْلَةِ: " سَافَرْتُ إِلَى الشَّامِ".
Number 2: ٢
Question 2: مَا الْفَرْقُ بَيْنَ (نَا) فِي الْفِعْلَيْنِ: " أَكْرَمْنَا الضَّيْفَ" (بِسُكُونِ الْمِيمِ) وَ " أَكْرَمَنَا الضَّيْفُ" (بِفَتْحِ الْمِيمِ)؟
Number 3: ٣
Question 3: مَا الْمَحَلُّ الْإِعْرَابِيُّ لِلضَّمِيرِ (الْكَافِ) فِي كَلِمَةِ " بَيْتُكَ "؟ وَمَا الْقَاعِدَةُ؟

--- END STREAM ---
