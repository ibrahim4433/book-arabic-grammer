# **SESSION 107**

[TASK DEFINITION]
Objective: Implement page 107.
File: `pages/page_107.html` (Note: Use the exact page number.)
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
[LESSON_NUMBER]: 107
[CHAPTER_TITLE]: page 107
[CATEGORY_HEADER]: 107
[SECTION_HEADER]: 107
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Continuation from previous page ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[BLOCK_TITLE]: الاستيعاب والفهم
[CONTENT]: وما كانت هذه الثورات لتقوم لولا إدراك أبناء سورية أن المقاومة وحدها الكفيلة بتحقيق الأهداف العظيمة، وإلحاق الهزيمة بالقوى الاستعمارية، وأنَّ الإرادة قادرة على الوقوف أمام الآلات العسكرية المتطورة الفاتكة، فخاضوا ملحمة بطولية تضاءل أمامها جبروت المستعمر الفرنسي، وقهرت جحافل الجيوش المدججة بالعتاد التي حشدها.
وأمام انعدام التكافؤ والتوازن بالنظر إلى العتاد العسكري، كان لابد من وجود معادل يعيد التوازن إلى ميادين الوغى وساحات النضال. وقد تمثل هذا المعادل بالتصميم على انتزاع النصر من براثن المعتدين وتحقيق الاستقلال بالإرادة القوية والإيمان بحق الدفاع عن الأرض. وتمثل كذلك بالوحدة الوطنية لشعبنا العربي السوري، فقد كان صدق الانتماء الوطني سلاحا فعالا في مقاومة المحتلين.
ومن جهة أخرى ليس بمقدور المرء أن ينسى تلك الدماء الزكية التي جاد بها أبناء سوريا بسخاء وعطروا بها ثرى الوطن الحبيب؛ فقد كان لها الدور الحاسم في ترجيح كفّة الحق على كفّة الباطل. إذ مكنت هذه التضحيات الشعب السوري بإمكاناته المتواضعة وإرادته القوية من أن يلوي ذراع المستعمر الدخيل ويجبره على الرحيل عن أرضنا.
وإذا بفضل هذه اللحمة الوطنية، والإصرار على تحدي المستعمر، والاستعداد لبذل التضحيات الجسام تحقَّق الاستقلال واندحر المستعمر الفرنسي، وقهرت جيوشه الغازية، وبقيت أرضنا حُرَّةً عصية على الباغين، وبقي شعبنا يشيد الروح العالية متخطيا العوائق التي أراد لها المستعمر أن تُعرقل تقدم الوطن، وتوقف ازدهاره ونماءه.

=== BLOCK 3: Applications Header ===
(Component: TEMPLATE_C_BLOCK.html)
Title: التطبيقات اللغوية
Content: <span class="text-accent">تدريبات على النص</span>

=== BLOCK 4: Application 1 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[QUESTION_NUMBER]: ١-
[QUESTION_TEXT]: ادْرُسَ مَبْحَثَ الحَالِ مُسْتَفِيدًا مِنَ الحَالِ الواردة في البيت الآتي:
وارْمى كير الليالي دُوهَا لَيْنَ النَّابِ كَلِيلَ الْمِخْلَبِ
[ANSWER_TEXT]: ج -۱ لين حال منصوبة، وعلامة نصبها الفتحة الظاهرة - كليل: حال منصوبة، وعلامة نصبها الفتحة الظاهرة.

=== BLOCK 5: Application 2 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[QUESTION_NUMBER]: ٢-
[QUESTION_TEXT]: اجعل كلمة (الشهادة) اسما مخصوصا بالمدح مستوفيًا أنواع الفاعل.
[ANSWER_TEXT]: ج -٢ نِعْمَ الْمَطْلَبُ الشَّهَادَة.ُ نِعْمَ مَطْلَبُ الإِنْسَانِ الشَّهَادَةُ - نِعْمَ مَطْلَبًا الشَّهَادَةُ - حَبَّذَا الشَّهَادَة.ُ

=== BLOCK 6: Application 3 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[QUESTION_NUMBER]: ٣-
[QUESTION_TEXT]: ادْرُسَ مَبْحَثَ النِّدَاءِ مُسْتَيْدًا مِمَّا وَرَدَ فِي النَّصَي،ِّ وَمِنَ الحَالَةِ الوَارِدَةِ فِي البَيْتِ الأول.
[ANSWER_TEXT]: ج- يا عروس المجد، عروس : منادى مُضافُ مَنْصُوب،ُ وعلامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَة.ُ

=== BLOCK 7: Application 4 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[QUESTION_NUMBER]: ٤-
[QUESTION_TEXT]: اذْكُرِ القَاعِدَةَ الصَّرِفِيَّةَ لِصَوْع اسم المُكَانِ (مَغْنَى)، ومثل لها بأمثَلَةٍ مُنَاسِبَةٍ مِنْ عِنْدَك.َ
[ANSWER_TEXT]: ج - صيغ اسم المكان (مَغْنَى) مِنْ فعل ثلاثي مُعْتَلِ الآخر على وَزْنِ (مَفْعَل) . عَلَى مَغْنَنى - مثل ذلك : رَمَى مَرْمَى، مَتَى تَمْشَى...

