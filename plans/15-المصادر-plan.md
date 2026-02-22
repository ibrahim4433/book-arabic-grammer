# **SESSION 15.0**

[TASK DEFINITION]
Objective: Implement المصادر.
File: `pages/15.0_nXX_المصادر.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/15.1_...` if page have a lot of blank space add exam elements from the lesson.
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
6. Templates: You are forbidden from inventing new HTML tags or classes or template elements. You must map all content using "Jules-workspace/Templates/" components as the STREAM says in suitable way.
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). use "Jules-workspace/id_manager.py" to generate or verify them.
8. **Self-Correction:** Run "Jules-workspace/lint_pages.py" after creating html files. If it fails, you MUST fix the errors (usually inline styles) before submitting.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...) .
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER)
[LESSON_NUMBER]: 15
[CHAPTER_TITLE]: المصادر
[CATEGORY_HEADER]: الصرف
[SECTION_HEADER]: المستوى اللغوي
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Intro ===
(Component: TEMPLATE_C_BLOCK)
id: b15001
Title: تعريف المصدر
Content:
<p class="text-accent text-justify">
المصدرُ اسمٌ يدلُّ على الحدَثِ مجرَّدًا مِن الزَّمنِ، وهو الأصلُ الذي تصدُرُ عنْهُ الأفعالُ، والأسماءُ المُشتقَّةُ. فالمصدرُ <span class="highlight-red">(ذهابٌ)</span> يدل على حَدَثِ الذَّهَاب لكنَّهُ لا يدلُّ على وقوعِ الحَدَثِ في زَمَنٍ مُعيِّنٍ، ومِنْ هذا المصدر نأخُذُ الفعلَ <span class="highlight-blue">(ذَهَبَ)</span> ونأخُذُ مِنْهُ اسم الفاعل (ذاهبٌ).
</p>

=== BLOCK 3: Auditory Sources ===
(Component: TEMPLATE_C_BLOCK)
id: b15002
Title: المصادرُ السَّماعيَّة (الثلاثية)
Content:
<p class="text-justify mb-2">
مصادر الأفعال الثلاثيَّة سماعيَّة تُعرَفُ بالرُّجوع إلى المُعجمات. فهي غير قياسيَّة إذ لا يمكنُ الاعتمادُ على قاعِدةٍ مُعيَّنةٍ لمعرفتها.
</p>
<div class="chips-container">
    <span class="bg-grey-lighter rounded p-1mm">شرب، شُرْب</span>
    <span class="bg-grey-lighter rounded p-1mm">ذهب، ذهاب</span>
    <span class="bg-grey-lighter rounded p-1mm">رحم، رحمة</span>
    <span class="bg-grey-lighter rounded p-1mm">طاف، طوفان</span>
    <span class="bg-grey-lighter rounded p-1mm">علِم، عِلْم</span>
</div>

=== BLOCK 4: Quadraliteral Sources ===
(Component: TEMPLATE_C_TABLE)
id: b15003
Title: أوزان مصادر الأفعال الرُّباعيَّة القياسية
[TABLE_HEADERS]: <th>وزن الفعل</th><th>مثال</th><th>وزن المصدر</th><th>مثال</th>
[TABLE_ROWS]:
<tr>
    <td class="font-bold highlight-blue">فَعَّلَ</td>
    <td>عَلَّمَ</td>
    <td class="font-bold highlight-red">تفعيل</td>
    <td>تعليم</td>
</tr>
<tr>
    <td class="font-bold highlight-blue">أفعل</td>
    <td>أقْبَل</td>
    <td class="font-bold highlight-red">إفعال</td>
    <td>إقبال</td>
</tr>
<tr>
    <td class="font-bold highlight-blue">فَاعَلَ</td>
    <td>شَارَكَ</td>
    <td class="font-bold highlight-red">مُفَاعَلَة</td>
    <td>مُشَارَكَة</td>
</tr>
<tr>
    <td class="font-bold highlight-blue">فَعْلَلَ</td>
    <td>زَلْزَلَ</td>
    <td class="font-bold highlight-red">فَعْلَلَة</td>
    <td>زَلْزَلَة</td>
</tr>

