# **SESSION 141**

[TASK DEFINITION]
Objective: Implement page 141.
File: `pages/page_141.html` (Note: Use the exact page number.)
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
[LESSON_NUMBER]: 141
[CHAPTER_TITLE]: page 141
[CATEGORY_HEADER]: 141
[SECTION_HEADER]: 141
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: حياة الشاعر وأعماله ===
(Component: TEMPLATE_C_TABLE.html)
Title: أحزان البنفسج (١٩٢٦ - ١٩٩٩م)
Row 1: نشأته | شاعر عراقي، ولد في بغداد، والتحق بدار المُعَلِمِينَ وفيها تَعَرَّف إلى نازك الملائكة وبدر شاكر السياب وسليمان العيسى.
Row 2: ريادته | يُعد في طليعة الشعراء المحدثين الذين طَوْرُوا الشَّعْرَ العَرَبِي،ُّ وَكَانَتْ سِيرَتُهُ الشَّعْرِيَّةُ صورةً حَقِيقِيَّةً لِحِيَاتِهِ الشَّخْصِيَّة.ِ
Row 3: أعماله | مِنْ أَعمالِه:ِ (المَجْدُ لِلأطفال والزيتون، كلمات لا تَمُوتُ، البَحْرُ أَسْمَعُهُ يَتَنَهَّد،ُ أَباريق مُهَشَّمَةِ الذي أُخِذَ مِنْهُ هذا النَّصْ).

=== BLOCK 3: مدخل إلى النص ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مدخل إلى النص:
Content: عَصَفَتْ بِالمُجْتَمَعِ العَرَبِي تَطَورات سياسية واجتماعية عميقة، بَدَتْ آثارها في مناحي الحياة كلها، ولا سيما الأدب؛ إِذْ أَفرزَتْ أَدبًا يَتَحَدَّثُ عَنْ قضايا الجماهير الكَادِحَة،ِ ويَسْتَمِدُّ مَادَّتَهُ مِنَ الواقع، ثُمَّ يُعِيدُ إبداعها مازجا بين الواقعية والفنّ الْعَذْبِ حَتَّى يُشَكَّلَ لوحة واقعِيَّةٌ تَشِحُ بِظلالِ الفَنِّ وَرَوْعَتِه،ِ ويَعْكس أحلام البسطاء وأمانيهم على الرغم مِنْ مُعاناتهم والامهم المُبَرَحَة.ِ

=== BLOCK 4: تنبيه هام ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: وهذا ما مَثَلَهُ نص (أحزانُ البَنَفْسَجٍ) خَيْرَ تَمثيل.ٍ

=== BLOCK 5: قصيدة أحزان البنفسج ===
(Component: TEMPLATE_C_POEM.html)
Title: أحزان البنفسج
Poet: عبد الوهاب البياتي
Verses:
(١)
الملايين التي تَكْدَح،ُ
لَا تَحْلُمُ فِي مَوْتِ فَرَاشَهُ
وبِأَحْزَانِ البَنَفْسَحْ
أو شِرَاعِ يَتَوج
تَحْتَ ضَوْءِ القَمَرِ الأَخْضَرِ فِي ليلة صيف
أو غراميَّاتِ مَجَنُونِ بِطَيْفِ
(٢)
الملايينُ التي تَكْدَحُ
تَغْرى
تَتَمَرَّقُ
الملايين التي تَصْنَعُ لِلحَالِمِ زَوْرَقُ
الملايين التي تَصْنَعُ مِنْدِيلًا لِمُغْرَمْ
الملايين التي تبكي
تغني
تتألم
في زوايا الأَرْض،ِ في مَصْنَعِ صَلْب،ٍ أو بِمَنْجَمْ
إِنَّهَا تَضَعُ قُرْصَ الشَّمْسِ مِنْ مَوْتِ مُحَمَّمُ
إِنَّهَا تَضْحَكُ مِنْ أَعْمَاقِها
تَضْحَكُ
تُغْرَمْ
لا كما يُغْرَمُ مَجَنُونٌ بِطَيْفِ
تحْتَ ضَوْءِ القَمَرِ الأَخْضَرِ فِي لَيْلَةِ صَيْفِ
(٣)
الملايين التي تبكي
تغني
تتألم
تحْتَ شَمْسِ اللَّيْلِ بِاللُّقْمَةِ تَحْلَّمْ
النجمة

=== BLOCK 6: استكمال الدرس ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
Title: يتبع في الصفحة التالية
Content: معاني النص:

--- END STREAM ---
