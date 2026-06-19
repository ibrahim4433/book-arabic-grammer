# **SESSION 06.0**

[TASK DEFINITION]
Objective: Implement كَيْف تُعْرِبُ ؟( خَطْوَاتِ الْإِعْرَابِ الصَّحِيحِ ).
File: `pages/06_nXX_كَيْف تُعْرِبُ ؟( خَطْوَاتِ الْإِعْرَابِ الصَّحِيحِ ).html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/06.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 06
[CHAPTER_TITLE]: كَيْف تُعْرِبُ ؟( خَطْوَاتِ الْإِعْرَابِ الصَّحِيحِ )
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition & Rule ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مُقَدَّمَةٌ
Content:
<p class="text-accent text-center font-bold mb-2mm">يَسْأَلُ الْكَثِيرُ مِن الطُّلَاَّبِ: كَيْف أَسْتَطِيعُ إِعْرَابَ الْكَلِمَاتِ وَتَحْدِيدِ مَوْقِعِهَا وَعُلَّامَتِهَا بِطَرِيقَةٍ صَحِيحَةٍ دُون أَخْطَاءٍ ؟</p>
<p class="text-sm">عَمَلِيَّةُ الْإِعْرَابِ تُشْبِهُ تَشْخِيصُ الطَّبِيبِ لِلْمَرِيضَ فِي الْمُسْتَشْفَى. لِكَي نَصِفُ الْعِلَاَجَ ( <span class="highlight-blue">الْإِعْرَابَ النِّهَائِيَّ</span> ) بِدِقَّةٍ ، يَجِبُ أَنّ نَمِرٍ بِأَرْبَعِ خَطْوَاتٍ أَو " تحاليل " أَسَاسِيَّةً.</p>

=== BLOCK 3: The Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Title: الْخَطْوَاتِ الْأَرْبَعَ لِلْإِعْرَابِ
Table Content:
Row 1: ١. نَوْعُ الْكَلِمَةِ | هَلٌّ هِي ( اِسْمٌ ، أَم فعَلّ ، أَم حَرْفُ )؟ وهَل هِي ( مُفْرَدٌ ، أَم مُثَنًّى ، أَم جَمْعُ )؟
Row 2: ٢. الْمَوْقِعُ الْإِعْرَابِيُّ | مَا وَظِيفَةِ هَذِه الْكَلِمَةِ فِي الْجُمْلَةِ ؟( هَل هِي فَاعِلٍ ، مَفْعُولٌ بِه ، مُبْتَدَأٌ ، خَبَرٌ ...؟)
Row 3: ٣. الْحَالَةُ الْإِعْرَابِيَّةُ | هَل مَوْقِعِهَا يَتَطَلَّبُ ( الرَّفْعَ ، أَم النُّصْبُ ، أَم الْجَرُّ ، أَم الجزم )؟
Row 4: ٤. الْعُلَّامَةُ الْإِعْرَابِيَّةُ | بِنَاءً عَلَى نَوْعِهَا وَحَالَتِهَا ، مَا هِي الْحَرَكَةِ أَو الْحَرْفُ الَّذِي سَتَأْخُذُهُ فِي آخِرِهَا ؟( ضَمَّةً ، فَتْحَةً ، كَسِرَّةٍ ، أَلَفٌّ ، واو ، ياء ).

=== BLOCK 4: Extra Info (Tip) ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Title: تَنْبِيهٌ هَامٌّ (مِن أَجْلِ الْإِعْرَابِ)
Content: فِي بِدَايَةِ الْإِعْرَابِ ، نَسْأَلُ دَائِمًا : مَا نَوْعِ الْجُمْلَةِ ؟ إِذَا بَدَأَتْ بِفِعْلٍ هِي جُمْلَةِ فِعْلِيَّةِ، وَنَبْدَأُ بِفَكِّ شَفْرَاتِهَا بِطَرْحِ الْأسْئِلَةِ!

=== BLOCK 5: Deep Dive ===
(Component: TEMPLATE_C_BLOCK.html)
Title: التَّطْبِيقَ الْعَمَلِيَّ ( ١ )
Content:
<p class="text-sm font-bold text-center mb-2mm">الْمِثَالَ : " إِِْنّ الْمُعَلِّمَ يُحِبُّ <span class="highlight-red">الْمُجْتَهِدِينَ</span> ".</p>
<p class="text-sm">لِنُعْرِبُ كَلَمَّةِ ( الْمُجْتَهِدِينَ ) بِتَطْبِيقِ الْخَطْوَاتِ الْأَرْبَعَ:</p>
(Inject TEMPLATE_C_LIST.html here)
- **النَّوْعُ :** اِسْمٌ ، جَمَعَ مُذَكَّرُ سَالِمُ.
- **الْمَوْقِعُ :** مِن الَّذِي يُحِبُّ ؟ الْمُعَلِّمَ. مَاذَا يُحِبُّ ؟ الْمُجْتَهِدِينَ. إِذْنُ وَقْعٍ عَلَيْهُمْ فعَلّ الْفَاعِلِ ، فهِي ( مَفْعُولٌ بِه ).
- **الْحَالَةُ :** الْمَفْعُولُ بِه دَائِمًا يُكَوِّنُ فِي حَالَةٍ ( نُصِبْ ).
- **الْعُلَّامَةُ :** عُلَّامَةُ النُّصْبِ لِجَمَعَ الْمُذَكَّرُ السَّالِمُ هِي ( الياء ).
(Inject TEMPLATE_C_BENEFIT.html for the final Irab)
Title: الْإِعْرَابَ النِّهَائِيَّ ( وَصَفَّةَ الدَّوَاءِ )
Content: مَفْعُولٌ بِه مَنْصُوبٍ ، وَعُلَّامَةَ نُصْبِهِ الياء لأَنّهُ جَمْعَ مُذَكَّرَ سَالِمَ.

=== BLOCK 6: Deep Dive 2 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: التَّطْبِيقَ الْعَمَلِيَّ الشَّامِلَ ( ٢ )
Content:
<p class="text-sm font-bold text-center mb-2mm">ذَاكَرَ الطَّالِبُ الْمُجْتَهِدُ الدُّرُوسَ صَبَاحًا مُرَكَّزًا رَغْبَةً فِي النُّجَّاحِ وَالتَّفَوُّقِ .</p>
(Inject multiple TEMPLATE_C_IRAB_ROW.html pairs here for parsing)

Row 1:
- Word: ذَاكِرَ (مَنَّ ذَاكِرَ؟)
- Irab: فعَلّ مَاضٍ مَبْنِيِّ عَلَى الْفَتْحِ .( الْفِعْلِ الْمَاضِي دَائِمًا مَبْنِيَّ ).
- Word: الطَّالِبُ (الْإِجَابَةَ عَن " مَنَّ " تُعْطِينَا الْفَاعِلُ)
- Irab: فَاعِلَ مَرْفُوعَ وَعُلَّامَةَ رَفْعِهِ الضَّمَّةَ.

Row 2:
- Word: الْمُجْتَهِدُ (الطَّالِبَ مَنَّ ؟/ مَا صَفَّتِهِ ؟)
- Irab: نَعَتْ ( أَو صَفَّةُ ) مَرْفُوعٌ وَعُلَّامَةُ رَفْعِهِ الضَّمَّةَ .( تَتْبَعُ الْمَوْصُوفُ ).
- Word: الدُّرُوسَ (مَاذَا ذَاكِرُ ؟ تُعْطِينَا الْمَفْعُولُ بِه)
- Irab: مَفْعُولٌ بِه مَنْصُوبٍ وَعُلَّامَةِ نُصْبِهِ الْفَتَحَةِ.

Row 3:
- Word: صَبَاحًا (مَتَى ذَاكِرُ ؟ تُعْطِينَا ظَرْفُ الزَّمَانِ)
- Irab: ظَرُفَ زَمَانُ مَنْصُوبٍ وَعُلَّامَةِ نُصْبِهِ الْفَتَحَةِ.
- Word: مَرْكَزًا (كَيْف ذَاكِرُ ؟ تُعْطِينَا الْحَالُ)
- Irab: حَالَ مَنْصُوبَةَ وَعُلَّامَةَ نُصْبِهَا الْفَتَحَةِ .( الْحَالُ دَائِمًا مَنْصُوبَةً ).

Row 4:
- Word: رَغْبَةً (لِمَاذَا ذَاكِرَ ؟ تُعْطِينَا الْمَفْعُولُ لِأَجَّلَهُ)
- Irab: مَفْعُولٌ لِأَجَّلَهُ مَنْصُوبٌ وَعُلَّامَةُ نُصْبِهِ الْفَتَحَةِ.
- Word: فِي
- Irab: حَرْفَ جَرِّ مَبْنِيِّ.

Row 5:
- Word: النُّجَّاحِ
- Irab: اِسْمَ مَجْرُورَ ب ( فِي ) وَعُلَّامَةَ جُرِّهِ الْكُسَّرَةِ.
- Word: وَالتَّفَوُّقِ
- Irab: ( و ): حَرْفَ عَطْفٍ. ( التَّفَوُّقِ ): اِسْمَ مَعْطُوفٍ عَلَى ( النُّجَّاحَ ) مَجْرُورٌ وَعُلَّامَةُ جُرِّهِ الْكُسَّرَةِ .( لأَنّ الْمَعْطُوفِ يَتْبَعُ الْمَعْطُوفُ عَلَيْهِ ).

=== BLOCK 7: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: تَدْرِيبَاتٍ وَتَطْبِيقَاتٍ عَمَلِيَّةٍ: اِمْلَأْ الْفَرَاغَاتِ لِاِكْتِشَافَ الْمَوْقِعِ الْإِعْرَابِيِّ فِي الْجُمْلَةِ الْفِعْلِيَّةِ : لِمَعْرِفَةُ الْفَاعِلِ نَسْأَلُ بِكَلِمَةٍ ... ، لِمَعْرِفَةُ الْمَفْعُولِ بِه نَسْأَلُ بِكَلِمَةٍ ... ، لِمَعْرِفَةُ الْمَفْعُولِ لِأَجَّلَهُ ( السَّبَبَ ) نَسْأَلُ بِكَلِمَةٍ ... ، لِمَعْرِفَةُ الْحَالِ ( الْهَيْئَةَ ) نَسْأَلُ بِكَلِمَةٍ ... ، لِمَعْرِفَةُ ظَرْفِ الزَّمَانِ نَسْأَلُ بِكَلِمَةٍ ...

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: أَعْرَبَ الْكَلِمَاتُ الْمُلَوَّنَةُ بَنَّاءً عَلَى الْخَطْوَاتِ الْأَرْبَعَ: شَرِبَ الْمَرِيضُ الدَّوَاءَ أَمَلًا فِي الشِّفَاءِ. (الْمَرِيضُ ، الدَّوَاءَ ، أَمَلًا).

--- END STREAM ---
