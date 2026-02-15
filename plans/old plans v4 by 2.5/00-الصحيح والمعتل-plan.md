# **SESSION 12.0**

[TASK DEFINITION]
Objective: Implement the lesson on "Sound and Weak Verbs" (الفِعْلُ الصَّحِيحُ وَالفِعْلُ المُعْتَلُّ).
File: `pages/12.0_n12_correct_weak.html`
Reference: Follow patterns in design_patterns.json and the "One-Page Law".

[CONSTRAINTS & PROTOCOLS]
1. Page Breaking: Use `tools/verify_layout.py` after every block. If "FULL", continue in `pages/12.1_...`. (Expected: This lesson fits on one page).
2. Content: 100% Arabic with full Harakat (Tashkeel).
3. Highlighting: Use `.highlight-red` for the specific letters (Hamza, Shadda, Illah letters) and `.highlight-blue` for general focus.
4. Definitions: All core definitions must use the `.text-accent` class within a `content-block`.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER)
Title: الفِعْلُ الصَّحِيحُ وَالفِعْلُ المِعْتَلُّ
Lesson: ١٢
Author: إِبْرَاهِيم أَبُو مُحَمَّد

=== BLOCK 2: Introduction ===
(Component: TEMPLATE_C_BLOCK)
Title: تَعْرِيفُ الفِعْلِ الصَّحِيحِ
Content: هُوَ مَا كَانَتْ <span class="text-accent">حُرُوفُهُ الأَصْلِيَّةُ خَالِيَةً مِنْ حُرُوفِ العِلَّةِ</span> (الأَلِف، الوَاو، اليَاء).

=== BLOCK 3: Types of Sound Verb ===
(Component: TEMPLATE_C_TABLE)
Title: أَنْوَاعُ الفِعْلِ الصَّحِيحِ
Headers: نَوْعُ الفِعْلِ | التَّعْرِيفُ | الأَمْثِلَةُ
Row 1: السَّالِمُ | مَا خَلَتْ أُصُولُهُ مِنَ الهَمْزَةِ وَالتَّضْعِيفِ. | كَتَبَ، جَلَسَ، نَصَرَ.
Row 2: المَهْمُوزُ | مَا كَانَ أَحَدُ أُصُولِهِ <span class="highlight-red">هَمْزَةً</span>. | <span class="highlight-red">أَ</span>مَرَ، سَ<span class="highlight-red">أَ</span>لَ، لَجَ<span class="highlight-red">أَ</span>.
Row 3: المُضَعَّفُ | مَا كَانَ أَحَدُ أُصُولِهِ <span class="highlight-red">مُشَدَّدًا</span> (مُضَعَّفًا). | صَ<span class="highlight-red">دَّ</span>، جَ<span class="highlight-red">دَّ</span>، مَ<span class="highlight-red">دَّ</span>.

=== BLOCK 4: Definition of Weak Verb ===
(Component: TEMPLATE_C_BLOCK)
Title: تَعْرِيفُ الفِعْلِ المُعْتَلِّ
Content: هُوَ مَا كَانَ <span class="text-accent">أَحَدُ حُرُوفِهِ الأَصْلِيَّةِ حَرْفَ عِلَّةٍ</span>.

=== BLOCK 5: Types of Weak Verb ===
(Component: TEMPLATE_C_TABLE)
Title: أَنْوَاعُ الفِعْلِ المُعْتَلِّ
Headers: نَوْعُ الفِعْلِ | التَّعْرِيفُ | الأَمْثِلَةُ
Row 1: المِثَالُ | مَا كَانَ <span class="highlight-red">أَوَّلُهُ</span> حَرْفَ عِلَّةٍ. | <span class="highlight-red">و</span>َصَلَ، <span class="highlight-red">و</span>َجَدَ، <span class="highlight-red">ي</span>َبِسَ.
Row 2: الأَجْوَفُ | مَا كَانَ <span class="highlight-red">أَوْسَطُهُ</span> حَرْفَ عِلَّةٍ. | قَ<span class="highlight-red">ا</span>لَ، صَ<span class="highlight-red">ا</span>مَ، بَ<span class="highlight-red">ا</span>عَ.
Row 3: النَّاقِصُ | مَا كَانَ <span class="highlight-red">آخِرُهُ</span> حَرْفَ عِلَّةٍ. | مَشَ<span class="highlight-red">ى</span>، دَنَ<span class="highlight-red">ا</span>، رَضِ<span class="highlight-red">يَ</span>.

=== BLOCK 6: Special Cases (Al-Lafif) ===
(Component: TEMPLATE_C_SPLIT)
Left_Title: اللَّفِيفُ المَقْرُونُ
Left_Content: مَا كَانَ فِيهِ <span class="highlight-red">حَرْفَا عِلَّةٍ مُتَتَالِيَانِ</span>.<br>مِثْلُ: رَ<span class="highlight-red">و</span>َ<span class="highlight-red">ى</span>، هَ<span class="highlight-red">و</span>َ<span class="highlight-red">ى</span>، طَ<span class="highlight-red">و</span>َ<span class="highlight-red">ى</span>.
Right_Title: اللَّفِيفُ المَفْرُوقُ
Right_Content: مَا كَانَ فِيهِ <span class="highlight-red">حَرْفَا عِلَّةٍ بَيْنَهُمَا فَاصِلٌ</span>.<br>مِثْلُ: <span class="highlight-red">و</span>َعَ<span class="highlight-red">ى</span>، <span class="highlight-red">و</span>َشَ<span class="highlight-red">ى</span>، <span class="highlight-red">و</span>َقَ<span class="highlight-red">ى</span>.

=== BLOCK 7: Exam ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: صَنِّفِ الأَفْعَالَ الآتِيَةَ إِلَى صَحِيحَةٍ وَمُعْتَلَّةٍ مَعَ ذِكْرِ النَّوْعِ: (قَرَأَ، وَعَدَ، سَعَى، هَزَّ، نَامَ، رَمَى).

--- END STREAM ---