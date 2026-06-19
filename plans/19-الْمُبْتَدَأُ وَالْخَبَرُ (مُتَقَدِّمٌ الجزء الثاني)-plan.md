# **SESSION 19.0**

[TASK DEFINITION]
Objective: Implement الْمُبْتَدَأُ وَالْخَبَرُ (مُتَقَدِّمٌ الجزء الثاني).
File: `pages/19.0_nXX_الْمُبْتَدَأُ وَالْخَبَرُ (مُتَقَدِّمٌ الجزء الثاني).html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/19.1_...` if page have a lot of blank space add exam elements from the lesson.
3. text Content: 100% Arabic with full Harakat.
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
7. Templates: You are forbidden from inventing new HTML tags or classes or template elements. You must map all content using "Jules-workspace/Templates/" components as the STREAM says in suitable way.
8. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). use "Jules-workspace/id_manager.py" to generate or verify them.
9. **Self-Correction:** Run "Jules-workspace/lint_pages.py" after creating html files. If it fails, you MUST fix the errors (usually inline styles) before submitting.
10. Do not summarize examples.
11. Do not provide uncompleted text content using (...) .
12. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
13. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
14. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal
15. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
16. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 19
[CHAPTER_TITLE]: الْمُبْتَدَأُ وَالْخَبَرُ (مُتَقَدِّمٌ الجزء الثاني)
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition Block (مَوَاضِعُ الْمُبْتَدَأِ) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٣- مَوَاضِعُ الْمُبْتَدَأِ (هَلْ يَأْتِي دَائِماً فِي أَوَّلِ الْكَلَامِ؟)
Content:
<p class="text-accent font-bold mb-4">نَعَمْ، يَأْتِي فِي:</p>
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT] 1: <span class="font-bold">أوَّل الجملة الابتدائية:</span> نحو: ( <span class="highlight-red">الحياةُ</span> جميلةٌ ).
[LIST_ITEM_CONTENT] 2: <span class="font-bold">أوَّل الجملة النَّعتيَّة</span> (الجملة التي تصف اسماً قبلها): نحو: (رأيتُ عالماً <span class="highlight-red">مَجْلِسُهُ</span> مُحْتَرَمٌ ).
<div class="mt-4">
(Component: TEMPLATE_C_BENEFIT.html)
Content: جُمْلَةُ (مَجْلِسُهُ مُحْتَرَمٌ) جُمْلَةٌ اسْمِيَّةٌ صَغِيرَةٌ دَاخِلَ الْجُمْلَةِ الْكَبِيرَةِ، مُبْتَدَؤُهَا (<span class="highlight-blue">مَجْلِسُهُ</span>).
</div>

=== BLOCK 3: Rule/Warning Box (الْقَاعِدَةُ وَالِاسْتِثْنَاءُ) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: <strong>٤- أَحْكَامُ الْمُبْتَدَأِ (مُسَوِّغَاتُ الِابْتِدَاءِ بِالنَّكِرَةِ):</strong> الْقَاعِدَةُ أَنَّ الْمُبْتَدَأَ يَجِبُ أَنْ يَكُونَ مَعْرِفَةً (فَلَا يَصِحُّ أَنْ تَقُولَ: رَجُلٌ قَائِمٌ). وَلَكِنْ يَجُوزُ أَنْ تَبْدَأَ بِنَكِرَةٍ فِي حَالَاتٍ مُحَدَّدَةٍ، كَمَا سَيَأْتِي:

