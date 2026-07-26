# **SESSION 149**

[TASK DEFINITION]
Objective: Implement page 149.
File: `pages/page_149.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
2.5 Cut Content: Content starts with "الإجابة:", meaning it is continuing from the previous page. Use `TEMPLATE_CUT_BOX_PART_2.html` wrapping a `TEMPLATE_C_BLOCK.html` to represent the continuation.
2.6 Cut Content Determinism: The keyword "الإجابة:" maps to a standard block.
3. Text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice. Handled OCR column-jumbling in the analysis section and poetry correctly.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`, `.highlight-green` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   **Rule:** NO INLINE STYLES.
*   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
*   **Mapping:** Use classes instead of inline styles.
*   **1-PAGE MODE RULE**: Replace any `<section>` tags from the templates with `<div>` tags (except `<header>`).
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX') on the replacing `<div>`. Use "Jules-workspace/id_manager.py" to generate or verify them.
8. Self-Correction: Run `lint_pages.py` after generation.
9. Do not summarize examples.
10. Do not provide uncompleted text content.
11. Preserve exact Tashkeel, fix obvious typos (Typo Exception).
12. Visual Density: Dense page.
13. Balanced colors: Added Orange via `.block-header.accent` and `TEMPLATE_C_BENEFIT_WARNING.html`.
14. Wrapper: Use `TEMPLATE_C_PAGE_WRAPPER.html` for all content.
15. Exam Section: End of lesson exam with no answers.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 149
[CHAPTER_TITLE]: page 149
[CATEGORY_HEADER]: 149
[SECTION_HEADER]: 149
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Cut Content Continuation (The Analysis) ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
Inner Template: TEMPLATE_C_BLOCK.html
Title: الإجابة:
Content: الشَّعْرُ مِرَاةٌ تَعْكس مخزونات العقل الباطني للشاعر، فالشّعْرُ مَجْلَّى يُنْشَرُ فِيهِ ما انطوى في نفسية الشاعر من مكنونات اختزنها اللاشُعُور،ُ وَيَتَمَثَلُ هذا عند الشاعر نديم محمد الذي يَكْشِفُ عَمَّا تواري في خزائن اللاشُعُور. فعلى مستوى معاني النَّصَ نَجِدُ أَنَّ الشَّاعِرَ يَبْدأ المَقْطَعَ الأَوَّلَ بِنداءِ شُعُوره، وَنَعْتِهِ بِالحَيَّةِ التِي تَنْفُتُ السَّمَّ فِي قَلْبِهِ بِغَزارة وكثافة، وكأنها امتلكت ألف نابِ يَضُحُ السُّمَّ ويدسه في قلبه. ثم لا يلبث أن يجعله السبب في تفاقم مرضه واستفحالِه،ِ فيؤكد أن شعوره قد جعل حزنه يبلغ الذروة، وجعل عذابه يمتد ويطُولُ وَيَبْدَأُ المَقْطَعَ الثاني بالتأكيد على أنَّ الدَّهْر قد تغلب عليه لأَنَّهُ عَالَبَهُ بالهوى، فَلَو غالبه بغيره لانتصر عليه انتصارا ساحقًا ولنَصَبَ قِبَابَهُ بِينَ الشُّهب في أعالي السماء. ولَطَوَّفَ فيها لاهِيَا يَرْفل برداء الانتصار، ويلاعِبُ وجنةَ البَدْر. وعلى مستوى استجلاء الظَّاهِرَةِ النَّفْسِيَّةِ نَجِدُ أَنَّ المعاني السابقة قد كَشَفَتْ مُعاناةً نَفْسِيَّةً عَمِيقَةً مَصْدَرُها حُبُّ مُخْفِق،ْ وآمالٌ مُنْكَسِرَة.ً ونَجِدُ الشَّاعِر،َ على مستوى تأويل الظَّاهِرَة،ِ يَنْدَفِعُ إلى التسامي النَّفْسِيِّ بِالتَّخَاذِهِ الفَنَّ الْمُبْدِعَ وسيلةً لِلتَعْبيرِ عَنْ مَكْنُونَاتِهِ الْمُكْبُونَةِ فِي اللَّاشُعُور،ِ وَقَدِ اتَّخَذَ اللاشُعُورُ لَدَى الشَّاعِرِ أشكالا فَنِّيَّةً لِلكَشْفِ عَنْ نَفْسِهِ مَعَ بَقَائِهِ مُتواريًا، تمثلت بما يأتي:

