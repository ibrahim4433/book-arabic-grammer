# **SESSION 120**

[TASK DEFINITION]
Objective: Implement page 120.
File: `pages/page_120.html` (Note: Use the exact page number.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools. If it overflows, it is a catastrophic failure. Do NOT try to solve overflow by deleting text (Strict Typographer Rule). Solve it by choosing denser templates or omitting optional white-space.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`. Ensure exact visual continuity (same title, same classes).
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md` to identify the correct template to use for the continuation. You are forbidden from guessing. Scan the raw text for the preceding keyword to determine the active template and apply the correct `_PART_2.html` wrapping.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`, `.highlight-green` for secondary.
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
[LESSON_NUMBER]: 120
[CHAPTER_TITLE]: page 120
[CATEGORY_HEADER]: 120
[SECTION_HEADER]: 120
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Continuation of List ===
(Component: TEMPLATE_CUT_BOX_PART_2.html mapped to TEMPLATE_C_LIST.html)
Title: [No Title]
List Items:
- **أ. اجْعَلْ شَخْصِيَّةَ الجَنْدِيَّ القَدِيمَ شَخْصِيَّةٌ مُؤَثَرَةً فِي مُجْرَيَاتِ الأَحْدَاثِ فِي النَّصَ، وَإِغْنَاءِ الحَوَار،ِ ثُمَّ أَجْرِ التَّغيير اللازم.َ**
الإجابة: سَارَ الثَّلَاثَةُ مُتَسَلْحِينَ بِالْحَنِينِ إِلَى لَثْم تُرَابِ الوَطَنِ الطَّاهِر،ِ وَاسْتِنْشَاقِ عَبِيرِهِ الفَوَّاحِ ... كَانَتْ الشَّمْسُ تَنْحَنِي مُوَدِّعَةً مُتَوَارِيَةً وَرَاءَ الْأُفْقِ ... حِينَمَا بَدَؤوا المسِيرِ فَاصِدِينِ جِسْرِ الْعُبُور ... كَانَ الجَنْدِيُّ القَدِيمُ يُحَاوِلُ جَاهِدًا أَنْ يَكُونَ فِي بِدَايَةِ الرَّكْب،ِ وَكَأَتِي بِهِ يَنْوِي أَنْ يَكُونَ أَوَّلَ مَنْ يَتَعَرَّضُ لِخَطَرٍ مُفَاجِيء ... كَانَ يُرَدُدُ عَلَى الدَّوَامِ: "سِيرًا خَلْفِي .. لَا تَسْبِقَانِي".
وَصَلَ الثَّلَاثَةُ جِسْرَ العُبُورِ وَتَعَاظَمَ فِي نُفُوسِهِم حُلُمُ الاتِصَالِ بِأَرْضِ الوَطَنِ ... لكِنَّ رَصَاصَاتِ جُنُودِ الصَّهَائِنَةِ الْمَرَابِطِينَ عَلَى الْحِسْرِ أَوْقَفَتْ مَسِيرَهُم. صَاحَ أَحَدُ جُنُودِ الاخْتِلَالِ: لَنْ تَمَرُوا مِنْ هُنَا. فَرَدَّ الجَنْدِيُّ القَدِيمُ بِصَوتٍ يَشِيْ بِرَبَاطَةِ الجَأْشِ وَثَبَاتِ القَلْبِ: لَنْ تُرْهِبُونَا بِرَصَاصِكُم،ْ سَنَمُرُّ رِغْمَ النَّار،ِ وَبَعْدَ أَنْ أَتَمَّ قُولَه،ُ أَشَارَ إِلَى الشَّيخ وَابْنَتِهِ قَائِلًا: اتَّبِعَانِي وَاتَّخِذَا جَسَدِي دِرْعًا يَصُدُّ عَنْكُمَا رَصَاصَ الغَاصِبِين".
صَاحَ أَحَدُ الجَنُودِ المرابطين مُحَدرًا: توقفوا ... تَوَفَّفُوا. لَكِنَّ الثَّلَاثَةَ تَابَعُوا رِحْلَةَ العُبُورِ بِخُطُوَاتٍ وَاثِقَة،ٍ وَكَأَنَّ الخَطَرَ قَدْ زَادَهُمْ قُوَّةً. وَفَجْأَةً يَنْهَمِرُ الرَّصَاصُ لِتَسْتَقِرَ رَصَاصَةٌ فِي قَلْبِ الجَنْدِيَ القَدِيمِ الشَّجَاعِ الذِي جَعَلَ جَسَدَهُ حِصْنَا حَمَى رَفِيقَي دَرْبِهِ مِنْ رَصَاصِ المُجْرِمِين ...

=== BLOCK 3: Linguistic Applications ===
(Component: TEMPLATE_C_BLOCK.html)
Title: التطبيقات اللغوية
Content: <p class="text-accent">ادرس مَبْحَثَ عَلاماتِ الإِعْرَابِ الأَصْلِيَّةِ وَالفَرْعِيَّةِ فِي الأَسْمَاءِ والأَفْعَال،ِ مُسْتَفِيدًا مِمَّا فِي الأَسْطُر الآتية:</p>
<ul class="structured-list">
<li class="list-item-content">وَكَانَ النَّهْرُ يَبْصُقُ ضِفَتَيْه قِطَعًا مِنَ اللَّحْمِ الْمُفَتَتِ</li>
<li class="list-item-content">كانُوا ثلاثة عائدين شيخ، وابنته، وجندي قديم</li>
<li class="list-item-content">يقفونَ عِنْدَ الحِسْر</li>
</ul>

=== BLOCK 4: I'rab Details (Original Signs) ===
(Component: TEMPLATE_C_BLOCK.html - Orange Accent)
Title: ج - الأسماء المعربة بعلامات إعراب أصلية:
Content:
<ul class="structured-list">
<li class="list-item-content"><span class="highlight-blue">النهر، شيخ، ابنته، جندي قديم:</span> مرفوع بالضمة.</li>
<li class="list-item-content"><span class="highlight-blue">قطعا، ثلاثة، عند:</span> منصوب بالفتحة.</li>
<li class="list-item-content"><span class="highlight-blue">اللحم المفتت، الجسر:</span> مجرور بالكسرة.</li>
</ul>

=== BLOCK 5: I'rab Details (Sub-signs in Nouns) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الأسماء المعربة بعلامات إعراب فرعية:
Content:
<ul class="structured-list">
<li class="list-item-content"><span class="highlight-red">ضفتيه:</span> منصوب بالياء؛ لأنه مثنى.</li>
<li class="list-item-content"><span class="highlight-red">عائدين:</span> مجرور بالياء؛ لأنه جمع مذكر سالم.</li>
</ul>

=== BLOCK 6: I'rab Details (Verbs) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الأفعال:
Content:
<ul class="structured-list">
<li class="list-item-content"><strong>الفعل المعرب بعلامة إعراب أصلية:</strong> <span class="highlight-blue">يبصق:</span> مرفوع بالضمة.</li>
<li class="list-item-content"><strong>الفعل المعرب بعلامة إعراب فرعية:</strong> <span class="highlight-red">يقفون:</span> مرفوع بثبوت النون؛ لأنه من الأفعال الخمسة.</li>
</ul>

=== BLOCK 7: Matrix Table (Signs in Nouns and Verbs) ===
(Component: TEMPLATE_C_TABLE.html)
Title: العلامة الإعرابية الفرعية والأصلية في الأسماء والأفعال
Table HTML:
<div class="block-body p-0">
  <table class="dense-table">
    <thead>
      <tr>
        <th>الحالة</th>
        <th>الأصلية</th>
        <th>في الأسماء (الفرعية والملحقات)</th>
        <th>في الأفعال (الفرعية)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="font-bold">الرفع</td>
        <td>الضم (أصلية) <br> <span class="text-sm">نجح أخوك</span></td>
        <td>
          <strong>المثنى:</strong> نَجَعَ الْمُجِدَّانِ <br>
          <strong>جمع المذكر السالم:</strong> الصادقون <br>
          <strong>الأسماء الخمسة:</strong> (اب، أخ، حم، ذو، فو) مفردة مضافة إلى غير ياء المتكلم
        </td>
        <td>
          <strong>الأفعال الخمسة:</strong> ثبوت النون <br>
          <span class="text-sm">يخلصون</span>
        </td>
      </tr>
      <tr>
        <td class="font-bold">النصب</td>
        <td>الفتح (أصلية)</td>
        <td>
          <strong>المثنى:</strong> رَأَيْتُ الْمُجِدِّينَ (الياء) <br>
          <strong>جمع المذكر السالم:</strong> رَأَيْتُ الْمُجِدِّينَ (الياء) <br>
          <strong>جمع المؤنث السالم:</strong> رَأَيْتُ الطَّالباتِ (الكسر نيابة عن الفتح) <br>
          <strong>الأسماء الخمسة:</strong> رَأَيْتُ أباك
        </td>
        <td>
          <strong>الأفعال الخمسة:</strong> حذف النون <br>
          <span class="text-sm">الصادقان لن يكذبا</span>
        </td>
      </tr>
      <tr>
        <td class="font-bold">الجر</td>
        <td>الكسر (أصلية)</td>
        <td>
          <strong>المثنى:</strong> مَرَرْتُ بِالْمُجِدِّينَ (الياء) <br>
          <strong>جمع المذكر السالم:</strong> مَرَرْتُ بِالْمُجِدِّينَ (الياء) <br>
          <strong>الممنوع من الصرف:</strong> سافرت إلى مكة (الفتح نيابة عن الكسر) <br>
          <strong>الأسماء الخمسة:</strong> سلمت على أخيك
        </td>
        <td>
          -
        </td>
      </tr>
      <tr>
        <td class="font-bold">الجزم</td>
        <td>السكون (أصلية)</td>
        <td>
          -
        </td>
        <td>
          <strong>الأفعال الخمسة:</strong> حذف النون <br>
          <span class="text-sm">الصادقان لم يكذبا</span> <br>
          <strong>الفعل المضارع المعتل الآخر:</strong> حذف حرف العلة <br>
          <span class="text-sm">لم يسعَ</span>
        </td>
      </tr>
    </tbody>
  </table>
</div>

--- END STREAM ---
