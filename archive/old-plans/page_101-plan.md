# **SESSION 101**

[TASK DEFINITION]
Objective: Implement page 101.
File: `pages/page_101.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`.
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md`.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   **Rule:** NO INLINE STYLES.
*   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
*   **Mapping:**
    *   `style="width: 20%"` -> `class="w-20pct"`
    *   `style="margin-top: 2mm"` -> `class="mt-2mm"`
    *   `style="text-align: center"` -> `class="text-center"`
    *   `style="font-weight: bold"` -> `class="font-bold"`
6. Templates: You are forbidden from inventing new HTML tags or classes or template elements. Replace any `<section>` tags from the templates with `<div>` tags (keep `<header>` for page headers as is).
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). Use "Jules-workspace/id_manager.py" to generate or verify them.
8. **Self-Correction:** Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files.
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
[LESSON_NUMBER]: 101
[CHAPTER_TITLE]: page 101
[CATEGORY_HEADER]: 101
[SECTION_HEADER]: 101
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: الوحدة الأولى ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الوحدة الأولى قضايا وطنية وقومية
Content:
<p class="text-accent">تعالج قصيدتاها بعض القضايا الوطنية والقومية، وقد تضمنت القصيدتين الآتيتين:</p>

=== BLOCK 3: القصائد ===
(Component: TEMPLATE_C_TABLE.html)
Content:
<table class="dense-table">
  <tr>
    <td>عرس المجد</td>
    <td>للشاعر السوري عمر أبو ريشة، عالج فيها قضية وطنية: إِذْ صَوّر فيها، معتزا، فرحة الانتصار بجلاء المحتل الفرنسي عَنْ أرض وطنه سوريا، وأشاد بتضحيات السوريين العظيمة في يوم الجلاء.</td>
  </tr>
  <tr>
    <td>الجسر</td>
    <td>للشاعر الفلسطيني محمود درويش، يرصد فيها عدم تخلي الفلسطينيين المهجرين عن حلم العودة إلى ديارهم.</td>
  </tr>
</table>

=== BLOCK 4: حياة الشاعر ===
(Component: TEMPLATE_C_POEM.html)
Title: <span class="block-header accent">عرس المجد عمر أبو ريشة ۱۹۱۰- ۰۹۹۱م</span>
Content:
<ul class="structured-list">
  <li>شاعر سُورِي،ٌّ نَشَاً وتَرَغْرَ فِي مَنْبِج،َ ثُمَّ أَقَامَ فِي حلب، وتَعَلَّم في مدارسها، ثُمَّ أَكمل دِرَاسَتَهُ فِي الجَامِعَةِ الأميركية في بيروت.</li>
  <li>شَغَلَ مَنَاصِبَ عِدَّة،ٌ فَمِنْ مدير لدار الكُتُبِ الوطنِيَّةِ يجلب، إلى سفير لبلاده في الهند، والمسا، والولايات المتحدة.</li>
  <li>أجاد في شِعْرِ الْحَمَاسَةِ والوطنية والغزل.</li>
  <li>خلف تسعة دواوين أحدها بالإنكليزية، ومَلحَمَة،ً وتسع مسرحيات.</li>
</ul>

=== BLOCK 5: مدخل إلى النص ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مدخل إلى النص:
Content:
<ul class="structured-list">
  <li>سَطْرَ الشعب في سورية بِدِمَائِهِ يوم الجلاء العظيم في السَّابِعَ عَشَرَ مِنْ نيسان عام ٦٤٩١م.</li>
  <li>أبو ريشة في هذا النَّصَ يُوْرَخُ لا نْتِصَارَاتِ بَلَدِهِ بِحُرُوفِ مِنْ نُور،ٍ وَيُصَوِّرُ فَرْحَةَ الأَنْتِصَارِ بِجَلَاءِ الْمُحْتَلِ عَنْ أَرْضِ الوطن، ويُشِيْدُ بتضحيات السوريين العظيمة في يوم الجلاء.</li>
</ul>

=== BLOCK 6: قصيدة عرس المجد ===
(Component: TEMPLATE_C_POEM.html)
Title: القصيدة
Content:
<div class="hemistich">
  <div>يا عَرُوسَ الْمَجْدِ تيهي واسحبي</div>
  <div>فِي مَغَانِينَا ذُيُولَ الشَّهب</div>
</div>
<div class="hemistich">
  <div>لَنْ تَرَي حَفْنَةَ رَمْلٍ فَوْقَهَا</div>
  <div>لَمَّ تُعَطَّرْ بِدما حرّ أَبِي</div>
</div>
<div class="hemistich">
  <div>دَرَجَ البَغْيُ عَلَيْهَا حِقْبَةً</div>
  <div>وَهَوى دُونَ بُلُوغِ الْأَرْبِ</div>
</div>
<div class="hemistich">
  <div>وارمى كير الليالي دُوهَا</div>
  <div>لَينَ النَّاب،ِ كَلِيلَ الْمِخْلَبِ</div>
</div>
<div class="hemistich">
  <div>ه لا يَمُوتُ الحَقُ مَهْمَا لَطَمَتْ</div>
  <div>عَارِضَيْهِ قَبْضَةُ الْمُغْتَصِبِ</div>
</div>
<div class="hemistich">
  <div>مِنْ هُنا شَقَّ الهُدَى أَكْمَامَهُ</div>
  <div>وَقَادَى مَوْكِبًا فِي مَوْكِبِ</div>
</div>
<div class="hemistich">
  <div>وأَتَى الدنيا فَرَفَّتْ طَرَبًا</div>
  <div>وانْتَشَتْ مِنْ عَبْقِهِ الْمُنْسَكِبِ</div>
</div>
<div class="hemistich">
  <div>وتَغَنَّتْ بِالمروات التي</div>
  <div>عَرَفَنْهَا فِي فَتاها العربي</div>
</div>
<div class="hemistich">
  <div>أَصْيَرِةٌ ضَاقَتْ بِهِ صَخواه</div>
  <div>فَأَعَدَّتْهُ لِأُفْقِ أَرْحَبِ</div>
</div>
<div class="hemistich">
  <div>۱۰- هَبَّ للفتح، فَأَدْمَى ..</div>
  <div>حَافِرُ الْمُهْرِ جَبِينَ الكُوكَبِ</div>
</div>
<div class="hemistich">
  <div>-۱۱ يا عَرُوسَ الْمَجْد،ِ طَابَ الْمُلْتَقَى</div>
  <div>بَعْدَمَا طَالَ جَوَى الْمُغْتَرِبِ</div>
</div>
<div class="hemistich">
  <div>-۱۲ قَدْ عَرَفْنَا مَهْرَكِ الغالي فَلَمْ</div>
  <div>نُرْخص الْمَهْر،َ وَلَمْ تَحْتَسِبِ</div>
</div>
<div class="hemistich">
  <div>-۱۳ وأَرقناها دِمَاءً حُرَّةً</div>
  <div>فاعرفي ما شِنْتِ منها واشربي!</div>
</div>
<div class="hemistich">
  <div>-١٤ نَحْنُ مِنْ ضَعَفٍ بَنَيْنَا قُوَّةً</div>
  <div>لَمْ تَلِنْ لِلْمَارِج الْمُلْتَهِبِ</div>
</div>
<div class="hemistich">
  <div>-١٥ هَذِهِ تُرْبِتُنَا لَنْ تَزْدَهِي</div>
  <div>بسوانا مِن حُمَاةٍ تُدُبِ</div>
</div>

--- END STREAM ---
