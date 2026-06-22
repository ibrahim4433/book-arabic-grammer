# **SESSION 01.0**

[TASK DEFINITION]
Objective: Implement أَقْسَامُ الْكَلَاَمِ الْمُفِيدِ فِي اللُّغَةَ الْعَرَبِيَّةَ.
File: `pages/01.0_nXX_أَقْسَامُ الْكَلَاَمِ الْمُفِيدِ فِي اللُّغَةَ الْعَرَبِيَّةَ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/01.1_...` if page have a lot of blank space add exam elements from the lesson.
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
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
15. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 01
[CHAPTER_TITLE]: أَقْسَامُ الْكَلَاَمِ الْمُفِيدِ فِي اللُّغَةَ الْعَرَبِيَّةَ
[CATEGORY_HEADER]:
[SECTION_HEADER]:
[AUTHOR_NAME]: أ. حنا خفيف
[AUTHOR_PHONE]:  

=== BLOCK 2: مُقَدَّمَةً ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مُقَدَّمَةً
Content: <p class="text-accent">يُقَسِّمُ عُلَمَاءُ اللُّغَةَ الْعَرَبِيَّةَ مَا يَتَلَفَّظُ بِه الْإِنْسَانِ إِلَى خَمْسَةٍ أَقْسَامَ رَئِيسِيَّةَ لِفَهِمَ قَوَاعِدُ اللُّغَةَ الْعَرَبِيَّةَ بِشَكْلِ صَحِيحِ ، يَجِبُ أَوْلَا التَّمْييزِ بَيْن هَذِه الْمُصْطَلَحَاتِ الْخُمُسَةَ:</p>
(Component: TEMPLATE_C_CHIPS.html)
Chips: الْكَلِمَةُ, الْكِلَاَمُ, الْكَلْمُ, الْقَوْلُ, اللَّفْظُ

=== BLOCK 3: الْكَلِمَةُ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ١. الْكَلِمَةُ
Content:
<p class="text-accent"><strong>التَّعْرِيفَ:</strong> هِي اللَّفْظِ الْمَوْضُوعِ لِمُعَنَّى مُفْرَدَ. أي أَنّهَا لَفْظَةَ وَاحِدَةَ تَدَلٍّ عَلَى شَيْءِ مُعَيَّنِ بذَاتهُ.</p>
<p><strong>أَمِثْلَةَ:</strong> <span class="highlight-red">بَحْرٌ</span> ، <span class="highlight-red">قَلَمٌ</span> ، <span class="highlight-red">شَجَرَةً</span> ، <span class="highlight-red">تِلْميذٌ</span> ، <span class="highlight-red">مُعَلِّمٌ</span> ، <span class="highlight-red">رَجُلٌ</span></p>

=== BLOCK 4: اِسْتِثْنَاءَ ( إِطْلَاقَ الْكَلِمَةِ عَلَى الْجُمْلَةِ ) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: مُلَاحِظَةً وَاِسْتِثْنَاءَ
Content:
<p>فِي بَعْضِ الْأَحْيَانِ فِي اللُّغَةَ الْعَرَبِيَّةَ ، قَد يُقْصَدُ بـ "الْكَلِمَةَ" جُمْلَةَ كَامِلَةَ أَو كَلَاَمَا طَوِيلَا، كَمَا فِي:</p>
(Component: TEMPLATE_C_LIST.html)
Items:
- <strong>الشِّعْرَ الْعَرَبِيَّ:</strong> قَوْلُ الشَّاعِرِ: "أَقُولُ لهُ وقَد طَارَتْ شَعَاعًا ... مِنَ الْأَبْطَالِ وَيْحَكَ لَنْ تُرَاعِي"، فَالْمَقْصُودَ بِالْكَلِمَةِ هُنَا الْبَيْتُ كَامِلًا.
- <strong>الْخُطَبَ وَالْمَقُولَاتِ:</strong> مَقُولَةُ الْقَائِدِ الْمَشْهُورَةِ: "<span class="highlight-red">كَلِمَةُ</span> وَاحِدَةً أَقُولُهَا لَكُم اِتَّحَدُوا تَسُودُوا"، فَالْمَقْصُودَ بِالْكَلِمَةِ هُنَا الْجُمْلَةُ كَامِلَةٌ.

=== BLOCK 5: الشاهد الشعري ===
(Component: TEMPLATE_C_POEM.html)
Poem Verses: أَقُولُ لهُ وقَد طَارَتْ شَعَاعًا ... مِنَ الْأَبْطَالِ وَيْحَكَ لَنْ تُرَاعِي

=== BLOCK 6: إعراب الشاهد ===
(Component: TEMPLATE_C_IRAB_ROW.html)
Word: وَيْحَكَ لَنْ تُرَاعِي
Analysis: اِسْتُخْدِمَتْ هُنَا بِمَعْنَى "الْكَلِمَةِ" لِلدَّلَالَةِ عَلَى جُمْلَةٍ كَامِلَةٍ.

