# **SESSION 123**

[TASK DEFINITION]
Objective: Implement page 123.
File: `pages/page_123.html` (Note: Use the exact page number.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools. If it overflows, it is a catastrophic failure. Do NOT try to solve overflow by deleting text (Strict Typographer Rule). Solve it by choosing denser templates or omitting optional white-space.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`. Ensure exact visual continuity (same title, same classes).
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md` to identify the correct template to use for the continuation. You are forbidden from guessing. Scan the raw text for the preceding keyword to determine the active template and apply the correct `_PART_2.html` wrapping.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide: NO INLINE STYLES. Irab Words inside `.irab-word` MUST be white.
7. Templates: You are forbidden from inventing new HTML tags or classes or template elements. You must map all content using "Jules-workspace/Templates/" components as the STREAM says in suitable way. **CRITICAL 1-PAGE MODE RULE**: You MUST NOT use `<section>` tags when applying templates. Replace any `<section>` tags from the templates with `<div>` tags (keep `<header>` for page headers as is).
8. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). The ID MUST be applied to the `<div>` tag that replaced the `<section>` tag.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...) .
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense. Do NOT leave empty space.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
15. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 123
[CHAPTER_TITLE]: page 123
[CATEGORY_HEADER]: 123
[SECTION_HEADER]: 123
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: إعراب المقطع السابق (Cut Content Continuation) ===
(Component: TEMPLATE_CUT_BOX_PART_2.html wrapping TEMPLATE_C_IRAB.html)
[BLOCK_TITLE]: إعراب
Content:
- وسُكِّنَ: لِلضَّرُورَةِ الشِّعْرِيَّةِ.
- والشيخ: الواو، حَرْفُ استئناف. الشَّيْخُ، مُبْتَدَأٌ مَرْفُوعٌ
- كَ: مَفْعُولٌ بِهِ مَنْصُوبُ
- ابْنَتِهِ: مُضَافُ إليهِ مَجْرُور،ُ وعلامة جَرَهِ الكَسْرَةُ الظَّاهِرَةُ والهاء، ضمير متصل مَبْنِي على الكَسْرَةِ فِي مَحَلِّ جر، مُضَاف إليه.
- ويتلو: الواو، حَرْفُ عَطْفٍ. يَتْلو، فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وعلامَةُ رَفْعِهِ الضَّمَّةُ المُقَدَّرَةُ على الواو، مَنَعَ ظهورها الثَّقَلُ
- هَمْسًا: حالٌ مَنْصُوبَةٌ
- سُورة: مَفْعُولُ بِهِ مَنْصُوب،ُ وعلامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَة.ُ وسُكِّنَ لِلضرورة الشعْرِيَّة.ِ
- وبلهْجَةِ: الواو، حَرْفُ اسْتِثْنَاف والباء، حَرْفُ جر. لهجة، اسم مجرور
- كالحلم: الكَافُ حَرْفُ جر. الحلم، اسم مجرور.
- عَيْنَا: مُبْتَداً مَرْفُوع، وعلامَةُ رَفْعِهِ الأَلِفُ لِأَنَّهُ مُثَنَّى وَحُذِفَتِ النُونُ لِلإِضَافَةِ
- حَبِيبتي: مُضَافُ إليهِ مَجْرُور،ُ وعلامَةُ جَرَهِ الكَسْرَةُ الظَّاهِرَةُ والياء، ضميرٌ مُتَّصِلِّ مَبْنِي على السُّكُون في محل جر،ٍ مُضَاف إليه
- الصغيرة: صفة مجرورة، وعلامَةُ جَرِهِ الكَسْرَةُ الظَّاهِرَة.ُ وسُكِّنَتْ لِلضرورة الشعْرِيَّة.ِ
- يا جنود: يا، حَرْفُ نِدَاءِ جُنُود،ُ مُنَادَى نَكِرَةٌ مَقْصُودَة،ٌ مَبْنِي على الضَّمَّة،ِ في مَحَلِّ نَصْبِ على النِّدَاء.ِ
- ووجهها: الواو، حَرْفُ عَطْفٍ وَجْهُهَا، مُبْتَداً مَرْفُوع، وعلامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَة.ُ وها، ضميرٌ مُتَّصِلِّ مَبْنِي على السكون فِي مَحَلِّ جر،ٍ مُضَاف إليهِ
- القَمْحِيُّ: صِفَةٌ مَرْفُوعَة،ٌ وعلامَةُ رَفْعِها الضَّمَّةُ الظَّاهِرَةُ
- لي: اللام، حَرْفُ جر. والياء، ضمير متصلِّ مَبْنِي على السكون فِي مَحَلِّ جرّ بِحَرْفِ الجر. مُتَعَلقَانَ بِخَبَرٍ مَحْذُوف.
- لا تَقْتُلوها: لا، حَرْفٌ جازمٌ تَقْتُلوها، فِعْلٌ مُضَارِعٌ مَجْزُوم، وعلامَةُ جَزْمِهِ حَذْفُ النُّونِ لَأَنَّهُ مِنَ الْأَفْعَالِ الخَمْسَة.ِ والواو، ضميرٌ مُتَّصِلِّ مَبْنِي على السُّكُون في مَحَلِّ رَفْع، فاعل. وها، ضميرٌ مُتَصِلِّ مَبْنِي على السُّكُونِ فِي مَحَلِّ نَصْب،ِ مَفْعُول به.
- واقْتُلُوني: الواو، حَرْفُ عَطْفٍ اقْتُلُونِي، فِعْلُ أَمْرٍ مَبْنِي على حَذْفِ النُّون،ِ لَأَنَّ مُضَارِعَهُ مِنَ الْأَفْعَالِ الخَمْسَة.ِ والواو، ضمير مُتَّصِلِّ مَبْنِي على السُّكُونِ فِي مَحَلِّ رَفْع،ِ فَاعِلٌ والنُّون، حَرْفُ وقاية. والياء، ضمير مُتَّصِلِّ مَبْنِي على السُّكُونِ فِي مَحَلِّ نَصْب،ِ مَفْعُولُ بِهِ

