# **SESSION 181**

[TASK DEFINITION]
Objective: Implement page 181.
File: `pages/page_181.html`
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
[LESSON_NUMBER]: 181
[CHAPTER_TITLE]: page 181
[CATEGORY_HEADER]: 181
[SECTION_HEADER]: 181
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Cut Content (Part 2) ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[BLOCK_TITLE]: البلاغة والإعراب
(Component: TEMPLATE_C_BLOCK.html)
Title: البلاغة والإعراب
Content: <p class="text-accent">البلاغة: (حُزْنُ النَّفْسِ <span class="highlight-red">ظِلَّ</span> وَهُم) تشبيه بليغ (ظِلَّ وَهُم) تشبيه بليغ إضافي.</p>

=== BLOCK 3: الإعراب - حزن ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: حزن
[IRAB_ANALYSIS]: اسم (لَيْسَ) مَرْفُوع. النَّفْسِ: مُضَاف إليهِ مَجْرُورٌ. إلَّا: أداة حَصْرٍ. ظِلَّ: خَبَرُ (لَيْسَ) مَنْصُوبٌ. وَهُم: مُضَافُ إِلَيْهِ مَجْرُورٌ.

=== BLOCK 4: الإعراب - الجمل ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: جملة (لا يَدُومْ)
[IRAB_ANALYSIS]: حُزْنُ النَّفْسِ إِلَّا ظِلَّ يَدُوم: لا: حَرْفُ نَفْي. يَدُومْ: فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وعلامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ، وسُكِّنَ لِلضَّرُورَةِ الشِّعْرِيَّةِ. جملةٌ لَيْسَ النَّكِرَةَ (ظِلَّ) قَدِ وَهُم: استئنافية، لا محل لها من الإعراب. جملة (لا يَدُوم): صِفَةٌ، مَحَلَّها الجر. (ومِنَ الْمَقْبُولِ أَنْ تُعْرَبَ فِي محل نَصْبِ حال؛ لأَنَّ النكرة اختصَّتْ بالإضافة).

=== BLOCK 5: قصيدة وَغُيُومُ النَّفُسِ ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: وَغُيُومُ النَّفُسِ
[POET_NAME]: أ.الياس خفيف
[RIGHT_HEMISTICH_1]: وَغُيُومُ النَّفُسِ تَبْدُو مِنْ ثَنَايَاهَا النُّجُومُ
[LEFT_HEMISTICH_1]: مَبْثُوثَةٌ مُتَنَاثِرَةً بَيْنَ أَجواء الغابِ

=== BLOCK 6: الشرح والفكرة ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الشرح والفكرة
Content: <p class="text-accent">الشرح: يَتَعَانَقُ الحُزْنُ والفَرَحُ، فالنُّجُومُ الْمُتَلَالِئَةُ، وهيَ رَمْزُ الْفَرَحِ والتَّفَاؤُلِ لَدَى الإِنْسَانِ، تَرَاهَا مِنْ ثَنَايَا غُيُومِ نَفْسِهِ وثنايا آلامِهِ، فَتَغْدُو النُّجُومُ والغُيُومُ كُلًّا مُوَحَّدًا يَجْمَعُهُ التَّوَافُقُ، لا التَّنَاقُضُ. وبذَلِكَ يُطْرَدُ تَشَاؤُمُ النَّفْسِ، وتُبْعَدُ سَوْدَاوِيَّتُهَا. الفكرة: الغَابُ عالم المَسَرَّاتِ وَالفَرَحِ وَالأَمَلِ (الدَّعْوَةُ للعيش في عالم الغابِ هَرَبًا مِنْ عَالَمِ المَدِينَةِ المَادِيِّ).</p>

=== BLOCK 7: تنبيه الفكرة ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[BENEFIT_TITLE]: الفكرة
[BENEFIT_CONTENT]: خُلُوُّ الْغَابِ مِنَ الهم والحزن.

