# **SESSION 11.0**

[TASK DEFINITION]
Objective: Implement Lesson 11 - Substitution (Al-Ibdal).
File: `pages/11.0_n28_ibdal.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Page Breaking: Use `tools/verify_layout.py` after every block. If "FULL" or "OVERFLOW", close the current file (e.g., `11.0_...`) and move the remaining content to the next sequential file (e.g., `11.1_...`).
2. Content: 100% Arabic with full Harakat.
3. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue` for secondary.
4. Definitions: Must use `.text-accent` class.
5. Solved Exercises: Use `.exercise-question` class inside `TEMPLATE_C_BLOCK` and explicitly render the provided answers.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER)
Title: الإِبْدَالُ
Lesson: ١١
Author: إِبْرَاهِيم أَبُو مُحَمَّد

=== BLOCK 2: Definition ===
(Component: TEMPLATE_C_BLOCK)
Title: تَعْرِيفُ الإِبْدَالِ
Content: <p class="text-accent text-justify">هو جَعْلُ حرفٍ مكانَ حَرْفٍ، سواء أكانَ الحرفُ صحيحاً أم معتلّاً.</p>

=== BLOCK 3: The Core Matrix (Summary Table) ===
(Component: TEMPLATE_C_TABLE)
Title: حَالَاتُ الإِبْدَالِ
Columns: ["الحَالَةُ", "التَّغْيِيرُ", "مِثَالٌ"]
Rows:
1. ["تَطَرُّفُ الوَاوِ/اليَاءِ بَعْدَ أَلِفٍ زَائِدَةٍ", "تُبْدَلُ هَمْزَةً", "كَسَاءٌ، بِنَاءٌ"]
2. ["وُقُوعُ الوَاوِ/اليَاءِ عَيْنًا فِي اسْمِ الفَاعِلِ (أَجْوَف)", "تُبْدَلُ هَمْزَةً", "قَائِلٌ، بَائِعٌ"]
3. ["وُقُوعُ حَرْفِ المَدِّ بَعْدَ أَلِفِ (فَعَائِل)", "يُبْدَلُ هَمْزَةً", "عَجَائِزُ، صَحَائِفُ"]
4. ["وُقُوعُ تَاءِ (افْتَعَلَ) بَعْدَ (ص/ض)", "تُبْدَلُ طَاءً", "اصْطَبَرَ، اضْطَرَّ"]
5. ["وُقُوعُ تَاءِ (افْتَعَلَ) بَعْدَ (ز)", "تُبْدَلُ دَالًا", "ازْدَهَرَ"]
6. ["وُقُوعُ الوَاوِ فَاءً فِي (افْتَعَلَ)", "تُبْدَلُ تَاءً", "اتَّصَلَ، اتَّقَدَ"]

=== BLOCK 4: First - Waw/Ya to Hamza ===
(Component: TEMPLATE_C_SPLIT)
Title: أَوَّلًا - إِبْدَالُ الوَاوِ وَاليَاءِ هَمْزَةً
Left (Examples):
- <span class="highlight-red">كَسَاءٌ</span> (أَصْلُهَا كَسَاوٌ)
- <span class="highlight-red">بِنَاءٌ</span> (أَصْلُهَا بِنَايٌ)
Right (Rule A):
<p class="text-justify">آ - إِذَا تَطَرَّفَتَا بَعْدَ أَلِفٍ زَائِدَةٍ؛ أَيْ إِذَا وَقَعَتَا فِي آخِرِ الكَلِمَةِ، وَكَانَتْ قَبْلَهُمَا أَلِفٌ زَائِدَةٌ.</p>

