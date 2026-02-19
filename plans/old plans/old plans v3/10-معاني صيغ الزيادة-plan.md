# **SESSION 10.0**

[TASK DEFINITION]
Objective: Implement مَعَانِي صِيَغِ الزِّيَادَةِ.
File: `pages/10.0_n29_maani_ziyada.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Page Breaking: Use `tools/verify_layout.py` after every major block. If the status is 'FULL' or 'OVERFLOW', close the current file and move the remaining content to `pages/10.1_...`.
2. Content: 100% Arabic with full Harakat. 
3. Highlighting: Use `.highlight-blue` for the augmented forms (patterns) and `.highlight-red` for specific morphological changes if applicable.
4. Definitions: Must use the `.text-accent` class within content blocks.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER)
Title: مَعَانِي صِيَغِ الزِّيَادَةِ
Lesson: ١٠
Author: إِبْرَاهِيم أَبُو مُحَمَّد

=== BLOCK 2: Definition ===
(Component: TEMPLATE_C_BLOCK)
Title: أَهَمُّ الْمَعَانِي الْمُسْتَفَادَةِ مِنْ صِيَغِ الزِّيَادَةِ فِي الْأَفْعَالِ
Content: <span class="text-accent">تَتَغَيَّرُ دَلَالَةُ الْفِعْلِ (مَعْنَاهُ) بِحَسَبِ مَا يُزَادُ عَلَى الثُّلَاثِيِّ مِنْ حُرُوفِ الزِّيَادَةِ، وَهَذِهِ الْمَعَانِي الْجَدِيدَةُ لَمْ تَكُنْ لِلْفِعْلِ قَبْلَ زِيَادَةِ الْأَحْرُفِ عَلَى أَصْلِهِ الثُّلَاثِيِّ، وَالْجَدْوَلُ الْآتِي يُوَضِّحُ الْمَعَانِيَ الَّتِي تُفِيدُهَا حُرُوفُ الزِّيَادَةِ:</span>

=== BLOCK 3: Meanings Matrix ===
(Component: TEMPLATE_C_TABLE)
Title: جَدْوَلُ صِيَغِ الزِّيَادَةِ وَمَعَانِيهَا
Header: الصِّيغَةُ الصَّرْفِيَّةُ | الْمَعَانِي الَّتِي تُفِيدُهَا حُرُوفُ الزِّيَادَةِ | الْمِثَالُ
Rows:
- <span class="highlight-blue">أَفْعَلَ</span> | التَّحَوُّلُ مِنْ حَالٍ إِلَى حَالٍ، الدُّخُولُ فِي الزَّمَانِ، التَّعْدِيَةُ وَالْمُطَاوَعَةُ | (أَجْلَسَ، أَسْعَدَ)، (أَصْبَحَ، أَمْسَى)، (فَطَرْتُهُ فَأَفْطَرَ).
- <span class="highlight-blue">افْعَلَّ</span> | الْمُبَالَغَةُ | احْمَرَّ، اخْضَرَّ، ...
- <span class="highlight-blue">اسْتَفْعَلَ</span> | الطَّلَبُ وَالسُّؤَالُ، حُصُولُ الزَّمَنِ، التَّحَوُّلُ | اسْتَوْقَفَ، اسْتَحْصَدَ، اسْتَحْجَرَ، ...
- <span class="highlight-blue">انْفَعَلَ</span> | الْمُطَاوَعَةُ | انْكَسَرَ، انْطَلَقَ، ...
- <span class="highlight-blue">افْتَعَلَ</span> | الْمُطَاوَعَةُ، الِاتِّخَاذُ لِلنَّفْسِ، الْمُشَارَكَةُ | اقْتَرَبَ، اجْتَهَدَ، اخْتَصَمَ، ...
- <span class="highlight-blue">تَفَعَّلَ</span> | الصَّيْرُورَةُ وَالتَّحَوُّلُ، الْمُطَاوَعَةُ، التَّكَلُّفُ، التَّدَرُّجُ فِي حُصُولِ الْفِعْلِ | تَزَوَّجَ، تَأَهَّلَ، تَحَجَّرَ، تَعَوَّضَ، ...
- <span class="highlight-blue">تَفَاعَلَ</span> | الْمُشَارَكَةُ، التَّظَاهُرُ، التَّدَرُّجُ | تَعَاوَنَ، تَغَافَلَ، تَكَاثَرَ، ...
- <span class="highlight-blue">تَفَعْلَلَ</span> | الْمُطَاوَعَةُ | تَدَحْرَجَ.
- <span class="highlight-blue">فَعَّلَ</span> | الْمُبَالَغَةُ، الدُّخُولُ فِي إِحْدَى الْجِهَتَيْنِ، التَّعْدِيَةُ، التَّكْثِيرُ | كَسَّرَ، شَرَّقَ، غَرَّبَ، حَطَّمَ، نَوَّمَ، عَوَّضَ، ...
- <span class="highlight-blue">فَاعَلَ</span> | الْمُشَارَكَةُ بَيْنَ الْفَاعِلِ وَالْمَفْعُولِ بِهِ، التَّكْثِيرُ | نَاوَلَ، سَاعَدَ، نَازَلَ، ضَاعَفَ، ...

=== BLOCK 4: Exam ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: حَدِّدِ المَعْنَى الَّذِي أَفَادَتْهُ الزِّيَادَةُ فِي الفِعْلِ (اسْتَحْجَرَ) فِي قَوْلِنَا: "اسْتَحْجَرَ الطِّينُ".

--- END STREAM ---