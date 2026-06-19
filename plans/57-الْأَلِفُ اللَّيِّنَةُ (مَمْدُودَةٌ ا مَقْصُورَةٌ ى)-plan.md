# **SESSION 57.0**

[TASK DEFINITION]
Objective: Implement الْأَلِفُ اللَّيِّنَةُ (مَمْدُودَةٌ ا مَقْصُورَةٌ ى).
File: `pages/57.0_nXX_الْأَلِفُ اللَّيِّنَةُ (مَمْدُودَةٌ ا مَقْصُورَةٌ ى).html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/57.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 57
[CHAPTER_TITLE]: الْأَلِفُ اللَّيِّنَةُ (مَمْدُودَةٌ ا مَقْصُورَةٌ ى)
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم الإملاء
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition & Rule ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَعْرِيفُ الأَلِفِ اللَّيِّنَةِ
Content: <p class="text-accent">هِيَ <span class="highlight-red">أَلِفُ مَدٍّ سَاكِنَةٌ مَفْتُوحٌ مَا قَبْلَهَا</span> (ا / ى). لَا تَقْبَلُ الْحَرَكَاتِ، وَتُكْتَبُ فِي آخِرِ الْكَلِمَاتِ، وَيَجِبُ التَّمْيِيزُ مَتَى نَكْتُبُهَا طَوِيلَةً (<span class="highlight-blue">مَمْدُودَةً ا</span>) وَمَتَى نَكْتُبُهَا بِلَا نُقَطٍ (<span class="highlight-blue">مَقْصُورَةً ى</span>).</p>

=== BLOCK 3: The Core Matrix ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مُلَخَّصُ قَوَاعِدِ رَسْمِ الأَلِفِ اللَّيِّنَةِ
Content:
(Component: TEMPLATE_C_TABLE.html)
Headers: [نَوْعُ الْكَلِمَةِ, الْقَاعِدَةُ, رَسْمُ الْأَلِفِ, أَمْثِلَةٌ]
Row 1: [الثُّلَاثِيَّةُ, أَصْلُهَا وَاوٌ, مَمْدُودَةٌ (ا), دَنَا - سَمَا - غَزَا - عَصَا]
Row 2: [الثُّلَاثِيَّةُ, أَصْلُهَا يَاءٌ, مَقْصُورَةٌ (ى), رَمَى - مَشَى - بَكَى - فَتَى]
Row 3: [فَوْقَ الثُّلَاثِيَّةِ, قَبْلَهَا يَاءٌ, مَمْدُودَةٌ (ا), دُنْيَا - هَدَايَا - مَرَايَا]
Row 4: [فَوْقَ الثُّلَاثِيَّةِ, قَبْلَهَا غَيْرُ الْيَاءِ, مَقْصُورَةٌ (ى), مُلْتَقَى - مُسْتَشْفَى - اعْتَدَى]

=== BLOCK 4: Deep Dive - Three-Letter Words ===
(Component: TEMPLATE_C_SPLIT.html)
LeftSide:
  (Component: TEMPLATE_C_BLOCK.html)
  Title: الثُّلَاثِيَّةُ (أَصْلُهَا وَاوٌ)
  Content: <p>الْقَاعِدَةُ: نَبْحَثُ عَنْ أَصْلِ الْأَلِفِ فِي الْمُضَارِعِ أَوْ الْمُثَنَّى أَوْ الْمَصْدَرِ. إِذَا كَانَ أَصْلُهَا (<span class="highlight-blue">وَاواً</span>): تُكْتَبُ <span class="highlight-red">مَمْدُودَةً (ا)</span>.</p>
  (Component: TEMPLATE_C_LIST.html)
  Items:
  - دَنَا (يَدْنُو)، سَمَا (يَسْمُو)، غَزَا (يَغْزُو).
  - عَصَا (الْعَصَوَانِ)، خُطَا (مُفْرَدُهَا خُطْوَةٌ)، ذُرَا (ذُرْوَةٌ).
RightSide:
  (Component: TEMPLATE_C_BLOCK.html)
  Title: الثُّلَاثِيَّةُ (أَصْلُهَا يَاءٌ)
  Content: <p>إِذَا كَانَ أَصْلُهَا (<span class="highlight-blue">يَاءً</span>): تُكْتَبُ <span class="highlight-red">مَقْصُورَةً (ى)</span>.</p>
  (Component: TEMPLATE_C_LIST.html)
  Items:
  - رَمَى (يَرْمِي)، مَشَى (يَمْشِي)، بَكَى (يَبْكِي)، هَدَى (يَهْدِي).
  - فَتَى (الْفَتَيَانِ)، هُدًى (الْهِدَايَةُ)، قُرًى (مُفْرَدُهَا قَرْيَةٌ).

=== BLOCK 5: Deep Dive - Four-Letter Words and Above ===
(Component: TEMPLATE_C_SPLIT.html)
LeftSide:
  (Component: TEMPLATE_C_BLOCK.html)
  Title: فَوْقَ الثُّلَاثِيَّةِ (قَبْلَهَا يَاءٌ)
  Content: <p>الْقَاعِدَةُ: لَا نَبْحَثُ عَنْ الْأَصْلِ هُنَا! فَقَطْ نَنْظُرُ إِلَى الْحَرْفِ الَّذِي قَبْلَ الْأَلِفِ مُبَاشَرَةً. إِذَا كَانَ الْحَرْفُ الَّذِي قَبْلَهَا (<span class="highlight-blue">يَاءً</span>): تُكْتَبُ <span class="highlight-red">مَمْدُودَةً (ا)</span> كَرَاهَةَ تَجَمُّعِ يَائَيْنِ.</p>
  (Component: TEMPLATE_C_LIST.html)
  Items:
  - دُنْيَا ، هَدَايَا ، مَرَايَا ، حَيَا ، يَحْيَا (الْفِعْلُ).
RightSide:
  (Component: TEMPLATE_C_BLOCK.html)
  Title: فَوْقَ الثُّلَاثِيَّةِ (قَبْلَهَا غَيْرُ الْيَاءِ)
  Content: <p>إِذَا كَانَ الْحَرْفُ الَّذِي قَبْلَهَا (<span class="highlight-blue">أَيَّ حَرْفٍ غَيْرَ الْيَاءِ</span>): تُكْتَبُ <span class="highlight-red">مَقْصُورَةً (ى)</span>.</p>
  (Component: TEMPLATE_C_LIST.html)
  Items:
  - مُلْتَقَى ، مُسْتَشْفَى ، اعْتَدَى ، أَمْضَى ، مَغْزَى.

=== BLOCK 6: Extra Info (Exception) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: اسْتِثْنَاءٌ هَامٌّ
Content: <p>وَيُسْتَثْنَى الِاسْمُ الْعَلَمُ (<span class="highlight-red">يَحْيَى</span>) لِلتَّمْيِيزِ بَيْنَهُ وَبَيْنَ الْفِعْلِ.</p>

=== BLOCK 7: Evaluation ===
(Component: TEMPLATE_C_EXAM.html)
Header Class: bg-dark
Number: ١
Question: مَتَى تُكْتَبُ الْأَلِفُ اللَّيِّنَةُ مَمْدُودَةً فِي الْكَلِمَاتِ الثُّلَاثِيَّةِ؟
Number: ٢
Question: لِمَاذَا كُتِبَتِ الْأَلِفُ مَقْصُورَةً فِي كَلِمَةِ "مُسْتَشْفَى"؟
Number: ٣
Question: مَا سَبَبُ كِتَابَةِ الْأَلِفِ مَقْصُورَةً فِي "يَحْيَى" بِالرَّغْمِ مِنْ أَنَّ مَا قَبْلَهَا يَاءٌ؟

--- END STREAM ---