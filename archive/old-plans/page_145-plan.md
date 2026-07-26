# **SESSION 145**

[TASK DEFINITION]
Objective: Implement page 145.
File: `pages/page_145.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools. If it overflows, it is a catastrophic failure. Do NOT try to solve overflow by deleting text (Strict Typographer Rule). Solve it by choosing denser templates or omitting optional white-space.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`. Ensure exact visual continuity.
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md` to identify the correct template to use for the continuation. You are forbidden from guessing. Scan the raw text for the preceding keyword to determine the active template and apply the correct `_PART_2.html` wrapping.
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
[LESSON_NUMBER]: 145
[CHAPTER_TITLE]: page 145
[CATEGORY_HEADER]: 145
[SECTION_HEADER]: 145
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Cut Content Continuation ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
(Component: TEMPLATE_C_BLOCK.html)
Title: المحتوى الجديد للأدب
Content: <span class="text-accent">وسيلة فتيةً واحِدَةً مِنَ الوسائِلِ التِي جَسَدَتْ العلاقة بين هذا الأدب والمجتمع، ثُمَّ ادرس يُقِلُ النَّص السَّابق الأدب الاجتماعي. وضح المحتوى الجديد للأدب.</span>

=== BLOCK 3: Poem Evidence ===
(Component: TEMPLATE_C_POEM.html)
Title: شواهد شعرية
Poet: - قَالَ الشَّاعِرُ حافظ إبراهيم:
Hemistich 1: اللَّهِ دَرُّهُمُ فَكَمْ مِنْ بانس
Hemistich 2: جَمِ الوَجِيْعَةِ سَيِّيَ الْأَحْوَالِ
Hemistich 3: ترْمِي بِهِ الدُّنْيَا فَمِنْ جُوْعِ إِلى
Hemistich 4: عري إلى سقم إلى إقلال
Hemistich 5: عَيْنٌ مُسَهَّدَةٌ وَقَلْبٌ وَاحِفْ
Hemistich 6: نفس مُرَوَّعَةً وَجَيْبٌ خالي

=== BLOCK 4: Analysis Block ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المنهج الاجتماعي في النقد الأدبي: إجابات الأسئلة التطبيقية التي تدور حول الأبيات
Content: دلالتها الاجتماعية. حَدّدُ مِنَ الأبيات السابقة صورة ثُمَّ وَصَحْ المجسدة للمحتوى الجديد للأدب. تُعَدُّ الصُّورة المعبرة إحدى الوسائل الفنية ظاهرة الفقر والعوز. الاجتماعية التي تدور حولها البَلَاء،ُ شَجْوي، جياعًا(. - الظاهرة ج ۱- المُعْجَمُ اللغويُّ لِلمُعاناة: )الأَحْرَانُ فَنَّا طليعيًا. الْمُجْتَمَعِ مَا تَهُ ثُمَّ يُعِيدُها إليهِ علاقة تبادلية فالشاعر يأخُذُ مِنَ ج - العلاقةُ بَينَ الأدب والمجتمع العلاقة بين الأدب والمجتمع - الوسيلة الفنية التي جَسَدَتْ المحتوى الجديد للأدب وَحْدَةِ الشَّكْلِ وَالْمَضَمُونِ؛ وحدة الشكل والمضمون، فقد حرص الشاعر على وَسْمُوه.ِ وَيَنْبَغِي أَنْ يكونَ مَفْهُومًا، كما حافظ على رُقِيَ الشَّكْلِ الْفَنِّي إِذْ كَانَ الْمَضْمُونُ واضحا ، انطلاقا مِنْ أَنَّ الأَدَبَ يَتَوَجُهُ إِلَى جُمْهُور،ٍ المعنى بما أوحَتْ بِهِ مِنَ الْمَشَفَّةِ وَالْمَعاناة - تحديد الصورة : )ترمي بِهِ الدنيا(. - دلالتها الاجتماعية : خدمت هذه الصورة مُعَانَاةِ الْفَقِيْر.ِ والحاجة، وما أثارته من مشاعر الألم والحزن، مُعَبَرَةً بذلك عَنْ مَظَاهِرِ المنهج النفسي في النقد الأدبي الاستيعاب والفهم والتحليل: المؤلفون

=== BLOCK 5: Core Matrix (Q&A) ===
(Component: TEMPLATE_C_TABLE.html)
Title: أسئلة وإجابات في المنهج النفسي
Headers: السؤال | الإجابة
Row 1: س - علام يعتمدُ المَنْهَجُ النَّفْسِيُّ فِي التَّقْدِ؟ والامَ يسعى؟ | ج -۱ يَعْتَمِدُ مُعْطَيَاتِ عِلْمِ النَّفْسِ فِي دِرَاسَةِ النَّ الأَدَي، وفي مَعْرِفَةِ العالم النَّفْسِي أَهداف، منها: محاولة اكتشاف ثُمَّ فِي مَعْرِفَةِ ذَلِكَ العالم. والمَنْهَج النَّفْسِي في النَّقْدِ الأَدَبَيِّ لِمُبْدِعِهِ ثُمَّ فِي مَعْرِفَةِ النَّ نَفْسِه،ِ أو فِي مَعْرِفَةِ النَّصِ تَجْعَلُ مِنْهُ مُبْدِعًا، واكتشافِ عَمَلِيَّةِ الإِبداع نَفْسِهَا، الخصائص النَّفْسِيَّةِ الْمُمَيِّرَةِ لِمُبْدِعِ النَّصِ مِنْ سِواهُ مِنَ النَّاسِ العادين؛ أي الخصائص التي
Row 2: س٢ - ما الحقُولُ التي يتحرك فيها المنهج النَّفْسِيُّ؟ | ج٢ - يَتَحَرَّلُ الْمَنْهَجُ بِينَ ثلاثةِ حُقُول: عِلْمٍ واكتشاف الآثارِ النَّفْسِيَّةِ لِنَّصَ في القراء. ذَاتَا مِنَ العَمَلِيَّاتِ النَّفْسِيَّة،ِ وَالْمُبَدِعِ بِوَصْفِهِ والإشارات والصور التي تحيل بدورها على مجموعَةٍ النَّفْس،ِ والنَّصَ الأدبي بِوَصْفِهِ مجموعَةَ مِنَ الرُّمُوز
Row 3: س٣- ما الَّذِي يَكْتَشِفُهُ النَّاقِدُ مِنْ دِرَاسِتِهِ النَّ الأَدَبِيَّ وَفْقَ الْمَنْهَجِ النَّفْسِي؟ | تمتلك مِنَ الخصائص النَّفْسِيَّةِ مَا يُيَزُهَا مِنَ النَّاسِ العادِينَ وَحَصَائِصِهِ النَّفْسِيَّة.ِ تفسير دوافعه إلى الكِتَابَةِ مَعْرِفَةِ شَخْصِيَّةِ الْمُبْدِع، وَمِنْ مُحاولة النَّفْسِي مَكِّنُ النَّاقِدَ مِنْ - دراسةُ النَّص الأَدَى وَفْقَ الْمَنْهَجِ
Row 4: س٤ - يُعَدُ النَّصُّ الأَدَبِيُّ وثيقة دالةً على نَفْسِيَّةِ مُبْدِعِه.ِ ما المرتكزات التي يَجِبُ تَتَبُّعُهَا لِمَعْرِفَةِ شَخْصِيَّةِ الْمَ دِعِ؟ | ج - النَّ الْأَدَبِيُّ فِي الْمَنْهَحِ النَّفْسِي يُتِلُ وَثِيقَةً دالَّةَ على نَفْسِيَّةِ مُبْدِعِه،ِ إِذْ يَتَصَمَّنُ فِي داخِلِهِ رُمُوزًا وإشارات وصورًا وأفكارا.
Row 5: سه - يرى فرويد أنَّ الأَدَبَ وَالْفَنَّ تَعْبِيرٌ عَنِ اللا وعي الفَرْدِي. وضح ذلِكَ مِمَّا وَرَدَ فِي المقطع الثاني. | جه - لأنه يرى أنَّ العَمَلَ الأَدَبِيَّ الْمُكْبُونَةِ مَادَةً ثَرِيَّة بالإشارات الدالة على الرَّغَبَاتِ وَفَتِهِ
Row 6: س٦ - تباينتْ نَظْرَةُ )يونغ( لِتِلْكَ الرَّعْبَاتِ وَالمَخَاوِفِ التي تُجْهَرُ بِنَفْسِهَا فِي أَدَبِهِ لِمُبْدِعِه، وعلى مخاوفه أيضًا، فالاشُعُور،ُ عِنْدَه،ُ مُسْتَوَدَعْ معينة. - أدلر : يرى أن الباعث الأساسي أدلر( ليواعِثِ الإبداع. وَحْ نَطْرَةً كُلِّ مِنْهما. | ج٦ - يونغ: يرجع عملية الإبداع إلى حالة نفسية القدماء. عِنْدَ بَعْضِ التَّقَادِ العَرَبِ بُدُورُ الْمَنْهَحِ النَّفْسِيِّ أو في حُبّ ال هور .
Row 7: س٧- ظَهَرَتْ للإبداع التعويضُ عَنِ النَّقْصِ أو الرَّغْبَةِ في السيطرة مِنْ قَوْلِ عَنْ بِوَاعِتِ الشَّعْرِ ذَلِكَ : - ما تَضَمَّنَهُ كِتَابُ ابْنِ فَتَيْبَةِ الشَّعْرُ والشَّعراء وَضَحْ ذَلِكَ مِنْ فَهْمِكَ الْمُقْطَعَ الثَّالِث.َ | ج۷ - مِنْ بواكيرٍ كان التِي يَفْرِضُ الشَّعْرُ نَفْسَهُ فيها. - ما والغَضَب،ِ وَمِنْ قَوْلِ آخِرَ عَنِ الأوقات والأماكن ودوافعه، كاللَّمَع، والشَّوْق،ِ والشراب، والطَّرَب،ِ النَّصَيِّ فِيه.ِ
Row 8: س٨ - إلى العلاقةِ بَيْنَ نَفْسِيَّةِ الْمُتَلَقِي وأَثَرَ طبائع الشعراء. - إشارة ابن طباطبا القاضي الجرجان قد فَصَّلَ القَوْلَ فِيهِ عَنِ اختلاف نُوا فِي ضَوْءِ العُقْدَةِ مِنْهُما ؟ علام اعتمد العقاد ومُحَمَّدُ النويهي في تفسير شَخْصِيَّةِ أَبِي نُواسِ وإلامَ تَوَصَّلَ كُلِّ | ج٨- فَسَّرَ العقَادُ شَخْصِيَّةَ أَبِي الحِسْمَانِي فِي تَوتُرِ أَعْصَابِه،ِ وزواج دراستِهِ إِلى مجْمُوعَةٍ مِنَ ال تائج، مِنْ أَهَمَهَا دَوْرُ اضطرابه المَرَضِيَّةِ المعروفة بالنَّرْجِسِيَّة"، وانتهى التويهي، في النَّفْسِي.
Row 9: س٩ - ادْكُرْ بَعْضَ الآخِذ التي أُخِذَتْ على المنهج أُهِ مِنْ رَجُل آخر بِعْدَ وفاة أبيه. | ج۹ - مِنْ هذه المآخذ : - النظر إلى النَّصَ - ليسَ كُلُّ نَيِّ أَدَيَّ قَابلا قوانين، ومن الخطأ تطبيقها على الأدب. ٣ الأَدَتِي بِوَصْفِهِ وَثِيقَةَ نَفْسِيَّة. - مَقُولَاتُ عِلْمِ النَّفْسِ فَرُوضٌ وليست على جَاهِرَةِ الأَمْرُ الذي لا يُحَرِّضُ النَّاقِدَ النَّفْسِي في النَّقْدِ الأَدَبِي يَعْنِي وجُودَ مَعْرِفَةٍ للتحليل والدِّرَاسَةِ نَفْسِيًّا. ٤- استخدامُ مُنْجَزَاتِ التَّحليل

=== BLOCK 6: Benefit Warning (Orange color balance and Answer to Final Exam) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: تنبيه حول المنهج النفسي
Content: <span class="font-bold">إجابة سؤال الامتحان:</span> الخامس ج ۱- يرتكرُ المَنْهَجُ النَّفْسِي إلى: -١ اعتماد معطياتِ عِلْمِ النَّفْس.ِ - ٢ دِرَاسَةِ الْمُحْتَوى الظَّاهِرِ لِلنَّص.َ - دِرَاسَةِ المحتوى الكامن تأويل الظَّاهِرَةِ(. - - )٤٩٩١-٨٠٩١م(

=== BLOCK 7: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: س۰۱ - الام يرتكز المنهج الابتكار، ويجعله أسير تِلْكَ المَنْجَزَاتِ فِي دِرَاسَةِ المقطع النَّفْسِي في قراءتِهِ لِلنَّصِ الأدبي كما ورد في النَّص الأدبي.

--- END STREAM ---