=== BLOCK 5: First - Waw/Ya to Hamza (Case B) ===
(Component: TEMPLATE_C_SPLIT)
Title: تَابِع - إِبْدَالُ الوَاوِ وَاليَاءِ هَمْزَةً
Left (Examples):
- <span class="highlight-red">عَائِدٌ</span> (عَاوِدٌ)
- <span class="highlight-red">صَائِدٌ</span> (صَايِدٌ)
Right (Rule B):
<p class="text-justify">ب - إِذَا وَقَعَتْ عَيْنًا (أَيْ إِذَا قَابَلَتِ الوَاوَ أَوِ اليَاءَ حَرْفُ العَيْنِ فِي المِيزَانِ الصَّرْفِيِّ) فِي اسْمِ الفَاعِلِ المَصُوغِ مِنَ الفِعْلِ الثُّلَاثِيِّ الأَجْوَفِ.</p>

=== BLOCK 6: Second - Mad Letter to Hamza ===
(Component: TEMPLATE_C_SPLIT)
Title: ثَانِيًا - إِبْدَالُ حَرْفِ المَدِّ هَمْزَةً
Left (Examples):
- <span class="highlight-red">عَجَائِزُ</span> (عَجَاوِزُ)
- <span class="highlight-red">قَصَائِدُ</span> (قَصَايِدُ)
Right (Rule):
<p class="text-justify">يُبْدَلُ حَرْفُ المَدِّ (...ي، ...و، ...ا) فِي المُفْرَدِ المُؤَنَّثِ هَمْزَةً إِذَا وَقَعَ بَعْدَ أَلِفِ صِيَغِ مُنْتَهَى الجُمُوعِ (فَعَائِلُ).</p>

=== BLOCK 7: Third - Ta of Ifta'ala to Ta (ط) ===
(Component: TEMPLATE_C_SPLIT)
Title: ثَالِثًا - إِبْدَالُ تَاءِ (افْتَعَلَ) طَاءً
Left (Examples):
- <span class="highlight-red">اضْطَرَّ</span> (اضْتَرَّ)
- <span class="highlight-red">اصْطَحَبَ</span> (اصْتَحَبَ)
Right (Rule):
<p class="text-justify">تُبْدَلُ تَاءُ (افْتَعَلَ) طَاءً إِذَا وَقَعَتْ بَعْدَ الضَّادِ أَوِ الصَّادِ.</p>

=== BLOCK 8: Fourth - Ta of Ifta'ala to Dal (د) ===
(Component: TEMPLATE_C_SPLIT)
Title: رَابِعًا - إِبْدَالُ تَاءِ (افْتَعَلَ) دَالًا
Left (Examples):
- <span class="highlight-red">ازْدَهَرَ</span> (ازْتَهَرَ)
Right (Rule):
<p class="text-justify">تُبْدَلُ تَاءُ (افْتَعَلَ) دَالًا إِذَا وَقَعَتْ بَعْدَ الزَّايِ.</p>

=== BLOCK 9: Fifth - Waw to Ta (ت) ===
(Component: TEMPLATE_C_SPLIT)
Title: خَامِسًا - إِبْدَالُ الوَاوِ تَاءً
Left (Examples):
- <span class="highlight-red">اتَّقَدَ</span> (اوْتَقَدَ)
Right (Rule):
<p class="text-justify">تُبْدَلُ الوَاوُ تَاءً إِذَا وَقَعَتْ فَاءً فِي صِيغَةِ (افْتَعَلَ).</p>

=== BLOCK 10: Solved Exercises (Applied Questions) ===
(Component: TEMPLATE_C_BLOCK)
Title: أَسْئِلَةٌ تَطْبِيقِيَّةٌ حَوْلَ الإِعْلَالِ وَالإِبْدَالِ
Content:
<div class="exercise-question mb-5mm">
  <p class="m-0 mb-2mm font-bold">س١- سَمِّ مَعَ التَّوْضِيحِ العِلَّةَ الصَّرْفِيَّةَ فِي كُلٍّ مِنْ: (قَالَ، عُدْ، دَنَا).</p>
  <p class="m-0 text-grey-dark">ج١- قَالَ: إِعْلَالٌ بِالقَلْبِ، قُلِبَتِ الوَاوُ أَلِفًا؛ لِتَحَرُّكِهَا بَعْدَ فَتْحٍ.<br>
  - عُدْ: إِعْلَالٌ بِالحَذْفِ، حُذِفَ حَرْفُ العِلَّةِ لِوُجُودِ سَاكِنٍ بَعْدَهُ.<br>
  - دَنَا: إِعْلَالٌ بِالقَلْبِ، قُلِبَتِ الوَاوُ أَلِفًا؛ لِتَحَرُّكِهَا بَعْدَ فَتْحٍ.</p>
