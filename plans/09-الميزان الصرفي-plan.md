# **SESSION 09.0**

[TASK DEFINITION]
Objective: Implement الميزان الصرفي.
File: `pages/09.0_nXX_الميزان الصرفي.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually, instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/09.1_...`.
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
[LESSON_NUMBER]: 09
[CHAPTER_TITLE]: الميزان الصرفي
[CATEGORY_HEADER]: الصرف
[SECTION_HEADER]: المستوى اللغوي
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition and Concept ===
(Component: TEMPLATE_C_BLOCK)
Title: الْمِيزَانُ الصَّرْفِيُّ
Content:
<p class="text-justify leading-relaxed">
    <span class="text-accent font-bold">هُوَ مِقْيَاسٌ لِمَعْرِفَةِ حُرُوفِ الْكَلِمَةِ</span>، يَتَأَلَّفُ مِنْ ثَلاثَةِ أَحْرُفٍ تُقَابِلُ الأُصُولَ الثَّلاثَةَ الَّتِي تَتَكَوَّنُ مِنْهَا أَغْلَبُ الْكَلِمَاتِ الْعَرَبِيَّةِ (الفَاءُ وَالعَيْنُ وَاللَّامُ)، عَلَى النَّحْوِ الآتِي:
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
<ul class="structured-list pr-5mm space-y-2mm">
    <li class="list-item-content">
        <span class="font-bold text-accent">تَطَابُقُ الْحَرَكَاتِ:</span> ضَبْطُ بِنْيَةِ الْكَلِمَةِ الْمَوْزُونَةِ (بِالْحَرَكَاتِ وَالسَّكَنَاتِ) يُطَابِقُ ضَبْطَ الْوَزْنِ الصَّرْفِيِّ تَمَامًا، وَعَدَدُ حُرُوفِ الْكَلِمَةِ الْمَوْزُونَةِ يُسَاوِي عَدَدَ حُرُوفِ الْمِيزَانِ.
    </li>
    <li class="list-item-content">
        <span class="font-bold text-accent">الرُّبَاعِيُّ وَالْخُمَاسِيُّ الْأَصْلِيُّ:</span> إِذَا كَانَتْ حُرُوفُ الْكَلِمَةِ الأَصْلِيَّةِ أَرْبَعَةَ حُرُوفٍ، نُكَرِّرُ اللّامَ فِي آخِرِ الْمِيزَانِ (فَعْلَلَ). وَإِنْ كَانَتْ خَمْسَةَ أَحْرُفٍ، نَزِيدُ لَامَيْنِ (فَعَلَّلَ).
    </li>
</ul>

=== BLOCK 5: Four & Five Letter Examples ===
(Component: TEMPLATE_C_TABLE)
Title: نَمُوذَجُ الرُّبَاعِيِّ وَالْخُمَاسِيِّ
Content:
| حروف الميزان | فاء الفعل | عين الفعل | لام الفعل | الحرف ٤ | الحرف ٥ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| الكلمة (بَعْثَرَ) | بَـ | ـعْـ | ـثَـ | ـرَ | - |
| الميزان | فَـ | ـعْـ | ـلَـ | ـلَ | - |
| الكلمة (غَضَنْفَرَ) | غَـ | ـضَـ | ـنْـ | ـفَـ | ـرَ |
| الميزان | فَـ | ـعَـ | ـلْـ | ـلَـ | ـلَ |

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
<ul class="structured-list pr-5mm space-y-2mm">
    <li class="list-item-content">
        <span class="font-bold text-accent">الْمُعْتَلُّ:</span> يُعَامَلُ كَالصَّحِيحِ. مِثَال: (وَعَدَ ⟵ فَعَلَ)، (قَامَ ⟵ فَعَلَ). إِذَا كَانَتِ الْعَيْنُ مُعْتَلَّةً (يَقُولُ)، نَعُدُّهَا مُتَحَرِّكَةً فِي الْمِيزَانِ (يَفْعُلُ) عَلَى وَزْنِ (يَكْتُبُ).
    </li>
    <li class="list-item-content">
        <span class="font-bold text-accent">الْمُضَعَّفُ الثُّلاثِيُّ:</span> الْحَرْفُ الْمُشَدَّدُ يُعَدُّ حَرْفَيْنِ (عَيْنٌ وَلَامٌ) وَلَا يُشَدَّدُ فِي الْمِيزَانِ. مِثَال: (شَدَّ ⟵ فَعَلَ).
    </li>
    <li class="list-item-content">
        <span class="font-bold text-accent">الْحَذْفُ:</span> إِذَا حُذِفَ حَرْفٌ مِنَ الْكَلِمَةِ، يُحْذَفُ مَا يُقَابِلُهُ فِي الْمِيزَانِ. مِثَال: (قُلْ ⟵ فُلْ)، (ارْمِ ⟵ افْعِ).
    </li>
</ul>

=== BLOCK 8: Core Matrix (Solved Applied Examples) ===
(Component: TEMPLATE_C_TABLE)
Title: خُلَاصَةُ التَّطْبِيقَاتِ الصَّرْفِيَّةِ (مُجَابَةٌ)
Content:
| الكلمة | الوزن | الكلمة | الوزن | الكلمة | الوزن |
| :---: | :---: | :---: | :---: | :---: | :---: |
| قُلْتُ | فُلْتُ | لَمْ يَرَ | لَمْ يَفَ | غَدٍ | فَعٍ |
| يَنقَضِي | يَنْفَعِلُ | ثِقَةٌ | عِلَةٌ | حَاج | فَاعٍ |
| بُرُوق | فُعُول | كُنْ | فُلْ | غَدَوْتَ | فَعَلْتَ |
| تَخِذْتَ | فَعِلْتَ | الأماني | الأفاعل | عشا | فَلَا |
| أوهت | أفعت | تغطت | تفعّت | عاد | فَعَل |
| رئاسة | فِعَالَة | تستقل | تَسْتَفْعِل | تذوب | تَفْعُل |
| حزت | فُلْت | عِش | فِل | الفَن | الفَعْل |
| أغرانِي | أفعَلَني | أرجو | أفعُل | أشتهي | أفتَعِل |
| راح | فَعَل | يَنِم | يَفِل | خَلا | فَعَل |
| أسطورة | أفعُولَة | قِل | فِل | لاقني | فاعِني |
| سِل | فِل | يتصباني | يتفعّلني | - | - |

=== BLOCK 9: Exam (Test Yourself) ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question:
<p class="font-bold mb-2mm">س ١ - زِنْ كُلَّ كَلِمَةٍ مِمَّا يَأْتِي مَعَ ضَبْطِ الْمِيزَانِ بِالْحَرَكَاتِ:</p>
<div class="flex flex-wrap gap-2mm justify-center text-center">
    <span class="bg-white px-3mm py-1mm rounded border border-gray-200">اسْتَغْفَرَ</span>
    <span class="bg-white px-3mm py-1mm rounded border border-gray-200">دَحْرَجَ</span>
    <span class="bg-white px-3mm py-1mm rounded border border-gray-200">قِفْ</span>
    <span class="bg-white px-3mm py-1mm rounded border border-gray-200">صُمْ</span>
    <span class="bg-white px-3mm py-1mm rounded border border-gray-200">انْطَلَقَ</span>
</div>

--- END STREAM ---
