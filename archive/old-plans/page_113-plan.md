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
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
15. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 113
[CHAPTER_TITLE]: page 113
[CATEGORY_HEADER]: 113
[SECTION_HEADER]: 113
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: البيت التاسع عشر ===
(Component: TEMPLATE_C_BLOCK.html)
Title: البيت التاسع عشر
Content:
(Component: TEMPLATE_C_POEM.html)
-١٩ أينما جال بنا الطرف انثنى وطيوف الزهو فوق الهدب
(Component: TEMPLATE_C_BLOCK.html)
المفردات: انثنى: انحنى، وارتد، وتمايل، وتَبَخْتَر.َ زها : تاه وتعاظم وافتخر الزهو: الكِبَر.ُ ويُرِيدُ هنا الفرح والفخر.
الشرح: أينما تَجَوَّلنا بأبصارنا في ربوع الوَطَنِ تَمَايَلَتْ أبصارنا وتَبَخْتَرَتْ والفَرَحُ والفَخْرُ يَعْلوان أهدابها.
الشعور: فرح الأداة: التَّراكيب المثال: طيوف الزهو فوق الهدب.
البلاغة: (الطرف انثنى) استعارَةٌ مَكْنِيَّة.
(Component: TEMPLATE_C_IRAB.html)
Target: أينما
Role: اسم شرط جازم مَبْنِي على الفتح في حَلِّ نَصْبِ مَفْعُولٌ فِيهِ ظرف مكان. وما زائدة.
Target: (جال بنا الطرف)
Role: في محل جر بالإضافة.
Target: (انثنى)
Role: جملة جواب الشَّرْطِ لا محل لها مِنَ الإعراب
Target: طيوف
Role: مُبْتَدَاً مَرْفُوع.
Target: فوق
Role: مَفْعُولٌ فِيهِ ظَرْفُ مكانٍ مَنْصُوبُ
Target: الزهو ، الهدب
Role: مُضاف إِلَيْهِ مَجْرُورٌ
Target: طيوفُ الزهو فوق الهدب
Role: في محل نصب حال.

=== BLOCK 3: البيت العشرون ===
(Component: TEMPLATE_C_BLOCK.html)
Title: البيت العشرون
Content:
(Component: TEMPLATE_C_POEM.html)
۲۰- فلنصنْ مِنْ حَرم الملك لها منبر الحقد وسيف الغضب
(Component: TEMPLATE_C_BLOCK.html)
المفردات: نصن: صانَ حَفظ في مكان أمين منبر : اسم آلَة.ٍ
الشرح: فَلْنَحْم هذه التربَةَ الطَّاهِرَة، ولُنُحَافِظُ مِنْ أَجْلِهَا عَلَى مَوَاقِفِنَا الْمُعَادِيَةِ لِلْمُسْتَعْمِر الذي استباح حُرْمَةَ هذه التربة، ولنُبْقِ سَيُوفَنَا مُشْرَعَةً فِي وَجْهِه.
البلاغة: (منبر الحقد)، (سيف الغضب): تَشْبِيهُ بَلِيْعٌ إضافي.
(Component: TEMPLATE_C_IRAB.html)
Target: فلنصن
Role: الفاء: حَرْفُ استئناف اللام: حَرْفٌ جَازِمْ نصن: فِعْلٌ مُضَارِعٌ مَجْزُوم
Target: منبر
Role: مَفْعُولُ بِهِ مَنْصُوبٌ
Target: سيف
Role: اسمٌ مَعْطُوف مَنْصُوبُ
Target: الحقد، الغضب
Role: مُضَافُ إِلَيْهِ مَجْرُور.ٌ

