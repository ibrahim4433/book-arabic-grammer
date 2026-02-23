# **SESSION 29.0**

[TASK DEFINITION]
Objective: Implement وظائف عناصر المستوى التركيبي.
File: `pages/29.0_nXX_وظائف_عناصر_المستوى_التركيبي.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/29.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 29
[CHAPTER_TITLE]: وظائف عناصر المستوى التركيبي
[CATEGORY_HEADER]: فوائد
[SECTION_HEADER]: المستوى الفني
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition of Nominal Sentence Function ===
(Component: TEMPLATE_C_BLOCK)
Title: وَظِيفَةُ الْجُمْلَةِ الْاسْمِيَّةِ
Content: <p class="text-accent text-justify">تَدُلُّ الْجُمْلَةُ الْاسْمِيَّةُ عَلَى <span class="highlight-red">الثَّبَاتِ وَالِاسْتِقْرَارِ وَالدَّيْمُومَةِ</span>؛ وَذَلِكَ مِنْ جِهَةِ ثَبَاتِ الْحَالِ، وَثَبَاتِ الْمَوْقِفِ، وَدَيْمُومَةِ الصِّفَةِ، وَاسْتِقْرَارِ الْعَاطِفَةِ. وَيَنْبَغِي لِلطَّالِبِ أَنْ يَعِيَ أَنَّ الْجُمْلَةَ الْاسْمِيَّةَ كُلُّ جُمْلَةٍ تَبْدَأُ بِمُبْتَدَأٍ (سَوَاءٌ أَكَانَ اسْمًا أَمْ ضَمِيرًا)، أَوْ تَبْدَأُ بِحَرْفٍ مُشَبَّهٍ بِالْفِعْلِ. وَتَبْقَى هَذِهِ الْجُمْلَةُ اسْمِيَّةً سَوَاءٌ أَكَانَ خَبَرُهَا مُفْرَدًا (اسْمًا)، أَوْ جُمْلَةً فِعْلِيَّةً أَوْ جُمْلَةً اسْمِيَّةً.</p>

=== BLOCK 3: Methodology Tip ===
(Component: TEMPLATE_C_BENEFIT_TIP)
[BENEFIT_TITLE]: كَيْفِيَّةُ الْإِجَابَةِ
[BENEFIT_TEXT]: بِمَقْدُورِ الطَّالِبِ اعْتِمَادُ الْقَالِبِ النَّظَرِيِّ الْآتِي فِي إِجَابَتِهِ، حِينَمَا يُسْأَلُ عَنْ دَوْرِ اسْتِعْمَالِ الْجُمْلَةِ الْاسْمِيَّةِ فِي خِدْمَةِ الْمَعْنَى. يَنْبَغِي لِلطَّالِبِ أَنْ يُشِيرَ فِي إِجَابَتِهِ إِلَى الْمَعَانِي الَّتِي أَرَادَ الشَّاعِرُ أَنْ يُؤَكِّدَ ثَبَاتَهَا وَاسْتِقْرَارَهَا وَدَيْمُومَتَهَا مِنْ خِلَالِ اسْتِعْمَالِ الْجُمْلَةِ الْاسْمِيَّةِ، أَيْ؛ يَجِبُ رَبْطُ الثَّبَاتِ وَالِاسْتِقْرَارِ وَالدَّيْمُومَةِ بِالْمَعْنَى.

=== BLOCK 4: Template Answer Model ===
(Component: TEMPLATE_C_BLOCK)
Title: الْقَالِبُ النَّظَرِيُّ لِلْإِجَابَةِ
Content: <p class="text-justify mb-2mm">حَاوَلَ الشَّاعِرُ مِنْ خِلَالِ اسْتِعْمَالِ الْجُمْلَةِ الْاسْمِيَّةِ أَنْ يَعْرِضَ الْمَعَانِيَ بِصُورَةِ <span class="highlight-red">الثَّبَاتِ وَالِاسْتِقْرَارِ وَالدَّيْمُومَةِ</span>. فَهَذَا الِاسْتِعْمَالُ مَكَّنَهُ مِنَ الْإِشَارَةِ إِلَى ثَبَاتِ .... [ نَذْكُرُ هُنَا الْمَعْنَى أَوِ الْمَعَانِي الَّتِي دَلَّتْ عَلَيْهَا الْجُمْلَةُ الْاسْمِيَّةُ] .... .</p><p class="text-justify">وَبِمَقْدُورِ الطَّالِبِ أَنْ يُشِيرَ إِلَى ثَبَاتِ الشُّعُورِ الْعَاطِفِيِّ، فَيَقُولُ: .....، كَمَا أَسْهَمَتِ الْجُمْلَةُ الْاسْمِيَّةُ، بِالتَّأْكِيدِ عَلَى ثَبَاتِ الْعَاطِفَةِ، فَ..... [نَذْكُرُ هُنَا الشُّعُورَ الْعَاطِفِيَّ] .... ثَابِتٌ دَائِمٌ لَا يَتَبَدَّلُ.</p>

=== BLOCK 5: Applied Example 1 (Al-Zahawi) ===
(Component: TEMPLATE_C_SPLIT)
Title: الْمِثَالُ التَّطْبِيقِيُّ الْأَوَّلُ
[LEFT_CONTENT]: (Component: TEMPLATE_C_POEM)
[POET_NAME]: جَمِيل صِدْقِي الزَّهَاوِي
[POEM_VERSES]: <div class="poem-line"><span class="hemistich">لَهُمْ أَثَرٌ لِلْجَوْرِ فِي كُلِّ بَلْدَةٍ</span><span class="hemistich">يُمَثِّلُ مِنْ أَطْمَاعِهِمْ مَا يُمَثِّلُ</span></div>
[RIGHT_CONTENT]: (Component: TEMPLATE_C_BLOCK)
Title: التَّحْلِيلُ وَالْإِجَابَةُ
Content: <p class="text-justify mb-2mm"><strong>تَحْدِيدُ الْجُمْلَةِ الْاسْمِيَّةِ:</strong> <span class="highlight-blue">(لَهُمْ أَثَرٌ لِلْجَوْرِ)</span>.</p><p class="text-justify"><strong>أَثَرُهَا فِي خِدْمَةِ الْمَعْنَى:</strong> حَاوَلَ الشَّاعِرُ مِنْ خِلَالِ اسْتِعْمَالِ الْجُمْلَةِ الْاسْمِيَّةِ أَنْ يَعْرِضَ الْمَعْنَى بِصُورَةِ الثَّبَاتِ وَالِاسْتِقْرَارِ وَالدَّيْمُومَةِ. فَهَذَا الِاسْتِعْمَالُ مَكَّنَهُ مِنَ الْإِشَارَةِ إِلَى <span class="highlight-red">ثَبَاتِ ظُلْمِ الْعُثْمَانِيِّينَ وَاسْتِقْرَارِهِ</span>، فَالظُّلْمُ صِفَةٌ دَائِمَةٌ مُلَازِمَةٌ لَهُمْ لَا تَمَّحِي عَنْهُمْ عَبْرَ الزَّمَنِ.</p>

=== BLOCK 6: Applied Example 2 (George Saydah) ===
(Component: TEMPLATE_C_SPLIT)
Title: الْمِثَالُ التَّطْبِيقِيُّ الثَّانِي
[LEFT_CONTENT]: (Component: TEMPLATE_C_POEM)
[POET_NAME]: جُورْج صَيْدَح
[POEM_VERSES]: <div class="poem-line"><span class="hemistich">فِيهِ رَبْعِي، فِيهِ جَنَّاتٌ جَرَتْ</span><span class="hemistich">تَحْتَهَا الْأَنْهَارُ وَالرِّزْقُ جَمَدْ</span></div><div class="poem-line"><span class="hemistich">فِيهِ مُرُّ الْعَيْشِ يَحْلُو وَأَرَى</span><span class="hemistich">فِي سِوَاهُ زُبْدَةَ الْعَيْشِ زَبَدْ</span></div><div class="poem-line"><span class="hemistich">وَطَنِي مَا زِلْتُ أَدْعُوكَ أَبِي</span><span class="hemistich">وَجِرَاحُ الْيُتْمِ فِي قَلْبِ الْوَلَدْ</span></div>
[RIGHT_CONTENT]: (Component: TEMPLATE_C_BLOCK)
Title: التَّحْلِيلُ وَالْإِجَابَةُ
Content: <p class="text-justify mb-2mm"><strong>تَحْدِيدُ الْجُمَلِ الْاسْمِيَّةِ:</strong> (فِيهِ رَبْعِي)، (فِيهِ جَنَّاتٌ)، (الرِّزْقُ جَمَدْ)، (فِيهِ مُرُّ الْعَيْشِ يَحْلُو)، (جِرَاحُ الْيُتْمِ فِي قَلْبِ الْوَلَدِ).</p><p class="text-justify"><strong>أَثَرُهَا فِي خِدْمَةِ الْمَعْنَى:</strong> حَاوَلَ الشَّاعِرُ مِنْ خِلَالِ اسْتِعْمَالِ الْجُمْلَةِ الْاسْمِيَّةِ أَنْ يَعْرِضَ الْمَعْنَى بِصُورَةِ الثَّبَاتِ وَالِاسْتِقْرَارِ وَالدَّيْمُومَةِ. فَهَذَا الِاسْتِعْمَالُ مَكَّنَهُ مِنَ الْإِشَارَةِ إِلَى <span class="highlight-red">ثَبَاتِ الْخَيْرِ وَاسْتِقْرَارِ الْجَمَالِ فِي وَطَنِهِ</span> الَّذِي يَغْدُو فِيهِ الْمُرُّ عَذْبًا سَائِغًا، وَيَسْتَحِيلُ فِيهِ كَدَرُ الْعَيْشِ صَفَاءً عَلَى الدَّوَامِ، كَذَلِكَ أَفَادَهُ هَذَا الِاسْتِعْمَالُ فِي التَّعْبِيرِ عَنْ <span class="highlight-blue">ثَبَاتِ مُعَانَاتِهِ وَدَيْمُومَةِ شَقَائِهِ</span> بِسَبَبِ الْبُعْدِ عَنْ وَطَنِهِ. كَمَا أَسْهَمَتِ الْجُمْلَةُ الْاسْمِيَّةُ، بِالتَّأْكِيدِ عَلَى ثَبَاتِ الْعَاطِفَةِ (مَشَاعِرَ الْإِعْجَابِ وَالْمَحَبَّةِ).</p>

=== BLOCK 7: Definition of Verbal Sentence Function ===
(Component: TEMPLATE_C_BLOCK)
Title: وَظِيفَةُ الْجُمْلَةِ الْفِعْلِيَّةِ
Content: <p class="text-accent text-justify">تَدُلُّ الْجُمْلَةُ الْفِعْلِيَّةُ عَلَى <span class="highlight-red">التَّغَيُّرِ وَالْحَرَكَةِ</span> فَتَبْعَثُ فِي النَّصِّ الْحَيَوِيَّةَ؛ ذَلِكَ أَنَّ أَزْمِنَةَ الْأَفْعَالِ الْمُخْتَلِفَةَ تَظْهَرُ فِي النَّصِّ سِيَاقَاتٍ زَمَنِيَّةً وَفَضَاءَاتٍ حَرَكِيَّةً مُخْتَلِفَةً، وَهَذَا يُؤَدِّي إِلَى تَبَدِّي الْحَرَكَةِ وَالتَّغَيُّرِ وَالْحَيَوِيَّةِ فِي النَّصِّ.</p>

=== BLOCK 8: Summary Matrix ===
(Component: TEMPLATE_C_TABLE)
Title: مُقَارَنَةٌ بَيْنَ وَظَائِفِ الْجُمَلِ
[TABLE_HEADERS]: <th>نَوْعُ الْجُمْلَةِ</th><th>الْوَظِيفَةُ وَالدَّلَالَةُ</th><th>الْأَثَرُ فِي الْمَعْنَى</th>
[TABLE_ROWS]: <tr><td><strong>الْجُمْلَةُ الْاسْمِيَّةُ</strong></td><td>الثَّبَاتُ، الِاسْتِقْرَارُ، الدَّيْمُومَةُ</td><td>تَأْكِيدُ صِفَةٍ مُلَازِمَةٍ، أَوْ حَالَةٍ شُعُورِيَّةٍ دَائِمَةٍ لَا تَتَبَدَّلُ.</td></tr><tr><td><strong>الْجُمْلَةُ الْفِعْلِيَّةُ</strong></td><td>التَّغَيُّرُ، الْحَرَكَةُ، الْحَيَوِيَّةُ</td><td>عَرْضُ الْأَحْدَاثِ فِي سِيَاقٍ حَرَكِيٍّ مُتَغَيِّرٍ وَمُتَجَدِّدٍ.</td></tr>

=== BLOCK 9: Exam ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: اسْتَعْمَلَ الشَّاعِرُ فِي الْبَيْتِ الْآتِي جُمْلَةً اسْمِيَّةً، حَدِّدْهَا، ثُمَّ بَيِّنْ أَثَرَهَا فِي خِدْمَةِ الْمَعْنَى:<br>قَالَ الشَّاعِرُ: وَالْيَأْسُ يَقْطَعُ أَحْيَانًا بِصَاحِبِهِ ** لَا تَيْأَسَنَّ فَإِنَّ الصَّانِعَ اللهُ
Number: ٢
Question: مَا الْفَرْقُ بَيْنَ وَظِيفَةِ الْجُمْلَةِ الْاسْمِيَّةِ وَوَظِيفَةِ الْجُمْلَةِ الْفِعْلِيَّةِ مِنْ حَيْثُ الدَّلَالَةُ عَلَى الزَّمَنِ وَالْحَرَكَةِ؟

--- END STREAM ---
