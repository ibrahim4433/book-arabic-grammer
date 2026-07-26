# **SESSION 167**

[TASK DEFINITION]
Objective: Implement page 167.
File: `pages/page_167.html`
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
[LESSON_NUMBER]: 167
[CHAPTER_TITLE]: page 167
[CATEGORY_HEADER]: 167
[SECTION_HEADER]: 167
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Cut Text Continuation ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
(Inner Component: TEMPLATE_C_BLOCK.html)
Title: الخصائص الإبداعية في النص
Content: - مِنَ الْخَصَائِصِ الإبداعِيَّةِ فِي النَّصِّ: (استِعْمَالُ اللَّغَةِ المَأْنُوسَةِ الْمَشْحُونَةِ بِطَاقَاتِ عاطفية وخَيَالِيةِ رَقِيقَة،ٍ والتركيز في موضوعات يثيرها التَّشَاؤُمُ والكابة).

=== BLOCK 3: The Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Title: فائدة حول سمات الإبداعية والتمثيل لها
Headers: السمة | التمثيل لها
Row 1: ١- ظهور ذاتية الشاعر، وعُمْقُ المعاناة (الذَّاتِيَّةُ والغنائية). | الأمثلة التي تدعم هذه السمة كلمات تشتمل على ضمير المتكلم.
Row 2: ۲- استخدام اللغة المأنوسَةِ الإِيحَائِيَّةِ الْمَشْحُونَةِ بِعَواطف إنسانية حارة. | الأمثلة الملائمة لهذه السمة تراكيب وجمل تبرز فيها المشاعر العاطفية.
Row 3: ٣- الجنوح إلى الخيال. | يكون الاستشهاد على هذه السمة من خلال اختيار الصور البيانية (تشبيه – استعارة).
Row 4: ٤- الجنوح إلى الطبيعة وبثها الشكوى، والتغني بجمالها. | يكون التمثيل لهذه السمة من خلال اختيار جمل فيها توجه إلى الطبيعة.
Row 5: ٥- النزوع إلى التحرر مِنَ الوزن والقافية. | النص كله في شعر التفعيلة.
Row 6: ٦- الوَحْدَةُ المَقْطَعِيَّة. | -
Row 7: ٧- تمجيد الألم بوصفه معلماً للإنسان - التركيز على موضوعات يُثِيرها التَّشَاؤُمُ والكَابَةُ. | -
Row 8: ٨- استخدام الرمز الموحي. | لأَنَّهُ يُناسب الأجواء الغامضة التي يصعب تحديدها وإيضاحها.

=== BLOCK 4: Answers List (Teal) ===
(Component: TEMPLATE_C_BENEFIT.html)
Content:
ج١ - استِعْمَالُ اللَّغَةِ المَأْنُوسَةِ الْمَشْحُونَةِ بِطَاقات عاطِفَيَّةِ وَخَيَالِيَّةٍ رَقِيقَةٍ: (انطَلَقَتْ مِنْ أَسْرِهَا زَفَرَاتُ العاجز، حُلُمُ يَوْمِكَ فِي الميماس محتفل، في مشارقها حبّي وإِيمَانِي، ماسَتْ رَقْضَ نَشْوَانِ، كَسَوْهَا وَرَقَ الْأَشْوَاقِ فَازْدَهَرَتْ). التركيز في موضوعات يُثِيرها التَّشَاؤُمُ والكابة: تصوير المعاناة من استمرار الرحيل، والمعاناةِ مِنَ التَّمَزُّقِ الرُّوحِيِّ.
ج٢ - أسلوب القصر: (ليس يرويكَ إِلَّا نهلة). أثره في خدمة المعنى: وضح هذا الأسلوب المعنى وقوَّاهُ وَأَكَّدَهُ، فَقَدْ أَظْهَرَ الإعجابَ بِعُذُوبَةِ مَاءِ الوَطَنِ والتعلق بِهِ، وَعَدَمَ الْاِرْتِوَاءِ بِسِوَاهُ.

=== BLOCK 5: Answers List (Yellow) ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Content:
ج٣ - أَدَاةُ الشَّرْطِ: (كُلَّما). دَوْرُهَا فِي إِبْرَازِ مُعَانَاةِ الشَّاعِرِ: أَبْرَزَتْ مُعاناةَ الشَّاعِرِ المتكررة، ورَبَطَتها بأسبابها، فَكُلَّمَا لَاحَ أَمَامَهُ أَمْرٌ يُذَكِّرُهُ بِوَطَنِهِ، تَجَدَّدَتْ مُعَانَاتُهُ بِسَبَبِ البَعْدِ عَنْهُ.
ج٤ - دلالة الفعل المضارع (تسير) في تجلِيَةِ عَذَابِ الشَّاعِرِ وَتَمَزُّقِهِ الرُّوحِيِّ: دَلَّ على تَجَدُّدِ حَالِ نَفْسِهِ الأولى التي يعيش بها في غُرْبَتِهِ وتَبَدُّدِهَا، واستمرار معاناتها وتقلبِهَا بين المعاناة والأَلم. دلالة المصدرِ (رَهْن) في تجلِيَةِ عَذَابِ الشَّاعِرِ وَتَمَزُّقِهِ الرُّوحِيِّ: أوحى هذا الاستعمال بِتَعَلُّقِ الشَّاعِرِ الْمُطْلَقِ بِوَطَنِهِ، فهو لَا يَنْفَصِلُ عَنْهُ مهما باعَدَتْ بَيْنَهُمَا الْمَسافات، فَنَفْسُ الشَّاعِرِ مَسْكُونَةٌ بِالوَطَنِ، مُتَعَلِّقَةٌ بِهِ تَعَلقًا شديدًا بِأَعلى دَرَجَاتِ التَّعَلُّقِ، وَبِذَلِكَ تَجَلَّتْ شِدَّةُ مُعاناة الشاعر في بلاد الغربة، وتَمَزُّقُهُ الروحي بين الاغْتراب الذي يحياه، والحنين الذي يَشْدُّهُ الى الوَطَنِ الذي ابتعدَ عَنْهُ.