=== BLOCK 4: البيت الحادي والعشرون ===
(Component: TEMPLATE_C_BLOCK.html)
Title: البيت الحادي والعشرون
Content:
(Component: TEMPLATE_C_POEM.html)
-٢١ ولنسل حنجرة الشدو بها بين أطلال الضحايا الغيب
(Component: TEMPLATE_C_BLOCK.html)
الشرح: ولْتَبْقَ حَناجِرُنَا مُشِيْدَةً بهذه التَّرْبَةِ الطَّاهِرَة،ِ مُمَجَدَةَ دِمَاءَ الشَّهَدَاءِ التِي طَهَّرَتْهَا مِنْ دَنَسِ الْمُسْتَعْمِرِين.
(Component: TEMPLATE_C_IRAB.html)
Target: لنسل
Role: اللام: حَرْفٌ جازم نسل : فعل مضارع مجزوم.
Target: حنجرة
Role: مَفْعُولُ بِهِ مَنْصُوبٌ
Target: الشدو، أطلال، الضحايا
Role: مُضافَ إِلَيْهِ مَجْرُورٌ
Target: الغيبِ
Role: صِفَةً مَجْرُورَة.ٌ

=== BLOCK 5: البيت الثاني والعشرون ===
(Component: TEMPLATE_C_BLOCK.html with .block-header.accent)
Title: البيت الثاني والعشرون
Content:
(Component: TEMPLATE_C_POEM.html)
۲۲- ضلت الأمة إن أرخت على جرح ماضيها كثيف الحجب
(Component: TEMPLATE_C_BLOCK.html)
المفردات: ضَلَّتِ : ضَلَّ ضَلالاً، وضلالة: ضاعَ زَلَّ عَنِ الشَّيْءٍ ولم يَهْتَدِ إليه. والضَّلال:ُ العُدُولُ عَنِ الطَّريق المستقيم عَمَّدًا أو سَهْوًا.
الشرح: تَتِيْهُ الأَمَّةُ وَتَضِيعُ وَتَحِيدُ عَنِ الطَّرِيقِ المستقيم إذا أَغْمَضَتْ عَيْنَهَا عَنْ آلَامِهَا المَاضِيَة، وغَضَتِ الطَّرْفَ عَنْ نَكَبَاتِهَا السَّالِفَة وتَغَاضَتْ عَنها.
الفكرة: التغاضي عن آلام الماضي يؤدي إلى الضياع.
البلاغة: (جرح ماضيها): تشبيه بَلِيعٌ إضافي.
(Component: TEMPLATE_C_IRAB.html)
Target: إن
Role: حَرْفُ شَرْطِ جازم
Target: ماضيها، الحجب
Role: مُضَافُ إِلَيْهِ مَجْرُور.ٌ

=== BLOCK 6: البيت الثالث والعشرون ===
(Component: TEMPLATE_C_BLOCK.html)
Title: البيت الثالث والعشرون
Content:
(Component: TEMPLATE_C_POEM.html)
-٢٣ ما بَلَغْنَا بَعْدُ مِنْ أَحلامِنا ذلك الحلمَ الكَرِيمَ الذَّهَبِي
(Component: TEMPLATE_C_BLOCK.html)
الشرح: حَقَّقْنَا بَعْضًا مِنْ أَحلامنا لكننا إلى الآن لم نحقق ذلك الحلم العظيم الذي لطالما حلمنا بتحقيقه.
(Component: TEMPLATE_C_IRAB.html)
Target: بَعْدُ
Role: ظَرْفُ زمانٍ مَقْطُوع عَنِ الإضافةِ مَبْنِي على الضَّمَ فِي مَحَلِّ نَصْب.
Target: ذَلِكَ
Role: اسم إشارة في محل نصب مَفْعُول به.
Target: الحلمَ
Role: بَدَلْ مَنْصُوبُ
Target: الكَرِيمَ، الذَّهَبِي
Role: صِفَةٌ مَنْصُوبَة.ٌ

