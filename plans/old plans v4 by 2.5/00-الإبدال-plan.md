# **SESSION 11.0**

[TASK DEFINITION]
Objective: Implement الإِبْدَالُ.
File: `pages/11.0_n28_ibdal.html`
Reference: Follow patterns in design_patterns.json and Sarf section rules.

[CONSTRAINTS & PROTOCOLS]
1. Page Breaking: Use `tools/verify_layout.py` after every major block. If the status is 'FULL' or 'OVERFLOW', close the current file and move the remaining content to `pages/11.1_n28_ibdal_cont.html`.
2. Content: 100% Arabic with full Harakat (Tashkeel) as provided in raw text.
3. Highlighting: Use `.highlight-red` for the changed letters (the result of Ibdal) and `.highlight-blue` for the original letters or roots.
4. Definitions: Must use the `.text-accent` class for the core definition text.
5. Atomic Components: Strictly use `TEMPLATE_C_...` snippets. Map lists to `TEMPLATE_C_LIST`.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER)
Title: الإِبْدَالُ
Lesson: ٢٨
Author: إِبْرَاهِيم أَبُو مُحَمَّد

=== BLOCK 2: Definition ===
(Component: TEMPLATE_C_BLOCK)
Title: تَعْرِيفُ الإِبْدَالِ
Content: <p class="text-accent">هُوَ جَعْلُ حَرْفٍ مَكَانَ حَرْفٍ، سَوَاءٌ أَكَانَ الحَرْفُ صَحِيحًا أَمْ مُعْتَلًّا.</p>

=== BLOCK 3: Case 1: Waw and Ya to Hamza ===
(Component: TEMPLATE_C_BLOCK)
Title: إِبْدَالُ الوَاوِ وَاليَاءِ هَمْزَةً
Content: <p>تُبْدَلُ الوَاوُ وَاليَاءُ هَمْزَةً فِي الحَالَتَيْنِ الآتِيَتَيْنِ:</p>
<ul class="structured-list">
    <li>إِذَا <span class="highlight-red">تَطَرَّفَتَا</span> بَعْدَ أَلِفٍ زَائِدَةٍ: مِثْلُ: <span class="highlight-blue">كَسَاءٌ</span> (أَصْلُهَا كَسَاوٌ)، <span class="highlight-blue">بِنَاءٌ</span> (أَصْلُهَا بِنَايٌ).</li>
    <li>إِذَا وَقَعَتَا <span class="highlight-red">عَيْنًا</span> فِي اسْمِ الفَاعِلِ المَصُوغِ مِنَ الفِعْلِ الثُّلَاثِيِّ الأَجْوَفِ: مِثْلُ: <span class="highlight-blue">عَائِدٌ</span> (أَصْلُهَا عَاوِدٌ)، <span class="highlight-blue">صَائِدٌ</span> (أَصْلُهَا صَايِدٌ).</li>
</ul>

=== BLOCK 4: Case 2: Mad Letter to Hamza ===
(Component: TEMPLATE_C_BLOCK)
Title: إِبْدَالُ حَرْفِ المَدِّ هَمْزَةً
Content: <p>يُبْدَلُ حَرْفُ المَدِّ (ي، و، ا) فِي المُفْرَدِ المُؤَنَّثِ هَمْزَةً إِذَا وَقَعَ بَعْدَ <span class="highlight-red">أَلِفِ صِيَغِ مُنْتَهَى الجُمُوعِ</span> (فَعَائِلُ):</p>
<p>مِثْلُ: <span class="highlight-blue">عَجَائِزُ</span> (أَصْلُهَا عَجَاوِزُ)، <span class="highlight-blue">قَصَائِدُ</span> (أَصْلُهَا قَصَايِدُ).</p>

=== BLOCK 5: Cases 3 & 4: Ta' of Ifta'ala ===
(Component: TEMPLATE_C_SPLIT)
Left Title: إِبْدَالُ التَّاءِ طَاءً
Left Content: <p>تُبْدَلُ تَاءُ (افْتَعَلَ) <span class="highlight-red">طَاءً</span> إِذَا وَقَعَتْ بَعْدَ الضَّادِ أَوِ الصَّادِ:</p>
<p>مِثْلُ: <span class="highlight-blue">اضْطَرَّ</span> (أَصْلُهَا اضْتَرَّ)، <span class="highlight-blue">اصْطَحَبَ</span> (أَصْلُهَا اصْتَحَبَ).</p>
Right Title: إِبْدَالُ التَّاءِ دَالًا
Right Content: <p>تُبْدَلُ تَاءُ (افْتَعَلَ) <span class="highlight-red">دَالًا</span> إِذَا وَقَعَتْ بَعْدَ الزَّايِ:</p>
<p>مِثْلُ: <span class="highlight-blue">ازْدَهَرَ</span> (أَصْلُهَا ازْتَهَرَ).</p>

=== BLOCK 6: Case 5: Waw to Ta' ===
(Component: TEMPLATE_C_BLOCK)
Title: إِبْدَالُ الوَاوِ تَاءً
Content: <p>تُبْدَلُ الوَاوُ تَاءً إِذَا وَقَعَتْ <span class="highlight-red">فَاءً</span> فِي صِيغَةِ (افْتَعَلَ):</p>
<p>مِثْلُ: <span class="highlight-blue">اتَّقَدَ</span> (أَصْلُهَا اوْتَقَدَ).</p>

=== BLOCK 7: Exam ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: بَيِّنْ مَا أَصَابَ كَلِمَةَ (صَائِدٌ) مِنْ تَغْيِيرٍ، وَاذْكُرْ نَوْعَهُ.
Answer: إِبْدَالٌ، أُبْدِلَتِ اليَاءُ هَمْزَةً؛ لِأَنَّهَا وَقَعَتْ عَيْنًا فِي صِيغَةِ اسْمِ الفَاعِلِ المَصُوغِ مِنَ الفِعْلِ الثُّلَاثِيِّ الأَجْوَفِ.

--- END STREAM ---