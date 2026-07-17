# **SESSION 30.0**

[TASK DEFINITION]
Objective: Implement الْمَنْصُوبَاتُ التَّمْيِيزُ.
File: `pages/30.0_nXX_الْمَنْصُوبَاتُ التَّمْيِيزُ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/30.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 30
[CHAPTER_TITLE]: الْمَنْصُوبَاتُ التَّمْيِيزُ
[CATEGORY_HEADER]: المستوى المتوسط
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. حنا خفيف
[AUTHOR_PHONE]:  

=== BLOCK 2: Definition & Rule ===
(Component: TEMPLATE_C_BLOCK.html)
Title: التَّمْيِيزُ (مُزِيلُ الْغُمُوضِ)
Content:
<p class="text-accent">التَّمْيِيزُ: اسْمٌ جَامِدٌ نَكِرَةٌ مَنْصُوبٌ يُمَيِّزُ (يُفَسِّرُ وَيُزِيلُ الْغُمُوضَ) عَنْ دَلَالَةِ اسْمٍ مُبْهَمٍ قَبْلَهُ يُدْعَى (الْمُمَيَّزَ).</p>
<p>إِذَا قُلْتُ لَكَ: اشْتَرَيْتُ عِشْرِينَ.. وَسَكَتُّ. هَلْ فَهِمْتَ شَيْئاً؟ لَا. لَكِنْ لَوْ قُلْتُ: اشْتَرَيْتُ عِشْرِينَ <span class="highlight-red">كِتَاباً</span>. فَقَدْ مَيَّزْتُ الْكَلَامَ.</p>

=== BLOCK 3: Detailed Breakdown 1 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَوَّلاً: التَّمْيِيزُ الْمَلْفُوظُ (الْمُفْرَدُ) يَقَعُ بَعْدَ الْمَقَادِيرِ
Content:
<p>يُزِيلُ الْإِبْهَامَ عَنْ اسْمٍ مَلْفُوظٍ قَبْلَهُ (أَسْمَاءُ الْوَزْنِ، الْكَيْلِ، الْمِسَاحَةِ، الْعَدَدِ).</p>
Inject `TEMPLATE_C_LIST.html` here:
[LIST_ITEM_CONTENT]: ١. أَسْمَاءُ الْوَزْنِ: اشْتَرَيْتُ كِيلُو <span class="highlight-red">مَوْزاً</span> – أَوْقَدْتُ قِنْطَاراً <span class="highlight-red">حَطَباً</span>.
[LIST_ITEM_CONTENT]: ٢. أَسْمَاءُ الْكَيْلِ: أَطْعَمْتُ الطُّيُورَ حَفْنَةً <span class="highlight-red">قَمْحاً</span> – شَرِبْتُ كُوباً <span class="highlight-red">مَاءً</span>.
[LIST_ITEM_CONTENT]: ٣. أَسْمَاءُ الْمِسَاحَةِ: اشْتَرَيْتُ ذِرَاعاً <span class="highlight-red">قُمَاشاً</span> – زَرَعْتُ هِكْتَاراً <span class="highlight-red">قَمْحاً</span>.
[LIST_ITEM_CONTENT]: ٤. أَسْمَاءُ الْعَدَدِ: (مِنْ ١١ إِلَى ٩٩): فِي قِسْمِ الأَشِعَّةِ أَحَدَ عَشَرَ <span class="highlight-red">طَبِيباً</span>. نَجَحَ عِشْرُونَ <span class="highlight-red">طَالِباً</span>.

=== BLOCK 4: Extra Info (Benefit Warning) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: فَائِدَةٌ إِعْرَابِيَّةٌ
Content: الِاسْمُ الْمُبْهَمُ (الْمُمَيَّزُ كَـ <span class="highlight-blue">عِشْرِينَ</span> وَ<span class="highlight-blue">كِيلُو</span>) يُعْرَبُ بِحَسَبِ مَوْقِعِهِ فِي الْجُمْلَةِ فَاعِلًا أَوْ مَفْعُولًا، بَيْنَمَا الِاسْمُ الْمَنْصُوبُ الْأَخِيرُ (<span class="highlight-red">مَوْزاً</span>، <span class="highlight-red">طَبِيباً</span>) يُعْرَبُ تَمْيِيزاً مَنْصُوباً.

=== BLOCK 5: Detailed Breakdown 2 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ثَانِياً: التَّمْيِيزُ الْمَلْحُوظُ (تَمْيِيزُ الْجُمْلَةِ/الْمُحَوَّلُ)
Content:
<p>هُوَ مَا يُزِيلُ الْإِبْهَامَ عَنْ مَعْنَى الْجُمْلَةِ كَكُلٍّ (يَأْتِي كَثِيراً بَعْدَ كَلِمَاتِ الْمُقَارَنَةِ كَـ <span class="highlight-blue">أَكْبَر</span> وَ<span class="highlight-blue">أَحْسَن</span> وَ<span class="highlight-blue">أَكْثَر</span>، وَبَعْدَ أَفْعَالِ الِامْتِلَاءِ كَـ <span class="highlight-blue">طَابَ</span>، وَ<span class="highlight-blue">امْتَلَأَ</span>، وَ<span class="highlight-blue">ازْدَادَ</span>):</p>
Inject `TEMPLATE_C_LIST.html` here:
[LIST_ITEM_CONTENT]: • (التَّمْيِيزُ بَعْدَ أَفْعَلِ التَّفْضِيلِ): أَنَا أَكْبَرُ مِنْكَ <span class="highlight-red">عُمْراً</span>. / أَنَا أَكْثَرُ مِنْكَ <span class="highlight-red">مَالاً</span>. (أَصْلُهَا: عُمْرِي أَكْبَرُ مِنْ عُمْرِكَ. عُمْراً: تَمْيِيزٌ مَنْصُوبٌ).
[LIST_ITEM_CONTENT]: • (التَّمْيِيزُ الْمُحَوَّلُ عَنِ الْفَاعِلِ بَعْدَ أَفْعَالٍ مُعَيَّنَةٍ): كَقَوْلِنَا: فَاضَ النَّهْرُ <span class="highlight-red">مَاءً</span>. مَاءً تَمْيِيزٌ مَنْصُوبٌ (الْأَصْلُ: فَاضَ مَاءُ النَّهْرِ).
[LIST_ITEM_CONTENT]: وَكَقَوْلِنَا: طَابَ الْمَكَانُ <span class="highlight-red">هَوَاءً</span>. هَوَاءً تَمْيِيزٌ مَنْصُوبٌ. (طَابَ هَوَاءُ الْمَكَانِ).

=== BLOCK 6: The Core Matrix ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مُقَارَنَةٌ هَامَّةٌ بَيْنَ الْحَالِ وَالتَّمْيِيزِ (كِلَاهُمَا نَكِرَةٌ مَنْصُوبَةٌ، كَيْفَ أُفَرِّقُ؟)
Content:
Inject `TEMPLATE_C_TABLE.html` here.
Headers:
[HEADER_1]: الْمِعْيَارُ
[HEADER_2]: الْحَالُ (كَيْفَ؟)
[HEADER_3]: التَّمْيِيزُ (مِنْ أَيِّ شَيْءٍ؟)
Row 1:
[CELL_1]: طَبِيعَةُ الِاسْمِ
[CELL_2]: مُشْتَقٌّ (يُبَيِّنُ الْهَيْئَاتِ مِثْلَ: ضَاحِكاً، مُسْرِعاً).
[CELL_3]: جَامِدٌ (يُبَيِّنُ الذَّوَاتِ/الْمَقَادِيرِ مِثْلَ: عُمُراً، كِتَاباً، قَمْحاً).
Row 2:
[CELL_1]: التَّكْرَارُ
[CELL_2]: يَتَكَرَّرُ بِلَا حَرْفِ عَطْفٍ (جِئْتُ جَائِعاً مُتْعَباً مَرِيضاً).
[CELL_3]: لَا يَتَكَرَّرُ إِلَّا بِالْعَطْفِ (اشْتَرَيْتُ تُفَّاحاً وَمَوْزاً).
Row 3:
[CELL_1]: التَّقْدِيمُ
[CELL_2]: يَجُوزُ تَقْدِيمُهُ عَلَى الْفِعْلِ (غَاضِباً جَاءَ الرَّجُلُ).
[CELL_3]: لَا يَجُوزُ تَقْدِيمُهُ إِطْلَاقاً (لَا يَصِحُّ: مَوْزاً اشْتَرَيْتُ كِيلُو).

=== BLOCK 7: Extra Evaluation Examples ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَمْثِلَةٌ إِضَافِيَّةٌ لِلتَّدْرِيبِ
Content:
Inject `TEMPLATE_C_LIST.html` here:
[LIST_ITEM_CONTENT]: ١. عِنْدِي عِشْرُونَ <span class="highlight-red">كِتَاباً</span>. (تَمْيِيزٌ مَلْفُوظٌ - عَدَدٌ)
[LIST_ITEM_CONTENT]: ٢. زَرَعَ الْفَلَّاحُ فَدَّاناً <span class="highlight-red">قُطْناً</span>. (تَمْيِيزٌ مَلْفُوظٌ - مِسَاحَةٌ)
[LIST_ITEM_CONTENT]: ٣. حَسُنَ الطَّالِبُ <span class="highlight-red">خُلُقاً</span>. (تَمْيِيزٌ مَلْحُوظٌ - مُحَوَّلٌ عَنِ الْفَاعِلِ)

=== BLOCK 8: Evaluation ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: اِسْتَخْرِجِ التَّمْيِيزَ مِنَ الْجُمَلِ التَّالِيَةِ وَبَيِّنْ نَوْعَهُ (مَلْفُوظٌ أَمْ مَلْحُوظٌ):
١. حَصَدَ الْفَلَّاحُ هِكْتَاراً قَمْحاً.
٢. خَالِدٌ أَكْثَرُ مِنْكَ خِبْرَةً.
٣. طَابَتِ الْقَرْيَةُ هَوَاءً.
٤. شَرِبْتُ كُوباً عَصِيراً.

=== BLOCK 9: Evaluation ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: أَعْرِبْ مَا تَحْتَهُ خَطٌّ: ازْدَادَ الطَّالِبُ عِلْماً. (الْخَطُّ تَحْتَ كَلِمَةِ عِلْماً).

--- END STREAM ---