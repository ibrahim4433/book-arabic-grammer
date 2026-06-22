# **SESSION 07.0**

[TASK DEFINITION]
Objective: Implement أَنْوَاعُ الْجَمَلِ وَكَيْفِيَّةِ التَّمْييزِ بَيْنهَا.
File: `pages/07.0_nXX_أَنْوَاعُ الْجَمَلِ وَكَيْفِيَّةِ التَّمْييزِ بَيْنهَا.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/07.1_...` if page have a lot of blank space add exam elements from the lesson.
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
7. Templates: You are forbidden from inventing new HTML tags or classes or template elements. You must map all content using "Jules-workspace/Templates/" components as the STREAM says in suitable way.
8. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). use "Jules-workspace/id_manager.py" to generate or verify them.
9. **Self-Correction:** Run "Jules-workspace/lint_pages.py" after creating html files. If it fails, you MUST fix the errors (usually inline styles) before submitting.
10. Do not summarize examples.
11. Do not provide uncompleted text content using (...) .
12. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
13. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
14. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal
15. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
16. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 07
[CHAPTER_TITLE]: أَنْوَاعُ الْجَمَلِ وَكَيْفِيَّةِ التَّمْييزِ بَيْنهَا
[CATEGORY_HEADER]:
[SECTION_HEADER]:
[AUTHOR_NAME]: أ. حنا خفيف
[AUTHOR_PHONE]:  

=== BLOCK 2: Introduction ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مُقَدَّمَةً
Content:
<p class="text-accent mb-2mm">الْجُمْلَةُ فِي اللُّغَةَ الْعَرَبِيَّةَ هِي مَجْمُوعَةٍ مِن الْكَلِمَاتِ الَّتِي تُفِيدُ مُعَنَّى تَامًّا.</p>
<p>وَتَنْقَسِمُ الْجَمَلُ فِي لُغَتِنَا إِلَى نَوْعَيْنِ رَئِيِسيَّيْنِ فَقَط لَا ثَالِثٍ لهُمَا: <span class="font-bold highlight-red">الْجُمْلَةُ الِاسْمِيَّة</span>، و<span class="font-bold highlight-blue">الْجُمْلَةَ الْفِعْلِيَّةَ</span>.</p>

=== BLOCK 3: Common Mistake ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: خَطَأٌ شَائِعٌ
Content: الْخَطَأَ الشَّائِعَ لَدَى الطُّلَاَّبِ هُو التَّسَرُّعِ فِي تَحْدِيدِ نَوْعِ الْجُمْلَةِ دُون التَّفْكِيرِ فِي الْكَلِمَةِ الْأوْلَى الَّتِي بَدَأَتْ بِهَا وَمَوْقِعَهَا.

=== BLOCK 4: Nominal Sentence Definition ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ١. الْجُمْلَةُ الِاسْمِيَّة
Content:
<p class="text-accent mb-2mm"><span class="font-bold text-primary">التَّعْرِيفَ:</span> هِي الْجُمْلَةِ الَّتِي تَبْدَأُ بـ (<span class="highlight-red font-bold">اِسْمَ</span>).</p>
<p class="font-bold mb-2mm">أَرْكَانَهَا الْأَسَاسِيَّةَ: تَتُكُّونَ مِن رُكْنَيْنِ لَا يَسْتَغْنِي أحَدُهُمَا عَنِّ الْآخَرِ:</p>
(Inject: TEMPLATE_C_LIST.html)
- **الْمُبْتَدَأُ:** هُو الْاِسْمِ الَّذِي نَبْدَأُ بِه الْكِلَاَمِ (وَيَكْوُنَّ مَرْفُوعًا دَائِمًا).
- **الْخَبَرُ:** هُو الْجُزْءِ الَّذِي يُخْبِرُنَا بِمَعْلُومَةٍ عَن الْمُبْتَدَأِ وَيَتْمِمْ مُعَنَّى الْجُمْلَةِ (وَيَكْوُنَّ مَرْفُوعًا دَائِمًا).

=== BLOCK 5: Nominal Sentence Examples ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَمِثْلَةَ
Content:
<p class="text-center font-bold text-lg mb-2mm">الْعِلْمُ نُورٌ</p>
(Inject: TEMPLATE_C_IRAB_ROW.html)
Word 1: الْعِلْمَ
Role 1: اِسْمٌ فِي بِدَايَةِ الْجُمْلَةِ (مُبْتَدَأَ مَرْفُوعَ بِالضَّمَّةِ).
Word 2: نُورَ
Role 2: أَخْبَرَتْ عَن الْعِلْمِ وَأَتَمَّتْ الْمُعَنَّى (خَبَرَ مَرْفُوعَ بِالضَّمَّةِ).

=== BLOCK 6: Warning Box ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: تَحْذِيرٌ: مَاذَا لَو بَدَأَتْ الْجُمْلَةُ بِحَرْفِ جَرِّ؟
Content:
فِي جُمَلَةٍ مِثْل: (<span class="highlight-blue font-bold">فِِي كِتَابِيَّ</span> صُورٌ). قَد يَظُنُّ الْبَعْضُ أَنّهَا جُمْلَةَ "حَرْفِيَّةَ" لأَنّهَا بَدَأَتْ بِحَرْفِ جَرٍّ.
هَذَا خَطَأٍ! لَا تَوَجُّدِ جُمْلَةِ حَرْفِيَّةِ! إِذَا بَدَأَتْ الْجُمْلَةَ بشِبْه جُمْلَةِ (حَرْفَ جَرٍّ وَاِسْمِ مَجْرُورِ أَو ظَرْفُ)، فهَذَا يَعْنِي أَنّ هُنَاك "تَقْديمًا وَتَأْخِيرًا".
أَصِلُ الْجُمْلَةَ: (صُورٌ فِِي كِتَابِيَّ)، فَتَكَوَّنَ "صُورَ" هِي الْمُبْتَدَأِ (مُبْتَدَأَ مُؤَخَّرَ)، وَتُصَنِّفُ الْجُمْلَةُ عَلَى أَنّهَا جُمْلَةَ اِسْمِيَّةَ.

