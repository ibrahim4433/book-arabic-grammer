# **SESSION 05.0**

[TASK DEFINITION]
Objective: Implement اسلوب المدح و الذم.
File: `pages/05.0_nXX_اسلوب المدح و الذم.html`
Reference: Follow patterns in design_patterns.json.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 05
[CHAPTER_TITLE]: اسلوب المدح و الذم
[CATEGORY_HEADER]: 05
[SECTION_HEADER]: 05
[AUTHOR_NAME]: أ. حنا خفيف
[AUTHOR_PHONE]:

=== BLOCK 2: أركان الأسلوب ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أركان أسلوب المدح والذم
Content: <p class="text-accent mb-2mm text-center">يتألَّفُ أسلوبُ المَدح، أو أسلوبُ الذَّمِّ من ثلاثةِ أركانٍ هي:</p>

=== BLOCK 3: الأركان (List) ===
(Component: TEMPLATE_C_LIST.html)
- <b>فعلُ</b> المَدح أو فعلُ الذَّمِّ.
- <b>فاعلُ</b> المَدح أو فاعلُ الذَّمِ.
- <b>المَخصوصُ</b> بالمَدح أو المَخصوصُ بالذَّمِّ.

=== BLOCK 4: فاعل حبذا ولا حبذا ===
(Component: TEMPLATE_C_BENEFIT.html)
Title: فاعل (حبَّذا) و(لا حَبَّذا)
Content: <p class="text-center font-bold mb-2mm">فاعِلُ (<span class="highlight-green">حبَّذا</span>) و(<span class="highlight-green">لا حَبَّذا</span>) اسمُ الإشارة (<span class="highlight-blue">ذا</span>).</p><div class="flex flex-row justify-center gap-4mm w-full"><div class="flex-1 text-center bg-white p-2mm rounded-md">- <span class="highlight-green">حَبَّذا</span> <span class="highlight-red">الأمانَةُ</span>.</div><div class="flex-1 text-center bg-white p-2mm rounded-md">- <span class="highlight-green">لا حَبَّذا</span> <span class="highlight-red">الكذبُ</span>.</div></div>

=== BLOCK 5: فاعل نعم وبئس ===
(Component: TEMPLATE_C_BLOCK.html)
Title: فاعِلُ (نِعْمَ) و(بِئْسَ)
Content: <p class="mb-2mm text-primary font-bold">يأتي فاعل (نِعْمَ) و(بِئْسَ) على ثلاثة أوجه:</p>

=== BLOCK 6: أوجه فاعل نعم وبئس ===
(Component: TEMPLATE_C_LIST.html)
- <b>اسمًا مُعَرَّفًا بـ (ال)</b>، نحو: <br> - <span class="highlight-green">نِعْمَ</span> <span class="highlight-blue">الخلقُ</span> <span class="highlight-red">الإخلاصُ</span>. <br> - <span class="highlight-green">بِئْسَ</span> <span class="highlight-blue">الصِّفَةُ</span> <span class="highlight-red">الكَذِبُ</span>.
- <b>مُضَافًا إلى مُعَرَّفٍ بـ (ال)</b>، نحو: <br> - <span class="highlight-green">نِعْمَ</span> <span class="highlight-blue">خلقُ الرَّجلِ</span> <span class="highlight-red">الإخلاصُ</span>. <br> - <span class="highlight-green">بِئْسَ</span> <span class="highlight-blue">صِفَةُ الرَّجلِ</span> <span class="highlight-red">الكَذِبُ</span>.
- <b>ضميرًا مُستَتِرًا وجوبًا مُمَيَّزًا باسم نكرة منصوب يُعربُ تمييزًا</b>، نحو: <br> - <span class="highlight-green">بِئْسَ</span> <span class="highlight-blue">صِفَةً</span> <span class="highlight-red">الخيانَةُ</span>. <br> - <span class="highlight-green">نِعْمَ</span> <span class="highlight-blue">عَمَلًا</span> <span class="highlight-red">الاجتهادُ</span>.

=== BLOCK 7: إعراب المخصوص ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Title: قاعدة إعراب المخصوص بالمدح أو الذم
Content: <p class="text-center font-bold">يُعْرَبُ المَخصوصُ بالمَدحِ أو المَخصوصُ بالذَّمِّ <span class="highlight-red">مبتدأ مُؤَخَّرًا</span>، وتُعرَبُ الجملةُ قبلَهُ في مَحَلِّ رفع <span class="highlight-blue">خَبَرَ مُقَدَّم</span> لَهُ.</p>

