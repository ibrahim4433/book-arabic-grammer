# **SESSION 22.0**

[TASK DEFINITION]
Objective: Implement الْفِعْلُ الْمُضَارِعُ وَإِعْرَابُهُ.
File: `pages/22.0_nXX_الْفِعْلُ الْمُضَارِعُ وَإِعْرَابُهُ.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually, instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/22.1_...` if page have a lot of blank space add exam elements from the lesson.
3. Text Content: 100% Arabic with full Harakat.
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
6. Templates: You are forbidden from inventing new HTML tags or classes or template elements. You must map all content using "Jules-workspace/Templates/" components as the STREAM says in suitable way.
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). use "Jules-workspace/id_manager.py" to generate or verify them.
8. **Self-Correction:** Run "Jules-workspace/lint_pages.py" after creating html files. If it fails, you MUST fix the errors (usually inline styles) before submitting.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...) .
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
13. balanced page colors between teal and orange: make sure every page have minimum 1 element in orange instead of all teal
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
15. Exam section always be in the end of the lesson ( in the final page of that lesson), and without the answers!

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 22
[CHAPTER_TITLE]: الْفِعْلُ الْمُضَارِعُ وَإِعْرَابُهُ
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition & Rule ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَعْرِيفُ الْفِعْلِ الْمُضَارِعِ
Content:
<p class="text-accent font-bold">هُوَ الْفِعْلُ الْوَحِيدُ الَّذِي يَكُونُ مُعْرَبًا فِي الْأَصْلِ (<span class="highlight-blue">يَرْفَعُ</span> وَ<span class="highlight-blue">يُنْصَبُ</span> وَ<span class="highlight-blue">يُجْزَمُ</span>)، وَقَدْ يَأْتِي مَبْنِيّاً فِي حَالَتَيْنِ فَقَطْ.</p>
<ul class="structured-list">
  <li class="list-item-content">
    <span class="font-bold text-primary">الْمُعْرَبُ:</span> تَتَغَيَّرُ حَالَةُ آخِرِهِ بِتَغَيُّرِ الْعَوَامِلِ (مَرْفُوعٌ إِذَا لَمْ يَسْبِقْهُ شَيْءٌ، مَنْصُوبٌ إِذَا سَبَقَهُ نَاصِبٌ، مَجْزُومٌ إِذَا سَبَقَهُ جَازِمٌ) بِشَرْطِ أَلَّا تَتَّصِلَ بِهِ نُونُ النِّسْوَةِ أَوْ نُونُ التَّوْكِيدِ.
  </li>
  <li class="list-item-content">
    <span class="font-bold text-primary">الْمَبْنِيُّ:</span> يَلْزَمُ حَالَةً وَاحِدَةً إِذَا اتَّصَلَتْ بِهِ (نُونُ النِّسْوَةِ) أَوْ (إِحْدَى نُونَيِ التَّوْكِيدِ الثَّقِيلَةِ أَوِ الْخَفِيفَةِ).
  </li>
</ul>

