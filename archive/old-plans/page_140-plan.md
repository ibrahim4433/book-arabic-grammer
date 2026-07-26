# **SESSION 140**

[TASK DEFINITION]
Objective: Implement page 140.
File: `pages/page_140.html`
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
[LESSON_NUMBER]: 140
[CHAPTER_TITLE]: page 140
[CATEGORY_HEADER]: 140
[SECTION_HEADER]: 140
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: الاستيعاب والفهم والتحليل ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الاستيعاب والفهم والتحليل
Content: <span class="text-accent">الوحدة الثانية مناهج النقد المنهج الاجتماعي في النقد الأدبي أحزان البنفسج عبد الوهاب البياتي المنهج النفسي في النقد الأدبي شعوری التفكير النقدي المنهج الاجتماعي في النقد الأدبي نديم محمد د. محمود السيد</span>

=== BLOCK 3: إجابات الاستيعاب ===
(Component: TEMPLATE_C_TABLE.html)
Header 1: المفهوم
Header 2: الإجابة
Row 1 Col 1: المنهج الاجتماعي
Row 1 Col 2: ج -۱ المنهج الاجتماعي في التَّقْدِ الأدبي هو المنهج الذي يربط الأدب بالمجتمع، وينظر إليهِ بِوَصْفِهِ لِسَانَ حَالِ الْمُجْتمع وصورته، ووثيقة تارجية واجتماعيةً عَنه.ُ ومن خصائِصِه:ِ ١ - الْأَدَبُ ظَاهِرَةً اجتماعية، وله وظيفة اجتماعية - الأديب والمجتمع طرفانِ مُتكاملانٍ تَنْشَأْ بينهما علاقاتُ تَأْثير وتَأْثُر ٣- الأَدَبُ لِيسَ مِرْآةٌ جَامِدَةً للمُجْتَمَعِ بَلْ وعي بِه.ِ - الأَدَبُ يَتوجه إلى جمهور، ومطلوب مِنْهُ أَن يجعل هذا الجمهور غايته.
Row 2 Col 1: الأدب والمجتمع
Row 2 Col 2: ج ۲ - أَي أَنَّ الأَدَبَ لَا يَنْقُلُ الوَاقِعَ نَقْلَا حَرْفِيًّا وَيَعْكِسُهُ كما هو، وإنما يَنْقُلُهُ بعد انفعالِ الأَدِيبِ بِه،ِ وَوَعْبِهِ لَهُ فَالْآدِيبُ يُسْهِمُ بِرُواه ومواقفه في بناء الواقع الاجتماعي، وينقلُهُ إِلَى طَوْرٍ أَكْثَرَ عَدَالَة.ٍ

=== BLOCK 4: آراء نقدية ===
(Component: TEMPLATE_C_SPLIT.html)
Right Title: مدام دو ستايل
Right Content: ج - تناولتْ فِيهِ تَأْثير الدين والعادات والقوانين في الأدب، وتأثر الأدب بالدين وبالعادات وبالقوانين، وانتهت إلى أَنَّ الأَدَبَ يتغيَّرُ بِتغير المجْتَمعات،ِ وَيَتَطَوَّرُ بِتَطورها .
Left Title: لوسيان كولدمان
Left Content: ج ٤ - انطلق في دراستِهِ لِلأَدَبِ مِنَ أَنَّ السُّلُوكَ الإنساني يسعى إلى إيجاد توازن بينَ الدَّاتِ الفَاعِلَةِ والمُجْتَمَعِ وَأَنَّ هذا السَّعْيَ سرعان ما يتجاوز نفسه في عملية تقويض وبناء منتابِعَتَيْن،ِ وَلَدَى محاولة تحديدِهِ الدَّاتَ الفَاعِلَةَ أهي الفَرْدُ أَم الجماعة؟، انتهى إلى أَنَّ الجماعةَ لِيسَتْ سوى شَبَكَةٍ مُعَقَدَةٍ مِنَ العلاقات المُتَبَادَلَةِ بِينَ الْأَفْرَاد،ِ وَدَوَرَ الأَفْرَادِ الفاعلين فيها هي التي تحدد بنِيةَ تِلْكَ الشَّبَكَةِ وَأَنَّ الدَّرَاسَةَ النَّقْدِيَّةَ الصَّائِيةَ الإدراك العلاقَةِ بينَ الأَدَبِ وَمُبْدِعِهِ الحقيقي الذي هو، برأيه، الجماعة الاجتماعية وليس الفَرْد.َ

=== BLOCK 5: أبرز ملامح المنهج ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: تنبيه
Content: جه - الملام أن الأدب فعل اجتماعي، ولا غِنَى لَهُ عَنْ مُتَلَق،ٍ وأَنَّهُ مَا مِنْ بقاء لأدب ما لم يَتَّخِذْ لبقائه مادةً لَه،ُ فيقِفُ إلى جانب الإنسان وقضاياه، ويتعدى تصوير ما هو كائِنٌ إلى تصوير ما يجب أن يكون. - أبرز الأعلام عمر فالحوري، سلامة موسى محمد مندور، محمود أمين العالم.

=== BLOCK 6: اختبار الاستيعاب ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: س -۱ وَضِحِ الْمَقَصُودَ بِالمَنْهَج الاجتماعي في النقد الأدبي، واذكر بعض خصائِصِه.ِ
Number: ٢
Question: س - ٢ الأدب ليس مرآة جامِدَةً لِلْمُجْتَمَع، بَلْ وعي بِه.ِ وضح ذَلِك.َ
Number: ٣
Question: س - ما الذي تناولته مدام دو ستايل" في كتابها "الأدب وعلاقته بالأنظمة الاجتماعية "؟
Number: ٤
Question: س ٤ - ما مُنْطَلَقُ "لوسيان كولدمان" في دراستِهِ الأَدَبَ؟ وما الدراسةُ النَّقْدِيَّةُ الصَّائِبَةُ فِي رأيهِ؟
Number: ٥
Question: سه - ما أبرز ملامح المنهج الاجتماعي في التَّقْدِ الأدب العربي ومَنْ أَبرز اعلامه ؟

--- END STREAM ---
