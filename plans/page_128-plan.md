# **SESSION 128**

[TASK DEFINITION]
Objective: Implement page 128.
File: `pages/page_128.html`
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
[UNIQUE_ID]: b79607
[LESSON_NUMBER]: 128
[CHAPTER_TITLE]: page 128
[CATEGORY_HEADER]: 128
[SECTION_HEADER]: 128
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Cut Content Continuation (I'rab) ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[UNIQUE_ID]: b98487
[BLOCK_TITLE]: الإعراب
[CONTENT]: محل رفع، فَاعِلْ يَا سَمَاء:ُ يا، حَرْفُ نِدَاءٍ سَمَاء،ُ مُنَادى نَكِرَةً مَقْصُودَة،ٌ مَبْنِي على الصَّمَّة،ِ في محل نصب على النداء. جُلَةٌ إِنَّهَا فَرْحَةُ الحَيَاةِ(: استئنافية، لا محل لها مِنَ الإعراب جملةً مِيدِي(: اسْتئنافِيَّة،ٌ لَا مَحَلَّ لها مِنَ الإعراب جُمْلَةً )هَلِلِي( : مَعْطُوفَة،ً لا تحل لها مِنَ الإعراب.

=== BLOCK 3: Verse 1 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b97485
[POEM_TITLE]: البيت الأول
[POET_NAME]:
[RIGHT_HEMISTICH]: وَتَفَنَّي بِأَمَّتِي إِنَّهَا عادَتْ
[LEFT_HEMISTICH]: وَإِنَّا فِي أَرْضِنا طُلَقَاءُ

=== BLOCK 4: المفردات والشرح ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b29900
Title: المفردات والشرح
Content: <span class="font-bold text-accent">المفردات:</span> تفقي: أَشِيدِي طَلَقَاء: أَحْرار. وطلقاء : صِفَةٌ مُشَبَّهَةٌ باسم الفاعل، فعلها : طلق<br><span class="font-bold text-accent">الشرح:</span> تباهي أيتها السَّمَاءُ بِأَمَّتِنَا العَربيَّة،ِ وأَشِيْدِي بها؛ فَقَدْ تَخَلَّصَتْ مِنْ قُيُودِ المستَعْمِرِين، واسْتَعَادَتْ إِرَادَهَا المصادَرَة،َ واستَرَدَتِ اسْتِقْلَالَ قَرَارِهَا المَنْهُوب،ِ فَهَا نَحْنُ نَنْعُمُ بالتَّحَرُرِ فَوْقَ تَرَى بِلَادِنَا الْحَبيبة.

=== BLOCK 5: الفكرة (Orange Box) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[UNIQUE_ID]: b43688
Content: <span class="font-bold">الفكرة:</span> الدَّعْوَة إلى الإِشَادَةِ بِالْأُمَّةِ العَرَبِيَّةِ لِتَحَرُرِهَا وَاسْتِقْلالها الاعتِزَازُ بِتَحَرُّرِ الْأُمَّةِ الْعَرَبِيَّةِ(.

=== BLOCK 6: الأساليب ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b57964
Title: الأساليب
Content: <span class="font-bold text-accent">الأساليب:</span> تفتي بأمتي : أسلوب أمر. صِيفَتُهُ فِعل أمر. إنها عادَ ،( )إِنَّا فِي أَرْضِنَا طَلَقَاءُ(: أسلوب توكيد المؤكد: إن. نوع التوكيد: جائز.

=== BLOCK 7: الإعراب (Row 1) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b40373
[WORD_1]: وَتَغَنَّي
[DETAILS_1]: الوَاو،ِ حَرْفُ عَطْفٍ تَغَي،َّ فِعْلُ أَمْرٍ مَبْنِي على حَذْفِ النُّون،ِ لَأَنَّ مُضَارِعَهُ مِنَ الْأَفْعَالِ الخَمْسَة.ِ والياء، صَمِيرٌ مُتَّصِلِّ مبني على السكون فِي مَحَلِ رَفْع،ِ فاعل
[UNIQUE_ID_2]: b65097
[WORD_2]: بِأَمَّتِي
[DETAILS_2]: الباء، حَرْفُ جَر. أمتي، اسم تجرور، وعلامَةُ جَرِهِ الكَسْرَةُ الظَّاهِرَة،ُ والياء، ضَمِيرٌ مُتَصِلُّ مَبْنِيَّ على السكون فِي مَحَلِّ جَر،َ مُضَافَ إِلَيْهِ

=== BLOCK 8: الإعراب (Row 2) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b79596
[WORD_1]: إِنَّهَا
[DETAILS_1]: إِن،َّ حَرْفٌ مُشَبَّهُ بِالفِعْل.ِ وها، صَمِيرٌ مُتَصِلِّ مَبْنِي على السُّكُونِ فِي مَحَلَّ نَصْب،ِ اسمُ إِنَّ
[UNIQUE_ID_2]: b93074
[WORD_2]: عَادَتْ
[DETAILS_2]: فعل ماض، مَبْنِي على الفَتْحَةِ؛ لاتِصَالِهِ بِتَاءِ التَّأْنِيثِ السَّاكِنَةِ وَالنَّاء،ُ حَرْفُ تَأْنِيتِ لَا تَحَلَّ لَهُ مِنَ الإعراب.

=== BLOCK 9: الإعراب (Row 3) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b76357
[WORD_1]: وَإِنَّا
[DETAILS_1]: الواو، حَرْفُ عَطْفٍ إِن،َّ حَرْفٌ مُشَيَّة بالفعل. ونا، ضَمِيرٌ مُتَّصِلِّ مَبْنِي على السكون في محل نَصْب،ٍ اسم إِنَّ
[UNIQUE_ID_2]: b36217
[WORD_2]: طَلَقَاءُ
[DETAILS_2]: خَبَرٌ مَرْفُوع. جُمْلَةُ )تَغَنَّي( : مَعْطُوفَة،ً لا محل لها مِنَ الإعراب. جُمْلَةُ )إِنَّا عَادَتْ(: اسْتَئنافِيَّة،ٌ لا محل لها مِنَ الإعراب جُمْلَهُ إِنَّا فِي أَرْضِنَا طَلَقَاءُ( : مَعْطُوفَة،ٌ لَا مَحَل لها مِنَ الإعراب.

=== BLOCK 10: Verse 2 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b06518
[POEM_TITLE]: البيت الثاني
[POET_NAME]:
[RIGHT_HEMISTICH]: أَيُّهَا النَّائِهُونَ فِي مَهْمَهِ الْأَمْسِ
[LEFT_HEMISTICH]: سرابٌ دُرُوبُكُمْ وَشَقَاءُ

=== BLOCK 11: المفردات والشرح والفكرة ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b38137
Title: المفردات والشرح
Content: <span class="font-bold text-accent">المفردات:</span> النَّائِهُونَ : المَتَخَلِفُونَ عَنْ رَكْبِ الوَحْدَةِ مَهْمَه: المفازة البعيدة، وهي الصَّحراء الواسعة، أو البَلَدَ القَفْر. سراب : وَهُم، وهو ما يرى في نِصْفِ النَّهَارِ عِنْدَ اسْتِدَادِ الحر كالماء في الصَّحَارَى يَلْصَقُ بِالأَرْضِ والنَّائِهُونَ : اسم فاعل، فعله: تاه.<br><span class="font-bold text-accent">الشرح:</span> أَيُّهَا المَتَحَلِّفُونَ عَنْ رَكْبِ الوَحْدَة،ِ يَا مَنْ تَتَشَبَّنُونَ بِأَوْهَامِ الْمَاضِي، وَتَتَخَبَّطُونَ بِمَتَاهَاتِهِ المُضِلَّة،ِ إِنَّ سَبِيلَ الفُرْقَةِ وَالتَّجْزِيَّةِ الذي اخْتَرَمُوهُ طريق مَفْرُوسُ بِالأَوْهَام،ِ مُعَبَّدُ بِالمُشَقَة،ِ مَرْصُوفُ بِالعَذَابِب<br><span class="font-bold text-accent">الفكرة:</span> الدَّعْوَة إلى الوَحْدَةِ العَرَبِيَّةِ تَحْفِيز المترددين للالتحاق بِرَكْبِ الوَحْدَةِ العَرَبِيَّةِ(، التَّحْذِيرَ مِنَ التَّجْزِنَةِ وَنَبْدَ الْفُرْقَةِ(.<br><span class="font-bold text-accent">الشُّعُور:</span> حب، وغيرة الأداة التراكيب المثال: سَرَابٌ دُرُوبُكُمْ وَشَمَاء.ُ<br><span class="font-bold text-accent">البلاغة:</span> )سَرَابٌ دُرُوبُكُمُ(: تشبية بليغ

=== BLOCK 12: الإعراب (Row 1) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b95887
[WORD_1]: أَيُّهَا
[DETAILS_1]: أَي،ُّ مُنادى نَكِرَةٌ مَقْصُودَةٌ مَبْنِي على الصَّمَ فِي تَكَلِّ نَصْبِ على النداء. وها، للتنبيه.
[UNIQUE_ID_2]: b82226
[WORD_2]: النَّائِهُونَ
[DETAILS_2]: صِفَةٌ مَرْفُوعَة،ٌ وعلامَةُ رَفْعِهَا الواو؛ لأَنَّهَا جَمْعُ مُذَكّر سالم، والتون، عِوَضُ عَنِ التَّنْوِينِ فِي الاسم المفرد.

=== BLOCK 13: الإعراب (Row 2) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b69205
[WORD_1]: فِي مَهْمَهِ
[DETAILS_1]: في، حَرْفُ جَرٍ مَهْمَه،ِ اسم مجرور، وعلامةُ جَرَهِ الكَسْرَةُ الظَّاهِرَةُ الأَمْسِ : مُضَافُ إِلِيهِ يَجْرُورٌ سَرَابٌ : خَبَرٌ مُقَدَّمَ مَرْفُوعٌ
[UNIQUE_ID_2]: b30778
[WORD_2]: دُرُوبُكُمْ
[DETAILS_2]: مُبْتَدَةٌ مُؤَخَرُ مَرْفُوعٌ وَشَقَاء:ُ الواو، حَرْفُ عَطْفٍ شَقَاء،ُ اسمٌ مَعْطُوفٌ مَرْفُوعٌ جَمْلَهُ سَرَابٌ دُرُوبُكُمْ( : اسْتِتَنَافِيَّة،ٌ لَا مَحَكَ لَا مِنَ الإعراب.

=== BLOCK 14: Verse 3 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b49792
[POEM_TITLE]: البيت الثالث
[POET_NAME]:
[RIGHT_HEMISTICH]: أَزْهَرَتْ وَاحَةُ العُرُوبَةِ وَافْتَرَّتْ
[LEFT_HEMISTICH]: وماسَتْ جِنَانُهَا الخَضْرَاءُ

=== BLOCK 15: المفردات والشرح ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b70059
Title: المفردات والشرح
Content: <span class="font-bold text-accent">المفردات:</span> واحة ساحة. افْتَرَت : بَدَا عَلَهَا الابتِسَامِ مَاسَتْ تَبَخْتَرَتْ وَاخْتَالَتْ . جنانها المفرد : جَنَّة، وهي الحديقة ذات الشجر، أو البُسْتَان. والخضراء: صِفَةٌ مُشَبَّهَةٌ باسم الفاعل فعلها خضر<br><span class="font-bold text-accent">الشرح:</span> بِقِيَامِ الوَحْدَةِ اكْتَسَتْ سَاحَةُ العُرُوبَةِ رَبِّيْعًا، بَعْدَ أَنْ أَجْدَبَتْهَا التَّجْزِنَة،ُ حَيْثُ تَفَتَّحَتْ فِيهَا أَكْمَامُ الرُّهُورِ فَبَدَتْ بَاسِمَةَ التَّغْرِ مِنْ شِدَّةِ حُسْنِهَا ، وَرَاحَتْ حَدَائِقُهَا الغَنَّاءُ تَخْتَالُ وَتَتَبَخْتَرُ تِيْهَا مِنْ رَوْعَةِ جَمَالها.<br><span class="font-bold text-accent">الفكرة:</span> الإشارة إلى مارِ الوَحْدَةِ وَصْفِ جَمَالِ الحَيَاةِ بَعْدَ قِيَامِ الوَحْدَةِ(.<br><span class="font-bold text-accent">البلاغة:</span> )ماسَتْ جِنَاها( : استِعَارَةُ مَكْنِيَّة.

=== BLOCK 16: الإعراب (Row 1) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b95169
[WORD_1]: وَاحَةٌ
[DETAILS_1]: فَاعِلَ مَرْفُوعٌ العُرُوبَةِ مُضَافُ إليهِ يَجْرُورٌ جَنَاتُها : فَاعِلٌ مَرْفُوعُ
[UNIQUE_ID_2]: b92352
[WORD_2]: الخَضْرَاءُ
[DETAILS_2]: صِفَةٌ مَرْفُوعَةٌ جُمْلَهُ أَزْهَرَتْ وَاحَةُ العُرُوبَةِ : اسْتِنَافِيَّة،ٌ لا محل لها مِنَ الإعراب . جُمَلَةُ افْتَرَتْ(، وجُمْلَةً )ماسَتْ جِنَانُهَا : مَعْطُوفَة،ٌ لَا مَحَلَّ لها مِنَ الإعراب.

=== BLOCK 17: Verse 4 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b49567
[POEM_TITLE]: البيت الرابع
[POET_NAME]:
[RIGHT_HEMISTICH]: وَتَشَنَّتْ فِيهَا الْجَدَاوِلُ سَكْرَى
[LEFT_HEMISTICH]: وَتَرَامَتْ فِي رَبِّعِهَا الْأَفْيَاءُ

=== BLOCK 18: المفردات والشرح ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b14401
Title: المفردات والشرح
Content: <span class="font-bold text-accent">المفردات:</span> تَفَنَّت:ُ تَمَا يَلَتْ وَتَبَخْتَرَتْ الجداول : السَّوَاقِي ربعها : الجمع : ربوع، وهو المنزل والمسكن الأفياء المفرد: فيء، وهو الظل. وسكرى : صفَةٌ مُشَبَّهَةٌ باسم الفاعل فعلها : سكر<br><span class="font-bold text-accent">الشرح:</span> بِقِيَامِ الوَحْدَةِ بَدَتْ فِي سَاحَةِ العُرُوبَةِ جَدَاوِلُ المَاءِ الرَّقْرَاقَةِ تَتَمَايَلُ مُنْتَشِيَةً كَمَخْمُورٍ ثَمَلِ دَارَتْ الخَمْرَةُ بِرَأْسِه،ِ وَرَاحَتْ رُبُوعُهَا تَضُحُ مِنْ تَزَاحُمِ الطَّلَالِ الوَارِفَةِ التِي تَرَاكَمَتْ فيها<br><span class="font-bold text-accent">الفكرة:</span> الإشارة إلى تمارِ الوَحْدَةِ وَصْفَ جَمَالِ الْحَيَاةِ بَعْدَ قِيَامٍ الوَحْدَة(. الشُّعُور: فرح الأداة : التَّراكيب المثال : تَثَنَّتْ فِيهَا الجَدَاوِلُ سَكْرَى<br><span class="font-bold text-accent">البلاغة:</span> )تَثَنَّتُ الجَدَاوِلُ(، )الجَدَاوِلُ سَكْرَى( : استعارَةً مَكْنِيَّة.

=== BLOCK 19: الإعراب (Row 1) ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID_1]: b91900
[WORD_1]: وَتَثَنَّتْ
[DETAILS_1]: وَتَرَامَتْ : الواو، حَرْفُ عَطْفٍ تَشَنَّتْ تَرَامَتْ فِعل ماض، مَبْنِي على الفَتْحَةِ المُقَدَّرَةِ على الأَلِفِ الْمَحْذُوفَةِ لَاتِصَالِهِ بِتَاءِ التانيثِ السَّاكِنَة.ِ والتَّاء،ُ حَرْفُ تَأْنيث لا مَحَلَّ لَهُ مِنَ الإعراب
[UNIQUE_ID_2]: b99808
[WORD_2]: فيها
[DETAILS_2]: في، حَرْفُ جة.ٍ وها، ضَمِيرٌ مُتَّصِلِّ مَبْنِي على السُّكُونِ فِي مَحَلِّ جَة،ٍ بِحَرْفِ الجز. والجار والمَجْرُورُ مُتَعَلقان بِالفِعْلِ تَشَنَّتْ(. الجَدَاوِلُ الأَفْيَاء:ُ فَاعِلْ مَرْفُوعٌ

=== BLOCK 20: الإعراب (Row 2) ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b32341
[TARGET_WORD]: سَكْرَى
[IRAB_ANALYSIS]: حالٌ مَنْصُوبَة،ٌ وعلامَةُ نَصْبِهَا الفَتْحَةُ المُقَدَّرَةُ على الأَلِف،ِ مَنَعَ ظُهُورَهَا التَّعَدُّرُ جُمْلَةُ تَشَنَّتْ فِيهَا الجَدَاوِلُ( وجُمَلَهُ تَرَامَتْ فِي رَبِّعِهَا الأَفْيَاءُ(: مَعْطُوفَة،ٌ لَا مَحَكَ لها مِنَ الإعراب.

--- END STREAM ---
