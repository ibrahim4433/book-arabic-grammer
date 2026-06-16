# **SESSION 30.0**

[TASK DEFINITION]
Objective: Implement العاطفة.
File: `pages/30.0_nXX_العاطفة.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/30.1_...` if page have a lot of blank space add exam elements from the lesson.
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

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER)
[LESSON_NUMBER]: 30
[CHAPTER_TITLE]: العاطفة
[CATEGORY_HEADER]: فوائد
[SECTION_HEADER]: المستوى الفني
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Concept of Emotion ===
(Component: TEMPLATE_C_BLOCK)
Title: مَفْهُومُ العاطِفَةِ وأَدَواتُها
Content:
<p class="text-accent text-justify mb-2mm">
    العاطِفَةُ هِيَ الشُّعُورُ الَّذِي يُخالِجُ الأَدِيبَ تِجاهَ مَوْقِفٍ أَوْ تَجْرِبَةٍ، كَالحُزْنِ والأَسَى والأَلَمِ والكَآبَةِ، أَوِ الفَرَحِ والإِعْجابِ والافْتِخارِ.
</p>
<p class="text-justify">
    ويَتِمُّ التَّعْبِيرُ عَنْ هَذا الشُّعُورِ بِأَدَواتٍ فَنِّيَّةٍ مُتَنَوِّعَةٍ، أَبْرَزُها: <span class="highlight-red">الأَلْفاظُ</span>، و<span class="highlight-blue">التَّراكِيبُ</span>، و<span class="highlight-green">الصُّورُ البَيانِيَّةُ</span>.
</p>

=== BLOCK 3: Summary Matrix ===
(Component: TEMPLATE_C_TABLE)
Title: جَدْوَلُ تَحْلِيلِ العاطِفَةِ (نَماذِجُ)
[TABLE_HEADERS]:
<th>الشُّعُورُ العاطِفِيُّ</th>
<th>الأَداةُ الفَنِّيَّةُ</th>
<th>المِثالُ التَّطْبِيقِيُّ</th>
[TABLE_ROWS]:
<tr>
    <td class="font-bold text-center">الحُزْنُ والأَسَى</td>
    <td class="text-center">التَّراكِيبُ</td>
    <td>إِنْ كُنْتَ مُكْتَئِبًا، إِنْ كُنْتَ مُكْتَئِبًا لِعِزٍّ مَضَى</td>
</tr>
<tr>
    <td class="font-bold text-center">الأَلَمُ والكَآبَةُ</td>
    <td class="text-center">الصُّورُ البَيانِيَّةُ</td>
    <td>يُرْجِعُهُ تَنَدُّمُ، عِزٍّ قَدْ مَضَى</td>
</tr>
<tr>
    <td class="font-bold text-center">الإِعْجابُ</td>
    <td class="text-center">الصُّورُ البَيانِيَّةُ</td>
    <td>صُوَرٌ تَتَكَلَّمُ، تُطِلُّ مِنَ الثَّرَى صُوَرٌ</td>
</tr>

=== BLOCK 4: Applied Model 1 (Admiration) ===
(Component: TEMPLATE_C_BLOCK)
Title: نَمُوذَجٌ تَطْبِيقِيٌّ: شُعُورُ الإِعْجابِ
Content:
<div class="mb-4mm">
    (Component: TEMPLATE_C_POEM)
    [POEM_VERSE_1_RIGHT]: كُنْ غَدِيـــرًا يَسِيرُ في الأَرْضِ رَقْرا
    [POEM_VERSE_1_LEFT]: قًا فَيَسْقِي مِنْ جانِبَيْهِ الحُقُولا
</div>
<p class="mb-2mm">أَسْهَمَتِ الأَلْفاظُ والتَّراكِيبُ الوارِدَةُ في البَيْتِ السَّابِقِ بِإِبْرازِ شُعُورِ <span class="highlight-red">الإِعْجابِ</span>:</p>
(Component: TEMPLATE_C_LIST)
[LIST_ITEMS]:
<li class="list-item-content">
    <span class="font-bold text-primary">الأَلْفاظُ:</span> (غَدِير، رَقراق، يَسْقِي).
</li>
<li class="list-item-content">
    <span class="font-bold text-primary">التَّراكيبُ:</span> (كُنْ غَدِيرًا، يَسِيرُ في الأَرْضِ، يَسْقِي مِنْ جانِبِهِ الحُقُولا).
</li>

