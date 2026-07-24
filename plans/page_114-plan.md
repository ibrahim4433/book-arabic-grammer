# **SESSION 114**

[TASK DEFINITION]
Objective: Implement page 114.
File: `pages/page_114.html` (Note: Use the exact page number.)
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
[LESSON_NUMBER]: 114
[CHAPTER_TITLE]: page 114
[CATEGORY_HEADER]: 114
[SECTION_HEADER]: 114
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Cut Box Part 2 ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
Title: تتمة
Content:
- أ.

=== BLOCK 3: Verse 27 ===
(Component: TEMPLATE_C_POEM.html)
Verses:
٢٧- أي أنشودة خزي غص في
بنها بين الأسى والكرب

=== BLOCK 4: Analysis 27 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: شرح البيت السابع والعشرين
Content:
<span class="text-accent font-bold">المفردات:</span> الكرب مفردها الكُرْبَة،ُ (الكَرْبُ): الحزن والغَم. خزي: خَزِي الرَّجُلُ ما أبقى مِنْ نَفْسِه،ِ استحيا، وخَجِلَ مِنها.
<span class="text-accent font-bold">الشرح:</span> التاريخ جريمة مُخْزِيَةً مُخْجِلَةً مِنَ الجَرَائِمِ التِي اقْتَرَفَهَا الصَّهَابِنَةً بِحَقِّ الفلسطينيين وجَلَبَتْ لَهُم الحزن والهموم، إلا رواها وكشفها للعالم.
<span class="text-accent font-bold">البلاغة:</span> (أنشودة خزي): تشبيه بليغ إضافي.
<span class="text-accent font-bold">الإعراب:</span> أي: اسم استفهام، مُبْتَدَاً مَرْفُوع. أنشودة، خزي، الأسى: مُضَافَ إِلَيْهِ تَجْرُور.ٌ

=== BLOCK 5: Verse 28 ===
(Component: TEMPLATE_C_POEM.html)
Verses:
٢٨- ما لأبناء السبايا ركبوا
للأماني البيض أشهى مركــــــــب

=== BLOCK 6: Analysis 28 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: شرح البيت الثامن والعشرين
Content:
<span class="text-accent font-bold">المفردات:</span> السبايا المفرد: السبيَّة والسبي: المأسور. ويريد هنا بأبناء السبايا: اليهود. مِن أبناء سبايا الأمم البيض: صِفَةٌ مُشَبَّهَةٌ باسم الفاعل. أشهى: اسم تفضيل.
<span class="text-accent font-bold">الشرح:</span> ما بال اليهود قد بالغُوا في أحلامهم، وتمادوا في أُمْنِياتِهِم وَطَمَحُوا لِبلوغِ مُسْتَقْبَلٍ عَظِيمٍ فَوْقَ تَرِى بلادنا العربية.
<span class="text-accent font-bold">الإعراب:</span> ما: اسم استفهام فِي مَحَلِ رَفْع مُبْتَدَا. (رَكَبُوا): في مَحَلَّ نَصْب حال. الْبِيضِ: صِفَةً مَجْرُورَةٌ. أَشهى: مَفْعُولُ بِهِ مَنْصُوب.ٌ مركب: مضاف إليهِ مَجْرُورٌ.

=== BLOCK 7: Verse 29 ===
(Component: TEMPLATE_C_POEM.html)
Verses:
٢٩- ومتى هروا علينا رايةً
ما انطوت بين رخيص السَّلَبِ؟

=== BLOCK 8: Analysis 29 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: شرح البيت التاسع والعشرين
Content:
<span class="text-accent font-bold">الشرح:</span> مَا سَبَقَ لِلْيَهُودِ أن غارُوا علينا وخاضوا ضِدَّنَا حَرْبًا، إِلَّا هَزَمْنَاهُم وَانْتَصَرْنَا عَلَيْهِم وَطَوَيْنَا أَعْلَامَهِم مَعَ مَا غَنِمْنَاهُ مِنْهُم.
<span class="text-accent font-bold">الإعراب:</span> متى: اسم استفهام في محل نصب ظرف زمان. (ما انطوت): في محل نصب صفة راية. رخيص: صِفَةً مُشَبَّهَةٌ باسم الفاعل. السلب: مُضَافُ إِلَيْهِ مَجْرُور.ٌ

