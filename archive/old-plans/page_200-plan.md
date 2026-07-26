# **SESSION 200**

[TASK DEFINITION]
Objective: Implement page 200.
File: `pages/page_200.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools. If it overflows, it is a catastrophic failure. Do NOT try to solve overflow by deleting text (Strict Typographer Rule). Solve it by choosing denser templates or omitting optional white-space.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green`  for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide: NO INLINE STYLES.
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). The ID MUST be applied to the `<div>` tag that replaced the `<section>` tag. Use "Jules-workspace/id_manager.py" to generate or verify them.
8. Self-Correction: Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...) .
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
15. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 200
[CHAPTER_TITLE]: page 200
[CATEGORY_HEADER]: 200
[SECTION_HEADER]: 200
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Warning Benefit Box ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: أ. المعاناة بِسَبَبٍ فِرَاقِ المحبوبة
Content: <span class="text-accent">التَّعْبِيرُ عَنِ الحَسْرَةِ على انقطاع الوِصَالِ والشَّوْقُ والحنين إليها مَعَ الْمَحْبُوبَةِ</span>

=== BLOCK 3: Poem ===
(Component: TEMPLATE_C_POEM.html)
Bio: جورج صيدح
[RIGHT_HEMISTICH]: وطني حتام ترتد الصبا
[LEFT_HEMISTICH]: دُونَ أَنْ تَحْمِلَ مِنْ سَلْمَايَ رَدّ؟
[RIGHT_HEMISTICH]: قَسَما لولا أنيني ما اهتدى
[LEFT_HEMISTICH]: لسريري طَيْفُهَا لَمَّا وَفَدْ
[RIGHT_HEMISTICH]: زَارَ الْمَامًا فَمَا مِلْتُ إلى
[LEFT_HEMISTICH]: ضمّهِ حَتَّى تَجَافى وابْتَعَدْ

=== BLOCK 4: Standard Block ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ١٠- التَّعْبِيرُ عَنِ الشَّوْقِ والحَنِينِ
Content: إِلَى لِقَاءِ الوَطَنِ وَالأَحِبَّةِ (الحَنِينُ الدَّائم للديار):

=== BLOCK 5: Poem ===
(Component: TEMPLATE_C_POEM.html)
Bio: نسيب عريضة
[RIGHT_HEMISTICH]: وَلَيْسَ يَرْوِيكَ مِنْ مَاءٍ دِجْلَةَ أو سَلْسَالِ لُبَنَانِ
[LEFT_HEMISTICH]: إِلَّا نَخْلَةٌ بَعْدَتْ
[RIGHT_HEMISTICH]: وحُلُمُ يَوْمِكَ في المِيمَاسِ مُحْتَفِل
[LEFT_HEMISTICH]: بالعيد والصيد فِي أَعْرَاسِ نُدْمَانِ

=== BLOCK 6: Standard Block ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ١١- التعلق بالوطن والارتباط به، والألم والمعاناة
Content: بِسَبب البُعْدَ عَنْهُ (الحنين الدائم للديار):

=== BLOCK 7: Poem ===
(Component: TEMPLATE_C_POEM.html)
Bio: نسيب عريضة
[RIGHT_HEMISTICH]: كُلَّمَا هَبَّتِ الْأَرْيَاحُ خَافِقَةً
[LEFT_HEMISTICH]: تَجُرُّ فِي ذَيْلِهَا أَنْفَاسَ رَيُحَانِ
[RIGHT_HEMISTICH]: حَسِبْتَهَا نَسَمَاتِ الشيح فانطَلَقَتْ
[LEFT_HEMISTICH]: مِنْ أَسْرِهَا زَفَرَاتُ العَاجِزِ الوَانِي

=== BLOCK 8: Standard Block ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ١٢- تصوير الشَّوْقِ والحنين إلى الأهل والخلان:
Content: (Empty)

=== BLOCK 9: Poem ===
(Component: TEMPLATE_C_POEM.html)
Bio: نسيب عريضة
[RIGHT_HEMISTICH]: صَحْبِي دَعُوا النَّسَمَاتِ المِيسَ تَلْمِسُنِي
[LEFT_HEMISTICH]: فَقَدْ عَرَفْتُ بِمَا أَنْفَاسَ كُثْبَانِي
[RIGHT_HEMISTICH]: تَدَفَقِي يا رياح الشَّرْقِ هَائِجَةً
[LEFT_HEMISTICH]: فَأَنْتَ لا شك من أهلي وإخواني

