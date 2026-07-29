# **SESSION 134**

[TASK DEFINITION]
Objective: Implement page 134.
File: `pages/page_134.html` (Note: Use the exact page number.)
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
11. You MUST preserve the EXACT Tashkeel (Harakat) from the input. Stripping diacritics is a critical failure. Do not generate bare Arabic letters without their vowels.
12. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal
14. **Page Wrappers**: The compiler will automatically wrap the final page in `TEMPLATE_C_PAGE_WRAPPER.html`. Do NOT include this template in your `[CONTENT STREAM]` blocks.
15. **Exam Section**: ONLY include the `TEMPLATE_C_EXAM.html` block if the provided raw text slice actually contains test/exam questions (e.g., keywords like "تطبيق", "امتحان"). Do NOT hallucinate an exam if it is not in the source text. **CRITICAL:** If an exam or exercise contains the answers in the raw text, you MUST use `TEMPLATE_C_EXAM_SOLVED.html` instead of `TEMPLATE_C_EXAM.html`.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[UNIQUE_ID]: b10001
[LESSON_NUMBER]: 134
[CHAPTER_TITLE]: page 134
[CATEGORY_HEADER]: 134
[SECTION_HEADER]: 134
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Cut Content Part 2 ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[UNIQUE_ID]: b10002
[BLOCK_TITLE]: الأدب العربي والنضال
[CONTENT]:
التي هَبُوا فِي وَجْهِ الدُّخَلَاءِ فِي غَضْبَةٍ عَارِمَة،ِ وَتَوْرَةِ لاهِبَةٍ للكِفَّاح والنِّضَالِ لِتَحْرِيرِ وَلَيْهِم وإعادةِ وَحْدَتِهِ التي مُزَقَت،ْ واسترداد حريته بِرُوحِ التَّوْرَةِ سُلِبَتْ وقد استَجَابَ الأَدَبُ العَرَبِيُّ هذا التطور الخلاقِ في النفسِ الْعَرَبِيَّة،ِ فَوَاكَبَ مَسِيرَةِ النِّضَال،ِ وَشَحَنَ النُّفُوسَ بِجَلَاءِ الْمُسْتَعْمِرِ العَرْبَي،َّ ذَلِكَ أَنَّ يَوْمَ والكفاح لتحرير الأُمَّةِ المُسْتَعْبَدَةِ وَتَوْحِيدِ الوَطَنِ المَمَرَّق.ِ فقد قام الأدباء بالتعبير عَنِ الفَرَحِ مُشْرِةٌ فِي تاريخ سُوْرِيَّة ؛ كَتَبَ سُطُورَهَا أَبْنَاؤُهَا الْأَبَاةُ السابع عشرَ مِنْ نَيْسَان، عَامَ سِبّ وأربعين وتِسْعِمِنَةٍ وَأَلْف، يوم مجيد، وصفحة فقد زَلْزَلَ السوريون بدمائهم. فالجلاء لَمَرَةً لِكِفاح مُرِّ خَاضَهُ الشَّعْبُ العربي في سورية منذ وَطَاتْ أَقْدَامُ الْمُسْتَعْمِرِينَ أَرْضَ سُورية.

=== BLOCK 3: Matrix Table ===
(Component: TEMPLATE_C_TABLE.html)
[UNIQUE_ID]: b10003
[HEADER_1]: أَطْمَاعَهُ الْحَبِيْثَةَ التي يَرُومُ
[HEADER_2]: الأَرْضَ تَحْتَ أَقْدَام الفرنسيين
[HEADER_3]: بِثَورات لاهِبَةٍ حَارِقَةٍ
[CELL_1]: عَمَّتْ كُلِّ مِنْطَقَةٍ مِنْ رُبُوعِ الوَطَن،ِ
[CELL_2]: أَنْسَتِ الْخَتَلَ الطَّامِعَ بِقَذَائِفِ كُلُّ بُفْعَةٍ
[CELL_3]: مِنْ بِقَاعِ سُورِيَّة إلى مِدْفَعِ هَادِرٍ يَرْمِي الطَّامِعِينَ الغَادِرِينَ

