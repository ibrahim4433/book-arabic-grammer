# **SESSION 125**

[TASK DEFINITION]
Objective: Implement page 125.
File: `pages/page_125.html`
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
[LESSON_NUMBER]: 125
[CHAPTER_TITLE]: page 125
[CATEGORY_HEADER]: 125
[SECTION_HEADER]: 125
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: النص الإفْراني الأول ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b19770
[POEM_TITLE]: النص الإفْراني الأول
[UNIQUE_ID_BIO]: b00273
[POET_NAME]: سلامة عبيد ١٩٢١) - ٤٨٩١م(
Verse 1:
[RIGHT_HEMISTICH]: أَشْرَقَ الفَجْرُ فَالدُّرُوبُ ضِيَاءُ
[LEFT_HEMISTICH]: وأَنَاشِيْدُ عِزَّةِ وحُدَاءُ
Verse 2:
[RIGHT_HEMISTICH]: وتلاشَتْ مَعَ القُيُودِ أساطير
[LEFT_HEMISTICH]: حدُودِ رَهِيْبَةٌ نَكْرَاءُ
Verse 3:
[RIGHT_HEMISTICH]: وقَادَى الغَدُ الضَّعُولُ طَلِيْقًا
[LEFT_HEMISTICH]: وبِهِ مِنْ سَنَا الرَّجَاءِ سَنَاءُ
Verse 4:
[RIGHT_HEMISTICH]: - إِهَا فَرْحَةُ الْحَيَاةِ فَمِيدِي
[LEFT_HEMISTICH]: يَا رَاوَابِي وَهَلِلِي يَا سَمَاءُ
Verse 5:
[RIGHT_HEMISTICH]: ه وتعني بِأُمَّتِي إِنَّهَا عَا
[LEFT_HEMISTICH]: دَتْ وَإِنَّا فِي أَرْضِنَا طُلَقَاءُ
Verse 6:
[RIGHT_HEMISTICH]: - أَيُّهَا النَّائِهُونَ فِي مَهْمَهِ الأَمْ
[LEFT_HEMISTICH]: س سَرَابٌ دُرُوبُكُم وَشَقَاءُ
Verse 7:
[RIGHT_HEMISTICH]: وتَشَنَّتْ فِيهَا الجَدَاوِلُ سَكُرَى
[LEFT_HEMISTICH]: وَتَرَامَتْ فِي رَبِّعِهَا الأَفْيَاءُ
Verse 8:
[RIGHT_HEMISTICH]: أَزْهَرَتْ وَاحَةُ العُرُوبَةِ وَافْتَر
[LEFT_HEMISTICH]: رَتْ وَمَاسَتْ جِنَاهَا الخَضْرَاءُ
Verse 9:
[RIGHT_HEMISTICH]: - أَقْبِلُوا أَيُّهَا الْحَيَارِي فَهَذَا الد
[LEFT_HEMISTICH]: دَرْبُ طَلْق،ٌ مُشَوَقٌ وَضَاءُ
Verse 10:
[RIGHT_HEMISTICH]: -۱۰ دَرْبُ تَوْحِيدِ أُمَّةٍ جَبَلَتْهَا
[LEFT_HEMISTICH]: مِنْ عَبِير المكَارِمِ العَلْيَاءُ
Verse 11:
[RIGHT_HEMISTICH]: -۱۱ في غَدٍ تَزْحَفُ الجُمُوعُ لِتَبْنِي
[LEFT_HEMISTICH]: بيَدَيْهَا مَا هَدَّمَ الأَعْدَاءُ

=== BLOCK 3: حياة الشاعر ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b02987
[BLOCK_TITLE]: سلامة عبيد
[CONTENT]: سلامة عبيد شَاعِرٌ سُورِي، ولد فِي مُحَافَظَةِ السُّوَيْدَاء عام ۱۲۹۱م. والدة علي عبيد شَاعِرٌ شَعْيِّ أَرَّحَ الْمُعْظَمِ أَحْدَاثِ التَّوْرَةِ السُّورِيَّةِ الكُبْرَى ضِد الاحتلال الفرنسي. عمل سلامة عبيد مُعَلمًا، ونَاضَلَ ضد الاختلال الفِرَنْسِي،ِّ وَشَغَلَ مَنْصِبَ مُدِيرِ التَّرْبِيَةِ فِي مُحَافَظَةِ السُّوَيْدَاء ١٩٥٣)- ٠٦٩١م(. انتخِبَ عُضُوا في مجلس الأُمَّةِ إِنَّانَ الوَحْدَةِ بَيْنَ سُورِيَّة ومصر . أَقَامَ فِي الصّينِ مُدَرِّسًا لِلغَةِ العربية في جامِعَةِ بِكين ۱۹۷۲)- ٤٨٩١م(. عاد إلى أَرْضِ الوطن، ومات فيها بَعْدَ يَوْمٍ وَاحِدٍ مِنْ وَسُولِهِ إِلَيْهَا في ٢٥ آذار عام ٤٨٩١م. كتب هذه القصيدة قبل الاستفتاء على وحدة سورية ومصر عام ٨٥٩١م.

=== BLOCK 4: الاستيعاب والفهم والتحليل ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b26706
[BLOCK_TITLE]: الاستيعاب والفهم والتحليل:
[CONTENT]: المستوى الفكري:

=== BLOCK 5: تنبيه هام ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[UNIQUE_ID]: b27003
[TITLE]: اختر الإجابة الصَّحِيحَةَ فيما يَأْتِي :
[CONTENT]: -۱ يُعالج الشاعر في هذا النَّصَ قَضِيَّة:ٌ ذاتية. ب وَطَنِيَّة. إِنْسَانِيَّة. د قومية.

=== BLOCK 6: أسئلة ===
(Component: TEMPLATE_C_LIST.html)
[UNIQUE_ID]: b67476
Item 1:
[LIST_ITEM_CONTENT]: - مِنْ أَسْبَابِ الفَرَح بِالوَحْدَةِ فِي الْبَيْتِ الأَوَّل:ِ تجدد الآمال. ب برُوعَ بَشَائِرِ النَّصْر. التَّغَني بِانْتِصَارِ الْعُرُوبَة.ِ كُلُّ مَا سَبَق.َ
Item 2:
[LIST_ITEM_CONTENT]: استَعْمَلَ الشَّاعِرُ كَلِمَةَ (أَسَاطِيرُ) في البَيْتِ الثَّانِي لِيُؤكد: تراث الأُمَّةِ العَرَبَيَّة.ِ ب قُوَّة الأَمَّةِ العَرَبِيَّة.ِ وَحْدَة الأُمَّةِ العَرَبِيَّة.ِ أَصَالَةِ الأُمَّةِ العَرَبِيَّة.ِ
Item 3:
[LIST_ITEM_CONTENT]: - الأمل بالمستقبل المشرق( فكرة البيت : الأول. الثاني. الرابع. الثالث. اد
Item 4:
[LIST_ITEM_CONTENT]: ه- النَّائِهون في البيت السادس هم المُتَمَسِكُون بأوهام الماضي. ب المتخلفُونَ عَنْ رَكْبِ الْوَحْدَة.ِ اد الصَّائِعُونَ فِي الصَّحْرَاء.ِ الغَارِقُونَ فِي ذِكْرَيَاتِ المَاضِي.
Item 5:
[LIST_ITEM_CONTENT]: - تَرْتِيْبُ كَلِمَاتِ الشَّطْرِ الثَّانِي مِنَ البَيْتِ الأَوَّلِ وفق ورودها في معجم يأخذ بأوائل الكلمات : حداء، عزة، أناشيد(. )عزة، أناشيد، حداء(. ب )حداء، أناشيد، عزّة(. こ( أناشيد، عزة، حداء(.

=== BLOCK 7: سؤال مجاب ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b93313
[QUESTION_NUMBER]: -٢
[QUESTION_TEXT]: - لماذا طَلَبَ الشَّاعِرُ إلى السَّمَاءِ أَنْ لِل؟ ج
[ANSWER_TEXT]: مِنْ أَجْلِ أَنْ تُعَبَرَ عَنْ فَرَحِهَا بِالوَحْدَة.ِ

=== BLOCK 8: سؤال مقطوع ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
[UNIQUE_ID]: b42809
[BLOCK_TITLE]: الاستيعاب والفهم والتحليل:
[CONTENT]: مَا مَوْقِفُ الشَّاعِرِ مِنَ الحُدُودِ وفق ما وَرَدَ فِي البيْتِ النَّانِي وَكَيْفَ تَجَلَّى هذا المؤقف؟ - - ١٢٥ LAUHG

=== BLOCK 9: Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
[UNIQUE_ID]: b35658
[HEADER_1]: الخيار أ
[HEADER_2]: الخيار ب
[HEADER_3]: الخيار ج / د
Row 1:
[CELL_1]: ذاتية.
[CELL_2]: ب وَطَنِيَّة.
[CELL_3]: إِنْسَانِيَّة. د قومية.

--- END STREAM ---
