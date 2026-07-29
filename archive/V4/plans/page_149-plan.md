# **SESSION 149**

[TASK DEFINITION]
Objective: Implement page 149.
File: `pages/page_149.html`
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
[LESSON_NUMBER]: 149
[CHAPTER_TITLE]: page 149
[CATEGORY_HEADER]: 149
[SECTION_HEADER]: 149
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Cut Box Start (Part 2) ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[UNIQUE_ID]: b64104
[BLOCK_TITLE]: الإجابة
[CONTENT]: الشَّعْرُ مِرَاةٌ تَعْكس مخزونات العقل الباطني للشاعر، فالشّعْرُ مَجْلَّى يُنْشَرُ فِيهِ ما انطوى في نفسية الشاعر من مكنونات اخترتها
اللاشُعُور،ُ وَيَتَمَثَلُ هذا عند الشاعر نديم محمد الذي يَكْشِفُ عَمَّا تواري في خزائن اللاشُعُور. فعلى مستوى معاني النَّصَ نَجِدُ أَنَّ
الشَّاعِرَ يَبْدأ المَقْطَعَ الأَوَّلَ بِنداءِ شُعُوره، وَنَعْتِهِ بِالحَيَّةِ التِي تَنْفُتُ السَّمَّ فِي قَلْبِهِ بِغَزارة وكثافة، وكأنها امتلكت ألف نابِ يَضُحُ السُّمَّ
ويدسه في قلبه. ثم لا يلبث أن يجعله السبب في تفاهم مرضه واستفحالِه،ِ فيؤكد أن شعوره قد جعل حزنه يبلغ الدروة، وجعل عذابه
يمتد ويطُولُ وَيَبْدَةُ المَقْطَعَ الثاني بالتأكيد على أنَّ الدَّهْر قد تغلب عليه لأَنَّهُ عَالَبَهُ باهوى، فَلَو غالبه بغيره لانتصر عليه انتصارا ساحقًا
ولنَصَبَ قِبَابَهُ بِينَ الشُّهب في أعالي السماء. ولَطَوَّفَ فيها لاهِيَا يَرْفل برداء الانتصار، ويلاعِبُ وجنةَ البَدْر. وعلى مستوى استجلاء
الظَّاهِرَةِ النَّفْسِيَّةِ نَجِدُ أَنَّ المعاني السابقة قد كَشَفَتْ مُعاناةً نَفْسِيَّةً عَمِيقَةً مَصْدَرُها حُبُّ مُخْفِق،ْ وآمالٌ مُنْكَسِرَة.ً ونَجِدُ الشَّاعِر،َ على
مستوى تأويل الظَّاهِرَة،ِ يَنْدَفِعُ إلى التسامي النَّفْسِيِّ بِالتَّخَاذِهِ الفَنَّ الْمُبْدِعَ وسيلةً لِلتَعْبيرِ عَنْ مَكْنُونَاتِهِ الْمُكْبُونَةِ فِي اللَّاشُعُور،ِ وَقَدِ الْخَذَ
اللاشُعُورُ لَدَى الشَّاعِرِ أشكالا فَنِّيَّةً لِلكَشْفِ عَنْ نَفْسِهِ مَعَ بَقَائِهِ مُتواريًا، تمثلت بما يأتي:

