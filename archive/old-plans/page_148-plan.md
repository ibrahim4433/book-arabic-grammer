# **SESSION 148**

[TASK DEFINITION]
Objective: Implement page 148.
File: `pages/page_148.html`
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
[LESSON_NUMBER]: 148
[CHAPTER_TITLE]: page 148
[CATEGORY_HEADER]: 148
[SECTION_HEADER]: 148
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: الإجابة الإبداعية ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الإجابة الإبداعية
Content: <span class="text-accent font-bold">الإجابة :</span> إِنَّ رُوحِي المُعَذَّبَةَ تَنْزِعُ إِلَى لِقَاءِ مَحْبُوبَتِي بَعْدَ طُولِ الفراق،ِ فَقَلْبِي مُمَرَّقَ يَتُوقُ إِلَى الوصالِ بَعْدَ طُولِ البَعَاد.ِ كلما لاحَتْ بَارِقَةُ أَمَلِ حصول هذا اللَّقَاءِ تَحْتَدِمُ فِي نَفْسِي لَهْفَةٌ عَارِمَةً لِرؤياهَا، فَأَبْدَأُ بِتَخَيْلِ مَشْهَدِ اللَّقَاء،ِ فَتَرِفُ فِي قَلْبِي مَنَازِعُ الشَّوْق،ِ فَتَجْتَاحُنِي رَغْبَةٌ عارِمَةً بِالقُرْبِ مِنْهَا لأَتَخَلَّصَ مِنْ غَصَّةِ الوَحْشَة،ِ وَمَرَارَةِ اللَّوعَةِ اللَّذَينِ رافَقَانِي طَوَالَ غيابِهَا عَنِّي.<br><br>كَمْ آمَلُ أَنْ يَتَحَقَّقَ هذا اللقاء، عَلَّهُ يُخَفِّفُ معاناتي، ويُنْهِي عَذَابِي فَأَسْتَعِيدُ تِلْكَ الْأَيَّامَ الخَوَالي التي جَمَعَتْنِي بِمَحْبُوبَتِي؛ فهي أَهْنَأُ للبال، وأَكْثَرُ مُتْعَةً للنَّفْسِ لأَنَّهَا كَانَتْ أَيَّامَا عَامِرَةً بِالفَرَح مُفْعَمَةً بِالسَّعَادَة.ِ

=== BLOCK 3: The Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Table Headers: المفهوم | الدلالة النفسية
Row 1: مِنْ ج ٢- الخَبَر | نقل الحالة النَّفْسِيةَ اللَّتِي تَمَلَكَتِ الشَّاعِر،َ وَوَصَفَ حَالَتَهُ الجَسَدِيَّة المزرية،َ وَأَخْبَرَ عَنْ آمَالِهِ وطُمُوحَاتِهِ وَرَغْبَتِهِ بِالتَّخَلُصِ مِنْ معاناته
Row 2: الإنشاء | دلل على حالة الشاعر الانفعالِيَّة،ِ فَأَفْصَحَ عَنْ أَحْزَانِهِ وعَذاباته، وأبان اضطراباتِهِ النَّفْسِيَّةِ.
Row 3: الرمز | تَمَكَّنَتِ الرُّمُوزُ مِنَ الإِفْصَاحِ عَنِ الحالة النفسِيَّةِ التي يحياها، فقد رمز بالحيَّةِ إلى الألم والعَذَابِ اللَّذِينَ يُعاني منهما بِسَبَبٍ مَشَاعِرِ الحب ورمز بالنُّجُومِ إِلَى السَّعَادَةِ التِي يَرْغَبُ بِبُلُوغِها .

=== BLOCK 4: تأثير الصور بمعاناة الشاعر ===
(Component: TEMPLATE_C_LIST.html)
Title: تأثير الصور بمعاناة الشاعر النفسية
- <span class="highlight-blue">يا شعوري، يا حَيَّة:</span> اصطَبَعَتْ هذه الصورة بما أَضْفَاهُ اللَّاشْعُورُ عليها مِنْ آلَامِ ومُعاناة، فَكَانَتْ خَيْرَ مُعَبَرِ عَنْ مُعَانَاةَ الشَّاعِرِ الْمُكْبُوتَةِ،ِ فَكَانَتْ خَيْرَ مُعَبَرِ عَنِ الْمَعَانَاةِ الْجَسَدِيَّةِ في أَعْماقه.
- <span class="highlight-blue">شهد الحب:</span> اصطبَغَتْ هذه الصُّورَةُ بما أَضْفَاهُ اللَّاشُعُورُ عليها مِنْ مُعَانَاةٍ وأحلام، لتجاوز خَيْبَةَ والآلامِ النَّفْسِيَّةِ المَكْبُوتَةِ.ِ
- <span class="highlight-blue">يطاولني الدَّهْرُ بغير الهوى:</span> اصطبَغَتْ هذه الصورة بما أضفاهُ اللاشعُورُ عليها مِنْ آلام الأمل والانكسار أَمَامَ دَهْرِ غَالَبَ الشَّاعِر،َ فَكَانَتْ خَيْرَ مُعَبِّرِ عَمَّا كَانَ مَكْبُوتًا فِي أَعْمَاقِه.ِ

