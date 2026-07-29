# **SESSION 145**

[TASK DEFINITION]
Objective: Implement page 145.
File: `pages/page_145.html` (Note: Use the exact page number.)
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
[LESSON_NUMBER]: 145
[CHAPTER_TITLE]: page 145
[CATEGORY_HEADER]: 145
[SECTION_HEADER]: 145
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Cut Block Part 2 ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[UNIQUE_ID]: b04905
[BLOCK_TITLE]: الأدب الاجتماعي
[CONTENT]: وسيلة فنيةً واحِدَةً مِنَ الوسائِلِ التِي جَسَدَتْ العلاقة بين هذا الأدب والمجتمع، ثُمَّ ادرس يُقِلُ النَّص السَّابق الأدب الاجتماعي. وضح<br>المحتوى الجديد للأدب.

=== BLOCK 3: Poem ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b79284
[POEM_TITLE]: قَالَ الشَّاعِرُ حافظ إبراهيم:
[UNIQUE_ID_BIO]: b52383
[POET_NAME]: حافظ إبراهيم
[RIGHT_HEMISTICH]: اللَّهِ دَرُّهُمُ فَكَمْ مِنْ بائسٍ<br>ترْمِي بِهِ الدُّنْيَا فَمِنْ جُوْعِ إِلى<br>عَيْنٌ مُسَهَّدَةٌ وَقَلْبٌ وَاجِفٌ
[LEFT_HEMISTICH]: عري إلى سقم إلى إقلال<br>جَمِ الوَجِيْعَةِ سَيِّيَ الْأَحْوَالِ<br>نفس مُرَوَّعَةً وَجَيْبٌ خالي

=== BLOCK 4: Question / Rule ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b59103
[BLOCK_TITLE]: دلالتها الاجتماعية
[CONTENT]: حَدّدُ مِنَ الأبيات السابقة صورة ثُمَّ وَصَحْ المجسدة للمحتوى الجديد للأدب. تُعَدُّ الصُّورة المعبرة إحدى الوسائل الفنية<br>المنهج الاجتماعي في النقد الأدبي: إجابات الأسئلة التطبيقية التي تدور حول<br>الأبيات ظاهرة الفقر والعوز. الاجتماعية التي تدور حولها البَلَاء،ُ شَجْوي، جياعًا(.

=== BLOCK 5: Solved Exercises 1 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b82259
[QUESTION_NUMBER]: ۱
[QUESTION_TEXT]: الظاهرة
[ANSWER_TEXT]: المُعْجَمُ اللغويُّ لِلمُعاناة: )الأَحْرَانُ<br>فَنَّا طليعيًا. الْمُجْتَمَعِ مَا تَهُ ثُمَّ يُعِيدُها إليهِ علاقة تبادلية فالشاعر يأخُذُ مِنَ

