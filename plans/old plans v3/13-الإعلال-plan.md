# **SESSION 13.0**

[TASK DEFINITION]
Objective: Implement الإِعْلَالُ (I'lal).
File: `pages/13.0_n13_ilal.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Page Breaking: Use `tools/verify_layout.py` after every block. If "FULL" or "OVERFLOW", close the current file and continue in `pages/13.1_n13_ilal_cont.html`.
2. Content: 100% Arabic with full Harakat. No English.
3. Highlighting: Use `.highlight-red` for the affected weak letters (Waw, Ya, Alif) or their changes. Use `.highlight-blue` for particles.
4. Definitions: Must use `.text-accent` class within the content block.
5. Atomic Components: Strictly use TEMPLATE_C_HEADER, TEMPLATE_C_BLOCK, TEMPLATE_C_LIST, and TEMPLATE_C_EXAM.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER)
Title: الإِعْلَالُ
Lesson: ١٣
Author: إِبْرَاهِيم أَبُو مُحَمَّد

=== BLOCK 2: Definition ===
(Component: TEMPLATE_C_BLOCK)
Title: تَعْرِيفُ الإِعْلَالِ
Content: <span class="text-accent">الإِعْلَالُ هُوَ تَغْيِيرٌ يُصِيبُ <span class="highlight-red">حَرْفَ العِلَّةِ</span> (الأَلِف، الوَاو، اليَاء)</span>، وَيَكُونُ إِمَّا بِتَسْكِينِ الحَرْفِ، أَوْ حَذْفِهِ، أَوْ قَلْبِهِ إِلَى حَرْفٍ آخَرَ.

=== BLOCK 3: Types of I'lal ===
(Component: TEMPLATE_C_LIST)
Title: أَنْوَاعُ الإِعْلَالِ
Items:
- ١- <span class="font-bold">الإِعْلَالُ بِالتَّسْكِينِ:</span> حَذْفُ حَرَكَةِ حَرْفِ العِلَّةِ.
- ٢- <span class="font-bold">الإِعْلَالُ بِالحَذْفِ:</span> حَذْفُ حَرْفِ العِلَّةِ مِنَ الكَلِمَةِ.
- ٣- <span class="font-bold">الإِعْلَالُ بِالقَلْبِ:</span> قَلْبُ حَرْفِ العِلَّةِ إِلَى حَرْفِ عِلَّةٍ آخَرَ.

=== BLOCK 4: I'lal by Quiescence ===
(Component: TEMPLATE_C_BLOCK)
Title: أَوَّلاً- الإِعْلَالُ بِالتَّسْكِينِ
Content: هُوَ <span class="highlight-red">تَسْكِينُ</span> أَحَدِ حَرْفَيِ العِلَّةِ (الوَاو أَوِ اليَاء) لِثِقَلِ الحَرَكَةِ عَلَيْهِمَا، وَيَكُونُ فِي حَالَتَيْنِ:

=== BLOCK 5: Cases of Quiescence ===
(Component: TEMPLATE_C_LIST)
Items:
- ١- <span class="font-bold">فِي لَامِ الكَلِمَةِ:</span> إِذَا سُبِقَتِ <span class="highlight-red">الوَاوُ</span> بِضَمَّةٍ، أَوْ <span class="highlight-red">اليَاءُ</span> بِكَسْرَةٍ. مِثْلُ: <span class="marker">يَسْمُو</span> (أَصْلُهَا يَسْمُـوُ)، <span class="marker">يَمْشِي</span> (أَصْلُهَا يَمْشِـيُ).
- ٢- <span class="font-bold">فِي عَيْنِ الكَلِمَةِ:</span> إِذَا تَحَرَّكَ حَرْفُ العِلَّةِ وَسُبِقَ بِحَرْفٍ صَحِيحٍ سَاكِنٍ، تُنْقَلُ حَرَكَتُهُ إِلَى الصَّحِيحِ وَيُسَكَّنُ هُوَ. مِثْلُ: <span class="marker">يَقُومُ</span> (أَصْلُهَا يَقْـوُمُ)، <span class="marker">يَبِينُ</span> (أَصْلُهَا يَبْـيِنُ).

=== BLOCK 6: I'lal by Deletion ===
(Component: TEMPLATE_C_BLOCK)
Title: ثَانِيًا- الإِعْلَالُ بِالحَذْفِ
Content: هُوَ <span class="highlight-red">حَذْفُ</span> حَرْفِ العِلَّةِ تَمَاماً لِأَسْبَابٍ صَرْفِيَّةٍ، وَمَوَاضِعُهُ ثَلَاثَةٌ:

=== BLOCK 7: Cases of Deletion ===
(Component: TEMPLATE_C_LIST)
Items:
- ١- <span class="font-bold">فِي أَوَّلِ الكَلِمَةِ:</span> فِي الفِعْلِ المِثَالِ عِنْدَ المُضَارِعِ وَالأَمْرِ. مِثْلُ: <span class="marker">يَرِثُ</span> (حُذِفَتِ الوَاوُ)، <span class="marker">زِنْ</span> (حُذِفَتِ الوَاوُ).
- ٢- <span class="font-bold">فِي وَسَطِ الكَلِمَةِ:</span> فِي الفِعْلِ الأَجْوَفِ إِذَا التَقَى سَاكِنَانِ. مِثْلُ: <span class="marker">قُلْ</span> (أَصْلُهَا قُولْ)، حُذِفَتِ <span class="highlight-red">الأَلِفُ</span> لِالْتِقَاءِ السَّاكِنَيْنِ.
- ٣- <span class="font-bold">فِي آخِرِ الكَلِمَةِ:</span> فِي الفِعْلِ النَّاقِصِ (المُضَارِعُ المَجْزُومُ، الأَمْرُ، المَاضِي مَعَ وَاوِ الجَمَاعَةِ). مِثْلُ: <span class="marker">لَمْ يَمْشِ</span>، <span class="marker">اسْعَ</span>، <span class="marker">مَشَتْ</span>، <span class="marker">دَعَوْا</span>.

=== BLOCK 8: I'lal by Turning (Alif) ===
(Component: TEMPLATE_C_BLOCK)
Title: ثَالِثًا- الإِعْلَالُ بِالقَلْبِ
Content: هُوَ <span class="highlight-red">قَلْبُ</span> حَرْفِ العِلَّةِ إِلَى حَرْفٍ آخَرَ، وَأَهَمُّ حَالَاتِهِ:
<br>
١- <span class="font-bold">قَلْبُ الوَاوِ أَوِ اليَاءِ أَلِفًا:</span> إِذَا تَحَرَّكَتَا وَانْفَتَحَ مَا قَبْلَهُمَا. مِثْلُ: <span class="marker">قَالَ</span> (قَوَلَ)، <span class="marker">بَاعَ</span> (بَيَعَ)، <span class="marker">سَمَا</span> (سَمَوَ)، <span class="marker">جَرَى</span> (جَرَيَ).

=== BLOCK 9: Turning to Ya ===
(Component: TEMPLATE_C_LIST)
Title: ٢- قَلْبُ الوَاوِ يَاءً
Items:
- أ- <span class="font-bold">إِذَا تَطَرَّفَتْ بَعْدَ كَسْرٍ:</span> مِثْلُ <span class="marker">رَضِيَ</span> (أَصْلُهَا رَضِـوَ).
- ب- <span class="font-bold">إِذَا وَقَعَتْ حَشْوًا بَيْنَ كَسْرَةٍ وَأَلِفٍ:</span> مِثْلُ <span class="marker">قِيَامٌ</span> (أَصْلُهَا قِـوَامٌ).
- ج- <span class="font-bold">إِذَا سُكِّنَتْ بَعْدَ كَسْرٍ:</span> مِثْلُ <span class="marker">مِيزَانٌ</span> (أَصْلُهَا مِـوْزَانٌ).
- د- <span class="font-bold">إِذَا اجْتَمَعَتِ الوَاوُ وَاليَاءُ وَكَانَ السَّابِقُ سَاكِنًا:</span> مِثْلُ <span class="marker">سَيِّدٌ</span> (سَيْوِدٌ).

=== BLOCK 10: Turning to Waw ===
(Component: TEMPLATE_C_BLOCK)
Title: ٣- قَلْبُ اليَاء الوَاوًا
Content: تُقْلَبُ اليَاءُ <span class="highlight-red">وَاوًا</span> إِذَا سُكِّنَتْ بَعْدَ ضَمٍّ. مِثْلُ: <span class="marker">مُوقِنٌ</span> (أَصْلُهَا مُـيْقِنٌ)، <span class="marker">مُوسِرٌ</span> (أَصْلُهَا مُـيْسِرٌ).

=== BLOCK 11: Exam ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: سَمِّ مَعَ التَّوْضِيحِ العِلَّةَ الصَّرْفِيَّةَ فِي الكَلِمَاتِ الآتِيَةِ: (قَالَ، عُدْ، دَنَا، مِيزَان).
Answer: 
- قَالَ: إِعْلَالٌ بِالقَلْبِ (قُلِبَتِ الوَاوُ أَلِفًا لِتَحَرُّكِهَا بَعْدَ فَتْحٍ).
- عُدْ: إِعْلَالٌ بِالحَذْفِ (حُذِفَتِ الوَاوُ لِالْتِقَاءِ السَّاكِنَيْنِ).
- دَنَا: إِعْلَالٌ بِالقَلْبِ (قُلِبَتِ الوَاوُ أَلِفًا لِتَحَرُّكِهَا بَعْدَ فَتْحٍ).
- مِيزَان: إِعْلَالٌ بِالقَلْبِ (قُلِبَتِ الوَاوُ يَاءً لِسُكُونِهَا بَعْدَ كَسْرٍ).

--- END STREAM ---