=== BLOCK 5: Penta/Hexa Sources ===
(Component: TEMPLATE_C_SPLIT)
id: b15004
[LEFT_TITLE]: المبدوء بتاء (خماسي)
[LEFT_CONTENT]:
<p class="text-justify">
إذا بدأ الفعل الخماسيُّ بتاء يكونُ مصدرُه بوضع <span class="highlight-red">ضمة</span> قبل الآخر.
</p>
<ul class="structured-list mt-2">
    <li><span class="list-item-content">تدافَع <span class="arrow">←</span> تدافُع</span></li>
    <li><span class="list-item-content">تقدَّم <span class="arrow">←</span> تقدُّم</span></li>
</ul>
[RIGHT_TITLE]: المبدوء بهمزة وصل (خماسي/سداسي)
[RIGHT_CONTENT]:
<p class="text-justify">
إذا بدأ الفعل الخماسيّ، أو الفعل السُّداسيّ بهمزة وصل يكونُ مصدرُهما بوضع <span class="highlight-red">ألف</span> قبل الآخر.
</p>
<ul class="structured-list mt-2">
    <li><span class="list-item-content">اعتمد <span class="arrow">←</span> اعتماد</span></li>
    <li><span class="list-item-content">استقبل <span class="arrow">←</span> استقبال</span></li>
</ul>

=== BLOCK 6: Special Cases ===
(Component: TEMPLATE_C_LIST)
id: b15005
Title: حالات خاصة في المصادر
Content:
<li><span class="list-item-content">لبعضِ الأفعالِ الرباعيةِ التي تكونُ على وزنِ (فَاعَلَ) مصدرٌ آخرُ سماعيٌّ هو وزنُ <span class="highlight-red">(فِعَال)</span>، نحو: (قاتَلَ، قِتَال)، (جاهَدَ، جِهَاد).</span></li>
<li><span class="list-item-content">إِذا كان الفعلُ الرباعيُّ على وزنِ (فَعَّلَ) وكان معتلَّ الآخرِ، أو مهموزَ الآخرِ يكونُ مصدرُه على وزنِ <span class="highlight-red">(تَفْعِلَة)</span>، نحو: (رَبَّى، تَربِية)، (جَزَّأ، تجزِئَة).</span></li>
<li><span class="list-item-content">إِذا كان الفعلُ الخماسيُّ مبدوءًا بتاء وكان معتلَّ الآخرِ بالألفِ يكونُ مصدرُه بتحويلِ الألفِ إِلى ياء. نحو: (تمادَى، تمادِي).</span></li>
<li><span class="list-item-content">إِذا كان قبلَ آخرِ الفعلِ الرباعيِّ أو السُّداسيِّ ألفٌ يضافُ إِلى مصدرهِ <span class="highlight-red">تاء مربوطة</span>. نحو: (أفادَ، إِفادَة)، (استطاعَ، استِطاعَة).</span></li>
<li><span class="list-item-content">إِذا كان قبلَ آخرِ الفعلِ الخماسيِّ ألف فيكونُ مصدرُه بإِضافةِ ياءٍ تسبقُ هذه الألفَ. نحو: (الساق، انسِياق)، (ارتاحَ، ارتِياح).</span></li>

=== BLOCK 7: Function of Source ===
(Component: TEMPLATE_C_BLOCK)
id: b15006
Title: عمل المصدر
Content:
<p class="text-justify">
قد يعملُ المصدرُ عملَ فعلِهِ، فيرفعُ فاعلًا إِنْ كانَ فعلُهُ لازمًا، وينصُبُ مفعولًا به إِنْ كانَ فعلُهُ مُتعدِّيًا. ورفعُهُ للفاعلِ نادرٌ؛ لأنَّهُ يُضافُ إِلى فاعلِهِ غالبًا.
<br><br>
<span class="highlight-red">مثال:</span> إِطعامُكَ اليتيمَ شرفٌ.
<br>
- اليتيمَ: مفعولٌ بِهِ للمصدرِ (إِطعام) منصوبٌ، وعلامةُ نصبِهِ الفتحةُ الظَّاهرة.
</p>

