# **SESSION 187**

[TASK DEFINITION]
Objective: Implement page 187.
File: `pages/page_187.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html`.
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md` to identify the correct template to use for the continuation.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`, `.highlight-green` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   Rule: NO INLINE STYLES.
*   Rule: Irab Words inside `.irab-word` MUST be white.
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). Use "Jules-workspace/id_manager.py".
8. Self-Correction: Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...) .
11. You must preserve the exact Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense.
13. balanced page colors between teal and orange: make sure every page have minimum 1 element in orange.
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html`.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 187
[CHAPTER_TITLE]: page 187
[CATEGORY_HEADER]: 187
[SECTION_HEADER]: 187
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Listening Skills ===
(Component: TEMPLATE_C_LIST.html)
Title: مهارات الاستماع
Item 1: - ما أَبْرَز ما يعاني البناء؟ ج١ - يُعاني الحاجة والعوز وقلة الحظ، والتعب من العمل الشاق في ظل ظروف قاسية.
Item 2: - ٢- ما مَوْقِفُ الشَّاعِرِ مِنَ البَنَّاءِ كما بَدًا لَكَ فِي النَّص؟ ج -٢ أبدى التعاطف معه، وحاول أن يخفف من آلامه.

=== BLOCK 3: Reading Skills ===
(Component: TEMPLATE_C_LIST.html)
Title: مهارات القراءة: القِرَاءَةُ الصَّامِتَةُ :
Item 1: - لماذا بَدَتْ مُعاناةُ البَنَّاءِ مُضَاعَفَةً مُقارنَةً بمعاناةِ أَمْثَالِهِ فِي الوَطَنِ؟ ج -۱ لأنَّهُ يُعاني في بلاد الغربة حيث لا أهل ولا أصحاب، فقد رمَتْهُ الغربة في دُرُوبها المؤحِشَة،ِ فعاش في عزلةٍ مُؤْلِمَةِ .
Item 2: - ٢- ادْكُرْ ثلاث صفات بارزةِ لِلبَنَّاءِ فِي النَّص. ج - حظه عاثر، متعب، محروم.

=== BLOCK 4: Analysis ===
(Component: TEMPLATE_C_LIST.html)
Title: الاستيعاب والفهم والتحليل: المستوى الفكري:
Item 1: - اعمل مع أفراد مجموعتك على تنفيذ النشاط الآتي مُستعينا بِأَحَدِ المعجماتِ اللُّغَوِيَّة:ِ
Item 2: - اذكر معنى كُلِّ مِنْ : (يَنْبُو، يزدهي، كبا). ج- يَنْبُو: نَبَا جَنْبُهُ عن الفراش : لم يطمئن به ولم يستقر فيه. - يَزْدَهِي : يُضِيء. - كَبَا : تَعْثَر.َ

=== BLOCK 5: The Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Title: كَوَنْ مِنَ النَّصِ مُعْجَمًا لغويا لِكُلِّ مِنْ (المعاناة، الطبيعة).
Headers: المُعْجَمُ اللَّغَوِيُّ لِلْمُعاناة | المُعْجَمُ اللَّغَوِيُّ لِلطَّبيعة
Row 1: حرب، ساءَت، تعب، الشوك، يشوكه، سغب، الحرمان، النصب، النوب، دامي، يمضه، ألم، ذاوي، ... | الرياح، السحب، الريح، ليله، الليل، ...

=== BLOCK 6: Analysis Continuation ===
(Component: TEMPLATE_C_LIST.html)
Item 1: - ٢- اذكر الفِكْرَةَ التي بني عليها النص مستفيدا مِنَ الْمُعْجَمِينِ السابقين. ج٢ - وصف معاناة البناء الكادح، وتصوير حظه العاثر.
Item 2: - اصطدمت أماني المغتربين بواقع الحياة القاسِي في الغُرْبَةِ تَقَصَّ مَلامِحَ ذَلِكَ الواقع مِمَّا ورد فِي الْمَقْطَعِ الأَوَّل.ِ ج - إنَّه واقع يبرز فيه التفاوت بين الأغنياء المترفين والفقراء الأشقياء، مليء بالمعاناة والمتاعب خال من الأمل، يعيش فيه المهاجر معزولا، فلا أهل ولا أصحاب، يحيا حياة شقية لا يجد فيها راحة في نهاره، ولا هناء عند هجوعه.
Item 3: - صَوَّرَ الشَّاعِرُ فِي المقطع الثاني مَظَاهِرَ الشَّقَاءِ فِي السَّعْي لِكَسْبِ الرَّزْق.ِ اذكرها، وبين أيها أكثر تأثيرا في نفسك. ج - تمثلت مظاهر شقاء البناء الكادح في سعيه الدؤوب الحاد وفي آلام قلبِهِ وأَحَزَانِهِ وَمَشَفَّتِهِ وُجُوعِه،ِ وَعَمَلِهِ الذي لا يجنِي فِيهِ ثَرَة.ً في ظل ظُرُوفٍ قَاسِيَة؛ حَيْثُ يَبَدُو مُرْتَجِفًا يُقَاسِي البَرَدَ القَارِس، فَمِن شِدَّةِ الْبَرَدِ غَرِقَتِ عَيْنَاهُ فِي الدموع التي الصَقَتْ أَهْدَابِهِ بِبَعْضِها، وقد التصقت يَدَهُ بِمقبَضِ قُذُومِهِ التي يَنحَتْ بها الحجارة ويقطَعُهَا . أما الرِّيَاحُ البَارِدَةِ فَتَصَفَعُهُ بِهُبُوبَهَا الْعَاصِف، بَيْنَمَا السَّمَاءُ تَسْكُبُ أَمْطَارِهَا فَوْقَ جَسَدَهُ الْمُتَعَب. وإِنَّ هَذِهِ الْمَشَاهِدَ القاسِيَةَ لَتَحُزَّ القَلْبَ بِسِكين الأَسَى، وتعصُرُه بِشِدَّةِ الْأَلم.
Item 4: ه- بلَغَتْ مُشاركةُ الشَّاعِرِ البَنَّاءَ مُعاناتهُ حَدَّ الذُّروة في البيتِ الثَّامِنِ بَيِّنْ ذَلِكَ. جه - بَلَغَ مِن مُشَارَكَةِ الشَّاعِرِ البَنَّاءِ فِي مُعَانَاتِهِ أَنْ فَدَى نَظَرَتَهُ فِي كَانُونَ وَمُسَانَدَتِهِ بِرُوحِه.ِ
Item 5: - عَدَّ الشَّاعِرُ مُعَانَاةَ البَنَّاءِ جُزْءًا مِنْ مُعاناةِ المُغَرَّبِينَ المُنْسَيِّينَ فِي مَجَاهِلِ الغُرْبَةِ وَضِحْ ذَلِكَ مِنْ فَهْمِكَ الْمَقْطَعَ الثَّالِث.َ ج - يُصَوِّرِ الشَّاعِرِ وَاقِعِ حَال البنَّاءِ الكَادِح فِي غُرَبَتِهِ مُحَاولا إِثارة انتباه المجتمع ولَفَتَ نَظَرِهِ نَحْوَه،ُ مِن أَجل الاهتمام به والاعتراف بِمَجْهُودَاتُهُ وَتَفَانِيهِ فِي عَمَلِه،ِ ويدعوة إلى الصبر على قسوة الحياة، والابتعاد عَنِ الغَضَب؛ لِأَنَّهُ لَا يُفرج الكرب، ويُؤْكِدُ لَهُ أَنَّهُ لَيْسَ أَوَّلَ كَادِحِ ضَاعَتِ مَجْهُودَاتُهُ هَدَرًا فِي بِلَادِ الغُربة.

=== BLOCK 7: Warning Benefit ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: - دعا الشَّاعِرُ البَنَّاءَ إلى الصَّبْرِ على واقعه اقترح حلولا أخرى لِلحَدٍ مِنْ مُعاناتِهِ؟ ج - التَّحَلِّي بِالصَّلَابَةِ أَمَامٍ قَسْوَةِ الواقع، تَحَدِي الواقع المر وعدم الاستسلام له والاستكانة لصعوباته، العودة إلى الوطن.

=== BLOCK 8: Poem ===
(Component: TEMPLATE_C_POEM.html)
Title: - قَالَ الشَّاعِرُ المَهْجَرِيُّ نَصْر سمعان :
Right Hemistich 1: أسعى وراء الرّزْقِ مُجِتَهِدًا
Left Hemistich 1: والدهر في الحرمان يجتهد
Right Hemistich 2: وأجوب أطراف البلاد ولا
Left Hemistich 2: يدري بما في مُهْجِتِي أَحَدُ

=== BLOCK 9: Comparison ===
(Component: TEMPLATE_C_LIST.html)
Title: وازن بين هذين البيتين والمَقْطَعِ الثَّانِي مِنَ النَّصَ مِنْ حَيْثُ الْمَضْمُون.ِ
Item 1: ج - التَّشَابُهُ :
Item 2: - كلا الشاعرين يعبر عن السعي الجاد وراء الرزق دون جدوى.
Item 3: - كلا الشَّاعِرَين يُعَبِّرُ عَنْ خَيْبَةِ أَمَلِهِ فِي الحُصُول على الرزق.

=== BLOCK 10: Cut Content ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
Title: - الاختلاف:

--- END STREAM ---