=== BLOCK 7: الْكِلَاَمُ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٢. الْكِلَاَمُ
Content:
<p class="text-accent"><strong>التَّعْرِيفَ:</strong> هُو مَا تَرَكُّبٍ مِن كَلْمَتَيْنِ فأَكْثَرِ ، وَأَفَادَ مُعَنًّى يُحْسِنُ السُّكُوتُ عَلَيْهِ (أَيَّ جُمْلَةِ تَامَّةِ الْمُعَنَّى).</p>
<p><strong>أَمِثْلَةَ:</strong></p>
(Component: TEMPLATE_C_LIST.html)
Items:
- <span class="highlight-red">السَّفَرُ مُفِيدٌ</span> (جُمْلَةَ اِسْمِيَّةَ مُكَوِّنَةَ مِن كَلْمَتَيْنِ وَتُفِيدُ مُعَنَّى تَامًّا).
- <span class="highlight-red">اِذْهَبْ</span> (تَبْدُو كَكَلِمَةِ وَاحِدَةِ ، لَكِنّهَا فِي الْأَصْلِ جُمْلَةً تَتَكَوَّنُ مِن كَلْمَتَيْنِ: الْفِعْلُ "اِذْهَبْ" وَالضَّمِيرَ الْمُسْتَتِرَ "أَنْت"، وَتُفِيدُ مُعَنَّى تَامًّا).

=== BLOCK 8: الْكَلِمُ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٣. الْكَلِمُ
Content:
<p class="text-accent"><strong>التَّعْرِيفَ:</strong> هُو مَا تَكَوُّنٍ مِن ثَلاث كَلِمَاتٍ فأَكْثَرِ ، <strong>سَوَاءً أَفَادَ مُعَنًّى يُحْسِنُ السُّكُوتُ عَلَيْهِ أَم لَم يُفِدْ</strong>.</p>
<p><strong>أَمِثْلَةَ:</strong></p>
(Component: TEMPLATE_C_LIST.html)
Items:
- <span class="highlight-red">كَتَبَ الطَّالِبُ الدَّرْسَ</span> (مُكَوِّنٌ مِن 3 كَلِمَاتٍ ، وَأَفَادَ مُعَنَّى تَامًّا يُسَمَّى <strong>كَلَّمَ</strong> وَيُسَمَّى أيضاً <strong>كِلَاَمَ</strong>).
- <span class="highlight-red">إِنْْ قَامَ زَيْدٌ...</span> أَو <span class="highlight-red">ضَعْ إِلَى نَحْفَظُ...</span> (مُكَوِّنٌ مِن 3 كَلِمَاتٍ ، لَكِنّهُ لَا يُفِيدُ مُعَنَّى تَامًّا يُسَمَّى <strong>كَلَّمَ</strong> فَقَط ، ولَا يُسَمَّى كَلَاَمَا).

=== BLOCK 9: الْقَوْلُ وَاللَّفْظُ ===
(Component: TEMPLATE_C_SPLIT.html)
Column 1 (Right/Logically Left):
(Component: TEMPLATE_C_BLOCK.html)
Title: ٤. الْقَوْلُ
Content:
<p class="text-accent"><strong>التَّعْرِيفَ:</strong> كَلٌّ مَا يَتَلَفَّظُ بِه الْإِنْسَانِ وَيَدُلُّ عَلَى مُعَنًّى ، سَوَاءً كَان مُفْرَدًا أَو مَرْكَبًا ، مُفِيدًا أَو غَيْر مُفِيدٍ. (وهُو أَعَمِّ مِن الْكَلِمَةِ وَالْكِلَاَمِ وَالْكَلْمِ).</p>
<p><strong>أَمِثْلَةَ:</strong></p>
(Component: TEMPLATE_C_LIST.html)
Items:
- <span class="highlight-red">أَسُدْ</span> (مُفْرَدٌ يَدُلُّ عَلَى مُعَنَّى قَوْلٍ ، وَكَلِمَةَ).
- <span class="highlight-red">طَالِبُ الْعِلْمِ</span> (مَرْكَبٌ يَدُلُّ عَلَى مُعَنًّى ، لَكِنّهُ لَا يُحْسِنُ السُّكُوتُ عَلَيْهِ قَوْلَ).
- <span class="highlight-red">الْعِلْمُ نُورٌ</span> (مَرْكَبٌ يَدُلُّ عَلَى مُعَنَّى تَامِّ قَوْلٍ ، وَكِلَاَمَ).

Column 2 (Left/Logically Right):
(Component: TEMPLATE_C_BLOCK.html)
Title: ٥. اللَّفْظُ
Content:
<p class="text-accent"><strong>التَّعْرِيفَ:</strong> هُو الصَّوْتِ الْمُشْتَمِلِ عَلَى بَعْضِ الْحُروفِ ، سَوَاءً أَفَادَ مُعَنًّى أَم لَم يُفِدْ.</p>
<p><strong>أَمِثْلَةَ:</strong></p>
(Component: TEMPLATE_C_LIST.html)
Items:
- <span class="highlight-red">سَيَّارَةَ</span> (صَوْتٌ بِحُروفٍ لَه مُعَنَّى لَفْظِ).
- <span class="highlight-red">لُزِّنَّ</span> أَو <span class="highlight-red">ديز</span> (مَقْلُوبَ كَلِمَةِ زَيْدِ) (صَوْتٌ بِحُروفٍ لَيْس لَه مُعَنَّى لَفْظٍ فَقَط ، ولَا يُسَمَّى كَلَمَّةٍ ولَا قَوْلًا).

