# **SESSION 121**

[TASK DEFINITION]
Objective: Implement page 121.
File: `pages/page_121.html` (Note: Use the exact page number.)
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
[LESSON_NUMBER]: 121
[CHAPTER_TITLE]: page 121
[CATEGORY_HEADER]: 121
[SECTION_HEADER]: 121
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: نشاط القراءة ===
(Component: TEMPLATE_C_BLOCK.html)
Title: نشاط القراءة
Content: <span class="text-accent">- اقرأ الأَسْطُرَ الآتية، ثُمَّ نَفِّذِ النشاط الذي يليها :</span>

=== BLOCK 3: القصيدة ===
(Component: TEMPLATE_C_POEM.html)
- لم يَعْرِفُوا أَنَّ الطَّرِيقَ إِلَى الطَّرِيقِ # دَمٌ، وَمِصْيَدَةٌ، وَبِيْدُ
- كُلُّ القوافِلِ قَبْلَهُمْ غَاصَتْ # وكانَ النَّهْرُ يَبْصُقُ ضِفَتَيْهِ
- حَرَسُ الْحُدُودِ مُرابطٌ # وهِجْرَةُ الدَّمِ في مِيَاهِ النَّهْرِ تَنْحَتُ
- من حصى الوادي تماثيلًا # لَهَا لَوْنُ النُّجُوم

=== BLOCK 4: الجمل الاسمية (Table) ===
(Component: TEMPLATE_C_TABLE.html)
Title: استخرج الجمل الاسمية الواردة فِي الأَسْطُرِ السَّابِقَةِ، وَاذْكُرْ نَوْعَ رُكْنَيْ كُلٍّ مِنْهَا .
Headers: الجملة الاسمية | الركن الأول | نوعه | الركن الثاني | نوعه
Row 1: أن الطريق ... دم | الطريق | اسم | دم | مفرد
Row 2: كل القوافل قبلهم غاصت | كل | اسم | (غاصت) | جملة فعلية
Row 3: حرس الحدود مرابط | حرس | اسم | مرابط | مفرد
Row 4: هجرة الدم ... تنحت | هجرة | اسم | (تنحت) | جملة فعلية
Row 5: لها لون النجوم | لون | اسم | لها | شبه جملة

=== BLOCK 5: قاعدة الإبدال ===
(Component: TEMPLATE_C_LIST.html)
Title: اشْرَحْ قَاعِدَةَ الإِبْدَالِ فِي الكَلِمَاتِ التي تحتها خط فيما يأتي: (كانوا ثلاثة عائدين ... وَبَعْدَ دَقَائِقَ يَصِلُّونَ: هل في البيت ماء؟)
List Items:
- <span class="highlight-red font-bold">عائدين</span>: إبدال، أُبْدِلَتِ الواوُ هَمْزَةً؛ لِأَنَّهَا وَقَعَتْ عَيْناً فِي صِيغَةِ اسمِ الفاعِلِ المَصُوغِ مِنَ الْفِعْلِ الثَّلاثيِّ الْأَجْوَفِ.
- <span class="highlight-red font-bold">دقائق</span>: إبدال، أُبْدِلَتِ اليَاءُ هَمْزَةً؛ لِأَنَّهَا وَقَعَتْ بَعْدَ أَلِفِ صِيغَةِ مُنْتَهَى الجُمُوعِ.

=== BLOCK 6: قاعدة التاء ===
(Component: TEMPLATE_C_LIST.html)
Title: اشْرَحْ قَاعِدَةَ كِتَابَةِ التَّاءِ المربوطة والمُبْسُوطَةِ فِي الكَلِمَاتِ الآتية: (غاصَتْ، قبعة، الصَّمْت).
List Items:
- <span class="highlight-red font-bold">غاصَتْ</span>: كُتِبَتِ التَّاءُ مبْسُوطَةً؛ لِأَنَّهَا تَاءُ التَّأْنِيثِ السَّاكِنَةُ.
- <span class="highlight-red font-bold">قَبَعَة</span>: كُتِبَتِ التَّاءُ مَرْبُوطَةً؛ لِأَنَّهَا جَاءَتْ فِي اسمٍ مُفْرَدٍ مُؤَنَّثٍ.
- <span class="highlight-red font-bold">الصَّمْتُ</span>: كُتِبَتِ التَّاءُ مَبْسُوطَةً؛ لِأَنَّهَا مِنْ أَصْلِ الاسمِ، أو: كُتِبَتْ مَبْسُوطَةً؛ لأنها جاءَتْ في اسمٍ ثلاثيٍّ ساكنِ الوَسَطِ.

