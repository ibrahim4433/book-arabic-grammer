# **SESSION 173**

[TASK DEFINITION]
Objective: Implement page 173.
File: `pages/page_173.html`
Reference: Follow patterns in design_patterns.json.
Instructions:
1. Use id_manager.py next-id to generate unique IDs.
2. The page is very dense. You MUST wrap every adjacent (شرح وتحليل) block and (إعراب) block inside a TEMPLATE_C_TWO_COLUMNS_WRAPPER.html to save vertical space. Place the Analysis in the right column and the I'rab in the left column.
3. Create a dummy picture at `input/integrated-pictures/pic_173.jpg` (e.g. using `touch` or `cp`).

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 173
[CHAPTER_TITLE]: page 173
[CATEGORY_HEADER]:
[SECTION_HEADER]:
[AUTHOR_NAME]:
[AUTHOR_PHONE]:

=== BLOCK 2: إعراب ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[BLOCK_TITLE]: إعراب
Content:
مُضَاف إليه مَجْرُورٌ.
جملة (هَزَزْتِ): استئنافية، لا محل لها مِنَ الإعراب.
جملة (خَلَعَتْ): صِلَةُ المَوْصُولِ، لا محل لها مِنَ الإعراب.
جملة (مَاسَتْ): مَعْطُوفَةٌ، لا محل لها مِنَ الإعراب.

=== BLOCK 3: Verse 13 ===
(Component: TEMPLATE_C_POEM.html)
[RIGHT_HEMISTICH]: كَسَوْتِهَا وَرَقَ الأَشْواقِ فَازْدَهَرَتْ
[LEFT_HEMISTICH]: خَضْرَاءَ يَعْبَقُ مِنْهَا رَوْحُ نَيْسانِ

=== BLOCK 4: شرح وتحليل ===
(Component: TEMPLATE_C_BLOCK.html)
Title: شرح وتحليل
Content:
<span class="text-accent">المفردات:</span> ازدهرت: تَلالاتْ. يَعْبُقُ: يَفُوحُ. رَوْحُ: نَسِيم. خَضْرَاءَ: صفة مشبهة باسم الفاعل فعلها خضر.
<span class="text-accent">الشرح:</span> أَلْبَسْتِ أَيَّتُها الرياحُ القَادِمَةُ مِنَ الشَّرْقِ هَذِهِ الأَغْصَانَ الجرداء أوراق المَحَبَّةِ والشَّوقِ، فَبَدَتْ مُتَلَالِئَةً مُخْضَلَّةً تَرْفِلُ بِأَثواب خضراء سُندسِيَّةِ، يَفوح منها عَبَقَ الربيع وعبيرُهُ، ويَضُوعُ مِنْهَا نَسِيمُ نَيْسَانَ الفَوَّاحُ.
<span class="text-accent">الفكرة:</span> التَّعْبِيرِ عَنْ إِثَارَةِ مَشَاعر الشَّوْقِ وتجددها.
<span class="text-accent">البلاغة:</span> (وَرَقَ الأَشواقِ): تشبيه بليغ إضافي.

=== BLOCK 5: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: كَسَوْتِهَا
[IRAB_ANALYSIS]: فِعْلٌ مَاضٍ مَبْنِي على السُّكُونِ؛ لاتِّصَالِهِ بِتَاءِ الرَّفْعِ الْمُتَحَرِّكَةِ. والتَّاءُ، ضميرٌ مُتَّصِلٌ مَبْنِي على الكَسْرَةِ في محل رفع، فاعل. وها، ضمير متصل مبني على السُّكُونِ فِي مَحَلِّ نَصْبٍ، مَفْعُولٌ بِهِ أَول.
[TARGET_WORD]: وَرَقَ
[IRAB_ANALYSIS]: مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ.
[TARGET_WORD]: الأَشْوَاقِ
[IRAB_ANALYSIS]: مُضَافٌ إليه مَجْرُورٌ.
[TARGET_WORD]: فَازْدَهَرَتْ
[IRAB_ANALYSIS]: الفَاءُ، حَرْفُ عَطْفٍ.
[TARGET_WORD]: خَضْرَاءَ
[IRAB_ANALYSIS]: حالٌ مَنْصُوبَةٌ.
[TARGET_WORD]: رَوْحُ
[IRAB_ANALYSIS]: فَاعِلٌ مَرْفُوعٌ.
[TARGET_WORD]: نَيْسَانِ
[IRAB_ANALYSIS]: مُضَاف إليهِ مَجْرُورٌ.
[TARGET_WORD]: جملة (كَسَوْتِهَا)
[IRAB_ANALYSIS]: استئنافية، لا محل لها مِنَ الإعراب.
[TARGET_WORD]: جملة (فازْدَهَرَتْ)
[IRAB_ANALYSIS]: مَعْطُوفَةٌ، لَا مَحَلَّ لها من الإعراب.
[TARGET_WORD]: جملة (يَعْبَقُ مِنْهَا رَوْحُ نَيْسان)
[IRAB_ANALYSIS]: حاليَّةٌ، مَحَلُّها النَّصْب.

