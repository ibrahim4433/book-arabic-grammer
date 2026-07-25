# **SESSION 130**

[TASK DEFINITION]
Objective: Implement page 130.
File: `pages/page_130.html` (Note: Use the exact page number.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools. If it overflows, it is a catastrophic failure. Do NOT try to solve overflow by deleting text (Strict Typographer Rule). Solve it by choosing denser templates or omitting optional white-space.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`. Ensure exact visual continuity (same title, same classes).
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md` to identify the correct template to use for the continuation. You are forbidden from guessing. Scan the raw text for the preceding keyword to determine the active template and apply the correct `_PART_2.html` wrapping.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
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
[LESSON_NUMBER]: 130
[CHAPTER_TITLE]: page 130
[CATEGORY_HEADER]: 130
[SECTION_HEADER]: 130
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Core Matrix (Summary Table) ===
(Component: TEMPLATE_C_TABLE.html)
(id="b00001")
Headers: الفكرة | الشاعر
Rows:
- إلغاء التجزئة والتخلص من قيود المستعمرين | سلامة عبيد
- التفاؤل بالمستقبل المشرق | سلامة عبيد
- الإشادة بالأمة العربية وتحررها | سلامة عبيد
- التحذير من التجزئة والدعوة للوحدة | سلامة عبيد
- الأدب الوطني ومشاعر الفرح بالجلاء | بدر الدين الحامد، عمر أبو ريشة، شفيق جبري

=== BLOCK 3: Cut Content Continuation ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
(id="b00002")
[BLOCK_TITLE]: تابع
Content: - إلغاء التَّجْزِيَّةِ والتَّخَلُّصِ مِنْ قُيُودِ الْمُسْتَعْمِرِين (رَفْضُ التَّجْزِئَةِ وَإِنْكَارُ الحُدُودِ الوَهْمِيَّةِ التي رسمها المسْتَعْمرون):

=== BLOCK 4: Poem 1 ===
(Component: TEMPLATE_C_POEM.html)
(id="b00003")
Poet: سلامة عبيد :
Verse 1: وتلاشَتْ مَعَ القُيُودِ أَسَاطِيرُ | حُدُودٍ رَهِيْبَةٌ نَكْرَاءُ

=== BLOCK 5: National Ideas 1 ===
(Component: TEMPLATE_C_BLOCK.html)
(id="b00004")
Content: - التفاؤل بالمُسْتَقْبَلِ المُشْرِقِ الوَاعِدِ بَعْدَ قِيَامِ الْوَحْدَة:ِ

=== BLOCK 6: Poem 2 ===
(Component: TEMPLATE_C_POEM.html)
(id="b00005")
Poet: سلامة عبيد
Verse 1: وأتى الغَدُ الضَّحُوكُ طَلِيقًا | وبِهِ مِنْ سَنَا الرَّجَاءِ سَنَاءُ

=== BLOCK 7: Call to Arab Nation ===
(Component: TEMPLATE_C_BLOCK.html)
(id="b00006")
Content: - الدعوة إلى الإِشَادَةِ بِالأُمَّةِ العَرَبِيَّةِ لِتَحَرُرِهَا وَاسْتِقْلاها (الاعتِزَارُ بِتَحَرَّرِ الْأُمَّةِ العَرَبِيَّةِ):

=== BLOCK 8: Poem 3 ===
(Component: TEMPLATE_C_POEM.html)
(id="b00007")
Poet: سلامة عبيد
Verse 1: وتغني أنادت | وَإِنَّا فِي أَرْضِنَا طُلَقَاءُ

=== BLOCK 9: Glorifying Arab Nation ===
(Component: TEMPLATE_C_BLOCK.html)
(id="b00008")
Content: تَمْجِيدُ الأُمَّةِ العَرَبِيَّةِ وَالتَّغَنِي بِصِفَاتِهَا : عا بأمني

=== BLOCK 10: Poem 4 ===
(Component: TEMPLATE_C_POEM.html)
(id="b00009")
Poet: سلامة عبيد :
Verse 1: دَرْبُ تَوْحِيدِ أُمَّةٍ جَبَلَتُهَا | مِنْ عَبِيرِ الْمُكَارِمِ العَلْيَاءُ

=== BLOCK 11: Warning against Division ===
(Component: TEMPLATE_C_BLOCK.html)
(id="b00010")
Content: -١٠ التَّحْذِيرَ مِنَ التَّجْزِنَةِ وَنَبْدَ الفُرْقَة:ِ

=== BLOCK 12: Poem 5 ===
(Component: TEMPLATE_C_POEM.html)
(id="b00011")
Poet: سلامة عبيد
Verse 1: أَيُّهَا التَّائِهُونَ فِي مَهْمَهِ الأَمْسِ | سَرَابٌ دُرُوبُكُم وَشَقَاءُ

=== BLOCK 13: Call to Arab Unity ===
(Component: TEMPLATE_C_BLOCK.html)
(id="b00012")
Content: ۱۱- الدَّعْوَة إلى الوَحْدَةِ العَرَبِيَّةِ (تَحْفِيز المتَرَدِّدِين للالتحاق بِرَكَبِ الوحْدَةِ العَرَبِيَّةِ):

=== BLOCK 14: Poem 6 ===
(Component: TEMPLATE_C_POEM.html)
(id="b00013")
Poet: سلامة عبيد:
Verse 1: أَيُّهَا التَّائِهُونَ فِي مَهْمَهِ الْأَمْسِ | سَرَابٌ دُرُوبُكُم وَشَقَاءُ
Verse 2: أَقْبِلُوا أَيُّهَا الْحَيَارَى فَهَذَا الدَّرْبُ | طَلْقٌ مُشَوَقٌ وَضَاءُ
Verse 3: دَرْبُ تَوْحِيدِ أُمَّةٍ جَبَلَتْهَا | مِنْ عَبِير المكَارِمِ العَلْيَاءُ

=== BLOCK 15: Fruits of Unity ===
(Component: TEMPLATE_C_BLOCK.html)
(id="b00014")
Content: -١٢ الإشارة إلى ثمارِ الوَحْدَةِ (وَصْفَ جَمَالِ الْحَيَاةِ بَعْدَ قِيَامِ الوَحْدَةِ):

=== BLOCK 16: Poem 7 ===
(Component: TEMPLATE_C_POEM.html)
(id="b00015")
Poet: سلامة عبيد :
Verse 1: أَزْهَرَتْ وَاحَةُ العُرُوبَةِ وَافْتَرَّتْ | وَمَاسَتْ جِنَانُهَا الْخَضْرَاءُ
Verse 2: وتَثَنَّتْ فِيهَا الجَدَاوِلُ سَكْرَى | وتَرَامَتْ فِي رَبُعِهَا الأَفْيَاءُ

=== BLOCK 17: Optimism in Unity ===
(Component: TEMPLATE_C_BLOCK.html)
(id="b00016")
Content: -۱۳ التَّفَاؤُلَ بِقِيَامِ الوَحْدَةِ (الإيمان بِقُدْرَةِ الجَمَاهِيرِ الْعَرَبِيَّةِ على بِنَاءِ مَا هَدَّمَهُ المُسْتَعْمِرُ):

=== BLOCK 18: Poem 8 ===
(Component: TEMPLATE_C_POEM.html)
(id="b00017")
Poet: سلامة عبيد
Verse 1: في غدٍ تَزْحَفُ الْجُمُوعُ لِتَبْنِي | بِيَدَيْهَا مَا هَدَّمَ الأَعْدَاءُ

=== BLOCK 19: Nature's Joy ===
(Component: TEMPLATE_C_BLOCK.html)
(id="b00018")
Content: -١٤ إشراك الطبيعة بالفرح بالوحدة :

=== BLOCK 20: Poem 9 ===
(Component: TEMPLATE_C_POEM.html)
(id="b00019")
Poet: سلامة عبيد:
Verse 1: إِنَّهَا فَرْحَةُ الْحَيَاةِ فَمِيدِي | يَا رَوَابِي وَهَلِلِي يَا سَمَاءُ

=== BLOCK 21: National Literature Header ===
(Component: TEMPLATE_C_BLOCK.html)
(id="b00020")
Classes: block-header accent
Title: ثالثاً - الأدب الوطني:
Content: - التَّعْبِيرِ عَنْ مَشَاعِرِ الفَرَحِ وَالزَّهو بِتَحْقِيقِ الجلاء (الفرح بجلاء المسْتَعْمر الغَرْبِي عَنْ أَرْضِ الوَطَنِ):

=== BLOCK 22: Poem 10 ===
(Component: TEMPLATE_C_POEM.html)
(id="b00021")
Poet: بدر الدين الحامد:
Verse 1: يَوْمُ الجَلَاءِ هُوَ الدُّنْيَا وَزَهْوَتُهَا | لَنَا ابْتِهَاجٌ وللباغِينَ إِرْغَامُ

=== BLOCK 23: Poem 11 ===
(Component: TEMPLATE_C_POEM.html)
(id="b00022")
Poet: عمر أبو ريشة:
Verse 1: يا عروس المجد تِيْهِي واسحبي | فِي مَغَانِينَا ذُيُولَ الشُّهُبِ

=== BLOCK 24: Poem 12 ===
(Component: TEMPLATE_C_POEM.html)
(id="b00023")
Poet: شفيق جبري:
Verse 1: يا عروس المجدِ طَابَ الْمُلْتَقَى | بَعْدَمَا طَالَ جَوَى المُغْتَرِبِ
Verse 2: حُلْمٌ على جَنَبَاتِ الشَّامِ أَمْ عِيدُ | لا الهم هم ولا التَّسْهِيدُ تَسْهِيدُ

=== BLOCK 25: Defeat of Colonizer ===
(Component: TEMPLATE_C_BLOCK.html)
(id="b00024")
Content: - تصوير هزيمة المستَعْمِرِ وَخَيْبَتِهِ فِي تَوْطِيدِ وُجُودِه على أَرْضِنا (السُّخْرِيَةِ مِنَ المُسْتَعْمر والشَّمَاتَةِ بِهَزِيمَتِهِ):

=== BLOCK 26: Poem 13 ===
(Component: TEMPLATE_C_POEM.html)
(id="b00025")
Poet: عمر أبو ريشة:
Verse 1: دَرَجَ البَغْيُ عَلَيْهَا حِقْبَةً | وَهَوَى دُونَ بُلُوغِ الْأَرَبِ
Verse 2: وَارَى كِبْرَ اللَّيَالِي دُونَهَا | لَيِّنَ النَّابِ كَلِيلَ الْمِخْلَبِ

=== BLOCK 27: Glorifying Martyrs ===
(Component: TEMPLATE_C_BLOCK.html)
(id="b00026")
Content: - تَمْجِيدُ النَّضْحِيَاتِ الَّتِي قَدَّمَهَا الشَّعْبُ السوري لنيل استقلاله، والاعتزاز بها (تَمْجِيدُ الشهادة والتضحيات المشرفة للأجدادِ مِنْ أَجْلِ الوَطَنِ والشُّهَدَاء):
عمر أبو ريشة :
بدر الدين الحامد:
(۱۳۰)

--- END STREAM ---