=== BLOCK 7: البيت الرابع والعشرون ===
(Component: TEMPLATE_C_BLOCK.html)
Title: البيت الرابع والعشرون
Content:
(Component: TEMPLATE_C_POEM.html)
-٢٤ أين في القدس ضلوع غضة لم تلامسها ذنابى عقرب؟
(Component: TEMPLATE_C_BLOCK.html)
المفردات: غَضَّةٌ: الغَضُّ الطري الحديث مِنْ كُلِّ شيء. وغضَّةٌ: صِفَةٌ مُشَبَّهَةٌ باسم الفاعل. ذنابى: الذَّنب.
الشرح: لا يوجد في أي بُقْعَةٍ مِنْ بِقَاعِ القُدْسِ طِفْلٌ سَلِمَ مِنْ أَذَى الاحتلال الصهيوني، فهذا المُحْتَلُ عَقْرَبٌ لَم يَسْلَمْ طِفْلٌ مِنْ أَطْفَالِ القُدْسِ مِنْ لَسْعِ ذَنَبِه.ِ
(Component: TEMPLATE_C_IRAB.html)
Target: أين
Role: اسم استفهام فِي مَحَلَ نَصْبَ مَفْعُولٌ فِيهِ ظَرْفُ مَكَانٍ مُتَعَلِّقٌ بِخَبَرِ مُقَدَّم.
Target: ضلوع
Role: مُبْتَدَاً مَرْفُوعٌ
Target: غَضَّةٌ
Role: صِفَةٌ مَرْفُوعَةٌ
Target: ذنابى
Role: فَاعِلَ مرفوع.
Target: (لم تلامسها ذنابى عقرب)
Role: فِي مَحَلِّ رَفْعِ صِفَة.

=== BLOCK 8: البيت الخامس والعشرون ===
(Component: TEMPLATE_C_BLOCK.html)
Title: البيت الخامس والعشرون
Content:
(Component: TEMPLATE_C_POEM.html)
-٢٥ وقف التاريخ في محرابها وقفة المرتجف المضطرب
(Component: TEMPLATE_C_BLOCK.html)
المفردات: محرابها: المحراب الغرفة، والقصر. المرتجف، المضطرب: اسم فاعل، والفعل على الترتيب: ارتجف، اضطرب.
الشرح: وقف التاريخ أمام الجرائم التي يرتكبها الصَّهَائِنَةُ بِحَقِّ أبناء القُدْسِ مَفْزُوعًا مُضْطَرِبًا.
البلاغة: (وقف التاريخ): استعارَةٌ مِكْنِيَّة.ٌ
(Component: TEMPLATE_C_IRAB.html)
Target: وقفة
Role: مَفْعُولُ مُطْلَقَ منصوب
Target: المرتجف
Role: مضاف إلَيْهِ مَجْرُورٌ
Target: المضطرب
Role: صِفَةً مَجْرُورَة.ٌ

=== BLOCK 9: البيت السادس والعشرون ===
(Component: TEMPLATE_C_BLOCK.html)
Title: البيت السادس والعشرون
Content:
(Component: TEMPLATE_C_POEM.html)
-٢٦ كم روى عنها أناشيد النُّهى في سماع العالم المستغرب
(Component: TEMPLATE_C_BLOCK.html)
المفردات: النَّهَى: المُفْرَدُ : النَّهْيَةُ : وهي: العَقْلُ. المستغرب : اسم فاعِلِ فِعْلُهُ استَغْرَبَ.
الشرح: روى التاريخ الكثيرَ مِنَ الجرائِمِ البَشِعَةِ التي ارتكبها الصَّهَائِنَةُ بِحَقِّ أبناء القدس، وحينما لا مَسَتْ أسماع العالم، وَقَفَ العالم مَذْهُولاً مُسْتَغْربا .
(Component: TEMPLATE_C_IRAB.html)
Target: كَمْ
Role: خَبَرَيَّةٌ مَبْنِيَّةٌ على السكون في محلِّ نَصْبِ مَفْعُولُ مُطْلَق
Target: النُّهى، العالم
Role: مضاف إليه مجرور
Target: المستغرب
Role: صِفَةٌ مَجْرُورَة.ٌ

=== BLOCK 10: خلاصة البلاغة ===
(Component: TEMPLATE_C_TABLE.html)
Title: خلاصة الصور البيانية
Headers: الصورة البيانية | نوعها
Row 1: (الطرف انثنى) | استعارَةٌ مَكْنِيَّة
Row 2: (منبر الحقد)، (سيف الغضب) | تَشْبِيهُ بَلِيْعٌ إضافي
Row 3: (جرح ماضيها) | تشبيه بَلِيعٌ إضافي
Row 4: (وقف التاريخ) | استعارَةٌ مِكْنِيَّة.ٌ

--- END STREAM ---
