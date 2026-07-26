# **SESSION 142**

[TASK DEFINITION]
Objective: Implement page 142.
File: `pages/page_142.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
1.5 ANTI-HALLUCINATION & STRICT TYPOGRAPHER RULE (CRITICAL): Do NOT invent, hallucinate, or add new grammar rules, examples, or external text. ONLY use the exact text slices provided in the Raw Input Text. You MUST use 100% of the provided raw text. NO summarizing, NO deleting, NO adding new content. Every piece of text must map to an approved TEMPLATE.
1.6 THE TYPO EXCEPTION: You are explicitly permitted to correct obvious typos, spelling errors, or grammatical errors in the raw Arabic text during planning.
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
[LESSON_NUMBER]: 142
[CHAPTER_TITLE]: page 142
[CATEGORY_HEADER]: 142
[SECTION_HEADER]: 142
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Cut Content Part 2 ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[UNIQUE_ID]: b50275
[BLOCK_TITLE]: شرح المقاطع
[CONTENT]: فَرَاشَة،ٍ ولا بِجُزْنِ وَرْدَةِ إِنَّهُم لَا يَحْلُمُونَ أَحْلَامًا معاني المقطع الأول : الكادِحُونَ يَتَمَنُونَ الخَيْرَ لِجَمِيعِ الكائناتِ؛ فلا يَحْلُمُونَ بِمَوتِ صفحة الماء، تُكَلِلَّهُ أَشِعَةُ القَمَرِ الْفِضَيَّةِ فِي لَيْلَةِ أَنْسِ عَظِيمَةً كبيرة، فلا يَخْلُمُونَ بِقَضَاءِ أَوْقَاتٍ سَعِيدَة على ظهر قارب يَطْفُو على العَاشِقُون.َ صيفية، لا ولا يَخْلُمُونَ بِلَحَظَاتِ العِشق والغرام التي ينعم بِسَعَادَتِهَا الفَقْرِ والعَوَن،ِ وَمَعَ كُل ذلك يَكْدَحُونَ لِيَصْنَعُوا معانى المقطع الثاني: الكادِحُونَ يَتَجَرَّعُونَ مَرَارَةَ الْمُعَانَاةِ وَعَلْقَمَ الحرمان وعذابَ مُولَعِ مُعْرَم. مَنْ يَنْسِجُونَ مِنْدِيلَ العِشْقِ لِكَلِفٍ السَّعَادَةَ لِغَيْرِهِم فَهُم مَنْ يَصْنَعُونَ زَوْرَقَ العاشق الحالم ، وهُم فَيَصْنَعُونَ لَأَنْفُسِهِمُ الْمُسَرَّاتِ فَمَعَ أَنَّ كَنَّ القَدَرِ قَدْ إن هؤلاء الكادِحِينَ يَتَحَدَّونَ جَحِيمَ المعاناة،ِ وَيَقْهَرُونَ قَسْوَةَ الأَلَم،َ الحَدِيدِ ومناجم الفحم، وتطحن قواهم تَحْتَ أَشِعَةِ الشَّمْسِ أَلْقَتْ بِهِم في بقاع الأَرْضِ فَجَعَلَتْ رَحى الشَّمَاءِ تَعْرُكُ جَهْدَهُم فِي مَصَانِعِ أَحْلَامَ أَهْلِ العَرَامِ المِثَالِيَّة.ِ بِأَحْلامٍ مُتَوَاضِعَة،ٍ فلا يَخْلُمُونَ الحارقة، غير أن السعادة تملأ أعماقهم وتعمر أنفسهم لأهم يَخْلُمُونَ على الرَّغْمِ مِنَ المعاناة والأَلَمِ اللَّذِينَ يُحِيطَانِ معاني المقطع الثالث: إن هؤلاء الكادِحِينَ يَصْنَعُونَ لِأَنْفُسِهِم الأَفْرَاحَ وَالمَسَرَّاتِ أَصْلَابَهُم. مَةِ عَيْشِ تُقِيتُهُم وَتُسِكُ لا يَخْلُمُونَ إِلَّا بالحصولِ على لُ بِحَيَاتِهِم لَأَكُم يَعْلُمُونَ أَخْلَامًا بَسِيطَةً مُتَوَاضِعَةَ؛ فهم

=== BLOCK 3: مهارات الاستماع ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b51281
[BLOCK_TITLE]: مهارات الاستماع :
[CONTENT]:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: - ما الطَّبَقَةُ الاجتماعية التي يَتَحَدَّثُ عنها الشَّاعِرُ فِي النَّص؟ ج -۱ الطَّبَقَةُ الفَقِيرَةُ الكَادِحَة.ُ
[LIST_ITEM_CONTENT]: - مِمَّ اسْتَمَدَّ الشَّاعِرُ مَوْضُوعَهُ فِي الأبياتِ السَّابِقَةِ؟ ج٢ - اسْتَمَدَّهُ مِنَ الواقع الاجتماعي.

=== BLOCK 4: مهارات القراءة ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b71163
[BLOCK_TITLE]: مهارات القراءة :
[CONTENT]:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: - ما القضية التي تناونها النَّ؟ ج -۱ معاناة الكادِحِينَ مِنَ الفَقْر،ِ وَبَسَاطَةُ أَحْلامِهِم.
[LIST_ITEM_CONTENT]: - ٢ اعتمد الشاعر على المتناقضاتِ فِي عَرْضِ فِكَرِهِ ذَلِكَ على ذَلِكَ مِنَ المَقْطَعِينِ الثَّاني والثَّالِث.ِ ج -٢ المقطع الثاني: الملايين التي تَكْدَحُ تَعْرَى تَتَمَزَّق،ْ الملاينُ التِي تَصْنَعُ لِلحَالِمٍ زَوْرَق،ْ الملاينُ التِي تَصْنَعُ مِنْدِيلًا لِمُغْرَم.ْ المَقْطَعُ الثَّالِثِ الملايين التي تبكي، تُعْني.

=== BLOCK 5: الاستيعاب والفهم والتحليل ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b13930
[BLOCK_TITLE]: الاستيعاب والفهم والتحليل: المستوى الفكري:
[CONTENT]:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: - استَعِنْ بِالْمُعْجَمِ فِي تَعَرَّفِ مَعْنى كلِمَةِ مغرم(، في كل ما يأتي: قال البياتي: الملايين التي تصنَعُ مِنْدِيلًا لِمُغْرَم. قال أحمد محرم: مَعَارِمُ شَتَّى لا تزال تُصِيبُنِي إِذا مَغْرَمٌ مِنْهَا انْقَضَى جَاءَ مَعْرَمُ - عند البياني المفرم: المولع الذي أولع بالشَّيْءٍ لَا يَصْبَرُ على مُفَارَقَتِهِ - عند محرم المفرم: الدين والغرامة، وجمعها: معارم.
[LIST_ITEM_CONTENT]: - شَكَّلْ مُعْجَمَا لُغَوِيَّا لِكُلِّ مِن:ْ )المعاناة - السعادة(. ج٢ - المعاناة: )تَكَدَح، مؤت، أَحزان، تَعْرَى، تنمرق، تبكي نام....( - السعادة: )تُفَني، تَضْحَك،َ القمر الحالم ، تحلم، فراشة، البنفسج (...
[LIST_ITEM_CONTENT]: ج - المُقْطَعُ الْأَوَّلُ التَّرُوعُ الإِنْسَانِي لَدَى الكَادِحِينَ تَمَني الكادِحِينَ الخير لجميع الكائنات، وعدم حُلْمِهِم بأحلام مثالية(. اذكر الفِكَرِ الرَّئيسةَ لِكُلِّ مَقْطَعِ مِنَ مَقاطِعِ النَّصِ مُسْتَعِيْنَا بِالْمُعْجَمَيْنِ السَّابِقِين.ِ - المقطع الثاني: تصوير معاناة الكادِحِينَ وَبَيَانُ دَوْرِهِمْ فِي إسعاد الآخرين، وإظهارُ قَنَاعَتِهِمْ بِوَاقِعِهِم. - المَقْطَعُ الثَّالث: معاناة الكادِحِينَ وبساطة أحلامهم.
[LIST_ITEM_CONTENT]: - بدا النزوع الإنساني واضحا لدى الكادِحِينَ على الرغم مِنْ شَقَائِهِم بَنْ ذَلِكَ مِنْ فَهْمِكَ الْمَقْطَعَ الْأَوَّل.َ وَرْدَة.ٍ ج - ظهر التزوع الإنساني لدى الكادحين من خلال عدم حُلِمِهِم بَمَوتِ فَرَاشَةٍ أو بِحُزْنِ
[LIST_ITEM_CONTENT]: النَّانِي؟ ه- ما الذي يُقَدِّمُهُ الكَادِحُونَ مِنْ أَجْلِ إسعاد الآخرين كما بَدَا فِي الْمُقْطَعِ جه - إنَّ الكَادِحِينَ يَصْنَعُونَ زَوْرَقَ العاشِقِ الحالم، وينسجُونَ مَندِيلَ العِشْقَ لِكُلفِ وَلِهِ مُولَعِ مُغْرَم.
[LIST_ITEM_CONTENT]: أَنْرَهَا فِيهِم. - صَوَّرَ الشَّاعِرُ الظُّروف القاسية التي يَعْمَلُ فيها الكادِحُونَ اذْكُرُ هَذِهِ الظُّروف، وَبَيَنْ ج - إِنَّ الكَادِحِينَ يَعْمَلُونَ فِي مصانع الحديد ومناجمِ الفَحْم،ِ وَيَكْدَحُونَ تَحْتَ أَشِيَّةِ الشَّمْسِ الْحَارِقَة.ِ

=== BLOCK 6: Cut Content Part 1 ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
[UNIQUE_ID]: b63831
[BLOCK_TITLE]: الاستيعاب والفهم والتحليل
[CONTENT]: الإنساني الدافي وأحلامهم. أَبْرَزَ الشَّاعِرُ تَحَدِّي الكادِحِينَ ظُرُوفَهُمُ القَاسِيةَ بَيِّنْ أَوْجُهُ التَّحَدِي مِنْ خلال عالمهم
-  -
١٤٢

--- END STREAM ---
