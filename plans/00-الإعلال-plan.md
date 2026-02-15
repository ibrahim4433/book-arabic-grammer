# **SESSION 28.0**

[TASK DEFINITION]
Objective: Implement the lesson on **I'lal (Morphology of Weak Vowels)**.
File: `pages/09.0_n28_ilal.html`
Reference: Follow patterns in `design_patterns.json` and Sarf chapter structure.

[CONSTRAINTS & PROTOCOLS]
1. **Page Breaking:** Use `tools/verify_layout.py` after every block. If the layout is "FULL" or "OVERFLOW", close the current file and continue the content stream in `pages/09.1_n29_ilal_cont.html`.
2. **Content:** 100% Arabic with full Harakat. Preserve all technical linguistic terms.
3. **Highlighting:** 
    - Use `.highlight-red` for the modified weak letters (the result of I'lal).
    - Use `.highlight-blue` for the original letters or conditions (like Sukun/Fatha).
4. **Definitions:** Must use the `.text-accent` class within a `content-block`.
5. **Space Optimization:** Use `TEMPLATE_C_SPLIT` for comparing the original form (Asl) vs. the modified form (Mu'all).

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER)
Title: الإِعْلَالُ
Lesson: ١٣
Author: إِبْرَاهِيم أَبُو مُحَمَّد

=== BLOCK 2: Definition of I'lal ===
(Component: TEMPLATE_C_BLOCK)
Title: تَعْرِيفُ الإِعْلَالِ
Content: <span class="text-accent">الإِعْلَالُ هُوَ تَغْيِيرٌ يُصِيبُ حَرْفَ الْعِلَّةِ (الأَلِف، الوَاو، اليَاء)</span>، وَيَكُونُ إِمَّا بِتَسْكِينِهِ، أَوْ بِحَذْفِهِ، أَوْ بِقَلْبِهِ إِلَى حَرْفٍ آخَرَ؛ لِتَحْقِيقِ الخِفَّةِ فِي النُّطْقِ.

=== BLOCK 3: I'lal by Silencing (Vocalization) ===
(Component: TEMPLATE_C_BLOCK)
Title: أَوَّلًا: الإِعْلَالُ بِالتَّسْكِينِ
Content: هُوَ نَقْلُ حَرَكَةِ حَرْفِ العِلَّةِ إِلَى الحَرْفِ الصَّحِيحِ السَّاكِنِ قَبْلَهُ، أَوْ حَذْفُ الحَرَكَةِ لِلثِّقَلِ.
(Component: TEMPLATE_C_LIST)
Items:
- إِذَا تَطَرَّفَتِ <span class="highlight-blue">الوَاوُ</span> أَوِ <span class="highlight-blue">اليَاءُ</span> بَعْدَ ضَمٍّ أَوْ كَسْرٍ: <span class="marker">مِثْلُ:</span> (يَسْمُـ<span class="highlight-red">و</span>، يَمْشِـ<span class="highlight-red">ي</span>).
- إِذَا كَانَتِ <span class="highlight-blue">الوَاوُ</span> أَوِ <span class="highlight-blue">اليَاءُ</span> مَبْدُوءَةً بِحَرَكَةٍ وَقَبْلَهَا سَاكِنٌ صَحِيحٌ: <span class="marker">مِثْلُ:</span> يَقُومُ (أَصْلُهَا <span class="highlight-blue">يَقْوُمُ</span>)، يَبِينُ (أَصْلُهَا <span class="highlight-blue">يَبْيِنُ</span>).

=== BLOCK 4: I'lal by Deletion ===
(Component: TEMPLATE_C_BLOCK)
Title: ثَانِيًا: الإِعْلَالُ بِالحَذْفِ
Content: يُحْذَفُ حَرْفُ العِلَّةِ لِأَسْبَابٍ صَرْفِيَّةٍ أَوْ لِمَنْعِ اِلْتِقَاءِ السَّاكِنَيْنِ.
(Component: TEMPLATE_C_SPLIT)
Left Column (Title: مَوَاضِعُ الحَذْفِ):
- <span class="font-bold">أَوَّلُ الكَلِمَةِ:</span> فِي الفِعْلِ المِثَالِ (يَرِثُ، زِنْ).
- <span class="font-bold">وَسَطُ الكَلِمَةِ:</span> فِي الأَجْوَفِ عِنْدَ سُكُونِ آخِرِهِ (قُـ<span class="highlight-red">لْ</span>، لَمْ يَبِـ<span class="highlight-red">عْ</span>).
Right Column (Title: آخِرُ الكَلِمَةِ):
- <span class="font-bold">المُضَارِعُ المَجْزُومُ:</span> (لَمْ يَمْـ<span class="highlight-red">شِ</span>).
- <span class="font-bold">أَمْرُ المُفْرَدِ:</span> (اِسْـ<span class="highlight-red">عَ</span>، اِرْ<span class="highlight-red">مِ</span>).
- <span class="font-bold">المَاضِي:</span> عِنْدَ اِتِّصَالِهِ بِتَاءِ التَّأْنِيثِ (مَشَـ<span class="highlight-red">تْ</span>) أَوْ وَاوِ الجَمَاعَةِ (دَعَـ<span class="highlight-red">وْا</span>).

=== BLOCK 5: I'lal by Conversion (Part 1) ===
(Component: TEMPLATE_C_BLOCK)
Title: ثَالِثًا: الإِعْلَالُ بِالقَلْبِ
Content: وَهُوَ قَلْبُ حَرْفِ العِلَّةِ إِلَى حَرْفٍ آخَرَ لِيُنَاسِبَ الحَرَكَةَ الَّتِي قَبْلَهُ.
(Component: TEMPLATE_C_LIST)
Items:
- <span class="font-bold">قَلْبُ الوَاوِ أَوِ اليَاءِ أَلِفًا:</span> إِذَا تَحَرَّكَتَا وَانْفَتَحَ مَا قَبْلَهُمَا. <span class="marker">مِثْلُ:</span> قَـ<span class="highlight-red">ا</span>لَ (قَوَلَ)، بَـ<span class="highlight-red">ا</span>عَ (بَيَعَ)، سَمَـ<span class="highlight-red">ا</span> (سَمَوَ).
- <span class="font-bold">قَلْبُ الوَاوِ يَاءً:</span> إِذَا تَطَرَّفَتْ بَعْدَ كَسْرٍ (رَضِـ<span class="highlight-red">يَ</span> - أَصْلُهَا رَضِوَ)، أَوْ سُكِّنَتْ بَعْدَ كَسْرٍ (مِـ<span class="highlight-red">ي</span>ـزَان - أَصْلُهَا مِوْزَان).

=== BLOCK 6: I'lal by Conversion (Part 2) ===
(Component: TEMPLATE_C_BLOCK)
Title: تَتِمَّةُ الإِعْلَالِ بِالقَلْبِ
Content:
(Component: TEMPLATE_C_LIST)
Items:
- <span class="font-bold">قَلْبُ اليَاءِ وَاوًا:</span> إِذَا سَكَنَتْ بَعْدَ ضَمٍّ. <span class="marker">مِثْلُ:</span> مـ<span class="highlight-red">و</span>قِن (أَصْلُهَا مُيْقِن)، مـ<span class="highlight-red">و</span>سِر (أَصْلُهَا مُيْسِر).
- <span class="font-bold">اجْتِمَاعُ الوَاوِ وَاليَاءِ:</span> تُقْلَبُ الوَاوُ يَاءً وَتُدْغَمَانِ إِذَا سَبَقَتْ إِحْدَاهُمَا بِالسُّكُونِ. <span class="marker">مِثْلُ:</span> سَيِّـ<span class="highlight-red">د</span> (سَيْوِد)، مَيِّـ<span class="highlight-red">ت</span> (مَيْوِت).

=== BLOCK 7: Practical Exam ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: سَمِّ العِلَّةَ الصَّرْفِيَّةَ فِي الكَلِمَاتِ الآتِيَةِ مَعَ التَّوْضِيحِ: (قَالَ، عُدْ، دَنَا، يَسْقِي).
(Component: TEMPLATE_C_IRAB_ROW)
Items:
- Word: قَالَ
  Role: إِعْلَالٌ بِالقَلْبِ (قُلِبَتِ الوَاوُ أَلِفًا لِتَحَرُّكِهَا بَعْدَ فَتْحٍ).
- Word: عُدْ
  Role: إِعْلَالٌ بِالحَذْفِ (حُذِفَتِ الوَاوُ لِمَنْعِ اِلْتِقَاءِ السَّاكِنَيْنِ).
- Word: يَسْقِي
  Role: إِعْلَالٌ بِالتَّسْكِينِ (سُكِّنَتِ اليَاءُ لِتَطَرُّفِهَا بَعْدَ كَسْرٍ).

--- END STREAM ---