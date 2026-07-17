# **SESSION 14.0**

[TASK DEFINITION]
Objective: Implement الجَامِدُ وَالمُشْتَقُّ.
File: `pages/14.0_n33_jamid_mushtaq.html`
Reference: Follow patterns in design_patterns.json and Morphological standards.

[CONSTRAINTS & PROTOCOLS]
1. Page Breaking: Use `tools/verify_layout.py` after every block. If "FULL", continue in `pages/14.1_n33_mushtaq_cont.html`.
2. Content: 100% Arabic with full Harakat. Essential for Shuruhat (Explanations).
3. Highlighting: Use `.highlight-red` for weights (Awzan) and `.highlight-blue` for derived suffixes/prefixes.
4. Definitions: Must use `.text-accent` class within `.content-block`.
5. Tables: Use `TEMPLATE_C_TABLE` for side-by-side comparisons of Jamid types.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER)
Title: الجَامِدُ وَالمُشْتَقُّ
Lesson: ١٤
Author: إِبْرَاهِيم أَبُو مُحَمَّد

=== BLOCK 2: Definition ===
(Component: TEMPLATE_C_BLOCK)
Title: تَعْرِيفُ الجَامِدِ وَالمُشْتَقِّ
Content: <span class="text-accent">الاسْمُ الجَامِدُ:</span> هُوَ الاسْمُ الَّذِي لَا يُؤْخَذُ مِنْ غَيْرِهِ، مِثْلُ: (قَلَم، صِدْق).<br>
<span class="text-accent">الاسْمُ المُشْتَقُّ:</span> هُوَ الاسْمُ الَّذِي يُؤْخَذُ مِنْ غَيْرِهِ (غَالِبًا مِنَ المَصْدَرِ)، مِثْلُ: (كَاتِب، مَكْتُوب).

=== BLOCK 3: Types of Jamid ===
(Component: TEMPLATE_C_SPLIT)
Right_Title: اسْمُ جَامِدُ ذَاتٍ
Right_Content: هُوَ مَا يُدْرَكُ بِإِحْدَى الحَوَاسِّ الخَمْسِ، وَلَهُ حَيِّزٌ فِي الوَاقِعِ.<br>مِثْلُ: <span class="highlight-blue">(شَجَرَة، كُرْسِيّ، قَلَم، رَجُل).</span>
Left_Title: اسْمُ جَامِدُ مَعْنَى
Left_Content: هُوَ مَا يُدْرَكُ بِالعَقْلِ (المَصْدَرُ)، وَيَدُلُّ عَلَى حَدَثٍ مُجَرَّدٍ مِنَ الزَّمَنِ.<br>مِثْلُ: <span class="highlight-blue">(نَجَاح، أَمَل، نِضَال، رَغْبَة).</span>

=== BLOCK 4: Mushtaqat List ===
(Component: TEMPLATE_C_CHIPS)
Title: أَنْوَاعُ المُشْتَقَّاتِ السَّبْعَةِ:
Items: ["اسْمُ الفَاعِلِ", "مُبَالَغَةُ اسْمِ الفَاعِلِ", "اسْمُ المَفْعُولِ", "الصِّفَةُ المُشَبَّهَةُ", "اسْمُ الآلَةِ", "اسْمَا المَكَانِ وَالزَّمَانِ", "اسْمُ التَّفْضِيلِ"]

=== BLOCK 5: Ism al-Fa'il ===
(Component: TEMPLATE_C_BLOCK)
Title: ١- اسْمُ الفَاعِلِ
Content: اسْمٌ يَدُلُّ عَلَى مَنْ قَامَ بِالفِعْلِ. يُصَاغُ:<br>
• مِنَ الثُّلَاثِيِّ: عَلَى وَزْنِ <span class="highlight-red">(فَاعِل)</span>، مِثْلُ: (كَتَبَ -> <span class="highlight-blue">كَاتِب</span>).<br>
• فَوْقَ الثُّلَاثِيِّ: عَلَى صِيغَةِ مُضَارِعِهِ بِإِبْدَالِ حَرْفِ المُضَارَعَةِ <span class="highlight-red">مِيمًا مَضْمُومَةً</span> وَكَسْرِ مَا قَبْلَ الآخِرِ، مِثْلُ: (كَرَّمَ -> <span class="highlight-blue">مُكَرِّم</span>).

=== BLOCK 6: Mubalagha ===
(Component: TEMPLATE_C_BLOCK)
Title: ٢- مُبَالَغَةُ اسْمِ الفَاعِلِ
Content: اسْمٌ يَدُلُّ عَلَى القِيَامِ بِالفِعْلِ بِكَثْرَةٍ وَمُبَالَغَةٍ. أَوْزَانُهَا المَشْهُورَةُ:<br>
<span class="highlight-red">(فَعَّال)</span> مِثْلُ جَلَّاد، <span class="highlight-red">(فَعَّالَة)</span> مِثْلُ عَلَّامَة، <span class="highlight-red">(مِفْعَال)</span> مِثْلُ مِعْطَاء، <span class="highlight-red">(فَعُول)</span> مِثْلُ أَكُول، <span class="highlight-red">(فَعِيل)</span> مِثْلُ رَحِيم.