=== BLOCK 8: Application 5 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[QUESTION_NUMBER]: ٥-
[QUESTION_TEXT]: كُتِبَتِ الأَلِفُ اللَّيِّنَةُ على صورتها في الفِعْلَين: (أَتَى - هادى). اشرح القاعدة الإملائِيَّةَ لِكِتَابَةِ كُلِّ مِنْهُما.
[ANSWER_TEXT]: جه - أتى كتبت الألف مقصورة؛ لأن أصلها ياء. - هادى كتبت الألف مقصورة؛ لأنها جاءت خامسة في فعل، ولم تسبق بياء. أو : كتبت الألف مقصورة؛ لأنهما جاءت فوق الثالثة في فعل، ولم تسبق بياء.

=== BLOCK 9: Application 6 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[QUESTION_NUMBER]: ٦-
[QUESTION_TEXT]: هَاتِ الْمَصْدَرَ مِنَ الْفِعْل (انتَشَتْ) واشْرَحْ قَاعِدَتَيَ الهَمْرَةِ الأَوَّلِيَّةِ والمُتَطَرِّفَةِ فِي هذا الْمَصْدَر.ِ
[ANSWER_TEXT]: - الْمَصْدَرُ : انتشاء - انتشاء: هَمْرَةُ وَصْلِ جَاءَتْ فِي مَصْدَرٍ هُمَاسِي. - انتشاء: هَمْرَةً مُتَطَرَفَة،ٌ سُبِقَتْ بِسَاكِن.ِ

=== BLOCK 10: Poem Text ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: تحليل مفصل المضمون الأبيات:
[POET_NAME]:
[RIGHT_HEMISTICH]: يا عروس المجد تيهي واسحبي
[LEFT_HEMISTICH]: في مغانِينَا ذُيُولَ النُّهُب

=== BLOCK 11: Core Matrix Analysis ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: المفردات
[HEADER_2]: الشرح
[HEADER_3]: الأداة
[CELL_1]: تيهي تكبري (سيري بكبرياء). مغانينا منازلنا المفرد مغنى الشهب المفرد شهاب نجم مضيء لامع، أو جرم سماوي يسبح في الفضاء
[CELL_2]: أيتها الحرية سيري بزهو وفخار فوق ثرى بلادنا، واختالي كما تختال العروس، وجرّري خلفك أذيال الشهب الساطعة، وزيني بها أرجاء بلادنا
[CELL_3]: التراكيب المثال: يا عروس المجد تيهي.

=== BLOCK 12: Core Matrix Analysis 2 ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: البلاغة
[HEADER_2]: الأساليب
[HEADER_3]: الشعور
[CELL_1]: (اسحبي الشهب): تَصْرِيع (يا عَرُوس): استعارَةً تَصْرِعِيَّة. (شبه الحرية بالعروس).
[CELL_2]: (تيهي)، (اسْحَبِي فِي مَعَانِينَا ذُيُولَ الشَّهْبِ): أسلوب أمر. صِيغَتُهُ فِعْلُ أَمْر.
[CELL_3]: الفرح

=== BLOCK 13: Warning Benefit ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[CONTENT]: الفكرة : التَّعْبِيرِ عَنْ مَشَاعِرِ الفَرَحِ وَالزَّهو بِتَحْقِيقِ الجلاء (الفرح بجلاء المستَعْمر الغربي).

=== BLOCK 14: Cut Content End ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
[BLOCK_TITLE]: الإعراب
[CONTENT]: يا عروس: يا، حَرْفُ نِدَاءٍ عَرُوس،َ مُنَادَى مُضَافُ مَنْصُوبُ الْمَجْدِ الشَّهْبِ : مُضَافُ إِلَيهِ مَجْرُورٌ تيهي: فِعْلُ أَمْرِ مَبْنِيَّ عَلَى حَذْفِ التون؛ لأن مُصَارِعَهُ مِنَ الْأَفْعَالِ الخَمْسَة.ِ والياء، ضمير متصل مَبْنِي على السُّكونِ فِي مَحَلِّ رَفْع،ٍ فاعل واسحبي الواو، حَرْفُ عَطْفُ اسْحَي، فِعْلَ أَمْرِ مَبْنِي عَلَى خَذْفِ النُونِ لِإِنَّ مُصَارِعَهُ مِنَ الأَفْعَالِ الخَمْسَة.ِ والياء، ضميرٌ مُتَصِلَ مَبْنِي على السُّكُونِ فِي مَحَلِّ رَفْه،ِ فَاعِلٌ ذُيُول:َ مَفْعُولُ

--- END STREAM ---
