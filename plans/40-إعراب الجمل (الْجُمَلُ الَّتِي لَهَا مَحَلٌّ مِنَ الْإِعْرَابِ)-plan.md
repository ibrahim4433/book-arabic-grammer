# **SESSION 40.0**

[TASK DEFINITION]
Objective: Implement إعراب الجمل (الْجُمَلُ الَّتِي لَهَا مَحَلٌّ مِنَ الْإِعْرَابِ).
File: `pages/40.0_nXX_إعراب الجمل (الْجُمَلُ الَّتِي لَهَا مَحَلٌّ مِنَ الْإِعْرَابِ).html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/40.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 40
[CHAPTER_TITLE]: إعراب الجمل (الْجُمَلُ الَّتِي لَهَا مَحَلٌّ مِنَ الْإِعْرَابِ)
[CATEGORY_HEADER]: المستوى المتقدم
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. حنا خفيف
[AUTHOR_PHONE]:  

=== BLOCK 2: Definition & Rule ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مَفْهُومُ إِعْرَابِ الْجُمَلِ (مُسْتَوًى مُتَقَدِّمٌ)
Content:
<p class="text-accent">فِي الْعَادَةِ نَحْنُ نُعْرِبُ الْكَلِمَاتِ الْمُفْرَدَةَ. لَكِنْ أَحْيَاناً تَكُونُ (الْجُمْلَةُ الْكَامِلَةُ بِمُبْتَدَئِهَا وَخَبَرِهَا، أَوْ فِعْلِهَا وَفَاعِلِهَا) تَحْتَلُّ مَكَاناً إِعْرَابِيّاً مَخْصُوصاً.</p>
<p>الجمل التي تُؤوَّل بمفرد (يُمْكِنُ أَنْ نَضَعَ مَكَانَهَا كَلِمَةً وَاحِدَةً اسْماً) يَكُونُ لها محلٌّ من الإعراب (رَفْعٌ أَوْ نَصْبٌ أَوْ جَرٌّ أَوْ جَزْمٌ).</p>
<p class="font-bold">مثال:</p>
<p>جَاءَ سَعِيدٌ <span class="highlight-red">(يَرْكُضُ)</span> . (يركض) جملة فعلية، يُمْكِنُ حَذْفُهَا وَوَضْعُ (رَاكِضاً) مَكَانَهَا كَحَالٍ، إِذَنْ الْجُمْلَةُ فِي مَحَلِّ نَصْبِ حَالٍ.</p>

=== BLOCK 3: The Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Content: A dense table summarizing the three types of sentences with grammatical place:
- Header row: نَوْعُ الْجُمْلَةِ, مَحَلُّهَا الْإِعْرَابِيُّ, مِثَالٌ
- Row 1: الْجُمْلَةُ الْخَبَرِيَّةُ, رَفْعٌ أَوْ نَصْبٌ, الصَّقْرُ (يَطِيرُ)
- Row 2: الْجُمْلَةُ الْحَالِيَّةُ, نَصْبٌ دَائِماً, جَاءَ الرَّجُلُ (وَهُوَ يَبْتَسِمُ)
- Row 3: الْجُمْلَةُ الْوَصْفِيَّةُ, رَفْعٌ أَوْ نَصْبٌ أَوْ جَرٌّ, مَرَرْتُ بِرَجُلٍ (يَبْتَسِمُ)

=== BLOCK 4: Deep Dive - الْجُمْلَةُ الْخَبَرِيَّةُ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ١- الجملة الْخَبَرِيَّةُ
Content:
<p>تَقَعُ خَبَراً لِلْمُبْتَدَأِ أَوْ النَّوَاسِخِ:</p>
(Inject TEMPLATE_C_LIST.html inside here)
[LIST_ITEM_CONTENT]: فِي مَحَلِّ رَفْعِ خَبَرِ الْمُبْتَدَأِ: الصَّقْرُ <span class="highlight-red">(يَطِيرُ)</span>. يطير جملة فعلية في محل رفع خبر المبتدأ "الصقر".
[LIST_ITEM_CONTENT]: فِي مَحَلِّ رَفْعِ خَبَرِ (إِنَّ) وَأَخَوَاتِهَا: إِنَّ الطَّالِبَ <span class="highlight-red">(يَدْرُسُ)</span>.
[LIST_ITEM_CONTENT]: فِي مَحَلِّ نَصْبِ خَبَرِ (كَانَ) وَأَخَوَاتِهَا: كَانَ الطَّالِبُ <span class="highlight-red">(يَدْرُسُ)</span>.

=== BLOCK 5: Deep Dive - الجملة الحالية ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٢- الجملة الحالية (محلها النصب دَائِماً)
Content:
<p>تأتي لتبيِّن هيئة صاحبها المعرفة.</p>
(Inject TEMPLATE_C_BENEFIT_TIP.html inside here)
Tip Content: القاعدة الذهبية: الجمل بعد المعارف أحوال.
<p class="font-bold">أمثلة:</p>
(Inject TEMPLATE_C_LIST.html inside here)
[LIST_ITEM_CONTENT]: جَاءَ الرَّجُلُ <span class="highlight-red">(وَهُوَ يَبْتَسِمُ)</span> . الجملة الاسمية في محل نصب حال.
[LIST_ITEM_CONTENT]: جَاءَ الرَّجُلُ <span class="highlight-red">(يَرْكُضُ)</span> . الجملة الفعلية في محل نصب حال.

=== BLOCK 6: Deep Dive - الجُمْلَةُ الوَصْفِيَّةُ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٣- الجُمْلَةُ الوَصْفِيَّةُ (النَّعْتُ - تَتْبَعُ الْمَوْصُوفَ)
Content:
<p>تأتي لتصف نكرةً قبلها. مَحَلُّهَا يَكُونُ (رَفْعاً أَوْ نَصْباً أَوْ جَرّاً) حَسَبَ النَّكِرَةِ قَبْلَهَا.</p>
(Inject TEMPLATE_C_BENEFIT_WARNING.html inside here)
Warning Content: القاعدة الذهبية: الجمل بعد النكرات صفات.
<p class="font-bold">أمثلة:</p>
(Inject TEMPLATE_C_LIST.html inside here)
[LIST_ITEM_CONTENT]: مثال الرفع: جَاءَ رَجُلٌ <span class="highlight-red">(يَبْتَسِمُ)</span> . (يَبْتَسِمُ جملة في محل رفع صفة لأن رجل مرفوع).
[LIST_ITEM_CONTENT]: مثال النصب: رَأَيْتُ رَجُلاً <span class="highlight-red">(يَبْتَسِمُ)</span> . (محل نصب صفة).
[LIST_ITEM_CONTENT]: مثال الجر: مَرَرْتُ بِرَجُلٍ <span class="highlight-red">(يَبْتَسِمُ)</span> . (محل جر صفة).

=== BLOCK 7: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: حَدِّدْ مَحَلَّ الْجُمْلَةِ مِنَ الْإِعْرَابِ فِي: جَاءَ سَعِيدٌ (يَرْكُضُ).
Number: ٢
Question: بَيِّنْ نَوْعَ الْجُمْلَةِ بَيْنَ قَوْسَيْنِ وَمَحَلَّهَا مِنَ الْإِعْرَابِ فِي: جَاءَ رَجُلٌ (يَبْتَسِمُ).
Number: ٣
Question: أَعْرِبِ الْجُمْلَةَ فِي: الصَّقْرُ (يَطِيرُ).

--- END STREAM ---