=== BLOCK 6: ملحق الأبيات ===
(Component: TEMPLATE_C_POET_BIO.html)
[POET_NAME]: الشاعر نسيب عريضة
[BIO_TEXT]: ملحق الأبيات الخارجية المتممة الواردة في ديوان الشاعر.

=== BLOCK 7: External Verse 1 ===
(Component: TEMPLATE_C_POEM.html)
[RIGHT_HEMISTICH]: حُبٌّ فِي الغَرْبِ ذكرى الأرز والبان
[LEFT_HEMISTICH]: ما أَذْهَبَتْكَ ليالي البعد يا عاني

=== BLOCK 8: شرح وتحليل ===
(Component: TEMPLATE_C_BLOCK.html)
Title: شرح وتحليل
Content:
<span class="text-accent">المفردات:</span> البان: ضَرْبٌ مِنَ الشَّجَرِ سَبْطُ القوام، لين، ورقة كورق الصفصاف ويُشَبَّهُ بِهِ الحسان في الطول واللين. عاني: العاني: الذليل. الجمع: عوان.
<span class="text-accent">الشرح:</span> أَيُّها المهاجر العاني لم تستطع الليالي التي أمضيتها في بلادِ الغُرْبَةِ بَعِيدًا عَنْ وَطَنِكَ، أَنْ تُنْسِيكَ ذِكْرَيَاتِ الوَطَنِ.
<span class="text-accent">الفكرة:</span> الاحتفاظ بذكريات الوَطَنِ في بلاد الغُرْبَةِ.
<span class="text-accent">الشُّعُور:</span> الشَّوْقُ والحنين.
<span class="text-accent">الأداة:</span> التراكيب. المثال: حُبٌّ في الغرب ذكرى الأرز والبان.
<span class="text-accent">البلاغة:</span> (حُبٌّ ذكرى، أذهبتك ليالي): استعارَةُ مَكْنِيَّةٌ. (البان، عاني): تصريع.

=== BLOCK 9: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: جملة (حُبٌّ في الغَرْبِ ذكرى الأَرزِ)
[IRAB_ANALYSIS]: ابتدائية لا محل لها مِنَ الإعراب.
[TARGET_WORD]: جملة (ما أَذْهَبَتْكَ ليالي البعدِ)
[IRAB_ANALYSIS]: استئنافية لا محل لها من الإعراب.
[TARGET_WORD]: ذكرى، ليالي
[IRAB_ANALYSIS]: فاعل مَرْفُوعٌ.
[TARGET_WORD]: الأَرْزِ، البَعْدِ
[IRAB_ANALYSIS]: مُضَافُ إِلَيْهِ مَجْرُورٌ.

=== BLOCK 10: External Verse 2 ===
(Component: TEMPLATE_C_POEM.html)
[RIGHT_HEMISTICH]: ابن العروبة لا أَسْلُو الرُّبُوعَ وَلَو
[LEFT_HEMISTICH]: كانت مثيرةً أوصابي وأشجاني

