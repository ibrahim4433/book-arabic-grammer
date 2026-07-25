# **SESSION 142**

[TASK DEFINITION]
Objective: Implement page 142.
File: `pages/page_142.html` (Note: Use the exact page number.)
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
[LESSON_NUMBER]: 142
[CHAPTER_TITLE]: page 142
[CATEGORY_HEADER]: 142
[SECTION_HEADER]: 142
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: معاني المقاطع ===
(Component: TEMPLATE_C_BLOCK.html)
Title: معاني المقاطع
Content:
<p class="text-accent">معاني المقطع الأول : الكادِحُونَ يَتَمَنُونَ الخَيْرَ لِجَمِيعِ الكائناتِ؛ فلا يَحْلُمُونَ بِمَوتِ فَرَاشَة،ٍ ولا بِحُزْنِ وَرْدَةِ إِنَّهُم لَا يَحْلُمُونَ أَحْلَامًا عَظِيمَةً كبيرة، فلا يَحْلُمُونَ بِقَضَاءِ أَوْقَاتٍ سَعِيدَة على ظهر قارب يَطْفُو على صفحة الماء، تُكَلِلَّهُ أَشِعَةُ القَمَرِ الْفِضَيَّةِ فِي لَيْلَةِ أَنْسِ صيفية، لا ولا يَحْلُمُونَ بِلَحَظَاتِ العِشق والغرام التي ينعم بِسَعَادَتِهَا العَاشِقُون.َ</p>
<p>معانى المقطع الثاني: الكادِحُونَ يَتَجَرَّعُونَ مَرَارَةَ الْمُعَانَاةِ وَعَلْقَمَ الحرمان وعذابَ الفَقْرِ والعَوَن،ِ وَمَعَ كُل ذلك يَكْدَحُونَ لِيَصْنَعُوا السَّعَادَةَ لِغَيْرِهِم فَهُم مَنْ يَصْنَعُونَ زَوْرَقَ العاشق الحالم ، وهُم مَنْ يَنْسِجُونَ مِنْدِيلَ العِشْقِ لِكَلِفٍ مُولَعِ مُغْرَم. إن هؤلاء الكادِحِينَ يَتَحَدَّونَ جَحِيمَ المعاناة،ِ وَيَقْهَرُونَ قَسْوَةَ الأَلَم،َ فَيَصْنَعُونَ لَأَنْفُسِهِمُ الْمُسَرَّاتِ فَمَعَ أَنَّ كَفَّ القَدَرِ قَدْ أَلْقَتْ بِهِم في بقاع الأَرْضِ فَجَعَلَتْ رَحى الشَّقَاءِ تَعْرُكُ جَهْدَهُم فِي مَصَانِعِ الحَدِيدِ ومناجم الفحم، وتطحن قواهم تَحْتَ أَشِعَةِ الشَّمْسِ الحارقة، غير أن السعادة تملأ أعماقهم وتعمر أنفسهم لأنهم يَحْلُمُونَ بِأَحْلامٍ مُتَوَاضِعَة،ٍ فلا يَحْلُمُونَ أَحْلَامَ أَهْلِ الغَرَامِ المِثَالِيَّة.ِ</p>
<p>معاني المقطع الثالث: إن هؤلاء الكادِحِينَ يَصْنَعُونَ لِأَنْفُسِهِم الأَفْرَاحَ وَالمَسَرَّاتِ على الرَّغْمِ مِنَ المعاناة والأَلَمِ اللَّذِينَ يُحِيطَانِ بِحَيَاتِهِم لأنهم يَحْلُمُونَ أَحْلَامًا بَسِيطَةً مُتَوَاضِعَةَ؛ فهم لا يَحْلُمُونَ إِلَّا بالحصولِ على لُقْمَةِ عَيْشِ تُقِيتُهُم وَتُسْنِدُ أَصْلَابَهُم.</p>

=== BLOCK 3: مهارات الاستماع والقراءة ===
(Component: TEMPLATE_C_LIST.html)
Title: مهارات الاستماع والقراءة
List Items:
- <span class="highlight-blue">ما الطَّبَقَةُ الاجتماعية التي يَتَحَدَّثُ عنها الشَّاعِرُ فِي النَّص؟</span> الطَّبَقَةُ الفَقِيرَةُ الكَادِحَة.ُ (مهارات الاستماع - ج۱)
- <span class="highlight-blue">مِمَّ اسْتَمَدَّ الشَّاعِرُ مَوْضُوعَهُ فِي الأبياتِ السَّابِقَةِ؟</span> اسْتَمَدَّهُ مِنَ الواقع الاجتماعي. (ج٢)
- <span class="highlight-blue">ما القضية التي تناونها النَّصُ؟</span> معاناة الكادِحِينَ مِنَ الفَقْر،ِ وَبَسَاطَةُ أَحْلامِهِم. (مهارات القراءة - ج۱)
- <span class="highlight-blue">اعتمد الشاعر على المتناقضاتِ فِي عَرْضِ فِكَرِهِ ذَلِكَ على ذَلِكَ مِنَ المَقْطَعِينِ الثَّاني والثَّالِث.ِ</span> (ج٢) المقطع الثاني: الملايين التي تَكْدَحُ تَعْرَى تَتَمَزَّق،ْ الملاينُ التِي تَصْنَعُ لِلحَالِمٍ زَوْرَق،ْ الملاينُ التِي تَصْنَعُ مِنْدِيلًا لِمُغْرَم.ْ المَقْطَعُ الثَّالِثِ الملايين التي تبكي، تُغَنِّي.

