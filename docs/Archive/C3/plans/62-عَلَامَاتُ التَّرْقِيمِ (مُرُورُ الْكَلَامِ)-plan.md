# **SESSION 62.0**

[TASK DEFINITION]
Objective: Implement عَلَامَاتُ التَّرْقِيمِ (مُرُورُ الْكَلَامِ).
File: `pages/62.0_nXX_عَلَامَاتُ التَّرْقِيمِ (مُرُورُ الْكَلَامِ).html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/62.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 62
[CHAPTER_TITLE]: عَلَامَاتُ التَّرْقِيمِ (مُرُورُ الْكَلَامِ)
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم الإملاء
[AUTHOR_NAME]: أ. حنا خفيف
[AUTHOR_PHONE]:  

=== BLOCK 2: تَعْرِيفُ عَلَامَاتِ التَّرْقِيمِ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَعْرِيفُ عَلَامَاتِ التَّرْقِيمِ
Content:
<p class="mt-1mm text-accent">هِيَ إِشَارَاتُ مُرُورٍ تُوضَعُ بَيْنَ الْجُمَلِ لِتُنَظِّمَ السَّيْرَ، فَتُخْبِرُ الْقَارِئَ مَتَى يَقِفُ، وَمَتَى يَتَعَجَّبُ، وَمَتَى يَسْأَلُ، لِيُفْهَمَ الْمَعْنَى صَحِيحاً بِدُونِ اخْتِلَاطٍ.</p>

=== BLOCK 3: جَدْوَلُ عَلَامَاتِ التَّرْقِيمِ وَاسْتِخْدَامَاتِهَا ===
(Component: TEMPLATE_C_BLOCK.html wrapping TEMPLATE_C_TABLE.html)
Title: جَدْوَلُ مُلَخَّصِ عَلَامَاتِ التَّرْقِيمِ وَاسْتِخْدَامَاتِهَا
Content:
(Insert TEMPLATE_C_TABLE.html here)
Headers: الرَّمْزُ | الاسْمُ | الاسْتِخْدَامُ (مَتَى نَضَعُهَا؟)
Row 1: ( <span class="highlight-red">.</span> ) | النُّقْطَةُ | عِنْدَ انْتِهَاءِ الْكَلَامِ، وَاكْتِمَالِ الْمَعْنَى تَمَاماً، وَنِهَايَةِ الْفِقْرَةِ.
Row 2: ( <span class="highlight-red">:</span> ) | النُّقْطَتَانِ | بَعْدَ الْقَوْلِ (قَالَ، أَجَابَ، رَدَّ). وَقَبْلَ التَّعْدَادِ وَالتَّفْصِيلِ (فُصُولُ السَّنَةِ أَرْبَعَةٌ: الرَّبِيعُ، وَالصَّيْفُ، وَالْخَرِيفُ، وَالشِّتَاءُ).
Row 3: ( <span class="highlight-red">...</span> ) | النِّقَاطُ المُتَعَدِّدَةُ | (عَادَةً ٣ نِقَاطٍ) لِلدَّلَالَةِ عَلَى كَلَامٍ مَحْذُوفٍ أَوْ بَقِيَّةٍ لَمْ نُكْمِلْهَا.
Row 4: ( <span class="highlight-red">،</span> ) | الفَاصِلَةُ | فَاصِلٌ قَصِيرٌ لِأَخْذِ نَفَسٍ، نَضَعُهَا بَيْنَ الْجُمَلِ الْقَصِيرَةِ، وَقَبْلَ حُرُوفِ الْعَطْفِ (وَ، فـ)، وَبَعْدَ النِّدَاءِ (يَا بُنَيَّ، اصْبِرْ).
Row 5: ( <span class="highlight-red">؛</span> ) | الفَاصِلَةُ المَنْقُوطَةُ | تُوضَعُ بَيْنَ جُمْلَتَيْنِ، الثَّانِيَةُ سَبَبٌ لِلْأُولَى (نَجَحَ الطَّالِبُ؛ لِأَنَّهُ سَهِرَ اللَّيَالِيَ).
Row 6: ( <span class="highlight-red">!</span> ) | عَلَامَةُ التَّعَجُّبِ | لِإِظْهَارِ الدَّهْشَةِ، الْفَرَحِ، الْحُزْنِ، أَوْ الِاسْتِغْرَابِ (مَا أَجْمَلَ السَّمَاءَ! ، وَاحَسْرَتَاهُ!).
Row 7: ( <span class="highlight-red">؟</span> ) | عَلَامَةُ الاسْتِفْهَامِ | بَعْدَ السُّؤَالِ دَائِماً (مَا اسْمُكَ؟ ، هَلْ ذَاكَرْتَ؟).
Row 8: ( <span class="highlight-red">« »</span> ) | عَلَامَةُ التَّنْصِيصِ | لِحَصْرِ كَلَامٍ مَنْقُولٍ بِالْحَرْفِ (كَمَا هُوَ دُونَ تَغْيِيرٍ) مِثْلَ الْأَقْوَالِ الْمَأْثُورَةِ أَوْ كَلَامِ الْعُلَمَاءِ. قَالَ الْحَكِيمُ: «الْوَقْتُ ثَمِينٌ».
Row 9: ( <span class="highlight-red">- -</span> ) | الشَّرْطَتَانِ / الِاعْتِرَاضِ | لِحَصْرِ جُمْلَةٍ اعْتِرَاضِيَّةٍ (لَوْ حَذَفْنَاهَا لَا يَتَغَيَّرُ الْمَعْنَى)، كَالدُّعَاءِ وَالتَّوْضِيحِ. (أَخِي - سَلَّمَهُ الزَّمَانُ - مُخْلِصٌ).

=== BLOCK 4: التَّفْصِيلُ: عَلَامَاتُ الْوَقْفِ وَالْفَصْلِ ===
(Component: TEMPLATE_C_BLOCK.html wrapping TEMPLATE_C_LIST.html)
Title: أَوْلاً: عَلَامَاتُ الْوَقْفِ وَالْفَصْلِ
Content:
(Insert TEMPLATE_C_LIST.html here)
List Items:
- <strong>النُّقْطَةُ ( . ) :</strong> عِنْدَ انْتِهَاءِ الْكَلَامِ، وَاكْتِمَالِ الْمَعْنَى تَمَاماً، وَنِهَايَةِ الْفِقْرَةِ.
- <strong>الفَاصِلَةُ ( ، ) :</strong> فَاصِلٌ قَصِيرٌ لِأَخْذِ نَفَسٍ، نَضَعُهَا بَيْنَ الْجُمَلِ الْقَصِيرَةِ، وَقَبْلَ حُرُوفِ الْعَطْفِ (وَ، فـ)، وَبَعْدَ النِّدَاءِ (يَا بُنَيَّ، اصْبِرْ).
- <strong>الفَاصِلَةُ المَنْقُوطَةُ ( ؛ ) :</strong> تُوضَعُ بَيْنَ جُمْلَتَيْنِ، الثَّانِيَةُ سَبَبٌ لِلْأُولَى (نَجَحَ الطَّالِبُ؛ لِأَنَّهُ سَهِرَ اللَّيَالِيَ).

=== BLOCK 5: التَّفْصِيلُ: عَلَامَاتُ الِانْفِعَالِ وَالِاسْتِفْهَامِ ===
(Component: TEMPLATE_C_BLOCK.html wrapping TEMPLATE_C_LIST.html)
Title: ثَانِياً: عَلَامَاتُ الِانْفِعَالِ وَالِاسْتِفْهَامِ
Content:
(Insert TEMPLATE_C_LIST.html here)
List Items:
- <strong>عَلَامَةُ التَّعَجُّبِ ( ! ) :</strong> لِإِظْهَارِ الدَّهْشَةِ، الْفَرَحِ، الْحُزْنِ، أَوْ الِاسْتِغْرَابِ (مَا أَجْمَلَ السَّمَاءَ! ، وَاحَسْرَتَاهُ!).
- <strong>عَلَامَةُ الاسْتِفْهَامِ ( ؟ ) :</strong> بَعْدَ السُّؤَالِ دَائِماً (مَا اسْمُكَ؟ ، هَلْ ذَاكَرْتَ؟).

=== BLOCK 6: التَّفْصِيلُ: عَلَامَاتُ التَّوْضِيحِ وَالنَّقْلِ ===
(Component: TEMPLATE_C_BLOCK.html wrapping TEMPLATE_C_LIST.html)
Title: ثَالِثاً: عَلَامَاتُ التَّوْضِيحِ وَالنَّقْلِ
Content:
(Insert TEMPLATE_C_LIST.html here)
List Items:
- <strong>النُّقْطَتَانِ ( : ) :</strong> بَعْدَ الْقَوْلِ (قَالَ، أَجَابَ، رَدَّ). وَقَبْلَ التَّعْدَادِ وَالتَّفْصِيلِ (فُصُولُ السَّنَةِ أَرْبَعَةٌ: الرَّبِيعُ، وَالصَّيْفُ، وَالْخَرِيفُ، وَالشِّتَاءُ).
- <strong>النِّقَاطُ المُتَعَدِّدَةُ ( ... ) :</strong> (عَادَةً ٣ نِقَاطٍ) لِلدَّلَالَةِ عَلَى كَلَامٍ مَحْذُوفٍ أَوْ بَقِيَّةٍ لَمْ نُكْمِلْهَا.
- <strong>عَلَامَةُ التَّنْصِيصِ ( « » ) :</strong> لِحَصْرِ كَلَامٍ مَنْقُولٍ بِالْحَرْفِ (كَمَا هُوَ دُونَ تَغْيِيرٍ) مِثْلَ الْأَقْوَالِ الْمَأْثُورَةِ أَوْ كَلَامِ الْعُلَمَاءِ. قَالَ الْحَكِيمُ: «الْوَقْتُ ثَمِينٌ».
- <strong>الشَّرْطَتَانِ / الِاعْتِرَاضِ ( - - ) :</strong> لِحَصْرِ جُمْلَةٍ اعْتِرَاضِيَّةٍ (لَوْ حَذَفْنَاهَا لَا يَتَغَيَّرُ الْمَعْنَى)، كَالدُّعَاءِ وَالتَّوْضِيحِ. (أَخِي - سَلَّمَهُ الزَّمَانُ - مُخْلِصٌ).

=== BLOCK 7: تَنْبِيهٌ هَامٌّ ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Text: <strong>تَنْبِيهٌ:</strong> يَجِبُ الِانْتِبَاهُ إِلَى عَلَامَاتِ التَّرْقِيمِ؛ لِأَنَّهَا تُوضَحُ مَعْنَى الْكَلَامِ بِدُونِ اخْتِلَاطٍ كَمَا فِي الْجُمَلِ الِاعْتِرَاضِيَّةِ أَوِ التَّعَجُّبِ.

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: ضَعْ عَلَامَةَ التَّرْقِيمِ الْمُنَاسِبَةَ: نَجَحَ الطَّالِبُ لِأَنَّهُ سَهِرَ اللَّيَالِيَ
Number: ٢
Question: ضَعْ عَلَامَةَ التَّرْقِيمِ الْمُنَاسِبَةَ: مَا اسْمُكَ
Number: ٣
Question: ضَعْ عَلَامَةَ التَّرْقِيمِ الْمُنَاسِبَةَ: قَالَ الْحَكِيمُ الْوَقْتُ ثَمِينٌ
Number: ٤
Question: ضَعْ عَلَامَةَ التَّرْقِيمِ الْمُنَاسِبَةَ: مَا أَجْمَلَ السَّمَاءَ

--- END STREAM ---