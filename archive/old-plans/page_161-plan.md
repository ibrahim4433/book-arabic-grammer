# **SESSION 161**

[TASK DEFINITION]
Objective: Implement page 161.
File: `pages/page_161.html`
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
15. Strict Typographer Rule overrides mandatory Exam. No fabricated exams.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 161
[CHAPTER_TITLE]: page 161
[CATEGORY_HEADER]: 161
[SECTION_HEADER]: 161
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Verse 1 ===
(Component: TEMPLATE_C_POEM.html)
Title: البيت الأول
Content:
فيهِ رَبْعِي، فيهِ جَنَّاتٌ جَرَتْ *** تَحْتَهَا الأَنْهَارُ والرِّزْقُ جَمَدْ

=== BLOCK 3: Vocabulary and Idea 1 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح
Content:
المفردات: ربع الربع المؤضِعُ يُنْزَلُ فِيهِ زَمَنَ الرَّبِيع، وهو الدار والمنزل حمد : امْتَنَعَ الرّزْقُ وانقطع الشرح في شاطئ وطني منزلي الذي نَشَأْتُ فِيه،ِ وفيهِ بِقَاعٌ عَنَّاءُ خَضْرَاءُ جَمِيلَةٌ وَارِفَةُ الظلال، فَقَد حَبَاهُ الله آيَاتٍ مِنَ الْجُمَالِ وَزَانَهُ بأنهارٍ رَقْرَاقَةٍ عَذَبَة،ٍ ومع كل هذا الخير العميم قد ضاق العيش فيه، وامتنع تحصيل الرزق وصَعُبَ الفكرة: انقِطَاعُ الرِّزْقِ في الوَطَنِ رِعْمَ وَفْرَةِ خَيْرَاتِه.ِ

