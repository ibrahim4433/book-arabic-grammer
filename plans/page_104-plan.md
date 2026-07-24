# **SESSION 104**

[TASK DEFINITION]
Objective: Implement page 104.
File: `pages/page_104.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. Verify using `verify_layout.py`.
2.5 Cut Content: Use `TEMPLATE_CUT_BOX_PART_2.html` for the truncated prosody section at the top.
2.6 Cut Content Determinism: The top section is a continuation of prosody, mapped to `TEMPLATE_C_BLOCK.html` (wrapped in `TEMPLATE_CUT_BOX_PART_2.html`).
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`, `.highlight-green` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide: NO INLINE STYLES. Irab Words white.
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX') using `id_manager.py`.
8. Self-Correction: Run linting.
9. Do not summarize examples.
10. Do not provide uncompleted text content.
11. Preserve exact Tashkeel.
12. Visual Density: Dense page.
13. balanced page colors between teal and orange: Use `.block-header.accent` for at least one element (e.g. the Warning box).
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` with `.force-new-page`.
15. Exam section always at the end.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 104
[CHAPTER_TITLE]: page 104
[CATEGORY_HEADER]: 104
[SECTION_HEADER]: 104
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: تقطيع العروض (Cut Content Part 2) ===
(Component: TEMPLATE_CUT_BOX_PART_2.html -> TEMPLATE_C_BLOCK.html)
Title: تتمة تقطيع العروض
Content:
هُ لِأُفْقِ أَرْحَب فأعدد
이이 이 이
فعلائن فعلاتن فَاعِلُنْ
قَتْ بِهِ صَحْ راوه أصيد ضا
이어 이이이 이
فَاعِلَاتُنْ فَاعِلَاتُنْ فَاعِلُن
بحر الرمل

=== BLOCK 3: المستوى الإبداعي ===
(Component: TEMPLATE_C_BLOCK.html)
Title: المستوى الإبداعي
Content:
خَتَمَ الشَّاعِرُ قصيدتَهُ بِدَوْرِ الأَبْطَالِ فِي حماية الأَرْضِ وحفظ كرامتها ، أَضِفُ إِلَى هَذِهِ الخَالِمَةِ مَا يُعَرِّزُ هذا الدَّوْر.َ
بمقدور الطالب أن يجيب على هذا السؤال بالقول:
لا يَنْبَغِي لأَبْنَاءِ الوَطَنِ الأَبْطَالِ أَنْ يُخِلُوا بَادَاءِ مَسْؤوليتِهِم المتَمَثَلَةِ بِالحِفَاظِ على الأَرْض،ِ والدفاع عنها. فعلى عَاتِقِهِم تَقَعُ مَسْؤُولِيَّةِ حمَايَةِ ممتَلَكَاتِ المَوَاطِنِينِ الْخَاصَّة،ِ وَصَوْنِ مَرَافِقِ الوَطَنِ العَامَّة،ِ وَتَتَمَثَلُ بُطُولَةُ أَبْنَاءِ الوَطَنِ فِي أَعْلَى صُورِهَا فِي حِفَاظِهِم عَلَى ثَرَوَاتِ الْوَطَنِ وتَقْدِيمِ الفِدَاءِ لِتَأْمِينِ سَلَامَةِ أَرْوَاحِهِم. الماديَّةِ بِجَمِيعِ أَنْوَاعِهَا، وَحِفَاظِهِم على ثَرَوَاتِهِ البَشَرِيَّةِ عَنْ طَرِيقِ نَشْرِ الأَمْنِ فِي أَرْجَاءِ الوَطَنِ كَافَّة؛ لَيَحُولَ دُونَ هِجْرَةِ أَصْحَابِ الْعُقُول،ِ وتَتَجَلَّى البُطُولَةَ كَذَلِكَ فِي المُسَاهَمَةِ فِي عَمَلَيَّةِ بِنَاءِ الوَطَن،ِ وَالعَمَل على ازدِهَارِهِ وَتَقَدُّمِهِ مِنْ خِلَالِ الإِقْبَالِ على طَلَبِ العِلْم،ِ ومُتَابَعَةِ التَّحْصِيلِ العِلْمِي إلى أَعْلَى الْمُسْتَوَيَاتِ التَّعْلِيمِيَّة،ِ وَالسَّعْمِ الجَادَ لِتَطْوِيرِ الدَّاتِ عَنْ طَرِيقِ الاهتمام بالتَّقَانَةِ والبرمجة والحُوَاسِيبِ وَيَنْبَغِي الأَبِنَاءِ الوَطَنِ الْأَبْطَالِ أَلَّا يَغْضُوا الطَّرْفَ عَنْ تَجَارِبِ الأُمَمِ المَتَقَدِّمَةِ والخبراتِ التِي وَصَلَتْ إليها؛ لأَمَا عَامِلٌ فَعَالٌ فِي دَفْعِ عَمَلِيَّةِ التَّنمِيَةِ والازدهار.
وبمقدوري أن أقول :

=== BLOCK 4: التعبير الكتابي ===
(Component: TEMPLATE_C_BLOCK.html)
Title: التعبير الكتابي
Content:
حَرَرُ نَصَ )عُرْسِ المجد( مُسْتَعِينا بالفائدة الآتية:

=== BLOCK 5: الشعر ===
(Component: TEMPLATE_C_POEM.html)
كَفَّنَتْ أَجْدَادَنَا فِي جَوْفِها
وطَوَهم فِي ثِيابِ حُضْبِ
وسَيَأْتِي دَوْرُنا القاضي بأن
نُرْخِصَ الروح فداء الحسب

=== BLOCK 6: فائدة حول منهجية تحرير النص ===
(Component: TEMPLATE_C_BENEFIT.html)
Title: فائدة حول منهجية تحرير النص
Content:
(Inject Component: TEMPLATE_C_LIST.html)
- المقدمة: يستفاد في كتابتها من الموضوع الذي يدور حوله النص، أو ما ورد في مدخل النص.
- دراسة المستوى الفكري: تذكر الفكر والمعاني التي يتضمنها النص؛ أي يُذكر ما يتوافر في النَّصَ مِنْ فِكْرَةِ عَامَّة،ِ وَفِكَرِ فَرْعِيَّة،ِ ومعان.ٍ ] إِذا طَلِبَ تَحْرِيرُ نَصٍّ كامل، تُذَكَرُ الفِكَرُ الرئيسَةُ لمقاطعه، والمعاني المُندَرِجَةُ تَحْتَ كُلِّ فِكْرَةِ رَئِيسَةٍ بإيجاز لا يخل بالمعنى[
- دراسة المستوى الفني من الممكن أن تدرس في هذا المستوى:
بعض الوسائل التعبيرية )الصياغة اللفظية، الحقل المعجمي ......
- بعض العناصر البلاغية البارزة في النص المحسنات البديعية، الأساليب الخبرية والإنشائية، الصور البيانية، .(...
بعض عناصر المستوى التركيبي البارزة في النص الجملة الاسمية، الفعل الماضي، الفعل المضارع، فعل الأمر .....
- بعض العناصر الموسيقية البارزة في النص وحدة الوزن والقافية وحرف الروي، التكرار، حروف الهمس والجهر، .....
- الخاتمة: تظهر تكامل المستويين الفكري والفني وتأزرهما لإبراز مقولة النص الرئيسة، وإيصال مضمونه إلى المتلقي للتأثير فيه وإقناعه.

=== BLOCK 7: ملاحظة هامة ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: ملاحظة
Content:
لا يشترط في المستوى الفتي دراسة كل ما ذكر على سبيل الاستقصاء، وإنما يدرس ما هو بارز منها في النَّ؛ لأنَّ لكل نص أدبي مكونات فكرية، وأدوات تعبيرية، ووسائل فنية خاصة به.

=== BLOCK 8: Exam (التطبيق العملي) ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: يمكن الاستفادة من القالب الآتي من أجل تحرير النص وفق منهجية تحرير النص: يبدأ تحرير النص بمقدمة مناسبة وقد جَعَلَ الشَّاعِرُ ] يُذكر هنا اسم الشاعر ..... تذكر هنا الفكرة العامة التي تدور حولها الأبيات الثلاثة أو الأربعة ..... فكرة عامَّةً لِنَصِه الذي قَسَمَهُ إِلى ثلاث فكر فرعية أو أربع فكر فرعية ، ضمن كل واحدة منها في بيت من أبيات النص الثلاثة أو الأربعة ،[ فقد تضمن البيت
-  -   .

--- END STREAM ---
