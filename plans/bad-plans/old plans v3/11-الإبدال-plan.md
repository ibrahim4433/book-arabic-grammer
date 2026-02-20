# **SESSION 11.0**

[TASK DEFINITION]
Objective: Implement Lesson 11: Al-Ibdal (Substitution).
File: `pages/11.0_n28_ibdal.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Page Breaking: Use `tools/verify_layout.py` after every block. If "FULL", continue in `pages/11.1_n29_ibdal.html`.
2. Content: 100% Arabic with full Harakat.
3. Highlighting: Use `.highlight-red` for the changed letter/substitute, `.highlight-blue` for the original letter/context.
4. Definitions: Must use `.text-accent` class.

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
Content:
<p class="text-accent text-center text-xl">
هُوَ جَعْلُ حَرْفٍ مَكَانَ حَرْفٍ، سَوَاءٌ أَكَانَ الحَرْفُ صَحِيحًا أَمْ مُعْتَلًّا.
</p>

=== BLOCK 3: The Ibdal Matrix (Summary) ===
(Component: TEMPLATE_C_TABLE)
Title: خُلَاصَةُ قَوَاعِدِ الإِبْدَالِ
Columns: [ "الحَالَةُ", "التَّغْيِيرُ", "مِثَالٌ" ]
Rows:
1. [ "تَطَرُّفُ (و، ي) بَعْدَ أَلِفٍ زَائِدَةٍ", "قَلْبُهَا هَمْزَةً", "سَمَاءٌ، بِنَاءٌ" ]
2. [ "وَقَعَتْ (و، ي) عَيْنًا لِاسْمِ فَاعِلٍ أَجْوَفَ", "قَلْبُهَا هَمْزَةً", "قَائِلٌ، بَائِعٌ" ]
3. [ "وَقَعَ حَرْفُ المَدِّ بَعْدَ أَلِفِ (فَعَائِل)", "قَلْبُهُ هَمْزَةً", "صَحَائِفُ، عَجَائِزُ" ]
4. [ "وَقَعَتْ تَاءُ (افْتَعَلَ) بَعْدَ (ص، ض، ط، ظ)", "قَلْبُهَا طَاءً", "اصْطَبَرَ، اضْطَرَّ" ]
5. [ "وَقَعَتْ تَاءُ (افْتَعَلَ) بَعْدَ (د، ذ، ز)", "قَلْبُهَا دَالًا", "ازْدَهَرَ، ادَّخَرَ" ]
6. [ "وَقَعَتْ فَاءُ (افْتَعَلَ) وَاوًا", "قَلْبُهَا تَاءً", "اتَّصَلَ، اتَّقَدَ" ]

=== BLOCK 4: Rule 1 - Swap to Hamza (Final Position) ===
(Component: TEMPLATE_C_SPLIT)
Title: أَوَّلًا: إِبْدَالُ الوَاوِ وَاليَاءِ هَمْزَةً (١)
Right_Content:
<h4 class="font-bold mb-2mm text-teal-800">١- إِذَا تَطَرَّفَتَا بَعْدَ أَلِفٍ زَائِدَةٍ</h4>
<p class="text-justify mb-2mm">
تُبْدَلُ الوَاوُ وَاليَاءُ <span class="highlight-red">هَمْزَةً</span> إِذَا وَقَعَتَا فِي آخِرِ الكَلِمَةِ، وَكَانَتْ قَبْلَهُمَا أَلِفٌ زَائِدَةٌ.
</p>
<div class="example-box bg-gray-50 p-2 rounded border-r-4 border-teal-500">
<p><strong>كِسَاءٌ:</strong> أَصْلُهَا <span class="highlight-blue">كِسَاوٌ</span> (يَكْسُو)، قُلِبَتِ الوَاوُ هَمْزَةً لِتَطَرُّفِهَا بَعْدَ أَلِفٍ.</p>
<p><strong>بِنَاءٌ:</strong> أَصْلُهَا <span class="highlight-blue">بِنَايٌ</span> (يَبْنِي)، قُلِبَتِ اليَاءُ هَمْزَةً لِتَطَرُّفِهَا بَعْدَ أَلِفٍ.</p>
</div>
Left_Content:
<h4 class="font-bold mb-2mm text-teal-800">٢- فِي اسْمِ الفَاعِلِ الأَجْوَفِ</h4>
<p class="text-justify mb-2mm">
إِذَا وَقَعَتِ (الوَاوُ أَوِ اليَاءُ) عَيْنًا فِي اسْمِ الفَاعِلِ مِنَ الفِعْلِ الثُّلَاثِيِّ الأَجْوَفِ.
</p>
<div class="example-box bg-gray-50 p-2 rounded border-r-4 border-teal-500">
<p><strong>عَائِدٌ:</strong> أَصْلُهَا <span class="highlight-blue">عَاوِدٌ</span> (عَادَ يَعُودُ).</p>
<p><strong>صَائِدٌ:</strong> أَصْلُهَا <span class="highlight-blue">صَايِدٌ</span> (صَادَ يَصِيدُ).</p>
</div>

=== BLOCK 5: Rule 2 - Plural Forms ===
(Component: TEMPLATE_C_BLOCK)
Title: ثَانِيًا: الإِبْدَالُ فِي صِيغَةِ مُنْتَهَى الجُمُوعِ
Content:
<p class="text-justify mb-4">
يُبْدَلُ حَرْفُ المَدِّ (الأَلِفُ، الوَاوُ، اليَاءُ) فِي المُفْرَدِ المُؤَنَّثِ <span class="highlight-red">هَمْزَةً</span> إِذَا وَقَعَ بَعْدَ أَلِفِ صِيَغِ مُنْتَهَى الجُمُوعِ (فَعَائِلُ).
</p>
<div class="grid grid-cols-2 gap-4">
    <div class="bg-gray-50 p-3 rounded">
        <span class="font-bold text-teal-700 block mb-1">عَجَائِزُ (عَجُوزٌ)</span>
        <p class="text-sm">أَصْلُهَا <span class="highlight-blue">عَجَاوِزُ</span>. جَذْرُهَا (عَجَزَ). قُلِبَتِ الوَاوُ هَمْزَةً لِوُقُوعِهَا بَعْدَ أَلِفِ الجَمْعِ.</p>
    </div>
    <div class="bg-gray-50 p-3 rounded">
        <span class="font-bold text-teal-700 block mb-1">قَصَائِدُ (قَصِيدَةٌ)</span>
        <p class="text-sm">أَصْلُهَا <span class="highlight-blue">قَصَايِدُ</span>. جَذْرُهَا (قَصَدَ). قُلِبَتِ اليَاءُ هَمْزَةً لِوُقُوعِهَا بَعْدَ أَلِفِ الجَمْعِ.</p>
    </div>
</div>

=== BLOCK 6: Break Point Check ===
(Component: SYSTEM_CHECK)
Protocol: If Page 11.0 > 80% Full, Start 11.1.
Most likely split here.

=== BLOCK 7: Rule 3 & 4 - Ifta'ala (Ta' Changes) ===
(Component: TEMPLATE_C_TABLE)
Title: ثَالِثًا وَرَابِعًا: إِبْدَالُ تَاءِ (افْتَعَلَ)
Columns: [ "القَاعِدَةُ", "الأَصْلُ (الوَزْن)", "التَّغْيِيرُ", "المِثَالُ" ]
Rows:
1. [ "بَعْدَ الضَّادِ (ض)", "اضْتَرَّ (افْتَعَلَ)", "ت ⟵ ط", "اضْطَرَّ" ]
2. [ "بَعْدَ الصَّادِ (ص)", "اصْتَحَبَ (افْتَعَلَ)", "ت ⟵ ط", "اصْطَحَبَ" ]
3. [ "بَعْدَ الزَّايِ (ز)", "ازْتَهَرَ (افْتَعَلَ)", "ت ⟵ د", "ازْدَهَرَ" ]
4. [ "بَعْدَ الدَّالِ (د)", "ادْتَخَرَ (افْتَعَلَ)", "ت ⟵ د", "ادَّخَرَ" ]

=== BLOCK 8: Rule 5 - Ifta'ala (Fa' Changes) ===
(Component: TEMPLATE_C_BLOCK)
Title: خَامِسًا: إِبْدَالُ فَاءِ (افْتَعَلَ)
Content:
<div class="flex items-center gap-4">
    <div class="flex-1 text-justify">
        تُبْدَلُ <span class="highlight-blue">الوَاوُ</span> <span class="highlight-red">تَاءً</span> إِذَا وَقَعَتْ فَاءً فِي صِيغَةِ (افْتَعَلَ)، ثُمَّ تُدْغَمُ فِي تَاءِ الافْتِعَالِ.
    </div>
    <div class="bg-teal-50 p-4 rounded-lg border border-teal-200 text-center w-1/3">
        <div class="font-bold text-xl mb-1">اتَّقَدَ</div>
        <div class="text-sm text-gray-600">أَصْلُهَا: <span class="highlight-blue">اوْتَقَدَ</span></div>
        <div class="text-xs text-gray-500 mt-1">(و) ⟵ (ت) ⟵ إِدْغَامٌ</div>
    </div>
</div>

=== BLOCK 9: Practical Application (Drills) ===
(Component: TEMPLATE_C_SPLIT)
Title: أَسْئِلَةٌ تَطْبِيقِيَّةٌ وَإِجَابَاتُهَا
Right_Content:
<h5 class="font-bold text-teal-800 border-b border-teal-100 pb-1 mb-2">س: بَيِّنِ العِلَّةَ الصَّرْفِيَّةَ (قَالَ، عُدْ، دَنَا)</h5>
<ul class="list-none space-y-2 text-sm">
    <li><span class="font-bold">قَالَ:</span> إِعْلَالٌ بِالقَلْبِ (و ⟵ ا) لِتَحَرُّكِهَا بَعْدَ فَتْحٍ.</li>
    <li><span class="font-bold">عُدْ:</span> إِعْلَالٌ بِالحَذْفِ (مَنْعًا لِالْتِقَاءِ السَّاكِنَيْنِ).</li>
    <li><span class="font-bold">دَنَا:</span> إِعْلَالٌ بِالقَلْبِ (و ⟵ ا).</li>
</ul>
Left_Content:
<h5 class="font-bold text-teal-800 border-b border-teal-100 pb-1 mb-2">س: وَضِّحِ الإِبْدَالِ فِي (يَزْدَهِي، صَائِدٌ)</h5>
<ul class="list-none space-y-2 text-sm">
    <li><span class="font-bold">يَزْدَهِي:</span> إِبْدَالٌ (ت ⟵ د) لِوُقُوعِهَا بَعْدَ زَايٍ.</li>
    <li><span class="font-bold">صَائِدٌ:</span> إِبْدَالٌ (ي ⟵ ء) لِوُقُوعِهَا عَيْنًا فِي اسْمِ الفَاعِلِ الأَجْوَفِ.</li>
</ul>

=== BLOCK 10: Exam ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: حَدِّدْ نَوْعَ الإِبْدَالِ وَسَبَبَهُ فِي الكَلِمَاتِ الآتِيَةِ: (اتَّصَلَ، سَمَاءٌ، مُدَّكِرٌ).

--- END STREAM ---