# **SESSION 137**

[TASK DEFINITION]
Objective: Implement page 137.
File: `pages/page_137.html` (Note: Use the exact page number.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools. If it overflows, it is a catastrophic failure. Do NOT try to solve overflow by deleting text (Strict Typographer Rule). Solve it by choosing denser templates or omitting optional white-space.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`. Ensure exact visual continuity (same title, same classes).
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md` to identify the correct template to use for the continuation. You are forbidden from guessing. Scan the raw text for the preceding keyword to determine the active template and apply the correct `_PART_2.html` wrapping.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
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
6. Templates: You are forbidden from inventing new HTML tags or classes or template elements. You must map all content using "Jules-workspace/Templates/" components as the STREAM says in suitable way. **CRITICAL 1-PAGE MODE RULE**: You MUST NOT use `<section>` tags when applying templates. Replace any `<section>` tags from the templates with `<div>` tags (keep `<header>` for page headers as is).
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). The ID MUST be applied to the `<div>` tag that replaced the `<section>` tag. Use "Jules-workspace/id_manager.py" to generate or verify them.
8. **Self-Correction:** Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files. If it fails, you MUST fix the errors (usually inline styles or forbidden section tags) before submitting.
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
[LESSON_NUMBER]: 137
[CHAPTER_TITLE]: page 137
[CATEGORY_HEADER]: 137
[SECTION_HEADER]: 137
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: تابع النص ===
(Component: TEMPLATE_CUT_BOX_PART_2.html wrapping TEMPLATE_C_BLOCK.html)
Title: [No Title]
Content: <div class="text-primary font-bold">أَشْرَسَ المعَارِك،ِ ولم يدعنُوا لهم، بل تَصَدَّوا لهم وخَاضُوا ضدهم وحب للوطن واستعداد للتضحية في سبيله، لَمْ يَسْتَكِينوا للمحتلين وحَقَّقُوا أَعظم الانتصارات.</div>

=== BLOCK 3: مشاعر الفرح ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مشاعر الفرح
Content: <div class="text-accent">عَنْ مَشَاعِرِ الفَرَحِ وَالرَّهِو لأَدَقِ تَفَاصِيلِهَا . فقد قام الأدباء بالتعبير فكانَ الأَدَبُ العَرَبِيُّ مُوَاكِبًا لهذه الأحداث، ناقلا أمينا العَرَبِيُّ؛ مِنْ أَعْظَمِ المُنجَزَاتِ التِي حَقَّقَها الإِنسَانُ رَدًّا حَقِيقِيًّا على نَكْسَة حزيران، فهي بنصر تشرين، فقد كانَتْ حَرْبُ تشرين التَّحْرِيرِيَّةِ عِزَّهَا وَكَرَامَتَهَا وَكِبْرِيَاءَها المهدور، حزيران، وأَعَادَتْ للأُمَّةِ جَبِينَ الأَمَّةِ العَرَبِيَّةِ جَرَّاء هَزِيمَةِ إذ غسلَتْ بِدِمَاءِ الأبطال العارَ الذي لَطَّحَ وشَفَتْ وَجْدَانَهَا المطعُون.َ خَفَقَتْ خَرَجَ الوَطَنُ مِنَ الْحَرْبِ مُنْتَصِرًا حَتَّى الفَرَحَ فِي قَوَافِي الشُعَرَاءِ؛ فَمَا إِنْ ولأَجْلِ ذَلِكَ كُلِّهُ عَكَسَ انتِصَارُ تِشْرِينِ طَالِبًا تشرين حِينَمَا نَاجَى دِمَشْقَ نِزَارِ قَبَّانِي صَوَّرَ فَرْحَةَ انتصار بِهَذَا الْحَدَثِ الجَلَل.ِ فالشَّاعِرُ قُلُوبُ الشَّعَرَاءِ وَقَوَافِيهِم فَرَحَةً مُتَغَنِّيَةً عَظِيمَةٍ خَالِدَةِ حَقَّقَهَا الْإِنْسَانُ فَنَصْرُ تشرين قد أَحْيَا فِي النَّفْسِ ذِكْرَى انتِصَارَاتٍ مِنْهَا أَنْ تَمْحُوَ مِنْ ذَاكِرِهَا أَيَّامَ الإخْفَاقِ والانْكِسَار،ِ كَرَامَتَنَا الْمُهْدُورَة. يقول: سِنِينَ مُرَّة،ٍ واستَعَدْنَا العَزِيمَةَ بِالعَدُةِ بَعْدَ ويُؤكد لها مُبْتَهِدًا أَنَّنَا أَحَقْنَا العَرَبِيُّ فِي مَوْقِعَةِ بَدْرِ ومعركة حطين،</div>

