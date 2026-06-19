# **SESSION 43.0**

[TASK DEFINITION]
Objective: Implement الْمِيزَانُ الصَّرْفِيُّ.
File: `pages/43.0_nXX_الْمِيزَانُ الصَّرْفِيُّ.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually, instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/43.1_...` if page have a lot of blank space add exam elements from the lesson.
3. text Content: 100% Arabic with full Harakat.
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
[LESSON_NUMBER]: 43
[CHAPTER_TITLE]: الْمِيزَانُ الصَّرْفِيُّ
[CATEGORY_HEADER]: المستوى المتوسط
[SECTION_HEADER]: علم الصرف
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition Block ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَعْرِيفُ الْمِيزَانِ الصَّرْفِيِّ
Content:
<p class="text-accent mb-4">
    <span class="font-bold">الْمِيزَانُ الصَّرْفِيُّ:</span> هُوَ مِقْيَاسٌ لِمَعْرِفَةِ حُرُوفِ الْكَلِمَةِ (الْأَصْلِيَّةِ وَالزَّائِدَةِ وَالْمَحْذُوفَةِ)، يَتَأَلَّفُ مِنْ ثَلَاثَةِ أَحْرُفٍ (<span class="highlight-red">فَ</span>، <span class="highlight-blue">عَ</span>، <span class="highlight-green">لَ</span>) تُقَابِلُ الْأُصُولَ الثَّلَاثَةَ الَّتِي تَتَكَوَّنُ مِنْهَا أَغْلَبُ الْكَلِمَاتِ الْعَرَبِيَّةِ فِي صِيغَةِ الْمَاضِي الثُّلَاثِيِّ.
</p>

=== BLOCK 3: Summary Table ===
(Component: TEMPLATE_C_TABLE.html)
Title: مِثَالٌ تَوْضِيحِيٌّ لِلْمِيزَانِ
Columns: 4
[HEADER_1]: حُرُوفُ الْمِيزَانِ
[HEADER_2]: فَاءُ الْفِعْلِ (الْحَرْفُ الْأَوَّلُ)
[HEADER_3]: عَيْنُ الْفِعْلِ (الثَّانِي)
[HEADER_4]: لَامُ الْفِعْلِ (الثَّالِثُ)
Rows:
- Row 1: الْكَلِمَةُ | ضَ | حِ | كَ
- Row 2: الْمِيزَانُ | فَ | عِ | لَ
Post-Table Text: نُطَابِقُ الْحَرَكَاتِ بِالضَّبْطِ: ضَحِكَ = فَعِلَ. شَرِبَ = فَعِلَ. كَتَبَ = فَعَلَ. كَرُمَ = فَعُلَ.

=== BLOCK 4: Deep Dive - Rules (Part 1) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: قَوَاعِدُ الْمِيزَانِ الصَّرْفِيِّ فِي الزِّيَادَةِ وَالْحَذْفِ
Content:
(Component: TEMPLATE_C_LIST.html inside body)
Items:
1. <span class="font-bold">الْفِعْلُ الثُّلَاثِيُّ الْمُجَرَّدُ (لَيْسَ فِيهِ زِيَادَةٌ):</span> تُقَابَلُ أُصُولُهُ بِـ (ف ع ل) مَعَ ضَبْطِ الْحَرَكَاتِ. <br>مِثَالٌ: <span class="highlight-blue">دَرَسَ</span> = <span class="highlight-red">فَعَلَ</span>.
2. <span class="font-bold">الزِّيَادَةُ بِأَحْرُفٍ زَائِدَةٍ (غَيْرِ أَصْلِيَّةٍ):</span> حُرُوفُ الزِّيَادَةِ مَجْمُوعَةٌ فِي كَلِمَةِ (سَأَلْتُمُونِيهَا).<br><span class="font-bold">الْقَاعِدَةُ:</span> نَزِنُ الْحُرُوفَ الْأَصْلِيَّةَ بِـ (ف ع ل)، وَنُنْزِلُ الْحُرُوفَ الزَّائِدَةَ فِي الْمِيزَانِ كَمَا هِيَ بِنَفْسِ مَكَانِهَا.<br>أَمْثِلَةٌ:<br>- <span class="highlight-blue">فَاتِحٌ</span> (مِنْ فَتَحَ فَعَلَ، الزَّائِدُ الْأَلِفُ بَعْدَ الْفَاءِ) = <span class="highlight-red">فَاعِلٌ</span>.<br>- <span class="highlight-blue">اسْتَخْرَجَ</span> (مِنْ خَرَجَ فَعَلَ، الزَّائِدُ أ، س، ت) = <span class="highlight-red">اسْتَفْعَلَ</span>.<br>- <span class="highlight-blue">مَكْتُوبٌ</span> (مِنْ كَتَبَ فَعَلَ، الزَّائِدُ الْمِيمُ وَالْوَاوُ) = <span class="highlight-red">مَفْعُولٌ</span>.

