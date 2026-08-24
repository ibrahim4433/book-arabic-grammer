# **SESSION 04.0**

[TASK DEFINITION]
Objective: Implement اسلوب الاستثناء.
File: `pages/04.0_nXX_اسلوب الاستثناء.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 04
[CHAPTER_TITLE]: اسلوب الاستثناء
[CATEGORY_HEADER]: 04
[SECTION_HEADER]: 04
[AUTHOR_NAME]: أ. حنا خفيف
[AUTHOR_PHONE]:

=== BLOCK 2: أسلوب الاستثناء ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أُسْلُوبُ الِاسْتِثْنَاءِ
Content: <p class="text-accent text-lg font-bold">الِاسْتِثْنَاءُ:</p> <p>إِخْرَاجُ مَا بَعْدَ <span class="highlight-blue">"إِلَّا"</span> أَوْ إِحْدَى أَخَوَاتِهَا مِنْ أَدَوَاتِ الِاسْتِثْنَاءِ مِنْ حُكْمِ مَا قَبْلَهُ. وَالْمُخْرَجُ يُسَمَّى <span class="highlight-red">"الْمُسْتَثْنَى"</span> وَالْمُخْرَجُ مِنْهُ يُسَمَّى <span class="highlight-red">"الْمُسْتَثْنَى مِنْهُ"</span>. وَلِلِاسْتِثْنَاءِ أَدَوَاتٌ، مِنْهَا: <span class="highlight-green">(إِلَّا، غَيْرُ، سِوَى، خَلَا، عَدَا)</span>.</p>

=== BLOCK 3: أحكام المستثنى ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَحْكَامُ الْمُسْتَثْنَى
Content:
<ul class="structured-list">
<li><span class="text-primary font-bold">١- وَاجِبُ النَّصْبِ:</span> إِذَا كَانَ الِاسْتِثْنَاءُ تَامًّا مُثْبَتًا (يَتَضَمَّنُ أَرْكَانَ الِاسْتِثْنَاءِ الثَّلَاثَةَ، وَلَا يُسْبَقُ بِنَفْيٍ): <br> (حَضَرَ الطَّلَّابُ <span class="highlight-blue">إِلَّا</span> <span class="highlight-red">خَالِدًا</span>)، (حَضَرَ الطَّلَّابُ <span class="highlight-blue">غَيْرَ</span> <span class="highlight-red">خَالِدٍ</span>)، (حَضَرَ الطَّلَّابُ <span class="highlight-blue">سِوَى</span> <span class="highlight-red">خَالِدٍ</span>).</li>
<li><span class="text-primary font-bold">٢- جَائِزُ النَّصْبِ عَلَى الِاسْتِثْنَاءِ، أَوِ الْإِتْبَاعِ عَلَى الْبَدَلِيَّةِ:</span> إِذَا كَانَ الِاسْتِثْنَاءُ تَامًّا مَنْفِيًّا (يَتَضَمَّنُ أَرْكَانَ الِاسْتِثْنَاءِ الثَّلَاثَةَ، وَيُسْبَقُ بِنَفْيٍ): <br> (<span class="highlight-blue">مَا</span> حَضَرَ الطَّلَّابُ <span class="highlight-blue">إِلَّا</span> <span class="highlight-red">خَالِدًا/خَالِدٌ</span>)، (<span class="highlight-blue">مَا</span> حَضَرَ الطَّلَّابُ <span class="highlight-blue">غَيْرَ/غَيْرُ</span> <span class="highlight-red">خَالِدٍ</span>)، (<span class="highlight-blue">مَا</span> حَضَرَ الطَّلَّابُ <span class="highlight-blue">سِوَى</span> <span class="highlight-red">خَالِدٍ</span>).</li>
<li><span class="text-primary font-bold">٣- وَاجِبُ الْإِعْرَابِ بِحَسَبِ مَوْقِعِهِ:</span> إِذَا كَانَ الِاسْتِثْنَاءُ نَاقِصًا مَنْفِيًّا (يُحْذَفُ مِنْهُ (الْمُسْتَثْنَى مِنْهُ)، وَيُسْبَقُ بِنَفْيٍ):</li>
</ul>

=== BLOCK 4: تنبيه (ملاحظات إعرابية) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: تَنْبِيهٌ وَمُلَاحَظَاتٌ إِعْرَابِيَّةٌ
Content: <p><span class="text-primary font-bold">١ - أَدَوَاتُ الشَّرْطِ الظَّرْفِيَّاتُ:</span> <span class="highlight-blue">(إِذَا - لَمَّا - كُلَّمَا - مَتَى - أَيَّانَ - أَيْنَمَا - أَنَّى - حَيْثُمَا)</span>. ٢ - الظَّرْفُ غَيْرُ الْمُنَوَّنِ.</p> <p>تُعْرَبُ جُمْلَةُ جَوَابِ الشَّرْطِ فِي مَحَلِّ جَزْمٍ، إِذَا كَانَتْ أَدَاةُ الشَّرْطِ جَازِمَةً، وَكَانَ الْجَوَابُ مُقْتَرِنًا بِالْفَاءِ. وَيَجِبُ أَنْ يَتَحَقَّقَ هَذَانِ الشَّرْطَانِ مَعًا.</p> <p><span class="text-primary font-bold">٦- الْجُمْلَةُ الْوَاقِعَةُ فِي مَحَلِّ جَزْمِ جَوَابِ الشَّرْطِ:</span> مَحَلُّهَا بِحَسَبِ مَحَلِّ الْجُمْلَةِ الْمَعْطُوفِ عَلَيْهَا. وَيَنْبَغِي الِانْتِبَاهُ إِلَى أَنَّ الْجُمْلَةَ الْمَعْطُوفَةَ لَا تَتْبَعُ الْجُمْلَةَ الْمَعْطُوفَ عَلَيْهَا إِلَّا بِالْمَحَلِّ الْإِعْرَابِيِّ.</p> <p><span class="text-primary font-bold">ثَانِيًا:</span> الْجُمَلُ الَّتِي لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.</p>

=== BLOCK 5: أمثلة الاستثناء الناقص ===
(Component: TEMPLATE_C_BENEFIT.html)
Title: أَمْثِلَةُ الِاسْتِثْنَاءِ النَّاقِصِ الْمَنْفِيِّ
Content: <p>(<span class="highlight-blue">مَا</span> حَضَرَ <span class="highlight-blue">إِلَّا</span> <span class="highlight-red">خَالِدٌ</span>)، (<span class="highlight-blue">مَا</span> حَضَرَ <span class="highlight-blue">غَيْرُ</span> <span class="highlight-red">خَالِدٍ</span>)، (<span class="highlight-blue">مَا</span> حَضَرَ <span class="highlight-blue">سِوَى</span> <span class="highlight-red">خَالِدٍ</span>).</p>

=== BLOCK 6: حكم غير وسوى ===
(Component: TEMPLATE_C_BLOCK.html)
Title: حُكْمُ (غَيْر وَسِوَى) فِي الْإِعْرَابِ
Content:
<ul class="structured-list">
<li><span class="text-primary font-bold">١- تُعْرَبَانِ إِعْرَابَ الِاسْمِ الْوَاقِعِ بَعْدَ إِلَّا إِذَا كَانَ الِاسْتِثْنَاءُ تَامًّا:</span> فَفِي الِاسْتِثْنَاءِ التَّامِّ الْمُثْبَتِ تُعْرَبُ كُلٌّ مِنْهُمَا: <span class="highlight-red">اسْمًا مَنْصُوبًا عَلَى الِاسْتِثْنَاءِ</span>، وَيُعْرَبُ مَا بَعْدَهُمَا <span class="highlight-blue">(مُضَافًا إِلَيْهِ)</span>. وَفِي الِاسْتِثْنَاءِ التَّامِّ الْمَنْفِيِّ تُعْرَبُ كُلٌّ مِنْهُمَا: <span class="highlight-red">اسْمًا مَنْصُوبًا عَلَى الِاسْتِثْنَاءِ، أَوْ بَدَلًا</span>، وَيُعْرَبُ مَا بَعْدَهُمَا <span class="highlight-blue">(مُضَافًا إِلَيْهِ)</span>.</li>
<li><span class="text-primary font-bold">٢- تُعْرَبَانِ بِحَسَبِ مَوْقِعِهِمَا:</span> إِذَا كَانَ الِاسْتِثْنَاءُ نَاقِصًا مَنْفِيًّا، وَيُعْرَبُ مَا بَعْدَهُمَا <span class="highlight-blue">(مُضَافًا إِلَيْهِ)</span>.</li>
</ul>

=== BLOCK 7: حكم خلا وعدا ===
(Component: TEMPLATE_C_BLOCK.html)
Title: حُكْمُ الْمُسْتَثْنَى بِـ "خَلَا" وَ"عَدَا"
Content:
<p><span class="text-accent font-bold">خَلَا وَعَدَا:</span> فِعْلَانِ مَاضِيَانِ ضُمِّنَا مَعْنَى <span class="highlight-blue">"إِلَّا"</span> الِاسْتِثْنَائِيَّةِ، وَحُكْمُ الْمُسْتَثْنَى بِهِمَا جَوَازُ نَصْبِهِ وَجَرِّهِ؛ <span class="highlight-red">النَّصْبُ</span> عَلَى أَنَّهُمَا فِعْلَانِ مَاضِيَانِ، وَمَا بَعْدَهُمَا مَفْعُولٌ بِهِ. وَ<span class="highlight-red">الْجَرُّ</span> عَلَى أَنَّهُمَا حَرْفَا جَرٍّ زَائِدَانِ، وَالْجَارُّ وَالْمَجْرُورُ لَا مُتَعَلَّقَ لَهُمَا؛ لِأَنَّهُمَا حَرْفَا جَرٍّ زَائِدَانِ. <br>نَحْوَ: حَضَرَ الطُّلَّابُ <span class="highlight-blue">عَدَا</span> طَالِبًا/طَالِبٍ.</p>
<p>· إِذَا اقْتَرَنَتْ بِـ <span class="highlight-blue">"خَلَا"</span> وَ<span class="highlight-blue">"عَدَا"</span> (مَا) الْمَصْدَرِيَّةُ، كَانَتَا فِعْلَيْنِ مَاضِيَيْنِ، وَمَا بَعْدَهُمَا مَفْعُولًا بِهِ، وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْ (مَا) وَالْفِعْلِ (عَدَا) أَوْ (خَلَا) فِي مَحَلِّ نَصْبِ حَالٍ. <br>نَحْوَ: حَضَرَ الطُّلَّابُ <span class="highlight-blue">مَا عَدَا</span> طَالِبًا.</p>

=== BLOCK 8: مصفوفة الخلاصة ===
(Component: TEMPLATE_C_TABLE.html)
Title: خُلَاصَةُ أَحْكَامِ الِاسْتِثْنَاءِ
Content:
<table class="dense-table">
<thead>
<tr>
<th>نَوْعُ الِاسْتِثْنَاءِ</th>
<th>الْأَدَاةُ</th>
<th>حُكْمُ الْمُسْتَثْنَى</th>
</tr>
</thead>
<tbody>
<tr>
<td>تَامٌّ مُثْبَتٌ</td>
<td>إِلَّا</td>
<td>وَاجِبُ النَّصْبِ</td>
</tr>
<tr>
<td>تَامٌّ مَنْفِيٌّ</td>
<td>إِلَّا</td>
<td>جَائِزُ النَّصْبِ أَوْ بَدَلٌ</td>
</tr>
<tr>
<td>نَاقِصٌ مَنْفِيٌّ</td>
<td>إِلَّا</td>
<td>حَسَبَ مَوْقِعِهِ</td>
</tr>
<tr>
<td>جَمِيعُ الْحَالَاتِ</td>
<td>غَيْر/سِوَى</td>
<td>مُضَافٌ إِلَيْهِ مَجْرُورٌ</td>
</tr>
<tr>
<td>بِدُونِ (مَا) الْمَصْدَرِيَّةِ</td>
<td>خَلَا/عَدَا</td>
<td>مَفْعُولٌ بِهِ (نَصْبٌ) أَوْ اسْمٌ مَجْرُورٌ</td>
</tr>
<tr>
<td>مَعَ (مَا) الْمَصْدَرِيَّةِ</td>
<td>مَا خَلَا/مَا عَدَا</td>
<td>مَفْعُولٌ بِهِ (نَصْبٌ)</td>
</tr>
</tbody>
</table>

=== BLOCK 9: Exam ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
Number: ١
Question: أَسْئِلَةُ أُسْلُوبِ الِاسْتِثْنَاءِ الْوَارِدَةُ فِي الدَّوْرَاتِ الِامْتِحَانِيَّةِ السَّابِقَةِ:<br>سُؤَالُ الدَّوْرَةِ الْأُولَى (٢٠٢٤ عِلْمِيّ):<br>ضَعْ كَلِمَةَ (غَيْر) بَدَلًا مِنْ (إِلَّا) فِي الْجُمْلَةِ الْآتِيَةِ: (مَا كُرِّمَ فِي الْمُسَابَقَةِ إِلَّا نَبِيلٌ)، وَأَجْرِ التَّغْيِيرَ اللَّازِمَ مُرَاعِيًا الضَّبْطَ الصَّحِيحَ.
Answer: إِجَابَاتُ أَسْئِلَةِ أُسْلُوبِ الِاسْتِثْنَاءِ الْوَارِدَةِ فِي الدَّوْرَاتِ الِامْتِحَانِيَّةِ السَّابِقَةِ:<br>جَوَابُ سُؤَالِ الدَّوْرَةِ الْأُولَى (٢٠٢٤ عِلْمِيّ): - مَا كُرِّمَ فِي الْمُسَابَقَةِ غَيْرَ نَبِيلٍ (٢ دَرَجَةٌ) لِضَبْطِ كُلِّ كَلِمَةٍ (٤ دَرَجَاتٍ).

=== BLOCK 10: تتمة ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مُقَدِّمَةُ الدَّرْسِ التَّالِي
Content: <p class="text-accent font-bold text-center">أُسْلُوبُ الْمَدْحِ وَالذَّمِّ</p>

--- END STREAM ---