=== BLOCK 3: Structured List for Forms ===
(Component: TEMPLATE_C_LIST.html)
[UNIQUE_ID]: b76224
[LIST_ITEM_CONTENT]: - الألفاظ الموحِيَةُ بمعانٍ جَدِيدَةِ أَخْرَجَهَا السياقُ عَنْ معانيها المُعْجَمِيَّةِ وَالحِسَيَّةِ إِلَى مَعَانِ مُتَّشِحَةٍ بِ لَالِ اللَّاشُعُورِ وَأَطْيَافِهِ وَقَدْ
شَكَّلَتْ هَذِهِ الْأَلْفَاظُ فِي النَّصَ مُعْجَمَيْنِ لُغَوِينِ : )المعاناة( و)السَّعَادَةِ(. وانْدَرَجَتْ تَحْتَ مُعْجَم المعاناة الألفاظ الآتية: )علتي، حزبي
عذابي، السم(، على حين اندرَجَتْ نَحْتَ مُعْجَمِ السَّعَادَةِ الأَلفاظ الآتية: )النجوم، هوي، دعابي(. والمعجمان السَّابِقَانَ يَكْشِفَانِ
فَالْمُعْجَمُ محاولات اللاشْعُورِ فِي التَّعْبِيرِ عَنْ نَفْسِه،ِ وميله إلى إشباع حاجاتهِ مِنْ خلال إنكار المعاناةِ وَالبُعْدِ عَنْهَا، وَبُلُوعِهِ لَدَّةَ السَّعَادَةِ
إلى آفاق جديدة عبر الارتفاع والتَّسَامِي الدَّائِمَيْن.ِ الثاني )السَّعَادَةِ يَسْعَى إلى طَمْسِ الْمُعْجَمِ الأَوَّلِ )المعاناة(، والقَفْزِ فوقه
[LIST_ITEM_CONTENT]: - الرَّمْرُ : أَمَّا الشَّكُلُ الآخَرُ الذي الخَذَهُ اللَّاشُعُورُ عِنْدَ الشَّاعِرِ فِي التعبيرِ عَنْ
مَكْنُونَاتِهِ فهو الرُّمُوزُ الدالة على حالاتٍ نَفْسِيَّةِ كَامِنَةِ إلى السعادة التي في أعماقِ اللَّاشُعُورِ إِذْ رَمز بالحية إلى الألم والعذاب اللذين يعاني منهما بِسَبَبِ مَشَاعِرِ الْحُبّ الْمُخْفِق.ِ ورَمَرَ بِالنُّجُوم
يَرْغَبُ بِبُلُوعِهَا .
[LIST_ITEM_CONTENT]: - الصور : أَدَّتِ الصور وظيفةً فِي التَّعْبِيرِ عَنْ مَكْنُونَاتِ اللَّاشُعُور؛ إِذْ تَجَرَّدَتْ مِنْ حِسَيتها، واصطبعت بما أضفاهُ اللَّاشُعُورُ عليها،
ومعاناة، فَكَانَتْ خَيْرَ مُعَ رِ عَنْ مُعَانَاةَ الشَّاعِرِ الْمُكْبُونَةِ صُورَةُ )يا شُعُوري، يَا حَيَّة التي اصطَبَغَتْ بما أَضْفَاهُ اللاشُعُورُ عليها من آلام بها ساحة الوعي ورقابته الصَّارِمَةَ وَمِنْ تِلْكَ الصُّورِ حَتَّى بَاتَتْ خَيْرَ مُعَبَرِ عَنْ الْأَفكارِ اللَّاشْعُورِيَّةِ التي يُحَوَهَا اللَّاشْعُورُ إِلَى صُورٍ يَقْتَحِمُ
عليها من آلام وأحلام، لتجاوز خَيْبَةَ الْأَمَلِ فِي أَعْمَاقِه.ِ وصورة بطاولني الدهر بغير الهوى التي اصطبعت بما أَضْفَاهُ اللَّاشُعُورُ
والانكسار أَمَامَ دَهْرِ عَالَبَ الشَّاعِر،َ فَكَانَتْ خَيْرَ مُعَبِّرِ عَمَّا كَانَ مَكْبُونَا فِي أَعْمَاقِه.ِ

=== BLOCK 4: Warning Box for Summary ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[UNIQUE_ID]: b25551
[TITLE]:
[CONTENT]: ومِمَا سَبَقَ نَرَى أَنَّ النَّصَنَّ الأَدَبِيَّ في التحليل السابق، كَشَفَ عَنْ سَعْي اللَّاشُعُورِ إِلى التعبيرِ عَنْ نَفْسِهِ بِوَسَائِلَ فَنِيَّةٍ مُتَنَوَعَة،ٍ
شَكَّلَتْ اليَّاتٍ نَفْسِيَّة تجاوزَتْ رقابَةَ الشَّعُور،ِ وَسَعَتْ عبرَ النَّصَ إلى البوح بمكنُونَاتِ اللَّاشُعُورِ الَّذِي جَعَلَ النَّصَ - برأي الأَنْجَاهِ
النَّفْسِي - تمثيلًا رَمْزِيَّا لِمُعْطياتِ اللَّاشُعُورِ الْمَكْبُونَة.ِ