=== BLOCK 5: Deep Dive - Rules (Part 2) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: التَّضْعِيفُ وَالرُّبَاعِيُّ
Content:
(Component: TEMPLATE_C_LIST.html inside body)
Items:
1. <span class="font-bold">الزِّيَادَةُ بِالتَّكْرَارِ (التَّضْعِيف الشَّدَّةُ):</span> إِذَا كَانَتِ الشَّدَّةُ زِيَادَةً عَلَى الْأَصْلِ (كَانَ أَصْلُهُ ٣ أَحْرُفٍ وَشَدَّدْنَا الْوَسَطَ)، نُشَدِّدُ الْحَرْفَ الْمُقَابِلَ لَهُ فِي الْمِيزَانِ.<br>مِثَالٌ: <span class="highlight-blue">قَدَّمَ</span> (مِنْ قَدِمَ) = <span class="highlight-red">فَعَّلَ</span>. <span class="highlight-blue">دَرَّسَ</span> = <span class="highlight-red">فَعَّلَ</span>.
2. <span class="font-bold">الْفِعْلُ الرُّبَاعِيُّ الْمُجَرَّدُ (أُصُولُهُ ٤ أَحْرُفٍ مِثْلَ دَحْرَجَ، زَلْزَلَ):</span> بِمَا أَنَّ الْمِيزَانَ ٣ أَحْرُفٍ (ف ع ل)، نُكَرِّرُ (اللَّامَ) فِي آخِرِ الْمِيزَانِ لِيُصْبِحَ رُبَاعِيّاً.<br>مِثَالٌ: <span class="highlight-blue">دَحْرَجَ</span> = <span class="highlight-red">فَعْلَلَ</span>. <span class="highlight-blue">زَلْزَلَ</span> = <span class="highlight-red">فَعْلَلَ</span>. <span class="highlight-blue">طَمْأَنَ</span> = <span class="highlight-red">فَعْلَلَ</span>. (وَإِذَا كَانَ خُمَاسِيّاً مِثْل سَفَرْجَل نَقُولُ: <span class="highlight-red">فَعَلَّل</span>).

=== BLOCK 6: Benefit / Warning Box ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: تَنْبِيهٌ مُهِمٌّ
Content:
فِي الْمُضَعَّفِ الثُّلَاثِيِّ (مِثْلَ: شَدَّ، رَدَّ، مَدَّ)، الْحَرْفُ الْمُشَدَّدُ عِبَارَةٌ عَنْ حَرْفَيْنِ أَصْلِيَّيْنِ: أَحَدُهُمَا عَيْنُ الْكَلِمَةِ وَالْآخَرُ لَامُهَا (شَدَدَ). وَلِذَلِكَ لَا يُشَدَّدُ فِي الْمِيزَانِ، فَوَزْنُ (شَدَّ) هُوَ (فَعَلَ).

=== BLOCK 7: Deep Dive - Rules (Part 3) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الْإِعْلَالُ وَالْحَذْفُ (حَذْفُ حَرْفٍ أَصْلِيٍّ)
Content:
<p class="font-bold mb-4">الْقَاعِدَةُ: مَا يُحْذَفُ مِنَ الْكَلِمَةِ، نَحْذِفُ مَا يُقَابِلُهُ فِي الْمِيزَانِ.</p>
(Component: TEMPLATE_C_LIST.html inside body)
Items:
1. <span class="highlight-blue">قُلْ</span>: أَصْلُهُ (قَاوَلَ / قَالَ عَلَى وَزْنِ فَعَلَ). حُذِفَ حَرْفُ الْعِلَّةِ الَّذِي فِي النُّصْفِ (الْعَيْنُ). إِذَنْ (قُلْ) وَزْنُهَا (<span class="highlight-red">فُلْ</span>).
2. <span class="highlight-blue">صِفَة</span>: أَصْلُهَا وَصَفَ (فَعَلَ). حُذِفَتِ الْوَاوُ (الْفَاءُ)، وَزِيدَتِ التَّاءُ الْمَرْبُوطَةُ. إِذَنْ (صِفَة) وَزْنُهَا (<span class="highlight-red">عِلَة</span>).
3. <span class="highlight-blue">امْشِ</span>: أَصْلُهُ مَشَى (فَعَلَ). حُذِفَتِ الْيَاءُ الْأَخِيرَةُ (اللَّامُ) وَزِيدَتِ الْأَلِفُ. إِذَنْ (امْشِ) وَزْنُهَا (<span class="highlight-red">افْعِ</span>).
4. <span class="highlight-blue">يَرَى</span>: حُذِفَتِ الْفَاءُ فَيُصْبِحُ <span class="highlight-red">يَفَلُ</span>.

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Questions:
1. زِنِ الْكَلِمَةَ الْآتِيَةَ: اسْتَمَعَ.
2. زِنِ الْكَلِمَةَ الْآتِيَةَ: انْتَصَرَ.
3. زِنِ الْكَلِمَتَيْنِ: دَحْرَجَ، وَاسْتَعْمَلَ.

--- END STREAM ---