=== BLOCK 8: الإعراب - وغيوم النفس ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: وَغُيُومُ النَّفْسِ تَبْدُو
[IRAB_ANALYSIS]: الإعراب: وَغُيُومُ: الواو، حَرْفُ اسْتِثْنَافٍ. غُيُومُ: مُبْتَدَأٌ مَرْفُوعٌ. النَّفْسِ: مُضَافٌ إِلَيهِ مَجْرُورٌ. تَبْدُو: فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وعلامَةُ رَفْعِهِ الضَّمَّةُ المقدرة على الواو، مَنَعَ ظُهُورَهَا الثِّقَلُ. مِنْ: حَرْفُ جر. ثَنَايَاهَا: اسم مجرُور، وعلامَةُ جَرِّهِ الكَسْرَةُ المُقَدَّرَةُ على الأَلِفِ، مَنَعَ ظُهُورَها التعذر. وها، ضمير متصل مبني على السُّكُونِ فِي مَحَلِّ جَرٍّ، مُضَاف إليه. النُّجُومُ: فَاعِلٌ مَرْفُوع، وعلامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ وَسُكِّنَ لِلضَّرَوَرَةِ الشعرية.

=== BLOCK 9: الإعراب - جمل وغيوم ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: جمل
[IRAB_ANALYSIS]: جملة (غُيُومُ النَّفْسِ تَبْدُو مِنْ ثَنَايَاهَا النُّجُومُ): استئنافية، لا محل لها من الإعراب. جملة (تَبْدُو مِنْ ثَنَايَاهَا النُّجُوم): خَبَرِيَّةٌ، مَحَلَّهَا الرَّفْعُ.

=== BLOCK 10: قصيدة أغطني الناي ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: أغطني النَّايَ
[POET_NAME]: أ.الياس خفيف
[RIGHT_HEMISTICH_1]: أغطني النَّايَ وَغَنِّ فَالِغِنَا يَمْحُو المِحَنْ
[LEFT_HEMISTICH_1]:

=== BLOCK 11: المفردات والشرح والفكرة والبلاغة ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح
Content: <p class="text-accent">المفردات: المحن: المفرد: محنة، وهي البلاء والشدة. الشرح: أَقْبل على الفَنِّ لأَنَّهُ الطريق الوحيدة التي تُخَلِّصُكَ مِنْ بَرَاثِنِ وَاقِعِكَ، وتُدْنِيكَ مِنْ عَالَمِ الغَابِ المِثَالِيِّ الفَاضِلِ، فَأَمَامَ تَرَاتِيلِ الْغِنَاءِ وَأَنْغَامِ الْمُوسِيقَى تَزُولُ المِحَنُ، وَتَتَذَلَّلُ الصعاب وتَتَصَاغَرُ. الفكرة: تَأْكِيدُ دَوْرِ الفَنِّ فِي الْحَيَاةِ الإِنْسَانِيَّةِ. البلاغة: (الغنا تمحو): استعارة مَكْنِيَّةٌ.</p>

=== BLOCK 12: الإعراب - أعطني ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: أَعْطِنِي
[IRAB_ANALYSIS]: الإعراب: أَعْطِنِي: فِعْلُ أَمْرٍ مَبْنِي على حَذْفِ حَرْفِ العِلَّةِ، والنون، حرف للوقاية. والياء، ضمير مُتَّصِلٌ مَبْنِي على السُّكُونِ فِي مَحَلِّ نَصْبٍ، مَفْعُولُ بِهِ أَوَّلِ. أَمْرٍ مَبْنِي على حَذْفِ حَرْفِ العِلَّةِ. النَّايَ: مَفْعُولُ بِهِ ثانٍ مَنْصُوبٌ، وعلامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَةُ. وَغَنِّ: الواو، حَرْفُ عَطْفٍ. غَنِّ: فِعْلُ.

