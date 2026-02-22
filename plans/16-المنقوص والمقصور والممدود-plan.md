# **SESSION 16.0**

[TASK DEFINITION]
Objective: Implement المنقوص والمقصور والممدود.
File: `pages/16.0_nXX_المنقوص والمقصور والممدود.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/16.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 16
[CHAPTER_TITLE]: المنقوص والمقصور والممدود
[CATEGORY_HEADER]: الصرف
[SECTION_HEADER]: المستوى اللغوي
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Ism Manqous Definition ===
(Component: TEMPLATE_C_BLOCK)
Title: الاسمُ المنقوصُ
Content:
<p class="text-accent">هو اسمٌ مُعْرَبٌ، ينتهي بياءٍ أصليةٍ مسبوقةٍ بكسرٍ.</p>
<p class="mt-2mm"><strong>أمثلة:</strong> <span class="highlight-red">المحامِي</span>، <span class="highlight-red">الرَّاعِي</span>.</p>

=== BLOCK 3: Manqous Rules (Deletion vs Retention) ===
(Component: TEMPLATE_C_SPLIT)
[LEFT_TITLE]: ثبوتُ الياء
[RIGHT_TITLE]: حذفُ الياء
[LEFT_CONTENT]:
<ul class="structured-list">
    <li>
        <span class="list-item-content">تبقى الياءُ في ثلاثِ حالاتٍ:</span>
        <ul class="structured-list mt-1mm">
            <li><span class="list-item-content">إذا كان مُعَرَّفاً بـ (ال): <span class="highlight-green">جاءَ الساعي</span>.</span></li>
            <li><span class="list-item-content">إذا كان مُضَافاً: <span class="highlight-green">جاءَ ساعي البريدِ</span>.</span></li>
            <li><span class="list-item-content">إذا كان منصوباً بتنوينِ النصبِ: <span class="highlight-green">رأيتُ ساعياً</span>.</span></li>
        </ul>
    </li>
</ul>
[RIGHT_CONTENT]:
<ul class="structured-list">
    <li>
        <span class="list-item-content">تُحذَفُ ياءُ الاسمِ المنقوصِ إذا كان <span class="highlight-red">نكرةً</span> في حالتي الرفع والجر.</span>
        <ul class="structured-list mt-1mm">
            <li><span class="list-item-content">الرفع: <span class="highlight-red">جاءَ محامٍ</span> (فاعل مرفوع بضمة مقدرة على الياء المحذوفة).</span></li>
            <li><span class="list-item-content">الجر: <span class="highlight-red">مرَرْتُ بوادٍ</span> (اسم مجرور بكسرة مقدرة على الياء المحذوفة).</span></li>
        </ul>
    </li>
</ul>

=== BLOCK 4: Manqous Dual & Plural ===
(Component: TEMPLATE_C_TABLE)
Title: تثنيةُ وجمعُ الاسمِ المنقوصِ
[TABLE_HEADERS]:
<th>الحالة</th>
<th>القاعدة</th>
<th>مثال</th>
[TABLE_ROWS]:
<tr>
    <td class="font-bold text-center">التثنية</td>
    <td>تُرَدُّ الياءُ المحذوفةُ.</td>
    <td>جاء <span class="highlight-blue">قاضٍ</span> ← جاء <span class="highlight-green">قاضيان</span>.</td>
</tr>
<tr>
    <td class="font-bold text-center">جمع المذكر السالم</td>
    <td>تُحذَفُ الياءُ ويُضَمُّ ما قبلَ الواوِ أو يُكسَرُ ما قبلَ الياءِ.</td>
    <td>جاءَ <span class="highlight-red">راعُونَ</span>، رأيتُ <span class="highlight-red">راعِين</span>.</td>
</tr>

=== BLOCK 5: Ism Maqsour Definition ===
(Component: TEMPLATE_C_BLOCK)
Title: الاسمُ المقصورُ
Content:
<p class="text-accent">هو اسمٌ مُعْرَبٌ، ينتهي بألفٍ لازمةٍ قبلها فتحةٌ.</p>
<p class="mt-2mm"><strong>أمثلة:</strong> <span class="highlight-red">الهوَى</span>، <span class="highlight-red">العصَا</span>.</p>
<p class="mt-2mm"><strong>قاعدة الإعراب:</strong> تُحذَفُ ألفُهُ لفظاً إذا كان مُنَوَّناً (تنويناً، نصباً، أو جراً) ولكن تبقى كتابةً.</p>
<ul class="structured-list mt-1mm">
    <li><span class="list-item-content">مثال: <span class="highlight-blue">قالَ فتىً</span> (فاعل مرفوع بضمة مقدرة على الألف المحذوفة لفظاً المثبتة كتابةً).</span></li>
</ul>

=== BLOCK 6: Maqsour Rules Matrix ===
(Component: TEMPLATE_C_TABLE)
Title: تثنيةُ وجمعُ الاسمِ المقصورِ
[TABLE_HEADERS]:
<th>الحالة</th>
<th>الاسم الثلاثي</th>
<th>الاسم فوق الثلاثي</th>
[TABLE_ROWS]:
<tr>
    <td class="font-bold text-center">التثنية / جمع المؤنث</td>
    <td>
        تُرَدُّ الألفُ إلى أصلها (واو أو ياء).<br>
        <span class="highlight-green">عصا ← عصوان</span><br>
        <span class="highlight-green">فتى ← فتيان/فتيات</span>
    </td>
    <td>
        تُقلَبُ الألفُ ياءً دائماً.<br>
        <span class="highlight-green">مشفى ← مشفيان/مشفيات</span>
    </td>
</tr>
<tr>
    <td class="font-bold text-center">جمع المذكر السالم</td>
    <td colspan="2" class="text-center">
        تُحذَفُ الألفُ، وتظلُّ الفتحةُ قبلَ الواوِ أو الياءِ للدلالةِ عليها.<br>
        <span class="highlight-red">مصطفى ← مصطفَوْن / مصطفَيْن</span>
    </td>
</tr>

=== BLOCK 7: Ism Mamdoud Definition & Types ===
(Component: TEMPLATE_C_BLOCK)
Title: الاسمُ الممدودُ
Content:
<p class="text-accent">هو اسمٌ مُعْرَبٌ آخِرُهُ همزةٌ بعدَ ألفٍ زائدةٍ: <span class="highlight-blue">بناء، حسناء</span>.</p>
<p class="mt-2mm">وللهمزةِ في الاسمِ الممدودِ ثلاثةُ أنواعٍ تُؤثِّرُ في تثنيتِه وجمعِه.</p>

=== BLOCK 8: Mamdoud Rules Matrix ===
(Component: TEMPLATE_C_TABLE)
Title: أحكامُ همزةِ الممدودِ عندَ التثنيةِ والجمعِ
[TABLE_HEADERS]:
<th>نوع الهمزة</th>
<th>الحكم</th>
<th>المثال</th>
[TABLE_ROWS]:
<tr>
    <td class="font-bold text-center">أصلية</td>
    <td>تبقى على حالها.</td>
    <td><span class="highlight-green">قُرَّاء ← قُرَّاءان</span></td>
</tr>
<tr>
    <td class="font-bold text-center">منقلبة (عن واو/ياء)</td>
    <td>يجوزُ بقاؤها أو قلبها واواً.</td>
    <td>
        <span class="highlight-green">دُعاء ← دُعاءان / دُعاوَان</span><br>
        <span class="highlight-green">بِناء ← بِناءان / بِنايان</span>
    </td>
</tr>
<tr>
    <td class="font-bold text-center">زائدة للتأنيث</td>
    <td>تُقلَبُ واواً وجوباً.</td>
    <td><span class="highlight-red">حسناء ← حسناوان</span> (وليس حسناءان)</td>
</tr>

=== BLOCK 9: Applications (Solved Ministry Questions) ===
(Component: TEMPLATE_C_BLOCK)
Title: تطبيقاتٌ وزاريةٌ محلولةٌ
Content:
<div class="bg-grey-lighter p-2mm rounded mb-2mm">
    <p class="font-bold text-accent mb-1mm">دورة 2013 (علمي):</p>
    <ul class="structured-list">
        <li><span class="list-item-content"><strong>السؤال:</strong> ما العِلَّةُ الصَّرفيَّةُ في كلمة (يسقي)؟ وما وزن كلمة (شفيتم)؟</span></li>
        <li><span class="list-item-content"><strong>الجواب:</strong> (يسقي): إعلالٌ بالتّسكين. (شَفَيْتُم): فَعَلْتُم.</span></li>
    </ul>
</div>
<div class="bg-grey-lighter p-2mm rounded mb-2mm">
    <p class="font-bold text-accent mb-1mm">دورة 2014 (علمي):</p>
    <ul class="structured-list">
        <li><span class="list-item-content"><strong>السؤال:</strong> ما العلَّة الصَّرْفيَّة في كلمة (كانتْ)؟ وما وزن كلمة (اختاروا)؟</span></li>
        <li><span class="list-item-content"><strong>الجواب:</strong> (كانتْ): إعلال بالقلب. (اختاروا): افتعلوا.</span></li>
    </ul>
</div>
<div class="bg-grey-lighter p-2mm rounded">
    <p class="font-bold text-accent mb-1mm">دورة 2014 (الثانية):</p>
    <ul class="structured-list">
        <li><span class="list-item-content"><strong>السؤال:</strong> العِلَّةُ الصَّرفيَّةُ في (يقى): .........، وزْنُ (ينطلق): ........</span></li>
        <li><span class="list-item-content"><strong>الجواب:</strong> (يقى): إعلالٌ بالقلب. (ينطلق): ينفعل.</span></li>
    </ul>
</div>

=== BLOCK 10: Exam ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: املأ الفراغ بما يُناسِبُه: (نِضال) اسمٌ جامدٌ نوعُهُ: ........ - وزْنُ كلمةِ (أَنْزَلْتُهُ): ........
Number: ٢
Question: ثَنِّ الأسماءَ الآتيةَ واذكرِ التغييرَ الحاصلَ: (داعٍ - عصا - صحراء).
Number: ٣
Question: اجعل الاسمَ المقصورَ (مصطفى) جمعَ مذكرٍ سالماً في جملةٍ مفيدةٍ واضبطهُ بالشكلِ.

--- END STREAM ---
