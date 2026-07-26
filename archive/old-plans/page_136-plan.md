# **SESSION 136**

[TASK DEFINITION]
Objective: Implement page 136.
File: `pages/page_136.html`
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
11. You must preserve the exact Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
15. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 136
[CHAPTER_TITLE]: page 136
[CATEGORY_HEADER]: 136
[SECTION_HEADER]: 136
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Opening Verse ===
(Component: TEMPLATE_C_POEM.html)
Verse 1: غَدًا سَنَعُودُ وَالأَجْيَالُ تُصْغِي | إلى وَقْعِ الخطا عِنْدَ الْإِيَابِ

=== BLOCK 3: Introduction Block ===
(Component: TEMPLATE_C_BLOCK.html)
Title:
Content: ولا يغرب عن مخيلة الإنسان العربي أن الأمة العربية وقَعَتْ فريسة بين مخالب الدول الاستعمارية الغربية التي اندفعت نحو ربوع بلادنا كالوحوش الضارية الفاتكة متَّخِذَةً شعارات الوصاية والحماية والانتداب أقنعة تغطي بها مآربها الدنيئة. لكن الخديعة لم تنطل على أبناء الأمة الذين هبوا في وجه الدخلاءِ فِي غَضْبَةٍ عَارِمَةٍ وثورة لاهبة متسلحين بالإباء وعشق الحرية.

=== BLOCK 4: Core Literature Analysis ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: ولأن الأدب مطواع مستجيب لكل ظرف يعصف بالأمة واكب مسيرة الكفاح والنضال فشحن النفوس بروح الثورة لتحرير الأمة المسْتَعْبَدَة وتوحيد الوطن الممزق، فقد قام الأدباء العرب باستنكار خداع الفرنسيين الشعوب العربية، فلم يخف على الأدباء زيف ادعاءات المستعمر الغربي فأقدموا على كشف وعوده البراقة الكاذبة وفضح أساليبه الملتوية التي يَبْغِي مِنْ وَرَائِهَا جَعْلَ البلاد العَرَبِيَّة لقمَةً سَائِغَة،َ وَمَطْمَعًا مَرِيئًا ، لِيَتَمَكَّنَ مِنْ احتلالِ الأَرْضِ واستعباد الإنسان. فالشَّاعِرُ خَيْرُ الدِّينِ الزِرَكْلِي يُؤْكِدُ أَنَّ المستعمر أعلن أنَّهُ جَاءَ لِيقِفَ إلى جانب الأقطَارِ العَرَبِيَّةِ ويأخُذَ بِيَدِهَا لِتَنهَضَ وَتَتَحَرَّرَ من الجهل والتخلف، ويزرع العدالة والمساواة بَيْنَ أَبِنَائِهَا وَيَجْعَلَهُم يَنْعَمُونَ بِالْحَرِّيَّة، لَكِنَّهُ مَا إِنْ وَضَعَ أقدامه على الأرض العربية كشر عن أنياب الشر والغدر والخيانة، فتنكر لوعوده، وتجاهل المواثيق التي قطعها للعرب. فاستعمر البلاد وعاث فسادا في ربوع الأمة العربية، التي قدمت للعالم أزهى الحضارات وأعرقها، حيث أضمر لها الغدر والخديعة وارْتَكَبَ بحقِّهَا أَفْظَعَ الجرائم. يقول:

=== BLOCK 5: Zirikli Verses ===
(Component: TEMPLATE_C_POEM.html)
Verse 1: جَهَرُوا بِتَحْرِيرِ الشَّعُوبِ وَأَثْقَلَتْ | مَتْنَ الشَّعُوبِ سَلَاسِلٌ وَقُيُودُ
Verse 2: خَدَعُوكِ يَا أُمَّ الْحَضَارَةِ فَارْتَمَتْ | تَجْنِي عَلَيْكِ فَيَالِقٌ وَجُنُودُ

