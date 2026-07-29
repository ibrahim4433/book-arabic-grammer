# **SESSION 110**

[TASK DEFINITION]
Objective: Implement page 110.
File: `pages/page_110.html` (Note: Use the exact page number.)
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
[LESSON_NUMBER]: 110
[CHAPTER_TITLE]: page 110
[CATEGORY_HEADER]: 110
[SECTION_HEADER]: 110
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: إعراب (تتمة) ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[BLOCK_TITLE]: إعراب
[CONTENT]: ولَمْ نَحْتَسِبِ : الواو، حَرْفُ عَطْفٍ لَم،ْ حَرْفٌ جازمٌ نَحْتَسِب،ٍ فِعْلَ مُصَارِعُ مَجْرُوم، وعلامَةُ جَزْمِهِ السُّكُونُ وحرك بالكُسْرَةِ لِلضرورة الشَّعْرِيَّةِ. جُمَلَةً قَدْ عرفنا : استئنافية، لا محل لها مِنَ الإعراب. جُمْلَةُ (لَمْ نُرْخِص) : مَعْطُوفَة،ٌ لَا مَحَكَ لَهَا مِنَ الإعراب. جملةً (لَمْ نَحْتَسِب) : مَعْطُوفَة،ٌ لَا حَل لها مِنَ الإعراب.

=== BLOCK 3: البيت الثالث عشر ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البيت الثالث عشر
[POET_NAME]:
[RIGHT_HEMISTICH]: وأَرَقُناها دِمَاءً حَرَّةً
[LEFT_HEMISTICH]: فاعرفي ما شنت منها واشربي !

=== BLOCK 4: الشرح ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الشرح
Content: <span class="text-accent">أهرقنا بسخاء دماءنا الطاهرة الزكية في سبيلك أيتها الحرية، فاهنئي واسعدي وتباهي بهذا المهر الثمين.</span>

=== BLOCK 5: الفكرة والأساليب ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: الفكرة
[HEADER_2]: الشعور
[HEADER_3]: الأداة والمثال والأساليب
[CELL_1]: تَمَجِيدُ النَّصْحِياتِ الَّتِي قَدَّمَهَا الشَّعْبُ السوري لِنَيْلِ استقلاله، والاعتزاز بها (تمجيد الشَّهَادِة والشُّهَدَاء).
[CELL_2]: اعتزاز وافتخار
[CELL_3]: الأداة: التراكيب المثال: أَرَقْنَاهَا دِمَاءً حُرَّة. الأساليب: (اغرفي ما شِنْتِ)، (اشربي): أسلوب أمر. صيغته: فعل أمر.

=== BLOCK 6: إعراب مفردات البيت الثالث عشر ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: وأَرقناها
[IRAB_ANALYSIS]: الواو، حَرْفُ عَطْفِ أَرَقْنَاها، فعل ماض مبني على السُّكُون لاتِصَالِهِ بِصَمِيرِ الرَّفْعِ (نا) الدَّالَّةِ على الفاعلين. ونا، ضمير مُتَّصِلِّ مَبْنِي على السكون فِي مَحَلِّ رَفْع،ِ فاعل. وها، ضمير مُتَصِلِّ مَيْنِي على السُّكُونِ فِي حَلِّ نَصْب،ِ مَفْفُولٌ بِهِ.

=== BLOCK 7: إعراب مفردات ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: دِمَاءً
[DETAILS_1]: بَدَلِّ مَنْصُوبُ.
[WORD_2]: حَرَّةٌ
[DETAILS_2]: صِفَةٌ مَنْصُوبَة،ٌ.

=== BLOCK 8: إعراب مفردات ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: فَاغْرفي
[IRAB_ANALYSIS]: الفاء، حَرْفُ اسْتِثْنَافِ اغْرفي، فِعْلَ أَمْرِ مَبْنِي على خَذْفِ النُّون، لأن مُضَارِعَهُ مِنَ الْأَفْعَالِ الخمسة والياء، ضمير مُتَصِلَ مَبْنِي على السُّكون في محل رفع، فاعل.

