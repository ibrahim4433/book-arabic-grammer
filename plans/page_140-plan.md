# **SESSION 140**

[TASK DEFINITION]
Objective: Implement page 140.
File: `pages/page_140.html` (Note: Use the exact page number.)
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
[UNIQUE_ID]: b28327
[LESSON_NUMBER]: 140
[CHAPTER_TITLE]: page 140
[CATEGORY_HEADER]: 140
[SECTION_HEADER]: 140
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: الاستيعاب والفهم والتحليل ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b49875
[BLOCK_TITLE]: الاستيعاب والفهم والتحليل:
[OPTIONAL_CLASS]:
[CONTENT]:
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: الوحدة الثانية مناهج النقد
[HEADER_2]: المنهج الاجتماعي في النقد الأدبي
[HEADER_3]: أحزان البنفسج عبد الوهاب البياتي
[CELL_1]: المنهج النفسي في النقد الأدبي شعوری
[CELL_2]: التفكير النقدي المنهج الاجتماعي في النقد الأدبي
[CELL_3]: نديم محمد د. محمود السيد

=== BLOCK 3: السؤال الأول ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b45666
[BLOCK_TITLE]: التَّقْدِ الأدبي هو المنهج الذي بعض خصائِصِه.ِ ج -۱ المنهج الاجتماعي في س -۱ وَضِحِ الْمَقَصُودَ بِالمَنْهَج الاجتماعي في النقد الأدبي، واذكر
[OPTIONAL_CLASS]: accent
[CONTENT]:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEMS]:
(Component: TEMPLATE_C_LIST_ITEM.html)
[MARKER]: ١ -
[LIST_ITEM_CONTENT]: <span class="text-accent">الْأَدَبُ ظَاهِرَةً وصورته، ووثيقة تارجية واجتماعيةً عَنه.ُ ومن خصائِصِه:ِ يربط الأدب بالمجتمع، وينظر إليهِ بِوَصْفِهِ لِسَانَ حَالِ الْمُجْتمع</span>
(Component: TEMPLATE_C_LIST_ITEM.html)
[MARKER]: -
[LIST_ITEM_CONTENT]: مِرْآةٌ جَامِدَةً علاقاتُ تَأْثير وتَأْثُر ٣- الأَدَبُ لِيسَ والمجتمع طرفانِ مُتكاملانٍ تَنْشَأْ بينهما اجتماعية، وله وظيفة اجتماعية - الأديب
(Component: TEMPLATE_C_LIST_ITEM.html)
[MARKER]: -
[LIST_ITEM_CONTENT]: غايته. مِنْهُ أَن يجعل هذا الجمهور إلى جمهور، ومطلوب للمُجْتَمَعِ بَلْ وعي بِه.ِ - الأَدَبُ يَتوجه

=== BLOCK 4: السؤال الثاني ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b53797
[BLOCK_TITLE]: حَرْفِيًّا وَيَعْكِسُهُ كما هو، وإنما - أَي أَنَّ الأَدَبَ لَا يَنْقُلُ الوَاقِعَ نَقْلَا بِه.ِ وضح ذَلِك.َ ج ۲ س - ٢ الأدب ليس مرآة جامِدَةً لِلْمُجْتَمَع، بَلْ وعي
[OPTIONAL_CLASS]:
[CONTENT]:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEMS]:
(Component: TEMPLATE_C_LIST_ITEM.html)
[MARKER]: -
[LIST_ITEM_CONTENT]: أَكْثَرَ عَدَالَة.ٍ الاجتماعي، وينقلُهُ إِلَى طَوْرٍ فَالْآدِيبُ يُسْهِمُ بِرُواه ومواقفه في بناء الواقع يَنْقُلُهُ بعد انفعالِ الأَدِيبِ بِه،ِ وَوَعْبِهِ لَهُ