=== BLOCK 7: إعراب النص ===
(Component: TEMPLATE_C_IRAB.html)
Title: إعراب النص (إعْرَابُ المقطع الأَوَّلِ)
Words:
- مشيا: حالٌ مَنْصُوبة.
- أو زَحْفًا: أو: حَرْفُ عَطْفٍ، زَحْفًا: اسمٌ مَعْطُوفٌ مَنْصُوبٌ.
- وكان: الواو: واو الحال، كان: فعل ماض ناقص، مَبْنِي على الفَتْحَةِ الظَّاهِرَةِ.
- الصَّخْرُ: اسم (كانَ) مَرْفُوع.
- والمَسَاءُ: الواو: حَرْفُ عَطْفٍ، المَسَاءُ: اسم (كانَ) المَحْذُوفة مَرْفُوعٌ.
- يَدًا: خَبَرُ (كَانَ) الْمَحْذُوفة مَنْصُوبٌ.
- لَمْ يَعْرِفُوا: لَمْ: حَرْفٌ جازمٌ، يَعْرِفُوا: فعل مُضارع مجزوم، وعلامَةُ جَزْمِهِ حَذْفُ النُّونِ؛ لِأَنَّهُ مِنَ الْأَفْعَالِ الخَمْسَةِ. والواو: ضميرٌ مُتَّصِل مبني على السُّكُونِ، فِي مَحَلِّ رَفْعٍ فَاعِل، والآلِفُ حَرْفُ تَفريق.
- أَنَّ الطَّريق: أَنَّ: حَرْفٌ مُشَبَّه بالفعل، الطريق: اسم (أَنَّ) مَنْصُوبٌ. وَالْمَصْدَرُ المؤولُ (أَنَّ الطَّرِيقَ دَمٌ)، في مَحَلِّ نَصْبٍ، مَفْعُولَ بِهِ.
- دم: خَبَرٌ مَرْفُوع.
- ومِصْيَدَةٌ: الواو: حَرْفُ عَطْفٍ، مِصْيَدَةٌ: اسمٌ مَعْطُوفٌ مَرْفُوع.
- وبيدُ: الواو: حَرْفُ عَطْفٍ، بِيدُ: اسِمٌ مَعْطُوفٌ مَرْفُوعٌ.
- كُلُّ: مُبْتَدَأٌ مَرْفُوعٌ.
- القوافِلِ: مُضَافٌ إليهِ مَجْرُورٌ.
- قَبْلَهُمْ: مَفْعُولُ فِيهِ ظَرْفُ زَمَانٍ مَنْصُوبٌ.
- وكان: الواو: واو الحال، كان: فعل ماض ناقص مبني على الفَتْحَةِ الظَّاهِرَةِ.
- النَّهْرُ: اسم (كانَ) مَرْفُوعٌ.
- ضِفَتَيْهِ: مَفْعُولُ بِهِ أَوَّلٌ مَنْصُوبٌ، وعلامَةُ نَصْبِهِ الياء؛ لِأَنَّهُ مُثَنَّى، وحُذِفَتِ النُّونُ لِلإِضافة. والهاء: ضمير مُتَّصِلٌ مَبْنِي على الكَسْرَةِ فِي مَحَلِّ جَرٍّ، مُضَافٌ إليه.
- قِطَعًا: مَفْعُولُ بِهِ ثَانٍ مَنْصُوبٌ.
- المُفَتَتِ: صِفَةٌ مَجْرُورَةٌ.
- العَائِدِين: مُضَافٌ إِلَيْهِ مَجْرُورٌ، وعلامة جره الياء؛ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سالم. والنُّونُ: عوض عَنِ التنوين في الاسم المَفْرَدِ.
- كَانُوا: فعل ماضٍ ناقص، مَبْنِيٌّ على الضَّمَّةِ؛ لاتصاله بواو الجماعة، والواو: ضمير مُتَّصِلٌ مَبْنِي على السكون فِي مَحَلِّ رَفْعٍ، اسم (كَانَ). والأَلِفُ: حَرْفُ تفريق.
- ثلاثة: خَبَرٌ مَنْصُوبٌ.
- عَائِدِينَ: مُضَافٌ إِلَيهِ مَجْرُور، وعلامَةُ جَرَهِ الياء؛ لِأَنَّهُ جَمْعُ مُذَكَّر سالم. والنُّون: عوض عَنِ التنوين في الاسم المفرد.
- شيخ: خبر لمبتدأ محذُوفٍ مَرْفُوعٌ.
- وَابْنَتُهُ: الواو: حَرْفُ عَطْفٍ، ابْنَتُهُ: اسم معطوف مرفوع والهاء: ضمير مُتَّصِلٌ مَبْنِي عَلَى الضَّمَّةِ فِي مَحَلِّ جَرٍّ، مُضَافٌ إليه.
- وجُنْدِي: الواو: حَرْفُ عَطْفٍ، جُنْدِي: اسمٌ مَعْطُوفٌ مَرْفُوعٌ.
- قَديم: صِفَةٌ مَرْفُوعَةٌ، وعلامَةُ رَفْعِهَا الضَّمَّةُ الظَّاهِرَةُ. وَسُكِّنَتْ لِلضَّرورة الشَّعْرِيَّةِ.
- يَقِفُونَ: فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وعلامَةُ رَفْعِهِ ثُبُوتُ النونِ، لِأَنَّهُ مِنَ الْأَفْعَالِ الخَمْسَةِ. والواو: ضَمِيرٌ مُتَصِلٌ مَبْنِي على السُّكُونِ فِي مَحَلِّ رفعٍ، فَاعِلٌ.
- عِنْدَ: مَفْعُولُ فِيهِ ظَرْفُ مَكَانٍ مَنْصُوبٌ.
- الجسر: مُضَاف إليه مجرور.
- كان: فعل ماض ناقص، مبني على الفتحة الظاهرة.
- الجسر: اسم (كانَ) مَرْفُوعٌ.
- نَعْسَانًا: خَبَرُ (كَانَ) منصوب.
- وكان: الواو: حَرْفُ عَطْفٍ، كَانَ: فِعْلٌ مَاضٍ ناقص، مَبْنِي على الفَتْحَةِ الظَّاهِرَةِ.
- اللَّيْلُ: اسم (كانَ) مَرْفُوعٌ.
- قَبْعَةَ: خَبَرُ (كان) منصوب.
- وبعد: الواو: حَرْفُ استئنافٍ، بَعْدَ: مَفْعُولُ فِيهِ ظَرْفُ زَمَانٍ مَنْصُوبٌ.
- دَقَائِقٍ: مُضَافٌ إِلَيْهِ مَجْرُورٌ.
- يَصِلُونَ: فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وعلامَةُ رَفْعِهِ ثُبُوتُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الخمسة. والواو: ضمير مُتَّصِلٌ مَبْنِي على السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.

--- END STREAM ---
