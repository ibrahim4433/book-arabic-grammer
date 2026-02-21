# **SESSION 09.0**

[TASK DEFINITION]
Objective: Implement Lesson 09 - Morphological Balance.
File: `pages/09.0_nxx_almizan.html`
Reference: Follow patterns in `BOOK_RULES.md` and `styles/main.css`.

[CONSTRAINTS & PROTOCOLS]
1. Page Breaking: Use `python3 "Jules-workspace/verify_layout.py"` after every block. If "FULL" or "OVERFLOW", close the current file (e.g., `09.0`) and continue in `pages/09.1_n29_almizan.html`.
2. Content: 100% Arabic with full Harakat.
3. Highlighting: Use `.highlight-red` for primary focus words (e.g., weights) and `.highlight-blue` for secondary focus.
4. Definitions: Must use `.text-accent` class for the definition text.
5. Applied Examples: Format the Q&A section as a dense table or list of `.exercise-question` blocks for clarity.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER)
Title: المِيزَانُ الصَّرْفِيُّ
Lesson: ٩

=== BLOCK 2: Definition ===
(Component: TEMPLATE_C_BLOCK)
Title: تَعْرِيفُ المِيزَانِ
Content: <p class="text-accent m-0">هُوَ مِقْيَاسٌ لِمَعْرِفَةِ حُرُوفِ الكَلِمَةِ، يَتَأَلَّفُ مِنْ ثَلَاثَةِ أَحْرُفٍ تُقَابِلُ الأُصُولَ الثَّلَاثَةَ الَّتِي تَتَكَوَّنُ مِنْهَا أَغْلَبُ الكَلِمَاتِ العَرَبِيَّةِ، عَلَى النَّحْوِ الآتِي:</p>

=== BLOCK 3: The 3-Letter Matrix ===
(Component: TEMPLATE_C_TABLE)
Title: مِيزَانُ الثُّلَاثِيِّ المُجَرَّدِ
Table Data:
Header: حُرُوفُ المِيزَانِ | فَاءُ الفِعْلِ | عَيْنُ الفِعْلِ | لَامُ الفِعْلِ
Row 1: الكَلِمَةُ | ضَـ | ـرَ | بَ
Row 2: المِيزَانُ الصَّرْفِيُّ | فَـ | ـعَ | لَ

=== BLOCK 4: Basic Rules ===
(Component: TEMPLATE_C_BLOCK)
Title: قَوَاعِدُ أَسَاسِيَّةٌ
Content:
<ul class="structured-list">
  <li>
    <span class="marker">•</span>
    <span class="list-item-content">ضَبْطُ بِنْيَةِ الكَلِمَةِ المَوْزُونَةِ، بِالحَرَكَاتِ وَالسَّكَنَاتِ، يُطَابِقُ ضَبْطَ الوَزْنِ الصَّرْفِيِّ، وَعَدَدُ حُرُوفِ الكَلِمَةِ المَوْزُونَةِ يُسَاوِي عَدَدَ حُرُوفِ المِيزَانِ.</span>
  </li>
  <li>
    <span class="marker">•</span>
    <span class="list-item-content">إِذَا كَانَتْ حُرُوفُ الكَلِمَةِ الأَصْلِيَّةُ أَرْبَعَةَ حُرُوفٍ، فَإِنَّنَا نُكَرِّرُ اللَّامَ فِي آخِرِ المِيزَانِ الصَّرْفِيِّ. فَكَلِمَةُ (<span class="highlight-red">بَعْثَرَ</span>) تُوزَنُ كَمَا يَلِي:</span>
  </li>
</ul>

