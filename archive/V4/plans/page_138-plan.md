# **SESSION 138**

[TASK DEFINITION]
Objective: Implement page 138.
File: `pages/page_138.html`
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
[UNIQUE_ID]: b21772
[LESSON_NUMBER]: 138
[CHAPTER_TITLE]: page 138
[CATEGORY_HEADER]: 138
[SECTION_HEADER]: 138
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Poem (Free Verse) ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b03266
[POET_NAME]:
[BIO_TEXT]:
[POEM_VERSES]:
[RIGHT_HEMISTICH]: لَنْ يَمُرَّ العَائِدُون
[LEFT_HEMISTICH]: حَرَسُ الْحُدُودِ مُرَابِط
[RIGHT_HEMISTICH]: يَحْمِي الْحُدُودَ مِنَ الْحَنين
[LEFT_HEMISTICH]:

=== BLOCK 3: Block ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b18922
[BLOCK_TITLE]:
[CONTENT]:
<p class="text-accent mb-0">ويُعْلِنُ محمود درويش على لِسَانِ جُنُودِ الصَّهَائِنَةِ هذا المنْعَ حِيْنَمَا يَنْقُلُ لَنَا نَصَّ التَّحْذِيرِ الذي أَلقَاهُ هَؤلاء الجنود على أسماع المهَجْرِينَ الرَّاغِبين بِالعَوْدَة : لَدَيْنَا أمر بإطلاق الرصاص على كُلِّ مَنْ يُحاولُ اجتياز هذا الجسر، فعلى هذا الجِسْرِ سَتَكون نهاية كُلِّ مَنْ تُسَوَلُ لَهُ نَفْسُهُ التَّفْكِيرَ بِالعَوْدَةِ إِلَى الوَطَنِ يَقُولُ:</p>

=== BLOCK 4: Poem (Free Verse) ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b99128
[POET_NAME]:
[BIO_TEXT]:
[POEM_VERSES]:
[RIGHT_HEMISTICH]: أَمْرٌ بِإِطلاق الرصاص على الذي
[LEFT_HEMISTICH]: يَجْتَازُ هَذا الجِسْر؛ هذا الجِسْرُ
[RIGHT_HEMISTICH]: مِقْصَلَةُ الذِي مَا زَالَ يَحْلُمُ
[LEFT_HEMISTICH]: بالوطن

=== BLOCK 5: Block ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b77237
[BLOCK_TITLE]:
[CONTENT]:
<p class="mb-0">وهَكَذَا نَجِدُ أَنَّ الأدب العَرَبِيَّ ظَلَ مُلازِمَا لِلقَضَايا الوَطَنِيَّة والقومية التي تبرز في الساحة العربية، فقد وَجَدَ الأدباء في هذه القضايا مادةً غزيرة غَمَسُوا فيها أقلامَهُم، فَصَاغُوا منها أَدَبًا تَجَلَّتْ فِيهِ الفَرْحَةُ الصَّاخِبَةُ بِتَحَقَّقِ انتِصَارِ تشرين، وَبَرَزَ فِيهِ التَّأْكِيدُ على عَدَمِ تَخَلِّي المهجرين الفِلَسْطِينيين عَنْ حُلُمِ العَوْدَة.ِ كما تَبَدَّى في صَفَحَاتِ هذا الأدب الكشف عن هَضْمِ الصَّهَائِنَةِ حُقُوقَ الْمُهَجَرِين الفلسطينيين، ومَنْعِهِم مِنَ العَوْدَةِ إِلَى دِيَارِهِم.</p>

