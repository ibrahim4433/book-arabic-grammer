# **SESSION 117**

[TASK DEFINITION]
Objective: Implement page 117.
File: `pages/page_117.html`
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
[LESSON_NUMBER]: 117
[CHAPTER_TITLE]: page 117
[CATEGORY_HEADER]: 117
[SECTION_HEADER]: 117
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: شرح المقطع الأول (Cut Content) ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[BLOCK_TITLE]: شرح المقطع الأول
[CONTENT]: وقد بدأت عودتهم قبل دخول الليل بقليل، لم يعرف هؤلاء الثلاثة المصير المجهول الذي يتربص بهم في طريق العودة، لم يعرفوا أن طريق العودة الطويل محفوف بالأخطار مترع بالأهوال فيه القتل، وكمائن الصهاينة ... كل من سبقهم إلى ركوب هذا الطريق واجه مصيرا فاجعا، فها هو النهر الذي يحاول هؤلاء العائدون اجتيازه يرمي في وجوههم جثثا فارقتها الحياة، فقد رست على ضفتيه أشلاء من سبقوهم إلى محاولة العودة. وقف الثلاثة عند جسر العبور الذي مازال غافلا عنهم غير متنبه لحضورهم، وهم يتخذون الظلام ستارا يمنع رؤيتهم. كانت نفوسهم تطفح بالشوق للعودة، وأحلام الوصول إلى المنزل تراود خواطرهم.
بدا الشيخ متيقنا من الوصول إلى بيته واثقًا من تفقد الماء فيه ليتوضأ، والبحث عن مفتاح بابه، عازما على قراءة القرآن فيه. قال الشيخ وهو مفعم بالتفاؤل: "يقطن المرء في حياته كثيراً من البيوت لكنه يبقى أبدًا مشتاقا متعلقا بأوّل منزل ترعرع فيه". قالت الفتاة وقد تسرب اليأس إلى نفسها: "لكن البيوت تحطمت ودُمِّرَتْ وصارت آثارا". فيجيب الشيخ محاولا طرد اليأس عنها: "ستبنى من جديد".
ما لم يكدِ الشَّيخ يُكْمِلُ التعبير عن آماله، ولم تكد الفتاة تنهي التعبير عن يأسها وشعورها بفقد منزلها وتحطمه، حتى يعلو صوت البنادق ليسكت كل أمل وكل يأس. يصرخ جنود الاحتلال بالعابرين: "تعالوا أَيُّهَا المتسللون"، ثم يتلو ذلك وابل من الرصاص معلنا منْعَ العائدين من المرور، مؤكدًا وقوف حرس الحدود لوقف عودة العائدين، مصرحًا بأن هذا الوقوف مسخر لاغتيال حنين العائدين.

=== BLOCK 3: شرح المقطع الثاني ===
(Component: TEMPLATE_C_BLOCK.html)
Title: شرح المقطع الثاني
Content: يأتي نداء من حرس الحدود: "لدينا أمر بإطلاق الرصاص على كل من يحاول اجتياز هذا الجسر، فعلى هذا الجسر ستكون غاية كل من تسول له نفسه التفكير بالعودة إلى الوطن". ثم يبدأ أزيز الرصاص مبددًا حجب الظلام، فتنغرز رصاصة في قلب الجندي القديم وترديه قتيلا، في حين راح الشيخ يمسك يد ابنته محاولا إبعادها عن رصاص الصهاينة. كان مُفْعَمًا بالإيمان يتلو في سره سورة من سور القرآن لتكون رقية وحجابا يحجزان عنهما رصاصات الغدر والعدوان. قال بلهجة تشبه الحلم: "أيها الجنود اقتلوني واتركوا ابنتي الصغيرة تحيا بعينيها الجميلتين، ووجهها الذي شابه لونه لون القمح".

=== BLOCK 4: شرح المقطع الثالث ===
(Component: TEMPLATE_C_BLOCK.html)
Title: شرح المقطع الثالث
Content: ومع أن القتل عند الصهاينة عادة ومزاج خاص كالتدخين يصعب عليهم التخلص منه، غير أن هؤلاء المغتصبين الذين فرضوا وجودهم في فلسطين دون وجه شرعي، لم يقتلوا الشيخ وابنته معًا، إنما قتلوا الشيخ وأبقوا الفتاة حية. لم يحققوا حلم الشيخ لطيبة جُبِلُوا عليها، بل لاطلاعهم على ما يعتمل في نفوس العائدين، ومعرفتهم أن الأب هو من يملك صنع القرار؛ فهو الذي يقود الفتاة إلى الضفة الأخرى. وبعد أن يغدو الشيخ جثة تغوص في مياه النهر تصبح الفتاة يتيمة، فتنتهك حرمتها ويدوس الجنود طهرها.

=== BLOCK 5: شرح المقطع الرابع ===
(Component: TEMPLATE_C_BLOCK.html)
Title: شرح المقطع الرابع
Content: بعد انتهاء محاولة العودة بهذه الفاجعة يعود الصمت ليخيم من جديد، ويعود النهر من جديد يرمي في وجوه العائدين جُتَنا فارقتها الحياة، فقد رَسَتْ على ضفتيه أشلاء من حاولوا العودة، أولئك الذين لم يعرفوا أن طريق العودة محفوف بالأخطار مترع بالأهوال؛ ففيه القتل وكمائن الصهاينة.

=== BLOCK 6: جرائم العبور ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: جرائم العبور
Content: كذلك لا يعرف أحد شيئا عن تلك الجرائم البشعة التي ترتكب بحق من أراد عبور هذا النهر. إن هذا الجسر صار طريقا يزداد امتدادا وطولا وصعوبة يوما بعد يوم، طريقا محفوفًا بالمخاطر والموت مفروشا باللحم المفتت من جثث الذين حاولوا العودة. أولئك الذين ضربوا بإصرارهم على العودة أروع الأمثلة، فغدوا رموزا مشعة كالنجوم. لقد أثبتوا بإصرارهم على العودة أن حبهم لوطنهم قد تعاظم حتى بلغ مدى تجاوز حدود العبادة.

=== BLOCK 7: مهارات الاستماع ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مهارات الاستماع
Content: مهارات الاستماع :

=== BLOCK 8: مهارات الاستماع - الأسئلة ===
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: - ما القَضِيَّةُ التِي يَعْرِضُها النَّصُّ؟ ج -۱ حلم المهجرين الفلسطينيين بالعودة إلى ديارهم.
[LIST_ITEM_CONTENT]: - حَدِدْ طَرَفَي الصراع في النص. ج -۲ الطرف الأول: المهجرون من أبناء فلسطين، المتمثلون بالشيخ وابنته والجندي القديم. الطرف الثاني: الجنود الصهاينة المحتلون.

=== BLOCK 9: مهارات القراءة ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مهارات القراءة
Content: مهارات القراءة :

=== BLOCK 10: مهارات القراءة - الأسئلة ===
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: - عَدِّدْ شَخْصِيَّاتِ القِصَّةِ الشَّعْرِيَّة.ِ ج -۱ الشيخ، وابنته، والجندي القديم، والجنود الصهاينة.

--- END STREAM ---