=== BLOCK 5: The 4-Letter Matrix ===
(Component: TEMPLATE_C_TABLE)
Title: مِيزَانُ الرُّبَاعِيِّ المُجَرَّدِ
Table Data:
Header: حُرُوفُ المِيزَانِ | فَاءُ الفِعْلِ | عَيْنُ الفِعْلِ | لَامُ الفِعْلِ | الحَرْفُ الرَّابِعُ
Row 1: الكَلِمَةُ | بَـ | ـعْ | ثَـ | ـرَ
Row 2: المِيزَانُ الصَّرْفِيُّ | فَـ | ـعْ | لَـ | لَ
Text below table: <p class="m-0 mt-2mm">وَنَزِيدُ لَامَيْنِ فِي آخِرِ المِيزَانِ إِذَا كَانَ الحَرْفَانِ الزَّائِدَانِ مِنْ أَصْلِ الكَلِمَةِ؛ فَوَزْنُ (<span class="highlight-red">غَضَنْفَر</span>) يُصْبِحُ (<span class="highlight-blue">فَعَلَّل</span>)، وَوَزْنُ (<span class="highlight-red">زَبَرْجَد</span>) يُصْبِحُ (<span class="highlight-blue">فَعَلَّل</span>).</p>

=== BLOCK 6: Ziyadah Rules ===
(Component: TEMPLATE_C_BLOCK)
Title: مِيزَانُ الكَلِمَاتِ المَزِيدَةِ
Content:
<p class="m-0 mb-2mm">عِنْدَمَا يَكُونُ فِي الكَلِمَةِ حَرْفٌ زَائِدٌ، نَزِنُهَا عَلَى النَّحْوِ الآتِي:</p>
<ul class="structured-list">
  <li>
    <span class="marker">١</span>
    <span class="list-item-content">إِذَا كَانَ الحَرْفُ الزَّائِدُ نَاتِجًا عَنْ تَكْرِيرِ حَرْفٍ مِنْ حُرُوفِ الكَلِمَةِ الأَصْلِيَّةِ، كَرَّرْنَا مَا يُقَابِلُهُ فِي المِيزَانِ، فَوَزْنُ (<span class="highlight-red">سَبَّحَ</span>) يُصْبِحُ (<span class="highlight-blue">فَعَّلَ</span>)، وَوَزْنُ (<span class="highlight-red">عَلَّمَ</span>) يُصْبِحُ (<span class="highlight-blue">فَعَّلَ</span>).</span>
  </li>
  <li>
    <span class="marker">٢</span>
    <span class="list-item-content">وَإِذَا كَانَ الحَرْفُ الزَّائِدُ حَرْفًا غَيْرَ أَصْلِيٍّ وَغَيْرَ مُكَرَّرٍ، فَإِنَّنَا نَزِنُ الأُصُولَ فَقَطْ بِمَا يُقَابِلُهَا فِي المِيزَانِ، ثُمَّ نَذْكُرُ الحُرُوفَ الزَّائِدَةَ كَمَا هِيَ فِي الكَلِمَةِ، فَوَزْنُ (<span class="highlight-red">كَاتَبَ</span>) يُصْبِحُ (<span class="highlight-blue">فَاعَلَ</span>)، وَوَزْنُ (<span class="highlight-red">اسْتَفْتَحَ</span>) يُصْبِحُ (<span class="highlight-blue">اسْتَفْعَلَ</span>).</span>
  </li>
</ul>