=== BLOCK 11: شرح وتحليل ===
(Component: TEMPLATE_C_BLOCK.html)
Title: شرح وتحليل
Content:
<span class="text-accent">المفردات:</span> أوصابي: الوَصَبُ الوَجَعُ والمرض، والتَّعَبُ وَالفُتُورُ فِي البَدَنِ. أَشجاني: الشَّجَنُ: الهم والحزن. مثيرة: اسم فاعل، فِعْلُه: أثار.
<span class="text-accent">الشرح:</span> أنا العربي لا أنسى رُبُوعَ الوَطَنِ مَعَ أَنَّهَا السَّبَبُ الْمُبَاشَرُ في إثارة أوجاعي وأمراضي، والمحرك لِهُمُومي وأحزاني.
<span class="text-accent">الفكرة:</span> الانتماء إلى الوَطَنِ رُغْم المعاناةِ بِسَبَبِهِ.
<span class="text-accent">الشَّعور:</span> ألم.
<span class="text-accent">الأداة:</span> التراكيب. المثال: كانت مثيرة أوصابي.

=== BLOCK 12: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: ابنُ
[IRAB_ANALYSIS]: خبر مَرْفُوع للمبتَدَأ محذوف تَقْدِيرُهُ "أنا".
[TARGET_WORD]: العُرُوبَةِ، أوصابي
[IRAB_ANALYSIS]: مُضاف إِلَيْهِ مَجْرُورٌ.
[TARGET_WORD]: جملة (لا أَسْلُو)
[IRAB_ANALYSIS]: في مَحَلِّ رَفْعِ خَبَر ثانٍ للمبتدأ المحذوف "أنا".
[TARGET_WORD]: الرَّبُوعَ
[IRAB_ANALYSIS]: مَفْعُولٌ بِهِ مَنصُوبٌ.
[TARGET_WORD]: لَو
[IRAB_ANALYSIS]: حَرْفُ شَرْطٍ غَيْرِ جَازِمٍ.
[TARGET_WORD]: مثيرةً
[IRAB_ANALYSIS]: خَبَرٌ كَانَ مَنْصُوبٌ.

=== BLOCK 13: External Verse 3 ===
(Component: TEMPLATE_C_POEM.html)
[RIGHT_HEMISTICH]: تَغَلْغَلِي بينَ أَضْلاعي إلى كَبِدِي
[LEFT_HEMISTICH]: وَخَفَّفِي مِنْ حَرُورِ السَّائِلِ القاني

=== BLOCK 14: شرح وتحليل ===
(Component: TEMPLATE_C_BLOCK.html)
Title: شرح وتحليل
Content:
<span class="text-accent">الشرح:</span> اخترقي أيتها الرياح الشَّرْقِيَّةُ أضلاعي وابلغي أحشائي لتخففي مِنْ حرارَةِ نَارِ الشَّوْقِ الْمُسْتَعِرَةِ في داخلي.
<span class="text-accent">الفكرة:</span> تَصْوِيرُ شِدَّةِ الشَّوْقِ والحنين إلى الوطن.

=== BLOCK 15: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: تَغَلْغَلِي، خَفَّفِي
[IRAB_ANALYSIS]: فِعْلُ أَمْرٍ مَبْنِي على حذف النُّونِ.
[TARGET_WORD]: بينَ
[IRAB_ANALYSIS]: مَفْعُولٌ فِيهِ ظَرْفُ مَكانٍ مَنصُوبٌ.
[TARGET_WORD]: أَضْلاعي، السَّائِلِ
[IRAB_ANALYSIS]: مُضافُ إِلَيْهِ مَجْرُورٌ.
[TARGET_WORD]: القاني
[IRAB_ANALYSIS]: صِفَةٌ مَجْرُورَةٌ.

=== BLOCK 16: External Verse 4 ===
(Component: TEMPLATE_C_POEM.html)
[RIGHT_HEMISTICH]: وذكريني بِمَا أُنسِيتُ مِنْ أَمَلٍ
[LEFT_HEMISTICH]: وجَنِّحِينِي أُرَفْرِفْ فوق أوطاني

