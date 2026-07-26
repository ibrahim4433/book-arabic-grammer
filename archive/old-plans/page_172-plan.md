# **SESSION 172**

[TASK DEFINITION]
Objective: Implement page 172.
File: `pages/page_172.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
2.5 Cut Content: The page starts and ends with cut content. Use `TEMPLATE_CUT_BOX_PART_2.html` for the beginning and `TEMPLATE_CUT_BOX_PART_1.html` for the end, mapping both to `TEMPLATE_C_IRAB.html`.
2.6 Cut Content Determinism: Keyword "إعراب" dictates mapping to `TEMPLATE_C_IRAB.html`.
3. Text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   NO INLINE STYLES.
*   Irab Words inside `.irab-word` MUST be white.
*   Mapping: `style="width: 20%"` -> `class="w-20pct"`, etc.
*   `<section>` tags MUST be replaced with `<div>` tags (keep `<header>`).
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX') applied to the replacement `<div>`. Use "Jules-workspace/id_manager.py" to generate or verify them.
8. Self-Correction: Run "Jules-workspace/lint_pages.py --one-page-mode <filename>".
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...).
11. Preserve exact Tashkeel and add missing Tashkeel. Correct typos based on The Typo Exception.
12. Visual Density: The page must be dense.
13. Balanced page colors between teal and orange: Use `.accent` (Orange) for Block 9's header to satisfy the minimum 1 orange element rule.
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`).
15. Exam section always be in the end of the lesson. However, the Strict Typographer Rule overrides this since the raw text has no exam. Do not hallucinate an exam.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 172
[CHAPTER_TITLE]: page 172
[CATEGORY_HEADER]: 172
[SECTION_HEADER]: 172
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Cut Content Part 2 (Previous Irab) ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
Target Template: TEMPLATE_C_IRAB.html
Title: إعراب
Content:
مرفوع، وعلامَةُ رَفْعِهِ الضَّمَّةُ المقدرة على ما قَبْلَ يَاءِ الْمُتَكَلِم،ِ مَنَعَ ظُهُورَهَا اشْتِغَالُ الْمَحَلِ بِالْحَرَكَةِ المناسبة. والياء، ضميرٌ مُتَّصِلِّ مَبْنِي على السُّكُون في محل جر، مُضَاف إليه. جملة (ما إن أبالي): استئنافية، لا محل لها من الإعراب. جملة (في مشارقها حي): حاليَّة،ٌ مَحَلُّهَا النَّصْب.ِ

=== BLOCK 3: Poem 10 ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: ١٠- صَحْبِي دَعُوا النَّسَمَاتِ المَيْسَ تَلْمِسْنِي
Hemistich 2: فَقَدْ عَرَفْتُ بِهَا أَنْفَاسَ كُثْبَانِي

=== BLOCK 4: Analysis 10 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح والفكرة
Content:
<div class="mb-2mm"><span class="text-accent font-bold">المفردات:</span> النسمات الميس: النسمات التي تَهُبُّ مِنْ جِهَةِ مَنَابِتِ شَجَرِ الميس الحرجي. كثباني: الْمُفْرَدُ كَثِيب، وهو الرَّمْلُ.</div>
<div class="mb-2mm"><span class="text-accent font-bold">الشرح:</span> أيها الأصحاب يا شركائي فِي غُرْبَتِي، افْسَحُوا الطَّرِيقَ أَمَامَ النَّسَائِمِ الْمُحَمَّلَةِ بِعِطْرِ رِمَالِ الوَطَن،ِ واتركُوهَا تُعَانِقُ أَنْفَاسِيَ الْمُشْتَاقَة،َ وَتَلْفَحُ جَسَدِي المُغْتَرِبَ.</div>
<div class="mb-2mm"><span class="text-accent font-bold">الفكرة:</span> تصوير الشَّوْقِ والحنين إلى الوطن.</div>
<div class="mb-0"><span class="text-accent font-bold">الأساليب:</span> النسمات: اسم معرب بعلامة إعراب فرعية؛ لأنَّهُ منصوب بالكسرة.</div>

