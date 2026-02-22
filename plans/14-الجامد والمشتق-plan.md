# **SESSION 14.0**

[TASK DEFINITION]
Objective: Implement الجامد والمشتق.
File: `pages/14.0_nXX_الجامد والمشتق.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK\_RULES.md and elements\_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/14.1_...`.
3. text Content: 100% Arabic with full Harakat.
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
6. Templates: You are forbidden from inventing new HTML tags or classes or template elements. You must map all content strictly using "Jules-workspace/Templates/" components as the STREAM says.
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). use "Jules-workspace/id_manager.py" to generate or verify them.
8. **Self-Correction:** Run "Jules-workspace/lint_pages.py" after creating html files. If it fails, you MUST fix the errors (usually inline styles) before submitting.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...) .
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed.
12. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of teal , also use this tool to verify "Jules-workspace/smart_color_fixer.py"
14. DO Create a temporary Python generation script to help you generate the lesson html pages in the perfect way needed without problems !

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER)
[LESSON_NUMBER]: 14
[CHAPTER_TITLE]: الجامد والمشتق
[CATEGORY_HEADER]: الصرف
[SECTION_HEADER]: المستوى اللغوي
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition (Jamid & Mushtaq) ===
(Component: TEMPLATE_C_BLOCK)
Title: تعريف الجامد والمشتق
Content:
<span class="text-accent">أَسْماءُ العَرَبِيَّةِ نَوعانِ: جامِدَةٌ ومُشتَقَّةٌ.</span>
<br>
<span class="font-bold text-teal-800">١. الاسمُ الجَامِدُ:</span> هو الاسمُ الَّذِي لا يُؤْخَذُ مِنْ غَيرِهِ.
<br>
<span class="font-bold text-teal-800">٢. الاسمُ المُشْتَقُّ:</span> فَهُوَ الاسمُ الذِي يُؤْخَذُ مِنْ غَيرِهِ.

=== BLOCK 3: The Two Types of Jamid ===
(Component: TEMPLATE_C_SPLIT)
[LEFT_TITLE]: الجَامِدُ الذَّاتِ
[LEFT_CONTENT]:
<div class="p-2mm bg-teal-50 rounded-lg border-r-4 border-teal-500">
    <p class="text-right">
        <span class="font-bold text-teal-700">التعريف:</span> هو الاسمُ الذِي يُدْرَكُ بإِحْدى <span class="highlight-blue">الحَواسِّ الخَمْسِ</span>.
        <br>
        <span class="font-bold">أمثلة:</span> (شَجَرَة، كُرسِيّ، قَلَم...).
    </p>
</div>
[RIGHT_TITLE]: الجَامِدُ المَعنَى
[RIGHT_CONTENT]:
<div class="p-2mm bg-orange-50 rounded-lg border-r-4 border-orange-500">
    <p class="text-right">
        <span class="font-bold text-orange-700">التعريف:</span> هو الاسمُ الذِي يُدْرَكُ <span class="highlight-red">بالعَقلِ</span>.
        <br>
        <span class="font-bold">ويُسَمَّى:</span> المَصدَرُ، ومِنهُ تُؤْخَذُ الأَفْعَالُ والأَسْماءُ المُشْتَقَّةُ.
        <br>
        <span class="font-bold">أمثلة:</span> (نَجَاح، أَمَل).
    </p>
</div>

=== BLOCK 4: Overview of Derivatives ===
(Component: TEMPLATE_C_LIST)
Title: الأَسْماءُ المُشْتَقَّةُ (سبعة أنواع)
Items:
1. اسمُ الفَاعِلِ
2. مُبالَغَةُ اسمِ الفاعِلِ
3. اسمُ المَفعُولِ
4. الصِّفَةُ المُشَبَّهَةُ باسمِ الفاعِلِ
5. اسمُ الآلَةِ
6. اسمُ المَكانِ واسمُ الزَّمانِ
7. اسمُ التَّفضِيلِ