=== BLOCK 4: Core Matrix (مُسَوِّغَاتُ الِابْتِدَاءِ بِالنَّكِرَةِ) ===
(Component: TEMPLATE_C_TABLE.html)
Headers: الْحَالَةُ | الْمِثَالُ | التَّوْضِيحُ
Row 1: أَنْ تَكُونَ مَوْصُوفَةً | صَديقٌ مُخْلِصٌ خَيْرٌ مِنْ أخٍ لَمْ تَلِدْهُ أُمُّكَ | تَكْتَسِبُ التَّخْصِيصَ (مُخْلِصٌ صِفَتُهُ)
Row 2: أَنْ تَكُونَ مُضَافَةً | صُحْبَةُ كِتابٍ خَيْرٌ مِنْ صُحْبَةِ جَاهِلٍ | مُضَافٌ إِلَى نَكِرَةٍ
Row 3: أَنْ يَسْبِقَهَا الْخَبَرُ | فِي القَفَصِ عُصْفُورٌ | خَبَرٌ شِبْهُ جُمْلَةٍ (ظَرْفٌ أَوْ جَارٌّ وَمَجْرُورٌ)
Row 4: أَنْ تُسْبَقَ بِنَفْيٍ أَوْ اسْتِفْهَامٍ | هَلْ أَحَدٌ فِي الدَّارِ؟ / مَا خَائِنٌ مَحْبُوبٌ | سُبِقَتْ بِـ (هَلْ) أَو (مَا)
Row 5: بَعْدَ الْأَدَوَاتِ | لَوْلَا حَيَاءٌ لَبَكَيْتُ / خَرَجْتُ فَإِذَا رَجُلٌ بِالْبَابِ | بَعْدَ (لَوْلَا، إِذَا الفجائية، لَامِ الِابْتِدَاءِ)
Row 6: أَنْ تُفِيدَ الدُّعَاءَ | نَجَاحٌ لِلْمُجْتَهِدِينَ / وَيْلٌ لِلْمُهْمِلِينَ | دُعَاءٌ بِالنَّجَاحِ أَوِ الْوَيْلِ

=== BLOCK 5: Deep Dive Part 1 (التَّخْصِيصُ وَالْإِضَافَةُ) ===
(Component: TEMPLATE_C_SPLIT.html)
--- LeftSide ---
(Component: TEMPLATE_C_BLOCK.html)
Title: ١- مَوْصُوفَةٌ (لِلتَّخْصِيصِ)
Content:
<p class="mb-4 text-accent">أَنْ تَكُونَ مَوْصُوفَةً (فَتَكْتَسِبُ التَّخْصِيصَ): مِثْل (<span class="highlight-red">صَديقٌ</span> مُخْلِصٌ خَيْرٌ مِنْ أخٍ لَمْ تَلِدْهُ أُمُّكَ).</p>
(Component: TEMPLATE_C_IRAB_ROW.html)
Word 1: صَديقٌ
Irab 1: مُبْتَدَأٌ نَكِرَةٌ مَرْفُوعٌ
Word 2: مُخْلِصٌ
Irab 2: صِفَتُهُ مَرْفُوعَةٌ
--- RightSide ---
(Component: TEMPLATE_C_BLOCK.html)
Title: ٢- مُضَافَةٌ إِلَى نَكِرَةٍ
Content:
<p class="mb-4 text-accent">أَنْ تَكُونَ مُضَافَةً: مِثْل (<span class="highlight-red">صُحْبَةُ</span> كِتابٍ خَيْرٌ مِنْ صُحْبَةِ جَاهِلٍ).</p>
(Component: TEMPLATE_C_IRAB_ROW.html)
Word 1: صُحْبَةُ
Irab 1: مُبْتَدَأٌ مَرْفُوعٌ مُضَافٌ إِلَى نَكِرَةٍ
Word 2: كِتابٍ
Irab 2: مُضَافٌ إِلَيْهِ مَجْرُورٌ

