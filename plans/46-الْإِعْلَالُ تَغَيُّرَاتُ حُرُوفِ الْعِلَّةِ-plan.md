# **SESSION 46.0**

[TASK DEFINITION]
Objective: Implement الْإِعْلَالُ تَغَيُّرَاتُ حُرُوفِ الْعِلَّةِ.
File: `pages/46.0_nXX_الْإِعْلَالُ تَغَيُّرَاتُ حُرُوفِ الْعِلَّةِ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/46.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 46
[CHAPTER_TITLE]: الْإِعْلَالُ تَغَيُّرَاتُ حُرُوفِ الْعِلَّةِ
[CATEGORY_HEADER]: المستوى المتوسط
[SECTION_HEADER]: علم الصرف
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition Block ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَعْرِيفُ الْإِعْلَالِ
Content: <p class="text-accent mb-2mm">الْإِعْلَالُ: هُوَ تَغْيِيرٌ مَرَضِيٌّ يُصِيبُ حَرْفَ الْعِلَّةِ الْمَرِيضَ (الْأَلِفَ، الْوَاوَ، الْيَاءَ) لِتَسْهِيلِ النُّطْقِ بِهِ، لِأَنَّ حُرُوفَ الْعِلَّةِ ثَقِيلَةٌ عَلَى اللِّسَانِ العَرَبِيِّ إِذَا تَحَرَّكَتْ كَثِيراً.</p>

=== BLOCK 3: Types of I'lal Table ===
(Component: TEMPLATE_C_TABLE.html)
Headers: النّوع | التّعريف | مثال
Row 1: الإعلال بالتّسكين (السُّكُونُ بَدَلَ الْحَرَكَةِ) | تسكينُ أحد حرفي العلّة (الواو أو الياء) لثقلهما بالضمة أو الكسرة، (والألف ساكنة دائمًا لا تُعَلُّ بِالتَّسْكِينِ). | يَسْمُوْ (أصله يَسْمُوُ بِضَمَّةٍ عَلَى الْوَاوِ، فَحُذِفَتِ الضَّمَّةُ لِلثِّقَلِ). يَمْشِيْ (أصله يَمْشِيُ، سُكِّنَتِ الْيَاءُ لِلثِّقَلِ).
Row 2: الإعلال بالحذْف (حَذْفُ الْحَرْفِ نِهَائِيّاً) | حذفُ حرفِ العلةِ تَمَاماً للتخلص من التقاء الساكنين أو في حالات الجزم. | قُلْ (أَصْلُهَا قُوْلْ، حُذِفَتِ الْوَاوُ لِمَنْعِ الْتِقَاءِ سَاكِنَيْنِ). لَمْ يَمْشِ (حُذِفَت الياء لِلْجَزْمِ).
Row 3: الإعلال بالقلب (تَحْوِيلُهُ لِحَرْفٍ آخَرَ) | قَلبُ حرفِ العِلَّةِ إلى حرفٍ آخر (ألف، واو، ياء) لِيُنَاسِبَ الْحَرَكَةَ الَّتِي قَبْلَهُ. | قَالَ (أصله قَوَلَ، قُلِبَتِ الْوَاوُ أَلِفاً لِتُنَاسِبَ الْفَتْحَةَ). قِيَام (أصله قِوَام، قُلِبَتِ الْوَاوُ يَاءً لِتُنَاسِبَ الْكَسْرَةَ).

=== BLOCK 4: Extra Details and Analysis ===
(Component: TEMPLATE_C_SPLIT.html)
LeftSide Component: TEMPLATE_C_BLOCK.html
Title: التَّحْلِيلُ
Content: نُشَاهِدُ فِي الْأَمْثِلَةِ السَّابِقَةِ تَغَيُّرَاتٍ مَلْحُوظَةً عَلَى حُرُوفِ الْعِلَّةِ (الْوَاوِ، الْيَاءِ، الْأَلِفِ)، وَقَدْ تَمَّ تَسْكِينُ بَعْضِهَا كَمَا فِي (يَسْمُوْ)، أَوْ حَذْفُهَا كَمَا فِي (قُلْ)، أَوْ قَلْبُهَا كَمَا فِي (قَالَ). هَذِهِ التَّغَيُّرَاتُ ضَرُورِيَّةٌ لِضَمَانِ سُهُولَةِ النُّطْقِ.
RightSide Component: TEMPLATE_C_LIST.html
Title: أَمْثِلَةٌ إِضَافِيَّةٌ لِلتَّوْضِيحِ
List Items:
- <span class="highlight-red">يَسْعَى</span> (الْأَصْلُ يَسْعَيُ).
- <span class="highlight-red">بَاعَ</span> (الْأَصْلُ بَيَعَ).
- <span class="highlight-red">لَمْ يَرْمِ</span> (حُذِفَتِ الْيَاءُ لِلْجَزْمِ).

=== BLOCK 5: Golden Rule Box ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Content: <p class="mb-0">فَائِدَةٌ ذَهَبِيَّةٌ: مَعْرِفَةُ أَصْلِ الْأَلِفِ. لِكَيْ تَعْرِفَ أَصْلَ الْأَلِفِ فِي أَيِّ كَلِمَةٍ (هَلْ هِيَ وَاوٌ أَمْ يَاءٌ؟ لِأَنَّ الْأَلِفَ لَيْسَتْ أَصْلِيَّةً أَبَداً)، ارْجِعْ إِلَى أَحَدِ ثَلَاثَةِ أَشْيَاءَ:</p>

=== BLOCK 6: Golden Rule Explanation ===
(Component: TEMPLATE_C_BLOCK.html)
Title: طُرُقُ مَعْرِفَةِ الْأَصْلِ
Content: (Component: TEMPLATE_C_LIST.html)
List Items:
- ١- الْمُضَارِعُ: قَال -> يَقُولُ (إِذَنْ الْأَلِفُ أَصْلُهَا واو). بَاع -> يَبِيعُ (إِذَنْ أَصْلُهَا ياء).
- ٢- الْمَصْدَرُ: سَعَى -> السَّعْي (أَصْلُهَا ياء). رَجَا -> الرَّجَاء (أَصْلُهَا واو).
- ٣- إِسْنَادُ الْفِعْلِ لِضَمِيرٍ (تَاءِ الْفَاعِلِ): رَجَا -> رَجَوْتُ (واو). رَمَى -> رَمَيْتُ (ياء).

=== BLOCK 7: Warning Box ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: تَذَكَّرْ دَائِماً أَنَّ الْأَلِفَ اللّيِّنَةَ لَا يُمْكِنُ أَنْ تَكُونَ أَصْلِيَّةً فِي الْكَلِمَةِ، بَلْ هِيَ دَائِمًا مُنْقَلِبَةٌ عَنْ وَاوٍ أَوْ يَاءٍ، أَوْ زَائِدَةٌ.

=== BLOCK 8: Exam Header Block ===
(Component: TEMPLATE_C_BLOCK.html)
Title:  اخْتَبِرْ نَفْسَكَ (الْإِعْلَالُ)
Content:

=== BLOCK 9: Exam 1 ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: بَيِّنْ نَوْعَ الْإِعْلَالِ فِي: ( ارْجُ ).

=== BLOCK 10: Exam 2 ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: هَاتِ أَصْلَ الْكَلِمَةِ: ( بَاعَ ) وَبَيِّنِ التَّغْيِيرَ.

=== BLOCK 11: Exam 3 ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٣
Question: عَلِّلْ حَذْفَ حَرْفِ الْعِلَّةِ فِي كَلِمَةِ (قُلْ).

--- END STREAM ---
