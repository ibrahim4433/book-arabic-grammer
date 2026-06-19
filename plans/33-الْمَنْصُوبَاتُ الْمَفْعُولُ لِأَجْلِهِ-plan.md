# **SESSION 33.0**

[TASK DEFINITION]
Objective: Implement الْمَنْصُوبَاتُ الْمَفْعُولُ لِأَجْلِهِ.
File: `pages/33.0_nXX_الْمَنْصُوبَاتُ الْمَفْعُولُ لِأَجْلِهِ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/33.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 33
[CHAPTER_TITLE]: الْمَنْصُوبَاتُ الْمَفْعُولُ لِأَجْلِهِ
[CATEGORY_HEADER]: المستوى المتوسط
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition & Rule ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفعول لأجله (بَيَانُ السَّبَبِ)
Content: <p class="text-accent">المفعول لأجله، أو المفعول له: هو مصدرٌ قَلْبِيٌّ (إِحْسَاسٌ أَوْ رَغْبَةٌ دَاخِلِيَّةٌ) منصوبٌ يُذكر في الجملة لبيان سبب حدوث الفعل، وبيان الغاية التي من أجلها وقع الفعل.</p>

=== BLOCK 3: Detailed Breakdown ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَمْثِلَةٌ تَوْضِيحِيَّةٌ
Content:
<p>عندما تقول: عاقب القاضي المجرم <span class="highlight-red">تأديبًا</span> له... (لِمَاذَا عَاقَبَهُ؟ <span class="highlight-red">تَأْدِيباً</span>).</p>
<p>صَفَّقْتُ <span class="highlight-red">تَشْجِيعاً</span> لِلَّاعِبِ... (لِمَاذَا صَفَّقْتُ؟ <span class="highlight-red">تَشْجِيعاً</span>).</p>

=== BLOCK 4: Extra Info / Deep Dive ===
(Component: TEMPLATE_C_BLOCK.html)
Title: علامات معرفة المفعول لأجله بسهولة
Content: <p>أسهلُ طريقةٍ لتعرف المفعول لأجله هي العلامات التالية:</p>
(Inject TEMPLATE_C_LIST.html here inside the block-body)
[LIST_ITEM_CONTENT]: ١. أن يصلح جوابًا للسُّؤال المصَدَّر بإحدى أدوات الاستفهام: (لِمَ؟ لماذا؟).<br>- لماذا تَقْرَأُ؟ <span class="highlight-red">رَغْبَةً</span> فِي التَّعَلُّمِ. (<span class="highlight-red">رَغْبَةً</span>: مفعول لأجله).
[LIST_ITEM_CONTENT]: ٢. أن نُدْخِلَ عليه في جملته حرف الجرّ (اللَّام) من دون أنْ يتغيَّر المعنى.<br>- ذهَبْتُ إلى بِلاد الغُرْبَةِ <span class="highlight-red">طَلَبًا</span> للعلم = لطلبِ العلم.
[LIST_ITEM_CONTENT]: ٣. جواز تقديمه على فعله من دون أن يتغيَّر المعنى.<br>- أحجمْتُ عن ركوب البحر <span class="highlight-red">خوفًا</span> = <span class="highlight-red">خوفًا</span> أحجمْتُ.

=== BLOCK 5: Core Matrix (Summary Table) ===
(Component: TEMPLATE_C_TABLE.html)
Title: مُلَخَّصُ عَلامَاتِ الْمَفْعُولِ لِأَجْلِهِ
[HEADER_1]: الْعَلَامَةُ
[HEADER_2]: الْمِثَالُ
[HEADER_3]: التَّوْضِيحُ
[ROW_1_COL_1]: جَوَابٌ لِسُؤَالٍ (لِمَاذَا؟)
[ROW_1_COL_2]: لماذا تَقْرَأُ؟ <span class="highlight-red">رَغْبَةً</span> فِي التَّعَلُّمِ
[ROW_1_COL_3]: صَلُحَ أَنْ يَكُونَ جَوَاباً لِسُؤَالٍ بـ (لِمَاذَا)
[ROW_2_COL_1]: إِدْخَالُ حَرْفِ الْجَرِّ (اللَّامِ)
[ROW_2_COL_2]: ذهَبْتُ إلى بِلاد الغُرْبَةِ <span class="highlight-red">طَلَبًا</span> للعلم = لطلبِ العلم
[ROW_2_COL_3]: لَمْ يَتَغَيَّرِ الْمَعْنَى بِإِدْخَالِ اللَّامِ
[ROW_3_COL_1]: جَوَازُ تَقْدِيمِهِ عَلَى الْفِعْلِ
[ROW_3_COL_2]: أحجمْتُ عن ركوب البحر <span class="highlight-red">خوفًا</span> = <span class="highlight-red">خوفًا</span> أحجمْتُ
[ROW_3_COL_3]: جَازَ تَقْدِيمُهُ عَلَى الْفِعْلِ مِنْ دُونِ أَنْ يَتَغَيَّرَ الْمَعْنَى

=== BLOCK 6: Benefit Tip ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: تَنْبِيهٌ هَامٌّ
Content: المفعول لأجله يجب أن يكون مصدراً قلبياً (مثل: رغبة، خوف، طمع)، ولا يكون من أفعال الجوارح (مثل: القراءة، الكتابة).

=== BLOCK 7: Extra Examples ===
(Component: TEMPLATE_C_SPLIT.html)
LeftSide:
(Inject TEMPLATE_C_BLOCK.html inside left side)
Title: مِثَالٌ إِضَافِيٌّ ١
Content: <p>قُمْتُ <span class="highlight-red">إِجْلَالاً</span> لِلأُسْتَاذِ.</p>
(Inject TEMPLATE_C_IRAB_ROW.html inside block)
[WORD_1]: إِجْلَالاً
[DETAILS_1]: مفعول لأجله منصوب وعلامة نصبه الفتحة الظاهرة على آخره.
RightSide:
(Inject TEMPLATE_C_BLOCK.html inside right side)
Title: مِثَالٌ إِضَافِيٌّ ٢
Content: <p>يَجْتَهِدُ الطَّالِبُ <span class="highlight-red">أَمَلاً</span> فِي النَّجَاحِ.</p>
(Inject TEMPLATE_C_IRAB_ROW.html inside block)
[WORD_1]: أَمَلاً
[DETAILS_1]: مفعول لأجله منصوب وعلامة نصبه الفتحة الظاهرة على آخره.

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: حَدِّدْ نَوْعَ الْمَنْصُوبِ فِي الْجُمْلَةِ: "ذَاكَرْتُ مُذَاكَرَةً جَيِّدَةً".
Number: ٢
Question: حَدِّدْ نَوْعَ الْمَنْصُوبِ فِي الْجُمْلَةِ: "وَقَفْتُ احْتِرَامًا لِلْمُعَلِّمِ".
Number: ٣
Question: أَعْرِبْ مَا تَحْتَهُ خَطٌّ: "اشْتَرَيْتُ عِشْرِينَ <u class="highlight-red">كِتَابًا</u>".
Number: ٤
Question: أعرب ما تحته خط: " سَافَرْتُ <u class="highlight-red">لَيْلاً</u> ".

--- END STREAM ---