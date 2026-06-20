# **SESSION 08.0**

[TASK DEFINITION]
Objective: Implement حُروفُ الْجَرِّ وَعَلَاَّمَاتِ الْإِعْرَابِ الْمَجْرُورَةِ.
File: `pages/08.0_nXX_حُروفُ الْجَرِّ وَعَلَاَّمَاتِ الْإِعْرَابِ الْمَجْرُورَةِ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/08.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 08
[CHAPTER_TITLE]: حُروفُ الْجَرِّ وَعَلَاَّمَاتِ الْإِعْرَابِ الْمَجْرُورَةِ
[CATEGORY_HEADER]:
[SECTION_HEADER]:
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition and Rule (مُقَدَّمَةً) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مُقَدَّمَةً
Content:
<p class="text-accent text-center mb-2mm">"الْجَرَّ" هُو حَالَةٍ إِعْرَابِيَّةٍ خَاصَّةً بـ <span class="font-bold">الْأَسْمَاءَ فَقَط</span>؛ فلَا يُوجَدُ فعَلّ مَجْرُورٍ ولَا حَرْفِ مَجْرُورِ.</p>
<p class="text-center">مِن أَشْهُرِ مُسَبِّبَاتِ الْجَرِّ فِي اللُّغَةَ الْعَرَبِيَّةَ أَن يُسَبِّقُ الْاِسْمُ بـ (حَرْفَ جَرِّ).</p>

=== BLOCK 3: Core Matrix Summary Table ===
(Component: TEMPLATE_C_TABLE.html)
Table Content:
Row 1 (Header): [عَلَاَّمَةُ الْجَرِّ, نَوْعُهَا, الْمَوَاضِعُ]
Row 2: [الْكَسْرَةَ, أَصْلِيَّةٌ, الْمُفْرَدُ - جَمَعَ التَّكْسيرُ - جَمَعَ الْمُؤَنَّثُ السَّالِمُ]
Row 3: [الياء, فَرْعِيَّةٌ, الْمُثَنَّى - جَمَعَ الْمُذَكَّرُ السَّالِمُ - الْأَسْمَاءُ الْخُمُسَةَ]

=== BLOCK 4: Deep Dive - Letters of Jar ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مَا هِي حُروفِ الْجَرِّ ؟
Content:
<p class="mb-2mm">حُروفُ الْجَرِّ سَهْلَةَ الْحِفْظِ ، وهِي:</p>
(Inject TEMPLATE_C_CHIPS.html)
Chips: مِنْ, عَنْ, إِِْلََى, عَلَى, فِِي, الْكَافَّ, اللَّاَمَ, الْبَاءَ
<p class="mt-2mm mb-2mm">لِتَبْسِيطُ حِفْظِهَا ، قُسِّمَتْ إِلَى:</p>

=== BLOCK 5: Split Grid for Letters of Jar ===
(Component: TEMPLATE_C_SPLIT.html)
Right Side:
(Inject TEMPLATE_C_BLOCK.html)
Title: حُروفَ مُنْفَصِلَةَ (تُكْتِبُ وَحْدُهَا)
Content:
(Inject TEMPLATE_C_CHIPS.html)
Chips: مِنْ, عَنْ, إِِْلََى, عَلَى, فِِي

Left Side:
(Inject TEMPLATE_C_BLOCK.html)
Title: حُروفَ مُتَّصِلَةَ (تَتَّصِلُ بِالْاِسْمِ مُبَاشِرَةَ)
Content:
(Inject TEMPLATE_C_CHIPS.html)
Chips: الْكَافَّ, اللَّاَمَ, الْبَاءَ

=== BLOCK 6: Benefit Warning ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: مُلَاحِظَةَ هَامَةٍ
Content: اِحْذَرْ أَن تَظُنُّ أَنّ "الواو" أَو "الْفَاءَ" مِن حُروفِ الْجَرِّ ، فهِي غَالِبَا حُروفِ عَطْفِ.

=== BLOCK 7: Deep Dive - Signs of Jar (Introduction) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: عَلَاَّمَاتُ الْجَرِّ
Content:
<p class="mb-2mm">عِنْدَمَا يَأْتِي اِسْمُ بَعْد حَرْفِ الْجَرِّ ، يُعْرِبُ دَائِمَا: <span class="font-bold text-accent">(اِسْمُ مَجْرُورُ وَعُلَّامَةُ جَرِّهِ ...)</span>.</p>
<p>لُكْنٌ مَا هِي عُلَّامَةِ الْجَرِّ الْمُنَاسِبَةِ ؟ لَدَيْنَا عَلَاَّمَتَانِِ أَسَاسِيَّتَانِِ:</p>

=== BLOCK 8: Detailed Section - Kasra ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أ. الْكَسْرَةَ (وهِي الْعُلَّامَةِ الْأَصْلِيَّةِ)
Content:
<p class="mb-2mm">تَأْتِي الْكَسْرَةُ مَع ثَلَاثَةِ أَنْوَاعٍ مِن الْأَسْمَاءِ:</p>
(Inject TEMPLATE_C_LIST.html)
Item 1: <span class="font-bold">الْمُفْرَدُ:</span> وَضَعَ الطَّالِبُ الْكِتَابَ <span class="highlight-blue">عَلَى</span> <span class="highlight-red">الْمَكْتَبِ</span>.
Item 2: <span class="font-bold">جَمَعَ التَّكْسيرُ:</span> يَبْحَثُ الصَّيَّادُ <span class="highlight-blue">عَن</span> <span class="highlight-red">الْأَسْمَاكِ</span>.
Item 3: <span class="font-bold">جَمَعَ الْمُؤَنَّثُ السَّالِمُ:</span> أَخَذْتُ الْأبْحَاثَ <span class="highlight-blue">مِن</span> <span class="highlight-red">الطَّالِبَاتِ</span>.

=== BLOCK 9: Irab for Kasra Examples (Row 1) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
Box 1: [Word: عَلَى الْمَكْتَبِ] [Details: عَلَى: حَرْفُ جَرٍّ. الْمَكْتَبِ: اِسْمُ مَجْرُورُ بِالْكَسْرَةِ.]
Box 2: [Word: عَن الْأَسْمَاكِ] [Details: عَنْ: حَرْفُ جَرٍّ. الْأَسْمَاكِ: اِسْمُ مَجْرُورُ بِالْكَسْرَةِ.]

=== BLOCK 10: Irab for Kasra Examples (Row 2) ===
(Component: TEMPLATE_C_IRAB.html)
Word: مِن الطَّالِبَاتِ
Details: مِنْ: حَرْفُ جَرٍّ. الطَّالِبَاتِ: اِسْمُ مَجْرُورُ بِالْكَسْرَةِ.

=== BLOCK 11: Detailed Section - Yaa ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ب. الياء (وهِي عُلَّامَةٍ فَرْعِيَّةٍ)
Content:
<p class="mb-2mm">تَأْتِي الياء مَع ثَلَاثَةِ أَنْوَاعٍ مِن الْأَسْمَاءِ أيضاً:</p>
(Inject TEMPLATE_C_LIST.html)
Item 1: <span class="font-bold">الْمُثَنَّى:</span> أَلْقَيْتُ مُحَاضَرَاتٍ <span class="highlight-blue">فِي</span> <span class="highlight-red">الْمُدَرِّسَتَيْنِ</span>.
Item 2: <span class="font-bold">جَمَعَ الْمُذَكَّرُ السَّالِمُ:</span> أَعْطَيْتُ الْهَدَايَا <span class="highlight-blue">لِـ</span><span class="highlight-red">لْمُتَمَيِّزِينَ</span>.
Item 3: <span class="font-bold">الْأَسْمَاءُ الْخُمُسَةَ:</span> ذَهَبْتُ <span class="highlight-blue">إِلَى</span> <span class="highlight-red">أَبِيكَ</span> وَأَخِيكَ.

=== BLOCK 12: Irab for Yaa Examples (Row 1) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
Box 1: [Word: فِي الْمُدَرِّسَتَيْنِ] [Details: فِي: حَرْفُ جَرٍّ. الْمَدْرَسَتَيْنِ: مَجْرُورُ بالياء ، وَنَوَّنَهُ مَكْسُورَةُ.]
Box 2: [Word: لِلْمُتَمَيِّزِينَ] [Details: اللَّاَمُ حَرْفَ جَرٍّ ، وَالْمُتَمَيِّزِينَ مَجْرُورَ بالياء ، وَنَوَّنَهُ مَفْتُوحَةُ.]

=== BLOCK 13: Irab for Yaa Examples (Row 2) ===
(Component: TEMPLATE_C_IRAB.html)
Word: إِلَى أَبِيكَ
Details: إِلَى: حَرْفُ جَرٍّ. أَبِيكَ: مَجْرُورُ بالياء لأَنّهُ مِن الْأَسْمَاءِ الْخُمُسَةَ.

=== BLOCK 14: Exam (Part 1) ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: اِسْتَخْرَجَ حَرْفُ الْجَرِّ وَالْاِسْمِ الْمَجْرُورِ وَبَيِّنِ عَلَاَّمَةِ جَرِّهِ وَالسَّبَبِ فِي الْجَمَلِ الْآتِيَةِ : ١. يَبْدُو وَجْهُ الطِّفْلِ كَالْْبَدْرِ . ٢. يَفْخُرُ الْمُعَلِّمُ بِالطَّالِبَيْنِ الْمُتَفَوِّقِينَ . ٣. شَرَحْتُ الدَّرْسَ فِي الْفَصْلَيْنِ .

=== BLOCK 15: Exam (Part 2) ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: صَحَّحَ الْخَطَأُ فِي الْجَمَلِ الْآتِيَةِ : ١. سَلَّمْتُ عَلَى الْمُهَنْدِسُونَ فِي الْمَوْقِعِ . ٢. أَخَذْتُ الْقَلَمَ مِن أَخُوكَ .

--- END STREAM ---
