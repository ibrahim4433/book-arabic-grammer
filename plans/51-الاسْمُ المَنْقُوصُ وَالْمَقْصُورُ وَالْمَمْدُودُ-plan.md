# **SESSION 51.0**

[TASK DEFINITION]
Objective: Implement الاسْمُ المَنْقُوصُ وَالْمَقْصُورُ وَالْمَمْدُودُ.
File: `pages/51.0_nXX_الاسْمُ المَنْقُوصُ وَالْمَقْصُورُ وَالْمَمْدُودُ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/51.1_nXX_الاسْمُ المَنْقُوصُ وَالْمَقْصُورُ وَالْمَمْدُودُ_تابع.html` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 51
[CHAPTER_TITLE]: الاسْمُ المَنْقُوصُ وَالْمَقْصُورُ وَالْمَمْدُودُ
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم الإملاء
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: الاسْمُ المَنْقُوصُ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الِاسْمُ الْمَنْقُوصُ (آخِرُهُ يَاءٌ)
Content: <span class="text-accent">هُوَ اسْمٌ مُعْرَبٌ، يَنْتَهِي بِيَاءٍ أَصْلِيَّةٍ مَسْبُوقَةٍ بِكَسْرَةٍ.</span>

(Component: TEMPLATE_C_CHIPS.html)
Chips: الْقَاضِي, الْمُحَامِي, الرَّاعِي, الْبَانِي, السَّاعِي