=== BLOCK 9: إعراب مفردات ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: ما
[DETAILS_1]: اسم مَوْصُولُ مَبْنِي على السُّكُونِ فِي مَحَلِّ نَصْب،ِ مَفْعُولُ بِهِ.
[WORD_2]: وَاشْرَبِي
[DETAILS_2]: الواو، حَرْفُ عَطْفُ اشْرَبِي، فِعْلُ أَمْرٍ مَبْنِي على حَذْفِ النُّونِ لِأَنْ مُصَارِعَهُ مِنَ الأفعال الخمسة. والياء، ضمير متصل مبني على السُّكُونِ فِي مَحَلَ رَفْع، فَاعِل.ْ

=== BLOCK 10: إعراب الجمل ===
(Component: TEMPLATE_C_BLOCK.html)
Title: إعراب الجمل
Content: جملَةُ (اغْرُفِي): استئنافية، لا محل لها مِنَ الإعراب. جُمْلَةُ (شِنْتِ): صلة الموصول، لا مَحَلَّ لها مِنَ الإعراب. جملة (اشْرَبِي) : مَعْطُوفَة،ٌ لا تحل لها مِنَ الإعراب.

=== BLOCK 11: البيت الرابع عشر ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البيت الرابع عشر
[POET_NAME]:
[RIGHT_HEMISTICH]: نَحْنُ مِنْ ضَغْفِ بَيْنَا قُوَّةً
[LEFT_HEMISTICH]: لَا تَلِنْ لِلْمارج الملتهب

=== BLOCK 12: المفردات والشرح ===
(Component: TEMPLATE_C_SPLIT.html)
[TITLE_RIGHT]: المفردات
[CONTENT_RIGHT]: تلن: تنقاد. المارج: الشعلة الساطعة ذات اللهب الشديد. الملتهب: اللامع المتقد.
[TITLE_LEFT]: الشرح
[CONTENT_LEFT]: صنعنا من الضَّعف قوة ما انقادت أو ضَعُفَتْ أمام جبروت المستعمر المدجج بالأسلحة الفتاكة التي تقذف حمم الغدر المتقدة.

=== BLOCK 13: الفكرة (Warning Box for Orange Color Balance) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[TITLE]: الفكرة
[CONTENT]: الإصرار على تَحَدِي قُوَّةِ المُسْتَعْمِرِ رغم ضَعْفِ الإمكانات. الشعور: اعتزاز وافتخار. الأداة: التراكيب المثال: نَحْنُ مِنْ ضَعْفِ بَيْنَا قُوَّة.ً البلاغة: (ضَعْف، قُوَّة): طباق إيجاب. الأساليب : لم تلن: أسلوب نفي الأداة: لم. أفادت نفي وقوع الفعل المضارع في الزمن الماضي.

=== BLOCK 14: إعراب مفردات البيت الرابع عشر ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: نَحْنُ
[IRAB_ANALYSIS]: ضميرُ رَفْعٍ مُنْفَصِل، مبني على الصَّمَّةِ فِي مَحَلِ رَفْع،ِ مُبْتَدَا.

=== BLOCK 15: إعراب مفردات ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: بَنَيْنَا
[IRAB_ANALYSIS]: فعل ماضِ مَبْنِي على السُّكُون: لا تَصَالِهِ بِضمير الرفع (نا) الدالة على الفاعلين.َ ونا، ضميرٌ مُتَّصِلِّ مَبْنِي على السُّكُونِ فِي مَحَلِّ رَفْه،ِ فَاعِلٌ.

