# **SESSION 154**

[TASK DEFINITION]
Objective: Implement page 154.
File: `pages/page_154.html` (Note: Use the exact page number.)
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
[LESSON_NUMBER]: 154
[CHAPTER_TITLE]: page 154
[CATEGORY_HEADER]: 154
[SECTION_HEADER]: 154
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: الوحدة الثالثة ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الغُرْبَةُ والاغتراب في الأدب المهجري
Content: الوحدة الثالثة

=== BLOCK 3: نصوص الوحدة ===
(Component: TEMPLATE_C_LIST.html)
- القراءة التمهيدية الأدب المهجرى
- نص أدبي وطني جورج صيدح
- نص أدبي المهاجر نسيب عريضة
- نص أدبي الغاب جبران خليل جبران
- نص أدبي البناء زكي قنصل
- نص إثرائي معاناة المغترب فوزي المعلوف
- المطالعة رسالة الشرق المتجدد ميخائيل نعيمة

=== BLOCK 4: الوحدة الثانية ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الغربة والاغتراب في الأدب المهجري
Content: الوحدة الثانية: الغربة والاغتراب في الأدب المهجري: تضمن بعض نتاج شعراء المهجر الذين توزعوا على المهجرين الشمالي والجنوبي، على هذا النحو :

=== BLOCK 5: المهجر الشمالي والجنوبي ===
(Component: TEMPLATE_C_SPLIT.html)
Right Content: المهجر الشمالي في الولايات المتحدة الأمريكية، فقد شكل الأدباء في هذا المهجر الرابطة القلمية، ومن أدباء هذه الرابطة: نسيب عريضة، جبران خليل جبران، ميخائيل نعيمة، إيليا أبو ماضي، عبد المسيح حداد. ومن أبرز ما امتاز به نتاج أدباء المهجر الشمالي التحرر مِنْ قُيُود الألفاظ والأساليب القديمة، وقد كان أدبهم في طابعه الرئيس وجدانياً إنسانياً صوفياً، يَنْزِعُ إلى الانعتاق الروحي والاجتماعي، ويميل إلى التنديد بالمادية والتفاخر بروحانية الشرق.
Left Content: المهجر الجنوبي في أمريكا الجنوبية، شكل الأدباء في هذا المهجر العصبة الأندلسية، ومن أدباء العصبة الأندلسية: جورج صيدح، فوزي المعلوف، زكي قنصل، حسني غراب، ميشال معلوف، داوود شکور، نظير زيتون، نصر سمعان، رشيد سليم الخوري (القروي)، إلياس فرحات. ومن أبرز ما امتاز به نتاج أدباء المهجر الجنوبي غلبة نفثات القومية الحماسية، والنزعة العربية الخالصة، وقد حافظ أدباء هذا المهجر على الديباجة العربية المشرقة والجزالة اللفظية.

=== BLOCK 6: القصائد الآتية ===
(Component: TEMPLATE_C_BLOCK.html)
Title: محتوى الوحدة
Content: وقد تضمنت هذه الوحدة القصائد الآتية:

=== BLOCK 7: Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Columns: القصيدة | الشاعر | المهجر | الرابطة
Row 1: وطني | للشاعر السوري جورج صيدح | الذي استقر في المهجر الجنوبي في أمريكا الجنوبية | فهو من شعراء العصبة الأندلسية.
Row 2: المهاجر | للشاعر السوري نسيب عريضة | الذي استقر في المهجر الشمالي في الولايات المتحدة الأمريكية | فهو من شعراء الرابطة القلمية.
Row 3: الغاب | للشاعر اللبناني جبران خليل جبران | الذي استقر في المهجر الشمالي في الولايات المتحدة الأمريكية | فهو من شعراء الرابطة القلمية.
Row 4: البناء | للشاعر السوري زكي قنصل | الذي استقر في المهجر الجنوبي في أمريكا الجنوبية | فهو من شعراء العصبة الأندلسية.

=== BLOCK 8: تواريخ ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: ملاحظة
Content: - - (۱۸۹۳ - ۱۹۷۸ م)

--- END STREAM ---