=== BLOCK 4: الاستيعاب والفهم والتحليل - المستوى الفكري ===
(Component: TEMPLATE_C_SPLIT.html)
Title: الاستيعاب والفهم والتحليل - المستوى الفكري
Content Right:
<div class="block-body">
  <p>استَعِنْ بِالْمُعْجَمِ فِي تَعَرَّفِ مَعْنى كلِمَةِ (مغرم)، في كل ما يأتي:</p>
  <ul class="structured-list">
    <li>قال البياتي: الملايين التي تصنَعُ مِنْدِيلًا لِمُغْرَم. (عند البياتي المُغْرَم: المولع الذي أولع بالشَّيْءٍ لَا يَصْبَرُ على مُفَارَقَتِهِ)</li>
    <li>قال أحمد محرم: مَغَارِمُ شَتَّى لا تزال تُصِيبُنِي إِذا مَغْرَمٌ مِنْهَا انْقَضَى جَاءَ مَغْرَمُ (عند محرم المَغْرَم: الدين والغرامة، وجمعها: مَغَارِم.)</li>
  </ul>
</div>
Content Left:
<div class="block-body">
  <p>شَكَّلْ مُعْجَمَا لُغَوِيَّا لِكُلِّ مِن:ْ (المعاناة - السعادة). (ج٢)</p>
  <ul class="structured-list">
    <li><span class="highlight-red">المعاناة:</span> (تَكَدَح، مؤت، أَحزان، تَعْرَى، تتمزق، تبكي، نام....)</li>
    <li><span class="highlight-blue">السعادة:</span> (تُغَنِّي، تَضْحَك،َ القمر الحالم ، تحلم، فراشة، البنفسج ...)</li>
  </ul>
</div>

=== BLOCK 5: الفكر الرئيسة ===
(Component: TEMPLATE_C_TABLE.html)
Title: اذكر الفِكَرِ الرَّئيسةَ لِكُلِّ مَقْطَعِ مِنَ مَقاطِعِ النَّصِ مُسْتَعِيْنَا بِالْمُعْجَمَيْنِ السَّابِقِين.ِ
Headers: المقطع | الفكرة الرئيسة
Row 1: المُقْطَعُ الْأَوَّلُ | النَّزُوعُ الإِنْسَانِي لَدَى الكَادِحِينَ تَمَني الكادِحِينَ الخير لجميع الكائنات، وعدم حُلْمِهِم بأحلام مثالية(.
Row 2: المقطع الثاني | تصوير معاناة الكادِحِينَ وَبَيَانُ دَوْرِهِمْ فِي إسعاد الآخرين، وإظهارُ قَنَاعَتِهِمْ بِوَاقِعِهِم.
Row 3: المَقْطَعُ الثَّالث | معاناة الكادِحِينَ وبساطة أحلامهم.

=== BLOCK 6: أجوبة الاختبار ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: أجوبة الاختبار
Content:
- ج: ظهر النزوع الإنساني لدى الكادحين من خلال عدم حُلِمِهِم بَمَوتِ فَرَاشَةٍ أو بِحُزْنِ وَرْدَة.ٍ
- جه - إنَّ الكَادِحِينَ يَصْنَعُونَ زَوْرَقَ العاشِقِ الحالم، وينسجُونَ مَندِيلَ العِشْقَ لِكُلفِ وَلِهِ مُولَعِ مُغْرَم.
- ج - إِنَّ الكَادِحِينَ يَعْمَلُونَ فِي مصانع الحديد ومناجمِ الفَحْم،ِ وَيَكْدَحُونَ تَحْتَ أَشِعَّةِ الشَّمْسِ الْحَارِقَة.ِ
- ١٤٢

=== BLOCK 7: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Title: اختبر نفسك
Question 1: بدا النزوع الإنساني واضحا لدى الكادِحِينَ على الرغم مِنْ شَقَائِهِم بَنْ ذَلِكَ مِنْ فَهْمِكَ الْمَقْطَعَ الْأَوَّل.َ
Question 2: ه- ما الذي يُقَدِّمُهُ الكَادِحُونَ مِنْ أَجْلِ إسعاد الآخرين كما بَدَا فِي الْمُقْطَعِ النَّانِي؟
Question 3: صَوَّرَ الشَّاعِرُ الظُّروف القاسية التي يَعْمَلُ فيها الكادِحُونَ اذْكُرُ هَذِهِ الظُّروف، وَبَيَنْ أَنْرَهَا فِيهِم.
Question 4: أَبْرَزَ الشَّاعِرُ تَحَدِّي الكادِحِينَ ظُرُوفَهُمُ القَاسِيةَ بَيِّنْ أَوْجُهُ التَّحَدِي مِنْ خلال عالمهم الإنساني الدافي وأحلامهم.

--- END STREAM ---
