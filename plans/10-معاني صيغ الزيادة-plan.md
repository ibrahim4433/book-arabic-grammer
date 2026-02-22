# **SESSION 10.0**

[TASK DEFINITION]
Objective: Implement معاني صيغ الزيادة.
File: `pages/10.0_nXX_معاني صيغ الزيادة.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK\_RULES.md and elements\_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/10.1_...`.
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
6. Templates: You are forbidden from inventing new HTML tags or classes or template elements. You must map all content strictly using "Jules-workspace/Templates/" components as the STREAM says.
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). use "Jules-workspace/id_manager.py" to generate or verify them.
8. **Self-Correction:** Run "Jules-workspace/lint_pages.py" after creating html files. If it fails, you MUST fix the errors (usually inline styles) before submitting.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...) .
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed.
12. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of teal , also use this tool to verify "Jules-workspace/smart_color_fixer.py"
14. DO Create a temporary Python generation script to help you generate the lesson html pages in the perfect way needed without problems !

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER)
[LESSON_NUMBER]: 10
[CHAPTER_TITLE]: معاني صيغ الزيادة
[CATEGORY_HEADER]: الصرف
[SECTION_HEADER]: المستوى اللغوي
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: [Concept of Augmentation] ===
(Component: TEMPLATE_C_BLOCK)
Title: مَفْهُومُ الزِّيَادَةِ فِي الأَفْعَالِ
Content: <p class="text-accent text-justify">تَتَغَيَّرُ دَلَالَةُ الفِعْلِ (مَعْنَاهُ) بِحَسَبِ مَا يُزَادُ عَلَى الثُّلَاثِيِّ مِنْ حُرُوفِ الزِّيَادَةِ، وَهَذِهِ المَعَانِي الجَدِيدَةُ لَمْ تَكُنْ لِلْفِعْلِ قَبْلَ زِيَادَةِ الأَحْرُفِ عَلَى أَصْلِهِ الثُّلَاثِيِّ. فَكُلَّمَا زَادَ المَبْنَى، زَادَ المَعْنَى.</p>

=== BLOCK 3: [Core Meanings Matrix] ===
(Component: TEMPLATE_C_TABLE)
Title: أَهَمُّ المَعَانِي المُسْتَفَادَةِ مِنْ صِيَغِ الزِّيَادَةِ
Columns: الصِّيغَةُ الصَّرْفِيَّةُ | المَعَانِي الَّتِي تُفِيدُهَا | أَمْثِلَةٌ تَطْبِيقِيَّةٌ
Row 1: أَفْعَلَ | التَّحَوُّلُ، الدُّخُولُ فِي الزَّمَانِ، التَّعْدِيَةُ | <span class="highlight-red">أَجْلَسَ</span>، <span class="highlight-blue">أَصْبَحَ</span>، <span class="highlight-green">أَفْطَرَ</span>
Row 2: افْعَلَّ | المُبَالَغَةُ (فِي الْأَلْوَانِ وَالْعُيُوبِ) | <span class="highlight-red">احْمَرَّ</span> الوَجْهُ، <span class="highlight-blue">اخْضَرَّ</span> الزَّرْعُ
Row 3: اسْتَفْعَلَ | الطَّلَبُ وَالسُّؤَالُ، التَّحَوُّلُ | <span class="highlight-red">اسْتَوْقَفَ</span>، <span class="highlight-blue">اسْتَحْجَرَ</span> الطِّينُ
Row 4: انْفَعَلَ | المُطَاوَعَةُ (لِفِعْلٍ ثُلَاثِيٍّ) | <span class="highlight-red">انْكَسَرَ</span> الزُّجَاجُ، <span class="highlight-blue">انْطَلَقَ</span>
Row 5: افْتَعَلَ | المُطَاوَعَةُ، الِاتِّخَادُ، المُشَارَكَةُ | <span class="highlight-red">اقْتَرَبَ</span>، <span class="highlight-blue">اخْتَصَمَ</span> الخَصْمَانِ
Row 6: تَفَعَّلَ | التَّكَلُّفُ، التَّدَرُّجُ، المُطَاوَعَةُ | <span class="highlight-red">تَشَجَّعَ</span>، <span class="highlight-blue">تَجَرَّعَ</span>، <span class="highlight-green">تَكَسَّرَ</span>
Row 7: تَفَاعَلَ | المُشَارَكَةُ، التَّظَاهُرُ | <span class="highlight-red">تَعَاوَنَ</span> القَوْمُ، <span class="highlight-blue">تَغَافَلَ</span>، <span class="highlight-green">تَمَارَضَ</span>
Row 8: فَعَّلَ | التَّكْثِيرُ، التَّعْدِيَةُ | <span class="highlight-red">كَسَّرَ</span>، <span class="highlight-blue">غَلَّقَ</span> الأَبْوَابَ
Row 9: فَاعَلَ | المُشَارَكَةُ بَيْنَ اثْنَيْنِ | <span class="highlight-red">قَاتَلَ</span>، <span class="highlight-blue">شَارَكَ</span>، <span class="highlight-green">جَادَلَ</span>
Row 10: تَفَعْلَلَ | المُطَاوَعَةُ (لِلرُّبَاعِيِّ) | <span class="highlight-red">تَدَحْرَجَ</span> الحَجَرُ