=== BLOCK 5: Irab 10 ===
(Component: TEMPLATE_C_IRAB.html)
Title: الإعراب
Word 1: صَحْبِي
Details 1: منادى مُضَافُ مَنْصُوب، وعلامَةً نَصْبِهِ الفَتْحَةُ الْمُقَدَّرَةُ على ما قبل ياء المتكلم، مَنَعَ ظُهُورَهَا اشْتِغَالُ الْمَحَلِ بِالحَرَكَةِ المُنَاسِبَة.ِ والياء، ضميرٌ مُتَصِلِّ مَبْنِي على السُّكُون في محل جر، مُضَاف إليهِ.
Word 2: دَعُوا
Details 2: فِعْلُ أَمْرِ مَبْنِي على حَذْفِ النُّونِ ؛ لَأَنَّ مُضَارِعَهُ مِنَ الأَفْعَالِ الْخَمْسَة.ِ والواو، ضميرٌ مُتَّصِلِّ مَبْنِي على السُّكُونِ فِي مَحَلِّ رَفْع، فاعل والآلِفُ حَرْفُ تَفْرِيق.ِ
Word 3: النَّسَمَاتِ
Details 3: مَفْعُولُ بِهِ مَنْصُوب، وعلامَةُ نَصْبِهِ الكَسْرَةُ نِيابةٌ عَنِ الفَتْحَةِ لِأَنَّهُ جَمْعُ مُوَنَّتْ سالم.
Word 4: المَيْسَ
Details 4: صِفَةٌ مَنْصُوبَةٌ.
Word 5: تَلْمِسْنِي
Details 5: فِعْلَ مُضَارِعٌ مَرْفُوع، وعلامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ والنُّون،ُ حَرْفُ وَقَايَة.ٍ والياء، ضميرٌ مُتَّصِلِّ مَبْنِي على السُّكُونِ فِي مَحَلِّ نَصْب،ِ مَفْعُولُ بِهِ.
Word 6: فَقَدْ
Details 6: الفاء، حَرْفُ اسْتِنْنَاف.ِ قَدْ: حَرْفُ تَحقيق.
Word 7: أَنْفَاسَ
Details 7: مَفْعُولُ بِهِ مَنْصُوب.ُ
Word 8: كُثْبَانِي
Details 8: مُضَاف إليهِ مَجْرُور،ُ وعلامَةُ جَرَهِ الكَسْرَةُ الظَّاهِرَةُ والياء، ضمير مُتَصِلِّ مَبْنِي على السُّكُونِ فِي مَحَلِّ جَرٍ ، مُضَافُ إليه.
Word 9: جملة (دَعُوا)
Details 9: استئنافية، لا محل لها من الإعراب.
Word 10: جملة (تلمسني)
Details 10: حالية، محلها النَّصْب.ِ
Word 11: جملة (قَدْ عَرَفْتُ)
Details 11: استئنافية، لا مُحَلَّ لها مِنَ الإعراب.

=== BLOCK 6: Poem 11 ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: ١١- تَدَفَّقِي يَا رِيَاحَ الشَّرْقِ هَائِجَةً
Hemistich 2: فَأَنْتِ لَا شَكَ مِنْ أَهْلِي وَإِخْوَانِي

=== BLOCK 7: Analysis 11 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح والفكرة
Content:
<div class="mb-2mm"><span class="text-accent font-bold">المفردات:</span> هائجة: اسم فاعِلِ فِعْلُه هاج.</div>
<div class="mb-2mm"><span class="text-accent font-bold">الشرح:</span> أيتها الرِّيَاحُ القَادِمَةُ مِنَ الشَّرْق،ِ زيدي هُبُوبَكِ وَتَدَفَقِي إِليَّ لَأَنَّكِ تَحْمِلِينَ رَائِحَةَ الأهل والأَحِبَّةِ.</div>
<div class="mb-2mm"><span class="text-accent font-bold">الفكرة:</span> تصويرُ الشَّوْقِ والحنين إلى الأهل والخلانِ (تَصْوِيرُ الفَرَحِ وَالنَّشْوَةِ بِلِقَاءِ الرِّيَاحِ القادِمَةِ مِنَ الوَطَنِ - الْحَنِينُ الدَّائِمُ لِلدِّيار).</div>
<div class="mb-0"><span class="text-accent font-bold">البلاغة:</span> (يا رياح): استعارَةً مَكْنِيَّة.ٌ</div>

