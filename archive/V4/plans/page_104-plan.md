# **SESSION 104**

[TASK DEFINITION]
Objective: Implement page 104.
File: `pages/page_104.html` (Note: Use the exact page number.)
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
[LESSON_NUMBER]: 104
[CHAPTER_TITLE]: page 104
[CATEGORY_HEADER]: 104
[SECTION_HEADER]: 104
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: هُ لِأُفْقِ أَرْحَب فأعدد ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[BLOCK_TITLE]: هُ لِأُفْقِ أَرْحَب فأعدد
[CONTENT]:
هُ لِأُفْقِ أَرْحَب فأعدد
이이 이 이
فعلائن فعلاتن فَاعِلُنْ
قَتْ بِهِ صَحْ راوه أصيد ضا
이어 이이이 이
فَاعِلَاتُنْ فَاعِلَاتُنْ فَاعِلُن

بحر الرمل

=== BLOCK 3: المستوى الإبداعي ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المستوى الإبداعي:
Content:
<span class="text-accent">خَتَمَ الشَّاعِرُ قصيدتَهُ بِدَوْرِ الأَبْطَالِ فِي حماية الأَرْضِ وحفظ كرامتها ، أَضِفُ إِلَى هَذِهِ الخَالِمَةِ مَا يُعَرِّزُ هذا الدَّوْر.َ</span>
بمقدور الطالب أن يجيب على هذا السؤال بالقول:
لا يَنْبَغِي لأَبْنَاءِ الوَطَنِ الأَبْطَالِ أَنْ يُخِلُوا بَادَاءِ مَسْؤوليتِهِم المتَمَثَلَةِ بِالحِفَاظِ على الأَرْض،ِ والدفاع عنها. فعلى عَاتِقِهِم تَقَعُ مَسْؤُولِيَّةِ حمَايَةِ ممتَلَكَاتِ المَوَاطِنِينِ الْخَاصَّة،ِ وَصَوْنِ مَرَافِقِ الوَطَنِ العَامَّة،ِ وَتَتَمَثَلُ بُطُولَةُ أَبْنَاءِ الوَطَنِ فِي أَعْلَى صُورِهَا فِي حِفَاظِهِم عَلَى ثَرَوَاتِ الْوَطَنِ وتَقْدِيمِ الفِدَاءِ لِتَأْمِينِ سَلَامَةِ أَرْوَاحِهِم. الماديَّةِ بِجَمِيعِ أَنْوَاعِهَا، وَحِفَاظِهِم على ثَرَوَاتِهِ البَشَرِيَّةِ عَنْ طَرِيقِ نَشْرِ الأَمْنِ فِي أَرْجَاءِ الوَطَنِ كَافَّة؛ لَيَحُولَ دُونَ هِجْرَةِ أَصْحَابِ الْعُقُول،ِ وتَتَجَلَّى البُطُولَةَ كَذَلِكَ فِي المُسَاهَمَةِ فِي عَمَلَيَّةِ بِنَاءِ الوَطَن،ِ وَالعَمَل على ازدِهَارِهِ وَتَقَدُّمِهِ مِنْ خِلَالِ الإِقْبَالِ على طَلَبِ العِلْم،ِ ومُتَابَعَةِ التَّحْصِيلِ العِلْمِي إلى أَعْلَى الْمُسْتَوَيَاتِ التَّعْلِيمِيَّة،ِ وَالسَّعْمِ الجَادَ لِتَطْوِيرِ الدَّاتِ عَنْ طَرِيقِ الاهتمام بالتَّقَانَةِ والبرمجة والحُوَاسِيبِ وَيَنْبَغِي الأَبِنَاءِ الوَطَنِ الْأَبْطَالِ أَلَّا يَغْضُوا الطَّرْفَ عَنْ تَجَارِبِ الأُمَمِ المَتَقَدِّمَةِ والخبراتِ التِي وَصَلَتْ إليها؛ لأَمَا عَامِلٌ فَعَالٌ فِي دَفْعِ عَمَلِيَّةِ التَّنمِيَةِ والازدهار.
وبمقدوري أن أقول :

=== BLOCK 4: شعر ===
(Component: TEMPLATE_C_POEM.html)
Title:
Poet:
[RIGHT_HEMISTICH_1]: كَفَّنَتْ أَجْدَادَنَا فِي جَوْفِها
[LEFT_HEMISTICH_1]: وطَوَهم فِي ثِيابِ حُضْبِ
[RIGHT_HEMISTICH_2]: وسَيَأْتِي دَوْرُنا القاضي بأن
[LEFT_HEMISTICH_2]: نُرْخِصَ الروح فداء الحسب