=== BLOCK 10: Standard Block ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ١٣- تَصْوِيرُ الفَرَح والنَّشْوَةِ بِلِقَاءِ الرِّيَاحِ القادِمَةِ مِنَ الوَطَنِ
Content: (الْحَنِيْنُ الدائم للديار):

=== BLOCK 11: Poem ===
(Component: TEMPLATE_C_POEM.html)
Bio: نسيب عريضة
[RIGHT_HEMISTICH]: تَدَفْقِي يَا رِيَاحَ الشَّرْقِ هَائِجَةً
[LEFT_HEMISTICH]: فأَنْتَ لا شك من أهلي وإخواني
[RIGHT_HEMISTICH]: هَزَزْتِ أَغْصَانَ قَلِبِي بَعْدَمَا خَلَعَتْ
[LEFT_HEMISTICH]: ثوبَ الرَّبِيعِ فَمَاسَتْ رَقْصَ نَشْوَانِ

=== BLOCK 12: Standard Block ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ١٤- التعبير عَنْ إِثَارَةِ مَشَاعِرِ الشَّوْقِ وتجددها:
Content: (Empty)

=== BLOCK 13: Poem ===
(Component: TEMPLATE_C_POEM.html)
Bio: نسيب عريضة
[RIGHT_HEMISTICH]: كَسَوْتِهَا وَرَقَ الْأَشْوَاقِ فَازْدَهَرَتْ
[LEFT_HEMISTICH]: خَضْرَاءِ يَعْبقُ مِنْها روح نيسان

=== BLOCK 14: Core Matrix Table ===
(Component: TEMPLATE_C_TABLE.html)
Title: ثالثا - البوس والشقاء والمعاناة :
Headers: التعبير | الشاعر | الشاهد
Row 1: ١- تصوير البوس والشقاء والمعاناةِ فِي الغُرْبَةِ: | حسني غراب | زورقي تائه وزادي قليل وشراعي بال ونجمي خاب، كلما لاح لي بريق رجاء أَوْصَدَ اليَأْسُ دُونَهُ كُلِّ بَابِ، إنَّ في الموت راحةً مِنْ عَنَاءِ ونَجَاةٌ مِنْ حَيْرَةِ واضطراب
Row 2: - إفناء العمر في الغُرْبَةِ طَلَبًا لِلغِنى: | جورج صيدح | فَتَجَشَمْتُ العَنَا نحو المنى و تقاضاني الغنى عُمْرًا نَفَدْ
Row 3: - التَّعْبِيرُ عَنِ الْخَيْرَةِ والتَّشَتِ وَالضَّيَاعِ: | نسيب عريضة | أَحَاضِرْ أَنْتَ أَمْ بَادٍ أَمُهْتَجِرٌ في الغرب؟ أو هائم فِي بِيدٍ قحطانِ؟
Row 4: - التَّمَزُّقُ الرُّوحِيُّ بَيْنَ الغُرْبَةِ وَالوَطَنِ: | نسيب عريضة | مَنْ أَنْتَ؟ ما أَنْتَ؟ قد وزَعْتَ رُوحَكَ في عَهْدَيْنِ مِنْ شَاسِع ماض ومن داني، أنا المهاجر ذو نَفْسَين واحِدَةً تسير سيري، وأخرى رهن أوطاني
Row 5: ه - تنازل المُغْتَرَبِ وَتَخَلِيهِ عَنْ أَحْلَامِهِ (عَدَمُ قُدْرَةِ المُغْتَرَبِ على تحقيقٍ أَحلامه): | فوزي المعلوف | وتلاشَتْ حُلمًا فَحُلَمًا إلى اللاشيءٍ تَمْشِي بِهِ قَلِيلًا قَلِيلا
Row 6: ٦- تصوير بُرُوزِ آثَارِ مُعَانَاةِ الْمُغْتَرِبِ على محياه (تصوير آثار الغُرْبَةِ الجَسَدِيَّة) (انعِكَاسَ عَذَابَاتِ المغترب ومعاناته): | فوزي المعلوف | هو في مَيْعَةِ الشَّبَابِ ولو حَدَّقْتَ فِيهِ أَبْصَرْتَ شَيْخًا هَزِيلا، بِقَوَامِ كَأَنَّ قَاصِمَةَ الظَّهْرِ أَنَاخَتْ عَلَيْهِ حِمْلًا تَقِيلا، وَجَبِيْنِ الْقَتْ عَلَيْهِ شُجُونُ النَّفْسِ ظِلَّا ظَلِيلا

=== BLOCK 15: Benefit Box ===
(Component: TEMPLATE_C_BENEFIT.html)
Title: - - -
Content: ٢٠٠ مكتبة حكمة

--- END STREAM ---
