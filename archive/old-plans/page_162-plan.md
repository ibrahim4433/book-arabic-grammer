# **SESSION 162**

[TASK DEFINITION]
Objective: Implement page 162.
File: `pages/page_162.html`
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
    *   `class="w-20pct"` (instead of `style="width: 20%"`)
    *   `class="mt-2mm"` (instead of `style="margin-top: 2mm"`)
    *   `class="text-center"` (instead of `style="text-align: center"`)
    *   `class="font-bold"` (instead of `style="font-weight: bold"`)
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
[LESSON_NUMBER]: 162
[CHAPTER_TITLE]: page 162
[CATEGORY_HEADER]: 162
[SECTION_HEADER]: 162
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Irab Continuation ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[BLOCK_TITLE]: إعراب
[CONTENT]:
<div class="flex flex-col gap-2mm">
    <div class="irab-box" id="b16202">
        <div class="irab-word">البَيْنِ</div>
        <div class="irab-details">مُضَافٌ إِلَيْهِ مَجْرُورٌ</div>
    </div>
    <div class="irab-box" id="b16203">
        <div class="irab-word">أَشَدْ</div>
        <div class="irab-details">مَفْعُولُ بِهِ ثَانٍ مَنْصُوب، وعلامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَة،ُ وسُكِّنَ لِلضَّرورة الشعْرِيَّة.ِ</div>
    </div>
    <div class="irab-box" id="b16204">
        <div class="irab-word">جملة )رَضِيتُ(</div>
        <div class="irab-details">استئنافيَّة،ٌ لَا محل لها من الإعراب</div>
    </div>
    <div class="irab-box" id="b16205">
        <div class="irab-word">جملة )وَجَدَتْنِي ... أَشَدْ(</div>
        <div class="irab-details">صِفَة،ٌ مَحَلَّهَا الرَّفْع.ُ</div>
    </div>
</div>

=== BLOCK 3: Poem Verse 9 ===
(Component: TEMPLATE_C_POEM.html)
Title: البيت التاسع
Poet:
Hemistich 1: ٩- فَتَجَشَّمْتُ العَنَا نَحْوَ الْمُنَى
Hemistich 2: وتَقَاضَانِي الغِنَى عُمْرًا نَفَدْ

=== BLOCK 4: Poem Analysis 9 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: التحليل
Content:
<div class="flex flex-col gap-2mm">
    <div class="text-accent"><b>المفردات:</b> تَجَشَّمْتُ: تَكَلَّفَتُ الأَمْرَ على مَشَقَّة. العنا: التعب. المنى: البُغْيَة. تَقَاضَانِي: تقاضاهُ الدَّيْن،َ قَبَضَهُ مِنْهُ. نَفَدْ: ذَهَبَ وَفَنِي.</div>
    <div class="text-accent"><b>الشرح:</b> فتكلَّفَتُ المَشَقَةَ وتحمَّلْتُ المَتَاعِبَ مِن أَجْلِ أَنْ أَبْلُغَ ما أَصْبُو إليه من مطالب وأَهداف، إِذْ يَتَطَلَّبُ مِنِي الْحُصُولُ على الغِنى أَنْ أُفْنِي عُمْرِي وأُذْهِبَه.ُ</div>
    <div class="text-accent"><b>البلاغة:</b> )العناء، المنى، الغنى(: جناس ناقص. )تَقَاضَانِي الغنى(: استعارة مَكْنِيَّة.ٌ</div>
</div>

=== BLOCK 5: Idea Benefit Box (Orange Component) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[BENEFIT_TITLE]: الفكرة
[BENEFIT_CONTENT]: إفناء العُمْرِ فِي الغُرْبَةِ طَلَبًا لِلغِنى.

=== BLOCK 6: Irab Verse 9 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الإعراب
Content:
<div class="flex flex-col gap-2mm">
    <div class="irab-box" id="b16206">
        <div class="irab-word">فَتَجَشَّمْتُ</div>
        <div class="irab-details">الفاء استئنافية. تجشمت: فعل ماضِ مَبْنِي على السُّكُونِ لاتصاله بتاء الفاعل، والتاء ضمير متصل في محل رفع فاعل.</div>
    </div>
    <div class="irab-box" id="b16207">
        <div class="irab-word">العَنَا</div>
        <div class="irab-details">مَفْعُولُ بِهِ مَنْصُوبَ.</div>
    </div>
    <div class="irab-box" id="b16208">
        <div class="irab-word">نَحْوَ</div>
        <div class="irab-details">مَفْعُولُ فِيهِ ظَرْفُ مَكَانٍ مَنْصُوبُ.</div>
    </div>
    <div class="irab-box" id="b16209">
        <div class="irab-word">الْمُنَى</div>
        <div class="irab-details">مُضَافُ إِلَيهِ مَجْرُورٌ.</div>
    </div>
    <div class="irab-box" id="b16210">
        <div class="irab-word">وَتَقَاضَانِي</div>
        <div class="irab-details">الواو حَرْفُ عَطْف.ِ تقاضاني: فعل ماضِ مَبْنِي على الفَتْحَةِ المُقَدَّرَةِ على الأَلِف،ِ مَنَعَ ظُهُورَهَا التَعَذِّرُ. والنُّونُ حَرْفُ وقاية. والياء، ضميرٌ مُتَّصِلَ مَبْنِي على السُّكُونِ فِي مَحَلِّ نَصْب،ِ مَفْعُولُ بِهِ.</div>
    </div>
    <div class="irab-box" id="b16211">
        <div class="irab-word">الغِنَى</div>
        <div class="irab-details">فَاعِلٌ مَرْفُوعٌ.</div>
    </div>
    <div class="irab-box" id="b16212">
        <div class="irab-word">عُمْرًا</div>
        <div class="irab-details">مَفْعُولُ بِهِ مَنْصُوبٌ.</div>
    </div>
    <div class="irab-box" id="b16213">
        <div class="irab-word">نَفَدْ</div>
        <div class="irab-details">فِعْلَ مَاضِ مَبْنِي على الفَتْحَةِ الظَّاهِرَة.ِ وسُكِّنَ لِلضَّرُورَةِ الشَّعْرِيَّة.ِ</div>
    </div>
    <div class="irab-box" id="b16214">
        <div class="irab-word">جملة )تَجَشَّمْتُ(</div>
        <div class="irab-details">استئنافية، لا محل لها مِنَ الإعراب.</div>
    </div>
    <div class="irab-box" id="b16215">
        <div class="irab-word">جملة )تَقَاضَانِي الغنى(</div>
        <div class="irab-details">مَعْطُوفَة،ٌ لَا مَحَلَّ لَهَا مِنَ الإِعراب.</div>
    </div>
    <div class="irab-box" id="b16216">
        <div class="irab-word">جملة )نَفَدْ(</div>
        <div class="irab-details">صِفَة،ٌ مَحَلَّهَا النَّصْب.</div>
    </div>
</div>

=== BLOCK 7: Poem Verse 10 ===
(Component: TEMPLATE_C_POEM.html)
Title: البيت العاشر
Poet:
Hemistich 1: ١٠- هَلْ دَرَى الدَّهْرُ الذِي فَرَّقَنَا
Hemistich 2: أَنَّهُ فَرَّقَ رَوْحًا عَنْ جَسَدْ؟

=== BLOCK 8: Poem Analysis 10 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: التحليل
Content:
<div class="flex flex-col gap-2mm">
    <div class="text-accent"><b>الشرح:</b> يا تُرَى هَلْ أَدْرَكَ الدَّهْرُ الذِي عَمَدَ إِلى تفرِيقِنَا أَنَّهُ بِصَنِيعِهِ هَذَا تَسَبَّبَ بِنَزْعِ رُوحٍ عَنْ جَسَدِها؟!</div>
    <div class="text-accent"><b>الفِكْرَة:</b> تصوير قُوَّة الانتماء إلى الوطن.</div>
    <div class="text-accent"><b>البلاغة:</b> )دَرَى الدَّهْرُ(: استعارة مَكْنِيَّةٌ. )الدَّهْرُ فَرَّقَنَا(: استعارة مَكْنِيَّة.</div>
    <div class="text-accent"><b>الأساليب:</b> )هَلْ دَرَى الدَّهْرُ(: أسلوب استفهام، الأداة: هل. نَوْعُها: حرف.</div>
</div>

=== BLOCK 9: Irab Verse 10 Matrix ===
(Component: TEMPLATE_C_TABLE.html)
[TABLE_CONTENT]:
<table class="dense-table">
    <thead>
        <tr>
            <th>الكلمة / الجملة</th>
            <th>الإعراب</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>هل</td>
            <td>حَرْفُ استِفْهَامِ.</td>
        </tr>
        <tr>
            <td>الدَّهْرُ</td>
            <td>فَاعِلٌ مَرْفُوعٌ.</td>
        </tr>
        <tr>
            <td>الذي</td>
            <td>اسمٌ مَوْصُولُ مَبْنِي على السكون فِي مَحَلِّ رَفْع،ٍ صِفَةٌ.</td>
        </tr>
        <tr>
            <td>أَنَّه</td>
            <td>أَنَّ: حَرْفٌ مُشَبَّهٌ بالفعل. والهاء: ضمير مُتَّصِلٌ مَبْنِي على الضَّمَّةِ فِي مَحَلِّ نَصْب،ِ اسمها. والمَصْدَرُ الْمُؤَوَّلُ )أَنَّهُ فَرَّقَ( فِي مَحَلِّ نَصْب،ِ مَفْعُولُ بِهِ.</td>
        </tr>
        <tr>
            <td>رُوْحًا</td>
            <td>مَفْعُولُ بِهِ مَنْصُوبُ.</td>
        </tr>
        <tr>
            <td>عَنْ</td>
            <td>حَرْفُ جر.</td>
        </tr>
        <tr>
            <td>جسد</td>
            <td>اسم مَجْرُور.</td>
        </tr>
        <tr>
            <td>جملة )دَرَى الدَّهْرُ(</td>
            <td>استئنافية، لا محل لها من الإعراب.</td>
        </tr>
        <tr>
            <td>جملة )فَرَّقَنَا(</td>
            <td>صِلَةُ الْمَوْصُول،ِ لا مَحَلَّ لَهَا مِنَ الإعراب.</td>
        </tr>
        <tr>
            <td>جملة )فَرَّقَ(</td>
            <td>خَبَرِيَّة،ٌ مَحَلَّهَا الرَّفْع.ُ</td>
        </tr>
    </tbody>
</table>

=== BLOCK 10: Poem Verse 11 ===
(Component: TEMPLATE_C_POEM.html)
Title: البيت الحادي عشر
Poet:
Hemistich 1: ١١- وطني حتَّامَ تَرْتَدُّ الصَّبَا
Hemistich 2: دُونَ أَنْ تَحْمِلَ مِنْ سَلْمَايَ رَدْ؟

=== BLOCK 11: Poem Analysis 11 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: التحليل
Content:
<div class="flex flex-col gap-2mm">
    <div class="text-accent"><b>المفردات:</b> الصَّبا: رِيحٌ تَهُبُّ مِنْ مَشْرِقِ الشَّمْسِ.</div>
    <div class="text-accent"><b>الشرح:</b> وَطَنِي الحبيب، إلى متى أبقى أُحَمِّلُ رِيَاحَ الصَّبَا الْمُنْدَفِعَةَ نَحْوَ الشَّرْقِ رسائِلِي، وَأَنْتَظِرُ عَوْدَتَهَا، فتعود خالية الوفاضِ دُونَ أَنْ تَجْلِبَ لِي رَدًّا مِنْ مَحْبُوبَتِي.</div>
    <div class="text-accent"><b>الفكرة:</b> المعاناة بِسَبَبِ فِرَاقِ الأَحِبَّةِ وَالشَّوْقُ والحنين إليهم. )التَّعْبِيرُ عَنِ الحَسْرَةِ على انقطاع الوِصَالِ مَعَ الْمَحْبُوبَة(.</div>
    <div class="text-accent"><b>البلاغة:</b> أسلوب إنشاء طلبي نداء: )وَطَنِي(. أسلوب إنشاء طلبي استفهام: )حَتَّامَ تَرْتَدُّ(.</div>
</div>

=== BLOCK 12: Irab Verse 11 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الإعراب
Content:
<div class="flex flex-col gap-2mm">
    <div class="irab-box" id="b16217">
        <div class="irab-word">حَتَّامَ</div>
        <div class="irab-details">حَتَّى: حَرْفُ جر. ما: اسم استفهام مبني على السكون في محل جرٍ بِحَرْفِ الجر. مُتَعَلَّقان بالفِعْلِ )تَرْتَدُّ(.</div>
    </div>
    <div class="irab-box" id="b16218">
        <div class="irab-word">الصَّبَا</div>
        <div class="irab-details">فَاعِلٌ مَرْفُوعُ.</div>
    </div>
    <div class="irab-box" id="b16219">
        <div class="irab-word">دُونَ</div>
        <div class="irab-details">مَفْعُولُ فِيهِ ظَرْفُ زَمَانٍ مَنْصُوبُ.</div>
    </div>
    <div class="irab-box" id="b16220">
        <div class="irab-word">أَنْ تَحْمِلَ</div>
        <div class="irab-details">أَن:ْ حَرْفٌ نَاصِبٌ. تَحْمِل:َ فِعْلَ مُضَارِعٌ مَنْصُوبٌ. وَالمَصْدَرُ الْمُؤَوَّلُ )أَنْ تَحْمِلَ( فِي مَحَلِّ جر، مُضَاف إليه.</div>
    </div>
    <div class="irab-box" id="b16221">
        <div class="irab-word">مِنْ سَلْمَايَ</div>
        <div class="irab-details">مِنْ: حَرْفُ جرٍ. سَلْمَاي:َ اسمٌ مَجْرُور، وعلامَةُ جَرَهِ الكَسْرَةُ المُقَدَّرَةُ على الأَلِف،ِ مَنَعَ ظُهُورَهَا التَّعَذُّر.ُ والياء، ضمير متصل مبني على الفتحة في محل جر، مُضَافُ إِلَيْهِ.</div>
    </div>
    <div class="irab-box" id="b16222">
        <div class="irab-word">رَدْ</div>
        <div class="irab-details">مَفْعُولُ بِهِ مَنْصُوب،ُ وعلامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَة.ُ وسُكِّنَ لِلضَّرورة الشَّعْرِيَّةِ.</div>
    </div>
    <div class="irab-box" id="b16223">
        <div class="irab-word">جملة )تَرْتَدُّ الصَّبَا(</div>
        <div class="irab-details">استئنافية، لا محل لها من الإعراب.</div>
    </div>
    <div class="irab-box" id="b16224">
        <div class="irab-word">جملة )تَحْمِلَ(</div>
        <div class="irab-details">صِلَةُ الْمَوْصُولِ الْحَرْفِي، لَا مَحَلَّ لها مِنَ الإعراب.</div>
    </div>
</div>

=== BLOCK 13: Poem Verse 12 ===
(Component: TEMPLATE_C_POEM.html)
Title: البيت الثاني عشر
Poet:
Hemistich 1: ١٢- فَسَمَا لولا أَنِينِي مَا اهْتَدَى
Hemistich 2: لِسَرِيرِي طَيْفُهَا لَمَّا وَفَدْ

=== BLOCK 14: Poem Analysis 12 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: التحليل
Content:
<div class="flex flex-col gap-2mm">
    <div class="text-accent"><b>المفردات:</b> أنيني: تأوهي. طيفها: الخيَالُ الطَّائِفُ وهو ما يَرَاهُ النَّائِمُ. وَفَد: قَدِمَ.</div>
    <div class="text-accent"><b>الشرح:</b> أُقسم لولا تأوهي وصَوْتُ تَوَجُعِي لما استدَلَّ على فراش نومِي خَيَالها اللَّذِي أَلَمَّ بي.</div>
    <div class="text-accent"><b>الفكرة:</b> المعاناة بِسَبَبِ فِرَاقِ الأَحِبَّةِ وَالشَّوْقُ والحنين إليهم. )التَّعْبِيرُ عَنِ الحَسْرَةِ على انقطاع الوِصَالِ مَعَ الْمَحْبُوبَةِ(.</div>
</div>

=== BLOCK 15: Irab Verse 12 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الإعراب
Content:
<div class="flex flex-col gap-2mm">
    <div class="irab-box" id="b16225">
        <div class="irab-word">فَسَمَا</div>
        <div class="irab-details">مَفْعُولُ مُطْلَقُ مَنْصُوب.ُ</div>
    </div>
    <div class="irab-box" id="b16226">
        <div class="irab-word">لولا أَنِينِي</div>
        <div class="irab-details">لولا: حَرْفُ شَرْطِ غَيْرُ جازم. أَنِينِي: مُبْتَدَأٌ مَرْفُوع، وعلامَةُ رَفْعِهِ الضَّمَّةُ المُقَدَّرَةُ على ما قَبْلَ ياء المُتَكَلِم،ِ مَنَعَ ظُهُورَهَا اشْتِغَالُ الْمَحَلِ بِالحَرَكَةِ المُنَاسِبَة.ِ والخبر محذوف وُجُوبًا تقديرُهُ )مَوْجُودٌ(.</div>
    </div>
    <div class="irab-box" id="b16227">
        <div class="irab-word">مَا اهْتَدَى</div>
        <div class="irab-details">ما: حَرْفُ نَفْي. اهْتَدَى: فعل ماضِ.</div>
    </div>
    <div class="irab-box" id="b16228">
        <div class="irab-word">طَيْفُها</div>
        <div class="irab-details">فَاعِلٌ مَرْفُوعٌ.</div>
    </div>
    <div class="irab-box" id="b16229">
        <div class="irab-word">لَمَّا</div>
        <div class="irab-details">اسمُ شَرْطٍ غَيْرُ جازم، مَبْنِي على السُّكُونِ فِي مَحَلِّ نَصْب،ِ مَفْعُولُ فِيهِ ظَرْفُ زَمَانٍ.</div>
    </div>
    <div class="irab-box" id="b16230">
        <div class="irab-word">وَفَدْ</div>
        <div class="irab-details">فِعْلَ مَاضِ مَبْنِيٌّ على الفَتْحَةِ الظَّاهِرَةِ وَسُكِّنَ لِلضَّرُورَةِ الشَّعْرِيَّة.ِ</div>
    </div>
    <div class="irab-box" id="b16231">
        <div class="irab-word">جملة )لولا أَنِينِي مَا اهْتَدَى ... طيفها(</div>
        <div class="irab-details">استئنافية، لا محل لها من الإعراب.</div>
    </div>
    <div class="irab-box" id="b16232">
        <div class="irab-word">جملة )مَا اهْتَدَى(</div>
        <div class="irab-details">جوابُ الشَّرْطِ غَيْرِ الجازم، لا مَحَلَّ لها مِنَ الإعراب.</div>
    </div>
    <div class="irab-box" id="b16233">
        <div class="irab-word">جملة )وَفَدْ(</div>
        <div class="irab-details">مُضَاف إليه،ِ مَحَلَّها الجر.</div>
    </div>
</div>

=== BLOCK 16: Poem Verse 13 ===
(Component: TEMPLATE_C_POEM.html)
Title: البيت الثالث عشر
Poet:
Hemistich 1: ١٣- زَارَ إِلْمَامًا فَمَا مِلْتُ إِلَى
Hemistich 2: ضَمِّهِ حَتَّى تَجَافَى وَابْتَعَدْ

=== BLOCK 17: Poem Analysis 13 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: التحليل
Content:
<div class="flex flex-col gap-2mm">
    <div class="text-accent"><b>المفردات:</b> إِلْمَامًا: أَلَمَّ، زارَ زِيَارَةً غَيْرَ طَوِيْلَةٍ خَاطِفَة،َ. تَجَافَى: أَعْرَضَ عَنِّي.</div>
    <div class="text-accent"><b>الشرح:</b> زارني خيالها زيارة خاطفة، فَمَا إِنْ نَوَيْتُ الاقْتِرَابَ مِنْهُ حَتَّى تَنَكَّرَ لي، وأَعْرَضَ عَنِّي وَرَحَلَ بَعِيدًا.</div>
    <div class="text-accent"><b>الفكرة:</b> المعاناةُ بِسَبَبِ فِرَاقِ الأَحِبَّةِ وَالشَّوْقُ والحنين إليهم. )التَّعْبِيرُ عَنِ الحَسْرَةِ على انقطاع الوِصَالِ مَعَ المحبوبة(.</div>
</div>

=== BLOCK 18: Irab Cut Part 1 ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
[BLOCK_TITLE]: إعراب
[CONTENT]:
<div class="flex flex-col gap-2mm">
    <div class="irab-box" id="b16234">
        <div class="irab-word">زارَ</div>
        <div class="irab-details">فعل ماض مبني على الفَتْحَةِ الظَّاهِرَةِ.</div>
    </div>
    <div class="irab-box" id="b16235">
        <div class="irab-word">إِلْمَامًا</div>
        <div class="irab-details">نَائِبُ مَفْعُولِ مُطْلَقٍ مَنْصُوبٌ.</div>
    </div>
    <div class="irab-box" id="b16236">
        <div class="irab-word">فَمَا</div>
        <div class="irab-details">الْفَاء،ُ حَرْفُ عَطْفِ. مَا: حَرْفُ نَفْي.</div>
    </div>
    <div class="irab-box" id="b16237">
        <div class="irab-word">إلى ضمه</div>
        <div class="irab-details">إلى: حَرْفُ جر. ضَمِّه،ِ اسم مجرور. والهاء، ضمير متصل مَبْنِي على الكَسْرَةِ فِي مَحَلِّ جَر،ٍ مُضَافَ إِلَيْهِ.</div>
    </div>
    <div class="irab-box" id="b16238">
        <div class="irab-word">حَتَّى</div>
        <div class="irab-details">حَرْفُ غاية وجر.</div>
    </div>
    <div class="irab-box" id="b16239">
        <div class="irab-word">تَجَافى</div>
        <div class="irab-details">فعل ماض مبني على الفتحة المقدرة على الألف للتعذر.</div>
    </div>
</div>

--- END STREAM ---