=== BLOCK 5: التعبير الكتابي ===
(Component: TEMPLATE_C_BLOCK.html)
Title: التعبير الكتابي:
Content:
<span class="text-accent">حَرَرُ نَصَ (عُرْسِ المجد) مُسْتَعِينا بالفائدة الآتية:</span>

=== BLOCK 6: فائدة ===
(Component: TEMPLATE_C_BENEFIT.html)
Title: فائدة
Content: فائدة حول منهجية تحرير النص

=== BLOCK 7: منهجية تحرير النص - المقدمة والفكر ===
(Component: TEMPLATE_C_LIST.html)
[LIST_TITLE]:
[LIST_ITEMS]:
- المقدمة: يستفاد في كتابتها من الموضوع الذي يدور حوله النص، أو ما ورد في مدخل النص.
- دراسة المستوى الفكري: تذكر الفكر والمعاني التي يتضمنها النص؛ أي يُذكر ما يتوافر في النَّصَ مِنْ فِكْرَةِ عَامَّة،ِ وَفِكَرِ فَرْعِيَّة،ِ ومعان.ٍ [ إِذا طَلِبَ تَخْرِيرُ نص كامل، تُذَكَرُ الفِكَرُ الرئيسَةُ لمقاطعه، والمعاني المُندَرِجَةُ تَحْتَ كُلِّ فِكْرَةِ رَئِيسَةٍ بإيجاز لا يخل بالمعنى]

=== BLOCK 8: دراسة المستوى الفني ===
(Component: TEMPLATE_C_TABLE.html)
[TABLE_TITLE]: دراسة المستوى الفني من الممكن أن تدرس في هذا المستوى:
[HEADER_1]: العنصر الفني
[HEADER_2]: التفاصيل
[ROW_1_COL_1]: بعض الوسائل التعبيرية (الصياغة اللفظية، الحقل المعجمي ......)
[ROW_1_COL_2]:
[ROW_2_COL_1]: - بعض العناصر البلاغية البارزة في النص (المحسنات البديعية، الأساليب الخبرية والإنشائية، الصور البيانية، ......)
[ROW_2_COL_2]:
[ROW_3_COL_1]: بعض عناصر المستوى التركيبي البارزة في النص (الجملة الاسمية، الفعل الماضي، الفعل المضارع، فعل الأمر ......)
[ROW_3_COL_2]:
[ROW_4_COL_1]: - بعض العناصر الموسيقية البارزة في النص (وحدة الوزن والقافية وحرف الروي، التكرار، حروف الهمس والجهر، ......)
[ROW_4_COL_2]:

=== BLOCK 9: الخاتمة ===
(Component: TEMPLATE_C_LIST.html)
[LIST_TITLE]:
[LIST_ITEMS]:
- الخاتمة: تظهر تكامل المستويين الفكري والفني وتأزرهما لإبراز مقولة النص الرئيسة، وإيصال مضمونه إلى المتلقي للتأثير فيه وإقناعه.

=== BLOCK 10: ملاحظة ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: ملاحظة:
Content: لا يشترط في المستوى الفني دراسة كل ما ذكر على سبيل الاستقصاء، وإنما يدرس ما هو بارز منها في النَّص؛ لأنَّ لكل نص أدبي مكونات فكرية، وأدوات تعبيرية، ووسائل فنية خاصة به.

=== BLOCK 11: قالب تحرير النص ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
[BLOCK_TITLE]:
[CONTENT]:
يمكن الاستفادة من القالب الآتي من أجل تحرير النص وفق منهجية تحرير النص:
يبدأ تحرير النص بمقدمة مناسبة وقد جَعَلَ الشَّاعِرُ [ يُذكر هنا اسم الشاعر ..... تذكر هنا الفكرة العامة التي تدور حولها الأبيات الثلاثة أو الأربعة ..... فكرة عامَّةً لِنَصِه الذي قَسَمَهُ إِلى ثلاث فكر فرعية أو أربع فكر فرعية ، ضمن كل واحدة منها في بيت من أبيات النص الثلاثة أو الأربعة ،] فقد تضمن البيت

--- END STREAM ---