=== BLOCK 5: Block Definition for Practice ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b66644
[BLOCK_TITLE]: التطبيقات اللغوية:
[CONTENT]: أعرب ما وُضِعَ تَحْتَهُ خط في البيت الآتي:

=== BLOCK 6: Poem ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b13669
[POEM_TITLE]:
[UNIQUE_ID_BIO]: b49920
[POET_NAME]:
[RIGHT_HEMISTICH]: يا شُعُورِي يَا حَيَّةً تَنْفُتُ السُّمْ
[LEFT_HEMISTICH]: مَ فَيَجْرِي فِي القَلْبِ مِنْ أَلْفِ نَابِ

=== BLOCK 7: Solved Exam - Irab ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b20453
[QUESTION_NUMBER]: ج -۱
[QUESTION_TEXT]:
[ANSWER_TEXT]:
يا شُعُورِي: يا، أداة نداء. شعوري: منادى مضافُ مَنْصُوب، وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ المُقَدَّرَةُ على ما قَبْلِ يَاءِ الْمُتَكَلِّمِ مَنَعَ
ظهورها اشتغالُ المَحَلِ بِالحَرَكَةِ المناسِبَة،ِ والياء، صَمِيرٌ مُتَصِلِّ مَبْنِي على السكون فِي مَحَلِّ جَة،ٍ مُضَافُ إِلَيْه.ِ
- يا حَيَّة : ادىنمناد نَكِرَةٌ غَيْرُ مَقْصُودَة،ِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَة.ُ

=== BLOCK 8: Structured List for Further Practice ===
(Component: TEMPLATE_C_LIST.html)
[UNIQUE_ID]: b70206
[LIST_ITEM_CONTENT]: - اقرأ البيت الآتي، ثُمَّ نَفْدِ النَّشاط :

=== BLOCK 9: Poem ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b45919
[POEM_TITLE]:
[UNIQUE_ID_BIO]: b05588
[POET_NAME]:
[RIGHT_HEMISTICH]: وَلَطَوَّفُتُ بِالنَّعِيمٍ فَرَشَّتْ
[LEFT_HEMISTICH]: نِي حِسَانُ النَّعِيمِ بِالْأَطياب

=== BLOCK 10: Solved Exam - Ta'ajub ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b78509
[QUESTION_NUMBER]: -
[QUESTION_TEXT]: تَعَجَّبْ مِنَ الفِعْلِ )طَوَ تُ بِالنَّعِيم الوارد في البَيْتِ السَّابِقِ بَصِيفَتَيَ التَّعجب القياسيتين.
[ANSWER_TEXT]:
ج - ما أجمل أنْ أُطَوّفَ بِالنَّعِيم - أجمل بأنْ أَطَوَفَ بِالنَّعِيم ! - ما أجمل تطويفي بالنعيم !
- أَجْمِل بتطويفي بالنعيم!

=== BLOCK 11: Exam Cut part 1 ===
(Component: TEMPLATE_CUT_EXAM_SOLVED_PART_1.html)
[UNIQUE_ID]: b67847
[QUESTION_NUMBER]: -
[QUESTION_TEXT]: اذْكُرِ الوَزْنَ الصَّرْفِي للأسماء والأفعال الواردة في البيت الآتي:
[ANSWER_TEXT]:

=== BLOCK 12: Poem Cut box ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
[UNIQUE_ID]: b69755
[BLOCK_TITLE]:
[CONTENT]:
لو بِغَير الهوى يُطَاوِلُنِي الدَّهْ
ر لأَرْكَرْتُ فِي النُّجُومِ قبابي

--- END STREAM ---