=== BLOCK 10: مُلَخَّصَ الْفَرُوقِ ===
(Component: TEMPLATE_C_TABLE.html)
Headers: الْعِبَارَةَ / اللَّفْظَ | هَل هِي لَفْظِ ؟ | هَل هِي قَوْلِ ؟ | هَل هِي كَلِمَةِ ؟ | هَل هِي كِلَاَمِ ؟ | هَل هِي كَلِمِ ؟ | السَّبَبَ
Row 1: بَيْتَ | نَعَم | نَعَم | نَعَم | لَا | لَا | لَفْظَ مُفْرَدَ لَه مُعَنَّى .
Row 2: الْعِلْمُ نُورٌ | نَعَم | نَعَم | لَا | نَعَم | لَا | مَرْكَبٌ مِن كَلْمَتَيْنِ وَأَفَادَ مُعَنَّى تَامًّا يُحْسِنُ السُّكُوتُ عَلَيْهِ .
Row 3: فَهِمَ الطَّالِبُ الدَّرْسَ | نَعَم | نَعَم | لَا | نَعَم | نَعَم | مَرْكَبٌ مِن 3 كَلِمَاتٍ وَأَفَادَ مُعَنَّى تَامًّا .( فهُو كِلَاَمٍ وَكَلِمِ مَعَا ).
Row 4: لُزِّنَّ | نَعَم | لَا | لَا | لَا | لَا | مُجَرَّدَ حُروفِ تَخَرُّجٍ مِن الْفَمِ بِلَا أَيِّ مُعَنَّى .

=== BLOCK 11: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: حَدَّدَ نَوْعُ الْعِبَارَاتِ التَّالِيَةِ بِنَاءً عَلَى مَا دَرَسَتْ ( الْكَلِمَةَ ، الْكِلَاَمَ ، الْكَلْمَ ، الْقَوْلَ ، اللَّفْظَ ). مُلَاحِظَةً: قَد تَقْبَلُ الْعِبَارَةُ أَكْثَرَ مِن إِجَابَةِ:
1. شَجَرَةُ
2. السَّفَرُ مُفِيدٌ
3. اِذْهَبْ
4. كَتَبَ الطَّالِبُ الدَّرْسَ
5. ضَعْ إِلَى نَحْفَظُ
6. أَسَدُّ
7. طَالِبُ الْعِلْمِ
8. سَيَّارَةُ
9. لُزِّنَّ

Number: ٢
Question: اِقْرَأْ الْمَقُولَاتِ وَالْأَشْعَارِ التَّالِيَةِ ، ثُمَّ أَجِبُ:
أ) يَقُولُ الشَّاعِرُ: "أَقُولُ لهُ وقَد طَارَتْ شَعَاعًا ... مِنَ الْأَبْطَالِ وَيْحَكَ لَنْ تُرَاعِي". مَا الْمَقْصُودِ بـ "كَلِمَةَ" (وَيَحْكِ لَن تُرَاعِي) فِي هَذَا السِّيَاقِ، وهَل هِي لَفْظَةٍ مُفْرَدَةٍ أَم جُمْلَةٌ؟
ب) الْمَقُولَةَ الْمَشْهُورَةَ: "كَلِمَةُ وَاحِدَةُ أَقُولُهَا لَكُم: اِتَّحَدُوا تَسُودُوا". لِمَاذَا أُطْلِقُ عَلَى عِبَارَةِ "اِتَّحَدُوا تَسُودُوا" بأَنّهَا "كَلِمَةَ" رَغْمٌ أَنّهَا جُمْلَةَ كَامِلَةَ؟

Number: ٣
Question: ضَعْ عُلَّامَةَ (صَحَّ) أَو (خَطَأَ) مَع تَصْحِيحِ الْخَطَأِ:
1. ( ) كُلّ كَلِمٍ هُو كَلَاَمِ مُفِيدِ يُحْسِنُ السُّكُوتُ عَلَيْهِ.
2. ( ) "الْعِلْمُ نُورٌ" تُعْتَبَرُ كَلَاَمًا لأَنّهَا تَتُكُّونَ مِن كَلْمَتَيْنِ وَتُفِيدُ مُعَنَّى تَامًّا.
3. ( ) أَيَّ صَوْتٍ يَخْرُجُ مِن فَمِ الْإِنْسَانِ يَحْتَوِي عَلَى حُروفِ يُسَمَّى "قَوْلًا" حَتَّى لَو لَم يَكُنُّ لَه مُعَنًّى.
4. ( ) جُمْلَةُ "اِذْهَبْ" هِي كَلِمَةِ وَاحِدَةِ ولَيْسَت كَلَاَمًا.

--- END STREAM ---
