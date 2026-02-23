# **SESSION 17.0**

[TASK DEFINITION]
Objective: Implement الهمزة الأولية.
File: `pages/17.0_nXX_الهمزة الأولية.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/17.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 17
[CHAPTER_TITLE]: الهمزة الأولية
[CATEGORY_HEADER]: الإملاء
[SECTION_HEADER]: المستوى اللغوي
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Hamzat Wasl Definition ===
(Component: TEMPLATE_C_BLOCK)
Title: همزة الوصل
Content: هي <span class="text-accent">همزةٌ أوّليّةٌ زائدةٌ</span>، تُلفَظُ في أوّلِ الكلامِ وتُكتَبُ ألِفَ وصلٍ، ولا تُلفَظُ في دَرْجِهِ، مثل: <span class="highlight-red">ا</span>ستعانَ، <span class="highlight-red">ا</span>حسَبْ، <span class="highlight-red">ا</span>رتفاع.

=== BLOCK 3: Wasl Positions Matrix ===
(Component: TEMPLATE_C_TABLE)
Title: مواضع كتابة همزة الوصل
[HEADERS]: الموضع | المثال
[ROW]: أمرُ الفعلِ الثّلاثيّ | <span class="highlight-red">ا</span>شرَبْ، <span class="highlight-red">ا</span>كتُبْ
[ROW]: ماضي الخماسيّ والسّداسيّ، وأمرُهما، ومصدرُهما | <span class="highlight-red">ا</span>ستلمَ، <span class="highlight-red">ا</span>ستلِمْ، <span class="highlight-red">ا</span>ستلام، <span class="highlight-red">ا</span>ستقبلَ، <span class="highlight-red">ا</span>ستقبِلْ، <span class="highlight-red">ا</span>ستقبال
[ROW]: الأسماءُ العشرةُ | <span class="highlight-red">ا</span>سم، <span class="highlight-red">ا</span>بن، <span class="highlight-red">ا</span>بنة، <span class="highlight-red">ا</span>ثنان، <span class="highlight-red">ا</span>ثنتان، <span class="highlight-red">ا</span>مرؤ، <span class="highlight-red">ا</span>مرأة، <span class="highlight-red">ا</span>يمُ الله، <span class="highlight-red">ا</span>يمَنُ الله
[ROW]: (ال) التّعريف | <span class="highlight-red">ال</span>كتاب، <span class="highlight-red">ال</span>مدرسة

=== BLOCK 4: Reasoning Examples ===
(Component: TEMPLATE_C_BLOCK)
Title: نموذج تعليل الهمزة
Content:
<span class="font-bold text-accent">انظُرْ:</span> كُتِبتِ الهمزةُ ألفَ وصلٍ؛ لأنّها جاءتْ في أوّلِ فعلِ أمرٍ مأخوذٍ من فعلٍ ثلاثيّ.<br>
<span class="font-bold text-accent">انتشَرَ:</span> كُتِبتِ الهمزةُ ألفَ وصلٍ؛ لأنّها جاءتْ في أوّلِ فعلٍ ماضٍ خماسيّ.<br>
<span class="font-bold text-accent">ابتهاج:</span> كُتِبتِ الهمزةُ ألفَ وصلٍ؛ لأنّها جاءتْ في أوّلِ مصدرٍ خماسيّ.

=== BLOCK 5: Hamzat Qat Definition ===
(Component: TEMPLATE_C_BLOCK)
Title: همزة القطع
Content: هي <span class="text-accent">همزةٌ أوليّةٌ تُلفَظُ وتُكتَبُ في أوّلِ الكلامِ</span>، ولا يمكنُ الاستغناءُ عنها، وتكونُ همزتُها فوقَ الألفِ إذا لُفِظَتْ مضمومةً أو مفتوحةً (<span class="highlight-red">أُ</span>، <span class="highlight-red">أَ</span>)، وتحتَ الألفِ إذا لُفِظَتْ مكسورةً (<span class="highlight-red">إِ</span>).

=== BLOCK 6: Qat Types Matrix ===
(Component: TEMPLATE_C_TABLE)
Title: نوعا همزة القطع
[HEADERS]: النّوع | الشّرح | الأمثلة
[ROW]: أصلية | إذا كانت حرفاً أصليّاً في الكلمة، ولا يقومُ معناها من دونِه. | <span class="highlight-red">أ</span>خذَ، <span class="highlight-red">أ</span>مَلَ، <span class="highlight-red">إ</span>نّ
[ROW]: زائدة | في أوّلِ الفعلِ الماضي الرّباعيّ وأمرِه ومصدرِه، وفي أوّلِ الفعلِ المضارعِ المسندِ إلى الضّميرِ (أنا). | <span class="highlight-red">أ</span>قبلَ، <span class="highlight-red">أ</span>قْبِلْ، <span class="highlight-red">إ</span>قبالٌ، <span class="highlight-red">أ</span>عْلَمُ، <span class="highlight-red">أ</span>ستعْجِلُ

=== BLOCK 7: Important Alerts ===
(Component: TEMPLATE_C_BENEFIT_WARNING)
Title: تنبيهات هامة
Content:
١- تُحْذَفُ همزةُ (ال) التّعريفِ إذا دخلتْ عليها اللّامُ الجارّةُ أو لامُ الابتداءِ: السّماء ⬅ <span class="highlight-red">للسّماءِ</span>، البيتُ ⬅ <span class="highlight-red">لَلبيتُ</span>. أمّا إذا دخلتِ اللّامُ على اسمٍ معرّفٍ بـ (ال) مبدوءٍ بلامٍ، فتُحذَفُ (ال) تجنّبًا لتوالي الأمثالِ: (لـ + اللّغة = <span class="highlight-red">للّغة</span>).<br>
٢- تُحْذَفُ همزةُ (ابن)، و(ابنة) إذا وقعتا بينَ اسمينِ علمينِ الثّاني منهما أبٌ للأوّلِ، أو جدٌّ له، نحو: (خالدُ <span class="highlight-red">بنُ</span> الوليد، خولةُ <span class="highlight-red">بنتُ</span> الأزور، عمر <span class="highlight-red">بن</span> أبي ربيعة)، أو بعدَ النّداءِ أو بعدَ همزةِ الاستفهامِ، نحو: (يا <span class="highlight-red">بن</span> الأكرمين، <span class="highlight-red">أبنُ</span> عبدِ الله؟).<br>
٣- تُحْذَفُ همزةُ (اسم) في البسملةِ الكاملةِ: <span class="highlight-red">بسمِ</span> اللهِ الرّحمنِ الرّحيمِ.

=== BLOCK 8: Interaction with Hamzat Istifham ===
(Component: TEMPLATE_C_TABLE)
Title: اجتماع الهمزة الأوّليّة مع همزة الاستفهام
[HEADERS]: همزة الاستفهام | الكلمة | الحالة | المثال
[ROW]: <span class="highlight-blue">أ</span> | مبدوءة بهمزة وصل | تُحذف همزة الوصل | <span class="highlight-blue">أ</span> + ابن = <span class="highlight-red">أ</span>بن ؟، <span class="highlight-blue">أ</span> + انكسرَ = <span class="highlight-red">أ</span>نكسرَ؟
[ROW]: <span class="highlight-blue">أ</span> | مبدوءة بـ (ال) التعريف | تتحول الهمزتان إلى مدّة | <span class="highlight-blue">أ</span> + العِلمُ حياةٌ = <span class="highlight-red">آ</span>لعِلمُ حياةٌ؟
[ROW]: <span class="highlight-blue">أ</span> | فعل أوله همزة قطع | تتحول همزة القطع إلى متوسطة | <span class="highlight-blue">أ</span> + أؤدي واجبي = <span class="highlight-red">أؤ</span>ؤدي واجبي؟
[ROW]: <span class="highlight-blue">أ</span> | اسم أو حرف أولهما همزة قطع | تبقى همزة القطع على حالها | <span class="highlight-blue">أ</span> + إلى السوق = <span class="highlight-red">أإ</span>لى السوق؟<br><span class="highlight-blue">أ</span> + أحلام = <span class="highlight-red">أأ</span>حلام؟

=== BLOCK 9: Exam ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: علّل كتابة الهمزة في الكلمات الآتية: (استخرجَ، إكرام، ابن).
Number: ٢
Question: أدخل همزة الاستفهام على الجمل الآتية وغيّر ما يلزم: (الرجل قادم؟)، (استمعت للنصيحة؟).

--- END STREAM ---
