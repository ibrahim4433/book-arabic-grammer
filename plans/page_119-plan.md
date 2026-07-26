# **SESSION 119**

[TASK DEFINITION]
Objective: Implement page 119.
File: `pages/page_119.html`
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
[LESSON_NUMBER]: 119
[CHAPTER_TITLE]: page 119
[CATEGORY_HEADER]: 119
[SECTION_HEADER]: 119
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: مؤشرات النمط الوصفي ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[BLOCK_TITLE]: مؤشرات النمط الوصفي
[CONTENT]:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_1]: ١- الإكثار مِنَ الصفات، أو الجمل الاسمية التي تمكن من إطلاق الصفات والنعوت.
[LIST_ITEM_2]: ٢- استعمال الأفعال الدالة على حالة الموصوف،
[LIST_ITEM_3]: ٣- اعتماد الفعل الماضي، والمضارع للدلالة على الحركة والحيوية والاستمرار. وبدخول (كان) على هذه الجمل، ينتقل الوَصْفُ مِنَ الحاضر إلى الماضي.
[LIST_ITEM_4]: ٤- استعمال الفعل الماضي لوَصْفِ حادث مَضَى
[LIST_ITEM_5]: ٥- الإكثار مِنَ الأساليب الانفعالية، كالتعجب والتمني والاستفهام.
[LIST_ITEM_6]: ٦- تحديد واضح لزمان والمكان واستخدام روابطهما.
[LIST_ITEM_7]: ٧- استعمال المصادر، والأفعال الدالة على الانفعال.
[LIST_ITEM_8]: ٨- كَثْرَةُ الصُّور الفنيَّةِ المُؤَثِّرَةِ فِي النَّفْس،ِ والخيالية الموحية.
[LIST_ITEM_9]: ٩- تكوين حَقْلِ مُعْجَمي خاص بالموصوف
[LIST_ITEM_10]: ١٠- اندماج ذات الكاتب بالموصوف، والنَّظَرُ إليه من خلال حالتِهِ النَّفُسِية.ِ

=== BLOCK 3: مؤشرات النَّمَطِ السَّرْدِي ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مؤشرات النَّمَطِ السَّرْدِي:
Content:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_1]: - اعتماد الحوار الذي يضفي على الشرد الواقعية والحركة والحياة، ويساعد في الكشف عن الطبائع: قال الشيخ منتعشا: وكم ... يدان(.
[LIST_ITEM_2]: - استعمال الأفعال الماضية: (تحسس، تلا، صاح، أزاحت، أصابت، طار، .....).

=== BLOCK 4: الحوار و الكشف عن الطبائع ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الحوار والكشف عن الطبائع
Content:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_1]: - لَجَأَ الشَّاعِرُ إلى أسلوب الحوار في النص لِلْكَشْفِ عَنْ أَعْمَاقِ الشَّحْصِيَّات وتوجهاتها. وَضَحْ ذَلِكَ مِنَ النَّصِّ.
[LIST_ITEM_2]: - تمكن الشاعر من خلال إجراء الحوار بين الشيخ وابنته من الكشف عن طبيعة كل منهما؛ فعندما أنطق الفتاة بالقول: (ولكن المنازل يا أبي أطلال)، كشف عن نفسيتها المتشائمة، وأظهر اليأس الذي تسرب إلى نفسها. وعندما أنطق الشيخ بالقول: (تبنيها يدان) كشف عن نفسيته المتفائلة، وأظهر أن الأمل لم يزل يسري في كيانه.

=== BLOCK 5: الرمز ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Content: - اتكأ الشاعر على الرمز فِي نَصِّهِ، فَمَا الذي رَمَرَ إِليهِ كُلِّ مِن: (الجسر، النهر، الطريق)؟
ج - الجسر : طريق العودة . - النهر حاجز حدودي يحول دون تحقق حلم العودة. - الطريق العودة.

=== BLOCK 6: الصورة الفنية 1 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الصورة الفنية
Content:
- حلل الصورتين الآتيتين : (هِجْرَةُ الدَّم، القتل كالتدخين)، ثُمَّ اذْكُرُ وظيفةً مِنْ وَظَائِفِ كُلِّ مِنْهُما.
ج - الصورة (هجرة الدم).
- تَسْمِيَةُ الصورة: استعارة مكنية.
- تحليل الصورة: شبه الدم بكائن مهاجر، وحذف المشبه به وأبقى شيئًا من لوازمه وهو : "هجرة".
- تسمية الوظيفة الإيحاء.
- شرح الوظيفة أو توضيح الوظيفة : جَعَلَ الشَّاعِرُ الصورة موحِيَةً بتشبيهه الدم بكائن مهاجر، فهذا أوحى بالموت والقتل والخطر، وأثار مشاعر الخوف والحزن.

