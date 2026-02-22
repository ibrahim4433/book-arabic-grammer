# **SESSION 09.0**

[TASK DEFINITION]
Objective: Implement الميزان الصرفي.
File: `pages/09.0_nXX_الميزان الصرفي.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/09.1_...`.
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
14. after finishing the pages you must run "Jules-workspace/smart_replace_haam.py" to fix all هام , هامة mistakes !
15. every text line or raw in the page if it is more than 18 arabic words , you must wrap it into a second line or it will maybe smashed !

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

=== BLOCK 2: Definition & Concept ===
(Component: TEMPLATE_C_BLOCK)
Title: تعريف الميزان الصرفي
Content:
<p class="text-accent mb-2mm">هو مِقْياسٌ لمعرفةِ حُروفِ الكَلِمَةِ، يَتَأَلَّفُ مِنْ ثَلَاثَةِ أَحْرُفٍ تُقَابِلُ الأُصُولَ الثَّلَاثَةَ الَّتِي تَتَكَوَّنُ مِنْهَا أَغْلَبُ الكَلِمَاتِ العَرَبِيَّةِ.</p>

(Component: TEMPLATE_C_TABLE)
Title: مثال توضيحي
Columns: حروف الميزان, فاء الفعل, عين الفعل, لام الفعل
Rows:
- الكَلِمَةُ | ضَ | حِ | كَ
- المِيزَانُ | <span class="highlight-red">فَ</span> | <span class="highlight-red">عِ</span> | <span class="highlight-red">لَ</span>

=== BLOCK 3: The Core Matrix (Rules Summary) ===
(Component: TEMPLATE_C_TABLE)
Title: قواعد الميزان الصرفي
Columns: الحالة, القاعدة, مثال, الوزن
Rows:
- الفِعْلُ الثُّلَاثِيُّ المُجَرَّدُ | تُقَابَلُ أُصُولُهُ بِـ (ف ع ل) مَعَ ضَبْطِ الحَرَكَاتِ | ضَحِكَ | فَعِلَ
- الفِعْلُ الرُّبَاعِيُّ المُجَرَّدُ | نُكَرِّرُ اللَّامَ فِي آخِرِ المِيزَانِ الصَّرْفِيِّ | بَعْثَرَ | فَعْلَلَ
- الزِّيَادَةُ بِالتَّكْرَارِ (التَّضْعِيف) | نُكَرِّرُ مَا يُقَابِلُهُ فِي المِيزَانِ | قَدَّمَ | فَعَّلَ
- الزِّيَادَةُ بِأَحْرُفٍ زَائِدَةٍ | نَزِنُ الأُصُولَ ونُضِيفُ الزَّوَائِدَ كَمَا هِيَ | اسْتَفْتَحَ | اسْتَفْعَلَ
- الإِعْلَالُ وَالحَذْفُ | نَحْذِفُ مَا يُقَابِلُهُ فِي المِيزَانِ | قُلْ | فُلْ

=== BLOCK 4: Deep Dive (Split) ===
(Component: TEMPLATE_C_SPLIT)
[RIGHT_TITLE]: الزيادة في الميزان
[RIGHT_CONTENT]:
(Component: TEMPLATE_C_BLOCK)
Title: زيادة الحروف
Content:
<p class="mb-2mm">إذا كانَتْ حُرُوفُ الكَلِمَةِ الأَصْلِيَّةِ أَرْبَعَةً، نُكَرِّرُ اللَّامَ، مِثْلَ: <span class="highlight-blue">بَعْثَرَ</span> (فَعْلَلَ). وَإِذَا كَانَتْ خَمْسَةً، نَزِيدُ لَامَيْنِ، مِثْلَ: <span class="highlight-blue">غَضَنْفَر</span> (فَعَلَّل).</p>
<p class="mb-2mm">أَمَّا إِذَا كَانَتِ الزِّيَادَةُ نَاتِجَةً عَنْ تَكْرِيرِ حَرْفٍ أَصْلِيٍّ، نُكَرِّرُ مَا يُقَابِلُهُ فِي المِيزَانِ، مِثْلَ: <span class="highlight-blue">سَبَّحَ</span> (فَعَّلَ). وَإِذَا كَانَتْ غَيْرَ أَصْلِيَّةٍ، نَذْكُرُهَا كَمَا هِيَ، مِثْلَ: <span class="highlight-blue">كَاتِبٌ</span> (فَاعِلٌ).</p>

