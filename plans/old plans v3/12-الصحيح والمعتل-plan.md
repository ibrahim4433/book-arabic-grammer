# **SESSION 12.0**

[TASK DEFINITION]
Objective: Implement Lesson 12: "الفعل الصحيح والفعل المعتل".
File: `pages/12.0_n31_sahih_muatal.html`
Reference: Follow patterns in design_patterns.json and apply the "One-Page Law".

[CONSTRAINTS & PROTOCOLS]
1. Page Breaking: Use `tools/verify_layout.py` after every block. If "FULL", continue in `pages/12.1_...`.
2. Content: 100% Arabic with full Harakat. 
3. Highlighting: Use `.highlight-red` for the vowel letters and specific characteristics (Hamza, Shadda) and `.highlight-blue` for classification names.
4. Definitions: Must use `.text-accent` class within content blocks.
5. Digits: Use Arabic-Indic digits (١، ٢، ٣...).

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER)
Title: الصَّحِيحُ وَالمُعْتَلُّ مِنَ الأَفْعَالِ
Lesson: ١٢
Author: إِبْرَاهِيم أَبُو مُحَمَّد

=== BLOCK 2: Definition: The Sound Verb ===
(Component: TEMPLATE_C_BLOCK)
Title: الفِعْلُ الصَّحِيحُ
Content: <span class="text-accent">هُوَ الفِعْلُ الَّذِي خَلَتْ حُرُوفُهُ الأَصْلِيَّةُ مِنْ حُرُوفِ العِلَّةِ</span> (الأَلِف، الوَاو، اليَاء). وَيَنْقَسِمُ إِلَى ثَلَاثَةِ أَنْوَاعٍ:

=== BLOCK 3: Types of Sound Verb ===
(Component: TEMPLATE_C_LIST)
Items:
- <b>١- المَهْمُوزُ:</b> مَا كَانَ أَحَدُ أُصُولِهِ <span class="highlight-red">هَمْزَةً</span>، مِثْلُ: (<span class="highlight-blue">أَ</span>مَرَ، سَـ<span class="highlight-blue">أَ</span>لَ، لَجَـ<span class="highlight-blue">أَ</span>).
- <b>٢- المُضَعَّفُ:</b> مَا كَانَ أَحَدُ أُصُولِهِ <span class="highlight-red">مُشَدَّدًا</span> (مُدْغَمًا)، مِثْلُ: (صَ<span class="highlight-blue">دَّ</span>، جَ<span class="highlight-blue">دَّ</span>، مَ<span class="highlight-blue">دَّ</span>).
- <b>٣- السَّالِمُ:</b> مَا خَلَتْ أُصُولُهُ مِنَ <span class="highlight-red">الهَمْزَةِ وَالتَّضْعِيفِ</span>، مِثْلُ: (<span class="highlight-blue">كَتَبَ</span>، <span class="highlight-blue">جَلَسَ</span>، <span class="highlight-blue">دَخَلَ</span>).

=== BLOCK 4: Definition: The Defective Verb ===
(Component: TEMPLATE_C_BLOCK)
Title: الفِعْلُ المُعْتَلُّ
Content: <span class="text-accent">هُوَ الفِعْلُ الَّذِي كَانَ أَحَدُ حُرُوفِهِ الأَصْلِيَّةِ (أَوْ أَكْثَر) حَرْفَ عِلَّةٍ</span>. وَيَنْقَسِمُ إِلَى خَمْسَةِ أَنْوَاعٍ:

=== BLOCK 5: Types of Defective Verb ===
(Component: TEMPLATE_C_LIST)
Items:
- <b>١- المِثَالُ:</b> مَا كَانَ <span class="highlight-red">أَوَّلُهُ</span> حَرْفَ عِلَّةٍ، مِثْلُ: (<span class="highlight-blue">وَ</span>صَلَ، <span class="highlight-blue">وَ</span>جَدَ، <span class="highlight-blue">يَ</span>بِسَ).
- <b>٢- الأَجْوَفُ:</b> مَا كَانَ <span class="highlight-red">أَوْسَطُهُ</span> حَرْفَ عِلَّةٍ، مِثْلُ: (قَـ<span class="highlight-blue">ا</span>لَ، صَـ<span class="highlight-blue">ا</span>مَ، بَـ<span class="highlight-blue">ا</span>عَ).
- <b>٣- النَّاقِصُ:</b> مَا كَانَ <span class="highlight-red">آخِرُهُ</span> حَرْفَ عِلَّةٍ، مِثْلُ: (مَشَـ<span class="highlight-blue">ى</span>، دَنَـ<span class="highlight-blue">ا</span>، رَمَـ<span class="highlight-blue">ى</span>).
- <b>٤- اللَّفِيفُ المَقْرُونُ:</b> مَا اجْتَمَعَ فِيهِ <span class="highlight-red">حَرْفَا عِلَّةٍ مُتَتَالِيَانِ</span>، مِثْلُ: (رَ<span class="highlight-blue">وَى</span>، هَـ<span class="highlight-blue">وَى</span>، طَـ<span class="highlight-blue">وَى</span>).
- <b>٥- اللَّفِيفُ المَفْرُوقُ:</b> مَا كَانَ فِيهِ حَرْفَا عِلَّةٍ <span class="highlight-red">بَيْنَهُمَا حَرْفٌ صَحِيحٌ</span>، مِثْلُ: (<span class="highlight-blue">وَ</span>عَـ<span class="highlight-blue">ى</span>، <span class="highlight-blue">وَ</span>شَـ<span class="highlight-blue">ى</span>، <span class="highlight-blue">وَ</span>قَـ<span class="highlight-blue">ى</span>).

=== BLOCK 6: Visual Summary Matrix ===
(Component: TEMPLATE_C_TABLE)
Headers: [الفِعْلُ, نَوْعُهُ, السَّبَبُ]
Rows:
- [قَرَأَ, صَحِيحٌ مَهْمُوزٌ, وُجُودُ الهَمْزَةِ فِي آخِرِهِ]
- [شَدَّ, صَحِيحٌ مُضَعَّفٌ, وُجُودُ التَّضْعِيفِ فِي آخِرِهِ]
- [وَصَفَ, مُعْتَلٌّ مِثَالٌ, حَرْفُ العِلَّةِ فِي أَوَّلِهِ]
- [نَوَى, مُعْتَلٌّ لَفِيفٌ مَقْرُونٌ, حَرْفَا عِلَّةٍ مُجْتَمِعَانِ]

=== BLOCK 7: Exam ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: صَنِّفِ الأَفْعَالَ التَّالِيَةَ حَسَبَ نَوْعِهَا مِنَ الصِّحَّةِ وَالاعْتِلَالِ: (سَعَى، قَامَ، عَدَّ، نَصَرَ، وَفَى، نَأَى).

--- END STREAM ---