=== BLOCK 3: إعراب الجمل (Matrix) ===
(Component: TEMPLATE_C_TABLE.html)
[BLOCK_TITLE]: إعراب الجمل
Table Headers: الجملة | إعرابها
Row 1: جُمْلَةً (أَمْرٌ بِإِطلاق الرصاص) | استئنافية، لا محل لها مِنَ الإعراب.
Row 2: جُمْلَهُ (يَجْتَازُ) | صِلَةُ المَوْصُولِ، لا محل لها مِنَ الإعراب
Row 3: جُمْلَةُ (هَذَا الجِسْرُ مِقْصَلَةُ الذي ما زالَ يَحْلُم) | استئنافية، لا محل لها من الإعراب
Row 4: جمله (ما زَالَ يَحْلُمُ) | صِلَةُ المَوْصُول، لا مَحَلَّ لَهَا مِنَ الإعراب.
Row 5: جُمْلَةُ (يَحْلُمُ) | خَبَرَيَّة،ٌ مَحَلُّهَا النَّصْبُ
Row 6: جُمْلَةُ (الطَّلقةُ الأُولَى أَزَاحَت) | استئنافية، لا مَحَلَّ لها مِنَ الإعراب. الرَّفْع.ُ
Row 7: جُمْلَةً (أَرَاحَتْ) | خَبَرَيَّة،ٌ مَحَلُهَا الرَّفْعُ
Row 8: جملة (الطلقةُ الأُخْرَى أَصَابَتْ) | مَعْطُوفَة،ٌ لَا مَحَلَّ لها مِنَ الإعراب
Row 9: جُمْلَةُ (أَصَابَتْ) | خَبَرَيَّة،ٌ مَحَلَّهَا الرَّفْعُ
Row 10: جملة (الشيخ يَأْخُذُ) | استئنافية، لا محل لها من الإعراب
Row 11: جُمْلَةً (يَأْخُذُ) | خَبَرَيَّة،ٌ مَحَلُّها الرفع.
Row 12: جُمْلَةً (يَتْلُو) | مَعْطُوفَة،ٌ مَحَلُّهَا الرَّفْعُ
Row 13: جَمْلَهُ (قَالَ) | مَحَلَّهَا النَّصْب.ُ استئنافية، لا محل لها مِنَ الإعراب
Row 14: جملة (عَيْنَا حبيبتي الصغيرة لي يا جنود، ووَجْهُهَا القَمْحِيُّ لِي لا تَقْتُلُوهَا وَاقْتُلُونِي) | مَفْعُولُ بِه،ِ مَقُولُ القَوْلِ.
Row 15: جُمْلَةً (عَيْنَا حبيبتي الصغيرة لي) | ابتدائية، لا محل لها مِنَ الإعراب
Row 16: جملة (وجهها القَمْحِيُّ لِي) | مَعْطُوفَة،ٌ لَا مَحَل لها مِنَ الإعراب.
Row 17: جملة (لا تَقْتُلوها) | استئنافية، لا محل لها مِنَ الإعراب .
Row 18: جُمْلَةُ (اقْتُلُونِي) | مَعْطُوفَة،ٌ لا محل لها مِنَ الإعراب.

