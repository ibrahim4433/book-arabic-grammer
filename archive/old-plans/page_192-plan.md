# **SESSION 192**

[TASK DEFINITION]
Objective: Implement page 192.
File: `pages/page_192.html`
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
[LESSON_NUMBER]: 192
[CHAPTER_TITLE]: page 192
[CATEGORY_HEADER]: 192
[SECTION_HEADER]: 192
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: إعراب (تتمة) ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[BLOCK_TITLE]: إعراب
[CONTENT]: ولا وَصَبُ الواو، حَرْفُ عَطْف. نفي. نصب، مبتداً مَرْفُوع عزيمته : مَفْعُولُ بِهِ مَنْصُوب، والهاء، ضميرٌ مُتَصِلٌ فِي مَحَلِّ جَر،ٍ مُضَاف إليه. : فِي مَحَلِّ رَفْعٍ خَبَر.ِّ زائِدَةً لتوكيدِ النَّفِي وَصَب،ْ اسمٌ مَعْطُوفٌ مَرْفُوع جملة لا نصب يوهي عزيمته في محل نَصْب، صفة جملة )يوهي(

=== BLOCK 3: البيت الثاني عشر ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البيت الثاني عشر
[POET_NAME]:
[RIGHT_HEMISTICH]: ۱۲- صبرا على الأَيَّامِ إِنْ عَبَسَتْ
[LEFT_HEMISTICH]: هَيْهَاتَ يَفْرج ضيقها غضب

=== BLOCK 4: الشرح ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: الشرح
[CONTENT]: إني أدعوك إلى الصَّر على قسوة الحياة، وأَنصَحُكَ بالابتِعَادِ عَنِ الانفعال والغَضَبِ؛ لأنهما لا يُفَرَجَانِ الكُرَب.َ

=== BLOCK 5: الفكرة ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[CONTENT]: الفكرة: مُحَاوَلَةُ التَّخْفِيفِ مِنْ آلَامِ البَنَّاءِ الكَادِحِ )دَعْوَةُ البَنَّاءِ الكادح إلى الصبر والابْتِعَادِ عَنِ الغَضَب(.

=== BLOCK 6: إعراب ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: صبر / إِنْ
[DETAILS_1]: صبر: مَفْعُول مُطْلَقَ مَنْصُوبٌ. إِنْ: حَرْفُ شَرْطِ جازم
[WORD_2]: هيهات / ضيقها
[DETAILS_2]: هيهات: اسمُ فِعْلِ ماض بمعنى: بَعْدَ(، مَبْنِي على الفَتْحَةِ الظَّاهِرَة.ِ ضيقها: مَفْعُولَ بِهِ مَنْصُوب،ُ وها، ضمير متصل في محل جر، مضاف إليه.

=== BLOCK 7: إعراب 2 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: غضب
[DETAILS_1]: فَاعِلَ مَرْفُوع
[WORD_2]: جملة
[DETAILS_2]: جملة )عَبَسَت(: جملة الشرط غير الطرفي لا محل لها من الإعراب جملة هَيْهَاتَ يَفْرُجُ .. غَضَبُ( : استنَافَيَّة،ٌ لَا حَلَ لها مِنَ الإعراب.

=== BLOCK 8: البيت الثالث عشر ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البيت الثالث عشر
[POET_NAME]:
[RIGHT_HEMISTICH]: ۱۳- ما أنتَ أَوَّلَ كَادِحِ عَثَرَتْ آماله
[LEFT_HEMISTICH]: وَكَبَابِهِ الدَّأَبُ

=== BLOCK 9: المفردات ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: الكلمة
[HEADER_2]: المعنى
[HEADER_3]: ملاحظات
[CELL_1]: كبا / الدَّابُ
[CELL_2]: تعرَ / السَّعْي والجد.
[CELL_3]: المفردات

=== BLOCK 10: الشرح ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: الشرح
[CONTENT]: عليكَ أَيُّهَا البَنَّاءُ أَنْ تعلمَ أَنَّ هُناك الكثير من الحائبين المتعبين الذين يعانون في هَذِهِ الحَيَاةِ مَا تُعاني منه،ُ فَلَسْتَ وحدَكَ مَنْ تكد وتشقى دون طائل.

=== BLOCK 11: الفكرة ===
(Component: TEMPLATE_C_BENEFIT.html)
[CONTENT]: الفكرة محاوَلَةُ التَّخْفِيفِ مِنْ آلَامِ البَنَّاءِ الكَادِحِ تَذْكِيرُ الْبَنَّاءِ الكادح بكثرة الخابين المتعيين(.

=== BLOCK 12: إعراب ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: ما أنت / أَوَّلَ
[DETAILS_1]: ما: ما، نافية تعمل عمل )ليس(. أَنْت،َ ضميرُ رَفْهِ مُنْفَصِلٌ فِي مَحَلَ رَفْعِ اسم )ما(. أَوَّلَ : خَبَرُ )ما( مَنْصُوبُ
[WORD_2]: كَادِحِ / آمالُهُ
[DETAILS_2]: كَادِحِ: مُضَاف إليهِ مَجْزَورٌ. آمالُهُ: فَاعِلْ مَرْفُوع والهاء، ضمير متصل في محل جر، مُضَاف إليه.

=== BLOCK 13: إعراب 2 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: وكيا / الدَّابُ
[DETAILS_1]: وكيا: الْوَاد،ِ حَرْفَ عَطْف.ِ كَبَبًا، فِعْلَ مَاضِ مَبْنِي على الفَتْحَةِ المُقَدَّرَةِ على الأَلِف،ِ مَنَعَ ظُهُورَهَا التَّعَذِّرُ. الدَّابُ : فَاعِلْ مَرْفُوع
[WORD_2]: جمله
[DETAILS_2]: جمله )مَا أَنتَ أَوَّلَ كَادِحٍ(: استِبْنَافَيَّة،ٌ لَا تَحَلَّ محلها الجر. لها من الإعراب جملة )عَلَرَتْ آماله(: في مَحَلَ جَة،ٍ صِفَةً جملةٌ كَيَا بِهِ الدَّاب(: معطوفة،ً

=== BLOCK 14: البيت الرابع عشر ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البيت الرابع عشر
[POET_NAME]:
[RIGHT_HEMISTICH]: -١٤ بَيْنِي وَبَيْنَكَ في البلاء وإن
[LEFT_HEMISTICH]: كَذَبَتْ عليك ظَوَاهِرِي نَسَبُ

=== BLOCK 15: الشرح ===
(Component: TEMPLATE_C_BLOCK.html)
[BLOCK_TITLE]: الشرح
[CONTENT]: أنا وأَنتَ أَيُّهَا البَنَّاءُ شريكان يَتَقَاسَمَان المعاناة والشَّقَاء،َ فلا تَغْرَنَّكَ مَظَاهِرُ النعيم التي تستُرُ مَشَقْتِي، وتحجب عنكَ عَنَائِي.

=== BLOCK 16: الفكرة ===
(Component: TEMPLATE_C_BENEFIT.html)
[CONTENT]: الفكرة : محاولة التَّخْفِيفِ مِنْ آلَامِ البَنَّاءِ الكادِح )مُشائِكَةُ البَنَّاء في الشقاء(.

=== BLOCK 17: إعراب ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: بيني / وبيتك
[DETAILS_1]: بيني: مَفْعُولُ فِيهِ ظَرْفُ مَكَانٍ مَنْصُوب، وعلامَةً نَصْبِهِ الفَتْحَةُ المقدرة على ما قبل باءِ التَّكَلِمَ مَتَعَ ظُهُورَها اشتغال المحل بالحركة المناسبة، والياء، ضمير متصل مَبْنِي على السكون فِي مَحَلَ جَر،ٍ مضاف إليه. وبيتك: الواو، حَرْفُ عَطْفٍ بين،َ مَفْعُول فيه ظرف مكانٍ مَعْطُوفَ مَنْصُوب، وعلامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَةُ والكاف، ضمير المُقدرة على ما قبل ياء المتكلم ، مَنَعَ ظهورها اشتغال المحل بالحركة المناسبة. والياء، ضميرٌ مُتَصِلَ مَبْنِي على السُّكُونِ فِي مَحَلَ جَر،ٍ مُضَافُ مُنصِلِّ مَبْنِي على الفَتْحَةِ فِي مَحَلَ جَر، مُضَاف إليه.
[WORD_2]: وإن / ظواهري
[DETAILS_2]: وإن: الواو، واو الحال. إن، وصلية زائدة. ظواهري : فاعل مرفوع، وعلامَةُ رَفْعِهِ الصَّمَّة

=== BLOCK 18: إعراب 2 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: نسب
[DETAILS_1]: نسب: مبتداً مؤخر مرفوع
[WORD_2]: جمله
[DETAILS_2]: جمله )بي... نسب(: استنافية، لا تحل لها مِنَ الإعراب جملة )كَذَبَتْ .. ظواهري(: في مُحَلَ نَصْب،ٍ حال.

=== BLOCK 19: أبيات النص المتممة ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: أبيات النص المُتَمِّمَةُ الوَارِدَةُ في ديوان زكي قنصل
[POET_NAME]: زكي قنصل
[RIGHT_HEMISTICH]: - فَكَأَنَّهُ فِي النَّاسِ حَاشِيَةٌ
[LEFT_HEMISTICH]: وَأَنَّهُ فِي الأَهْلِ مُغْتَرَبُ

=== BLOCK 20: بيت 2 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]:
[RIGHT_HEMISTICH]: جلبَابُهُ رُقَعُ تَالْفَهَا
[LEFT_HEMISTICH]: غرض وباعد بينها نَسَبُ

=== BLOCK 21: بيت 3 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]:
[RIGHT_HEMISTICH]: مَشَتِ السنين عليهِ فَاخْتَلَطَتْ
[LEFT_HEMISTICH]: أَصْبَاغُهُ وَتَقَارَبَ السَّبَبُ

=== BLOCK 22: بيت 4 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]:
[RIGHT_HEMISTICH]: الرَّفْسُ والمِنْقَارُ عُدَّتُهُ
[LEFT_HEMISTICH]: في العيش، لا علم ولا نَشَبُ

=== BLOCK 23: بيت 5 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]:
[RIGHT_HEMISTICH]: ه- ضَاقَتْ بِهِ دُنیاهُ وَاعْتَلَجَتْ
[LEFT_HEMISTICH]: فِي صَدْرِهِ الزَّقَرَاتُ والكُرَبُ

=== BLOCK 24: بيت 6 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]:
[RIGHT_HEMISTICH]: - بالروح في موز وقفته
[LEFT_HEMISTICH]: يَكُويهِ مِنْ أَنْفَاسِهِ فَعَبُ

