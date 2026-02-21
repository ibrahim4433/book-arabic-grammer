# **SESSION 00.0**

[TASK DEFINITION]
Objective: Implement الميزان الصرفي.
File: `pages/00.0_nXX_الميزان الصرفي.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually, instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/00.1_...`.
3. Text Content: 100% Arabic with full Harakat.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`, `.highlight-green` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
    *   **Rule:** NO INLINE STYLES.
    *   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
    *   **Mapping:**
        *   `style="width: 20%"` -> `class="w-20pct"`
        *   `style="margin-top: 2mm"` -> `class="mt-2mm"`
        *   `style="text-align: center"` -> `class="text-center"`
        *   `style="font-weight: bold"` -> `class="font-bold"`
7. Templates: You are forbidden from inventing new HTML tags or classes. You must map all content strictly using "Jules-workspace/Templates/" components as the STREAM says.
8. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). Use "Jules-workspace/id_manager.py" to generate or verify them.
9. **Self-Correction:** Run "Jules-workspace/lint_pages.py" after creating html files. If it fails, you MUST fix the errors (usually inline styles) before submitting.
10. Do not summarize examples.
11. Do not provide uncompleted text content using (...).
12. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed.
13. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER)
[LESSON_NUMBER]: 00
[CHAPTER_TITLE]: الميزان الصرفي
[CATEGORY_HEADER]:
[SECTION_HEADER]:
[AUTHOR_NAME]:
[AUTHOR_PHONE]:

=== BLOCK 2: Definition and Concept ===
(Component: TEMPLATE_C_BLOCK)
Title: الْمِيزَانُ الصَّرْفِيُّ
Content:
<p class="text-justify leading-relaxed">
    <span class="text-accent font-bold">هُوَ مِقْيَاسٌ لِمَعْرِفَةِ حُرُوفِ الْكَلِمَةِ</span>، يَتَأَلَّفُ مِنْ ثَلاثَةِ أَحْرُفٍ تُقَابِلُ الأُصُولَ الثَّلاثَةَ الَّتِي تَتَكَوَّنُ مِنْهَا أَغْلَبُ الْكَلِمَاتِ الْعَرَبِيَّةِ (الفَاءُ وَالعَيْنُ وَاللَّامُ).
</p>

=== BLOCK 3: Basic Weighting Example ===
(Component: TEMPLATE_C_TABLE)
Title: نَمُوذَجُ وَزْنِ الْفِعْلِ الثُّلَاثِيِّ
Content:
| حروف الميزان | فاء الفعل | عين الفعل | لام الفعل |
| :--- | :---: | :---: | :---: |
| الكلمة | ضَـ | ـحِـ | ـكَ |
| الميزان الصَّرْفِيُّ | فَـ | ـعِـ | ـلَ |

=== BLOCK 4: Fundamental Rules ===
(Component: TEMPLATE_C_BLOCK)
Title: قَوَاعِدُ ضَبْطِ الْمِيزَانِ
Content:
<ul class="list-disc pr-5mm space-y-2mm">
    <li>
        <span class="font-bold text-accent">تَطَابُقُ الْحَرَكَاتِ:</span> ضَبْطُ بِنْيَةِ الْكَلِمَةِ الْمَوْزُونَةِ (بِالْحَرَكَاتِ وَالسَّكَنَاتِ) يُطَابِقُ ضَبْطَ الْوَزْنِ الصَّرْفِيِّ تَمَامًا، وَعَدَدُ حُرُوفِ الْكَلِمَةِ الْمَوْزُونَةِ يُسَاوِي عَدَدَ حُرُوفِ الْمِيزَانِ.
    </li>
    <li>
        <span class="font-bold text-accent">الرُّبَاعِيُّ الْأَصْلِيُّ:</span> إِذَا كَانَتْ حُرُوفُ الْكَلِمَةِ الأَصْلِيَّةِ أَرْبَعَةَ حُرُوفٍ، فَإِنَّنَا نُكَرِّرُ اللّامَ فِي آخِرِ الْمِيزَانِ الصَّرْفِيِّ (فَعْلَلَ).
    </li>
</ul>

=== BLOCK 5: Four-Letter Root Example ===
(Component: TEMPLATE_C_TABLE)
Title: نَمُوذَجُ وَزْنِ الرُّبَاعِيِّ (بَعْثَرَ)
Content:
| حروف الميزان | فاء الفعل | عين الفعل | لام الفعل | الحرف الرَّابع |
| :--- | :---: | :---: | :---: | :---: |
| الكلمة | بَـ | ـعْـ | ـثَـ | ـرَ |
| الميزان الصَّرْفِيُّ | فَـ | ـعْـ | ـلَـ | ـلَ |
<p class="text-sm mt-2mm text-gray-700">
    * وَنَزِيدُ لامَيْنِ فِي آخِرِ الْمِيزَانِ إِذَا كَانَ الْحَرْفَانِ الزَّائِدَانِ مِنْ أَصْلِ الْكَلِمَةِ؛ فَوَزْنُ (<span class="highlight-red">غَضَنْفَرَ</span>) يُصْبِحُ (<span class="highlight-blue">فَعَلَّلَ</span>)، وَوَزْنُ (<span class="highlight-red">زَبَرْجَدَ</span>) يُصْبِحُ (<span class="highlight-blue">فَعَلَّلَ</span>).
</p>

=== BLOCK 6: Rules of Increase (Ziyadah) ===
(Component: TEMPLATE_C_BLOCK)
Title: أَحْكَامُ حُرُوفِ الزِّيَادَةِ
Content:
<div class="space-y-3mm">
    <p class="font-bold border-b border-gray-300 pb-1mm mb-2mm">١- تَكْرَارُ الْأَصْلِ:</p>
    <p>إِذَا كَانَ الْحَرْفُ الزَّائِدُ نَاتِجًا عَنْ تَكْرِيرِ حَرْفٍ مِنْ حُرُوفِ الْكَلِمَةِ الأَصْلِيَّةِ، <span class="highlight-red">كَرَّرْنَا مَا يُقَابِلُهُ فِي الْمِيزَانِ</span>.</p>
    <p class="bg-gray-100 p-2mm rounded text-center">
        (سَبَّحَ) ⟵ (<span class="highlight-blue">فَعَّلَ</span>) &nbsp;|&nbsp; (عَلَّمَ) ⟵ (<span class="highlight-blue">فَعَّلَ</span>)
    </p>

    <p class="font-bold border-b border-gray-300 pb-1mm mb-2mm mt-3mm">٢- الزِّيَادَةُ غَيْرُ الْأَصْلِيَّةِ:</p>
    <p>إِذَا كَانَ الْحَرْفُ الزَّائِدُ حَرْفًا غَيْرَ أَصْلِيٍّ وَغَيْرَ مُكَرَّرٍ، نَزِنُ الأُصُولَ فَقَطْ بِمَا يُقَابِلُهَا، ثُمَّ <span class="highlight-red">نَذْكُرُ الْحُرُوفَ الزَّائِدَةَ كَمَا هِيَ</span>.</p>
    <p class="bg-gray-100 p-2mm rounded text-center">
        (كَاتِبٌ) ⟵ (<span class="highlight-blue">فَاعِلٌ</span>) &nbsp;|&nbsp; (اسْتَفْتَحَ) ⟵ (<span class="highlight-blue">اسْتَفْعَلَ</span>)
    </p>
</div>

=== BLOCK 7: Special Rules (Weak, Geminated, Deleted) ===
(Component: TEMPLATE_C_BLOCK)
Title: قَوَاعِدُ الْمُعْتَلِّ وَالْمُضَعَّفِ وَالْحَذْفِ
Content:
<ul class="list-disc pr-5mm space-y-2mm">
    <li>
        <span class="font-bold text-accent">الْمُعْتَلُّ:</span> يُعَامَلُ كَالصَّحِيحِ.
        <br><span class="text-sm">مِثَال:</span> (وَعَدَ ⟵ فَعَلَ)، (قَامَ ⟵ فَعَلَ). إِذَا كَانَتِ الْعَيْنُ مُعْتَلَّةً (يَقُولُ)، نَعُدُّهَا مُتَحَرِّكَةً فِي الْمِيزَانِ (يَفْعُلُ) عَلَى وَزْنِ (يَكْتُبُ).
    </li>
    <li>
        <span class="font-bold text-accent">الْمُضَعَّفُ الثُّلاثِيُّ:</span> الْحَرْفُ الْمُشَدَّدُ يُعَدُّ حَرْفَيْنِ (عَيْنٌ وَلَامٌ) وَلَا يُشَدَّدُ فِي الْمِيزَانِ.
        <br><span class="text-sm">مِثَال:</span> (شَدَّ ⟵ فَعَلَ).
    </li>
    <li>
        <span class="font-bold text-accent">الْحَذْفُ:</span> إِذَا حُذِفَ حَرْفٌ مِنَ الْكَلِمَةِ، يُحْذَفُ مَا يُقَابِلُهُ فِي الْمِيزَانِ.
        <br><span class="text-sm">مِثَال:</span> (قُلْ ⟵ فُلْ)، (ارْمِ ⟵ افْعِ).
    </li>
</ul>

=== BLOCK 8: Core Matrix (Summary) ===
(Component: TEMPLATE_C_TABLE)
Title: خُلَاصَةُ قَوَاعِدِ الْمِيزَانِ الصَّرْفِيِّ
Content:
| الحالة | القاعدة | مثال | الوزن |
| :--- | :--- | :---: | :---: |
| الثلاثي المجرد | مقابلة الأصول بالفاء والعين واللام | كَتَبَ | فَعَلَ |
| الرباعي المجرد | تكرار اللام | دَحْرَجَ | فَعْلَلَ |
| الزيادة (تكرار) | تكرار ما يقابله في الميزان | قَدَّمَ | فَعَّلَ |
| الزيادة (حرف جديد) | زيادة الحرف نفسه في الميزان | أَكْرَمَ | أَفْعَلَ |
| المضعف الثلاثي | فك التضعيف (لا يظهر في الميزان) | مَدَّ | فَعَلَ |
| الحذف | حذف ما يقابله في الميزان | قِ | عِ |

=== BLOCK 9: Solved Applied Examples ===
(Component: TEMPLATE_C_BLOCK)
Title: أَمْثِلَةٌ تَطْبِيقِيَّةٌ مُجَابَةٌ
Content:
<div class="space-y-2mm">
    <div class="flex flex-col bg-gray-50 p-2mm rounded border-r-4 border-accent">
        <span class="font-bold text-gray-800">س١- زِنْ كُلَّ كَلِمَةٍ مِمَّا يَأْتِي: (قُلْتُ، لَمْ يَرَ، غَدٍ، يَنقَضِي).</span>
        <span class="mt-1mm text-accent">ج١- قُلْتُ: فُلْتُ | لَمْ يَرَ: لَمْ يَفَ | غَدٍ: فَعٍ | يَنقَضِي: يَنْفَعِلُ.</span>
    </div>
    <div class="flex flex-col bg-gray-50 p-2mm rounded border-r-4 border-accent">
        <span class="font-bold text-gray-800">س٢- زِنْ: (ثِقَةٌ، حَاج، بُرُوق).</span>
        <span class="mt-1mm text-accent">ج٢- ثِقَةٌ: عِلَةٌ | حَاج: فَاعٍ | بُرُوق: فُعُول.</span>
    </div>
    <div class="flex flex-col bg-gray-50 p-2mm rounded border-r-4 border-accent">
        <span class="font-bold text-gray-800">س٣- زِنْ: (كُنْ، غَدَوْتَ، تَخِذْتَ).</span>
        <span class="mt-1mm text-accent">ج٣- كُنْ: فُلْ | غَدَوْتَ: فَعَلْتَ | تَخِذْتَ: فَعِلْتَ.</span>
    </div>
    <div class="flex flex-col bg-gray-50 p-2mm rounded border-r-4 border-accent">
        <span class="font-bold text-gray-800">س٤- اذكر وزن: (الأماني، عشا، أوهت، تغطت).</span>
        <span class="mt-1mm text-accent">ج٤- الأماني: الأفاعل | عشا: فَلَا | أوهت: أفعت | تغطت: تفعّت.</span>
    </div>
</div>

=== BLOCK 10: Exam (Unsolved) ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question:
<p class="font-bold mb-2mm">س ٥ - اذكر الوزن الصرفي للكلمات الآتية:</p>
<p class="mb-4mm text-center">(عاد - رئاسة - تستقل - تذوب - حزت).</p>

<p class="font-bold mb-2mm">س ٦ - بيّن الوزن الصرفي للكلمتين:</p>
<p class="mb-4mm text-center">(عِش - الفَن).</p>

<p class="font-bold mb-2mm">س ٧ - حدّد وزن كل من الكلمات الآتية:</p>
<p class="mb-4mm text-center">أغرانِي - أرجو - أشتهي - راح.</p>

<p class="font-bold mb-2mm">س ٨ - اذكر وزن كل من الكلمات الآتية:</p>
<p class="mb-4mm text-center">(يَنِم - خَلا - أسطورة - قِل).</p>

<p class="font-bold mb-2mm">س ٩ - ما الوزن الصرفي لكل من الكلمات الآتية:</p>
<p class="mb-4mm text-center">(لاقني - سِل - يتصباني)؟</p>

--- END STREAM ---
