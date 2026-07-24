# **SESSION 107**

[TASK DEFINITION]
Objective: Implement page 107.
File: `pages/page_107.html`
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
[LESSON_NUMBER]: 107
[CHAPTER_TITLE]: page 107
[CATEGORY_HEADER]: 107
[SECTION_HEADER]: 107
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: الاستيعاب والفهم ===
(Component: TEMPLATE_CUT_BOX_PART_2.html wrapping TEMPLATE_C_BLOCK.html)
Title: الاستيعاب والفهم
Paragraph 1: وما كانت هذه النورات لتقوم لولا إدراك أبناء سورية أن المقاومة وحدها الكفيلة بتحقيق الأهداف العظيمة، وإلحاق الهزيمة بالقوى الاستعمارية، وأنَّ الإرادة قادرة على الوقوف أمام الآلات العسكرية المتطورة الفاتكة، فخاضوا ملحمة بطولية تضاءل أمامها جبروت المستعمر الفرنسي، وفهرت جحافل الجيوش المدججة بالعتاد التي حشدها.
Paragraph 2: وأمام انعدام التكافؤ والتوازن بالنظر إلى العتاد العسكري، كان لابد من وجود معادل يعيد التوازن إلى ميادين الوغى وساحات النضال. وقد تمثل هذا المعادل بالتصميم على انتزاع النصر من برائن المعتدين وتحقيق الاستقلال بالإرادة القوية والإيمان بحق الدفاع عن الأرض. وتمثل كذلك بالوحدة الوطنية لشعبنا العربي السوري، فقد كان صدق الانتماء الوطني سلاحا فعالا في مقاومة المحتلين.
Paragraph 3: ومن جهة أخرى ليس بمقدور المرء أن ينسى تلك الدماء الزكية التي جاد بها أبناء سوريا بسخاء وعطروا بها ثرى الوطن الحبيب؛ فقد كان لها الدور الحاسم في ترجيح كفّة الحق على كفّة الباطل. إذ مكنت هذه التضحيات الشعب السوري بإمكاناته المتواضعة وإرادته القوية من أن يلوي ذراع المستعمر الدخيل ويجبره على الرحيل عن أرضنا.
Paragraph 4: وإذا بفضل هذه اللحمة الوطنية، والإصرار على تحدي المستعمر، والاستعداد لبذل التضحيات الحِسَامِ تَحَقَّق الاستقلال واندحر المستعمر الفرنسي، وفهرت جيوشه الغازية، وبقيت أرضنا حُرَّةً عصية على الباغين، وبقي شعبنا يشيد الروح العالية متخطيا العوائق التي أراد لها المستعمر أن تُعرقل تقدم الوطن، وتوقف ازدهاره وثماءه.

