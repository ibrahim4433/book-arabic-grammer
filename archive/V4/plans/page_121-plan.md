# **SESSION 121**

[TASK DEFINITION]
Objective: Implement page 121.
File: `pages/page_121.html`
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
[UNIQUE_ID]: b00121
[LESSON_NUMBER]: 121
[CHAPTER_TITLE]: page 121
[CATEGORY_HEADER]: 121
[SECTION_HEADER]: 121
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: النص ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b00122
Title: اقرأ الأَسْطُرَ الآتية، ثُمَّ نَفْذِ النشاط الذي يليها :
Content:

=== BLOCK 3: القصيدة ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b00123
Title:
Poet:
Verse 1 Right: لم يَعْرِفُوا أَنَّ الطَّرِيقَ إِلَى الطَّرِيقِ
Verse 1 Left: دَم،ْ وَمِصْيَدَة،ٌ وَبِيْدُ
Verse 2 Right: كُلُّ القوافِلِ قَبْلَهُمْ غَاصَتْ
Verse 2 Left: وكانَ النَّهْرُ يَبْصُقُ ضِفَتَيْهِ
Verse 3 Right: حَرَسُ الْحُدُودِ مُرابط
Verse 3 Left: وهِجْرَةُ الدَّم في مِيَاهِ النَّهْرِ تَنْحَتُ
Verse 4 Right: من حصى الوادي تماثيلًا
Verse 4 Left: لَهَا لَوْنُ النُّجُوم

=== BLOCK 4: النشاط - الجمل الاسمية ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b00124
Title: نشاط استخراج الجمل الاسمية
Content: استخرج الجمل الاسمية الواردة ففِي الأَسْطُرِ السَّابِقَة،ِ وَاذْكُرُ نَوْعَ رُكْنَيْ كُلِّ مِنْهَا .

=== BLOCK 5: جدول الجمل الاسمية ===
(Component: TEMPLATE_C_TABLE.html)
[UNIQUE_ID]: b00125
Headers: الجملة الاسمية | الركن الأول | نوعه | الركن الثاني | نوعه
Row 1: أن الطريق ... دم | الطريق | اسم | دم | مفرد
Row 2: كل القوافل قبلهم غاصت | كل | اسم | (غاصت) | جملة فعلية
Row 3: حرس الحدود مرابط | حرس | اسم | مرابط | مفرد
Row 4: هجرة الدم ... تنحت | هجرة | اسم | (تنحت) | جملة فعلية
Row 5: لها لون النجوم | لون | اسم | (لها) | شبه جملة

=== BLOCK 6: قاعدة الإبدال ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b00126
Title: قاعدة الإبدال (في الكلمات التي تحتها خط)
Content: اشْرَحْ قَاعِدَةَ الإِبْدَالِ فِي الكَلِمَاتِ التي تحتها خط فيما يأتي: كَانُوا ثَلاثَةً عَائِدِينَ ... وَبَعْدَ دَقَائِقَ يَصِلُّون:َ هَلْ فِي البَيْتِ مَاءٌ؟

=== BLOCK 7: قائمة قاعدة الإبدال ===
(Component: TEMPLATE_C_LIST.html)
[UNIQUE_ID]: b00127
Item 1: <span class="highlight-red">عائدين</span> : إبدال، أُبْدِلَتِ الواوُ هَمْزَةً؛ لِأَنَّهَا وَقَعَتْ عَيْنًا فِي صِيغَةِ اسمِ الفاعِلِ المَصُوغِ مِنَ الْفِعْلِ الثَّلاثي الْأَجْوَفِ.
Item 2: <span class="highlight-red">دقائق</span> : إبدال، أُبْدِلَتِ اليَاءُ هَمْزَةً؛ لِأَنَّهَا وَقَعَتْ بَعْدَ أَلِفِ صِيغَةِ مُنْتَهَى الجُمُوعِ.

=== BLOCK 8: قاعدة كتابة التاء ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b00128
Title: قاعدة كتابة التاء المربوطة والمبسوطة (تنبيه)
Classes: .block-header.accent
Content: اشْرَحْ قَاعِدَةَ كِتَابَةِ التَّاءِ المربوطة والمُبْسُوطَةِ فِي الكَلِمَاتِ الآتية: (غاصَتْ، قبعة، الصَّمْت).