=== BLOCK 6: Benefit Warning ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[UNIQUE_ID]: b03026
[BENEFIT_TITLE]: الموضوع المقترح المكتوب الرابع:
[CONTENT]:
<p class="mb-0">قيل : ((شَغَلَتِ القضايا الوطنية والقومية اهتمام الأدباء العرب، فَعَبَّرُوا عَنْ فَرَحِهِم بِجَلَاءِ المُستَعْمِرِ الغَرْبِي عَنْ أَرْضِ الوطن، مُبْرِزِينَ اعتزازهم بتدمير حصون الصهاينة في حرب تشرين، مُمَجِّدِينَ التَّضْحِيَاتِ الْمُشْرَفَةَ التي حَقَّقَتِ الجلاء)). ناقش المؤضُوعَ السَّابِقَ وَأَيَدْ مَا تَذْهَبُ إِلَيْهِ بِالشَّوَاهِدِ الْمُنَاسِبَة،ِ مُوَفِّقًا الشَّاهِدَ الآتي على ما يناسِبُهُ مِنَ الْفِكَرِ السَّابِقَةِ قَالَ الشاعر عبد الرحيم الحصني:</p>

=== BLOCK 7: Poem ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b04663
[POET_NAME]:
[BIO_TEXT]:
[POEM_VERSES]:
[RIGHT_HEMISTICH]: ونَسَفْتَ بِالزَّحْفِ المُقَدَّسِ ما ابتنى
[LEFT_HEMISTICH]: حِقْدُ العداةِ مِنَ الحصون وشِيدَا

=== BLOCK 8: Block ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b40409
[BLOCK_TITLE]: إجابة الموضوع المقترح المكتوب الرابع :
[CONTENT]:
<p>وَقَعَتِ الْأُمَّةُ العَرَبِيَّةُ بَينَ مَخَالِبِ الدَّولِ الاستعمارية، والكيان الصهيوني الذين اندَفَعُوا نَحْوَهَا كالوحوش الضَّارِيَةِ التِي تَنْقَضُ على الفريسة لِتَفْتِكَ بِهَا، إِلَّا أَنَّ أَبْنَاءَ الوَطَنِ العربي، بما فُطِرُوا عليه من إباء للظلم وتَعَشُّقِ للحُرِّيَّة،ِ لَمْ يَكُونُوا صَيْدًا سَهْلًا، فقد هَبُوا في وَجْهِ الدُّخَلَاءِ فِي غَضْبَةٍ عَارِمَة،ِ وَثَوْرَةِ لَاهِبَةٍ للكِفَاحِ والنِّضَالِ لِتَحْرِيرِ وَطَنِهِم وإعادةِ وَحْدَتِهِ التي مُزِّقَتْ، واستردادِ حُرِّيَّتِهِ التي سُلِبَتْ.</p>
<p>وقد استَجَابَ الأَدَبُ العَرَبِيُّ هَذَا التَّطُورِ الخلاقِ فِي النَّفْسِ الْعَرَبِيَّة،ِ فَوَاكَبَ مَسِيرَةَ النِّضَال،ِ وَشَحَنَ النُّفُوسَ بِرُوحِ الثَّوْرَةِ وَالكِفَاحِ لتحرير الأُمَّةِ المُسْتَعْبَدَةِ وَتَوْحِيدِ الوَطَنِ الممزق.</p>
<p>فقد قام الأدباء بالتَّعْبِيرِ عَنِ الفَرَحِ بِجَلَاءِ الْمُسْتَعْمِرِ الغَرْبِي عَنْ أَرْضِ الوطَنِ؛ ذَلِكَ أَنَّ يَوْمَ السَّابِع عشرَ مِنْ نَيْسَان،َ عَامَ سِت وأرْبَعِينَ وَتِسْعِمِئَةٍ والف، يوم مجيد، وصفحة مشرقة في تاريخ سورية ؛ كَتَبَ سُطُورَهَا أَبْنَاؤُها الْأَبَاةُ بِدِمَائِهِم. فالجلاءُ ثَمَرَةٌ لِكِفَاحِ مُرِّ خَاضَهُ الشَّعْبُ العَرَبِي فِي سُورِيَّة منذ وَطِئَتْ أَقْدَامُ الْمُسْتَعْمِرِينَ أَرْضَ سُورِيَّة.</p>
<p>فقد زَلَزَلَ السُّوريون الأَرْضَ تَحْتَ أَقْدَامِ الفرنسيين بثورات لاهِبَةٍ حَارِقَةٍ عَمَّتْ كُلَّ مِنْطَقَةٍ مِنْ رَبُوعِ الوَطَن،ِ أَنْسَتِ المحتل الطَّامِعَ أَطْمَاعَهُ الْخَبِيْثَةَ التي يَرُومُ مِنْ وَرَائِهَا تَدْنِيْسَ الْأَرْضِ وَسَلْبَ الكَرَامَةِ حَيْثُ تَحَوَّلَتْ كُلُّ بُقْعَةٍ مِنْ بِقَاعِ سُورِيَّة إلى مِدْفَعِ هَادِرٍ يَرْمِي الطَّامِعِينَ الغَادِرِينَ بِقَذَائِفِ النَّارِ الملتَهِبَةِ؛ ليُطَهِّرَ بِحِمَمِهَا المُنصَهِرَةِ الأَرْضَ وَيُحَرِّرَ الإِنْسَان. فَمِنْ مَدِينَةِ النَّواعِيرِ يَقِفُ شَاعِرُ العاصي بَدْرُ الدِّينِ الْحَامِدِ مُبْتَهْجًا مُزْهُوًّا فِي أَوَّلِ عِيدٍ جَلَاءٍ عَنْ سُورية؛ ليتغنى بهذا المنجَزِ العَظِيم، مُظْهِرًا فَرَحَهُ العَارِم،ُ مُؤَكَدًا أَنَّ الجلاءَ فَرْحَةٌ عَرَبِيَّة،ٌ وَغُصَّةٌ غَرْبِيَّةٌ نَاشِبَةٌ لا يزيلها تعاقب السنين. يقول:</p>

