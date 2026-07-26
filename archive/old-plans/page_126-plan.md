# **SESSION 126**

[TASK DEFINITION]
Objective: Implement page 126.
File: `pages/page_126.html`
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
[LESSON_NUMBER]: 126
[CHAPTER_TITLE]: page 126
[CATEGORY_HEADER]: 126
[SECTION_HEADER]: 126
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Cut Content Continuation ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
Inner Component: TEMPLATE_C_LIST.html
Content:
- <span class="text-accent">ج -</span> الشَّاعِرُ رَافِضٌ لهذه الحُدُودِ غَيْرُ مُعْتَرِفٍ بِهَا، وقد تَجَلَّى ذلك مِنْ خلالِ وَصْفِهِ لِلْأَحَادِيثِ التِي تَدُورُ حَوْلَ هذه الحُدُودِ بِالْأَسَاطِيرِ والأَبَاطِيلِ الزَّائِفَةِ.

=== BLOCK 3: Values Question ===
(Component: TEMPLATE_C_BLOCK.html)
Content:
<div class="mb-4">- تجلَّتْ في النص قِيَمٌ كثيرة ، اذكرْ بَعْضًا منها. مُحَدِّدًا مِنَ النَّصِّ مُؤَشِّرًا لكل منها.</div>

=== BLOCK 4: Values Table ===
(Component: TEMPLATE_C_TABLE.html)
Headers: القيمة | مُؤشِّرُها
Row 1: رَفْضُ التَّجْزِيئَةِ وإنكار الحدود التي رسمها المُسْتَعْمرون | تلاشتْ مَعَ الْقُيُودِ أَسَاطِيرُ حَدُودٍ رَهِيبَةٌ نَكْرَاءُ
Row 2: التَّفَاوُلُ بمسْتَقْبَلِ مُشْرِقٍ وَاعِدٍ | هَادَى الغَدُ الضَّحُوكَ طَلِيْقًا وبِهِ مِنْ سَنَا الرَّجَاءِ سَنَاءُ
Row 3: الاعتزاز بِتَحَرُّرِ الْأُمَّةِ الْعَرَبِيَّةِ | تَهْتِفُ بِأُمَّتِي إِنَّمَا عَادَتْ وَإِنَّا فِي أَرْضِنَا طَلَقَاءُ
Row 4: تَمْجِيدُ الأَمَّةِ العَرَبِيَّةِ وَالتَّغَنِي بِصِفَاتِهَا | أُمَّةٌ جَبَلَتْهَا مِنْ عَبِيرِ الْمَكَارِمِ العَلْيَاءُ
Row 5: تَحْفِيزُ الْمُتَرَدِّدِين للالتحاقِ بِرَكْبِ الوَحْدَةِ العَرَبِيَّةِ | أَقْبِلُوا أَيُّهَا الحَيَارَى فَهَذا الدَّرْبُ طَلْقٌ، مُشَوِّقٌ وَضَّاءُ
Row 6: الإيمانُ بِقُدْرَةِ الجَمَاهِيرِ العَرَبِيَّةِ على بِنَاءِ مَا هَدَّمَهُ المُسْتَعْمِرُ | فِي غَدٍ تَزْحَفُ الْجُمُوعُ لِتَبْنِي بِيَدَيْهَا مَا هَدَّمَ الْأَعْدَاءُ

=== BLOCK 5: Poetry Comparison Introduction ===
(Component: TEMPLATE_C_POEM.html)
Context/Bio: ه- قَالَ الشَّاعِرُ سُلَيْمَان العيسى:
Verse 1 Right: يا ليالي الضياع والقيد زولي
Verse 1 Left: نَحْنُ بَاقُونَ وَحْدَةً لَن تَزُولَا

=== BLOCK 6: Question & Answer (Comparison) ===
(Component: TEMPLATE_C_BLOCK.html)
Inner Component: TEMPLATE_C_LIST.html
Content:
- <span class="text-accent">وازن بَيْنَ هَذَا الْبَيْتِ، وَالبَيْتِ الثَّانِي مِنْ أَبْيَاتِ النَّصِّ، وَبَيِّنْ أَيُّهَمَا أَفْضَلُ فِي التَّعْبِيرِ عَنِ الْمَعْنَى مَعَ التَّعْلِيلِ.</span>
- <span class="text-accent">ج - التشابه:</span> كلا الشَّاعِرَيْنِ يَتَحَدَّثُ عَنِ القُيُودِ والخلاص مِنْهَا.
  أو: كلا الشَّاعِرَين يَتَغَنَّى بِالوَحْدَةِ.
  أو: كلا الشَّاعِرَيْنِ يُعَبِّرُ عَنْ فَرَحِهِ بِالوَحْدَةِ.