=== BLOCK 9: قائمة قاعدة كتابة التاء ===
(Component: TEMPLATE_C_LIST.html)
[UNIQUE_ID]: b00129
Item 1: ج - <span class="highlight-red">غَاصَتْ</span> : كُتِبَتِ التَّاءُ مَبْسُوطَةً؛ لِأَنَّهَا تَاءُ التَّأنِيثِ السَّاكِنَةُ.
Item 2: <span class="highlight-red">قَبَعَة</span> : كُتِبَتِ التَّاءُ مَرْبُوطَةً؛ لِأَنَّهَا جَاءَتْ فِي اسمٍ مُفْرَدٍ مُؤَنَّثٍ.
Item 3: <span class="highlight-red">الصَّمْتُ</span> : كُتِبَتِ التَّاءُ مَبْسُوطَةً؛ لِأَنَّهَا مِنْ أَصْلِ الاسمِ، أو : كُتِبَتْ مَبْسُوطَةً؛ لأنها جاءَتْ في اسمٍ ثلاثيٍّ ساكنِ الوَسَطِ.

=== BLOCK 10: إعراب النص ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b00130
Title: إعراب النص
Content: إعْرَابُ المقطع الأَوَّلِ :

=== BLOCK 11: تفصيل الإعراب 1 ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b00131
Word 1: مشيا
Details 1: حالٌ مَنْصُوبة.
Word 2: أو زَحْفًا
Details 2: أو ، حَرْفُ عَطْفٍ زَحْفًا، اسمٌ مَعْطُوفٌ مَنْصُوبٌ.
Word 3: وكان
Details 3: الواو، واو الحال كان، فعل ماض ناقص، مَبْنِي على الفَتْحَةِ الظَّاهِرَةِ.
Word 4: الصَّخْرُ
Details 4: اسم (كانَ) مَرْفُوعٌ.
Word 5: والمَسَاءُ
Details 5: الواو، حَرْفُ عَطْفِ المَسَاءُ، اسم (كانَ) المَحْذُوفة مَرْفُوعٌ.
Word 6: يَدًا
Details 6: خَبَرُ (كَانَ) الْمَحْذُوفة مَنْصُوبٌ.

=== BLOCK 12: تفصيل الإعراب 2 ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b00132
Word 1: لَمْ يَعْرِفُوا
Details 1: لَمْ، حَرْفٌ جازمٌ يَعْرِفُوا، فعل مُضارع مجزوم، وعلامَةُ جَزْمِهِ حَذْفُ النُّونِ ؛ لأَنَّهُ مِنَ الْأَفْعَالِ الخَمْسَةِ. والواو، ضميرٌ مُتَّصِل مبني على السُّكُون، فِي مَحَلِّ رَفْعٍ فَاعِل، والآلِفُ حَرْفُ تَفريق.
Word 2: أَنَّ الطَّريق
Details 2: أَنَّ، حَرْفٌ مُشَبَّهٌ بالفعل الطريق، اسم (أَنَّ) مَنْصُوبٌ وَالْمَصْدَرُ المؤولُ (أَنَّ الطَّرِيقَ دَمَ)، في مَحَلِّ نَصْبٍ، مَفْعُولَ بِهِ.
Word 3: دم
Details 3: خَبَرٌ مَرْفُوعٌ.
Word 4: ومِصْيَدَةٌ
Details 4: الواو، حَرْفُ عَطْفِ مِصْيَدَةٌ، اسمٌ مَعْطُوفٌ مَرْفُوعٌ.
Word 5: وبيد
Details 5: الواو، حَرْفُ عَطْفِ بِيدُ، اسِمٌ مَعْطُوفٌ مَرْفُوعٌ.
Word 6: كُلُّ
Details 6: مُبْتَداً مَرْفُوعٌ.

=== BLOCK 13: تفصيل الإعراب 3 ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b00133
Word 1: القوافِلِ
Details 1: مُضَافٌ إليهِ مَجْرُورٌ.
Word 2: قَبْلَهُمْ
Details 2: مَفْعُولُ فِيهِ ظَرْفُ زَمَانٍ مَنْصُوبٌ.
Word 3: وكان
Details 3: الواو، واو الحال كان، فعل ماض ناقص مبني على الفَتْحَةِ الظَّاهِرَةِ.
Word 4: النَّهْرُ
Details 4: اسم (كانَ) مَرْفُوعٌ.
Word 5: ضِفَتَيْهِ
Details 5: مَفْعُولُ بِهِ أَوَّلٌ مَنْصُوبٌ، وعلامَةُ نَصْبِهِ الياء؛ لِأَنَّهُ مُثَنَّى، وحُذِفَتِ النُّونُ لِلإِضافة. والهاء، ضمير مُتَّصِلِّ مَبْنِي على الكَسْرَةِ فِي مَحَلِّ جَرٍّ، مُضَافُ إليه.
Word 6: قِطَعًا
Details 6: مَفْعُولُ بِهِ ثَانٍ مَنْصُوبٌ.