=== BLOCK 3: Forms of the Subconscious - The Words ===
(Component: TEMPLATE_C_BLOCK.html)
Title: - الألفاظ
Content: <span class="text-accent">الألفاظ الموحِيَةُ بمعانٍ جَدِيدَةِ أَخْرَجَهَا السياقُ عَنْ معانيها المُعْجَمِيَّةِ وَالحِسَيَّةِ إِلَى مَعَانِ مُتَّشِحَةٍ بِظِلَالِ اللَّاشُعُورِ وَأَطْيَافِهِ</span> وَقَدْ شَكَّلَتْ هَذِهِ الْأَلْفَاظُ فِي النَّصَ مُعْجَمَيْنِ لُغَوِينِ : (المعاناة) و(السَّعَادَةِ).

=== BLOCK 4: The Core Matrix (المعجمان) ===
(Component: TEMPLATE_C_TABLE.html)
Table Content:
| مُعْجَم المعاناة | مُعْجَمِ السَّعَادَةِ |
| --- | --- |
| وانْدَرَجَتْ تَحْتَهُ الألفاظ الآتية: (علتي، حزني، عذابي، السم) | على حين اندرَجَتْ تَحْتَهُ الأَلفاظ الآتية: (النجوم، هوى، دعابي) |

=== BLOCK 5: Matrix Follow-up ===
(Component: TEMPLATE_C_BENEFIT.html)
Content: والمعجمان السَّابِقَانَ يَكْشِفَانِ محاولات اللاشْعُورِ فِي التَّعْبِيرِ عَنْ نَفْسِه،ِ وميله إلى إشباع حاجاتهِ مِنْ خلال إنكار المعاناةِ وَالبُعْدِ عَنْهَا، وَبُلُوعِهِ لَذَّةَ السَّعَادَةِ فَالْمُعْجَمُ الثاني (السَّعَادَةِ) يَسْعَى إلى طَمْسِ الْمُعْجَمِ الأَوَّلِ (المعاناة)، والقَفْزِ فوقه إلى آفاق جديدة عبر الارتفاع والتَّسَامِي الدَّائِمَيْن.ِ

=== BLOCK 6: Forms of the Subconscious - The Symbol ===
(Component: TEMPLATE_C_BLOCK.html)
Title: - الرَّمْزُ
Header Class: accent
Content: <span class="text-accent">أَمَّا الشَّكُلُ الآخَرُ الذي اتَّخَذَهُ اللَّاشُعُورُ عِنْدَ الشَّاعِرِ فِي التعبيرِ عَنْ مَكْنُونَاتِهِ فهو الرُّمُوزُ الدالة على حالاتٍ نَفْسِيَّةِ كَامِنَةِ</span> إِذْ رَمز بالحية إلى الألم والعذاب اللذين يعاني منهما بِسَبَبِ مَشَاعِرِ الْحُبّ الْمُخْفِق.ِ ورَمَزَ بِالنُّجُوم إلى السعادة التي في أعماقِ اللَّاشُعُورِ يَرْغَبُ بِبُلُوعِهَا .

=== BLOCK 7: Forms of the Subconscious - The Images ===
(Component: TEMPLATE_C_BLOCK.html)
Title: - الصور
Content: <span class="text-accent">أَدَّتِ الصور وظيفةً فِي التَّعْبِيرِ عَنْ مَكْنُونَاتِ اللَّاشُعُور؛ إِذْ تَجَرَّدَتْ مِنْ حِسَيتها، واصطبعت بما أضفاهُ اللَّاشُعُورُ عليها، حَتَّى بَاتَتْ خَيْرَ مُعَبَرِ عَنْ الْأَفكارِ اللَّاشْعُورِيَّةِ التي يُحَوَهَا اللَّاشْعُورُ إِلَى صُورٍ يَقْتَحِمُ بها ساحة الوعي ورقابته الصَّارِمَةَ.</span> وَمِنْ تِلْكَ الصُّورِ صُورَةُ (يا شُعُوري، يَا حَيَّة) التي اصطَبَغَتْ بما أَضْفَاهُ اللاشُعُورُ عليها من آلام ومعاناة، فَكَانَتْ خَيْرَ مُعَبِّرِ عَنْ مُعَانَاةَ الشَّاعِرِ الْمُكْبُونَةِ لتجاوز خَيْبَةَ الْأَمَلِ فِي أَعْمَاقِه.ِ وصورة (يطاولني الدهر بغير الهوى) التي اصطبعت بما أَضْفَاهُ اللَّاشُعُورُ عليها من آلام وأحلام، والانكسار أَمَامَ دَهْرِ عَالَبَ الشَّاعِر،َ فَكَانَتْ خَيْرَ مُعَبِّرِ عَمَّا كَانَ مَكْبُونَا فِي أَعْمَاقِه.ِ

