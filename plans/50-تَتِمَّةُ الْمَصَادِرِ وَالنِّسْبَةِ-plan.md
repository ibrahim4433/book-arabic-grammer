# **SESSION 50.0**

[TASK DEFINITION]
Objective: Implement تَتِمَّةُ الْمَصَادِرِ وَالنِّسْبَةِ.
File: `pages/50.0_nXX_تَتِمَّةُ الْمَصَادِرِ وَالنِّسْبَةِ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/50.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 50
[CHAPTER_TITLE]: تَتِمَّةُ الْمَصَادِرِ وَالنِّسْبَةِ
[CATEGORY_HEADER]: المستوى المتوسط
[SECTION_HEADER]: علم الصرف
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition & Rule - إِعْرَابُ المَصَادِرِ المُؤَوَّلَةِ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: إِعْرَابُ المَصَادِرِ المُؤَوَّلَةِ
Content:
<p class="text-accent">الْمَصْدَرُ الْمُؤَوَّلُ يُعْرَبُ حَسَبَ مَوْقِعِهِ فِي الْجُمْلَةِ كَأَنَّهُ كَلِمَةٌ وَاحِدَةٌ مُفْرَدَةٌ. لِمَعْرِفَةِ إِعْرَابِهِ بِسُهُولَةٍ، حَوِّلْهُ إِلَى مَصْدَرٍ صَرِيحٍ فِي عَقْلِكَ.</p>

=== BLOCK 3: The Core Matrix - أَمْثِلَةٌ ===
(Component: TEMPLATE_C_TABLE.html)
Title: أَمْثِلَةٌ:
Headers:
[HEADER_1]: مَوْقِعُهُ فِي الْإِعْرَابِ
[HEADER_2]: الْمِثَالُ (الْمَصْدَرُ الْمُؤَوَّلُ)
[HEADER_3]: التَّحْوِيلُ (الْمَصْدَرُ الصَّرِيحُ)
[HEADER_4]: الْإِعْرَابُ
Rows:
- (مَفْعُولٌ بِهِ) | أَرَدْتُ (<span class="highlight-red">أَنْ أُسَافِرَ</span>) . | التَّحْوِيلُ: أَرَدْتُ (<span class="highlight-blue">السَّفَرَ</span>) . | إِذَنْ الْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.
- (فَاعِلٌ) | سَرَّنِي (<span class="highlight-red">أَنَّكَ نَجَحْتَ</span>) . | التَّحْوِيلُ: سَرَّنِي (<span class="highlight-blue">نَجَاحُكَ</span>) . (مَنْ الَّذِي سَرَّنِي؟ نَجَاحُكَ). | إِذَنْ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.
- (مَجْرُورٌ) | انْهَضْ كَـ(<span class="highlight-red">مَا نَهَضَ</span>) البَطَلُ. | التَّحْوِيلُ: انْهَضْ كَـ(<span class="highlight-blue">نُهُوضِ</span>) البَطَلِ. (الْكَافُ حَرْفُ جَرٍّ). | إِذَنْ فِي مَحَلِّ جَرٍّ.
- (مُبْتَدَأٌ) | (<span class="highlight-red">أَنْ تَتَعَلَّمُوا</span>) مُفِيدٌ لَكُمْ. | التَّحْوِيلُ: (<span class="highlight-blue">تَعَلُّمُكُمْ</span>) مُفِيدٌ. | إِذَنْ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.

=== BLOCK 4: Definition & Rule - النِّسْبَةُ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: النِّسْبَةُ
Content:
<p class="text-accent">هِيَ طَرِيقَةٌ لِنِسْبَةِ شَخْصٍ أَوْ شَيْءٍ إِلَى مَكَانٍ، أَوْ قَبِيلَةٍ، أَوْ حِرْفَةٍ.</p>
<p>قَاعِدَتُهَا: إِضَافَةُ يَاءٍ مُشَدَّدَةٍ مَكْسُورٌ مَا قَبْلَهَا إِلَى آخِرِ الاسْمِ.</p>
<p>(دِمَشْق -> دِمَشْقِيّ، عَرَب -> عَرَبِيّ).</p>

=== BLOCK 5: Deep Dive - قَوَاعِدُ النِّسْبَةِ وَحَالَاتُهَا الْخَاصَّةُ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: قَوَاعِدُ النِّسْبَةِ وَحَالَاتُهَا الْخَاصَّةُ
Content:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: ١- المَخْتُومُ بِتَاءٍ مَرْبُوطَةٍ (نَحْذِفُ التَّاءَ): قَاهِرَة -> قَاهِرِيّ (وَلَيْسَ قَاهِرَتِيّ). جَامِعَة -> جَامِعِيّ. هَنْدَسَة -> هَنْدَسِيّ. بَصْرَة -> بَصْرِيّ.
[LIST_ITEM_CONTENT]: ٢- المُرَكَّبُ الإِضَافِيُّ (نَنْسُبُ لِلْأَوَّلِ غَالِباً): دَيْرُ الزُّورِ -> دَيْرِيّ. سَيْفُ الدَّوْلَةِ -> سَيْفِيّ. أَوْ نَنْسُبُ لِلثَّانِي مِثْلَ: أَبُو سَعِيدٍ -> سَعِيدِيّ (لِأَنَّ أَبُو كَلِمَةٌ عَامَّةٌ).
[LIST_ITEM_CONTENT]: ٣- المُرَكَّبُ المَزْجِيُّ (نَنْحَتُ الْكَلِمَتَيْنِ مَعاً): حَضْرَمَوْتَ -> حَضْرَمِيّ. بَعْلَبَكّ -> بَعْلِيّ.
[LIST_ITEM_CONTENT]: ٤- المُؤَنَّثُ عَلَى وَزْنِ (فَعِيلَة) (نَحْذِفُ الْيَاءَ وَالتَّاءَ): قَبِيلَة -> قَبَلِيّ. مَدِينَة -> مَدَنِيّ. صَحِيفَة -> صَحَفِيّ.
[LIST_ITEM_CONTENT]: ٥- المَمْدُودُ المُنْتَهِي بِهَمْزَةِ التَّأْنِيثِ (تُقْلَبُ وَاواً): صَحْرَاء -> صَحْرَاوِيّ. حَمْرَاء -> حَمْرَاوِيّ.

=== BLOCK 6: Benefit / Warning ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: (شَاذٌّ: طَبِيعَة -> طَبِيعِيّ لِلْمُحَافَظَةِ عَلَى الْمَعْنَى).

=== BLOCK 7: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: حَوِّلِ الْمَصْدَرَ الْمُؤَوَّلَ إِلَى صَرِيحٍ فِي الْجُمْلَةِ: (أَنْ تَتَعَلَّمُوا) مُفِيدٌ لَكُمْ.

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: انْسُبْ إِلَى الْكَلِمَاتِ التَّالِيَةِ: دِمَشْق، جَامِعَة، صَحْرَاء.

--- END STREAM ---