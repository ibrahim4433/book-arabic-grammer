# **SESSION 188**

[TASK DEFINITION]
Objective: Implement page 188.
File: `pages/page_188.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`.
3. Text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice. (Applied 'Typo Exception' to logically reconnect scrambled OCR and remove isolated page numbers like ۱۸۸).
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide: NO INLINE STYLES. Use 100% templates.
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). Use `id_manager.py` to generate or verify them.
8. Self-Correction: Run `lint_pages.py --one-page-mode <filename>` after creating html files.
9. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal (Using TEMPLATE_C_BENEFIT_WARNING).
10. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html`.
11. The Strict Typographer Rule overrides the mandatory Exam section rule. Do not fabricate an Exam block since the raw text contains no exam.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Page Wrapper & Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 188
[CHAPTER_TITLE]: page 188
[CATEGORY_HEADER]: 188
[SECTION_HEADER]: 188
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Cut Box Part 2 ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
[UNIQUE_ID]: b18801
[BLOCK_TITLE]: الموازنة
[CONTENT]: - أ. نصر سمعان عبر عَنْ خَيْبَةِ أَمَلِهِ فِي الحُصُول على الرزق، بينما زكي قنصل عبر عن خَيْبَةِ أَمَلِ غَيْرِهِ فِي الحصول على الرزق.<br>- نصر سمعان يُحَمِّلُ الدَّهْرَ مَسْوولِيَّة خَيْبَةِ سَعْيهِ وَحِرْمَانِهِ مِنَ الرِّزْق، بينما زكي قنصل لم يحمل أَحَدًا خَيْبَةَ سَعْي البَنَّاء.ِ<br>- نصر سمعان أشار إلى غَفْلَةٍ أَبْنَاءِ الْمُجْتَمَعِ عَنْ مُعَانَاتِه،ِ بينما زكي قنصل لم يشر إلى غفلتِهِم عَنْ مُعَانَاةِ الْبَنَّاء.<br>- زكي قنصل صور مظاهر شَقَاءِ البَنَّاءِ فِي السَّعْي لكسب الرِّزْق،ِ بينما نصر سمعان لم يُصَوِّرُ مَظَاهِرَ شَقَائِه.ِ

=== BLOCK 3: المستوى الفني ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المستوى الفني
Content: <span class="text-accent">مِنْ سمات الواقعية القديمة في النَّص: النظرة إلى الواقع على أَنَّهُ مُعْطى ثابت لا يتغير، النَّظْرَةُ التشاؤمِيَّة،ُ مَثِّلْ لِكُلِّ سِمَةٍ مِمَّا سَبَقَ بِمِثال مناسب.</span>

=== BLOCK 4: الأمثلة ===
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: <span class="highlight-blue">النظر إلى الواقع عَلَى أَنَّهُ مُعطى ثابت لا يتغير :</span> (دامي الفؤادِ يَمَضُّهُ سَعَب،ُ يَنْبُو بِهِ فِي اللَّيْلِ مَضْجَعُه،ُ أَلم، داوي الجُفُونِ يَعَضُهُ لَا أَرَبُ).
[LIST_ITEM_CONTENT]: <span class="highlight-blue">النَّظْرَةُ التَّشَاؤُمية :</span> (يسعى ولكن لا إلى أَمَل،ِ يَدِبُّ لَكِنْ حَيْثُ يَشُوكُهُ الحَرْمَانُ وَالنَّصَبُ).
[LIST_ITEM_CONTENT]: في البيت الثالث تقديم وتأخيرٌ حَدَدْه،ُ وَاذْكُرْ فَائِدَتَه.ُ <br> <span class="highlight-red">ج -</span> تولَّتْ طمسَهُ التَّوَب،ُ قدَّمَ المفعول به طمسة على الفاعل النوب. وقد أفاد التقديم الدلالة على الأهمية، وأفاد التأخير التشويق.
[LIST_ITEM_CONTENT]: تَنَوْعَتِ المشاعِرُ فِي النَّص، سَمَ اثنين مِنْهَا، ثُمَّ اذكر أداة تعبير لِكُلِّ مِنْهُما. <br> <span class="highlight-red">ج -</span> الشُعُورُ : خيبة الأمل. أداة التعبير عَنْهُ : التَّراكيب. - المثال: تولَّتْ طَمَسَهُ النَّوَب.ُ <br> - الشعور : الألم. - أداة التعبير عَنْه:ُ الألفاظ. - المثال: (دامي، يمضه، ألم، ...).
[LIST_ITEM_CONTENT]: استخرج مِنَ الْمَقْطَعِ الثاني مثالا على: (الاستعارة، التشبيه)، مبينا وظيفتين مِنْ وَظَائِفِ كُلِّ مِنْهُما. <span class="highlight-red">ج -</span>

=== BLOCK 5: Core Matrix (الاستعارة والتشبيه) ===
(Component: TEMPLATE_C_TABLE.html)
[HEADER_1]: الصورة
[HEADER_2]: الوظيفة
[HEADER_3]: الشرح
[CELL_1]: <span class="text-accent">الاستعارة:</span> (يعضُّهُ سَغَبُ).
[CELL_2]: المبالغة، الشَّرْحُ وَالتَّوْضِيحُ
[CELL_3]: بالغ الشاعر في شرح معنى: شقاء البناء الكادح وجوعه وتوضيحه بتشبيههِ السَّغب (الجوع) بوحش يَعَض، حيث أراد أن يوصل إلى المتلقي الحد الأعلى من جوع البَنَّاء،ِ فَجَعَلَ الْمُتَخَيَّلَ كالمتحقق. شرحَتِ الصورة معنى: (شقاء البناء الكادح وجوعه) ووَضَحَتْ ذلك المعنى من خلال تشبيه السغب (الجوع) بوَحْشِ يَعَض،َ فأقنَعَتِ المتلقي بمضمون المعنى وصدقه.
[CELL_1]: <span class="text-accent">التشبيه :</span> (كَأَنَّا مِنْ بَعْضِهِ خَشَبُ).
[CELL_2]: الشَّرْحُ والتَّوْضِيحُ، الوَصْفُ والمحاكاة
[CELL_3]: شرحَتِ الصُّورة معنى: (قسوة الظروف التي يسعى فيها البنَّاءُ الكادِحُ لكسب الرزق) ووَضَحَتْ ذلك المعنى من خلال تشبيه راحة البناء بالخشب، فأقتَعَتِ المتلقي بمضمون المعنى وصدقه. اسْتَمَدَّتْ هَذِهِ الصُّورَةُ عَناصرها من الواقع المحسوس الذي حرصت على محاكاته، حيثُ شَبه الشاعر (راحة البنَّاءِ بالخشب)، وكلاهما عُنْصُران حِسِيَّان مُنْتَزَعَانَ مِنَ الواقع.

=== BLOCK 6: الجناس والموسيقا (Split) ===
(Component: TEMPLATE_C_SPLIT.html)
[UNIQUE_ID_1]: b18804
[COLUMN_1_TITLE]: الجناس
[COLUMN_1_CONTENT]: ه - هاتِ مِنَ البيت السابع جناسا، واذكُرْ نَوْعَهُ.<br><span class="highlight-red">ج -</span> الجناسُ : (يَمَضُّه،ُ يَعَضُّهِ) - نوعه جناس ناقص.
[UNIQUE_ID_2]: b18805
[COLUMN_2_TITLE]: الموسيقا الدَّاخِلِيَّةِ
[COLUMN_2_CONTENT]: - مِنْ مَصَادِرِ الموسيقا الدَّاخِلِيَّةِ فِي النَّص:َّ (التصريع، تكرارُ الأَخْرُفِ). مَثَلْ لِكُلِّ مِنْهُمَا بِمِثَالِ مُنَاسِب.<br><span class="highlight-red">ج -</span> التصريع: (خَرِبُ، تَعِبُ). - تكرار الأحرف في البيت الحادي عشر : (الصاد، الهاء، الياء، الواو، الباء، ...).

=== BLOCK 7: العروض (Benefit Warning) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: - قَطَعْ عروضيًّا البيت الثاني مِنَ النَّص، وسم بَحْرَه،ُ ثُمَّ حَدِّدْ قَافِيتَهُ وَرَوَيَّه.ُ <br> <span class="highlight-red">ج -</span> البَحْرُ الكامل.<br>والريح ما تَصْطَخب لكها الشوك يَز خُرُ فِي مسا <br> متفاعلن متفاعلن فعلن متفاعلن متفاعلن فعلن <br> ///o ///o //o ///o ///o //o <br> - القافية : تَصْطَخب = //// <br> - حَرْفُ الروي: الباء المضمومة المشبعة واوا.ً (تم تصحيح الرموز الكورية 이이이 إلى الرموز العروضية).

=== BLOCK 8: المستوى الإبداعي ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المستوى الإبداعي
Content: <span class="text-accent">حَوِّلِ المَقْطَعَ الْأَوَّلَ مِنَ النَّصِّ إِلَى نَصٍّ نَثْرِيِّ مُعْتَمِدًا النَّمَطَيْنِ السَّرْدِي وَالوَصْفِي.</span><br><br><span class="highlight-red">الإجابة :</span> إِنَّ البَنَّاءَ الكَادِحَ يُشَيِّدُ قُصُورَ الأَغْنياء الفارهة، في الوقت الذي يبدو فيه بيته المتواضِعُ وَضِيعًا مُهَدَّمًا، أَلَا سُحْقًا لِحَيَاتِهِ تلك الشَّقِيَّة التي لا يجنى فيها إلَّا المَتَاعِبَ و لا يَحْصُدُ فِيهَا إِلَّا المَعَانَاةَ، الحياة التي ملأت طرقها وأنحاءها الأَشْواك، وطغى على أجوائها عَصْفُ الريح وهُبُوبُها اللذين لا يَفْتُران ولا يَنْقَطعان. فهذا البائِسُ الكَادِحُ لَا يُشْرِقُ فِي لَيْلِهِ نُورٌ مِنَ الْأَمَلِ إِلَّا تَكَفَّلَتْ بِحَجْبِهِ وَمَحْوهِ المصائب والمِحَن.ُ وزاد معاناة هذا البَنَّاءِ الكَادِحِ تَفَرُّقُ الأَصْدِقَاءِ مِنْ حَوْلِه،ِ وابتعادهم عَنْه،ُ فَكُلما سعى وجد في طَلَبِهم عاد صفر اليدين، وباءَتْ جُهُودُهُ بِالفَشَل.ِ - -

--- END STREAM ---
