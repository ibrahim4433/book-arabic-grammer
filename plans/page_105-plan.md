# **SESSION 105**

[TASK DEFINITION]
Objective: Implement page 105.
File: `pages/page_105.html` (Note: Use the exact page number.)
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
[LESSON_NUMBER]: 105
[CHAPTER_TITLE]: page 105
[CATEGORY_HEADER]: 105
[SECTION_HEADER]: 105
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: الأفكار (تتمة) ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
Mapping: `TEMPLATE_C_BLOCK.html` (Standard Block)
Title: الأفكار
Content:
الأول فكرة : .......... وتضمن البيت الثاني فكرة: واشتمل البيت الثالث على فكرة ....
البيت الرابع فكانَت:ْ
أما فكرة

=== BLOCK 3: المعاني ووظيفتها وسماتها ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المعاني
Content:
<span class="text-accent">ومن جهة المعاني ووظيفتها المتمثلة بقدرتها على عرض أفكار الشَّاعِرِ وَنَفْلِها إلى المتلقي، نجد البيت الأول قد اشتمل
البيت الثالث معنى: أما البيت الرابع، على معنى ........، واشتمل البيت الثاني على معنى: وتضمن
فاشتمل على معنى.</span>
وفيما يتصل بشأن سمات المعاني التي اشتملت عليها الأبيات، نَجِدُ أَنَّ هذهِ الْمَعَانِي قد اتسمَتْ بالترابط والتسلسل، فقد
جاءَتْ مُتَعاقبة، متوافقة، منسجمة فيما بينها .

=== BLOCK 4: الوسائل التعبيرية ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الوسائل التعبيرية
Class: `.block-header accent`
Content:
وقد استعان الشاعر على إيصال معانيه الفكرية ببعض الوسائل التعبيرية والفنية فمن جهة الوسائل التعبيرية، بني الشاعر
نصة بناء فنيا معتمدا على أدوات تعبيرية أقامت له هذا البناء، جاءت في الطليعة منها الصياغة اللفظية، فقد استعان بألفاظ
انسمَتْ بالدقة التعبيرية والانسجام، وقد بدا التنوع جليًّا فيها؛ ذلك أن بعضها قد امتاز بالليونة والرشاقة، في حين انصف بعضها
بالقوة والجزالة.

