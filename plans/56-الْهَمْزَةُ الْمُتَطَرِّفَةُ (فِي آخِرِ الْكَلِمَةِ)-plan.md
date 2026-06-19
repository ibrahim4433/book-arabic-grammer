# **SESSION 56.0**

[TASK DEFINITION]
Objective: Implement الْهَمْزَةُ الْمُتَطَرِّفَةُ (فِي آخِرِ الْكَلِمَةِ).
File: `pages/56.0_nXX_الْهَمْزَةُ الْمُتَطَرِّفَةُ (فِي آخِرِ الْكَلِمَةِ).html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/56.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 56
[CHAPTER_TITLE]: الْهَمْزَةُ الْمُتَطَرِّفَةُ (فِي آخِرِ الْكَلِمَةِ)
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم الإملاء
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition and Rule ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَعْرِيفُ الْهَمْزَةِ الْمُتَطَرِّفَةِ وَقَاعِدَتُهَا
Content:
<p class="mt-1mm text-accent">الْهَمْزَةُ الْمُتَطَرِّفَةُ: هِيَ الَّتِي تُكْتَبُ فِي آخِرِ الْكَلِمَةِ تَمَاماً (مِثْل: قَرَأَ، لُؤْلُؤ، شَاطِئ، شَيْء).</p>
<p class="mt-1mm">الْقَاعِدَةُ: أَسْهَلُ مِنَ الْمُتَوَسِّطَةِ. هُنَا (لَا نُقَارِنُ أَبَداً) وَ (لَا نَهْتَمُّ لِحَرَكَةِ الْهَمْزَةِ). نَنْظُرُ فَقَطْ وَفَقَطْ إِلَى حَرَكَةِ الْحَرْفِ الَّذِي قَبْلَ الْهَمْزَةِ.</p>

=== BLOCK 3: The Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Title: مَوَاضِعُ كِتَابَةِ الْهَمْزَةِ الْمُتَطَرِّفَةِ
Columns:
- حَرَكَةُ الْحَرْفِ الَّذِي قَبْلَهَا
- تُكْتَبُ عَلَى
- أَمْثِلَةٌ
Rows:
1. مَا قَبْلَهَا مَكْسُوراً | يَاءٍ (ـئ / ئ) | شَاطِئ، يُومِئ، يُكَافِئ، هَادِئ، قَارِئ
2. مَا قَبْلَهَا مَضْمُوماً | وَاوٍ (ـؤ / ؤ) | تَبَاطُؤ، تَكـَافُؤ، لُؤْلُؤ، يَجْرُؤ، تَبَوُّؤ
3. مَا قَبْلَهَا مَفْتُوحاً | أَلِفٍ (ـأ / أ) | قَرَأَ، الْمَبْدَأ، نَشَأَ، يَلْجَأ، مَلْجَأ
4. مَا قَبْلَهَا سَاكِناً (أَوْ حَرْفَ مَدٍّ) | السَّطْرِ (ء) | دِفْء، عِبْء، شَيْء، بُطْء، دَوَاء، هُدُوء، بَرِيء

=== BLOCK 4: Detailed Rules Part 1 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَفْصِيلُ مَوَاضِعِ كِتَابَةِ الْهَمْزَةِ الْمُتَطَرِّفَةِ
Content:
(Component: TEMPLATE_C_LIST.html inside body)
- إِذَا كَانَ مَا قَبْلَهَا مَكْسُوراً: تُكْتَبُ عَلَى يَاءٍ (ـئ / ئ). مِثْل: <span class="highlight-red">شَاطِئ</span> (الطَّاءُ مَكْسُورَةٌ)، <span class="highlight-red">يُومِئ</span>، <span class="highlight-red">يُكَافِئ</span>، <span class="highlight-red">هَادِئ</span>، <span class="highlight-red">قَارِئ</span>.
- إِذَا كَانَ مَا قَبْلَهَا مَضْمُوماً: تُكْتَبُ عَلَى وَاوٍ (ـؤ / ؤ). مِثْل: <span class="highlight-red">تَبَاطُؤ</span> (الطَّاءُ مَضْمُومَةٌ)، <span class="highlight-red">تَكـَافُؤ</span>، <span class="highlight-red">لُؤْلُؤ</span>، <span class="highlight-red">يَجْرُؤ</span>، <span class="highlight-red">تَبَوُّؤ</span>.
- إِذَا كَانَ مَا قَبْلَهَا مَفْتُوحاً: تُكْتَبُ عَلَى أَلِفٍ (ـأ / أ). مِثْل: <span class="highlight-red">قَرَأَ</span> (الرَّاءُ مَفْتُوحَةٌ)، <span class="highlight-red">الْمَبْدَأ</span>، <span class="highlight-red">نَشَأَ</span>، <span class="highlight-red">يَلْجَأ</span>، <span class="highlight-red">مَلْجَأ</span>.
- إِذَا كَانَ مَا قَبْلَهَا سَاكِناً (أَوْ حَرْفَ مَدٍّ لِأَنَّ الْمَدَّ سَاكِنٌ): تُكْتَبُ عَلَى السَّطْرِ (ء). مِثْل: <span class="highlight-red">دِفْء</span> (الْفَاءُ سَاكِنَةٌ)، <span class="highlight-red">عِبْء</span>، <span class="highlight-red">شَيْء</span>، <span class="highlight-red">بُطْء</span>، <span class="highlight-red">دَوَاء</span>، <span class="highlight-red">هُدُوء</span>، <span class="highlight-red">بَرِيء</span>.

=== BLOCK 5: Special Note on Shay ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Content: <strong>مُلَاحَظَةٌ:</strong> لَاحِظْ كَلِمَةَ <span class="highlight-red">شَيْء</span>: تُكْتَبُ الْهَمْزَةُ بَعْدَ الْيَاءِ عَلَى السَّطْرِ.

=== BLOCK 6: Important Warnings - Tanween ===
(Component: TEMPLATE_C_BLOCK.html with .block-header.accent for orange theme balance)
Title: تَنْبِيهَاتٌ هَامَّةٌ جِدَّاً: اجْتِمَاعُ الْهَمْزَةِ الْمُتَطَرِّفَةِ مَعَ إِضَافَاتٍ (١)
Content:
<p class="mt-1mm font-bold">١- الْهَمْزَةُ الْمُتَطَرِّفَةُ مَعَ تَنْوِينِ النَّصْبِ (فَتْحَتَيْنِ ً):</p>
(Component: TEMPLATE_C_LIST.html inside body)
- إِذَا كَانَتْ مَسْبُوقَةً بِأَلِفٍ: نَضَعُ التَّنْوِينَ فَوْقَ الْهَمْزَةِ (<span class="highlight-blue">سَمَاءً</span>، <span class="highlight-blue">نِدَاءً</span>، <span class="highlight-blue">مَاءً</span>). (لَا نَكْتُبُ سَمَاءاً!).
- إِذَا كَانَتْ مَكْتُوبَةً عَلَى أَلِفٍ: نَضَعُ التَّنْوِينَ فَوْقَهَا مُبَاشَرَةً (<span class="highlight-blue">مَبْدَأً</span>، <span class="highlight-blue">مَنْشَأً</span>، <span class="highlight-blue">خَطَأً</span>).
- إِذَا لَمْ تُسْبَقْ بِأَلِفٍ وَكَانَتْ عَلَى السَّطْرِ، إِنْ كَانَ الْحَرْفُ الَّذِي قَبْلَهَا لَا يَتَّصِلُ (د، ذ، ر، ز، و): تُبْقَى عَلَى السَّطْرِ وَنَضَعُ أَلِفَ تَنْوِينٍ (<span class="highlight-blue">جُزْءاً</span>، <span class="highlight-blue">بَدْءاً</span>، <span class="highlight-blue">ضَوْءاً</span>).
- إِذَا لَمْ تُسْبَقْ بِأَلِفٍ وَكَانَتْ عَلَى السَّطْرِ، إِنْ كَانَ الْحَرْفُ يَتَّصِلُ (ب، ت، ش، ي...): نَكْتُبُهَا عَلَى نَبْرَةٍ لِنَصِلَهَا بِأَلِفِ التَّنْوِينِ (<span class="highlight-blue">شَيْئاً</span>، <span class="highlight-blue">عِبْئاً</span>، <span class="highlight-blue">بُطْئاً</span>).

=== BLOCK 7: Important Warnings - Alif Ithnayn ===
(Component: TEMPLATE_C_BLOCK.html with .block-header.accent)
Title: تَنْبِيهَاتٌ هَامَّةٌ جِدَّاً: اجْتِمَاعُ الْهَمْزَةِ الْمُتَطَرِّفَةِ مَعَ إِضَافَاتٍ (٢)
Content:
<p class="mt-1mm font-bold">٢- الْهَمْزَةُ الْمُتَطَرِّفَةُ مَعَ أَلِفِ الِاثْنَيْنِ (ـَانِ):</p>
(Component: TEMPLATE_C_LIST.html inside body)
- <span class="highlight-blue">جُزْءَانِ</span> : تَبْقَى عَلَى السَّطْرِ لِأَنَّ الزَّايَ لَا تَتَّصِلُ.
- <span class="highlight-blue">شَيْئَانِ</span> : تُكْتَبُ عَلَى نَبْرَةٍ لِأَنَّ الْيَاءَ تَتَّصِلُ.
- <span class="highlight-blue">بَدَأَا</span>، <span class="highlight-blue">يَقْرَأَانِ</span> : تُكْتَبُ أَلِفَانِ مُتَتَالِيَتَانِ (الْأُولَى عَلَيْهَا هَمْزَةٌ وَالثَّانِيَةُ مَدٌّ) فِي الْأَفْعَالِ. أَمَّا فِي الْأَسْمَاءِ مِثْلَ "<span class="highlight-blue">مَبْدَآنِ</span>" فَتُدْغَمُ أَلِفاً مَمْدُودَةً (آ).

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: اكْتُبِ الْكَلِمَاتِ التَّالِيَةَ كِتَابَةً صَحِيحَةً مَعَ تَنْوِينِ النَّصْبِ: (جُزْء، شَيْء، سَمَاء، مَبْدَأ).
Number: ٢
Question: بَيِّنْ سَبَبَ كِتَابَةِ الْهَمْزَةِ عَلَى هَذِهِ الصُّورَةِ فِي الْكَلِمَاتِ التَّالِيَةِ: (شَاطِئ، لُؤْلُؤ، قَرَأَ، عِبْء).

--- END STREAM ---
