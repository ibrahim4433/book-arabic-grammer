# **SESSION 136**

[TASK DEFINITION]
Objective: Implement page 136.
File: `pages/page_136.html` (Note: Use the exact page number.)
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
[UNIQUE_ID]: b53906
[LESSON_NUMBER]: 136
[CHAPTER_TITLE]: page 136
[CATEGORY_HEADER]: 136
[SECTION_HEADER]: 136
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: الاستيعاب والفهم ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[UNIQUE_ID]: b97819
[BLOCK_TITLE]: الموضوع المقترح
[CONTENT]: غَدًا سَنَعُودُ وَالأَجْيَالُ تُصْفِي إلى وَقْعِ الخطا عِنْدَ الْإِيَابِ
ولا يغرب عن مخيلة الإنسان العربي أن الأمة العربية وقَعَتْ فريسة بين مخالب الدول الاستعمارية الغربية التي اندفعت نحو
ربوع بلادنا كالوحوش الضارية الفاتكة متَّخِدَةً شعارات الوصاية والحماية والانتداب أقنعة تغطي بها مارتها الدنيئة. لكن الخديعة لم
تنطل على أبناء الأمة الذين هبوا في وجه الدخلاءِ فِي غَضْبَةٍ عَارِمَةٍ وثورة لاهبة متسلحين بالإباء وعشق الحرية.

=== BLOCK 3: الأدب والكفاح ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b44855
Title: دور الأدب في مسيرة الكفاح
Content: ولأن الأدب من مطواع مستجيب لكل ظرف يعصف بالأمة واكب مسيرة الكفاح والنضال فشحن النفوس بروح الثورة
لتحرير الأمة المسْتَعْبَدَة وتوحيد الوطن الممزق، فقد قام الأدباء العرب باستنكار خداع الفرنسيين الشعوب العربية، فلم يخف على
الأدباء زيف ادعاءات المستعمر الغربي فأقدموا على كشف وعوده البراقة الكاذبة وفضح أساليبه الملتوية التي يَبْغِي مِنْ وَرَائِهَا جَعُلَ
البلاد العَرَبِيَّة لقمَةً سَائِغَة،َ وَمَطْمَعًا مَرِينًا ، لِيَتَمَكْنَ مِنْ احتلالِ الأَرْضِ واستعباد الإنسان. فالشَّاعِرُ خَيْرُ الدِّينِ الزِرَكْلِي يُؤْكِدُ أَنَّ
المستعمر أعلن أنَّهُ جَاءَ لِيقِفَ إلى جانب الأقطَارِ العَرَبِيَّةِ ويأخُذَ بِيَدِهَا لِتَنهَضَ وَتَتَحَرَّرَ من الجهل والتخلف، ويزرع العدالة والمساواة
بَيْنَ أَبِنَائِهَا وَيَجْعَلَهُم يَنْعَمُونَ بِالْحَرِّيَّة، لَكِنَّهُ مَا إِنْ وَضَعَ أقدامه على الأرض العربية كشر عن أنياب الشر والغدر والخيانة، فتنكر لوعوده،
وتجاهل المواثيق التي قطعها للعرب. فاستعمر البلاد وعاث فسادا في ربوع الأمة العربية، التي قدمت للعالم أزهى الحضارات وأعرفها،
حيث أضمر لها الغدر والخديعة وارْتَكَبَ بحقِّهَا أَفع الجرائم. يقول:

=== BLOCK 4: الشواهد الشعرية ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b18854
[UNIQUE_ID_BIO]: b15900
[POEM_TITLE]: الشاهد الشعري
[POET_NAME]: خير الدين الزركلي
[RIGHT_HEMISTICH]: جَهَرُوا بِتَحْرِيرِ الشَّعُوبِ وَأَثْقَلَتْ
[LEFT_HEMISTICH]: مَثْنَ الشَّعُوبِ سَلَاسِلٌ وَقُيُودُ
[RIGHT_HEMISTICH_2]: خَدَعُوكِ يَا أُمَّ الْحَضَارَةِ فَارِتَمَتْ
[LEFT_HEMISTICH_2]: تَجْنِي عَلَيْكِ فَيَالِقٌ وَجُنُودُ

=== BLOCK 5: بطولات الأمة ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b66159
Title: تضحيات المشرفة التي حققت الجلاء
Content: ونظرا لكثرة المواجهات الدَّامِيَة،ِ والمعارك الضارية التي خاصها أبناء الأمَّةِ العربية، وهم يتصدون للمستعمرين العراةِ الطَّامِعين،
المعت بطولات لأبطال سطروا أروع ملاحم الفداء والتضحية؛ فلم يبخل أبناء الأمة العربية خلال كفاحهم المتواصل بالدم، فقدموا
قوافل الشهداء الذينَ صَارُوا وَسَامَ شرف وقلادة ترصعانِ صَدْرَ الأمة العربية. وأمام هذا العَطَاءِ الفياض والبذلِ السَّخِيِّ جَادَتْ أَقلامُ
الأدباء بتمجيد التضحيات المشرفَةِ التِي حَقَقَتِ الخلاء؛ فما أروع التضحيات التي بدنها أبناء سورية لتحقيق مُنْجَزِ الجلاء حيث
استعدبُوا الموت وأرخصوا دماءهم في سبيل حرية الوطن، فقروا أقوالهم بأفعالهم، وجعلوا أجسادَهُم حِمَمًا تُلْهِبُ ظهور المستعمرين
وتحرِقُ جباه الطَّغَاةِ الظَّالمين. فالشاعر عمر أبو ريشة يؤكد للحرية أنها ما جلبت إلى ربوع سورية بمهر بحس، وإنما جُلِيت بأغلى الأمان
وأنفسها، فكل حبة من تراب الوطنِ تَعَطَّرَتْ بِدَمَ شَهِيْدٍ بَطَل،ِ رَفَضَ الدُّلَّ والخضُوع،َ وقَدَّمَ روحهُ رَخِيْصَةَ على مَذْبَحِ الخَرَيَّةِ يَقُول:ُ