=== BLOCK 13: الإعراب - فالغنا ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: فَالِغِنَا
[IRAB_ANALYSIS]: فَالِغِنَا: الفَاءُ، حَرْفُ استِئْنَافٍ. الغنا: مُبْتَدَأٌ مَرْفُوعٌ، وعلامَةُ رَفْعِهِ الضَّمَّةُ المُقَدَّرَةُ على الأَلِفِ، مَنَعَ ظُهُورَهَا التَّعَذُّرُ (عُومِلَ الْمَمْدُودُ مُعَامَلَةِ الْمَقْصُورِ لِلضَّرَوَرَةِ الشِّعْرِيَّةِ). يَمْحُو: فِعْلٌ مُضَارع مَرْفُوع، وعلامَةُ رَفْعِهِ الضَّمَّةُ الْمُقَدَّرَةُ على الواو، مَنَعَ ظُهُورَهَا الثِّقَلُ. الْمِحَنْ: مَفْعُولٌ بِهِ مَنْصُوب، وعلامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَةُ، وَسُكِّنَ لِلضَّرَوَرَةِ الشِّعْرِيَّةِ. جملة (أَعْطِنِي): استئنافية، لا محل لها مِنَ الإعراب. جملة (غَنِّ): مَعْطُوفَةٌ، لَا مَحَلَّ لَهَا مِنَ الإعراب. جملة (الغِنَا يَمْحُو): استئنافية، لا محل لها من الإعراب. جملة (تمحو): خَبَرِيَّةٌ، مَحَلَّهَا الرَّفْعُ.

=== BLOCK 14: قصيدة وأنين الناي ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: وأنينُ النَّاي
[POET_NAME]: أ.الياس خفيف
[RIGHT_HEMISTICH_1]: وأنينُ النَّاي يَبْقَى بَعْدَ أَنْ يَفْنَى الزَّمَنْ
[LEFT_HEMISTICH_1]:

=== BLOCK 15: المفردات والشرح والفكرة ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح
Content: <p class="text-accent">المفردات: الأنين التأوه. الشرح: تَأَكُّدُ أَنَّ الفَنَّ هو الأَكْثَرُ قُدْرَةً عَلَى البَقَاءِ والاستمرار. فهو البَاقِي بَعْدَ أَنْ يَفْنَى الزَّمَنُ نَفْسُهُ. الفكرة: تأكيد خلود الفن.</p>

=== BLOCK 16: الإعراب - وأنين الناي ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: وأَنينُ النَّايِ
[IRAB_ANALYSIS]: الإعراب: وأَنينُ: الواو، حرف استِثْنَافٍ. أَنِينُ: مُبْتَدَأٌ مَرْفُوعٌ. النَّايِ: مُضَافُ إِلَيْهِ مَجْرُورٌ، وعلامَةُ جَرِّهِ الكَسْرَةُ الظَّاهِرَةُ. يَبْقَى: فِعْلٌ مُضَارِعٌ مَرْفُوع، وعلامَةُ رَفْعِهِ الضَّمَّةُ المُقَدَّرَةُ على الأَلِفِ مَنَعَ ظُهُورَهَا التَّعَذَّرُ. بَعْدَ: مَفْعُولٌ فِيهِ ظَرْفُ زَمَانٍ مَنْصُوبٌ. أَنْ: حَرْفٌ ناصِبٌ. يَفْنَى: فِعْلٌ مُضَارِعٌ مَنْصُوب، وعلامَةُ نَصْبِهِ الفَتْحَةُ المُقَدَّرَةُ على الأَلِفِ، مَنَعَ ظُهُورَهَا التَّعَذَّرُ. والمَصْدَرُ المُؤَوَّلُ (أَنْ يَفْنَى) فِي مَحَلِّ جَرٍّ، مُضَاف إِلَيْهِ. الزَّمَنْ: فَاعِلٌ مَرْفُوع، وعلامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ، وَسُكِّنَ لِلضرورة الشِّعْرِيَّةِ. جملة (أنينُ النَّاي يبقى): استئنافية، لا محل لها من الإعراب. جملة (يبقى): خَبَرِيَّةٌ، محلها الرَّفْعُ. جملة (يَفْنَى الزَّمَنَ): صِلَةُ المَوْصُولِ الحَرْفِيِّ، لا محل لها مِنَ الإعراب.

=== BLOCK 17: قصيدة هل تخذت الغاب ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: هل تخذت الغاب
[POET_NAME]: أ.الياس خفيف
[RIGHT_HEMISTICH_1]: هَلْ تَخِذْتَ الغَابَ مِثْلِي مَنْزِلًا دُونَ القُصُور؟
[LEFT_HEMISTICH_1]:

