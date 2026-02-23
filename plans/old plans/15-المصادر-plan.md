# **SESSION 15.0**

[TASK DEFINITION]
Objective: Implement المصادر.
File: `pages/15.0_nXX_المصادر.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/15.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 15
[CHAPTER_TITLE]: المصادر
[CATEGORY_HEADER]: الصرف
[SECTION_HEADER]: المستوى اللغوي
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition of Masdar ===
(Component: TEMPLATE_C_BLOCK)
Title: تَعْرِيفُ المَصْدَرِ
Content: <p class="text-accent text-justify">المصدرُ اسمٌ يدلُّ على الحدَثِ مجرَّدًا مِن الزَّمنِ، وهو الأصلُ الذي تصدُرُ عنْهُ الأفعالُ، والأسماءُ المُشتقَّةُ. فالمصدرُ <span class="highlight-red">(ذهابٌ)</span> يدل على حَدَثِ الذَّهَاب لكنَّهُ لا يدلُّ على وقوعِ الحَدَثِ في زَمَنٍ مُعيِّنٍ، ومِنْ هذا المصدر نأخُذُ الفعلَ <span class="highlight-blue">(ذَهَبَ)</span> ونأخُذُ مِنْهُ اسم الفاعل <span class="highlight-green">(ذاهبٌ)</span>...</p>

=== BLOCK 3: Sama'iyya Sources ===
(Component: TEMPLATE_C_BLOCK)
Title: المَصَادِرُ السَّمَاعِيَّةُ (الثُّلَاثِيَّةُ)
Content: <p class="text-justify mb-2mm">مصادر الأفعال الثلاثيَّة سماعيَّة تُعرَفُ بالرُّجوع إلى المُعجمات. فهي غير قياسيَّة إذ لا يمكنُ الاعتمادُ على قاعِدةٍ مُعيَّنةٍ لمعرفتها. وللتأكُّدِ من هذا الكلام يكفي أنْ تنظرَ إلى الأفعال التالية وإلى مصادرها:</p>
(Component: TEMPLATE_C_LIST)
Title: أَمْثِلَةٌ عَلَى المَصَادِرِ السَّمَاعِيَّةِ
Items:
- شَرِبَ، <span class="highlight-red">شُرْب</span>
- ذَهَبَ، <span class="highlight-red">ذَهَاب</span>
- رَحِمَ، <span class="highlight-red">رَحْمَة</span>
- طَافَ، <span class="highlight-red">طُوفَان</span>
- عَلِمَ، <span class="highlight-red">عِلْم</span>

=== BLOCK 4: Qiyasiyya Sources (Quadriliteral) ===
(Component: TEMPLATE_C_TABLE)
Title: مَصَادِرُ الأَفْعَالِ الرُّبَاعِيَّةِ (القِيَاسِيَّةُ)
Columns: وَزْنُ الفِعْلِ | وَزْنُ المَصْدَرِ | مِثَالٌ
Rows:
- <span class="highlight-blue">فَعَّلَ</span> | <span class="highlight-red">تَفْعِيل</span> | عَلَّمَ - تَعْلِيم
- <span class="highlight-blue">أَفْعَلَ</span> | <span class="highlight-red">إِفْعَال</span> | أَقْبَلَ - إِقْبَال
- <span class="highlight-blue">فَاعَلَ</span> | <span class="highlight-red">مُفَاعَلَة</span> | شَارَكَ - مُشَارَكَة
- <span class="highlight-blue">فَعْلَلَ</span> | <span class="highlight-red">فَعْلَلَة</span> | زَلْزَلَ - زَلْزَلَة

=== BLOCK 5: Quinqueliteral and Sextiliteral Sources ===
(Component: TEMPLATE_C_BLOCK)
Title: مَصَادِرُ الأَفْعَالِ الخُمَاسِيَّةِ وَالسُّدَاسِيَّةِ
Content: <p class="text-justify mb-2mm">– الأفعال الماضية الخماسية جميعها تبدأ <span class="highlight-red">بهمزة وصل (ا...)</span>، أو تبدأ <span class="highlight-red">بتاء (تـ...)</span>، والأفعال الماضية السُّداسية لا تبدأ إلا بهمزة وصل.</p>
<p class="text-justify mb-2mm">– ويمكن الاعتماد على هذه القوانين اللُّغويَّة في معرفة مصادر الفعلين الخماسيِّ والسُّداسيِّ:</p>
(Component: TEMPLATE_C_LIST)
Title: قَوَاعِدُ صِيَاغَةِ المَصْدَرِ
Items:
- إِذَا بَدَأَ الفِعْلُ الخُمَاسِيُّ، أَوِ الفِعْلُ السُّدَاسِيُّ بِهَمْزَةِ وَصْلٍ يَكُونُ مَصْدَرُهُمَا بِوَضْعِ أَلِفٍ قَبْلَ الآخِرِ: <span class="highlight-blue">(اعْتَمَدَ، اعْتِمَاد)</span> – <span class="highlight-blue">(اسْتَقْبَلَ، اسْتِقْبَال)</span>.
- إِذَا بَدَأَ الفِعْلُ الخُمَاسِيُّ بِتَاءٍ يَكُونُ مَصْدَرُهُ بِوَضْعِ ضَمَّةٍ قَبْلَ الآخِرِ: <span class="highlight-blue">(تَدَافَعَ، تَدَافُع)</span> – <span class="highlight-blue">(تَقَدَّمَ، تَقَدُّم)</span>.

=== BLOCK 6: Special Cases ===
(Component: TEMPLATE_C_BLOCK)
Title: حَالَاتٌ خَاصَّةٌ فِي صِيَاغَةِ المَصَادِرِ
Content: <p class="mb-2mm">يُضَافُ إِلى البَيَانَاتِ المُدَوَّنَةِ فِي الجَدْوَلِ السَّابِقِ الحَالَاتُ الخَاصَّةُ الآتِيَةُ:</p>
(Component: TEMPLATE_C_LIST)
Title: مُلَاحَظَاتٌ هَامَّةٌ
Items:
- لِبَعْضِ الأَفْعَالِ الرُّبَاعِيَّةِ الَّتِي تَكُونُ عَلَى وَزْنِ <span class="highlight-blue">(فَاعَلَ)</span> مَصْدَرٌ آخَرُ سَمَاعِيٌّ هُوَ وَزْنُ <span class="highlight-red">(فِعَال)</span>، نَحْوَ: <span class="font-bold">(قَاتَلَ، قِتَال)، (جَاهَدَ، جِهَاد)</span>.
- إِذَا كَانَ الفِعْلُ الرُّبَاعِيُّ عَلَى وَزْنِ <span class="highlight-blue">(فَعَّلَ)</span> وَكَانَ مُعْتَلَّ الآخِرِ، أَوْ مَهْمُوزَ الآخِرِ يَكُونُ مَصْدَرُهُ عَلَى وَزْنِ <span class="highlight-red">(تَفْعِلَة)</span>، نَحْوَ: <span class="font-bold">(رَبَّى، تَرْبِيَة)، (جَزَّأَ، تَجْزِئَة)</span>.
- إِذَا كَانَ الفِعْلُ الخُمَاسِيُّ مَبْدُوءًا بِتَاءٍ وَكَانَ مُعْتَلَّ الآخِرِ بِالأَلِفِ يَكُونُ مَصْدَرُهُ بِتَحْوِيلِ الأَلِفِ إِلى يَاءٍ. نَحْوَ: <span class="font-bold">(تَمَادَى، تَمَادِي)</span>.
- إِذَا كَانَ قَبْلَ آخِرِ الفِعْلِ الرُّبَاعِيِّ أَوِ السُّدَاسِيِّ أَلِفٌ يُضَافُ إِلى مَصْدَرِهِ تَاءٌ مَرْبُوطَةٌ. نَحْوَ: <span class="font-bold">(أَفَادَ، إِفَادَة)، (اسْتَطَاعَ، اسْتِطَاعَة)</span>.
- أَمَّا إِذَا كَانَ قَبْلَ آخِرِ الفِعْلِ الخُمَاسِيِّ أَلِفٌ فَيَكُونُ مَصْدَرُهُ بِإِضَافَةِ يَاءٍ تَسْبِقُ هَذِهِ الأَلِفَ. نَحْوَ: <span class="font-bold">(انْسَاقَ، انْسِيَاق)، (ارْتَاحَ، ارْتِيَاح)</span>.

=== BLOCK 7: Benefit - Syntactic Function ===
(Component: TEMPLATE_C_BENEFIT)
Title: عَمَلُ المَصْدَرِ
Content: <p>قَدْ يَعْمَلُ المَصْدَرُ عَمَلَ فِعْلِهِ، فَيَرْفَعُ فَاعِلًا إِنْ كَانَ فِعْلُهُ لَازِمًا، وَيَنْصِبُ مَفْعُولًا بِهِ إِنْ كَانَ فِعْلُهُ مُتَعَدِّيًا. وَرَفْعُهُ لِلْفَاعِلِ نَادِرٌ؛ لِأَنَّهُ يُضَافُ إِلى فَاعِلِهِ غَالِبًا. نَحْوَ: <span class="highlight-red">إِطْعَامُكَ اليَتِيمَ شَرَفٌ</span>.</p><p><span class="font-bold">اليَتِيمَ:</span> مَفْعُولٌ بِهِ لِلْمَصْدَرِ (إِطْعَام) مَنْصُوبٌ، وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَةُ.</p>

=== BLOCK 8: Masdar Mimi ===
(Component: TEMPLATE_C_BLOCK)
Title: المَصْدَرُ المِيمِيُّ
Content: <p class="text-accent text-justify">مِثْلُ المَصْدَرِ العَادِيِّ، فَهُوَ اسْمٌ جَامِدٌ يَدُلُّ عَلَى حَدَثٍ مُجَرَّدٍ عَنِ الزَّمَانِ وَالمَكَانِ، وَلَكِنْ فِيهِ <span class="highlight-red">مِيمٌ زَائِدَةٌ</span> تُمَيِّزُهُ عَنِ المَصْدَرِ الطَّبِيعِيِّ. وَهُوَ مِنْ حَيْثُ الوَزْنُ وَالصِّيَاغَةُ نَفْسُ اسْمِ المَكَانِ، أَوْ اسْمُ الزَّمَانِ مِنَ الفِعْلِ الثُّلَاثِيِّ، وَمِنْ فَوْقِ الثُّلَاثِيِّ، وَيُفَرِّقُ بَيْنَهُ وَبَيْنَهُمَا سِيَاقُ الكَلَامِ لَا غَيْرَ، فَإِنْ دَلَّ عَلَى حَدَثٍ، كَانَ مَصْدَرًا مِيمِيًّا، وَإِنْ دَلَّ عَلَى مَكَانٍ، كَانَ اسْمَ مَكَانٍ، وَإِنْ دَلَّ عَلَى زَمَانٍ، كَانَ اسْمَ زَمَانٍ عَلَى النَّحْوِ التَّالِي:</p>
(Component: TEMPLATE_C_LIST)
Title: أَمْثِلَةٌ لِلتَّمْيِيزِ بَيْنَ الأَنْوَاعِ
Items:
- **اسْمُ مَكَانٍ:** مَوْقِفُ السَّيَّارَاتِ فِي الحَيِّ الجَنُوبِيِّ.
- **اسْمُ زَمَانٍ:** المَسَاءُ مَوْقِفُ العُمَّالِ عَنِ العَمَلِ.
- **مَصْدَرٌ مِيمِيٌّ:** كَانَ <span class="highlight-red">مَوْقِفُ</span> الرَّجُلِ مِنَ القَضِيَّةِ سَلْبِيًّا.

=== BLOCK 9: Masdar Sina'i ===
(Component: TEMPLATE_C_BLOCK)
Title: المَصْدَرُ الصِّنَاعِيُّ
Content: <p class="text-accent text-justify">اسْمٌ لَحِقَتْهُ يَاءُ النِّسْبَةِ، تَلِيهَا تَاءُ التَّأْنِيثِ المَرْبُوطَةِ لِلدَّلَالَةِ عَلَى مَعْنَى المَصْدَرِ؛ أَيْ كُلّ اسْمٍ أُضِيفَتْ إِلَيْهِ <span class="highlight-red">(يَّة)</span>. نَحْوَ: <span class="font-bold">(عِلْم، عِلْمِيَّة - هَمَج، هَمَجِيَّة - انْتِهَاز، انْتِهَازِيَّة - وَطَن، وَطَنِيَّة - ..)</span>.</p>

=== BLOCK 10: Warning - Sina'i vs Nisba ===
(Component: TEMPLATE_C_BENEFIT_WARNING)
Title: تَنْبِيهٌ هَامٌّ
Content: <p class="mb-2mm">يَنْبَغِي التَّفْرِيقُ بَيْنَ المَصَادِرِ الصِّنَاعِيَّةِ، وَبَيْنَ الأَسْمَاءِ المَنْسُوبَةِ الَّتِي تَلْحَقُهَا اليَاءُ المُشَدَّدَةُ وَالتَّاءُ المَرْبُوطَةُ. وَيَكُونُ ذَلِكَ بِالنَّظَرِ إِلى السِّيَاقِ عَلَى النَّحْوِ الآتِي:</p>
<ul class="structured-list">
<li><span class="font-bold">مَصْدَرٌ صِنَاعِيٌّ:</span> إِنَّ <span class="highlight-red">الْهَمَجِيَّةَ</span> صُورَةٌ مِنْ صُوَرِ الشُّعُوبِ المُتَخَلِّفَةِ. (لِأَنَّهَا مَصْدَرٌ تَجَرَّدَ لِلدَّلَالَةِ عَلَى مَعْنَى المَصْدَرِيَّةِ).</li>
<li><span class="font-bold">اسْمٌ مَنْسُوبٌ:</span> إِنَّ الدَّعَوَاتِ <span class="highlight-blue">الْهَمَجِيَّةَ</span> خَطَرٌ عَلَى شُعُوبِ العَالَمِ. (لِأَنَّهَا صِفَةٌ لِمَا قَبْلَهَا).</li>
</ul>

=== BLOCK 11: Applied Examples ===
(Component: TEMPLATE_C_SPLIT)
[LEFT_TITLE]: الإِجَابَاتُ
[RIGHT_TITLE]: الأَسْئِلَةُ
[LEFT_CONTENT]:
(Component: TEMPLATE_C_LIST)
Title:
Items:
- هَدَّمَتْ: <span class="highlight-red">تَهْدِيم</span> - وَارَى: <span class="highlight-red">مُوَارَاة</span> - اكْفَهَرَّ: <span class="highlight-red">اكْفِهْرَار</span>.
- غَشَّى: <span class="highlight-red">تَغْشِيَة</span> - أَذَابَ: <span class="highlight-red">إِذَابَة</span> (مَصَادِرُ قِيَاسِيَّةٌ).
- يَتَجَلَّى: <span class="highlight-red">تَجَلِّي</span> - يُبْدِعُ: <span class="highlight-red">إِبْدَاع</span>.
- يَتَعَاطَى: <span class="highlight-red">تَعَاطِي</span> - يَتَفَهَّمُ: <span class="highlight-red">تَفَهُّم</span>.
[RIGHT_CONTENT]:
(Component: TEMPLATE_C_LIST)
Title:
Items:
- هَاتِ مَصْدَرَ كُلٍّ مِنَ الأَفْعَالِ: (هَدَّمَتْ، وَارَى، اكْفَهَرَّ).
- هَاتِ مَصْدَرَ كُلٍّ مِنَ الأَفْعَالِ الآتِيَةِ، وَاذْكُرْ نَوْعَهُ: (غَشَّى - أَذَابَ).
- مَا مَصْدَرُ كُلٍّ مِن: (يَتَجَلَّى - يُبْدِعُ).
- مَا مَصْدَرُ كُلٍّ مِن: (يَتَعَاطَى - يَتَفَهَّمُ).

=== BLOCK 12: Masdar Mu'awwal ===
(Component: TEMPLATE_C_BLOCK)
Title: المَصْدَرُ المُؤَوَّلُ
Content: <p class="text-accent text-justify mb-2mm">هُوَ تَرْكِيبٌ لُغَوِيٌّ يَتَكَوَّنُ مِنْ حَرْفٍ مَصْدَرِيّ وَفِعْلٍ، أَوْ حَرْفٍ عَامِلٍ وَاسْمِهِ وَخَبَرِهِ، يُمْكِنُ تَأْوِيلُهُ بِمَصْدَرٍ صَرِيحٍ. وَالْفَرْقُ بَيْنَ مَصْدَرِ الصَّرِيحِ، وَالمَصْدَرِ المُؤَوَّلِ، أَنَّ الْمَصْدَرَ الصَّرِيحَ يُؤْخَذُ مِنْ لَفْظِ الفِعْلِ، وَيُذْكَرُ فِي الكَلَامِ بِلَفْظِهِ وَلَا يَحْتَاجُ إِلى تَأْوِيلٍ. أَمَّا الْمَصْدَرُ المُؤَوَّلُ، فَلَا يَكُونُ لَفْظًا مُفْرَدًا مَذْكُورًا فِي الكَلَامِ، وَإِنَّمَا يُؤَوَّلُ تَأْوِيلًا.</p>
(Component: TEMPLATE_C_LIST)
Title: أَشْكَالُ المَصْدَرِ المُؤَوَّلِ
Items:
- <span class="highlight-red">أَنْ وَالْفِعْلُ</span> الَّذِي يَأْتِي بَعْدَهُ، نَحْوَ: (أَرَادَ أَنْ يَقُولَ، أَغْضَبَنِي أَنْ قَالَ).
- <span class="highlight-red">أَنَّ وَاسْمُهَا وَخَبَرُهَا</span>، نَحْوَ: (عَلِمْتُ أَنَّكَ مُسَافِرٌ، بَلَغَنِي أَنَّهُ نَاجِحٌ).
- <span class="highlight-red">مَا الْمَصْدَرِيَّةُ وَالْفِعْلُ</span> الَّذِي يَأْتِي بَعْدَهَا، نَحْوَ: (انْهَضْ كَمَا نَهَضَ البَطَلُ).

=== BLOCK 13: Parsing Mu'awwal Table ===
(Component: TEMPLATE_C_TABLE)
Title: إِعْرَابُ المَصَادِرِ المُؤَوَّلَةِ
Columns: الجُمْلَةُ | تَحْوِيلُ المُؤَوَّلِ إِلى صَرِيح | إِعْرَابُ المُؤَوَّلِ
Rows:
- أَرَدْتُ <span class="highlight-red">أَنْ أُسَافِرَ</span>. | أَرَدْتُ <span class="highlight-blue">السَّفَرَ</span>. | فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.
- سَرَّنِي <span class="highlight-red">أَنَّكَ نَجَحْتَ</span>. | سَرَّنِي <span class="highlight-blue">نَجَاحُكَ</span>. | فِي مَحَلِّ رَفْعٍ فَاعِلٌ.
- انْهَضْ <span class="highlight-red">كَمَا نَهَضَ</span> البَطَلُ. | انْهَضْ <span class="highlight-blue">كَنُهُوضِ</span> البَطَلِ. | فِي مَحَلِّ جَرٍّ بِحَرْفِ الجَرِّ.

=== BLOCK 14: Poetic Evidence ===
(Component: TEMPLATE_C_POEM)
Title: شَوَاهِدُ شِعْرِيَّةٌ
Verses:
- كُلَّمَا قُلْتُ: فِي غَدٍ أُدْرِكُ السُّؤْ ... لَ أَتَانِي غَدٌ بِمَا لا أَشَــاءُ
- مِثْلَ <span class="highlight-red">ما يُبْدِعُ</span> السَّحَابُ إذَا ما ... عَانَــقَ الأَرْضَ بَعْدَ قَطْعِ الوِصَالِ
- أَهَبْتُ بِشُبَّانِ العِراقِ وإِنَّمَــا ... أردْتُ بِشِعْرِي <span class="highlight-red">أنْ أهِيجَ</span> سِبَاعَـا
- كُلُّ نَجْمٍ إلى الأُفُولِ ولكِنْ ... آفَةُ النَّجْــمِ <span class="highlight-red">أنْ يَخافَ</span> الأُفولا

=== BLOCK 15: Parsing Evidence ===
(Component: TEMPLATE_C_IRAB_ROW)
Title: إِعْرَابُ الشَّوَاهِدِ
Rows:
- (مَا + قُلْتُ): فِي مَحَلِّ جَرٍّ، مُضَافٌ إِلَيْهِ.
- (مَا + يُبْدِعُ): فِي مَحَلِّ جَرٍّ، مُضَافٌ إِلَيْهِ.
- (أَنْ + أُهَيِّجَ): فِي مَحَلِّ نَصْبٍ، مَفْعُولٌ بِهِ.
- (أَنْ + يَخَافَ): فِي مَحَلِّ رَفْعٍ، خَبَرٌ.

=== BLOCK 16: An-Nisba ===
(Component: TEMPLATE_C_BLOCK)
Title: النِّسْبَةُ
Content: <p class="text-accent text-justify">وَهِيَ إِضَافَةُ <span class="highlight-red">يَاءٍ مُشَدَّدَةٍ</span> مَسْبُوقَةٍ بِكَسْرٍ إِلَى آخِرِ الاسْمِ، لِلدَّلَالَةِ عَلَى نِسْبَةِ شَيْءٍ إِلَى آخِر. نَحْوَ: (دِمَشْق، دِمَشْقِيّ). وَالجَدْوَلُ الآتِي يُوَضِّحُ قَوَاعِدَ النِّسْبَةِ إِلَى الأَسْمَاءِ:</p>
(Component: TEMPLATE_C_TABLE)
Title: قَوَاعِدُ النِّسْبَةِ
Columns: المَنْسُوبُ | المَنْسُوبُ إِلَيْهِ (نَوْعُهُ) | التَّغْيِيرُ الحَاصِلُ
Rows:
- مَكِّيّ | مَكَّة (مَخْتُومٌ بِتَاءٍ مَرْبُوطَةٍ) | حُذِفَتِ التَّاءُ المَرْبُوطَةُ.
- دَيْرِيّ | دَيْرُ الزُّورِ (مُرَكَّبٌ إِضَافِيٌّ) | حُذِفَ المُضَافُ إِلَيْهِ وَنُسِبَ إِلَى المُضَافِ.
- حَضْرَمِيّ | حَضْرَمَوْتَ (مُرَكَّبٌ مَزْجِيٌّ) | نُحِتَ اسْمٌ، وَنُسِبَ إِلَيْهِ.
- جَلِيلِيّ | جَلِيل (مُفْرَدٌ مُذَكَّرٌ) | لَا تَغْيِيرَ عَلَيْهِ.
- قَبَلِيّ | قَبِيلَة (مُؤَنَّثٌ عَلَى وَزْنِ فَعِيلَة) | حُذِفَتِ اليَاءُ وَالتَّاءُ.
- صَحْرَاوِيّ | صَحْرَاء (مَمْدُودٌ مُنْتَهٍ بِهَمْزَةِ التَّأْنِيثِ) | قُلِبَتْ هَمْزَتُهُ (وَاوًا) عِنْدَ النِّسْبَةِ.

=== BLOCK 17: Exam ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: هَاتِ مَصَادِرَ الأَفْعَالِ الآتِيَةِ وَبَيِّنْ نَوْعَهَا (سَمَاعِيّ/قِيَاسِيّ):
(شَرِبَ - أَكْرَمَ - اسْتَغْفَرَ - دَحْرَجَ).
Number: ٢
Question: حَوِّلِ المَصْدَرَ المُؤَوَّلَ إِلَى مَصْدَرٍ صَرِيحٍ فِي الجُمَلِ الآتِيَةِ، ثُمَّ أَعْرِبْهُ:
- يَجِبُ أَنْ تَجْتَهِدَ لِتَنْجَحَ.
- سَرَّنِي مَا صَنَعْتَ مِنَ الخَيْرِ.
Number: ٣
Question: صُغِ المَصْدَرَ المِيمِيَّ وَالمَصْدَرَ الصِّنَاعِيَّ مِنَ الأَسْمَاءِ وَالأَفْعَالِ الآتِيَةِ:
(وَقَفَ - حُرّ - إِنْسَان - لَعِبَ).

--- END STREAM ---