=== BLOCK 8: Irab 11 Part 1 ===
(Component: TEMPLATE_C_IRAB.html)
Title: الإعراب
Word 1: تَدَفَّقِي
Details 1: فِعْلُ أَمْرٍ مَبْنِي على حَذْفِ النُّونِ لَأَنَّ مُضَارِعَهُ مِنَ الْأَفْعَالِ الْحَمْسَة.ِ والياء، ضَمِيرٌ مُتَّصِلَ مَبْنِي على السكون فِي مَحَلَ رَفْع، فاعل.
Word 2: يَا رِيَاحَ
Details 2: يا، حرف نداء. رياح، مُنَادى مُضَافُ مَنْصُوبُ.
Word 3: الشَّرْقِ
Details 3: مُضَافُ إِلَيْهِ مجرور.
Word 4: هَائِجَةً
Details 4: حال منصوبة.ٌ
Word 5: فَأَنْتِ
Details 5: الفاء، حَرْفُ استئنافِ. أَنْتِ، ضميرُ رَفْعِ مُنفَصِلُ مَبْنِي على الكَسْرَةِ فِي مَحَلِّ رَفْع،ِ مُبْتَدَأ.ٌ
Word 6: لَا شَكَ
Details 6: لا، نافية للجنسِ تَعْمَلُ عَمَلَ (إِنَّ). شَكَ، اسم (لا) مَبْنِي على الفتحة، في مَحَلِ نَصْبٍ. (الخَبَرُ مَحْذُوفٌ دَلَّ على كَوْنِ عام).

