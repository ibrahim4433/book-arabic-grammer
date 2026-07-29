# **SESSION 141**

[TASK DEFINITION]
Objective: Implement page 141.
File: `pages/page_141.html` (Note: Use the exact page number.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
1.5 ANTI-HALLUCINATION & STRICT TYPOGRAPHER RULE (CRITICAL): Do NOT invent, hallucinate, or add new grammar rules, examples, or external text. ONLY use the exact text slices provided in the Raw Input Text. You MUST use 100% of the provided raw text. NO summarizing, NO deleting, NO adding new content. Every piece of text must map to an approved TEMPLATE.
1.6 THE TYPO EXCEPTION: You are explicitly permitted to correct obvious typos, spelling errors, or grammatical errors in the raw Arabic text during planning.
2. Metadata:
    *   Page Number: 141
    *   Title: page 141
    *   Header Data (MANDATORY): You must populate the TEMPLATE_C_HEADER.html component with the specific metadata provided in the prompt:
        *   [CATEGORY_HEADER] <- Use 141
        *   [SECTION_HEADER] <- Use 141
        *   [AUTHOR_NAME] <- Use أ.الياس خفيف
        *   [AUTHOR_PHONE] <- Use 994066850 963+
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
11. You MUST preserve the EXACT Tashkeel (Harakat) from the input. Stripping diacritics is a critical failure. Do not generate bare Arabic letters without their vowels.
12. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal
14. **Page Wrappers**: The compiler will automatically wrap the final page in `TEMPLATE_C_PAGE_WRAPPER.html`. Do NOT include this template in your `[CONTENT STREAM]` blocks.
15. **Exam Section**: ONLY include the `TEMPLATE_C_EXAM.html` block if the provided raw text slice actually contains test/exam questions (e.g., keywords like "تطبيق", "امتحان"). Do NOT hallucinate an exam if it is not in the source text. **CRITICAL:** If an exam or exercise contains the answers in the raw text, you MUST use `TEMPLATE_C_EXAM_SOLVED.html` instead of `TEMPLATE_C_EXAM.html`.

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

=== BLOCK 2: Poet Biography ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b22080
[UNIQUE_ID_BIO]: b37657
[POEM_TITLE]: أحزان البنفسج
[POET_NAME]: (١٩٢٦ - ١٩٩٩م) <br> - شاعر عراقي، ولد في بغداد، والتحق بدار المُعَلِمِينَ وفيها تَعَرَّف إلى نازك الملائكة وبدر شاكر السياب وسليمان العيسى. <br> - يُعد في طليعة الشعراء المحدثين الذين طَوْرُوا الشَّعْرَ العَرَبِي،ُّ وَكَانَتْ سِيرَتُهُ الشَّعْرِيَّةُ صورةً حَقِيقِيَّةً لِحِيَاتِهِ الشَّخْصِيَّة.ِ <br> - مِنْ أَعمالِه:ِ (المَجْدُ لِلأطفال والزيتون كلمات لا تَمُوتُ البَحْرُ أَسْمَعُهُ يَتَنَهَّد،ُ أَباريق مُهَشَّمَةِ الذي أُخِذَ مِنْهُ هذا النَّصْ).

=== BLOCK 3: Introduction ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b37013
[UNIQUE_ID_BIO]: b01410
[POEM_TITLE]: مدخل إلى النص:
[POET_NAME]: - عَصَفَتْ بِالمُجْتَمَعِ العَرَبِي تَطَورات سياسية واجتماعية عميقة، بَدَتْ آثارها في مناحي الحياة كلها، ولا سيما الأدب؛ إِذْ أَفرزَتْ أَدبًا يَتَحَدَّثُ عَنْ قضايا الجماهير الكَادِحَة،ِ ويَسْتَمِدُّ مَادَّتَهُ مِنَ الواقع، ثُمَّ يُعِيدُ إبداعها مازجا بين الواقعية والفنّ الْعَذْبِ حَتَّى يُشَكَّلَ لوحة واقعِيَّةٌ تَشِعُّ بِظِلالِ الفَنِّ وَرَوْعَتِه،ِ ويَعْكس أحلام البسطاء وأمانيهم على الرغم مِنْ مُعاناتهم والامهم المُبَرِّحَة،ِ وهذا ما مَثَلَهُ في (أحزانُ البَنَفْسَجِ) خَيْرَ تَمْثِيلٍ.

=== BLOCK 4: Poem Verses ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b49430
[UNIQUE_ID_BIO]: b51090
[POEM_TITLE]: أحزان البنفسج
[POET_NAME]: عبد الوهاب البياتي
[RIGHT_HEMISTICH]: (١) الملايين التي تَكْدَح،ُ لَا تَحْلُمُ فِي مَوْتِ فَرَاشَهُ
[LEFT_HEMISTICH]: وبِأَحْزَانِ البَنَفْسَحْ
[RIGHT_HEMISTICH]: أو شِرَاعِ يَتَوج
[LEFT_HEMISTICH]: تَحْتَ ضَوْءِ القَمَرِ الأَخْضَرِ فِي ليلة صيف
[RIGHT_HEMISTICH]: أو غراميَّاتِ مَجَنُونِ بِطَيْفِ
[LEFT_HEMISTICH]: (٢) الملايينُ التي تَكْدَحُ
[RIGHT_HEMISTICH]: تَعْرَى
[LEFT_HEMISTICH]: تَتَمَزَّقُ
[RIGHT_HEMISTICH]: الملايين التي تَصْنَعُ لِلحَالِمِ زَوْرَقُ
[LEFT_HEMISTICH]: الملايين التي تَصْنَعُ مِنْدِيلًا لِمُغْرَمْ
[RIGHT_HEMISTICH]: الملايين التي تبكي
[LEFT_HEMISTICH]: تغني
[RIGHT_HEMISTICH]: تتألم
[LEFT_HEMISTICH]: في زوايا الأَرْض،ِ في مَصْنَعِ صَلْب،ٍ أو بِمَنْجَمْ
[RIGHT_HEMISTICH]: إِنَّهَا تَضَعُ قُرْصَ الشَّمْسِ مِنْ مَوْتٍ مُحَتَّمُ
[LEFT_HEMISTICH]: إِنَّهَا تَضْحَكُ مِنْ أَعْمَاقِها
[RIGHT_HEMISTICH]: تَضْحَكُ
[LEFT_HEMISTICH]: تُغْرَمْ
[RIGHT_HEMISTICH]: لا كما يُغْرَمُ مَجَنُونٌ بِطَيْفِ
[LEFT_HEMISTICH]: تحْتَ ضَوْءِ القَمَرِ الأَخْضَرِ فِي لَيْلَةِ صَيْفِ
[RIGHT_HEMISTICH]: (٣) الملايين التي تبكي
[LEFT_HEMISTICH]: تغني
[RIGHT_HEMISTICH]: تتألم
[LEFT_HEMISTICH]: تحْتَ شَمْسِ اللَّيْلِ بِالظُّلْمَةِ تَحْلَّمْ النَّجْمَةُ

=== BLOCK 5: Cut Content Part 1 ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
[UNIQUE_ID]: b64070
[BLOCK_TITLE]: معاني النص
[CONTENT]: معاني النص:

--- END STREAM ---
