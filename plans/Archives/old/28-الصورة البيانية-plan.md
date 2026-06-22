# **SESSION 28.0**

[TASK DEFINITION]
Objective: Implement الصورة البيانية.
File: `pages/28.0_nXX_الصورة البيانية.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/28.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 28
[CHAPTER_TITLE]: الصُّورَةُ البَيَانِيَّةُ
[CATEGORY_HEADER]: فَوَائِدُ
[SECTION_HEADER]: المُسْتَوَى الفَنِّيُّ
[AUTHOR_NAME]: أ. اليَاس خَفِيف
[AUTHOR_PHONE]:  

=== BLOCK 2: Definition of Imagery ===
(Component: TEMPLATE_C_BLOCK)
ID: b28001
Title: عِلْمُ البَيَانِ
Content: <p class="text-accent text-xl leading-loose text-justify mb-4mm">عِلْمُ البَيَانِ فِي البَلَاغَةِ العَرَبِيَّةِ يَدْرُسُ الصُّورَةَ البَيَانِيَّةَ (الفَنِّيَّةَ). وَيُقْسَمُ إِلَى ثَلَاثَةِ أَقْسَامٍ هِيَ: (التَّشْبِيهُ، وَالاسْتِعَارَةُ، وَالكِنَايَةُ).</p>

=== BLOCK 3: Simile Definition ===
(Component: TEMPLATE_C_BLOCK)
ID: b28002
Title: أَوَّلًا - التَّشْبِيهُ
Content: <p class="text-accent text-lg leading-loose text-justify mb-4mm">هُوَ عَقْدُ مُقَارَنَةٍ بَيْنَ شَيْئَيْنِ اشْتَرَكَا بِصِفَةٍ وَاحِدَةٍ، وَتَكُونُ هَذِهِ الصِّفَةُ فِي المُشَبَّهِ بِهِ أَقْوَى مِنْهَا فِي المُشَبَّهِ. نَحْوَ: خَالِدٌ كَالبَحْرِ فِي الجُودِ.</p>
<div class="benefit-box bg-grey-lighter p-4mm rounded-lg border-r-4 border-primary mb-4mm">
    <h4 class="text-primary font-bold text-lg mb-2mm">أَرْكَانُ التَّشْبِيهِ:</h4>
    <p class="text-gray-800 text-lg">المُشَبَّهُ، وَالمُشَبَّهُ بِهِ (وَهُمَا الرُّكْنَانِ الأَسَاسِيَّانِ)، وَالأَدَاةُ، وَوَجْهُ الشَّبَهِ.</p>
</div>

=== BLOCK 4: Simile Tools ===
(Component: TEMPLATE_C_CHIPS)
ID: b28003
Title: أَدَوَاتُ التَّشْبِيهِ
Content: الكَافُ | كَأَنَّ | مِثْلُ | شِبْهُ | أَشْبَهُ | شَبِيهُ | يُشْبِهُ | شَابَهَ | حَاكَى | يُحَاكِي | مَاثَلَ | يُمَاثِلُ

=== BLOCK 5: Simile Types Matrix ===
(Component: TEMPLATE_C_TABLE)
ID: b28004
Title: أَنْوَاعُ التَّشْبِيهِ (بِحَسَبِ الأَرْكَانِ)
Headers: النَّوْعُ | التَّعْرِيفُ | المِثَالُ
Rows:
<tr>
    <td class="font-bold text-primary">تَشْبِيهٌ تَامُّ الأَرْكَانِ</td>
    <td>هُوَ الَّذِي يَشْتَمِلُ عَلَى الأَرْكَانِ الأَرْبَعَةِ.</td>
    <td>خَالِدٌ <span class="highlight-red">مِثْلُ</span> البَحْرِ <span class="highlight-blue">فِي الجُودِ</span>.</td>
</tr>
<tr>
    <td class="font-bold text-primary">تَشْبِيهٌ مُؤَكَّدٌ</td>
    <td>هُوَ الَّذِي حُذِفَتْ مِنْهُ الأَدَاةُ.</td>
    <td>خَالِدٌ ... بَحْرٌ <span class="highlight-blue">فِي الجُودِ</span>.</td>
</tr>
<tr>
    <td class="font-bold text-primary">تَشْبِيهٌ مُجْمَلٌ</td>
    <td>هُوَ الَّذِي حُذِفَ مِنْهُ وَجْهُ الشَّبَهِ.</td>
    <td>خَالِدٌ <span class="highlight-red">مِثْلُ</span> البَحْرِ ...</td>
</tr>
<tr>
    <td class="font-bold text-primary">تَشْبِيهٌ بَلِيغٌ</td>
    <td>هُوَ الَّذِي حُذِفَتْ مِنْهُ الأَدَاةُ وَوَجْهُ الشَّبَهِ.</td>
    <td>خَالِدٌ ... بَحْرٌ ...</td>
</tr>

=== BLOCK 6: Representative Simile ===
(Component: TEMPLATE_C_BLOCK)
ID: b28005
Title: التَّشْبِيهُ التَّمْثِيلِيُّ
Content: <p class="text-accent text-lg leading-loose text-justify mb-2mm">هُوَ مَا كَانَ وَجْهُ الشَّبَهِ فِيهِ هَيْئَةً مُنْتَزَعَةً مِنْ مُتَعَدِّدٍ؛ أَيْ هُوَ تَشْبِيهُ صُورَةٍ بِصُورَةٍ أُخْرَى.</p>
<div class="poem-container mb-2mm">
    <div class="poem-line flex justify-between items-center mb-2">
        <div class="hemistich w-45pct text-center font-amiri text-xl">تَمْشِي المَصَالِحُ فِي أَقْلَامِ دَوْلَتِنَا</div>
        <div class="hemistich w-45pct text-center font-amiri text-xl">مَشْيَ الخَنَافِسِ فِي جَزٍّ مِنَ الصُّوفِ</div>
    </div>
</div>
<ul class="structured-list list-none p-0">
    <li class="list-item-content mb-1mm"><span class="font-bold text-primary">• المُشَبَّهُ:</span> صُورَةُ سَيْرِ المُعَامَلَاتِ الرَّسْمِيَّةِ فِي الدَّوَائِرِ الحُكُومِيَّةِ.</li>
    <li class="list-item-content mb-1mm"><span class="font-bold text-primary">• المُشَبَّهُ بِهِ:</span> صُورَةُ مَشْيِ الخُنْفُسَاءِ فِي جَزٍّ مِنَ الصُّوفِ.</li>
    <li class="list-item-content mb-1mm"><span class="font-bold text-primary">• وَجْهُ الشَّبَهِ:</span> بُطْءُ السَّيْرِ وَالتَّعَثُّرِ.</li>
</ul>

=== BLOCK 7: Metaphor Intro ===
(Component: TEMPLATE_C_BLOCK)
ID: b28006
Title: ثَانِيًا - الاسْتِعَارَةُ
Content: <p class="text-accent text-lg leading-loose text-justify">هِيَ تَشْبِيهٌ بَلِيغٌ، حُذِفَ مِنْهُ أَحَدُ رُكْنَيْهِ (المُشَبَّهُ، أَوْ المُشَبَّهُ بِهِ)، وَلَهَا نَوْعَانِ:</p>

=== BLOCK 8: Metaphor Types Split ===
(Component: TEMPLATE_C_SPLIT)
ID: b28007
Title: أَنْوَاعُ الاسْتِعَارَةِ
Left_Title: اسْتِعَارَةٌ تَصْرِيحِيَّةٌ
Left_Content: <p class="text-justify mb-2mm">فِيهَا يُحْذَفُ <span class="text-red-700 font-bold">المُشَبَّهُ</span>، وَيُصَرَّحُ بِالمُشَبَّهِ بِهِ.</p><p class="text-sm text-gray-600 mb-1mm">مِثَالٌ (أَحْمَد شَوْقِي):</p><p class="font-amiri text-lg text-center mb-1mm">يَا أَيُّهَا السَّيْفُ المُجَرَّدُ فِي الفَلَا</p><p class="text-sm text-gray-600">شَبَّهَ المُجَاهِدَ (مَحْذُوف) بِالسَّيْفِ (مُصَرَّح بِهِ).</p>
Right_Title: اسْتِعَارَةٌ مَكْنِيَّةٌ
Right_Content: <p class="text-justify mb-2mm">فِيهَا يُحْذَفُ <span class="text-red-700 font-bold">المُشَبَّهُ بِهِ</span>، وَتَبْقَى إِحْدَى قَرَائِنِهِ (صِفَاتِهِ) تَدُلُّ عَلَيْهِ.</p><p class="text-sm text-gray-600 mb-1mm">مِثَالٌ (بِشَارَة الخُورِي):</p><p class="font-amiri text-lg text-center mb-1mm">يَا جِهَادًا صَفَّقَ المَجْدُ لَهُ</p><p class="text-sm text-gray-600">شَبَّهَ المَجْدَ بِإِنْسَانٍ (مَحْذُوف) وَأَبْقَى صِفَةَ التَّصْفِيقِ.</p>

=== BLOCK 9: Personification & Embodiment Split ===
(Component: TEMPLATE_C_SPLIT)
ID: b28008
Title: التَّشْخِيصُ وَالتَّجْسِيمُ
Left_Title: التَّشْخِيصُ
Left_Content: <p class="text-justify mb-2mm">هُوَ مَنْحُ الحَيَاةِ لِغَيْرِ الإِنْسَانِ، وَمَنْحُ صِفَاتِ الأَشْخَاصِ لِلْجَمَادِ.</p><ul class="list-disc pr-4mm text-sm"><li>أَشْوَاقُ السَّنَابِلِ</li><li>نَبْضُ المَصَانِعِ</li></ul><p class="mt-2mm text-xs text-gray-500">وَظِيفَتُهُ: تَوْكِيدُ المَعْنَى وَإِبْرَازُهُ.</p>
Right_Title: التَّجْسِيمُ
Right_Content: <p class="text-justify mb-2mm">هُوَ تَحْوِيلُ الأَشْيَاءِ المَعْنَوِيَّةِ مِنْ مَجَالِهَا التَّجْرِيدِيِّ إِلَى مَجَالٍ آخَرَ حِسِّيٍّ.</p><p class="font-amiri text-lg text-center mb-1mm">وَتَصُبُّ الحَيَاةَ فِي مَسْمَعَيَّا</p><p class="text-sm text-gray-600">شَبَّهَ الحَيَاةَ (مَعْنَوِيّ) بِمَاءٍ يُصَبُّ (حِسِّيّ).</p>

=== BLOCK 10: Functions Intro ===
(Component: TEMPLATE_C_BLOCK)
ID: b28009
Title: وَظِيفَةُ الصُّورَةِ البَيَانِيَّةِ (القِيمَةُ الفَنِّيَّةُ)
Content: <p class="text-lg text-justify leading-loose">لِلصُّورَةِ البَيَانِيَّةِ (التَّشْبِيه، الاسْتِعَارَة) وَظَائِفُ مُتَعَدِّدَةٌ تُبْرِزُ المَعْنَى وَتُؤَثِّرُ فِي المُتَلَقِّي، مِنْهَا:</p>

=== BLOCK 11: Function - Explanation ===
(Component: TEMPLATE_C_BLOCK)
ID: b28010
Title: ١- الشَّرْحُ وَالتَّوْضِيحُ
Content: <p class="text-justify mb-2mm">تُعَدُّ خُطْوَةً أَوَّلِيَّةً فِي إِقْنَاعِ المُتَلَقِّي بِمَعْنًى مِنَ المَعَانِي، حَيْثُ تَنْتَقِلُ الصُّورَةُ مِنَ الوَاضِحِ إِلَى الأَوْضَحِ.</p>
(Component: TEMPLATE_C_BENEFIT_TIP)
Title: القَالِبُ النَّظَرِيُّ للإِجَابَةِ
Content: شَرَحَتِ الصُّورَةُ مَعْنَى: (... [المَعْنَى/الفِكْرَة] ...) وَوَضَّحَتْ ذَلِكَ المَعْنَى مِنْ خِلَالِ تَشْبِيهِ ... [المُشَبَّهُ] ... بِـ ... [المُشَبَّهُ بِهِ] ...، فَأَقْنَعَتِ المُتَلَقِّيَ بِمَضْمُونِ المَعْنَى وَصِدْقِهِ.

=== BLOCK 12: Function - Exaggeration ===
(Component: TEMPLATE_C_BLOCK)
ID: b28011
Title: ٢- المُبَالَغَةُ
Content: <p class="text-justify mb-2mm">يُقْصَدُ بِهَا التَّعْبِيرُ عَنِ الشَّيْءِ بِصُورَتِهِ العُلْيَا (المَثَلِ الأَعْلَى)، حَتَّى يُصْبِحَ الغَائِبُ حَاضِرًا وَالمُتَخَيَّلُ مُتَحَقِّقًا.</p>
(Component: TEMPLATE_C_BENEFIT_TIP)
Title: القَالِبُ النَّظَرِيُّ للإِجَابَةِ
Content: بَالَغَ الشَّاعِرُ فِي شَرْحِ مَعْنَى: (... [المَعْنَى] ...) وَتَوْضِيحِهِ بِتَشْبِيهِهِ ... [المُشَبَّهُ] ... بِـ ... [المُشَبَّهُ بِهِ] ...، حَيْثُ أَرَادَ أَنْ يُوصِلَ إِلَى المُتَلَقِّي الحَدَّ الأَعْلَى مِنْ ... [الصِّفَة] ...، فَجَعَلَ المُتَخَيَّلَ كَالمُتَحَقِّقِ.

=== BLOCK 13: Functions - Beautification & Uglification ===
(Component: TEMPLATE_C_SPLIT)
ID: b28012
Title: ٣- التَّحْسِينُ وَالتَّقْبِيحُ
Left_Title: التَّحْسِينُ
Left_Content: <p class="text-justify mb-2mm">جَعْلُ الحَسَنِ يَجْرِي فِي الصُّورَةِ لِجَذْبِ المُتَلَقِّي واسْتِمَالَتِهِ.</p><div class="bg-yellow-50 p-2mm rounded border border-yellow-200 text-sm"><span class="font-bold text-yellow-700">القَالِبُ:</span> حَسَّنَ الشَّاعِرُ مَعْنَى (...) بِتَشْبِيهِهِ (...) بـ (...)، فَأَثَّرَ ذَلِكَ فِي المُتَلَقِّي، وَأَثَارَ انْفِعَالَ (الحُبِّ/الإِعْجَابِ)، وَأَدَّى إِلَى جَذْبِهِ واسْتِمَالَتِهِ.</div>
Right_Title: التَّقْبِيحُ
Right_Content: <p class="text-justify mb-2mm">جَعْلُ القُبْحِ يَجْرِي فِي الصُّورَةِ لِلتَّنْفِيرِ مِنْهَا.</p><div class="bg-yellow-50 p-2mm rounded border border-yellow-200 text-sm"><span class="font-bold text-yellow-700">القَالِبُ:</span> قَبَّحَ الشَّاعِرُ مَعْنَى (...) بِتَشْبِيهِهِ (...) بـ (...)، فَأَثَّرَ ذَلِكَ فِي المُتَلَقِّي، وَأَثَارَ انْفِعَالَ (الكُرْهِ/الاشْمِئْزَازِ)، وَأَدَّى إِلَى نُفُورِهِ.</div>

=== BLOCK 14: Functions - Description & Suggestion ===
(Component: TEMPLATE_C_SPLIT)
ID: b28013
Title: ٤- الوَصْفُ وَالإِيحَاءُ
Left_Title: الوَصْفُ وَالمُحَاكَاةُ
Left_Content: <p class="text-justify mb-2mm">تَظْهَرُ عِنْدَ الاتِّبَاعِيِّينَ، حَيْثُ تَسْتَمِدُّ الصُّوَرُ عَنَاصِرَهَا مِنَ الوَاقِعِ المَحْسُوسِ.</p><div class="bg-blue-50 p-2mm rounded border border-blue-200 text-sm"><span class="font-bold text-blue-700">القَالِبُ:</span> اسْتَمَدَّتِ الصُّورَةُ عَنَاصِرَهَا مِنَ الوَاقِعِ المَحْسُوسِ (المُحَاكَاة)، حَيْثُ شَبَّهَ (...) بـ (...)، وَكِلَاهُمَا عُنْصُرَانِ حِسِّيَّانِ.</div>
Right_Title: الإِيحَاءُ
Right_Content: <p class="text-justify mb-2mm">تَظْهَرُ عِنْدَ الإِبْدَاعِيِّينَ، فَتُوحِي بِدِلَالَاتٍ مَعْنَوِيَّةٍ وَتُثِيرُ المَشَاعِرَ.</p><div class="bg-blue-50 p-2mm rounded border border-blue-200 text-sm"><span class="font-bold text-blue-700">القَالِبُ:</span> جَعَلَ الشَّاعِرُ الصُّورَةَ مُوحِيَةً بِتَشْبِيهِ (...) بـ (...)، فَهَذَا أَوْحَى بِـ (... وَ ...)، وَأَثَارَ مَشَاعِرَ (...).</div>

=== BLOCK 15: Functions - Projection & Symbolism ===
(Component: TEMPLATE_C_SPLIT)
ID: b28014
Title: ٥- إِضْفَاءُ النَّفْسِيَّةِ وَالرَّمْزُ
Left_Title: إِضْفَاءُ نَفْسِيَّةِ المُبْدِعِ
Left_Content: <p class="text-justify mb-2mm">تَنْقُلُ الطَّبِيعَةَ وَالأَشْيَاءَ بَعْدَ انْفِعَالِ المُبْدِعِ بِهَا، فَتَتَلَوَّنُ بِمَشَاعِرِهِ.</p><div class="bg-green-50 p-2mm rounded border border-green-200 text-sm"><span class="font-bold text-green-700">القَالِبُ:</span> شَخَّصَ الشَّاعِرُ (...) وَنَقَلَهُ بَعْدَ انْفِعَالِهِ بِهِ، فَتَلَوَّنَ بِمَشَاعِرِهِ وَرُؤَاهُ، حَيْثُ أَضْفَى عَلَيْهِ مَشَاعِرَ (...).</div>
Right_Title: الرَّمْزُ
Right_Content: <p class="text-justify mb-2mm">وَسِيلَةٌ لِلإِشَارَةِ وَالاخْتِصَارِ وَالتَّكْثِيفِ، تَخْتَبِئُ فِيهَا الدَّلَالَاتُ.</p><div class="bg-green-50 p-2mm rounded border border-green-200 text-sm"><span class="font-bold text-green-700">القَالِبُ:</span> رَمَزَ الشَّاعِرُ بـ (...) لـِ (...)، فَاخْتَصَرَ الكَلَامَ، وَكَثَّفَ المَعْنَى، وَأَوْحَى بِدِلَالَاتٍ مُخْتَلِفَةٍ.</div>

=== BLOCK 16: Metonymy Intro ===
(Component: TEMPLATE_C_BLOCK)
ID: b28015
Title: ثَالِثًا - الكِنَايَةُ
Content: <p class="text-accent text-lg leading-loose text-justify mb-2mm">هِيَ كَلَامٌ أُطْلِقَ، وَأُرِيدَ مَا يُلَازِمُهُ مِنْ مَعْنًى، مَعَ جَوَازِ إِرَادَةِ المَعْنَى الحَقِيقِيِّ. وَهِيَ تَعْبِيرٌ عَنِ المَعْنَى تَلْمِيحًا لَا تَصْرِيحًا.</p>
<div class="bg-grey-lighter p-2mm rounded border-l-4 border-accent"><span class="font-bold text-accent">القِيمَةُ الفَنِّيَّةُ:</span> تَقْرِيبُ المَعْنَى مِنَ الذِّهْنِ، وَتَأْكِيدُهُ.</div>

=== BLOCK 17: Metonymy Types Matrix ===
(Component: TEMPLATE_C_TABLE)
ID: b28016
Title: أَنْوَاعُ الكِنَايَةِ
Headers: النَّوْعُ | الشَّرْحُ | المِثَالُ
Rows:
<tr>
    <td class="font-bold text-primary">كِنَايَةٌ عَنْ صِفَةٍ</td>
    <td>المُكَنَّى عَنْهُ صِفَةٌ مَعْنَوِيَّةٌ (كَالشَّجَاعَةِ، الجُودِ...).</td>
    <td>طَوِيلُ النِّجَادِ رَفِيعُ العِمَادِ.<br><span class="text-xs text-gray-500">(كِنَايَةٌ عَنْ طُولِ القَامَةِ وَعِظَمِ الشَّأْنِ)</span></td>
</tr>
<tr>
    <td class="font-bold text-primary">كِنَايَةٌ عَنْ مَوْصُوفٍ</td>
    <td>يُطْلَبُ بِهَا المَوْصُوفُ نَفْسُهُ (اسْمُ ذَاتٍ).</td>
    <td>يَا أُمَّ الحَضَارَةِ.<br><span class="text-xs text-gray-500">(كِنَايَةٌ عَنْ مَدِينَةِ دِمَشْقَ)</span></td>
</tr>
<tr>
    <td class="font-bold text-primary">كِنَايَةٌ عَنْ نِسْبَةٍ</td>
    <td>نِسْبَةُ أَمْرٍ لِآخَرَ، أَوْ نَفْيُهُ عَنْهُ.</td>
    <td>المَجْدُ بَيْنَ ثَوْبَيْهِ.<br><span class="text-xs text-gray-500">(نِسْبَةُ المَجْدِ إِلَى المَمْدُوحِ)</span></td>
</tr>

=== BLOCK 18: Evidence Poem ===
(Component: TEMPLATE_C_POEM)
ID: b28017
Title: شَوَاهِدُ تَطْبِيقِيَّةٌ
Content:
<div class="poem-line flex justify-between items-center mb-2">
    <div class="hemistich w-45pct text-center font-amiri text-xl">كُلَّمَا قُلْتُ فِي غَدٍ أُدْرِكُ السُّؤْ</div>
    <div class="hemistich w-45pct text-center font-amiri text-xl">لَ أَتَانِي غَدٌ بِمَا لَا أَشَاءُ</div>
</div>
<div class="poem-line flex justify-between items-center mb-2">
    <div class="hemistich w-45pct text-center font-amiri text-xl">كُنْ هَزَارًا فِي عُشِّهِ يَتَغَنَّى</div>
    <div class="hemistich w-45pct text-center font-amiri text-xl">وَمَعَ الكَبْلِ لَا يُبَالِي الكُبُولَا</div>
</div>
<div class="poem-line flex justify-between items-center mb-2">
    <div class="hemistich w-45pct text-center font-amiri text-xl">هَاهُنَا وَارَيْتُ أَجْدَادِي هُنَا</div>
    <div class="hemistich w-45pct text-center font-amiri text-xl">وَهُمُ اخْتَارُوا ثَرَاهَا كَفَنَا</div>
</div>

=== BLOCK 19: Rhetorical Analysis ===
(Component: TEMPLATE_C_IRAB_ROW)
ID: b28018
Title: التَّحْلِيلُ البَلَاغِيُّ لِلشَّوَاهِدِ
Content:
<div class="irab-box flex-1 mx-1mm bg-white border border-gray-300 rounded shadow-sm text-center">
    <div class="irab-word bg-primary text-white py-1mm px-2mm font-bold rounded-t">أَتَانِي غَدٌ</div>
    <div class="irab-details p-2mm text-sm leading-snug">
        <span class="font-bold text-accent">اسْتِعَارَةٌ مَكْنِيَّةٌ</span><br>
        شَبَّهَ الغَدَ بِإِنْسَانٍ يَأْتِي، فَحَذَفَ المُشَبَّهَ بِهِ وَأَبْقَى لَازِمَةً (أَتَانِي).<br>
        <span class="text-xs text-gray-500">الوَظِيفَةُ: التَّشْخِيصُ وَالتَّوْضِيحُ.</span>
    </div>
</div>
<div class="irab-box flex-1 mx-1mm bg-white border border-gray-300 rounded shadow-sm text-center">
    <div class="irab-word bg-primary text-white py-1mm px-2mm font-bold rounded-t">كُنْ هَزَارًا</div>
    <div class="irab-details p-2mm text-sm leading-snug">
        <span class="font-bold text-accent">تَشْبِيهٌ مُؤَكَّدٌ</span><br>
        شَبَّهَ المُخَاطَبَ بِالهَزَارِ، وَحَذَفَ الأَدَاةَ.<br>
        <span class="text-xs text-gray-500">الوَظِيفَةُ: التَّحْسِينُ وَالتَّوْضِيحُ.</span>
    </div>
</div>
<div class="irab-box flex-1 mx-1mm bg-white border border-gray-300 rounded shadow-sm text-center">
    <div class="irab-word bg-primary text-white py-1mm px-2mm font-bold rounded-t">ثَرَاهَا كَفَنَا</div>
    <div class="irab-details p-2mm text-sm leading-snug">
        <span class="font-bold text-accent">تَشْبِيهٌ بَلِيغٌ</span><br>
        شَبَّهَ الثَّرَى بِالكَفَنِ، حُذِفَتِ الأَدَاةُ وَوَجْهُ الشَّبَهِ.<br>
        <span class="text-xs text-gray-500">الوَظِيفَةُ: الإِيحَاءُ بِالتَّضْحِيَةِ.</span>
    </div>
</div>

=== BLOCK 20: Exam ===
(Component: TEMPLATE_C_EXAM)
ID: b28019
Title: اخْتَبِرْ نَفْسَكَ
Question_1: س١- اسْتَخْرِجِ الصُّورَةَ البَيَانِيَّةَ مِنْ قَوْلِهِ: (رَايَاتُنَا بَصَرُ الضَّرِيرِ)، وَسَمِّهَا، وَحَلِّلْهَا.
Question_2: س٢- مَيِّزِ التَّشْخِيصَ مِنَ التَّجْسِيمِ فِي العِبَارَتَيْنِ: (أَشْوَاقُ سُنْبُلَةٍ)، (يَصُبُّ فِيهَا النُّورَ).
Question_3: س٣- اشْرَحْ وَظِيفَةَ "الشَّرْحِ وَالتَّوْضِيحِ" فِي قَوْلِ الشَّاعِرَةِ: (أَغْرَقُ فِي بَحْرِ يَأْسٍ).
Question_4: س٤- هَاتِ مِنَ الأَبْيَاتِ مِثَالًا لِكِنَايَةٍ عَنْ نِسْبَةٍ.

--- END STREAM ---
