# **SESSION 24.0**

[TASK DEFINITION]
Objective: Implement أشهر مواطن الفصل والوصل.
File: `pages/24.0_nXX_أشهر مواطن الفصل والوصل.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/24.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 24
[CHAPTER_TITLE]: أشهر مواطن الفصل والوصل
[CATEGORY_HEADER]: الإملاء
[SECTION_HEADER]: المستوى اللغوي
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition & Rule (Ma) ===
(Component: TEMPLATE_C_BLOCK)
Title: أحكام (ما) الاسميَّة والحرفيَّة
Content:
<p class="text-accent">تُكْتَبُ (ما) <strong>مفصولَةً</strong> إذا جاءَتْ بمعنى الاسمِ الموصولِ بعَدَ (إِنَّ، كُلَّ، أينَ )، وتُكتبُ <strong>موصولةً</strong> إذا جاءَتْ بعدَ (إِنَّ) الحرفِ المُشبَّهِ بالفعلِ وتكُفُّهُ عَنِ العملِ، كما تتصلُ بـ (أينَ، وكُلَّ) في أسلوبِ الشَّرطِ.</p>

=== BLOCK 3: Summary Matrix ===
(Component: TEMPLATE_C_TABLE)
Title: ملخص مواطن الفصل والوصل
[TABLE_HEADERS]: <th>الأداة</th><th>الحالة والقاعدة</th><th>المثال</th>
[TABLE_ROWS]:
(Component: TEMPLATE_C_TABLE_ROW)
[CELL_1]: (ما)
[CELL_2]: <span class="text-red font-bold">مفصولة</span>: إذا كانت اسماً موصولاً بعد (إنَّ، كلَّ، أينَ)
[CELL_3]: إِنَّ <span class="highlight-red">ما</span> تقولُهُ الصِّدْقُ

(Component: TEMPLATE_C_TABLE_ROW)
[CELL_1]: (ما)
[CELL_2]: <span class="text-green font-bold">موصولة</span>: إذا كانت كافَّةً أو شرطيَّةً بعد (إنَّ، أينَ، كلَّ)
[CELL_3]: إنَّ<span class="highlight-green">ما</span> الباطلُ زاهِقٌ

(Component: TEMPLATE_C_TABLE_ROW)
[CELL_1]: (لا)
[CELL_2]: <span class="text-green font-bold">موصولة</span>: بعد (أنْ) الناصبة، أو بعد (كي) المسبوقة باللام
[CELL_3]: ألا، لكيلا

(Component: TEMPLATE_C_TABLE_ROW)
[CELL_1]: (لا)
[CELL_2]: <span class="text-red font-bold">مفصولة</span>: بعد (أنْ) المخففة، أو بعد (كي) غير المسبوقة باللام
[CELL_3]: أن لا، كي لا

(Component: TEMPLATE_C_TABLE_ROW)
[CELL_1]: الظروف
[CELL_2]: <span class="text-green font-bold">موصولة</span>: بـ (إذْ) إذا نُوِّنَ الظرفُ
[CELL_3]: يومئذٍ

(Component: TEMPLATE_C_TABLE_ROW)
[CELL_1]: الظروف
[CELL_2]: <span class="text-red font-bold">مفصولة</span>: بـ (إذْ) إذا لم يُنوَّنْ
[CELL_3]: يومَ إذْ

(Component: TEMPLATE_C_TABLE_ROW)
[CELL_1]: العدد (٣-٩)
[CELL_2]: <span class="text-green font-bold">جائز الوجهين</span>: الوصل أو الفصل بـ (مئة)
[CELL_3]: ثلاثمئة / ثلاث مئة

=== BLOCK 4: Deep Dive - La ===
(Component: TEMPLATE_C_SPLIT)
[LEFT_TITLE]: (لا) النافية مع (أنْ)
[LEFT_CONTENT]:
(Component: TEMPLATE_C_LIST)
Title:
[LIST_ITEMS]:
(Component: TEMPLATE_C_LIST_ITEM)
[MARKER]: ✅
[CONTENT]: <strong>موصولة ومُدغمة (ألَّا):</strong> إذا جاءت (أنْ) ناصبةً للفعل المضارع.
<br>Example: <span class="highlight-green">أريدُ ألَّا أتأخَرَ عَنِ الموعدِ</span>.

(Component: TEMPLATE_C_LIST_ITEM)
[MARKER]: ❌
[CONTENT]: <strong>مفصولة (أنْ لا):</strong> إذا جاءت (أنْ) مخففةً من الثقيلة (غير ناصبة).
<br>Example: <span class="highlight-red">اعلمْ أنْ لا فائدةَ مِنَ الكذِبِ</span>.

[RIGHT_TITLE]: (لا) النافية مع (كي)
[RIGHT_CONTENT]:
(Component: TEMPLATE_C_LIST)
Title:
[LIST_ITEMS]:
(Component: TEMPLATE_C_LIST_ITEM)
[MARKER]: ✅
[CONTENT]: <strong>موصولة (لكيلا):</strong> إذا اقترنت (كي) بحرف الجر (اللام).
<br>Example: <span class="highlight-green">أذهبُ لِكيلا أبقى فريسَةً للجهلِ</span>.

(Component: TEMPLATE_C_LIST_ITEM)
[MARKER]: ❌
[CONTENT]: <strong>مفصولة (كي لا):</strong> إذا لم تسبقها اللام الجارة.
<br>Example: <span class="highlight-red">كي لا أعكِّرَ الصَّفاءَ</span>.

=== BLOCK 5: Deep Dive - Adverbs & Numbers ===
(Component: TEMPLATE_C_SPLIT)
[LEFT_TITLE]: الظروف مع (إذْ)
[LEFT_CONTENT]:
(Component: TEMPLATE_C_LIST)
Title:
[LIST_ITEMS]:
(Component: TEMPLATE_C_LIST_ITEM)
[MARKER]: 🔹
[CONTENT]: <strong>موصولة:</strong> إذا جاء الظرف منوناً (يومئذٍ، حينئذٍ، وقتئذٍ).

(Component: TEMPLATE_C_LIST_ITEM)
[MARKER]: 🔸
[CONTENT]: <strong>مفصولة:</strong> إذا لم يُنوَّن الظرف (يومَ إذْ، حينَ إذْ، وقتَ إذْ).

[RIGHT_TITLE]: الأعداد مع (مئة)
[RIGHT_CONTENT]:
<p class="text-justify">يجوز في الأعداد من (٣) إلى (٩) وجهان عند إضافتها إلى (مئة):</p>
(Component: TEMPLATE_C_LIST)
Title:
[LIST_ITEMS]:
(Component: TEMPLATE_C_LIST_ITEM)
[MARKER]: ١
[CONTENT]: <strong>الوصل:</strong> (ثلاثمئة، أربعمئة، خمسمئة...).

(Component: TEMPLATE_C_LIST_ITEM)
[MARKER]: ٢
[CONTENT]: <strong>الفصل:</strong> (ثلاث مئة، أربع مئة، خمس مئة...).

=== BLOCK 6: Benefit Tip ===
(Component: TEMPLATE_C_BENEFIT_TIP)
Title: فائدة إملائية
Content:
اعلم أن المعنى هو الحَكَم في الفصل والوصل، ففي قولنا (إن ما فعلته رائع) فُصلت (ما) لأنها اسم موصول بمعنى (الذي)، أما في قولنا (إنما المؤمنون إخوة) وُصلت لأنها (كافة) كفّت (إن) عن العمل وحصرت المعنى.

=== BLOCK 7: Evidence ===
(Component: TEMPLATE_C_IRAB_ROW)
[BOXES]:
(Component: TEMPLATE_C_IRAB_BOX)
[WORD]: يومئذٍ
[DETAILS]: ظرف زمان منصوب، و(إذٍ) مضاف إليه مجرور، وُصلت الكلمتان لكثرة الاستعمال وتنوين الظرف.

(Component: TEMPLATE_C_IRAB_BOX)
[WORD]: يومَ إذْ
[DETAILS]: ظرف زمان منصوب، و(إذْ) مضاف إليه مبني على السكون، فُصلت لعدم تنوين الظرف.

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: بيّن سبب كتابة (ما) موصولة أو مفصولة في الجملتين الآتيتين: (أحبُّ كلَّ ما يصدر عنك - كلَّما زرتني أكرمتك).

Number: ٢
Question: صوّب الخطأ الإملائي في الجملة الآتية مع التعليل: (سافرت ل كي لا أتأخر).

--- END STREAM ---