=== BLOCK 5: الوسائل الفنية (المحسنات البديعية) ===
(Component: TEMPLATE_C_SPLIT.html)
Title: الوسائل الفنية
Left Content:
ومِن جهة الوسائل الفنية نجد الشاعر قد استعان في بناء نصه بالمحسنات البديعية المعنوية طالبا من ذلك إصابة مقاصد
رمى إليها، فطباق الإيجاب: ،(.......... أو طباق السلب: (.........) مكنه من الحصول على قيم فنية كثيرة من بينها
إبراز التناقض وإدراك الفرق التاسع بين الـ .
Right Content:
كما أفاد الشاعر في بناء نصه بناء فنيا جماليا من استثمار طاقات المحسنات البديعية اللفظية، هادفا من ذلك إلى
توضيح المعنى، وإبراز الشعور، وتحسين الإيقاع الموسيقي، فمُحسّنُ الجناسِ الناقص : (...........) مَكَّنَ الشَّاعِرَ مِن إِشَاعَةِ
إيقاع موسيقي لافت للسمع في البيت الذي حل فيه؛ فقد أضفى على هذا البيت رونقا وعذوبة، ومنحه إيقاعا موسيقيا جميلا.
كما أن محسن التصريع : (...........) بدوره أضفى على النص إيقاعا موسيقيا جميلا.

=== BLOCK 6: الأساليب والمستويات ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الأساليب
Content:
ويبدو أن الشاعر قد زاوح بين أسلوب الخبر وأسلوب الإنشاء في نصه، فأضفى هذا النوع جمالا فنيا على النص، ذلك
أَنَّ التنويع بين الإنشاء والخبر يُعد مصدرا من مصادر الجمال الأدبي. ومن أساليب الخبر في النص الخبر الابتدائي .........
الذي عكس ...... والخبر الطلبية (........ الذي أكد ......... ومن أساليب الإنشاء في النص ........) الذي أبرز
أما من جهة الأسلوب التصويري، فالنَّ يُطْفَحُ بالصور الشعرية التي لم يكن استعمالها عبثيًا وإنما جاء الخدمة المضمون
الفكري فالشاعر بدا متمكنا حينما وظف هذه الصور لتؤدي وظائف معنوية، وتقدم لبناء النص قيمة فنية، فقد أكثر الشاعر في
صورهِ مِنَ التشخيص طلبا لإيضاح المعاني التي قَصَدَ إليها، فالتشخيص يزيد المعنى وضوحًا وجلاء. ومن الصور التي أسهمت في
تقريب المعنى وتوضيحه الصورة (.............. قد أوضحت معنى فأقنعت المتلقي بصدق معناها.
كما وظف الشاعر بعضا من عناصر المستوى التركيبي وجندها لتكون جسرًا يوصل من خلاله أفكاره إلى المتلقي؛ حيث
أفاد من الجملة الاسمية (.............) في الدلالة على ثبات واستقراره وديمومته. وأفاد من الفعل الماضي
.............. في الدلالة على تأكيد تحقق .......... ونفي الشك في حدوثه. وأفاد من الفعل المضارع .............في.
الدلالة على تجدد واستمراره.
وما سبق يظهر جليًّا تعاضد المستويين الفكري والفني في إبراز مقولة الشاعر الذي أمن لأبياته محتوى معنويا متوافقا منسجما
واضحا، نقل من خلاله أفكاره ومعانيه إلى المتلقي، تلك المعاني التي اتسمت بالصدق الأدبي لاشتمالها على ما تقبلهُ النَّفْس.ُ كما
نهل من مصادر الإبداع الأدبي، ومشاربه المختلفة؛ ليبني نصه بناء فتيا عاليًا جعل أفكاره ومعانيه قريبة من نفس المتلقي متقبلة
عنده. فباعْتَمَادِهِ الوسائل التعبيرية البس النَّص ثوب الجمال، وباستثمار الأساليب البلاغية نقل الحقيقة إلى الخيال، فتمكن بذلك
كله من إيضاح المعاني، وتجلية المشاعر الجياشة، وإثارة الخيال.

=== BLOCK 7: خلاصة الأفكار الرئيسية (Summary Table) ===
(Component: TEMPLATE_C_TABLE.html)
Title: الإجابة والفِكَر الرئيسة
Intro Text:
الإجابة : خَرَجَ الشعب السوري على الاحتلال الفرنسي مُشْعِلَا التَّوْرات في كل مكان إلى أنْ سَطَّرَ بِدِمَائِهِ يَوْمَ الجلاء العظيم. وقد أرخ
الشَّاعِرُ عُمر أبو ريشة لانتصارات بَلَدِهِ بِحُرُوفِ مِنْ نُور،ٍ حيثُ صَوَّرَ فَرْحَة الانتصار بجلاء المُحْتَلِ عَنْ أَرْضِ الوَطَن،ِ وَأَشَادَ بِتَصْحِيات
السوريين العظيمة في يوم الجلاء. وقد جَعَلَ الشَّاعر أبو ريشة التغني والاعتزاز بمنجز الجلاء، والإشادة بالتضحيات التي صنعته فكرة عامة
لنصه الذي قَسَمَهُ إِلى ثلاثِ فِكر رئيسة،
Table Content:
Row 1: فقد تضمن المقطع الأول فكرة التعبير عَنِ الفَرَح بتحقيق الجلاء والإشادة بالتضحيات التي أَنجَزَتْه.ُ
Row 2: وتضمن المقطع الثاني فكرة الاعتزاز بالماضي المجيد.
Row 3: واشتمل المقطع الثالث على فكرة: بيان ما قدمه أبناء سورية لنيل الاستقلال.

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: -  -
Number: ٢
Question: .  -

--- END STREAM ---
