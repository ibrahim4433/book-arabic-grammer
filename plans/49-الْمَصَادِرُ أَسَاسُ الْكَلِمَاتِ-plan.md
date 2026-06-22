# **SESSION 49.0**

[TASK DEFINITION]
Objective: Implement الْمَصَادِرُ أَسَاسُ الْكَلِمَاتِ.
File: `pages/49.0_nXX_الْمَصَادِرُ أَسَاسُ الْكَلِمَاتِ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/49.1_nXX_الْمَصَادِرُ أَسَاسُ الْكَلِمَاتِ_تابع.html`. If page has a lot of blank space add exam elements from the lesson.
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
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
15. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 49
[CHAPTER_TITLE]: الْمَصَادِرُ أَسَاسُ الْكَلِمَاتِ
[CATEGORY_HEADER]: المستوى المتوسط
[SECTION_HEADER]: علم الصرف
[AUTHOR_NAME]: أ. حنا خفيف
[AUTHOR_PHONE]:  

=== BLOCK 2: تَعْرِيفُ المَصْدَرِ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَعْرِيفُ المَصْدَرِ
Content:
<p class="text-accent">المصدرُ هو الْجَامِدُ الْمَعْنَى؛ اسمٌ يدلُّ على الحدَثِ مُجَرَّدًا مِن الزَّمنِ (بِدُونِ مَاضٍ أَوْ حَاضِرٍ)، وهو الأصلُ الذي تصدُرُ (تَخْرُجُ) عنْهُ الأفعالُ، والأسماءُ المُشتقَّةُ.</p>
<p>فالمصدرُ (<span class="highlight-red">الذَّهَابُ</span>) يَدُلُّ عَلَى حَدَثِ الْمَشْيِ بِلَا زَمَنٍ. وَنَأْخُذُ مِنْهُ الْفِعْلَ الْمَاضِي (<span class="highlight-blue">ذَهَبَ</span>)، وَالْمُضَارِعَ (<span class="highlight-blue">يَذْهَبُ</span>)، وَالأَمْرَ (<span class="highlight-blue">اذْهَبْ</span>)، وَاسْمَ الْفَاعِلِ (<span class="highlight-blue">ذَاهِبٌ</span>).</p>

=== BLOCK 3: أَنْوَاعُ الْمَصَادِرِ وَصِيَاغَتُهَا ===
(Component: TEMPLATE_C_SPLIT.html)
LeftSide:
(Component: TEMPLATE_C_BLOCK.html)
Title: ١- المَصَادِرُ السَّمَاعِيَّةُ (مَصَادِرُ الْأَفْعَالِ الثُّلَاثِيَّةِ)
Content:
<p>لَيْسَ لَهَا قَاعِدَةٌ ثَابِتَةٌ، وَتُعْرَفُ بِالسَّمَاعِ عَنِ الْعَرَبِ وَالرُّجُوعِ لِلْمُعْجَمِ.</p>
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: <span class="highlight-blue">شَرِبَ</span> -> <span class="highlight-red">شُرْب</span>
[LIST_ITEM_CONTENT]: <span class="highlight-blue">ذَهَبَ</span> -> <span class="highlight-red">ذَهَاب</span>
[LIST_ITEM_CONTENT]: <span class="highlight-blue">نَجَحَ</span> -> <span class="highlight-red">نَجَاح</span>
[LIST_ITEM_CONTENT]: <span class="highlight-blue">طَارَ</span> -> <span class="highlight-red">طَيَرَان</span>
[LIST_ITEM_CONTENT]: <span class="highlight-blue">فَرِحَ</span> -> <span class="highlight-red">فَرَح</span>
[LIST_ITEM_CONTENT]: <span class="highlight-blue">خَرَجَ</span> -> <span class="highlight-red">خُرُوج</span>

