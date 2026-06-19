# **SESSION 52.0**

[TASK DEFINITION]
Objective: Implement تَثْنِيَةُ وَجَمْعُ المَنْقُوصِ وَالْمَقْصُورِ وَالْمَمْدُودِ.
File: `pages/52.0_nXX_تَثْنِيَةُ وَجَمْعُ المَنْقُوصِ وَالْمَقْصُورِ وَالْمَمْدُودِ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually, instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/52.1_...` if page have a lot of blank space add exam elements from the lesson.
3. text Content: 100% Arabic with full Harakat.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`, `.highlight-green` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   **Rule:** NO INLINE STYLES.
*   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
*   **Mapping:**
    *   inline style width: 20% -> `class="w-20pct"`
    *   inline style margin-top: 2mm -> `class="mt-2mm"`
    *   inline style text-align: center -> `class="text-center"`
    *   inline style font-weight: bold -> `class="font-bold"`
6. Templates: You are forbidden from inventing new HTML tags or classes or template elements. You must map all content using "Jules-workspace/Templates/" components as the STREAM says in a suitable way.
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). use "Jules-workspace/id_manager.py" to generate or verify them.
8. **Self-Correction:** Run "Jules-workspace/lint_pages.py" after creating html files. If it fails, you MUST fix the errors (usually inline styles) before submitting.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...).
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
13. balanced page colors between teal and orange: make sure every page has minimum 1 element in orange instead of all teal.
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
15. Exam section always be in the end of the lesson (in the final page of that lesson), and without the answers!

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 52
[CHAPTER_TITLE]: تَثْنِيَةُ وَجَمْعُ المَنْقُوصِ وَالْمَقْصُورِ وَالْمَمْدُودِ
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم الإملاء
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: الاسْمُ المَنْقُوصُ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ١- الاسْمُ المَنْقُوصُ
Content: (Contains Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: <span class="text-accent">عِنْدَ التَّثْنِيَةِ:</span> تُرَدُّ الياء المحذوفة (<span class="highlight-blue">قَاضٍ</span> -> <span class="highlight-red">قَاضِيَانِ</span>، <span class="highlight-red">قَاضِيَيْنِ</span>). <span class="highlight-blue">الْبَانِي</span> -> <span class="highlight-red">الْبَانِيَانِ</span>.
[LIST_ITEM_CONTENT]: <span class="text-accent">عِنْدَ جَمْعِ المُذَكَّرِ السَّالِمِ:</span> تُحْذَفُ الياء <span class="font-bold">دَائِماً</span> (<span class="highlight-blue">الرَّاعِي</span> -> <span class="highlight-red">الرَّاعُونَ</span> / <span class="highlight-red">الرَّاعِينَ</span>). <span class="highlight-blue">الْبَانِي</span> -> <span class="highlight-red">الْبَانُونَ</span>.

=== BLOCK 3: الاسْمُ المَقْصُورُ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٢- الاسْمُ المَقْصُورُ
Content: (Contains Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: <span class="text-accent">عِنْدَ التَّثْنِيَةِ (إِذَا كَانَ ثُلَاثِيّاً):</span> نُعِيدُ الألف لأصلها الواو أو الياء. (<span class="highlight-blue">فَتَى</span> -> <span class="highlight-red">فَتَيَانِ</span>). (<span class="highlight-blue">عَصَا</span> -> <span class="highlight-red">عَصَوَانِ</span>).
[LIST_ITEM_CONTENT]: <span class="text-accent">عِنْدَ التَّثْنِيَةِ (إِذَا كَانَ فَوْقَ ٣ أَحْرُفٍ):</span> تُقْلَبُ الألفُ ياءً <span class="font-bold">دَائِماً</span>. (<span class="highlight-blue">مُسْتَشْفَى</span> -> <span class="highlight-red">مُسْتَشْفَيَانِ</span>). (<span class="highlight-blue">مَبْنَى</span> -> <span class="highlight-red">مَبْنَيَانِ</span>).

=== BLOCK 4: تَنْبِيهٌ هَامٌّ لِلْمَقْصُورِ ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: <span class="text-accent">عِنْدَ جَمْعِ المُذَكَّرِ السَّالِمِ:</span> تُحْذَفُ الألفُ دَائِماً <span class="highlight-red font-bold">وَيُفْتَحُ مَا قَبْلَهَا!</span> (<span class="highlight-blue">مُسْتَدْعَى</span> -> <span class="highlight-red">مُسْتَدْعَوْنَ</span> / <span class="highlight-red">مُسْتَدْعَيْنَ</span>). (<span class="highlight-blue">الْأَعْلَى</span> -> <span class="highlight-red">الْأَعْلَوْنَ</span>).

=== BLOCK 5: الاسْمُ المَمْدُودُ (حَسَبَ نَوْعِ هَمْزَتِهِ) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٣- الاسْمُ المَمْدُودُ
Content: (Contains Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: <span class="text-accent">إِذَا كَانَتِ الهَمْزَةُ أَصْلِيَّةً</span> (مِنْ أَصْلِ الْفِعْلِ، <span class="highlight-green">قَرَأَ</span>): تَبْقَى كَمَا هِيَ. (<span class="highlight-blue">قَرَّاء</span> -> <span class="highlight-red">قَرَّاءَانِ</span>، <span class="highlight-red">قَرَّاؤُونَ</span>).
[LIST_ITEM_CONTENT]: <span class="text-accent">إِذَا كَانَتِ الهَمْزَةُ زَائِدَةً لِلتَّأْنِيثِ</span> (لَا تُوجَدُ فِي الْفِعْلِ، <span class="highlight-green">حَسُنَ</span>): تُقْلَب واوًا. (<span class="highlight-blue">حَسْنَاء</span> -> <span class="highlight-red">حَسْنَاوَانِ</span>، <span class="highlight-red">حَسْنَاوَات</span>). (<span class="highlight-blue">صَحْرَاء</span> -> <span class="highlight-red">صَحْرَاوَانِ</span>).
[LIST_ITEM_CONTENT]: <span class="text-accent">إِذَا كَانَتِ الهَمْزَةُ مُنْقَلِبَةً عَنْ أَصْلٍ</span> (وَاو أَوْ يَاء، <span class="highlight-green">رَجَا</span>): يَجُوزُ بَقَاؤُهَا أَوْ قَلْبُهَا وَاواً. (<span class="highlight-blue">رَجَاء</span> -> <span class="highlight-red">رَجَاءَانِ</span> / <span class="highlight-red">رَجَاوَانِ</span>). (<span class="highlight-blue">سَمَاء</span> -> <span class="highlight-red">سَمَاءَانِ</span> / <span class="highlight-red">سَمَاوَانِ</span>).

=== BLOCK 6: جَدْوَلُ مُقَارَنَةِ الْأَحْكَامِ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: جَدْوَلُ مُقَارَنَةِ الْأَحْكَامِ (عِنْدَ التَّثْنِيَةِ وَالْجَمْعِ)
Content: (Contains Component: TEMPLATE_C_TABLE.html)
Headers: النَّوْعُ | حُكْمُهُ عِنْدَ التَّثْنِيَةِ | حُكْمُهُ عِنْدَ الْجَمْعِ السَّالِمِ
Row 1: الْمَنْقُوصُ | تُرَدُّ الياء المحذوفة | تُحْذَفُ الياء دَائِماً
Row 2: الْمَقْصُورُ | الثُّلَاثِيُّ: نُعِيدُ الألف لأصلها / فَوْقَ الثُّلَاثِيِّ: تُقْلَبُ ياءً | تُحْذَفُ الألفُ دَائِماً وَيُفْتَحُ مَا قَبْلَهَا
Row 3: الْمَمْدُودُ | الأَصْلِيَّةُ: تَبْقَى / لِلتَّأْنِيثِ: تُقْلَبُ واواً / مُنْقَلِبَةٌ: بَقَاؤُهَا أَوْ قَلْبُهَا | الأَصْلِيَّةُ: تَبْقَى / لِلتَّأْنِيثِ: تُقْلَبُ واواً / مُنْقَلِبَةٌ: بَقَاؤُهَا أَوْ قَلْبُهَا

=== BLOCK 7: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: كَيْفَ يُثَنَّى الاسْمُ المَقْصُورُ إِذَا كَانَ ثُلَاثِيّاً وَإِذَا كَانَ فَوْقَ ثَلَاثَةِ أَحْرُفٍ؟
Number: ٢
Question: مَاذَا يَحْدُثُ لِلِاسْمِ المَنْقُوصِ وَالمَقْصُورِ عِنْدَ جَمْعِهِمَا جَمْعَ مُذَكَّرٍ سَالِماً؟
Number: ٣
Question: مَا هُوَ حُكْمُ هَمْزَةِ المَمْدُودِ إِذَا كَانَتْ زَائِدَةً لِلتَّأْنِيثِ عِنْدَ التَّثْنِيَةِ؟ هَاتِ مِثَالاً.

--- END STREAM ---