=== BLOCK 6: الشواهد الشعرية 2 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b71433
[UNIQUE_ID_BIO]: b00031
[POEM_TITLE]: الشاهد الشعري
[POET_NAME]: عمر أبو ريشة
[RIGHT_HEMISTICH]: لَنْ تَرَيْ حَفْنَةَ رَمْلِ فَوْقَهَا
[LEFT_HEMISTICH]: لَمْ تُعَطَرْ بِدِمَا حُرَ أَبِي

=== BLOCK 7: الأدب العربي منبرا ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[UNIQUE_ID]: b33295
[TITLE]: الفكرة
[CONTENT]: وهكذا كانَ الأَدَبُ العَرَبِيُّ مِنْبَرًا يَفْضَحُ عن إصرار الفلسطيني المهر على العودة إلى أَرْضِ الوَطَنِ الحَبيب؛ وكانَ مِرْآةً صَافِيَةً انعكست على صفحتها المشرِقَةِ أَكَاذِيبُ الْمُسْتَعْمِرِينَ ووعُودُهُم الزَّائِفَة،ُ وكان الصوت المجلجل الذي صَدَحَ مُتَغَنِّيَا بِتَضْحِيَاتِ الشُّهَدَاءِ العِظَامِ الذين قَدَّمُوا أَرْوَاحَهُم بِسَخَاءٍ لِتَنعم الأُمَّةُ بالحرَيَّةِ والكرامة.

=== BLOCK 8: The Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
[UNIQUE_ID]: b96570
[HEADER_1]: الموضوع المقترح المكتوب الثالث
[HEADER_2]: الفكرة
[HEADER_3]: الشاهد
[CELL_1]: أَوْلَى الْأَدْدَبَاءُ العَرَبُ فِي العَصْرِ الحَدِيثِ القضايا الوَطَبَيَّةَ والقَوْمِيَّةَ اهْتِمَامًا كَبِيرًا
[CELL_2]: فَعَبُرُوا عَنْ مَشَاعِرِ الْفَرَحِ وَالرَّهِوَ بِنَصْرِ تشرين
[CELL_3]: -

=== BLOCK 9: موضوع مقترح (امتحان مع إجابة) ===
(Component: TEMPLATE_CUT_EXAM_SOLVED_PART_1.html)
[UNIQUE_ID]: b17034
[QUESTION_NUMBER]: ١
[QUESTION_TEXT]: الموضوع المقترح المكتوب الثالث: قيل: )أَوْلَى الْأَدْدَبَاءُ العَرَبُ فِي العَصْرِ الحَدِيثِ القضايا الوَطَبَيَّةَ والقَوْمِيَّةَ اهْتِمَامًا كَبِيرًا، فَعَبُرُوا عَنْ مَشَاعِرِ الْفَرَحِ وَالرَّهِوَ بِنَصْرِ تشرين، وأَكْدُوا تَمَسُّكَ المَهَجْرِينَ الفلسطينيين بِالأَمَلِ وَتَطَلْعَهُم إلى العَوْدَة،َ فَاضِحِينَ مُمَا رَسَاتِ الصَّهَائِنَةِ العُ وَانِيَّةِ الْمُتَمَثَلَةِ بِحِرْمَانِ المهَجَّرين الفلسطينيين مِنْ حَقِ العَوْدَةِ إِلَى دِيَارِهِم(. ناقش المؤضُوعَ السَّابِقَ وَأَيْدُ مَا تَذْهَبُ إِلَيْهِ بِالشَّوَاهِدِ الْمُنَاسِة،ِ مُوَ فا الشَّاهِدَ الآتي: قَالَ الشَّاعِرُ عَبْدِ الكَرِيمِ الكَرْمِي: غَدًا سَنَعُودُ والأَجْيَالُ تُصْغِي إلى وقع الخطا عِنْدَ الإِيَابِ
[ANSWER_TEXT]: إجابة الموضوع المقترح المكتوب الثالث: وَفَعَتِ الأُمَّةُ العَرَبِيَّةُ بَينَ تَخَالب الدول الاستعمارية، والكيان الصهيوني الذين اندَفَعُوا نَحْوَ رُبُوع بلادنا كالوُحُوشِ الصَّارِيَة،ِ فَعَانُوا بِمَا فَسَادًا، وساموا أبناءَهَا ألوان العذاب فقد عاني الإنسان العربي وهو يرزخ تحت قبضة المحلينَ مِنَ الظَّلم والقَهْرِ وَالبَطْشِ؛ ذلك أن المغتصب كان باطشا لا يرحم وظامًا لا يعدِلُ إِلَّا أَنَّ أَبْنَاءَ الوَطَنِ العَربي، بما فطروا عليه من إباء للظلم وتَعَشقِ للحرِّيَّةِ

--- END STREAM ---
