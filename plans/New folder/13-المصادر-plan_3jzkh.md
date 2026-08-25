# **SESSION 13.0**

[TASK DEFINITION]
Objective: Implement المصادر.
File: `pages/13.0_nXX_المصادر.html`
Reference: Follow patterns in design_patterns.json.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 13
[CHAPTER_TITLE]: المصادر
[CATEGORY_HEADER]: 13
[SECTION_HEADER]: 13
[AUTHOR_NAME]: أ. حنا خفيف
[AUTHOR_PHONE]:

=== BLOCK 2: Definition Block ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المَصَادِرُ
Content: <p class="text-accent">المَصْدَرُ اسمٌ يَدُلُّ عَلَى الحَدَثِ مُجَرَّدًا مِنَ الزَّمَنِ، وَهُوَ الأَصْلُ الَّذِي تَصْدُرُ عَنْهُ الأَفْعَالُ، وَالأَسْمَاءُ المُشْتَقَّةُ.</p><p>فَالمَصْدَرُ (<span class="highlight-blue">ذَهَابٌ</span>) يَدُلُّ عَلَى حَدَثِ الذَّهَابِ لَكِنَّهُ لَا يَدُلُّ عَلَى وُقُوعِ الحَدَثِ فِي زَمَنٍ مُعَيَّنٍ، وَمِنْ هَذَا المَصْدَرِ نَأْخُذُ الفِعْلَ (<span class="highlight-blue">ذَهَبَ</span>) وَنَأْخُذُ مِنْهُ اسْمَ الفَاعِلِ (<span class="highlight-blue">ذَاهِبٌ</span>). وَالْجَدْوَلُ الْآتِي يُمَكِّنُ مِنْ مَعْرِفَةِ الْمَصَادِرِ السَّمَاعِيَّةِ وَالْقِيَاسِيَّةِ، وَمَعْرِفَةِ أَوْزَانِهَا:</p>

=== BLOCK 3: Semantic Split Grid ===
(Component: TEMPLATE_C_SPLIT.html)
Col 1: (Right)
    (Component: TEMPLATE_C_BLOCK.html)
    Title: الْمَصَادِرُ السَّمَاعِيَّةُ
    Content: <p>مَصَادِرُ الْأَفْعَالِ الثُّلَاثِيَّةِ سَمَاعِيَّةٌ، تُعْرَفُ بِالرُّجُوعِ إِلَى الْمُعْجَمَاتِ. فَهِيَ غَيْرُ قِيَاسِيَّةٍ إِذْ لَا يُمْكِنُ الِاعْتِمَادُ عَلَى قَاعِدَةٍ مُعَيَّنَةٍ لِمَعْرِفَتِهَا. وَلِلتَّأَكُّدِ مِنْ هَذَا الْكَلَامِ يَكْفِي أَنْ تَنْظُرَ إِلَى الْأَفْعَالِ التَّالِيَةِ وَإِلَى مَصَادِرِهَا:</p><p class="text-center font-bold">(<span class="highlight-blue">شَرِبَ</span>، شُرْبٌ) - (<span class="highlight-blue">ذَهَبَ</span>، ذَهَابٌ) - (<span class="highlight-blue">رَحِمَ</span>، رَحْمَةٌ) - (<span class="highlight-blue">طَافَ</span>، طُوفَانٌ) - (<span class="highlight-blue">عَلِمَ</span>، عِلْمٌ)</p>
Col 2: (Left)
    (Component: TEMPLATE_C_BLOCK.html)
    Title: الْمَصَادِرُ الْقِيَاسِيَّةُ
    Content: <p class="text-accent">لَهَا قَاعِدَةٌ مُعَيَّنَةٌ يُمْكِنُ الِاعْتِمَادُ عَلَيْهَا لِمَعْرِفَتِهَا.</p>
    (Component: TEMPLATE_C_LIST.html)
    - مَصَادِرُ الْأَفْعَالِ الرُّبَاعِيَّةِ.
    - مَصَادِرُ الْأَفْعَالِ الْخُمَاسِيَّةِ وَالسُّدَاسِيَّةِ.

=== BLOCK 4: Data Table for Quadriconsonant ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَوْزَانُ الْمَصَادِرِ الْقِيَاسِيَّةِ الرُّبَاعِيَّةِ
Content:
(Component: TEMPLATE_C_TABLE.html)
| وَزْنُ الْفِعْلِ | مِثَالٌ عَلَيْهِ | وَزْنُ الْمَصْدَرِ | مِثَالٌ عَلَيْهِ |
| --- | --- | --- | --- |
| فَعَّلَ | عَلَّمَ | تَفْعِيلٌ | تَعْلِيمٌ |
| أَفْعَلَ | أَقْبَلَ | إِفْعَالٌ | إِقْبَالٌ |
| فَاعَلَ | شَارَكَ | مُفَاعَلَةٌ | مُشَارَكَةٌ |
| فَعْلَلَ | زَلْزَلَ | فَعْلَلَةٌ | زَلْزَلَةٌ |

