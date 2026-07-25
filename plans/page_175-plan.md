# **SESSION 175**

[TASK DEFINITION]
Objective: Implement page 175.
File: `pages/page_175.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
2.5 Cut Content: Not violently cut. No CUT_BOX required.
2.6 Cut Content Determinism: N/A.
3. Text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice. Typo Exception applied to fix scrambled OCR in irab and verse endings, and page footer removed.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   **Rule:** NO INLINE STYLES.
*   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
*   **Mapping:** `style="width: 20%"` -> `class="w-20pct"`, etc.
6. Templates: Replace any `<section>` tags from the templates with `<div>` tags (keep `<header>` for page headers as is).
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). Use "Jules-workspace/id_manager.py".
8. Self-Correction: Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...) .
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense. Do NOT leave empty space.
13. Balanced page colors between teal and orange: Included orange `TEMPLATE_C_BENEFIT_WARNING.html` for ideas and feelings.
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`).
15. Exam section: None exists in raw text. Strict Typographer Rule applied.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 175
[CHAPTER_TITLE]: page 175
[CATEGORY_HEADER]: 175
[SECTION_HEADER]: 175
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: أبيات القصيدة ===
(Component: TEMPLATE_C_POEM.html)
Title: أبيات القصيدة
Poet:
Verse 13 Right: ١٣- والمالُ أَهْوَنُ مَبْذُولٍ إِذا رَفَضُوا
Verse 13 Left: شَوْقًا بِشَوق وتَحْنَانًا بِتَحْنَانِ
Verse 14 Right: ١٤- أنا الذي إن تناسى النَّاسُ قَوْمَهُمُ
Verse 14 Left: هيهات يَنْسَى وما الكفرانُ مِنْ شاني
Verse 15 Right: ١٥- إن جاهَدُوا كان قلبي في جهادهم
Verse 15 Left: وإِنْ تَنَادَوا يُلَبِّ الصَّوت وجداني
Verse 16 Right: ١٦- لا حَدَّ عِنْدِي إذا جارَتْ حُدُودُهُمُ
Verse 16 Left: الشام شامي ومصرُ أَخْتُ لبناني
Verse 17 Right: ١٧- وفي فلسطين أقداسي وعاطفتي
Verse 17 Left: في نجد والقِبْلَةُ السَّمحاء إيماني
Verse 18 Right: ١٨- لي العروبة أمشي في مخارِفِهَا
Verse 18 Left: مِنَ العراق إلى ما بَعْدَ وَهُرَانِ
Verse 19 Right: ١٩- أزهو بِنُوبِ فَخَارِ مِنْ مَنَاسِجِها
Verse 19 Left: حتى تقرب أيدي البَيْنِ أَكْفَانِي

=== BLOCK 3: الشرح ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الشرح
Content: <span class="font-bold">١٣- </span>بذل المال والتَّضْحِيَةُ بِهِ مِنْ أَجْلِهِم أَقَلُّ مَا نُقَدِّمُه،ُ إِذَا رَفَضُوا أَنْ يُبَادِلُونَا الشَّوْقَ بِالشَّوق والحنان بالحنان.<br><br><span class="font-bold">١٤- </span>إذا النَّاسُ قَبِلُوا على أَنْفُسِهِم أَنْ يَنْسَوا ذَوِيهِم وَيَتَنَكُرُوا لَهُم،ْ فَلَيْسَ مِنْ طَبْعِي ولا مِنْ شِيْمَتِي القيامُ بِذَلِكَ<br><br><span class="font-bold">١٥- </span>إذا خاضوا حَرْبًا مَعَ الأعداء فإنَّ قلبي يبقى مُرْتَبِطًا بِهِم مُتضامِنَا مَعَهُم رُعْمَ بُعْدِي عَنْهُم، وإذا ارتفعت أصواتهم داعية إلى الاجتماع، فَإِنَّ رُوحِي تُسارع إلى تَلْبِيَةِ نِدَائِهِم والاستجابة لَهُ<br><br><span class="font-bold">١٦- </span>إِذا أَصَرَّتِ الحُدُودُ المَصْنُوعَةُ بِينَ دُولِ الوَطَنِ العَرَبي بأبنائِهِ وَفَرَّقَتَهُم، فأنا لا أَعْتَرِفُ بِتِلْكَ الْحُدُودِ؛ فَبِلَادُ الشَّامِ مَوْطِني، وَمِصْرِ عِنْدِي أُخْتُ لِمَوطِنِي الآخر لبنان<br><br><span class="font-bold">١٧- </span>لي في فلسطين أماكن طاهرة مباركة، وميلي وحبي مكرسان لنجد ذلك القسم من أرض الجزيرة العربية القائِمِ بَيْنَ الحجاز والعراق، أمَّا عَقِيدتي فهي تلك النفحات التي تسري مِنَ الكَعْبَةِ المُشَرَّقَة،ِ مِنَ الْمُسْجِد الحرام في مكة المكرمة<br><br><span class="font-bold">١٨- </span>الأرض العَرَبِيَّةُ كُلُّهَا أَرْضِي أَسِير في بساتينها ورُبُوعِهَا الْمُمْتَدَّةِ مِنَ العراق إلى مَدِينَةِ وهران الجزائرية.<br><br><span class="font-bold">١٩- </span>سأبقى فَخُورًا أتيه مختالا بسبب انتمائي وانتسابي إلى الأمة العربية، إلى أَنْ أَمُوتَ وَأَكَفَّنَ وَأَفارق الدُّنْيا.