[LEFT_TITLE]: الإعلال والحذف
[LEFT_CONTENT]:
(Component: TEMPLATE_C_BLOCK)
Title: التعامل مع المعتل والمحذوف
Content:
<p class="mb-2mm">يُعْتَبَرُ الحَرْفُ المُعْتَلُّ كَأَنَّهُ صَحِيحٌ فَيُقَابَلُ بِنَظِيرِهِ، مِثْلَ: <span class="highlight-red">وَعَدَ</span> (فَعَلَ) و <span class="highlight-red">قَامَ</span> (فَعَلَ). وَعِنْدَ حُصُولِ حَذْفٍ فِي الكَلِمَةِ، نَحْذِفُ مَا يُقَابِلُهُ فِي المِيزَانِ.</p>

(Component: TEMPLATE_C_LIST)
Items:
- <span class="font-bold">قُلْ</span> (أَصْلُهَا قَالَ): وَزْنُهَا <span class="highlight-red">فُلْ</span> (حُذِفَتِ العَيْنُ).
- <span class="font-bold">ارْمِ</span> (أَصْلُهَا رَمَى): وَزْنُهَا <span class="highlight-red">افْعِ</span> (حُذِفَتِ اللَّامُ).

=== BLOCK 5: Solved Applied Examples ===
(Component: TEMPLATE_C_TABLE)
Title: أمثلة تطبيقية محلولة
Columns: الكلمة, الوزن الصرفي
Rows:
- قُلْتُ | فُلْتُ
- لَمْ يَرَ | لَمْ يَفَ
- غَدِ | فَعِ
- يَنْقَضِي | يَنْفَعِلُ
- ثِقَةٌ | عِلَةٌ
- حَاج | فَاعٍ
- بُرُوق | فُعُول
- كُنْ | فُلْ
- غَدَوْتَ | فَعَلْتَ
- تَخِذَتْ | فَعِلَتْ
- الأَمَانِي | الأَفَاعِل
- عِشْنَا | فِلْنَا
- أَوْهَتْ | أَفْعَتْ
- تَغَطَّتْ | تَفَعَّتْ
- عادَ | فَعَلَ
- رِئَاسَة | فِعَالَة
- تَسْتَقِل | تَسْتَفْعِل
- تَذُوب | تَفْعُل
- حِزْتَ | فِلْتَ
- عِشْ | فِلْ
- الفَنّ | الفَعْل
- أَغْرَانِي | أَفْعَلَنِي
- أَرْجُو | أَفْعُل
- أَشْتَهِي | أَفْتَعِل
- رَاحَ | فَعَلَ
- يَنِمْ | يَفِلْ
- خَلَا | فَعَلَ
- أُسْطُورَة | أُفْعُولَة
- قُلْ | فُلْ
- لَاقِنِي | فَاعِنِي
- سِلْ | فِلْ
- يَتَصَبَانِي | يَتَفَعَّلَنِي

=== BLOCK 6: Benefits ===
(Component: TEMPLATE_C_BENEFIT)
Title: تنبيه هام
Content:
في المُضَعَّفِ الثُّلاثيِّ (مثل: شَدَّ)، الحرفُ المشدَّدُ عبارة عن حرفين: أحدهما عينُ الكلمةِ والآخرُ لامُها، ولذلك لا يُشَدَّدُ في الميزانِ، فوزنُ (شَدَّ) هو (فَعَلَ).

=== BLOCK 7: Exam ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: زِنِ الكَلِمَاتِ الآتِيَةَ وَاضْبِطِ المِيزَانَ بِالشَّكْلِ التَّامِّ: (اسْتَمَعَ، انْتَصَرَ، دَحْرَجَ، اسْتَغْفَرَ).
Answer: (متروك للطالب)

--- END STREAM ---
