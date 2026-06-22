# **SESSION 11.0**

[TASK DEFINITION]
Objective: Implement الضَّمَائِرُ.
File: `pages/11.0_nXX_الضَّمَائِرُ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/11.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 11
[CHAPTER_TITLE]: الضَّمَائِرُ
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: تَعْرِيفُ الضَّمِيرِ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَعْرِيفُ الضَّمِيرِ
Content: <p class="text-accent">الضَّمِيرُ هُوَ: اسْمٌ مَعْرِفَةٌ يَدُلُّ عَلَى مُتَكَلِّمٍ (<span class="highlight-blue">أَنَا</span>، <span class="highlight-blue">نَحْنُ</span>) أَوْ مُخَاطَبٍ (<span class="highlight-blue">أَنْتَ</span>، <span class="highlight-blue">أَنْتِ</span>) أَوْ غَائِبٍ (<span class="highlight-blue">هُوَ</span>، <span class="highlight-blue">هِيَ</span>) لِيَحِلَّ مَحَلَّ الِاسْمِ الظَّاهِرِ لِلِاخْتِصَارِ وَمَنْعِ التَّكْرَارِ.</p>

=== BLOCK 3: مُلَخَّصُ الضَّمَائِرِ بِأَنْوَاعِهَا ===
(Component: TEMPLATE_C_TABLE.html)
Title: مُلَخَّصُ الضَّمَائِرِ بِأَنْوَاعِهَا
Content:
- Headers: النَّوْعُ | حَالَةُ الرَّفْعِ (مُبْتَدَأٌ/فَاعِلٌ) | حَالَةُ النَّصْبِ (مَفْعُولٌ بِهِ) | حَالَةُ الْجَرِّ (مُضَافٌ إِلَيْهِ/اسْمٌ مَجْرُورٌ)
- Row 1: الْمُنْفَصِلُ (الَّذِي يُكْتَبُ وَحْدَهُ كَكَلِمَةٍ مُسْتَقِلَّةٍ) | • أَنَا، نَحْنُ (لِلْمُتَكَلِّمِ). • أَنْتَ، أَنْتِ... (لِلْمُخَاطَبِ). • هُوَ، هِيَ... (لِلْغَائِبِ). (تُعْرَبُ غَالِباً: مُبْتَدَأً). | • إِيَّايَ، إِيَّانَا (لِلْمُتَكَلِّمِ). • إِيَّاكَ، إِيَّاهُ... (لِلْمُخَاطَبِ وَالْغَائِبِ). (تُعْرَبُ مَفْعُولاً بِهِ). | لَا يُوجَدُ ضَمِيرٌ مُنْفَصِلٌ فِي حَالَةِ جَرٍّ أَبَداً.
- Row 2: الْمُتَّصِلُ (الَّذِي يَلْتَصِقُ بِالْكَلِمَةِ كَاللَّاصِقِ) | مَجْمُوعَةٌ فِي كَلِمَةِ (<span class="highlight-red">تَوَانَيْنَا</span>) وَهِيَ لِلرَّفْعِ فَقَطْ: • تَاءُ الْفَاعِلِ. • وَاوُ الْجَمَاعَةِ. • أَلِفُ الِاثْنَيْنِ. • نُونُ النِّسْوَةِ. • يَاءُ الْمُخَاطَبَةِ. • (نَا) الْفَاعِلِينَ. | مَجْمُوعَةٌ فِي كَلِمَةِ (<span class="highlight-blue">نَاهِيكَ</span>): • نَا الْمَفْعُولِينَ. • هَاءُ الْغَائِبِ. • يَاءُ الْمُتَكَلِّمِ. • كَافُ الْخِطَابِ. إِذَا اتَّصَلَتْ بِالْفِعْلِ. | نَفْسُ ضَمَائِرِ (<span class="highlight-blue">نَاهِيكَ</span>): إِذَا اتَّصَلَتْ بِمُضَافٍ (اسْمٍ)، أَوْ مَعَ حَرْفٍ (حَرْفِ جَرٍّ).

=== BLOCK 4: ضَمَائِرُ الرَّفْعِ الْمُنْفَصِلَةُ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ١. ضَمَائِرُ الرَّفْعِ الْمُنْفَصِلَةُ (تُعْرَبُ مُبْتَدَأً)
Content:
تُعْرَبُ غَالِباً: ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعِ مُبْتَدَأٍ.
(Inject TEMPLATE_C_LIST.html here)
List Items:
- لِلْمُتَكَلِّمِ: أَنَا ، نَحْنُ . (أَنَا طَالِبٌ، نَحْنُ نُحِبُّ الْعِلْمَ).
- لِلْمُخَاطَبِ: أَنْتَ ، أَنْتِ ، أَنْتُمَا ، أَنْتُمْ ، أَنْتُنَّ . (أَنْتَ رَجُلٌ، أَنْتُمْ عُلَمَاءُ).
- لِلْغَائِبِ: هُوَ ، هِيَ ، هُمَا ، هُمْ ، هُنَّ . (هُوَ مُعَلِّمٌ، هُنَّ أُمَّهَاتٌ).

=== BLOCK 5: الضَّمَائِرُ الْمُتَّصِلَةُ بِالتَّفْصِيلِ ===
(Component: TEMPLATE_C_SPLIT.html)
Title: ٢. الضَّمَائِرُ الْمُتَّصِلَةُ بِالتَّفْصِيلِ
LeftSide (Component: TEMPLATE_C_BLOCK.html inside split grid):
Title: أَوَّلاً:  مَجْمُوعَةُ (تَوَانِينَا) لِلرَّفْعِ
Content:
تَتَّصِلُ بِالْفِعْلِ فَقَطْ وَتُعْرَبُ (فِي مَحَلِّ رَفْعِ فَاعِلٍ):
(Inject TEMPLATE_C_LIST.html here)
List Items:
- تَاءُ الْفَاعِلِ الْمُتَحَرِّكَةِ: (سَمِعْتُ، سَمِعْتَ، سَمِعْتِ).
- وَاوُ الْجَمَاعَةِ: (سَمِعُوا، يَسْمَعُونَ).
- أَلِفُ الِاثْنَيْنِ: (يَسْمَعَانِ، سَمِعَا).
- نُونُ النِّسْوَةِ: (سَمِعْنَ، يَسْمَعْنَ).
- يَاءُ الْمُؤَنَّثَةِ الْمُخَاطَبَةِ: (تَسْمَعِينَ، اسْمَعِي).
- نَا الْفَاعِلِينَ: (سَمِعْنَا)، نَحْنُ مَنْ قَامَ بِالسَّمَاعِ.
(Inject TEMPLATE_C_BENEFIT_WARNING.html here)
Content: ⚠️ تَنْبِيهٌ: يَاءُ الْمُؤَنَّثَةِ الْمُخَاطَبَةِ لَا تَتَّصِلُ بِالْفِعْلِ الْمَاضِي أَبَداً (لَا يُقَالُ: سَمِعْتِي بَلْ سَمِعْتِ بِكَسْرَةٍ).

RightSide (Component: TEMPLATE_C_BLOCK.html inside split grid):
Title: ثَانِياً: 🅱️ مَجْمُوعَةُ (نَاهِيكَ) لِلنَّصْبِ وَالْجَرِّ
Content:
وَهِيَ: نَا الْمَفْعُولِينَ، هَاءُ الْغَائِبِ، يَاءُ الْمُتَكَلِّمِ، كَافُ الْخِطَابِ.
(مِثْل: أَعْطَانَا، كِتَابُهُ، قَلَمِي، أُحِبُّكَ).

=== BLOCK 6: نَمُوذَجُ إِعْرَابٍ هَامٌّ ===
(Component: TEMPLATE_C_BLOCK.html)
Title:  نَمُوذَجُ إِعْرَابٍ هَامٌّ (تَمْيِيزُ "نَا" الْفَاعِلِينَ عَنْ "نَا" الْمَفْعُولِينَ)
Content:
كَثِيرٌ مِنَ الطُّلَّابِ يَخْلِطُونَ بَيْنَ (نَا) الَّتِي تَكُونُ فَاعِلاً، وَ(نَا) الَّتِي تَكُونُ مَفْعُولاً بِهِ. الْفَرْقُ بَسِيطٌ فِي نُطْقِ الْفِعْلِ قَبْلَهَا:
(Inject TEMPLATE_C_LIST.html here)
List Items:
- <span class="highlight-blue">أَكْرَمَنَا</span>: أَكْرَمَنَا (الضَّيْفُ الْمَرْفُوعُ). الْفَتْحَةُ عَلَى الْمِيمِ تَعْنِي أَنَّنَا وَقَعَ عَلَيْنَا الْكَرَمُ وَلَمْ نُكْرِمْ أَحَداً.
- <span class="highlight-blue">أَكْرَمْنَا</span>: أَكْرَمْنَا (الضَّيْفَ الْمَنْصُوبَ). السُّكُونُ عَلَى الْمِيمِ تَعْنِي أَنَّنَا نَحْنُ مَنْ قُمْنَا بِالْكَرَمِ.

(Inject TEMPLATE_C_IRAB_ROW.html here)
Row:
Box 1 (Component: TEMPLATE_C_IRAB_BOX.html):
Word: أَكْرَمَنَا
Details: فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ الظَّاهِرِ، وَ(نَا) ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبِ مَفْعُولٍ بِهِ مُقَدَّمٍ. (الضَّيْفُ هُوَ الْفَاعِلُ).
Box 2 (Component: TEMPLATE_C_IRAB_BOX.html):
Word: أَكْرَمْنَا
Details: فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا الْفَاعِلِينَ، وَ(نَا) ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعِ فَاعِلٍ. (الضَّيْفَ هُوَ الْمَفْعُولُ بِهِ).

=== BLOCK 7: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: اِسْتَخْرِجِ الضَّمَائِرَ مِنَ الْجُمَلِ التَّالِيَةِ وَحَدِّدْ نَوْعَهَا (مُنْفَصِلٌ / مُتَّصِلٌ):
١. هُوَ يَقْرَأُ كِتَابَهُ كُلَّ يَوْمٍ.
٢. أَنْتُمْ سَمِعْتُمُ النَّصِيحَةَ.
٣. إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ.

--- END STREAM ---