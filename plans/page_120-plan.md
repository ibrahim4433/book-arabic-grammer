# **SESSION 120**

[TASK DEFINITION]
Objective: Implement page 120.
File: `pages/page_120.html`
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
[UNIQUE_ID]: b00120
[LESSON_NUMBER]: 120
[CHAPTER_TITLE]: page 120
[CATEGORY_HEADER]: 120
[SECTION_HEADER]: 120
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Solved Exercise ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
[UNIQUE_ID]: b00121
[QUESTION_NUMBER]: أ -
[QUESTION_TEXT]: اجْعَلْ شَخْصِيَّةَ الجَنْدِيَّ القَدِيمَ شَخْصِيَّةٌ مُؤَثَرَةً فِي مُجْرَيَاتِ الأَحْدَاثِ فِي النَّصَ وَإِغْنَاءِ الحَوَار،ِ ثُمَّ أَجْرِ التَّغيير اللازم.َ
[ANSWER_TEXT]: سَارَ الثَّلَاثَةُ مُتَسَلْحِينَ بِالْحَنِينِ إِلَى لَثْم تُرَابِ الوَطَنِ الطَّاهِر،ِ وَاسْتِنْشَاقِ عَبِيرِهِ الفَوَّاحِ ... كَانَتْ الشَّمْسُ تَنْحَنِي مُوَدِّعَةً مُتَوَارِيَةً وَرَاءَ الْأُفْقِ ... كَانَ الجَنْدِيُّ حِينَمَا بَدَؤوا المسِيرِ قَاصِدِينَ جِسْرَ الْعُبُورِ ... القَدِيمُ يُحَاوِلُ جَاهِدًا أَنْ يَكُونَ فِي بِدَايَةِ الرَّكْب،ِ وَكَأَتِي بِهِ يَنْوِي أَنْ يَكُونَ أَوَّلَ مَنْ يَتَعَرَّضُ لِخَطَرٍ مُفَاجِيءٍ ... كَانَ يُرَدُدُ عَلَى الدَّوَامِ: "سِيرًا خَلْفِي .. لَا تَسْبِقَانِي". وَصَلَ الثَّلَاثَةُ جِسْرَ العُبُورِ وَتَعَاظَمَ فِي نُفُوسِهِم حُلُمُ الاتِصَالِ بِأَرْضِ الوَطَنِ ... لكِنَّ رَصَاصَاتِ جُنُودِ الصَّهَائِنَةِ الْمَرَابِطِينَ عَلَى الْحِسْرِ أَوْقَفَتْ مَسِيرَهُم، صَاحَ أَحَدُ جُنُودِ الاخْتِلَالِ: لَنْ تَمَرُوا مِنْ هُنَا. فَرَدَّ الجَنْدِيُّ القَدِيمُ بِصَوتٍ يَشِيْ بِرَبَاطَةِ الجَأْشِ وَثَبَاتِ القَلْبِ: لَنْ تُرْهِبُونَا بِرَصَاصِكُم،ْ سَنَمُرُّ رِغْمَ النَّار،ِ وَبَعْدَ أَنْ أَتَمَّ قُولَه،ُ أَشَارَ إِلَى الشَّيخ وَابْنَتِهِ قَائِلًا: اتَّبِعَانِي وَاتَّخِذَا جَسَدِي دِرْعًا يَصُدُّ عَنْكُمَا رَصَاصَ الغَاصِبِين. صَاحَ أَحَدُ الجَنُودِ المرابطين مُحَذِّرًا: توقفوا ... تَوَقَّفُوا. لَكِنَّ الثَّلَاثَةَ تَابَعُوا رِحْلَةَ العُبُورِ بِخُطُوَاتٍ وَاثِقَة،ٍ وَكَأَنَّ الخَطَرَ قَدْ زَادَهُمْ قُوَّةً، وَفَجْأَةً يَنْهَمِرُ الرَّصَاصُ لِتَسْتَقِرَ رَصَاصَةٌ فِي قَلْبِ الجَنْدِيَ القَدِيمِ الشَّجَاعِ الذِي جَعَلَ جَسَدَهُ حِصْنَا حَمَى رَفِيقَي دَرْبِهِ مِنْ رَصَاصِ الْمُجْرِمِينَ ...

=== BLOCK 3: Linguistic Applications ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b00122
Title: التطبيقات اللغوية
Content: <p class="text-accent text-center font-bold mb-2mm">ادرس مَبْحَثَ عَلاماتِ الإِعْرَابِ الأَصْلِيَّةِ وَالفَرْعِيَّةِ فِي الأَسْمَاءِ والأَفْعَال،ِ مُسْتَفِيدًا مِمَّا فِي الأَسْطُر الآتية:</p>