RightSide:
(Component: TEMPLATE_C_BLOCK.html)
Title: ٣- مَصَادِرُ الأَفْعَالِ الخُمَاسِيَّةِ وَالسُّدَاسِيَّةِ (قَوَاعِدُ مَضْمُونَةٌ)
Content:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: إِذَا بَدَأَ الفِعْلُ بِهَمْزَةِ وَصْلٍ (ا): نَكْسِرُ الْحَرْفَ الثَّالِثَ، وَنُضِيفُ أَلِفاً قَبْلَ الآخِرِ. (<span class="highlight-green">اعْتَمَدَ -> اعْتِمَاد</span>) ، (<span class="highlight-green">اسْتَقْبَلَ -> اسْتِقْبَال</span>) ، (<span class="highlight-green">اسْتَخْدَمَ -> اسْتِخْدَام</span>) .
[LIST_ITEM_CONTENT]: إِذَا بَدَأَ الفِعْلُ بِتَاءٍ (تَـ): فَقَطْ نَضَعُ ضَمَّةً قَبْلَ الآخِرِ (نَفْسُ الْحُرُوفِ!). (<span class="highlight-green">تَدَافَعَ -> تَدَافُع</span>) ، (<span class="highlight-green">تَقَدَّمَ -> تَقَدُّم</span>) ، (<span class="highlight-green">تَعَاوَنَ -> تَعَاوُن</span>) .

=== BLOCK 4: تنبيه هام (Orange Benefit Box) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: لَيْسَ لِلْمَصَادِرِ السَّمَاعِيَّةِ (لِلْأَفْعَالِ الثُّلَاثِيَّةِ) قَاعِدَةٌ ثَابِتَةٌ، وَتُعْرَفُ بِالسَّمَاعِ عَنِ الْعَرَبِ وَالرُّجُوعِ لِلْمُعْجَمِ.

=== BLOCK 5: الجدول الشامل لأوزان المصادر القياسية ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: نَوْعُ الْفِعْلِ
[HEADER_2]: وَزْنُ الْفِعْلِ
[HEADER_3]: وَزْنُ الْمَصْدَرِ
[HEADER_4]: أَمْثِلَةٌ
[ROW_1_COL_1]: رُبَاعِيٌّ
[ROW_1_COL_2]: فَعَّلَ
[ROW_1_COL_3]: تَفْعِيل
[ROW_1_COL_4]: عَلَّمَ -> تَعْلِيم، نَظَّمَ -> تَنْظِيم، هَذَّبَ -> تَهْذِيب
[ROW_2_COL_1]: رُبَاعِيٌّ
[ROW_2_COL_2]: أَفْعَلَ
[ROW_2_COL_3]: إِفْعَال
[ROW_2_COL_4]: أَقْبَلَ -> إِقْبَال، أَكْرَمَ -> إِكْرَام، أَحْسَنَ -> إِحْسَان
[ROW_3_COL_1]: رُبَاعِيٌّ
[ROW_3_COL_2]: فَاعَلَ
[ROW_3_COL_3]: مُفَاعَلَة / فِعَال
[ROW_3_COL_4]: شَارَكَ -> مُشَارَكَة، قَاتَلَ -> مُقَاتَلَة / قِتَال
[ROW_4_COL_1]: رُبَاعِيٌّ
[ROW_4_COL_2]: فَعْلَلَ
[ROW_4_COL_3]: فَعْلَلَة / فِعْلَال
[ROW_4_COL_4]: زَلْزَلَ -> زَلْزَلَة / زِلْزَال، دَحْرَجَ -> دَحْرَجَة