=== BLOCK 8: Mimi Source ===
(Component: TEMPLATE_C_SPLIT)
id: b15007
[LEFT_TITLE]: الفرق في السياق
[LEFT_CONTENT]:
<ul class="structured-list">
    <li><span class="list-item-content"><strong>اسمُ مَكانٍ:</strong> مَوْقِفُ السَّيَّاراتِ في الحيِّ الجنوبيِّ.</span></li>
    <li><span class="list-item-content"><strong>اسمُ زَمَانٍ:</strong> المساءُ مَوْقِفُ العُمَّالِ عَنِ العملِ.</span></li>
    <li><span class="list-item-content"><strong>مَصدَرٌ ميميٌّ:</strong> كانَ مَوقِفُ الرَّجُلِ مِنَ القضيَّةِ سلبيًّا (دل على حدث).</span></li>
</ul>
[RIGHT_TITLE]: تعريف المصدر الميمي
[RIGHT_CONTENT]:
<p class="text-accent text-justify">
هو اسمٌ جامدٌ يدلُّ على حَدَثٍ مجرَّدٍ عَنِ الزمانِ والمكانِ، ولكنْ فيهِ <span class="highlight-red">ميمٌ زائدةٌ</span> تميزُه عن المصدرِ الطبيعيِّ. وهو مِنْ حيثُ الوزنُ والصِّياغَةُ نفسُ اسمِ المكانِ، أو اسمُ الزَّمانِ.
</p>

=== BLOCK 9: Industrial Source ===
(Component: TEMPLATE_C_BLOCK)
id: b15008
Title: المصدر الصناعي
Content:
<p class="text-accent text-justify mb-2">
اسمٌ لحقَتْهُ ياءُ النِّسبةِ، تليها تاءُ التأنيثِ المربوطةِ للدَّلالةِ على معنى المصدرِ؛ أي كُلّ اسمٍ أضيفَتْ إِليهِ <span class="highlight-red">(يَّة)</span>. نحو: (عِلْم، عِلميَّة - وَطَن، وطَنِيَّة).
</p>
(Component: TEMPLATE_C_BENEFIT_WARNING)
Title: تنبيه هام
Content:
وينبغي التفريقُ بينَ المصادرِ الصِّناعيَّةِ، وبينَ الأسماءِ المنسوبةِ التي تلحقُها الياءُ المشدَّدةُ والتاءُ المربوطةُ (الصفة).
<ul class="structured-list mt-2">
    <li><span class="list-item-content"><strong>مصدر صناعي:</strong> إِنَّ الهمجيَّةَ صورةٌ مِنْ صورِ الشُّعوبِ المُتخلِّفَةِ. (دلت على معنى المصدر).</span></li>
    <li><span class="list-item-content"><strong>صفة منسوبة:</strong> إِنَّ الدَّعَواتِ الهمجيَّةَ خطرٌ على شعوبِ العالمِ. (صفة لما قبلها).</span></li>
</ul>

=== BLOCK 10: Interpreted Source ===
(Component: TEMPLATE_C_TABLE)
id: b15009
Title: المصدر المؤول (أشكاله وإعرابه)
[TABLE_HEADERS]: <th>الصورة</th><th>مثال</th><th>التأويل</th><th>المحل الإعرابي</th>
[TABLE_ROWS]:
<tr>
    <td class="font-bold">أَنْ + الفعل</td>
    <td>أرَدْتُ أنْ أسافرَ</td>
    <td>أرَدْتُ السَّفرَ</td>
    <td>في محلِّ نصبٍ مفعولٌ به</td>
</tr>
<tr>
    <td class="font-bold">أَنَّ + اسمها وخبرها</td>
    <td>سرَّني أنَّكَ نجحْتَ</td>
    <td>سرَّني نجاحُكَ</td>
    <td>في محلِّ رفعٍ، فاعلٌ</td>
</tr>
<tr>
    <td class="font-bold">ما المصدريَّة + الفعل</td>
    <td>انهَضْ كَمَا نهضَ البطلُ</td>
    <td>انهَضْ كنُهوضِ البطلِ</td>
    <td>في محلِّ جرٍّ بحرفِ الجرِّ</td>
</tr>

