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
*   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-red` classes inside it.
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

=== BLOCK 2: Definitions (Split View) ===
(Component: TEMPLATE_C_SPLIT)
[LEFT_TITLE]: الاسْمُ المَنْقُوصُ
[LEFT_CONTENT]:
(Component: TEMPLATE_C_BLOCK)
Title: تعريف المنقوص
Content: <p class="text-accent">اسم مُعْرَبٌ، ينتهي <span class="highlight-red">بياء أصلية</span> مسبوقة بكسر.</p>
<p>نحو: <span class="highlight-blue">المحامي</span>، <span class="highlight-blue">الرَّاعِي</span>.</p>

[RIGHT_TITLE]: الاسْمُ المَقْصُورُ
[RIGHT_CONTENT]:
(Component: TEMPLATE_C_BLOCK)
Title: تعريف المقصور
Content: <p class="text-accent">اسم مُعْرَبٌ، ينتهي <span class="highlight-red">بألفٍ</span> قبلها فتحة.</p>
<p>نحو: <span class="highlight-blue">الهوَى</span>، <span class="highlight-blue">العصَا</span>.</p>

=== BLOCK 3: The Extended Noun (Mamdoub) ===
(Component: TEMPLATE_C_BLOCK)
Title: الاسْمُ المَمْدُودُ
Content: <p class="text-accent">اسم معرب آخرُهُ <span class="highlight-red">همزةٌ</span> بعدَ <span class="highlight-blue">ألفٍ زائدة</span>.</p>
<p>نحو: <span class="highlight-green">بناء</span>، <span class="highlight-green">حسناء</span>.</p>

=== BLOCK 4: The Core Matrix (Summary Table) ===
(Component: TEMPLATE_C_TABLE)
[TABLE_TITLE]: جدول مقارنة الأحكام
[TABLE_HEADER]:
  <th class="w-20pct">النوع</th>
  <th class="w-25pct">التعريف</th>
  <th class="w-25pct">عند التثنية</th>
  <th class="w-30pct">عند الجمع السالم</th>
[TABLE_ROWS]:
<tr>
  <td class="font-bold highlight-red">المنقوص</td>
  <td>ياء لازمة قبلها كسر</td>
  <td>تُرَدُّ الياء المحذوفة<br><span class="text-sm">(قاضٍ -> قاضيان)</span></td>
  <td>تُحْذَفُ الياء ويضم/يكسر ما قبلها<br><span class="text-sm">(الراعي -> راعُونَ/راعِين)</span></td>
</tr>
<tr>
  <td class="font-bold highlight-blue">المقصور (ثلاثي)</td>
  <td>ألف قبلها فتحة</td>
  <td>تُرَدُّ الألفُ إلى أصلها<br><span class="text-sm">(فتى -> فتيان، عصا -> عصوان)</span></td>
  <td rowspan="2">تُحْذَفُ الألفُ وتفتح ما قبلها<br><span class="text-sm">(مصطفى -> مصطفَوْن)</span></td>
</tr>
<tr>
  <td class="font-bold highlight-blue">المقصور (فوق 3)</td>
  <td>ألف قبلها فتحة</td>
  <td>تُقْلَبُ الألفُ ياءً<br><span class="text-sm">(مشفى -> مشفيان)</span></td>
</tr>
<tr>
  <td class="font-bold highlight-green">الممدود (أصلية)</td>
  <td>همزة أصلية</td>
  <td>تبقى على حالها<br><span class="text-sm">(قرّاء -> قرّاءان)</span></td>
  <td>تبقى على حالها<br><span class="text-sm">(قرّاء -> قرّاؤون)</span></td>
</tr>
<tr>
  <td class="font-bold highlight-green">الممدود (منقلبة)</td>
  <td>منقلبة عن واو/ياء</td>
  <td>تبقى أو تُقلَب واوًا<br><span class="text-sm">(دعاء -> دعاءان/دعاوَان)</span></td>
  <td>(حسب القياس)</td>
</tr>
<tr>
  <td class="font-bold highlight-green">الممدود (للتأنيث)</td>
  <td>زائدة للتأنيث</td>
  <td>تُقْلَب واوًا<br><span class="text-sm">(حسناء -> حسناوان)</span></td>
  <td>تُقْلَب واوًا<br><span class="text-sm">(حسناوات)</span></td>
</tr>

=== BLOCK 5: Deep Dive - Al-Manqoos Details ===
(Component: TEMPLATE_C_BLOCK)
Title: أحكام الاسم المنقوص التفصيلية
Content:
(Component: TEMPLATE_C_LIST)
[LIST_ITEMS]:
(Component: TEMPLATE_C_LIST_ITEM)
Content: <span class="font-bold highlight-red">حذف الياء:</span> تُحْذَفُ يَاءُ الاسم المنقوص إذا كان <span class="highlight-blue">نكرةً</span> في حالتي <span class="highlight-blue">الرفع والجر</span>.
<br>مثال: (جاءَ محامٍ، مرَرْتُ بوادٍ).

(Component: TEMPLATE_C_LIST_ITEM)
Content: <span class="font-bold highlight-green">بقاؤها:</span> تبقى ياء الاسم المنقوص في ثلاث حالات:
<br>1. إذا كان معرفاً بـ (ال): (جاء الساعي).
<br>2. إذا كان مضافاً: (جاء ساعي البريد).
<br>3. إذا كان منصوبًا بتنوين النصب: (رأيتُ ساعيًا).

=== BLOCK 6: Irab Examples (Manqoos) ===
(Component: TEMPLATE_C_IRAB_ROW)
[ROW_CONTENT]:
(Component: TEMPLATE_C_IRAB_BOX_COMPACT)
Word: محامٍ
Details: فاعل مرفوع، وعلامة رفعه الضَّمَّة المقدرة على <span class="highlight-red">الياء المحذوفة</span>؛ لأنه اسم منقوص.

(Component: TEMPLATE_C_IRAB_BOX_COMPACT)
Word: وادٍ
Details: اسم مجرور، وعلامة جرّه الكسرة المقدرة على <span class="highlight-red">الياء المحذوفة</span>؛ لأنه اسم منقوص.

=== BLOCK 7: Deep Dive - Al-Maqsur Details ===
(Component: TEMPLATE_C_BLOCK)
Title: أحكام الاسم المقصور التفصيلية
Content:
(Component: TEMPLATE_C_LIST)
[LIST_ITEMS]:
(Component: TEMPLATE_C_LIST_ITEM)
Content: <span class="font-bold highlight-red">حذف الألف (لفظًا):</span> تُحْذَفُ ألفُه لفظًا إذا كان <span class="highlight-blue">منونًا</span> بتنوين النَّصب، أو الرفع، أو الجرّ.
<br>أمثلة: (رأيتُ فتى)، (قالَ فتى)، (مررْتُ بفتًى).

(Component: TEMPLATE_C_LIST_ITEM)
Content: <span class="font-bold highlight-green">بقاؤها:</span> تبقى ألفُ الاسم المقصور لفظًا وكتابة، إذا كان معرفاً بـ (ال). نحو: الهوى.

=== BLOCK 8: Irab Example (Maqsur) ===
(Component: TEMPLATE_C_IRAB)
Word: فتى
Details: فاعلٌ مرفوعٌ، وعلامة رفعه الضَّمَّةُ المقدرة على <span class="highlight-red">الألف المحذوفة (لفظًا)</span> المثبتة كتابةً؛ لأنه اسم مقصور.

=== BLOCK 9: Deep Dive - Al-Mamdoub Types ===
(Component: TEMPLATE_C_BLOCK)
Title: أنواع همزة الممدود وتفاصيلها
Content:
(Component: TEMPLATE_C_LIST)
[LIST_ITEMS]:
(Component: TEMPLATE_C_LIST_ITEM)
Content: <span class="font-bold text-accent">أصلية:</span> مثل (قرأ: قارئ، قرّاء). <span class="highlight-green">حكمها:</span> تبقى على حالها في المثنى والجمع السالم.

(Component: TEMPLATE_C_LIST_ITEM)
Content: <span class="font-bold text-accent">منقلبة عن واو أو ياء:</span> مثل (دعا، يدعو: دعاو، دعاء) أو (بنى، يبني: بناي، بناء). <span class="highlight-green">حكمها:</span> تبقى على حالها، أو تُرَدُّ إلى أصلها (واوًا أو ياءً).

(Component: TEMPLATE_C_LIST_ITEM)
Content: <span class="font-bold text-accent">زائدة للتأنيث:</span> مثل (حَسُنَ: حسناء). <span class="highlight-green">حكمها:</span> تقلب واوًا عند التثنية والجمع.

=== BLOCK 10: Solved Exam Models ===
(Component: TEMPLATE_C_BLOCK)
Title: نماذج امتحانية محلولة (دورات سابقة)
Content:
(Component: TEMPLATE_C_TABLE)
[TABLE_TITLE]: نماذج إعرابية وصرفية
[TABLE_HEADER]:
  <th class="w-30pct">السؤال (الدورة)</th>
  <th class="w-70pct">الجواب النموذجي</th>
[TABLE_ROWS]:
<tr>
  <td class="font-bold">2013 علمي (أولى)<br>نوع (نِضال) ووزن (أَنْزَلْتُهُ)</td>
  <td>نِضال: اسم جامد معنى.<br>وزْنُ (أَنْزَلْتُهُ): أَفْعَلْتُهُ.</td>
</tr>
<tr>
  <td class="font-bold">2013 علمي (ثانية)<br>العلة في (يسقي) ووزن (شفيتم)</td>
  <td>العلة في (يسقي): إعلال بالتسكين.<br>وزن (شَفَيْتُم): (فَعَلْتُم).</td>
</tr>
<tr>
  <td class="font-bold">2014 علمي (أولى)<br>العلة في (كانت) ووزن (اختاروا)</td>
  <td>العلة في (كانت): إعلال بالقلب.<br>وزن (اختاروا): افتعلوا.</td>
</tr>
<tr>
  <td class="font-bold">2014 علمي (ثانية)<br>العلة في (يقى) ووزن (ينطلق)</td>
  <td>العلة في (يقى): إعلالٌ بالقلب.<br>وزن (ينطلق): ينفعل.</td>
</tr>

=== BLOCK 11: Final Evaluation ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: ما نوع الهمزة في كلمة (صحراء) وما حكمها عند التثنية؟
Number: ٢
Question: ثنِّ كلمة (قاضٍ) في حالة الرفع، وكلمة (عصا) في حالة النصب.

--- END STREAM ---