=== BLOCK 4: Grammar Analysis 1 ===
(Component: TEMPLATE_C_IRAB.html)
Title: الإعراب
Content:
فيه في حرف جر. والهاء، ضميرٌ مُتَصِلٌ مَبْنِي على الكَسْرَةِ فِي مَحَلَ جَرَ بِحَرْفِ الجَر.ِ متعلقان بخبَرِ مُقَدَّم مخذُوفٍ
رَبَّعِي: مُبْتَدَةٌ مُؤَخَّرٌ مَرْفُو، وعلامَةُ رَفْعِهِ الضَّمَّةُ الْمُقَدَّرَةُ على ما قَبْلَ يَاءِ الْمُتَكَلِّم،ِ مَنَعَ ظُهُورَها اشتغالُ الْمَحَقِّ بالحركة المناسبة. والياء، ضميرٌ مُتَّصِلِّ مَبْنِي على السكون في محل جر، مُضَاف إليه.
فيهِ فِي حَرْفُ جة.ٍ والهاء، ضميرٌ مُتَصِلِّ مَبْنِي على الكَسْرَةٍ فِي مَحَلِّ جَةٍ بِحَرْفِ الجَرِ مُتَعَلَّقَان بِخَبَرِ مُقَدَّم مَحْذُوفِ
جَنَّاتٌ : مُبْتَدَاً مُؤَخَرُ مَرْفُوعٌ
جَرَتْ : فعل ماض مَبْنِي على الفَتْحَةِ المُقَدَّرَةِ على الأَلِفِ المَحْدُوفَةِ؛ لا تَصَالِهِ بِتَاءِ التَّانيثِ السَّاكِنَةِ وَالنَّاء،ُ حَرْفُ تَأْنِيثِ لَا مَحَلَّ لَهُ مِنَ الإعراب
تَحْتَهَا مَفْعُولُ فِيهِ ظَرْفُ مَكَانٍ مَنْصُوب، وعلامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَة.ُ وها، ضميرٌ مُتَّصِلِّ مَبْنِي على السكونِ فِي حَلِ جر، مُضَاف إليه
الأنهار : فَاعِلَ مَرْفُوعٌ
والرزق : الواو، واو الحال الرزق، مُبْتَدَاً مَرْفُوع
جم : فعل ماضِ مَبْنِي على الفتحة الظاهرة. وسكن للضرورة الشعرية.
جملة )فيهِ رَبْعِي( : صِفَة،ٌ فَحَلُّهَا الرَّفْعُ
جملة )فيهِ جَنَّاتٌ(: صِفَة،ٌ مَحَلَّهَا الرَّفْع.
جملة )جَرَتْ تَحْتَهَا الْأَنْهَارُ(: صفة، محلها الرفع
جمله )الرِّزْقُ جَم :( حالِيَّة،ٌ مَحَلُّهَا النَّصْبُ
جملة )جَمَد( : خَبَرَيَّة،ٌ مَحَلُّهَا الرَّفْع.ُ

=== BLOCK 5: Verse 2 ===
(Component: TEMPLATE_C_POEM.html)
Title: البيت الثاني
Content:
فيهِ مُرُ العَيْش يخلو *** وأرى في سواهُ زُبْدَةَ العَيْ زَبَدْ

=== BLOCK 6: Summary Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Title: ملخص المفردات والأفكار
Content:
| المفهوم | الشرح |
| --- | --- |
| المفردات (البيت الثاني) | زبدة خلاصة زيد: رغوة |
| الشرح | في شاطئ وطني تَسْتَحِيلُ مَرَارَةُ العيش عذوبة، وَيَعْدُو كَدَرُهُ صَفْوا، وفي أي بقعة سواه يظل رغدُ العيش مُنَضًا عَكِرًا؛ فلا تلد الحياة بعيدا عنهُ لأَنَّ معالِمَهَا مصبوغة بجراح الغربة |
| الفكرة | استعذاب ضَنْكِ العَيْشِ وضِيْقِهِ فِي الوَطَن،ِ وتَفْضِيْلِهِ على العَيْشِ الرَّغِيد في الغُرْبَة |

=== BLOCK 7: Grammar Analysis 2 ===
(Component: TEMPLATE_C_IRAB.html)
Title: الإعراب
Content:
فيه في حرف جر. والهاء، ضميرٌ مُتَّصِلِّ مَبْنِي على الكُسْرَةِ فِي مَحَلَ جَرٍ بِحَرْفِ الجَرِ مُتَعَلَقَان بالفعل )يَحْلُو(.
مُر: مُبْتَدِةٌ مَرْفُوعُ
العَيْش:ِ مُضَافُ إِلَيْهِ تَجْرُورٌ
يَحْلُو : فِعْلَ مُصَارِعٌ مَرْفُوع، وعلامَةُ رَفْعِهِ الصَّمَّةُ الْمُقَدَّرَةُ على الواو، مَنَعَ ظُهُورَها التقل.
وأرى الواو، حَرْفُ عَطْفٍ أَرَى فِعْلَ مُضَارِعٌ مَرْفُوع، وعلامَةُ رَفْعِهِ الضَّمَّةُ المُقَدَّرَةُ على الأَلِفِ مَنَعَ ظُهُورَهَا التَّعَذِّرُ
زُبْدَةَ : مَفْعُولٌ بِهِ أَوَّلَ مَنْصُوبُ
زَبَدْ : مَفْعُولُ بِهِ تَانٍ مَنْصُوب،ٌ وعلامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَة.ُ وسُكِّنَ لِلضَّرُورَةِ الشَّعْرِيَّةِ
جملة )فيهِ مُرُ العَيْشِ يَخْلُو(: صِفَة،ٌ مَحَلَّها الرفع
جملة )يعلُو( : خَبَرَيَّة،ٌ مَحَلها الرَّفْعُ
جملة )أرى :(... مَعْطُوفَة،ٌ مَحَلُّهَا الرَّفْع.ُ

=== BLOCK 8: Verse 3 ===
(Component: TEMPLATE_C_POEM.html)
Title: البيت الثالث
Content:
وطني، ما زِلْتُ أَدْعُوكَ أَبِي *** وَجِرَاحُ اليُنْمِ فِي قَلْبِ الوَلَدْ

=== BLOCK 9: Explanation 3 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الشرح
Content:
الشرح وطني الحبيب مازِلْتُ الْجُ بِاسْمِكَ وَأَنَادِيك: "أبي"، وسأبقى على الدوام أَنْتَسِبُ إِليَك،َ وَأَرَى فِيكَ صُورَةَ أَبِي، فَبَعْدَ فَقْدِكَ عَانَيْتُ ما عَانَاهُ الْيَتِيمُ مِنْ مَرَارَةِ اليُنْم،ِ حَيْثُ انْغَرَزَتْ فِي قَلْبِي آلامُ اليُتم وعَذَابَاتُهُ الْفِكْرة: تصوير قُوَّة الانتماء إلى الوطن البلاغة: )أَدْعُوكَ أَبِي(: تشبيه بليغ المشبه الوطن أو : الضَّمير الكاف والمشبه به : أبي جراح اليتم( تشبيه بليغ المشبه اليتم. والمشبه به جراح.

=== BLOCK 10: Grammar Analysis 3 ===
(Component: TEMPLATE_C_IRAB.html)
Title: الإعراب
Content:
مازِلْت:ُ فعل ماض ناقص مَبْنِي على السُّكُون لاتِصَالِهِ بِتَاءِ الرَّفْعِ المتحركة. والنَّاء،ُ ضميرٌ مُتَّصِلِّ مَبْنِي على الضَّمَّةِ فِي مَحَلِّ رَفْع،ِ اسْمُهَا
أَدْعُوكَ فِعْلَ مُضَارِعٌ مَرْفُوع،ٌ وعلامَةُ رَفْعِهِ الضَّمَّةُ المُقَدَّرَةُ على الواو، مَنَعَ ظُهُورَهَا النَّقَلُ والكاف، ضميرٌ مُتَّصِلِّ مَبْنِي على الفَتْحَةِ في محَلَ نَصْب،ِ مَفْعُولٌ بِهِ أَوَّلَ
أَبِي مَفْعُولُ بِهِ تَانٍ مَنْصُوب، وعلامَةُ نَصْبِهِ الفَتْحَةُ المُقَدَّرَةُ على ما قَبْلَ ياءِ الْمُتَكَلِم،ِ مَعَ ظُهُورَهَا اسْتِغَالُ الْمَحَلَّ بالحركة المناسبة والياء، ضمير مُتَّصِلِّ مَبْنِي على السكون في محل جر، مُضَاف إليه.
وَجِرَاحُ الواو، واو الخال. جراح، مُبْتَدَةٌ مَرْفُو
اليُثم: مُضَافُ إليهِ مَجْرُورُ
الوَلَدْ : مُضَاف إليهِ مَجْرُور، وعلامَةُ جَرَهِ الكَسْرَةُ الظَّاهِرَة،ُ وَسُ نَ لِلضَّرُورَةِ الشَّعْرِيَّةِ
جملة )ما زِلْتُ أَدْعُوكَ(: استئنافية، لا محل لها من الإعراب
جملة )أَدْعُوكَ( : خَبَرَيَّة،ٌ حَلُّهَا النَّصْب.
جملة )جِرَاحُ الْيُنمِ فِي قَلْبِ الوَلَدُ( : حاليَّة،ٌ مَحَلُّهَا النَّصْب.ُ

=== BLOCK 11: Verse 4 ===
(Component: TEMPLATE_C_POEM.html)
Title: البيت الرابع
Content:
ما رَضِيتُ البَيْنَ لولا شِدَّةُ *** وَجَدَثْنِي سَاعَةَ البَيْنِ أَشَدْ

=== BLOCK 12: Vocabulary and Explanation 4 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح والبلاغة
Content:
المفردات: البين الفراق والبُعْدُ شِدَّةٌ : الشدة : الأَمْرُ يَصْعُبُ تَحَمُلُهُ وَشِدَّةُ العَيْش:ِ شَ فَهُ وَضِيقُه،ُ وَأَرَادَ هُنَا ضِيْقَ العَيْش.ِ الشرح : لم أكُنْ لأَرْتَضِي البُعْدَ عَنْكَ وَالأَنْفِصَالَ عَنْ تَرَاكَ الطَّاهر لولا شَظَفُ العَيْشِ وضِيقُه،ُ اللَّذِينِ تَفَاقَمَا لحظةَ الْفِرَاق،ِ فَتَعَاظَمَتْ مُعَانَاتِي وَبَلَغَتْ عَذَابَاتِي درْوَتَها الفكرة : هَجْرِ الوَطَنِ بِسَبْبٍ شَظَفِ العَيْشِ وَضِيْقِهِ التَّعْبِيرُ عَنِ الغَرْيَةِ القَسْرِيَّة.ِ الشُّعُور: الشوق والحنين الأداة: التراكيب المثال: ما رَضِيتُ البَيْنَ لولا شِدَّة.ٌ البلاغة: )شِدَّة،ٌ أَشَد( جناس ناقص )جناس اشتقاقي(. )شِدَّةً وَجَدَتْنِي( : استعارةٌ مَكْنِيَّة.ُ

=== BLOCK 13: Benefit Warning ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: الأساليب
Content:
)لولا شِدَّةٌ( : حذف خَبَرُ المبتدأ الواقع بعد لولا وجوبا.

=== BLOCK 14: Cut Content 1 ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
Title: الإعراب
Content:
الإعراب : ما رَضِيتُ : ما، حَرْفُ نَفْيِ رَضِيْت،ُ فعل ماضِ مَبْنِي على السُّكُونِ؛ لَاتِصَالِهِ بِتَاءِ الرفع المتحركة. والنَّاء،ُ ضميرٌ مُتَصِلَ مَبْنِي عَلَى الصَّمَّةِ فِي مَحَلِ رَفْعٍ فَاعِلَ البَيْنَ : مَفْعُولُ بِهِ مَنْصُوب. لولا: حَرْفُ شَرْطِ غَيْرُ جازم. شِدَّة:ٌ مُبْتَدَاً مرفوع والخبر محذوف وجوبًا تقديرُهُ مَوْجُودَةٌ(. وَجَدَثَنِي : فِعْلَ مَاضِ مَبْنِي على الفَتْحَةِ؛ لاتِصَالِهِ بِنَاءِ الثَّانيثِ السَّاكَنَة.ِ والنَّاء،ُ حَرْفُ تَأْني لا مَحَالَ لَهُ مِنَ الإعراب والتون، حرف وفاية. والياء، ضمير مُتَّصِلِّ مَبْنِي عَلَى السُّكُونِ فِي مَحَلِّ نَصْب،ِ مَفْعُولٌ بِهِ أَوْلَ سَاعَة:َ مَفْعُولُ فِيهِ ظَرْفُ

--- END STREAM ---
