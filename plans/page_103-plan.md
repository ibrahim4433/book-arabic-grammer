# **SESSION 103**

[TASK DEFINITION]
Objective: Implement page 103.
File: `pages/page_103.html` (Note: Use the exact page number.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools. If it overflows, it is a catastrophic failure. Do NOT try to solve overflow by deleting text (Strict Typographer Rule). Solve it by choosing denser templates or omitting optional white-space.
2.5 Cut Content: Use `TEMPLATE_CUT_BOX_PART_2.html` for the beginning list which was cut violently. Ensure exact visual continuity.
3. Text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice. Fixed garbled OCR text by correcting word order without dropping words.
4. Highlighting: Use `.highlight-red`, `.highlight-blue`, and `.highlight-green` for focus words.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide: NO INLINE STYLES.
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX') on `<div>` tags replacing `<section>`.
8. Self-Correction: Run `lint_pages.py --one-page-mode`.
9. Do not summarize examples.
10. Do not provide uncompleted text content.
11. Preserve exact Tashkeel and add missing if necessary.
12. Visual Density: The page must be dense.
13. Balanced page colors between teal and orange: Use `.block-header.accent` class combinations.
14. Wrapper: `TEMPLATE_C_PAGE_WRAPPER.html`.
15. Exam section at the end without answers.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 103
[CHAPTER_TITLE]: page 103
[CATEGORY_HEADER]: 103
[SECTION_HEADER]: 103
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Cut Content Part 2 (الموازنة) ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
Title: الموازنة
Element: TEMPLATE_C_LIST.html
Content:
<ul class="structured-list">
  <li><span class="text-accent">الاختلاف :</span> - <span class="highlight-red">نزار قباني</span> بيّن سبب غلاء المهر بينما <span class="highlight-blue">عمر أبو ريشة</span> لم يبين.</li>
  <li>- <span class="highlight-red">نزار قباني</span> جعل المهر لدمشق، بينما <span class="highlight-blue">عمر أبو ريشة</span> جعله للحرية.</li>
  <li>- <span class="highlight-red">نزار قباني</span> تكلم بلسان الفرد بينما <span class="highlight-blue">عمر أبو ريشة</span> تكلم بلسان الجماعة.</li>
</ul>

=== BLOCK 3: ملاحظة ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: <strong>ملاحظة:</strong> يكتفى بوجه واحد للتشابه، وبوجه واحد للاختلاف.

=== BLOCK 4: المستوى الفني (النمط السردي) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المستوى الفني
Classes: block-header accent
Content:
<div class="block-body">
  <p><span class="text-accent">١- اعتمدَ الشَّاعِرُ النَّمَطَ السَّرِدِي فِي المَقْطَعِ الثاني للتعبيرِ عَنْ مَعَانِيهِ هات مُؤَشِّرَيْنَ لِذَلِك.َ</span></p>
  <p><strong>ج ١-</strong></p>
  <ul class="structured-list">
    <li><strong>استعمال الأفعال الماضية:</strong> شق، أتى، رفت، انتشت، تغنت، عرفتها، ضاقت، أدمى، هب، أعدته، تهادى.</li>
    <li><strong>استعمال ضمائر الغائب:</strong> شق، أتى، رفت طربا، انتشت من عبقه، تغنت بالمروءات، عرفتها في فتاها، ضاقت به صحراؤه، أعدته لأفق، هب للفتح، أدمى تحته، الدنيا، الهدى، أكمامه، تهادى موكبا، أتى.</li>
  </ul>
  <p><span class="text-accent">مؤشرات النمط السردي:</span></p>
  <ul class="structured-list">
    <li>- اعتماد ضمائر الغائب.</li>
    <li>- استعمال الأفعال الماضية.</li>
    <li>٢- استعمال الأفعال المضارعة المسبوقة بالفعل الناقص (كانَ).</li>
    <li>- استخدام الحوار.</li>
    <li>٥- الإكثار من أدوات الرَّبْطِ الدَّالَّةِ على الزمان والمكان: (وعندما، وحين، وبينما، ...).</li>
    <li>٦- غلبة الأسلوب الخبري إثباتا ونفيًا.</li>
  </ul>
</div>

=== BLOCK 5: دلالات الألفاظ والضمائر ===
(Component: TEMPLATE_C_BLOCK.html)
Title: دلالات الألفاظ والضمائر
Content:
<div class="block-body">
  <p><span class="text-accent">- بِمَ تُعَلِلُ اعتِمَادَ الشَّاعِرِ على الصَّفَاتِ المُشَبَّهَةِ باسم الفاعل في تعبيرهِ عَنِ الْإِنْسَانِ الْعَرَبِيِّ، وَالْمُحْتَلِّ؟</span></p>
  <p><strong>ج -</strong> تمكن الشاعر من خلال هذا الاستعمال من إبراز بعض الصفات الثابتة المستقرة الدائمة في الإنسان العربي، وبذلك بدا الإنسان العربي حراً أبياً أصيد على الدوام. ومن جهة أخرى مكنه هذا الاستعمال من تثبيت حالة الضعف والانكسار عند المحتل الذي بدا كليلاً ضعيفاً.</p>
  <p><span class="text-accent">- استَعْمَلَ الشَّاعِرُ فِي الْمَقْطَعِ الثَّانِي ضَمِيرَ الغَائِبِ، ثُمَّ ضَمِيرَ المُتَكَلِّمِ فِي المَقْطَعِ الثَّالِثِ بَيِّنْ دَوْرَ كُلِّ مِنْهُمَا فِي خِدْمَةِ الْمَعْنَى.</span></p>
  <p><strong>ج -</strong> أفاد الشاعر من ضمير الغائب في المقطع الثاني في إظهار الاعتزاز بالماضي المجيد المشرف الذي سطره الأجداد؛ فقد مكنه الضمير من استحضار دور الإنسان العربي في نشر الرسالة الإنسانية السامية داخل الأرض العربية وخارجها.</p>
  <p>- أما ضمير المتكلم فأفاد منه في تضخيم ذاته الجماعية، مظهراً مشاعر الاعتزاز والفرح، مشيداً بالتضحيات التي قدمها الشعب العربي السوري لنيل استقلاله.</p>
</div>

=== BLOCK 6: الصور البيانية والمحسنات البديعية ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الصور البيانية والمحسنات البديعية
Content:
<div class="block-body">
  <p><span class="text-accent">- استخرج مِنَ المَقْطَعِ الْأَوَّلِ صُورةً بَيَانِيَّةً، ثُمَّ حَلَّلْهَا، وَاذْكُرْ وظيفتين مِنْ وظائفها.</span></p>
  <p><strong>ج - الصورة :</strong> (الحق لطمت عارضيه قبضة المغتصب).</p>
  <ul class="structured-list">
    <li><strong>تسمية الصورة:</strong> استعارة مكنية.</li>
    <li><strong>تحليل الصورة:</strong> شبه الحق بإنسان له عارضان، فحذف المشبه به، وأبقى شيئاً من لوازمه وهو عارضيه.</li>
    <li><strong>تَسْمِيةُ الوَظِيفة:</strong> الشرح والتوضيح.</li>
    <li><strong>شرح الوظيفة أو توضيح الوظيفة:</strong> شرحَتِ الصُورَةُ وَوَضَحَتْ معنى: ثبات الحق في وجه المغتصب من خلال تشبيه الحق بإنسان، فاقنعت المتلقي بمضمون المعنى وصدقه.</li>
    <li><strong>تَسْمِية الوظيفة:</strong> الإيحاء.</li>
    <li><strong>شرح الوظيفة أو توضيح الوظيفة:</strong> جَعَلَ الشَّاعِرُ الصورة موحِيَةً بتشبيهه الحق بإنسان، فهذا أوحى بالثبات والصلابة والصمود والتحدي والانتصار والشجاعة، وأثار مشاعر الإعجاب بالحق، والاستياء من المستعمر، واستنكار الظلم.</li>
  </ul>
  <p><span class="text-accent">٥- مِنْ وَظَائِفِ الصورة إضفاء نَفْسِيَّةِ المُبدع على الطبيعة والأشياء. وَضِّحْ ذَلِكَ في الصورة الآتية: (هذه تربتنا لن تزدهي بسوانا).</span></p>
  <p><strong>ج - الصورة:</strong> (هذه تُرْبَتُنَا لَنْ تَزْدَهِي بِسِوانا).</p>
  <ul class="structured-list">
    <li><strong>تَسْمِيَةُ الصورة:</strong> استعارة مكنية.</li>
    <li><strong>تحليل الصورة:</strong> شبه التربة بالإنسان، فحذف المشبه به وأبقى شيئاً من لوازمه وهو : " تَزْدَهِي ".</li>
    <li><strong>تَسْمِيَةُ الوَظِيفَةِ:</strong> إضفاء نفسية المبدع على الطبيعة والأشياء.</li>
    <li><strong>شرح الوظيفة أو توضيح الوظيفة:</strong> شخص الشَّاعِرُ التربةَ وَنَقَلَهَا بَعْدَ انفعالِهِ بِهَا، فَتَلَوَّنَتْ بمشاعره ورُواه، حيث أضفى عليها مشاعر الافتخار والاعتزاز، فبدت كالشَّاعِرِ رافضةً وِصَايَةَ المسْتَعْمر وحمايته.</li>
  </ul>
  <p><span class="text-accent">٦- استخرج مِنَ المَقْطَعِ الثَّالِثِ طِبَاقاً، ثُمَّ بَيِّنْ دَوْرَهُ فِي خِدْمَةِ الْمَعْنى.</span></p>
  <p><strong>ج ٦- الطباق:</strong> (ضعف، قوة).</p>
  <ul class="structured-list">
    <li><strong>دوره في خدمة المعنى:</strong> إعمال العقل في المتناقضات، حيث استطاع الشاعر من خلال هذا الطباق أن يعمل عقل المتلقي في المتناقضات فجعله يدرك الفرق الشاسع بين الضعف والقوة.</li>
  </ul>
</div>

=== BLOCK 7: The Core Matrix (الأدوات الفنية والموسيقا الداخلية) ===
(Component: TEMPLATE_C_TABLE.html)
Title: الأدوات الفنية والموسيقا الداخلية
Content:
<div class="block-body p-0">
  <p class="text-center font-bold p-2"><span class="text-accent">٧- مَثِّلْ لِأَدَاتَين مِنَ الأَدَوَاتِ الفَنِّيَّةِ التي اتكأ الشاعر عليها في النَّص لإبراز كُلِّ مِنْ شُعُوري الفَرَحِ والاعتزاز.</span></p>
  <table class="dense-table">
    <thead>
      <tr>
        <th>الشعور</th>
        <th>الأداة</th>
        <th>المثال</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="highlight-green">الفرح</span></td>
        <td>الألفاظ</td>
        <td>انتشت، طاب</td>
      </tr>
      <tr>
        <td><span class="highlight-green">الفرح</span></td>
        <td>التراكيب</td>
        <td>رفت طربا، يا عروس المجد طاب الملتقى</td>
      </tr>
      <tr>
        <td><span class="highlight-blue">الاعتزاز</span></td>
        <td>التراكيب</td>
        <td>أرقناها دماء حرة، لم نرخص المهر</td>
      </tr>
      <tr>
        <td><span class="highlight-blue">الاعتزاز</span></td>
        <td>الصور</td>
        <td>(هذه تربتنا لن تزدهي بسوانا)</td>
      </tr>
    </tbody>
  </table>
  <p class="text-center font-bold p-2 mt-2"><span class="text-accent">٨- مِنْ مَنَابِعِ الموسيقا الداخلية: تكرارُ الْمُفْرَدَاتِ - استِعْمَالُ الحُرُوفِ الهَامِسَةِ - الْمُحَسَنَاتُ اللَّفِظِيَّةِ. مَثِّلْ لِكُلِّ مِنْهَا.</span></p>
  <table class="dense-table">
    <thead>
      <tr>
        <th>منبع الموسيقى</th>
        <th>المثال</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>تكرار المفردات</td>
        <td>(موكبًا، موكب)، (مهرك، المهر)</td>
      </tr>
      <tr>
        <td>استعمال الحروف الهامسة</td>
        <td>ظهر التناغم والانسجام بين حروف الهمس والجهر في الكلمات المتعاقبة في البيت السادس: (هنا، شق، الهدى، أكمامه، تهادى، موكبا، موكب)</td>
      </tr>
      <tr>
        <td>المحسنات اللفظية (التصريع)</td>
        <td>(اسحبي، الشهب)</td>
      </tr>
      <tr>
        <td>المحسنات اللفظية (الجناس الناقص)</td>
        <td>(طاب، طال)</td>
      </tr>
    </tbody>
  </table>
</div>

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٩
Question: قَطِّعْ عروضيًا البيتَ التَّاسِعَ مِنَ النَّص، ثُمَّ سَمِّ بَحْرَه،ُ وَادْكُرْ جَوازاته: (تقطيع البيت التَّاسِع، وتسمية بحره، وتحديد جوازاته: - -) ۱۰۳

--- END STREAM ---
