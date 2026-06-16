# **SESSION 02.0**

[TASK DEFINITION]
Objective: Implement عَلَاَّمَاتُ الْاِسْمِ.
File: `pages/02.0_nXX_عَلَاَّمَاتُ الْاِسْمِ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/02.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 02
[CHAPTER_TITLE]: عَلَاَّمَاتُ الْاِسْمِ
[CATEGORY_HEADER]:
[SECTION_HEADER]:
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: مُقَدَّمَةً ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مُقَدَّمَةً
Content:
<p class="text-accent">أَقْسَامُ الْكَلَاَمِ فِي اللُّغَةَ الْعَرَبِيَّةَ ثَلَاثَةَ : اِسْمٌ ، وَفِعْلٌ ، وَحَرْفَ .</p>
<p>لِكَي نَتَعَلَّمُ الْإِعْرَابَ بِالصُّورَةِ الصَّحِيحَةِ ، يَجِبُ أَن نَبْدَأُ بِخَطْوَتِنَا الْأوْلَى وهِي التَّمْييزِ بَيْن هَذِه الْأَقْسَامِ</p>
<p>وَالْيَوْمُ سَنُرَكِّزُ عَلَى الْقِسْمِ الْأَوَّلِ : <strong>الْاِسْمُ</strong>.</p>

=== BLOCK 3: مَعْلُومَةٌ مُهِمَّةٌ ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Title: مَعْلُومَةٌ مُهِمَّةٌ
Content: كَيْف نَعْرُفُ أَنّ هَذِه الْكَلِمَةِ اِسْمٌ ؟ لِلْاِسْمَ عَلَاَّمَاتٍ مُمَيَّزَةٍ ، وَمَجْمُوعَاتٍ يَنْتَمِي إِلَيْهَا.

=== BLOCK 4: Core Matrix of Signs ===
(Component: TEMPLATE_C_TABLE.html)
Title: مُلَخَّصُ عَلَاَّمَاتِ الْاِسْمِ
Columns: | الْعَلَاَّمَةُ | الْمِثَالُ |
Row 1: | الْجَرُّ | ذَهَبْتُ إِلَى الْبَيْتِ |
Row 2: | التَّنْوِينُ | كِتَابًا ، قَلَمًا |
Row 3: | النِّدَاءُ | يَا سَعِيدَ |
Row 4: | التَّعْرِيفُ ب ( الَ ) | الْفَصْلَ |
Row 5: | التَّاءُ الْمَرْبُوطَةُ ( ة ) | حَديقَةُ |

=== BLOCK 5: أَوْلًا الْعَلَاَّمَاتُ النَّحْوِيَّةُ لِلْاِسْمَ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَوْلًا الْعَلَاَّمَاتُ النَّحْوِيَّةُ لِلْاِسْمَ
Content:
<p>إِذَا قَبِلَتْ الْكَلِمَةَ إحْدَى هَذِه الْعَلَاَّمَاتِ الْخُمُسَ ، فهِي <strong>اِسْمَ</strong> بِلَا شَكٍّ.</p>
(Inject TEMPLATE_C_LIST.html here)
List Items:
1. <strong>الْجَرُّ :</strong> أَنّ تَقَبُّلِ الْكَلِمَةِ دُخُولَ حَرْفِ الْجَرِّ عَلَيْهَا. مِثَالَ : ذَهَبْتُ إِلَى <span class="highlight-red">الْبَيْتِ</span>. ( كَلِمَةَ " الْبَيْتَ " اِسْمٌ لأَنّهَا سَبَّقَتْ بِحَرْفِ جَرِّ ).
2. <strong>التَّنْوِينُ :</strong> أَيَّ كَلِمَةِ تَقَبُّلِ التَّنْوِينِ ( ً ٍ ٌ ) هِي اِسْمٍ. أَمِثْلَةَ : اِشْتَرَيْتُ <span class="highlight-red">كِتَابًا</span>، أَو <span class="highlight-red">قَلَمًا</span>.
3. <strong>النِّدَاءُ :</strong> الْكَلِمَاتُ الَّتِي يُصْحِ نِدَاءَهَا هِي أَسْمَاءٍ. أَمِثْلَةَ : يَا <span class="highlight-red">سَعِيدَ</span>، يَا <span class="highlight-red">هِنْدَ</span>، يَا <span class="highlight-red">سَارَّةَ</span>.
4. <strong>التَّعْرِيفُ ب ( الَ ):</strong> أَيَّ كَلِمَةٍ تَبْدَأُ بِأدَاةِ التَّعْرِيفِ ( الَ ) أَو تَقْبَلُ دُخُولَهَا. أَمِثْلَةَ : فَصِلْ <span class="highlight-red">الْفَصْلَ</span>، كِتَابَ <span class="highlight-red">الْكِتَابَ</span>.
5. <strong>التَّاءُ الْمَرْبُوطَةُ ( ة ):</strong> الْكَلِمَةَ الَّتِي تَنْتَهِي بِتَاءِ مَرْبُوطَةِ هِي مِن الْأَسْمَاءِ دُون تَفْكِيرٍ. أَمِثْلَةَ : <span class="highlight-red">حَديقَةُ</span>، <span class="highlight-red">شَجَرَةَ</span>.

=== BLOCK 6: ثَانِيًا الْمُعَنَّى وَالدَّلَالَةُ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ثَانِيًا الْمُعَنَّى وَالدَّلَالَةُ ( الطَّرِيقَةَ الْعَمَلِيَّةَ لِمَعْرِفَةَ الْاِسْمِ )
Content:
<p>يُمْكِنُنَا أيضاً تَمْييزَ الْأَسْمَاءِ مِن خِلَال دَلَالَتِهَا فِي الْحَيَاةِ ، فَالْاِسْمَ يَشْمَلُ كُلّ مَا يُشِيرُ إِلَى</p>
(Inject TEMPLATE_C_LIST.html here)
List Items:
- <strong>الْإِنْسَانَ :</strong> أَيَّ اِسْمٍ لِذِكْرٍ أَو أُنْثَى
- <strong>الْحَيَوَانَ وَالطُّيُورَ وَالْحَشَرَاتِ :</strong> مِثْل ( <span class="highlight-green">عَصْفُورٌ</span> ، <span class="highlight-green">طَائِرٌ</span> ، <span class="highlight-green">فَرَاشَةَ</span> ).
- <strong>النَّبَاتَاتِ :</strong> مِثْل ( <span class="highlight-green">شَجَرَةً</span> ، <span class="highlight-green">زَهْرَةً</span> ، <span class="highlight-green">فَوَاكِهَ</span> ، <span class="highlight-green">خُضْرُوَاتُ</span> ).
- <strong>الْجَمَادَاتِ :</strong> الْأَشْيَاءُ الَّتِي لَا حَيَاةٍ فِيهَا ( <span class="highlight-green">حَجَرٌ</span> ، <span class="highlight-green">قَلَمَ</span> ).
- <strong>الصَّفَّاتِ :</strong> مِثْل ( <span class="highlight-green">طَوِيلٌ</span> ، <span class="highlight-green">قَصِيرٌ</span> ، <span class="highlight-green">كَرِيمٌ</span> ، <span class="highlight-green">بِخَيْلِ</span> ).
- <strong>الْمُصَادَرَ ( الْأَحْدَاثَ الْمُجَرَّدَةَ مِن الزَّمَنِ ):</strong> مِثْل ( <span class="highlight-green">خُرُوجٌ</span> ، <span class="highlight-green">إعْلَاَنٌ</span> ، <span class="highlight-green">زِيَارَةَ</span> ).

=== BLOCK 7: ثَالِثًا أَسَمَاءُ مَبْنِيَّةُ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ثَالِثًا أَسَمَاءُ مَبْنِيَّةُ ( أَنْوَاعَ خَاصَّةٍ مِن الْأَسْمَاءِ )
Content:
<p>هُنَاك كَلِمَاتٍ فِي اللُّغَةَ الْعَرَبِيَّةَ هِي مِن الْأَسْمَاءِ بِالرَّغْمِ مِن أَنّهَا لَا تَتَغَيَّرُ حَرَكَتُهَا ، مِثْل:</p>
(Inject TEMPLATE_C_LIST.html here with TEMPLATE_C_CHIPS.html inside the list items)
List Items:
- <strong>أَسَمَاءَ الْإشَارَةِ :</strong> (Inject TEMPLATE_C_CHIPS.html: هَذَا ، هَذِه ، هَذَان ، هَاتَان ، هَؤُلَاء)
- <strong>الْأَسْمَاءَ الْمَوْصُولَةَ :</strong> (Inject TEMPLATE_C_CHIPS.html: الَّذِي ، الَّتِي ، الْلَذَان ، الْلَتَان ، الَّذِين ، الْلَاتِي ، الْلَائِي)
- <strong>الضَّمَائِرَ :</strong> (Inject TEMPLATE_C_CHIPS.html: هُو ، هِي ، أَنْتُم ، هُم ، نَحْن ، أَنْتُمَا)
- <strong>أَسَمَاءَ الْاِسْتِفْهَامِ :</strong> (Inject TEMPLATE_C_CHIPS.html: مَنٌّ ، مَاذَا ، لِمَاذَا ، مَتَى ، أَيْن ، كَيْف)

=== BLOCK 8: Exam / Exercises ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: اِسْتَخْرَجَ الْأَسْمَاءُ مِن بَيْن الْكَلِمَاتِ التَّالِيَةِ وَضَعَ خَطًّا تَحْتهَا : ( مُعَلِّمًا - إِلَى - شَجَرَةً - كَيْف - كَتَبٍّ - هَذِه )

Number: ٢
Question: اُذْكُرْ عُلَّامَةَ الْاِسْمِ فِي الْكَلِمَاتِ الْمُلَوَّنَةِ فِي الْجَمَلِ التَّالِيَةِ : ١. ذَهَبْتُ إِلَى الْحَديقَةِ الْعَظِيمَةَ . ٢. يَا طَالِبُ الْعِلْمِ . ٣. رَأَيْتُ عَصْفُورًا يَطِيرُ . ٤. الْقَلَمُ جَدِيدٌ .

Number: ٣
Question: صَنَّفَ الْأَسْمَاءُ التَّالِيَةُ حَسْب دَلَالَتِهَا ( إِنْسَانٌ ، حَيَوَانَ / طَيْرٌ ، نَبَاتٌ ، جَمَادٌ ، صَفَّةً ، مَصْدَرٌ ، اِسْمَ إشَارَةٍ ، ضَمِيرٌ ، اِسْمَ اِسْتِفْهَامِ ) : ١. هِنْدٌ ٢. خُرُوجٌ ٣. طَوِيلٌ ٤. نَحْن ٥. مَاذَا ٦. هَؤُلَاء ٧. فَرَاشَةٌ

--- END STREAM ---