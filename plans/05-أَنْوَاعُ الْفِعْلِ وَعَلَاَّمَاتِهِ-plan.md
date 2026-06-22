# **SESSION 03.0**

[TASK DEFINITION]
Objective: Implement أَنْوَاعُ الْفِعْلِ وَعَلَاَّمَاتِهِ.
File: `pages/03.0_nXX_أَنْوَاعُ الْفِعْلِ وَعَلَاَّمَاتِهِ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/03.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 03
[CHAPTER_TITLE]: أَنْوَاعُ الْفِعْلِ وَعَلَاَّمَاتِهِ
[CATEGORY_HEADER]:
[SECTION_HEADER]:
[AUTHOR_NAME]: أ. حنا خفيف
[AUTHOR_PHONE]:  

=== BLOCK 2: [Topic] ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مُقَدَّمَةً
Content:
<p class="text-accent">الْفِعْلُ فِي اللُّغَةَ الْعَرَبِيَّةَ هُو : <strong>حَدَثَ مُقْتَرِنٌ بِزَمَنِ</strong>.</p>
<p>أي أَنّهُ يَدُلُّ عَلَى عَمَلٍ أَو حَرَكَةُ (الْحَدَثَ) حَصَّلَتْ فِي وَقْتِ مُعَيَّنِ (الزَّمَنَ).</p>

=== BLOCK 3: [Topic Details] ===
(Component: TEMPLATE_C_BENEFIT.html)
Title: أَقْسَامُ الْفِعْلِ
Content:
<p>وَيَنْقَسِمُ الْفِعْلُ فِي اللُّغَةَ الْعَرَبِيَّةَ إِلَى ثَلَاثَةِ أَقْسَامِ رَئِيسِيَّةِ حَسْب الزَّمَنِ:</p>
(Component: TEMPLATE_C_CHIPS.html)
- الْمَاضِي
- الْمُضَارِعَ
- الْأَمْرَ

=== BLOCK 4: [Topic] ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ١. الْفِعْلِ الْمَاضِي
Content:
<p class="text-accent"><strong>التَّعْرِيفَ:</strong> هُو مَا دَلٍّ عَلَى حَدَثِ وَقْعٍ وَاِنْتَهَى <strong>قَبْل</strong> زَمَانَ التَّكَلُّمِ (أَيَّ قَبْل أَنّ أَتَحَدُّثٌ عَنهُ).</p>
<p><strong>أَمِثْلَةَ:</strong> <span class="highlight-green">دَخَلَ</span> ، <span class="highlight-green">خَرَجَ</span> ، <span class="highlight-green">فَهِمَ</span>.</p>

=== BLOCK 5: [Topic Details List] ===
(Component: TEMPLATE_C_LIST.html)
Title: عَلَاَّمَاتِ الْفِعْلِ الْمَاضِي
Content:
<p>كَيْف أَتَأَكُّدٌ أَنّ هَذَا الْفِعْلُ مَاضٍ؟ إِذَا قَبْل إحْدَى الْعَلَاَّمَاتِ التَّالِيَةِ فِي آخِرِهِ:</p>
Items:
1. <strong>تَاءُ التَّأْنِيثِ السَّاكِنَةَ (تْ):</strong> مِثْل (سَمِعَ<span class="highlight-red">تْ</span>، قَرَأَ<span class="highlight-red">تْ</span>، خَرَجَ<span class="highlight-red">تْ</span>، قَالَتْ).
2. <strong>تَاءُ الْفَاعِلِ الْمُتَحَرِّكَةِ (تُ، تَ، تِ):</strong> مِثْل (كَتَبْ<span class="highlight-red">تُ</span> لِلْمُتَكَلِّمَ، كَتَبْ<span class="highlight-red">تَ</span> لِلْمُخَاطِبَ، كَتَبْ<span class="highlight-red">تِ</span> لِلْمُخَاطَبَةَ الْمُؤَنَّثَةَ).
3. <strong>نُونُ النِّسْوَةِ (نَ):</strong> مِثْل (الطَّالِبَاتُ فَهِمْ<span class="highlight-red">نَ</span> الشَّرْحَ).
4. <strong>دُخُولُ (قَدْ) قِبَلَهُ:</strong> مِثْل الْمِثَالِ: "<span class="highlight-blue">قَدْ</span> أَفْلَحَ الْمُجْتَهِدُونَ".

=== BLOCK 6: [Note] ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Title: مُلَاحِظَةً
Content:
<p>نُونُ النِّسْوَةِ تَدْخُلُ عَلَى جَمِيعِ الْأَفْعَالِ.</p>

=== BLOCK 7: [Topic] ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٢. الْفِعْلُ الْمُضَارِعُ
Content:
<p class="text-accent"><strong>التَّعْرِيفَ:</strong> هُو مَا دَلٍّ عَلَى حَدَثٍ يَقُعُّ <strong>فِي زَمَانِ التَّكَلُّمِ</strong> (الْآن) أَو <strong>بَعْدهُ</strong> (فِي الْمُسْتَقْبَلِ).</p>
<p><strong>أَمِثْلَةَ:</strong> <span class="highlight-green">يَقْرَأُ</span> ، <span class="highlight-green">يَسْمَعُ</span> ، <span class="highlight-green">يَكْتُبُ</span>.</p>

=== BLOCK 8: [Topic Details List] ===
(Component: TEMPLATE_C_LIST.html)
Title: عَلَاَّمَاتِ الْفِعْلِ الْمُضَارِعِ
Content:
<p>يَتَمَيَّزُ الْفِعْلُ الْمُضَارِعُ بِعَلَاَّمَاتِ خَاصَّةٍ لَا تَدَخُّلٍ عَلَى غَيْرهُ:</p>
Items:
1. <strong>دُخُولُ (السِّينَ) أَو (سَوْف) قِبَلَهُ:</strong> مِثْل (<span class="highlight-blue">سَ</span>أُذَاكِرُ دُرُوسَي، <span class="highlight-blue">سَوْف</span> أُذَاكِرُ دُرُوسَي).
2. <strong>دُخُولُ (لَم) و(لَن) قِبَلَهُ:</strong> مِثْل (<span class="highlight-blue">لَم</span> أُهْمِلْ دُرُوسَي، <span class="highlight-blue">لَن</span> أُهْمِلَ دُرُوسَي).
3. <strong>دُخُولُ (قَدْ) قِبَلَهُ:</strong> (تَدُلُّ هُنَا إِمَّا عَلَى التَّقْليلِ مِثْل: <span class="highlight-blue">قَد</span> يَنْجَحُ الْكَسُولُ، أَو عَلَى التَّكْثيرِ مِثْل: <span class="highlight-blue">قَد</span> يَنْجَحُ الْمُجْتَهِدُ).
4. <strong>الْبَدْءُ بِحُروفِ الْمُضَارِعَةِ (أ، ن، ي، ت):</strong> وَيَجْمَعُهَا كَلِمَةُ (أَنِيتُ) أَو (نَأْتِي).
   <p><strong>أَمِثْلَةَ:</strong> <span class="highlight-red">أَ</span>حْفَظُ، <span class="highlight-red">نَ</span>حْفَظُ، <span class="highlight-red">يَ</span>حْفَظُ، <span class="highlight-red">تَ</span>حْفَظُ.</p>

=== BLOCK 9: [Note] ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Title: تَنْبِيه
Content:
<p>هَمْزَةُ الْفِعْلِ الْمُضَارِعِ تَكَوَّنَ دَائِمَا هَمْزَةِ قَطْعِ.</p>

=== BLOCK 10: [Topic] ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٣. فعَلّ الْأَمْرِ
Content:
<p class="text-accent"><strong>التَّعْرِيفَ:</strong> هُو مَا دَلٍّ عَلَى حَدَثِ <strong>يُطْلَبُ</strong> حُدوثَهُ <strong>بَعْد</strong> زَمَانَ التَّكَلُّمِ.</p>
<p><strong>أَمِثْلَةَ:</strong> <span class="highlight-green">اِسْمَعْ</span> ، <span class="highlight-green">اُكْتُبْ</span> ، <span class="highlight-green">أَغْلِقْ</span>.</p>

=== BLOCK 11: [Topic Details List] ===
(Component: TEMPLATE_C_LIST.html)
Title: عَلَاَّمَاتٍ فعَلّ الْأَمْرِ
Content:
<p>لَهَّ عَلَاَمَتَانِ يَجِبُ أَن تَجْتَمِعَا فِيهِ:</p>
Items:
1. <strong>دَلَالَتُهُ عَلَى الطَّلَبِ بِصِيغَتِهِ:</strong> مِثْل (<span class="highlight-red">اِحْفَظْ</span>، <span class="highlight-red">اِفْهَمْ</span>).
2. <strong>قَبُولُهُ ياء الْمُخَاطَبَةَ:</strong> مِثْل (اِحْفَظِ<span class="highlight-red">ي</span>، اِفْهَمِ<span class="highlight-red">ي</span>).

=== BLOCK 12: [Warning] ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: تَنْبِيهَاتِ هَامَةِ
Content:
(Component: TEMPLATE_C_LIST.html) (nested or injected visually)
Items:
- إِذَا دَلَّتْ الْكَلِمَةَ عَلَى الطَّلَبِ ولَكِنّهَا <strong>لَم تَقْبَلُ ياء الْمُخَاطَبَةَ</strong>، فهِي (اِسْمٌ فعَلّ أَمْرِ) مِثْل: <span class="highlight-blue">صَهْ</span> (بِمُعَنَّى اسكت).
- إِذَا قَبِلَتْ الْكَلِمَةَ ياء الْمُخَاطَبَةَ ولَكِنّهَا <strong>لَم تَدُلُّ عَلَى الطَّلَبِ</strong>، فهِي فعَلّ مُضَارِعِ مِثْل: <span class="highlight-green">تُذَاكِرِينَ</span>.

=== BLOCK 13: [Note] ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Title: مُلَاحِظَةً: دَلَالَاتٍ بَلَاغِيَّةٍ لِفِعْلَ الْأَمْرِ حَسْب الرُّتْبَةِ
Content:
(Component: TEMPLATE_C_LIST.html) (nested or injected visually)
Items:
- مِن الْاِبْنِ لأَبِيهُ: يُسَمَّى <strong>رَجَاءً</strong> (مِثْل: يَا أبِي <span class="highlight-green">سَامِحْنِِي</span>).
- مِن الْمُعَلِّمِ لِلتِّلْميذَ: يُسَمَّى <strong>أَمْرًا</strong> (مِثْل: <span class="highlight-green">اِقْرَأْ</span> دَرَسَكَ).
- بَيْن المتساويين (مِن شَخْصٍ لِصَدِيقَهُ): يُسَمَّى <strong>طَلَبًا</strong> أَو اِلْتِمَاسَا (مِثْل: يَا صَدِيقِي <span class="highlight-green">اِسْمَعْ</span> كِلَاَمَي).

=== BLOCK 14: [Summary Matrix] ===
(Component: TEMPLATE_C_TABLE.html)
Title: مُلَخَّصُ أَنْوَاعِ الْفِعْلِ وَعَلَامَاتِهِ
Content:
| نَوْعُ الْفِعْلِ | الزَّمَنُ | أَهَمُّ الْعَلَامَاتِ | مِثَالٌ |
|---|---|---|---|
| الْمَاضِي | قَبْلَ زَمَانِ التَّكَلُّمِ | تَاءُ التَّأْنِيثِ، تَاءُ الْفَاعِلِ، نُونُ النِّسْوَةِ | كَتَبَتْ، كَتَبْتُ |
| الْمُضَارِعُ | فِي زَمَانِ التَّكَلُّمِ أَو بَعْدَهُ | السِّينُ، سَوْفَ، لَمْ، لَنْ، قَدْ، أَنِيتُ | سَيَكْتُبُ، يَكْتُبُ |
| الْأَمْرُ | بَعْدَ زَمَانِ التَّكَلُّمِ | دَلَالَتُهُ عَلَى الطَّلَبِ، قَبُولُ ياء الْمُخَاطَبَةَ | اُكْتُبْ، اُكْتُبِي |

=== BLOCK 15: Exam Part 1 ===
(Component: TEMPLATE_C_EXAM.html)
Title: تَدْرِيبَاتٍ وَتَطْبِيقَاتٍ عَمَلِيَّةٍ (مُسْتَخْرَجَةً مِن الدَّرْسِ)
Number: ١
Question: اِسْتَخْرَجَ الْأَفْعَالُ مِن بَيْن الْكَلِمَاتِ التَّالِيَةِ ، وَحَدَّدَ نَوْعُهَا (مَاضٍ ، مُضَارِعٌ ، أَمْرَ): (تَقَدَّمَ - تَعَلَّمْ - أَكْتُبُ)

=== BLOCK 16: Exam Part 2 ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: ضَعْ عُلَّامَةَ (صَحَّ) أَو (خَطَأَ) مَع تَصْحِيحِ الْخَطَأِ:
١. كَلِمَةُ "تُذَاكِرِينَ" هِي فعَلّ أَمْرٍ لأَنّهَا تَقَبُّلَ ياء الْمُخَاطَبَةَ.
٢. تَاءُ الْفَاعِلِ الْمُتَحَرِّكَةِ لَا تَتَّصِلُ إِلَّا بِالْفِعْلِ الْمَاضِي.
٣. إِذَا سَبَقَ الْفِعْلُ ب (سَوْف) فهُو فعَلّ مَاضٍ يَدُلُّ عَلَى الْمُسْتَقْبَلِ.
٤. فعَلّ الْأَمْرِ يَجِبُ أَن يَجْمَعُ بَيْن الدَّلَالَةِ عَلَى الطَّلَبِ وَقَبُولِ ياء الْمُخَاطَبَةَ.

=== BLOCK 17: Exam Part 3 ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٣
Question: صَنَّفَ الْأَفْعَالُ فِي الْجَمَلِ التَّالِيَةِ حَسْب نَوْعِهَا (مَاضٍ ، مُضَارِعٌ ، أَمْرَ):
١. قَالَتْ سَارَّةُ الْحَقِّ.
٢. لَمْ أُهْمِلْ وَاجِبِيٌّ.
٣. يَا طَالِبَةُ اِجْتَهِدِي.
٤. قَدْ أَفْلَحَ الْمُجْتَهِدُونَ.
٥. سَوْفَ نُسَافِرُ غَدًا.

--- END STREAM ---