=== BLOCK 17: شرح وتحليل ===
(Component: TEMPLATE_C_BLOCK.html)
Title: شرح وتحليل
Content:
<span class="text-accent">الشرح:</span> جَدِّدِي أَيَّتُها الرياحُ الشَّرْقِيَّةُ أَمَلَ العودة إلى الوَطَنِ فِي نَفْسِي، وامنحيني جناحين؛ لأطير بهما إلى الوطن.
<span class="text-accent">الشعور:</span> الشَّوْقُ والحَنِين.
<span class="text-accent">الأداة:</span> التراكيب. المثال: جَنِّحِينِي أُرَفْرِفُ فوق أوطاني.
<span class="text-accent">البلاغة:</span> (ذكرينِي)، (أَرَفْرِف): استعارَةُ مَكْنِيَّة.

=== BLOCK 18: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: ذكريني، جَنِّحِينِي
[IRAB_ANALYSIS]: فِعْلُ أَمْرٍ مَبْنِي على حذف النون.
[TARGET_WORD]: بما
[IRAB_ANALYSIS]: الباءُ حَرْفُ جَرٍّ. ما اسمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ بِحَرْفِ الجَرِّ.
[TARGET_WORD]: أُنْسِيتُ
[IRAB_ANALYSIS]: فِعْلٌ مَاضٍ مَبْنِي لِلْمَجْهُولِ.
[TARGET_WORD]: جملة (أُنسِيتُ)
[IRAB_ANALYSIS]: صِلَةُ الموصول لا محل لها من الإعراب.
[TARGET_WORD]: أرفرفْ
[IRAB_ANALYSIS]: فعل مُضارع مَجْزُومٌ؛ لأنَّهُ جواب الطلب.
[TARGET_WORD]: فوق
[IRAB_ANALYSIS]: مَفْعُولٌ فِيهِ ظَرْفُ مكان منصوب.
[TARGET_WORD]: أوطاني
[IRAB_ANALYSIS]: مُضافُ إِلَيْهِ مَجْرُورٌ.

=== BLOCK 19: External Verse 5 ===
(Component: TEMPLATE_C_POEM.html)
[RIGHT_HEMISTICH]: أنا المهاجر لا أنسى الوداع وما
[LEFT_HEMISTICH]: جَرَى مِنَ الدمع في أَجْفان غزلان

=== BLOCK 20: شرح وتحليل ===
(Component: TEMPLATE_C_BLOCK.html)
Title: شرح وتحليل
Content:
<span class="text-accent">المفردات:</span> أجفان غزلان: يعني هنا عيون الأحبة. المهاجر: اسم فاعِلِ فِعْلُه هاجر.
<span class="text-accent">الشرح:</span> أنا القاطِنُ في بلاد الغُرْبَةِ، لا أستطيع نسيان لحظات الفراق المؤثرة، ولا سيما تلك الدموع السَّخِيَّة التي جادَتْ بها عُيُونُ الأَحِبَّةِ.
<span class="text-accent">الفكرة:</span> تأكيد عدم نسيانِ مَشْهَدِ فِرَاقِ الأحبة.
<span class="text-accent">الشعور:</span> الشَّوْقُ والحنين.
<span class="text-accent">الأداة:</span> التراكيب. المثال: لا أنسى الوداع.
<span class="text-accent">البلاغة:</span> (أجفان غزلان): استعارَةُ تَصْرِيحِيَّةٌ. (شَبَّهَ الْأَحِبَّة بالغزلان).

=== BLOCK 21: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
[TARGET_WORD]: أنا
[IRAB_ANALYSIS]: ضمير رفع مُنْفَصِلٌ فِي مَحَلِّ رَفْعِ مُبْتَدَأ.
[TARGET_WORD]: المهاجر
[IRAB_ANALYSIS]: خَبَرَ مَرْفُوع.
[TARGET_WORD]: جملة (لا أنسى)
[IRAB_ANALYSIS]: في محل رفع خبر.
[TARGET_WORD]: الوداع
[IRAB_ANALYSIS]: مَفْعُولٌ بِهِ مَنصوبٌ.
[TARGET_WORD]: ما
[IRAB_ANALYSIS]: اسم مَوْصُول في محل نصب اسم مَعْطُوفٌ.
[TARGET_WORD]: جملة (جَرَى)
[IRAB_ANALYSIS]: صِلَةُ الموصول لا محل لها من الإعراب.
[TARGET_WORD]: غزلان
[IRAB_ANALYSIS]: مُضَافُ إِلَيْهِ مَجْرُورٌ.

--- END STREAM ---