=== BLOCK 6: Answers List (Orange) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content:
ج٥ - الصورَةُ البَيَانِيَّة: (الأرياحُ تَجُرُّ فِي ذَيْلها). تحليل الصورة: شبه الشَّاعِرُ الأَرياح بكائنِ لَهُ ذَيْل، وحَذَفَ الْمُشَبَّهَ بِهِ، وَأَبْقَى شَيْئًا مِنْ لوازمه، وهو (تَجُرُّ، ذيلها). وظيفتا الصورة: الشرح والتوضيح، والإيحاء.
ج٦ - الطباق: (ماض، دانٍ). نَوْعُهُ: طباق إيجاب. أَثَرَهُ فِي المَعْنَى: ١- إظهارُ الْمَعْنَى بِجَلَاءٍ وَوُضُوح حيثُ أَوضَحَ الشَّاعِرُ مِنْ خلال هذا الطَّبَاقِ مُعاناتَهُ بِسَبَبِ تَشَتُّتِهِ وَتَمَزُّقِهِ الرُّوحِيِّ. ٢- إثارة الخيال: تمكن الشَّاعِرُ مِنْ خلال هذا الطباق مِنْ إِثارة خيالِ المتلقي وجَعْلِهِ يَتَخَيَّلُ حالة الضياع والتَشَتُّتِ التي يَحْيَاهَا الشَّاعِرُ مُوَزَّعًا بين ماضيه الذي عاشَهُ فِي وَطَنِهِ، وبين حاضره الذي يحياه في الغُرْبَة. ٣- إعمال العقل في المتناقضات: تَمَكَّنَ الشَّاعِرُ مِنْ خِلَالِ هذا الطَّبَاقِ مِنْ إِعْمَالِ عَقْلِ المُتَلَقِّي فِي المُتَنَاقِضَاتِ، فَجَعَلَهُ يُدْرِكُ الفَرْقَ الشَّاسِعَ بِينَ حالة الشاعر في الماضي الذي عاشَهُ فِي وَطَنِهِ، وحالته في الحاضر الذي يحياه في الغربة. ٤- تَحْدِيدُ الرُّؤْيَةِ (المَوْقِف): تمكن هذا الطَّبَاقُ مِنَ الكَشْفِ عَنْ مَوْقِفِ الشَّاعِرِ، حيثُ أَظْهَرَ أَنَّ الماضي الذي عاشَهُ فِي وَطَنِهِ مُفَضَّلٌ لَدِيهِ مُقَدَّمٌ عِندَهُ.
ج٧ - مِنْ عناصر الموسيقا الداخلية في المقطع الأخير: استعمال حُرُوفِ الهَمْسِ في البيت العاشر: (ص، ح، س، ت، ف، ك). واستعمال المدود في البيت الحَادِي عَشَر: (تدفقي، يَا، رياح هائجة، أهلي، إخواني).

=== BLOCK 7: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: مَثِّلْ لِكُلِّ خَصِيصَةٍ مِمَّا سَبَقَ بِمِثَالٍ مُنَاسِبٍ.
Number: ٢
Question: في البَيْتِ الرَّابِعِ أَسْلُوبُ قَصْرٍ. استَخْرِجْهُ، وَبَيِّنْ أَثَرَهُ فِي خِدْمَةِ الْمَعْنَى.
Number: ٣
Question: استَخْرِجْ مِنَ المَقْطَعِ الأَوَّلِ أَدَاةَ شَرْطٍ، وَبَيِّنْ دَوْرَهَا فِي إِبْرَازِ مُعَانَاةِ الشَّاعِرِ.
Number: ٤
Question: استَعْمَلَ الشَّاعِرُ فِي البَيْتِ السَّابع الفِعْلَ المَضَارِعَ لِلتَّعْبِيرِ عَنْ نَفْسِهِ الْأُولى، وَالمَصْدَرَ لِلتعبيرِ عَنْ نَفْسِهِ الْأُخْرَى. وَضِّحْ دِلَالَةَ كُلِّ مِنَ المُضَارِعِ وَالمَصْدَرِ فِي تَجْلِيَةِ عَذَابِ الشَّاعِرِ وَتَمَزُّقِهِ الرُّوحِيِّ.
Number: ٥
Question: استخرج مِنَ البيتِ الثاني صُورَةً بَيَانِيَّةً حَلِّلْهَا، ثُمَّ اذْكُرْ اثنتين مِنْ وظائفها.
Number: ٦
Question: استخرج مِنَ البيتِ السَّادِسِ طِبَاقًا، وَاذْكُرْ نَوْعَهُ، وَأَثَرَهُ فِي المَعْنَى.
Number: ٧
Question: مَثِّلْ لِثلاثَةِ مِنْ عَنَاصِرِ الموسيقا الدَّاخِلِيَّةِ فِي المقطع الأخير، وبين دور إيقاعاتها الخفية في الإيحاء بمناخ المعنى العام.

--- END STREAM ---
