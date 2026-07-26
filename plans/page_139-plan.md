# **SESSION 139**

[TASK DEFINITION]
Objective: Implement page 139.
File: `pages/page_139.html` (Note: Use the exact page number.)
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
[UNIQUE_ID]: b30022
[LESSON_NUMBER]: 139
[CHAPTER_TITLE]: page 139
[CATEGORY_HEADER]: 139
[SECTION_HEADER]: 139
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: المطالعة والقراءة التمهيدية ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b31642
Title: القراءة التمهيدية - نص أدبي
Content: القراءة التمهيدية - نص أدبي - المطالعة. كانَتْ حِرْبُ تشرين التحريرية ردا حقيقيا على نكسة حزيران، تلك النكسة التي صَدَمَتِ الإِنْسَانَ العَرَبِي،َّ وَنَالَتْ مِنْ كبريائِه،ِ وأَحْدَثَتْ في وجدانِهِ أَلَمَا عنيفًا ؛ لأَنَّهُ لَم يَكُنْ يَتَوَفَّعُ هَذِهِ النَّهَايَةَ الفَاجِعَةَ فَعَكس انتصار تشرين الفرح في قوافي الشعراء، فبعد أن خرج الوطنُ مِنَ الحرب منتصرًا، خفقت قلوب الشعراء مع قوافيهم متغنية بهذا الحدث الجلل، ترسم وتخط أشعارا تنتفض فرحا وتتطاير زهوا وإشراقا.ً حيث لجأ الأدباء إلى إبراز اعتزازهم بتدمير حصون الصهاينة فِي حَرْبِ تشرين،َ فَإِنَّ حَرْبَ تَشْرِينَ الَّتِي هَبَّتْ فِي ذَرَا الجَوْلَانِ وفوق رمال سيناء، حَمَلَتْ فِي عَصْفِهَا الزَّاحِفِ تَبَاشِيرَ النَّصْرِ والثقَةَ وَالأَمَلَ بِمِيلَادِ الإِنْسَانِ العَرَبِي الجديد، وخَطَّتْ صَفْحَةً مُشَرِّفَةً فِي تاريخ المسيرة العَرَبِيَّةِ نَحْوَ التَّقَدم والرقي. كانَتْ فَجْرًا عَرَبِيَّا جديدًا حَطَّمَ السُّدُودَ كُلها، وأَعَادَ لِلإِنْسَانِ العَرَبِيِّ كرامتهُ بِتِلْكَ الدماء التي بُذِلَتْ في ذلك اليوم لتحقيق النَّصْرِ وَرَسم بداية الانطلاقِ نَحْوَ التَّقدم وإثبات الوُجُودِ على السَّاحَةِ الدولية. وها هو الشاعر عبد الرحيم الحصني يُؤكد أنَّ الوَطَنَ المكافح استطاع بنضالِهِ المتواصل أَنْ يَدُكَ تَحْصِينَاتِ الأَعداء ويُدمرها، تلك التَّحْصِينَاتُ التي شَيَّدها الأعداء بروح يسيل منها الحقد، وتفوحُ مِنْهَا الكراهية. يقُول:ُ

=== BLOCK 3: Poem 1 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b69241
[RIGHT_HEMISTICH]: ونَسَفْتَ بِالرَّحْفِ المَقَدَّسِ مَا ابْتَنَى
[LEFT_HEMISTICH]: حِقْدُ العداةِ مِنَ الْحُصُونِ وَشَيَّدا

=== BLOCK 4: مواجهات وتضحيات ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b02398
Title: التضحيات والفداء
Content: ونظرا لكثرة المواجهات الدَّامِيَة،ِ والمعارك الضارية التي خاضَهَا أبناء الأمة العربية، وهم يتصدون للمستعمرين الغُزَاةِ الطَّامِعِين، لمَعَتْ بطولات لأبطال سطروا أروع ملاحم الفداء والتضحية؛ فلم يبخل أبناء الأمة العربية خلال كفاحهم المتواصل بالدَّم،ِ فَقَدَّمُوا قوافل الشهداء الذين صارُوا وَسَامَ شرف وقلادة ترصعُ صَدْرَ الأمة العربية. وأمام هذا العطاء الفياض والبذلِ السَّخِيِّ جَادَتْ أَقلامُ الأدباء بتمجيد التضحيات المشرفة التي حَقَّقَتِ الجَلَاءَ فما أروع التضحيات التي بذلها أبناء سورية لتحقيق منجز الجلاء حيث استعذبوا الموت وأرخصوا دماءهم في سبيل حرية الوطن، فقرنُوا أقوالهم بأفعالهم، وجعلوا أجسادهم حممًا تُلْهِبُ ظهور المستعمرين، وتحرق جباه الطُّغَاةِ الظَّالمين. فالشاعر عمر أبو ريشة يؤكد للحرية أنها ما جلبت إلى ربوع سورية بمهر بخس، وإنما جلبت بأغلى الأثمان وأنفسها، فكل حبة من تراب الوطن تَعَطَّرَتْ بِدَمٍ شَهِيْدٍ بَطَل،ِ رَفَضَ الذُّلَ والخَضُوع،َ وقَدَّمَ روحَهُ رَخِيْصَةً على مَذْبَحِ الحُرَيَّةِ يَقُول:ُ

