# **SESSION 170**

[TASK DEFINITION]
Objective: Implement page 170.
File: `pages/page_170.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: Verify layout using `verify_layout.py`.
2.5 Cut Content: Handled.
2.6 Cut Content Determinism: TEMPLATE_CUT_BOX_PART_2.html used for الإعراب.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD.
4. Highlighting: Use `.highlight-red`.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide: NO INLINE STYLES. Irab Words inside `.irab-word` MUST be white. No `<section>` tags in components (use `<div>`), keeping `<header>`.
7. Unique IDs: Use id='bXXXXX'. Use `id_manager.py`.
8. Self-Correction: `lint_pages.py`.
9. Do not summarize examples.
10. Do not provide uncompleted text content.
11. Preserve exact Tashkeel.
12. Visual Density: dense.
13. balanced page colors between teal and orange: minimum 1 element in orange (Warning/Tip).
14. Wrapped in `TEMPLATE_C_PAGE_WRAPPER.html`.
15. Exam section always in the end (omitted if no questions present).

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 170
[CHAPTER_TITLE]: page 170
[CATEGORY_HEADER]: 170
[SECTION_HEADER]: 170
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: إعراب (تتمة) ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[BLOCK_TITLE]: إعراب
[CONTENT]:
<div class="flex flex-col gap-2mm">
    <div class="irab-box" id="b17001">
        <div class="irab-word">أَكُلما</div>
        <div class="irab-details">
            <span class="highlight-red">الهَمْرَة،ُ</span> حَرْفُ استفهام <span class="highlight-red">كلما،</span> اسم شرط غير جازم مبني على السكون في محل نصب مَفْعُول فيه ظرف زمان
        </div>
    </div>
    <div class="irab-box" id="b17002">
        <div class="irab-word">هَيَّتِ</div>
        <div class="irab-details">
            فِعْل ماض، مَبْنِي على الفَتْحَةِ؛ لاتصَالِهِ بِنَاءِ التَّأْنيثِ السَّاكِنَةِ وَالتَّاء،ُ حَرْفُ تَأْنيث لا مَحَلَّ لَهُ مِنَ الإعراب. وحرك بالكُسْرَةِ لِمَنْعِ التَّقَاءِ السَّاكِنَين.
        </div>
    </div>
    <div class="irab-box" id="b17003">
        <div class="irab-word">الأَرْبَاحُ</div>
        <div class="irab-details">
            فَاعِلْ مَرْفُوعٌ
        </div>
    </div>
    <div class="irab-box" id="b17004">
        <div class="irab-word">خَافِقَة:ً</div>
        <div class="irab-details">
            حالٌ مَنْصُوبَةٌ
        </div>
    </div>
    <div class="irab-box" id="b17005">
        <div class="irab-word">تَجُرُ</div>
        <div class="irab-details">
            فِعْلَ مُضَارع مَرْفُوعُ
        </div>
    </div>
    <div class="irab-box" id="b17006">
        <div class="irab-word">فِي ذَيْلِها</div>
        <div class="irab-details">
            <span class="highlight-red">في،</span> حَرْفُ جرٍ <span class="highlight-red">ذَيْلِها،</span> اسمٌ تَجْرُور،َ وَعَلَامَةُ جَرَهِ الكَسْرَةُ الظاهرة. وها، ضمير مُتَّصِلِّ مَبْنِي على السُّكُونِ فِي مَحَلِّ جَر،ٍ مُضَافُ إِلَيْهِ
        </div>
    </div>
    <div class="irab-box" id="b17007">
        <div class="irab-word">أَنْفَاسَ</div>
        <div class="irab-details">
            مَفْعُولُ بِهِ مَنْصُوبُ
        </div>
    </div>
    <div class="irab-box" id="b17008">
        <div class="irab-word">رَيْحَانِ</div>
        <div class="irab-details">
            مُضَافُ إِلِيهِ تَجْرُور.ٌ
        </div>
    </div>
    <div class="irab-box" id="b17009">
        <div class="irab-word">جملة )كُلَّمَا هَبَّتِ الأَرْيَاحُ ... تجر (</div>
        <div class="irab-details">
            استئنافية، لا محل لها مِنَ الإعراب
        </div>
    </div>
    <div class="irab-box" id="b17010">
        <div class="irab-word">جملة )هَبَّتِ الأَرباح(</div>
        <div class="irab-details">
            في محلِّ جَرِّ بالإضافة
        </div>
    </div>
    <div class="irab-box" id="b17011">
        <div class="irab-word">جملة )تجر(</div>
        <div class="irab-details">
            حاليَّة،ٌ مَحَلَّهَا النَّصْب.ُ
        </div>
    </div>
</div>

=== BLOCK 3: البيت الشعري ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البيت الشعري
[POET_NAME]:
[RIGHT_HEMISTICH]: حَسِبْتَهَا نَسَمَاتِ الشَّيْحِ فَانْطَلَقَتْ
[LEFT_HEMISTICH]: مِنْ أَسْرِهَا زَفَرَاتُ العاجز الواني

=== BLOCK 4: شرح البيت ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح
Content:
<p class="mt-1mm text-accent"><span class="highlight-red font-bold">المفردات:</span> الشَّيْحِ : نَبْتٌ زَكِيُّ الرَّائِحَة،ِ زَفَرَات : الأَنْفَاسُ المَحْبُوسَةُ مُدَّةٌ مِنَ الزَّمَنِ الوَانِي : الواهِنُ الضَّعيف. و الوَانِي، اسم فاعِلِ فِعْلُه:ُ وني. و العاجز، اسم فاعِلِ فِعْلُه: عجز</p>
<p class="mt-1mm text-accent"><span class="highlight-red font-bold">الشرح:</span> تظنُ الريح التي تَلْفَحُ وَجْهَكَ نسماتٍ عَرَبِيَّةً مُشْبَعَةً بِرَائِحَةِ نَبَاتِ الشَّيْحِ الْعَطِرَة،ِ فَتَأَجَّجُ جَمَرَاتُ الشَّوقِ الكَامِنَةُ فِي رَمَادِ أَحْزَائِك،َ فَتَتَدَفْقُ زَفَرَاتُ التَّوَجُعِ المَكْبُوتَهُ فِي صَدْرِكَ مُظْهِرَةً وَهُنَكَ وَضَعْفَكَ</p>
<p class="mt-1mm text-accent"><span class="highlight-red font-bold">الفكرة:</span> التَّعَلَّقُ بالوطن والارتباط به، والألم والمعاناة بسبب البعد عَنْهُ )الحنين الدائم للديار(.</p>

=== BLOCK 5: إعراب البيت ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b17012
[TARGET_WORD]: حَسِبْتَها
[IRAB_ANALYSIS]: فعل ماض مَبْنِي على السُّكُون؛ لاتِصَالِهِ بناء الرفع المتحركة. والنَّاء،ُ ضميرٌ مُتَصِلِّ مَبْنِي على الفتحة في محل رفع، فاعل. وها، ضميرٌ مُتَّصِلِّ مَيْنِي على السُّكُونِ فِي مَحَلِّ نَصْب،ِ مَفْعُولُ بِهِ أَوَّلَ

=== BLOCK 6: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b17013
[TARGET_WORD]: نَسَمَاتِ
[IRAB_ANALYSIS]: مَفْعُولُ بِهِ تَانٍ مَنْصُوب، وعلامَةُ نَصْبِهِ الكَسْرَةُ نِيَابَةً عَنِ الفَتْحَةِ لِأَنَّهُ جَمْعُ مُؤَنَّث سالم

=== BLOCK 7: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b17014
[TARGET_WORD]: الشَّيْحِ
[IRAB_ANALYSIS]: مُضَاف إليهِ مَجْرُورٌ

=== BLOCK 8: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b17015
[TARGET_WORD]: فَانْطَلَقَتْ
[IRAB_ANALYSIS]: <span class="highlight-red">الفاء،</span> حَرْفُ عَطْفُ <span class="highlight-red">انْطَلَقَت،ْ</span> فعل ماض، مَبْنِي على الفَتْحَةِ؛ لاتِصَالِهِ بِنَاءِ التَّأْنيتِ السَّاكِنَةِ وَالنَّاء،ُ حَرْفُ تأنيث لا مُحَلَّ لَهُ مِنَ الإِعراب.

=== BLOCK 9: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b17016
[TARGET_WORD]: مِنْ
[IRAB_ANALYSIS]: حَرْفُ جر.

=== BLOCK 10: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b17017
[TARGET_WORD]: أَسْرها
[IRAB_ANALYSIS]: اسم مجرور، وعلامَةُ جَرَهِ الكُسْرَةُ الظَّاهِرَة.ُ وها، ضمير متصل مَبْنِي على السكون في محل جر،ٍ مُضَافَ إِلَيْهِ

=== BLOCK 11: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b17018
[TARGET_WORD]: زَفَرَات:ُ
[IRAB_ANALYSIS]: فَاعِلَ مَرْفُوعُ

=== BLOCK 12: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b17019
[TARGET_WORD]: الْعَاجِز
[IRAB_ANALYSIS]: مُضَاف إليهِ مَجْرُور

=== BLOCK 13: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b17020
[TARGET_WORD]: الواني
[IRAB_ANALYSIS]: صفةً مَجُرُورَة،ً وعلامة جَرِّهَا الكَسْرَةُ المُقَدَّرَةُ على الياء، مَنَعَ ظهورها التَّقَلُ

=== BLOCK 14: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b17021
[TARGET_WORD]: جملة )حَسِبْتَها(
[IRAB_ANALYSIS]: جواب الشَّرْط،ِ لا محل لها مِنَ الإعراب

=== BLOCK 15: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b17022
[TARGET_WORD]: جملة )انطَلَقَتْ زَفَرَاتُ العَاجِزِ(
[IRAB_ANALYSIS]: مَعْطُوفَة،ً لا تحل لها مِنَ الإعراب.

=== BLOCK 16: البيت الشعري ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البيت الشعري
[POET_NAME]:
[RIGHT_HEMISTICH]: وليس يرويكَ إِلَّا نَهْلَةٌ بَعُدَتْ
[LEFT_HEMISTICH]: مِنْ مَاءٍ دِجْلَةَ أَو سَلْسَالِ لُبُنَانِ

=== BLOCK 17: المفردات والشرح ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح
Content:
<p class="mt-1mm text-accent"><span class="highlight-red font-bold">المفردات:</span> نَهْلَةٌ : شَرْبَةٌ سلسال : الماء العذب</p>
<p class="mt-1mm text-accent"><span class="highlight-red font-bold">الشرح:</span> لا يهنا لكَ عَيش في غُربتك ولا يَسُوخُ لَكَ شَرَاب،ٌ أو يَلَدُّ لَكَ طَعَام،ُ فَتبقى عَطِشًا تمني النَّفْسَ بأن ترتوي بياهِ الوَطَنِ العَذَبَة.ِ</p>

=== BLOCK 18: تحليل ===
(Component: TEMPLATE_C_TABLE.html)
[TABLE_TITLE]: تحليل فني
[TABLE_HEADERS]:
<tr>
    <th>الفكرة</th>
    <th>الشعور</th>
    <th>التراكيب (الأداة / المثال)</th>
    <th>الأساليب</th>
</tr>
[TABLE_ROWS]:
<tr>
    <td>التَّعْبِيرُ عَنِ الشَّوْقِ والحنين إلى لِقَاءِ الوَطَنِ وَالأَحِيَّةِ )الحنين الدائم للديار(.</td>
    <td>الشوق والحنين</td>
    <td>ليس يرويك إلا نَهْلَةٌ</td>
    <td>)ليسَ يَرويك(: أسلوب نفي. الأداة: ليس. مهملة؛ لأنَّما دخَلَتْ على الفِعْلِ المضارع ولم يتصل بها ضمير</td>
</tr>

=== BLOCK 19: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b17023
[TARGET_WORD]: وليس
[IRAB_ANALYSIS]: <span class="highlight-red">الواو،</span> حَرْفُ استثناف <span class="highlight-red">ليس،</span> حَرْفُ نَفْي

=== BLOCK 20: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b17024
[TARGET_WORD]: يرويكَ
[IRAB_ANALYSIS]: فِعْلَ مُصَارع مَرْفُوع، وعلامَةُ رَفْعِهِ الضَّمَةُ المُقَدَّرَةً على الياء، مَنَعَ ظهورها الثقل والكاف، ضمير مُتَصِلِّ مَبْنِي على الفَتْحَةِ فِي مَحَلَ نَصْب،ِ مَفْعُولُ بِه.ِ

=== BLOCK 21: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b17025
[TARGET_WORD]: إِلَّا
[IRAB_ANALYSIS]: أَدَاةُ حَصْرِ

=== BLOCK 22: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b17026
[TARGET_WORD]: نَهْلَةٌ
[IRAB_ANALYSIS]: فَاعِلَ مَرْفُوعٌ

=== BLOCK 23: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b17027
[TARGET_WORD]: بَعْدَتْ
[IRAB_ANALYSIS]: فعل ماض، مَبْنِي على الفَنْحَةِ؛ لاتِصَالِهِ بِتَاءِ التأنيث السَّاكِنَة.ِ والنَّاء،ُ حَرْفٌ تَأْنِي لا مَحَلَّ لَهُ مِنَ الإعراب

=== BLOCK 24: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b17028
[TARGET_WORD]: مِنْ مَاءِ
[IRAB_ANALYSIS]: <span class="highlight-red">مِنْ</span> حَرْفُ جَر،ٍ <span class="highlight-red">مَاء،ِ</span> اسم مجرور والجار والمَجْرُورُ مُتَعَلِقَانِ بِصِفَةٍ مَحْدُوفَةٍ

=== BLOCK 25: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b17029
[TARGET_WORD]: دِجْلَةَ
[IRAB_ANALYSIS]: مُضَافُ إليهِ مَجْرُور،ٌ وعلامَةً جَرَهِ الفَتَحَةً نِيَابَةٌ عَنِ الكَسْرَةِ لِأَنَّهُ مَمْنُوعُ مِنَ الصَّرْف.ِ

=== BLOCK 26: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b17030
[TARGET_WORD]: أو سَلْسَال:ِ
[IRAB_ANALYSIS]: <span class="highlight-red">أو،</span> حَرْفُ عَطْفٍ <span class="highlight-red">سَلْسَال،ِ</span> اسمٌ مَعْطُوفٌ مَجْرُورٌ

=== BLOCK 27: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b17031
[TARGET_WORD]: لَبْنَانِ
[IRAB_ANALYSIS]: مُضَافُ إِلَيْهِ مَجْرُور.ٌ

=== BLOCK 28: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b17032
[TARGET_WORD]: جملة )ليس يرويكَ إِلَّا نَهْلَةٌ(
[IRAB_ANALYSIS]: استئنافية، لا محل لها مِنَ الإعراب

=== BLOCK 29: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b17033
[TARGET_WORD]: جملة )بَعْدَتْ(
[IRAB_ANALYSIS]: صِفَة،ٌ مَحَلُّهَا الرَّفْع.ُ

=== BLOCK 30: البيت الشعري ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البيت الشعري
[POET_NAME]:
[RIGHT_HEMISTICH]: وَحُلْمُ يَوْمِكَ في الميماس محتفل
[LEFT_HEMISTICH]: بالغيد والصيد فِي أَعْرَاسِ نُدْمَانِ

=== BLOCK 31: المفردات والشرح ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح
Content:
<p class="mt-1mm text-accent"><span class="highlight-red font-bold">المفردات:</span> الميماس : مُتَنَزَّه على العاصي في حمص الغيد : المفرد، غيداء، وهي الفتاة التي تتمايل وتتثنى في لين وَنُعُومَةِ الصيد : الْمُفْرَد،ُ أصيد، وهو الشاب المرهو بِنَفْسِهِ نَدْمان : المفرد، نديم، وهو الصَّاحِبُ والمسامر والفيد، والصيد، وتدمان : صِفَةٌ مُشَبَّهَةٌ باسم الفاعل. و محتفل، اسم فاعِلِ فِعْلُه:ُ احتفل</p>
<p class="mt-1mm text-accent"><span class="highlight-red font-bold">الشرح:</span> وتظلُ تَحْلُمُ وَأَنتَ قابعُ فِي مَهْجَرِكَ القَصِيِّ بِطِيبِ العَوْدَةِ إِلَى حِمْصَكَ، حَيَّ الميماس الحِمْصِيَ لِتَنْعَمَ بحلاوَةِ الوِصَالِ وَتَمَتْعَ بِقَضَاءِ الأَوْقَاتِ الجميلة في احتفالات أعراس الأصحاب، حيث الحسَانُ النَّاعِمَات،ُ وَالشَّبَّانُ الْمُعْتَذِينَ بِأَنْفُسِهِم</p>

=== BLOCK 32: تنبيه وملاحظة ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[BENEFIT_TITLE]: الفكرة
[BENEFIT_CONTENT]: التَّعْبِيرُ عَنِ الشَّوْقِ وَالحَنِيْنِ إِلَى لِقَاءِ الوَطَنِ وَالأَحِيَّةِ )الحَنِين الدائم للديار(.

=== BLOCK 33: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b17034
[TARGET_WORD]: وحلم
[IRAB_ANALYSIS]: <span class="highlight-red">الواو،</span> حَرْفُ استنَاف.ِ <span class="highlight-red">حُلَمْ ،</span> مُبْتَداً مَرْفُوعٌ

=== BLOCK 34: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b17035
[TARGET_WORD]: يَوْمِكَ
[IRAB_ANALYSIS]: مُضَافَ إِلَيهِ مَجْرُور،ٌ وعلامَةُ جَرَهِ الكَسْرَةُ الظَّاهِرَة.ُ والكاف، ضميرٌ مُتَّصِلِّ مَبْنِي على الفَتْحَةِ فِي مُحَلَ جَر،ٍ مُضَافُ إِلَيْهِ

=== BLOCK 35: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b17036
[TARGET_WORD]: مُحْتَفِل:ُ
[IRAB_ANALYSIS]: خَبَرٌ مَرْفُوع

=== BLOCK 36: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b17037
[TARGET_WORD]: والصيد
[IRAB_ANALYSIS]: <span class="highlight-red">الواو،</span> حَرْفُ عَطْفٍ <span class="highlight-red">الصيد،</span> اسمٌ مَعْطُوفٌ مَجْرُورٌ

=== BLOCK 37: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b17038
[TARGET_WORD]: نُدْمَانِ
[IRAB_ANALYSIS]: مُضَافٌ إليهِ مَجْرُور.ٌ

=== BLOCK 38: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[UNIQUE_ID]: b17039
[TARGET_WORD]: جملة )حُلْمُ يَوْمِكَ فِي المِيمَاسِ مُحْتَفِل(
[IRAB_ANALYSIS]: استئنافية، لا محل لها مِنَ الإعراب.

=== BLOCK 39: البيت الشعري ===
(Component: TEMPLATE_C_POEM.html)
[POEM_TITLE]: البيت الشعري
[POET_NAME]:
[RIGHT_HEMISTICH]: مَنْ أَنْتَ مَا أَنْتَ؟ قد وَزَعْتَ رُوْحَكَ فِي
[LEFT_HEMISTICH]: عَهْدَيْنِ مِنْ شَاسِع ماض ومن داني

=== BLOCK 40: المفردات والشرح ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات والشرح
Content:
<p class="mt-1mm text-accent"><span class="highlight-red font-bold">الشرح:</span> مَنْ أنت؟ مِمَّ أَنْتَ مجبول؟ قد أصبحت روحكَ نَهْبًا لِزَمَنَيْن،ِ مَشْطُورةً بينهما: زَمَنٍ عَرِيقٍ عِشْتَ فِيهِ هَانِئًا مُرْتَاحًا بَيْنَ أَحضانِ الوَطَنِ الدَّافِيَةِ الحنونَة،ِ وَزَمَنِ رَاهِن تلوكُكَ فِيهِ أَنْيَابُ الغَرْيَة،ِ وَيَفْتَرَسُكَ صَقِيعُهَا المُوحِشُ</p>
<p class="mt-1mm text-accent"><span class="highlight-red font-bold">الفكرة:</span> التَّمَزَّقُ الروحِيُّ بَيْنَ الغُرْبَةِ وَالوَطَن.ِ</p>

--- END STREAM ---
