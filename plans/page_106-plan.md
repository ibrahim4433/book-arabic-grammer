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
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
15. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !

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

=== BLOCK 2: [التحليل] ===
(Component: TEMPLATE_CUT_BOX_PART_2.html wrapping TEMPLATE_C_BLOCK.html)
Title: تتمة التحليل
Content:
- أ.
معنى: الأول قد اشتمل على وَنَقْلِها إلى المتلقي، نجد المقطع بقدرتها على عَرْضِ أفكار الشَّاعِرِ ومن جهة المعاني ووظيفتها المتمثلة
بدماء أجلها تعطر تراب سورية إلى ربوعنا بمهر غال نفيس، فمن مزهوة بنفسها؛ لأنها جلبت دعوة الشاعر الحرية لأن تفخر وتختال كعروس
العربي الساعي إلى نشر نور إظهار الجوانب الإيجابية التي رافقت فتوحات الإنسان الشهداء الأبرار، واشتمل المقطع الثاني على معنى:
العربي إلى نشرها. كما الرسالة الإنسانية التي سعى الإنسان الدنيا وتمايلت فرحا وارتياحا لهذه الهداية والرشاد في كل الأنحاء. فقد اهتزت
به الشباب السُّورِي مِن مَهَمَّاتٍ بها. وتضمن المقطع الثالث معنى: إبراز ما قام أنها تغنت بمحاسن الأخلاق وجميل العادات التي تحلى
أسلحة المستعمر ولم يرضوا به، وإنما حولوه إلى قوة تحدت التضحيات، ولم يستسلموا للضعف جليلة في سبيل نَيْل الاستقلال؛ حيث بذلوا
بأنفسهم. وأصروا أن يحموا تراب بلادهم والانتداب التي نادى بها المستعمر، الفتاكة. كما رفضوا أشكال الوصاية والحماية
اتسمَتْ بالترابط والتسلسل، فقد جاءت عليها الأبيات، نَجِدُ أَنَّ هذه المعاني قد وفيما يتصل بشأن سِمَاتِ المعاني التي اشتملت
بينها. متعاقبة، متوافقة، منسجمةً فيما

=== BLOCK 3: [الوسائل التعبيرية والفنية] ===
(Component: TEMPLATE_C_BLOCK.html)
Title: <span class="text-accent">الوسائل التعبيرية والفنية</span>
Content:
التعبيرية، بني الشاعر نصهُ التعبيرية والفنية فمن جهة الوسائل معانيه الفكرية ببعض الوسائل وقد استعان الشاعر على إيصال
بِالدِّقَةِ اللفظية، فقد استعان بألفاظ اتَّسَمَتْ له هذا البناء، جاءت في الطليعة منها الصياغة بناء فنيا معتمدا على أدوات تعبيرية أقامت
بعضها بالقوة والجزالة. والرشاقة، في حين انصف ذلك أن بعضها قد امتاز بالليونة التعبيرية والانسجام، وقد بدا التنوع جليًّا فيها؛