=== BLOCK 8: أمثلة الإعراب ===
(Component: TEMPLATE_C_TWO_COLUMNS_WRAPPER.html)
Child 1:
(Component: TEMPLATE_C_BLOCK.html)
Title: الأمثلة
Content: <p class="text-center font-bold">- <span class="highlight-green">نِعْمَ</span> <span class="highlight-blue">العَمَلُ</span> <span class="highlight-red">الجِدُّ</span>.<br>- <span class="highlight-green">بِئْسَ</span> <span class="highlight-blue">الصِّفَةُ</span> <span class="highlight-red">الكَذِبُ</span>.<br>- <span class="highlight-green">حَبَّذا</span> <span class="highlight-red">الكَرَمُ</span>.</p>
Child 2:
(Component: TEMPLATE_C_IRAB.html)
Word 1: الجِدُّ، الكَذِبُ، الكَرَمُ
Role 1: مُبتدأ مُؤَخَّرٌ مرفوعٌ، وعلامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهرةُ.
Word 2: الجملُ (نِعْمَ العَمَلُ)، (بِئْسَ الصِّفَةُ)، (حَبَّذا)
Role 2: في مَحَلِّ رَفْعٍ، خَبَرَ مُقَدَّم.

=== BLOCK 9: ملخص القاعدة ===
(Component: TEMPLATE_C_TABLE.html)
Title: خلاصة أفعال المدح والذم وفاعلها
Content: <table class="dense-table"><thead><tr><th>الفعل</th><th>الفاعل</th><th>المخصوص</th></tr></thead><tbody><tr><td>نِعْمَ / بِئْسَ</td><td>مُعَرَّف بـ (ال) / مُضاف لمُعَرَّف / ضمير مستتر</td><td>مبتدأ مؤخر</td></tr><tr><td>حَبَّذا / لا حَبَّذا</td><td>اسم الإشارة (ذا) دائمًا</td><td>مبتدأ مؤخر</td></tr></tbody></table>

=== BLOCK 10: تدريب محلول 1 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
Number: ١
Question: اجْعَل (الظَّالمَ) مَخْصُوصًا بالذَّمِ على أنْ يَكُونَ الفاعِلُ ضميرًا مُستترًا.
Answer: بِئْسَ إنسانًا الظَّالِمُ. أو: بِئْسَ إنسانًا الظَّالِمُ.

=== BLOCK 11: تدريب محلول 2 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
Number: ٢
Question: حَدِّدْ المَخصُوصَ بالمَدْح واضبطْ آخرَهُ بالشَّكلِ في الجُملَةِ الآتيةِ: (نِعمَ الحاكِم حاكِم يُنْصِفُ رَعِيَّتَهُ).
Answer: المخصُوصُ بالمَدْح: حاكِم. ضبطُهُ بالشَّكلِ: حاكِمٌ.

=== BLOCK 12: تدريب محلول 3 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
Number: ٣
Question: اجعلْ كلمةَ (العَرَب) مَخْصُوصًا بالمَدْح مُستَخْدِمًا (نِعمَ) على أَنْ يكونَ الفاعِلُ اسما ظاهِرًا مُعرَّفًا بأل.
Answer: نِعْمَ القَوْمُ العَرَبُ.

=== BLOCK 13: تدريب محلول 4 ===
(Component: TEMPLATE_C_EXAM_SOLVED.html)
Number: ٤
Question: أَنشئ جُمْلَتَين تمدَحُ في الأُولى (العَيْشَ في الوطَنِ)، وتذمُّ في الثَّانيةِ (الهِجْرة مِنَ الوطَنِ).
Answer: <div class="text-right"><strong>المَدح:</strong><br>- نِعْمَ العَمَلُ العَيْشُ في الوطَنِ.<br>- نِعْمَ عَمَلُ الإِنْسانِ العَيْشُ في الوطَنِ.<br>- نِعْمَ ما تفعلُهُ العَيْشُ في الوطَنِ.<br>- نِعْمَ عملا العَيْشُ في الوطَنِ.<br>- العَيْشُ في الوطَنِ نِعْمَ العملُ.<br>- حبَّذا العَيْشُ في الوطَنِ.<br><br><strong>الذَّم:</strong><br>- بِئْسَ العَمَلُ الهِجْرَةُ مِنَ الوطَنِ.<br>- بِئْسَ عَمَلُ الإنسانِ الهِجْرَةُ مِنَ الوطَنِ.<br>- بِئْسَ ما تفعلُهُ الهِجْرَةُ مِنَ الوطَنِ.<br>- بِئْسَ عملا الهِجْرَةُ مِنَ الوطَنِ.<br>- الهِجْرَةُ مِنَ الوطَنِ بِئْسَ العملُ.<br>- لا حبَّذا الهِجْرَةُ مِنَ الوطَنِ.</div>

=== BLOCK 14: Cut Content ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
Title: علامات الإعراب
Content: <p class="text-center font-bold">علامات الإعراب الأصلية والفرعية في الأسماء والأفعال:</p>

--- END STREAM ---