=== BLOCK 4: شعر نزار قباني ===
(Component: TEMPLATE_C_POEM.html)
Bio:
Verses:
مَزِّقِي يَا دِمَشْقُ خَارِطَةَ الذُّلِّ
وَقُولِي لِلدَّهْرِ كُنْ فَيَكُونُ
اسْتَرَدَّتْ أَيَّامَهَا بِكِ بَدْرٌ
وَاسْتَعَادَتْ شَبَابَهَا حِطِّينُ
هُزِمَ الرُّومُ بَعْدَ سَبْعِ عِجَافٍ
وَتَعَالَى وِجْدَانُنَا المَطْعُونُ

=== BLOCK 5: فلسطين والمسؤولية الأدبية ===
(Component: TEMPLATE_C_BLOCK.html)
Title: فلسطين والمسؤولية الأدبية
Content: أَجَلٍ تَخْرِيرِ بَاقِي إِلَى مُوَاصَلَةِ النَّضَالِ مِنْ الإِنْسَانُ العَرَبِيُّ يَتَطَلَّعُ تَبْقَى في الحَلْقِ غَصَّة،ٌ فَيَظَلُ وفِي غَمْرَةِ الفَرَح بِنَصْرِ تشرين يُعاني أبْنَاؤُها، الذين أَرْغِمُوا والليمون،ِ فَلَسْطِين المغتصبة التي دَنَى الغُزَاة،ِ ولا سيما أَرْضُ الرَّيْتُونِ الْأَرَاضِي العَرَبِيَّةِ الخَتَلَّة،ِ وَتَطْهِيرِهَا مِنَ في ماقيهم، وغَطَّتْ وُجُوهَهُم حَيْثُ اعتَصَرَ الألم والحزن نفوسهم، وجَمَدَ الدَّمْعُ على مُعَادَرَهَا، أَلْوَانًا مِنَ العَذَابِ فِي مَوَاطِنِ هَجْرَهِم وَالصَّبَا. الحَبَيْنُ إِلَى مَلَاعِبِ الطَّقُولَةِ الأَشْوَاقِ لَأَرْضِ الْوَطَن،ِ وَطَحَنَهُم سَحَابَةٌ مِنَ الدُّ والانكسار، ولا كَنْهُم أَنْيَابُ الْمُسْ ولِيَّة،ِ فقد حَمَلَ الأَدَبَاءُ الفَلَسْطِينِيُّونَ أَعْبَاءَ فَكَانَ صَوْتُ الْأَدِيبِ الفَلَسْطِينِي مُعَبَرًا صَادِقًا عَنِ مِحْنَةِ المهجرين الفلسطينيين،

=== BLOCK 6: الجدول التلخيصي - توجه الأدباء ===
(Component: TEMPLATE_C_TABLE.html)
Header: ["المرحلة", "التوجه الأدبي"]
Row 1: ["الْأَدَبَاءُ المهجرين الفلسطينيين بالأمل وتطلعهم إلى العَوْدَة،ِ", "فَلَم يَجْعَلِ وَتَبَنَّوْا تَجَاؤُزَ مَرْحَلَةِ النَّ بِ وَالعَوِيلِ"]
Row 2: ["مِنْ خِلَالِ تَأْكِيدِ تَمَشْكِ فِي أَعْمَاقِهِم صَوْتُ التَّمَرُدِ والاحتجاج على الوَاقِع،ِ", "فَتَمَسَّكُوا الفَلَسْطِينِيون"]
Row 3: ["شِعْرَهُم صَدَى لآلامِهِم وَإِنَّمَا رَمَوا أَحْزَاهُم جَانِبًا،", "فارتَفَعَ بالأمل الذي يَرْسُمُ لَهُم صُورَةَ الْمُسْتَقْبَلِ المُشْرِق.ِ"]

=== BLOCK 7: صوت الشاعر ===
(Component: TEMPLATE_C_BENEFIT.html)
Content: إِلَيْهَا بَعْدَ النَّكْبَةِ كَسِيرَ فقد بَرَزَ صَوْتُ الشَّاعِرِ الفَلَسْطِينِي عَبْدِ الكريم الكرمي الذي دَرَسَ فِي دِمَشْقَ قَبْلَ النَّكْبَة،ِ ثُمَّ عَادَ ومعَ ذلك يَتَمَثَلُ مَنْظَرَ القَلْبِ فَفَتَحَتْ لَهُ ذِرَاعَيْهَا، وَحَاوَلَتْ كَفَكَفَةَ آلامِه،ِ وَمُدَوَاةٍ جِرَاحٍ قَلْبِهِ الذي ظل مُعَلَّقًا بِوَطَنِهِ المُغْتَصَب. شَعْبِه،ِ عَوْدَةَ فَرَحِ وَشُمُوخِ وانتِصَار،ِ يَقُول:ُ العَوْدَةِ فِي صُورَةِ الحُلْم،ِ وَيَرَى رَى أَنَّا أَ سَتَكُونُ عَوْدَةً ظَافِرَةً تَشْهَدُهَا الأَجْيَالُ مِنْ أَبْنَاءِ