</div>

<div class="exercise-question mb-5mm">
  <p class="m-0 mb-2mm font-bold">س٢- وَضِّحِ العِلَّةَ الصَّرْفِيَّةَ فِي كُلٍّ مِنْ: (غَزَتْ، يَزْدَهِي).</p>
  <p class="m-0 text-grey-dark">ج٢- غَزَتْ: إِعْلَالٌ بِالحَذْفِ، حُذِفَ حَرْفُ العِلَّةِ لِوُقُوعِهِ فِي آخِرِ الفِعْلِ المَاضِي الَّذِي اتَّصَلَتْ بِهِ تَاءُ التَّأْنِيثِ السَّاكِنَةُ.<br>
  - يَزْدَهِي: إِبْدَالٌ، أُبْدِلَتِ التَّاءُ دَالًا لِوُقُوعِهَا بَعْدَ الزَّايِ فِي صِيغَةِ (افْتَعَلَ، يَفْتَعِلُ).<br>
  - يَزْدَهِي: إِعْلَالٌ بِالتَّسْكِينِ، سُكِّنَتِ اليَاءُ لِتَطَرُّفِهَا بَعْدَ كَسْرٍ.</p>
</div>

<div class="exercise-question mb-5mm">
  <p class="m-0 mb-2mm font-bold">س٣- بَيِّنْ مَا أَصَابَ كَلِمَةَ: (صَائِدٌ) مِنْ تَغْيِيرٍ، وَاذْكُرْ نَوْعَهُ.</p>
  <p class="m-0 text-grey-dark">ج٣- صَائِدٌ: إِبْدَالٌ، أُبْدِلَتِ اليَاءُ هَمْزَةً؛ لِأَنَّهَا وَقَعَتْ عَيْنًا فِي صِيغَةِ اسْمِ الفَاعِلِ المَصُوغِ مِنَ الفِعْلِ الثُّلَاثِيِّ الأَجْوَفِ.</p>
</div>

<div class="exercise-question mb-5mm">
  <p class="m-0 mb-2mm font-bold">س٤- وَضِّحِ العِلَّةَ الصَّرْفِيَّةَ فِي كُلٍّ مِنَ الكَلِمَاتِ الآتِيَةِ: (سَائِلٌ "مِنَ الفِعْلِ سَالَ" - أَخْفِي - مُلْقَاةٌ).</p>
  <p class="m-0 text-grey-dark">ج٤- سَائِلٌ: إِبْدَالٌ، أُبْدِلَتِ اليَاءُ هَمْزَةً؛ لِأَنَّهَا وَقَعَتْ عَيْنًا فِي صِيغَةِ اسْمِ الفَاعِلِ المَصُوغِ مِنَ الفِعْلِ الثُّلَاثِيِّ الأَجْوَفِ.<br>
  - أَخْفِي: إِعْلَالٌ بِالتَّسْكِينِ، سُكِّنَتِ اليَاءُ لِأَنَّهَا تَطَرَّفَتْ بَعْدَ كَسْرٍ.<br>
  - مُلْقَاةٌ: إِعْلَالٌ بِالقَلْبِ، قُلِبَتِ اليَاءُ أَلِفًا؛ لِأَنَّهَا تَحَرَّكَتْ بَعْدَ فَتْحٍ.</p>
</div>