=== BLOCK 6: المَصْدَرُ المِيمِيُّ وَالصِّنَاعِيُّ ===
(Component: TEMPLATE_C_SPLIT.html)
LeftSide:
(Component: TEMPLATE_C_BLOCK.html)
Title: المَصْدَرُ المِيمِيُّ وَالصِّنَاعِيُّ
Content:
<p class="text-accent"><span class="highlight-blue">المَصْدَرُ المِيمِيُّ:</span> مَصْدَرٌ يَبْدَأُ بِمِيمٍ زَائِدَةٍ، يُؤَدِّي نَفْسَ مَعْنَى الْمَصْدَرِ الْأَصْلِيِّ لَكِنَّهُ أَقْوَى بَلَاغِيّاً. يُصَاغُ عَلَى وَزْنِ (<span class="highlight-red">مَفْعَل/مَفْعِل</span>)، مِثْلَ اسْمِ الزَّمَانِ وَالْمَكَانِ، وَالسِّيَاقُ يُفَرِّقُ بَيْنَهَا.</p>
<p>مِثَالٌ: نَفَعَنِي النَّصِيحَةُ <span class="highlight-red">مَنْفَعَةً</span> عَظِيمَةً. (أَيْ نَفْعاً عَظِيماً، مَنْفَعَةً = مَصْدَرٌ مِيمِيٌّ).</p>
<p class="mt-4"><span class="text-accent"><span class="highlight-blue">المَصْدَرُ الصِّنَاعِيُّ:</span> اسْمٌ عَادِيٌّ صَنَعْنَا مِنْهُ مَصْدَراً بِإِضَافَةِ (<span class="highlight-red">يَّة</span>) مُشَدَّدَةٍ إِلَى آخِرِهِ (يَاءُ نِسْبَةٍ + تَاءٌ مَرْبُوطَةٌ).</span></p>
<p>مِثَالٌ: (<span class="highlight-blue">عِلْم</span> -> <span class="highlight-red">عِلْمِيَّة</span>)، (<span class="highlight-blue">وَطَن</span> -> <span class="highlight-red">وَطَنِيَّة</span>)، (<span class="highlight-blue">حُرّ</span> -> <span class="highlight-red">حُرِّيَّة</span>).</p>

RightSide:
(Component: TEMPLATE_C_BLOCK.html)
Title: المَصْدَرُ المُؤَوَّلُ
Content:
<p class="text-accent">هُوَ خِدْعَةٌ لُغَوِيَّةٌ: حَرْفٌ مَصْدَرِيٌّ (<span class="highlight-blue">أَنْ</span>) مَعَ فِعْلٍ (<span class="highlight-blue">يَفْعَلَ</span>)، يُسَاوِي مَصْدَراً صَرِيحاً وَاحِداً يُمْكِنُكَ أَنْ تَضَعَهُ مَكَانَهُمَا لِلتَّجْرِبَةِ.</p>
<p>أَمْثِلَةٌ:</p>
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: (<span class="highlight-blue">أَنْ</span>) + الفِعْلُ الْمُضَارِعُ: أُحِبُّ (<span class="highlight-red">أَنْ نَدْرُسَ</span>). الْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ نَصْبِ مَفْعُولٍ بِهِ. التَّقْدِيرُ الصَّرِيحُ: أُحِبُّ (<span class="highlight-green">الدِّرَاسَةَ</span>).
[LIST_ITEM_CONTENT]: (<span class="highlight-blue">أَنَّ</span>) + اسْمُهَا وَخَبَرُهَا: عَلِمْتُ (<span class="highlight-red">أَنَّكَ نَاجِحٌ</span>). التَّقْدِيرُ: عَلِمْتُ (<span class="highlight-green">نَجَاحَكَ</span>).

=== BLOCK 7: الإعراب ===
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: الْمَصْدَرُ الْمُؤَوَّلُ
[DETAILS_1]: فِي مَحَلِّ نَصْبِ مَفْعُولٍ بِهِ.
[WORD_2]: مَنْفَعَةً
[DETAILS_2]: مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ.

=== BLOCK 8: Exam Section ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: هَاتِ مَصْدَرَ الأَفْعَالِ الآتِيَةِ: (أَكْرَمَ، تَعَلَّمَ، اسْتَخْرَجَ).
Number: ٢
Question: اسْتَخْرِجِ الْمَصْدَرَ الْمُؤَوَّلَ وَحَوِّلْهُ لِصَرِيحٍ: "يُسْعِدُنِي أَنْ تَنْجَحَ".

--- END STREAM ---