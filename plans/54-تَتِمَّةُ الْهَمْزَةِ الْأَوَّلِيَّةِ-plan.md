# **SESSION 54.0**

[TASK DEFINITION]
Objective: Implement تَتِمَّةُ الْهَمْزَةِ الْأَوَّلِيَّةِ.
File: `pages/54.0_nXX_تَتِمَّةُ الْهَمْزَةِ الْأَوَّلِيَّةِ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/54.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 54
[CHAPTER_TITLE]: تَتِمَّةُ الْهَمْزَةِ الْأَوَّلِيَّةِ
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم الإملاء
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Introduction to Hamzat Al-Istifham ===
(Component: TEMPLATE_C_BLOCK.html)
Title: اجْتِمَاعُ الْهَمْزَةِ الْأَوَّلِيَّةِ مَعَ هَمْزَةِ الِاسْتِفْهَامِ (أَ)
Content:
<p class="text-accent">مَاذَا يَحْدُثُ لَوْ سَأَلْنَا بِاسْتِخْدَامِ الْهَمْزَةِ وَأَتَى بَعْدَهَا كَلِمَةٌ تَبْدَأُ بِهَمْزَةٍ أَيْضاً؟</p>

=== BLOCK 3: Rules Breakdown ===
(Component: TEMPLATE_C_BLOCK.html)
Title: قَوَاعِدُ اجْتِمَاعِ الْهَمْزَتَيْنِ
Content: (Use TEMPLATE_C_LIST.html for the following items)
[LIST_ITEM_CONTENT]: <span class="font-bold">١- إِذَا كَانَتْ هَمْزَةَ وَصْلٍ (فِعْلٌ أَوْ اسْمٌ عَادِيٌّ):</span> تُحْذَفُ هَمْزَةُ الْوَصْلِ نِهَائِيّاً!
<br><span class="highlight-blue">أَ</span> + ابْنُكَ هَذَا؟ = <span class="highlight-red">أَبْنُكَ</span> هَذَا؟ (وَلَيْسَ أَابْنُكَ).
<br><span class="highlight-blue">أَ</span> + انْكَسَرَ الزُّجَاجُ؟ = <span class="highlight-red">أَنْكَسَرَ</span> الزُّجَاجُ؟
[LIST_ITEM_CONTENT]: <span class="font-bold">٢- إِذَا كَانَتْ أَدَاةَ التَّعْرِيفِ (الـ):</span> تُدْغَمُ الْهَمْزَتَانِ وَتُصْبِحَانِ مَدَّةً (<span class="highlight-red">آ</span>).
<br><span class="highlight-blue">أَ</span> + الْعِلْمُ نُورٌ؟ = <span class="highlight-red">آلْعِلْمُ</span> نُورٌ؟ (مِثْلُ: <span class="highlight-red">آلْكِتَابُ</span> مُفِيدٌ؟).
[LIST_ITEM_CONTENT]: <span class="font-bold">٣- إِذَا كَانَتْ هَمْزَةَ قَطْعٍ:</span> تَبْقَى كَمَا هِيَ!
<br><span class="highlight-blue">أَ</span> + أَنْتَ نَاجِحٌ؟ = <span class="highlight-red">أَأَنْتَ</span> نَاجِحٌ؟
<br><span class="highlight-blue">أَ</span> + إِلَى السُّوقِ تَذْهَبُ؟ = <span class="highlight-red">أَإِلَى</span> السُّوقِ تَذْهَبُ؟

=== BLOCK 4: The Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Headers: نَوْعُ الْهَمْزَةِ، الْقَاعِدَةُ، الْمِثَالُ
Row 1: هَمْزَةُ وَصْلٍ | تُحْذَفُ هَمْزَةُ الْوَصْلِ | أَبْنُكَ هَذَا؟
Row 2: أَدَاةُ التَّعْرِيفِ (الـ) | تُدْغَمُ إِلَى مَدَّةٍ (آ) | آلْعِلْمُ نُورٌ؟
Row 3: هَمْزَةُ قَطْعٍ | تَبْقَى كَمَا هِيَ | أَأَنْتَ نَاجِحٌ؟

=== BLOCK 5: Details on Deleting Hamzat Ibn ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَفْصِيلُ مَوَاضِعِ حَذْفِ هَمْزَةِ (ابْن)
Content:
<p class="text-accent">كَلِمَةُ (ابْن) هَمْزَتُهَا وَصْلٌ. لَكِنَّهَا تُحْذَفُ كِتَابَةً (وَنَكْتُبُهَا: <span class="highlight-red">بْن</span>) فِي حَالَاتٍ:</p>
(Use TEMPLATE_C_LIST.html for the following items)
[LIST_ITEM_CONTENT]: <span class="font-bold">١.</span> بَيْنَ عَلَمَيْنِ (اسْمَيْ أَشْخَاصٍ) بِشَرْطِ أَنْ يَكُونَ الثَّانِي أَبًا لِلْأَوَّلِ وَالْكَلِمَةُ مُفْرَدَةٌ فِي سَطْرٍ وَاحِدٍ: طَارِقُ <span class="highlight-red">بْنُ</span> حَازِمٍ، سَامِي <span class="highlight-red">بْنُ</span> رَامِي.
[LIST_ITEM_CONTENT]: <span class="font-bold">٢.</span> بَعْدَ حَرْفِ النِّدَاءِ (<span class="highlight-blue">يَا</span>): يَا <span class="highlight-red">بْنَ</span> الْكِرَامِ، يَا <span class="highlight-red">بْنَ</span> خَالِدٍ.
[LIST_ITEM_CONTENT]: <span class="font-bold">٣.</span> بَعْدَ هَمْزَةِ الِاسْتِفْهَامِ كَمَا مَرَّ: <span class="highlight-red">أَبْنُكَ</span> هَذَا؟

=== BLOCK 6: Benefit Warning Box ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: ⚠️ مَتَى تَثْبُتُ وَتُكْتَبُ أَلِفاً؟
Content:
(Use TEMPLATE_C_LIST.html for the following items)
[LIST_ITEM_CONTENT]: إِذَا جَاءَتْ فِي أَوَّلِ السَّطْرِ (حَتَّى لَوْ بَيْنَ عَلَمَيْنِ).
[LIST_ITEM_CONTENT]: إِذَا أُضِيفَتْ إِلَى الْأُمِّ أَوْ الْجَدِّ: رَامِي <span class="highlight-red">ابْنُ</span> سَلْمَى.
[LIST_ITEM_CONTENT]: إِذَا كَانَتْ خَبَراً لَيْسَ بَيْنَ أَبٍ وَابْنِهِ: أَخِي <span class="highlight-red">ابْنُ</span> أُسْتَاذِي.
[LIST_ITEM_CONTENT]: إِذَا ثُنِّيَتْ أَوْ جُمِعَتْ: طَارِقٌ وَحَازِمٌ <span class="highlight-red">ابْنَا</span> زَيْدٍ. هَؤُلَاءِ <span class="highlight-red">أَبْنَاءُ</span> زَيْدٍ.

=== BLOCK 7: Matrix 2 (Summary Table for Ibn) ===
(Component: TEMPLATE_C_TABLE.html)
Headers: الْحَالَةُ، الْقَاعِدَةُ، الْمِثَالُ
Row 1: بَيْنَ عَلَمَيْنِ، بَعْدَ (يَا)، بَعْدَ (أَ) | تُحْذَفُ أَلِفُ (ابْن) | طَارِقُ بْنُ حَازِمٍ
Row 2: أَوَّلُ السَّطْرِ، لِلْأُمِّ، خَبَرٌ، مُثَنَّى/جَمْعٌ | تَثْبُتُ أَلِفُ (ابْن) | أَبْنَاءُ زَيْدٍ

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: كَيْفَ نَكْتُبُ الْجُمَلَ التَّالِيَةَ عِنْدَ دُخُولِ هَمْزَةِ الِاسْتِفْهَامِ عَلَيْهَا: ابْنُكَ هَذَا؟، انْكَسَرَ الزُّجَاجُ؟، الْعِلْمُ نُورٌ؟، أَنْتَ نَاجِحٌ؟
Number: ٢
Question: مَتَى تَثْبُتُ أَلِفُ (ابْن) وَتُكْتَبُ كَمَا فِي الْأَمْثِلَةِ: رَامِي ابْنُ سَلْمَى، أَخِي ابْنُ أُسْتَاذِي، طَارِقٌ وَحَازِمٌ ابْنَا زَيْدٍ؟

--- END STREAM ---