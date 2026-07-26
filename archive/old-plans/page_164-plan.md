# **SESSION 164**

[TASK DEFINITION]
Objective: Implement page 164.
File: `pages/page_164.html` (Note: Use the exact page number.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`.
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md` to identify the correct template to use for the continuation.
3. Text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green`  for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   **Rule:** NO INLINE STYLES.
*   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
6. Templates: You are forbidden from inventing new HTML tags or classes or template elements. Replace any `<section>` tags from the templates with `<div>` tags (keep `<header>`).
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). The ID MUST be applied to the `<div>` tag that replaced the `<section>` tag. Use "Jules-workspace/id_manager.py" to generate or verify them.
8. Self-Correction: Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...) .
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense. Do NOT leave empty space.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
15. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 164
[CHAPTER_TITLE]: page 164
[CATEGORY_HEADER]: 164
[SECTION_HEADER]: 164
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: تتمة شرح الأبيات ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
Title: تتمة شرح الأبيات
Content:
بالتابع صَدْرًا قُومُهُ فَعَلَى لُقْمَتِهِ سُمُ الحَسَدُ
المفردات التابع : عَظِيمُ الشَّأْنِ
الشَّرح : امتلات صدور أبناء المَهْجَرِ بِالحَسَدِ لِذَلِكَ الْمُهَاجِرِ عَظِيم الشَّأْن،ِ حَيْثُ حَسَدُوهُ عَلَى لُ مَةِ عَيْشِهِ التي يحصل عَلَيْهَا بِكَدِهِ
البلاغة: )سم الحَسَد(: تشية بَلِيعٌ إضافي

=== BLOCK 3: إعراب التتمة ===
(Component: TEMPLATE_C_IRAB_ROW.html)
Word 1: صَدْرا
Details 1: مي مَنْسُوبٌ
Word 2: قَوْمُهُ
Details 2: فَاعِلَ مَرْفُوع
Word 3: سم:
Details 3: مُبْتَدَاً مَرْفُوع.

=== BLOCK 4: البيت العاشر ===
(Component: TEMPLATE_C_POEM.html)
Title: البيت العاشر
Right Hemistich: -۱۰ ذَنْبُهُ الإفلاتُ مِنْ مِنْتِهِمْ
Left Hemistich: عِنْدَمَا جَدَّ وبالجةِ وَجَد

=== BLOCK 5: شرح البيت العاشر ===
(Component: TEMPLATE_C_BLOCK.html)
Title: شرح البيت العاشر
Content:
المفردات : منتهم : يمين على النَّاسِ بِعَطاياه : مَنْ يَعُدُّ وَيَحْسُبُ مَا يَفْعَلُهُ وَيُقَدِّمُهُ مِنْ صَنائع وعطايا لغيره.
الشرح: ضاقَ صَدْرُ أَبِنَاءِ الْمَهْجَرِ بالمهاجرٍ مِنْ دُونَ أَنْ يَرْتَكِبَ أَيَّ ذَنْبِ فَكُلُّ مَا فَعَلَهُ الاستغناء عَنْ إِحْسَانِهِم، حينما اعتمد على نَفْسِهِ وَعَمِلَ بِحِدٍ واجتهاد فَحَصَل على لُقْمَةِ عِيشِهِ مِنْ عَرَقٍ جَبِيْنِهِ
البلاغة: )جَد،َّ وَجَد(، أو : )الجد،ٍ وَجَد( جناس ناقص

=== BLOCK 6: إعراب البيت العاشر ===
(Component: TEMPLATE_C_IRAB.html)
Word 1: ذَنْبُه:
Details 1: مُبْتَداً مَرْفُوع
Word 2: الإفلات :
Details 2: خَبَرِّ مَرْفُوعُ
Word 3: عِنْدَمَا
Details 3: عِنْدَ : مَفْعُولٌ فِيهِ ظَرْفُ زَمَانٍ مَنْصُوبٌ وَمَا حَرْفٌ مَصْدَرِي.
Word 4: )جَدَّ( :
Details 4: صِلَةَ المَوْصُولِ لا محل لها من الإعراب.
Word 5: وجد :
Details 5: جملةٌ مَعْطُوفَةً لا محل لها من الإعراب.

=== BLOCK 7: البيت الحادي عشر ===
(Component: TEMPLATE_C_POEM.html)
Title: البيت الحادي عشر
Right Hemistich: -۱۱ شاعِرٌ يُرْجَى ولا يرجو،
Left Hemistich: وفي مَسْجِدِ الأَصْنَامِ يومًا مَا سَجَدْ

=== BLOCK 8: شرح البيت الحادي عشر ===
(Component: TEMPLATE_C_BLOCK.html)
Title: شرح البيت الحادي عشر
Content:
الشرح: إِنَّهُ شَاعِرٌ مُعْتَدَّ بِنَفْسِهِ تَطْلُبُ النَّاسُ عطاياه، ولا يَطْلُبُ عطاياهُم، وَيَكْفِيهِ فَخَرًا قُوَّةُ انتمانِهِ إِلَى قِيمِ وَطَنِهِ الرُّوحِيَّة،ِ وَعَدَمُ تَأْثْرِهِ بِقِيَمِ المَهْجَرِ
البلاغة: )يَرْجَى، لا يرجو( : طباق سلب

=== BLOCK 9: إعراب البيت الحادي عشر ===
(Component: TEMPLATE_C_IRAB.html)
Word 1: شَاعِرٌ :
Details 1: خَبَرٌ مَرْفُوعٌ
Word 2: )يُرْجَي(:
Details 2: في مَحَلِّ رَفْعِ صِفَة.
Word 3: )لا يرجو( :
Details 3: جملَةً مَعْطُوفَةٌ فِي مَحَلِّ رَفع.
Word 4: يَومًا
Details 4: مَفْعُولُ فِيهِ ظَرْفُ زَمَانٍ مَنْصُوبُ
Word 5: مَا
Details 5: حَرْفُ نَفِي.
Word 6: ما سَجَد(
Details 6: جُمْلَةٌ مَعْطُوفَةٌ فِي مَحَلِّ رَفع

=== BLOCK 10: ملاحظة ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content:
ملاحظة: وجَدْتُ لهذا البيت رواية أخرى على هذا النحو : شاعر يرجى ولا يرجو يجدي إلا الله . المدد وعلى هذه الرواية يكونُ شَرْحُ البَيْتِ كما يلي : إِنَّهُ شَاعِرٌ مُعْتَدَّ بِنَفْسِهِ تَطْلُبُ النَّاسُ عَطَاياه، ولا يطلب عطاياهم، ويَكْفِيهِ فَخْرًا أَنَّهُ لَا يَطْلُبُ العَوْنَ إِلَّا مِنْ رَبِّه.ِ

=== BLOCK 11: البيت الثاني عشر ===
(Component: TEMPLATE_C_POEM.html)
Title: البيت الثاني عشر
Right Hemistich: -۱۲ عَزَّ مَنْ يَفْهَمْ شَكوى زوجه
Left Hemistich: رُبَّ حَشد فيه بالروح انْفَرَة

=== BLOCK 12: شرح البيت الثاني عشر ===
(Component: TEMPLATE_C_BLOCK.html)
Title: شرح البيت الثاني عشر
Content:
المفردات الحشد : الحشدُ مِنَ الناس الجماعة الجمع: حُشُودٌ عَرَّ : عَنَّ الشَّيْء،ُ فَلَ فلا يَكَادُ يوجد
الشرح : قَلَّ وَنَدَرَ أَنْ يُوجد في بلاد المَهْجَرِ مَنْ يَنْسَجِمُ مَعَ طَبِيعَتِهِ وَيَفْهَم شكوى نَفْسِه،ِ فروحه فريدة مميزةً عَنْ أرواح الكثير مِنْ أَفراد الجموع التي يتعامل معها في غُرْبَتِهِ

=== BLOCK 13: إعراب البيت الثاني عشر ===
(Component: TEMPLATE_C_IRAB.html)
Word 1: من
Details 1: اسم مَوْصُولُ فِي مُحَلِّ رَفْع لَفَا فاعل
Word 2: )يَفْهَم(:
Details 2: صِلَةُ الموصول لا محل لها من الإعراب
Word 3: شكوى:
Details 3: مَفْعُولُ بِهِ مَنْصُوبٌ
Word 4: رَبَّ
Details 4: حَرْفُ جَرِّ شِيه بالزَّائِدِ
Word 5: حَشَدِ :
Details 5: اسمٌ تَجْرُورٌ مَرْفُوعٌ مَحَلَّا على أَنَّهُ مُبْتَدَا.

=== BLOCK 14: البيت الثالث عشر ===
(Component: TEMPLATE_C_POEM.html)
Title: البيت الثالث عشر
Right Hemistich: وَجَلَدْ -١٣ تَتَحَدَّاهُ البُغَاتُ استَنْسَرَتْ
Left Hemistich: زاد

=== BLOCK 15: شرح البيت الثالث عشر ===
(Component: TEMPLATE_C_BLOCK.html)
Title: شرح البيت الثالث عشر
Content:
المفردات البغات : طَائِرٌ أَصغر مِنَ الرَّحْمِ بطيء الطيران، ضَعِيفٌ الجمع: فنان
الشرح يتمادى الْحَمْقَى مِنْ أَبناءِ المَهْجَرِ الضُّعَفَاءِ فِي تَحَدِّيهِم لِلشَّاعِرِ الْمُهَاجِرِ وَيُظْهِرُون استِقُواءَهُم عَلَيه ، كلما ازداد صبره على ما يُلَاقِيهِ مِنْ أذاهُم، وتَمَهَّلَ فِي الرَّةِ عَلَيْهِم
البلاغة : )تَتَحَدَّاهُ الْبُغَاتُ( استعارة مكنية

=== BLOCK 16: إعراب البيت الثالث عشر ===
(Component: TEMPLATE_C_IRAB.html)
Word 1: )استنْسَرَتْ(
Details 1: في محل نصب حال.
Word 2: )زاد(
Details 2: في محلِّ جَرِّ بالإضافة. ييز منصوب. أناة : سكان المهجر.

=== BLOCK 17: البيت الرابع عشر ===
(Component: TEMPLATE_C_POEM.html)
Title: البيت الرابع عشر
Right Hemistich: -١٤ عَافَ وِرْدَ المَاءِ فيه ولغت
Left Hemistich: حَشَرَاتُ الأرض، فاستسقى البرد

=== BLOCK 18: شرح البيت الرابع عشر ===
(Component: TEMPLATE_C_BLOCK.html)
Title: شرح البيت الرابع عشر
Content:
المفردات : وَلَغَتْ : وَلَعَ الكَلْبُ وغيرهُ مِنَ السباع في الإناء، وشَرِبَ ما فيهِ بِأَطْرَافِ لِسَانِه،ِ أو أَدْخَلَ فِيهِ لِسَانَهُ فَحَرَّكَهُ اسْتَسْقَى: طَلَبَ الشقيا. البرد: الماء الجامِدُ يَنْزِلُ مِنَ السَّحَابِ قطعا صغارا. ويسمى حَبُّ الغمام، وحَبُّ أَنْ هَيْمَنَ الْمُزْنِ
الشَّرح : تَرَكَ الشَّاعِرُ المهاجر خيرات بلادِهِ بَعْدَ المُخْتَلُ عَلَيْهَا وَتَحْكَمَ بِمَصَادِرِها، وراحَ يَبْحَثُ عَنِ الرَّزْقِ في بلاد الغُرْبَة،ِ فَبَدَا كَمَنْ تَرَكَ مَنابع الماء الصَّافِيَة؛ لأن كاناتِ الْأَرْضِ كَدَّرَتْ صَفْوَهَا، وراحَ يَطْلُبُ السّايَةَ مِنْ حَبَّاتِ البَرَدِ النَّازِلَةِ مِنَ السَّحَاب.ِ

=== BLOCK 19: البيت الخامس عشر ===
(Component: TEMPLATE_C_POEM.html)
Title: البيت الخامس عشر
Right Hemistich: ١٥- وتَعَنَى المَوْتَ حَتَّى لا يرى
Left Hemistich: غَارَةَ الْهِرِّ عَلَى ذَيْلِ الأَسَدُ!

=== BLOCK 20: شرح البيت الخامس عشر ===
(Component: TEMPLATE_C_BLOCK.html)
Title: شرح البيت الخامس عشر
Content:
المفردات غارة الغارة: الهجوم على العدو. الجر: القط.
الشرح: فَضَلَ الْمُهَاجِرُ أَنْ يَمُوتَ قَبْلَ أَنْ يَرَى هَؤلاء الْحَمْقِى الضُّعفاء مِنْ أَبناء الْمُهْجَرِ يُغِيرون عَلَيْهِ وَيَتَمادون في التطاول عليه، ويُمْعِنُون في إلحاق الأذى الهُجُوم بِهِ حَيْثُ بَدَتْ غَارَتُكُم عَلَيْهِ كَارَةِ قِطِ تَطَاوَلَ وَتَجَرَّا فِي على أسد.

=== BLOCK 21: التحليل الفني والموضوعي للأبيات ===
(Component: TEMPLATE_C_TABLE.html)
Header 1: الفكرة
Header 2: الشعور
Header 3: الأداة (المثال)
Row 1: استغناء المُهَاجِرِ عَنْ عَطَاءِ أبناء المهْجَرِ واعتماده على نَفْسِهِ | اعتزاز وافتخار | التراكيب (جَدَّ وبالجد وَجَد، أو : ذَنْبُهُ الإِفْلَاتُ مِنْ مِنتهم)
Row 2: قِيمِ وَطَنِهِ الرُّوحِيَّة،ِ وَعَدَمُ تَأْثْرِهِ بِقِيَمِ المَهْجَرِ | اعتزاز وافتخار | التراكيب (شاعر يرجى ولا يرجو)
Row 3: تصوير معاناة المهاجر الروحية | أم وأسى | التراكيب (عَزَّ مَنْ يَفْهَمُ شكوى زوجه)
Row 4: تصويرُ مُعَانَاةِ الْمُهَاجِرِ مِنْ سكان المهجر. | - | -
Row 5: تصوير معاناة المهاجرٍ مِنْ سُكَانِ الْمَهْجَر. | - | -

=== BLOCK 22: نبذة عن الشاعر ===
(Component: TEMPLATE_C_POEM.html)
Title: حياة الشاعر
Poet Name: الشاعر (١٨٧٨ - ١٩٤٦م)
Content:
- وُلِدَ فِي حِمْصَ وَتَلَقَى تعليمه الابتدائي في مدارسها، ثُمَّ غادرها إلى النَّاصِرَةِ فِي فِلِسْطِينَ لِيُكْمِلَ تَعْلِيمَه،ُ وَهَاجَرَ بَعْدَها إلى نيويورك.
- أَنشَأَ مَجَلَّةَ )الفنون( التي رَفَعَتْ رايةَ النَّهْضَة الأَدَبِيَّة،ِ وَحَمَلَتْ مَطَامِحَ مُنْشِئِهَا بالتجديد.
- أسهم في تأسيس الرابطة القلمية.
- عَصَفَتْ بِهِ الْمَصَائِبُ وأَعْيَتْهُ الحِيلَة،ُ فاستحوذتْ عليه الحيْرَة،ُ فَأَصْبَحَ شاعِرَهَا الْأَوَّلَ ، وأَطَلَقَ اسمها على ديوانه الوحيد الأرواح الحائرة( الذي أُخِذَ مِنْهُ هذا النَّص.ُ

--- END STREAM ---
