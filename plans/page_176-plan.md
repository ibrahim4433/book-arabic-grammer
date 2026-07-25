# **SESSION 176**

[TASK DEFINITION]
Objective: Implement page 176.
File: `pages/page_176.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. Verify this using `verify_layout.py`.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`.
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md`.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`, `.highlight-green` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   **Rule:** NO INLINE STYLES.
*   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
*   **Mapping:** `style="width: 20%"` -> `class="w-20pct"`, `style="margin-top: 2mm"` -> `class="mt-2mm"`, `style="text-align: center"` -> `class="text-center"`, `style="font-weight: bold"` -> `class="font-bold"`
6. Templates: You are forbidden from inventing new HTML tags or classes or template elements. Replace any `<section>` tags from the templates with `<div>` tags (keep `<header>` for page headers as is).
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). The ID MUST be applied to the `<div>` tag that replaced the `<section>` tag. Use "Jules-workspace/id_manager.py" to generate or verify them.
8. **Self-Correction:** Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...) .
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`).
15. Exam section always be in the end of the lesson.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 176
[CHAPTER_TITLE]: page 176
[CATEGORY_HEADER]: 176
[SECTION_HEADER]: 176
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Introduction Part 1 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مدخل إلى النص:
Content: <p class="text-accent">تاه المهاجرونَ فِي عَالَم مَادِّي يُحْصِي ويَزِنُ وَيَقِيسُ كُلِّ شَيْء،ٍ واحْتَنَقَتْ أصواتهُمُ الرَّقِيقَةُ فِي ضَجِيجِ الْمَصَانِعِ الْمَرَوْعِ وَصَفِيرِ البَوَاخِرِ الْمُدَوِي،</p>

=== BLOCK 3: Introduction Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Content: <table class="dense-table">
  <tr>
    <td class="w-50pct">فَزَاغَتِ الأَبْصَار،ُ وَرَاحَتِ الْبَصَائِرُ تَبْحَثُ عَنْ عَالَم بَدِيلِ خَلْفَ نَاطِحَاتِ السَّحَابِ وَمَدَائِنِ الضَّيَاع،ِ</td>
    <td class="w-50pct">فَتَوَلَّدَتْ عوالم نابضة بالجمال، وتَفَتَّحَتْ على ما يُشْبِهُ الجَنَّةَ الْمَوْعُودَة.َ</td>
  </tr>
</table>

=== BLOCK 4: Title Warning Box ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: <p class="m-0">- (الغاب) عُنوان مُخْتَارٌ لِمَقْطَعِ مِنْ مَقَاطِعِ الْمَوَاكِبِ الْمُطَوَّلَة الشعرية، وهي أَوَّلُ صَوْتٍ عَرَبِي يَرْتَفِعُ مُنَدِّدًا بقيم المُجْتَمَعِ الْمَادِّيِّ بَاحِثًا عَنْ وَطَنِ سِحْرِي.</p>

=== BLOCK 5: The Poem and Bio ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: الغاب
[POET_NAME]: أ. جبران خليل جبران (١٨٨٣ - ١٩٣١م) - ولد في بشري فِي لَبْنَان،َ وَتَلَقَى تعليمه في بيروت، ثُم ارتحل إلى الولايات المتحدة الأمريكية، عاد بعدها إلى بيروتَ فَتَتَقْفَ بِاللُّغَةِ العَرَبِيَّةِ أَرْبَعَ سَنَوات،ِ وَسَافَرَ إلى باريس، فَمَكَثَ فيها ثلاث سنواتٍ . حاز بعدها إجازة الفُنُونِ فِي الرَّسْم.ِ - لَهُ كُتُبُ كثيرةٌ ذَائِعِةُ الصَّيتِ شِعْرًا ونَفْرًا منها : (المواكِب)؛ وهي مُطَوْلَةٌ شِعْرِيَّة،ٌ مِنْهَا اقْتُطِفَتْ هَذِهِ الأَبِيَات.ُ جُمِعَتْ أَعْمَالَهُ فِي مُجَلَّدين (الأَعمال العربية، والأَعْمَالُ المُعَرَّبَةُ).
[RIGHT_HEMISTICH]: ١- لَيْسَ فِي الغَابَاتِ حُزْنٌ
[LEFT_HEMISTICH]: لا ولا فيها هُمُوم
[RIGHT_HEMISTICH]: ٢- فَإِذا هَبَّ نَسِيم
[LEFT_HEMISTICH]: لم تَجِئْ معه السموم
[RIGHT_HEMISTICH]: ٣- لَيْسَ حَزْنُ النَّفْسِ إِلَّا
[LEFT_HEMISTICH]: ظلَ وَهُم لَا يَدُوم
[RIGHT_HEMISTICH]: ٤- وَغُيُومُ النَّفْسِ تَبْدُو
[LEFT_HEMISTICH]: مِنْ ثَناياهَا النجوم
[RIGHT_HEMISTICH]: ٥- أَعْطِنِي النَّايَ وَغَنِ
[LEFT_HEMISTICH]: فَالغِنا مَحْوُ المِحَنْ
[RIGHT_HEMISTICH]: ٦- وأنين الناي يَبْقَى
[LEFT_HEMISTICH]: بَعْدَ أَنْ يَفْنَى الزَّمَنْ
[RIGHT_HEMISTICH]: ٧- هَلْ تَخِذْتَ الغَابَ مِثْلِي
[LEFT_HEMISTICH]: مَنْزِلَا دُونَ القُصُور؟
[RIGHT_HEMISTICH]: ٨- وَتَسَلَّقْتَ الصخور
[LEFT_HEMISTICH]: فَتَتَبَّعْتَ السواقي
[RIGHT_HEMISTICH]: ٩- هَلْ تَحَمَّمْتَ بِعِطْرِ
[LEFT_HEMISTICH]: وتَنَشَفْتَ بِنُور؟
[RIGHT_HEMISTICH]: ١٠- وشربتَ الفَجْرَ خَمَرًا
[LEFT_HEMISTICH]: في كؤوسِ مِنْ أَثِيرُ
[RIGHT_HEMISTICH]: ١١- هَلْ جَلَسْتَ العَصْرَ مِثْلِي
[LEFT_HEMISTICH]: بَيْنَ جَفْنَاتِ العِنَبْ؟!
[RIGHT_HEMISTICH]: ١٢- والعَنَاقِيدُ تَدَلَّتْ
[LEFT_HEMISTICH]: كَتُرَيَّاتِ الذَّهَبْ
[RIGHT_HEMISTICH]: ١٣- هَلْ فَرَشْتَ العُشْبَ لَيْلًا
[LEFT_HEMISTICH]: وَتَلَحَّفْتَ الفَضَا؟
[RIGHT_HEMISTICH]: ١٤- زاهدا فِيمَا سَيَأْتي
[LEFT_HEMISTICH]: ناسيا ما قَدْ مَضَى
[RIGHT_HEMISTICH]: ١٥- وَسُكُوتُ اللَّيْلِ بَحْرٌ
[LEFT_HEMISTICH]: مَوْجُهُ فِي مسمعك
[RIGHT_HEMISTICH]: ١٦- وَبِصَدْرِ اللَّيْلِ قَلْبٌ
[LEFT_HEMISTICH]: خَافِقٌ فِي مَضْجَعِك
[RIGHT_HEMISTICH]: ١٧- أَعْطِنِي النَّايَ وَغَنِّ
[LEFT_HEMISTICH]: وَانْسَ داءً وَدَواء
[RIGHT_HEMISTICH]: ١٨- إنما النَّاسُ سُطُور
[LEFT_HEMISTICH]: كُتِبَتْ لَكِنْ بِمَاءً

=== BLOCK 6: Cut Box Start ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
Title: مهارات الاستماع :
Content:

--- END STREAM ---