=== BLOCK 7: الصورة الفنية 2 ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content:
- الصورة: (القتل كالتدخين).
- تَسْمِيةُ الصورة: تشبيه مجمل
- تحليل الصورة: المشبه القتل المشبه به : التدخين. أداة التشبيه: الكاف. وجه الشبه : محذوف
- تَسْمِيةُ الوَظِيفة الشرح والتوضيح.
- شرح الوظيفة أو توضيح الوظيفة: شرحَتِ الصُّورَةُ وَوَضَحَتْ معنى: "إدمان الصهاينة على القتل والاستمتاع به من خلال تشبيه القتل بالتدخين، فأقنعت المتلقي بمضمون المعنى وصدقه.

=== BLOCK 8: الصور من المقطعين الثالث والرابع ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الصور من المقطعين الثالث والرابع
Content:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_1]: ه - اسْتَخْرِجُ مِنَ المَقْطَعَين الثَّالِثِ والرَّابِعِ صُورًا تُوَضَحُ الْمَعَانِي الْآتية:
[LIST_ITEM_2]: (عَدَمُ شَرْعِيَّةِ الوُجُودِ الصَّهْيَوِنِي فِي فَلِسْطِينَ - كَثْرَةُ القَتْلَى الفِلِسْطِينِيِّينَ الْحَالِمِينَ بِالعَوْدَةِ - تَعَاظُمُ حُلُمِ الْعَوْدَةِ).
[LIST_ITEM_3]: ج ه- عَدَمُ شَرْعِيَّةِ الوُجُودِ الصَّهْيَوَنِي فِي فِلِسْطِينَ : (لكن الجنود الطيبين الطالعين على فهارس دفتر قذفته أمعاء السنين).
[LIST_ITEM_4]: - كَفْرَةُ القَتْلَى الْفِلِسْطِييِّينَ الحَالِمِينَ بِالعَوْدَةِ : (النهر يبصق ضفتيه قطعا من اللحم المفتت).
[LIST_ITEM_5]: - تَعَاظُمُ حُلُمِ العَوْدَة:ِ (السعة الذكرى)، (طعم الحب حين يصير أكبر من عباده).

=== BLOCK 9: عاطفة الشيخ وابنته ===
(Component: TEMPLATE_C_BLOCK.html)
Title: عاطفة الشيخ وابنته
Content:
- تَبَبَّعْ عَاطِفَةً كُلِّ مِنَ الشَّيْخِ وَابْنَتِهِ مِنْ خِخلال الحوار الذي دارَ بَيْنَهُما، مُؤيِّدًا مَا تَذْهَبُ إِلَيهِ بِالشَّوَاهِدِ الْمُنَاسِبَة.ِ
(Component: TEMPLATE_C_TABLE.html)
[COL_1_HEADER]: الكلام
[COL_2_HEADER]: العاطفة
[COL_3_HEADER]: الشاهد
[ROW_1_COL_1]: ج ٦- كلام الشيخ :
[ROW_1_COL_2]: أظهر أنه يشعر بالتفاؤل والأمل
[ROW_1_COL_3]: - الشاهد قوله: (تبنيها يدان).
[ROW_2_COL_1]: کلام ابنة الشيخ :
[ROW_2_COL_2]: أظهر أنها تشعر باليأس والقنوط والتشاؤم.
[ROW_2_COL_3]: - الشاهد قولها (ولكن المنازل يا أبي أطلال).

=== BLOCK 10: مصادر الموسيقا الداخلية ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مصادر الموسيقا الداخلية
Content:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_1]: - مِنْ مَصَادِرِ الموسيقا الداخلية (تكرار الكلمات، تكرار الحروف). مَقِّلْ لِذَلِكَ مِنَ النَّص،ِ ثُمَّ اذْكُرُ مَصَادِرَ أُخْرَى أَعْنَتِ الإِيقَاعَ الْمُوسِيقِي.َّ
[LIST_ITEM_2]: ج- - تكرار الكلمات في المقطع الأول : (الطريق الطريق)، ( العائدين، عائدين)، (الجسر، الجسر)، (الحدود، الحدود). في المقطع الثاني: (الجِسْر،َ الجسر)، (الطلقة، الطلقة).
[LIST_ITEM_3]: - تكرار الحروف تكرار حرفي الحاء والدال في السطرين: (حرس الحدود مرابط / يحمي الحدود من الحنين).
[LIST_ITEM_4]: ومن مصادر الموسيقا التي أغنت الإيقاع الموسيقي:
[LIST_ITEM_5]: - تكرار الصيع الاشتقَاقِيَّةِ : المقطع الثاني: (تقتلوها، اقتلوني)، (يعلم، الحلم)، المقطع الثالث: (القتل، يقتلوا)..

=== BLOCK 11: المستوى الإبداعي ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
[BLOCK_TITLE]: المستوى الإبداعي:
[CONTENT]: المستوى الإبداعي:

--- END STREAM ---