=== BLOCK 16: إعراب مفردات ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: قُوَّةَ
[DETAILS_1]: مَفْعُولُ بِهِ مَنْصُوبُ.
[WORD_2]: لَمْ تَلِنْ
[DETAILS_2]: لَم حَرْفٌ جارَمٌ تَلِنْ فِعْلَ مُضارع مُجْرُوم، وعلامَةً جَزْمِهِ السُّكُونُ.

=== BLOCK 17: إعراب مفردات والجمل ===
(Component: TEMPLATE_C_BLOCK.html)
Title: إعراب الجمل والصفات
Content: الملتهبِ : صِفَةً مجْرُورَةٌ. جُمْلَةً (نَحْنُ مِنْ ضَعْفٍ بَنَيْنَا) : استئنافية، لا تحل لها من الإعراب. جُمْلَهُ (بَبَيْنَا) : خَبَرَيَّة،ٌ مَحَلُّهَا الرَّفْعُ. جملة (لَم تَلِنَ): صِفَة،ٌ مَحَلُّهَا النَّصْب.ُ

=== BLOCK 18: البيت الخامس عشر ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البيت الخامس عشر
[POET_NAME]:
[RIGHT_HEMISTICH]: هَذِهِ تُرْبِتُنَا لَنْ تَزْدَهِي
[LEFT_HEMISTICH]: بسوانا من حماةٍ نُدُبِ

=== BLOCK 19: المفردات والشرح ===
(Component: TEMPLATE_C_SPLIT.html)
[TITLE_RIGHT]: المفردات
[CONTENT_RIGHT]: ندب: المفرد ندب، وهو الخفيف في الحاجة؛ لأنه إذا ندب إليها خف لقضائها.
[TITLE_LEFT]: الشرح
[CONTENT_LEFT]: إنَّ أرضنا المباركة الطاهرة لا تفخر إلا بحماية أبنائها، وترفض كل أشكال الحماية والوصاية والانتداب.

=== BLOCK 20: الفكرة ===
(Component: TEMPLATE_C_BENEFIT.html)
[TITLE]: الفكرة
[CONTENT]: دور الأبطال في حمايةِ الأَرْضِ وَحِفْظِ كَرَامَتِها (رفض الحماية والوصاية والانْتِدَابِ مِنْ قِبَلِ المُسْتَعْمِرِ).

=== BLOCK 21: البلاغة والأساليب ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
[TITLE]: البلاغة والأساليب
[CONTENT]: البلاغة: (تربتُنَا لَنْ تَزْدَهِي): استعارَةُ مَكْنِيَّة.ٌ الأساليب: لَنْ تَزْدَهِي: أسلوب نفي الأداة: لن. أفادت نفي وقوع الفعل المضارع في الزَّمَن المستقبل.

=== BLOCK 22: إعراب مفردات البيت الخامس عشر ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: هَذِهِ
[IRAB_ANALYSIS]: الهَاء،ُ حَرْفُ تَنْبِيهِ ذِه،ِ اسمُ إِشَارَةِ مَبْنِي على الكَسْرَةِ فِي مَحَلِ رَفْع،ِ مُبْتَدَأٌ.

=== BLOCK 23: إعراب مفردات ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: تربتنا
[IRAB_ANALYSIS]: خَبَرٌ مَرْفُوع، وعلامَةُ رَفْعِهِ السَّمَةُ الظَّاهِرَة.ُ ونا، ضمير متصل مبني على السُّكُون في محل جر، مُضَاف إليه.

=== BLOCK 24: إعراب مفردات ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: لَنْ تَزْدَهي
[IRAB_ANALYSIS]: لَنْ حَرْفٌ نَاصِب.ٌ تَزْدَهي، فِعْلَ مُصَارِعٌ مَنْصُوب،ُ وعلامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَة.ُ وسُكِّنَ لِلضرورة الشَّعْرِيَّة.

