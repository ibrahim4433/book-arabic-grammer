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
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
15. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[CATEGORY_HEADER]: 138
[SECTION_HEADER]: 138
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+
[CHAPTER_TITLE]: page 138
[LESSON_NUMBER]: 138

=== BLOCK 2: مدخل إلى النص ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مدخل إلى النص
Content:
<div class="text-center font-bold mb-2mm">
لَنْ يَمُرَّ العَائِدُون<br>
حَرَسُ الْحُدُودِ مُرَابِط<br>
يَحْمِي الْحُدُودَ مِنَ الْحَنين
</div>
<p class="text-accent">ويُعْلِنُ محمود درويش على لِسَانِ جُنُودِ الصَّهَابِنَةِ هذا المنْعَ حِيْنَمَا يَنْقُلُ لَنَا نَصَنَّ التَّحْذِيرِ الذي أَلقَاهُ هَؤلاء الجنود على أسماع المهَجْرِينَ الرَّاغِبين بِالعَوْدَة : الدينا أمر بإطلاق الرصاص على كُلِّ مَنْ يُحاولُ اجتياز هذا الجسر، فعلى هذا الحِسْرِ سَتَكون نهاية كُلِّ مَنْ تُسَوَلُ لَهُ نَفْسُهُ التَّفْكِيرَ بِالعَوْدَةِ إِلَى الوَطَنِ يَقُول:ُ</p>

=== BLOCK 3: الشاهد الشعري ===
(Component: TEMPLATE_C_POEM.html)
أَمْرٌ بِإِطلاق الرصاص على الذي | يَجْتَازُ هَذا الحِسْر؛ هذا الحِسْرُ
مِقْصَلَةُ الذِي مَا زَالَ يَحْلُمُ | بالوطن

=== BLOCK 4: فائدة ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: فائدة
Content: وهَكَذَا نَجِدُ أَنَّ الأدب العَرَبِيَّ ظَلَ مُلازِمَا لِلقَضَايا الوَطَنِيَّة والقومية التي تبرز في الساحة العربية، فقد وَجَدَ الأدباء في هذه القضايا مادةً غزيرة غَمَسُوا فيها أقلامَهُم، فَصَاعُوا منها أَدَبًا تَجَلَّتْ فِيهِ الفَرْحَةُ الصَّاخِبَةُ بِتَحَقَّقِ انتِصَارِ تشرين، وَبَرَزَ فِيهِ التَّأْكِيدُ على عَدَمِ تَخَلَّي المهجرين الفِلَسْطِينيين عَنْ حُلُمِ العَوْدَة.ِ كما تَبَدِّى في صَفَحَاتِ هذا الأدب الكشف عن هَضْمِ الصَّهَائِنَةِ حُقُوقَ الْمُهَجَرِين الفلسطينيين، ومَنْعِهِم مِنَ العَوْدَةِ إِلَى دِيَارِهِم.

