# **SESSION 63.0**

[TASK DEFINITION]
Objective: Implement عِلْمُ الْمَعَانِي الْأُسْلُوبُ الْخَبَرِيُّ وَالْإِنْشَائِيُّ.
File: `pages/63.0_nXX_عِلْمُ الْمَعَانِي الْأُسْلُوبُ الْخَبَرِيُّ وَالْإِنْشَائِيُّ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/63.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 63
[CHAPTER_TITLE]: عِلْمُ الْمَعَانِي الْأُسْلُوبُ الْخَبَرِيُّ وَالْإِنْشَائِيُّ
[CATEGORY_HEADER]: المستوى المتقدم
[SECTION_HEADER]: علم البلاغة
[AUTHOR_NAME]: أ. حنا خفيف
[AUTHOR_PHONE]:  

=== BLOCK 2: تَمْهِيدٌ لِعِلْمِ الْبَلَاغَةِ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَمْهِيدٌ لِعِلْمِ الْبَلَاغَةِ
Content: <p class="text-accent">عِلْمُ الْبَلَاغَةِ هُوَ عِلْمُ تَزْيِينِ الْكَلَامِ وَقُوَّةِ التَّأْثِيرِ.</p>
<p>وَيَنْقَسِمُ كَلَامُنَا كُلُّهُ فِي اللُّغَةِ إِلَى نَوْعَيْنِ: (<span class="highlight-blue">خَبَرٍ</span>، وَ<span class="highlight-blue">إِنْشَاءٍ</span>).</p>

=== BLOCK 3: أولًا - الأسلوب الخبري ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَوَّلًا - الْأُسْلُوبُ الْخَبَرِيُّ
Content: <p class="text-accent">تَعْرِيفُهُ بِبَسَاطَةٍ: كَلَامٌ يَنْقُلُ لَكَ مَعْلُومَةً، فَيَحْتَمِلُ الصِّدْقَ أَوْ الْكَذِبَ.</p>
<p>(يُمْكِنُكَ أَنْ تَقُولَ لِقَائِلِهِ: أَنْتَ صَادِقٌ، أَوْ أَنْتَ كَاذِبٌ).</p>
<p>مِثَالٌ: "<span class="highlight-red">الْمَطَرُ يَهْطِلُ الْآنَ</span>". هَذَا خَبَرٌ، قَدْ يَكُونُ صِدْقًا وَقَدْ يَكُونُ كَذِبًا.</p>

=== BLOCK 4: أنواعُ الخبرِ (مِنْ حيثُ التَّوْكِيدِ) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَنْوَاعُ الْخَبَرِ (مِنْ حَيْثُ التَّوْكِيدِ)
Content: <p>هَلْ نَحْتَاجُ أَنْ نَحْلِفَ لِلْمُسْتَمِعِ لِيُصَدِّقَنَا؟</p>
<ul class="structured-list">
<li><span class="marker">•</span><div><span class="font-bold">١. الْخَبَرُ الِابْتِدَائِيُّ:</span> لِلشَّخْصِ خَالِي الذِّهْنِ (يُصَدِّقُكَ مُبَاشَرَةً). لَا نَضَعُ فِيهِ أَيَّ مُؤَكِّدٍ. (<span class="highlight-red">نَجَحَ أَكْرَمُ</span>).</div></li>
<li><span class="marker">•</span><div><span class="font-bold">٢. الْخَبَرُ الطَّلَبِيُّ:</span> لِلشَّخْصِ الْمُتَرَدِّدِ (الشَّاكِّ قَلِيلاً). نَضَعُ فِيهِ مُؤَكِّدًا وَاحِدًا كَـ(<span class="highlight-blue">إِنَّ</span>، <span class="highlight-blue">قَدْ</span>). (<span class="highlight-blue">إِنَّ</span> أَكْرَمَ نَاجِحٌ / <span class="highlight-blue">قَدْ</span> نَجَحَ أَكْرَمُ).</div></li>
<li><span class="marker">•</span><div><span class="font-bold">٣. الْخَبَرُ الْإِنْكَارِيُّ:</span> لِلشَّخْصِ الْمُنْكِرِ الَّذِي يُكَذِّبُكَ. نَضَعُ فِيهِ مُؤَكِّدَيْنِ أَوْ أَكْثَرَ. (<span class="highlight-blue">لَعَمْرِي إِنَّ</span> أَكْرَمَ نَاجِحٌ / <span class="highlight-blue">قَسَمًا لَقَدْ</span> نَجَحَ أَكْرَمُ).</div></li>
</ul>

=== BLOCK 5: ثانيًا - الأسلوب الإنشائي ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ثَانِيًا - الْأُسْلُوبُ الْإِنْشَائِيُّ
Content: <p class="text-accent">تَعْرِيفُهُ: كَلَامٌ لَا يَنْقُلُ خَبَرًا، بَلْ يُنْشِئُ مَوْقِفًا (يَطْلُبُ شَيْئًا أَوْ يُعَبِّرُ عَنْ شُعُورٍ). لَا يَحْتَمِلُ الصِّدْقَ وَالْكَذِبَ.</p>
<p>مِثَالٌ: "<span class="highlight-red">اغْسِلْ يَدَيْكَ!</span>". (لَا يُمْكِنُ أَنْ نَقُولَ هَذَا كَذِبٌ!).</p>

=== BLOCK 6: أقسام الإنشاء الأَسَاسِيَّةُ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَقْسَامُ الْإِنْشَاءِ الْأَسَاسِيَّةُ خَمْسَةٌ (الْإِنْشَاءُ الطَّلَبِيُّ)
Content: <ul class="structured-list">
<li><span class="marker">•</span><div><span class="font-bold">١. الْأَمْرُ:</span> طَلَبُ حُدُوثِ الْفِعْلِ. (<span class="highlight-red">اذْهَبْ</span>، <span class="highlight-red">اقْرَأْ</span>).</div></li>
<li><span class="marker">•</span><div><span class="font-bold">٢. النَّهْيُ:</span> طَلَبُ الْكَفِّ عَنِ الْفِعْلِ. وَلَهُ صِيغَةٌ وَاحِدَةٌ (<span class="highlight-blue">لَا</span> النَّاهِيَةُ + الْمُضَارِعُ). (<span class="highlight-blue">لَا</span> <span class="highlight-red">تَلْعَبْ</span>).</div></li>
<li><span class="marker">•</span><div><span class="font-bold">٣. النِّدَاءُ:</span> لِاسْتِدْعَاءِ الْمُخَاطَبِ. (<span class="highlight-blue">يَا</span> <span class="highlight-red">حَارِسُ</span>، <span class="highlight-blue">أَيُّهَا</span> <span class="highlight-red">الرَّجُلُ</span>).</div></li>
<li><span class="marker">•</span><div><span class="font-bold">٤. الِاسْتِفْهَامُ:</span> طَلَبُ مَعْرِفَةِ شَيْءٍ. (<span class="highlight-blue">هَلْ</span> <span class="highlight-red">دَرَسْتَ؟</span> <span class="highlight-blue">مَتَى</span> <span class="highlight-red">نُسَافِرُ؟</span>).</div></li>
<li><span class="marker">•</span><div><span class="font-bold">٥. التَّمَنِّي:</span> طَلَبُ شَيْءٍ مُسْتَحِيلٍ أَوْ صَعْبٍ مَحْبُوبٍ. أَدَاتُهُ الْأَصْلِيَّةُ (<span class="highlight-blue">لَيْتَ</span>). (<span class="highlight-blue">لَيْتَ</span> <span class="highlight-red">الشَّبَابَ يَعُودُ يَوْمًا</span>).</div></li>
</ul>

=== BLOCK 7: Extra Info ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: (وَهُنَاكَ إِنْشَاءٌ غَيْرُ طَلَبِيٍّ لَا نُرَكِّزُ عَلَيْهِ كَثِيرًا: مِثْلَ التَّعَجُّبِ "<span class="highlight-red">مَا أَجْمَلَهُ!</span>"، وَالْقَسَمِ "<span class="highlight-red">لَعَمْرِي</span>"، وَالْمَدْحِ وَالذَّمِّ "<span class="highlight-red">نِعْمَ الرَّجُلُ</span>").

=== BLOCK 8: خروج الإنشاء الطَّلبيّ عن معناه الأصليّ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: خُرُوجُ الْإِنْشَاءِ الطَّلَبِيِّ عَنْ مَعْنَاهُ الْأَصْلِيِّ (الْبَلَاغَةُ الْعَمِيقَةُ)
Content: <p class="text-accent">أَحْيَانًا نَسْتَخْدِمُ (الْأَمْرَ أَوْ الِاسْتِفْهَامَ) وَلَكِنَّنَا لَا نَقْصِدُ مَعْنَاهُ الْحَرْفِيَّ! بَلْ نَقْصِدُ غَرَضًا بَلَاغِيًّا يُفْهَمُ مِنَ السِّيَاقِ.</p>
<ul class="structured-list">
<li><span class="marker">•</span><div><span class="font-bold">الِاسْتِفْهَامُ لِلتَّعَجُّبِ:</span> <span class="highlight-red">هَلْ يُعْقَلُ أَنْ تَرْسُبَ وَأَنْتَ الذَّكِيُّ؟!</span> (الْغَرَضُ التَّعَجُّبُ وَالِاسْتِنْكَارُ).</div></li>
<li><span class="marker">•</span><div><span class="font-bold">الِاسْتِفْهَامُ لِلنَّفْيِ:</span> <span class="highlight-red">هَلْ يَسْتَوِي الَّذِينَ يَجْتَهِدُونَ وَالَّذِينَ يَتَكَاسَلُونَ؟</span> (الْمَعْنَى: لَا يَسْتَوُونَ).</div></li>
<li><span class="marker">•</span><div><span class="font-bold">الْأَمْرُ لِلرَّجَاءِ:</span> إِذَا كَانَ مِنَ الْأَدْنَى لِلْأَعْلَى كَالْمُوَظَّفِ لِمُدِيرِهِ (<span class="highlight-red">سَامِحْنِي هَذِهِ الْمَرَّةَ</span>). (نَحْنُ لَا نَأْمُرُ مَنْ يَفُوقُنَا رُتْبَةً!).</div></li>
<li><span class="marker">•</span><div><span class="font-bold">النِّدَاءُ لِلِاسْتِغَاثَةِ:</span> <span class="highlight-red">يَا لَلْأَطِبَّاءِ</span>، <span class="highlight-red">يَا لَلْعَرَبِ</span>.</div></li>
</ul>

=== BLOCK 9: The Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Title: مُلَخَّصُ أَنْوَاعِ الْكَلَامِ وَالْأَسَالِيبِ
Content:
<table class="dense-table">
<thead>
<tr>
<th>النَّوْعُ</th>
<th>الْأُسْلُوبُ</th>
<th>الْغَرَضُ</th>
<th>يَحْتَمِلُ الصِّدْقَ وَالْكَذِبَ؟</th>
</tr>
</thead>
<tbody>
<tr>
<td>خَبَرٍ</td>
<td>الْخَبَرُ الِابْتِدَائِيُّ / الطَّلَبِيُّ / الْإِنْكَارِيُّ</td>
<td>يَنْقُلُ مَعْلُومَةً</td>
<td>نَعَمْ</td>
</tr>
<tr>
<td>إِنْشَاءٍ</td>
<td>الْأَمْرُ / النَّهْيُ / النِّدَاءُ / الِاسْتِفْهَامُ / التَّمَنِّي</td>
<td>يَطْلُبُ شَيْئًا أَوْ يُعَبِّرُ عَنْ شُعُورٍ</td>
<td>لَا</td>
</tr>
</tbody>
</table>

=== BLOCK 10: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: حَدِّدْ نَوْعَ الْأُسْلُوبِ (خَبَرِيٌّ أَمْ إِنْشَائِيٌّ) فِي الْجُمَلِ الْآتِيَةِ.

=== BLOCK 11: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: مَا هُوَ غَرَضُ الِاسْتِفْهَامِ فِي قَوْلِنَا: هَلْ يُعْقَلُ أَنْ تَرْسُبَ وَأَنْتَ الذَّكِيُّ؟!

--- END STREAM ---