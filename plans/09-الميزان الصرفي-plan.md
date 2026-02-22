# **SESSION 09.0**

[TASK DEFINITION]
Objective: Implement الميزان الصرفي.
File: `pages/09.0_nXX_الميزان الصرفي.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/09.1_...`.
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
14. after finishing the pages you must run "Jules-workspace/smart_replace_haam.py" to fix all هام , هامة mistakes !
15. every text line or raw in the page if it is more than 18 arabic words , you must wrap it into a second line or it will maybe smashed !

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER)
[LESSON_NUMBER]: 09
[CHAPTER_TITLE]: الميزان الصرفي
[CATEGORY_HEADER]: الصرف
[SECTION_HEADER]: المستوى اللغوي
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition of Sarf & Mizan ===
(Component: TEMPLATE_C_BLOCK)
Title: تعريف الصرف والميزان
Content:
<p class="text-justify leading-relaxed dir-rtl">
<span class="text-accent font-bold">الصَّرْفُ:</span> عِلْمٌ يبحثُ في بنيةِ الكلمةِ العربيَّةِ المفردةِ قبلَ أن تدخلَ في تركيبِ الكلامِ، ووزنِها، وتغيُّراتِها من شكلٍ إلى آخرٍ.
<br>
<span class="text-primary font-bold">أهمُّ مباحثهِ:</span> الميزانُ الصَّرفِيُّ للكلمةِ، معاني أحرفِ الزيادةِ، الإعلالُ، الإبدالُ، المشتقاتُ، المصادرُ.
<br><br>
<span class="text-accent font-bold">الميزانُ الصرفيُّ:</span> هو مقياسٌ لمعرفةِ حروفِ الكلمةِ، يتألَّفُ من ثلاثةِ أحرفٍ تقابلُ الأصولَ الثلاثةَ التي تتكوَّنُ منها أغلبُ الكلماتِ العربيَّةِ (ف - ع - ل).
</p>

=== BLOCK 3: The Core Matrix (3-Letter Root) ===
(Component: TEMPLATE_C_TABLE)
Title: ميزان الفعل الثلاثي (مثال: ضَحِكَ)
Columns: ["البيان", "فاء الفعل", "عين الفعل", "لام الفعل"]
Rows:
- ["الكلمة", "ضَـ", "ـحِـ", "ـكَ"]
- ["الميزان الصَّرفيُّ", "فَـ", "ـعِـ", "ـلَ"]
Footer: <p class="text-sm text-gray-600 mt-2">تطابق الحركات والسكنات بين الكلمة والميزان أمر ضروري.</p>

=== BLOCK 4: The 4-Letter Root Rule ===
(Component: TEMPLATE_C_BLOCK)
Title: ميزان الرباعي المجرد
Content:
<p class="text-justify leading-relaxed dir-rtl mb-4">
إذا كانَتْ حروفُ الكلمةِ الأصليةِ أربعةَ حروفٍ، فإنَّنا نُكرِّرُ <span class="highlight-red">اللَّامَ</span> في آخرِ الميزانِ الصَّرفيِّ (فَعْلَلَ).
</p>
(Component: TEMPLATE_C_TABLE)
Title: مثال: بَعْثَرَ
Columns: ["البيان", "فاء الفعل", "عين الفعل", "لام الفعل 1", "لام الفعل 2"]
Rows:
- ["الكلمة", "بَـ", "ـعْـ", "ـثَـ", "ـرَ"]
- ["الميزان", "فَـ", "ـعْـ", "ـلَـ", "ـلَ"]
Footer: <p class="text-sm mt-2">أمثلة إضافية: غَضَنْفَر (فَعَلَّل)، زَبَرْجَد (فَعَلَّل).</p>

