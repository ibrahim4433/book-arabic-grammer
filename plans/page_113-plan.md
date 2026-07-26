# **SESSION 113**

[TASK DEFINITION]
Objective: Implement page 113.
File: `pages/page_113.html` (Note: Use the exact page number.)
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
[UNIQUE_ID]: b21783
[LESSON_NUMBER]: 113
[CHAPTER_TITLE]: page 113
[CATEGORY_HEADER]: 113
[SECTION_HEADER]: 113
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Verse 19 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b21784
Title: البيت التاسع عشر
Right: -١٩ أينما جال بنا الطرف انثنى
Left: وطيوف الزهو فوق الهدب

=== BLOCK 3: Vocabulary 19 ===
(Component: TEMPLATE_C_TABLE.html)
[UNIQUE_ID]: b21785
Title: مفردات البيت
Headers: الكلمة, معناها
Row 1: انثنى, الحنى، وارتد، وتمايل، وتَبَخْتَر.َ
Row 2: زها, تاه وتعاظم وافتخر
Row 3: الزهو, الكِبَر.ُ ويُرِيدُ هنا الفرح والفخر

=== BLOCK 4: دراسة البيت 19 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b21786
Title: الشرح والبلاغة
Content:
<span class="text-accent">الشرح</span> أينما تَجَوَّلنا بأبصارنا في ربوع الوَطَنِ تَمَايَلَتْ أبصارنا وتَبَخْتَرَتْ والفَرَحُ والفَخْرُ يَعْلوان أهداتها
<span class="text-accent">الشعور</span> فرح <span class="text-accent">الأداة:</span> التَّراكيب <span class="text-accent">المثال:</span> طيوف الزهو فوق الهدب
<span class="text-accent">البلاغة :</span> )الطرف انثنى( استعارَةٌ مَكْنِيَّة

=== BLOCK 5: إعراب البيت التاسع عشر ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b21787
Title: الإعراب
Word 1: أينما
Role 1: اسم شرط جازم مَبْنِي على الفتح في حَلِّ نَصْبِ مَفْعُولٌ فِيهِ ظرف مكان. وما زائدة.
Word 2: جال بنا الطرف(
Role 2: في محل جر بالإضافة.
Word 3: انثني(
Role 3: جملة جواب الشَّرْطِ لا محل لها مِنَ الإعراب
Word 4: طيوف:
Role 4: مُبْتَدَاً مَرْفُوع.
Word 5: فوق :
Role 5: مَفْعُولٌ فِيهِ ظَرْفُ مكانٍ مَنْصُوبُ
Word 6: الزهو ، الهدب :
Role 6: مُضاف إِلَيْهِ مَجْرُورٌ
Word 7: طيوفُ الزهو فوق الهدب
Role 7: في محل نصب حال.

=== BLOCK 6: Verse 20 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b21788
Title: البيت العشرون
Right: ۲۰- فلنصنْ مِنْ حَرم الملك لها
Left: منبر الحقد وسيف الغضب

=== BLOCK 7: دراسة البيت 20 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b21789
Title: الشرح والمفردات
Content:
<span class="text-accent">المفردات</span> نصن: صانَ حَفظ في مكان أمين منبر : اسم آلَة.ٍ
<span class="text-accent">الشرح :</span> فَلْنَحْم هذه التربَةَ الطَّاهِرَة، ولُنُحَافِظُ مِنْ أَجْلِهَا عَلَى مَوَاقِفِنَا الْمُعَادِيَةِ لِلْمُسْتَعْمِر الذي استباح حُرْمَةَ هذه التربة، ولنُبْقِ سَيُوفَنَا مُشْرَعَةً فِي وَجْهِه.
<span class="text-accent">البلاغة:</span> منبر الحقد(، )سيف الغضب(: تَشْبِيهُ بَلِيْعٌ إضافي.

=== BLOCK 8: إعراب البيت العشرين ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID]: b21790
Title: الإعراب
Word 1: فلتصن:
Role 1: الفاء: حَرْفُ استئناف الام: حَرْفٌ جَازِمْ نَصَنَّ فِعُلْ مُضَارِعٌ تَجْزُوم
Word 2: منبر :
Role 2: مَفْعُولُ بِهِ مَنْصُوبٌ
Word 3: سيف :
Role 3: اسمٌ مَعْطُوف مَنْصُوبُ
Word 4: الحقد، الغضب :
Role 4: مُصَافُ إِلَيْهِ مَجْرُور.ٌ

=== BLOCK 9: Verse 21 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b21791
Title: البيت الحادي والعشرون
Right: -٢١ ولنسل حنجرة الشدو بها
Left: بين أطلال الضحايا الغيب

=== BLOCK 10: دراسة البيت 21 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b21792
Title: الشرح
Content:
<span class="text-accent">الشرح</span> ولْتَبْقَ حَناجِرُنَا مُشِيْدَةً بهذه التَّرْبَةِ الطَّاهِرَة،ِ مُمَجَدَةَ دِمَاءَ الشَّهَدَاءِ التِي طَهَّرَقًا مِنْ دَنَسِ الْمُسْتَعْمِرِين

=== BLOCK 11: إعراب البيت الحادي والعشرين ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID]: b21793
Title: الإعراب
Word 1: لتسل:
Role 1: الام: حَرْفٌ جازم نسل : فعل مضارع تجزوم.
Word 2: حنجرة :
Role 2: مَفْعُولُ بِهِ مَنْصُوبٌ
Word 3: الشدو، أطلال، الضحايا :
Role 3: مُضافَ إِلَيْهِ مَجْرُورٌ
Word 4: الغيبِ :
Role 4: صِفَةً مَجْرُورَة.ٌ

=== BLOCK 12: Verse 22 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b21794
Title: البيت الثاني والعشرون
Right: ۲۲- صلت الأمة إن أرخت على
Left: جرح ماضيها كثيف الحجب

=== BLOCK 13: الفكرة ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[UNIQUE_ID]: b21795
Title: الفكرة
Content:
التغاضي عن آلام الماضي يؤدي إلى الضياع

=== BLOCK 14: دراسة البيت 22 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b21796
Title: الشرح والمفردات
Content:
<span class="text-accent">المفردات:</span> صَلَّتِ : ضَكَ صَلَّا، وضلالا، وضلالة: ضاعَ رَلَّ عَنِ الشَّيْءٍ ولم يَهْتَدِ إليه. والضَّلال:ُ العُدُولُ عَنِ الطَّريق المستقيم عَمَّدًا أو سَهْوًا
<span class="text-accent">الشرح :</span> تَتِيْهُ الأَمَّةُ وَتَضِيعُ وَتَحِيدُ عَنِ الطَّرِيقِ المستقيم إذا أَغْمَضَتْ عَيْنَهَا عَنْ آلَامِهَا المَاضِيَة، وغَضَتِ الطَّرْفَ عَنْ نَكَبَاتِهَا السَّالِفَة وتَغَاضَتْ عَنها.
<span class="text-accent">البلاغة</span> جرح ماضيها(: تشبيه بَلِيعٌ إضافي

=== BLOCK 15: إعراب البيت الثاني والعشرين ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID]: b21797
Title: الإعراب
Word 1: إن :
Role 1: حَرْفُ شَرْطِ جازم
Word 2: ماضيها الحجب :
Role 2: مُضَافُ إِلَيْهِ مَجْرُور.ٌ

=== BLOCK 16: Verse 23 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b21798
Title: البيت الثالث والعشرون
Right: -٢٣ ما بَلَغْنَا بَعْدُ مِنْ أَخلامِنا ذلك
Left: الحلمَ الكَرِيمَ الذَّهَي

=== BLOCK 17: الشرح 23 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b21799
Title: الشرح
Content:
<span class="text-accent">الشرح</span> حَتَّقْنَا بَعْضًا مِنْ أَحلامنا لكننا إلى الآن لم تحقق ذلك الحلم العظيم الذي لطالما حلمنا بتحقيقه

=== BLOCK 18: إعراب البيت الثالث والعشرين ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b21800
Title: الإعراب
Word 1: بَعْد :
Role 1: ظَرْفُ زمانٍ مَقْطُوع عَنِ الإضافةِ مَبْنِي على الضَّمَ فِي مَحَلِّ نَصْب.
Word 2: ذَلِكَ :
Role 2: اسم إشارة في محل نصب مَفْعُول به.
Word 3: الحلم :
Role 3: بَدَلْ مَنْصُوبُ
Word 4: الكَرِيمَ الذَّهَبِي :
Role 4: صِفَةٌ مَنْصُوبَة.ٌ

=== BLOCK 19: Verse 24 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b21801
Title: البيت الرابع والعشرون
Right: -٢٤ أين في القدس ضلوع غضة
Left: لم تلامشها ذنابي عقرب؟

=== BLOCK 20: دراسة البيت 24 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b21802
Title: الشرح والمفردات
Content:
<span class="text-accent">المفردات:</span> غَضَةُ الغَضُ الطري الحديث مِنْ كُلِّ شيء. وغة صِفَةٌ مُشَبَّهَةٌ باسم الفاعل ذنابي: الذَّنب
<span class="text-accent">الشرح</span> لا يوجد في أي بُقْعَةٍ مِنْ بِقَاعِ القُدْسِ طِفْلِّ سَلِمَ مِنْ أَذِي الاحتلال الصهيوني، فهذا المُحْتَلُ عَقْرَبٌ لَم يَسْلَمْ طِفْلٌ مِنْ أَطْفَالِ القُدْسِ مِنْ لَسْعِ ذَنَبِه.ِ

=== BLOCK 21: إعراب البيت الرابع والعشرين ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b21803
Title: الإعراب
Word 1: أين
Role 1: اسم استفهام فِي مَحَلَ نَصْبَ مَفْعُولٌ فِيهِ ظَرْفُ مَكَانٍ مُتَعَلِّقٌ بِخَبَرِ مُقَدَّم.
Word 2: ضلوع :
Role 2: مُبْتَدَاً مَرْفُوعٌ
Word 3: غَضَةٌ
Role 3: صِفَةٌ مَرْفُوعَةٌ
Word 4: ذناي:
Role 4: فَاعِلَ مرفوع.
Word 5: لم تلامشها ذنابي عقرب(:
Role 5: فِي مَحَلِّ رَفْعِ صِفَة.

=== BLOCK 22: Verse 25 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b21804
Title: البيت الخامس والعشرون
Right: -٢٥ وقف التاريخ في محرابها
Left: وقفة المرتجف المضطرب

=== BLOCK 23: دراسة البيت 25 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b21805
Title: الشرح والمفردات
Content:
<span class="text-accent">المفردات</span> محرابها المحراب الغرفة، والقصر المرتجف المضطرب اسم فاعل، والفعل على الترتيب: ارتجف، اضطرب.
<span class="text-accent">الشرح</span> وقف التاريخ أمام الجرائم التي يرتكبها الصَّهَائِنَةُ بِحَقِّ أبناء القُدْسِ مَفْرُوعًا مُضْطَربًا.
<span class="text-accent">البلاغة:</span> وقف التاريخ استعارَةٌ مِكْنِيَّة.ٌ

=== BLOCK 24: إعراب البيت الخامس والعشرين ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID]: b21806
Title: الإعراب
Word 1: وقفة :
Role 1: مَفْعُولُ مُطْلَقَ منصوب
Word 2: المرتجف :
Role 2: مضاف إلَيْهِ مَجْرُورٌ
Word 3: المضطرب :
Role 3: صِفَةً مَجْرُورَة.ٌ

=== BLOCK 25: Verse 26 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b21807
Title: البيت السادس والعشرون
Right: -٢٦ كم روى عنها أناشيد التهي في
Left: سماع العالم المستغرب

=== BLOCK 26: دراسة البيت 26 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b21808
Title: الشرح والمفردات
Content:
<span class="text-accent">المفردات :</span> النَّهَى المُفْرَدُ : النَّهْيَةُ : وهي: العَقْلُ المستغرب : اسم فاعِلِ فِعْلُهُ استَغْرَبَ
<span class="text-accent">الشرح :</span> روى التاريخ الكثيرَ مِنَ الجرائِمِ البَشِعَةِ التي ارتكبها الصَّهَائِنَةُ بِحَقِّ أبناء القدس، وحينما لا مَسَتْ أسماع العالم، وَقَفَ العالم مَدْهُولا مُسْتَغْربا .

=== BLOCK 27: إعراب البيت السادس والعشرين ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[UNIQUE_ID]: b21809
Title: الإعراب
Word 1: كَمْ :
Role 1: خَبَرَيَّةٌ مَبْنِيَّةٌ على السكون في محلِّ نَصْبِ مَفْعُولُ مُطْلَق
Word 2: النهي العالم :
Role 2: مضاف إليه مجرور
Word 3: المستغرب :
Role 3: صِفَةٌ تَجْرُورَة.ٌ

--- END STREAM ---