=== BLOCK 5: الموسيقا الداخلية ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: الموسيقا الداخلية والخارجية
Content: جاءَتِ الموسيقا الدَّاخِلِيَّةِ مُتَنَاغِمَةً مُنْسَجِمَةً مَعَ انفعالات الشاعر العاطفية، فالتَّنَاغُمُ والانسجامُ بَيْنَ حُرُوفِ الهَمْسِ وَالجَهْرِ وَافْقَ انفعالات الشاعر وحالته المضطربة. والتناغُمُ بَيْنَ حُرُوفَ المَدِ الطَّوِيلِ وَالمَدِ القَصِيرِ لاءَمَ حالة الأسى التي يحياها، ومكنهُ مِنْ إِخراج الآهات المكبُوتَةِ فِي صَدْرِهِ أَمَّا رَوِي الباءِ المَكْسُورَةِ فَيُشِيرُ إِلَى نَفْسِيَّةِ الشَّاعِرِ الْمُنْكَسِرَة.ِ

=== BLOCK 6: التقطيع العروضي ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Title: ج-٦ تقطيع صَدْرِ البيتِ الأَوَّلِ مِنَ النَّص،َ وتسميةُ بَحْرِهِ البَحْرُ الخفيف.
Content: <div class="text-center">يا حَيَّةٌ تنفُثُ السُّمَّ يا شُعُورِي<br>فاعلاتن مستفعلن فاعلاتن</div>

=== BLOCK 7: التعبير الكتابي (فدوى طوقان) ===
(Component: TEMPLATE_C_POEM.html)
Title: التعبير الكتابي
Poet: فدوى طوقان(
Hemistich 1: يا شُعُوري يا حَيَّةً تَنْفُثُ السُّمَّ
Hemistich 2: فَيَجْرِي فِي القَلْبِ مِنْ أَلْفِ نَابِ
Hemistich 3: كَبْرَتِ فِيكَ عِلْتِي وَتَناهي
Hemistich 4: فيك حزني، وطال فيكَ عَذَابِي
Hemistich 5: لو بغير الهوى يطاولني الدهـ
Hemistich 6: ـر لأَرْكَزْتُ فِي النجوم قبائي
Hemistich 7: وَجَرَّرْتُ بُرْدَ هَوَايَ على البد
Hemistich 8: رِ ولَطَّمْتُ حَدَّهُ بِدُعَابِي

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: ما دَوْرُ كُلِّ مِنَ الخَبَرِ والإِنْشَاءِ فِي تَفسير الحالةِ الشَّعُورِيَّةِ التِي تَكْتَنِفُ الشَّاعِر.َ
Number: ٢
Question: استَعْمَلَ الشَّاعِرُ الرُّمُوزَ بَيِّنْ أَثَرَهَا فِي التَّعْبِيرِ عَنْ حالاتِهِ النَّفْسِيَّة،ِ مَعَ مِثَالٍ مُنَاسِبِ لِذَلِك.َ
Number: ٣
Question: تأثَرَتِ الصور بمعاناةِ الشَّاعِرِ النَّفْسِيَّة،ِ وأمانيهِ المَكْبُوتَةِ فِي اللاشُعُورِ - مَثِّلْ لِكُلِّ مِنْهُما، مُبَيِّنَا مَا عَكَسَتْهُ مِنْ أَحَاسِيسَ وَرَغَبَاتٍ مُخْتَزَنَةٍ لَدَى الشَّاعِرِ .
Number: ٤
Question: : ه- جاءت الموسيقا الداخلية والخارجية استجابة لانفعالاتِ الشَّاعِرِ الْمُحْتَدِمَة.ِ ادرُسُ ذَلِكَ مِنْ خلال عناصر الموسيقا الدَّاخِلِيَّةِ - روي الباءِ المَكْسُورَة(.
Number: ٥
Question: - قَطَعْ عروضِيًّا صَدْرَ البيتِ الأَوَّل،ِ ثُمَّ سَمَ بَحْرَه.ُ
Number: ٦
Question: المستوى الإبداعي: كَشَفَ المَقْطَعُ الثَّانِي عَنْ أَماني الشَّاعِرِ الخَبِيئَة.ِ أضف ما تراهُ مُناسبًا مِنْ أُمنيات أخرى مُوَظِّفاً الْأَسْلُوبَ السَّرْدِي.
Number: ٧
Question: التعبير الكتابي: ادرس الأبيات الآتية من النَّصَ وَفَقَ المَنْهَجِ النَّفْسِي، مُستَفِيدًا مِنْ إِجابتِكَ عَنْ أَسْئِلَةِ الْمُسْتَوَيَيْنِ الْفِكْرِيِّ والفني، وَمَا مَرَّ فِي نَصَ *

--- END STREAM ---