=== BLOCK 9: Verse 30 ===
(Component: TEMPLATE_C_POEM.html)
Verses:
٣٠- ومن الطاعي الذي مد لهم
من سراب الحق أوهی سبب؟

=== BLOCK 10: Analysis 30 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: شرح البيت الثلاثين
Content:
<span class="text-accent font-bold">المفردات:</span> الطَّاغِي: الظَّالم، والطَّاغِيَةُ العَظِيم الظُّلم، الكثير الطغيان. والطَّاغِي: اسم فاعل. أوهى: أضعف، وأوهى اسم تفضيل.
<span class="text-accent font-bold">الشرح:</span> من هذا الظَّالم الذي أَبَاحَ لِلْيَهُودِ أَنْ يَحْتَلُوا أَرْضَنا دونَ وَجْهِ حَق، وَسَوَّغَ لَهُم هذا الاحتلال، وأمدهم بِشَرْعِيَّتِهِ.
<span class="text-accent font-bold">البلاغة:</span> (سراب الحق): تشبيه بليغ إضافي.
<span class="text-accent font-bold">الإعراب:</span> من: اسم استفهام فِي مَحَلَّ رَفْعِ مُبْتَدَأ. الطَّاغِي: خَبَرَ مَرْفُوعٌ. الذي: اسمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعِ صفة. (مد): صِلَةُ المَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الإعراب. الحق، سبب: مُضَافُ إِلَيْهِ مَجْرُورٌ. أوهى: مَفْعُولُ بِهِ مَنْصُوب.ٌ

=== BLOCK 11: Verse 31 ===
(Component: TEMPLATE_C_POEM.html)
Verses:
٣١- أو ما كنا له في خطبه
مَعُقل الأمن وجسر الهرب؟

=== BLOCK 12: Analysis 31 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: شرح البيت الحادي والثلاثين
Content:
<span class="text-accent font-bold">المفردات:</span> خطبه: الخطب المكروه. معقل: اسم مكان.
<span class="text-accent font-bold">الشرح:</span> ألم نَكُنْ لَهُ فِي شِدَّتِهِ وَكَرْبِهِ مَلَاذَا آمِنَا يَأْوِي إِلَيْهِ لِيَنْعَمَ بِالْأَمْن،ِ وَطَرِيقًا يَسْلُكَهُ لِيَنْجُو مِنَ الأَخْطَارِ المحدِقَةِ به.
<span class="text-accent font-bold">الإعراب:</span> أ: الهَمْزَةُ حَرْفُ استفهام. و: الواو حرف زائد. ما: حَرْفُ نَفي. مَعْقَلَ: خَبَرَ كَانَ مَنْصُوب.ٌ الأمن، الهرب: مُضَافُ إِلَيْهِ مَجْرُورٌ.

=== BLOCK 13: Verse 32 ===
(Component: TEMPLATE_C_POEM.html)
Verses:
٣٢- ما لنا لمح في مشيته
مجلب الذئب وجلد التَّغْلب؟

=== BLOCK 14: Analysis 32 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: شرح البيت الثاني والثلاثين
Content:
<span class="text-accent font-bold">المفردات:</span> مجلب / مخلب: اسم آلة.
<span class="text-accent font-bold">الشرح:</span> تبدو لنا فِي هَيْئَتِهِ حِينَمَا نُبْصِرُهُ مَاشِيَا مَلامِحُ الوَحْشِيَّة،ِ ومعالم المكر والحيل والخداع.
<span class="text-accent font-bold">البلاغة:</span> (مجلب الذَّئب): كِنايَةً عَنِ الوَحْشِيَّة.ِ (جلد التَّعْلَبِ): كِنَايَةً عَنِ المكر والخداع.
<span class="text-accent font-bold">الإعراب:</span> ما: اسم استفهام فِي مَحَلِّ رَفْعِ مُبْتَدَأ. (نلمح): في محل نصب حال. مِخْلَب: مَفْعُولُ بِهِ مَنْصُوبُ. الذَّئب، التَّعْلَبِ: مُضَافُ إِلَيْهِ مَجْرُور.ٌ