=== BLOCK 7: Verbal Sentence Definition ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٢. الْجُمْلَةُ الْفِعْلِيَّةُ
Content:
<p class="text-accent mb-2mm"><span class="font-bold text-primary">التَّعْرِيفَ:</span> هِي الْجُمْلَةِ الَّتِي تَبْدَأُ بـ (<span class="highlight-blue font-bold">فعَلّ</span>) (سَوَاءً كَان فِعْلًا مَاضِيًا، أَو مُضَارِعًا، أَو أَمْرَا).</p>
<p class="font-bold mb-2mm">أَرْكَانَهَا الْأَسَاسِيَّةَ:</p>
(Inject: TEMPLATE_C_LIST.html)
- **الْفِعْلُ:** الْحَدَثُ.
- **الْفَاعِلُ:** مَن قَام بِالْحَدَثِ أَو اِتَّصَفَ بِه (وَيَكْوُنَّ مَرْفُوعًا دَائِمًا).
<p class="text-sm mt-2mm">(وقَد تَحْتَاجُ الْجُمْلَةُ إِلَى مَفْعُولٍ بِه إِذَا كَان الْفِعْلُ مُتَعَدِّيًا).</p>

=== BLOCK 8: Verbal Sentence Examples ===
(Component: TEMPLATE_C_SPLIT.html)

-- Element 1 (Right Visual) --
(Component: TEMPLATE_C_BLOCK.html)
Title: أَمِثْلَةَ: نَامَ الطِّفْلُ
Content:
(Inject: TEMPLATE_C_IRAB.html)
Word 1: نَامٍ
Role 1: فعَلّ مَاضٍ.
Word 2: الطِّفْلَ
Role 2: فَاعِلَ مَرْفُوعَ بِالضَّمَّةِ.
<p class="text-sm mt-2mm">(اِكْتَمَلَ الْمُعَنَّى هُنَا لأَنّ الْفِعْلِ "نَامٍ" فعَلّ لَازِمٍ، لَا يَحْتَاجُ لِمَفْعُولٌ بِه).</p>

-- Element 2 (Left Visual) --
(Component: TEMPLATE_C_BLOCK.html)
Title: أَمِثْلَةَ: كَتَبَ التِّلْميذُ الدَّرْسَ
Content:
(Inject: TEMPLATE_C_IRAB.html)
Word 1: كَتَبَ
Role 1: فعَلّ مَاضٍ.
Word 2: التِّلْميذَ
Role 2: فَاعِلَ مَرْفُوعَ بِالضَّمَّةِ.
Word 3: الدَّرْسَ
Role 3: مَفْعُولٌ بِه مَنْصُوبٍ بِالْفَتْحَةِ.
<p class="text-sm mt-2mm">(اِحْتَاجَتْ الْجُمْلَةُ إِلَى مَفْعُولٍ بِه لِيَكْتَمِلُ الْمُعَنَّى لأَنّ الْفِعْلِ "كَتَبَ" فعَلّ مُتَعَدٍّ).</p>

=== BLOCK 9: The Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Title: مُلَخَّصُ أَنْوَاعِ الْجَمَلِ
Headers: نَوْعُ الْجُمْلَةِ | تَبْدَأُ بـ | أَرْكَانُهَا الْأَسَاسِيَّةُ | مِثَالٌ
Row 1: اِسْمِيَّة | اِسْم | الْمُبْتَدَأُ + الْخَبَرُ | الْعِلْمُ نُورٌ
Row 2: فِعْلِيَّة | فِعْل | الْفِعْلُ + الْفَاعِلُ | نَامَ الطِّفْلُ

=== BLOCK 10: Exam 1 ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: حَدَّدَ نَوْعُ الْجُمْلَةِ (اِسْمِيَّةً أَم فِعْلِيَّةُ) فِي الْأَمْثَلَةِ التَّالِيَةِ، مَع ذِكْرِ السَّبَبِ:
١. فَوَائِدُ الْعِلْمِ كَثِيرَةٌ.
٢. أَبُّوكَ رَجُلٌ كَرِيمٌ.
٣. اِحْتَرِمْ وَالِدَيْكَ.
٤. اِلْتَهَمَ الْجَائِعُ الطَّعَامَ.

=== BLOCK 11: Exam 2 ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: عَيَّنَ أَرْكَانُ الْجُمْلَةِ (الْمُبْتَدَأِ وَالْخَبَرِ أَو الْفِعْلَ وَالْفَاعِلَ) فِي الْجَمَلِ التَّالِيَةِ:
١. أَبُوكَ رَجُلٌ كَرِيمٌ. (تَلْميحٌ: الْخَبَرُ هُو الَّذِي أَتَمَّ الْمُعَنَّى ولَيْس كَلِمَةِ كَرِيمِ الَّتِي هِي صَفَّةٍ).
٢. اِحْتَرِمْ وَالِدِيَّكَ. (تَلْميحٌ: أَيْن مَن سَيَقُومُ بِالْاِحْتِرَامِ؟)

=== BLOCK 12: Exam 3 ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٣
Question: أَعْرَبَ الْجُمْلَةُ التَّالِيَةُ إِعْرَابًا تَامًّا: (كَتَبَ التِّلْميذُ الدَّرْسَ)
١. كَتَبٍّ:
٢. التِّلْميذَ:
٣. الدَّرْسَ:

--- END STREAM ---