=== BLOCK 4: إعرابُ الْمَقْطَعِ الثَّالِثِ ===
(Component: TEMPLATE_C_IRAB.html)
[BLOCK_TITLE]: إعرابُ الْمَقْطَعِ الثَّالِثِ:
Content:
- وبرغم: الواو، حرف استِثْنَافِ الباء، حَرْفُ جر. رغم اسم مجرورٌ
- أَنَّ: حَرْفٌ مُشَبَّهُ بِالفِعْلِ
- القَتْلَ: اسم (أنَّ).
- كالتدخين: الكاف، حَرْفُ جر. التدخين، اسم مجرور، وعلامَةُ جَرَهِ الكَسْرَةُ الظَّاهِرَةُ والجَارُ وَالمَجْرُورُ مُتَعَلّقان بِخَبَرِ مَحْذُوف.ِ والمَصْدَرُ الْمُؤَوَّلُ (أَنَّ القَتْلَ كالتدخين)، في محل جر، مُضَاف إليه.
- لكِنَّ: حَرْفٌ مُشَبَّهُ بِالفِعْلِ
- الجُنُودَ: اسمُ لَكِنَّ مَنْصُوبُ
- الطَّيبين: صِفَةً مَنْصُوبَة،ٌ وعلامَةُ نَصْبِها الياء؛ لِأَنَّهَا جَمْعُ مُذَكَّر سالم. والنُّون، عوض عَنِ التنوين في الاسم المُفْرَدِ
- الطَّالِعِينَ: صِفَةٌ مَنْصُوبَة،ٌ وعلامَةُ نَصْبِهَا الياء؛ لِأَنَّهَا جَمع مذكر سالم والنون، عوض عَنِ التنوين في الاسم المفردِ
- دَفْتَرِ: مُضَاف إليهِ مَجْرُورٌ
- قَذَفَتْهُ: فِعْلِّ مَاضِ مَبْنِي على الفَتْحَةِ؛ لاتِصَالِهِ بِنَاءِ التَّأْنيثِ السَّاكِنَة.ِ والنَّاء،ُ حَرْفُ تَأْنيثٍ لَا مَحَلَّ لَهُ مِنَ الإعراب والهاء، ضمير مُتَصِلِّ مَبْنِي على الضَّمَّةِ فِي مَحَلِّ نَصْب،ِ مَفْعُولُ بِهِ
- أَمْعَاءُ: فَاعِلْ مَرْفُوعٌ
- السنين: مُضَافُ إليهِ مَجْرُور، وعلامَةُ جَرَهِ الياء؛ لأَنَّهُ مُلْحَقِّ بِجَمْعِ الْمُذَكَرِ السَّالِمِ.
- لم يَقْتلوا: لَم حَرْفٌ جَازِمٌ يَقْتُلُوا فِعْلَ مُضَارِع مجزوم، وعلامَةُ جَزْمِهِ حَذْفُ النُّونِ لأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَة.ِ والواو، ضمير متصل مَبْنِي على السكون، فِي مَحَلِّ رَفْع،ِ فاعل والآلِفُ حَرْفُ تفريق
- الاثنين: مَفْعُولُ بِهِ مَنْصُوب،ُ وعلامَةُ نَصْبِهِ اليَاءُ لَأَنَّهُ مُلْحَقِّ بالمثنى
- كانَ: فعل ماض ناقص، مَبْنِي على الفَتْحَةِ الظَّاهِرَةِ
- الشَّيْخ: اسم (كانَ) مَرْفُوعُ
- النَّهْرِ: مُضَاف إليهِ مَجْرُور.ٌ
- والبِنْتُ: الواو، حَرْفُ عَطْفٍ . البنت، مُبْتَداً مرفوع
- التي: اسم مَوْصُولٍ مَبْنِي على السكون فِي مَحَلِّ رَفْع،ِ صِفَةٌ،
- صَارَتْ: فِعل ماض ناقص مَبْنِي على الفَتْحَةِ لِاتِصَالِهِ بِتَاءِ التأنيث السَّاكِنَة.ِ والنَّاء،ُ حَرْفُ تَأْنيثٍ لا مَحَلَّ لَهُ مِنَ الإعراب.
- يتيمة: خَبر (صار) مَنْصُوب، وعلامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَة.ُ وسُكِنَ لِلضَّرورة الشَّعْرِيَّة.ِ
- كانَتْ: فعل ماض ناقِصٌ، مَبْنِي عَلَى الفَتْحَةِ؛ لاتِصَالِهِ بِتَاءِ التَّانيثِ السَّاكِنَةِ وَالنَّاء،ُ حَرْفُ تَأْنيثٍ لا مَحَلَ لَهُ مِنَ الإعراب.
- مُمَزَّقَةَ: خَبَرُ (كانَ) مَنْصُوبُ
- الثِّيَابِ: مُضَافُ إِلَيْهِ مَجْرُورٌ
- عِطْرُ: فَاعِلْ مَرْفُوعٌ
- الياسمين: مُضَاف إليهِ مَجْرُور،ٌ وعلامَةُ جَرَهِ الكَسْرَةُ الظَّاهِرَة.ُ وسُكِنَ لِلضَّرورة الشَّعْرِيَّةِ

=== BLOCK 5: إعراب الجمل (Cut Content Start) ===
(Component: TEMPLATE_CUT_BOX_PART_1.html wrapping TEMPLATE_C_TABLE.html)
[BLOCK_TITLE]: إعراب الجمل
Table Headers: الجملة | إعرابها
Row 1: جملة (لكن الجنود ... لم يقتلوا) | استئنافية، لا محل لها مِنَ الإعراب
Row 2: جُمْلَةً (لم يَقْتُلوا) | خَبَرِيَّةٌ، مَحَلُّهَا الرَّفْعُ
Row 3: جَمْلَهُ (قَذَفَتْهُ أَمْعَاءُ السَّنِينَ) | صِفَة،ً محلها الجر.
Row 4: جملة (كانَ الشَّيْحُ يَسْقُط) | استئنافية، لا محل لها مِنَ الإعراب .
Row 5: جُمْلَةً (يَسْقُط) | خَبَرِيَّةٌ، مَحَلَّهَا النَّصْب.
Row 6: جُمْلَةُ (البِنْتُ ... كانَتْ) |

--- END STREAM ---
