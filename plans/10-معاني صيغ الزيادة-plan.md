# **SESSION 10.0**

[TASK DEFINITION]
Objective: Implement مَعَانِي صِيَغِ الزِّيَادَةِ (Lesson 10).
File: `pages/10.0_n29_maani_ziyada.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Page Breaking: Use `tools/verify_layout.py` after every block. If "FULL" or "OVERFLOW", close the current file and continue in `pages/10.1_n29_...`.
2. Content: 100% Arabic with full Harakat.
3. Highlighting: Use `.highlight-red` for the augmented verb forms (الصِّيَغ) and `.highlight-blue` for specific particles or examples if necessary.
4. Definitions: Must use `.text-accent` class for the main explanation of the concept.
5. Digits: All visible numbers must be Arabic-Indic (١, ٢, ٣...).

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER)
Title: مَعَانِي صِيَغِ الزِّيَادَةِ
Lesson: ١٠
Author: إِبْرَاهِيم أَبُو مُحَمَّد

=== BLOCK 2: تعريف معاني الزيادة ===
(Component: TEMPLATE_C_BLOCK)
Title: مَعَانِي أَحْرُفِ الزِّيَادَةِ
Content: <p class="text-accent">تَتَغَيَّرُ دَلَالَةُ الْفِعْلِ (مَعْنَاهُ) بِحَسَبِ مَا يُزَادُ عَلَى الثُّلَاثِيِّ مِنْ حُرُوفِ الزِّيَادَةِ، وَهَذِهِ الْمَعَانِي الْجَدِيدَةُ لَمْ تَكُنْ لِلْفِعْلِ قَبْلَ زِيَادَةِ الْأَحْرُفِ عَلَى أَصْلِهِ الثُّلَاثِيِّ.</p>

=== BLOCK 3: جدول صيغ الزيادة ===
(Component: TEMPLATE_C_TABLE)
Title: جَدْوَلُ أَهَمِّ الْمَعَانِي الْمُسْتَفَادَةِ مِنْ صِيَغِ الزِّيَادَةِ
Headers: الصِّيغَةُ الصَّرْفِيَّةُ | الْمَعَانِي الَّتِي تُفِيدُهَا حُرُوفُ الزِّيَادَةِ | الْمِثَالُ
Rows:
- <span class="highlight-red">أَفْعَلَ</span> | التَّحَوُّلُ مِنْ حَالٍ إِلَى حَالٍ، الدُّخُولُ فِي الزَّمَانِ، التَّعْدِيَةُ وَالْمُطَاوَعَةُ | (أَجْلَسَ، أَسْعَدَ)، (أَصْبَحَ، أَمْسَى)، (فَطَرْتُهُ فَأَفْطَرَ).
- <span class="highlight-red">افْعَلَّ</span> | الْمُبَالَغَةُ | احْمَرَّ، اخْضَرَّ، ...
- <span class="highlight-red">اسْتَفْعَلَ</span> | الطَّلَبُ وَالسُّؤَالُ، حُصُولُ الزَّمَنِ، التَّحَوُّلُ | اسْتَوْقَفَ، اسْتَحْصَدَ، اسْتَحْجَرَ، ...
- <span class="highlight-red">انْفَعَلَ</span> | الْمُطَاوَعَةُ | انْكَسَرَ، انْطَلَقَ، ...
- <span class="highlight-red">افْتَعَلَ</span> | الْمُطَاوَعَةُ، الِاتِّخَاذُ لِلنَّفْسِ، الْمُشَارَكَةُ | اقْتَرَبَ، اجْتَهَدَ، اخْتَصَمَ، ...
- <span class="highlight-red">تَفَعَّلَ</span> | الصَّيْرُورَةُ وَالتَّحَوُّلُ، الْمُطَاوَعَةُ، التَّكَلُّفُ، التَّدَرُّجُ فِي حُصُولِ الْفِعْلِ | تَزَوَّجَ، تَأَهَّلَ، تَحَجَّرَ، تَعَوَّضَ، ...
- <span class="highlight-red">تَفَاعَلَ</span> | الْمُشَارَكَةُ، التَّظَاهُرُ، التَّدَرُّجُ | تَعَاوَنَ، تَغَافَلَ، تَكَاثَرَ، ...
- <span class="highlight-red">تَفَعْلَلَ</span> | الْمُطَاوَعَةُ | تَدَحْرَجَ
- <span class="highlight-red">فَعَّلَ</span> | الْمُبَالَغَةُ، الدُّخُولُ فِي إِحْدَى الْجِهَتَيْنِ، التَّعْدِيَةُ، التَّكْثِيرُ | كَسَّرَ، شَرَّقَ، غَرَّبَ، حَطَّمَ، نَوَّمَ، عَوَّضَ، ...
- <span class="highlight-red">فَاعَلَ</span> | الْمُشَارَكَةُ بَيْنَ الْفَاعِلِ وَالْمَفْعُولِ بِهِ، التَّكْثِيرُ | نَاوَلَ، سَاعَدَ، نَازَلَ، ضَاعَفَ، ...

=== BLOCK 4: تقويم الدرس ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: حَدِّدِ الْفِعْلَ الْمَزِيدَ فِيمَا يَأْتِي، ثُمَّ اذْكُرِ الْمَعْنَى الَّذِي أَفَادَتْهُ الزِّيَادَةُ: (اسْتَحْجَرَ الطِّينُ - تَغَافَلَ الصَّدِيقُ عَنِ الزَّلَّةِ - كَسَّرَ النَّجَّارُ الْخَشَبَ).

--- END STREAM ---