# **SESSION 68.0**

[TASK DEFINITION]
Objective: Implement وَظَائِفُ الْجُمَلِ الِاسْمِيَّةِ وَالْفِعْلِيَّةِ (الْمُسْتَوَى التَّرْكِيبِيُّ).
File: `pages/68.0_nXX_وَظَائِفُ الْجُمَلِ الِاسْمِيَّةِ وَالْفِعْلِيَّةِ (الْمُسْتَوَى التَّرْكِيبِيُّ).html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/68.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 68
[CHAPTER_TITLE]: وَظَائِفُ الْجُمَلِ الِاسْمِيَّةِ وَالْفِعْلِيَّةِ (الْمُسْتَوَى التَّرْكِيبِيُّ)
[CATEGORY_HEADER]: المستوى المتقدم
[SECTION_HEADER]: علم البلاغة
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: وَظِيفَةُ الْجُمْلَةِ الْاسْمِيَّةِ (الثَّبَاتُ وَالسُّكُونُ) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: وَظِيفَةُ الْجُمْلَةِ الْاسْمِيَّةِ (الثَّبَاتُ وَالسُّكُونُ)
Content:
<p class="text-accent mb-2mm">الْجُمْلَةُ الْاسْمِيَّةُ (الْمُبْتَدَأُ وَالْخَبَرُ) تُعْطِي الْمُسْتَمِعَ إِحْسَاسًا بِـ (<span class="highlight-red font-bold">الثَّبَاتِ وَالِاسْتِقْرَارِ وَالدَّيْمُومَةِ</span>)، لِأَنَّهَا لَا تَرْتَبِطُ بِزَمَنٍ يَنْتَهِي، بَلْ تَصِفُ حَالَةً ثَابِتَةً لَا تَتَغَيَّرُ.</p>
<p class="mb-2mm">مِثَالٌ: "<span class="highlight-blue font-bold">الْأَرْضُ مُسْتَدِيرَةٌ</span>". (حَقِيقَةٌ ثَابِتَةٌ كَانَتْ وَسَتَبْقَى دَائِماً).</p>

=== BLOCK 3: أَثَرُ الْجُمْلَةِ الْاسْمِيَّةِ فِي الشِّعْرِ ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Title: أَثَرُهَا فِي الشِّعْرِ
Content: إِذَا كَانَ الشَّاعِرُ يُحِبُّ وَطَنَهُ بِشِدَّةٍ، يَسْتَخْدِمُ جُمْلَةً اسْمِيَّةً لِيُؤَكِّدَ أَنَّ حُبَّهُ ثَابِتٌ لَا يَتَغَيَّرُ مَعَ الْأَيَّامِ (<span class="highlight-green font-bold">أَنَا مُحِبٌّ لَكَ يَا وَطَنِي</span>).

=== BLOCK 4: وَظِيفَةُ الْجُمْلَةِ الْفِعْلِيَّةِ (الْحَرَكَةُ وَالتَّجَدُّدُ) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: وَظِيفَةُ الْجُمْلَةِ الْفِعْلِيَّةِ (الْحَرَكَةُ وَالتَّجَدُّدُ)
Content:
<p class="text-accent mb-2mm">الْجُمْلَةُ الْفِعْلِيَّةُ مُرْتَبِطَةٌ دَائِماً بِزَمَنٍ (مَاضٍ انْتَهَى، أَوْ مُضَارِعٍ يَسْتَمِرُّ)، لِذَلِكَ تَدُلُّ عَلَى (<span class="highlight-red font-bold">التَّغَيُّرِ وَالْحَرَكَةِ وَالْحَيَوِيَّةِ وَالتَّجَدُّدِ</span>).</p>
<p class="mb-2mm">مِثَالٌ: "<span class="highlight-blue font-bold">يَرْكُضُ اللِّصُّ</span>". (فِيهَا حَرَكَةٌ، وَحَدَثٌ قَدْ يَتَوَقَّفُ أَوْ يَتَجَدَّدُ).</p>

=== BLOCK 5: أَثَرُ الْجُمْلَةِ الْفِعْلِيَّةِ فِي الشِّعْرِ ===
(Component: TEMPLATE_C_BENEFIT.html)
Title: أَثَرُهَا فِي الشِّعْرِ
Content: يَسْتَخْدِمُهَا الشَّاعِرُ لِسَرْدِ الْقِصَصِ وَالْمَعَارِكِ وَنَقْلِ الْمُشَاهِدِ الْحَرَكِيَّةِ لِيَجْعَلَ الْمُسْتَمِعَ يَعِيشُ الْحَدَثَ (<span class="highlight-green font-bold">انْطَلَقْنَا، ثُرْنَا، مَحَوْنَا</span>).

=== BLOCK 6: مُقَارَنَةٌ سَرِيعَةٌ ===
(Component: TEMPLATE_C_TABLE.html)
Title: مُقَارَنَةٌ سَرِيعَةٌ
Content:
<table class="dense-table text-center">
  <thead>
    <tr>
      <th>نَوْعُ الْجُمْلَةِ</th>
      <th>الْمِثَالُ</th>
      <th>الدَّلَالَةُ وَالْأَثَرُ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>الاسْمِيَّةُ</td>
      <td>(الْعِلْمُ نُورٌ)</td>
      <td>ثَبَاتٌ وَاسْتِقْرَارٌ صِفَةٌ لَازِمَةٌ لَا تَتَبَدَّلُ.</td>
    </tr>
    <tr>
      <td>الْفِعْلِيَّةُ (الْمَاضِي)</td>
      <td>(حَقَّقْنَا النَّصْرَ)</td>
      <td>حَرَكَةٌ وَسَرْدٌ لِحَدَثٍ وَقَعَ فِي الْمَاضِي وَثَبَتَ انْتِهَاؤُهُ.</td>
    </tr>
    <tr>
      <td>الْفِعْلِيَّةُ (الْمُضَارِعِ)</td>
      <td>(نَبْنِي الْمَجْدَ)</td>
      <td>حَرَكَةٌ وَتَجَدُّدٌ مُسْتَمِرٌّ لِحَدَثٍ يَقَعُ الْآنَ وَيَسْتَمِرُّ فِي الْمُسْتَقْبَلِ.</td>
    </tr>
  </tbody>
</table>

=== BLOCK 7: Exam Question 1 ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: حَدِّدْ نَوْعَ الْجُمْلَةِ فِيمَا يَأْتِي وَبَيِّنْ دَلَالَتَهَا عَلَى الثَّبَاتِ أَوْ التَّجَدُّدِ: "الشَّمْسُ مُشْرِقَةٌ".

=== BLOCK 8: Exam Question 2 ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: حَدِّدْ نَوْعَ الْجُمْلَةِ فِيمَا يَأْتِي وَبَيِّنْ دَلَالَتَهَا عَلَى الثَّبَاتِ أَوْ التَّجَدُّدِ: "يَسْقُطُ الْمَطَرُ بِغَزَارَةٍ".

--- END STREAM ---