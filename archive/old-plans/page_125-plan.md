# **SESSION 125**

[TASK DEFINITION]
Objective: Implement page 125.
File: `pages/page_125.html` (Note: Use the exact page number.)
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
[LESSON_NUMBER]: 125
[CHAPTER_TITLE]: page 125
[CATEGORY_HEADER]: 125
[SECTION_HEADER]: 125
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Poem (النص الإقرائي الأول) ===
(Component: TEMPLATE_C_POEM.html)
Title: النص الإقرائي الأول
Verses:
1. أَشْرَقَ الفَجْرُ فَالدُّرُوبُ ضِيَاءُ *** وأَنَاشِيْدُ عِزَّةِ وحُدَاءُ
2. وتلاشَتْ مَعَ القُيُودِ أساطيـ *** ـرُ حدُودٍ رَهِيْبَةٌ نَكْرَاءُ
3. وغَدَا الغَدُ المَأْمُولُ طَلِيْقًا *** وبِهِ مِنْ سَنَا الرَّجَاءِ سَنَاءُ
4. إِيهِ فَرْحَةُ الْحَيَاةِ فَمِيدِي *** يَا رَاوَابِي وَهَلِلِي يَا سَمَاءُ
5. وتَغَنَّي بِأُمَّتِي إِنَّهَا عَا *** دَتْ وَإِنَّا فِي أَرْضِنَا طُلَقَاءُ
6. أَيُّهَا التَّائِهُونَ فِي مَهْمَهِ الأَمْـ *** ـسِ سَرَابٌ دُرُوبُكُم وَشَقَاءُ
7. أَزْهَرَتْ وَاحَةُ العُرُوبَةِ وَافْتَر *** رَتْ وَمَاسَتْ جِنَاهَا الخَضْرَاءُ
8. وتَثَنَّتْ فِيهَا الجَدَاوِلُ سَكْرَى *** وَتَرَامَتْ فِي رَبُوعِهَا الأَفْيَاءُ
9. أَقْبِلُوا أَيُّهَا الْحَيَارَى فَهَذَا الـ *** دَرْبُ طَلْقٌ، مُشَوِّقٌ وَضَّاءُ
10. دَرْبُ تَوْحِيدِ أُمَّةٍ جَبَلَتْهَا *** مِنْ عَبِير المكَارِمِ العَلْيَاءُ
11. في غَدٍ تَزْحَفُ الجُمُوعُ لِتَبْنِي *** بيَدَيْهَا مَا هَدَّمَ الأَعْدَاءُ

=== BLOCK 3: Author Biography (حياة الشاعر) ===
(Component: TEMPLATE_C_POEM.html) (Bio block)
Title: حياة الشاعر
Author Name: سلامة عبيد (١٩٢١ - ١٩٨٤م)
Classes: text-accent for keywords
Content: سلامة عبيد شَاعِرٌ سُورِي، ولد فِي مُحَافَظَةِ السُّوَيْدَاء عام ١٩٢١م. والدُهُ علي عبيد شَاعِرٌ شَعْبِيّ أَرَّخَ لِمُعْظَمِ أَحْدَاثِ الثَّوْرَةِ السُّورِيَّةِ الكُبْرَى ضِد الاحتلال الفرنسي. عمل سلامة عبيد مُعَلمًا، ونَاضَلَ ضد الاحتلال الفِرَنْسِي،ِّ وَشَغَلَ مَنْصِبَ مُدِيرِ التَّرْبِيَةِ فِي مُحَافَظَةِ السُّوَيْدَاء (١٩٥٣ - ١٩٦٠م). انتخِبَ عُضُوا في مجلس الأُمَّةِ إِبَّانَ الوَحْدَةِ بَيْنَ سُورِيَّة ومصر . أَقَامَ فِي الصّينِ مُدَرِّسًا لِلغَةِ العربية في جامِعَةِ بِكين (١٩٧٢ - ١٩٨٤م). عاد إلى أَرْضِ الوطن، ومات فيها بَعْدَ يَوْمٍ وَاحِدٍ مِنْ وُصُولِهِ إِلَيْهَا في ٢٥ آذار عام ١٩٨٤م. كتب هذه القصيدة قبل الاستفتاء على وحدة سورية ومصر عام ١٩٥٨م.

=== BLOCK 4: Text Analysis (مناقشة وتحليل) ===
(Component: TEMPLATE_C_TABLE.html)
Title: مناقشة وتحليل (الاستيعاب والفهم)
Headers: السؤال | الإجابة
Row 1: لماذا طَلَبَ الشَّاعِرُ إلى السَّمَاءِ أَنْ تُهَلِّل؟ | (ج -٢) مِنْ أَجْلِ أَنْ تُعَبِّرَ عَنْ فَرَحِهَا بِالوَحْدَةِ.
Row 2: مَا مَوْقِفُ الشَّاعِرِ مِنَ الحُدُودِ وفق ما وَرَدَ فِي البيْتِ الثَّانِي وَكَيْفَ تَجَلَّى هذا المَوْقِفُ؟ | - -

=== BLOCK 5: Comprehension (الاستيعاب والفهم والتحليل) ===
(Component: TEMPLATE_C_EXAM.html)
Subtitle: المستوى الفكري - اختر الإجابة الصَّحِيحَةَ فيما يَأْتِي:
Number: ١
Question: يُعالج الشاعر في هذا النَّصَ قَضِيَّة:ٌ (ذاتية - وَطَنِيَّة - إِنْسَانِيَّة - قومية)
Number: ٢
Question: مِنْ أَسْبَابِ الفَرَح بِالوَحْدَةِ فِي الْبَيْتِ الأَوَّلِ: (تجدد الآمال - بزوغ بَشَائِرِ النَّصْر - التَّغَني بِانْتِصَارِ الْعُرُوبَةِ - كُلُّ مَا سَبَقَ)
Number: ٣
Question: استَعْمَلَ الشَّاعِرُ كَلِمَةَ (أَسَاطِيرُ) في البَيْتِ الثَّانِي لِيُؤكد: (تراث الأُمَّةِ العَرَبَيَّةِ - قُوَّة الأَمَّةِ العَرَبِيَّةِ - وَحْدَة الأُمَّةِ العَرَبِيَّةِ - أَصَالَةِ الأُمَّةِ العَرَبِيَّةِ)
Number: ٤
Question: (الأمل بالمستقبل المشرق) فكرة البيت: (الأول - الثاني - الرابع - الثالث)
Number: ٥
Question: التَّائِهُونَ في البيت السادس هم: (المُتَمَسِكُون بأوهام الماضي - المتخلفُونَ عَنْ رَكْبِ الْوَحْدَةِ - الضَّائِعُونَ فِي الصَّحْرَاءِ - الغَارِقُونَ فِي ذِكْرَيَاتِ المَاضِي)
Number: ٦
Question: تَرْتِيْبُ كَلِمَاتِ الشَّطْرِ الثَّانِي مِنَ البَيْتِ الأَوَّلِ وفق ورودها في معجم يأخذ بأوائل الكلمات (حداء، عزة، أناشيد): (عزة، أناشيد، حداء - حداء، أناشيد، عزّة - أناشيد، عزة، حداء)

=== BLOCK 6: Footnote (ملاحظة) ===
(Component: TEMPLATE_C_BENEFIT.html)
Content: ١٢٥ LAUHG

--- END STREAM ---