- <span class="text-accent">الاختلاف:</span>
  - سلامة عبيد أَكَّدَ أَنَّ القُيُودَ تَلَاشَتْ، بينما سُلَيْمَانَ العِيسَى يَطْلُبُ مِنَ القُيُودِ أَنْ تَزُولَ.
  - سلامة عبيد يُؤَكِّدُ أَنَّ أَسَاطِيرَ الحُدُودِ تَلَاشَتْ مَعَ القيود، بينما سُلَيْمَان العِيسَى يَطْلُبُ أَنْ تَزُولَ لَيَالِي الضَّيَاعِ مَعَ القُيُودِ.

=== BLOCK 7: Note / Benefit ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: ملاحظة
Content: يُكتفى بوجه واحد للتشابه، وبوجه واحد للاختلاف.

=== BLOCK 8: Technical Level (Answers part) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المستوى الفني
Inner Component: TEMPLATE_C_LIST.html
Content:
- <span class="text-accent">في البَيْتِ الأَخِيرِ مُحَسِّنٌ بديعي استخرجه وسمه، وَادْكُرْ قِيْمَةً مِنْ قِيَمِهِ الفَنِيَّةِ مَعَ التَّوْضِيح.</span>
  <br> - المحسن البديعي: (تبني، هَدَّمَ).
  <br> - تَسْمِيةُ المحسن البديعي: طباق إيجاب.
  <br> - القيمة الفنية وتوضيحها: إعمالُ العَقْلِ في المتناقضات حيث استطاع الشاعر من خلال هذا الطباق أن يعمل عقل المتلقي في المتناقضات فجعله يدرك الفرق الشاسع بين حالة البناء، وَحَالَةِ الهَدْم.
- <span class="text-accent">في البَيْتِ الأَوَّلِ مُحَسِّنٌ بَدِيعِي، اسْتَخْرِجْهُ وَسَمَه،ِ وَادْكُرْ قِيمَتَهُ الفَنِيَّةَ.</span>
  <br> ج - (ضِيَاءُ، حُدَاءُ).
  <br> - تَسْمِيَةُ المحسن البديعي: تصريع.
  <br> - قِيمَتُهُ الفَنِيَّةُ : يضفي على الكلام رونقًا وعذوبة، ويمنحه إيقاعا موسيقيا جميلا. ويعمد الشعراء إلى استخدامه في المطالع غالبا من أجل الإعلام عن القافية قبل الوصول إليها.
- <span class="text-accent">في قول الشاعر : الغَدُ الضَّحوك صورة بلاغيَّةٌ، اشرَحْهَا، وَوَضَحْ وَظِيفَةِ الإِيحَاءِ، والشرح والتوضيح.</span>
  <br> ج - الصورة: (الغَدُ الضَّحُوك).
  <br> - تسمية الصورة: استعارة مكنية.
  <br> - تحليل الصورة: شبه الغد بإنسان يضحك، فحذف المشبه به، وأبقى شيئًا من لوازمه وهو : "الضحوك".
  <br> توضيح وَظِيفَةِ الإِيحَاءِ : جَعَلَ الشَّاعِرُ الصُّورَةَ موحِيَةً بتشبيهه الغد بإنسان يضحك، فهذا أوحى بالمستقبل المشرق والخير الوفير وتحقق الأحلام، وأثار مشاعر الفرح والبَهْجَةِ وَالتَّفَاول.

=== BLOCK 9: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: اختر الإجابة الصَّحِيْحَةَ فيما يَأْتِي: في البَيْتِ الثَّالِثِ مُحَسِّنٌ بديعي، نوعُه: (جناس تام، جناس ناقص، طِبَاقُ إِيجَابٍ، طِبَاقُ سَلْبٍ).
Number: ٢
Question: في قول الشاعر : (سَرَابٌ دروبكم) تقديم وتأخير غَرَضُهُ : (أ- التوكيد، ب- التشويق للمتأخر، ج- إبراز أهمية المتقدم، د- ب + ج).

=== BLOCK 10: Page End Footer ===
(Component: TEMPLATE_C_BLOCK.html)
Content: <div class="text-center">- - ١٢٦ مكرر</div>

--- END STREAM ---