=== BLOCK 4: [Deep Dive: Mutawa'ah vs Participation] ===
(Component: TEMPLATE_C_SPLIT)
[LEFT_TITLE]: صِيَغُ المُطَاوَعَةِ
[LEFT_CONTENT]:
(Component: TEMPLATE_C_LIST)
List Items:
*   **انْفَعَلَ**: يُفِيدُ قَبُولَ أَثَرِ الفِعْلِ. مِثْلُ: كَسَرْتُهُ <span class="highlight-red">فَانْكَسَرَ</span>.
*   **افْتَعَلَ**: يُفِيدُ المُطَاوَعَةَ أَيْضاً. مِثْلُ: جَمَعْتُهُ <span class="highlight-red">فَاجْتَمَعَ</span>.
*   **تَفَعَّلَ**: مُطَاوَعَةُ (فَعَّلَ). مِثْلُ: كَسَّرْتُهُ <span class="highlight-red">فَتَكَسَّرَ</span>.
[RIGHT_TITLE]: صِيَغُ المُشَارَكَةِ
[RIGHT_CONTENT]:
(Component: TEMPLATE_C_LIST)
List Items:
*   **فَاعَلَ**: مُشَارَكَةٌ بَيْنَ طَرَفَيْنِ غَالِباً. مِثْلُ: <span class="highlight-blue">قَاتَلَ</span> الجَيْشُ العَدُوَّ.
*   **تَفَاعَلَ**: مُشَارَكَةٌ بَيْنَ أَكْثَرَ مِنْ طَرَفٍ، أَوْ تُفِيدُ التَّظَاهُرَ. مِثْلُ: <span class="highlight-blue">تَعَاوَنَ</span> المُوَاطِنُونَ.
*   **افْتَعَلَ**: قَدْ تَأْتِي لِلْمُشَارَكَةِ. مِثْلُ: <span class="highlight-blue">اخْتَصَمَ</span> الزَّيْدَانِ.

=== BLOCK 5: [Golden Rule Benefit] ===
(Component: TEMPLATE_C_BENEFIT)
Title: قَاعِدَةٌ ذَهَبِيَّةٌ
Content: <p class="text-center font-bold">كُلُّ زِيَادَةٍ فِي المَبْنَى تُؤَدِّي بِالضَّرُورَةِ إِلَى زِيَادَةٍ فِي المَعْنَى.</p><p class="text-justify">فَالفِعْلُ (غَفَرَ) يَدُلُّ عَلَى مُجَرَّدِ الغُفْرَانِ، بَيْنَمَا (اسْتَغْفَرَ) يَدُلُّ عَلَى طَلَبِ ذَلِكَ الغُفْرَانِ وَالسَّعْيِ إِلَيْهِ.</p>

=== BLOCK 6: [Evidence & Analysis] ===
(Component: TEMPLATE_C_POEM)
Poem Line 1: وَبِالزِّيَادَةِ المَعَانِي تَكْثُرُ ... كَمِثْلِ (اسْتَفْهَمَ) أَيْ يَسْتَفْسِرُ
Bio Name: قَاعِدَةٌ نَحْوِيَّةٌ
(Component: TEMPLATE_C_IRAB_ROW)
Word 1: اسْتَغْفَرَ
Details 1: فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الفَتْحِ، وَالزِّيَادَةُ (السين والتاء) تُفِيدُ الطَّلَبَ.
Word 2: المُؤْمِنُ
Details 2: فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ.

=== BLOCK 7: [Evaluation] ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: اسْتَخْرِجِ الفِعْلَ المَزِيدَ وَبَيِّنْ مَعْنَى الزِّيَادَةِ فِي الجُمْلَةِ: "اسْتَمْطَرَ النَّاسُ رَبَّهُمْ".
Number: ٢
Question: صُغْ فِعْلاً عَلَى وَزْنِ (تَفَاعَلَ) مِنَ الفِعْلِ (غَفَلَ) وَضَعْهُ فِي جُمْلَةٍ مُفِيدَةٍ.
Number: ٣
Question: مَيِّزْ بَيْنَ مَعْنَى (قَطَعَ) وَ (قَطَّعَ) فِي جُمْلَتَيْنِ مِنْ إِنْشَائِكَ.

--- END STREAM ---
