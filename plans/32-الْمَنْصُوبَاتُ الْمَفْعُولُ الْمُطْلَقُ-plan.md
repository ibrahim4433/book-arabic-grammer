# **SESSION 32.0**

[TASK DEFINITION]
Objective: Implement الْمَنْصُوبَاتُ الْمَفْعُولُ الْمُطْلَقُ.
File: `pages/32.0_nXX_الْمَنْصُوبَاتُ الْمَفْعُولُ الْمُطْلَقُ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/32.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 32
[CHAPTER_TITLE]: الْمَنْصُوبَاتُ الْمَفْعُولُ الْمُطْلَقُ
[CATEGORY_HEADER]: المستوى المتوسط
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفعول المطلق (مَصْدَرٌ مُؤَكِّدٌ)
Content:
<p class="text-accent">هُوَ مَصْدَرٌ مَنْصُوبٌ يُشْتَقُّ (يُؤْخَذُ) مِنْ نَفْسِ حُرُوفِ الْفِعْلِ الَّذِي قَبْلَهُ فِي الْجُمْلَةِ لِيُؤَكِّدَهُ، أَوْ يُبَيِّنَ نَوْعَهُ، أَوْ عَدَدَهُ.</p>

=== BLOCK 3: Examples ===
(Component: TEMPLATE_C_SPLIT.html)
Title: أَمْثِلَةٌ
LeftSide:
(Component: TEMPLATE_C_BLOCK.html)
Content:
- شَرِبَ الطِّفْلُ الحليبَ <span class="highlight-red">شُرْبًا</span> . (<span class="highlight-red">شُرْباً</span>: مَفْعُولٌ مُطْلَقٌ مَأْخُوذٌ مِن شَرِبَ).
- استمتع الطُّلَّابُ بالدَّرْسِ <span class="highlight-red">استمتاعًا</span> . (<span class="highlight-red">اسْتِمْتَاعاً</span>: مَأْخُوذٌ مِن اسْتَمْتَعَ).

RightSide:
(Component: TEMPLATE_C_BLOCK.html)
Content:
- انْتَصَرَ الْجَيْشُ <span class="highlight-red">انْتِصَاراً</span> كَبِيراً. (<span class="highlight-red">انْتِصَاراً</span>: مَأْخُوذٌ مِن انْتَصَرَ).

=== BLOCK 4: The Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Title: الغاية (أَنْوَاعُ) المفعول المطلق
Headers: [اَلنَّوْعُ], [اَلْمِثَالُ], [اَلتَّوْضِيحُ]
Rows:
- تأكيد معنى الفِعْل, خَطَفَ المهاجِمُ الكُرَةَ <span class="highlight-red">خَطْفًا</span> ., لَا يَأْتِي بَعْدَهُ شَيْءٌ يُوَضِّحُهُ. مِثْل: رَكَضْتُ <span class="highlight-red">رَكْضاً</span>.
- بيان عَدَدَ مَرَّاتِ حُدُوثِ الفِعْل, ضَرَبَ اللَّاعِبُ الكُرَةَ <span class="highlight-red">ضَرْبَةً</span> أَوْ <span class="highlight-red">ضَرْبَتَيْن</span> أَوْ <span class="highlight-red">ضَرَبَاتٍ</span> ., يُوَضِّحُ كَمْ مَرَّةً حَدَثَ الْفِعْلُ.
- بيان نوعَ الفِعْلِ (مُضافًا), مَرَّ المُتسابِقُ <span class="highlight-red">مَرَّ</span> السَّحاب., يَأْتِي بَعْدَهُ مُضَافٌ إِلَيْهِ لِتُوَضِّحَ نَوْعَ الْحَدَثِ (أَيْ مِثْلَ مُرُورِ السَّحَابِ).
- بيان نوعَ الفِعْلِ (موصوفًا), كَلَّمَ المُدَرِّسُ الطَّالِبَ <span class="highlight-red">تَكْلِيمًا</span> مُهَذَّبًا ., يَأْتِي بَعْدَهُ صِفَةٌ لِتُوَضِّحَ نَوْعَ الْحَدَثِ (<span class="highlight-red">تَكْلِيماً</span>: مَفْعُولٌ مُطْلَقٌ. مُهَذَّباً: صِفَتُهُ).
- بيان نوعَ الفِعْلِ (مُعَرَّفًا بأل), يَحْتَرِمُ الطُّلَّابُ المُدَرِّسَ <span class="highlight-red">الاحترامَ</span> كُلَّهُ., يَأْتِي بَعْدَهُ صِفَةٌ أَوْ مُضَافٌ.

=== BLOCK 5: Deep Dive - Types Expansion ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَفْصِيلُ أَنْوَاعِ المَفْعُولِ المُطْلَقِ
Content: يَأْتِي الْمَفْعُولُ الْمُطْلَقُ لِثَلَاثَةِ أَغْرَاضٍ:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: ١. تأكيد معنى الفِعْل: لَا يَأْتِي بَعْدَهُ شَيْءٌ يُوَضِّحُهُ. مِثْل: خَطَفَ المهاجِمُ الكُرَةَ <span class="highlight-red">خَطْفًا</span> . (لِلتَّأْكِيدِ فَقَطْ). رَكَضْتُ <span class="highlight-red">رَكْضاً</span>.
[LIST_ITEM_CONTENT]: ٢. بيان عَدَدَ مَرَّاتِ حُدُوثِ الفِعْل: يُوَضِّحُ كَمْ مَرَّةً حَدَثَ الْفِعْلُ. مِثْل: ضَرَبَ اللَّاعِبُ الكُرَةَ <span class="highlight-red">ضَرْبَةً</span> أَوْ <span class="highlight-red">ضَرْبَتَيْن</span> أَوْ <span class="highlight-red">ضَرَبَاتٍ</span> .
[LIST_ITEM_CONTENT]: ٣. بيان نوعَ الفِعْلِ: يَأْتِي بَعْدَهُ مُضَافٌ إِلَيْهِ أَوْ صِفَةٌ لِتُوَضِّحَ نَوْعَ الْحَدَثِ:
• مُضافًا (بَعْدَهُ مُضَافٌ إِلَيْهِ): مَرَّ المُتسابِقُ <span class="highlight-red">مَرَّ</span> السَّحاب. (أَيْ مِثْلَ مُرُورِ السَّحَابِ).
• موصوفًا (بَعْدَهُ صِفَةٌ): كَلَّمَ المُدَرِّسُ الطَّالِبَ <span class="highlight-red">تَكْلِيمًا</span> مُهَذَّبًا . (<span class="highlight-red">تَكْلِيماً</span>: مَفْعُولٌ مُطْلَقٌ. مُهَذَّباً: صِفَتُهُ).
• مُعَرَّفًا بأل: يَحْتَرِمُ الطُّلَّابُ المُدَرِّسَ <span class="highlight-red">الاحترامَ</span> كُلَّهُ.

=== BLOCK 6: Benefit Note (Orange Variant) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: حذف عامل المفعول المطلق
Content: قد يُحْذَفُ الفِعْلُ، ويَكْثُرُ هذا في الطَّلَب (الأمر) وَيَبْقَى الْمَفْعُولُ الْمُطْلَقُ نَائِباً عَنْهُ.
نحو: <span class="highlight-red">صَبْرًا</span> على الدِّرَاسَةِ أيُّها الطُّلَّابُ. (التَّقدير: اصبروا صَبْرًا). أَوْ <span class="highlight-red">شُكْرًا</span> لِلْمُعَلِّمِ. (أَشْكُرُهُ شُكْرًا). أَوْ <span class="highlight-red">سَمْعاً</span> وَطَاعَةً.

=== BLOCK 7: Extra Info: What Substitutes for Al-Maf'ul Al-Mutlaq ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ما ينوب عن المفعول المطلق
Content: أَحْيَاناً نَحْذِفُ الْمَفْعُولَ الْمُطْلَقَ، وَنَضَعُ مَكَانَهُ كَلِمَاتٍ أُخْرَى تَأْخُذُ إِعْرَابَهُ، مِنْهَا:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: ١. كَلِمَتا (كُلّ، وبَعْض): بشرط إضافتهما للمصدر (يَكُونُ الْمَصْدَرُ بَعْدَهُمَا مُضَافاً إِلَيْهِ). نحو: احترمْتُهُ <span class="highlight-red">كلَّ</span> الاحترام (أَحْتَرِمُهُ: فِعْلٌ. كُلَّ: نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ. الِاحْتِرَامِ: مُضَافٌ إِلَيْهِ).
[LIST_ITEM_CONTENT]: ٢. صِفَةُ المصْدَرِ المحذوف: أحِبُّ أرْضَ بِلادِي <span class="highlight-red">كَثِيرًا</span> . (الأصل: حُبًّا كَثِيرًا. حُذِفَ حُبّاً وَحَلَّتْ صِفَتُهُ مَكَانَهُ).
[LIST_ITEM_CONTENT]: ٣. العدد: ضَرَبْتُ الكُرَةَ <span class="highlight-red">ثَلَاثَ</span> ضَرَبَاتٍ. (ثَلَاثَ: نَائِبٌ، لِأَنَّهَا دَلَّتْ عَلَى الْعَدَدِ).
[LIST_ITEM_CONTENT]: ٤. اسم الإشارة: أقَدِّرُكَ <span class="highlight-red">هذا</span> التَّقْدِيرَ.

=== BLOCK 8: Evidence / I'rab ===
(Component: TEMPLATE_C_BLOCK.html)
Title: نَمُوذَجُ إِعْرَابٍ (المَفْعُول المُطْلَق)
Content: "حَفِظْتُ الدَّرْسَ <span class="highlight-red">حِفْظًا</span> جَيِّداً"
(Component: TEMPLATE_C_IRAB_ROW.html)
Word: حَفِظْتُ
Details: فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الفَاعِلِ، وَالتَّاءُ ضَمِيرٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.
Word: الدَّرْسَ
Details: مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَةُ.
Word: حِفْظًا
Details: مَفْعُولٌ مُطْلَقٌ (مُبَيِّنٌ لِلنَّوْعِ) مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَةُ.
Word: جَيِّداً
Details: صِفَةٌ مَنْصُوبَةٌ.

=== BLOCK 9: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: أَعْرِبْ مَا تَحْتَهُ خَطٌّ: "انْتَصَرَ الْجَيْشُ انْتِصَاراً كَبِيراً". (خَطٌّ تَحْتَ انْتِصَاراً كَبِيراً).
Number: ٢
Question: اسْتَخْرِجِ الْمَفْعُولَ الْمُطْلَقَ أَوِ النَّائِبَ عَنْهُ مِمَّا يَأْتِي، وَبَيِّنْ نَوْعَهُ.

--- END STREAM ---