=== BLOCK 8: شعر عبد الكريم الكرمي ===
(Component: TEMPLATE_C_POEM.html)
Bio:
Verses:
غَدًا سَنَعُودُ وَالأَجْيَالُ تُصْفِي
إلى وقع الخطا عِنْدَ الْإِيَابِ

=== BLOCK 9: الإصرار الصهيوني ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الإصرار الصهيوني
Content: على إِبْقَائِهِم بَعِيدًا عَنْ أَرْضِهِم، الفِلَسْطِينين، غَيْرِ أَنَّ إِصْرَارَ الصُّهِيُونِيَّةِ وَمَعَ أَنَّ أَمَلَ العَوْدَةِ ما يزالُ يُدَاعِبُ أَحلام المهجرين الصَّهَا نَةِ وَجَدْنَا الأَدَبَاءَ يَعْمَدُونَ إِلَى فَضْحِ مُمَارَسَاتِ كذلك، قَائِمًا ثابتا لا يَتَغَيَّر. ولأَجْلِ ذلك ومَنْعِهِم مِنَ العَوْدَةِ إِلَى الوَطَنِ مَا يَزَال،ُ كُلِّ مَا أَتِيْحَ لَهَا مِنْ أَجْلِ تَنْفِيذِ إِلَى دِيَارِهِم، فقد مارَسَتِ الصُّهْيُونِيَّةٌ الفلسطينيين مِنْ حَيَّ الْعَوْدَةِ العُدْوَانِيَّةِ المَتَمَثَلَةِ بِحِرْمَانِ المهجرين ارتِكَابِ عَشَرَاتِ اسْتَعْمَلَتِ القُوَّةَ المُفْرِطَةَ وَأَقْدَمَتْ على مِنْ ثُلَثَي الشَّعْبِ الفَلَسْطِينِي فَقَدِ فكْرَةِ الطَّرْدِ الجَمَاعِيَ القَسْرِي لَأَكْثَرِ القُرَى وَالبَلْدَاتِ حِجَارَهَا أَو تَخَلْصَتْ مِنْهَا، وَأَعْلَنَاتِ وَهَدَمَتِ البُيُوتِ وَحَرَقَتْهَا وَبَاعَتْ المجازر،ٍ وَتَدْمِيرِ المنات مِنَ القُرَى وَالبَلْدَات،ِ التي هَجَرَتْ سُكَانَا مَنَاطِقَ عَسْكَرِيَّة.ٌ

=== BLOCK 10: ممارسات الترهيب ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: المَهَجْرِين الذين اقْتَلَعَنْهُم مِنْ أَرْضِهِم سِيَاسَةِ التَّرهيب والتَّخْوِيفِ لِقَمْعِ ولم تكتف بهذه المارَسَاتِ الوَحْشِيَّةِ القَائِمَةِ على بِتَحْوِيل ممتلكاتهم وأَرَاضِيهم إلى المهجرين، حَيْثُ قَامَتِ السلطات الصُّهْيُونِيَّةُ ومَنَعَتْهُم مِنَ العَوْدَةِ إِلَيْهَا، وَإِنَّمَا قَامَتْ بِابْتِلاع حقوق كانَ ابْنَا بَارًا لِفِلَسْطِين الجَبِينُ يَرْتَفِعُ صَوْتُ شَاعِرِ الْأَرْضِ مَحْمود درويش الذي مُلْكِيَّتِهَا. وأمام هذه الممارساتِ المُخْزِيَةِ اله الى لها العَوْدَةِ إِلَى دِيارهم. قصوت السَّهَايِنَةِ القَمْعِيَّة، ويُؤَكِّدَ مَنْعَهُم المهجرين مِنْ حَقِ نَذَرَ روحَهُ وَشِعْرَهُ لِخِدْمَةِ قَضِيَّتِهَا، لَيَفْعُ مَارَسَاتِ العائدين، العائدين من المرور، مؤكدًا وقوف حرس الحدود لرفض عودة بنادق اليهود يسكت أمل المهجرين، ووايل الرصاص يعلن منع مصرحًا بأن هذا الوقوف مسخر الاختبال حنين العائدين، يقول:

--- END STREAM ---
