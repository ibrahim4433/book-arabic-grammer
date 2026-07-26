# **SESSION 132**

[TASK DEFINITION]
Objective: Implement page 132.
File: `pages/page_132.html`
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
[UNIQUE_ID]: b13452
[LESSON_NUMBER]: 132
[CHAPTER_TITLE]: page 132
[CATEGORY_HEADER]: 132
[SECTION_HEADER]: 132
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: التمسك بالأمل والتطلعُ إِلَى العَوْدَة ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b17276
Title: (Empty)
Content: <span class="text-accent font-bold">التمسك بالأمل والتطلعُ إِلَى العَوْدَة:</span>

=== BLOCK 3: Poem ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b48182
[POET_NAME]: عبد الكريم الكرمي:
[RIGHT_HEMISTICH_1]: غَدًا سَتَعُودُ والأَجْيَالُ تُصْغِي
[LEFT_HEMISTICH_1]: إِلَى وَقْعِ الخُطَا عِنْدَ الْإِيَابِ

=== BLOCK 4: إصْرَارُ المهجرين الفلسطينيين على العودة ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b34563
Title: (Empty)
Content: <span class="text-accent font-bold">إصْرَارُ المهجرين الفلسطينيين على العودة:</span>

=== BLOCK 5: Poem ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b51336
[POET_NAME]: محمود درويش:
[RIGHT_HEMISTICH_1]: مَشْيَا على الأَقدام
[LEFT_HEMISTICH_1]: أَوْ زَحْفًا على الأيدي نَعُودُ

=== BLOCK 6: فَضْحُ وَحْشِيَّةِ الصَّهَائِنَة ===
(Component: TEMPLATE_C_TABLE.html)
[UNIQUE_ID]: b33094
[ROW_1_COL_1]: فَضْحُ وَحْشِيَّةِ الصَّهَائِنَة،ِ
[ROW_1_COL_2]: وَإِبْرَازُ مُمَارَسَاتِ العُدْوَانِيَّة،ِ
[ROW_2_COL_1]: وَتَصْوِيرُ جَرَائِمِهِم التِي يَقْتَرِفُونَهَا
[ROW_2_COL_2]: بِحَقِّ العائِدِين:

=== BLOCK 7: حِرْمَانُ المُهَجَرِين الفلسطينيين ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b12051
Title: (Empty)
Content: <span class="text-accent font-bold">حِرْمَانُ المُهَجَرِين الفلسطينيين مِنْ حَقَ العَوْدَةِ إِلَى دِيَارِهِم:</span>

=== BLOCK 8: Poem ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b79898
[POET_NAME]: محمود درويش
[RIGHT_HEMISTICH_1]: لَنْ يَمُرَّ الْعَائِدُون
[LEFT_HEMISTICH_1]: حَرَسُ الْحُدُودِ مُرَابِطٌ

=== BLOCK 9: أو ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b16711
Title: (Empty)
Content: <span class="font-bold">أو:</span>

=== BLOCK 10: Poem ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b41161
[POET_NAME]: محمود درويش
[RIGHT_HEMISTICH_1]: يَحْمِي الحُدُودَ مِنَ الحَنين
[LEFT_HEMISTICH_1]: أَمْرٌ بِإِطلاق الرصاص على الذي
[RIGHT_HEMISTICH_2]: يَجْتَازُ هذا الجسر؛ هَذَا الْجِسْرُ
[LEFT_HEMISTICH_2]: مِقْصَلَةُ الذي مَا زَالَ يَحْلُمُ بالوطن

=== BLOCK 11: الإِدْمَانُ على القتل ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[UNIQUE_ID]: b35578
[BENEFIT_TEXT]: - الإِدْمَانُ على القتل واسْتِسْهَالُ الْقِيَامَ بِه:ِ

=== BLOCK 12: Poem ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b80362
[POET_NAME]: محمود درويش:
[RIGHT_HEMISTICH_1]: وَبِرَغْمِ أَنَّ القَتْلَ
[LEFT_HEMISTICH_1]: التَّدْخِينِ