(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: سُمِّيَ مَنْقُوصاً لِأَنَّ حَرَكَةَ الرَّفْعِ وَالْجَرِّ تَنْقُصُ (تُقَدَّرُ) عَلَيْهِ، أَوْ لِأَنَّ يَاءَهُ تُحْذَفُ أَحْيَاناً (<span class="highlight-red">قَاضٍ</span>).

=== BLOCK 3: الاسْمُ المَقْصُورُ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الِاسْمُ الْمَقْصُورُ (آخِرُهُ أَلِفٌ)
Content: <span class="text-accent">هُوَ اسْمٌ مُعْرَبٌ، يَنْتَهِي بِأَلِفٍ أَصْلِيَّةٍ مَسْبُوقَةٍ بِفَتْحَةٍ (سَوَاءٌ كُتِبَتْ أَلِفاً مَمْدُودَةً "<span class="highlight-red">ا</span>" أَوْ مَقْصُورَةً "<span class="highlight-red">ى</span>").</span>

(Component: TEMPLATE_C_CHIPS.html)
Chips: الْفَتَى, الْهُدَى, الْعَصَا, الدُّنْيَا, الْمُسْتَشْفَى, مَبْنَى

(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: حَرَكَاتُهُ الثَّلَاثُ كُلُّهَا مُقَدَّرَةٌ (مَخْفِيَّةٌ) لِلتَّعَذُّرِ.

=== BLOCK 4: الاسْمُ المَمْدُودُ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الِاسْمُ الْمَمْدُودُ (آخِرُهُ أَلِفٌ وَهَمْزَةٌ)
Content: <span class="text-accent">هُوَ اسْمٌ مُعْرَبٌ آخِرُهُ هَمْزَةٌ بَعْدَ أَلِفٍ زَائِدَةٍ مَمْدُودَةٍ.</span>

(Component: TEMPLATE_C_CHIPS.html)
Chips: بِنَاء, سَمَاء, صَحْرَاء, عُظَمَاء, قُرَّاء

=== BLOCK 5: أحكام الاسم المنقوص التفصيلية ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَحْكَامُ الِاسْمِ الْمَنْقُوصِ التَّفْصِيلِيَّةُ

(Component: TEMPLATE_C_LIST.html)
- ١. حَذْفُ الياءِ: تُحْذَفُ يَاءُ الِاسْمِ الْمَنْقُوصِ وَيُنَوَّنُ بِالْكَسْرِ بَدَلَهَا إِذَا كَانَ: (<span class="highlight-blue">نَكِرَةً، غَيْرَ مُضَافٍ، فِي حَالَتَيِ الرَّفْعِ وَالْجَرِّ فَقَطْ</span>).
  - الرَّفْعُ: جَاءَ <span class="highlight-red">قَاضٍ</span>. (فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ الْمُقَدَّرَةِ عَلَى الْيَاءِ الْمَحْذُوفَةِ).
  - الْجَرُّ: مَرَرْتُ بِـ<span class="highlight-red">وَادٍ</span> عَمِيقٍ.
- ٢. بَقَاءُ الْيَاءِ: تَبْقَى فِي ثَلَاثِ حَالَاتٍ:
  - إِذَا كَانَ مُعَرَّفاً بِـ (ال): جَاءَ <span class="highlight-red">الْقَاضِي</span>.
  - إِذَا كَانَ مُضَافاً: جَاءَ <span class="highlight-red">قَاضِي</span> الْمَدِينَةِ.
  - إِذَا كَانَ مَنْصُوباً: رَأَيْتُ <span class="highlight-red">قَاضِياً</span> عَادِلًا. (تَظْهَرُ الْفَتْحَةُ لِخِفَّتِهَا).

=== BLOCK 6: أحكام الاسم المقصور التفصيلية ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَحْكَامُ الِاسْمِ الْمَقْصُورِ التَّفْصِيلِيَّةُ
Content: الْأَلِفُ لَا تَسْقُطُ كِتَابَةً أَبَداً، وَلَكِنَّهَا تَسْقُطُ (لَفْظاً وَنُطْقاً) فِي حَالَةٍ وَاحِدَةٍ: إِذَا نُوِّنَ الِاسْمُ (أَيْ لَمْ يَكُنْ فِيهِ "ال" وَلَا بَعْدَهُ مُضَافٌ إِلَيْهِ)، نَضَعُ فَتْحَتَيْنِ قَبْلَ الْأَلِفِ، وَتُحْذَفُ الْأَلِفُ فِي النُّطْقِ.

(Component: TEMPLATE_C_BENEFIT_TIP.html)
Content: أَمْثِلَةٌ: رَأَيْتُ <span class="highlight-red">فَتًى</span>. جَاءَ <span class="highlight-red">فَتًى</span>. مَرَرْتُ بِـ<span class="highlight-red">فَتًى</span>. (يُنْطَقُ: <span class="highlight-blue">فَتَنْ</span>).

(Component: TEMPLATE_C_BENEFIT.html)
Content: أَمَّا مَعَ (الـ) فَتُكْتَبُ وَتُنْطَقُ: رَأَيْتُ <span class="highlight-green">الْفَتَى</span>.

=== BLOCK 7: خلاصة الأسماء (The Core Matrix) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: خُلَاصَةُ الْأَسْمَاءِ الْمَنْقُوصَةِ وَالْمَقْصُورَةِ وَالْمَمْدُودَةِ

(Component: TEMPLATE_C_TABLE.html)
Columns: نَوْعُ الِاسْمِ | تَعْرِيفُهُ | أَمْثِلَةٌ | مُلَاحَظَاتٌ
Row 1: الْمَنْقُوصُ | آخِرُهُ يَاءٌ أَصْلِيَّةٌ قَبْلَهَا كَسْرَةٌ | الْقَاضِي، الرَّاعِي | تُقَدَّرُ حَرَكَةُ الرَّفْعِ وَالْجَرِّ وَتُحْذَفُ يَاؤُهُ أَحْيَانًا
Row 2: الْمَقْصُورُ | آخِرُهُ أَلِفٌ أَصْلِيَّةٌ قَبْلَهَا فَتْحَةٌ | الْفَتَى، الْعَصَا | حَرَكَاتُهُ الثَّلَاثُ مُقَدَّرَةٌ لِلتَّعَذُّرِ
Row 3: الْمَمْدُودُ | آخِرُهُ هَمْزَةٌ بَعْدَ أَلِفٍ زَائِدَةٍ | بِنَاء، سَمَاء | اسْمٌ مُعْرَبٌ تَظْهَرُ عَلَيْهِ الْحَرَكَاتُ

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: مَيِّزِ الِاسْمَ الْمَنْقُوصَ وَالْمَقْصُورَ وَالْمَمْدُودَ فِيمَا يَلِي: السَّاعِي، دُنْيَا، صَحْرَاء، مُسْتَشْفَى، بَانٍ، قُرَّاء، مَبْنَى.

(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: اشْرَحْ سَبَبَ حَذْفِ الْيَاءِ فِي كَلِمَةِ "قَاضٍ" فِي جُمْلَةِ: "جَاءَ قَاضٍ عَادِلٌ".

(Component: TEMPLATE_C_EXAM.html)
Number: ٣
Question: بَيِّنْ حَالَةَ الْأَلِفِ لَفْظاً وَكِتَابَةً فِي كَلِمَةِ "فَتًى" فِي جُمْلَةِ: "رَأَيْتُ فَتًى".

--- END STREAM ---