=== BLOCK 5: Rules of Addition (Ziyada) ===
(Component: TEMPLATE_C_SPLIT)
[RIGHT_TITLE]: الزيادة بتكرير الأصل
[RIGHT_CONTENT]:
<p class="text-justify">
إذا كانَ الحرفُ الزائدُ ناتجًا عن تكريرِ حرفٍ أصلي، نكرر ما يقابله في الميزان.
<br>
<span class="highlight-blue">مثال:</span> سَبَّحَ &larr; فَعَّلَ
<br>
<span class="highlight-blue">مثال:</span> عَلَّمَ &larr; فَعَّلَ
</p>
[LEFT_TITLE]: الزيادة بحرف غير أصلي
[LEFT_CONTENT]:
<p class="text-justify">
إذا كان الحرف الزائد غير أصلي، نزن الأصول ونضيف الزوائد بلفظها.
<br>
<span class="highlight-blue">مثال:</span> كاتِبٌ &larr; فاعِلٌ
<br>
<span class="highlight-blue">مثال:</span> اسْتَفتَحَ &larr; اسْتَفْعَلَ
</p>

=== BLOCK 6: Weak Letters & Deletion ===
(Component: TEMPLATE_C_SPLIT)
[RIGHT_TITLE]: أحكام المعتل
[RIGHT_CONTENT]:
<p class="text-justify mb-2">يُعامل المعتل كالصحيح في الميزان:</p>
<ul class="list-disc mr-4">
    <li>وَعَدَ (معتل الفاء) &larr; فَعَلَ.</li>
    <li>قَامَ (معتل العين) &larr; فَعَلَ (وإن كانت الألف ساكنة).</li>
    <li>كَوَى (لفيف) &larr; فَعَلَ.</li>
</ul>
[LEFT_TITLE]: أحكام الحذف
[LEFT_CONTENT]:
<p class="text-justify mb-2"><span class="highlight-red">قاعدة:</span> ما يُحذف من الكلمة يُحذف ما يقابله في الميزان.</p>
<ul class="list-disc mr-4">
    <li>قُلْ (أصلها قَالَ - حذفت العين) &larr; فُلْ.</li>
    <li>ارْمِ (أصلها رَمَى - حذفت اللام) &larr; افْعِ.</li>
</ul>

=== BLOCK 7: The Doubled Root (Tip) ===
(Component: TEMPLATE_C_BENEFIT_TIP)
[BENEFIT_TITLE]: المضعف الثلاثي
[BENEFIT_TEXT]:
الحرف المشدد عبارة عن حرفين (عين ولام الفعل)، ولا يشدد في الميزان.
<br>
<span class="font-bold">مثال:</span> شَدَّ &larr; فَعَلَ.

=== BLOCK 8: Solved Applied Examples ===
(Component: TEMPLATE_C_TABLE)
Title: أمثلة تطبيقية محلولة
Columns: ["الكلمة", "الوزن الصرفي", "الملاحظات"]
Rows:
- ["قُلْتُ", "فُلْتُ", "حذف عين الفعل (الألف)"]
- ["لم يَرَ", "لم يَفَ", "حذف عين ولام الفعل"]
- ["غَدٍ", "فَعٍ", "أصلها غدو - حذف اللام"]
- ["ينقضي", "يَنْفَعِلُ", "مزيد بالهمزة والنون"]
- ["ثِقَةٌ", "عِلَةٌ", "أصلها وثق - حذف الفاء"]
- ["حاج", "فَعْلٍ", "اسم فاعل من حجّ"]
- ["بُرُوْق", "فُعُول", "جمع تكسير"]
- ["كُنْ", "فُلْ", "أمر من كان - حذف العين"]
- ["غُدوْتَ", "فَعُلْتَ", "تفكيك الإدغام إن وجد"]
- ["تخَذْتَ", "فَعِلْتُ", "صيغة افتعل محذوفة"]

=== BLOCK 9: Evaluation (Exam) ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: زن الكلمات الآتية مع ضبط الميزان بالشكل التام:
<br>
(اسْتَغْفَرَ - دَحْرَجَ - عِدْ - مَقُول - صِفَة)

--- END STREAM ---
