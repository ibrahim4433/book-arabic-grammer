# **SESSION 09.0**

[TASK DEFINITION]
Objective: Implement المِيزَانُ الصَّرْفِيُّ.
File: `pages/09.0_n28_mizan_sarfi.html`
Reference: Follow patterns in design_patterns.json and BOOK_RULES.md.

[CONSTRAINTS & PROTOCOLS]
1. Page Breaking: Use `tools/verify_layout.py` after every block. If "FULL", continue in `pages/09.1_...`.
2. Content: 100% Arabic with full Harakat.
3. Highlighting: Use `.highlight-red` for primary focus words (Harakat/Endings) and `.highlight-blue` for particles.
4. Definitions: Must use `.text-accent` class for the main explanatory text.
5. Numerals: Use Arabic-Indic digits (٩, ٢٨).

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER)
Title: المِيزَانُ الصَّرْفِيُّ
Lesson: ٩
Author: إِبْرَاهِيم أَبُو مُحَمَّد

=== BLOCK 2: التعريف بالصرف ===
(Component: TEMPLATE_C_BLOCK)
Title: تَعْرِيفُ الصَّرْفِ
Content: <p class="text-accent">الصَّرْفُ عِلْمٌ يَبْحَثُ فِي بِنْيَةِ الكَلِمَةِ العَرَبِيَّةِ المُفْرَدَةِ قَبْلَ أَنْ تَدْخُلَ فِي تَرْكِيبِ الكَلَامِ، وَوَزْنِهَا، وَتَغَيُّرَاتِهَا مِنْ شَكْلٍ إِلَى آخَرَ.</p>
<p>وَأَهَمُّ مَا يُدْرَسُ فِيهِ: (المِيزَانُ الصَّرْفِيُّ لِلكَلِمَةِ، مَعَانِي أَحْرُفِ الزِّيَادَةِ، الإِعْلَالُ، الإِبْدَالُ، المُشْتَقَّاتُ، المَصَادِرُ، ..).</p>

=== BLOCK 3: تعريف الميزان الصرفي ===
(Component: TEMPLATE_C_BLOCK)
Title: المِيزَانُ الصَّرْفِيُّ
Content: <p class="text-accent">هُوَ مِقْيَاسٌ لِمَعْرِفَةِ حُرُوفِ الكَلِمَةِ، يَتَأَلَّفُ مِنْ ثَلَاثَةِ أَحْرُفٍ (ف، ع، ل) تُقَابِلُ الأُصُولَ الثَّلَاثَةَ الَّتِي تَتَكَوَّنُ مِنْهَا أَغْلَبُ الكَلِمَاتِ العَرَبِيَّةِ.</p>

=== BLOCK 4: جدول الميزان الأساسي ===
(Component: TEMPLATE_C_TABLE)
Title: جَدْوَلُ المِيزَانِ لِلفِعْلِ الثُّلَاثِيِّ
Headers: ["حُرُوفُ المِيزَانِ", "فَاءُ الفِعْلِ", "عَيْنُ الفِعْلِ", "لَامُ الفِعْلِ"]
Row 1: ["الكَلِمَةُ", "ضَـ", "ـرَ", "بَ"]
Row 2: ["المِيزَانُ الصَّرْفِيُّ", "فَـ", "ـعَ", "لَ"]

=== BLOCK 5: الرباعي والخماسي المجرد ===
(Component: TEMPLATE_C_BLOCK)
Title: مِيزَانُ الرُّبَاعِيِّ وَالخُمَاسِيِّ المِجَرَّدِ
Content: 
<ul class="structured-list">
    <li><span class="marker">•</span> إِذَا كَانَتْ حُرُوفُ الكَلِمَةِ الأَصْلِيَّةُ <span class="highlight-red">أَرْبَعَةَ حُرُوفٍ</span>، نُكَرِّرُ اللَّامَ فِي آخِرِ المِيزَانِ (فَعْلَلَ). مِثْلُ: بَعْثَرَ ⇐ فَعْلَلَ.</li>
    <li><span class="marker">•</span> إِذَا كَانَتْ حُرُوفُ الكَلِمَةِ الأَصْلِيَّةُ <span class="highlight-red">خَمْسَةَ حُرُوفٍ</span>، نَزِيدُ لَامَيْنِ فِي آخِرِ المِيزَانِ (فَعَلَّل). مِثْلُ: غَضَنْفَر ⇐ فَعَلَّل، زَبَرْجَد ⇐ فَعَلَّل.</li>
</ul>

=== BLOCK 6: حروف الزيادة ===
(Component: TEMPLATE_C_SPLIT)
Left_Title: الزِّيَادَةُ بِالتَّكْرِيرِ
Left_Content: إِذَا كَانَ الحَرْفُ الزَّائِدُ نَاتِجًا عَنْ تَكْرِيرِ حَرْفٍ أَصْلِيٍّ، كَرَّرْنَا مَا يُقَابِلُهُ فِي المِيزَانِ. مِثْلُ: <span class="highlight-blue">سَبَّحَ</span> ⇐ <span class="highlight-red">فَعَّلَ</span>.
Right_Title: الزِّيَادَةُ بِحُرُوفِ (سألتمونيها)
Right_Content: إِذَا كَانَ الحَرْفُ الزَّائِدُ غَيْرَ أَصْلِيٍّ، نَذْكُرُهُ كَمَا هُو فِي المِيزَانِ. مِثْلُ: <span class="highlight-blue">كَاتَبَ</span> ⇐ <span class="highlight-red">فَاعَلَ</span>، <span class="highlight-blue">اسْتَفْتَحَ</span> ⇐ <span class="highlight-red">اسْتَفْعَلَ</span>.

=== BLOCK 7: Exam ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: زِنِ الكَلِمَاتِ الآتِيَةَ: (دَحْرَجَ، جَلْبَبَ، انْكَسَرَ).

--- END STREAM ---