=== BLOCK 4: Standard Block ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b10004
Title: متابعة
Content: <span class="text-accent">مِنْ وَرَائِهَا تَدْنِيْسَ الْأَرْضِ وَسَلَّبَ الكَرَامَةِ حَيْثُ تَحَوَّلَتْ الحَامِدِ مُبْتَهِجًا مَنْهُوا فَمِنْ مَدِينَةِ النَّوَاعِيرِ يَقِفُ شَاعِرُ العاصي بَدْرُ الدِّينِ النَّارِ الملتهبة؛ ليُطَهَرَ بِحِمَمِهَا المنصَهِرَةِ الْأَرْضَ وَيُحْرِّرَ الإِنْسَانَ عَرْبِيَّةٌ نَاشِبَةٌ لا فَرَحَهُ العَارِم،ُ مُؤَكِدًا أَنَّ الحَلَاءَ فَرْحَةٌ عَرَبِيَّة،ٌ وَغَصَّةً فِي أَوَّلِ عِيدٍ جَلَاءٍ عَنْ سُورية؛ ليتغنى بهذا المنجز العظيم، مُظْهرًا يزيلها تعاقب السنين. يقول:</span>

=== BLOCK 5: Poem 1 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b10005
[RIGHT_HEMISTICH]: إِرْغَام يَوْمُ الخَلَاءِ هُوَ الدُّنْيَا وَزَهُوها
[LEFT_HEMISTICH]: لنا ابتهاج وللباغِينَ

=== BLOCK 6: Standard Block ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b10006
Title: الشاعر عمر أبو ريشة
Content: <span class="text-accent">مِنَ الْخَرَيَّةِ ومِنْ حَلَبَ يَنْهَضُ ابن منبج الشاعر عُمر أبو ريشة لِيُصَوَرَ فَرْحَةَ الانتصار بِجَلَاءِ التَلِ عَنْ أَرْضِ الوَطَن،ِ فَيَطْلُبُ ها أَنَّ لِقَاءَهَا قَدْ حَسن وجاد بعد تلك الفرقة التي ضاقَ فِيهَا الصَّدْرُ من شِدَّة الوجد والشَّوْقِ يَقُول:ُ وَيُؤْكِّدُ أَنْ تَسِيرَ بَرَهْهِ وَفَخَارِ فَوْقَ تَرَى بلادنا، وأَنْ تَخْتَالَ كما تختال العروس، وتُجَرَرَ أَذيالَ الشَّهْبِ السَّاطِعَة،ِ وَتُزَيْنَ بِمَا أَرْجَاءَ بِلَادِنَا،</span>

=== BLOCK 7: Poem 2 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b10007
[RIGHT_HEMISTICH]: يا عروس المجد تِيْهِي واسحبي
[LEFT_HEMISTICH]: فِي مَغَانِينا ذُيُولَ الشَّهْبِ
[RIGHT_HEMISTICH_2]: بَعْدَمَا طَالَ جَوَى المغترب
[LEFT_HEMISTICH_2]: يا عروس المجدِ طَابَ الْمُلْتَقَى

=== BLOCK 8: Benefit Warning ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[UNIQUE_ID]: b10008
[CONTENT]: هَنَاكَ عَدُوا مُجْرِمًا ما زال يستبيحُ الأَرْضَ العَرَبِيَّةَ وَيَنْتَهِكُ حُرُمَاتِهَا ومَعَ نَشْوةِ النَّصْر،ِ وَغَمْرَةِ أَفراح الوَطَنِ بِهِ لَا يَنسَى الأَدَبَاءُ أَنَّ ويَتَعَدَّى على مُقَدَّسَاتِها. هذا العَدُو هو الصَّهْيُونِيَّة التي تَنْتَهِجُ مَبْدَأَ الاجْتِيَاحِ القَسْرِي، واحتلال أرض الآخرين بِقُوَّةِ السَّلَاحِ وَالنَّارِ؛ ظل المحتل الصهيوني وَاقِعًا صَعْبًا لِذَا نَجِدُ هَؤُلاء الأدباء يفضحون جرائم الصهاينة بحق أبناء فلسطين، حَيْثُ عَاشَ أبناء فلسطين في الاضْطِهَادِ وَالقَهْرِ مِنْ تَشْرِيدٍ وَعَجِيرِ إِلَى قَ لِ انوا فِيهِ مِنْ ظُلم المحتلين الطَّغَاةِ وإذلالهم، فقد ظل هذا المحتل يَسُومُ الفلسطينيين ألوان المصير الفاجع الذي يلقاه الحالمون بالعودة إلى جماعي مروع بهدف إرْغَامِهِم على مُعَادَرَةِ البلاد، فالشاعر محمود درويش يشير إلى فلسطين حيث امتلا طريق عودتهم بجثث اختطف الصهاينة أرواحها وصادروا حياتها. يَقُول:ُ

=== BLOCK 9: Poem 3 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b10009
[RIGHT_HEMISTICH]: كُلُّ القَوَافِلِ قَبْلَهُم غَاصَتْ
[LEFT_HEMISTICH]: وَكَانَ النَّهْرُ يَبْصُقُ ضِفَتَيْهِ
[RIGHT_HEMISTICH_2]: قطَعًا مِنَ اللَّحْمِ الْمُفَتَتِ
[LEFT_HEMISTICH_2]: في وُجُوهِ الْعَائِدِينَ