=== BLOCK 3: التطبيقات اللغوية ===
(Component: TEMPLATE_C_BLOCK.html with TEMPLATE_C_LIST.html inside)
Title: التطبيقات اللغوية
Classes: `.block-header accent`
List Item 1:
- - ادْرُسَ مَبْحَثَ الحَالِ مُسْتَفِيدًا مِنَ الحَالِ الواردة في البيت الآتي:
وارْمى كير الليالي دُوهَا لَيْنَ النَّابِ كَلِيلَ الْمِخْلَبِ
- (.text-accent) ج -۱ لين حال منصوبة، وعلامة نصبها الفتحة الظاهرة - كليل: حال منصوبة، وعلامة نصبها الفتحة الظاهرة.
List Item 2:
- - اجعل كلمة )الشهادة( اسما مخصوصا بالمدح مستوفيًا أنواع الفاعل.
- (.text-accent) ج -٢ نِعْمَ الْمَطْلَبُ الشَّهَادَة.ُ نِعْمَ مَطْلَبُ الإِنْسَانِ الشَّهَادَةُ - نِعْمَ مَطْلَبًا الشَّهَادَةُ - حَبَّذَا الشَّهَادَة.ُ
List Item 3:
- ادْرُسَ مَبْحَثَ النِّدَاءِ مُسْتَيْدًا مِمَّا وَرَدَ فِي النَّصَي،ِّ وَمِنَ الحَالَةِ الوَارِدَةِ فِي البَيْتِ الأول.
- (.text-accent) ج- يا عروس المجد، عروس : منادى مُضافُ مَنْصُوب،ُ وعلامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَة.ُ
List Item 4:
- اذْكُرِ القَاعِدَةَ الصَّرِفِيَّةَ لِصَوْع اسم المُكَانِ مَغْنَى(، ومثل لها بأمثَلَةٍ مُنَاسِبَةٍ مِنْ عِنْدَك.َ
- (.text-accent) ج - صيغ اسم المكان )مَغْنَى( مِنْ فعل ثلاثي مُعْتَلِ الآخر على وَزْنِ مَفْعَل( . عَلَى مَغْنَنى - مثل ذلك : رَمَى مَرْمَى، مَتَى تَمْشَى...
List Item 5:
- ه- كُتِبَتِ الأَلِفُ اللَّيِّنَةُ على صورتها في الفِعْلَين: )أَتَى - قادی(. اشرح القاعدة الإملائِيَّةَ لِكِتَابَةِ كُلِّ مِنْهُما.
- (.text-accent) جه - أتى كتبت الألف مقصورة؛ لأن أصلها ياء. - هادى كتبت الألف مقصورة؛ لأنها جاءت خامسة في فعل، ولم تسبق بياء.
أو : كتبت الألف مقصورة؛ لأنهما جاءت فوق الثالثة في فعل، ولم تسبق بياء.
List Item 6:
- - هَاتِ الْمَصْدَرَ مِنَ الْفِعْل )انتَشَتْ( واشْرَحْ قَاعِدَتَيَ الهَمْرَةِ الأَوَّلِيَّةِ والمُتَطَرِّفَةِ فِي هذا الْمَصْدَر.ِ
- (.text-accent) - الْمَصْدَرُ : انتشاء - انتشاء: هَمْرَةُ وَصْلِ جَاءَتْ فِي مَصْدَرٍ هُمَاسِي. - انتشاء: هَمْرَةً مُتَطَرَفَة،ٌ سُبِقَتْ بِسَاكِن.ِ

=== BLOCK 4: تحليل مفصل المضمون الأبيات ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تحليل مفصل المضمون الأبيات

(Sub-component: TEMPLATE_C_POEM.html)
Verse 1:
يا عروس المجد تيهي واسحبي
في مغانِينَا ذُيُولَ النُّهُب

(Sub-component: TEMPLATE_C_TABLE.html)
Row 1:
Col 1: المفردات
Col 2: تيهي تكبري سيري بكبرياء(. مغانينا منازلنا المفرد مغنى الشهب المفرد شهاب نجم مضيء لامع، أو جرم سماوي يسبح في الفضاء
Row 2:
Col 1: الشرح
Col 2: أيتها الحرية سيري بزهو وفخار فوق ثرى بلادنا، واختالي كما تختال العروس، وجرّري خلفك أذيال الشهب الساطعة، وزيني بها أرجاء بلادنا
Row 3:
Col 1: الفكرة
Col 2: التَّعْبِيرِ عَنْ مَشَاعِرِ الفَرَحِ وَالزَّهو بِتَحْقِيقِ الجلاء الفرح بجلاء المستَعْمر الغربي(.
Row 4:
Col 1: الشعور
Col 2: الفرح الأداة: التراكيب المثال: يا عروس المجد تيهي.
Row 5:
Col 1: البلاغة
Col 2: )اسحي الشهب(: تَصْرِيع )يا عَرُوس(: استعارَةً تَصْرِعِيَّة. )شبه الحرية بالعروس(.
Row 6:
Col 1: الأساليب
Col 2: )تيهي(، )اسْحَبِي فِي مَعَانِينَا ذُيُولَ الشَّهْبِ(: أسلوب أمر. صِيغَتُهُ فِعْلُ أَمْر.

=== BLOCK 5: الإعراب ===
(Component: TEMPLATE_CUT_BOX_PART_1.html wrapping TEMPLATE_C_IRAB.html)
Title: الإعراب
[Word]: يا عروس
[Details]: يا، حَرْفُ نِدَاءٍ عَرُوس،َ مُنَادَى مُضَافُ مَنْصُوبُ

[Word]: الْمَجْدِ الشَّهْبِ
[Details]: مُضَافُ إِلَيهِ مَجْرُورٌ

[Word]: تيهي
[Details]: فِعْلُ أَمْرِ مَبْنِيَّ عَلَى حَذْفِ
التون؛ لأن مُصَارِعَهُ مِنَ الْأَفْعَالِ الخَمْسَة.ِ والياء، ضمير متصل مَبْنِي على السُّكونِ فِي مَحَلِّ رَفْع،ٍ فاعل

[Word]: واسحبي
[Details]: الواو، حَرْفُ عَطْفُ اسْحَي،
فِعْلَ أَمْرِ مَبْنِي عَلَى خَذْفِ النُونِ لِإِنَّ مُصَارِعَهُ مِنَ الأَفْعَالِ الخَمْسَة.ِ والياء، ضميرٌ مُتَصِلَ مَبْنِي على السُّكُونِ فِي مَحَلِّ رَفْه،ِ فَاعِلٌ

[Word]: ذُيُولَ
[Details]: مَفْعُولُ

--- END STREAM ---
