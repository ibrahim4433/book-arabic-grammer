# **SESSION 13.0**

[TASK DEFINITION]
Objective: Implement الإعلال.
File: `pages/13.0_nXX_الإعلال.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK\_RULES.md and elements\_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/13.1_...`.
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
[LESSON_NUMBER]: 13
[CHAPTER_TITLE]: الإعلال
[CATEGORY_HEADER]: الصرف
[SECTION_HEADER]: المستوى اللغوي
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition of Ilal ===
(Component: TEMPLATE_C_BLOCK)
Title: تعريف الإعلال
Content: <p class="text-accent mb-2mm">الإعلال: هو تغييرٌ يصيب حرف العلّة، وله ثلاثة أنواع:</p>

=== BLOCK 3: Types of Ilal (Summary Matrix) ===
(Component: TEMPLATE_C_TABLE)
Title: أنواع الإعلال الثلاثة
Cols: النّوع | التّعريف | مثال
Row 1: الإعلال بالتّسكين | تسكينُ أحد حرفي العلّة (الواو أو الياء) لثقلهما، فالألف ساكنة دائمًا. | يَسْمُوْ (أصله يَسْمُوُ)، يَمْشِيْ (أصله يَمْشِيُ)
Row 2: الإعلال بالحذْف | حذفُ حرفِ العلةِ للتخلص من التقاء الساكنين أو في حالات الجزم والبناء. | قُلْ (حذفت الواو)، لَمْ يَمْشِ (حذفت الياء)
Row 3: الإعلال بالقلب | قَلبُ حرفِ العِلَّةِ إلى حرفٍ آخر (ألف، واو، ياء) لعلة صرفية. | قَالَ (أصله قَوَلَ)، صِيَام (أصله صِوَام)، مُوْقِن (أصله مُيْقِن)

=== BLOCK 4: First Type - Ilal by Taskin ===
(Component: TEMPLATE_C_SPLIT)
[LEFT_TITLE]: الحالة الأولى: في لام الكلمة
[LEFT_CONTENT]: <p>إذا وقع حرفُ <span class="highlight-red">الواوِ</span> أو <span class="highlight-red">الياءِ</span> في لامِ الكلمةِ (آخرِها) مسبوقينِ بحركة مجانسة:</p><ul class="structured-list"><li><span class="highlight-blue">الواو:</span> إذا سُبقت بضمٍّ تَسْكُن (يَسْمُوْ).</li><li><span class="highlight-blue">الياء:</span> إذا سُبقت بكسرٍ تَسْكُن (يَمْشِيْ).</li></ul>
[RIGHT_TITLE]: الحالة الثانية: في عين الكلمة
[RIGHT_CONTENT]: <p>إذا وقع حرفُ <span class="highlight-red">الواوِ</span> أو <span class="highlight-red">الياءِ</span> في عينِ الكلمةِ (وسطِها) مُتَحرِّكَينِ مسبوقينِ بحرفٍ <span class="highlight-blue">صحيحٍ ساكنٍ</span>:</p><p class="text-sm">يُسَكَّنانِ وتُنقَل حركتُهما إلى الساكن الصحيح قبلهما.</p><p class="text-center mt-2mm"><span class="highlight-green">يَقُوْمُ</span> (أصلها يَقْوُمُ) | <span class="highlight-green">يَبِيْنُ</span> (أصلها يَبْيِنُ)</p>

=== BLOCK 5: Second Type - Ilal by Hadhf ===
(Component: TEMPLATE_C_LIST)
Title: مواضع الإعلال بالحذْف
Items:
1. **في أول الكلمة (المثال):** يُحذف حرف العلة في المضارع والأمر من المثال الواوي.<br>مثال: <span class="highlight-red">يَزِنُ</span> (حُذِفَت الواو لوقوعها في أول المضارع)، <span class="highlight-red">زِنْ</span> (حُذِفَت الواو في الأمر).
2. **في وسط الكلمة (الأجوف):** يُحذف حرف العلة إذا التقى بساكن بعده.<br>مثال: <span class="highlight-red">قُلْ</span> (حُذِفَت الواو لالتقاء الساكنين).
3. **في آخر الكلمة (الناقص):**
   - **المضارع المجزوم:** <span class="highlight-blue">لَمْ يَمْشِ</span> (حُذِفَت الياء).
   - **أمر المفرد المذكر:** <span class="highlight-blue">اسْعَ</span> (حُذِفَت الألف).
   - **الماضي المتصل بـ (تْ) أو (وا):** <span class="highlight-blue">مَشَتْ</span> (حُذِفَت الألف)، <span class="highlight-blue">دَعَوْا</span> (حُذِفَت الألف).

