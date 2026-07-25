# **SESSION 191**

[TASK DEFINITION]
Objective: Implement page 191.
File: `pages/page_191.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`.
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md` to identify the correct template to use for the continuation. You are forbidden from guessing.
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
8. **Self-Correction:** Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files. If it fails, you MUST fix the errors.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...) .
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
15. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 191
[CHAPTER_TITLE]: page 191
[CATEGORY_HEADER]: 191
[SECTION_HEADER]: 191
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Cut Continuation ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[WRAPPED_COMPONENT]: TEMPLATE_C_IRAB.html
Title: الإعراب
Content:
مَرْفُوع، وعلامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ والهاء، ضَمِيرٌ مُتَّصِلِّ مَبْنِي على الضَّمَّةِ فِي مَحَلِّ جَرّ،ٍ مُضاف إليه.
ويشوكه: الواو، حَرْفُ عَطْفٍ. يَشُوكُه،ُ فِعْلٌ مُضَارِعٌ مَرْفُوع، وعلامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ والهاء، ضَمِيرٌ مُتَّصِلٌ مَبْنِي على الضَّمَّةِ فِي مَحَلِّ نَصْب،ِ مَفْعُولٌ بِهِ. الْحِرْمَان:ُ فَاعِلٌ مَرْفُوعٌ.
والنَّصَبُ : الواو، حَرْفُ عَطْفُ. النَّصب، اسمٌ مَعْطُوفٌ مَرْفُوعٌ.
جملة (يَنْبُو بِهِ فِي اللَّيْلِ مَضْجَعُهُ) : استئنافية، لا محل لها مِنَ الإعراب.
جملة (يَشُوكُهُ الحَرْمَانُ) : مَعْطُوفَة،ٌ لا مَحَلَ لها مِنَ الإعراب.

=== BLOCK 3: Poem 1 ===
(Component: TEMPLATE_C_POEM.html)
Right Hemistich: يسعى ولكن لا إلى أمل
Left Hemistich: وَيَدِبُّ لَكِنْ حَيْثُ لَا أَرَبُ

=== BLOCK 4: Analysis Matrix 1 ===
(Component: TEMPLATE_C_TABLE.html)
Title: تحليل البيت
Content:
المفردات | أرب: الحاجة والبغية والأمنية.
الشرح | إِنَّ هذا البَنَّاءَ الكَادِحَ يَسْعَى بِدَابِ لَا يَفْتُر،ُ وعزمٍ لَا يَلِينُ لَكِنَّهُ لَا يَبْلُعُ أَمَلَا مِنْ آمالِه،ِ فَكُلما جَدَّ السَّيْرَ فِي مَسْلَكِ لَم يَجِدُ فِيهِ بُغْيَة،َ وَلَمْ يُحَقِّقَ فِيهِ مُنْيَةَ.
الفكرة | حَظُ البَنَّاءِ العائِرِ وَخَيْبَةُ سَعْيه.

=== BLOCK 5: Irab 1 ===
(Component: TEMPLATE_C_IRAB.html)
Title: الإعراب
Content:
يسعى: فعل مُضَارَعٌ مَرْفُوعٌ.
وَلَكِنْ : الواو، حَرْفُ استنافِ. لَكِنْ حَرْفُ استدراك.
لا : حَرْفُ نَفْي.
إلى أَمَل: إِلَى حَرْفُ جَرٍ أَمَل،ِ اسم مجزور والجَارُ وَالمَجْرُورُ مُتَعَلِّقَانِ بالفعل يسعي المخذُوف (دَلَّ عَلَيْهِ يَسْعى المذكور).
وَيَدِبُّ: الواو، حَرْفُ عَطف.
لكِنْ: حَرْفُ استدراك.
حَيْثُ : اسم مَبْنِي على الضَّمَّةِ فِي مَحَلِّ نَصْبِ مَفْعُولُ فيه ظرف مكان. مُتَعَلِّقَ بِالفِعْلِ يَدِبُّ الْمَحْذُوف (دَلَّ عَلَيْهِ يَدِبُّ المذكور).
لا أرب: لا، حَرْفُ نَفى. أَرَب،ُ مبتداً مرفوع.
جملة (يسعى): استئنافية، لا محل لها مِنَ الإعراب.
جملة (يَدِبُّ) : مَعْطُوفَة،ٌ لا محل لها مِنَ الإعراب.

=== BLOCK 6: Poem 2 ===
(Component: TEMPLATE_C_POEM.html)
Right Hemistich: دامي الفُوَادِ يَمُضُهُ أَلَمُ
Left Hemistich: ذاوي الجفون يَعَضُهُ سَغَبُ

=== BLOCK 7: Analysis Matrix 2 ===
(Component: TEMPLATE_C_TABLE.html)
Title: تحليل البيت
Content:
المفردات | يمضه : يُؤْلِمُه ويُوجِعُه. سغب : جوع.
الشرح | يبدو البنَّاءُ مُنْكَسِرَ النَّفْس،ِ يعتصره الحزن والألم، ذابل الأَجْفَانِ مِن شِدَّةِ فَتَكِ الجوع به.
الفكرة | أَثَرُ كُلِّ مِنَ الْأَلَم والجوع في البناء.

=== BLOCK 8: Irab 2 ===
(Component: TEMPLATE_C_IRAB.html)
Title: الإعراب
Content:
دامي: خبر مرفوع، وعلامةُ رَفْعِهِ الضَّمَّةُ المقدرة على الياءِ مَنَعَ ظهورَهَا التَقَل.
الفواد : مُضَاف إليه مجرور.
يمضه: فعل مضارع مرفوع والهاء، ضمير متصل في محل نصب، مفعول به. آلم: فاعل مرفوع.
ذاوي: خبر مرفوع، وعلامةُ رَفْعِهِ الضَّمَّةُ المُقَدرة على الياءِ مَنَعَ ظهورها التَّقَلُ.
الجفون: مُضَاف إليه مجرورٌ.
يَعَضُهُ: فعل مُضَارع مرفوع. والهاء، ضميرٌ مُتَّصِلِّ مَبْنِي على الضم في محل نصب، مفعول به.
سغب: فاعل مرفوع.
جملة (يُمِضُهُ أَلم): في محل نصب، حال.
جملة (يَعَضُهُ سَغَبُ): في محل نَصْب،ِ حال.

=== BLOCK 9: Poem 3 ===
(Component: TEMPLATE_C_POEM.html)
Right Hemistich: بالروح في كانون نظرته
Left Hemistich: يَصْطَكُ مِنْ قُرِّ وَيَصْطَرِبُ

=== BLOCK 10: Analysis Matrix 3 ===
(Component: TEMPLATE_C_TABLE.html)
Title: تحليل البيت
Content:
المفردات | قر : برد.
الشرح | في فصل الشتاء، فيبدو البَنَّاءُ مُرْتَجِفًا، يُقَاسِي البرد القارس، فمن شِدَّةِ البَادِ اغروزَقَتْ عَيْنَاهُ بِالدموع.
الفكرة | تصوير مظاهر الشَّقَاءِ فِي السَّعْي لِكَسْبِ الرِّزْقِ (تَصْوِيْرُ مَلامِحٍ مُعاناةِ البَنَّاءِ فِي فصل الشتاء).

=== BLOCK 11: Irab 3 (Orange Benefit Warning for layout balance) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: إعراب البيت
Content:
في كانون: في، حرف جر. كانون اسم مجرور، وعلامة جره الفتحة نيابة عَنِ الكسرة؛ لأنه اسم ممنوع من الصرف.
نظرته : مبتداً مرفوع، وعلامةُ رَفْعِهِ الضَّمَةً الظاهرة، والهاء، ضمير متصل في محل جر، مُضَاف إليه.
جملة (يصطك): في محلِّ نَصْب، حال.
جملة (يضطرب): معطوفة، في محل نصب.

=== BLOCK 12: Poem 4 ===
(Component: TEMPLATE_C_POEM.html)
Right Hemistich: جمدت على المنقار راحته
Left Hemistich: فكانها من بَعْضِهِ خَشَبُ

=== BLOCK 13: Analysis Matrix 4 ===
(Component: TEMPLATE_C_TABLE.html)
Title: تحليل البيت
Content:
المفردات | المنقار : آلة كالفاس لها خلف تُقْطَعْ بِهِ الحِجَارَة.
الشرح | التصَقَتْ يَدُ البناء بِمِقْبَضِ قَدُومِهِ الَّتِي يَنْحَتُ بها الحجارة ويقطعها.
الفكرة | تصوير مظاهر الشقاء في السعي لِكُسْبِ الرِّزْقِ (تَصْوِيْرُ مَلامح مُعاناةِ البَنَّاءِ فِي فَصْلِ الشَّتَاءِ).

=== BLOCK 14: Irab 4 ===
(Component: TEMPLATE_C_IRAB.html)
Title: الإعراب
Content:
راحته: فاعل مرفوع، وعلامة رفعهِ الضَّمَّةُ الظَّاهرة. والهاء، ضمير متصل مَبْنِي على الضم في محل جر، مُضَاف إليه.
فَكَأَنها: الفاء، حرف استئناف. كأَن،َّ حرف مُشَبَّة بالفعل. وها، ضمير متصل مبني على السكون في محل نصب، اسم (كَأَنَّ).
من: حرف جر، بعضه، اسم مجرور وعلامة جره الكسرة الظاهرة، والهاء، ضميرٌ مُتَّصِلِّ مَبْنِي عَلَى الكسر في محل جر، مضاف إليه.
خَشَبُ : خَبَرِّ مرفوع.
جملة (جمدت ... راحته) : استثنافِيَّة،ٌ لا محل لها مِنَ الإعراب.
جملة (كأنها .. خشب): استنَافِيَّة،ٌ لَا مَحَلَّ لَهَا مِنَ الإعراب.

=== BLOCK 15: Poem 5 ===
(Component: TEMPLATE_C_POEM.html)
Right Hemistich: -١٠ تَلْهُو الرِّيَاحُ بِهِ فَإِنْ سَكَنَتْ
Left Hemistich: فَتَحَتْ عليهِ ثُقُوبَهَا السُّحُبُ

=== BLOCK 16: Analysis Matrix 5 ===
(Component: TEMPLATE_C_TABLE.html)
Title: تحليل البيت
Content:
الشرح | تَلْسَعُ الرياح الباردة البناء، وتَصْفَعُهُ بهبوبها العاصِف.ِ وعِندما تَهْدَأَ وَتَسْكُنُ تَبْدَأُ السَّمَاءُ بِسَكُبِ أَمْطَارِهَا العَزِيْرَةِ فَوْقَ جَسَدِهِ الْمُنْهَكِ.
الفكرة | تصوير مظاهر الشقاء في السعي لِكَسْبِ الرَزْقِ (تَصْوِيْرُ مَلامح مُعاناةِ البَنَّاءِ فِي فَصْلِ الشَّتَاءِ).

=== BLOCK 17: Irab 5 ===
(Component: TEMPLATE_C_IRAB.html)
Title: الإعراب
Content:
الرياحُ : فَاعِلَ مَرْفُوعٌ.
فَإِن: الفَاء،ُ حَرْفُ استناف. إِن حَرْفُ شَرْطٍ جَازَمٌ.
ثُقُوبَهَا : مَفْعُولُ بِهِ مَنْصُوب، وعلامَةً نَصْبِهِ الفَتْحَةُ الظَّاهِرَة.ُ وها، ضميرٌ مُتَّصِلِّ مَيْنِي على السُّكُونِ فِي مَحَلِّ جَر،ٍ مُضَاف إليه.
السُّحْبُ : فَاعِلَ مَرْفُوع.
جملة (تَلْهُو الرياح به): استنافَيَّة،ٌ لَا مَحَلَ لها مِنَ الإعراب.
جملة (إِنْ سَكَنَتْ فَتَحَتْ عَلَيْهِ ثُقُوبَهَا السحب): استئنافية، لا محل لها من الإعراب.
جملة (سَكَنَتْ) : جملَةُ الشَّرْطِ غَيْرِ الظرفي، لَا مَحَكَّ لَها من الإعراب.
جملة (فَتَحَتْ عليهِ ثُقُوبَهَا السُّحُبُ): جوابُ الشَّرْط،ِ لا مَحَلَّ لَهَا مِنَ الإعراب.

=== BLOCK 18: Poem 6 ===
(Component: TEMPLATE_C_POEM.html)
Right Hemistich: -۱۱ يا غَائِصًا بالطين لا نَصَب
Left Hemistich: يوهي عزيمته ولا وَصَبُ

=== BLOCK 19: Analysis Matrix 6 ===
(Component: TEMPLATE_C_TABLE.html)
Title: تحليل البيت
Content:
المفردات | وَصَب: وَجَع ومرض.
الشرح | أَيُّهَا البَنَّاء،ُ يَا مَنْ غَارَتْ قَدَمَاهُ فِي الوَحْلِ يَا مَنْ يُواصِلِ العَمَلَ رَغْمَ الْأَلَم والتعب.
الفكرة | مُوَاصَلَةُ البَنَّاءِ العَمَلَ رَغْمَ الْأَلَم والتَّعَبِ.

=== BLOCK 20: Cut Out ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
[WRAPPED_COMPONENT]: TEMPLATE_C_IRAB.html
Title: الإعراب
Content:
يا غائصا: يا، حَرْفُ نِدَاءٍ. غَائِصًا، مُنَادَى شبيه بالمَضَافِ مَنْصُوب.
لا نَصَب:ْ لا، حَرْفُ

--- END STREAM ---
