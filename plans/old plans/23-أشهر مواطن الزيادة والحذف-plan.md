# **SESSION 23.0**

[TASK DEFINITION]
Objective: Implement أشهر مواطن الزيادة والحذف.
File: `pages/23.0_nXX_أشهر مواطن الزيادة والحذف.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/23.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 23
[CHAPTER_TITLE]: أشهر مواطن الزيادة والحذف
[CATEGORY_HEADER]: الإملاء
[SECTION_HEADER]: المستوى اللغوي
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition & Intro ===
(Component: TEMPLATE_C_BLOCK)
Title: مفهوم الزيادة والحذف
Content:
<p class="text-right text-gray-700 leading-normal">
    <span class="text-accent font-bold">الزِّيَادَةُ:</span> هِيَ كِتَابَةُ حَرْفٍ زَائِدٍ فِي الْكَلِمَةِ لَا يُلْفَظُ، وَلَكِنَّهُ يُثْبَتُ رَسْمًا لِعِلَّةٍ صَرْفِيَّةٍ أَوْ إِمْلَائِيَّةٍ.<br>
    <span class="text-accent font-bold">الْحَذْفُ:</span> هُوَ إِسْقَاطُ حَرْفٍ مِنَ الْكَلِمَةِ رَسْمًا وَخَطًّا، مَعَ بَقَائِهِ فِي اللَّفْظِ أَحْيَانًا، أَوْ حَذْفِهِ لَفْظًا وَخَطًّا فِي مَوَاضِعَ أُخْرَى.
</p>

=== BLOCK 3: Summary Matrix ===
(Component: TEMPLATE_C_TABLE)
Title: مُلَخَّصُ مَوَاطِنِ الزِّيَادَةِ وَالْحَذْفِ
[TABLE_HEADERS]: <th>النَّوْعُ</th><th>الْمَوْضِعُ</th><th>مِثَالٌ</th>
[TABLE_ROWS]:
<tr>
    <td class="font-bold text-teal-700">الزِّيَادَةُ (تُكْتَبُ وَلَا تُلْفَظُ)</td>
    <td>بَعْدَ وَاوِ الْجَمَاعَةِ، تَنْوِينِ النَّصْبِ، إِطْلَاقِ الشِّعْرِ، فِي (عَمْرو، أُولَئِكَ)</td>
    <td><span class="highlight-red">سَافَرُوا</span>، <span class="highlight-red">كِتَابًا</span>، <span class="highlight-red">عَمْرو</span></td>
</tr>
<tr>
    <td class="font-bold text-red-700">الْحَذْفُ (تُلْفَظُ وَلَا تُكْتَبُ)</td>
    <td>أَلِفُ (اللَّهُ، الرَّحْمَنُ)، (مَا) الِاسْتِفْهَامِيَّةُ، (نُونُ) مِنْ/عَنْ، لَامُ الَّذِي</td>
    <td><span class="highlight-red">اللَّهُ</span>، <span class="highlight-red">لِمَ؟</span>، <span class="highlight-red">الَّذِي</span></td>
</tr>

=== BLOCK 4: Ziyadat al-Alif (Addition of Alif) ===
(Component: TEMPLATE_C_BLOCK)
Title: أَوَّلًا: مَوَاطِنُ زِيَادَةِ الْأَلِفِ
Content:
<p class="text-right text-gray-700 mb-4">تُزَادُ الْأَلِفُ فِي الْمَوَاضِعِ التَّالِيَةِ وَلَا تُلْفَظُ:</p>
<div class="structured-list">
    <div class="flex items-start mb-2">
        <span class="text-teal-600 font-bold ml-2">1.</span>
        <p>
            <span class="font-bold text-teal-700">أَلِفُ التَّفْرِيقِ:</span> تُزَادُ بَعْدَ <span class="highlight-blue">وَاوِ الْجَمَاعَةِ</span> لِلتَّفْرِيقِ بَيْنَهَا وَبَيْنَ الْوَاوِ الْأَصْلِيَّةِ، نَحْوَ: <span class="highlight-red">سَافَرُوا</span>، <span class="highlight-red">لَمْ يَكْتُبُوا</span>، <span class="highlight-red">ادْرُسُوا</span>.
        </p>
    </div>
    <div class="flex items-start mb-2">
        <span class="text-teal-600 font-bold ml-2">2.</span>
        <p>
            <span class="font-bold text-teal-700">أَلِفُ تَنْوِينِ النَّصْبِ:</span> فِي آخِرِ الِاسْمِ الْمَنْصُوبِ الْمُنَوَّنِ غَيْرِ الْمُنْتَهِي بِتَاءٍ مَرْبُوطَةٍ أَوْ هَمْزَةٍ قَبْلَهَا أَلِفٌ، نَحْوَ: <span class="highlight-red">رَأَيْتُ شَابًّا</span>، <span class="highlight-red">قَرَأْتُ كِتَابًا</span>.
        </p>
    </div>
    <div class="flex items-start mb-2">
        <span class="text-teal-600 font-bold ml-2">3.</span>
        <p>
            <span class="font-bold text-teal-700">أَلِفُ الْإِطْلَاقِ:</span> تُزَادُ فِي آخِرِ بَعْضِ أَبْيَاتِ الشِّعْرِ لِضَرُورَةِ الْوَزْنِ وَالْقَافِيَةِ.
        </p>
    </div>
</div>

=== BLOCK 5: Ziyadat al-Waw (Addition of Waw) ===
(Component: TEMPLATE_C_CHIPS)
Title: ثَانِيًا: مَوَاطِنُ زِيَادَةِ الْوَاوِ
[CHIPS_CONTENT]:
<div class="flex flex-wrap gap-2 justify-center">
    <span class="bg-gray-100 rounded-lg px-4 py-2 text-xl font-bold text-teal-800 border-2 border-teal-500">عَمْرو</span>
    <span class="bg-gray-100 rounded-lg px-4 py-2 text-xl font-bold text-teal-800 border-2 border-teal-500">أُولَئِكَ</span>
    <span class="bg-gray-100 rounded-lg px-4 py-2 text-xl font-bold text-teal-800 border-2 border-teal-500">أُولَاء</span>
    <span class="bg-gray-100 rounded-lg px-4 py-2 text-xl font-bold text-teal-800 border-2 border-teal-500">أُولُو</span>
    <span class="bg-gray-100 rounded-lg px-4 py-2 text-xl font-bold text-teal-800 border-2 border-teal-500">أُولَات</span>
    <span class="bg-gray-100 rounded-lg px-4 py-2 text-xl font-bold text-teal-800 border-2 border-teal-500">أُولِي</span>
</div>

=== BLOCK 6: Hadhf al-Alif (Deletion of Alif) ===
(Component: TEMPLATE_C_SPLIT)
[LEFT_TITLE]: حَذْفُ الْأَلِفِ مِنَ الْأَسْمَاءِ
[RIGHT_TITLE]: حَذْفُ الْأَلِفِ مِنْ (مَا) الِاسْتِفْهَامِيَّةِ
[LEFT_CONTENT]:
<p class="mb-2">تُحْذَفُ الْأَلِفُ كِتَابَةً فَقَطْ (تُلْفَظُ وَلَا تُكْتَبُ) فِي الْكَلِمَاتِ التَّالِيَةِ:</p>
<ul class="structured-list pr-4">
    <li class="mb-1"><span class="highlight-red">اللَّهُ</span>، <span class="highlight-red">الرَّحْمَنُ</span>، <span class="highlight-red">إِلَهٌ</span></li>
    <li class="mb-1"><span class="highlight-red">السَّمَوَاتُ</span></li>
    <li class="mb-1"><span class="highlight-red">هَذَا</span>، <span class="highlight-red">هَذِهِ</span>، <span class="highlight-red">هَذَانِ</span>، <span class="highlight-red">هَؤُلَاءِ</span>، <span class="highlight-red">هَكَذَا</span></li>
    <li class="mb-1"><span class="highlight-red">ذَلِكَ</span>، <span class="highlight-red">أُولَئِكَ</span></li>
    <li class="mb-1"><span class="highlight-red">لَكِنَّ</span>، <span class="highlight-red">لَكِنْ</span></li>
</ul>
[RIGHT_CONTENT]:
<p class="mb-2">تُحْذَفُ أَلِفُ (مَا) الِاسْتِفْهَامِيَّةِ إِذَا دَخَلَ عَلَيْهَا حَرْفُ جَرٍّ:</p>
<ul class="structured-list pr-4">
    <li class="mb-1">لِ + مَا = <span class="highlight-red font-bold">لِمَ؟</span></li>
    <li class="mb-1">بِ + مَا = <span class="highlight-red font-bold">بِمَ؟</span></li>
    <li class="mb-1">عَلَى + مَا = <span class="highlight-red font-bold">عَلَامَ؟</span></li>
    <li class="mb-1">إِلَى + مَا = <span class="highlight-red font-bold">إِلَامَ؟</span></li>
    <li class="mb-1">مِنْ + مَا = <span class="highlight-red font-bold">مِمَّ؟</span></li>
    <li class="mb-1">عَنْ + مَا = <span class="highlight-red font-bold">عَمَّ؟</span></li>
</ul>

=== BLOCK 7: Deletion of Nun and Mergers ===
(Component: TEMPLATE_C_TABLE)
Title: حَذْفُ النُّونِ وَالْإِدْغَامُ
[TABLE_HEADERS]: <th>الْقَاعِدَةُ</th><th>الْمُعَادَلَةُ</th><th>النَّتِيجَةُ</th>
[TABLE_ROWS]:
<tr>
    <td class="font-bold text-teal-700" rowspan="2">حَذْفُ نُونِ (مِنْ / عَنْ)</td>
    <td>مِنْ + مَنْ</td>
    <td><span class="highlight-red">مِمَّنْ</span></td>
</tr>
<tr>
    <td>عَنْ + مَا</td>
    <td><span class="highlight-red">عَمَّ</span> (مَعَ حَذْفِ الْأَلِفِ)</td>
</tr>
<tr>
    <td class="font-bold text-teal-700" rowspan="3">إِدْغَامُ (إِنْ / أَنْ)</td>
    <td>إِنْ (الشَّرْطِيَّة) + مَا</td>
    <td><span class="highlight-red">إِمَّا</span></td>
</tr>
<tr>
    <td>إِنْ (الشَّرْطِيَّة) + لَا</td>
    <td><span class="highlight-red">إِلَّا</span></td>
</tr>
<tr>
    <td>أَنْ (الْمَصْدَرِيَّة) + مَا</td>
    <td><span class="highlight-red">أَمَّا</span></td>
</tr>

=== BLOCK 8: Lam in Relative Pronouns ===
(Component: TEMPLATE_C_TABLE)
Title: اللَّامُ مَعَ الْأَسْمَاءِ الْمَوْصُولَةِ
[TABLE_HEADERS]: <th>الْحَالَةُ</th><th>الشَّرْحُ</th><th>الْأَمْثِلَةُ</th>
[TABLE_ROWS]:
<tr>
    <td class="font-bold text-teal-700">لَامٌ وَاحِدَةٌ مُشَدَّدَةٌ</td>
    <td>لِلْمُفْرَدِ بِنَوْعَيْهِ، وَجَمْعِ الْمُذَكَّرِ</td>
    <td><span class="highlight-blue">الَّذِي</span>، <span class="highlight-blue">الَّتِي</span>، <span class="highlight-blue">الَّذِينَ</span></td>
</tr>
<tr>
    <td class="font-bold text-teal-700">لَامَانِ اثْنَتَانِ</td>
    <td>لِلْمُثَنَّى بِنَوْعَيْهِ، وَجَمْعِ الْمُؤَنَّثِ</td>
    <td><span class="highlight-blue">اللَّذَانِ</span>، <span class="highlight-blue">اللَّتَانِ</span>، <span class="highlight-blue">اللَّوَاتِي</span>، <span class="highlight-blue">اللَّائِي</span></td>
</tr>
<tr>
    <td class="font-bold text-teal-700">دُخُولُ لَامِ الْجَرِّ</td>
    <td>تُكْتَبُ بِلَامَيْنِ عِنْدَ دُخُولِ اللَّامِ عَلَيْهَا</td>
    <td><span class="highlight-blue">لِلَّذِينَ</span>، <span class="highlight-blue">لِلَّذِي</span>، <span class="highlight-blue">لِلَّتَيْنِ</span></td>
</tr>

=== BLOCK 9: Benefit - Amr vs Umar ===
(Component: TEMPLATE_C_BENEFIT)
Title: فَائِدَةٌ (عَمْرو وَ عُمَر)
Content:
<p>
    تُزَادُ الْوَاوُ فِي كَلِمَةِ (<span class="highlight-red">عَمْرو</span>) فِي حَالَتَيِ الرَّفْعِ وَالْجَرِّ لِلتَّفْرِيقِ بَيْنَهَا وَبَيْنَ (<span class="highlight-blue">عُمَر</span>) الْمَمْنُوعَةِ مِنَ الصَّرْفِ. أَمَّا فِي حَالَةِ النَّصْبِ فَتُحْذَفُ الْوَاوُ وَتُنَوَّنُ الْأَلِفُ: (<span class="highlight-green">رَأَيْتُ عَمْرًا</span>).
</p>

=== BLOCK 10: Evidence Analysis (Irab) ===
(Component: TEMPLATE_C_IRAB_ROW)
Title: نَمَاذِجُ إِعْرَابِيَّةٌ
[IRAB_CONTENT]:
<div class="flex flex-row gap-4 justify-center">
    <div class="bg-white p-4 rounded-lg shadow-md w-1/3 text-center border-t-4 border-teal-500">
        <div class="text-2xl font-bold text-teal-800 mb-2">سَافَرُوا</div>
        <div class="text-gray-700 text-sm">
            <span class="font-bold text-teal-600">سَافَرَ:</span> فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ.<br>
            <span class="font-bold text-teal-600">الْوَاوُ:</span> ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعِ فَاعِلٍ.<br>
            <span class="font-bold text-teal-600">الْأَلِفُ:</span> لِلتَّفْرِيقِ، حَرْفٌ زَائِدٌ لَا مَحَلَّ لَهُ.
        </div>
    </div>
    <div class="bg-white p-4 rounded-lg shadow-md w-1/3 text-center border-t-4 border-red-500">
        <div class="text-2xl font-bold text-red-800 mb-2">لِمَ؟</div>
        <div class="text-gray-700 text-sm">
            <span class="font-bold text-red-600">اللَّامُ:</span> حَرْفُ جَرٍّ.<br>
            <span class="font-bold text-red-600">مَا:</span> اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ، وَحُذِفَتْ أَلِفُهُ لِاتِّصَالِهِ بِحَرْفِ الْجَرِّ.
        </div>
    </div>
</div>

=== BLOCK 11: Exam ===
(Component: TEMPLATE_C_EXAM)
Number: 1
Question: بَيِّنْ مَوْطِنَ الزِّيَادَةِ أَوْ الْحَذْفِ فِي الْكَلِمَاتِ الْمُلَوَّنَةِ فِي الْجُمَلِ الْآتِيَةِ:
Choices:
<div class="structured-list">
    <p class="mb-2">1. قَالَ تَعَالَى: {وَالَّذِينَ آمَنُوا وَعَمِلُوا الصَّالِحَاتِ <span class="highlight-red">أُولَئِكَ</span> أَصْحَابُ الْجَنَّةِ}.</p>
    <p class="mb-2">2. <span class="highlight-red">عَلَامَ</span> تَتَنَافَسُونَ وَالدُّنْيَا زَائِلَةٌ؟</p>
    <p class="mb-2">3. <span class="highlight-red">هَذَا</span> طَالِبٌ مُجْتَهِدٌ يَعْرِفُ وَاجِبَهُ.</p>
</div>

--- END STREAM ---