=== BLOCK 15: Verse 33 ===
(Component: TEMPLATE_C_POEM.html)
Verses:
٣٣- يا لذل العهد إن أغضى أسى
فوق صَدْرِ الشَّرف المنتحب

=== BLOCK 16: Analysis 33 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: شرح البيت الثالث والثلاثين
Content:
<span class="text-accent font-bold">المفردات:</span> أغضى: أغضى فلان: قارب بينَ أَجْفَانِهِ وأَغْضَى عَيْنَهُ. المنتحب: اسم فاعل.
<span class="text-accent font-bold">الشرح:</span> يا للعار ويا للذل الذي سَيُلَطَخُهُ إِنْ تناسى سَيُكَلِّلُ جَبِينَ الإنسان العربي، وتنصَّلَ مِنَ العَهْدَ الذي قَطَعَهُ لِفِلَسْطِينَ وَغَضَ الطَّرْفَ عَنْه،ُ وَحَوَّلَهُ عَنْهُ الدفاع.
<span class="text-accent font-bold">البلاغة:</span> (العهد أغضي)، (صَدْرِ الشَّرْفِ)، (الشرف المنتحب): استعارةً مَكْنِية.
<span class="text-accent font-bold">الإعراب:</span> العَهْد،ِ صَدْرِ الشَّرْفِ: مضافُ إِلَيْهِ مَجْرُورٌ. أسى: مَفْعُولٌ لأَجْلِهِ مَنْصُوبٌ. فوق: مَفْعُولٌ فِيهِ ظَرْفُ مكان منصوب. المنتحب: صفة مجرُورَة.ٌ

=== BLOCK 17: Verse 34 ===
(Component: TEMPLATE_C_POEM.html)
Verses:
٣٤- يا روابي القدس يا مجلى السنا
يا رؤى عيسى على جفن النبي

=== BLOCK 18: Analysis 34 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: شرح البيت الرابع والثلاثين
Content:
<span class="text-accent font-bold">المفردات:</span> السنا: الضوء السَّاطِعُ.
<span class="text-accent font-bold">الشرح:</span> يا مرتفعات فلسطين الحبيبة، يَا مَنْ كُنْتِ مَهْبَطَ الرسالات السماوية، أَشْرَقَتْ على تراك الأنوارُ الإِلَهِيَّة،ٌ.
<span class="text-accent font-bold">الإعراب:</span> روابي، القدس، مجلى، السنا، رؤى، عيسى، النبي: منادى مضاف منصوب / مُضافُ إِلَيْهِ مَجْرُور.ٌ

=== BLOCK 19: Verse 35 ===
(Component: TEMPLATE_C_POEM.html)
Verses:
٣٥- دون عليائك في الرحب المدى صهلة
الخيل ووهج القضب

=== BLOCK 20: Analysis 35 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: شرح البيت الخامس والثلاثين
Content:
<span class="text-accent font-bold">المفردات:</span> القضب: السُّيُوفُ القَطَاعَةُ.
<span class="text-accent font-bold">الشرح:</span> انتظري نَجْدَتَنَا سَتَجْعَلُ خُيُولَنَا مِنْ بَرَائِنِ العدوان وَأَسْلِحَتَنَا دِرْعًا حاميًا لك،ِ ومُخَلِّصًا لَكِ.
<span class="text-accent font-bold">الإعراب:</span> دونَ: مَفْعُولُ فِيهِ ظَرْفُ مكانٍ مَنْصُوب. عليائك، الخيل، القضب: مُضافُ إِلَيْهِ مَجْرُور. المدى: صِفَةً مَجْرُورَة.ٌ صهلة: مُبْتَدَاً مرفوع. وهج: اسمٌ مَعْطُوفٌ مَرْفُوع.ُ

=== BLOCK 21: Table / Matrix Summary ===
(Component: TEMPLATE_C_TABLE.html)
Title: خلاصة الإعراب
Headers: الكلمة | إعرابها
Rows:
أشهى | مفعول به منصوب
رخيص | صفة مشبهة باسم الفاعل
أوهى | مفعول به منصوب
معقل | خبر كان منصوب

=== BLOCK 22: Extra Symbols ===
(Component: TEMPLATE_C_BENEFIT.html)
Title: ملاحظة
Content:
- -
كمة
- -

--- END STREAM ---
