# **SESSION 130**

[TASK DEFINITION]
Objective: Implement page 130.
File: `pages/page_130.html` (Note: Use the exact page number.)
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
[LESSON_NUMBER]: 130
[CHAPTER_TITLE]: page 130
[CATEGORY_HEADER]: 130
[SECTION_HEADER]: 130
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Continuation of Previous Section ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[UNIQUE_ID]: b02447
[BLOCK_TITLE]: إلغاء التَّجْزِيَّةِ والتَّخَلص مِنْ قُيُودِ الْمُسْتَعْمِرِين
[CONTENT]: رَفْضُ التَّجْزِنَةِ وَإِنْكَارُ الحُدُودِ الوَهْمِيَّةِ التي رسمها المسْتَعْمرون(:

=== BLOCK 3: Poem 1 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b70128
[POEM_TITLE]: سلامة عبيد :
[UNIQUE_ID_BIO]: b45141
[POET_NAME]: سلامة عبيد
[RIGHT_HEMISTICH]: وتلاشَتْ مَعَ القُيُودِ أَسَاطِي
[LEFT_HEMISTICH]: ر حدُودِ رَهِيْبَةٌ نَكْرَاءُ

=== BLOCK 4: Rule 2 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b45872
Title: التفاول بالمُسْتَقْبَلِ المُشْرِقِ الوَاعِدِ بَعْدَ قِيَامِ الْوَحْدَة:ِ
Content: - التفاول بالمُسْتَقْبَلِ المُشْرِقِ الوَاعِدِ بَعْدَ قِيَامِ الْوَحْدَة:ِ

=== BLOCK 5: Poem 2 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b98678
[POEM_TITLE]: سلامة عبيد
[UNIQUE_ID_BIO]: b28476
[POET_NAME]: سلامة عبيد
[RIGHT_HEMISTICH]: وادى الغَدُ الضَّحُوكَ طَلِيقًا
[LEFT_HEMISTICH]: وبِهِ مِنْ سَنَا الرَّجَاءِ سَنَاءُ

=== BLOCK 6: Rule 3 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b09016
Title: الاعتِزَارُ بِتَحَرَّرِ الْأُمَّةِ العَرَبِيَّةِ
Content: - الدعوة إلى الإِشَادَةِ بِالأُمَّةِ العَرَبِيَّةِ لِتَحَرُرِهَا وَاسْتِقْلاها الاعتِزَارُ بِتَحَرَّرِ الْأُمَّةِ العَرَبِيَّةِ(:

=== BLOCK 7: Poem 3 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b54991
[POEM_TITLE]: سلامة عبيد وتغني
[UNIQUE_ID_BIO]: b82554
[POET_NAME]: سلامة عبيد
[RIGHT_HEMISTICH]: انا دَتْ
[LEFT_HEMISTICH]: وَإِنَّا فِي أَرْضِنَا طُلَقَاءُ

=== BLOCK 8: Rule 4 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b84137
Title: تَجِيد الأُمَّةِ العَرَبِيَّةِ وَالتَّغَنِي بِصِفَاتِهَا :
Content: تَجِيد الأُمَّةِ العَرَبِيَّةِ وَالتَّغَنِي بِصِفَاتِهَا :

=== BLOCK 9: Poem 4 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b87905
[POEM_TITLE]: سلامة عبيد :
[UNIQUE_ID_BIO]: b37252
[POET_NAME]: سلامة عبيد
[RIGHT_HEMISTICH]: عا بأمني دَرْبُ تَوْحِيدِ أُمَّةٍ جَبَلَتُهَا
[LEFT_HEMISTICH]: مِنْ عَبِيرِ الْمُكَارِمِ العَلْيَاءُ

=== BLOCK 10: Rule 5 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b30858
Title: -١٠ التَّحْذِيرَ مِنَ التَّجْزِنَةِ وَنَبْدَ الفُرْقَة:ِ
Content: -١٠ التَّحْذِيرَ مِنَ التَّجْزِنَةِ وَنَبْدَ الفُرْقَة:ِ

=== BLOCK 11: Poem 5 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b13481
[POEM_TITLE]: سلامة عبيد
[UNIQUE_ID_BIO]: b65751
[POET_NAME]: سلامة عبيد
[RIGHT_HEMISTICH]: فِي مَهْمَهِ الأَمْ أَيُّهَا النَّائِهُونَ
[LEFT_HEMISTICH]: مِنْ عَبِيرِ الْمُكَارِمِ العَلْيَاءُ س سَرَابٌ دُرُوبُكُم وَشَقَاءُ

=== BLOCK 12: Benefit Box ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[UNIQUE_ID]: b62181
[TITLE]: ۱۱- الدَّعْوَة إلى الوَحْدَةِ العَرَبِيَّةِ
[CONTENT]: تَحْفِيز المتَرَدِّدِين للالتحاق بِرَكَبِ الوحْدَةِ العَرَبِيَّةِ(:

=== BLOCK 13: Poem 6 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b59308
[POEM_TITLE]: سلامة عبيد:
[UNIQUE_ID_BIO]: b01477
[POET_NAME]: سلامة عبيد
[RIGHT_HEMISTICH]: أَيُّهَا النَّائِهُونَ فِي مَهْمَهِ الْأَمْ أَقْبِلُوا أَيُّهَا الْحَيَارِي فَهَذَا الد دَرْبُ تَوْحِيدِ أُمَّةٍ جَبَلَتْهَا
[LEFT_HEMISTICH]: س سراب دُرُوبُكُم وَشَقَاءُ دَرْبُ طَلْق،ٌ مُشَوَقٌ وَضَاءُ مِنْ عَبِير المكَارِمِ العَلْيَاءُ

=== BLOCK 14: Rule 6 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b59178
Title: -١٢ الإشارة إلى ثمارِ الوَحْدَةِ وَصْفَ جَمَالِ الْحَيَاةِ بَعْدَ قِيَامِ الوَحْدَةِ(:
Content: -١٢ الإشارة إلى ثمارِ الوَحْدَةِ وَصْفَ جَمَالِ الْحَيَاةِ بَعْدَ قِيَامِ الوَحْدَةِ(:

=== BLOCK 15: Poem 7 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b91247
[POEM_TITLE]: سلامة عبيد :
[UNIQUE_ID_BIO]: b86841
[POET_NAME]: سلامة عبيد
[RIGHT_HEMISTICH]: أَزْهَرَتْ وَاحَةُ العُرُوبَةِ وَافْتَر وتَتَنَّتْ فِيهَا الجَدَاوِلُ سَكْرَى
[LEFT_HEMISTICH]: رَتْ وَمَاسَتْ جِنَاهَا الْخَضْرَاءُ وتَرَامَتْ فِي رَبُعِهَا الأَفْيَاءُ

=== BLOCK 16: Rule 7 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b13289
Title: -۱۳ التَّفَاؤُلَ بِقِيَامِ الوَحْدَةِ الإيمان بِقُدْرَةِ الجَمَاهِيرِ الْعَرَبِيَّةِ على بِنَاءِ مَا هَدَّمَهُ المُسْتَعْمِرُ(:
Content: -۱۳ التَّفَاؤُلَ بِقِيَامِ الوَحْدَةِ الإيمان بِقُدْرَةِ الجَمَاهِيرِ الْعَرَبِيَّةِ على بِنَاءِ مَا هَدَّمَهُ المُسْتَعْمِرُ(:

=== BLOCK 17: Poem 8 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b82856
[POEM_TITLE]: سلامة عبيد
[UNIQUE_ID_BIO]: b14009
[POET_NAME]: سلامة عبيد
[RIGHT_HEMISTICH]: في غدٍ تَزْحَفُ الْجُمُوعُ لِتَبْنِي
[LEFT_HEMISTICH]: بِيَدَيْهَا مَا هَدَّمَ الأَعْدَاءُ

=== BLOCK 18: Rule 8 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b56585
Title: -١٤ إشراك الطبيعة بالفرح بالوحدة :
Content: -١٤ إشراك الطبيعة بالفرح بالوحدة :

=== BLOCK 19: Poem 9 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b34056
[POEM_TITLE]: سلامة عبيد:
[UNIQUE_ID_BIO]: b45142
[POET_NAME]: سلامة عبيد
[RIGHT_HEMISTICH]: إِنَّهَا فَرْحَةُ الْحَيَاةِ فَمِيدِي
[LEFT_HEMISTICH]: يَا رَاوَابِي وَهَلِلِي يَا سَمَاءُ

=== BLOCK 20: Table ===
(Component: TEMPLATE_C_TABLE.html)
[UNIQUE_ID]: b70129
[HEADER_1]: ثالثاً
[HEADER_2]: -
[HEADER_3]: الأدب الوطني:
[CELL_1]: - التَّعْبِيرِ عَنْ مَشَاعِرِ الفَرَحِ وَالزَّهو
[CELL_2]: بِتَحْقِيقِ الجلاء الفرح
[CELL_3]: جلاء المسْتَعْمر الغَرْبِي عَنْ أَرْضِ الوَطَنِ(:

=== BLOCK 21: Poem 10 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b45873
[POEM_TITLE]: بدر الدين الحامد:
[UNIQUE_ID_BIO]: b98679
[POET_NAME]: بدر الدين الحامد
[RIGHT_HEMISTICH]: يَوْمُ الخَلَاءِ هُوَ الدُّنْيَا وَزَهُوا
[LEFT_HEMISTICH]: لَنَا ابتهاج واللباغِينَ إِرْغَام

=== BLOCK 22: Poem 11 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b28477
[POEM_TITLE]: عمر أبو ريشة:
[UNIQUE_ID_BIO]: b09017
[POET_NAME]: عمر أبو ريشة
[RIGHT_HEMISTICH]: يا عروس المجد تِيْهِي واسحبي
[LEFT_HEMISTICH]: فِي مَغَانِينَا ذُيُولَ الشَّهب

=== BLOCK 23: Poem 12 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b54992
[POEM_TITLE]: شفيق جبري:
[UNIQUE_ID_BIO]: b82555
[POET_NAME]: شفيق جبري
[RIGHT_HEMISTICH]: يا عروس المجدِ طَابَ الْمُلْتَقَى حُلْمٌ على جَنَبَاتِ الشَّامِ أَمْ عِيدُ
[LEFT_HEMISTICH]: بَعْدَمَا طَالَ جَوَى المُغْتَرِبِ لا الهم هم ولا التَّسْهِيدُ تَسْهِيدُ

=== BLOCK 24: Rule 9 ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b84138
Title: - تصوير هزيمة المستَعْمِرِ وَخَيْبَتِهِ فِي تَوْطِيدِ وُجُودِه على أَرْضِنا (
Content: - تصوير هزيمة المستَعْمِرِ وَخَيْبَتِهِ فِي تَوْطِيدِ وُجُودِه على أَرْضِنا ( السُّخْرِيَةِ مِنَ المُسْتَعْمر والشَّمَاتَةِ هَزِمَتِهِ(:

=== BLOCK 25: Poem 13 ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b87906
[POEM_TITLE]: عمر أبو ريشة:
[UNIQUE_ID_BIO]: b37253
[POET_NAME]: عمر أبو ريشة
[RIGHT_HEMISTICH]: دَرَجَ البَغْيَّ عَلَيْهَا حِقْبَةً وارى كبر الليالي دُوها
[LEFT_HEMISTICH]: وَهَوَى دُونَ بُلُوغِ الْأَرَبِ لَيِّنَ النَّابِ كَلِيلَ الْمُخْلَبِ

=== BLOCK 26: Cut Box Part 1 ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
[UNIQUE_ID]: b30859
[BLOCK_TITLE]: التضحيات المشرفة للأجدادِ مِنْ أَجْلِ الوَطَنَ(:
[CONTENT]: والشُّهَدَاء(، )تَمْجِيدُ تمجِيدُ النَّضْحِيَاتِ الَّتِي قَدَّمَهَا الشَّعْبُ السوري لنيل استقلاله، والاعتزاز بها )تَجِيد الشهادة التضحيات المشرفة للأجدادِ مِنْ أَجْلِ الوَطَنَ(: - - ۱۳۰ عمر أبو ريشة : بدر الدين الحامد:

--- END STREAM ---
