# **SESSION 143**

[TASK DEFINITION]
Objective: Implement page 143.
File: `pages/page_143.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`.
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md` to identify the correct template to use for the continuation.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green`  for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide: NO INLINE STYLES. Irab Words inside `.irab-word` MUST be white. Mapping: `style="width: 20%"` -> `class="w-20pct"`, `style="margin-top: 2mm"` -> `class="mt-2mm"`, `style="text-align: center"` -> `class="text-center"`, `style="font-weight: bold"` -> `class="font-bold"`.
6. Templates: You are forbidden from inventing new HTML tags or classes or template elements. Replace any `<section>` tags from the templates with `<div>` tags (keep `<header>` for page headers as is).
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). The ID MUST be applied to the `<div>` tag that replaced the `<section>` tag. Use "Jules-workspace/id_manager.py" to generate or verify them.
8. **Self-Correction:** Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...) .
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html`.
15. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 143
[CHAPTER_TITLE]: page 143
[CATEGORY_HEADER]: 143
[SECTION_HEADER]: 143
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Continuation ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
Title: تتمة
Content: إِنَّ الكَادِحِينَ يَتَحَدُّونَ ظُرُوفَ العَمل القاسية في مصانع الحديد ومناجم الفحم، ويَقْهَرُونَ حرارَةَ الشَّمْسِ الْخَارِقَة. فَيَصْنَعُونَ لأَنْفُسِهِمُ المَسَرَّاتِ مِن خِلالِ إِقْنَاعِ أَنفُسِهِم، وإِرْضَائِهَا بِأَحلام بَسِيطَةٍ قَابِلَةٍ للتَّحَقَّقِ.

=== BLOCK 3: المستوى الفني (Matrix Table) ===
(Component: TEMPLATE_C_TABLE.html)
Title: المستوى الفني: عَبَّرَ الشَّاعِرُ عَنْ مَضَامِينِ الأَدَبِ الواقعي مُسْتَعْمِلاً أدوات: (السَّرْد، الصورة، التداعي، تضمين بَعْضِ قِصَصِ التُّرَاثِ الحاضرة في وجدان الجماعة). هاتِ مِثالًا لِكُلِّ مِنْهَا.
Headers: [الأداة] | [المثال]
Row 1: السرد | الملايين التي تكدح لا تَحْلُمُ بِمَوتِ فَرَاشَة
Row 2: الصورة | أحزان البنفسج
Row 3: التداعي | إِنَّهَا تَضْحَكُ مِن أعماقها
Row 4: تضمين قِصَصِ التُّرَاثِ الحاضِرَةِ في وجدان الجماعة | تغرم، لا كما يُغْرَمُ مَجْنُونُ بِطَيْف

=== BLOCK 4: الأسئلة والتدريبات ===
(Component: TEMPLATE_C_LIST.html)
Title: أسئلة وأجوبة
Item 1: سؤال: لجأ الشَّاعِرُ إلى الجُمَلِ الخَبَرِيَّةِ فِي النَّصَ كُلِّهِ اذْكُرُ مُسَوِّغَاتِ ذَلِكَ. الجواب: لجأ الشاعر إلى الأسلوب الخبري من أجل نقل المعلومات أو الأخبار والوصف والتصوير وتقرير الحقائق، وَتَثْبِيتِهَا فِي ذِهْنِ الْمُتَلَقِّي.
Item 2: سؤال: أكثَرَ الشَّاعِرُ مِنَ التفاصيل الجزئِيَّةِ المُنْتَزَعَةِ مِنْ حياةِ الكَادِحِين. اختر أَمْثِلَةً لِهِذِهِ التَّفَاصِيل، وبين دورها في التأثير الجمالي في المتلقي. الجواب: الأمثلة: الملايين التِي تَصْنَعُ لِلحَالِمِ زَوْرَقُ المَلايين التِي تَصْنَعُ مِنْدِيلًا لِمُغْرَم، الملايين التي تبكي، تغني، تتألم في زوايا الأرض، في مصنع صلب أو بمنجم. دورها في التأثير الجمالي: أسهمت هذه التفاصيل الجزئية الصغيرة في عَرْضِ الفكر والقضايا العامة للمتلقي، وتَعْمِيقها فِي وِجْدَانِهِ؛ ذلِكَ أَنَّ الشَّاعِرَ لَمْ يَعْرِضُ هذه الفِكر والقضابا عرضا مباشرا، وإنما عَرَضَهَا بِلَغَةِ الشِّعْرِ، ورؤياه الإبداعية.
Item 3: سؤال: استَخْرِجُ مِنَ المَقْطَّعِ الْأَوَّلِ: (كِناية، استعارة مَكْنِيَّة)، وَبَيْن وظيفةً لِكُلِّ مِنْهُما. الجواب: الكناية: الملايين التِي تَكْدَحُ، لَا تَحْلُمُ فِي مَوْتِ فراشة - وظيفتها تأكِيدُ إِنسانية الطَّبَقَةِ الكَادِحَةِ، وَتَقْرِيبُ ذَلِكَ مِنْ ذِهْنِ الْمُتَلَقِّي. الاستعارة المكنيَّةُ : (أَحْزان البَنَفْسَج) - وظيفتها الإيحاء، حيث جَعَلَ الشَّاعِرُ الصُّورَةَ مُوحِيَةً بِتَشْبِيهِهِ البَنَفْسَجِ بإنسان، فهذا أوحى بإنسانية الكادِحِين ولطفهم ورقتهم.
Item 4: سؤال: أَسْهَمَ تَنوع القوافي والأنغام في إبراز المشاعر المتنوعة، وحركتها الانفعالية، ادرس ذَلِكَ فِي المَقْطَعِ الثَّانِي مِنَ النَّصِّ. الجواب: أدى تَنَوُّعُ القَوَافِي والأَنْغَامِ فِي الأَسْطُرِ الشِّعْرِيَّةِ إِلَى تَنَوُّعِ الْمَشَاعِرِ العاطِفِيَّةِ، على النحو الآتي: مشاعر الحب. ورق: أبرز التنوعُ هنا مَشَاعِرَ الأَمَلِ. تغني، تضحك: أبرز التَّنوعُ هنا مَشَاعِرَ الفرح. تبكي: أبرز التنوع هنا مشاعر الحزن. تكدح، تعرى، تمزق، تعلم، منجم: أبرز التَّنوع هنا مشاعر الألم. تغرم، بطيف: أبرز التنوع هنا مشاعر الحب.
Item 5: سؤال: قطعْ عَرُوضِيَّا السَّطْرَ الْأَوَّلَ مِنَ النَّصِّ، واذكر التفعيلة التي بني عليها.

=== BLOCK 5: العروض (تنبيه برتقالي) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: تقطيع السَّطْرِ الأَوَّلِ مِنَ النَّصِّ، وَذِكُرُ التفعيلة التي يُبْنَى عليها
Content: الملايي / فاعلاتن | من التي تك / فاعلاتن | مدح لا تح لم في مؤ تِ فَرَاشَهُ / فعلاتن فعلاتن فعلاتن. بني النص على تَفْعِيلَةِ الرَّمَلِ (فاعلاتن) وجوازاتها.

=== BLOCK 6: إجابات نموذجية (تنبيه برتقالي) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: إجابات نموذجية
Content: وسائل تمكن الكادحين من تحقيق آمالهم: يُمكن للكادِحِينَ أَنْ يُحَقِّقُوا أَحلامَهُم مِنْ خلال: - الحصول على فُرَصِ عَمَلٍ تُؤَمِّن لَهُم رزقهم، وتحفظ كرامتهم. - استعادة مصادر الثروة، وافتكاكِهَا مِمَنْ يُهَيْمِنُونَ عَلَيْهَا مِنَ الْمُسْتَغِلين. - اعتمادِ برنامج اقتصادِي يُمَكِّنُ الْكَادِحِينَ مِنَ الإِسْهَامِ فِي إِدَارَةِ وَسَائِلِ الإنتاج. دراسة النص وفق المنهج الاجتماعي: الإجابة: تعدَّدَتِ المناهج النَّقْدِيَّةُ التِي تَتَنَاوِلُ دِرَاسَةَ النَّصِّ الأدبي في العصر الحديث، ومن بينها المنهج الاجتماعي الذي يربط الأدب بالمجتمع، ويقيس إجادة الأديب بمدى تصويره لهموم مجتمعه وطبقته تصويرًا صَادِقًا. فَالْأَدَبُ وَفَقَ رُؤْيَةِ الْمَنْهَجِ الاجِتِمَاعِيِّ يُمَثِّلُ حَيَاةَ الجَمَاعَةِ، ويُعَبِّرُ عَنِ الواقع.

=== BLOCK 7: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: المستوى الإبداعي: اكتفى الشَّاعِرُ بِتَناول أحلام الكادِحِينَ وآمالهم. اقْتَرَحْ وسائِلَ تُمَكِّنُهُم مِنْ تحقيق تِلْكَ الآمال؟
Number: ٢
Question: التعبير الكتابي : ادرس النص وفق المنهج الاجتماعي مستفيدا من إجاباتِكَ عَنْ أَسْئِلَةِ الْمُسْتَوَيْنِ (الفِكْرِيِّ والفني)، مُستَعِينَا بِمَا وَرَدَ فِي دِرَاسَةِ نَصِّ (أَنشُودَةِ المَطَرِ).

--- END STREAM ---