=== BLOCK 4: المفردات ===
(Component: TEMPLATE_C_TABLE.html)
Title: المفردات
Headers: الكلمة, معناها
Row 1: أهون, اسمُ تَفْضِيل، فِعْلُهُ هان
Row 2: مَبْذُولِ, اسمُ مَفْعُولٍ فِعْلُه:ُ بذل
Row 3: الكفرانُ, كَفَرَ بهذا : تَبَرَا مِنْهُ
Row 4: تَنَادوا, تنادى القُوم:ُ نادى بَعْضُهُم بَعْضًا، أي تداعوا بِصَوْتِ مُرْتَفِع،ِ تداعوا للاجتماع.
Row 5: وجداني, وجدانُ الْمَرْء:ِ نَفْسُهُ وَقُواهُ الباطنية.
Row 6: يُلَبِّ, لبى النداء: استجاب لَهُ
Row 7: جارَتْ, ظَلَمَتْ
Row 8: نجد, قِسْمَ مِنَ الجزيرة العَرَبِيَّة بين الحجاز والعراق.
Row 9: القبلة, الكعبة، لأن المسلمينَ يَسْتَقْبِلُونها في صلاتهم.
Row 10: القبلتان, المسجد الحرام في مكة المكرمة، والمسجد الأقصى في القدس الشريف
Row 11: مخارفها, بساتينها
Row 12: أَزهو, زَهَا زَهْوَا، ورُهُوا : تاه وتعاظم وافتَخَرَ.
Row 13: البَيْنُ, الفُرْقَةُ.
Row 14: مَنَاسِجها, المفرد : مَنْسَج، وهو اسم مكان.

=== BLOCK 5: الفكرة والشعور ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: الفكرة والشعور
Content: <span class="font-bold">١٣- الفكرة: </span>تأكيدُ التَّشَبُّثِ بحب الأهل والوطن<br><span class="font-bold">١٤- الفكرة: </span>تأكيدُ عَدَمِ نِسْيَانِ الأهل والوَطَنِ | <span class="font-bold">الشعور: </span>اعتزاز، وافتخار<br><span class="font-bold">١٥- الفكرة: </span>تأكيد الارتباط بقضايا الأهل والوطن<br><span class="font-bold">١٦- الفكرة: </span>عَدَمُ الاعترافِ بِالتَّجْزِنَة | <span class="font-bold">الشعور: </span>سُخْط وبغض<br><span class="font-bold">١٩- الفكرة: </span>الزهو بِمَجْدِ الأُمَّةِ العَرَبِيَّةِ | <span class="font-bold">الشعور: </span>اعتزاز، وافتخار.

