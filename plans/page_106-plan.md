# **SESSION 106**

[TASK DEFINITION]
Objective: Implement page 106.
File: `pages/page_106.html` (Note: Use the exact page number.)
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
[LESSON_NUMBER]: 106
[CHAPTER_TITLE]: page 106
[CATEGORY_HEADER]: 106
[SECTION_HEADER]: 106
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Cut Box Part 2 ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[UNIQUE_ID]: b39820
[BLOCK_TITLE]: الاستيعاب والفهم
[CONTENT]:
<p class="text-accent mb-2mm">
ومن جهة المعاني ووظيفتها المتمثلة بقدرتها على عَرْضِ أفكار الشَّاعِرِ وَنَقْلِها إلى المتلقي، نجد المقطع الأول قد اشتمل على معنى: دعوة الشاعر الحرية لأن تفخر وتختال كعروس مزهوة بنفسها؛ لأنها جلبت إلى ربوعنا بمهر غال نفيس، فمن أجلها تعطر تراب سورية بدماء الشهداء الأبرار، واشتمل المقطع الثاني على معنى: إظهار الجوانب الإيجابية التي رافقت فتوحات الإنسان العربي الساعي إلى نشر نور الهداية والرشاد في كل الأنحاء. فقد اهتزت الدنيا وتمايلت فرحا وارتياحا لهذه الرسالة الإنسانية التي سعى الإنسان العربي إلى نشرها. كما أنها تغنت بمحاسن الأخلاق وجميل العادات التي تحلى بها. وتضمن المقطع الثالث معنى: إبراز ما قام به الشباب السُّورِي مِن مَهَمَّاتٍ جليلة في سبيل نَيْل الاستقلال؛ حيث بذلوا التضحيات، ولم يستسلموا للضعف ولم يرضوا به، وإنما حولوه إلى قوة تحدت أسلحة المستعمر الفتاكة. كما رفضوا أشكال الوصاية والحماية والانتداب التي نادى بها المستعمر، وأصروا أن يحموا تراب بلادهم بأنفسهم.
</p>
<p class="m-0">
وفيما يتصل بشأن سِمَاتِ المعاني التي اشتملت عليها الأبيات، نَجِدُ أَنَّ هذه المعاني قد اتسمَتْ بالترابط والتسلسل، فقد جاءت متعاقبة، متوافقة، منسجمةً فيما بينها.
</p>
<p class="m-0 mt-2mm">
وقد استعان الشاعر على إيصال معانيه الفكرية ببعض الوسائل التعبيرية والفنية فمن جهة الوسائل التعبيرية، بني الشاعر نصهُ بناء فنيا معتمدا على أدوات تعبيرية أقامت له هذا البناء، جاءت في الطليعة منها الصياغة بِالدِّقَةِ اللفظية، فقد استعان بألفاظ اتَّسَمَتْ التعبيرية والانسجام، وقد بدا التنوع جليًّا فيها؛ ذلك أن بعضها قد امتاز بالليونة والرشاقة، في حين اتصف بعضها بالقوة والجزالة.
</p>
<p class="m-0 mt-2mm">
ومن جهة الوسائل الفنية نجد الشاعر قد استعان في بناء نصه بالمحسنات البديعية اللفظيَّة، هادفًا من ذلك إلى توضيح المعنى، وإبراز الشعور، وتحسين الإيقاع الموسيقي، فمحسن التصريع: اسْحَبِي الشَّهْبِ مَكُنَ الشَّاعِرَ من إشاعة إيقاع موسيقي لافت للسَّمْع في البيت الذي حل فيه، فقد أضفى على هذا البيت رونقًا وعذوبة، ومنحه إيقاعا موسيقيا جميلا.
</p>

=== BLOCK 3: Split Analysis ===
(Component: TEMPLATE_C_SPLIT.html)
[UNIQUE_ID]: b52537
[COL_1_CONTENT]:
<div class="block-body p-2mm">
    <p class="m-0 font-bold mb-2mm text-center">المحسنات المعنوية</p>
    <p class="m-0">