=== BLOCK 5: السؤال الثالث ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b81728
[BLOCK_TITLE]: وعلاقته بالأنظمة الاجتماعية "؟ س - ما الذي تناولته مدام دو ستايل" في كتابها "الأدب
[OPTIONAL_CLASS]:
[CONTENT]:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEMS]:
(Component: TEMPLATE_C_LIST_ITEM.html)
[MARKER]: -
[LIST_ITEM_CONTENT]: يتغيَّرُ بِتغير وبالقوانين، وانتهت إلى أَنَّ الأَدَبَ في الأدب، وتأثر الأدب بالدين وبالعادات ج - تناولتْ فِيهِ تَأْثير الدين والعادات والقوانين

=== BLOCK 6: السؤال الرابع ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b78906
[BLOCK_TITLE]: النَّقْدِيَّةُ الصَّائِبَةُ فِي رأيهِ؟ دراستِهِ الأَدَبَ؟ وما الدراسةُ - ما مُنْطَلَقُ "لوسيان كولدمان" في المجْتَمعات،ِ وَيَتَطَوَّرُ بِتَطورها . س ٤
[OPTIONAL_CLASS]:
[CONTENT]:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEMS]:
(Component: TEMPLATE_C_LIST_ITEM.html)
[MARKER]: -
[LIST_ITEM_CONTENT]: وَأَنَّ هذا السَّعْيَ سرعان الْمُبْدِعِ الدَّاتِ الفَاعِلَةِ والمُجْتَمَعِ الإنساني يسعى إلى إيجاد توازن بينَ - انطلق في دراستِهِ لِلأَدَبِ مِنَ أَنَّ السُّلُوكَ
(Component: TEMPLATE_C_LIST_ITEM.html)
[MARKER]: -
[LIST_ITEM_CONTENT]: أَنَّ الجماعةَ لِيسَتْ الفَاعِلَةَ أهي الفَرْدُ أَم الجماعة؟، انتهى إلى منتابِعَتَيْن،ِ وَلَدَى محاولة تحديدِهِ الدَّاتَ ما يتجاوز نفسه في عملية تقويض وبناء
(Component: TEMPLATE_C_LIST_ITEM.html)
[MARKER]: -
[LIST_ITEM_CONTENT]: وَدَوَرَ الأَفْرَادِ الفاعلين فيها هي التي تحدد بنِيةَ تِلْكَ الشَّبَكَةِ وَأَنَّ الدَّرَاسَةَ النَّقْدِيَّةَ الصَّائِيةَ سوى شَبَكَةٍ مُعَقَدَةٍ مِنَ العلاقات المُتَبَادَلَةِ بِينَ الْأَفْرَاد،ِ
(Component: TEMPLATE_C_LIST_ITEM.html)
[MARKER]: -
[LIST_ITEM_CONTENT]: الاجتماعية وليس الفَرْد.َ الذي هو، برأيه، الجماعة الإدراك العلاقَةِ بينَ الأَدَبِ وَمُبْدِعِهِ الحقيقي

=== BLOCK 7: السؤال الخامس ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b98467
[BLOCK_TITLE]: لَهُ عَنْ مُتَلَق،ٍ فعل اجتماعي، ولا غِنَى جه - الملام أن الأدب العربي ومَنْ أَبرز اعلامه ؟ سه - ما أبرز ملامح المنهج الاجتماعي في التَّقْدِ
[OPTIONAL_CLASS]:
[CONTENT]:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEMS]:
(Component: TEMPLATE_C_LIST_ITEM.html)
[MARKER]: -
[LIST_ITEM_CONTENT]: ما يجب تصوير ما هو كائِنٌ إلى تصوير جانب ما هو خى، ويتعدى قضايا الإنسان مادةً لَه،ُ فيقِفُ إلى وأَنَّهُ مَا مِنْ بقاء لأدب ما لم يَتَّخِذْ لبقائه
(Component: TEMPLATE_C_LIST_ITEM.html)
[MARKER]: -
[LIST_ITEM_CONTENT]: <span class="highlight-red">محمود أمين العالم. أن يكون. - أبرز الأعلام عمر فالحوري، سلامة موسى محمد مندور،</span>

--- END STREAM ---
