# **SESSION 101**

[TASK DEFINITION]
Objective: Implement page 101.
File: `pages/page_101.html` (Note: Use the exact page number.)
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
[LESSON_NUMBER]: 101
[CHAPTER_TITLE]: page 101
[CATEGORY_HEADER]: 101
[SECTION_HEADER]: 101
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: الوحدة الأولى ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[TITLE]: الوحدة الأولى
[CONTENT]: قضايا وطنية وقومية: تعالج قصيدتاها بعض القضايا الوطنية والقومية، وقد تضمنت القصيدتين الآتيتين:

=== BLOCK 3: القصائد ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: عرس المجد
[HEADER_2]: للشاعر السوري عمر أبو ريشة،
[HEADER_3]: عالج فيها قضية وطنية: إِذْ صَوّر فيها، معتزا، فرحة الانتصار بجلاء المحتل الفرنسي عَنْ أرض وطنه سوريا، وأشاد بتضحيات السوريين العظيمة في يوم الجلاء.
[CELL_1]: الجسر
[CELL_2]: للشاعر الفلسطيني محمود درويش،
[CELL_3]: يرصد فيها عدم تخلي الفلسطينيين المهجرين عن حلم العودة إلى ديارهم.

=== BLOCK 4: عرس المجد عمر أبو ريشة ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: عرس المجد عمر أبو ريشة ١٩١٠- ١٩٩٠م
[POET_NAME]: - شاعر سُورِي،ٌّ نَشَاً وتَرَغْرَ فِي مَنْبِج،َ ثُمَّ أَقَامَ فِي حلب، وتَعَلَّم في مدارسها، ثُمَّ أَكمل دِرَاسَتَهُ فِي الجَامِعَةِ الأميركية في بيروت. - شَغَلَ مَنَاصِبَ عِدَّة،ٌ فَمِنْ مدير لدار الكُتُبِ الوطنِيَّةِ يجلب، إلى سفير لبلاده في الهند، والمسا، والولايات المتحدة. - أجاد في شِعْرِ الْحَمَاسَةِ والوطنية والغزل. - خلف تسعة دواوين أحدها بالإنكليزية، ومَلحَمَة،ً وتسع مسرحيات.

=== BLOCK 5: مدخل إلى النص ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: مدخل إلى النص:
[POET_NAME]: - سَطْرَ الشعب في سورية بِدِمَائِهِ يوم الجلاء العظيم في السَّابِعَ عَشَرَ مِنْ نيسان عام ١٩٤٦م. - أبو ريشة في هذا النَّصَ يُوْرَخُ لا نْتِصَارَاتِ بَلَدِهِ بِحُرُوفِ مِنْ نُور،ٍ وَيُصَوِّرُ فَرْحَةَ الأَنْتِصَارِ بِجَلَاءِ الْمُحْتَلِ عَنْ أَرْضِ الوطن، ويُشِيْدُ بتضحيات السوريين العظيمة في يوم الجلاء.

=== BLOCK 6: قصيدة عرس المجد ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]:
[RIGHT_HEMISTICH]: - يا عَرُوسَ الْمَجْدِ تيهي واسحبي
[LEFT_HEMISTICH]: فِي مَغَانِينَا ذُيُولَ الشَّهب
[RIGHT_HEMISTICH]: - لَنْ تَرَي حَفْنَةَ رَمْلٍ فَوْقَهَا
[LEFT_HEMISTICH]: لَمَّ تُعَطَّرْ بِدما حرّ أَبِي
[RIGHT_HEMISTICH]: - دَرَجَ البَغْيُ عَلَيْهَا حِقْبَةً
[LEFT_HEMISTICH]: وَهَوى دُونَ بُلُوغِ الْأَرْبِ
[RIGHT_HEMISTICH]: - وارمى كير الليالي دُوهَا
[LEFT_HEMISTICH]: لَينَ النَّاب،ِ كَلِيلَ الْمِخْلَبِ
[RIGHT_HEMISTICH]: ٥- لا يَمُوتُ الحَقُ مَهْمَا لَطَمَتْ
[LEFT_HEMISTICH]: عَارِضَيْهِ قَبْضَةُ الْمُغْتَصِبِ
[RIGHT_HEMISTICH]: - مِنْ هُنا شَقَّ الهُدَى أَكْمَامَهُ
[LEFT_HEMISTICH]: وَقَادَى مَوْكِبًا فِي مَوْكِبِ
[RIGHT_HEMISTICH]: وأَتَى الدنيا فَرَفَّتْ طَرَبًا
[LEFT_HEMISTICH]: وانْتَشَتْ مِنْ عَبْقِهِ الْمُنْسَكِبِ
[RIGHT_HEMISTICH]: وتَغَنَّتْ بِالمروات التي
[LEFT_HEMISTICH]: عَرَفَنْهَا فِي فَتاها العربي
[RIGHT_HEMISTICH]: - أَصْيَرِةٌ ضَاقَتْ بِهِ صَخواه
[LEFT_HEMISTICH]: فَأَعَدَّتْهُ لِأُفْقِ أَرْحَبِ
[RIGHT_HEMISTICH]: ١٠- هَبَّ للفتح، فَأَدْمَى ..
[LEFT_HEMISTICH]: حَافِرُ الْمُهْرِ جَبِينَ الكُوكَبِ
[RIGHT_HEMISTICH]: ١١- يا عَرُوسَ الْمَجْد،ِ طَابَ الْمُلْتَقَى
[LEFT_HEMISTICH]: بَعْدَمَا طَالَ جَوَى الْمُغْتَرِبِ
[RIGHT_HEMISTICH]: ١٢- قَدْ عَرَفْنَا مَهْرَكِ الغالي فَلَمْ
[LEFT_HEMISTICH]: نُرْخص الْمَهْر،َ وَلَمْ تَحْتَسِبِ
[RIGHT_HEMISTICH]: ١٣- وأَرقناها دِمَاءً حُرَّةً
[LEFT_HEMISTICH]: فاعرفي ما شِنْتِ منها واشربي!
[RIGHT_HEMISTICH]: ١٤- نَحْنُ مِنْ ضَعَفٍ بَنَيْنَا قُوَّةً
[LEFT_HEMISTICH]: لَمْ تَلِنْ لِلْمَارِج الْمُلْتَهِبِ
[RIGHT_HEMISTICH]: ١٥- هَذِهِ تُرْبِتُنَا لَنْ تَزْدَهِي
[LEFT_HEMISTICH]: بسوانا مِن حُمَاةٍ تُدُبِ

--- END STREAM ---
