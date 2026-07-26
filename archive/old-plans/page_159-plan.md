# **SESSION 159**

[TASK DEFINITION]
Objective: Implement page 159.
File: `pages/page_159.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`.
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md` to identify the correct template to use for the continuation.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`, `.highlight-green` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   **Rule:** NO INLINE STYLES.
*   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
*   **Mapping:**
    *   `style="width: 20%"` -> `class="w-20pct"`
    *   `style="margin-top: 2mm"` -> `class="mt-2mm"`
    *   `style="text-align: center"` -> `class="text-center"`
    *   `style="font-weight: bold"` -> `class="font-bold"`
7. Templates: Replace `<section>` tags with `<div>` tags.
8. Unique IDs: All content blocks must have a unique ID (id='bXXXXX') applied to the `<div>`. Use "Jules-workspace/id_manager.py" to generate or verify them.
9. **Self-Correction:** Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files.
10. Do not summarize examples.
11. Do not provide uncompleted text content using (...).
12. Preserve exact Tashkeel and add missing Tashkeel. Remove stray dashes like "-  -  ". Correct typos like "النَّ" to "النَّصَّ".
13. Visual Density: The page must be dense.
14. balanced page colors between teal and orange: make sure every page have minimum 1 element in orange.
15. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (`.force-new-page`).
16. Exam section always be in the end of the lesson without the answers.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 159
[CHAPTER_TITLE]: page 159
[CATEGORY_HEADER]: 159
[SECTION_HEADER]: 159
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Analysis Section ===
(Component: TEMPLATE_C_BLOCK.html)
Title: [Empty]
Content: ادرس أبيات المقطع الثاني مِنَ النَّصَ وَفُقَ الْمَنْهَجِ النَّفْسِي، مُسْتَفِيدًا مِنْ إِجابتِكَ السَّابقة. <br> <span class="text-accent">الإجابة : الشَّعْرُ مِرْآةٌ تَعْكِسُ مخزونات العقل الباطني للشَّاعِر،ِ فالشَّعْرُ تجلى يُنْشَرُ فيه ما انطوى في نفسية الشاعر من مكنونات اخترتها اللاشُعُور،ُ وَيَتَمَثَلُ هَذَا عند الشاعر جورج صيدح الذي يَكْشِفُ عَمَّا تواري في خزائن اللاشْعُور، فعلى مستوى معاني النَّصَ نَجِدُ أَنَّ الشَّاعِرَ يَبْدَأُ بنداء وطنه، ونَعْتِهِ بالحبيب ويؤكد له أنه ما زال يلهج باسمه ويعلن له أنه سيبقى منتسبا إليه على الدوام، وأنه سيظل يرى فيه صورة الأب، لأَنَّه بَعْدَ فَقْدِهِ عَالَى مِنْ مَرَارَةِ اليُثم. ثم لا يلبث أن يؤكد له مُجَدَّدًا أَنَّهُ لَم يَكُنْ لِيَرْتَضِي البُعْدَ عَنْهُ وَالأَنْفِصَالَ عَنْ ثَرَاهُ الطَّاهر لولا شَظَفُ العَيْشِ وضِيقُهُ اللَّذِينِ تَفَاقَمَا لحظة الفراق، ففاقما مُعَانَاتَهُ وجعلا عَذَابَاتِهِ تَبْلُعُ ذُرْوَها. ويشير إلى أنه تكلّفَ المَشَقَّةَ وتحمل المتَاعِبَ مِن أَجْلِ أَنْ يَبْلُغَ ما يصبو إليه من مطالب وأَهداف، إِذْ يَتَطَلَّبُ مِنهُ الحصول على الغِنَى أَنْ يُفْنِي عُمْرَهُ وَيُذْهِبَه.ُ ويَخْتِمُ هذه الأبيات بالتساؤل عَمَّا إِذَا كَانَ الدَّهْرُ الذي عَمَدَ إلى إبعاده عن وطنه قد أَدْرَكَ أَنَّهُ بِصَنِيعِهِ هَذَا تَسَبَّبَ بِنَزْعِ رُوحٍ عَنْ جَسَدِها .</span> <br> وعلى مستوى استجلاءِ الظَّاهِرَةِ النَّفْسِيَّةِ نَجِدُ أَنَّ المعاني السَّابِقَةَ قَد كَشَفَتْ مُعاناةً نَفْسِيَّةٌ عَمِيقَةً مَصْدَرُها ابتعادُ الشَّاعِرِ عَنْ وَطَنِه،ِ وَسُوقُهُ إليه. ونَجِدُ الشَّاعِر،َ على مستوى تأويل الظَّاهِرَة،ِ يَنْدَفِعُ إلى التسامي النَّفْسِي باتخاذِهِ الفَنَّ الْمُبْدِعَ وسيلَةً لِلتَّعْبِيرِ عَنْ مَكْنُونَاتِهِ المَكْبُونَةِ فِي اللَّاشُعُور.ِ وقَدِ اتَّخَذَ الاشُعُورُ لَدَى الشَّاعِرِ أَشكالا فَنِيَّةً لِلكَشْفِ عَنْ نَفْسِهِ مَعَ بقائِهِ مُتواريًا، تَمَثَلَتْ بما يأتي:

