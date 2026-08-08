import re

def process_text():
    plan_content = """# **SESSION 287**

[TASK DEFINITION]
Objective: Implement page 287.
File: `pages/page_287.html` (Note: Use the exact page number.)
Reference: Follow patterns in design_patterns.json. Use Jules-workspace/id_manager.py to generate unique IDs if necessary.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 287
[CHAPTER_TITLE]: page 287
[CATEGORY_HEADER]: 287
[SECTION_HEADER]: 287
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Title ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ملحق الأبيات الخارجية المتممة الواردة في ديوان الشاعر محمود سامي البارودي:
Content:

=== BLOCK 3: Poem 1 ===
(Component: TEMPLATE_C_TWO_COLUMNS_WRAPPER.html)

--- COLUMN 1 ---
(Component: TEMPLATE_C_POEM.html)
Verse 1:
Hemistich 1: لَوْ لَمْ يَكُنْ فِي الْمَسَاعِي مَا يَبِيْنُ بِهِ
Hemistich 2: سَبْقُ الرِّجَالِ تَسَاوَى النَّاسُ فِي الْقِيَمِ

(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات
Content:
- <span class="highlight-blue">الْمَسَاعِي</span>: جَمْعُ الْمَسْعَاةِ، وَهِيَ الْمَكْرُمَةُ أَوِ السَّعْيُ فِي تَحْصِيلِ الْمَجْدِ.
- <span class="highlight-blue">يَبِيْنُ</span>: يَظْهَرُ وَيَتَّضِحُ.
- <span class="highlight-blue">الْقِيَمِ</span>: قِيمَةُ الشَّيْءِ قَدْرُهُ، وَجَمْعُهَا: الْقِيَمُ.

(Component: TEMPLATE_C_BLOCK.html)
Title: الشرح
Content: لَوْلَا سَعْيُ الرِّجَالِ إِلَى الْفَضَائِلِ وَالْمَكَارِمِ، تَسَاوَتْ أَقْدَارُهُمْ وَمَقَامَاتُهُمْ.

(Component: TEMPLATE_C_BLOCK.html)
Title: الفكرة
Content: مِعْيَارُ التَّفَاضُلِ بَيْنَ النَّاسِ سَعْيُهُمْ إِلَى الْفَضَائِلِ.

--- COLUMN 2 ---
(Component: TEMPLATE_C_IRAB.html)
[IRAB_TITLE]: الإعراب:
- <span class="highlight-red">مَا</span>: اِسْمٌ مَوْصُولٌ، فِي مَحَلِّ رَفْعِ اِسْمِ كَانَ.
- <span class="highlight-red">(يَبِيْنُ بِهِ سَبْقُ الرِّجَالِ)</span>: صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.
- <span class="highlight-red">(تَسَاوَى النَّاسُ)</span>: جُمْلَةُ جَوَابِ الشَّرْطِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.

=== BLOCK 4: Poem 2 ===
(Component: TEMPLATE_C_TWO_COLUMNS_WRAPPER.html)

--- COLUMN 1 ---
(Component: TEMPLATE_C_POEM.html)
Verse 1:
Hemistich 1: وَلِلْفَتَى مُهْلَةٌ فِي الدَّهْرِ إِنْ ذَهَبَتْ
Hemistich 2: أَوْقَاتُهَا عَبَثًا لَمْ يَخْلُ مِنْ نَدَمِ

(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات
Content:
- <span class="highlight-blue">مُهْلَةٌ</span>: يُرَادُ بِهَا هُنَا زَمَنُ الشَّبَابِ، وَصِحَّةُ الْجِسْمِ، وَقُوَّةُ الْإِدْرَاكِ، وَهُوَ زَمَنُ السَّعْيِ وَالنَّشَاطِ وَالْعَمَلِ وَالْإِنْتَاجِ.
- <span class="highlight-blue">ذَهَبَتْ أَوْقَاتُهَا عَبَثًا</span>: ضَاعَتْ فِي غَيْرِ فَائِدَةٍ.
- <span class="highlight-blue">لَمْ يَخْلُ مِنْ نَدَمٍ</span>: الْمُرَادُ لَمْ يَسْلَمْ.

(Component: TEMPLATE_C_BLOCK.html)
Title: الشرح
Content: تُسْنَحُ لِلْإِنْسَانِ فِي سِنِّ الشَّبَابِ فُرْصَةٌ إِذَا لَمْ يَسْتَثْمِرْهَا وَأَضَاعَهَا فِي غَيْرِ فَائِدَةٍ، لَمْ يَسْلَمْ مِنَ النَّدَمِ عَلَى إِهْدَارِهَا وَالتَّفْرِيطِ بِهَا.

(Component: TEMPLATE_C_BLOCK.html)
Title: الفكرة
Content: اِغْتِنَامُ الْفُرَصِ وَاسْتِثْمَارُ الْوَقْتِ.

--- COLUMN 2 ---
(Component: TEMPLATE_C_IRAB.html)
[IRAB_TITLE]: الإعراب:
- <span class="highlight-red">مُهْلَةٌ</span>: مُبْتَدَأٌ مَرْفُوعٌ.
- <span class="highlight-red">(لَمْ يَخْلُ)</span>: جُمْلَةُ جَوَابِ الشَّرْطِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.

=== BLOCK 5: Poem 3 ===
(Component: TEMPLATE_C_TWO_COLUMNS_WRAPPER.html)

--- COLUMN 1 ---
(Component: TEMPLATE_C_POEM.html)
Verse 1:
Hemistich 1: لَوْلَا مُدَاوَلَةُ الْأَفْكَارِ مَا ظَهَرَتْ
Hemistich 2: خَزَائِنُ الْأَرْضِ بَيْنَ السَّهْلِ وَالْعَلَمِ

(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات
Content:
- <span class="highlight-blue">مُدَاوَلَةُ الْأَفْكَارِ</span>: إِدَارَتُهَا بَيْنَ الْمُفَكِّرِينَ وَتَبَادُلُهَا.
- <span class="highlight-blue">خَزَائِنُ الْأَرْضِ</span>: كُنُوزُهَا وَذَخَائِرُهَا وَخَيْرَاتُهَا الْخَفِيَّةُ.
- <span class="highlight-blue">الْعَلَمِ</span>: الْجَبَلُ.

(Component: TEMPLATE_C_BLOCK.html)
Title: الشرح
Content: لَوْلَا تَبَادُلُ الْأَفْكَارِ بَيْنَ الْمُفَكِّرِينَ لَمَا ظَهَرَتْ كُنُوزُ الْأَرْضِ وَذَخَائِرُهَا، وَلَمَا اُسْتُثْمِرَتْ خَيْرَاتُهَا الْخَفِيَّةُ بَيْنَ سُهُولِهَا وَجِبَالِهَا.

(Component: TEMPLATE_C_BLOCK.html)
Title: الفكرة
Content: اِرْتِبَاطُ ظُهُورِ خَيْرَاتِ الْأَرْضِ بِتَبَادُلِ الْأَفْكَارِ بَيْنَ الْمُفَكِّرِينَ.

(Component: TEMPLATE_C_BLOCK.html)
Title: البلاغة
Content: (السَّهْلِ، وَالْعَلَمِ): طِبَاقُ إِيجَابٍ.

--- COLUMN 2 ---
(Component: TEMPLATE_C_IRAB.html)
[IRAB_TITLE]: الإعراب:
- <span class="highlight-red">مُدَاوَلَةُ</span>: مُبْتَدَأٌ مَرْفُوعٌ.
- <span class="highlight-red">(مَا ظَهَرَتْ خَزَائِنُ الْأَرْضِ)</span>: جُمْلَةُ جَوَابِ الشَّرْطِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.

=== BLOCK 6: Poem 4 ===
(Component: TEMPLATE_C_TWO_COLUMNS_WRAPPER.html)

--- COLUMN 1 ---
(Component: TEMPLATE_C_POEM.html)
Verse 1:
Hemistich 1: كَمْ أُمَّةٍ دَرَسَتْ أَشْبَاحُهَا وَسَرَتْ
Hemistich 2: أَرْوَاحُهَا بَيْنَنَا فِي عَالَمِ الْكَلِمِ

(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات
Content:
- <span class="highlight-blue">دَرَسَتْ</span>: فَنِيَتْ وَزَالَتْ.
- <span class="highlight-blue">الْأَشْبَاحُ</span>: جَمْعُ شَبَحٍ، وَشَبَحُ الشَّيْءِ: ظِلُّهُ وَخَيَالُهُ. وَيُرَادُ بِالْأَشْبَاحِ هُنَا: أَشْخَاصُ النَّاسِ وَأَجْسَادُهُمْ بَعْدَ الْمَوْتِ. يُقَالُ: هُمْ أَشْبَاحٌ بِلَا أَرْوَاحٍ.
- <span class="highlight-blue">سَرَتْ</span>: سَارَتْ مِنَ السُّرَى، وَهُوَ السَّيْرُ لَيْلًا، وَيُرَادُ هُنَا: الْحَرَكَةُ وَالْحَيَاةُ.
- <span class="highlight-blue">عَالَمِ الْكَلِمِ</span>: مَا نَقْرَؤُهُ وَنَتَدَاوَلُهُ مِنْ أَخْبَارِ الْأُمَمِ الْخَالِيَةِ وَسِيَرِهَا، وَعُلُومِهَا، وَفُنُونِهَا، وَآدَابِهَا.

(Component: TEMPLATE_C_BLOCK.html)
Title: الشرح
Content: كَثِيرٌ مِنَ الْأُمَمِ غَيَّبَ الْمَوْتُ عُلَمَاءَهَا وَأُدَبَاءَهَا وَأَفْنَى أَجْسَادَهُمْ، وَبَقِيَ نِتَاجُهُمُ الْعِلْمِيُّ وَالْأَدَبِيُّ حَاضِرًا فِيمَا نَقْرَؤُهُ وَنَتَدَاوَلُهُ فِي عَالَمِنَا مِنْ عُلُومٍ وَفُنُونٍ وَآدَابٍ.

(Component: TEMPLATE_C_BLOCK.html)
Title: الفكرة
Content: خُلُودُ عُلُومِ الْأُمَمِ السَّالِفَةِ بَعْدَ فَنَاءِ أَجْسَادِ مَنْ أَنْجَزُوهَا.

(Component: TEMPLATE_C_BLOCK.html)
Title: الشعور والأداة والمثال
Content:
- <span class="highlight-blue">الشعور</span>: إِعْجَابٌ.
- <span class="highlight-blue">الأداة</span>: التَّرَاكِيبُ.
- <span class="highlight-blue">المثال</span>: سَرَتْ أَرْوَاحُهَا بَيْنَنَا.

--- COLUMN 2 ---
(Component: TEMPLATE_C_IRAB.html)
[IRAB_TITLE]: الإعراب:
- <span class="highlight-red">كَمْ</span>: خَبَرِيَّةٌ مَبْنِيَّةٌ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعِ مُبْتَدَأٍ.
- <span class="highlight-red">(دَرَسَتْ أَشْبَاحُهَا)</span>: فِي مَحَلِّ رَفْعِ خَبَرٍ.
- <span class="highlight-red">أَشْبَاحُهَا، أَرْوَاحُهَا</span>: فَاعِلٌ مَرْفُوعٌ.

=== BLOCK 7: Poem 5 ===
(Component: TEMPLATE_C_TWO_COLUMNS_WRAPPER.html)

--- COLUMN 1 ---
(Component: TEMPLATE_C_POEM.html)
Verse 1:
Hemistich 1: فَانْظُرْ إِلَى الْهَرَمَيْنِ الْمَاثِلَيْنِ تَجِدْ
Hemistich 2: غَرَائِبًا لَا تَرَاهَا النَّفْسُ فِي الْحُلُمِ

(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات
Content:
- <span class="highlight-blue">الْهَرَمَيْنِ</span>: هُمَا الْهَرَمَانِ الْمِصْرِيَّانِ الْقَائِمَانِ عَلَى الْهَضَبَةِ الْغَرْبِيَّةِ تُجَاهَ الْجِيزَةِ.

(Component: TEMPLATE_C_BLOCK.html)
Title: الشرح
Content: إِنَّ الْهَرَمَيْنِ الْعَظِيمَيْنِ الْقَائِمَيْنِ عَلَى الْهَضَبَةِ الْغَرْبِيَّةِ تُجَاهَ الْجِيزَةِ لَمِمَّا يُدْهِشُ الْأَلْبَابَ، وَيُثِيرُ الْعَجَبَ الْعُجَابَ وَإِنَّمَا أَغْرَبُ مِنْ غَرَائِبِ حُلْمِ الْحَالِمِ، وَرُؤْيَا النَّائِمِ.

(Component: TEMPLATE_C_BLOCK.html)
Title: الشعور والأداة والمثال
Content:
- <span class="highlight-blue">الشعور</span>: إِعْجَابٌ.
- <span class="highlight-blue">الأداة</span>: التَّرَاكِيبُ.
- <span class="highlight-blue">المثال</span>: تَجِدْ غَرَائِبًا لَا تَرَاهَا النَّفْسُ فِي الْحُلُمِ.

--- COLUMN 2 ---
(Component: TEMPLATE_C_IRAB.html)
[IRAB_TITLE]: الإعراب:
- <span class="highlight-red">الْمَاثِلَيْنِ</span>: صِفَةٌ مَجْرُورَةٌ وَعَلَامَةُ جَرِّهَا الْيَاءُ.
- <span class="highlight-red">تَجِدْ</span>: فِعْلٌ مُضَارِعٌ مَجْزُومٌ؛ لِأَنَّهُ وَقَعَ جَوَابًا لِلطَّلَبِ، وَعَلَامَةُ جَزْمِهِ السُّكُونُ.
- <span class="highlight-red">(لَا تَرَاهَا النَّفْسُ)</span>: فِي مَحَلِّ نَصْبِ صِفَةٍ.

=== BLOCK 8: Poem 6 ===
(Component: TEMPLATE_C_TWO_COLUMNS_WRAPPER.html)

--- COLUMN 1 ---
(Component: TEMPLATE_C_POEM.html)
Verse 1:
Hemistich 1: صَرْحَانِ مَا دَارَتِ الْأَفْلَاكُ مُنْذُ جَرَتْ
Hemistich 2: عَلَى نَظِيرِهِمَا فِي الشَّكْلِ وَالْعِظَمِ

(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات
Content:
- <span class="highlight-blue">صَرْحَانِ</span>: مُثَنَّى صَرْحٍ، وَهُوَ الْبِنَاءُ الْعَالِي الذَّاهِبُ فِي السَّمَاءِ.
- <span class="highlight-blue">دَارَتِ الْأَفْلَاكُ</span>: تَعَاقَبَ الزَّمَانُ.
- <span class="highlight-blue">عَلَى نَظِيرِهِمَا</span>: أَيْ عَلَى نَظِيرِ الْهَرَمَيْنِ. وَنَظِيرُ الشَّيْءِ: مِثْلُهُ وَمُسَاوِيهِ.

(Component: TEMPLATE_C_BLOCK.html)
Title: الشرح
Content: لَمْ تَعْرِفِ الدُّنْيَا عَلَى تَعَاقُبِ الْأَزْمَانِ لِهَذَيْنِ الْهَرَمَيْنِ الْعَظِيمَيْنِ مَثِيلًا أَوْ شَبِيهًا، أَوْ نَظِيرًا فِي الْهَيْئَةِ وَالصُّورَةِ، وَالْعِظَمِ وَالضَّخَامَةِ.

(Component: TEMPLATE_C_BLOCK.html)
Title: الفكرة
Content: تَفَرُّدُ عَظَمَةِ الْهَرَمَيْنِ عَلَى امْتِدَادِ الزَّمَانِ.

(Component: TEMPLATE_C_BLOCK.html)
Title: الشعور والأداة والمثال
Content:
- <span class="highlight-blue">الشعور</span>: إِعْجَابٌ.
- <span class="highlight-blue">الأداة</span>: الْأَلْفَاظُ.
- <span class="highlight-blue">المثال</span>: الْعِظَمِ.

--- COLUMN 2 ---
(Component: TEMPLATE_C_IRAB.html)
[IRAB_TITLE]: الإعراب:
- <span class="highlight-red">صَرْحَانِ</span>: خَبَرٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْأَلِفُ.
- <span class="highlight-red">(مَا دَارَتِ الْأَفْلَاكُ)</span>: فِي مَحَلِّ رَفْعِ صِفَةٍ.
- <span class="highlight-red">مُنْذُ</span>: ظَرْفٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبِ مَفْعُولٍ فِيهِ ظَرْفِ زَمَانٍ.
- <span class="highlight-red">(جَرَتْ)</span>: فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ.

=== BLOCK 9: Poem 7 ===
(Component: TEMPLATE_C_POEM.html)
Verse 1:
Hemistich 1: تَضَمَّنَا حِكَمًا بَادَتْ مَصَادِرُهَا
Hemistich 2: لَكِنَّهَا بَقِيَتْ نَقْشًا عَلَى رَضَمِ

(Component: TEMPLATE_C_BLOCK.html)
Title: المفردات
Content:
- <span class="highlight-blue">تَضَمَّنَا</span>: اشْتَمَلَا.
- <span class="highlight-blue">بَادَتْ</span>: هَلَكَتْ وَفَنِيَتْ.
- <span class="highlight-blue">مَصَادِرُهَا</span>: مَصَادِرُ الْحِكَمِ.
- <span class="highlight-blue">الرَّضَمِ</span>: الصُّخُورُ الْعَظِيمَةُ.

(Component: TEMPLATE_C_BLOCK.html)
Title: الشرح
Content: اشْتَمَلَ الْهَرَمَانِ عَلَى حِكَمٍ غَيَّبَ الْمَوْتُ مَنْ أَنْجَزَهَا مِنْ قُدَمَاءِ الْمِصْرِيِّينَ؛ لَكِنَّهَا ظَلَّتْ مَنْقُوشَةً وَمَحْفُورَةً عَلَى صُخُورِ الْهَرَمَيْنِ الْعَظِيمَةِ.

=== BLOCK 10: Cut Content Part 1 ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
[BLOCK_TITLE]: الفكرة
[CONTENT]: خُلُودُ الْحِكَمِ الَّتِي

--- END STREAM ---
"""
    with open('plans/page_287-plan_9kdou.md', 'w', encoding='utf-8') as f:
        f.write(plan_content)

process_text()
