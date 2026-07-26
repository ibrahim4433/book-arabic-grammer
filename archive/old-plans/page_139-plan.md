# **SESSION 139**

[TASK DEFINITION]
Objective: Implement page 139.
File: `pages/page_139.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green`  for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide: NO INLINE STYLES. Replace `<section>` tags with `<div>` tags and apply unique IDs. Use classes like `w-20pct`, `mt-2mm`, `text-center`, `font-bold`.
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX') on the replacing `<div>`.
8. Self-Correction: Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...) .
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense.
13. balanced page colors between teal and orange.
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`).
15. Exam section always be in the end of the lesson without the answers.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 139
[CHAPTER_TITLE]: page 139
[CATEGORY_HEADER]: 139
[SECTION_HEADER]: 139
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: القراءة التمهيدية ===
(Component: TEMPLATE_C_BLOCK.html)
Title: القراءة التمهيدية
Content:
<p class="text-accent mb-2mm">كانَتْ حِرْبُ تشرين التحريرية ردا حقيقيا على نكسة حزيران، تلك النكسة التي صَدَمَتِ الإِنْسَانَ العَرَبِي،َّ وَنَالَتْ مِنْ كبريائِه،ِ وأَحْدَثَتْ في وجدانِهِ أَلَمَا عنيفًا ؛ لأَنَّهُ لَم يَكُنْ يَتَوَفَّعُ هَذِهِ النَّهَايَةَ الفَاجِعَةَ فَعَكس انتصار تشرين الفرح في قوافي الشعراء، فبعد أن خرج الوطنُ مِنَ الحرب منتصرًا، خفقت قلوب الشعراء مع قوافيهم متغنية بهذا الحدث الجلل، ترسم وتخط أشعارا تنتفض فرحا وتتطاير زهوا وإشراقا.ً</p>
<p class="mb-0">حيث لجأ الأدباء إلى إبراز اعتزازهم بتدمير خصون الصهاينة فِي حَرْبِ تشرين،َ فَإِنَّ حَرْبَ تَشْرِينَ الَّتِي هَبَّتْ فِي ذَرَا الجَوْلَانِ وفوق رمال سيناء، حَمَلَتْ فِي عَصْفِهَا الزَّاحِفِ تَبَاشِيرَ النَّصْرِ والثقَةَ وَالأَمَلَ بِمِيلَادِ الإِنْسَانِ العَرَبِي الجديد، وخَطَّتْ صَفْحَةً مُشَرِّفَةً فِي تاريخ المسيرة العَرَبِيَّةِ نَحْوَ التَّقَدم والرقي. كانَتْ فَجْرًا عَرَبِيَّا جديدًا حَلَّمَ السُّدُودَ كُلها، وأَعَادَ لِلإِنْسَانِ العَرَبِيِّ كرامتهُ بِتِلْكَ الدماء التي بُلَتْ في ذلك اليوم لتحقيق النَّصْرِ وَرَسم بداية الانطلاقِ نَحْوَ التَّقدم وإثبات الوُجُودِ على السَّاحَةِ الدولية. وها هو الشاعر عبد الرحيم الحصني يُؤكد أنَّ الوَطَنَ المكافح استطاع بنضالِهِ المتواصل أَنْ يَدُكَ تَحْصِينَاتِ الأَعداء ويُدمرها، تلك التَّحْصِينَاتُ التي شَيْدها الأعداء بروح يسيل منها الحقد، وتفوحُ مِنْهَا الكراهية. يقُول:ُ</p>

=== BLOCK 3: شعر ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: وَنَسَفْتَ بِالرَّحْفِ المَقَدَّسِ مَا ابْتَنَى
Hemistich 2: حِقْدُ العداةِ مِنَ الْحُصُونِ وَشَيَّدا

=== BLOCK 4: نص أدبي ===
(Component: TEMPLATE_C_BLOCK.html)
Title: نص أدبي
Content:
<p class="mb-0">ونظرا لكثرة المواجهات الدَّامِيَة،ِ والمعارك الضارية التي خاضَهَا أبناء الأمة العربية، وهم يتصدون للمستعمرين الغُزَاةِ الطَّامِعِين، لمَعَتْ بطولات لأبطال سطروا أروع ملاحم الفداء والتضحية؛ فلم يبخل أبناء الأمة العربية خلال كفاحهم المتواصل بالدَّم،ِ فَقَدَّمُوا قوافل الشهداء الذين صارُوا وَسَامَ شرف وقلادة ترعانِ صَدْرَ الأمة العربية. وأمام هذا العطاء الفياض والبذلِ السَّخِيِّ جَادَتْ أَقلامُ الأدباء بتمجيد التضحيات المشرفة التي حَتَّقَتِ الجَلَاءَ فما أروع التضحيات التي بدلها أبناء سورية لتحقيق منجز الجلاء حيث استعذبوا الموت وأرخصوا دماءهم في سبيل حرية الوطن، فقرنُوا أقوالهم بأفعالهم، وجعلوا أجسادهم حممًا تُلْهِبُ ظهور المستعمرين، وتحرق جباة الطَّعَاةِ الظَّالمين. فالشاعر عمر أبو ريشة يؤكد للحرية أنها ما جلبت إلى ربوع سورية بمهر بخس، وإنما جلبت بأغلى الأثمان وأنفسها، فكل حبة من تراب الوطن تَعَطَّرَتْ بِدَمٍ شَهِيْدٍ بَطَل،ِ رَفَضَ اللُّل والخَضُوع،َ وقَدَّمَ روحَهُ رَخِيْصَةً على مَذْبَحِ الحَرَيَّةِ يَقُول:ُ</p>

=== BLOCK 5: شعر ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: لَنْ تَرَيْ حَفْنَةَ رَمْلٍ فَوْقَهَا
Hemistich 2: لَمْ تُعَطَرْ بِدِمَا حُرِّ أَبِي

=== BLOCK 6: المطالعة ===
(Component: TEMPLATE_C_TABLE.html)
Title: المطالعة
Content:
<div class="block-body p-0">
  <table class="dense-table">
    <tbody>
      <tr>
        <td>هَكَذَا نَجِدُ أَنَّ الأدبَ العَرَبِيَّ ظَلَ مُلازِمَا لِلقَضَايا الوَطَنِيَّة والقَوْمِيَّة التي تبرز في الساحة العربية، فقد وَجَدَ الأدباء في هذه القضايا مادةً غزيرةً غَمَسُوا فيها أقلامهم،</td>
        <td>فَصَاغُوا منها أَدَبًا تَجَلَّتْ فِيهِ الفَرْحَةُ الصَّاخِبَةُ بجلاء المستعمر الفرنسي عَنْ البلاد،</td>
      </tr>
      <tr>
        <td>وَبَرَزَتْ فِيهِ قُدْرَةُ الوَطَنِ وأبنائِهِ على تحطيم تحصينات الأعداء،</td>
        <td>وكانَ الصَّوْتَ الْمُجَلْجِلَ الذي صَدَحَ مُتَغَتِيَا بِتَضْحِيَاتِ الشُّهَدَاءِ العِظَامِ الذين قَدَّمُوا أَزْوَاحَهم بِسَجَاءٍ لِتَنعم الأُمَّةُ بالحرية والكرامة.</td>
      </tr>
    </tbody>
  </table>
</div>

=== BLOCK 7: تنبيه ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content:
ثانيا: الموضوعان المقترحان غير المكتوبين تركنا هذين الموضوعين من دون كتابة ليكونا دِرْبَةٌ وَمِرَانًا للطالب [

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question:
<p class="mb-2mm">الموضوع المقترح غير المكتوب الأول : قيل : اهتم الأُدَبَاءُ العَرَبُ فِي العَصْرِ الحَدِيثِ اهْتِمَامًا كَبِيرًا بالقضايا الوَطَبَيَّةِ وَالقَوْمِيَّة،ِ فَفَضَحُوا جَرَائِمَ الصُّهْيُونِيَّة، وحَثُوا على النهوض في وجه المجرمين، واثقين بانتصار الحق وثباتِهِ أمام الغاصبين((. ناقش المَوْضُوعَ السَّابِقَ وَأَيِّدْ مَا تَذْهَبُ إِلَيْهِ بِالشَّوَاهِدِ المُنَاسِبَة،ِ مُوَظِّفًا الشَّاهِدَ الآتي: قَالَ الشَّاعِرُ إِبراهيم اليَازِجي:</p>
<div class="text-center text-primary font-bold">بالله يا قَوْمَنَا هَبُوا لِشَأْنِكُمُ فَكَم تُنَادِيكُمُ الأَشْعَارُ و الْخَطَبُ</div>

Number: ٢
Question:
<p class="mb-2mm">الموضوع المقترح غير المكتوب الثاني: قيل : اهتم الأدَبَاءُ العَرَبُ بِالقَضايا الوَطَنِيَّةِ وَالقَوْمِيَّة،ِ فَصَوَّرُوا هَزِيمَةَ الْمُسْتَعْمِرِ الغَرْبِي وَخَيْبَتَهُ فِي تَوْطِيدِ وُجُودِهِ عَلَى أَرْضِنَا، ثمَّ أَبْرَزُوا وحْدَةَ العَرَبِ في المصائب والشَّدَائِدِ مُمَجَدِين تضحيات الأجداد مِنْ أَجْلِ الوطن، مُعَبَرِينِ عَنِ الفَرَحِ بِجَلَاءِ الْمُسْتَعْمِرِ الغَرْبي عن البلاد(. ناقش المَوْضُوعَ السَّابِقَ وَأَيِّدْ مَا تَذْهَبُ إِلَيْهِ بِالشَّوَاهِدِ المُنَاسِبَة،ِ مُوَظِّفًا الشَّاهِدَ الآتي: قَالَ الشَّاعِرُ حافظ إبراهيم:</p>
<div class="text-center text-primary font-bold">إِذَا أَلَمَّتْ بِوَادِي النِّيلِ نَازِلَةٌ باتت لها راسيات الشَّامِ تَضْطَرِبُ</div>

--- END STREAM ---