=== BLOCK 25: بيت 7 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]:
[RIGHT_HEMISTICH]: عَرَقُ الجهاد يزين جبهته
[LEFT_HEMISTICH]: تاجا عَلَتْهُ هَالَةٌ عَجَبُ

=== BLOCK 26: بيت 8 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]:
[RIGHT_HEMISTICH]: یرنو بطرفٍ غَارَ بُوبُوهُ
[LEFT_HEMISTICH]: فِي دَمْعَةٍ وَتَكَمِّشَ الهدب

=== BLOCK 27: بيت 9 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]:
[RIGHT_HEMISTICH]: - يا رَبِّ عَفُوكَ إِنْ كَفَرْتُ فَمَا
[LEFT_HEMISTICH]: ترقي إلى مَلَكُوتك الريب

=== BLOCK 28: بيت 10 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]:
[RIGHT_HEMISTICH]: -۱۰ أَمِنَ العَدَالَةِ أَنْ تُعَرَضَهُ
[LEFT_HEMISTICH]: للفيمٍ يَنْهَشُهُ وَيَنْتَهِبُ؟

=== BLOCK 29: بيت 11 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]:
[RIGHT_HEMISTICH]: -۱۱ أو ضَاقَ عَطْفُكَ دونَ حَاجَتِهِ
[LEFT_HEMISTICH]: فَحَبَسْتَ عَنْهُ بَعْضَ ما تحب؟