=== BLOCK 5: الموضوع المقترح المكتوب الرابع ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الموضوع المقترح المكتوب الرابع:
Content: قيل : ))شَعْلَتِ القضايا الوطنية والقومية اهتمام الأدباء العرب، فَعَبَّرُوا عَنْ فَرَحِهِم بِجَلَاءِ المُستَعْمِرِ الغَربي عَنْ أَرْضِ الوطن، مُبْرِزِينَ اعتزازهم بتدمير خصون الصهاينة في حرب تشرين، مجدينِ التَّصْحِيَاتِ الْمُشْرَفَةَ التي حَقَّقَتِ الخلاء((.<br>ناقش المؤضُوعَ السَّابِقَ وَأَيَدْ مَا تَذْهَبُ إِلَيْهِ بِالشَّوَاهِدِ الْمُنَاسِبَة،ِ مُوَ فَا الشَّاهِدَ الآتي على ما يناسِبُهُ مِنَ الْفِكَرِ السَّابِقَةِ قَالَ الشاعر عبد الرحيم الحصني:
<div class="text-center font-bold mt-2mm mb-2mm">
ونَسَفْتَ بِالرَّحْفِ المُقَدَّسِ ما ابتنى<br>
حِقْدُ العداةِ مِنَ الحصون وشيدا
</div>

=== BLOCK 6: إجابة الموضوع المقترح ===
(Component: TEMPLATE_C_BLOCK.html)
Title: إجابة الموضوع المقترح المكتوب الرابع :
Content: وَقَعَتِ الْأُمَّةُ العَرَبِيَّةُ بَينَ مَخَالِبِ الدَّولِ الاستعمارية، والكيان الصهيوني الذين اندَفَعُوا تَحْوَهَا كالوحوش الضَّارِيَةِ التِي تَنْقَضُ على الفريسة لِتَفْتِكَ بِهَا، إِلَّا أَنَّ أَبْنَاءَ الوَطَنِ العربي، بما فُطِرُوا عليه من إباء للظلم وتَعَشْقِ للحُرِّيَّة،ِ لَمْ يَكُونُوا صَيْدًا سَهْلًا، فقد هَبُوا في وَجْهِ الدُّخَلَاءِ فِي غَضْبَةٍ عَارِمَة،ِ وَثَوْرَةِ لَاهِبَةٍ للكِفَاحِ والنِّضَالِ لِتَحْرِيرِ وَطَنِهِم وإعادةِ وَحْدَتِهِ التي مُزَقَت،ْ واستردادِ حُرِّيَّتِهِ التي سُلِبَتْ .<br>وقد استَجَابَ الأَدَبُ العَرَبِيُّ هَذَا التَّطُورِ الخلاقِ فِي النَّفْسِ الْعَرَبِيَّة،ِ فَوَاكَبَ مَسِيرَةَ النَّصَال،ِ وَشَحَنَ النُّفُوسَ بِرُوحِ التَّوْرَةِ وَالكِفَاحِ لتحرير الأُمَّةِ المُسْتَعْبَدَةِ وَتَوْحِيدِ الوَطَنِ الممزق. فقد قام الأدباء بالتَّعْبِيرِ عَنِ الفَرَحِ بِجَلَاءِ الْمُسْتَعْمِرِ الغَرْنِي عَنْ أَرْضِ الوطَنِ؛ ذَلِكَ أَنَّ يَوْمَ السَّابِع عشرَ مِنْ نَيْسَان،َ عَامَ سِت وأرْبَعِينَ وَتِسْعِمِنَةٍ والف، يوم مجيد، وصفحة مشرقة في تاريخ سورية ؛ كَتَبَ سُطُورَهَا أَبْنَاؤُها الْأَبَاةُ بِدِمَائِهِم. فالجلاءُ ثَرَةً لِكِفَاحِ مُرِّ خَاضَهُ الشَّعْبُ العَرَنِي فِي سُورِيَّة منذ وَطَاتُ أَقْدَامُ الْمُسْتَعْمِرِينَ أَرْضَ سُورِيَّة. فقد زَلَزَلَ السُّوريون الأَرْضَ تَحْتَ أَقْدَامِ الفرنسيين بثورات لاهِبَةِ حَارِفَةٍ عَمَّتْ كُلَّ مِنْطَقَةٍ مِنْ رَبُوعِ الوَطَن،ِ أَنْسَتِ المحتل الطَّامِعَ أَطْمَاعَهُ الْخَبِيْثَةَ التي يَرُومُ مِنْ وَرَائِهَا تَدْنِيْسَ الْأَرْضِ وَسَلْبَ الكَرَامَةِ حَيْثُ تَخَوَّلَتْ كُلُّ بُفْعَةٍ مِنْ بِقَاعِ سُورِيَّة إلى مِدْفَعِ هَادِرٍ يَرْمِي الطَّامِعِينَ الغَادِرِينَ بِقَذَائِفِ النَّارِ الملتَهِبَةِ؛ ليُطَهْرَ بِحِمَمِهَا المُنصَهِرَةِ الأَرْضَ وَيُخْرَرَ الإِنْسَان. فَمِنْ مَدِينَةِ النَّواعِيرِ يَقِفُ شَاعِرُ العاصي بَدْرُ الدِّينِ الْحَامِدِ مُبْتَهْجًا مَنْهُوا فِي أَوَّلِ عِيدٍ جَلَاءٍ عَنْ سُورية؛ ليتغنى بهذا المنجَزِ العَظِيم، مُظْهِرًا فَرَحَهُ العَارِم،ُ مُؤَكَدًا أَنَّ الخلاءَ فَرْحَةٌ عَرَبِيَّة،ٌ وَعَصَّةً عَرْبِيَّةٌ نَاشِبَةٌ لا يزيلها تعاقب السنين. يقول:

=== BLOCK 7: الشاهد الشعري ===
(Component: TEMPLATE_C_POEM.html)
يَوْمُ الخَلَاءِ هُوَ الدُّنْيَا وَزَهُوهَا | لنا ابتهاج وللباغِينَ إِرْغَامُ

=== BLOCK 8: الشاعر عمر أبو ريشة ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الشاعر عمر أبو ريشة
Content: ومِنْ حَلَبَ يَنْهَضُ ابْنُ منبج الشَّاعِرُ عُمر أبُو ريشة لِيُصَوّرَ فَرْحَةَ الانتصارِ بِجَلَاءِ الخَتَلِ عَنْ أَرْضِ الوَطَن،ِ فَيَطْلُبُ مِنَ الْحَرِّيَّةِ أَنْ تَسِيرَ برهو وفخارِ فَوْقَ تَرَى بلادنا، وأَنْ تَخْتَالَ كما تختالُ العَرُوس،ُ وتُجَرِّرَ أَدْيال الهب السَّاطِعَة، وتُزَيْنَ بِهَا أَرْجَاءَ بِلَادِنَا، وَيُؤْكِدُ ها أَنَّ لِقَاءَهَا قَدْ حسن وجاد بعد تلك الفُرْقَةِ التي ضاقَ فِيهَا الصَّدْرُ من شدة الوجد والشوق يقول : <br> - - -

=== BLOCK 9: الشاهد الشعري ===
(Component: TEMPLATE_C_POEM.html)
يا عروس المجد تيْهِي واسحي | في في ونهب
يا عروس المجد طَابَ الْمُلْتَقَى | بغي من السنة المغترب
<div class="text-center">۷۱</div>

--- END STREAM ---
