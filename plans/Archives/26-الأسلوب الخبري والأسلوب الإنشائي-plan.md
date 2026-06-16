# **SESSION 26.0**

[TASK DEFINITION]
Objective: Implement الأسلوب الخبري والأسلوب الإنشائي.
File: `pages/26.0_nXX_الأسلوب الخبري والأسلوب الإنشائي.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/26.1_...` if page have a lot of blank space add exam elements from the lesson.
3. Text Content: 100% Arabic with full Harakat.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`, `.highlight-green` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
    *   **Rule:** NO INLINE STYLES.
    *   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
    *   **Mapping:**
        *   `style="width: 20%"` -> `class="w-20pct"`
        *   `style="margin-top: 2mm"` -> `class="mt-2mm"`
        *   `style="text-align: center"` -> `class="text-center"`
        *   `style="font-weight: bold"` -> `class="font-bold"`
7. Templates: You are forbidden from inventing new HTML tags or classes or template elements. You must map all content using "Jules-workspace/Templates/" components as the STREAM says in suitable way.
8. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). use "Jules-workspace/id_manager.py" to generate or verify them.
9. **Self-Correction:** Run "Jules-workspace/lint_pages.py" after creating html files. If it fails, you MUST fix the errors (usually inline styles) before submitting.
10. Do not summarize examples.
11. Do not provide uncompleted text content using (...) .
12. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
13. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
14. Balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER)
[LESSON_NUMBER]: 26
[CHAPTER_TITLE]: الأسلوب الخبري والأسلوب الإنشائي
[CATEGORY_HEADER]: فوائد
[SECTION_HEADER]: المستوى الفني
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Introduction (Khabar vs Insha) ===
(Component: TEMPLATE_C_BLOCK)
Title: الأسلوب الخبري والأسلوب الإنشائي (علم المعاني)
[CONTENT_TEXT]:
<p class="text-accent mb-2mm">
يُقسَمُ الكلامُ، في البلاغةِ العربيَّةِ، إلى قسمين، هما: الخبرُ، والإنشاءُ. ويُدْرَسَانِ ضمن (علم المعاني).
</p>

=== BLOCK 3: Al-Uslub Al-Khabari (Definition & Purposes) ===
(Component: TEMPLATE_C_BLOCK)
Title: أولًا - الأسلوب الخبري
[CONTENT_TEXT]:
<p class="text-accent mb-2mm">
كلامٌ يحتملُ الصِّدْقَ أو الكذِبَ، ويصحُّ أنْ نقولَ لقائلِهِ: إنَّهُ صادقٌ فيه أو كاذبٌ.
</p>
<div class="mb-2mm">
    <strong>آ- أغراضُ الخبرِ:</strong> يُلقى الخبرُ لأحدِ غرضين:
</div>
<ul class="structured-list">
    <li>
        <span class="list-marker">•</span>
        <span class="font-bold text-primary">فائدةُ الخَبَرِ:</span> إفادةُ المُخاطَبِ الحُكْمَ الذي تضمَّنَتْهُ الجملةُ، لأنَّهُ لا يعرفُهُ مِنْ قبلُ، نحو: <span class="highlight-blue">(عمرُ بنُ عبدِ العزيزِ أعدلُ خُلفاءِ بني أميَّةَ).</span>
    </li>
    <li>
        <span class="list-marker">•</span>
        <span class="font-bold text-primary">لازمُ الفائدةِ:</span> إفادةُ المُخاطَبِ أنَّ المُتكلِّمَ عالِمٌ بالخبر الذي وردَ في الجملةِ، نحو: <span class="highlight-blue">(كُنْتَ تجلِسُ في الحديقةِ البارحةَ).</span>
    </li>
</ul>

=== BLOCK 4: Metaphorical Purposes of Khabar (Orange Benefit) ===
(Component: TEMPLATE_C_BENEFIT)
[BENEFIT_TITLE]: أغراضٌ بلاغيَّةٌ أُخرى للخبر
[BENEFIT_TEXT]:
<p>
وقد يخرجُ الخبرُ عَنِ الغرضينِ الرّئيسينِ إلى أغراضٍ أُخرى تُفهَمُ مِنْ سياقِ الكلامِ، أهمُّها: <span class="font-bold">(الفخرُ، إظهارُ الضَّعْفِ، الهجاءُ، ..).</span>
</p>

=== BLOCK 5: Types of Khabar (Table) ===
(Component: TEMPLATE_C_TABLE)
[TABLE_TITLE]: ب - أنواعُ الخبرِ (مِنْ حيثُ عددِ المُؤكِّدات)
[TABLE_HEADERS]:
<th>النوع</th>
<th>تعريفه</th>
<th>مثال</th>
[TABLE_ROWS]:
<tr>
    <td class="font-bold text-primary">١- الخبرُ الابتدائيُّ</td>
    <td>هو الخبرُ الخالي من المُؤكِّدات</td>
    <td>نجَحَ خالدٌ</td>
</tr>
<tr>
    <td class="font-bold text-primary">٢- الخبرُ الطَّلبيُّ</td>
    <td>هو الخبرُ الذي ورد فيهِ مُؤكِّدٌ واحدٌ</td>
    <td>واللهِ نَجَحَ خالدٌ</td>
</tr>
<tr>
    <td class="font-bold text-primary">٣- الخبرُ الإنكاريُّ</td>
    <td>هو الخبرُ الذي ورد فيهِ مُؤكِّدان، أو أكثر</td>
    <td>واللهِ قد نَجَحَ خالدٌ</td>
</tr>

=== BLOCK 6: Emphasis Particles (Chips/Tip) ===
(Component: TEMPLATE_C_BENEFIT_TIP)
[BENEFIT_TITLE]: أشهرُ المُؤكِّدات
[BENEFIT_TEXT]:
<div class="flex flex-wrap gap-1mm">
    <span class="bg-white p-1mm rounded border border-grey-light">إِنَّ</span>
    <span class="bg-white p-1mm rounded border border-grey-light">أَنَّ</span>
    <span class="bg-white p-1mm rounded border border-grey-light">لامُ الابتداءِ</span>
    <span class="bg-white p-1mm rounded border border-grey-light">اللَّامُ المُزحلقَةُ</span>
    <span class="bg-white p-1mm rounded border border-grey-light">قَدْ</span>
    <span class="bg-white p-1mm rounded border border-grey-light">القسَمُ</span>
    <span class="bg-white p-1mm rounded border border-grey-light">نونا التوكيدِ</span>
    <span class="bg-white p-1mm rounded border border-grey-light">أحرفُ التنبيهِ</span>
    <span class="bg-white p-1mm rounded border border-grey-light">الأحرفُ الزَّائدةُ</span>
    <span class="bg-white p-1mm rounded border border-grey-light">أمّا الشَّرطيَّةُ</span>
</div>

=== BLOCK 7: Al-Uslub Al-Insha'i (Definition & Division) ===
(Component: TEMPLATE_C_BLOCK)
Title: ثانيًا - الأسلوب الإنشائي
[CONTENT_TEXT]:
<p class="text-accent mb-2mm">
الإنشاءُ كلامٌ لا يحتملُ الصِّدقَ أو الكذِبَ، ولا يصحُّ أنْ نقولَ لقائلِهِ: إنَّهُ صادقٌ فيه أو كاذبٌ.
</p>

=== BLOCK 8: Insha Types (Table) ===
(Component: TEMPLATE_C_TABLE)
[TABLE_TITLE]: أقسام الإنشاء
[TABLE_HEADERS]:
<th>نوع الإنشاء</th>
<th>تعريفه</th>
<th>أشكاله</th>
[TABLE_ROWS]:
<tr>
    <td class="font-bold text-primary">الإنشاء غير الطلبي</td>
    <td>وهو ما لا يستدعي مطلوبًا</td>
    <td>التَّعجُّب، المدح والذَّمّ، القَسَم، الترجي</td>
</tr>
<tr>
    <td class="font-bold text-primary">الإنشاء الطَّلبيّ</td>
    <td>يُطلب به حصولُ شيءٍ لم يكن حاصلًا وقتَ الطّلب</td>
    <td>الأمر، النّهي، النداء، التمني، الاستفهام</td>
</tr>

=== BLOCK 9: Metaphorical Purposes of Insha Talabi (Detailed Table) ===
(Component: TEMPLATE_C_TABLE)
[TABLE_TITLE]: خروج الإنشاء الطَّلبيّ عن معناه الأصليّ
[TABLE_HEADERS]:
<th>نوعه</th>
<th>أدواته وصيغه</th>
<th>الأغراض البلاغية (من السياق)</th>
[TABLE_ROWS]:
<tr>
    <td class="font-bold text-primary">الأمر</td>
    <td>فعل الأمر، المضارع المقترن بلام الأمر، اسم فعل الأمر</td>
    <td>الدُّعاءُ، التحدّي، التمني، الالتماس، الحثُّ، الوعظ، الإرشاد، ...</td>
</tr>
<tr>
    <td class="font-bold text-primary">النَّهي</td>
    <td>له حالة واحدة: (لا) الناهية الجازمة + الفعل المضارع</td>
    <td>(يُفهم من السياق كالتهديد، التوبيخ، التحقير...)</td>
</tr>
<tr>
    <td class="font-bold text-primary">النداء</td>
    <td>
        <ul class="list-none p-0 m-0 text-sm">
            <li>(أ، أيْ، يا): للقريب</li>
            <li>(يا، أيا، هيا): للبعيد</li>
            <li>(وا): للنّدبة والاستغاثة</li>
        </ul>
        <div class="text-xs mt-1mm text-grey-dark">قد يُنادى البعيد بحرف نداء القريب للتحبُّب، والعكس للتعظيم أو التحقير.</div>
    </td>
    <td>اللوم والتوبيخ، التّعظيم، العتاب، الزّجْر، الاستغاثة، الذّمّ، التحقير، التنبيه، الإغراء، ...</td>
</tr>
<tr>
    <td class="font-bold text-primary">التمني</td>
    <td>اداته (ليت)، وقد يشاركها في طلب التمنّي (لو، لعل)</td>
    <td>إن كان الشّيءُ مُمكِن الحصول سُمّي ترجيًا، ويكون بـ (لعل، عسى)</td>
</tr>
<tr>
    <td class="font-bold text-primary">الاستفهام</td>
    <td>الحرفان: (الهمزة، وهل). الأسماء: (مَنْ، منذا، ما، ماذا، متى، أيّان، أين، أنّى، كيف، أي، كَمْ).</td>
    <td>النفي، التقرير، التهكّم والسُّخرية، التحقير، التعجُّب، التشويق، التمنّي، الأمر، التحسُّر، الإنكار، التعظيم، ...</td>
</tr>

=== BLOCK 10: Applied Examples Header ===
(Component: TEMPLATE_C_HEADER)
[LESSON_NUMBER]: 26
[CHAPTER_TITLE]: أمثلة تطبيقية
[CATEGORY_HEADER]: شواهد
[SECTION_HEADER]: تطبيقات
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 11: Example 1 (Poem) ===
(Component: TEMPLATE_C_POEM)
[POEM_VERSES]:
<div class="poem-line">
<span class="hemistich">أَيُهَذَا الشَّــاكي وَمَا بِكَ دَاءٌ</span>
<span class="hemistich">كَيْفَ تَغْدُو إِذَا غَدَوْتَ عَلِيــــــلا؟</span>
</div>
[POET_NAME]: الشاعر
[POET_BIO]: (إيليا أبو ماضي)

=== BLOCK 12: Example 1 Analysis ===
(Component: TEMPLATE_C_BLOCK)
Title: تحليل المثال الأول
[CONTENT_TEXT]:
<p><strong>س١- إلامَ خَرَجَ الاستفهامُ في قول الشّاعر؟</strong></p>
<p class="mt-2mm"><span class="highlight-green">ج١- خَرَجَ الاستفهامُ إلى معنى التّعجُّبِ والإنكار.</span></p>

=== BLOCK 13: Example 2 (Poem) ===
(Component: TEMPLATE_C_POEM)
[POEM_VERSES]:
<div class="poem-line">
<span class="hemistich">يا أَخِي في الشَّـــرقِ، في كُلِّ سَـــكَنْ</span>
<span class="hemistich">يا أَخِي في الأرضِ، في كُلِّ وَطَنْ</span>
</div>
<div class="poem-line">
<span class="hemistich">أَنَا أَدْعُوكَ... فَهَلْ تَعْرِفُنِي؟</span>
<span class="hemistich">يَا أَخَا أَعْرِفُهُ... رَغْمَ المِحَنْ سَــــاءْ</span>
</div>
<div class="poem-line">
<span class="hemistich">لَمْ أَعُدْ مَقْبَرَةً تَحكي البِلَى</span>
<span class="hemistich">لَمْ أَعُدْ سَــــاقِيَةً تَبكي الدِّمَــــــنْ</span>
</div>
<div class="poem-line">
<span class="hemistich">فَلَقَدْ ثُرْنَا عَلَى أَنْفُسِــــــنَا</span>
<span class="hemistich">ومحونا وصـــمـــة الذِّلَّةِ فيــــــن</span>
</div>
[POET_NAME]: الشاعر

=== BLOCK 14: Example 2 Analysis ===
(Component: TEMPLATE_C_BLOCK)
Title: تحليل المثال الثاني
[CONTENT_TEXT]:
<p><strong>س٢- استخرج من الأبيات: (إنشاء طلبي بصيغة النّداء، إنشاء طلبي بصيغة الاستفهام، خبر ابتدائيّ، خبر إنكاري)، وحدد الغرض منها.</strong></p>
<ul class="structured-list mt-2mm">
    <li><span class="list-marker">•</span> <strong>النّداءُ:</strong> <span class="highlight-blue">يا أخي في الشّرق، يا أخي في الأرض، يا أخا أعرفُه.</span> – الغرضُ منه: <span class="text-accent">الاستغاثة والعتاب.</span></li>
    <li><span class="list-marker">•</span> <strong>الاستفهام:</strong> <span class="highlight-blue">هل تعرفُني؟.</span> الغرضُ منه: <span class="text-accent">التّحسُّرُ والتّمنّي.</span></li>
    <li><span class="list-marker">•</span> <strong>خبر ابتدائيّ:</strong> <span class="highlight-blue">لم أعُدْ مَقْبرةً، لم أعُدْ ساقيةً...</span> الغرضُ منه: <span class="text-accent">الفخرُ.</span></li>
    <li><span class="list-marker">•</span> <strong>خبر إنكاري:</strong> <span class="highlight-blue">لقَدْ ثُرْنا على أنفُسِنا.</span> الغرضُ منه: <span class="text-accent">الفخرُ.</span></li>
</ul>

=== BLOCK 15: Example 3 (Poem) ===
(Component: TEMPLATE_C_POEM)
[POEM_VERSES]:
<div class="poem-line">
<span class="hemistich">يَطُولُ عَلى قَلبِي الإنتِظَارُ</span>
<span class="hemistich">وَأغْرَقُ في بَحْرِ يَأْسٍ حَزِينْ</span>
</div>
<div class="poem-line">
<span class="hemistich">دَقَائِق... ثُمَّ أَخِيبُ، وأَهْتِــــــ</span>
<span class="hemistich">ــــــفُ: لا شَيْءَ يُشْــــبِهُ يوتوبيــــــا</span>
</div>
[POET_NAME]: الشاعرة

=== BLOCK 16: Example 3 Analysis ===
(Component: TEMPLATE_C_BLOCK)
Title: تحليل المثال الثالث
[CONTENT_TEXT]:
<p><strong>س٣- هاتِ مثالين على الأسلوب الخبريّ، واذْكُر الغرَضَ البلاغيّ لِكُلٍّ منهما.</strong></p>
<ul class="structured-list mt-2mm">
    <li><span class="list-marker">•</span> <span class="highlight-blue">أغْرَقُ في بَحْرِ يَأْسٍ حزين.</span> – الغرضُ منه: <span class="text-accent">إظهارُ الضَّعْف.</span></li>
    <li><span class="list-marker">•</span> <span class="highlight-blue">دقائق ثمّ أخيبُ.</span> – الغرضُ منه: <span class="text-accent">إظهارُ خيبة الأمل.</span></li>
</ul>

=== BLOCK 17: Example 4 (Poem) ===
(Component: TEMPLATE_C_POEM)
[POEM_VERSES]:
<div class="poem-line">
<span class="hemistich">أَلا مَنْ يُرِينِي غَايتِي قَبْلَ مَذْهَبِي؟</span>
<span class="hemistich">ومِن أين والغَايَاتُ بَعْدَ المَذَاهِبِ؟!</span>
</div>
[POET_NAME]: الشاعر

=== BLOCK 18: Example 4 Analysis ===
(Component: TEMPLATE_C_BLOCK)
Title: تحليل المثال الرابع
[CONTENT_TEXT]:
<p><strong>س٤- ما الغرَضُ مِنَ الاستفهام في البيت الآتي؟</strong></p>
<p class="mt-2mm"><span class="highlight-green">ج ٤ – الغرضُ منه التّحسُّرُ واللّوعَةُ واللَّهْفَةُ.</span></p>

=== BLOCK 19: Example 5 (Poem) ===
(Component: TEMPLATE_C_POEM)
[POEM_VERSES]:
<div class="poem-line">
<span class="hemistich">يَا غَائِصًا بالطِّينِ لا تَنْصَــــــبِ</span>
<span class="hemistich">يُوهِي عَزِيمتَــــه وَلا وصَــــــبِ</span>
</div>
<div class="poem-line">
<span class="hemistich">صَبْرًا على الأيّام إِنْ عَبَــــــثَتْ</span>
<span class="hemistich">هَيْهَاتَ يفــرجُ ضيقَهــــا غَضَــــــبِ</span>
</div>
<div class="poem-line">
<span class="hemistich">مَــــــا أَنــــــتَ أوّل كادِح غَرَّت</span>
<span class="hemistich">آمــــــالَــــهُ، وَكَبــــــا بــــهِ الــــدَّأَبِ</span>
</div>
[POET_NAME]: الشاعر

=== BLOCK 20: Example 5 Analysis ===
(Component: TEMPLATE_C_BLOCK)
Title: تحليل المثال الخامس
[CONTENT_TEXT]:
<p><strong>س٥- استخدَم الشّاعر أسلوبين مُختلِفَين (إنشائيّ – خبري) للتّخفيف من مُعاناة البنّاء. حَدِّدْهُما.</strong></p>
<ul class="structured-list mt-2mm">
    <li><span class="list-marker">•</span> <strong>الأسلوبُ الإنشائيُّ:</strong> <span class="highlight-blue">يا غائِصًا بالطِّينِ</span> (في البيتِ الأوَّلِ). <span class="highlight-blue">صبرًا على الأيَّامِ</span> (في البيتِ الثَّاني).</li>
    <li><span class="list-marker">•</span> <strong>الأسلوبُ الخبريُّ:</strong> <span class="highlight-blue">هَيهاتَ يَفرُجُ ضيقَها غضَبٌ</span> (في البيتِ الثَّاني). <span class="highlight-blue">ما أنتَ أوَّلُ كادِحٍ عَثَرت آمالُهُ</span> (في البيتِ الثَّالثِ). <span class="highlight-blue">كبا بهِ الدَّأبُ</span> (في البيتِ الثَّالثِ).</li>
</ul>
<p class="mt-2mm"><strong>س- ما الغَرضُ مِن أسلوبِ النِّداءِ (يا غائِصًا)؟</strong></p>
<p class="mt-1mm"><span class="highlight-green">ج- إظهارُ الحسرةِ.</span></p>

=== BLOCK 21: Mixed Exercises (List) ===
(Component: TEMPLATE_C_LIST)
[LIST_TITLE]: تطبيقات إضافية (سَمِّ الأساليبَ وبَيِّنِ الغرضَ)
[LIST_ITEMS]:
<li class="list-item-content">
    <div class="font-bold text-primary">والموتُ أهونُ مِن خَطبِهِ</div>
    <div>أسلوبٌ خَبَريٌّ، نوعُهُ ابتدائيٌّ. - غرَضُهُ: <span class="text-accent">إظهارُ مشاعرِ الذُّلِّ والانكِسارِ.</span></div>
</li>
<li class="list-item-content">
    <div class="font-bold text-primary">يا ريحُ، يا إبَرًا تَخيطُ لي الشِّراعَ</div>
    <div>إنشاءٌ طَلبيٌّ بصيغةِ النِّداءِ. - غرَضُهُ: <span class="text-accent">الاستِغاثَةُ.</span></div>
</li>
<li class="list-item-content">
    <div class="font-bold text-primary">ليتَ السَّفائنَ لا تُقاضي راكبيها</div>
    <div>إنشاءٌ طَلبيٌّ بصيغةِ التَّمنّي. - غرَضُهُ: <span class="text-accent">التَّمنّي والتَّحسُّرِ.</span></div>
</li>
<li class="list-item-content">
    <div class="font-bold text-primary">متى أعودُ إلى العراقِ؟ متى أعودُ؟</div>
    <div>إنشاءٌ طَلبيٌّ بصيغةِ الاستِفهامِ. - غرَضُهُ: <span class="text-accent">إظهارُ تَمنّي العودةِ.</span></div>
</li>

=== BLOCK 22: Exam (Previous Years) ===
(Component: TEMPLATE_C_EXAM)
[EXAM_NUMBER]: ١
[EXAM_QUESTION]:
<div class="mb-2mm">قالَ الشَّاعِرُ مُحَمَّد مَهدي الجواهري (٢٠١٣ عِلمي):</div>
<div class="poem-container text-center font-amiri text-xl mb-2mm text-primary">
    وَكَلَّفْتُ نَفْسِي أَنْ تُحَقِّقَ سُؤْلَها<br>
    سِرَاعًا، أَوِ الموتَ الزُّؤَامَ سِراعَا
</div>
<div>استخرِجْ مِنَ البيتِ أسلوبًا خبريًّا، ثُمَّ اذكُرْ نوعَهُ.</div>
[EXAM_NUMBER]: ٢
[EXAM_QUESTION]:
<div class="mb-2mm">قالَ الشَّاعِرُ إيليا أبو ماضي (٢٠١٣ عِلمي):</div>
<div class="poem-container text-center font-amiri text-xl mb-2mm text-primary">
    كُنْ مَعَ الفَجْرِ نسمةً تُوسِعُ الأَزْ<br>
    هارَ شَمًّا وَتارَةً تقبيـــــــلا
</div>
<div>هاتِ مِنَ البيتِ أسلوبًا خبريًّا، واذكُرْ نوعَهُ.</div>
[EXAM_NUMBER]: ٣
[EXAM_QUESTION]:
<div class="mb-2mm">قالَ الشَّاعِرُ محمَّد الفيتوري (٢٠١٤ عِلمي):</div>
<div class="poem-container text-center font-amiri text-xl mb-2mm text-primary">
    نحنُ أهرقْنَا عليها دَمَنَا<br>
    ومَزَجْنَا بثرَاها عظْمَنَا
</div>
<div>استخرِجْ مِنَ البيتِ أسلوبًا خبريًّا، واذكُر نوعَه.</div>

--- END STREAM ---
