# **SESSION 21.0**

[TASK DEFINITION]
Objective: Implement الْفِعْلُ الْمَاضِي حَالَاتُ بِنَائِهِ بِالتَّفْصِيلِ.
File: `pages/21.0_nXX_الْفِعْلُ الْمَاضِي حَالَاتُ بِنَائِهِ بِالتَّفْصِيلِ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/21.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 21
[CHAPTER_TITLE]: الْفِعْلُ الْمَاضِي حَالَاتُ بِنَائِهِ بِالتَّفْصِيلِ
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: أَقْسَامُ الْأَفْعَالِ وَتَعْرِيفُ الْفِعْلِ الْمَاضِي ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَقْسَامُ الْأَفْعَالِ وَتَعْرِيفُ الْفِعْلِ الْمَاضِي
Content:
<p class="text-accent mb-2mm">تُقَسَّمُ الْأَفْعَالُ فِي اللُّغَةِ الْعَرَبِيَّةِ إِلَى ثَلَاثَةِ أَقْسَامٍ: <span class="highlight-red font-bold">الْمَاضِي</span> ، وَ <span class="highlight-blue font-bold">الْمُضَارِعُ</span> ، وَ <span class="highlight-green font-bold">الْأَمْرُ</span>.</p>
<p class="text-accent mb-2mm">وَالْأَصْلُ فِي الْأَفْعَالِ أَنَّهَا (<span class="font-bold">مَبْنِيَّةٌ</span>) أَيْ ثَابِتَةُ الْآخِرِ لَا تَتَغَيَّرُ مَعَ الْإِعْرَابِ، مَا عَدَا الْفِعْلَ الْمُضَارِعَ فَإِنَّهُ مُعْرَبٌ غَالِباً.</p>
<p class="font-bold mt-2mm mb-2mm">تَعْرِيفُ الْفِعْلِ الْمَاضِي:</p>
<p class="text-accent mb-2mm">هُوَ فِعْلٌ يَدُلُّ عَلَى حَدَثٍ وَقَعَ وَانْقَطَعَ قَبْلَ زَمَنِ التَّكَلُّمِ.</p>
<p><span class="font-bold">حُكْمُهُ:</span> <span class="highlight-blue">الْبِنَاءُ دَائِمًا</span> (لَا يَأْتِي مُعْرَبًا أَبَدًا، أَيْ لَا يُقَالُ عَنْهُ أَبَدًا "مَرْفُوعٌ" أَوْ "مَنْصُوبٌ"، بَلْ يُقَالُ "مَبْنِيٌّ عَلَى...").</p>
<p class="text-accent mt-2mm mb-2mm">لِلْفِعْلِ الْمَاضِي ثَلَاثُ حَالَاتٍ لِلْبِنَاءِ تَخْتَلِفُ بِاخْتِلَافِ الضَّمِيرِ الَّذِي يَتَّصِلُ بِهِ:</p>

=== BLOCK 3: أَحْوَالُ بِنَاءِ الْفِعْلِ الْمَاضِي بِالتَّفْصِيلِ ===
(Component: TEMPLATE_C_TABLE.html)
Title: أَحْوَالُ بِنَاءِ الْفِعْلِ الْمَاضِي بِالتَّفْصِيلِ
Content:
<table class="dense-table">
  <thead>
    <tr>
      <th>حَالَةُ الْبِنَاءِ</th>
      <th>الْحَالَةُ وَالسَّبَبُ</th>
      <th>أَمْثِلَةٌ</th>
      <th>إِعْرَابٌ مُفَصَّلٌ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="font-bold text-center">الْبِنَاءُ عَلَى الْفَتْحِ<br>(وَهُوَ الْأَصْلُ)</td>
      <td>
        <ul class="structured-list">
          <li class="list-item-content">إِذَا لَمْ يَتَّصِلْ بِهِ شَيْءٌ (أَوْ اتَّصَلَتْ بِهِ ضَمَائِرُ النَّصْبِ "نَاهِيكَ").</li>
          <li class="list-item-content">إِذَا اتَّصَلَتْ بِهِ تَاءُ التَّأْنِيثِ السَّاكِنَةُ (تْ). <span class="highlight-blue">مُلَاحَظَةٌ:</span> تُكْسَرُ لِمَنْعِ الْتِقَاءِ السَّاكِنَيْنِ إِذَا جَاءَ بَعْدَهَا سَاكِنٌ (<span class="highlight-red">ذَهَبَتِ</span> الْبِنْتُ).</li>
          <li class="list-item-content">إِذَا اتَّصَلَتْ بِهِ أَلِفُ الِاثْنَيْنِ.</li>
        </ul>
      </td>
      <td class="text-center">سَمِعَ ، سَمِعَهَا / شَاهَدَكَ / ذَهَبَتْ ، كَتَبَتِ الدَّرْسَ / ذَهَبَا</td>
      <td>
        <ul class="structured-list">
          <li class="list-item-content"><span class="font-bold">سَمِعَ:</span> فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ الظَّاهِرِ. (هَا): مَفْعُولٌ بِهِ.</li>
          <li class="list-item-content"><span class="font-bold">التَّاءُ:</span> حَرْفُ تَأْنِيثٍ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ.</li>
          <li class="list-item-content"><span class="font-bold">الْأَلِفُ:</span> ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعِ فَاعِلٍ.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td class="font-bold text-center">الْبِنَاءُ عَلَى السُّكُونِ</td>
      <td>
        <ul class="structured-list">
          <li class="list-item-content">إِذَا اتَّصَلَتْ بِهِ تَاءُ الرَّفْعِ الْمُتَحَرِّكَةُ (<span class="highlight-blue">تَ، تِ، تُ</span>).</li>
          <li class="list-item-content">إِذَا اتَّصَلَتْ بِهِ (<span class="highlight-blue">نَا</span>) الدَّالَّةُ عَلَى الْفَاعِلِينَ.</li>
          <li class="list-item-content">إِذَا اتَّصَلَتْ بِهِ نُونُ النِّسْوَةِ (<span class="highlight-blue">نَ</span>).</li>
        </ul>
      </td>
      <td class="text-center">سَافَرْتُ / دَرَسْنَا / كَتَبْنَ</td>
      <td>
        <ul class="structured-list">
          <li class="list-item-content"><span class="font-bold">التَّاءُ:</span> ضَمِيرٌ فِي مَحَلِّ رَفْعِ فَاعِلٍ.</li>
          <li class="list-item-content"><span class="font-bold">(نَا):</span> ضَمِيرٌ فِي مَحَلِّ رَفْعِ فَاعِلٍ. (<span class="highlight-red">تَنْبِيهٌ:</span> إِذَا كَانَتْ مَفْعُولاً بِهِ مِثْلَ: نَصَحَنَا الْمُعَلِّمُ، فَإِنَّ الْفِعْلَ يُبْنَى عَلَى الْفَتْحِ).</li>
          <li class="list-item-content"><span class="font-bold">النُّونُ:</span> ضَمِيرٌ فِي مَحَلِّ رَفْعِ فَاعِلٍ.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td class="font-bold text-center">الْبِنَاءُ عَلَى الضَّمِّ</td>
      <td>
        <ul class="structured-list">
          <li class="list-item-content">إِذَا اتَّصَلَتْ بِهِ وَاوُ الْجَمَاعَةِ فَقَطْ. (<span class="highlight-red font-bold">شَرْطٌ إِمْلَائِيٌّ:</span> تَلْحَقُهَا أَلِفٌ تُسَمَّى أَلِفَ التَّفْرِيقِ).</li>
        </ul>
      </td>
      <td class="text-center">كَتَبُوا / ذَهَبُوا</td>
      <td>
        <ul class="structured-list">
          <li class="list-item-content"><span class="font-bold">الْوَاوُ:</span> ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعِ فَاعِلٍ. وَالْأَلِفُ لِلتَّفْرِيقِ لَا مَحَلَّ لَهَا.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

=== BLOCK 4: فَائِدَةٌ إِمْلَائِيَّةٌ (أَلِفُ التَّفْرِيقِ) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: فَائِدَةٌ إِمْلَائِيَّةٌ (أَلِفُ التَّفْرِيقِ)
Content:
<p class="mb-2mm">يَجِبُ وَضْعُ (أَلِفٍ تُكْتَبُ وَلَا تُنْطَقُ) بَعْدَ وَاوِ الْجَمَاعَةِ الْمُتَّصِلَةِ بِالْأَفْعَالِ لِلتَّفْرِيقِ بَيْنَهَا وَبَيْنَ الْوَاوِ الْأَصْلِيَّةِ.</p>
(Component: TEMPLATE_C_LIST.html)
Items:
[LIST_ITEM_CONTENT]: ✅ كَتَبُوا ، ذَهَبُوا (وَاوُ جَمَاعَةٍ ← نَضَعُ أَلِفًا).
[LIST_ITEM_CONTENT]: ❌ يَدْعُو ، نَرْجُو (وَاوٌ أَصْلِيَّةٌ مِنْ أَصْلِ الْفِعْلِ ← لَا نَضَعُ أَلِفًا).

=== BLOCK 5: تَفْصِيلُ حَالَاتِ الْبِنَاءِ لِلْمُرَاجَعَةِ السَّرِيعَةِ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَفْصِيلُ حَالَاتِ الْبِنَاءِ لِلْمُرَاجَعَةِ السَّرِيعَةِ
Content:
(Component: TEMPLATE_C_LIST.html)
Items:
[LIST_ITEM_CONTENT]: <span class="font-bold text-primary">يُبْنَى عَلَى الْفَتْحِ:</span> الْأَصْلُ (مِثْلَ: <span class="highlight-red">كَتَبَ</span>). وَيَبْقَى كَذَلِكَ مَعَ (تَاءِ التَّأْنِيثِ السَّاكِنَةِ) أَوْ (أَلِفِ الِاثْنَيْنِ).
[LIST_ITEM_CONTENT]: <span class="font-bold text-primary">يُبْنَى عَلَى السُّكُونِ:</span> لِتَخْفِيفِ النُّطْقِ مَعَ ضَمَائِرِ الرَّفْعِ الْمُتَحَرِّكَةِ الْمُتَّصِلَةِ بِهِ (<span class="highlight-blue">تُ، تِ، تَ، نَا الْفَاعِلِينَ، نَ النِّسْوَةِ</span>).
[LIST_ITEM_CONTENT]: <span class="font-bold text-primary">يُبْنَى عَلَى الضَّمِّ:</span> لِمُنَاسَبَةِ حَرَكَةِ الْوَاوِ، إِذَا اتَّصَلَتْ بِهِ (<span class="highlight-blue">وَاوُ الْجَمَاعَةِ</span>).

=== BLOCK 6: نَمَاذِجُ إِعْرَابِيَّةٌ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: نَمَاذِجُ إِعْرَابِيَّةٌ
Content:
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: وَصَلَ
[DETAILS_1]: فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى <span class="highlight-red font-bold">الْفَتْحِ الظَّاهِرِ</span> عَلَى آخِرِهِ (لَمْ يَتَّصِلْ بِهِ شَيْءٌ).
[WORD_2]: كَتَبَتِ الْبِنْتُ
[DETAILS_2]: <span class="highlight-red font-bold">كَتَبَتِ:</span> فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ حَرْفٌ لِلتَّأْنِيثِ مَبْنِيٌّ عَلَى السُّكُونِ لَا مَحَلَّ لَهُ، حُرِّكَتْ بِالْكَسْرِ مَنْعًا لِالْتِقَاءِ السَّاكِنَيْنِ (مَعَ سُكُونِ اللَّامِ فِي الْبِنْت).

(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: شَاهَدَهُ
[DETAILS_1]: فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى <span class="highlight-red font-bold">الْفَتْحِ</span>، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبِ مَفْعُولٍ بِهِ.
[WORD_2]: نَجَحَا
[DETAILS_2]: فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى <span class="highlight-red font-bold">الْفَتْحِ</span> لِاتِّصَالِهِ بِأَلِفِ الِاثْنَيْنِ، وَالْأَلِفُ ضَمِيرٌ فِي مَحَلِّ رَفْعِ فَاعِلٌ.

(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: سَافَرْتُ
[DETAILS_1]: فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى <span class="highlight-red font-bold">السُّكُونِ</span> لِاتِّصَالِهِ بِتَاءِ الرَّفْعِ، وَالتَّاءُ ضَمِيرٌ فِي مَحَلِّ رَفْعِ فَاعِلٌ.
[WORD_2]: حَفِظْنَا
[DETAILS_2]: فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى <span class="highlight-red font-bold">السُّكُونِ</span> لِاتِّصَالِهِ بِـ (<span class="highlight-blue">نَا</span>) الْفَاعِلِينَ، وَهِيَ ضَمِيرٌ فِي مَحَلِّ رَفْعِ فَاعِلٌ.

(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: ذَهَبْنَ
[DETAILS_1]: فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى <span class="highlight-red font-bold">السُّكُونِ</span> لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ، وَالنُّونُ ضَمِيرٌ فِي مَحَلِّ رَفْعِ فَاعِلٌ.
[WORD_2]: نَجَحُوا
[DETAILS_2]: فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى <span class="highlight-red font-bold">الضَّمِّ</span> لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ ضَمِيرٌ فِي مَحَلِّ رَفْعِ فَاعِلٌ، وَالْأَلِفُ لِلتَّفْرِيقِ.

=== BLOCK 7: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: اسْتَخْرِجِ الْفِعْلَ الْمَاضِيَ مِمَّا يَلِي وَبَيِّنْ حَالَةَ بِنَائِهِ، مَعَ ذِكْرِ السَّبَبِ، وَأَعْرِبْهُ إِعْرَابًا تَامًّا: "وَصَلَ الْمُسَافِرُونَ بَعْدَ أَنْ سَافَرُوا لَيْلًا، ثُمَّ اسْتَرَاحُوا".

--- END STREAM ---