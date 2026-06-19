# **SESSION 18.0**

[TASK DEFINITION]
Objective: Implement الْمُبْتَدَأُ وَالْخَبَرُ (مُتَقَدِّمٌ الجزء الأول).
File: `pages/18.0_nXX_الْمُبْتَدَأُ وَالْخَبَرُ (مُتَقَدِّمٌ الجزء الأول).html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/18.1_...` if page have a lot of blank space add exam elements from the lesson.
3. text Content: 100% Arabic with full Harakat.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green`  for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   **Rule:** NO INLINE STYLES.
*   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
*   **Mapping:**
    *   inline style width: 20% -> `class="w-20pct"`
    *   inline style margin-top: 2mm -> `class="mt-2mm"`
    *   inline style text-align: center -> `class="text-center"`
    *   inline style font-weight: bold -> `class="font-bold"`
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
[LESSON_NUMBER]: 18
[CHAPTER_TITLE]: الْمُبْتَدَأُ وَالْخَبَرُ (مُتَقَدِّمٌ الجزء الأول)
[CATEGORY_HEADER]: المستوى المتقدم
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition and General Rule ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَعْرِيفُ الْمُبْتَدَأِ وَالْخَبَرِ
Content: <p class="text-accent">المبتدأ والخبر اسمان مرفوعان تتألَّفُ منهما جملةٌ مفيدةٌ اسْمِيَّةٌ، نَحو: ( <span class="highlight-red">العِلْمُ</span> <span class="highlight-blue">نورٌ</span> ) .</p>

=== BLOCK 3: Tip about Base Rule ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Content: <span class="font-bold">قَاعِدَة:</span> الأصلُ في المبتدأ والخبرِ الرفعُ دائماً إِلَّا إِذَا دَخَلَتْ عَلَيْهِمَا (إِنَّ أَو كَانَ).

=== BLOCK 4: The Core Matrix (Summary Table) ===
(Component: TEMPLATE_C_TABLE.html)
Header: مُلَخَّصُ الْمُبْتَدَأِ وَالْخَبَرِ الْمُتَقَدِّمِ
Columns: الْعُنْصُرُ | التَّعْرِيفُ | أَنْوَاعُهُ وَصُوَرُهُ | حُكْمُهُ الْإِعْرَابِيُّ
Row 1: الْمُبْتَدَأُ | الِاسْمُ الصَّرِيحُ أَوِ الْمُؤَوَّلُ الَّذِي نَبْدَأُ بِهِ الْجُمْلَةَ، وَهُوَ الْمُتَحَدَّثُ عَنْهُ. | • اسْمٌ صَرِيحٌ ( <span class="highlight-red">الْعِلْمُ</span> نُورٌ )<br>• ضَمِيرٌ مُنْفَصِلٌ ( <span class="highlight-red">أَنْتَ</span> مُجِدٌّ )<br>• مَصْدَرٌ مُؤَوَّلٌ ( <span class="highlight-red">أَنْ تَتَعَاوَنُوا</span> خَيْرٌ لَكُمْ) أَيْ: <span class="highlight-red">تَعَاوُنُكُمْ</span> خَيْرٌ. | الرَّفْعُ دَائِمًا (لَفْظاً أَوْ مَحَلّاً).
Row 2: الْخَبَرُ | الْجُزْءُ الَّذِي يُكْمِلُ الْفَائِدَةَ مَعَ الْمُبْتَدَأِ وَبِهِ يَتِمُّ الْمَعْنَى وَلَيْسَ شَرْطاً أَنْ يَكُونَ اسْمًا ظَاهِرًا. | • مُفْرَدٌ ( السَّمَاءُ <span class="highlight-blue">صَافِيَةٌ</span> )<br>• جُمْلَةٌ (اسْمِيَّةٌ مِثْلَ: الْوَلَدُ <span class="highlight-blue">خُلُقُهُ حَسَنٌ</span> / فِعْلِيَّةٌ مِثْلَ: الطَّالِبُ <span class="highlight-blue">يَدْرُسُ</span>)<br>• شِبْهُ جُمْلَةٍ (ظَرْفٌ: الْعُصْفُورُ <span class="highlight-blue">فَوْقَ الشَّجَرَةِ</span> / جَارٌّ وَمَجْرُورٌ: الرَّجُلُ <span class="highlight-blue">فِي الدَّارِ</span>). | الرَّفْعُ (أَوْ فِي مَحَلِّ رَفْعٍ إِذَا كَانَ جُمْلَةً أَوْ شِبْهَ جُمْلَةٍ).

=== BLOCK 5: Deep Dive: Prepositional Starting Words ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٢- جَرُّ الْمُبْتَدَأِ لَفْظًا (هَلْ يُمْكِنُ أَنْ نَرَى كَسْرَةً تَحْتَ الْمُبْتَدَأِ؟)
Content: <p class="text-accent">نَعَمْ، فِي حَالَاتٍ نَادِرَةٍ جِدّاً لِأَسْبَابٍ بَلَاغِيَّةٍ، يُجَرُّ المبتدأُ بحَرْفَي الجَرِّ (الزَّائدَيْن) اللَّذَيْنِ لَا مَحَلَّ لَهُمَا إِلَّا التَّوْكِيدُ: (الباء) و(مِنْ) ، أو يُجَرُّ بحَرفِ الجَرِّ الشَّبيهِ بالزَّائِدِ (رُبَّ).</p><p>فيكون الاسم بَعْدَهَا مجرورًا لفظًا (بالكسرة الظاهرة نطقاً) ولكنه مَرْفُوعٌ مَحَلًّا على أنَّهُ مُبْتَدَأ.</p>

=== BLOCK 6: Examples of Prepositional Starting Words ===
(Component: TEMPLATE_C_LIST.html)
List Items:
- ( <span class="highlight-blue">بِـ</span> <span class="highlight-red">حَسْبِ</span> كَ دِرْهَمٌ ) (يكفيك درهم).
- ( هَلْ <span class="highlight-blue">مِنْ</span> <span class="highlight-red">طَبِيبٍ</span> حَاضِرٌ ) (هَلْ طَبِيبٌ حَاضِرٌ).
- ( <span class="highlight-blue">رُبَّ</span> <span class="highlight-red">ضارَّةٍ</span> نافِعَةٌ ) (قد تكون الضارة نافعة).

=== BLOCK 7: Detailed Grammar Parsing Title ===
(Component: TEMPLATE_C_BLOCK.html)
Title: 🧠 نَمَاذِجُ إِعْرَابِيَّةٌ لِلْمُتَقَدِّمِينَ (الْمُبْتَدَأُ الْمَجْرُورُ لَفْظًا)
Content: <p>إليك إعراب النماذج المتقدمة لتوضيح جر المبتدأ لفظا.</p>

=== BLOCK 8: Parsing Row 1 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
Box 1 (TEMPLATE_C_IRAB_BOX.html):
Word: بِحَسْبِكَ
Details: <span class="highlight-blue">الباء:</span> حَرْف جرّ زائد لِلتَّوْكِيدِ. <span class="highlight-red">حَسْب:</span> اسم مَجْرُورٌ لَفْظًا (بِالْكَسْرَةِ)، مَرْفُوعٌ مَحَلًّا على أنَّهُ مُبْتَدَأ. والكاف ضَمِيرٌ فِي مَحَلِّ جرّ مُضاف إليه.
Box 2 (TEMPLATE_C_IRAB_BOX.html):
Word: دِرْهَمٌ
Details: خَبَرُ الْمُبْتَدَأِ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ. (هذا الإعراب من مكملات الجملة لتوضيح المعنى).

=== BLOCK 9: Benefit Warning ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: انتبه: في الجملة السابقة (بِحَسْبِكَ دِرْهَمٌ)، المبتدأ هو (حَسْب) وهو مجرور لفظاً مرفوع محلاً.

=== BLOCK 10: Parsing Row 2 ===
(Component: TEMPLATE_C_IRAB_ROW.html)
Box 1 (TEMPLATE_C_IRAB_BOX.html):
Word: مِنْ سُؤَالٍ
Details: <span class="highlight-blue">مِنْ:</span> حَرْفُ جَرٍّ زائد. <span class="highlight-red">سُؤَالٍ:</span> اسم مَجْرُورٌ لَفْظًا مَرْفُوعٌ مَحَلًّا على أنَّهُ مُبْتَدَأ.
Box 2 (TEMPLATE_C_IRAB_BOX.html):
Word: (الخبر)
Details: مَحْذُوفٌ تقديره "مَوْجُودٌ"، أَيْ هَلْ سُؤَالٌ مَوْجُودٌ.

=== BLOCK 11: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: أَعْرِبْ مَا تَحْتَهُ خَطٌّ: رُبَّ ضَارَّةٍ نَافِعَةٌ. (الخط تحت: رُبَّ ضَارَّةٍ)
--- END STREAM ---
