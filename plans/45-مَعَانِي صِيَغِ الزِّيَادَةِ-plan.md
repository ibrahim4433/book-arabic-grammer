# **SESSION 45.0**

[TASK DEFINITION]
Objective: Implement مَعَانِي صِيَغِ الزِّيَادَةِ.
File: `pages/45.0_nXX_مَعَانِي صِيَغِ الزِّيَادَةِ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/45.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 45
[CHAPTER_TITLE]: مَعَانِي صِيَغِ الزِّيَادَةِ
[CATEGORY_HEADER]: المستوى المتوسط
[SECTION_HEADER]: علم الصرف
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Concept & Rule ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مَفْهُومُ الزِّيَادَةِ فِي الأَفْعَالِ
Content:
<div class="text-accent mb-4">
أَنَّ إِضَافَةَ حَرْفٍ جَدِيدٍ لِلْفِعْلِ، لَيْسَتْ عَبَثاً، بَلْ تُضِيفُ مَعْنًى جَدِيداً كُلِّيّاً لَمْ يَكُنْ مَوْجُوداً فِي الْفِعْلِ الثُّلَاثِيِّ.
</div>
مِثَالٌ: <span class="highlight-blue">فَهِمَ</span> (فِعْلٌ عَادِيٌّ)، أَمَّا <span class="highlight-red">اسْتَفْهَمَ</span> (فِيهَا أَلِفٌ وَسِينٌ وَتَاءٌ) تَعْنِي <span class="font-bold">"طَلَبَ الْفَهْمَ"</span>.

=== BLOCK 3: Benefit Tip ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Title: قَاعِدَةٌ بَلَاغِيَّةٌ مَشْهُورَةٌ
Content: (كُلَّمَا زَادَ المَبْنَى، زَادَ المَعْنَى).

=== BLOCK 4: Summary Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Title: أَهَمُّ المَعَانِي المُسْتَفَادَةِ مِنْ صِيَغِ الزِّيَادَةِ
Headers:
- الصِّيغَةُ (الْوَزْنُ)
- المَعَانِي الَّتِي تُفِيدُهَا
- أَمْثِلَةٌ تَطْبِيقِيَّةٌ
Rows:
- Row 1: <span class="font-bold text-primary">أَفْعَلَ</span> | التَّعْدِيَةُ (جَعْلُ الْفَاعِلِ مَفْعُولاً بِهِ)، الدُّخُولُ فِي الزَّمَانِ، التَّحَوُّلُ | <span class="highlight-red">أَجْلَسْتُ</span> الطِّفْلَ (أَنَا جَعَلْتُهُ يَجْلِسُ)، <span class="highlight-blue">أَصْبَحْنَا</span> (دَخَلْنَا فِي الصَّبَاحِ).
- Row 2: <span class="font-bold text-primary">فَعَّلَ (بِالشَّدَّةِ)</span> | التَّكْثِيرُ (الْمُبَالَغَةُ فِي الْفِعْلِ)، التَّعْدِيَةُ | <span class="highlight-red">كَسَّرَ</span> الزُّجَاجَ (أَيْ حَطَّمَهُ قِطَعاً كَثِيرَةً جِدّاً بَدَلَ كَسَرَهُ مَرَّةً). <span class="highlight-blue">غَلَّقَ</span> النَّوَافِذَ.
- Row 3: <span class="font-bold text-primary">فَاعَلَ</span> | المُشَارَكَةُ بَيْنَ اثْنَيْنِ | <span class="highlight-red">قَاتَلَ</span> الْجُنْدِيُّ عَدُوَّهُ (كِلَاهُمَا يُقَاتِلُ الآخَرَ). <span class="highlight-blue">شَارَكَ</span>، جَادَلَ.
- Row 4: <span class="font-bold text-primary">تَفَاعَلَ</span> | المُشَارَكَةُ بَيْنَ جَمَاعَةٍ، أَوْ التَّظَاهُرُ (ادِّعَاءُ الشَّيْءِ وَالْكَذِبُ بِهِ) | <span class="highlight-red">تَعَاوَنَ</span> القَوْمُ (مُشَارَكَةٌ). <span class="highlight-blue">تَمَارَضَ</span> الْوَلَدُ لِيَغِيبَ (تَظَاهَرَ بِالْمَرَضِ). تَغَافَلَ.
- Row 5: <span class="font-bold text-primary">تَفَعَّلَ</span> | التَّكَلُّفُ (بَذْلُ الْجُهْدِ)، التَّدَرُّجُ (شَيْئاً فَشَيْئاً) | <span class="highlight-red">تَشَجَّعَ</span> الرَّجُلُ (تَكَلَّفَ الشَّجَاعَةَ)، <span class="highlight-blue">تَجَرَّعَ</span> الدَّوَاءَ (شَرِبَهُ قَطْرَةً قَطْرَةً تَدَرُّجاً).
- Row 6: <span class="font-bold text-primary">افْتَعَلَ</span> | المُطَاوَعَةُ، الِاتِّخَاذُ | <span class="highlight-red">اقْتَرَبَ</span>، <span class="highlight-blue">اخْتَصَمَ</span> الخَصْمَانِ. جَمَعْتُهُ فَاجْتَمَعَ.
- Row 7: <span class="font-bold text-primary">انْفَعَلَ</span> | المُطَاوَعَةُ التَّامَّةُ (قَبُولُ أَثَرِ الْفِعْلِ دُونَ رَفْضٍ) | كَسَرْتُهُ <span class="highlight-red">فَانْكَسَرَ</span> الزُّجَاجُ. فَتَحْتُهُ <span class="highlight-blue">فَانْفَتَحَ</span> البَابُ.
- Row 8: <span class="font-bold text-primary">اسْتَفْعَلَ</span> | الطَّلَبُ وَالسُّؤَالُ (أَشْهَرُ شَيْءٍ!)، أَوْ التَّحَوُّلُ | <span class="highlight-red">اسْتَفْهَمَ</span> الدَّرْسَ (طَلَبَ الْفَهْمَ). <span class="highlight-blue">اسْتَحْجَرَ</span> الطِّينُ (تَحَوَّلَ الطِّينُ إِلَى حَجَرٍ قَاسٍ).
- Row 9: <span class="font-bold text-primary">افْعَلَّ</span> | المُبَالَغَةُ فِي الْأَلْوَانِ وَالْعُيُوبِ الجَسَدِيَّةِ | <span class="highlight-red">احْمَرَّ</span> الوَجْهُ (اشْتَدَّ حُمْرَةً). <span class="highlight-blue">اخْضَرَّ</span> الزَّرْعُ. اعْوَرَّ الْعَيْنُ.

=== BLOCK 5: Deep Dive 1 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَفْصِيلُ أَهَمِّ الصِّيَغِ (الجُزْءُ الأَوَّلُ)
Content:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: <span class="font-bold text-primary">أَفْعَلَ:</span> تُفِيدُ التَّعْدِيَةَ (جَعْلُ الْفَاعِلِ مَفْعُولاً بِهِ)، الدُّخُولُ فِي الزَّمَانِ، التَّحَوُّلُ. مِثَالٌ: <span class="highlight-red">أَجْلَسْتُ</span> الطِّفْلَ (أَنَا جَعَلْتُهُ يَجْلِسُ)، <span class="highlight-blue">أَصْبَحْنَا</span> (دَخَلْنَا فِي الصَّبَاحِ).
[LIST_ITEM_CONTENT]: <span class="font-bold text-primary">فَعَّلَ (بِالشَّدَّةِ):</span> تُفِيدُ التَّكْثِيرَ (الْمُبَالَغَةُ فِي الْفِعْلِ)، التَّعْدِيَةُ. مِثَالٌ: <span class="highlight-red">كَسَّرَ</span> الزُّجَاجَ (أَيْ حَطَّمَهُ قِطَعاً كَثِيرَةً جِدّاً بَدَلَ كَسَرَهُ مَرَّةً). <span class="highlight-blue">غَلَّقَ</span> النَّوَافِذَ.
[LIST_ITEM_CONTENT]: <span class="font-bold text-primary">فَاعَلَ:</span> تُفِيدُ المُشَارَكَةَ بَيْنَ اثْنَيْنِ. مِثَالٌ: <span class="highlight-red">قَاتَلَ</span> الْجُنْدِيُّ عَدُوَّهُ (كِلَاهُمَا يُقَاتِلُ الآخَرَ). <span class="highlight-blue">شَارَكَ</span>، جَادَلَ.

=== BLOCK 6: Deep Dive 2 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَفْصِيلُ أَهَمِّ الصِّيَغِ (الجُزْءُ الثَّانِي)
Content:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: <span class="font-bold text-primary">تَفَاعَلَ:</span> تُفِيدُ المُشَارَكَةَ بَيْنَ جَمَاعَةٍ، أَوْ التَّظَاهُرَ (ادِّعَاءُ الشَّيْءِ وَالْكَذِبُ بِهِ). مِثَالٌ: <span class="highlight-red">تَعَاوَنَ</span> القَوْمُ (مُشَارَكَةٌ). <span class="highlight-blue">تَمَارَضَ</span> الْوَلَدُ لِيَغِيبَ (تَظَاهَرَ بِالْمَرَضِ). تَغَافَلَ.
[LIST_ITEM_CONTENT]: <span class="font-bold text-primary">تَفَعَّلَ:</span> تُفِيدُ التَّكَلُّفَ (بَذْلُ الْجُهْدِ)، التَّدَرُّجَ (شَيْئاً فَشَيْئاً). مِثَالٌ: <span class="highlight-red">تَشَجَّعَ</span> الرَّجُلُ (تَكَلَّفَ الشَّجَاعَةَ)، <span class="highlight-blue">تَجَرَّعَ</span> الدَّوَاءَ (شَرِبَهُ قَطْرَةً قَطْرَةً تَدَرُّجاً).
[LIST_ITEM_CONTENT]: <span class="font-bold text-primary">افْتَعَلَ:</span> تُفِيدُ المُطَاوَعَةَ، الِاتِّخَاذَ. مِثَالٌ: <span class="highlight-red">اقْتَرَبَ</span>، <span class="highlight-blue">اخْتَصَمَ</span> الخَصْمَانِ. جَمَعْتُهُ <span class="highlight-green">فَاجْتَمَعَ</span>.

=== BLOCK 7: Deep Dive 3 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَفْصِيلُ أَهَمِّ الصِّيَغِ (الجُزْءُ الثَّالِثُ)
Content:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: <span class="font-bold text-primary">انْفَعَلَ:</span> تُفِيدُ المُطَاوَعَةَ التَّامَّةَ (قَبُولُ أَثَرِ الْفِعْلِ دُونَ رَفْضٍ). مِثَالٌ: كَسَرْتُهُ <span class="highlight-red">فَانْكَسَرَ</span> الزُّجَاجُ. فَتَحْتُهُ <span class="highlight-blue">فَانْفَتَحَ</span> البَابُ.
[LIST_ITEM_CONTENT]: <span class="font-bold text-primary">اسْتَفْعَلَ:</span> تُفِيدُ الطَّلَبَ وَالسُّؤَالَ (أَشْهَرُ شَيْءٍ!)، أَوْ التَّحَوُّلَ. مِثَالٌ: <span class="highlight-red">اسْتَفْهَمَ</span> الدَّرْسَ (طَلَبَ الْفَهْمَ). <span class="highlight-blue">اسْتَحْجَرَ</span> الطِّينُ (تَحَوَّلَ الطِّينُ إِلَى حَجَرٍ قَاسٍ).
[LIST_ITEM_CONTENT]: <span class="font-bold text-primary">افْعَلَّ:</span> تُفِيدُ المُبَالَغَةَ فِي الْأَلْوَانِ وَالْعُيُوبِ الجَسَدِيَّةِ. مِثَالٌ: <span class="highlight-red">احْمَرَّ</span> الوَجْهُ (اشْتَدَّ حُمْرَةً). <span class="highlight-blue">اخْضَرَّ</span> الزَّرْعُ. <span class="highlight-green">اعْوَرَّ</span> الْعَيْنُ.

=== BLOCK 8: Exam Section ===
(Component: TEMPLATE_C_BLOCK.html)
Title:  اخْتَبِرْ نَفْسَكَ (معاني صيغ الزيادة)
Content:
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: اسْتَخْرِجِ الفِعْلَ المَزِيدَ وَبَيِّنْ مَعْنَى الزِّيَادَةِ فِي الجُمْلَةِ: "اسْتَفْهَمَ الطَّالِبُ مُعَلِّمَهُ".
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: صُغْ فِعْلاً عَلَى وَزْنِ (تَفَاعَلَ) مِنَ الفِعْلِ (غَفَلَ) وَبَيِّنْ مَعْنَاهُ.

--- END STREAM ---