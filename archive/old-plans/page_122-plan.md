# **SESSION 122**

[TASK DEFINITION]
Objective: Implement page 122.
File: `pages/page_122.html`
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
[LESSON_NUMBER]: 122
[CHAPTER_TITLE]: page 122
[CATEGORY_HEADER]: 122
[SECTION_HEADER]: 122
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: [No Title] ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
(Target Component: TEMPLATE_C_IRAB.html)
Title:
Content:
مَبْنِي الشَّعْرِيَّةِ ثُمَّ حَرْفُ عَطْف. تلا: فعل ماض، رَفْعِهِ الصَّمَّةُ الظَّاهِرَة.ُ وسُكِنَ لِلضَّرُورَةِ هَلْ حَرْفُ استفهام. مَاءً : مُبْتَداً مُؤَخَرٌ مَرْفُوع، وعلامةُ
في
لِلضَّرُورَةِ الشَّعْرِيَّةِ الشَّيخ: بِهِ مَنْصُوب، وعلامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَة،ُ وَسُكِّنَ على الفَتْحَةِ المُقَدَّرة على الأَلِف،ِ مَنَعَ ظُهُورَهَا التَّعَذِّر.ُ آية : مَفْعُولُ
مَنْزِل:ِ مِنْ حَرْفُ جَةٍ مَنْزِل،ِ خَبَرَيَّةٌ مَبْنِيَّةٌ على السُّكُونِ فِي مَحَلِ رَفْع،ِ مُبْتَدا.ً مِنْ فاعِلَ مَرْفُوعُ مُنْتَعِشا: حال منصوبة. وكَم:ْ الواو: زائدَةً كَمْ
مِنَ المنازِلِ كَائِنٌ مُتَعَلِّقان بحالِ مَحْدُوفَةٍ لـ )كم( ]التَّقْدِير : عَدَدٌ كَثِير حال كونه اسم مجرور، وعلامَةُ جَرَهِ الكَسْرَةُ الظَّاهِرَة.ُ والجار والمَجْرُورُ
على السكون فِي مَحَلَّ نَصْب،ِ مَفْعُولُ بِهِ الفَتَى: رَفْعِهِ الضَّمَّةُ الظَّاهِرَة،ُ وَالهاء، ضمير متصل مَبْنِي الأَرْضِ[ . يَأْلَهُ فِعْلَ مُضَارِعٌ مَرْفُوع، وعلامَةُ
مُشَبَّهُ بِالفِعِلِ الْمَنَازِلَ : اسم )لَكِنَّ( مَنَعَ ظُهُورَهَا التَّعَذِّر.ُ ولَكِنَّ الواو : زائدةً لَكِنَّ حَرْفٌ فاعِلْ مَرْفُوع، وعلامَةً رَفْعِهِ السَّمَةُ المُقَدَّرَةُ على الأَلِفِ
على ما قَبْلَ ياءِ الْمُتَكَلِم،ِ مَنَعَ ظُهُورَهَا اسْتِقَالُ الْمَحَلِّ منصوب يا أبي: يا، أَدَاةُ نِدَاء.ِ أبي، مُنَادى مُضَافُ مَنْصُوب، وعلامَةُ نَصْبِهِ الفَتْحَةُ المُقَدَّرَةُ
فَأَجَابَ : الفَاء،ُ حَرْفُ اسْتِثْنَافِ أَجاب، في محل جر، مُضَاف إليه. اطلال : خَبَرَ مَرْفُوعٌ بالحركة المناسبة. والياء، ضمير متصل مَبْنِي على السكون

=== BLOCK 3: [No Title] ===
(Component: TEMPLATE_C_IRAB.html)
Title:
Content:
الياء، مَنَعَ ظُهُورها التقل. وها، ضمير مُصَارِعٌ مَرْفُوع، وعلامَةُ رَفْعِهِ الصَّمَةُ المُقَدَّرَةُ على فعل ماض، مَبْنِي على الفَنْحَةِ الظَّاهِرَة.ِ تبنيها: فِعْلَ
لأَنَّهُ مُتَتَّى، والنُّون عوض عَنِ التنوين في الاسم بِهِ يَدَان: فاعل مَرْفُوع، وعلامَةُ رَفْعِهِ الأَلِفُ؛ مُتَّصِلِّ مَبْنِي على السكون في مَحَلَ نَصْب،ِ مَفْعُولُ
حديثة: مَفْعُولُ مُضَارِعٌ تجزوم، وعلامَةُ جَزْمِهِ السُّكُونُ الْمُقَدَّرُ بِسَبَبِ التَّضْعيف. المفرد. ولم يتم الواو، حَرْفُ استناف. لم، حَرْفٌ جازم. يُتِم،َّ فعل
السُّكُون في مَبْنِي على الضَّمَّة في محل جر، مُضَاف إليه. إِذ:ْ اسمٌ مَبْنِي على به منصوب، وعلامةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَةُ والهاء، ضميرٌ مُتَصِلِّ
لَأَنَّ مُصَارِعَهُ مِنَ الْأَفْعَالِ مَحَلَ نَصْب،ِ مَفْعُولُ فِيهِ ظَرْفُ زَمَانِ بمعنى حِينَ(. صَوْت:ُ فَاعِلَ مَرْفُوعٌ تَعَالوا : فِعْلُ أَمْرٍ مَبْنِي على حَذْفِ النُّونِ
والآلِفُ حَرْفُ تفريق. وتَلَتْهُ الواو، حَرْفُ عَطْفٍ تَلَتْه،ُ فِعْلَ مَاض،ِ الخمسة. والواو، ضمير مُتَصِلِّ مَبْنِي على السُّكُون فِي مَحَلِ رَفْع،ِ فَاعِلٌ
تَأْني لا مَحَنَّ لَهُ مِنَ الإعراب. لِاتِصَالِهِ بِتَاءِ التَّأْنيثِ السَّاكِنَة.ِ والنَّاء،ُ حَرْفُ مَبْنِي على الفَتْحَةِ المُقَدَّرة على الألف الْمَحْذُوفَةِ؛
مَرْفُوع، وعلامَةُ رَفْعِهِ مُضَارِعٌ مَنْصُوبُ العَاندون : فاعل يَجْرُورٌ لَنْ يَمُر:َّ لَنْ حَرْفٌ نَاصِب.ُ يمر، فِعْلَ طَقَطَقَةً : فَاعِلَ مَرْفُوعُ الْبَنَادِق:ِ مُضَافُ إِلَيهِ
الحُدُودِ : مُضَافَ إِلَيهِ مَجْرُورٌ مُرَابِ : خَبَرٌ مَرْفُوع.ٌ التنوين في الاسم المفرد. حَرَسُ : مُبْتَداً مَرْفُو الواو؛ لِأَنَّهُ جَمع مذكر سالم والتون عوض عَنِ
التَّقَلُ الحُدُودَ : مَفْعُولُ بِهِ مَنْصُوبٌ جُمْلَهُ مَشْيَّا على الأَقْدَام يحمي: فِعْلَ مُضارع مَرْفُوع، وعلامَةُ رَفْعِهِ الضَّمَةُ المُقَدرة على الياء، مَنَعَ ظُهُورَهَا

=== BLOCK 4: [No Title] ===
(Component: TEMPLATE_C_TABLE.html)
Title:
Content:
كَانَ الصَّحْرُ )قالُوا(: ابتدائية، لا محل لها مِنَ الإعراب. جُمْلَهُ أو رَحْفًا على الأَيْدِي نَعُود(: مَفْعُولُ بِه،ِ مَحَلُّهَا النَّصْبُ مَقُولُ القَوْلِ(. جملة
جُمْلَةً )مْ يَعْرِفُوا : استئنافية، لا محل لها مَحَلُّهَا النَّصْبُ جملة )تقود(: صِفَة،ٌ مَحَلُّهَا النَّصْبُ يَضْمُرُ( : حاليَّة،ٌ مَحَلُّهَا النَّصْبُ جُمْلَةً يَضْمُرُ( : خَبَريَّة،ٌ
خَبَرَيَّة،ٌ مَحَلُّهَا الرَّفْع.ُ يُمْلَهُ كَانَ النَّهْرُ : استئنافية، لا محل لها مِنَ الإعراب جملة )غاصَتْ( : مِنَ الإعراب جملة )كُلُّ القَوافِلِ قَبْلَهُم غَاصَتْ(
لا محل لها مِنَ الإعراب. جُلْلَةً كَانَ مَحَلُّهَا النَّصْبُ جُمْلَةً )كانُوا ثلاثة عائدين(: استئنافية، يَبْصُق( : حاليَّة،ٌ مَحَلُّهَا النَّصْبُ جُمْلَهُ يَبْصُقُ( : خَرَيَّة،ٌ
لا لها مِنَ الإعراب جملة يصلونَ(: استثْنَافِيَّة،ٌ لجملة )كانَ اللَّيْلُ قَبَّعَةٌ( : مَعْطُوفَة،ٌ لَا مَحَلَّ الجِسْرُ نَعْسَانًا( استئنافية، لا محل لها مِنَ الإعراب
تَحَسَّسَ(: النَّصْبُ جُمْلَةً تَحَسَّسَ( : استِثْنَافِيَّة،ٌ لا تحل لها مِنَ الإعراب جُمْلَةٌ محل لها مِنَ الإعراب جملة هل في البيت ماء : مَفْعُولُ بِه،ِ مَحَلَّهَا
. جُمْلَةً جُمْلَةُ قَالَ الشَّيْخ : استئنافية، لا محل لَهَا مِنَ الإعراب استئنافية، لا محل لها مِنَ الإعراب جملة )تلا( : مَعْطُوفَة،ٌ لَا مَحَكَ لها مِنَ الإعراب
يألَفُهُ الفتى( : مَفْعُولُ بِه،ِ مَحَلُّهَا النَّصْبُ مَقُولُ لها مِنَ الإعراب جملة )وَكَمْ مِنْ مَنْزِلِ فِي الْأَرْضِ وكَمْ مِنْ مَنْزِلٍ فِي الأَرْضِ : ابتدائية، لا محل
يَا أَبِي أَطَلَالٌ : مَفْعُول استنافية، لا محل لها مِنَ الإعراب جملة ولكن المنازِلَ القول(. جُمْلَةً يَأْلُفُهُ الفَتَى( : صِفَة،ٌ مَحَلَّها الجر. جُمْلَةً قَالَتْ( :
بِه،ِ حَلَّهَا النَّصْبُ مَقُولُ لا محل لها مِنَ الإعراب جملة تبنيها يَدَانِ(: مَفْعُولُ بِه،ِ مَحَلُّهَا النَّصْبُ مَقُولُ القَوْلِ(. جُجْلَةُ أَجَابَ(: استئنافية،
بِه،ِ مَحَلَّهَا النَّصْبُ صَوْت(: إضافِيَّة،ٌ مَحَلَّها الجر. جملَةً تَعَالوا : مَفْعُولُ القول(. جملة لم يتم(: استئنافية، لا محل لها مِنَ الإعراب جُمْلَةُ صَاحَ
مَقُولُ القَوْلِ(. جُلَةً )لَتْهُ طَقْطَقَةُ البَنَادِقِ( : مَعْطُوفَة،ٌ مَحَلُّها الجر. لَمْلَةً لَنْ يَمر العاندونَ(: استئنافية، لا محل لها مِنَ الإِعراب جُمْلَةٌ حَرَسُ
الحدُودِ مُرَابِ ( : استئنافية، لا محل لها مِنَ الإعراب جُمْلَةُ يَحْمِي( : خَبَرَيَّة،ٌ مَحَلَّهَا الرَّفْع.ُ

=== BLOCK 5: إعراب المقطع الثاني ===
(Component: TEMPLATE_C_IRAB.html)
Title: إعراب المقطع الثاني:
Content:
أَمْرُ خَيْرٌ لِمُبْتَنَا مَحْذُوفٌ مَرْفُوعَ الرَّصَاص:ِ مُضاف إليهِ مَجْرُور على حرف جر. الذي: اسمٌ مَوْصُولُ مَبْنِي على السُّكُون، فِي مَحَلِّ جَرٍ بِحَرْفِ
الجر. هَذَا : الهَاء،ُ حرف تنبيه. ذا، اسم إشارةٍ مَبْنِي على السُّكُونِ فِي مَحَلَ نَصْب،ِ مَفْعُولُ بِهِ الْجِسْرَ بَدَلَّ مِنِ اسم الإِشَارَةِ مَنْصُوبُ هَذَا الهَاء،ُ
حَرْفُ تنبيه ذا، اسم إشارة مَبْنِي على السكون فِي مَحَلِ رَفْع، مبتداً الجسر : بَدَلَّ مِنِ اسم الإشارةِ مَرْفُوعُ مِقْصَلَهُ خَبَرَ مَرْفُوعٌ الذي: اسم
مَبْنِي على الفَتْحَةِ الظَّاهِرَةِ الطلقة: مُبْتَداً مَرْفُوع الأولى: مَوْصُولُ مَبْنِي على السكون، في حل جة،ٍ مُضَاف إليه. ما زال : فعل ماض ناقص
: إليهِ يَجْرُورٌ فَبَّعَةَ مَفْعُولُ بِهِ مَنْصُوبُ الظَّلَامُ الأَلِفِ مَنَعَ ظُهُورَهَا التَّعَذُرُ اللَّيل: مُضَاف صفَةٌ مَرْفُوعَة،ٌ وعلامَةُ رَفْعِهَا الضَّمَّةُ المُقَدرة على
الْأُخْرَى صِفَةٌ حَرْفُ عَطْفٍ الطَّلقَة،ُ مُبْتَداً مَرْفُوعُ وسُكْنَ لِلضَّرورة الشَّعْرِيَّة.ِ والطلقة: الواو، مُضَاف إليهِ مَجْرُور، وعلامَةُ جَرَهِ الكَسْرَةُ الظَّاهِرَة.ُ
الظَّاهِرَةُ قَديم: صفة تجزورة، وعلامة جَرِّهَا الكَسْرَةُ مُصَافَ إِلَيهِ يَجْرُور،ٌ وعلامَةُ جَبِّهِ الكَسْرَةُ الظَّاهِرَةُ مَرْفُوعَةٌ قَلْبَ مَفْعُولُ بِهِ مَنْصُوبُ جُنْدِي:
AAL
مكتة

--- END STREAM ---
