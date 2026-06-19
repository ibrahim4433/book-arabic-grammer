# **SESSION 38.0**

[TASK DEFINITION]
Objective: Implement الْبَدَلُ.
File: `pages/38.0_nXX_الْبَدَلُ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/38.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 38
[CHAPTER_TITLE]: الْبَدَلُ
[CATEGORY_HEADER]: المستوى المتوسط
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition and Intro ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَعْرِيفُ الْبَدَلِ
Content: <p class="text-accent">هُوَ تَابِعٌ مَقْصُودٌ بِالْحُكْمِ، يُمَهَّدُ لَهُ بِكَلِمَةٍ قَبْلَهُ تُسَمَّى الْمُبْدَلَ مِنْهُ، وَلَا يُوجَدُ بَيْنَهُمَا حَرْفُ عَطْفٍ كَوَاسِطَةٍ.</p>
<p>مِثَالٌ: (<span class="highlight-blue">جَاءَ</span> <span class="highlight-green">الطَّالِبُ</span> <span class="highlight-red">سَامِرٌ</span>). <span class="highlight-red">سَامِرٌ</span> هُوَ الْبَدَلُ (الْمَقْصُودُ بِالْمَجِيءِ فِعْلِيّاً)، وَ<span class="highlight-green">الطَّالِبُ</span> هُوَ الْمُبْدَلُ مِنْهُ (وَظِيفَتُهُ أَو لَقَبُهُ). <span class="highlight-red">سَامِرٌ</span> بَدَلٌ مَرْفُوعٌ لِأَنَّ <span class="highlight-green">الطَّالِبَ</span> فَاعِلٌ مَرْفُوعٌ.</p>

=== BLOCK 3: The Core Matrix (Types of Badal) ===
(Component: TEMPLATE_C_TABLE.html)
Headers: النَّوْعُ | التَّعْرِيفُ | مِثَالٌ
Row 1: بَدَلُ كُلٍّ مِنْ كُلٍّ (الْبَدَلُ الْمُطَابِقُ) | الْبَدَلُ هُوَ الْمُبْدَلُ مِنْهُ نَفْسُهُ تَمَاماً. (اللَّقَبُ + الِاسْمُ) أَوْ (اسْمُ الْإِشَارَةِ + اسْمٌ مُعَرَّفٌ بِـ الـ). | الْمُهَنْدِسُ سَامِرٌ مُبْدِعٌ
Row 2: بَدَلُ بَعْضٍ مِنْ كُلٍّ | الْبَدَلُ جُزْءٌ حَقِيقِيٌّ مَادِّيٌّ مِنَ الْمُبْدَلِ مِنْهُ (يَحْتَاجُ ضَمِيرًا). | أَكَلْتُ الرَّغِيفَ نِصْفَهُ
Row 3: بَدَلُ اشْتِمَالٍ | الْبَدَلُ صِفَةٌ أَوْ أَمْرٌ مَعْنَوِيٌّ لَيْسَ مَادِّيّاً يَشْتَمِلُ عَلَيْهِ الْمُبْدَلُ مِنْهُ. | يُعْجِبُنِي الْقَائِدُ عَدْلُهُ

=== BLOCK 4: Deep Dive - Type 1 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ١- بَدَلُ كُلٍّ مِنْ كُلٍّ (الْبَدَلُ الْمُطَابِقُ)
Content: <p>الْبَدَلُ هُوَ الْمُبْدَلُ مِنْهُ نَفْسُهُ تَمَاماً.</p>
<p>(اللَّقَبُ + الِاسْمُ) أَوْ (اسْمُ الْإِشَارَةِ + اسْمٌ مُعَرَّفٌ بِـ الـ).</p>
<p>أَمْثِلَةٌ:</p>
<ul class="structured-list">
<li>(<span class="highlight-green">الْمُهَنْدِسُ</span> <span class="highlight-red">سَامِرٌ</span> مُبْدِعٌ). (<span class="highlight-red">سَامِرٌ</span> بَدَلٌ).</li>
<li>(رَأَيْتُ <span class="highlight-green">هَذَا</span> <span class="highlight-red">الْمُحَارِبَ</span>). <span class="highlight-red">الْمُحَارِبَ</span>: بَدَلٌ مَنْصُوبٌ بِالْفَتْحَةِ بَعْدَ اسْمِ الْإِشَارَةِ.</li>
</ul>

=== BLOCK 5: Deep Dive - Type 2 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٢- بَدَلُ بَعْضٍ مِنْ كُلٍّ
Content: <p>الْبَدَلُ جُزْءٌ حَقِيقِيٌّ مَادِّيٌّ مِنَ الْمُبْدَلِ مِنْهُ (يَحْتَاجُ ضَمِيرًا).</p>
<p>أَمْثِلَةٌ:</p>
<ul class="structured-list">
<li>(أَكَلْتُ <span class="highlight-green">الرَّغِيفَ</span> <span class="highlight-red">نِصْفَهُ</span>). النِّصْفُ جُزْءٌ مِنَ الرَّغِيفِ، وَالْهَاءُ تَعُودُ عَلَيْهِ.</li>
<li>(سَقَطَتِ <span class="highlight-green">الشَّجَرَةُ</span> <span class="highlight-red">فُرُوعُهَا</span>). الفُرُوعُ جُزْءٌ حَقِيقِيٌّ مِنَ الشَّجَرَةِ.</li>
</ul>

=== BLOCK 6: Extra Info (Orange Warning) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: ٣- بَدَلُ اشْتِمَالٍ: الْبَدَلُ صِفَةٌ أَوْ أَمْرٌ مَعْنَوِيٌّ لَيْسَ مَادِّيّاً يَشْتَمِلُ عَلَيْهِ الْمُبْدَلُ مِنْهُ.

=== BLOCK 7: Deep Dive - Type 3 Examples ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَمْثِلَةٌ عَلَى بَدَلِ الِاشْتِمَالِ
Content: <ul class="structured-list">
<li>نَحْوُ: (يُعْجِبُنِي <span class="highlight-green">الْقَائِدُ</span> <span class="highlight-red">عَدْلُهُ</span>). <span class="highlight-red">عَدْلُهُ</span>: بَدَلٌ مَرْفُوعٌ بِالضَّمَّةِ (أَمْرٌ مَعْنَوِيٌّ وَلَيْسَ جُزْءاً مِنَ الْجَسَدِ).</li>
<li>(أَعْجَبَنِي <span class="highlight-green">الطَّالِبُ</span> <span class="highlight-red">خُلُقُهُ</span>). <span class="highlight-red">خُلُقُهُ</span> أَمْرٌ مَعْنَوِيٌّ يَشْتَمِلُ عَلَيْهِ الطَّالِبُ.</li>
</ul>

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: استخرج التابع وبين نوعه: (حضر الطلابُ كُلُّهُم).
Number: ٢
Question: استخرج التابع وبين نوعه: (مررتُ بالرجلِ الكريمِ).
Number: ٣
Question: استخرج التابع وبين نوعه: (جاء الطبيبُ سَامِرٌ).
Number: ٤
Question: استخرج التابع وبين نوعه: (أحبُّ الفاكهةَ والخضارَ).

--- END STREAM ---