=== BLOCK 7: Special Rules ===
(Component: TEMPLATE_C_BLOCK)
Title: أَحْكَامٌ خَاصَّةٌ
Content:
<ul class="structured-list">
  <li>
    <span class="marker">•</span>
    <span class="list-item-content"><strong>الحَرْفُ المُعْتَلُّ:</strong> يُعْتَبَرُ كَأَنَّهُ صَحِيحٌ فَيُقَابَلُ بِنَظِيرِهِ فِي المِيزَانِ. فَوَزْنُ (<span class="highlight-red">وَعَدَ</span>) يُصْبِحُ (<span class="highlight-blue">فَعَلَ</span>). وَإِنْ كَانَ سَاكِنًا فِي الكَلِمَةِ، فَإِنَّهُ يُعْتَبَرُ مُتَحَرِّكًا فِي المِيزَانِ، كَمَا لَوْ كَانَ صَحِيحًا، فَوَزْنُ (<span class="highlight-red">قَامَ</span>) يُصْبِحُ (<span class="highlight-blue">فَعَلَ</span>). وَعِنْدَمَا تَكُونُ عَيْنُ الكَلِمَةِ حَرْفًا مُعْتَلًّا، فَإِنَّنَا نَعُدُّ العَيْنَ مُتَحَرِّكَةً فِي المِيزَانِ، وَإِنْ كَانَتْ سَاكِنَةً فِي المَوْزُونِ؛ وَنَعْتَبِرُ مَا قَبْلَ هَذِهِ العَيْنِ سَاكِنًا فِي المِيزَانِ، وَإِنْ كَانَ مُتَحَرِّكًا فِي المَوْزُونِ (عَلَى وَزْنِ الفِعْلِ الصَّحِيحِ)، فَوَزْنُ (<span class="highlight-red">يَقُولُ</span>) يُصْبِحُ (<span class="highlight-blue">يَفْعُلُ</span>)، وَوَزْنُ (<span class="highlight-red">يَقُودُ</span>) يُصْبِحُ (<span class="highlight-blue">يَفْعُلُ</span>). (عَلَى وَزْنِ الفِعْلِ الصَّحِيحِ مِثْل "<span class="highlight-red">يَكْتُبُ</span>").</span>
  </li>
  <li>
    <span class="marker">•</span>
    <span class="list-item-content"><strong>المُضَعَّفُ الثُّلَاثِيُّ:</strong> الحَرْفُ المُشَدَّدُ حَرْفَانِ (عَيْنٌ وَلَامٌ)، لَا يُشَدَّدُ فِي المِيزَانِ، فَوَزْنُ (<span class="highlight-red">شَدَّ</span>) يُصْبِحُ (<span class="highlight-blue">فَعَلَ</span>).</span>
  </li>
  <li>
    <span class="marker">•</span>
    <span class="list-item-content"><strong>الحَذْفُ:</strong> إِذَا حَصَلَ حَذْفٌ فِي الكَلِمَةِ، نَحْذِفُ مَا يُقَابِلُهُ فِي المِيزَانِ، فَوَزْنُ (<span class="highlight-red">قُلْ</span>) يُصْبِحُ (<span class="highlight-blue">فُلْ</span>)، وَوَزْنُ (<span class="highlight-red">ارْمِ</span>) يُصْبِحُ (<span class="highlight-blue">افْعِ</span>).</span>
  </li>
</ul>

=== BLOCK 8: Applied Examples ===
(Component: TEMPLATE_C_TABLE)
Title: أَمْثِلَةٌ تَطْبِيقِيَّةٌ
Table Data:
Header: الكَلِمَةُ | الوَزْنُ || الكَلِمَةُ | الوَزْنُ
Row 1: قُلْتُ | فُلْتُ || لَمْ يَرَ | لَمْ يَفِ
Row 2: عُدْ | فُعْ || يَنْقَضِي | يَنْفَعِلُ
Row 3: ثِقَةٌ | عِلَةٌ || حَاجٌ | فَاعٌ
Row 4: بُرُوقٌ | فُعُولٌ || كُنْ | فُلْ
Row 5: غَدَوْتُ | فَعَلْتُ || تَخَذْتُ | فَعَلْتُ
Row 6: الأَمَانِي | الأَفَاعِلُ || عِشْنَا | فِلْنَا
Row 7: أَوْهَتْ | أَفْعَتْ || تَغَطَّتْ | تَفَعَّتْ
Row 8: عَادَ | فَعَلَ || رِئَاسَة | فِعَالَة
Row 9: تَسْتَقِلُّ | تَسْتَفْعِلُ || تَذُوبُ | تَفْعُلُ
Row 10: حَرَّتْ | فَلَّتْ || عِشْ | فِلْ
Row 11: الْغَنِّ | الْفَعْلِ || أَغْرَانِي | أَفْعَلَنِي
Row 12: أَرْجُو | أَفْعُلُ || أَشْتَهِي | أَفْتَعِلُ
Row 13: رَاحَ | فَعَلَ || يَئِزُّ | يَفِلُّ
Row 14: خَلَا | فَعَلَ || أُسْطُورَة | أُفْعُولَة
Row 15: قُلْ | فُلْ || لَاقَتْنِي | فَاعَتْنِي
Row 16: سَلْ | فَلْ || يَنْصَبَانِي | يَنْفَعِلَانِي

=== BLOCK 9: Exam ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: زِنْ الكَلِمَاتِ الآتِيَةَ: (اسْتَغْفَرَ، دَحْرَجَ، سَعَى).

--- END STREAM ---