=== BLOCK 25: إعراب مفردات ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: بسوانا
[IRAB_ANALYSIS]: الباء، حَرْفُ جر. سوانا، اسم تجرُور، وعلامة جَرَّهِ الكَسْرَةُ المُقَدَّرَةُ على الأَلِفِ مَنَعَ ظُهُورَهَا التَعَدُّر.ُ ونا، ضميرٌ مُتَصِلَ مَبْنِي على السُّكُونِ فِي مَحَلِّ جَرٍّ، مُضَاف إليه.

=== BLOCK 26: إعراب مفردات والجمل ===
(Component: TEMPLATE_C_BLOCK.html)
Title: إعراب الجمل والصفات
Content: نُدْبِ : صِفَةٌ مَجْرُورَة.ً جُمْلَهُ (هَذِهِ تُرْبِتُنا): استثنافِيَّة،ٌ لَا مَحَلَّ لها مِنَ الإعراب. جُمْلَهُ (لَنْ تَزْدَهي): خَبَرَيَّة،ٌ مَحَلَّهَا الرَّفْع.ُ

=== BLOCK 27: ملحق الأبيات ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: الأبيات الخارجية
[POET_NAME]: ملحق الأبيات الخارجية المتممة الواردة في ديوان الشاعر عمر أبو ريشة
[RIGHT_HEMISTICH]: وأمانيه انتفاض الأرضِ
[LEFT_HEMISTICH]: مِنْ غَيْهَبِ الدَّل،ِّ وذُلِ الغَيْهَبِ

=== BLOCK 28: المفردات والشرح ===
(Component: TEMPLATE_C_SPLIT.html)
[TITLE_RIGHT]: المفردات
[CONTENT_RIGHT]: الغيهب: الظُّلْمَة.ُ ومِنَ اللَّيل الشديد الظُّلْمَةِ.
[TITLE_LEFT]: الشرح
[CONTENT_LEFT]: عندما أَقْدَمَ الإنسان العربي إلى فُتُوحَاتِهِ كَانَ يَحْلُمُ أَنْ يَنْتَفِضَ أَبْنَاءُ الأَمَّةِ العربية، ويثوروا مِنْ أَجْلِ الخلاص مِنْ ظُلْمَةِ الدُّل والخنُوع. البلاغة: (غَيْهَبِ الدُّذل)، (ذَلِ الغَيْهَبِ) : تَشْبِيهُ بَلِيْغٌ إِضَافِي.

=== BLOCK 29: إعراب الأبيات الخارجية ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: أمانيه / انتفاض
[DETAILS_1]: أمانيه: مُبْتَدَأٌ مَرْفُوعُ. انتفاض: خَبَرٌ مَرْفُوع.
[WORD_2]: الأرضِ / الذل / الغيهب
[DETAILS_2]: مُضَافُ إِلَيْهِ مَجْرُور.ٌ

=== BLOCK 30: البيت المتمم الثاني ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البيت المتمم الثاني
[POET_NAME]:
[RIGHT_HEMISTICH]: وانطلاق النور حتى يرتوي
[LEFT_HEMISTICH]: كُلُّ جَفْنٍ بالقرى مُخْتَضِبِ

=== BLOCK 31: المفردات والشرح ===
(Component: TEMPLATE_C_SPLIT.html)
[TITLE_RIGHT]: المفردات
[CONTENT_RIGHT]: مختضب : خَضَبَ خَضْبًا وَخُضُوبًا تلون ومختصب : اسم فاعل فعله: اختضب.
[TITLE_LEFT]: الشرح
[CONTENT_LEFT]: وكانَ يَحْلُمُ كَذَلِكَ بِأَنْ تَغْشَى أنوارُ النَّصْرِ وَجْهَ الإنسان العربي، وَتَسَحَ عَنْهُ غَبَارَ الذّلِ الذي لَطَّحْ جَبِيْنَه،ُ عَفَرَ جَفْنَهُ. البلاغة: (يَرتوي كُلِّ جَفْنِ) : استعارَةً مِكْنِيَّة.ٌ

--- END STREAM ---
