# **SESSION 09.0**

[TASK DEFINITION]
Objective: Implement المِيزَانُ الصَّرْفِيُّ.
File: `pages/09.0_n28_mizan_sarfi.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Page Breaking: Use `tools/verify_layout.py` after every block. If "FULL" or "OVERFLOW", close the current file (e.g., `09.0_...`) and move the remaining content to the next sequential file (e.g., `09.1_...`).
2. Content: 100% Arabic with full Harakat.
3. Highlighting: Use `.highlight-red` for primary focus (Mizan letters) and `.highlight-blue` for secondary focus (augmented letters).
4. Definitions: Must use `.text-accent` class within the content body.
5. Digits: Use Arabic-Indic digits (١، ٢، ٣...) for all visible numbering.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER)
Title: المِيزَانُ الصَّرْفِيُّ
Lesson: ٠٩
Author: إِبْرَاهِيم أَبُو مُحَمَّد

=== BLOCK 2: تَعْرِيفُ الصَّرْفِ ===
(Component: TEMPLATE_C_BLOCK)
Title: تَعْرِيفُ الصَّرْفِ
Content: الصَّرْفُ عِلْمٌ يَبْحَثُ فِي <span class="text-accent">بِنْيَةِ الكَلِمَةِ العَرَبِيَّةِ المُفْرَدَةِ</span> قَبْلَ أَنْ تَدْخُلَ فِي تَرْكِيبِ الكَلَامِ، وَوَزْنِهَا، وَتَغَيُّرَاتِهَا مِنْ شَكْلٍ إِلَى آخَرَ. وَأَهَمُّ مَا يُدْرَسُ فِيهِ: (المِيزَانُ الصَّرْفِيُّ لِلكَلِمَةِ، مَعَانِي أَحْرُفِ الزِّيَادَةِ، الإِعْلَالُ، الإِبْدَالُ، المُشْتَقَّاتُ، المَصَادِرُ).

=== BLOCK 3: تَعْرِيفُ المِيزَانِ الصَّرْفِيِّ ===
(Component: TEMPLATE_C_BLOCK)
Title: المِيزَانُ الصَّرْفِيُّ
Content: هُوَ <span class="text-accent">مِقْيَاسٌ لِمَعْرِفَةِ حُرُوفِ الكَلِمَةِ</span>، يَتَأَلَّفُ مِنْ ثَلَاثَةِ أَحْرُفٍ (ف، ع، ل) تُقَابِلُ الأُصُولَ الثَّلَاثَةَ الَّتِي تَتَكَوَّنُ مِنْهَا أَغْلَبُ الكَلِمَاتِ العَرَبِيَّةِ.

=== BLOCK 4: آلِيَّةُ الوَزْنِ ===
(Component: TEMPLATE_C_TABLE)
Title: هَيْكَلُ المِيزَانِ الصَّرْفِيِّ
Header: حُرُوفُ المِيزَانِ | فَاءُ الفِعْلِ | عَيْنُ الفِعْلِ | لَامُ الفِعْلِ
Row 1: الكَلِمَةُ | ضَـ | ـرَ | بَ
Row 2: المِيزَانُ | <span class="highlight-red">فَـ</span> | <span class="highlight-red">ـعَ</span> | <span class="highlight-red">ـلَ</span>

=== BLOCK 5: تَنْبِيهٌ هَامٌّ ===
(Component: TEMPLATE_C_BENEFIT)
Content: ضَبْطُ بِنْيَةِ الكَلِمَةِ المَوْزُونَةِ بِالحَرَكَاتِ وَالسَّكَنَاتِ يُطَابِقُ تَمَاماً ضَبْطَ المِيزَانِ الصَّرْفِيِّ.

=== BLOCK 6: الأُصُولُ الزَّائِدَةُ (الرُّبَاعِيُّ وَالخُمَاسِيُّ) ===
(Component: TEMPLATE_C_BLOCK)
Title: وَزْنُ الأُصُولِ الزَّائِدَةِ
Content: إِذَا كَانَتْ حُرُوفُ الكَلِمَةِ الأَصْلِيَّةُ أَرْبَعَةً، نُكَرِّرُ <span class="highlight-red">اللَّامَ</span> فِي آخِرِ المِيزَانِ. وَإِذَا كَانَتْ خَمْسَةً، نُكَرِّرُ <span class="highlight-red">اللَّامَ مَرَّتَيْنِ</span>.

=== BLOCK 7: مِثَالُ الفِعْلِ الرُّبَاعِيِّ ===
(Component: TEMPLATE_C_TABLE)
Title: وَزْنُ الفِعْلِ (بَعْثَرَ)
Header: حُرُوفُ المِيزَانِ | فَاءُ الفِعْلِ | عَيْنُ الفِعْلِ | لَامُ الفِعْلِ ١ | لَامُ الفِعْلِ ٢
Row 1: الكَلِمَةُ | بَـ | ـعْ | ثَـ | ـرَ
Row 2: المِيزَانُ | <span class="highlight-red">فَـ</span> | <span class="highlight-red">ـعْ</span> | <span class="highlight-red">ـلَ</span> | <span class="highlight-red">ـلَ</span>

=== BLOCK 8: قَوَاعِدُ الزِّيَادَةِ فِي الكَلِمَةِ ===
(Component: TEMPLATE_C_LIST)
Title: كَيْفِيَّةُ التَّعَامُلِ مَعَ الحُرُوفِ الزَّائِدَةِ
Item 1: <span class="font-bold">التَّكْرِيرُ:</span> إِذَا كَانَ الزَّائِدُ نَاتِجًا عَنْ تَكْرِيرِ أَصْلٍ، كَرَّرْنَا مَا يُقَابِلُهُ (سَبَّحَ : <span class="highlight-red">فَعَّلَ</span>).
Item 2: <span class="font-bold">حُرُوفُ الزِّيَادَةِ:</span> إِذَا كَانَ الزَّائِدُ حَرْفًا غَيْرَ أَصْلِيٍّ، نَذْكُرُهُ كَمَا هِيَ (كَاتَبَ : <span class="highlight-red">فَاعَلَ</span>).
Item 3: <span class="font-bold">الحَرْفُ المُعْتَلُّ:</span> يُعَامَلُ كَالصَّحِيحِ وَيُقَابَلُ بِنَظِيرِهِ (وَعَدَ، قَامَ : <span class="highlight-red">فَعَلَ</span>).
Item 4: <span class="font-bold">الحَذْفُ:</span> مَا يُحْذَفُ مِنَ الكَلِمَةِ يُحْذَفُ مَا يُقَابِلُهُ فِي المِيزَانِ (قُلْ : <span class="highlight-red">فُلْ</span>).

=== BLOCK 9: أَمْثِلَةٌ تَطْبِيقِيَّةٌ ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: زِنِ الكَلِمَاتِ الآتِيَةَ مَعَ الضَّبْطِ التَّامِّ: (اسْتَفْتَحَ، شَدَّ، ارْمِ، ثِقَةٌ، بُرُوقٌ).
Answer: (اسْتَفْعَلَ، فَعَلَ، افْعِ، عِلَةٌ، فُعُولٌ).

--- END STREAM ---