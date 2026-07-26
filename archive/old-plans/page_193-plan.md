# **SESSION 193**

[TASK DEFINITION]
Objective: Implement page 193.
File: `pages/page_193.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html`. Ensure exact visual continuity.
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md` to identify the correct template to use for the continuation. Scan the raw text for the preceding keyword to determine the active template and apply the correct `_PART_1.html` wrapping.
3. Text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice. Under the 'Typo Exception', obvious OCR errors like "حلي - ۱۹۳", "اهَمْ" to "الهَمُّ", "لأَحْانِهَا" to "لأَحْزَانِهَا", and scrambled verses have been corrected.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   Rule: NO INLINE STYLES.
*   Rule: Irab Words inside `.irab-word` MUST be white.
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). Use "Jules-workspace/id_manager.py" to generate or verify them.
8. Self-Correction: Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...) .
11. You must preserve the exact Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense.
13. Balanced page colors between teal and orange: ensure every page has minimum 1 element in orange instead of all teal. (Achieved with TEMPLATE_C_BENEFIT_WARNING).
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`).
15. Exam section always be in the end of the lesson, and without the answers! Since the page ends with a violent cut, an Exam block is forbidden on this page.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 193
[CHAPTER_TITLE]: page 193
[CATEGORY_HEADER]: 193
[SECTION_HEADER]: 193
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Vocabulary Table (The Core Matrix) ===
(Component: TEMPLATE_C_TABLE.html)
Title: شرح المفردات الصعبة بحسب ورودها في الأبيات المتممة الواردة في ديوان الشاعر زكي قنصل:
Table_Headers: الكلمة | المعنى
Row_1: حَاشِيَةُ | الحَاشِيةُ مِنْ كُلِّ شَيْءٍ: جانبُهُ وَطَرَفُه.ُ والحشو مِنَ النَّاسِ: الذي لا يُعْتَمَدُ عليه. ومِنَ الكلام الفضل الذي لا خَيْرَ فِيه.ِ
Row_2: جلبابه | الحِلْبَابُ: القَمِيص،ُ أو التَّوْبُ المُشْتَمِلُ على الجَسَدِ كُلِّهِ
Row_3: نَشَبُ | النَّشَبُ: المال، أو العَقَارُ
Row_4: اعْتَلَجَتْ | اعْتَلَجَ الهَمُّ فِي صَدْرِهِ اضْطَرَبَ، وتلاطَمَ، وَتَجَاذَبَهُ وَشَغَلَهُ
Row_5: الريب | الرَّيْبَةُ: الظَّنُّ والشَّكُ والتُهْمَةُ
Row_6: الصَّلْصَالِ | الطَّينُ
Row_7: نديه | النَّدِي مَجْلِسُ القَوْمِ وَمُجْتَمَعُهُم.

=== BLOCK 3: Poem and Biography ===
(Component: TEMPLATE_C_POEM.html)
Title: النص الإثرائي الثاني - معاناة المغترب
Poet: فوزي المعلوف (١٨٩٩ - ١٩٣٠)
Bio_Title: حياة الشاعر
Bio_Content: فوزي بن عيسى اسكندر المعلوف شاعر لبناني، ولد في زحلة، أتقن الفرنسية والعربية. عين مديرا لمدرسة المعلمين بدمشق، ومدرسة الطب فيها. فأمين سر لعميد... سافر إلى البرازيل عام ١٢٩١م، فنشر فيها قصائده ومنها: (سقوط غرناطة)، و(تأوهات الحب)، و(على بساط الريح).
Right_1: عَمَرَتْهُ الأَحْلامُ بِالشَّفَقِ الوَرْدِي
Left_1: يُغْرِيهِ بِالمنى تَعْلِيلا
Right_2: وتلاشتْ حُلَمًا فَحُلَمًا إلى اللاشيءٍ
Left_2: تَمَشِي بِهِ قَلِيلًا قَلِيلا
Right_3: هو في مَيْعَةِ الشَّبَابِ ولو حَدَّقْتَ فِيهِ
Left_3: أَبْصَرْتَ شَيْحًا هَزِيْلا
Right_4: بِقَوَامٍ كَأَنَّ قَاصِمَةَ الظَّهْرِ
Left_4: أَنَاخَتْ عَلَيْهِ حِمْلًا تَقِيلا
Right_5: وَجَبِيْنٍ أَلْقَتْ عَلَيْهِ شُجُونُ النَّفْسِ
Left_5: ظِلًّا مِنَ العُبُوسِ ظَلِيْلا
Right_6: فهو لا يَعْرِفُ التَّبَسُمَ إِلَّا
Left_6: عِنْدَمَا يَسْتَعِيدُ حُلَمًا جَمِيلا
Right_7: ألِفَ اليَأْسَ قَلْبُهُ فَهو والياس
Left_7: يحاكي بُتَيْنَةً وَجَمِيلا
Right_8: وإذا اليَأْسُ صَدَّ عَنْهُ قَلِيْلًا
Left_8: رَاحَ يَبْكي على نَوَاهُ طَوِيلا
Right_9: وإذا ما النَّسِيمُ مَرَّ عَلَيْهِ
Left_9: فَعَلِيلٌ أَتَى يَعُودُ عَلِيلا
Right_10: حَائِرَ الطَّرْفِ شَارِدَ الفِكْرِ يَحْكِي
Left_10: مُدْلِجًا فِي الظَّلَامِ ضَلَّ السَّبِيلا
Right_11: تاهَ فِي عَالَمَ الخَيَالِ فَضَاعَتْ
Left_11: نَفْسُهُ وهي تَنْشُدُ المستحيلا

