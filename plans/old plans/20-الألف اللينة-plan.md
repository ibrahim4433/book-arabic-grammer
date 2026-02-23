# **SESSION 20.0**

[TASK DEFINITION]
Objective: Implement الألف اللينة.
File: `pages/20.0_nXX_الألف اللينة.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/20.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 20
[CHAPTER_TITLE]: الألف اللينة
[CATEGORY_HEADER]: الإملاء
[SECTION_HEADER]: المستوى اللغوي
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition ===
(Component: TEMPLATE_C_BLOCK)
Title: تَعْرِيفُ الأَلِفِ اللَّيِّنَةِ
Content:
<p class="text-accent text-justify leading-loose">
هِيَ <span class="font-bold">أَلِفُ مَدٍّ سَاكِنَةٌ</span> مَفْتُوحٌ مَا قَبْلَهَا، وَلَا تَقْبَلُ الْحَرَكَاتِ، وَلَا تَرِدُ إِلَّا فِي وَسَطِ الْكَلِمَةِ أَوْ فِي آخِرِهَا، وَتُرْسَمُ فِي أَوَاخِرِ الْكَلِمَاتِ <span class="highlight-red">مَقْصُورَةً (ى)</span>، أَوْ <span class="highlight-red">مَمْدُودَةً (ا)</span>.
</p>

=== BLOCK 3: Triliteral Rules ===
(Component: TEMPLATE_C_SPLIT)
[LEFT_TITLE]: إِذَا كَانَ أَصْلُهَا وَاوًا
[RIGHT_TITLE]: إِذَا كَانَ أَصْلُهَا يَاءً
[LEFT_CONTENT]:
<div class="p-2mm">
    <p class="text-right mb-2mm">تُكْتَبُ الأَلِفُ <span class="highlight-red font-bold">مَمْدُودَةً (ا)</span>.</p>
    <div class="chips-container">
        <span class="bg-grey-lighter rounded p-1mm ml-1mm">دَنَا (أَصْلُهَا يَدْنُو)</span>
        <span class="bg-grey-lighter rounded p-1mm ml-1mm">ذُرَا (أَصْلُهَا ذُرْوَة)</span>
        <span class="bg-grey-lighter rounded p-1mm ml-1mm">سَمَا (أَصْلُهَا يَسْمُو)</span>
        <span class="bg-grey-lighter rounded p-1mm ml-1mm">عَصَا (أَصْلُهَا عَصَوَانِ)</span>
    </div>
</div>
[RIGHT_CONTENT]:
<div class="p-2mm">
    <p class="text-right mb-2mm">تُكْتَبُ الأَلِفُ <span class="highlight-blue font-bold">مَقْصُورَةً (ى)</span>.</p>
    <div class="chips-container">
        <span class="bg-grey-lighter rounded p-1mm ml-1mm">فَتَى (أَصْلُهَا فِتْيَان)</span>
        <span class="bg-grey-lighter rounded p-1mm ml-1mm">سَقَى (أَصْلُهَا يَسْقِي)</span>
        <span class="bg-grey-lighter rounded p-1mm ml-1mm">رَمَى (أَصْلُهَا يَرْمِي)</span>
        <span class="bg-grey-lighter rounded p-1mm ml-1mm">مَشَى (أَصْلُهَا يَمْشِي)</span>
    </div>
</div>

=== BLOCK 4: Technique Benefit ===
(Component: TEMPLATE_C_BENEFIT_TIP)
Title: كَيْفَ نَعْرِفُ أَصْلَ الأَلِفِ فِي الثُّلَاثِيِّ؟
Content:
<p class="text-right mb-2mm">لِمَعْرِفَةِ أَصْلِ الأَلِفِ (وَاو أَمْ يَاء)، نَلْجَأُ إِلَى إِحْدَى الطُّرُقِ التَّالِيَةِ:</p>
<ul class="structured-list">
    <li class="relative pr-4mm mb-1mm">
        <span class="absolute right-0 top-1mm text-accent">•</span>
        <span class="list-item-content">
            <span class="font-bold">فِي الأَفْعَالِ:</span> نَأْتِي بِالْمُضَارِعِ (دَعَا &#8592; <span class="highlight-red">يَدْعُو</span>) أَوْ بِالْمَصْدَرِ (رَمَى &#8592; <span class="highlight-blue">رَمْيًا</span>).
        </span>
    </li>
    <li class="relative pr-4mm mb-1mm">
        <span class="absolute right-0 top-1mm text-accent">•</span>
        <span class="list-item-content">
            <span class="font-bold">فِي الأَسْمَاءِ:</span> نَأْتِي بِالْمُثَنَّى (عَصَا &#8592; <span class="highlight-red">عَصَوَانِ</span>) أَوْ بِالْجَمْعِ (فَتَى &#8592; <span class="highlight-blue">فِتْيَان</span>).
        </span>
    </li>
</ul>

=== BLOCK 5: Non-Triliteral Rules ===
(Component: TEMPLATE_C_SPLIT)
[LEFT_TITLE]: إِذَا سُبِقَتْ بِيَاءٍ
[RIGHT_TITLE]: إِذَا لَمْ تُسْبَقْ بِيَاءٍ
[LEFT_CONTENT]:
<div class="p-2mm">
    <p class="text-right mb-2mm">تُكْتَبُ الأَلِفُ <span class="highlight-red font-bold">مَمْدُودَةً (ا)</span> كَرَاهِيَةَ تَوَالِي الأَمْثَالِ (يَائَيْنِ).</p>
    <div class="chips-container">
        <span class="bg-grey-lighter rounded p-1mm ml-1mm">دُنْيَا</span>
        <span class="bg-grey-lighter rounded p-1mm ml-1mm">حَيَا</span>
        <span class="bg-grey-lighter rounded p-1mm ml-1mm">هَدَايَا</span>
        <span class="bg-grey-lighter rounded p-1mm ml-1mm">مَرَايَا</span>
    </div>
</div>
[RIGHT_CONTENT]:
<div class="p-2mm">
    <p class="text-right mb-2mm">تُكْتَبُ الأَلِفُ <span class="highlight-blue font-bold">مَقْصُورَةً (ى)</span>.</p>
    <div class="chips-container">
        <span class="bg-grey-lighter rounded p-1mm ml-1mm">مَعْنَى</span>
        <span class="bg-grey-lighter rounded p-1mm ml-1mm">تَرَدَّى</span>
        <span class="bg-grey-lighter rounded p-1mm ml-1mm">مُصْطَفَى</span>
        <span class="bg-grey-lighter rounded p-1mm ml-1mm">مُسْتَشْفَى</span>
    </div>
</div>

=== BLOCK 6: Exception Benefit ===
(Component: TEMPLATE_C_BENEFIT_WARNING)
Title: فَائِدَةٌ هَامَةٌ (يَحْيَى VS يَحْيَا)
Content:
<p class="text-justify">
شَذَّتْ كَلِمَةُ <span class="font-bold text-accent">(يَحْيَى)</span> فَرُسِمَتْ بِالأَلِفِ الْمَقْصُورَةِ رَغْمَ أَنَّهَا مَسْبُوقَةٌ بِيَاءٍ؛ وَذَلِكَ لِلتَّفْرِيقِ بَيْنَ <span class="highlight-blue">الِاسْمِ (يَحْيَى)</span> وَبَيْنَ <span class="highlight-red">الْفِعْلِ (يَحْيَا)</span>.
</p>

=== BLOCK 7: Summary Matrix ===
(Component: TEMPLATE_C_TABLE)
Title: مُلَخَّصُ قَوَاعِدِ رَسْمِ الأَلِفِ اللَّيِّنَةِ
[TABLE_HEADERS]: <th>نَوْعُ الْكَلِمَةِ</th><th>الْحَالَةُ</th><th>الرَّسْمُ</th><th>مِثَالٌ</th>
[TABLE_BODY]:
<tr>
    <td class="font-bold">ثُلَاثِيَّةٌ</td>
    <td>أَصْلُهَا وَاوٌ</td>
    <td class="text-center font-bold highlight-red">مَمْدُودَة (ا)</td>
    <td>دَنَا، سَمَا</td>
</tr>
<tr>
    <td class="font-bold">ثُلَاثِيَّةٌ</td>
    <td>أَصْلُهَا يَاءٌ</td>
    <td class="text-center font-bold highlight-blue">مَقْصُورَة (ى)</td>
    <td>هَدَى، رَمَى</td>
</tr>
<tr>
    <td class="font-bold">فَوْقَ الثُّلَاثِيَّةِ</td>
    <td>سُبِقَتْ بِيَاءٍ</td>
    <td class="text-center font-bold highlight-red">مَمْدُودَة (ا)</td>
    <td>دُنْيَا، خَطَايَا</td>
</tr>
<tr>
    <td class="font-bold">فَوْقَ الثُّلَاثِيَّةِ</td>
    <td>لَمْ تُسْبَقْ بِيَاءٍ</td>
    <td class="text-center font-bold highlight-blue">مَقْصُورَة (ى)</td>
    <td>مُلْتَقَى، اسْتَدْعَى</td>
</tr>

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: لِمَاذَا كُتِبَتِ الأَلِفُ مَمْدُودَةً فِي كَلِمَةِ (عَصَا) وَمَقْصُورَةً فِي كَلِمَةِ (فَتَى)؟
Number: ٢
Question: صَحِّحِ الْخَطَأَ فِي الْكَلِمَةِ التَّالِيَةِ مَعَ التَّعْلِيلِ: (إِسْتَحْيَا الرَّجُلُ مِنْ جَارِهِ).
Number: ٣
Question: لِمَاذَا رُسِمَتِ الأَلِفُ مَقْصُورَةً فِي كَلِمَةِ (مُصْطَفَى)؟

--- END STREAM ---