=== BLOCK 14: تفصيل الإعراب 4 ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b00134
Word 1: المُفَتَتِ
Details 1: صِفَةٌ مَجْرُورَةٌ.
Word 2: العَائِدِين
Details 2: مُضَافَ إِلَيْهِ مَجْرُورٌ، وعلامة جره الياء؛ لأَنَّهُ جَمْعُ مُذَكر سالم. والنُونُ، عوض عَنِ التنوين في الاسم المَفْرَدِ.
Word 3: كَانُوا
Details 3: فعل ماضِ ناقص، مَبْنِيّ على الضَّمَّةِ؛ لاتصاله بواو الجماعة والواو، ضمير مُتَّصِلٌ مَبْنِي على السكون فِي مَحَلِ رَفْعٍ، اسم (كَانَ). والأَلِفُ، حَرْفُ تفريق.
Word 4: ثلاثة
Details 4: خَبَرٌ مَنْصُوبٌ.
Word 5: عَائِدِينَ
Details 5: مُضَافُ إِلَيهِ مَجْرُورٌ، وعلامَةُ جَرَهِ الياء؛ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سالمٌ. والنُّون، عوض عَنِ التنوين في الاسم المفرد.
Word 6: شيخ
Details 6: خبر لمبتدأ مَحْذُوفٍ مَرْفُوعٌ.

=== BLOCK 15: تفصيل الإعراب 5 ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b00135
Word 1: وَابْنَتُهُ
Details 1: الواو، حَرْفُ عَطْفٍ ابْنَتُهُ، اسم معطوف مرفوع والهاء، ضمير مُتَّصِلٌ مَبْنِي عَلَى الضَّمَّةِ فِي مَحَلّ جَرٍّ، مُضَافُ إليه.
Word 2: وجُنْدِي
Details 2: الواو، حَرْفُ عَطْفٍ جُنْدِي، اسمٌ مَعْطُوفٌ مَرْفُوعٌ.
Word 3: قَديم
Details 3: صِفَةٌ مَرْفُوعَةٌ، وعلامَةُ رَفْعِهَا الضَّمَّةُ الظَّاهِرَةُ. وسُكِّنَتْ لِلضَّرورة الشَّعْرِيَّةِ.
Word 4: يَقِفُونَ
Details 4: فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وعلامَةُ رَفْعِهِ ثُبُوتُ النونِ، لأَنَّهُ مِنَ الْأَفْعَالِ الخَمْسَةِ. والواو، ضَمِيرٌ مُتَصِلٌ مَبْنِي على السُّكُونِ فِي مَحَلَّ رفع، فَاعِلٌ.
Word 5: عِنْدَ
Details 5: مَفْعُولُ فِيهِ ظَرْفُ مَكَانٍ مَنْصُوبٌ.
Word 6: الجسر
Details 6: مُضَاف إليه مَجْرُورٌ.

=== BLOCK 16: تفصيل الإعراب 6 ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b00136
Word 1: كان
Details 1: فعل ماض ناقص، مبني على الفتحة الظاهرة.
Word 2: الجسر
Details 2: اسم (كانَ) مَرْفُوعٌ.
Word 3: نَعْسَانًا
Details 3: خَبَرُ (كَانَ) منصوب.
Word 4: وكان
Details 4: الواو ، حَرْفُ عَطْفٍ كَانَ، فِعْلٌ مَاضِ ناقص، مَبْنِي على الفَتْحَةِ الظَّاهِرَةِ.
Word 5: اللَّيْلُ
Details 5: اسم (كانَ) مَرْفُوعٌ.
Word 6: قَبْعَةَ
Details 6: خَبَرُ (كان) منصوب.

=== BLOCK 17: تفصيل الإعراب 7 ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b00137
Word 1: وبعد
Details 1: الواو، حَرْفُ استئنافٍ بَعْدَ مَفْعُولُ فِيهِ ظَرْفُ زَمَانٍ مَنْصُوبٌ.
Word 2: دَقَائِقٍ
Details 2: مُضَافُ إِلَيْهِ مَجْرُورٌ.
Word 3: يَصِلُونَ
Details 3: فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وعلامَةُ رَفْعِهِ ثُبُوتُ النُّونِ لَأَنَّهُ مِنَ الْأَفْعَالِ الخمسة. والواو، ضمير مُتَّصِلٌ مَبْنِي على السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.

--- END STREAM ---
