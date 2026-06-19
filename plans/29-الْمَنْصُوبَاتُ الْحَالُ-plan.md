# **SESSION 29.0**

[TASK DEFINITION]
Objective: Implement الْمَنْصُوبَاتُ الْحَالُ.
File: `pages/29.0_nXX_الْمَنْصُوبَاتُ الْحَالُ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/29.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 29
[CHAPTER_TITLE]: الْمَنْصُوبَاتُ الْحَالُ
[CATEGORY_HEADER]: المستوى المتوسط
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: الْمَنْصُوبَاتُ فِي اللُّغَةِ (الْحَالُ) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الْمَنْصُوبَاتُ فِي اللُّغَةِ (الْحَالُ)
Content:
<p class="text-accent mb-2mm">تَعَلَّمْنَا أَنَّ الْمَفَاعِيلَ (الْمَفْعُولَ بِهِ) مَنْصُوبَةٌ. هُنَاكَ أَسْمَاءٌ أُخْرَى تُنْصَبُ دَائِماً مِنْهَا <span class="highlight-red font-bold">الْحَالُ</span> وَالتَّمْيِيزُ وَالْمَفْعُولُ فِيهِ (الظَّرْفُ).</p>
<p class="font-bold text-primary mb-2mm">الْحَالُ:</p>
<p class="text-accent mb-2mm">اسْمٌ مَنْصُوبٌ يُذْكَرُ فِي الْجُمْلَةِ الْفِعْلِيَّةِ لِيُبَيِّنَ كَيْفِيَّةَ (هَيْئَةَ) مَنْ قَامَ بِالْفِعْلِ (الْفَاعِلِ) أَوْ مَنْ وَقَعَ عَلَيْهِ الْفِعْلُ (الْمَفْعُولِ بِهِ) عِنْدَ حُدُوثِ الْفِعْلِ.</p>
<p class="text-accent mb-2mm">وَيُسَمَّى الْفَاعِلُ أَوِ الْمَفْعُولُ بِهِ الَّذِي نُبَيِّنُ هَيْئَتَهُ بِـ (<span class="font-bold">صَاحِبِ الْحَالِ</span>).</p>
<p class="mb-2mm">وَيَكُونُ صَاحِبُ الْحَالِ، غَالِباً، مَعْرِفَةً أَمَّا الْحَالُ فَتَكُونُ نَكِرَةً. (وَنَسْتَخْرِجُهَا بِسُؤَالٍ يَبْدَأُ بِـ <span class="highlight-blue font-bold">كَيْفَ؟</span>).</p>

=== BLOCK 3: التَّطْبِيقُ وَالتَّحْلِيلُ ===
(Component: TEMPLATE_C_SPLIT.html)
LeftSide:
  (Component: TEMPLATE_C_BLOCK.html)
  Title: الْمِثَالُ
  Content: <p>عَادَ الطِّفْلُ <span class="highlight-red">بَاكِياً</span>. (كَيْفَ عَادَ الطِّفْلُ؟ <span class="highlight-red">بَاكِياً</span>).</p>
RightSide:
  (Component: TEMPLATE_C_BLOCK.html)
  Title: التَّحْلِيلُ
  Content: <p>إِذَنْ (<span class="highlight-red">بَاكِياً</span>) هِيَ الْحَالُ، وَصَاحِبُهَا <span class="highlight-blue">الطِّفْلُ</span> الْمَعْرِفَةُ.</p>

=== BLOCK 4: الإِعْرَابُ لِلْمِثَالِ ===
(Component: TEMPLATE_C_IRAB_ROW.html)
Word 1: بَاكِياً
Details 1: حَالٌ مَنْصُوبَةٌ وَعَلَامَةُ نَصْبِهَا الْفَتْحَةُ الظَّاهِرَةُ عَلَى آخِرِهَا.
Word 2: الطِّفْلُ
Details 2: صَاحِبُ الْحَالِ (مَعْرِفَةٌ). فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.

=== BLOCK 5: صُوَرُ مَجِيءِ الْحَالِ (أَنْوَاعُهَا) ===
(Component: TEMPLATE_C_TABLE.html)
Headers: النَّوْعُ | الْمِثَالُ | التَّحْلِيلُ وَالإِعْرَابُ
Row 1: اسْمٌ مُفْرَدٌ (كَلِمَةٌ وَاحِدَةٌ) | عَادَ الرَّجُلُ إِلَى بَيْتِهِ <span class="highlight-red">مُتْعَباً</span>. | (مُتْعَباً): حَالٌ مُفْرَدَةٌ مَنْصُوبَةٌ بِالْفَتْحَةِ.
Row 2: جُمْلَةٌ اسْمِيَّةٌ | دَخَلَ الْمُدَرِّسُ (<span class="highlight-red">لِبَاسُهُ أَنِيقٌ</span>). | كَيْفَ دَخَلَ؟ لِبَاسُهُ أَنِيقٌ (مُبْتَدَأٌ وَخَبَرٌ فِي مَحَلِّ نَصْبِ حَالٍ).
Row 3: جُمْلَةٌ فِعْلِيَّةٌ | اعْتَلَى الْمُتَفَوِّقُ مَنَصَّةَ التَّتْوِيجِ (<span class="highlight-red">تَرْقُبُهُ الْعُيُونُ</span>). | جُمْلَةُ (تَرْقُبُهُ) فِي مَحَلِّ نَصْبِ حَالٍ.

=== BLOCK 6: الْقَاعِدَةُ الذَّهَبِيَّةُ ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Content: <p class="font-bold text-center mb-2mm">الْجُمَلُ بَعْدَ الْمَعَارِفِ أَحْوَالٌ، وَبَعْدَ النَّكِرَاتِ صِفَاتٌ.</p><p class="text-center">بِمَا أَنَّ الْمُدَرِّسَ وَالْمُتَفَوِّقَ مَعْرِفَةٌ، فَالْجُمَلُ بَعْدَهُمَا أَحْوَالٌ.</p>

=== BLOCK 7: الرَّابِطُ فِي جُمْلَةِ الْحَالِ ===
(Component: TEMPLATE_C_BLOCK.html)
Variant: .block-header.accent
Title: الرَّابِطُ فِي جُمْلَةِ الْحَالِ
Content: <p class="mb-2mm">عِنْدَمَا تَأْتِي الْحَالُ جُمْلَةً يَنْبَغِي أَنْ يَكُونَ لَهَا رَابِطٌ يَرْبِطُهَا بِصَاحِبِ الْحَالِ:</p>
(Component: TEMPLATE_C_LIST.html)
Item 1: <span class="font-bold">وَاوُ الْحَالِ</span> (وَاوٌ تُسَمَّى وَاوَ الْحَالِ وَلَيْسَتْ لِلْعَطْفِ): نَطَقَ الْمُدَرِّسُ <span class="highlight-red">وَ</span>(الطَّالِبُ صَامِتٌ). (أَيْ نَطَقَ فِي حَالِ صَمْتِ الطَّالِبِ).
Item 2: <span class="font-bold">الضَّمِيرُ وَحْدَهُ</span>: سَكَتَ الطُّلَّابُ (عُيُونُ<span class="highlight-red">هُمْ</span> مَشْدُودَةٌ). (<span class="highlight-red">هُمْ</span> تَعُودُ عَلَى الطُّلَّابِ).
Item 3: <span class="font-bold">وَاوُ الْحَالِ وَالضَّمِيرُ كِلَاهُمَا</span>: لَا تَسْأَلِ الْمُدَرِّسَ <span class="highlight-red">وَهُوَ</span> (مُسْتَرْسِلٌ) فِي الشَّرْحِ.

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: حَدِّدِ الْحَالَ وَصَاحِبَهَا فِيمَا يَلِي، ثُمَّ بَيِّنْ نَوْعَهَا: جَاءَ الطَّالِبُ يَضْحَكُ.

=== BLOCK 9: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: اجْعَلِ الْحَالَ الْمُفْرَدَةَ جُمْلَةً فِيمَا يَلِي: رَجَعَ الْجَيْشُ مُنْتَصِراً.

=== BLOCK 10: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٣
Question: أَعْرِبْ مَا تَحْتَهُ خَطٌّ: شَاهَدْتُ الْفَلَّاحَ (يَحْصُدُ الْقَمْحَ).

--- END STREAM ---