=== BLOCK 5: Poem 2 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b01051
[RIGHT_HEMISTICH]: لَنْ تَرَيْ حَفْنَةَ رَمْلٍ فَوْقَهَا
[LEFT_HEMISTICH]: لَمْ تُعَطَرْ بِدِمَا حُرِّ أَبِي

=== BLOCK 6: استمرار الأدب القومي ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b47317
Title: الأدب العَرَبِيّ والقضايا الوَطَنِيَّة
Content: هَكَذَا نَجِدُ أَنَّ الأدبَ العَرَبِيَّ ظَلَ مُلازِمَا لِلقَضَايا الوَطَنِيَّة والقَوْمِيَّة التي تبرز في الساحة العربية، فقد وَجَدَ الأدباء في هذه القضايا مادةً غزيرةً غَمَسُوا فيها أقلامهم، فَصَاغُوا منها أَدَبًا تَجَلَّتْ فِيهِ الفَرْحَةُ الصَّاخِبَةُ بجلاء المستعمر الفرنسي عَنْ البلاد، وَبَرَزَتْ فِيهِ قُدْرَةُ الوَطَنِ وأبنائِهِ على تحطيم تحصينات الأعداء، وكانَ الصَّوْتَ الْمُجَلْجِلَ الذي صَدَحَ مُتَغَنِّيَا بِتَضْحِيَاتِ الشُّهَدَاءِ العِظَامِ الذين قَدَّمُوا أَرْوَاحَهم بِسَخَاءٍ لِتَنعم الأُمَّةُ بالحرية والكرامة.

=== BLOCK 7: تنبيه ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[UNIQUE_ID]: b91776
[CONTENT]: ثانيا: الموضوعان المقترحان غير المكتوبين تركنا هذبن الموضوعين من دون كتابة ليكونا دِرْبَةٌ وَمِرَانًا للطالب [

=== BLOCK 8: الموضوع المقترح الأول ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b12730
Title: الموضوع المقترح غير المكتوب الأول :
Content: قيل : اهتم الأُدَبَاءُ العَرَبُ فِي العَصْرِ الحَدِيثِ اهْتِمَامًا كَبِيرًا بالقضايا الوَطَنِيَّةِ وَالقَوْمِيَّة،ِ فَفَضَحُوا جَرَائِمَ الصُّهْيُونِيَّة، وحَثُوا على النهوض في وجه المجرمين، واثقين بانتصار الحق وثباتِهِ أمام الغاصبين((. ناقش المَوْضُوعَ السَّابِقَ وَأَيْدُ مَا تَذْهَبُ إِلَيْهِ بِالشَّوَاهِدِ المُنَاسِبَة،ِ مُوَظِّفًا الشَّاهِدَ الآتي: قَالَ الشَّاعِرُ إِبراهيم اليَازِجي:

=== BLOCK 9: Poem 3 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b56374
[RIGHT_HEMISTICH]: بالله يا قَوْمَنَا هَبُوا لِشَأْنِكُمُ
[LEFT_HEMISTICH]: فَكَم تُنَادِيكُمُ الأَشْعَارُ و الْخَطَبُ

=== BLOCK 10: الموضوع المقترح الثاني ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b68858
Title: الموضوع المقترح غير المكتوب الثاني:
Content: قيل : اهتم الأدَبَاءُ العَرَبُ بِالقَضايا الوَطَنِيَّةِ وَالقَوْمِيَّة،ِ فَصَوَّرُوا هَزِيمَةَ الْمُسْتَعْمِرِ الغَرْبِي وَخَيْبَتَهُ فِي تَوْطِيدِ وُجُودِهِ عَلَى أَرْضِنَا، ثمَّ أَبْرَزُوا وحْدَةَ العَرَبِ في المصائب والشَّدَائِدِ مُمَجَدِين تضحيات الأجداد مِنْ أَجْلِ الوطن، مُعَبَرِينِ عَنِ الفَرَحِ بِجَلَاءِ الْمُسْتَعْمِرِ الغَرْبي عن البلاد(. ناقش المَوْضُوعَ السَّابِقَ وَأَيِّدُ مَا تَذْهَبُ إِلَيْهِ بِالشَّوَاهِدِ المُنَاسِبَة،ِ مُوَظِّفًا الشَّاهِدَ الآتي: قَالَ الشَّاعِرُ حافظ إبراهيم:

=== BLOCK 11: Poem 4 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b88765
[RIGHT_HEMISTICH]: إِذَا الْمَّت توادي المسل نازلة
[LEFT_HEMISTICH]: باتت لها راسيات الشَّامِ تَضْطَرِبُ

--- END STREAM ---
