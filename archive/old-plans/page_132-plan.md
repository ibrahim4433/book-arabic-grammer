# **SESSION 132**

[TASK DEFINITION]
Objective: Implement page 132.
File: `pages/page_132.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools. If it overflows, it is a catastrophic failure. Do NOT try to solve overflow by deleting text (Strict Typographer Rule). Solve it by choosing denser templates or omitting optional white-space.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`. Ensure exact visual continuity (same title, same classes).
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md` to identify the correct template to use for the continuation. You are forbidden from guessing. Scan the raw text for the preceding keyword to determine the active template and apply the correct `_PART_2.html` wrapping.
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
6. Templates: You are forbidden from inventing new HTML tags or classes or template elements. You must map all content using "Jules-workspace/Templates/" components as the STREAM says in suitable way. **CRITICAL 1-PAGE MODE RULE**: You MUST NOT use `<section>` tags when applying templates. Replace any `<section>` tags from the templates with `<div>` tags (keep `<header>` for page headers as is).
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). The ID MUST be applied to the `<div>` tag that replaced the `<section>` tag. Use "Jules-workspace/id_manager.py" to generate or verify them.
8. **Self-Correction:** Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files. If it fails, you MUST fix the errors (usually inline styles or forbidden section tags) before submitting.
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
[LESSON_NUMBER]: 132
[CHAPTER_TITLE]: page 132
[CATEGORY_HEADER]: 132
[SECTION_HEADER]: 132
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: التمسك بالأمل ===
(Component: TEMPLATE_C_BLOCK.html)
Title: التمسك بالأمل والتطلعُ إِلَى العَوْدَة:
Content:
<div class="text-accent font-bold">عبد الكريم الكرمي:</div>
غَدًا سَتَعُودُ والأَجْيَالُ تُصْفِي إِلَى وَقْعِ الخُطَا عِنْدَ الْإِيَابِ
<br><br>
<div class="text-accent font-bold">إصْرَارُ المهجرين الفلسطينيين على العودة:</div>
<div class="text-accent font-bold">محمود درويش:</div>
مَشْيَا على الأَقدام<br>
أَوْ زَحْفًا على الأيدي نَعُودُ

=== BLOCK 3: فضح وحشية الصهاينة ===
(Component: TEMPLATE_C_BLOCK.html)
Title: فَضْحُ وَحْشِيَّةِ الصَّهَائِنَةِ، وَإِبْرَازُ مُمَارَسَاتِهِمُ العُدْوَانِيَّةِ، وَتَصْوِيرُ جَرَائِمِهِم التِي يَقْتَرِفُونَهَا بِحَقِّ العائِدِين:
Content:
<div class="text-accent font-bold">حِرْمَانُ المُهَجَرِين الفلسطينيين مِنْ حَقَ العَوْدَةِ إِلَى دِيَارِهِم:</div>
<div class="text-accent font-bold">محمود درويش</div>
لَنْ يَمُرَّ الْعَائِدُون<br>
حَرَسُ الْحُدُودِ مُرَابِطٌ<br>
أو:<br>
<div class="text-accent font-bold">محمود درويش</div>
يَحْمِي الحُدُودَ مِنَ الحَنين<br>
أَمْرٌ بِإِطلاق الرصاص على الذي<br>
يَجْتَازُ هذا الجسر؛ هَذَا الْجِسْرُ<br>
مِقْصَلَةُ الذي مَا زَالَ يَحْلُمُ<br>
بالوطن

=== BLOCK 4: Summary Table ===
(Component: TEMPLATE_C_TABLE.html)
Headers: [No headers]
Row 1:
  Col 1: - الإِدْمَانُ على القتل واسْتِسْهَالُ الْقِيَامَ بِهِ:
  Col 2: محمود درويش: وَبَرَغْمِ أَنَّ القَتْلَ كَالتَّدْخِينِ
Row 2:
  Col 1: - قَتْلُ الحَالِمِينَ بِالعَوْدَةِ:
  Col 2: محمود درويش: وَالطَّلْقَةُ الأُخْرَى ....<br>أَصَابَتْ قَلْبَ جُنْدِي قَدِيمٌ<br>أو :<br>محمود درويش لَمْ يَقْتُلُوا الاثنين<br>كَانَ الشَّيْخُ يَسْقُطُ فِي مِيَاهِ النَّهْرِ

=== BLOCK 5: كثرة القتلى ===
(Component: TEMPLATE_C_BENEFIT.html)
Content:
<div class="text-accent font-bold">كَثْرَةُ القَتْلَى الفلسطينيين الحَالِمِينَ بِالعَوْدَةِ:</div>
محمود درويش كُلُّ القَوَافِلِ قَبْلَهُم غَاصَتْ<br>
وَكَانَ النَّهْرُ يَبْصُقُ ضِفَتَيْهِ<br>
قِطَعاً مِنَ اللَّحْمِ الْمُفَتَتِ<br>
في وُجُوهِ الْعَائِدِينَ

=== BLOCK 6: السخرية من الجنود ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content:
<div class="text-accent font-bold">- الإِشَارَةُ إِلَى عَدَمِ شَرْعِيَّةِ الوُجُودِ الصُّهْيُونِي فِي فِلَسْطِين (السُّخْرِيَةُ مِنَ الجُنُودِ الصَّهَائِنَةِ):</div>
محمود درويش: لكِنَّ الجُنُودَ الطَّيِّبِين<br>
الطَّالِعِينَ عَلَى فَهَارِسِ دَفْتَرِ<br>
قَذَفَتْهُ أَمْعَاءُ السَّنِينَ

=== BLOCK 7: الإقدام على جريمة ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Content:
<div class="text-accent font-bold">الإقْدَامُ على جَرِيمَةِ الأَغْتِصَابِ (الاعتداء على الحرُمَاتِ وَتَدْنِيْسُ الشَّرَفِ):</div>
محمود درويش والبنت التي صَارَتْ يَتِيْمَهُ<br>
كَانَتْ مُمَزَّقَةَ الثِّيَابِ<br>
- - <br>
وطَارَ عِطْرُ اليَاسَمِين<br>
<div class="text-center mt-2mm">۱۳۲</div>

--- END STREAM ---
