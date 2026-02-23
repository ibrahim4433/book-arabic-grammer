# **SESSION 22.0**

[TASK DEFINITION]
Objective: Implement كسر همزة (إنّ) وفتح همزة (أنّ).
File: `pages/22.0_nXX_كسر همزة (إنّ) وفتح همزة (أنّ).html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/22.1_...` if page have a lot of blank space add exam elements from the lesson.
3. text Content: 100% Arabic with full Harakat.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green` for secondary.
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
[LESSON_NUMBER]: 22
[CHAPTER_TITLE]: كسر همزة (إنّ) وفتح همزة (أنّ)
[CATEGORY_HEADER]: الإملاء
[SECTION_HEADER]: المستوى اللغوي
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition ===
(Component: TEMPLATE_C_BLOCK)
Title: الفرق بين (إنّ) و (أنّ)
Content:
<p class="text-justify leading-loose text-accent">
تختص <span class="highlight-red font-bold">(إنّ)</span> بكسر الهمزة بأنها تأتي في جملة مستقلة، بينما <span class="highlight-red font-bold">(أنّ)</span> بفتح الهمزة تأتي كجزء من جملة أخرى وتُؤَوَّلُ مع معموليها بمصدر.
</p>

=== BLOCK 3: Detailed Breakdown - Kasr (Breaking) ===
(Component: TEMPLATE_C_SPLIT)
[LEFT_TITLE]: مواضع كسر همزة (إنّ) وجوباً
[LEFT_CONTENT]:
(Component: TEMPLATE_C_LIST)
Title: الحالات الأربع
Content:
<div class="list-item-content">
1. إذا جاءت في <span class="highlight-blue font-bold">بَدْءِ الكَلامِ</span>.
</div>
<div class="list-item-content">
2. إذا جاءت بعد <span class="highlight-blue font-bold">القَوْلِ</span> (مقول القول).
</div>
<div class="list-item-content">
3. إذا جاءت بعد <span class="highlight-blue font-bold">القَسَمِ</span> (جواب القسم).
</div>
<div class="list-item-content">
4. إذا وقَعتِ <span class="highlight-blue font-bold">اللامُ المُزَحْلَقَةُ</span> في خَبَرِهَا.
</div>

[RIGHT_TITLE]: أمثلة توضيحية
[RIGHT_CONTENT]:
(Component: TEMPLATE_C_LIST)
Title: شواهد
Content:
<div class="list-item-content">
1. <span class="highlight-red font-bold">إِنَّا</span> أَعْطَيْنَاكَ الكَوْثَرَ. (أول الكلام)
</div>
<div class="list-item-content">
2. قَالَ: <span class="highlight-red font-bold">إِنِّي</span> عَبْدُ اللهِ. (بعد القول)
</div>
<div class="list-item-content">
3. وَاللهِ <span class="highlight-red font-bold">إِنَّ</span> الحَقَّ مُنْتَصِرٌ. (بعد القسم)
</div>
<div class="list-item-content">
4. <span class="highlight-red font-bold">إِنَّكَ</span> لَعَلَى خُلُقٍ عَظِيمٍ. (اللام المزحلقة)
</div>

=== BLOCK 4: Detailed Breakdown - Fath (Opening) ===
(Component: TEMPLATE_C_BLOCK)
Title: مواضع فتح همزة (أنّ) وجوباً
Content:
<p class="text-justify leading-loose text-accent">
تُفْتَحُ همزةُ <span class="highlight-red font-bold">(أَنَّ)</span> إذا أمكنَ تأويلُها مَعَ اسمها وخبرها <span class="highlight-blue font-bold">بِمَصْدَرٍ صَرِيحٍ</span> (المصدر المؤول).
</p>
<div class="mt-4mm">
<p class="font-bold text-teal mb-2mm">أمثلة وتطبيق:</p>
(Component: TEMPLATE_C_CHIPS)
Title: أمثلة التأويل
Content:
<div class="chip bg-grey-lighter rounded p-1mm m-1mm">
عَلِمْتُ <span class="highlight-red">أَنَّكَ مُسَافِرٌ</span> = عَلِمْتُ <span class="highlight-green">سَفَرَكَ</span>
</div>
<div class="chip bg-grey-lighter rounded p-1mm m-1mm">
سَرَّنِي <span class="highlight-red">أَنَّكَ نَاجِحٌ</span> = سَرَّنِي <span class="highlight-green">نَجَاحُكَ</span>
</div>
<div class="chip bg-grey-lighter rounded p-1mm m-1mm">
بَلَغَنِي <span class="highlight-red">أَنَّ القَوْمَ قَادِمُونَ</span> = بَلَغَنِي <span class="highlight-green">قُدُومُ القَوْمِ</span>
</div>
</div>

=== BLOCK 5: Benefit Box ===
(Component: TEMPLATE_C_BENEFIT_TIP)
Title: فائدة إملائية (اللام المزحلقة)
Content:
<p class="text-justify leading-loose">
تسمى اللام التي تدخل على خبر (إنّ) المكسورة الهمزة بـ <span class="highlight-blue font-bold">اللامِ المُزَحْلَقَةِ</span>، وهي لام التوكيد التي زُحْلِقَتْ من صدر الجملة كراهة توالي مؤكدين (إنّ واللام)، ووجودها يوجب كسر همزة (إنّ).
</p>

=== BLOCK 6: The Core Matrix (Summary) ===
(Component: TEMPLATE_C_TABLE)
Title: خلاصة أحكام همزة (إنّ)
[TABLE_HEADERS]:
<th>الحالة (الموضع)</th>
<th>حكم الهمزة</th>
<th>مثال تطبيقي</th>
[TABLE_ROWS]:
(Component: TEMPLATE_C_TABLE_ROW)
Content:
<td>في ابتداء الكلام</td>
<td><span class="highlight-red font-bold">الكسر وجوباً</span></td>
<td><span class="highlight-green">إِنَّ</span> اللهَ غَفُورٌ رَحِيمٌ.</td>
(Component: TEMPLATE_C_TABLE_ROW)
Content:
<td>بعد القول (قال/يقول)</td>
<td><span class="highlight-red font-bold">الكسر وجوباً</span></td>
<td>قُلْتُ: <span class="highlight-green">إِنَّ</span> الجَوَّ بَدِيعٌ.</td>
(Component: TEMPLATE_C_TABLE_ROW)
Content:
<td>بعد القسم (والله/تالله)</td>
<td><span class="highlight-red font-bold">الكسر وجوباً</span></td>
<td>وَاللهِ <span class="highlight-green">إِنَّ</span> الصَّبْرَ مِفْتَاحُ الفَرَجِ.</td>
(Component: TEMPLATE_C_TABLE_ROW)
Content:
<td>اقتران الخبر باللام</td>
<td><span class="highlight-red font-bold">الكسر وجوباً</span></td>
<td><span class="highlight-green">إِنَّ</span> زَيْداً لَكَرِيمٌ.</td>
(Component: TEMPLATE_C_TABLE_ROW)
Content:
<td>صحّة التأويل بمصدر</td>
<td><span class="highlight-blue font-bold">الفتح وجوباً</span></td>
<td>يَسُرُّنِي <span class="highlight-green">أَنَّكَ</span> مُجْتَهِدٌ.</td>

=== BLOCK 7: Evidence (Irab) ===
(Component: TEMPLATE_C_IRAB_ROW)
Title: نموذج إعرابي
Content:
(Component: TEMPLATE_C_IRAB_BOX)
Word: إِنِّي
Details:
<div class="irab-details">
<span class="highlight-red font-bold">إنّ:</span> حرف مشبه بالفعل يفيد التوكيد، وكسرت همزته لوقوعه في ابتداء الكلام (أو بعد القول/القسم بحسب الجملة).
<br>
<span class="highlight-blue font-bold">الياء:</span> ضمير متصل مبني في محل نصب اسم (إنّ).
</div>
(Component: TEMPLATE_C_IRAB_BOX)
Word: عَبْدُ
Details:
<div class="irab-details">
خبر (إنّ) مرفوع وعلامة رفعه الضمة الظاهرة على آخره، وهو مضاف.
</div>

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: بيّن سبب كسر همزة (إنّ) في قوله تعالى: ((إِنَّا أَعْطَيْنَاكَ الْكَوْثَرَ)).

Number: ٢
Question: حوّل المصدر المؤول إلى مصدر صريح في الجملة: (أَعْجَبَنِي أَنَّكَ صَادِقٌ).

--- END STREAM ---