=== BLOCK 7: Ism al-Maf'ul ===
(Component: TEMPLATE_C_BLOCK)
Title: ٣- اسْمُ المَفْعُولِ
Content: اسْمٌ يَدُلُّ عَلَى مَنْ وَقَعَ عَلَيْهِ الفِعْلُ. يُصَاغُ:<br>
• مِنَ الثُّلَاثِيِّ المَبْنِيِّ لِلمَجْهُولِ: عَلَى وَزْنِ <span class="highlight-red">(مَفْعُول)</span>، مِثْلُ: (كُتِبَ -> <span class="highlight-blue">مَكْتُوب</span>).<br>
• فَوْقَ الثُّلَاثِيِّ: عَلَى صِيغَةِ مُضَارِعِهِ المَبْنِيِّ لِلمَجْهُولِ بِإِبْدَالِ حَرْفِ المُضَارَعَةِ <span class="highlight-red">مِيمًا مَضْمُومَةً وَفَتْحِ</span> مَا قَبْلَ الآخِرِ، مِثْلُ: (اسْتُخْرِجَ -> <span class="highlight-blue">مُسْتَخْرَج</span>).

=== BLOCK 8: Benefit Box ===
(Component: TEMPLATE_C_BENEFIT)
Title: فَائِدَةٌ فِي عَمَلِ المُشْتَقَّاتِ
Content: قَدْ تَعْمَلُ هَذِهِ المُشْتَقَّاتُ عَمَلَ فِعْلِهَا؛ فَيَرْفَعُ اسْمُ الفَاعِلِ فَاعِلًا، وَيَرْفَعُ اسْمُ المَفْعُولِ نَائِبَ فَاعِلٍ، نَحْوُ: <span class="highlight-blue">(الأَبُ مَشْكُورٌ فَضْلُهُ)</span>.

--- END STREAM ---

# **SESSION 14.1**
File: `pages/14.1_n33_mushtaqat_cont.html`

=== BLOCK 1: Sifa Mushabbaha ===
(Component: TEMPLATE_C_BLOCK)
Title: ٤- الصِّفَةُ المُشَبَّهَةُ بِاسْمِ الفَاعِلِ
Content: اسْمٌ يُشْتَقُّ لِيَدُلَّ عَلَى صِفَةٍ ثَابِتَةٍ. أَوْزَانُهَا:<br>
<span class="highlight-red">(فَعِيل)</span> كَرِيم، <span class="highlight-red">(فُعَال)</span> شُجَاع، <span class="highlight-red">(فَعَال)</span> جَبَان، <span class="highlight-red">(فَعِل)</span> بَطِل، <span class="highlight-red">(أَفْعَل)</span> الَّذِي مُؤَنَّثُهُ <span class="highlight-red">(فَعْلَاء)</span> فِي الأَلْوَانِ وَالعُيُوبِ (أَحْمَر/حَمْرَاء).

=== BLOCK 2: Ism al-Ala ===
(Component: TEMPLATE_C_BLOCK)
Title: ٥- اسْمُ الآلَةِ
Content: اسْمٌ يَدُلُّ عَلَى آلَةِ الفِعْلِ. أَوْزَانُهُ الخَمْسَةُ:<br>
<span class="highlight-red">(مِفْعَل)</span> مِثْقَب، <span class="highlight-red">(مِفْعَال)</span> مِصْبَاح، <span class="highlight-red">(مِفْعَلَة)</span> مِرْوَحَة، <span class="highlight-red">(فَعَّال)</span> بَرَّاد، <span class="highlight-red">(فَعَّالَة)</span> غَسَّالَة.

=== BLOCK 3: Ism al-Makan & al-Zaman ===
(Component: TEMPLATE_C_BLOCK)
Title: ٦- اسْمُ المَكَانِ وَاسْمُ الزَّمَانِ
Content: يُصَاغَانِ مِنَ الثُّلَاثِيِّ عَلَى وَزْنَيْنِ:<br>
• <span class="highlight-red">(مَفْعَل):</span> إِذَا كَانَ المُضَارِعُ مَفْتُوحَ العَيْنِ أَوْ مَضْمُومَهَا، مِثْلُ: <span class="highlight-blue">(مَسْبَح، مَدْخَل)</span>.<br>
• <span class="highlight-red">(مَفْعِل):</span> إِذَا كَانَ المُضَارِعُ مَكْسُورَ العَيْنِ أَوْ كَانَ مِثَالًا وَاوِيًّا، مِثْلُ: <span class="highlight-blue">(مَعْرِض، مَوْقِف)</span>.<br>
• <span class="highlight-red">فَوْقَ الثُّلَاثِيِّ:</span> كَصِيغَةِ اسْمِ المَفْعُولِ، مِثْلُ: <span class="highlight-blue">(مُجْتَمَع، مُسْتَقَى)</span>.

=== BLOCK 4: Ism al-Tafdil ===
(Component: TEMPLATE_C_BLOCK)
Title: ٧- اسْمُ التَّفْضِيلِ
Content: اسْمٌ يَدُلُّ عَلَى اشْتِرَاكِ شَيْئَيْنِ فِي صِفَةٍ وَزِيَادَةِ أَحَدِهِمَا. وَزْنُهُ <span class="highlight-red">(أَفْعَل)</span> لِلْمُذَكَّرِ وَ<span class="highlight-red">(فُعْلَى)</span> لِلْمُؤَنَّثِ.<br>
<span class="highlight-blue">مِثْلُ: (أَنْفَع، أَفْضَل، كُبْرَى).</span>

=== BLOCK 5: Exam ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: مَيِّزِ الجَامِدَ مِنَ المُشْتَقِّ فِي الكَلِمَاتِ الآتِيَةِ: (شَجَرَة، كَاتِب، نَجَاح، مِفْتَاح).

--- END STREAM ---