=== BLOCK 5: Rules for 5 and 6-letter words ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مَصَادِرُ الْأَفْعَالِ الْخُمَاسِيَّةِ وَالسُّدَاسِيَّةِ
Content: <p>الْأَفْعَالُ الْمَاضِيَةُ الْخُمَاسِيَّةُ جَمِيعُهَا تَبْدَأُ بِهَمْزَةِ وَصْلٍ (ا...)، أَوْ تَبْدَأُ بِتَاءٍ (ت...)، وَالْأَفْعَالُ الْمَاضِيَةُ السُّدَاسِيَّةُ لَا تَبْدَأُ إِلَّا بِهَمْزَةِ وَصْلٍ. وَيُمْكِنُ الِاعْتِمَادُ عَلَى هَذِهِ الْقَوَانِينِ اللُّغَوِيَّةِ فِي مَعْرِفَةِ مَصَادِرِ الْفِعْلَيْنِ الْخُمَاسِيِّ وَالسُّدَاسِيِّ:</p>
(Component: TEMPLATE_C_LIST.html)
- إِذَا بَدَأَ الْفِعْلُ الْخُمَاسِيُّ، أَوِ الْفِعْلُ السُّدَاسِيُّ <span class="highlight-blue">بِهَمْزَةِ وَصْلٍ</span> يَكُونُ مَصْدَرُهُمَا بِوَضْعِ <span class="highlight-red">أَلِفٍ</span> قَبْلَ الْآخِرِ، عَلَى هَذَا النَّحْوِ: (<span class="highlight-blue">اعْتَمَدَ</span>، اعْتِمَادٌ) - (<span class="highlight-blue">اسْتَقْبَلَ</span>، اسْتِقْبَالٌ).
- إِذَا بَدَأَ الْفِعْلُ الْخُمَاسِيُّ <span class="highlight-blue">بِتَاءٍ</span> يَكُونُ مَصْدَرُهُ بِوَضْعِ <span class="highlight-red">ضَمَّةٍ</span> قَبْلَ الْآخِرِ: (<span class="highlight-blue">تَدَافَعَ</span>، تَدَافُعٌ) - (<span class="highlight-blue">تَقَدَّمَ</span>، تَقَدُّمٌ).

=== BLOCK 6: Exceptions ===
(Component: TEMPLATE_C_BLOCK.html)
Title: حَالَاتٌ خَاصَّةٌ فِي الْمَصَادِرِ
Content: <p>يُضَافُ إِلَى الْبَيَانَاتِ الْمُدَوَّنَةِ فِي الْجَدْوَلِ السَّابِقِ الْحَالَاتُ الْخَاصَّةُ الْآتِيَةُ:</p>
(Component: TEMPLATE_C_LIST.html)
- لِبَعْضِ الْأَفْعَالِ الرُّبَاعِيَّةِ الَّتِي تَكُونُ عَلَى وَزْنِ (<span class="highlight-blue">فَاعَلَ</span>) مَصْدَرٌ آخَرُ سَمَاعِيٌّ هُوَ وَزْنُ (<span class="highlight-red">فِعَالٌ</span>)، نَحْوَ: (<span class="highlight-blue">قَاتَلَ</span>، قِتَالٌ)، (<span class="highlight-blue">جَاهَدَ</span>، جِهَادٌ).
- إِذَا كَانَ الْفِعْلُ الرُّبَاعِيُّ عَلَى وَزْنِ (<span class="highlight-blue">فَعَّلَ</span>) وَكَانَ مُعْتَلَّ الْآخِرِ، أَوْ مَهْمُوزَ الْآخِرِ يَكُونُ مَصْدَرُهُ عَلَى وَزْنِ (<span class="highlight-red">تَفْعِلَةٌ</span>)، نَحْوَ: (<span class="highlight-blue">رَبَّى</span>، تَرْبِيَةٌ)، (<span class="highlight-blue">جَزَّأَ</span>، تَجْزِئَةٌ).
- إِذَا كَانَ الْفِعْلُ الْخُمَاسِيُّ مَبْدُوءًا بِتَاءٍ وَكَانَ مُعْتَلَّ الْآخِرِ بِالْأَلِفِ يَكُونُ مَصْدَرُهُ بِتَحْوِيلِ الْأَلِفِ إِلَى يَاءٍ. نَحْوَ: (<span class="highlight-blue">تَمَادَى</span>، تَمَادِيًا).
- إِذَا كَانَ قَبْلَ آخِرِ الْفِعْلِ الرُّبَاعِيِّ أَوِ السُّدَاسِيِّ أَلِفٌ يُضَافُ إِلَى مَصْدَرِهِ تَاءٌ مَرْبُوطَةٌ. نَحْوَ: (<span class="highlight-blue">أَفَادَ</span>، إِفَادَةٌ)، (<span class="highlight-blue">اسْتَطَاعَ</span>، اسْتِطَاعَةٌ). أَمَّا إِذَا كَانَ قَبْلَ آخِرِ الْفِعْلِ الْخُمَاسِيِّ أَلِفٌ فَيَكُونُ مَصْدَرُهُ بِإِضَافَةِ يَاءٍ تَسْبِقُ هَذِهِ الْأَلِفَ. نَحْوَ: (<span class="highlight-blue">انْسَاقَ</span>، انْسِيَاقٌ)، (<span class="highlight-blue">ارْتَاحَ</span>، ارْتِيَاحٌ).