=== BLOCK 9: Core Matrix (Faa'idah on Ism Laa) ===
(Component: TEMPLATE_C_TABLE.html)
Title: فائدة نحوية حول إعراب (اسم لا) النافية للجنس
Description: يكون (اسم لا) النافية للجنس معرباً، أو مبنياً.
Headers: نوع (اسم لا) | حالته | أمثلة
Row 1: معرب | يأتي مُعْرَبًا (منصوبًا) إذا كانَ مُضَافًا (أَي بعدَهُ مُضَاف إليه) أو شبيها بِالْمُضَافِ (أَي مشتقاً منوناً). | لا مهمل وظيفة ناجح. / لا كاتبا وظيفة راسب.
Row 2: مبني | يكون مبنياً على ما يُنصَبُ بِهِ إِذا جَاءَ مُفَرَدًا (أَي ليس مُضَافًا ولا شبيها بالمضاف). | لا مهمل ناجح. / لا طالبين كسولان. / لا مُجدينَ راسبونَ. / لا طالبات كسولات.

=== BLOCK 10: Irab 11 Part 2 ===
(Component: TEMPLATE_C_IRAB.html)
Title: تتمة الإعراب
Word 1: مِنْ أَهْلِي
Details 1: مِنْ، حَرْفُ جر. أَهْلِي، اسم مَجْرُور،ُ وعلامَةُ جَرِهِ الكَسْرَةُ الظَّاهِرَة.ُ والياء،ُ ضميرٌ مُتَصِلِّ مَبْنِي على السكون في محل جر، مُضَاف إليه. والجار والمَجْرُورُ مُتَعَلقَانَ بِخَبَرِ مَحْذُوفِ (للمُبْتَدَأ أَنْتِ).
Word 2: وَإِخْوَانِي
Details 2: الواو، حَرْفُ عَطف. إخواني، اسم معطوف مَجْرُور،ُ وعلامَةُ جَرَهِ الكَسْرَةُ الظاهرة والياء، ضمير متصل مبني على السكون في محل جر، مُضَاف إليه.
Word 3: جملة (تَدَفَّقِي)
Details 3: استئنافية، لا محل لها من الإعراب.
Word 4: جملة (أَنْتِ لا شَكَ مِنْ أَهْلِي)
Details 4: استئنافية، لا محل لها من الإعراب.
Word 5: جملة (لا شَكَ ...)
Details 5: اعْتِرَاضِيَّة،ٌ لَا مَحَلَّ لها مِنَ الإعراب.

=== BLOCK 11: Poem 12 ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: ١٢- هَزَزْتِ أَغْصَانَ قَلْبِي بَعْدَمَا خَلَعَتْ
Hemistich 2: ثَوْبَ الرَّبِيعِ فَمَاسَتْ رَقْصَ نَشْوَانِ

=== BLOCK 12: Analysis 12 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح والفكرة
Content:
<div class="mb-2mm"><span class="text-accent font-bold">المفردات:</span> ماست: تَمَايَلَتْ وَتَبَخْتَرَتْ. نَشْوان: صفةٌ مُشبهة باسم الفاعل.</div>
<div class="mb-2mm"><span class="text-accent font-bold">الشرح:</span> أيتها الرِّيَاحُ القَادِمَةُ مِنَ الشَّرْق،ِ أعادَ قُدُومُكِ إِليَّ رَقْصَ مَخْمُورِ ربيع حياتي الذي صَادَرَتْهُ الغُرْبَةُ حَيْثُ اهْتَزَّتْ أَعْصَانُ قَلْبِي الحَامِلَةُ الحزينةُ فَرِحَةً بِلِقَائِك،ِ وراحَتْ تَتَمَايَلُ وَتَرْقُصُ مُنْتَشِيةَ مِثْلَ دَارَتِ الْخَمْرَةُ بِرَأْسِهِ.</div>
<div class="mb-2mm"><span class="text-accent font-bold">الفكرة:</span> تَصْوِيرُ الفَرَحِ وَالنَّشْوَةِ بِلِقَاءِ الرياح القادِمَةِ مِنَ الوَطَنِ (الحَنِينُ الدَّائِمُ لِلدِّيارِ). الشعور: الفرح. الأداة: التراكيب. المثال: مَاسَتْ رَقْصَ نَشوان.</div>
<div class="mb-0"><span class="text-accent font-bold">البلاغة:</span> (أَغْصَانَ قَلْبِي)، (الأَغْصَانِ خَلَعَتْ)، (الأَغْصَانِ مَاسَتْ)، (ثَوْب الربيع): استعارة مَكْنِيَّةٌ.</div>

=== BLOCK 13: Cut Content Part 1 (Irab 12) ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
Target Template: TEMPLATE_C_IRAB.html
Title: الإعراب
Word 1: أَغْصَانَ
Details 1: مَفْعُولٌ بِهِ مَنْصُوبُ.
Word 2: قَلْبِي
Details 2: مُضَاف إليهِ مَجْرُور، وعلامَةُ جَرِّهِ الكَسْرَةُ الظَّاهِرَة.ُ والياء، ضمير مُتَّصِلِّ مَبْنِيٌّ على السُّكُون في محل جر، مُضَاف إليه.
Word 3: بَعْدَمَا
Details 3: بَعْدَ، مَفْعُولُ فِيهِ ظَرْفُ زَمَانٍ مَنْصُوب، وعلامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَة.ُ وما، حَرْفٌ مَصْدَرِي. وَالْمَصْدَرُ الْمَوَّلُ (ما خَلَعَتْ) في محل جر،ٍ مُضَاف إليهِ.
Word 4: خَلَعَتْ
Details 4: فِعْلَ مَاض،ِ مبني على الفَتْحَةِ؛ لاتِّصَالِهِ بِتَاءِ التَّأْنيثِ السَّاكِنَة.ِ والتَّاء،ُ حَرْفُ تَأْنيث لا مَحَلَ لَهُ مِنَ الإعراب.
Word 5: ثَوْبَ
Details 5: مَفْعُولُ بِهِ مَنْصُوبُ.
Word 6: الربيع
Details 6: مُضَاف إليهِ مَجْرُورٌ.
Word 7: فَمَاسَتْ
Details 7: الفَاء،ُ حَرْفُ عَطْفٍ. مَاسَت،ْ فِعْلَ مَاض،ِ مبني على الفَتْحَةِ؛ لاتِّصَالِهِ بِتَاءِ التَّأْنيثِ السَّاكِنَة.ِ والتَّاء،ُ حَرْفُ تَأْنيث لا مَحَلَ لَهُ مِنَ الإعراب.
Word 8: رَقْصَ
Details 8: نَائِبُ مَفْعُولٍ مُطْلَقٍ مَنْصُوبٌ.
Word 9: نَشْوَانِ
Details 9: مُضَاف إليهِ مَجْرُور، وعلامَةُ جَرِّهِ الكَسْرَةُ الْمُقَدَّرَةُ.

--- END STREAM ---