=== BLOCK 10: Standard Block ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b10010
Title: مأساة فلسطين
Content: <span class="text-accent">وأشجار ليمون، وحجر يروي ملحمة الكفاح الدامي والثورة وحينما يُذكر اسم فَلَسْطِينَ يلوح في الأفق أغصان زيتون، الأدب مانحة الكلمة معنى خاصا، والخَرْفَ طَعْمًا خاصا اللاهبة على أرض الرسالات السماوية. إنها مأساة فلسطين التي دخلت ميدان والأدب نكهة خاصة. فقد عاشَتِ القَضِيَّةُ الفلسطينية مع الأدباء، ولا سيما الأدباء الفلسْطِينيين، الذينَ تَنَقْسُوا هواءَهَا وَرَافَقُوها في أَشَدَ أَرْمَائِهَا، وَأَعْظم انتصاراتها، فها هم يبرزون تمسك الفلسطينيين بِفِكْرَةِ النَّصَالِ فِي سَبِيلِ الوُجُود،ِ فرغم كُلِّ مَا اقْتَرَفَتْهُ الصَّهْيُونِيَّةُ التضالِ حَادِيهِم، والتَّمَسُّكُ مِنْ جرائم وحشية، بحقِّ أَبْنَاءِ فِلَسْطِينِ إِلَّا أَنَّهُم لَم يَسْتَسْلِمُوا لَهَا، أو يهابُوا فَتُكها، بل ظل الإصرار على بالكِفَاحِ رَائِدَهُم فَقَدْ نَذَرُوا أَنْفُسَهُم للمطالبة بالحقوق والدفاع عَنِ الْأَرْضِ وَالكَرَامَةِ والعرض، فالتحمُوا بِرَابِ الوطن التحامًا عضويا متماسكا، فأصبحوا جزءًا لا يَتَجَنَّا مِنْه،ُ حَتَى غدا الإنسان الفلسطيني عضوا مِن أَعْضَاء هَذِهِ الأَرْض،ِ مُتَوَجَدًا بِترابها. فها هُوَ كَبِير أَرْضَه،ُ فَيُعْلِنُ التَّحَدِي بِنَبْرَةِ وَائِقَةٍ لَا شُعَرَاءِ الأَرْضِ الْخَتَلَّةِ الشَّاعِرِ تَوْفِيقِ زَيَّادٍ يَضَعُ نَفْسَهُ فِي مُوَاجَهَةٍ سَافِرَةِ مَعَ عَدُةٍ مُغْتَصِبِ يُشَارِكُهُ تعرف الاستسلام أو تُقِرُ بِالإِذْعَان، مؤكدًا متابعة الشير في طريق الكفاح والتصال والقَاوَمَة،ِ والثبات في الأَرْضِ والتَّمَسُّكَ بها. يَقُول:ُ</span>

=== BLOCK 11: Poem 4 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b10011
[RIGHT_HEMISTICH]: أَهْوَنُ أَلْفَ مَرَّهُ
[LEFT_HEMISTICH]: أَنْ تُدْخِلُوا الْفِيلَ بِثَقُبِ إِبْرَهُ
[RIGHT_HEMISTICH_2]: مِنْ أَنْ تُمِيتُوا بِاضْطِهَادِكُم وَمِيضَ فِكْرَهُ
[LEFT_HEMISTICH_2]: وتَحْرِفُونَا عَنْ طَرِيْقِنَا الذي اخْتَرْنَاهُ قَيْدَ شَعْرَهُ

=== BLOCK 12: Cut Content Part 1 ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
[UNIQUE_ID]: b10012
[BLOCK_TITLE]: متابعة
[CONTENT]:
وَمَعَ أَنَّ هِجْرَة الفلسطينين قد أَمْسَتْ وَمَعَ أَنَّ انتاعِ الفَلَسْطِينِي مِنْ أَرْضِهِ قَد بَاتَ أَمْرًا واقعا لا عَجَالَ لَعَدَمِ الاعتراف بِه،ِ
حقيقة مرة لا عناص مِن تَجْرُعِ عَلَقَمِها، إِلَّا أَنَّ الفَلَسْطِينِي قَد سَيْطَرَ على أَشْوَاقِهِ العَمِيْقَة،ِ وَرَوْضَ حَنِيْنَهُ الوَثَابَ الأَرْضِ الْوَطَنِ التي
-  -  -

--- END STREAM ---