=== BLOCK 18: المفردات والشرح والفكرة والبلاغة ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح
Content: <p class="text-accent">المفردات: تخذ: تخذ الشَّيْءَ حَازَهُ وَحَصَلَهُ. المصدر: تَخَذ. الشرح: أيُّهَا الْإِنْسَانُ اتْرُكْ مَادِّيَّاتِ الْوَاقِعِ وَانْفُرْ مِنْ مَبَاهِجِهِ الزَّائِلَةِ، وَاجْعَلِ الغَابَ هَدَفَكَ الأَسْمَى، واتَّخِذْهُ، مِثْلِي، مَنْزِلًا تَأْوِي إِلَيْهِ، وَاتْرُكْ حَيَاةَ التَّرَفِ فِي القُصُور. الفكرة: استنكارُ المُجْتَمَعِ المَادِيِّ فِي الْمَهْجَرِ (الدَّعْوَةُ للعيش في عالم الغابِ هَرَبًا مِنْ عَالَمِ المَدِينَةِ المادي). البلاغة: (الغاب منزل): تشبيه بليغ.</p>

=== BLOCK 19: الإعراب - هل تخذت ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: هَلْ تَخِذْتَ
[IRAB_ANALYSIS]: الإعراب: هَلْ: حَرْفُ اسْتِفْهَام. تَخِذْتَ: فعل ماض، مَبْنِي على السُّكُونِ؛ لَاتِّصَالِهِ بِتَاءِ الرَّفْعِ الْمُتَحَرِّكَةِ. والتَّاءُ، ضمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الفَتْحَةِ فِي مَحَلِّ رَفْعٍ، فاعل. الغاب: مَفْعُولُ بِهِ أَوَّلٌ مَنْصُوبٌ. مِثْلِي: نَائِبُ مَفْعُولٍ مُطْلَقٍ مَنْصُوبٌ، وعلامَةُ نَصْبِهِ الفَتْحَةُ المُقَدَّرَةُ عَلَى مَا قَبْلِ يَاءِ الْمُتَكَلِّمِ، مَنَعَ ظهورها اشتغالُ الْمَحَلِّ بِالحَرَكَةِ المُنَاسِبَةِ، والياء، ضميرٌ مُتَّصِلٌ مَبْنِي على السكون فِي مَحَلِّ جَرٍّ، مُضَافُ إِلَيْهِ. التَّقْدِيرُ: هَلْ تَخِذْتَ الغَابَ مِثْلَ تخذي.

=== BLOCK 20: الإعراب - منزلا ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: مَنْزِلًا
[IRAB_ANALYSIS]: مَنْزِلًا: مَفْعُولُ بِهِ ثَانٍ مَنْصُوبٌ. دُونَ: مَفْعُولٌ فِيهِ ظَرْفُ مَكَانٍ مَنْصُوبٌ. الْقُصُورُ: مُضَافٌ إِلَيْهِ مَجْرُورٌ، وعلامَةُ جَرِّهِ الكَسْرَةُ الظَّاهِرَةُ. وسُكِّنَ لِلضَّرُورَةِ الشِّعْرِيَّةِ. جملة (تَخِذْتَ): استئنافية، لا محل لها مِنَ الإعراب.

=== BLOCK 21: The Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: الكلمة
[HEADER_2]: المعنى / الفكرة
[HEADER_3]: البلاغة / الإعراب
[CELL_1]: الغاب
[CELL_2]: عالم المسرّات والهرب من المدينة
[CELL_3]: الغاب منزل: تشبيه بليغ
[CELL_4]: الغنا
[CELL_5]: تمحو المحن
[CELL_6]: الغنا تمحو: استعارة مكنية
[CELL_7]: أنين الناي
[CELL_8]: تأكيد خلود الفن
[CELL_9]: يبقى بعد أن يفنى الزمن
[CELL_10]: حزن النفس
[CELL_11]: ظل وهم
[CELL_12]: تشبيه بليغ

--- END STREAM ---