=== BLOCK 4: [المحسنات والصور] ===
(Component: TEMPLATE_C_TABLE.html)
Headers: الأداة | الشاهد والتوضيح
Row 1: <span class="highlight-blue">التصريع</span> | المعنى، وإبراز البديعية اللفظيَّة، هادفًا من ذلك إلى توضيح قد استعان في بناء نصه بالمحسنات ومن جهة الوسائل الفنية نجد الشاعر موسيقي لافت للسَّمْع في البيت اسْحَبِي الشَّهْبِ مَكُنَ الشَّاعِرَ من إشاعة إيقاع الشعور، وتحسين الإيقاع الموسيقي، فمحسن التصريع: موسيقيا جميلا. البيت رونقًا وعذوبة، ومنحه إيقاعا الذي حل فيه، فقد أضفى على هذا
Row 2: <span class="highlight-blue">طباق الإيجاب</span> | رمى إليها، طالبا من ذلك إصابة مقاصد المحسنات البديعية المعنوية جماليا من استثمار طاقات كما أفاد الشاعر في بناء نصه بناء فنيا بين الضعف والقوة. التناقض وإدراك الفرق الشاسع فنية كثيرة من بينها إبراز الحصول على قيم فطباق الإيجاب: )ضَعف، قوة(، مكنه من
Row 3: <span class="highlight-blue">التشخيص</span> | عبثيًا وإنما جاء لخدمة المضمون الفكري بالصور الشعرية التي لم يكن استعمالها أما من جهة الأسلوب التصويري، فالنص يطْفَحُ فنية، فقد أكثر الشاعر في صورهِ مِنَ التشخيص لتؤدي وظائف معنوية، وتقدم لبناء النص قيمة فالشاعر بدا متمكنا حينما وظف هذه الصور الصورة التي أسهمت في تقريب المعنى وتوضيحه، يزيد المعنى وضوحا وجلاء. ومن الصور طلبا لإيضاح المعاني التي قَصَدَ إليها، فالتشخيص المتلقي بصدق معناها. معنى ثبات الحق في وجه المغتصب فأقنعت الحق لطمت عارضيه قبضة المغتصب فقد أوضحت

=== BLOCK 5: [المستوى التركيبي والتعاضد] ===
(Component: TEMPLATE_C_BLOCK.html)
Title: <span class="text-accent">المستوى التركيبي والتعاضد</span>
Content:
مِنَ جسرا يوصل من خلاله أفكاره إلى المتلقي؛ حيث أفادَ كما وظف الشاعر بعضا من عناصر المستوى التركيبي وجندها لتكون
العربي، وبذلك بدا الإنسان العربي على الصفات الثابتة المستقرة الدائمة في الإنسان الصَّفَتَين المُشَبَّهَتَين باسم الفاعل )حر، أبي( في الدلالة
حرا أبيا على الدوام.
واضحا، أمن لأبياته محتوى معنويا متوافقا منسجما والفني في إبراز مقولة الشاعر الذي وما سبق يظهر جليا تعاضد المستويين الفكري
كما نهل من مصادر الأدبي لاستمالها على ما تقبله النفس. تلك المعاني التي اسمت بالصدق نقل من خلاله أفكارة ومعانيه إلى المتلقي،
عنده. فباعْتَمَادِهِ الوسائل قريبة من نفس المتلقي متقبلةً نصه بداء فتيا عاليًا جَعَلَ أَفكاره ومعانيه الإبداع الأدبي، ومشاربه المختلفة؛ ليبني
بذلك كله من إيضاح المعاني، نقل الحقيقة إلى الخيال فتمكن الأساليب البلاغية الجمال، وباستثماره التعبيرية والموسيقية البس النص ثوب
وتجلية المشاعر الجيَّاشَة،ِ وإثارة الخيال.
مر

=== BLOCK 6: [تدريب] ===
(Component: TEMPLATE_C_BENEFIT.html)
Title: إضاءة على النص
Content:
الإجابة عاش أبناء سورية مرحلة شاقة من مراحل النضال إبان احتلال الفرنسيين أرض سورية الحبيبة، امتدت خمسة وعشرين عاما، بذلوا فيها كل طاقاتهم، وسخروا لها كل إمكاناتهم،
واحدة لمنع المستعمر من بلوغ ماربه. فكانت المعركة مع الاستعمار الفرنسي من أهم معارك
التضال الوطني التي خاضها شعبنا في سبيل الحصول على الاستقلال والتحرر بالتخلص من نير الاستعمار الفرنسي.
فالجلاء ثمرة لكفاح ؛ كتب سطورها أبناؤها الأباة بدمائهم. مجيد، وصفحة مشرقة في تاريخ سورية إنَّ يوم السابع عشر من نيسان يوم
تحت أقدام الفرنسيين بثورات سورية. فقد زلزل السوريون الأرض وطات أقدام المستعمرين أرض خاضه الشعب العربي في سورية منذ
حيث الأرض، وسلب الكرامة. الخبيثة التي يروم من ورائها تدنيس الوطن، أنست المحتل الطامع أطماعه لاهبة حارقة عمت كل منطقة من ربوع
الإنسان. بحممها المنصهرة الأرض ويحرر بقذائف النار الملتهبة ليظهر يرمي الطامعين الغادرين تحولت كل بقعة من بقاع سورية إلى مدفع هادر
-  -  اسکندرون

=== BLOCK 7: [التقويم النهائي] ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: اكتُبْ مَقَالَةً تَتَحَدَّثُ فِيهَا عَنْ جَلاء الْمُسْتَعْمِرِ الْفِرَنْسِي عَنْ سورية، وما يَتَضَمْنُهُ مِنْ مَعَانٍ وَقِيَمٍ سامية، مُبَيِّنَا العوامل التي أَسْهَمَتْ فِي تَحْقِيقِه.ِ

--- END STREAM ---
