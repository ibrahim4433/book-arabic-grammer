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
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
15. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !

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

=== BLOCK 2: إعراب مُكْتَمَل ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
(Component inside: TEMPLATE_C_IRAB.html)
Title: إعراب
Content:
- ولَمْ نَحْتَسِبِ : الواو، حَرْفُ عَطْفٍ. لَمْ، حَرْفٌ جازمٌ. نَحْتَسِبٍ، فِعْلَ مُصَارِعُ مَجْرُوم، وعلامَةُ جَزْمِهِ السُّكُونُ وحرك بالكُسْرَةِ لِلضرورة الشَّعْرِيَّةِ
- جُمَلَةً قَدْ عرفنا : استئنافية، لا محل لها مِنَ الإعراب
- جُمْلَةُ لَمْ نُرْخِص( : مَعْطُوفَة،ٌ لَا مَحَكَ لَهَا مِنَ الإعراب
- جملةً لَمْ نَحْتَسِب( : مَعْطُوفَة،ٌ لَا حَل لها مِنَ الإعراب.

=== BLOCK 3: البيت الثالث عشر ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: وأَرَقُناها دِمَاءً حَرَّةً
Hemistich 2: فاعرفي ما شنت منها واشربي !

=== BLOCK 4: شرح البيت الثالث عشر وتحليله ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تحليل البيت الثالث عشر (Class: accent)
Content:
(Component inside: TEMPLATE_C_LIST.html)
- <span class="text-accent">الشرح:</span> أهرقنا بسخاء دماءنا الطاهرة الزكية في سبيلك أيتها الحرية، فاهنئي واسعدي وتباهي بهذا المهر الثمين.
- <span class="text-accent">الفكرة:</span> تَمَجِيدُ النَّصْحِياتِ الَّتِي قَدَّمَهَا الشَّعْبُ السوري لِنَيْلِ استقلاله، والاعتزاز بها (تمجيد الشَّهَادِة والشُّهَدَاء).
- <span class="text-accent">الشعور:</span> اعتزاز وافتخار
- <span class="text-accent">الأداة:</span> التراكيب
- <span class="text-accent">المثال:</span> <span class="highlight-green">أَرَقْنَاهَا دِمَاءً حُرَّة.</span>
- <span class="text-accent">الأساليب:</span> (اغرفي ما شِنْتِ)، (الشربي): أسلوب أمر. صيفته: فعل أمر

=== BLOCK 5: إعراب البيت الثالث عشر ===
(Component: TEMPLATE_C_IRAB.html)
Title: إعراب المفردات والجمل
Content:
- وأَرقناها: الواو، حَرْفُ عَطْفِ. أَرَقْنَاها، فعل ماض مبني على السُّكُون لاتِصَالِهِ بِصَمِيرِ الرَّفْعِ (نا) الدَّالَّةِ على الفاعلين. ونا، ضمير مُتَّصِلِّ مَبْنِي على السكون فِي مَحَلِّ رَفْعٍ، فاعل. وها، ضمير مُتَصِلِّ مَيْنِي على السُّكُونِ فِي حَلِّ نَصْبٍ، مَفْفُولٌ بِهِ.
- دِمَاءً: بَدَلِّ مَنْصُوبُ.
- حَرَّةٌ: صِفَةٌ مَنْصُوبَةٌ.
- فَاغْرفي: الفاء، حَرْفُ اسْتِثْنَافِ. اغْرفي، فِعْلَ أَمْرِ مَبْنِي على خَذْفِ النُّون، لأن مُضَارِعَهُ مِنَ الْأَفْعَالِ الخمسة والياء، ضمير مُتَصِلَ مَبْنِي على السُّكون في محل رفع، فاعل.
- ما: اسم مَوْصُولُ مَبْنِي على السُّكُونِ فِي مَحَلِّ نَصْبٍ، مَفْعُولُ بِهِ.
- وَاشْري: الواو، حَرْفُ عَطْفُ. اشْرَبِي، فِعْلُ أَمْرٍ مَبْنِي على حَذْفِ النُّونِ لِأَنْ مُصَارِعَهُ مِنَ الأفعال الخمسة. والياء، ضمير متصل مبني على السُّكُونِ فِي مَحَلَ رَفْع، فَاعِلٌ.
- جملَةُ (اغْرُفِي): استئنافية، لا محل لها مِنَ الإعراب.
- جُمْلَةُ (شِنْتِ): صلة الموصول، لا مَحَلَّ لها مِنَ الإعراب.
- جملة (اشْرَبِي) : مَعْطُوفَة،ٌ لا تحل لها مِنَ الإعراب.

=== BLOCK 6: البيت الرابع عشر ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: نَحْنُ مِنْ ضَغْفِ بَيْنَا قُوَّةً
Hemistich 2: لَا تَلِنْ لِلْمارج الملتهب

=== BLOCK 7: شرح البيت الرابع عشر وتحليله ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تحليل البيت الرابع عشر
Content:
(Component inside: TEMPLATE_C_LIST.html)
- <span class="text-accent">المفردات:</span> تلن: تنقاد. المارج: الشعلة الساطعة ذات اللهب الشديد. الملتهب: اللامع المتقد.
- <span class="text-accent">الشرح:</span> صنعنا من الضَّعف قوة ما انقادت أو ضَعُفَتْ أمام جبروت المستعمر المدجج بالأسلحة الفتاكة التي تقذف حمم الغدر المتقدة.
- <span class="text-accent">الفكرة:</span> الإصرار على تَحَدِي قُوَّةِ المُسْتَعْمِرِ رغم ضَعْفِ الإمكانات.
- <span class="text-accent">الشعور:</span> اعتزاز وافتخار
- <span class="text-accent">الأداة:</span> التراكيب
- <span class="text-accent">المثال:</span> <span class="highlight-green">نَحْنُ مِنْ ضَعْفِ بَيْنَا قُوَّةً.</span>
- <span class="text-accent">البلاغة:</span> (ضَعْف، قُوَّة): طباق إيجاب.
- <span class="text-accent">الأساليب:</span> لم تلن: أسلوب نفي الأداة: لم. أفادت نفي وقوع الفعل المضارع في الزمن الماضي.

=== BLOCK 8: إعراب البيت الرابع عشر ===
(Component: TEMPLATE_C_IRAB.html)
Title: إعراب المفردات والجمل
Content:
- نَحْنُ : ضميرُ رَفْعٍ مُنْفَصِل، مبني على الصَّمَّةِ فِي مَحَلِ رَفْعٍ، مُبْتَدَا.
- بَنَيْنَا: فعل ماضِ مَبْنِي على السُّكُون: لا تَصَالِهِ بِضمير الرفع (نا) الدالة على الفاعلينَ. ونا، ضميرٌ مُتَّصِلِّ مَبْنِي على السُّكُونِ فِي مَحَلِّ رَفْهِ، فَاعِلٌ.
- قُوَّةَ: مَفْعُولُ بِهِ مَنْصُوبُ.
- لَمْ تَلِنْ: لَم حَرْفٌ جارَمٌ. تَلِنْ فِعْلَ مُضارع مُجْرُوم، وعلامَةً جَزْمِهِ السُّكُونُ.
- الْتَهِبِ : صِفَةً مجْرُورَةٌ.
- جُمْلَةً (نَحْنُ مِنْ ضَعْفٍ بَنَيْنَا) : استئنافية، لا تحل لها من الإعراب.
- جُمْلَهُ (بَبَيْنَا) : خَبَرَيَّة،ٌ مَحَلُّهَا الرَّفْعُ.
- جملة (لَم تَلِنَ): صِفَة،ٌ مَحَلُّهَا النَّصْبُ.

=== BLOCK 9: البيت الخامس عشر ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: هَذِهِ تُرْبِتُنَا لَنْ تَزْدَهِي
Hemistich 2: سوانا من حماةٍ نُدُبِ

=== BLOCK 10: شرح البيت الخامس عشر وتحليله ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تحليل البيت الخامس عشر
Content:
(Component inside: TEMPLATE_C_LIST.html)
- <span class="text-accent">المفردات:</span> ندب: المفرد نذب، وهو الخفيف في الحاجة؛ لأنه إذا ندب إليها خف لقضائها.
- <span class="text-accent">الشرح:</span> إنَّ أرضنا المباركة الطاهرة لا تفخر إلا بحماية أبنائها، وترفض كل أشكال الحماية والوصاية والانتداب.
- <span class="text-accent">الفكرة:</span> دور الأبطال في حمايةِ الأَرْضِ وَحِفْظِ كَرَامَتِها رفض الحماية والوصاية والانْتِدَابِ مِنْ قِبَلِ المُسْتَعْمِرِ.
- <span class="text-accent">البلاغة:</span> (تربتُنَا لَنْ تَزْدَهِي): استعارَةُ مَكْنِيَّةٌ.
- <span class="text-accent">الأساليب:</span> لَنْ تَزْدَهِي: أسلوب نفي الأداة: تن. أفادت نفي وقوع الفعل المضارع في الزَّمَن المستقبل.

=== BLOCK 11: إعراب البيت الخامس عشر ===
(Component: TEMPLATE_C_IRAB.html)
Title: إعراب المفردات والجمل
Content:
- هَذِهِ: الهَاءُ، حَرْفُ تَنْبِيهِ ذِهٍ، اسمُ إِشَارَةِ مَبْنِي على الكَسْرَةِ فِي مَحَلِ رَفْعٍ، مُبْتَدَاً.
- ترينا: خَبَرٌ مَرْفُوع، وعلامَةُ رَفْعِهِ السَّمَةُ الظَّاهِرَةُ. ونا، ضمير متصل مبني على السُّكُون في محل جر، مُضَاف إليه.
- لَنْ تَزْدَهي: لَنْ حَرْفٌ نَاصِبٌ. تَزْدَهي، فِعْلَ مُصَارِعٌ مَنْصُوب،ُ وعلامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَةُ. وسُكِّنَ لِلضرورة الشَّعْرِيَّة.
- بسوانا: الباء، حَرْفُ جر. سوانا، اسم تجرُور، وعلامة جَرَّهِ الكَسْرَةُ المُقَدَّرَةُ على الأَلِفِ مَنَعَ ظُهُورَهَا التَعَدُّرُ. ونا، ضميرٌ مُتَصِلَ مَبْنِي على السُّكُونِ فِي مَحَلِّ جَةٍ، مُضَاف إليه.
- نُدْبِ : صِفَةٌ مَجْرُورَةٌ.
- جُمْلَهُ (هَذِهِ تُرْبِتُنا): استثنافِيَّة،ٌ لَا مَحَلَّ لها مِنَ الإعراب.
- جُمْلَهُ (لَنْ تَزْدَهي): خَبَرَيَّة،ٌ مَحَلَّهَا الرَّفْعُ.

=== BLOCK 12: ملحق الأبيات الخارجية ===
(Component: TEMPLATE_C_BENEFIT.html)
Title: ملحق الأبيات الخارجية المتممة
Content: الواردة في ديوان الشاعر عمر أبو ريشة:

=== BLOCK 13: البيت الخارجي الأول ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: وأمانيه انتفاض الأرضِ مِنْ
Hemistich 2: غَيْهَبِ الدَّلِّ، وذُلِ الغَيْهَبِ

=== BLOCK 14: تحليل البيت الخارجي الأول ===
(Component: TEMPLATE_C_BLOCK.html)
Title: التحليل والإعراب (Class: accent)
Content:
(Component inside: TEMPLATE_C_LIST.html)
- <span class="text-accent">المفردات:</span> الفيهب: الظُّلْمَةُ. ومِنَ اللَّيل الشديد الظُّلْمَةِ.
- <span class="text-accent">الشرح:</span> عندما أَقْدَمَ الإنسان العربي إلى فُتُوحَاتِهِ كَانَ يَحْلُمُ أَنْ يَنْتَفِضَ أَبْنَاءُ الأَمَّةِ العربية، ويتوروا مِنْ أَجْلِ الخلاص مِنْ ظُلْمَةِ الدُّل والخنُوع.
- <span class="text-accent">البلاغة:</span> (غَيْهَبِ الدُّل)، (ذَلِ الغَيْهَبِ): تَشْبِيهُ بَلِيْ إِضَافِي.
- <span class="text-accent">الإعراب:</span> أمانيه : مُبْعَدَاً مَرْفُوعُ. انْتَقَاضُ: خَبَرٌ مَرْفُوع. الأَرْضِ، الدُّلِّ، الغَيْهَبِ : مُصَافُ إِلَيْهِ تَجْرُورٌ.

=== BLOCK 15: البيت الخارجي الثاني ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: مختضب وانطلاق النور حتى
Hemistich 2: يرتوي : كُلُّ خَفْنِ بالقرى

=== BLOCK 16: تحليل البيت الخارجي الثاني ===
(Component: TEMPLATE_C_BLOCK.html)
Title: التحليل والبلاغة
Content:
(Component inside: TEMPLATE_C_LIST.html)
- <span class="text-accent">المفردات:</span> مختضب : خَضَبَ خَضْبًا وَخُضُوبًا تلون ومختصب : اسم فاعل فعله: اختضب.
- <span class="text-accent">الشرح:</span> وكانَ يَحْلُمُ كَذَلِكَ بِأَنْ تَغْشَى أنوارُ النَّصْرِ وَجْهَ الإنسان العربي، وَتَسَحَ عَنْهُ غَبَارَ الذّلِ الذي لَطَّحْ جَبِيْنَهُ، عَفَرَ جَفْنَهُ.
- <span class="text-accent">البلاغة:</span> (يَرتوي كُلِّ جَفْنِ): استعارَةً مِكْنِيَّةٌ.

--- END STREAM ---
