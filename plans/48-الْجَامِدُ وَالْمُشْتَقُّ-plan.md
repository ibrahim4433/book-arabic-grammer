# **SESSION 48.0**

[TASK DEFINITION]
Objective: Implement الْجَامِدُ وَالْمُشْتَقُّ.
File: `pages/48.0_nXX_الْجَامِدُ وَالْمُشْتَقُّ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/48.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 48
[CHAPTER_TITLE]: الْجَامِدُ وَالْمُشْتَقُّ
[CATEGORY_HEADER]: المستوى المتوسط
[SECTION_HEADER]: علم الصرف
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: تَعْرِيفُ الْجَامِدِ وَالْمُشْتَقِّ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَعْرِيفُ الْجَامِدِ وَالْمُشْتَقِّ
Content:
<p class="text-accent mb-4">تَنْقَسِمُ الْأَسْمَاءُ فِي اللُّغَةِ الْعَرَبِيَّةِ إِلَى قِسْمَيْنِ مِنْ حَيْثُ الْأَصْلِ:</p>
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]:
<span class="font-bold">١. الِاسْمُ الْجَامِدُ:</span> هُوَ الِاسْمُ الَّذِي وُلِدَ هَكَذَا، لَا يُؤْخَذُ مِنْ كَلِمَةٍ أُخْرَى قَبْلَهُ. (كَـ <span class="highlight-red">الْحَجَرِ</span> الْجَامِدِ).
[LIST_ITEM_CONTENT]:
<span class="font-bold">٢. الِاسْمُ الْمُشْتَقُّ:</span> فَهُوَ الِاسْمُ الَّذِي يُؤْخَذُ (يُشْتَقُّ) مِنْ فِعْلٍ، وَيَحْمِلُ مَعْنَاهُ وَأَحْرُفَهُ الْأَصْلِيَّةَ.

=== BLOCK 3: أَنْوَاعُ الِاسْمِ الْجَامِدِ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَنْوَاعُ الِاسْمِ الْجَامِدِ
Content:
(Component: TEMPLATE_C_SPLIT.html)
LeftSide:
(Component: TEMPLATE_C_BLOCK.html)
Title: ١- الْجَامِدُ الذَّاتِ (الْمَحْسُوسُ)
Content:
<p class="text-accent mb-4">هُوَ الِاسْمُ الَّذِي يُدْرَكُ بِالْحَوَاسِّ الْخَمْسِ وَيُمْكِنُ رُؤْيَتُهُ أَوْ لَمْسُهُ.</p>
<p>أَمْثِلَةٌ: (<span class="highlight-blue">شَجَرَة</span>، <span class="highlight-blue">كُرْسِيّ</span>، <span class="highlight-blue">قَلَم</span>، <span class="highlight-blue">رَجُل</span>، <span class="highlight-blue">شَمْس</span>).</p>
RightSide:
(Component: TEMPLATE_C_BLOCK.html)
Title: ٢- الْجَامِدُ الْمَعْنَى (الْمُجَرَّدُ/الْمَصْدَرُ)
Content:
<p class="text-accent mb-4">يُدْرَكُ بِالْعَقْلِ فَقَطْ وَلَا جِسْمَ لَهُ.</p>
<p>أَمْثِلَةٌ: (<span class="highlight-green">الْعِلْم</span>، <span class="highlight-green">الشَّجَاعَة</span>، <span class="highlight-green">الْجَهْل</span>، <span class="highlight-green">الرَّغْبَة</span>).</p>

=== BLOCK 4: مُلَخَّصُ الْأَسْمَاءِ الْمُشْتَقَّةِ ===
(Component: TEMPLATE_C_TABLE.html)
Title: مُعْظَمُهَا مَأْخُوذٌ مِنَ الْأَفْعَالِ - سَبْعَةُ أَنْوَاعٍ
Headers: النَّوْعُ | الدَّلَالَةُ | مِثَالٌ
Rows:
١. اسْمُ الْفَاعِلِ | يَدُلُّ عَلَى مَنْ قَامَ بِالْفِعْلِ | كَاتِب، مُكْرِم
٢. اسْمُ الْمَفْعُولِ | يَدُلُّ عَلَى مَنْ وَقَعَ عَلَيْهِ الْفِعْلُ | مَكْتُوب، مُكْرَم
٣. مُبَالَغَةُ اسْمِ الْفَاعِلِ | اسْمُ فَاعِلٍ قَامَ بِالْفِعْلِ بِكَثْرَةٍ | كَذَّاب، صَبُور
٤. الصِّفَةُ الْمُشَبَّهَةُ | صِفَةٌ ثَابِتَةٌ كَالْأَلْوَانِ وَالطِّبَاعِ | شُجَاع، عَطْشَان
٥. اسْمُ الْآلَةِ | يَدُلُّ عَلَى الْأَدَاةِ | مِفْتَاح، ثَلَّاجَة
٦. اسْمُ الزَّمَانِ وَالْمَكَانِ | مَكَانِ أَوْ زَمَانِ حُدُوثِ الْفِعْلِ | مَلْعَب، مَوْقِف
٧. اسْمُ التَّفْضِيلِ | لِلْمُقَارَنَةِ بَيْنَ شَيْئَيْنِ | أَكْبَر، فُضْلَى

=== BLOCK 5: تَفْصِيلُ الْأَسْمَاءِ الْمُشْتَقَّةِ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ١. اسْمُ الْفَاعِلِ
Content:
<p class="text-accent mb-4">يَدُلُّ عَلَى مَنْ قَامَ بِالْفِعْلِ.</p>
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]:
مِنْ الثُّلَاثِيِّ: عَلَى وَزْنِ (فَاعِل): كَتَبَ -> <span class="highlight-red">كَاتِب</span>، ضَرَبَ -> <span class="highlight-red">ضَارِب</span>، سَأَلَ -> <span class="highlight-red">سَائِل</span>.
[LIST_ITEM_CONTENT]:
مِنْ غَيْرِ الثُّلَاثِيِّ (مِيمٌ مَضْمُومَةٌ وَكَسْرُ مَا قَبْلَ الْآخِرِ): أَكْرَمَ -> <span class="highlight-blue">مُكْرِم</span>، انْتَصَرَ -> <span class="highlight-blue">مُنْتَصِر</span>، اسْتَخْرَجَ -> <span class="highlight-blue">مُسْتَخْرِج</span>.

=== BLOCK 6: تَفْصِيلُ الْأَسْمَاءِ الْمُشْتَقَّةِ (يُتْبَعُ) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٢. اسْمُ الْمَفْعُولِ
Content:
<p class="text-accent mb-4">يَدُلُّ عَلَى مَنْ وَقَعَ عَلَيْهِ الْفِعْلُ.</p>
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]:
مِنْ الثُّلَاثِيِّ: عَلَى وَزْنِ (مَفْعُول): كَتَبَ -> <span class="highlight-red">مَكْتُوب</span>، شَرِبَ -> <span class="highlight-red">مَشْرُوب</span>.
[LIST_ITEM_CONTENT]:
مِنْ غَيْرِ الثُّلَاثِيِّ (مِيمٌ مَضْمُومَةٌ وَفَتْحُ مَا قَبْلَ الْآخِرِ): أُكْرِمَ -> <span class="highlight-blue">مُكْرَم</span>، اُسْتُخْرِجَ -> <span class="highlight-blue">مُسْتَخْرَج</span>.

=== BLOCK 7: تَفْصِيلُ الْأَسْمَاءِ الْمُشْتَقَّةِ (يُتْبَعُ) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٣. مُبَالَغَةُ اسْمِ الْفَاعِلِ
Content:
<p class="text-accent mb-4">اسْمُ فَاعِلٍ قَامَ بِالْفِعْلِ بِكَثْرَةٍ وَمُبَالَغَةٍ. لَهَا أَوْزَانٌ مَشْهُورَةٌ:</p>
(Component: TEMPLATE_C_CHIPS.html)
<span class="highlight-red">فَعَّال (جَلَّاد، خَبَّاز، كَذَّاب)</span>
<span class="highlight-blue">فَعَّالَة (عَلَّامَة، فَهَّامَة)</span>
<span class="highlight-green">مِفْعَال (مِعْطَاء، مِقْدَام)</span>
<span class="highlight-red">فَعُول (أَكُول، صَبُور)</span>
<span class="highlight-blue">فَعِيل (فَهِيم، خَبِير)</span>

=== BLOCK 8: تَفْصِيلُ الْأَسْمَاءِ الْمُشْتَقَّةِ (يُتْبَعُ) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٤. الصِّفَةُ الْمُشَبَّهَةُ بِاسْمِ الْفَاعِلِ
Content:
<p class="text-accent mb-4">صِفَةٌ ثَابِتَةٌ فِي الْمَوْصُوفِ كَالْأَلْوَانِ وَالطِّبَاعِ.</p>
<p>أَوْزَانُهَا:</p>
(Component: TEMPLATE_C_CHIPS.html)
<span class="highlight-red">فَعِيل (كَريم)</span>
<span class="highlight-blue">فُعَال (شُجَاع)</span>
<span class="highlight-green">فَعَال (جَبَان)</span>
<span class="highlight-red">فَعَل (بَطَل)</span>
<span class="highlight-blue">فَعْلَان (عَطْشَان)</span>
<span class="highlight-green">أَفْعَل (أَحْمَر، أَعْرَج)</span>

=== BLOCK 9: تَفْصِيلُ الْأَسْمَاءِ الْمُشْتَقَّةِ (يُتْبَعُ) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٥. اسْمُ الْآلَةِ
Content:
<p class="text-accent mb-4">يَدُلُّ عَلَى الْأَدَاةِ الَّتِي حَدَثَ بِهَا الْفِعْلِ.</p>
(Component: TEMPLATE_C_CHIPS.html)
<span class="highlight-red">مِفْعَل (مِثْقَب، مِبْرَد)</span>
<span class="highlight-blue">مِفْعَال (مِصْبَاح، مِفْتَاح)</span>
<span class="highlight-green">مِفْعَلَة (مِرْوَحَة، مِكْنَسَة)</span>
<span class="highlight-red">فَعَّالَة (غَسَّالَة، ثَلَّاجَة)</span>

=== BLOCK 10: تَفْصِيلُ الْأَسْمَاءِ الْمُشْتَقَّةِ (يُتْبَعُ) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٦. اسْمُ الزَّمَانِ وَاسْمُ الْمَكَانِ
Content:
<p class="text-accent mb-4">يَدُلُّ عَلَى مَكَانِ أَوْ زَمَانِ حُدُوثِ الْفِعْلِ (وَيَكُونُ مَبْدُوءاً بِمِيمٍ).</p>
<p>عَلَى وَزْنِ (مَفْعَل) أَوْ (مَفْعِل): <span class="highlight-red">مَلْعَب</span>، <span class="highlight-blue">مَكْتَب</span>، <span class="highlight-green">مَصْنَع</span>، <span class="highlight-red">مَوْقِف</span>، <span class="highlight-blue">مَخْرَج</span>.</p>

=== BLOCK 11: تَفْصِيلُ الْأَسْمَاءِ الْمُشْتَقَّةِ (يُتْبَعُ) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٧. اسْمُ التَّفْضِيلِ
Content:
<p class="text-accent mb-4">لِلْمُقَارَنَةِ بَيْنَ شَيْئَيْنِ، يُصَاغُ عَلَى وَزْنِ (أَفْعَل) لِلْمُذَكَّرِ وَ (فُعْلَى) لِلْمُؤَنَّثِ.</p>
<p>أَمْثِلَةٌ: <span class="highlight-red">أَكْبَر كُبْرَى</span>، <span class="highlight-blue">أَفْضَل فُضْلَى</span>، <span class="highlight-green">أَحْسَن حُسْنَى</span>.</p>

=== BLOCK 12: مُلَاحَظَةٌ هَامَّةٌ ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content:
الْأَسْمَاءُ الْمُشْتَقَّةُ مُعْظَمُهَا مَأْخُوذٌ مِنَ الْأَفْعَالِ.

=== BLOCK 13:  اخْتَبِرْ نَفْسَكَ (الْجَامِدُ وَالْمُشْتَقُّ) ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: صَنِّفْ: (رَجُل، رَغْبَة، قَوِيّ).

=== BLOCK 14:  اخْتَبِرْ نَفْسَكَ (الْجَامِدُ وَالْمُشْتَقُّ) ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: صُغِ اسْمَ الْفَاعِلِ وَاسْمَ الْمَفْعُولِ وَاسْمَ الْمَكَانِ مِنَ الْفِعْلِ (اِنْطَلَقَ).

--- END STREAM ---