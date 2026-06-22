# **SESSION 27.0**

[TASK DEFINITION]
Objective: Implement المحسنات البديعية.
File: `pages/27.0_nXX_المحسنات البديعية.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/27.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 27
[CHAPTER_TITLE]: المحسنات البديعية
[CATEGORY_HEADER]: فوائد
[SECTION_HEADER]: المستوى الفني
[AUTHOR_NAME]: أ. حنا خفيف
[AUTHOR_PHONE]:  

=== BLOCK 2: Introduction ===
(Component: TEMPLATE_C_BLOCK)
Title: المُحَسِّناتُ البديعيَّةُ (عِلمُ البَديعِ)
Content: <p class="text-accent text-right">تُقسَمُ المُحسِّناتُ البديعيَّةُ قِسمينِ: مُحسِّناتٌ لفظيَّةٌ، ومُحسِّناتٌ معنويَّةٌ.</p>
[BENEFIT_TITLE]: فَائِدَةُ الْجِنَاسِ وَوَظِيفَتُهُ (أَثَرُهُ الْفَنِّيُّ)
[BENEFIT_TEXT]: يضفي على الكلامِ رونقًا وعذوبةً، ويمنحُه إيقاعًا موسيقيًّا، فهو منبعٌ من منابعِ الموسيقا الدّاخليَّةِ.

=== BLOCK 3: The Core Matrix (Summary Table) ===
(Component: TEMPLATE_C_TABLE)
Title: جَدْوَلُ خُلَاصَةِ الْمُحَسِّنَاتِ الْبَدِيعِيَّةِ
[TABLE_HEADERS]: <th>الْمُحَسِّنُ</th><th>التَّعْرِيفُ الْمُوجَزُ</th><th>مِثَالٌ تَوْضِيحِيٌّ</th>
[TABLE_ROWS]:
<tr>
  <td class="font-bold text-primary">الْجِنَاسُ التَّامُّ</td>
  <td>تَطَابُقُ اللَّفْظَيْنِ فِي نَوْعِ الْحُرُوفِ، وَعَدَدِهَا، وَهَيْئَتِهَا، وَتَرْتِيبِهَا مَعَ اخْتِلَافِ الْمَعْنَى.</td>
  <td>(حَيِّهِمْ مَا دُمْتَ فِي حَيِّهِمْ).</td>
</tr>
<tr>
  <td class="font-bold text-primary">الْجِنَاسُ النَّاقِصُ</td>
  <td>اخْتِلَافُ اللَّفْظَيْنِ فِي وَاحِدٍ مِنَ الْأُمُورِ الْأَرْبَعَةِ (النَّوْعِ، الْعَدَدِ، الْهَيْئَةِ، التَّرْتِيبِ).</td>
  <td>(ظَالِم، عَالِم)، (سَاق، مَسَاق)، (خَلْقِي، خُلُقِي)، (فَتْح، حَتْف).</td>
</tr>
<tr>
  <td class="font-bold text-primary">التَّصْرِيعُ</td>
  <td>تَطَابُقُ الْعَرُوضِ وَالضَّرْبِ وَزْنًا وَتَقْفِيَةً وَإِعْرَابًا (غَالِبًا فِي الْبَيْتِ الْأَوَّلِ).</td>
  <td>ذَخَرْتُ لِأَحْدَاثِ الزَّمَانِ يَرَاعَا ... يُجِيدُ نِضَالًا دُونَهَا وَقِرَاعَا</td>
</tr>
<tr>
  <td class="font-bold text-primary">السَّجْعُ</td>
  <td>تَوَافُقُ الْحُرُوفِ الْأَخِيرَةِ فِي نِهَايَاتِ الْجُمَلِ (فِي النَّثْرِ).</td>
  <td>إِنَّ حِفْظَ الْعَرَبِ لُغَتَهُمْ حِفْظُهُم، وَإِنَّ أَضَاعُوهَا أَضَاعَتْهُمْ.</td>
</tr>
<tr>
  <td class="font-bold text-primary">التَّوَازُنُ</td>
  <td>اتِّفَاقُ الْكَلِمَتَيْنِ فِي الْوَزْنِ فِي أَوَاخِرِ الْفِقْرَتَيْنِ (دُونَ التَّقْفِيَةِ ضَرُورَةً).</td>
  <td>((اللَّهُمَّ أَعْطِ مُنْفِقًا خَلَفًا، وَأعْطِ مُمْسِكًا تَلَفًا)).</td>
</tr>
<tr>
  <td class="font-bold text-primary">الطِّبَاقُ (الْإِيجَابُ)</td>
  <td>الْجَمْعُ بَيْنَ لَفْظَيْنِ مُتَضَادَّيْنِ وَكُلٌّ مِنْهُمَا مُثْبَتٌ.</td>
  <td>(نَاجِح، رَاسِب).</td>
</tr>
<tr>
  <td class="font-bold text-primary">الطِّبَاقُ (السَّلْبُ)</td>
  <td>الْجَمْعُ بَيْنَ الْكَلِمَةِ وَنَفْيِهَا، أَو الْأَمْرِ وَالنَّهْيِ.</td>
  <td>(يَرَى، لَمْ يَرَ)، (اقْرَأ، لَا تَقْرَأ).</td>
</tr>
<tr>
  <td class="font-bold text-primary">الْمُقَابَلَةُ</td>
  <td>الْإِتْيَانُ بِمَعْنَيَيْنِ أَو أَكْثَرَ ثُمَّ مَا يُضَادُّهَا عَلَى التَّرْتِيبِ.</td>
  <td>فَتًى تَمَّ فِيهِ مَا يَسُرُّ صَدِيقَهُ ... عَلَى أَنَّ فِيهِ مَا يَسُوءُ الْأَعَادِيَا</td>
</tr>

=== BLOCK 4: Jinas Types (Conditions of Naqis) ===
(Component: TEMPLATE_C_BLOCK)
Title: أَوْجُهُ الِاخْتِلَافِ فِي الْجِنَاسِ النَّاقِصِ
Content: <p class="text-accent text-right">يَكُونُ الْجِنَاسُ نَاقِصًا عِنْدَمَا يَخْتَلِفُ اللَّفْظَانِ الْمُتَجَانِسَانِ فِي وَاحِدٍ مِنَ الْوُجُوهِ الْأَرْبَعَةِ، عَلَى النَّحْوِ الْآتِي:</p>

=== BLOCK 5: Conditions Chips ===
(Component: TEMPLATE_C_CHIPS)
Title: شُرُوطُ الْجِنَاسِ النَّاقِصِ
[CHIP_ITEMS]:
<div class="bg-grey-lighter p-2mm rounded text-center">نَوْعُ الْحُرُوفِ</div>
<div class="bg-grey-lighter p-2mm rounded text-center">عَدَدُ الْحُرُوفِ</div>
<div class="bg-grey-lighter p-2mm rounded text-center">هَيْئَةُ الْحُرُوفِ (الضَّبْطُ)</div>
<div class="bg-grey-lighter p-2mm rounded text-center">تَرْتِيبُ الْحُرُوفِ</div>

=== BLOCK 6: Semantic Enhancements (Definitions) ===
(Component: TEMPLATE_C_BLOCK)
Title: الْمُحَسِّنَاتُ الْبَدِيعِيَّةُ الْمَعْنَوِيَّةُ
Content: <p class="text-accent mb-2mm text-justify">١- الطِّبَاقُ (الْمُطَابَقَةُ): مُحسِّنٌ معنويٌّ، يجمعُ بين لفظينِ مُتضادَّينِ في المعنى، فيولِّدُ حركةً داخليَّةً في النَّفسِ تُبرِزُ الفارقَ بينهما.</p>
<p class="text-accent mb-2mm text-justify">٢- الْمُقَابَلَةُ: مُحسِّنٌ معنويٌّ، وهو أنْ يُؤتى بمعنينِ متوافقينِ، أو عدَّةِ معانٍ مُتوافِقةٍ، ثم يُؤتَى بضِدِّها على ترتيبِها. (هي الجمعُ بين طِباقينِ، فأكثر في الكلامِ على الترتيبِ).</p>

=== BLOCK 7: Aesthetic Values (List) ===
(Component: TEMPLATE_C_LIST)
[LIST_TITLE]: الْقِيَمُ الْجَمَالِيَّةُ وَالْمَعْنَوِيَّةُ لِلطِّبَاقِ وَالْمُقَابَلَةِ (أَثَرُهُمَا الْفَنِّيُّ)
[LIST_ITEMS]:
<li><span class="font-bold text-primary">١- إِظْهَارُ الْمَعْنَى بِجَلَاءٍ وَوُضُوحٍ.</span></li>
<li><span class="font-bold text-primary">٢- إِثَارَةُ الْخَيَالِ.</span></li>
<li><span class="font-bold text-primary">٣- إِعْمَالُ الْعَقْلِ فِي الْمُتَنَاقِضَاتِ.</span></li>
<li><span class="font-bold text-primary">٤- تَحْدِيدُ الرُّؤْيَةِ (الْمَوْقِفُ).</span></li>

=== BLOCK 8: Methodology Tip ===
(Component: TEMPLATE_C_BENEFIT_TIP)
[TIP_TITLE]: كَيْفِيَّةُ الْإِجَابَةِ عَنْ سُؤَالِ الْقِيمَةِ الْفَنِّيَّةِ
[TIP_TEXT]: <p class="text-justify mb-2mm">إِذَا طُلِبَ مِنَ الطَّالِبِ تَوْضِيحُ الْقِيَمِ الْجَمَالِيَّةِ وَالْمَعْنَوِيَّةِ لِلطِّبَاقِ وَالْمُقَابَلَةِ بِمَقْدُورِ الطَّالِبِ إِيضَاحُهَا عَلَى النَّحْوِ الْآتِي:</p>
<p class="mb-1mm"><strong>– إِظْهَارُ الْمَعْنَى بِجَلَاءٍ وَوُضُوحٍ:</strong> أَوْضَحَ الشَّاعِرُ مِنْ خِلَالِ هَذَا الطِّبَاقِ، (أَوْ: هَذِهِ الْمُقَابَلَةِ)... [نَذْكُرُ هُنَا فِكْرَةَ الْبَيْتِ، أَوْ مَعْنَاهُ أَوْ دَلَالَتَهُ].</p>
<p class="mb-1mm"><strong>– إِثَارَةُ الْخَيَالِ:</strong> تَمَكَّنَ الشَّاعِرُ مِنْ خِلَالِ هَذَا الطِّبَاقِ، (أَوْ: هَذِهِ الْمُقَابَلَةِ) مِنْ إِثَارَةِ خَيَالِ الْمُتَلَقِّي وَجَعَلِهِ يَتَخَيَّلُ... [نَذْكُرُ هُنَا مَا يُمْكِنُ أَنْ يُثِيرَهُ الْمُحَسِّنُ مِنْ خَيَالٍ].</p>
<p class="mb-1mm"><strong>– إِعْمَالُ الْعَقْلِ فِي الْمُتَنَاقِضَاتِ:</strong> تَمَكَّنَ الشَّاعِرُ مِنْ خِلَالِ هَذَا الطِّبَاقِ، (أَوْ: هَذِهِ الْمُقَابَلَةِ) مِنْ إِعْمَالِ عَقْلِ الْمُتَلَقِّي فِي الْمُتَنَاقِضَاتِ فَجَعَلَهُ يُدْرِكُ الْفَرْقَ الشَّاسِعَ بَيْنَ حَالِ... [نَذْكُرُ هُنَا الطَّرَفَ الْأَوَّلَ مِنَ الْمُحَسِّنِ] وَحَالِ... [نَذْكُرُ هُنَا الطَّرَفَ الثَّانِي مِنَ الْمُحَسِّنِ].</p>
<p><strong>– تَحْدِيدُ الرُّؤْيَةِ (الْمَوْقِفِ):</strong> تَمَكَّنَ هَذَا الطِّبَاقُ، (أَوْ: هَذِهِ الْمُقَابَلَةُ) مِنَ الْكَشْفِ عَنْ مَوْقِفِ الشَّاعِرِ حَيْثُ أَظْهَرَ وُقُوفَهُ إِلَى جَانِبِ...</p>

=== BLOCK 9: Practical Application Example ===
(Component: TEMPLATE_C_POEM)
[POEM_VERSE_1]: فَتَرْفَعُ بِالْإِعْزَازِ مَنْ كَانَ جَاهِلاً ... وَتَخْفِضُ بِالْإِذْلَالِ مَنْ كَانَ يَعْقِلُ

=== BLOCK 10: Analysis List ===
(Component: TEMPLATE_C_LIST)
[LIST_TITLE]: تَحْلِيلُ الْبَيْتِ الشِّعْرِيِّ (جَمِيل صِدْقِي الزَّهَاوِي)
[LIST_ITEMS]:
<li><span class="font-bold text-primary">الْمُقَابَلَةُ:</span> (تَرْفَعُ، تَخْفِضُ - الْإِعْزَازُ، الْإِذْلَالُ - جَاهِلاً، يَعْقِلُ).</li>
<li><span class="font-bold text-primary">قِيمَتُهَا الْفَنِّيَّةُ:</span> اسْتَطَاعَ الشَّاعِرُ مِنْ خِلَالِ هَذِهِ الْمُقَابَلَةِ تَحْقِيقَ قِيَمٍ فَنِّيَّةٍ كَثِيرَةٍ مِنْهَا:</li>
<li><span class="font-bold text-primary">إِظْهَارُ الْمَعْنَى بِجَلَاءٍ وَوُضُوحٍ:</span> حَيْثُ أَوْضَحَ مِنْ خِلَالِ هَذِهِ الْمُقَابَلَةِ افْتِقَارَ الدَّوْلَةِ الْعُثْمَانِيَّةِ إِلَى الْإِنْصَافِ وَالْمَنْطِقِيَّةِ.</li>
<li><span class="font-bold text-primary">إِثَارَةُ الْخَيَالِ:</span> فَقَدْ تَمَكَّنَ الشَّاعِرُ مِنْ خِلَالِ هَذِهِ الْمُقَابَلَةِ مِنْ إِثَارَةِ خَيَالِ الْمُتَلَقِّي وَجَعَلَهُ يَتَخَيَّلُ حَالَةَ التَّخَبُّطِ وَالْهَمَجِيَّةِ الَّتِي اتَّصَفَتْ بِهَا سِيَاسَةُ الدَّوْلَةِ الْعُثْمَانِيَّةِ.</li>
<li><span class="font-bold text-primary">إِعْمَالُ الْعَقْلِ فِي الْمُتَنَاقِضَاتِ:</span> تَمَكَّنَ الشَّاعِرُ مِنْ خِلَالِ هَذِهِ الْمُقَابَلَةِ مِنْ إِعْمَالِ عَقْلِ الْمُتَلَقِّي فِي الْمُتَنَاقِضَاتِ فَجَعَلَهُ يُدْرِكُ الْفَرْقَ الشَّاسِعَ بَيْنَ حَالِ ارْتِفَاعِ شَأْنِ الْجَاهِلِ وَحَالِ انْخِفَاضِ شَأْنِ الْعَاقِلِ.</li>
<li><span class="font-bold text-primary">تَحْدِيدُ الرُّؤْيَةِ (الْمَوْقِفِ):</span> تَمَكَّنَتْ هَذِهِ الْمُقَابَلَةُ مِنَ الْكَشْفِ عَنْ مَوْقِفِ الشَّاعِرِ حَيْثُ أَظْهَرَتْ وُقُوفَهُ إِلَى جَانِبِ عُقَلَاءِ الْمُجْتَمَعِ الَّذِينَ هُضِمَتْ حُقُوقُهُمْ فِي ظِلِّ سِيَاسَةِ الدَّوْلَةِ الْعُثْمَانِيَّةِ.</li>

=== BLOCK 11: Exam Questions ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: حَدِّدِ الْبَدِيعَ فِيمَا يَأْتِي مُبَيِّنًا نَوْعَهُ، وَقِيمَتَهُ الْفَنِّيَّةَ:<br>أَنْ يَرَى فَأْرَةً فَلَمْ يَرَ شَيْئًا ... نَاكِسًا رَأْسَهُ لِطُولِ الْمَلَالَةْ<br>فَكَأَنَّ الْإِصْبَاحَ عِنْدِي لِمَا فِيـــــــهِ حَبِيبٌ رَقِيبُهُ الْإِمْسَاءُ

Number: ٢
Question: أَوْرَدَ الشَّاعِرُ الطِّبَاقَ لِإِيضَاحِ الْمَعْنَى، وَإِثَارَةِ الْخَيَالِ. مَثِّلْ لِذَلِكَ مِنَ الْمَقْطَعِ الْآتِي:<br>أَبَدًا عَلَى هَذَا الطَّرِيقِ!! ... وَنَرُدُّ حَقْلاً .. شَاخَ فِيهِ الْجِذْعُ .. فِي شَرْخِ الشَّبَابِ<br>رَايَاتُنَا بَصَرُ الضَّرِيرِ .. وَصَوْتُنَا أَمَلُ الْغَرِيقْ ... وَنَصُبُّ فِي نَبْضِ الْمَصَانِعِ..<br>أَبَدًا .. جَحِيمُ عَدُوِّنَا .. أَبَدًا .. نَعِيمٌ لِلصَّدِيقْ ... لِلْمُرَبِّي .. وَالْحَقَائِبِ.. وَالثِّيَابِ

Number: ٣
Question: اقْرَأ الْبَيْتَ الْآتِي ثُمَّ وَضِّحِ الْمُحَسِّنَ الْبَدِيعِيَّ (نَصَبٍ، وَصَبٍ):<br>يَا غَانِمًا بِالظَّنِّ لَا نَصَبٍ ... يُوهِي عَزِيمَتَهُ وَلَا وَصَبُ

Number: ٤
Question: سُؤَالُ دَوْرَةٍ (٢٠١٤): اسْتَخْرِجْ مِنَ الْبَيْتِ مُحَسِّنًا بَدِيعِيًّا، سَمِّهِ، ثُمَّ اذْكُرْ قِيمَتَهُ الْفَنِّيَّةَ:<br>وَيُوتُوبِيَا حُلْمٌ فِي دَمِي ... أَمُوتُ وَأَحْيَا عَلَى ذِكْرِهِ

--- END STREAM ---