=== BLOCK 5: Comparative Analysis ===
(Component: TEMPLATE_C_SPLIT)
Title: مُقارَنَةٌ شُعُورِيَّةٌ بَيْنَ التَّراكِيبِ
[LEFT_CONTENT]:
<h4 class="text-center font-bold text-primary mb-2mm">التَّرْكِيبُ الأَوَّلُ</h4>
<div class="bg-grey-lighter p-2mm rounded mb-2mm text-center font-bold">
    سَتَبْقَى أَرْضُنا لَنا
</div>
<p class="text-justify">
    <span class="font-bold">الشُّعُورُ العاطِفِيُّ:</span> تَفاؤُلٌ، أو: حُبٌّ، أو: ثِقَةٌ، أو: أَمَلٌ.
</p>
[RIGHT_CONTENT]:
<h4 class="text-center font-bold text-accent mb-2mm">التَّرْكِيبُ الثَّانِي</h4>
<div class="bg-grey-lighter p-2mm rounded mb-2mm text-center font-bold">
    رَكَزْنا فَوْقَ أَرْضِنا أَعْلامَنا
</div>
<p class="text-justify">
    <span class="font-bold">الشُّعُورُ العاطِفِيُّ:</span> افْتِخارٌ، أو: فَرَحٌ، أو: اعْتِزازٌ، أو: زَهْوٌ.
</p>

=== BLOCK 6: Applied Model 3 (Sadness) ===
(Component: TEMPLATE_C_BLOCK)
Title: نَمُوذَجٌ تَطْبِيقِيٌّ: شُعُورُ الحُزْنِ
Content:
<div class="mb-4mm">
    (Component: TEMPLATE_C_POEM)
    [POEM_VERSE_1_RIGHT]: حارَ فِكْرِي وَضاقَ صَدْرِي وإِنْ حا
    [POEM_VERSE_1_LEFT]: رَ هُمُومًا يَضِيـــقُ عَنْها الفَضاءُ
</div>
<p class="mb-2mm">أَسْهَمَتِ الأَلْفاظُ والتَّراكِيبُ في البَيْتِ السَّابِقِ بِإِبْرازِ شُعُورِ <span class="highlight-red">الحُزْنِ</span> لَدَى الشَّاعِرِ:</p>
(Component: TEMPLATE_C_LIST)
[LIST_ITEMS]:
<li class="list-item-content">
    <span class="font-bold text-primary">الأَلْفاظُ:</span> (حارَ، ضاقَ، هُمُومًا، يَضِيقُ).
</li>
<li class="list-item-content">
    <span class="font-bold text-primary">التَّراكِيبُ:</span> (حارَ فِكْرِي، ضاقَ صَدْرِي، حارَ هُمُومًا، يَضِيقُ عَنْها الفَضاءُ).
</li>

=== BLOCK 7: Applied Model 4 (Optimism) ===
(Component: TEMPLATE_C_BLOCK)
Title: نَمُوذَجٌ تَطْبِيقِيٌّ: شُعُورُ التَّفاؤُلِ
Content:
<div class="mb-4mm">
    (Component: TEMPLATE_C_POEM)
    [POEM_VERSE_1_RIGHT]: وَتَوَقَّعْ إِذا السَّـــماءُ اكْفَهَرَّتْ
    [POEM_VERSE_1_LEFT]: مَطَرًا في السُّهُولِ يُحْيِي السُّهُولا
</div>
<p class="mb-2mm text-justify">
    <span class="font-bold">الشُّعُورُ العاطِفِيُّ:</span> التَّفاؤُلُ، أو: الأَمَلُ، أو: الإِعْجابُ.
</p>
<p class="mb-2mm text-justify">
    <span class="font-bold">الأَداةُ الَّتِي أَبْرَزَتْهُ:</span>
</p>
(Component: TEMPLATE_C_LIST)
[LIST_ITEMS]:
<li class="list-item-content">
    <span class="font-bold text-primary">التَّرْكِيبُ:</span> (تَوَقَّعْ مَطَرًا)، أو: (مَطَرًا يُحْيِي السُّهُولا).
</li>
<li class="list-item-content">
    <span class="font-bold text-primary">الأَلْفاظُ:</span> (مَطَرًا، يُحْيِي).
</li>
<li class="list-item-content">
    <span class="font-bold text-primary">الصُّورَةُ البَيانِيَّةُ:</span> (مَطَرًا يُحْيِي السُّهُولا).
</li>

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: حَدِّدِ الشُّعُورَ العاطِفِيَّ وأَداةَ التَّعْبِيرِ عَنْهُ (أَلْفاظٌ، تَراكِيبُ) في البَيْتِ الآتي:
Verse: أَنا الَّذِي نَظَرَ الأَعْمَى إِلَى أَدَبِي     وَأَسْمَعَتْ كَلِماتِي مَنْ بِهِ صَمَمُ

--- END STREAM ---
