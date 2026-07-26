# **SESSION 148**

[TASK DEFINITION]
Objective: Implement page 148.
File: `pages/page_148.html` (Note: Use the exact page number.)
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
[LESSON_NUMBER]: 148
[CHAPTER_TITLE]: page 148
[CATEGORY_HEADER]: 148
[SECTION_HEADER]: 148
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Question 1 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b30618
[QUESTION_NUMBER]: ١
[QUESTION_TEXT]: ما دَوْرُ كُلِّ مِنَ الخَبَرِ والإِنْشَاءِ فِي تَفسير الحالةِ الشَّعُورِيَّةِ التِي تَكْتَنِفُ الشَّاعِرَ.
[ANSWER_TEXT]: مِنْ ج ٢- الخَبَر: نقل الحالة النَّفْسِيةَ اللَّتِي تَمَلَكَتِ الشَّاعِر،َ وَوَصَفَ حَالَتَهُ الجَسَدِيَّة المُزْرِيَة،َ وَأَخْبَرَ عَنْ آمَالِهِ وطُمُوحَاتِهِ وَرَغْبَتِهِ بِالتَّخَلُصِ معاناته - الإنشاء : دلل على حالة الشاعر الانفعالِيَّة،ِ فَأَفْصَحَ عَنْ أَحْزَانِهِ وعَذاباته، وأبان اضطراباتِهِ النَّفْسِيَّةِ.

=== BLOCK 3: Question 2 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b15637
[QUESTION_NUMBER]: ٢
[QUESTION_TEXT]: استَعْمَلَ الشَّاعِرُ الرُّموزَ بَيِّنْ أَثَرَهَا فِي التَّعْبِيرِ عَنْ حالاتِهِ النَّفْسِيَّة،ِ مَعَ مِثَالٍ مُنَاسِبِ لِذَلِك.َ
[ANSWER_TEXT]: تَمَكَّنَتِ الرُّمُوزُ مِنَ الإِفْصَاحِ عَنِ الحالة النفسِيَّةِ التي يحياها، فقد رمز بالحيَّةِ إلى الألم والعَذَابِ اللَّذِينَ يُعاني منهما بِسَبَبٍ مَشَاعِرِ الحب ورمز بالنُّجُومِ إِلَى السَّعَادَةِ التِي يَرْغَبُ بِبُلُوغِها.

=== BLOCK 4: Question 3 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b77911
[QUESTION_NUMBER]: ٣
[QUESTION_TEXT]: اللاشُعُورِ - تأثَرَتِ الصور بمعاناةِ الشَّاعِرِ النَّفْسِيَّة،ِ وأمانيهِ المَكْبُوتَةِ مَثِّلْ لِكُلِّ مِنْهُما، مُبَيِّنَا مَا عَكَسَتْهُ مِنْ أَحَاسِيسَ وَرَغَبَاتٍ مُخْتَزَنَةٍ فِي لَدَى الشَّاعِرِ .
[ANSWER_TEXT]: مُعَبَرِ عَنْ مُعَانَاةَ الشَّاعِرِ الْمُكْبُوتَةِ - يا شعوري، يا حَيَّة: اصطَبَعَتْ هذه الصورة بما أَضْفَاهُ اللَّاشْعُورُ عليها مِنْ آلَامِ ومُعاناة، فَكَانَتْ خَيْرَ مَكْبُوتَة،ِ فَكَانَتْ خَيْرَ مُعَبَرِ عَنِ الْمَعَانَاةِ الْجَسَدِيَّةِ في أَعْماقه. - شهد الحب اصطبَغَتْ هذه الصُّورَةُ بما أَضْفَاهُ اللَّشُعُورُ عليها مِنْ مُعَانَاةٍ وأحلام، لتجاوز خَيْبَةَ والآلامِ النَّفْسِيَّةِ المَكْبُوتَةِ. - يطاولني الدَّهْرُ بغير الهوى اصطبَغَتْ هذه الصورة بما أضفاهُ اللاشعُورُ عليها مِنْ آلام الأمل والانكسار أَمَامَ دَهْرِ غَالَبَ الشَّاعِر،َ فَكَانَتْ خَيْرَ مُعَبِّرِ عَمَّا كَانَ مَكْبُوتًا فِي أَعْمَاقِه.ِ