=== BLOCK 30: بيت 12 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]:
[RIGHT_HEMISTICH]: -۱۲ أوليسَ يَجْمَعُهُ بِسَيِّدِهِ
[LEFT_HEMISTICH]: نَسَبْ مِنَ الصَّلْصَالِ أَوْ حَسَبُ؟

=== BLOCK 31: بيت 13 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]:
[RIGHT_HEMISTICH]: -۱۳ فَعَلَامَ تَشْتَاقُ الرِّيَالَ يَدْ
[LEFT_HEMISTICH]: وَيَدٌ تَرَاكَمَ حَهَا الذَّهَبُ؟

=== BLOCK 32: بيت 14 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]:
[RIGHT_HEMISTICH]: -١٤ وعلامَ يَشْرَقُ بالدموع فتى
[LEFT_HEMISTICH]: وفَتَّى يَر ندِيهُ الطَّرَبُ؟

=== BLOCK 33: بيت 15 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]:
[RIGHT_HEMISTICH]: -١٥ وعلامَ يُغْصَبُ حَقُّ مُجْتَهِدِ
[LEFT_HEMISTICH]: لِيَفُوز باللَّذَاتِ مُغْتَصِبُ؟

=== BLOCK 34: بيت 16 ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]:
[POET_NAME]:
[RIGHT_HEMISTICH]: ١٦- أ أشقَاكَ سَعْيِّ لَا ثَوَابَ لَهُ
[LEFT_HEMISTICH]: أَمَّا أَنَا فَمُصِيبَتِ الأدب مكن ۱۹۲

--- END STREAM ---