=== BLOCK 7: Note about Masdar acting like Verb ===
(Component: TEMPLATE_C_BLOCK.html)
Title: عَمَلُ الْمَصْدَرِ
Content:
(Component: TEMPLATE_C_BENEFIT.html)
Title: فَائِدَةٌ
Content: قَدْ يَعْمَلُ الْمَصْدَرُ عَمَلَ فِعْلِهِ، فَيَنْصِبُ مَفْعُولًا بِهِ إِنْ كَانَ فِعْلُهُ مُتَعَدِّيًا، نَحْوَ: إِطْعَامُكَ <span class="highlight-blue">الْيَتِيمَ</span> شَرَفٌ.

=== BLOCK 8: Solved Exam ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَمْثِلَةٌ تَطْبِيقِيَّةٌ تَدُورُ حَوْلَ الْمَصَادِرِ
Content:
(Component: TEMPLATE_C_EXAM_SOLVED.html)
Number: ١
Question: هَاتِ مَصْدَرَ كُلٍّ مِنَ الْأَفْعَالِ: (هَدَّمْتُ، وَارَى، اكْفَهَرَّ).
Answer: هَدَّمْتُ مَصْدَرُهُ: تَهْدِيمٌ - وَارَى مَصْدَرُهُ: مُوَارَاةٌ - اكْفَهَرَّ مَصْدَرُهُ: اكْفِهْرَارٌ.

(Component: TEMPLATE_C_EXAM_SOLVED.html)
Number: ٢
Question: هَاتِ مَصْدَرَ كُلٍّ مِنَ الْفِعْلَيْنِ الْآتِيَيْنِ، وَاذْكُرْ نَوْعَهُ: (غَشَّى - أَذَابَ).
Answer: (غَشَّى: تَغْشِيَةٌ - أَذَابَ: إِذَابَةٌ)، وَهَذَانِ الْمَصْدَرَانِ كِلَاهُمَا قِيَاسِيَّانِ.

(Component: TEMPLATE_C_EXAM_SOLVED.html)
Number: ٣
Question: مَا مَصْدَرُ كُلٍّ مِنْ: (يَتَجَلَّى - يُبْدِعُ - يَتَعَاطَى - يَتَفَهَّمُ)؟
Answer: يَتَجَلَّى: تَجَلٍّ - يُبْدِعُ: إِبْدَاعٌ - يَتَعَاطَى: تَعَاطٍ - يَتَفَهَّمُ: تَفَهُّمٌ.

(Component: TEMPLATE_C_EXAM_SOLVED.html)
Number: ٤
Question: هَاتِ مَصْدَرَ كُلٍّ مِنَ الْفِعْلَيْنِ الْآتِيَيْنِ: (تَأَنَّى - سَرَّحَ).
Answer: التَّأَنِّي - تَسْرِيحٌ.

(Component: TEMPLATE_C_EXAM_SOLVED.html)
Number: ٥
Question: اذْكُرْ مَصْدَرَ كُلٍّ مِنَ الْفِعْلَيْنِ الْآتِيَيْنِ: (ضَيَّعَنِي - يَنْجَبِلُ).
Answer: ضَيَّعَنِي: تَضْيِيعٌ - يَنْجَبِلُ: انْجِبَالٌ.

--- END STREAM ---
