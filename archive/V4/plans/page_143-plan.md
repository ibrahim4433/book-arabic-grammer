# **SESSION 143**

[TASK DEFINITION]
Objective: Implement page 143.
File: `pages/page_143.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
1.5 ANTI-HALLUCINATION & STRICT TYPOGRAPHER RULE (CRITICAL): Do NOT invent, hallucinate, or add new grammar rules, examples, or external text. ONLY use the exact text slices provided in the Raw Input Text. You MUST use 100% of the provided raw text. NO summarizing, NO deleting, NO adding new content. Every piece of text must map to an approved TEMPLATE.
1.6 THE TYPO EXCEPTION: You are explicitly permitted to correct obvious typos, spelling errors, or grammatical errors in the raw Arabic text during planning.
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
[LESSON_NUMBER]: 143
[CHAPTER_TITLE]: page 143
[CATEGORY_HEADER]: 143
[SECTION_HEADER]: 143
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Cut Content (Start of page) ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[UNIQUE_ID]: b77217
[BLOCK_TITLE]: المستوى الفكري:
[CONTENT]:
ويَقْهَرُونَ حرارَةَ الشَّمْسِ الْخَارِقَة. فَيَصْعُونَ - إِنَّ الكَادِحِينَ يَتَحَدُّونَ ظُرُوفَ العَمل القاسية في مصانع الحديد ومناجم الفحم، لأَنْفُسِهِمُ المَسَرَّاتِ مِن خِلالِ إِقْنَاعِ أَنفُسِهِم، وإِرْضَائِهَا بِأَحلام بَسِيطَةٍ قَابِلَةٍ للتَّحَقَّق.ِ

=== BLOCK 3: المستوى الفني (Matrix) ===
(Component: TEMPLATE_C_TABLE.html)
[UNIQUE_ID]: b66751
[BLOCK_TITLE]: المستوى الفني:
[CONTENT]:
- عَبْرَ الشَّاعِرُ عَنْ مَصَامِينِ الأَدَبِ الواقعي مُستَعْملا أدوات: )السَّرْد، الصورة التداعي، تضمين بَعْضِ قِصَصِ الثَّاثِ الحاضرة في وجدان الجماعة(. هاتِ مِثالًا لِكُلِّ مِنْهَا.
[HEADER_1]: السرد
[HEADER_2]: الصورة
[HEADER_3]: التداعي
[HEADER_4]: تضمين قِصَصِ الراثِ الحاضِرَةِ في وجدان الجماعة
[CELL_1]: الملايين التي تكتح لا تَحْلُمُ بِمَوتِ فَرَاشَة
[CELL_2]: أحزان البنفسج
[CELL_3]: إِنَّهَا تَصْحَكُ مِن أعماقها
[CELL_4]: تغرم، لا كما يُغْرَمُ مَجْنُونَ بِطَيْف

=== BLOCK 4: Question 2 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b20440
[QUESTION_NUMBER]: ٢
[QUESTION_TEXT]: - لجأ الشَّاعِرُ إلى الجُمَلِ الخَبَرِيَّةِ فِي النَّصَ كُلِّهِ اذْكُرُ مُسَوْعَاتِ ذَلِك.َ
[ANSWER_TEXT]: جا الشاعر إلى الأسلوب الخبري من أجل نقل المعلومات أو الأخبار والوصف والتصوير وتقرير الحقائق، وَتَفْبِيتِهَا فِي ذِهْنِ الْمُتَلَقِي.

=== BLOCK 5: Question 3 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b00344
[QUESTION_NUMBER]: ٣
[QUESTION_TEXT]: ۳- أكثَرَ الشَّاعِرُ مِنَ التفاصيل الجزنِيَّةِ المُنْتَرَعَةِ مِنْ حياةِ الكَادِحِين. اختر أَمَئِلَةً لِهِذِهِ التَّفَاصِيل، وبين دورها في التأثير الجمالي في المتلقي.
[ANSWER_TEXT]: في - الأمثلة: الملايين التِي تَصْنَعُ لِلحَالِمِ زَوْرَقُ المَلايين التِي تَصْنَعُ مِنْدِيلًا لِمُغْرَم،ْ الملايين التي تبكي، تغتي، تتألم في زوايا الأرض، مصنع صلب أو بمنجم، دورها في التأثير الجمالي: أسهمت هذه التفاصيل الجزئية الصغيرة في عَرْضِ الفكر والقضايا العامة للمتلقي، وتَعْمِيقها فِي وِجُدَانِهِ؛ ذلِكَ أَنَّ الشَّاعِرَ لَمْ يَعْرِضُ هذه الفِكر والقضابا عرضا مباشرا، وإنما عَرَضَهَا بِلَغَةِ الشَّعْر،ِ ورؤياه الإبداعية.

=== BLOCK 6: Question 4 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b63133
[QUESTION_NUMBER]: ٤
[QUESTION_TEXT]: - استَخْرِجُ مِنَ المَقْطَّعِ الْأَوَّل:ِ )كِناية، استعارة مَكْنِيَّة(، وَبَيْن وظيفةً لِكُلِّ مِنْهُما.
[ANSWER_TEXT]: ج - الكتابة: الملايين التِي نَكْدَح،ُ لَا تَحْلُمُ فِي مَوْتِ فراشة - وظيفتها تأكِيدُ إِنسانية الطَّبَقَةِ الكَادِحَة،ِ وَتَقْرِيبُ ذَلِكَ مِنْ ذِهْنِ الْمُتَلَقِي. الاستعارة المكنيَّةُ : )أَحْزان البَنَفْسَخ( - وظيفتها الإيحاء، حيث جَعَلَ الشَّاعِرُ الصُّورَةَ مُوحِيَةً بِتَشْبِيهِهِ البَنَفْسَحِ بإنسان، فهذا أوحى بإنسانية الكادِحِين وتُطْفِهم ورقتهم.

=== BLOCK 7: Question 5 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b46300
[QUESTION_NUMBER]: ٥
[QUESTION_TEXT]: ه- أَسْهَمَ تَنوع القوافي والأنغام في إبراز المشاعر المتنوعة، وحركتها الانفعالية، ادرس ذَلِكَ فِي المَقْطَعِ الثَّانِي مِنَ النَّص.َ
[ANSWER_TEXT]: ه- أدى تَنَؤُعُ القَوَافِي والأَنْعَامِ فِي الأَسْطُرِ الشَّعْرِيَّةِ إِلَى تَنَوُّعِ الْمَشَاعِرِ العاطِفِيَّة،ِ على النحو الآتي: - مَشَاعِرَ الحب ... ورق : أبرز التنوعُ هنا مَشَاعِرَ الأَمَل.ِ - ... تغي، ... تضحك: أبرز التَّنوعُ هنا مَشَاعِرَ الفرح. - ... تبكي: أبرز ... تكدح ... تعرى ... تمزق ... تعلم ... منجم : أبرز التَّنوع هنا مشاعر الألم. - ... فرم ... بطيف: أبرز التنوع هنا مشاعر الحب. - ... أحزان البنفسج: أبرز التنوع هنا مشاعر الحزن.

=== BLOCK 8: العروض ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[UNIQUE_ID]: b18707
[BLOCK_TITLE]: تنبيه عروضي
[CONTENT]:
- قطعْ عَرُوضِيَّا السَّطْرَ الْأَوَّلَ مِنَ النَّص،َ واذكر التفعيلة التي بي عليها. ج - تقطيع السَّطْرِ الأَوَّلِ مِنَ النَّ ، وَذِكُرُ التفعيلة التي يُنِي عليها: الملايي 이이이 فاعلاتن - من التي تك 이이이 فاعلاتن - مدح لا تح لم في مؤ تِ فَرَاشَهُ فعلاتن فعلاتن فعلاتن - بني النص على تَفْعِيلَةِ الرَّمَلِ )فاعلاتن( وجوازاتها .

=== BLOCK 9: المستوى الإبداعي ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b72332
[QUESTION_NUMBER]: ٦
[QUESTION_TEXT]: المستوى الإبداعي: اكتفى الشَّاعِرُ بِتَناول أحلام الكادِحِينَ وآمالهم. اقْتَرَحْ وسائِلَ مَكِّنُهُم مِنْ تحقيق تِلْكَ الآمال؟
[ANSWER_TEXT]: ج - يُمكن للكادِحِينَ أَنْ يُحَقِقُوا أَحلامَهُم مِنْ خلال : - الحصول على فُرَضِ عَمَلٍ تُؤْمِن لَهُم رزقهم، وتحفظ كرامتهم. - استعادة مصادر الزي، وافتكاكِهَا مِمَنْ يُهَيْمِنُونَ عَلَيْهَا مِنَ الْمُسْتَغِلين - اعتمادِ برنامج اقتصادِي يُمَكِّنُ الْكَادِحِينَ مِنَ الإِسْهَامِ فِي إِدَارَةِ وَسَائِلِ الإنتاج.

=== BLOCK 10: التعبير الكتابي ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
[UNIQUE_ID]: b94925
[BLOCK_TITLE]: التعبير الكتابي :
[CONTENT]:
ادرس النص وفق المنهج الاجتماعي مستفيدا من إجاباتِكَ عَنْ أَسْئِلَةِ الْمُسْتَوَيْنِ )الفِكْرِيِّ والفني(، مُستَعِينَا بِمَا وَرَةَ فِي دِرَاسَةِ نَصَيِّ أَنشُودَةِ المَطَرِ(. الإجابة: تعدَّدَتِ المناهج التَّقْدِيَّةُ التِي تَتَنَاوِلُ رَاسَةَ النَّ الأدبي في العصر الحديث، ومن بينها المنهج الاجتماعي الذي يربط الأدب بالمجتمع، ويقيس إجادة الأديب بمدى تصويره لهموم مجتمعه وطبقته تصويرًا صَادِقًا . فَالْأَدَبُ وَفَقَ رَؤْيَةِ الْمَنْهَحِ الاجِتِمَاعِيَ يُبْلُ حَيَاةَ الجمَاعَة،ِ ويُعَبَرُ عَنِ الواقع.

--- END STREAM ---