=== BLOCK 13: قَتْلُ الحَالِمِينَ بِالعَوْدَة ===
(Component: TEMPLATE_C_BENEFIT.html)
[UNIQUE_ID]: b31144
[BENEFIT_TEXT]: - قَتْلُ الحَالِمِينَ بِالعَوْدَة:ِ

=== BLOCK 14: Poem ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b77433
[POET_NAME]: محمود درويش:
[RIGHT_HEMISTICH_1]: وَالطَّلْقَةُ الأُخْرَى ....
[LEFT_HEMISTICH_1]: أَصَابَتْ قَلْبَ جُنْدِيّ قَدِيمٍ

=== BLOCK 15: أو ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b27298
Title: (Empty)
Content: <span class="font-bold">أو :</span>

=== BLOCK 16: Poem ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b85014
[POET_NAME]: محمود درويش
[RIGHT_HEMISTICH_1]: لَمْ يَقْتُلُوا الاثنين
[LEFT_HEMISTICH_1]: كَانَ الشَّيْخُ يَسْقُطُ فِي مِيَاهِ النَّهْرِ

=== BLOCK 17: كَثْرَةُ القَتْلَى الفلسطينيين ===
(Component: TEMPLATE_C_BENEFIT.html)
[UNIQUE_ID]: b09133
[BENEFIT_TEXT]: كَثْرَةُ القَتْلَى الفلسطينيين الحَالِمِينَ بِالعَوْدَة:ِ

=== BLOCK 18: Poem ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b75735
[POET_NAME]: محمود درويش
[RIGHT_HEMISTICH_1]: كُلُّ القَوَافِلِ قَبْلَهُم غَاصَتْ
[LEFT_HEMISTICH_1]: وَكَانَ النَّهْرُ يَبْصُقُ ضِفَتَيْهِ
[RIGHT_HEMISTICH_2]: قِطَعاً مِنَ اللَّحْمِ الْمُفَتَتِ
[LEFT_HEMISTICH_2]: في وُجُوهِ الْعَائِدِينَ

=== BLOCK 19: الإِشَارَةُ إِلَى عَدَمِ شَرْعِيَّةِ الوُجُودِ ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b07339
Title: (Empty)
Content: <span class="text-accent font-bold">- الإِشَارَةُ إِلَى عَدَمِ شَرْعِيَّةِ الوُجُودِ الصُّهْيُونِي فِي فِلَسْطِين السُّخْرِيَةُ مِنَ الجُنُودِ الصَّهَائِنَةِ(:</span>

=== BLOCK 20: Poem ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b22468
[POET_NAME]: محمود درويش:
[RIGHT_HEMISTICH_1]: لكِنَّ الجُنُودَ الطَّيِّبِين
[LEFT_HEMISTICH_1]: الطَّالِعِينَ عَلَى فَهَارِسِ دَفْتَرِ
[RIGHT_HEMISTICH_2]: قَذَفَتْهُ
[LEFT_HEMISTICH_2]: أَمْعَاءُ السَّنِينَ

=== BLOCK 21: الإقْدَامُ على جَرِيمَةِ الأَغْتِصَابِ ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b98994
Title: (Empty)
Content: <span class="text-accent font-bold">الإقْدَامُ على جَرِيمَةِ الأَغْتِصَابِ الاعتداء على الحرُمَاتِ وَتَدْنِيْسُ الشَّرَفِ(:</span>

=== BLOCK 22: Poem ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b44496
[POET_NAME]: محمود درويش
[RIGHT_HEMISTICH_1]: والبنت التي صَارَتْ يَتِيْمَهُ
[LEFT_HEMISTICH_1]: كَانَتْ مُمَزَّقَةَ الثِّيَابِ
[RIGHT_HEMISTICH_2]: - -
[LEFT_HEMISTICH_2]: وطَارَ عِطْرُ اليَاسَمِين

--- END STREAM ---