=== BLOCK 3: Psychological Elements ===
(Component: TEMPLATE_C_LIST.html)
Items:
- <span class="highlight-blue">الألفاظ:</span> الموحِيَةُ بمعانٍ جَدِيدَةٍ أَخْرَجَهَا السياقُ عَنْ معانيها المُعْجَمِيَّةِ وَالحِسَيَّةِ إلى مَعَانٍ مُتَّشِحَةٍ بِظِلالِ اللَّاشُعُورِ وَأَطْيَافِهِ وَقَدْ شَكْلَتْ هَذِهِ الألفاظ في النص مُعْجَمًا لُغَوِيَّا للمُعاناة انْدَرَجَتْ تَحْتَهُ الأَلفاظ الآتية: (جراح، اليتم، البين، شِدَة،ٌ أَشَد، تَجَشَمْتُ العنا). وهذا المعجم يَكْشِفُ محاولات اللاشُعُورِ فِي التَّعْبِيرِ عَنْ نَفْسِه،ِ وميله إلى إشباع حاجاتِهِ مِنْ خلال إنكار المعاناة ومحاولة الخلاص منها والبعد عنها.
- <span class="highlight-blue">الرَّمْزُ:</span> أَمَّا الشَّكُلُ الآخَرُ الذي اتَّخَذَهُ اللَّاشْعُورُ عِنْدَ الشَّاعِرِ فِي التعبيرِ عَنْ مَكْنُونَاتِهِ فهو الرُّمُوزُ الدالة على حالات نَفْسِيَّةِ كَامِنَةٍ فِي أعماق الاشُعُورِ؛ إِذْ رَمَزَ بالروح إلى ذاته، ورمز بالجسد إلى الوطن؛ لأنه يرى أن مغادرته الوطن تشبه خروج الرُّوح مِنَ الحَسَد.
- <span class="highlight-blue">الصور :</span> أَدَّتِ الصُّور وظيفة في التَّعْبيرِ عَنْ مَكُنُونَاتِ اللَّاشُعُورِ إِذْ تَجَرَّدَتْ مِنْ حِسَيتها، واصطبغَتْ بِما أضفاهُ اللَّاشُعُورُ عليها، حَتَّى بَاتَتْ خَيْرَ مُعَيِّرِ عَنْ الأفكار اللاشْعُورِيَّةِ التي يُحَقِّهَا الاشُعُورُ إِلَى صُورٍ يَقْتَحِمُ بها ساحة الوعي ورقابته الصَّارِمَةَ وَمِنْ تِلْكَ الصُّورِ صُورَةُ (فَرَّقَ رُوْحًا عن جسد) التي اصطبَعَتْ بما أَضْفَاهُ اللَّاشُعُورُ عليها من آلام ومعاناة، فَكَانَتْ خَيْرَ مُعَبِّرِ عَنْ مُعَاناة الشَّاعِرِ المَكْبُونَةِ فِي أَعْمَاقِهِ وَخَيْرِ مُعَبِّرِ عَنْ متانة وشائج العلاقة بين الشاعر والوطن. وصُورَةُ (جراح اليتم)، التي اصطبعت بما أَضْفَاهُ اللاشُعُورُ عليها من آلام. فهذه الصُّورةُ تُكَثِفُ مَأْسَاةَ الشاعر في الغربة، وتكشف ما يُكابِدُهُ مِن وَطَاةِ العَيْش،ِ وتَخْتَزِلُ شِدَّةَ المعاناة التي يُصارعها. ومما يزيد هذه الصورة جَمَالًا وَتَأْلُقَا أَنَّهَا تَبْعَتُ فِي النَّفْسِ مَا يَتُم على عُمْقِ الانتماء إلى الوطن والانتساب إليه،ِ فَكَانَتْ كَافِيَةً للتَّعْبِيرِ عَمَّا كَانَ مَكْبُوتًا فِي أَعْمَاقِه.ِ