=== BLOCK 5: Ism Fa'il & Mubalagha & Ism Maf'ul (Core Matrix) ===
(Component: TEMPLATE_C_TABLE)
Title: قواعد صياغة المشتقات الأساسية
Columns: المشتق | تعريفه | صياغته من الثلاثي | صياغته من فوق الثلاثي | عمله
Rows:
اسمُ الفَاعِلِ | يَدُلُّ عَلَى مَنْ قَامَ بالفِعلِ | على وَزْنِ <span class="highlight-red">فَاعِل</span> (كَتَبَ، كاتِب) | إِبْدالِ حَرفِ المُضارَعَةِ مِيمًا مَضمُومَةً و<span class="highlight-blue">كَسرِ</span> ما قَبلَ آخِرِهِ (مُكَرِّم) | يرفع فاعلاً أو ينصب مفعولاً به (جَاءَ الضَّاحِكُ سِنُّهُ، جاء ناكِسًا رَأْسَهُ).
مُبالَغَةُ اسمِ الفَاعِلِ | يَدُلُّ عَلى المُبالغَةِ والإِكثارِ | أوزان: فَعَّال (جَلَّاد)، فَعَّالَة (عَلَّامَة)، مِفْعَال (مِعْطَاء)، فَعُول (أَكُول)، فَعِيل (رَحِيم) | (قليل) | تَعْمَلُ عَمَلَ اسمِ الفَاعِلِ (جَاءَ الضَّحَّاكُ سِنُّهُ).
اسمُ المَفعُولِ | يَدُلُّ عَلى مَنْ وَقعَ عليهِ الفِعل | على وَزْنِ <span class="highlight-red">مَفعُول</span> (مَكتوب) | إِبْدالِ حَرفِ المُضارَعَةِ مِيمًا مَضمُومَةً و<span class="highlight-blue">فَتحِ</span> ما قَبلَ آخِرِهِ (مُسْتَخْرَج) | يَرفَعُ نائبَ فاعِلٍ (الأَبُ مَشكورٌ فَضْلُهُ).

=== BLOCK 6: Sifa Mushabbaha ===
(Component: TEMPLATE_C_BLOCK)
Title: الصِّفَةُ المُشَبَّهَةُ باسمِ الفاعِلِ
Content:
<p>
    <span class="text-accent">اسمٌ يُشْتَقُّ مِنَ المَصدَرِ لِيدُلَّ عَلى صِفةٍ ثابِتةٍ في الموصوفِ.</span>
    <br>
    تُصاغُ مِنَ الفِعلِ <span class="highlight-red">الثُّلاثِيِّ اللازمِ</span> عَلى الأَوزانِ الآتِيَةِ:
</p>
<ul class="list-disc list-inside mt-2mm">
    <li><span class="font-bold">فَعِيل:</span> كَريم</li>
    <li><span class="font-bold">فُعَال:</span> شُجَاع</li>
    <li><span class="font-bold">فَعَال:</span> جَبَان</li>
    <li><span class="font-bold">فَعَل:</span> بَطَل</li>
    <li><span class="font-bold">فَعِل:</span> فَرِحٌ</li>
    <li><span class="font-bold">فِعْل:</span> شَهْم</li>
    <li><span class="font-bold">فُعْل:</span> صُلْب</li>
    <li><span class="font-bold">فَعْلَان (مؤنَّثُه فَعْلَى):</span> عَطشَان، عَطْشَى</li>
    <li><span class="font-bold">أَفْعَل (مؤنَّثُه فَعْلَاء):</span> يَدُلُّ عَلى لونٍ أو عَيْبٍ أو حِليَةٍ (أحمر حمراء، أعرج عرجاء).</li>
</ul>
<p class="mt-2mm bg-gray-100 p-2mm rounded">
    <span class="font-bold">عملها:</span> ترفع فاعلاً (الطَّبيبُ عَظِيمٌ دَوْرُهُ).
</p>