=== BLOCK 6: Benefit Tip ===
(Component: TEMPLATE_C_BENEFIT_TIP)
Title: قاعدة هامة
Content: الحرفُ الصّحيحُ أقدرُ على تحمُّلِ الحركةِ من الحرفِ المعتلِّ، لذا في الإعلال بالتسكين (عين الكلمة) تُنقل الحركة من المعتل إلى الصحيح الساكن قبله.

=== BLOCK 7: Third Type - Ilal by Qalb ===
(Component: TEMPLATE_C_BLOCK)
Title: مواضع الإعلال بالقلب
Content:
<div class="mb-4mm">
<p class="font-bold text-accent">١- قلب الواو أو الياء ألفًا:</p>
<p>إذا تحرّكتا وانفتح ما قبلهما.</p>
<div class="chips-container"><span class="chip">قَالَ (قَوَلَ)</span><span class="chip">بَاعَ (بَيَعَ)</span><span class="chip">سَمَا (سَمَوَ)</span><span class="chip">جَرَى (جَرَيَ)</span></div>
</div>
<div class="mb-4mm">
<p class="font-bold text-accent">٢- قلب الواو ياءً:</p>
<ul class="structured-list">
<li>تطَرَّفَتْ بعدَ كسرٍ: <span class="highlight-red">رَضِيَ</span> (رَضِوَ)، <span class="highlight-red">قَوِيَ</span> (قَوِوَ).</li>
<li>وقَعَتْ حشوًا بينَ كسرةٍ وألفٍ: <span class="highlight-red">قِيَام</span> (قِوَام)، <span class="highlight-red">صِيَام</span> (صِوَام).</li>
<li>سُكِّنَتْ بعدَ كَسْرٍ: <span class="highlight-red">مِيْزَان</span> (مِوْزَان)، <span class="highlight-red">مِيْعَاد</span> (مِوْعَاد).</li>
<li>اجتمعَتِ الواو والياءُ (الأولى ساكنة): <span class="highlight-red">سَيِّد</span> (سَيْوِد)، <span class="highlight-red">مَيِّت</span> (مَيْوِت).</li>
</ul>
</div>
<div>
<p class="font-bold text-accent">٣- قلب الياء واوًا:</p>
<p>إذا سكنت بعد ضمٍّ.</p>
<p class="text-center"><span class="highlight-green">مُوْقِن</span> (أصلها مُيْقِن) | <span class="highlight-green">مُوْسِر</span> (أصلها مُيْسِر)</p>
</div>

=== BLOCK 8: Evidence from the Language ===
(Component: TEMPLATE_C_IRAB_ROW)
Word 1: يَقُومُ
Details 1: فعل مضارع مرفوع، وفيه إعلال بالتسكين، أصله (يَقْوُمُ)، نُقلت حركة الواو إلى القاف الساكنة قبلها فصارت (يَقُومُ).
Word 2: لَمْ يَمْشِ
Details 2: فعل مضارع مجزوم بلم، وعلامة جزمه حذف حرف العلة (الياء) من آخره، وهو إعلال بالحذف.
Word 3: قَالَ
Details 3: فعل ماض مبني على الفتح، وفيه إعلال بالقلب، أصله (قَوَلَ)، تحركت الواو وانفتح ما قبلها فقلبت ألفًا.

=== BLOCK 9: Evaluation ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: بيّن نوع الإعلال وسببه في الكلمات الآتية: (يَصُومُ - ادْعُ - مِيقَات).
Number: ٢
Question: هاتِ أصل الكلمات الآتية وبيّن ما حدث فيها من تغيير: (بَاعَ - مَشَى).
Number: ٣
Question: علّل حذف حرف العلة في كلمة (قُلْ) وقلبه ياءً في كلمة (سَيِّد).

--- END STREAM ---
