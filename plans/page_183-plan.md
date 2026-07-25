# **SESSION 183**

[TASK DEFINITION]
Objective: Implement page 183.
File: `pages/page_183.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`, `.highlight-green` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   **Rule:** NO INLINE STYLES.
*   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
*   **Mapping:** `style="width: 20%"` -> `class="w-20pct"`, etc.
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). The ID MUST be applied to the `<div>` tag that replaced the `<section>` tag. Use "Jules-workspace/id_manager.py".
8. **Self-Correction:** Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...).
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal.
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html`.
15. Exam section always be in the end of the lesson (in the final page of that lesson) ,and without the answers!

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 183
[CHAPTER_TITLE]: page 183
[CATEGORY_HEADER]: 183
[SECTION_HEADER]: 183
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Cut Content Continuation (I'rab) ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
Inner Component: TEMPLATE_C_IRAB.html
[BLOCK_TITLE]: الإعراب
[TARGET_WORD]: (وعلامةُ رَفْعِهِ)
[IRAB_ANALYSIS]: وعلامةُ رَفْعِهِ الضَّمَّةُ الْمُقَدَّرَةُ على الياء، مَنَعَ ظُهُورَها الثقل.

=== BLOCK 3: I'rab Details ===
(Component: TEMPLATE_C_BLOCK.html)
Content:
<div class="flex flex-col gap-2mm">
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">ناسيا</div>
      <div class="irab-details">حال منصوبة.</div>
  </div>
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">ما</div>
      <div class="irab-details">اسم مَوْصُولٌ مَبْنِي على السكون في مَحَلَّ نَصْب،ِ مَفْعُولُ به لاسم الفاعل (ناسيا).</div>
  </div>
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">الإعراب : زاهدا</div>
      <div class="irab-details">حال منصوبة.</div>
  </div>
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">فيما</div>
      <div class="irab-details">في، حَرْفُ جر. ما ، اسم مَوْصُولُ مَبْنِي على السُّكُون فِي مَحَلَ جَرٍّ بِحَرْفِ الجَرِ</div>
  </div>
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">سَيَأْتِي</div>
      <div class="irab-details">فِعْلَ مُضَارِعُ مَرْفُوع ، قَد:ْ حَرْفُ تحقيق.</div>
  </div>
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">مَضَى</div>
      <div class="irab-details">فعل ماض، مَبْنِي على الفَتْحَةِ المُقَدَّرَةِ على الآلِفِ مَنَعَ ظُهُورَهَا التَّعَذِّرُ</div>
  </div>
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">جملة (سَيَأْتِي)</div>
      <div class="irab-details">صِلَةً الموصول، لا محل لها مِنَ الإعراب</div>
  </div>
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">جملة (قَدْ مَضَى)</div>
      <div class="irab-details">صِلَةُ الْمَوْصُول،ِ لَا مَحَلَّ لها مِنَ الإعراب.</div>
  </div>
</div>

=== BLOCK 4: Verse 15 ===
(Component: TEMPLATE_C_POEM.html)
Title: البيت الخامس عشر
Poet: جبران خليل جبران
Right Hemistich: وَسُكُوتُ اللَّيْلِ بَحْرٌ مَوْجُهُ
Left Hemistich: فِي مِسْمَعِك

=== BLOCK 5: Explanation & Idea Verse 15 ===
(Component: TEMPLATE_C_TABLE.html)
Header 1: الشرح
Header 2: الفكرة
Header 3: البلاغة
Row 1: إِنْ هَجَرْتَ ماضيكَ ومُسْتَقْبَلَكَ أَلْفَيْتَ هُدُوءَ اللَّيْلِ بَحْرًا تَعْزِفُ أَمْوَاجُهُ أَلْحَانًا تَنْسَكِبُ فِي مَسْمِعَيْك.َ | الدَّعوة إلى الحياة الفِطْرِيَّةِ النَّقِيَّةِ (الدَّعوة إلى تأمل الطبيعة، والانْصِرَافِ عَنِ الدُّنيا) | (سُكُوتُ اللَّيْلِ بَحْرٌ): تشبية بليغ

=== BLOCK 6: I'rab Verse 15 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الإعراب
Content:
<div class="flex flex-col gap-2mm">
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">وَسُكُوتُ</div>
      <div class="irab-details">الواو، واو الحَال.ِ سُكُوت،ُ مُبْتَدَأٌ مَرْفُوعُ</div>
  </div>
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">اللَّيْلِ</div>
      <div class="irab-details">مُضَافٌ إليهِ مَجْرُورُ</div>
  </div>
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">بَحْرٌ</div>
      <div class="irab-details">خَبَرٌ مَرْفُوعٌ</div>
  </div>
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">مَوْجُهُ</div>
      <div class="irab-details">مُبْتَدَأٌ مَرْفُوع، وعلامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَة.ُ والهاء، ضميرٌ مُتَّصِلٌ مَبْنِي على الضَّمّ فِي مَحَلِّ جَر،ٍ مُضَاف إليه.</div>
  </div>
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">فِي مِسْمَعِك</div>
      <div class="irab-details">في حَرْفُ جَرٍّ مِسْمَعِك،َ اسم مَجْرُور، وعلامةُ جَرَهِ الكَسْرَةُ الظَّاهِرَةُ والجَارُ وَالْمَجْرُورُ مُتَعَلِّقَانَ بِخَبَرِ محذوف والكاف، ضميرٌ مُتَصِل في محل جَرّ،ٍ مُضَافَ إِلَيْه.ِ</div>
  </div>
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">جملة (سُكُوتُ اللَّيْلِ بَحْرٌ)</div>
      <div class="irab-details">حالية، محلها النصب</div>
  </div>
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">جملة (مَوْجُهُ فِي مِسْمَعِك)</div>
      <div class="irab-details">صِفَة،ٌ مَحَلَّهَا الرَّفْع.ُ</div>
  </div>
</div>

=== BLOCK 7: Verse 16 ===
(Component: TEMPLATE_C_POEM.html)
Title: البيت السادس عشر
Poet: جبران خليل جبران
Right Hemistich: وَبِصَدْرِ اللَّيْلِ قَلْبٌ خَافِقٌ
Left Hemistich: فِي مَضْجَعِك

=== BLOCK 8: Explanation, Idea & Vocabulary Verse 16 ===
(Component: TEMPLATE_C_TABLE.html)
Header 1: المفردات والشرح
Header 2: الفكرة
Header 3: البلاغة
Row 1: <span class="font-bold">مَضْجَعِك:</span> موضع الضُّجُوع، وهو وضع الجنب على الأرض. <span class="font-bold">الشرح:</span> تجد في جَوْفِ اللَّيْلِ قَلْبًا يَخْفِقُ مُوَقِّعًا دَقَّاتِهِ مَعَ دَقَّاتِ قَلْبِكَ النَّابِضِ فِي جَسَدِكَ الْمُلْقَى على بساط الأَرْضِ الْأَخْضَرِ | الدَّعوة إلى الحياةِ الفِطْرِيَّةِ النَّقِيَة.ِ (الدَّعوةُ إِلَى تَأْمُّلِ الطبيعة، والانْصِرَافِ عَنِ الدنيا) | (صَدْرِ اللَّيْلِ): استعارة مكنية

=== BLOCK 9: I'rab Verse 16 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الإعراب
Content:
<div class="flex flex-col gap-2mm">
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">اللَّيْلِ</div>
      <div class="irab-details">مُضَاف إليهِ مَجْرُورٌ</div>
  </div>
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">قَلْبٌ</div>
      <div class="irab-details">مُبْتَدَأٌ مُؤَخَرُ مَرْفُوعٌ</div>
  </div>
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">خَافِقٌ</div>
      <div class="irab-details">صِفَةٌ مَرْفُوعَةٌ</div>
  </div>
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">فِي مَضَجَعِكَ</div>
      <div class="irab-details">في، حَرْفُ جر. مَضْجَعِك،َ اسمٌ مَجْرُور، وعلامَةُ جَرَّهِ الكَسْرَةُ الظَّاهِرَةُ والجار والمَجْرُورُ مُتَعَلقان باسم الفاعل (خافِق). والكاف، ضميرٌ مُتَصِلَ مَبْنِي على الفتحة، وسُكِنَ لِلضَّرُورَةِ الشِّعْرِيَّة،ِ في محل جر، مُضَاف إليه.</div>
  </div>
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">جملة (بِصَدْرِ اللَّيْلِ قَلْبُ)</div>
      <div class="irab-details">حاليَّة،ٌ مَحَلُّهَا النَّصْب.ُ</div>
  </div>
</div>

=== BLOCK 10: Verse 17 ===
(Component: TEMPLATE_C_POEM.html)
Title: البيت السابع عشر
Poet: جبران خليل جبران
Right Hemistich: أَعْطِنِي النَّايَ وَغَنِّ
Left Hemistich: وَانْسَ دَاءً وَدَواء

=== BLOCK 11: Explanation & Idea Verse 17 ===
(Component: TEMPLATE_C_TABLE.html)
Header 1: الشرح
Header 2: الفكرة
Header 3: البلاغة
Row 1: أَقْبل على الفن، لِأَنَّهُ الطَّريقُ الوَحِيدة التي تُخَلَّصُكَ مِنْ بَرَاثِنِ وَاقِعِك،َ وَتُدْنِيكَ مِنْ عالم الغاب المثالي الفَاضِل،ِ فَأَمَامَ تَرَاتِيلِ الغناء وترانيم الموسيقا يَنْبَغِي لَكَ أَنْ تَنْسَى المَرَضَ والدَّواء، وَأَلَّا تَخْشَى الْمَوْتَ فَلَا مُوتَ مَعَ الغناء؛ لأَنَّهُ عِلاج وشفاء لِكُلِّ داء. | تَأْكِيدُ دَوْرِ الفَنِّ فِي الحَيَاةِ الإنسانية | (داء، دواء) طباق إيجاب

=== BLOCK 12: I'rab Verse 17 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الإعراب
Content:
<div class="flex flex-col gap-2mm">
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">وانس</div>
      <div class="irab-details">الواو، حَرْفُ عَطْفٍ انْسَ فِعْلُ أَمْرِ مَبْنِي على حَذْفِ حَرْفِ العِلَّةِ</div>
  </div>
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">داءً</div>
      <div class="irab-details">مَفْعُولُ بِهِ مَنْصُوبُ</div>
  </div>
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">وَدَواء</div>
      <div class="irab-details">الواو، حَرْفُ عَطْفٍ دواء، اسمٌ مَعْطُوف منصوب، وعلامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَة،ُ وَسُكِّنَ لِلضَّرُورَةِ الشِّعْرِيَّةِ</div>
  </div>
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">جملة (انْسَ)</div>
      <div class="irab-details">مَعْطُوفَة،ٌ لَا مَحَلَّ لَهَا مِنَ الإعراب.</div>
  </div>
</div>

=== BLOCK 13: Verse 18 ===
(Component: TEMPLATE_C_POEM.html)
Title: البيت الثامن عشر
Poet: جبران خليل جبران
Right Hemistich: إِنَّمَا النَّاسُ سُطُور
Left Hemistich: كُتِبَتْ لَكِنْ بِمَاء

=== BLOCK 14: Explanation & Idea Verse 18 ===
(Component: TEMPLATE_C_TABLE.html)
Header 1: الشرح
Header 2: البلاغة
Row 1: الغناء رَمْزُ الْبَقَاءِ وَالخُلُودِ الْمُطْلَقِ في عالم الغَابِ الفَاضِل،ِ أَمَّا النَّاسُ الَّذِينَ يَعِيشُونَ فِي الوَاقِعِ الفَانِي فَمَا هُمْ إِلَّا سُطُورٌ سَتُمْحَى عِنْدَ انْتِهاء آجالها، لأَنَّهَا دُوِّنَتْ بَحِبْرٍ مائي سرعان ما يَجِفُ ويتلاشى ويَزُولُ | (النَّاسُ سطور) : تشبية بليغ

=== BLOCK 15: Warning / Idea Verse 18 ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: الفكرة
Content: تَأْكِيدُ زَوَالِ الإِنْسَانِ

=== BLOCK 16: I'rab Verse 18 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الإعراب
Content:
<div class="flex flex-col gap-2mm">
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">إِنَّمَا</div>
      <div class="irab-details">مَكْفُوفَةٌ وكافة</div>
  </div>
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">النَّاسُ</div>
      <div class="irab-details">مُبْتَدَأٌ مَرْفُوع</div>
  </div>
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">سطور</div>
      <div class="irab-details">خَبَرٌ مَرْفُوع، وعلامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ</div>
  </div>
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">كُتِبَتْ</div>
      <div class="irab-details">فِعْلَ مَاضٍ مَبْنِي لِلْمَجْهُولِ مَبْنِي على الفَتْحَةِ؛ لاتِّصَالِهِ بِنَاءِ التَّأْنِيثِ السَّاكِنَةِ وَالتَّاء،ُ حَرْفُ تَأْنِيث لَا مَحَلَّ لَهُ مِنَ الإعراب</div>
  </div>
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">لَكِنْ</div>
      <div class="irab-details">حَرْفُ استدراك.</div>
  </div>
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">بِمَاء</div>
      <div class="irab-details">الباء، حَرْفُ جر. مَاء،ُ اسمٌ مَجْرُور، وعلامَةُ جَرّهِ الكَسْرَةُ الظَّاهِرَةُ وَسُكِّنَ لِلضَّرُورَةِ الشِّعْرِيَّةِ مُتَعَلَّقان بِفِعْلِ مَحْذُوفِ تَقْدِيرُه:ُ (كُتِبَتْ)، دَلَّ عَلَيْهِ السِّيَاق.ُ</div>
  </div>
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">جملة (الناس سطور)</div>
      <div class="irab-details">استئنافية، لا محل لها مِنَ الإعراب</div>
  </div>
  <div class="irab-box" id="[UNIQUE_ID]">
      <div class="irab-word">جملة (كُتِبَتْ)</div>
      <div class="irab-details">صِفَة،ٌ مَحَلُّهَا الرَّفْع.ُ</div>
  </div>
</div>

=== BLOCK 17: Extra Info - Poem Background ===
(Component: TEMPLATE_C_BENEFIT.html)
Title: ملحق الأبيات الخارجية المتممة الواردة في ديوان جبران خليل جبران
Content: <span class="text-accent">قَصِيدَةُ (الغاب) مُقْتَطَعَةٌ مِنْ قَصِيدَةُ المواكب، وهي قَصِيدَةٌ رومانسِيَّةٌ طَوِيْلَة،ٌ تَفَاعَلَ فيها جبران مَعَ وِجْدَانِ الطَّبِيْعَةِ وَتَفَاصِيلِهَا مُعَلِّلًا ذَلِكَ بِأَنَّ الطَّبِيْعَةَ سَبَبُ السَّعَادَةِ الْمُطْلَقَة،ِ وبِأَنَّهَا نَمُوذج للعالم المثالي البَعِيدِ عَنِ الأَشْرارِ والزِّيْف.ِ يُعَدُّ جبران مِنْ أَوَائِلِ الشُّعَرَاءِ العَرَبِ الَّذِينَ تَغَنُّوا بالطَّبِيْعَة،ِ وَأَبْدَعُوا فِي وَصْفِهَا سَمّى جبران قصيدَتَهُ باسم المواكب نسبة إلى الجموع البَشَرِيَّةِ من ضلوا في اختيار الطريق الصحيح الذي يسعدهم، وظنوا أن مصدر سعادتهم وحريتهم في عالم الماديات المزيف، والمدنية المتصنعة وخضعُوا لعادات وتقاليد زائفة، ودعا جبران في قصيدته إلى العودة إلى عالم الطبيعة حيث الفطرة السليمة. نظم جبران القصيدة في وزنين مختلفين هما مجزوء الرمل، والبسيط. وتتألف قصيدة المواكب من ست مقطوعات، تشير المقطوعات الخمسة الأولى المتشابهة في البناء والتركيب إلى وصف الواقع، ووَصْفِ الغَابِ حَسْبَ رأي الكاتب الشخصي، أما المُقْطُوعَةُ السَّادِسَةُ فتختلف في بِنَائِهَا وتركيبها. وقد عبر فيها جبران عن شوقه إلى طبيعة لبنان الخلابة. ولطول هذه المقطوعات اخترنا منها</span>

--- END STREAM ---
