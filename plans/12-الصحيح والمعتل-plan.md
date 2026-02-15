# **SESSION 12.0**

[TASK DEFINITION]
Objective: Implement the lesson on "Sound and Weak Verbs" (الْفِعْلُ الصَّحِيحُ وَالْفِعْلُ الْمُعْتَلُّ).
File: `pages/12.0_n28_sahih_mutal.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Page Breaking: Use `tools/verify_layout.py` after every block. If "FULL", continue in `pages/12.1_...`.
2. IDs: Use `tools/id_manager.py` to generate unique IDs for all blocks.
3. Content: 100% Arabic with full Harakat.
4. Highlighting: Use `.highlight-red` for primary focus words (vowels/types) and `.highlight-blue` for secondary.
5. Definitions: Must use `.text-accent` class.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER)
Title: الْفِعْلُ الصَّحِيحُ وَالْفِعْلُ الْمُعْتَلُّ
Lesson: ١٢
Author: إِبْرَاهِيم أَبُو مُحَمَّد

=== BLOCK 2: Definitions ===
(Component: TEMPLATE_C_BLOCK)
Title: تَعْرِيفُ الْفِعْلِ الصَّحِيحِ وَالْمُعْتَلِّ
Content:
<p class="text-accent mb-3mm"><strong>الْفِعْلُ الصَّحِيحُ:</strong> حُرُوفُهُ الْأَصْلِيَّةُ خَالِيَةٌ مِنْ حُرُوفِ الْعِلَّةِ.</p>
<p class="text-accent"><strong>الْفِعْلُ الْمُعْتَلُّ:</strong> أَحَدُ حُرُوفِهِ الْأَصْلِيَّةِ حَرْفُ عِلَّةٍ.</p>

=== BLOCK 3: Summary Matrix ===
(Component: TEMPLATE_C_TABLE)
Title: أَنْوَاعُ الْفِعْلِ الصَّحِيحِ وَالْمُعْتَلِّ
Headers: الْقِسْمُ | النَّوْعُ | التَّعْرِيفُ | الْأَمْثِلَةُ
Row 1: الصَّحِيحُ | الْمَهْمُوزُ | أَحَدُ أُصُولِهِ هَمْزَةٌ. | أَمَرَ، سَأَلَ، لَجَأَ.
Row 2: الصَّحِيحُ | الْمُضَعَّفُ | أَحَدُ أُصُولِهِ مُشَدَّدٌ. | صَدَّ، جَدَّ.
Row 3: الصَّحِيحُ | السَّالِمُ | أُصُولُهُ خَالِيَةٌ مِنَ الْهَمْزَةِ وَالتَّضْعِيفِ. | كَتَبَ، جَلَسَ.
Row 4: الْمُعْتَلُّ | الْمِثَالُ | أَوَّلُهُ حَرْفُ عِلَّةٍ. | وَصَلَ، وَجَدَ.
Row 5: الْمُعْتَلُّ | الْأَجْوَفُ | أَوْسَطُهُ حَرْفُ عِلَّةٍ. | قَالَ، صَامَ.
Row 6: الْمُعْتَلُّ | النَّاقِصُ | آخِرُهُ حَرْفُ عِلَّةٍ. | مَشَى، دَنَا.
Row 7: الْمُعْتَلُّ | اللَّفِيفُ الْمَقْرُونُ | حَرْفَا الْعِلَّةِ مُتَتَالِيَانِ. | رَوَى، هَوَى.
Row 8: الْمُعْتَلُّ | اللَّفِيفُ الْمَفْرُوقُ | بَيْنَ حَرْفَيِ الْعِلَّةِ فَاصِلٌ. | وَعَى، وَشَى.

=== BLOCK 4: Exam ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: عَرِّفِ الْفِعْلَ الصَّحِيحَ وَالْفِعْلَ الْمُعْتَلَّ، ثُمَّ مَيِّزْ بَيْنَهُمَا فِي الْأَمْثِلَةِ الْآتِيَةِ: (قَالَ، كَتَبَ، وَعَى، مَدَّ).

--- END STREAM ---