=== BLOCK 8: Summary of Psychological Analysis ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: ومِمَا سَبَقَ نَرَى أَنَّ النَّصَّ الأَدَبِيَّ في التحليل السابق، كَشَفَ عَنْ سَعْي اللَّاشُعُورِ إِلى التعبيرِ عَنْ نَفْسِهِ بِوَسَائِلَ فَنِيَّةٍ مُتَنَوَعَة،ٍ شَكَّلَتْ اليَّاتٍ نَفْسِيَّة تجاوزَتْ رقابَةَ الشَّعُور،ِ وَسَعَتْ عبرَ النَّصَ إلى البوح بمكنُونَاتِ اللَّاشُعُورِ الَّذِي جَعَلَ النَّصَ - برأي الاتِّجَاهِ النَّفْسِي - تمثيلًا رَمْزِيَّا لِمُعْطياتِ اللَّاشُعُورِ الْمَكْبُونَة.ِ

=== BLOCK 9: Linguistic Applications ===
(Component: TEMPLATE_C_BLOCK.html)
Title: التطبيقات اللغوية:
Content: أعرب ما وُضِعَ تَحْتَهُ خط في البيت الآتي:

=== BLOCK 10: Poem for Irab ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: يا شُعُورِي يَا حَيَّةً تَنْفُتُ السُّمْ
Hemistich 2: مَ فَيَجْرِي فِي القَلْبِ مِنْ أَلْفِ نَابِ

=== BLOCK 11: Irab Details ===
(Component: TEMPLATE_C_IRAB.html)
Row 1 Word: يا شُعُورِي
Row 1 Details: ج -۱ يا، أداة نداء. شعوري: منادى مضافُ مَنْصُوب، وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ المُقَدَّرَةُ على ما قَبْلِ يَاءِ الْمُتَكَلِّمِ مَنَعَ ظهورها اشتغالُ المَحَلِ بِالحَرَكَةِ المناسِبَة،ِ والياء، ضَمِيرٌ مُتَصِلٌ مَبْنِي على السكون فِي مَحَلِّ جَرٍّ مُضَافُ إِلَيْه.ِ
Row 2 Word: يا حَيَّة
Row 2 Details: منادى نَكِرَةٌ غَيْرُ مَقْصُودَة،ِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَة.ُ

=== BLOCK 12: Linguistic Activity ===
(Component: TEMPLATE_C_BLOCK.html)
Content: - اقرأ البيت الآتي، ثُمَّ نَفِّذِ النَّشاط :

=== BLOCK 13: Poem for Activity ===
(Component: TEMPLATE_C_POEM.html)
Hemistich 1: وَلَطَوَّفْتُ بِالنَّعِيمِ فَرَشَّتْ
Hemistich 2: نِي حِسَانُ النَّعِيمِ بِالْأَطيابِ

=== BLOCK 14: Activity Question & Answer ===
(Component: TEMPLATE_C_BENEFIT.html)
Content: - تَعَجَّبْ مِنَ الفِعْلِ (طَوَّفْتُ بِالنَّعِيم) الوارد في البَيْتِ السَّابِقِ بَصِيفَتَيَ التَّعجب القياسيتين.<br><br> ج - ما أجمل أنْ أُطَوّفَ بِالنَّعِيم - أجمل بأنْ أُطَوِّفَ بِالنَّعِيم ! - ما أجمل تطويفي بالنعيم ! - أَجْمِل بتطويفي بالنعيم!

=== BLOCK 15: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: اذْكُرِ الوَزْنَ الصَّرْفِي للأسماء والأفعال الواردة في البيت الآتي:<br><br> <span class="text-center block font-bold">لو بِغَير الهوى يُطَاوِلُنِي الدَّهْـ *** ـرُ لأَرْكَزْتُ فِي النُّجُومِ قبابي</span>

--- END STREAM ---