<div class="exercise-question mb-5mm">
  <p class="m-0 mb-2mm font-bold">س٥- حَدِّدِ العِلَّةَ الصَّرْفِيَّةَ فِيمَا يَأْتِي مَعَ التَّعْلِيلِ: كُنْتُ - أَتَاهُ.</p>
  <p class="m-0 text-grey-dark">ج٥- كُنْتُ: إِعْلَالٌ بِالحَذْفِ، حُذِفَ حَرْفُ العِلَّةِ لِوُجُودِ سَاكِنٍ بَعْدَهُ.<br>
  - أَتَاهُ: إِعْلَالٌ بِالقَلْبِ: قُلِبَتِ اليَاءُ أَلِفًا؛ لِأَنَّهَا جَاءَتْ مُتَحَرِّكَةً بَعْدَ فَتْحٍ.</p>
</div>

<div class="exercise-question mb-5mm">
  <p class="m-0 mb-2mm font-bold">س٦- بَيِّنِ العِلَّةَ الصَّرْفِيَّةَ فِي كُلٍّ مِنَ المُفْرَدَاتِ الآتِيَةِ: (يَصْطَلِكُ - يَضْطَرِبُ - غَائِصًا).</p>
  <p class="m-0 text-grey-dark">ج٦- يَصْطَلِكُ: إِبْدَالٌ: أُبْدِلَتِ التَّاءُ طَاءً؛ لِمَجِيئِهَا بَعْدَ الصَّادِ فِي صِيغَةِ (افْتَعَلَ).<br>
  - يَضْطَرِبُ: إِبْدَالٌ: أُبْدِلَتِ التَّاءُ طَاءً؛ لِمَجِيئِهَا بَعْدَ الضَّادِ فِي صِيغَةِ (افْتَعَلَ).<br>
  - غَائِصًا: إِبْدَالٌ: أُبْدِلَتِ الوَاوُ هَمْزَةً؛ لِأَنَّهَا وَقَعَتْ عَيْنًا فِي صِيغَةِ اسْمِ الفَاعِلِ المَصُوغِ مِنَ الفِعْلِ الثُّلَاثِيِّ الأَجْوَفِ.</p>
</div>

<div class="exercise-question mb-5mm">
  <p class="m-0 mb-2mm font-bold">س٧- بَيِّنْ نَوْعَ الإِعْلَالِ فِي كُلٍّ مِمَّا يَأْتِي: مَعَادٌ - أَعْطَتْ.</p>
  <p class="m-0 text-grey-dark">ج٧- مَعَادٌ: إِعْلَالٌ بِالقَلْبِ، قُلِبَتِ الوَاوُ أَلِفًا؛ لِتَحَرُّكِهَا بَعْدَ فَتْحٍ.<br>
  - أَعْطَتْ: إِعْلَالٌ بِالحَذْفِ، حُذِفَ حَرْفُ العِلَّةِ لِوُقُوعِهِ فِي آخِرِ الفِعْلِ المَاضِي الَّذِي اتَّصَلَتْ بِهِ تَاءُ التَّأْنِيثِ السَّاكِنَةِ.</p>
</div>

<div class="exercise-question mb-5mm">
  <p class="m-0 mb-2mm font-bold">س٨- حَدِّدِ العِلَّةَ الصَّرْفِيَّةَ فِيمَا يَأْتِي: (تَقَاضِي - اسْتَزِيدُ).</p>
  <p class="m-0 text-grey-dark">ج٨- تَقَاضِي: إِعْلَالٌ بِالتَّسْكِينِ؛ سُكِنَتِ اليَاءُ لِتَطَرُّفِهَا بَعْدَ كَسْرٍ.<br>
  - اسْتَزِيدُ: إِعْلَالٌ بِالتَّسْكِينِ، سُكِنَتِ اليَاءُ؛ لِتَحَرُّكِهَا بَعْدَ حَرْفٍ صَحِيحٍ سَاكِنٍ.</p>
</div>

--- END STREAM ---