=== BLOCK 5: Question 4 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b84197
[QUESTION_NUMBER]: ٤
[QUESTION_TEXT]: : ه- جاءت الموسيقا الداخلية والخارجية استجابة لانفعالاتِ الشَّاعِرِ الْمُحْتَدِمَة.ِ ادرُسُ ذَلِكَ مِنْ خلال عناصر الموسيقا الدَّاخِلِيَّةِ - روي الباءِ المَكْسُورَة(.
[ANSWER_TEXT]: - جاءَتِ الموسيقا الدَّاخِلِيَّةِ مُتَنَاغِمَةً مُنْسَجِمَةً مَعَ انفعالات الشاعر العاطفية، فالتَّنَاغُمُ والانسجامُ بَيْنَ حُرُوفِ الهَمْسِ وَالجَهْرِ وَافْقَ انفعالات الشاعر وحالته المضطربة. والتناغُمُ بَيْنَ حُرُوفَ المَدِ الطَّوِيلِ وَالمَدِ القَصِيرِ لَاءَمَ حالة الأسى التي يحياها، ومكنهُ مِنْ إِخراج الآهات المكبُوتَةِ فِي صَدْرِهِ أَمَّا رَوِي الباءِ المَكْسُورَةِ فَيُشِيرُ إِلَى نَفْسِيَّةِ الشَّاعِرِ الْمُنْكَسِرَة.ِ

=== BLOCK 6: Question 5 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b83175
[QUESTION_NUMBER]: ٥
[QUESTION_TEXT]: - قَطَعْ عروضِيًّا صَدْرَ البيتِ الأَوَّل،ِ ثُمَّ سَمَ بَحْرَه.ُ
[ANSWER_TEXT]: ج-٦ تقطيع صَدْرِ البيتِ الأَوَّلِ مِنَ النَّص،َ وتسميةُ بَحْرِهِ البَحْرُ الخفيف.

=== BLOCK 7: Table for Poetic Meter ===
(Component: TEMPLATE_C_TABLE.html)
[UNIQUE_ID]: b70274
[HEADER_1]: البيت
[HEADER_2]: التقطيع
[HEADER_3]: التفعيلات
[CELL_1]: يا حَيَّةٌ تنفث السم يا شُعُورِي
[CELL_2]: 이 이이이
[CELL_3]: فاعلاتن مستفعلن فاعلاتن

=== BLOCK 8: Creative Level ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[UNIQUE_ID]: b07100
[TITLE]: المستوى الإبداعي:
[CONTENT]: كَشَفَ المَقْطَعُ الثَّانِي عَنْ أَماني الشَّاعِرِ الحَبِيسَةِ. أضف ما تراهُ مُناسبًا مِنْ أُمنيات أخرى مُوَظِّفاً الْأَسْلُوبَ السَّرْدِي.

=== BLOCK 9: Answer ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b60688
Title: الإجابة :
Content: إِنَّ رُوحِي المُعَذَّبَةَ تَنْزِعُ إِلَى لِقَاءِ مَحْبُوبَتِي بَعْدَ طُولِ الفراق،ِ فَقَلْبِي مُمَزَّقٌ يَتُوقُ إِلَى الوصالِ بَعْدَ طُولِ البَعَاد.ِ كلما لاحَتْ بَارِقَةُ أَمَلِ حصول هذا اللَّقَاءِ تَحْتَدِمُ فِي نَفْسِي لَهْفَةٌ عَارِمَةً لِرؤياهَا، فَأَبْدَأُ بِتَخَيْلِ مَشْهَدِ اللَّقَاء،ِ فَتَرِفُ فِي قَلْبِي مَنَازِعُ الشَّوْق،ِ فَتَجْتَاحُنِي رَغْبَةٌ عارِمَةً بِالقُرْبِ مِنْهَا لأَتَخَلَّصَ مِنْ غَصَّةِ الوَحْشَة،ِ وَمَرَارَةِ اللَّوعَةِ اللَّذِين رافَقَانِي طَوَالَ غيابها عَنِّي.
كَمْ آمَلُ أَنْ يَتَحَقَّقَ هذا اللقاء، عَلَّهُ يُخَفِّفُ معاناتي، ويُنْهِي عَذَابِي فَأَسْتَعِيدُ تِلْكَ الْأَيَّامَ الخَوَالي التي جَمَعَتْنِي بِمَحْبُوبَتِي؛ فهي أَهْنَأُ للبال، وأَكْثَرُ مُنْعَةَ للنَّفْسِ لأَنَّهَا كَانَتْ أَيَّامَا عَامِرَةً بِالفَرَح مُفْعَمَةً بِالسَّعَادَة.ِ

=== BLOCK 10: Written Expression ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b58726
[UNIQUE_ID_BIO]: b38838
[POEM_TITLE]: التعبير الكتابي:
[POET_NAME]: ادرس الأبيات الآتية من النَّصَ وَفَقَ المَنْهَجِ النَّفْسِي، مُستَفِيدًا مِنْ إِجابتِكَ عَنْ أَسْئِلَةِ الْمُسْتَوِيَنِ الْفِكْرِيِّ والفني، وَمَا مَرَّ فِي نَصَ * فدوى طوقان(
[RIGHT_HEMISTICH]: يا شُعُوري يا حَيَّةً تَنْفُثُ السُّمَّ
[LEFT_HEMISTICH]: فَيَجْرِي فِي القَلْبِ مِنْ أَلْفِ نَابِ
[RIGHT_HEMISTICH]: كَبْرَتِ فِيكَ عِلْتِي وَتَناهى
[LEFT_HEMISTICH]: فيك حزني، وطال فيكَ عَذَابِي
[RIGHT_HEMISTICH]: لو بغير الهوى يطاولني الده
[LEFT_HEMISTICH]: ر لأَرْكَزْتُ فِي النجوم قبائي
[RIGHT_HEMISTICH]: وَجَرَّرْتُ بُرْدَ هَوىً على البَد
[LEFT_HEMISTICH]: رِ ولَطَّمْتُ حَدَّهُ بِدُعَابِي

--- END STREAM ---