=== BLOCK 3: The Core Matrix (Raf' and Nasb Signs) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: جَدْوَلُ عَلَامَاتِ الرَّفْعِ وَالنَّصْبِ لِلْمُعْرَبِ
Content:
<div class="block-body p-0">
  <table class="dense-table">
    <thead>
      <tr>
        <th>نَوْعُ الْفِعْلِ</th>
        <th>حَالَةُ الرَّفْعِ</th>
        <th>حَالَةُ النَّصْبِ</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="font-bold">صَحِيحُ الْآخِرِ</td>
        <td>الضَّمَّةُ الظَّاهِرَةُ</td>
        <td>الْفَتْحَةُ الظَّاهِرَةُ</td>
      </tr>
      <tr>
        <td class="font-bold">مُعْتَلُّ الْآخِرِ (بِالْوَاوِ أَوِ الْيَاءِ)</td>
        <td>الضَّمَّةُ الْمُقَدَّرَةُ (لِلثِّقَلِ، أَيْ ثِقَلِ النُّطْقِ)</td>
        <td>الْفَتْحَةُ الظَّاهِرَةُ (لِخِفَّتِهَا عَلَى الْوَاوِ وَالْيَاءِ)</td>
      </tr>
      <tr>
        <td class="font-bold">مُعْتَلُّ الْآخِرِ (بِالْأَلِفِ)</td>
        <td>الضَّمَّةُ الْمُقَدَّرَةُ (لِلتَّعَذُّرِ، أَيِ الِاسْتِحَالَةِ)</td>
        <td>الْفَتْحَةُ الْمُقَدَّرَةُ (لِلتَّعَذُّرِ)</td>
      </tr>
      <tr>
        <td class="font-bold">الْأَفْعَالُ الْخَمْسَةُ</td>
        <td>ثُبُوتُ النُّونِ</td>
        <td>حَذْفُ النُّونِ</td>
      </tr>
    </tbody>
  </table>
</div>

=== BLOCK 4: Deep Dive (Examples of Raf' and Nasb) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَمْثِلَةٌ وَنَمَاذِجُ إِعْرَابِيَّةٌ لِلرَّفْعِ وَالنَّصْبِ
Content:
<ul class="structured-list">
  <li class="list-item-content">
    <span class="font-bold text-primary">صَحِيحُ الْآخِرِ:</span><br>
    - يَكْتُبُ: فِعْلٌ مُضَارِعٌ مَرْفُوعٌ (لِخُلُوِّهِ مِنْ نَاصِبٍ وَجَازِمٍ) وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ.<br>
    - لَنْ <span class="highlight-red">أَهْرُبَ</span>: فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِـ (لَنْ) وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ.
  </li>
  <li class="list-item-content">
    <span class="font-bold text-primary">مُعْتَلُّ الْآخِرِ (بِالْوَاوِ أَوِ الْيَاءِ):</span><br>
    - يَدْعُو / يَرْمِي: مَرْفُوعٌ بِالضَّمَّةِ الْمُقَدَّرَةِ (مَنَعَ ظُهُورَهَا الثِّقَلُ فِي النُّطْقِ، فَلَا نَسْتَطِيعُ قَوْلَ: يَدْعُوُ).<br>
    - كَيْ <span class="highlight-red">أَدْعُوَ</span> / كَيْ <span class="highlight-red">أَرْمِيَ</span>: مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ لِسُهُولَةِ نُطْقِهَا.
  </li>
  <li class="list-item-content">
    <span class="font-bold text-primary">مُعْتَلُّ الْآخِرِ (بِالْأَلِفِ):</span><br>
    - يَهْوَى / يَسْعَى: مَرْفُوعٌ بِالضَّمَّةِ الْمُقَدَّرَةِ (مَنَعَ ظُهُورَهَا التَّعَذُّرُ اسْتِحَالَةُ نُطْقِ حَرَكَةٍ عَلَى الْأَلِفِ السَّاكِنَةِ).<br>
    - كَيْ يَهْوَى / لَنْ <span class="highlight-red">يَسْعَى</span>: مَنْصُوبٌ بِالْفَتْحَةِ الْمُقَدَّرَةِ لِلتَّعَذُّرِ.
  </li>
  <li class="list-item-content">
    <span class="font-bold text-primary">الْأَفْعَالُ الْخَمْسَةُ (كُلُّ مُضَارِعٍ اتَّصَلَتْ بِهِ أَلِفُ الِاثْنَيْنِ، أَوْ وَاوُ الْجَمَاعَةِ، أَوْ يَاءُ الْمُخَاطَبَةِ):</span><br>
    - يَذْهَبَانِ / يَذْهَبُونَ / تَذْهَبِينَ: مَرْفُوعٌ بِثُبُوتِ النُّونِ (وَالْأَلِفُ/الْوَاوُ/الْيَاءُ ضَمِيرُ فَاعِلٍ).<br>
    - لَنْ <span class="highlight-red">يَرْجِعُوا</span> / لَنْ <span class="highlight-red">تَعُودِي</span>: مَنْصُوبٌ بِحَذْفِ النُّونِ (وَالْوَاوُ فَاعِلٌ).
  </li>
</ul>

=== BLOCK 5: Deep Dive (Nasb Tools) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَدَوَاتُ النَّصْبِ الْأَسَاسِيَّةُ
Content:
<p class="text-accent font-bold">يُنْصَبُ الْفِعْلُ الْمُضَارِعُ إِذَا سُبِقَ بِـ:</p>
<ul class="structured-list">
  <li class="list-item-content"><span class="highlight-blue font-bold">أَنْ:</span> حَرْفٌ نَاصِبٌ مَصْدَرِيٌّ. (يَجِبُ أَنْ <span class="highlight-red">يَمْشِيَ</span> بِسُرْعَةٍ)</li>
  <li class="list-item-content"><span class="highlight-blue font-bold">لَنْ:</span> حَرْفُ نَفْيٍ وَنَصْبٍ وَاسْتِقْبَالٍ يُفِيدُ تَأْكِيدَ النَّفْيِ فِي الْمُسْتَقْبَلِ. (لَنْ <span class="highlight-red">أَهْرُبَ</span> مِنَ الْمَعْرَكَةِ)</li>
  <li class="list-item-content"><span class="highlight-blue font-bold">كَيْ:</span> حَرْفٌ مَصْدَرِيٌّ وَنَصْبٌ وَتَعْلِيلٌ (تُفِيدُ السَّبَبَ). (ذَاكِرْ كَيْ <span class="highlight-red">تَنْجَحَ</span> / اِسْقِ الزَّرْعَ كَيْ <span class="highlight-red">يَنْمُوَ</span>)</li>
  <li class="list-item-content"><span class="highlight-blue font-bold">إِذَنْ:</span> حَرْفُ جَوَابٍ وَجَزَاءٍ. (تَقُولُ: سَأَزُورُكَ، فَأَقُولُ: إِذَنْ <span class="highlight-red">أُكْرِمَكَ</span>).</li>
</ul>

=== BLOCK 6: Jazm Rules Matrix ===
(Component: TEMPLATE_C_BLOCK.html)
Title: جَزْمُ الْفِعْلِ الْمُضَارِعِ
Content:
<p class="text-accent font-bold">يُجْزَمُ الْمُضَارِعُ إِذَا سُبِقَ بِأَدَاةٍ جَازِمَةٍ، أَوْ وَقَعَ فِي جَوَابِ الطَّلَبِ. وَأَدَوَاتُ الْجَزْمِ هِيَ أَرْبَعَةُ أَحْرُفٍ تَجْزِمُ فِعْلًا وَاحِدًا: (<span class="highlight-blue">لَمْ</span>، <span class="highlight-blue">لَمَّا</span>، <span class="highlight-blue">لَامُ الْأَمْرِ</span>، <span class="highlight-blue">لَا النَّاهِيَةُ</span>).</p>
<div class="block-body p-0">
  <table class="dense-table">
    <thead>
      <tr>
        <th>نَوْعُ الْفِعْلِ</th>
        <th>عَلَامَةُ الْجَزْمِ</th>
        <th>مِثَالٌ وَنَمُوذَجُ إِعْرَابٍ</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="font-bold">صَحِيحُ الْآخِرِ</td>
        <td>السُّكُونُ</td>
        <td>لَمْ <span class="highlight-red">يَدْرُسْ</span>: فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِـ(لَمْ) وَعَلَامَةُ جَزْمِهِ السُّكُونُ الظَّاهِرُ.</td>
      </tr>
      <tr>
        <td class="font-bold">مُعْتَلُّ الْآخِرِ</td>
        <td>حَذْفُ حَرْفِ الْعِلَّةِ</td>
        <td>لَا <span class="highlight-red">تَدْنُ</span> (أَصْلُهَا تَدْنُو): مَجْزُومٌ وَعَلَامَةُ جَزْمِهِ حَذْفُ حَرْفِ الْعِلَّةِ (الْوَاوِ). لَمْ <span class="highlight-red">يَسْعَ</span> (أَصْلُهَا يَسْعَى): مَجْزُومٌ بِحَذْفِ الْعِلَّةِ.</td>
      </tr>
      <tr>
        <td class="font-bold">الْأَفْعَالُ الْخَمْسَةُ</td>
        <td>حَذْفُ النُّونِ</td>
        <td>لَمْ <span class="highlight-red">يَهْرُبُوا</span>: مَجْزُومٌ وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ (وَالْوَاوُ فَاعِلٌ).</td>
      </tr>
    </tbody>
  </table>
</div>

=== BLOCK 7: Extra Info (Warning) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[WARNING_TEXT]:  تَنْبِيهٌ مُهِمٌّ جِدّاً (الْفَرْقُ بَيْنَ لَا النَّاهِيَةِ وَلَا النَّافِيَةِ):<br>كَثِيرٌ مِنَ الطُّلَّابِ يَخْلِطُونَ بَيْنَهُمَا:<br>
• <span class="font-bold">لَا النَّاهِيَةُ (جَازِمَةٌ):</span> فِيهَا طَلَبٌ وَتَرْكٌ، كَأَنِّي أَمْنَعُكَ مِنْ شَيْءٍ مُبَاشَرَةً. (لَا تَتَكَلَّمْ فِي الْفَصْلِ، لَا تَلْعَبْ). الْفِعْلُ بَعْدَهَا مَجْزُومٌ بِالسُّكُونِ.<br>
• <span class="font-bold">لَا النَّافِيَةُ (غَيْرُ جَازِمَةٍ):</span> مُجَرَّدُ إِخْبَارٍ وَنَفْيٍ لِحُصُولِ الْفِعْلِ، لَا طَلَبَ فِيهَا، وَيَبْقَى الْفِعْلُ بَعْدَهَا مَرْفُوعاً كَمَا هُوَ. (أَنَا لَا يَتَكَلَّمُ زَمِيلِي فِي الْفَصْلِ، الْعَاقِلُ لَا يَكْذِبُ). يَكْذِبُ: مَرْفُوعٌ بِالضَّمَّةِ.

=== BLOCK 8: Evaluation (Exam) ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: أَعْرِبِ الْفِعْلَ الْمُضَارِعَ فِي الْجُمَلِ التَّالِيَةِ: كَيْ يَنْجَحَ الطَّالِبُ لَا بُدَّ أَنْ يَدْرُسَ.

=== BLOCK 9: Evaluation (Exam) ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: بَيِّنْ نَوْعَ (لَا) فِي الْجُمْلَتَيْنِ التَّالِيَتَيْنِ، وَأَعْرِبِ الْفِعْلَ بَعْدَهَا: لَا تَكْذِبْ، الْمُؤْمِنُ لَا يَكْذِبُ.

--- END STREAM ---