=== BLOCK 11: Interpreted Source Evidence ===
(Component: TEMPLATE_C_POEM)
id: b15010
Poem_Line_1: كُلَّمَا قُلْتُ: في غَدٍ أُدْرِكُ السُّؤْ ... لَ أَتَانِي غَدٌ بِمَا لا أشَــاءُ
Poem_Line_2: مِثْلَ ما يُبْدِعُ السَّحَابُ إذَا ما ... عانَــقَ الأرضَ بَعْدَ قَطْعِ الوِصالِ
Poem_Line_3: أهَبْتُ بِشُبَّانِ العِراقِ وإِنَّمَــا ... أردْتُ بِشِعْرِي أنْ أهِيجَ سِبَاعَـا
Author: شاعر
Bio: أمثلة شعرية
(Component: TEMPLATE_C_IRAB_ROW)
id: b15011
Content:
(Component: TEMPLATE_C_IRAB_BOX_COMPACT)
Word: ما قُلْتُ
Analysis: المَصْدَرُ المُؤَوَّلُ مِن ما والفعلِ قُلْتُ، في محلِّ جرٍّ، مُضَافٌ إليهِ.
(Component: TEMPLATE_C_IRAB_BOX_COMPACT)
Word: ما يُبْدِعُ
Analysis: المَصْدَرُ المُؤَوَّلُ مِن ما والفعلِ يُبْدِعُ، في محلِّ جرٍّ مُضَافٌ إليهِ.
(Component: TEMPLATE_C_IRAB_BOX_COMPACT)
Word: أنْ أهِيجَ
Analysis: المَصْدَرُ المُؤَوَّلُ أنْ أهيِجَ، في محلِّ نَصْبٍ مفعولٌ بِهِ.

=== BLOCK 12: Attribution (النسبة) ===
(Component: TEMPLATE_C_TABLE)
id: b15012
Title: قواعد النسبة
[TABLE_HEADERS]: <th>الاسم</th><th>نوعه</th><th>النسبة</th><th>التغيير</th>
[TABLE_ROWS]:
<tr>
    <td>مكة</td>
    <td>مختوم بتاء مربوطة</td>
    <td class="font-bold highlight-red">مَكِّيّ</td>
    <td>حُذِفَتِ التاء المربوطة.</td>
</tr>
<tr>
    <td>دير الزور</td>
    <td>مركب إضافي</td>
    <td class="font-bold highlight-red">ديريّ</td>
    <td>حُذِفَ المضاف إليه ونُسب إلى المضاف.</td>
</tr>
<tr>
    <td>حضرموت</td>
    <td>مركب مزجي</td>
    <td class="font-bold highlight-red">حضرميّ</td>
    <td>نُحتَ اسمٌ، ونُسِب إليه.</td>
</tr>
<tr>
    <td>جليل</td>
    <td>مفرد مذكّر</td>
    <td class="font-bold highlight-red">جليليّ</td>
    <td>لا تغيير (مكرَّر اللام).</td>
</tr>
<tr>
    <td>قبيلة</td>
    <td>على وزن (فعيلة)</td>
    <td class="font-bold highlight-red">قبليّ</td>
    <td>حُذِفَت الياء والتاء.</td>
</tr>
<tr>
    <td>صحراء</td>
    <td>ممدود (همزة تأنيث)</td>
    <td class="font-bold highlight-red">صحراويّ</td>
    <td>قُلِبَتْ همزته (واوًا).</td>
</tr>

=== BLOCK 13: Exam ===
(Component: TEMPLATE_C_EXAM)
id: b15013
Number: ١
Question: هات مَصْدَرَ كُلٍّ مِنَ الأفعالِ: (هدَّمَتْ، وارى، اكفهَرَّ).
Number: ٢
Question: هات مَصْدَرَ كُلٍّ مِنَ الأفعالِ الآتيةِ، واذكر نوعَهُ: (غشَّى - أَذَابَ).
Number: ٣
Question: ما مَصْدَرُ كُلٍّ مِن: (يَتَجَلَّى - يُبْدِعُ - يَتَعاطى - يَتَفَهَّمُ)؟
Number: ٤
Question: هَات مَصْدَرَ كُلٍّ مِنَ الأفعالِ الآتيةِ: (تَأَنَّى - سَرَّح - يغْلُب).
Number: ٥
Question: اذْكُرْ مَصْدَرَ كُلٍّ مِنَ الأفعالِ الآتيةِ: (ضَيَّعَنِي - يَنْجَبِلُ - أَحَارَ).

--- END STREAM ---