=== BLOCK 4: Example Sentences ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[UNIQUE_ID]: b00123
Content: <div class="text-center font-bold">وَكَانَ النَّهْرُ يَبْصُقُ ضِفَتَيْه<br>قِطَعًا مِنَ اللَّحْمِ الْمُفَتَتِ<br>كانُوا ثلاثة عائدين<br>شيخ، وابنته، وجندي قديم<br>يقفونَ عِنْدَ الحِسْر</div>

=== BLOCK 5: Parsing Split ===
(Component: TEMPLATE_C_SPLIT.html)
[UNIQUE_ID]: b00124
Right Title: ج - الأسماء المعربة
Right Content:
<ul class="structured-list">
<li class="list-item-content"><strong>بعلامات إعراب أصلية:</strong></li>
<li class="list-item-content"><span class="highlight-blue">النهر، شيخ، ابنته، جندي قديم:</span> مرفوع بالضمة.</li>
<li class="list-item-content"><span class="highlight-blue">قطعا، ثلاثة، عند:</span> منصوب بالفتحة.</li>
<li class="list-item-content"><span class="highlight-blue">اللحم المفتت، الجسر:</span> مجرور بالكسرة.</li>
<li class="list-item-content"><strong>بعلامات إعراب فرعية:</strong></li>
<li class="list-item-content"><span class="highlight-blue">ضفتيه:</span> منصوب بالياء؛ لأنه مثنى.</li>
<li class="list-item-content"><span class="highlight-blue">عائدين:</span> مجرور بالياء؛ لأنه جمع مذكر سالم.</li>
</ul>
Left Title: الأفعال المعربة
Left Content:
<ul class="structured-list">
<li class="list-item-content"><strong>بعلامة إعراب أصلية:</strong></li>
<li class="list-item-content"><span class="highlight-red">يبصق:</span> مرفوع بالضمة.</li>
<li class="list-item-content"><strong>بعلامة إعراب فرعية:</strong></li>
<li class="list-item-content"><span class="highlight-red">يقفون:</span> مرفوع بثبوت النون؛ لأنه من الأفعال الخمسة.</li>
</ul>

=== BLOCK 6: The Marks Table ===
(Component: TEMPLATE_C_BLOCK.html)
[UNIQUE_ID]: b00125
Title: العلامة الإعرابية
Content:
<div class="block-body p-0">
    <table class="dense-table text-xs">
        <thead>
            <tr>
                <th>الحالة</th>
                <th>الأصلية</th>
                <th>المثنى والملحق به</th>
                <th>جمع المذكر السالم والملحق به</th>
                <th>جَمْعُ الْمُؤْنَّتِ السالم والملحق</th>
                <th>الممنوع من الصرف</th>
                <th>الأسماء الخمسة مفردة مضافة إلى غير ياء المتكلم</th>
                <th>الأفعال الخمسة</th>
                <th>الفعل المضارع المعتل الآخر</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td class="font-bold">الرفع</td>
                <td>الضم</td>
                <td>نَجَحَ الْمُجِدَّانِ</td>
                <td>نَجَحَ الْمُجِدُّونَ</td>
                <td>أصلية</td>
                <td>أصلية</td>
                <td>نجح أخوك</td>
                <td>ثبوت النون<br>الصادقون يخلصون</td>
                <td>أصلية</td>
            </tr>
            <tr>
                <td class="font-bold">النصب</td>
                <td>الفتح</td>
                <td>رَأَيْتُ الْمُجِدَّيْنِ</td>
                <td>رَأَيْتُ الْمُجِدِّينَ</td>
                <td>الكسر نيابة عن الفتح<br>رَأَيْتُ الطَّالباتِ</td>
                <td>أصلية</td>
                <td>رَأَيْتُ أباك</td>
                <td>حذف النون<br>الصادقان لن يكذبا</td>
                <td>أصلية</td>
            </tr>
            <tr>
                <td class="font-bold">الجر</td>
                <td>الكسر</td>
                <td>مَرَرْتُ بِالْمُجِدَّيْنِ</td>
                <td>مَرَرْتُ بِالْمُجِدِّينَ</td>
                <td>أصلية</td>
                <td>الفتح نيابة عن الكسر<br>سافرت إلى مكةَ</td>
                <td>سلمت على أخيك</td>
                <td>-</td>
                <td>-</td>
            </tr>
            <tr>
                <td class="font-bold">الجزم</td>
                <td>السكون</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>-</td>
                <td>حذف النون<br>الصادقان لم يكذبا</td>
                <td>حذف حرف العلة<br>لم يسعَ</td>
            </tr>
        </tbody>
    </table>
</div>

--- END STREAM ---