=== BLOCK 4: Conclusion Box ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: [Empty]
Content: ومِمَا سَبَقَ نَرَى أَنَّ النَّصَّ الأَدَبِي في التحليل السابق، كَشَفَ عَنْ سَعْي اللاشُعُورِ إلى التعبيرِ عَنْ نَفْسِهِ بِوسائِلَ فَنِيَّةٍ مُتَنَوَعَة،ِ شَكْلَتْ اليَّاتٍ نَفْسِيَّةً تجاوزَتْ رقابة الشُّعُور،ِ وَسَعَتْ عبرَ النَّصِ إلى البَوْحِ بِمَكُنُونَاتِ اللَّاشْعُورِ الذي جَعَلَ النَّصَّ - برأي الاتجاهِ النَّفْسِي - تمثيلًا رَمْزِيَّا لمعطيات اللاشْعُورِ الْمُكْبُونَة.ِ

=== BLOCK 5: Applications Start ===
(Component: TEMPLATE_C_BLOCK.html)
Title: التطبيقات اللغوية
Content: - ادرس مَبْحَثَ الصَّفَةِ مُسْتَفِيدًا مِنَ الْحَالَةِ الواردة في البيت الآتي:

=== BLOCK 6: Poem Evidence 1 ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: غابَ خَلْفَ البَحْرِ عَنِّي شَاطِي
Hemistich 2: كل ما أَرَّقَنِي فِيهِ رَقَدْ

=== BLOCK 7: Irab Analysis ===
(Component: TEMPLATE_C_IRAB_ROW.html)
Word 1: جُمْلَةُ (كُلُّ مَا أَرْقَنِي فِيهِ رَقَد)
Details 1: ج - فِي مَحَلِّ رَفْع،ِ صِفَة.ٌ

=== BLOCK 8: Second Activity ===
(Component: TEMPLATE_C_BLOCK.html)
Title: [Empty]
Content: - اقْرَأَ البَيْتَين الآتيين، ثُمَّ نَفَذِ النَّشَاطَ الذي يليهما :

=== BLOCK 9: Poem Evidence 2 ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: فَتَجَشَّمْتُ العَنَا نَحْوَ الْمُنَى
Hemistich 2: وتَقَاضَانِي الغِنَى عُمْرًا نَفَدْ
Hemistich 3: هلْ دَرَى الدَّهْرُ الذي فَرَّقَنا
Hemistich 4: أَنَّهُ فَرَّقَ رُوْحًا عَنْ جَسَدٌ؟

=== BLOCK 10: The Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Header 1: الفعل
Header 2: فاعله
Header 3: نَوْعُهُ
Row 1: تَجَشَّمْتُ | تاء الرفع المتحركة | ضميرُ رَفْعِ مُتَّصِلِّ
Row 2: تَقَاضَانِي | الغنى | اسم ظاهر
Row 3: دَرَى | الدَّهْرُ | اسم ظاهر
Row 4: فَرَّقَنَا | هو | ضميرٌ مُسْتَتر جوازا
Row 5: فَرَّقَ | هو | ضمير مُسْتَتر جوازا

=== BLOCK 11: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: استَخْرِجُ فَاعِلَ كُلِّ مِنَ الْأَفْعَالِ الواردة في البيتين السَّابِقِين،َ وَاذْكُرْ نَوْعَه.ُ

--- END STREAM ---