=== BLOCK 4: Intro to Text ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: مدخل إلى النص:
Content: يمثل هذا النص تعبيرا عن معاناة ذاتية نابعة من بعد الشاعر معلوف عن وطنه الأم، ومن مرارة الاغتراب في المهجر؛ حَيْثُ تبرز فيه آلام الذات الإنسانية التي تمتزج بالطبيعة لتعكس من خلالها تجربتها الانفعالية الذاتية وتشرك الطبيعة في لواعجهَا وآلامِهَا حِينا في حنةٍ رقيق، وحينا آخر تنزوي إلى نفسها تتجرع كأس اللوعة والأسى. ثم ترقى بهذه التجربة الذاتية وتجعلها لوحة لكل البشر الذين يُكَابدون الشَّقَاء بين تطلع الحلم ووطأة الواقع. وهذه الأبيات مأخوذة من قصيدة بعنوان (رمز الألم) من ديوان (على بساط الريح).

=== BLOCK 5: Comprehension and Analysis ===
(Component: TEMPLATE_C_LIST.html)
Title: الاستيعاب والفهم والتحليل: المستوى الفكري: ☑
Item_1: انْسُبِ الْفِكَرَ الآتِيةَ إِلَى مَوْطِنِهَا الْأَصْلِي: اتَّخَاذُ المَصَائِبِ كَاهِلَ الشَّاعِرِ مَبْرَكًا لأَحْزَانِهَا التَّقِيلَة.ِ ج - (البيت الرابع). - مشاركة الطَّبِيعَةِ الشَّاعِرَ آلامَهُ ج - (البيت التاسع).
Item_2: تواشُجُ عَلَاقَةِ العِشْقِ والغرام بينَ قَلْبِ الشَّاعِرِ واليَأْس.ِ ج - (البيت الثَّامِنَ). - بُرُوزُ الْأَلْفَةِ بَيْنَ الشَّاعِرِ وَاليَأْسِ ج - (البيت السابع).
Item_3: سَيْطَرَةُ الحَيْرَةِ والقَلَقِ على الشاعر . ج - (البيت العاشر). - انعكاس عذاباتِ النَّفْسِ على مُحَيَّا الشاعر . ج - (البيت الخامس).
Item_4: وَظَّفَ الشَّاعِرُ التراث في بناء نَصَّهِ لِتَقْرِيبِ الْمَوْقِفِ الشُّعُورِي الذي يُرِيدُ نَقْلَهُ إلى المُتَلَقِي. حَدِّدْ مَوْطِنَ هذا التوظيفَ وَوَضِّحْه.ُ ج - برز هذا التوظيف في البيتِ السَّابِعِ فَقَدْ أَرَادَ الشَّاعِرُ أَنْ يُؤْكِدَ أَنَّ الأَلْفَةَ التي تَأَلَّفَتْ بَيْنَ قَلْبِهِ وَاليَأْسِ قَدْ بَلَغَتْ مُستَوَى مُتَقَدِّمًا، فَلَجَأَ إلى تَشْبِيهِهَا بِعَلَاقَةِ الحب التي انْعَقَدَتْ بين جميل وبثينة.
Item_5: بَرَزَتْ في البيتِ التَّاسِعِ قِيمَةٌ اجْتِمَاعِيَّةٌ فَاضِلَة.ٌ ماهِيَ؟ ج - عِيَادَةُ الْمَرِيْض.ِ
Item_6: مَا مَعْنَى كُلِّ مِنَ الكَلِمَتَين: (يحكي، تَنْشُد) بِحَسَبِ وُرُودِهما في البيتين: العاشر، والحادي عشر؟ ج - يحكي: يُمائِلُ وَيُشَابِه تنشد : تَطْلُب.ُ

=== BLOCK 6: Artistic Level (Cut Content) ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
Title: المستوى الفني
Content: ☑ المستوى الفني:

--- END STREAM ---