=== BLOCK 7: Instrument, Time, and Place ===
(Component: TEMPLATE_C_SPLIT)
[LEFT_TITLE]: اسمُ الآلَةِ
[LEFT_CONTENT]:
<p class="text-justify">
    اسمٌ يَدُلُّ عَلى آلَةِ حُدوثِ الفِعلِ. يُصاغُ غالباً من الثلاثي المتعدي.
    <br><span class="font-bold text-orange-700">أوزانه الخمسة:</span>
</p>
<ul class="list-none space-y-1">
    <li>1. <span class="font-bold">مِفْعَل:</span> مِثْقَب</li>
    <li>2. <span class="font-bold">مِفْعَال:</span> مِصْباح</li>
    <li>3. <span class="font-bold">مِفْعَلَة:</span> مِرْوَحة</li>
    <li>4. <span class="font-bold">فَعَّال:</span> بَرَّاد</li>
    <li>5. <span class="font-bold">فَعَّالَة:</span> غَسَّالَة</li>
</ul>
[RIGHT_TITLE]: اسما المَكانِ والزَّمانِ
[RIGHT_CONTENT]:
<p class="text-justify">
    يُشتقان للدلالة على زمان أو مكان الفِعل.
    <br><span class="font-bold text-teal-700">من الثلاثي:</span>
    <br>1. <span class="font-bold">مَفْعَل:</span> (مَسْبَح، مَدْخَل، مَلْقَى) إذا كان مضارعه مفتوح/مضموم العين أو معتل الآخر.
    <br>2. <span class="font-bold">مَفْعِل:</span> (مَعْرِض، مَوْقِف) إذا كان مضارعه مكسور العين أو معتل الفاء.
    <br><span class="font-bold text-teal-700">من فوق الثلاثي:</span>
    <br>كاسم المفعول (مُجتَمَع، مُنتَدَى).
</p>

=== BLOCK 8: Ism Tafdil ===
(Component: TEMPLATE_C_BLOCK)
Title: اسمُ التَّفضيلِ (شروطه وأحكامه)
Content:
<p>
    يُصاغُ على وزن <span class="font-bold text-red-600">(أَفْعَل)</span> للمذكر و <span class="font-bold text-red-600">(فُعْلَى)</span> للمؤنث، إذا استوفى الفعل <span class="highlight-blue">الشروط السبعة</span>:
</p>
<ol class="list-decimal list-inside mt-2mm space-y-1">
    <li>ثُلاثيَّا.</li>
    <li>تامًّا (ليسَ ناقِصًا).</li>
    <li>مُثبَتًا (غَيرَ مَنفيٍّ).</li>
    <li>مُتَصَرِّفًا (ليسَ جامِدًا).</li>
    <li>مَبنيًّا للمَعلومِ.</li>
    <li>قابِلًا للتَّفاوُتِ (ليس مات أو فني).</li>
    <li>ليس الوصف منه على (أفعل - فعلاء).</li>
</ol>
<p class="mt-2mm">
    <span class="font-bold text-orange-600">إذا فُقد شرط:</span> نأتي بمصدر الفعل منصوباً على التمييز بعد اسم مساعد (أشَدَّ، أكثَرَ). مثال: (أنتَ أكثَرُ ارتِقاءً).
</p>

=== BLOCK 9: Solved Exercises (Group 1) ===
(Component: TEMPLATE_C_TABLE)
Title: أمثلة تطبيقية (١)
Columns: السؤال | الإجابة | التوضيح
Rows:
صنّف: (رجُل، رَغْبَة، قَوِيّ) | رجل: جامد ذات، رغبة: جامد معنى، قوي: مشتق | (ذات: حواس، معنى: عقل، مشتق: من غيره)
ميّز المصدر من المشتق: (خَرِبَ، تَعَبَ، وَصَبَ، المِنْقَارَ، سَعْيَ) | خَرِب: صفة مشبهة، المِنْقَار: اسم آلة | تَعَب، وَصَب، سَعْي: مصادر
سمِّ المشتقات: (كَئِيب، مُدَار، مُقَام، شَرّ، قَفْر) | كئيب/قفر: صفة مشبهة، مُدار: اسم مفعول | مُقام: اسم مكان، شَرّ: اسم تفضيل
اشتقاقات (وَثِقَ): | واثِق (فاعل)، وَثوق (مبالغة)، مَوْثوق (مفعول) | -

