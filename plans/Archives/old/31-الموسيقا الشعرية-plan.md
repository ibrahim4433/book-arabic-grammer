# **SESSION 31.0**

[TASK DEFINITION]
Objective: Implement الموسيقا الشعرية.
File: `pages/31.0_nXX_الموسيقا الشعرية.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/31.1_...` if page have a lot of blank space add exam elements from the lesson.
3. text Content: 100% Arabic with full Harakat.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green`  for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   **Rule:** NO INLINE STYLES.
*   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
*   **Mapping:**
    *   `style="width: 20%"` -> `class="w-20pct"`
    *   `style="margin-top: 2mm"` -> `class="mt-2mm"`
    *   `style="text-align: center"` -> `class="text-center"`
    *   `style="font-weight: bold"` -> `class="font-bold"`
6. Templates: You are forbidden from inventing new HTML tags or classes or template elements. You must map all content using "Jules-workspace/Templates/" components as the STREAM says in suitable way.
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). use "Jules-workspace/id_manager.py" to generate or verify them.
8. **Self-Correction:** Run "Jules-workspace/lint_pages.py" after creating html files. If it fails, you MUST fix the errors (usually inline styles) before submitting.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...) .
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER)
[LESSON_NUMBER]: 31
[CHAPTER_TITLE]: الموسيقا الشعرية
[CATEGORY_HEADER]: فوائد
[SECTION_HEADER]: المستوى الفني
[AUTHOR_NAME]: أ. حنا خفيف
[AUTHOR_PHONE]:  

=== BLOCK 2: Introduction to Poetic Music ===
(Component: TEMPLATE_C_BLOCK)
Title: أقسام الموسيقا الشعرية
Content:
<p class="mb-4">تَنْقَسِمُ المُوسِيقا الشِّعْرِيَّةُ في النَّصِّ الشِّعْرِيِّ قِسْمَينِ: <span class="text-accent font-bold">المُوسِيقا الخارِجِيَّةِ</span>، و<span class="text-accent font-bold">المُوسِيقا الدَّاخِلِيَّةِ</span>.</p>

=== BLOCK 3: External Music Definitions (Intro) ===
(Component: TEMPLATE_C_BLOCK)
Title: أولاً: الموسيقا الخارجية
Content:
<p class="mb-2">تَتَمَثَّلُ المُوسِيقا الخارِجِيَّةِ في الأَوْزانِ الشِّعْرِيَّةِ العَرَبِيَّةِ المَعْرُوفَةِ (البُحُورِ)، والقافِيَةِ، وحَرْفِ الرَّوِيِّ.</p>

=== BLOCK 3b: Definitions List ===
(Component: TEMPLATE_C_LIST)
Title: تعريفات القافية والروي
[LIST_ITEMS]:
<li>
    <span class="marker">•</span>
    <span><span class="font-bold text-primary">القافِيَةُ:</span> هِيَ أَقْرَبُ ساكِنٍ، إِلى السَّاكِنِ الأَخِيرِ (في نِهايَةِ الشَّطْرِ الثَّانِي) مَعَ الحَرْفِ المُتَحَرِّكِ قَبْلَهُ.</span>
</li>
<li>
    <span class="marker">•</span>
    <span><span class="font-bold text-primary">حَرْفُ الرَّوِيِّ:</span> هُوَ الحَرْفُ الذِي تُبْنَى عَلَيهِ القَصِيدَةُ، وَتُنْسَبُ إِلَيْهِ، ويكونُ واحِدًا في نِهايَةِ الأَبْياتِ جَمِيعِها.</span>
</li>
[NOTE_TITLE]: مثال توضيحي
[NOTE_TEXT]:
<p class="mb-1">أَيُّهَذا الشَّــــاكِي وَمَا بِكَ دَاءُ &nbsp;&nbsp;&nbsp; كُنْ جَمِيـــلًا تَرَ الوجُودَ جَمِيـــلًا</p>
<p class="text-sm">- القافِيَةُ: (مِيلا = /ه/ه).<br>- حَرْفُ الرَّوِيِّ: اللَّامُ المَفْتُوحَةُ المُشْبَعَةُ أَلِفًا (فالقَصِيدَةُ لامِيَّةٌ).</p>

=== BLOCK 4: Rhyme Types Table ===
(Component: TEMPLATE_C_TABLE)
Title: أنواع القافية
[TABLE_HEADERS]:
<th>النوع</th>
<th>التعريف</th>
<th>مثال</th>
[TABLE_ROWS]:
<tr>
    <td class="font-bold text-primary">القافِيَةُ المُطْلَقَةُ</td>
    <td>وهِيَ التِي يكونُ فِيها حَرْفُ الرَّوِيِّ <span class="text-accent">مُتَحَرِّكًا</span> بِفَتْحٍ أو ضَمٍّ أو كَسْرٍ. تَتَضَمَّنُ حَرْفَ وَصْلٍ (الواو، أو الياء، أو الألف، أو الهاء).</td>
    <td>
        <p>ذَخَرْتُ لِأَحْداثِ الزَّمانِ يَراعــــــا</p>
        <p>يُجِيدُ نِضــــالًا دُونَها وقِراعًا</p>
        <p class="text-xs mt-1 text-grey-dark">(الرَّوِيُّ: العين المفتوحة، الوصل: الألف)</p>
    </td>
</tr>
<tr>
    <td class="font-bold text-primary">القافِيَةُ المُقَيَّدَةُ</td>
    <td>التِي يَكونُ فِيها حَرْفُ الرَّوِيِّ <span class="text-accent">مُقَيَّدًا (ساكِنًا)</span>. لا يُوجَدُ فِيها حَرْفُ وَصْلٍ.</td>
    <td>
        <p>وَمَرَّتْ حَياتِي مَرَّتْ صَـــدَى</p>
        <p>وَلا شَــــيْءَ يُطْفِئُ نارَ الحَنِيــــــنْ</p>
        <p class="text-xs mt-1 text-grey-dark">(الرَّوِيُّ: النون الساكنة)</p>
    </td>
</tr>

=== BLOCK 5: Connectors Benefit ===
(Component: TEMPLATE_C_BENEFIT_TIP)
Title: حروف الوصل
Content:
يَنبَغِي أَنْ نُدْرِكَ أَنَّ حَرْفَ الرَّوِيِّ قَدْ يَرِدُ بَعْدَهُ حَرْفٌ مِنْ حُرُوفِ الوَصْلِ الأَرْبَعَةِ الآتِيَةِ: <span class="font-bold text-red-700">(ا ، و ، ي ، هـ)</span>.
<br>مثال: "لَيسَ الصَّدِيقُ الذي أعطاكَ شاهِدَهُ ... وخانَ الغَيْبَ غائِبُهُ" (الروي: الباء المضمومة، الوصل: الهاء).

=== BLOCK 6: Internal Music Intro ===
(Component: TEMPLATE_C_BLOCK)
Title: ثانياً: الموسيقا الداخلية
Content:
<p class="mb-2">تَنْبُعُ مِن مَصادِرَ مُتنوِّعَةٍ، منها:</p>

=== BLOCK 6b: Sources List ===
(Component: TEMPLATE_C_LIST)
Title: مصادر الموسيقا الداخلية
[LIST_ITEMS]:
<li>
    <span class="marker">1</span>
    <span><span class="font-bold text-primary">حُرُوفُ الهَمْسِ وحُرُوفُ الجَهْرِ:</span> حُرُوفُ الهَمْسِ مَجمُوعَةٌ في عِبارَة: (<span class="text-accent">سَكَتَ فَحَثَّهُ شَخْصٌ</span>). والباقي جَهْرٌ.</span>
</li>
<li>
    <span class="marker">2</span>
    <span><span class="font-bold text-primary">التِّكرارُ:</span> يَكونُ بِتِكرار الحُرُوفِ، أو الكَلِماتِ، أو التَّراكِيبِ، أو التَّنوينِ.</span>
</li>
<li>
    <span class="marker">3</span>
    <span><span class="font-bold text-primary">التَّناغُمُ بَين حُرُوفِ المَدِّ الطَّويلِ والقصيرِ:</span> المَدُّ الطَّويلُ (ا، و، ي مسبوقة بحركة مجانسة)، والقصير (الحركات).</span>
</li>
<li>
    <span class="marker">4</span>
    <span><span class="font-bold text-primary">الصِّيَغُ الاشْتِقاقِيَّةُ:</span> الكَلِماتُ التي تَنْتَمِي إلى جَذْرٍ لُغَوِيٍّ واحِدٍ (دَخَلَ، كاتِبٌ، كِتابًا).</span>
</li>

=== BLOCK 7: Verbal Enhancements Table ===
(Component: TEMPLATE_C_TABLE)
Title: المُحَسِّناتُ اللَّفْظِيَّةُ
[TABLE_HEADERS]:
<th>المحسن</th>
<th>التعريف</th>
[TABLE_ROWS]:
<tr>
    <td class="font-bold text-primary">الجِناسُ</td>
    <td>اتِّفاقُ الكَلِمَتَينِ في اللَّفظِ، واختِلافُهُما في المَعنى.</td>
</tr>
<tr>
    <td class="font-bold text-primary">التَّصرِيعُ</td>
    <td>تَطابُقُ العَرُوضِ والضَّرْبِ وَزْنًا، وتَقْفِيةً، وإعرابًا (لازِمٌ في مَطلَعِ القَصيدةِ غالِبًا).</td>
</tr>
<tr>
    <td class="font-bold text-primary">السَّجْعُ</td>
    <td>تَوافُقُ الأحرُفِ الأَخيرةِ في نِهاياتِ الجُمَلِ في النَّثْرِ خاصَّةً.</td>
</tr>
<tr>
    <td class="font-bold text-primary">التَّوازُنُ</td>
    <td>اتِّفاقُ الكَلِمَتَينِ في الوَزْنِ في أواخِرِ الفِقْرَتَينِ (قد يكون مسجوعاً).</td>
</tr>
<tr>
    <td class="font-bold text-primary">التَّقابُلُ (الطباق والمقابلة)</td>
    <td>اجتِماعُ كَلِمَتَينِ (طباق) أو عِبارَتَينِ (مقابلة) مُتضادَّتَينِ في المَعْنَى.</td>
</tr>

=== BLOCK 8: Internal Rhyme ===
(Component: TEMPLATE_C_BLOCK)
Title: 7- التَّقْفِيَةُ الدَّاخِلِيَّةُ
Content:
<p class="mb-2 text-accent">هي تَشابُهُ نِهاياتِ الكَلِماتِ في الشِّعْرِ (تُقابِلُ السَّجْعَ في النَّثرِ). وهي مَنبَعٌ ثَرٌّ لِلمُوسيقا الدَّاخِلِيَّةِ (موسيقا الحشو).</p>
<p class="mb-2">لها شكلان:</p>
<div class="flex flex-col gap-2mm">
    <div class="p-2mm bg-grey-lighter border-r-4 border-primary rounded">
        <span class="font-bold text-primary">الشكل الأول:</span> في نهايات العبارات الشعرية (الأكثر تأثيراً).
        <br>مثال (شوقي): "يا مَرْحبًا بالسُّلَّهْ، والرقَبِ المُطِلَّهْ، الكافِيَاتِ الذِّلَّهْ".
    </div>
    <div class="p-2mm bg-grey-lighter border-r-4 border-accent rounded">
        <span class="font-bold text-accent">الشكل الثاني:</span> تتجاوز النهايات أو تتقارب في الأبيات (الأقل تأثيراً).
        <br>مثال (أمل دنقل): "(قُلْتُ لَهُمْ ما قُلْتُ عَنْ مَسِيرَةِ الأَشْجارْ ... فاسْتَضْحَكُوا مِنْ وَهْمِكِ الثَّرْثَارْ)".
    </div>
</div>

=== BLOCK 9: Applied Example 1 (Nazik) ===
(Component: TEMPLATE_C_POEM)
Poet: نازِكُ الملائِكَةُ
Verse 1: هُناكَ يَظَلُّ الرَّبيعُ رَبِيعًا      يُظَلِّلُ سُكَّانَ يوتوبيا

=== BLOCK 10: Analysis 1 ===
(Component: TEMPLATE_C_LIST)
Title: تحليل الموسيقا في المثال الأول
[LIST_ITEMS]:
<li>
    <span class="marker">•</span>
    <span><span class="font-bold text-primary">الجناس/المحسن:</span> (يظلّ، يُظلّل).</span>
</li>
<li>
    <span class="marker">•</span>
    <span><span class="font-bold text-primary">تكرار الكلمات:</span> (الرّبيع، ربيعًا).</span>
</li>
<li>
    <span class="marker">•</span>
    <span><span class="font-bold text-primary">تكرار الحروف:</span> (الظّاء، اللّام، الرّاء، الياء).</span>
</li>
<li>
    <span class="marker">•</span>
    <span><span class="font-bold text-primary">التناغم (همس/جهر):</span> (هناك، سُكّان، يوتوبيا).</span>
</li>
<li>
    <span class="marker">•</span>
    <span><span class="font-bold text-primary">التناغم (مد طويل/قصير):</span> (هناك، الرّبيع، ربيعًا، سُكّان، يوتوبيا).</span>
</li>

=== BLOCK 11: Applied Example 2 (Nazik) ===
(Component: TEMPLATE_C_POEM)
Poet: نازك الملائكة
Verse 1: وأحسَسْتُ في قَعْرِ رُوحي جنونًا     وشوقًا عميقًا كبَحْرٍ عميقْ

=== BLOCK 12: Analysis 2 ===
(Component: TEMPLATE_C_LIST)
Title: تحليل الموسيقا في المثال الثاني
[LIST_ITEMS]:
<li>
    <span class="marker">•</span>
    <span><span class="font-bold text-primary">تكرار المفردات:</span> (عميقًا، عميق).</span>
</li>
<li>
    <span class="marker">•</span>
    <span><span class="font-bold text-primary">تكرار الأحرف:</span> (القاف، الراء، الحاء).</span>
</li>
<li>
    <span class="marker">•</span>
    <span><span class="font-bold text-primary">التناغم (همس/جهر):</span> (أحْسَسْتُ، في، روحي، شوقًا، كبحرٍ).</span>
</li>
<li>
    <span class="marker">•</span>
    <span><span class="font-bold text-primary">تكرار التنوين:</span> (جُنونًا، شوقًا، عميقًا، بحرٍ).</span>
</li>

=== BLOCK 13: Applied Example 3 (Al-Jazzar) ===
(Component: TEMPLATE_C_POEM)
Poet: أبو الحُسينِ الجزّار
Verse 1: حارَ فِكْري وضاقَ صَدْري وإنْ حا     رَ هُمُومًا يَضيقُ عنها الفَضَاءُ

=== BLOCK 14: Analysis 3 ===
(Component: TEMPLATE_C_LIST)
Title: تحليل الموسيقا في المثال الثالث
[LIST_ITEMS]:
<li>
    <span class="marker">•</span>
    <span><span class="font-bold text-primary">تكرار المفردات:</span> (ضاق، يضيق).</span>
</li>
<li>
    <span class="marker">•</span>
    <span><span class="font-bold text-primary">التناغم (همس/جهر):</span> (حار، فكري، صدري، حاز، هُمومًا، عنها).</span>
</li>
<li>
    <span class="marker">•</span>
    <span><span class="font-bold text-primary">التناغم (مد طويل/قصير):</span> (حار، ضاق، حاز، همومًا، يضيق، الفضاء).</span>
</li>
<li>
    <span class="marker">•</span>
    <span><span class="font-bold text-primary">التوازن:</span> (حار فكري، ضاق صدري).</span>
</li>
<li>
    <span class="marker">•</span>
    <span><span class="font-bold text-primary">التقفية الداخلية:</span> (فِكْري)، (صَدْري).</span>
</li>
<li>
    <span class="marker">•</span>
    <span><span class="font-bold text-primary">تكرار الحروف:</span> (الحاء، الضاد، الياء).</span>
</li>

=== BLOCK 15: Intellectual Level (Dictionary) ===
(Component: TEMPLATE_C_LIST)
Title: فوائد في المستوى الفكري والمعجمي
[LIST_ITEMS]:
<li>
    <span class="marker">•</span>
    <span><span class="font-bold text-primary">معاجم الأوائل (الحرف الأول):</span> المنجد، مختار الصحاح، المصباح المنير، المعجم المدرسي، الوسيط.</span>
</li>
<li>
    <span class="marker">•</span>
    <span><span class="font-bold text-primary">معاجم الأواخر (باب آخر حرف، فصل أول حرف):</span> القاموس المحيط، لسان العرب، تاج العروس.</span>
</li>
[NOTE_TITLE]: تنبيه هام
[NOTE_TEXT]:
يجب تجريد الكلمة من أحرف الزيادة (مجموعة في "سألتمونيها") وإرجاعها إلى أصلها المجرد قبل البحث (مثال: استمطر -> مطر).

=== BLOCK 16: Summary Matrix ===
(Component: TEMPLATE_C_TABLE)
Title: ملخص الموسيقا الشعرية
[TABLE_HEADERS]:
<th>النوع</th>
<th>المكونات / المصادر</th>
[TABLE_ROWS]:
<tr>
    <td class="font-bold text-primary">الموسيقا الخارجية</td>
    <td>
        • الوزن (البحور)<br>
        • القافية (مطلقة / مقيدة)<br>
        • حرف الروي
    </td>
</tr>
<tr>
    <td class="font-bold text-primary">الموسيقا الداخلية</td>
    <td>
        • الهمس والجهر<br>
        • التكرار (حروف، كلمات...)<br>
        • التناغم (المدود)<br>
        • المحسنات اللفظية (جناس، تصريع...)<br>
        • التقفية الداخلية<br>
        • الصيغ الاشتقاقية
    </td>
</tr>

=== BLOCK 17: Exam ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: اذكر مصدراً من مصادر الموسيقا الداخلية برز في البيت التالي ومثّل له:
<br>أبْصَرْتُهُ فرَأيْتُ أبدعَ مَنْظَرٍ     ثُمَّ انْثَنَيْتُ بناظِري مَحْسُورا

--- END STREAM ---