كما أفاد الشاعر في بناء نصه بناء فنيا جماليا من استثمار طاقات المحسنات البديعية المعنوية طالبا من ذلك إصابة مقاصد رمى إليها، فطباق الإيجاب: )<span class="highlight-blue">ضَعف</span>، <span class="highlight-red">قوة</span>(، مكنه من الحصول على قيم فنية كثيرة من بينها إبراز التناقض وإدراك الفرق الشاسع بين الضعف والقوة.
    </p>
</div>
[COL_2_CONTENT]:
<div class="block-body p-2mm">
    <p class="m-0 font-bold mb-2mm text-center">الأسلوب التصويري</p>
    <p class="m-0">
أما من جهة الأسلوب التصويري، فالنص يطْفَحُ بالصور الشعرية التي لم يكن استعمالها عبثيًا وإنما جاء لخدمة المضمون الفكري فالشاعر بدا متمكنا حينما وظف هذه الصور لتؤدي وظائف معنوية، وتقدم لبناء النص قيمة فنية، فقد أكثر الشاعر في صورهِ مِنَ التشخيص طلبا لإيضاح المعاني التي قَصَدَ إليها، فالتشخيص يزيد المعنى وضوحا وجلاء.
    </p>
</div>

=== BLOCK 4: Standard Block ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b87149
[BLOCK_TITLE]: تحليل الصور والتراكيب
[CONTENT]:
<p class="m-0">
ومن الصور الصورة التي أسهمت في تقريب المعنى وتوضيحه، <span class="highlight-red">الحق لطمت عارضيه قبضة المغتصب</span> فقد أوضحت معنى ثبات الحق في وجه المغتصب فأقنعت المتلقي بصدق معناها.
</p>
<p class="m-0 mt-2mm">
كما وظف الشاعر بعضا من عناصر المستوى التركيبي وجندها لتكون جسرا يوصل من خلاله أفكاره إلى المتلقي؛ حيث أفادَ مِنَ الصَّفَتَين المُشَبَّهَتَين باسم الفاعل )<span class="highlight-blue">حر</span>، <span class="highlight-blue">أبي</span>( في الدلالة على الصفات الثابتة المستقرة الدائمة في الإنسان العربي، وبذلك بدا الإنسان العربي حرا أبيا على الدوام.
</p>

=== BLOCK 5: Core Summary Matrix ===
(Component: TEMPLATE_C_TABLE.html)
[UNIQUE_ID]: b11984
[BLOCK_TITLE]: خلاصة المستويات الفنية والفكرية
[TABLE_CONTENT]:
<table class="dense-table">
    <thead>
        <tr>
            <th>المستوى</th>
            <th>الوظيفة والسمات</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>الفكري</td>
            <td>المعاني اتسمت بالصدق الأدبي لاستمالها على ما تقبله النفس، أفكاره قريبة من نفس المتلقي.</td>
        </tr>
        <tr>
            <td>الفني</td>
            <td>باعتماده الوسائل التعبيرية والموسيقية ألبس النص ثوب الجمال، وباستثماره الأساليب البلاغية نقل الحقيقة إلى الخيال.</td>
        </tr>
    </tbody>
</table>

=== BLOCK 6: Benefit Note (Orange) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[UNIQUE_ID]: b93972
[CONTENT]:
وما سبق يظهر جليا تعاضد المستويين الفكري والفني في إبراز مقولة الشاعر الذي أمن لأبياته محتوى معنويا متوافقا منسجما واضحا، نقل من خلاله أفكاره ومعانيه إلى المتلقي. كما نهل من مصادر الإبداع الأدبي، ومشاربه المختلفة؛ ليبني نصه بناء فنيا عاليًا جَعَلَ أَفكاره ومعانيه متقبلةً عنده، فتمكن بذلك كله من إيضاح المعاني، وتجلية المشاعر الجيَّاشَة،ِ وإثارة الخيال.
- أ. - مر - اسکندرون

=== BLOCK 7: Exam Solved ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b71812
[QUESTION_NUMBER]: ١
[QUESTION_TEXT]: اكتُبْ مَقَالَةً تَتَحَدَّثُ فِيهَا عَنْ جَلاء الْمُسْتَعْمِرِ الْفِرَنْسِي عَنْ سورية، وما يَتَضَمْنُهُ مِنْ مَعَانٍ وَقِيَمٍ سامية، مُبَيِّنَا العوامل التي أَسْهَمَتْ فِي تَحْقِيقِه.ِ
[ANSWER_TEXT]: عاش أبناء سورية مرحلة شاقة من مراحل النضال إبان احتلال الفرنسيين أرض سورية الحبيبة، امتدت خمسة وعشرين عاما، بذلوا فيها كل طاقاتهم، وسخروا لها كل إمكاناتهم، لمنع المستعمر من بلوغ ماربه. فكانت المعركة مع الاستعمار الفرنسي واحدة من أهم معارك النضال الوطني التي خاضها شعبنا في سبيل الحصول على الاستقلال والتحرر بالتخلص من نير الاستعمار الفرنسي. إنَّ يوم السابع عشر من نيسان يوم مجيد، وصفحة مشرقة في تاريخ سورية؛ كتب سطورها أبناؤها الأباة بدمائهم. فالجلاء ثمرة لكفاح خاضه الشعب العربي في سورية منذ وطات أقدام المستعمرين أرض سورية. فقد زلزل السوريون الأرض تحت أقدام الفرنسيين بثورات لاهبة حارقة عمت كل منطقة من ربوع الوطن، أنست المحتل الطامع أطماعه الخبيثة التي يروم من ورائها تدنيس الأرض، وسلب الكرامة. حيث تحولت كل بقعة من بقاع سورية إلى مدفع هادر يرمي الطامعين الغادرين بقذائف النار الملتهبة ليطهر الأرض ويحرر بحممها المنصهرة الإنسان.

--- END STREAM ---