=== BLOCK 6: Struggle and Sacrifice ===
(Component: TEMPLATE_C_BLOCK.html)
Title:
Content: ونظرا لكثرة المواجهات الدَّامِيَة،ِ والمعارك الضارية التي خاضها أبناء الأمَّةِ العربية، وهم يتصدون للمستعمرين الغزاة الطَّامِعين، لمعت بطولات لأبطال سطروا أروع ملاحم الفداء والتضحية؛ فلم يبخل أبناء الأمة العربية خلال كفاحهم المتواصل بالدم، فقدموا قوافل الشهداء الذينَ صَارُوا وِسَامَ شرف وقلادة ترصعانِ صَدْرَ الأمة العربية. وأمام هذا العَطَاءِ الفياض والبذلِ السَّخِيِّ جَادَتْ أَقلامُ الأدباء بتمجيد التضحيات المشرفَةِ التِي حَقَقَتِ الجلاء؛ فما أروع التضحيات التي بذلها أبناء سورية لتحقيق مُنْجَزِ الجلاء حيث استعذبُوا الموت وأرخصوا دماءهم في سبيل حرية الوطن، فقرنوا أقوالهم بأفعالهم، وجعلوا أجسادَهُم حِمَمًا تُلْهِبُ ظهور المستعمرين وتحرِقُ جباه الطَّغَاةِ الظَّالمين. فالشاعر عمر أبو ريشة يؤكد للحرية أنها ما جلبت إلى ربوع سورية بمهر بخس، وإنما جُلِبَت بأغلى الأثمان وأنفسها، فكل حبة من تراب الوطنِ تَعَطَّرَتْ بِدَمِ شَهِيْدٍ بَطَل،ِ رَفَضَ الذُّلَّ والخضُوع،َ وقَدَّمَ روحهُ رَخِيْصَةً على مَذْبَحِ الحُرِّيَّةِ يَقُول:ُ

=== BLOCK 7: Abu Risha Verse ===
(Component: TEMPLATE_C_POEM.html)
Verse 1: لَنْ تَرَيْ حَفْنَةَ رَمْلِ فَوْقَهَا | لَمْ تُعَطَّرْ بِدِمَا حُرَّ أَبِي

=== BLOCK 8: Palestinian Struggle and Conclusion ===
(Component: TEMPLATE_C_BLOCK.html)
Title:
Content: وهكذا كانَ الأَدَبُ العَرَبِيُّ مِنْبَرًا يُفْصِحُ عن إصرار الفلسطيني المهجر على العودة إلى أَرْضِ الوَطَنِ الحَبيب؛ وكانَ مِرْآةً صَافِيَةً انعكست على صفحتها المشرِقَةِ أَكَاذِيبُ الْمُسْتَعْمِرِينَ ووعُودُهُم الزَّائِفَة،ُ وكان الصوت المجلجل الذي صَدَحَ مُتَغَنِّيَا بِتَضْحِيَاتِ الشُّهَدَاءِ العِظَامِ الذين قَدَّمُوا أَرْوَاحَهُم بِسَخَاءٍ لِتَنعم الأُمَّةُ بالحرَيَّةِ والكرامة.

=== BLOCK 9: The Core Matrix (Answer to Topic) ===
(Component: TEMPLATE_C_TABLE.html)
Title: إجابة الموضوع المقترح المكتوب الثالث
Content: وَقَعَتِ الأُمَّةُ العَرَبِيَّةُ بَينَ مَخَالِبِ الدول الاستعمارية، والكيان الصهيوني الذين اندَفَعُوا نَحْوَ رُبُوع بلادنا كالوُحُوشِ الضَّارِيَة،ِ فَعَاثُوا بِمَا فَسَادًا، وساموا أبناءَهَا ألوان العذاب فقد عاني الإنسان العربي وهو يرزخ تحت قبضة المحلينَ مِنَ الظَّلم والقَهْرِ وَالبَطْشِ؛ ذلك أن المغتصب كان باطشا لا يرحم وظامًا لا يعدِلُ إِلَّا أَنَّ أَبْنَاءَ الوَطَنِ العَربي، بما فطروا عليه من إباء للظلم وتَعَشقِ للحرِّيَّةِ

=== BLOCK 10: Exam Block (Topic Question) ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: الموضوع المقترح المكتوب الثالث: قيل: (أَوْلَى الْأُدَبَاءُ العَرَبُ فِي العَصْرِ الحَدِيثِ القضايا الوَطَنِيَّةَ والقَوْمِيَّةَ اهْتِمَامًا كَبِيرًا، فَعَبَّرُوا عَنْ مَشَاعِرِ الْفَرَحِ وَالزَّهْوِ بِنَصْرِ تشرين، وأَكَّدُوا تَمَسُّكَ المُهَجَّرِينَ الفلسطينيين بِالأَمَلِ وَتَطَلُّعَهُم إلى العَوْدَة،َ فَاضِحِينَ مُمَارَسَاتِ الصَّهَائِنَةِ العُدْوَانِيَّةِ الْمُتَمَثِّلَةِ بِحِرْمَانِ المُهَجَّرين الفلسطينيين مِنْ حَقِّ العَوْدَةِ إِلَى دِيَارِهِم). ناقش المَوْضُوعَ السَّابِقَ وَأَيِّدْ مَا تَذْهَبُ إِلَيْهِ بِالشَّوَاهِدِ الْمُنَاسِبَة،ِ مُوَظِّفاً الشَّاهِدَ الآتي: قَالَ الشَّاعِرُ عَبْدِ الكَرِيمِ الكَرْمِي: غَدًا سَنَعُودُ والأَجْيَالُ تُصْغِي إلى وقع الخطا عِنْدَ الإِيَابِ

--- END STREAM ---