=== BLOCK 6: Deep Dive Part 2 (تَقَدُّمُ الْخَبَرِ وَالسَّبْقُ بِالنَّفْيِ أَوِ الِاسْتِفْهَامِ) ===
(Component: TEMPLATE_C_SPLIT.html)
--- LeftSide ---
(Component: TEMPLATE_C_BLOCK.html)
Title: ٣- أَنْ يَسْبِقَهَا الْخَبَرُ
Content:
<p class="mb-4 text-accent">أَنْ يَسْبِقَهَا الْخَبَرُ (شِبْهُ جُمْلَةٍ، ظَرْفٌ أَوْ جَارٌّ وَمَجْرُورٌ): مِثْل ( فِي القَفَصِ <span class="highlight-red">عُصْفُورٌ</span> ).</p>
(Component: TEMPLATE_C_IRAB_ROW.html)
Word 1: عُصْفُورٌ
Irab 1: مُبْتَدَأٌ نَكِرَةٌ مُؤَخَّرٌ مَرْفُوعٌ
Word 2: فِي القَفَصِ
Irab 2: خَبَرٌ مُقَدَّمٌ (شِبْهُ جُمْلَةٍ)
--- RightSide ---
(Component: TEMPLATE_C_BLOCK.html)
Title: ٤- سَبْقٌ بِنَفْيٍ أَوْ اسْتِفْهَامٍ
Content:
<p class="mb-4 text-accent">أَنْ تُسْبَقَ بِنَفْيٍ أَوْ اسْتِفْهَامٍ: مِثْل ( هَلْ <span class="highlight-red">أَحَدٌ</span> فِي الدَّارِ؟ ) أَوْ ( مَا <span class="highlight-red">خَائِنٌ</span> مَحْبُوبٌ ).</p>
(Component: TEMPLATE_C_IRAB_ROW.html)
Word 1: أَحَدٌ / خَائِنٌ
Irab 1: مُبْتَدَأٌ نَكِرَةٌ مَرْفُوعٌ
Word 2: هَلْ / مَا
Irab 2: حَرْفُ اسْتِفْهَامٍ / حَرْفُ نَفْيٍ

=== BLOCK 7: Deep Dive Part 3 (بَعْدَ الْأَدَوَاتِ وَالدُّعَاءُ) ===
(Component: TEMPLATE_C_SPLIT.html)
--- LeftSide ---
(Component: TEMPLATE_C_BLOCK.html)
Title: ٥- بَعْدَ بَعْضِ الْأَدَوَاتِ
Content:
<p class="mb-4 text-accent">بَعْدَ (لَوْلَا، إِذَا الفجائية، لَامِ الِابْتِدَاءِ): مِثْل ( لَوْلَا <span class="highlight-red">حَيَاءٌ</span> لَبَكَيْتُ )، ( خَرَجْتُ فَإِذَا <span class="highlight-red">رَجُلٌ</span> بِالْبَابِ ).</p>
(Component: TEMPLATE_C_IRAB_ROW.html)
Word 1: حَيَاءٌ / رَجُلٌ
Irab 1: مُبْتَدَأٌ نَكِرَةٌ مَرْفُوعٌ
--- RightSide ---
(Component: TEMPLATE_C_BLOCK.html)
Title: ٦- إِذَا كَانَتْ تُفِيدُ الدُّعَاءَ
Content:
<p class="mb-4 text-accent">إِذَا كَانَتْ تُفِيدُ الدُّعَاءُ: مِثْل ( <span class="highlight-red">نَجَاحٌ</span> لِلْمُجْتَهِدِينَ )، أَوْ ( <span class="highlight-red">وَيْلٌ</span> لِلْمُهْمِلِينَ ).</p>
(Component: TEMPLATE_C_IRAB_ROW.html)
Word 1: نَجَاحٌ / وَيْلٌ
Irab 1: مُبْتَدَأٌ نَكِرَةٌ مَرْفُوعٌ

=== BLOCK 8: Exam Section ===
<section class="content-block">
<div class="block-body p-0">
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: حَدِّدِ الْمُبْتَدَأَ وَنَوْعَهُ فِي جُمْلَةِ: " فِي الْمَحَطَّةِ قِطَارٌ ".
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: أَعْرِبْ مَا تَحْتَهُ خَطٌّ: " بِحَسْبِكَ دِرْهَمٌ ".
(Component: TEMPLATE_C_EXAM.html)
Number: ٣
Question: حَوِّلِ الْخَبَرَ الْمُفْرَدَ إَلَى جُمْلَةٍ: " الْقَمَرُ سَاطِعٌ ".
</div>
</section>

--- END STREAM ---