=== BLOCK 10: Poem Application ===
(Component: TEMPLATE_C_POEM)
Poem_Text:
إنْ نَكُنْ سِرْنا على الشَّوكِ سِنينَا ... ولَقِينَا مِنْ أذَاهُ مَا لَقِينَا
إنْ نَكُنْ بِتْنَا عُرَاةً جَائِعِينَا ... أو نَكُنْ عِشْنَا حُفَاةً بائِسِينَا
فَلَقَدْ ثُرْنَا عَلَى أنْفُسِنَا ... ومحونَا وصمَةَ الذِّلَّةِ فِينَا

=== BLOCK 11: Poem Extraction & Benefits ===
(Component: TEMPLATE_C_SPLIT)
[LEFT_TITLE]: فائدة صرفية (توضيح الفرق)
[LEFT_CONTENT]:
<div class="bg-gray-100 p-2mm rounded">
    <p class="font-bold mb-1mm">الفرق بين (عَمِيق) و(عَلِيم):</p>
    <ul class="list-disc list-inside text-sm">
        <li><span class="text-teal-700">عَمِيق:</span> فعلها لازم (عَمُقَ)، لا نأخذ منها اسم فاعل (عامق)، فهي <span class="font-bold">صفة مشبهة</span>.</li>
        <li><span class="text-orange-700">عَلِيم:</span> فعلها متعدٍّ (عَلِمَ)، واسم الفاعل (عالِم)، فهي <span class="font-bold">مبالغة اسم فاعل</span>.</li>
    </ul>
</div>
[RIGHT_TITLE]: استخراج أسماء الفاعلين من الأبيات
[RIGHT_CONTENT]:
<table class="w-full text-center border-collapse">
    <tr class="bg-teal-100"><th>اسم الفاعل</th><th>فعله</th></tr>
    <tr><td>عُرَاةً</td><td>عَرِيَ</td></tr>
    <tr><td>جَائِعِينَا</td><td>جَاعَ</td></tr>
    <tr><td>حُفَاةً</td><td>حَفِيَ</td></tr>
    <tr><td>بائِسِينَا</td><td>بَئِسَ</td></tr>
</table>

=== BLOCK 12: Advanced Solved Exercises ===
(Component: TEMPLATE_C_TABLE)
Title: تطبيقات شاملة على المشتقات
Columns: الكلمة | نوع المشتق | فعله/ملاحظات
Rows:
الشَّاكِي، الجَنَاة، الصَّائِدون | اسم فاعل | شَكا، جنَى، صادَ
مَسْرَح، مَقِيل، مَجَال، مُسْتَنْقَع | اسم مكان | سَرَحَ، قالَ، جال، استنقع
جَهُول، عَجُوز | مبالغة اسم فاعل | جَهِلَ، عَجَزَ
مِرْآة، مِصْبَاح | اسم آلة | رأى، صَبُحَ
أزْهَد | اسم تفضيل | زَهِدَ
المُقَدَّس | اسم مفعول | قُدِّسَ (وقع عليه الفعل)
المُقَدِّس | اسم فاعل | قَدَّسَ (قام بالفعل)

=== BLOCK 13: Final Evaluation ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: (أنا أُحِبُّ العملَ المُتْقَنَ، والمُعامَلَةَ الحَسَنَةَ، والمَنْزِلَ النَّظِيفَ). استخرج من العبارة السابقة المشتقات وبين نوع كل منها وفعله.
Number: ٢
Question: صُغ اسم الفاعل واسم المفعول واسم المكان من الفعل (اِنْطَلَقَ) في جمل مفيدة.
Number: ٣
Question: علل: صياغة اسم التفضيل من (سَوِدَ) على (أشَدّ سَواداً) وليس (أسْوَد).

--- END STREAM ---