=== BLOCK 6: Solved Exercises 2 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b74614
[QUESTION_NUMBER]: ۲
[QUESTION_TEXT]: العلاقةُ بَينَ الأدب والمجتمع العلاقة بين الأدب والمجتمع<br>- الوسيلة الفنية التي جَسَدَتْ المحتوى الجديد للأدب
[ANSWER_TEXT]: وَحْدَةِ الشَّكْلِ وَالْمَضَمُونِ؛ وحدة الشكل والمضمون، فقد حرص الشاعر على<br>وَسْمُوه.ِ وَيَنْبَغِي أَنْ يكونَ مَفْهُومًا، كما حافظ على رُقِيَ الشَّكْلِ الْفَنِّي إِذْ كَانَ الْمَضْمُونُ واضحا ، انطلاقا مِنْ أَنَّ الأَدَبَ يَتَوَجُهُ إِلَى جُمْهُور،ٍ<br>المعنى بما أوحَتْ بِهِ مِنَ الْمَشَفَّةِ وَالْمَعاناة - تحديد الصورة : )ترمي بِهِ الدنيا(. - دلالتها الاجتماعية : خدمت هذه الصورة<br>مُعَانَاةِ الْفَقِيْر.ِ والحاجة، وما أثارته من مشاعر الألم والحزن، مُعَبَرَةً بذلك عَنْ مَظَاهِرِ

=== BLOCK 7: Subheader ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b97080
[BLOCK_TITLE]: المنهج النفسي في النقد الأدبي
[CONTENT]: الاستيعاب والفهم والتحليل:<br>المؤلفون<br>الأَدَي، وفي مَعْرِفَةِ العالم النَّفْسِي

=== BLOCK 8: Solved Exercises 3 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b47389
[QUESTION_NUMBER]: س١
[QUESTION_TEXT]: علام يعتمدُ المَنْهَجُ النَّفْسِيُّ فِي التَّقْدِ؟ والامَ يسعى؟
[ANSWER_TEXT]: يَعْتَمِدُ مُعْطَيَاتِ عِلْمِ النَّفْسِ فِي دِرَاسَةِ النَّ<br>أَهداف، منها: محاولة اكتشاف ثُمَّ فِي مَعْرِفَةِ ذَلِكَ العالم. والمَنْهَج النَّفْسِي في النَّقْدِ الأَدَبَيِّ لِمُبْدِعِهِ ثُمَّ فِي مَعْرِفَةِ النَّ نَفْسِه،ِ أو فِي مَعْرِفَةِ النَّصِ<br>تَجْعَلُ مِنْهُ مُبْدِعًا، واكتشافِ عَمَلِيَّةِ الإِبداع نَفْسِهَا، الخصائص النَّفْسِيَّةِ الْمُمَيِّرَةِ لِمُبْدِعِ النَّصِ مِنْ سِواهُ مِنَ النَّاسِ العادين؛ أي الخصائص التي

=== BLOCK 9: Solved Exercises 4 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b75620
[QUESTION_NUMBER]: س٢
[QUESTION_TEXT]: ما الحقُولُ التي يتحرك فيها المنهج النَّفْسِيُّ؟
[ANSWER_TEXT]: يَتَحَرَّلُ الْمَنْهَجُ بِينَ ثلاثةِ حُقُول: عِلْمٍ واكتشاف الآثارِ النَّفْسِيَّةِ لِنَّصَ في القراء.<br>ذَاتَا مِنَ العَمَلِيَّاتِ النَّفْسِيَّة،ِ وَالْمُبَدِعِ بِوَصْفِهِ والإشارات والصور التي تحيل بدورها على مجموعَةٍ النَّفْس،ِ والنَّصَ الأدبي بِوَصْفِهِ مجموعَةَ مِنَ الرُّمُوز

=== BLOCK 10: Solved Exercises 5 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b36738
[QUESTION_NUMBER]: س٣
[QUESTION_TEXT]: ما الَّذِي يَكْتَشِفُهُ النَّاقِدُ مِنْ دِرَاسِتِهِ النَّ الأَدَبِيَّ وَفْقَ الْمَنْهَجِ النَّفْسِي؟
[ANSWER_TEXT]: تمتلك مِنَ الخصائص النَّفْسِيَّةِ مَا يُيَزُهَا مِنَ النَّاسِ العادِينَ<br>وَحَصَائِصِهِ النَّفْسِيَّة.ِ تفسير دوافعه إلى الكِتَابَةِ مَعْرِفَةِ شَخْصِيَّةِ الْمُبْدِع، وَمِنْ مُحاولة النَّفْسِي مَكِّنُ النَّاقِدَ مِنْ - دراسةُ النَّص الأَدَى وَفْقَ الْمَنْهَجِ

=== BLOCK 11: Solved Exercises 6 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b56042
[QUESTION_NUMBER]: س٤
[QUESTION_TEXT]: يُعَدُ النَّصُّ الأَدَبِيُّ وثيقة دالةً على نَفْسِيَّةِ مُبْدِعِه.ِ ما المرتكزات التي يَجِبُ تَتَبُّعُهَا لِمَعْرِفَةِ شَخْصِيَّةِ الْمَ دِعِ؟
[ANSWER_TEXT]: النَّ الْأَدَبِيُّ فِي الْمَنْهَحِ<br>- يرى فرويد أنَّ الأَدَبَ وَالْفَنَّ تَعْبِيرٌ عَنِ فِي داخِلِهِ رُمُوزًا وإشارات وصورًا وأفكارا.

=== BLOCK 12: Solved Exercises 7 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b04218
[QUESTION_NUMBER]: س٥
[QUESTION_TEXT]: النَّفْسِي يُتِلُ وَثِيقَةً دالَّةَ على نَفْسِيَّةِ مُبْدِعِه،ِ إِذْ يَتَصَمَّنُ الْمُكْبُونَةِ مَادَةً ثَرِيَّة بالإشارات الدالة على الرَّغَبَاتِ الثاني. وضح ذلِكَ مِمَّا وَرَدَ فِي المقطع
[ANSWER_TEXT]: لأنه يرى أنَّ العَمَلَ الأَدَبِيَّ اللا وعي الفَرْدِي.<br>وَفَتِهِ - ٦ تباينتْ نَظْرَةُ )يونغ لِتِلْكَ الرَّعْبَاتِ وَالمَخَاوِفِ التي تُجْهَرُ بِنَفْسِهَا فِي أَدَبِهِ لِمُبْدِعِه، وعلى مخاوفه أيضًا، فالاشُعُور،ُ عِنْدَه،ُ مُسْتَوَدَعْ<br>معينة. - أدلر : يرى أن الباعث الأساسي أدلر( ليواعِثِ الإبداع. وَحْ نَطْرَةً كُلِّ مِنْهما.

=== BLOCK 13: Solved Exercises 8 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b31495
[QUESTION_NUMBER]: س٦
[QUESTION_TEXT]: يونغ: يرجع عملية الإبداع إلى حالة نفسية القدماء. عِنْدَ بَعْضِ التَّقَادِ العَرَبِ بُدُورُ الْمَنْهَحِ النَّفْسِيِّ أو في حُبّ ال هور . ظَهَرَتْ للإبداع التعويضُ عَنِ النَّقْصِ أو الرَّغْبَةِ في السيطرة
[ANSWER_TEXT]: مِنْ قَوْلِ عَنْ بِوَاعِتِ الشَّعْرِ ذَلِكَ : - ما تَضَمَّنَهُ كِتَابُ ابْنِ فَتَيْبَةِ الشَّعْرُ والشَّعراء وَضَحْ ذَلِكَ مِنْ فَهْمِكَ الْمُقْطَعَ الثَّالِث.َ

=== BLOCK 14: Solved Exercises 9 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b25498
[QUESTION_NUMBER]: س٧
[QUESTION_TEXT]: مِنْ بواكيرٍ كان التِي يَفْرِضُ الشَّعْرُ نَفْسَهُ فيها. - ما والغَضَب،ِ وَمِنْ قَوْلِ آخِرَ عَنِ الأوقات والأماكن ودوافعه، كاللَّمَع، والشَّوْق،ِ والشراب، والطَّرَب،ِ النَّصَيِّ فِيه.ِ إلى العلاقةِ بَيْنَ نَفْسِيَّةِ الْمُتَلَقِي وأَثَرَ طبائع الشعراء. - إشارة ابن طباطبا القاضي الجرجان قد فَصَّلَ القَوْلَ فِيهِ عَنِ اختلاف
[ANSWER_TEXT]: نُوا فِي ضَوْءِ العُقْدَةِ مِنْهُما ؟ فَسَّرَ العقَادُ شَخْصِيَّةَ أَبِي شَخْصِيَّةِ أَبِي نُواسِ وإلامَ تَوَصَّلَ كُلِّ علام اعتمد العقاد ومُحَمَّدُ النويهي في تفسير<br>الحِسْمَانِي فِي تَوتُرِ أَعْصَابِه،ِ وزواج دراستِهِ إِلى مجْمُوعَةٍ مِنَ ال تائج، مِنْ أَهَمَهَا دَوْرُ اضطرابه المَرَضِيَّةِ المعروفة بالنَّرْجِسِيَّة"، وانتهى التويهي، في<br>النَّفْسِي. أُهِ مِنْ رَجُل آخر بِعْدَ وفاة أبيه.

=== BLOCK 15: Solved Exercises 10 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b28097
[QUESTION_NUMBER]: س٩
[QUESTION_TEXT]: ادْكُرْ بَعْضَ الآخِذ التي أُخِذَتْ على المنهج
[ANSWER_TEXT]: مِنْ هذه المآخذ : - النظر إلى النَّصَ<br>- ليسَ كُلُّ نَيِّ أَدَيَّ قَابلا قوانين، ومن الخطأ تطبيقها على الأدب. ٣ الأَدَتِي بِوَصْفِهِ وَثِيقَةَ نَفْسِيَّة. - مَقُولَاتُ عِلْمِ النَّفْسِ فَرُوضٌ وليست<br>على جَاهِرَةِ الأَمْرُ الذي لا يُحَرِّضُ النَّاقِدَ النَّفْسِي في النَّقْدِ الأَدَبِي يَعْنِي وجُودَ مَعْرِفَةٍ للتحليل والدِّرَاسَةِ نَفْسِيًّا. ٤- استخدامُ مُنْجَزَاتِ التَّحليل<br>المقطع النَّفْسِي في قراءتِهِ لِلنَّصِ الأدبي كما ورد في النَّص الأدبي.

=== BLOCK 16: Solved Exercises 11 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b33151
[QUESTION_NUMBER]: س١٠
[QUESTION_TEXT]: الام يرتكز المنهج الابتكار، ويجعله أسير تِلْكَ المَنْجَزَاتِ فِي دِرَاسَةِ لِلنَّص.َ - دِرَاسَةِ المحتوى عِلْمِ النَّفْس.ِ - ٢ دِرَاسَةِ الْمُحْتَوى الظَّاهِرِ الخامس
[ANSWER_TEXT]: يرتكرُ المَنْهَجُ النَّفْسِي إلى: -١ اعتماد معطياتِ الكامن تأويل الظَّاهِرَةِ(.<br>- -<br>)٤٩٩١-٨٠٩١م(

--- END STREAM ---