=== BLOCK 6: التراكيب والبلاغة ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Title: التراكيب والبلاغة
Content: <span class="font-bold">١٤- التراكيب: </span>الأداة: التراكيب المثال: إِنْ تَنَاسَى النَّاسُ قَوْمَهُمْ هِيهَاتَ يَنْسَى. أو ما الكفرانُ مِنْ شاني<br><span class="font-bold">١٥- البلاغة: </span>)يُلَبِّي وجداني(: استعارَةٌ مَكْنِيَّة<br><span class="font-bold">١٦- التراكيب: </span>الأداة: التراكيب. المثال: جارَتْ حُدُودَهُم.ْ<br><span class="font-bold">١٦- البلاغة: </span>)جارَتْ حُدُودَهُمْ( : اسْتِعَارَةٌ مَكْنِيَّة<br><span class="font-bold">١٩- التراكيب: </span>الأداة : التراكيب المثال: أَزهو بِنُوبٍ فَخَارِ مِنْ مَنَاسِجها.<br><span class="font-bold">١٩- البلاغة: </span>)توب فَخَارِ(: تَشْبِيةٌ بَلِيعٌ إضافي )أيدي البَيْنِ(: استعارَةُ مَكْنِيَّةُ.

=== BLOCK 7: الإعراب ===
(Component: TEMPLATE_C_TABLE.html)
Title: الإعراب
Headers: الكلمة, إعرابها
Row 1: المال, مُبْتَدَاً مَرْفُوعٌ
Row 2: أَهُونَ, خَبَرَ مَرْفُوع.ٌ
Row 3: )المالُ أَهُونُ مَبْذُول(, استئنافية لا محل لها مِنَ الإعراب
Row 4: )رفضوا(, في محل جَرِّ بالإضافة.
Row 5: أنا, ضَمِيرُ رَفْعِ مُنْفَصِلٌ فِي مَحَلِّ رفع مبتدا.
Row 6: الذي, اسم موصول، في محل رفع خبر.
Row 7: هيهات, اسم فعل ماض بمعنى بعد مبني على الفتح.
Row 8: الكفرانُ, مُبْتَدَاً مَرْفُوع.
Row 9: )إِنْ تَنَاسَى النَّاسُ قَوْمَهُمْ هيهات يَنْسَى(, صلة الموصول لا محل لها من الإعراب.
Row 10: قلبي, اسم كانَ مَرْفُوع.
Row 11: )كان قلبي في جهادِهِمُ(، )يُلَبِّ الصَّوتَ وَجَدَانِي(, جُمْلَةٌ جَواب الشَّرْطِ لا محل لها مِنَ الإعراب.
Row 12: يُلَبِّ, فعل مضارع مجزوم؛ لأنَّهُ جوابُ الشَّرْطِ وعلامَةً جَزْمِهِ حَذْفُ حَرْفِ العِلَّة.
Row 13: الصوت, مَفْعُولُ بِهِ مَنصوب.
Row 14: وجداني, فَاعِلَ مَرْفُوع.ُ
Row 15: لا, نافِيَةً لِلجِنس، تَعْمَلُ عَمَلَ إِنَّ.
Row 16: حَد:َّ, اسمُ لَا النَّافِيَة للجنس مبني على الفتح في مَحَلَ نَصْب.
Row 17: )جارَتْ خُدُودَهُم(, في محل جَرِّ بالإضافة.
Row 18: الشام، مصر, مُبْتَدَاً مَرْفُوع.
Row 19: شامي، أخت, خبر مرفوع.
Row 20: أقداسي، عاطفتي، القبلة, مُبْتَدَاً مَرْفُوعُ.
Row 21: السَّمْحاء, صِفَةٌ مَرْفُوعَةٌ.
Row 22: إِيمَانِي, خَبَرِّ مَرْقُوع.
Row 23: العُرُوبَةُ, مُبْتَدَاً مَرْفُوع.
Row 24: فَخَارِ, مُضافُ إِلَيْهِ مَجْرُورُ.
Row 25: البَيْنِ, مُضافُ إِلَيْهِ مَجْرُورُ.
Row 26: تُقَرب, فِعْلَ مُصَارِعٌ مَنْصُوبٌ.
Row 27: أيدي, فَاعِلْ مَرْفُوع.
Row 28: تقرب أيدي البَيْنِ, صِلَةُ الموصولِ لَا مُحَلَّ لَهَا مِنَ الإعراب.
Row 29: أكفاني, مَفْعُولُ بِهِ مَنصُوب.ُ

--- END STREAM ---