=== BLOCK 9: Poem ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b64001
[POET_NAME]:
[BIO_TEXT]:
[POEM_VERSES]:
[RIGHT_HEMISTICH]: يَوْمُ الجَلَاءِ هُوَ الدُّنْيَا وَزَهُوهَا
[LEFT_HEMISTICH]: لنا ابتهاج وللباغِينَ إِرْغَامُ

=== BLOCK 10: Block ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b87339
[BLOCK_TITLE]:
[CONTENT]:
<p class="mb-0">ومِنْ حَلَبَ يَنْهَضُ ابْنُ منبج الشَّاعِرُ عُمر أبُو ريشة لِيُصَوّرَ فَرْحَةَ الانتصارِ بِجَلَاءِ المُحْتَلِ عَنْ أَرْضِ الوَطَن،ِ فَيَطْلُبُ مِنَ الْحَرِّيَّةِ أَنْ تَسِيرَ بِزَهْوٍ وفخارِ فَوْقَ ثَرَى بلادنا، وأَنْ تَخْتَالَ كما تختالُ العَرُوس،ُ وتُجَرِّرَ أَدْيَالَ الشُّهُبِ السَّاطِعَة، وتُزَيِّنَ بِهَا أَرْجَاءَ بِلَادِنَا، وَيُؤْكِدُ لها أَنَّ لِقَاءَهَا قَدْ حسن وجاد بعد تلك الفُرْقَةِ التي ضاقَ فِيهَا الصَّدْرُ من شدة الوجد والشوق يقول :</p>

=== BLOCK 11: Poem ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b07374
[POET_NAME]:
[BIO_TEXT]:
[POEM_VERSES]:
[RIGHT_HEMISTICH]: يا عروس المجد تيْهِي واسحبي
[LEFT_HEMISTICH]: في مَغَانِينَا أذيالَ الشُّهُبِ
[RIGHT_HEMISTICH]: يا عروس المجد طَابَ الْمُلْتَقَى
[LEFT_HEMISTICH]: بَعْدَمَا طَالَ جَوَى المُغْتَرِبِ

--- END STREAM ---
