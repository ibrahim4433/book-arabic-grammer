# **SESSION 171**

[TASK DEFINITION]
Objective: Implement page 171.
File: `pages/page_171.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`. Ensure exact visual continuity.
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md`.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice. Typo Exception applied.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green`  for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   **Rule:** NO INLINE STYLES.
*   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
6. Templates: You are forbidden from inventing new HTML tags or classes or template elements. You must map all content using "Jules-workspace/Templates/" components. Replace `<section>` tags with `<div>` tags (keep `<header>`).
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). The ID MUST be applied to the `<div>` tag that replaced the `<section>` tag. Use "Jules-workspace/id_manager.py".
8. **Self-Correction:** Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...) .
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel.
12. Visual Density: The page must be dense.
13. balanced page colors between teal and orange: minimum 1 element in orange (e.g. `TEMPLATE_C_BENEFIT_WARNING.html`).
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`).
15. Exam section always be in the end of the lesson without answers. Override: Strict Typographer Rule applied, no exam in raw text, so no exam block is fabricated.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 171
[CHAPTER_TITLE]: page 171
[CATEGORY_HEADER]: 171
[SECTION_HEADER]: 171
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: تتمة تحليل ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
Cut-Template: TEMPLATE_C_BLOCK.html
Title: البلاغة والأساليب
Content: <span class="text-accent font-bold">البلاغة:</span> ماض، داني (طباق إيجاب). <span class="text-accent font-bold">الأساليب:</span> (مَنْ أَنْتَ)، (ما أَنْتَ): تَقَدَّمَ الخَبَرُ على المُبْتَدَأِ؛ لأَنَّهُ مِنْ أسماء الصدارة (اسم استفهام).

=== BLOCK 3: إعراب ===
(Component: TEMPLATE_C_IRAB.html)
Word 1: مَنْ
Role 1: اسم استفهام، مَبْنِي على السكون في محل رفع، خَبَرٌ مُقَدَّمٌ.
Word 2: أَنْتَ
Role 2: ضميرُ رَفْعٍ مُنْفَصِلٌ مَبْنِيٌّ على الفَتْحَةِ فِي مَحَلِّ رَفْعٍ، مبتدأ.
Word 3: ما
Role 3: اسم استفهام، مبني على السُّكُونِ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ.
Word 4: أَنْتَ
Role 4: ضميرُ رَفْعٍ مُنْفَصِلٌ مَبْنِيٌّ على الفَتْحَةِ فِي مَحَلِّ رَفْعٍ، مُبْتَدَأٌ.
Word 5: قد
Role 5: حَرْفُ تحقيق.
Word 6: رُوْحَكَ
Role 6: مَفْعُولُ بِهِ مَنْصُوب، وعلامَةُ نَصْبِهِ الفَتْحَةُ الظَّاهِرَةُ والكاف، ضميرٌ مُتَّصِلٌ مَبْنِي على الفَتْحَةِ فِي مَحَلِّ جَرٍّ، مُضَاف إليه.
Word 7: فِي عَهْدَين
Role 7: في: حَرْفُ جر، عَهْدَين: اسم مَجْرُور، وعلامَةُ جَرِّهِ الياء لأَنَّهُ مُثَنَّى والنُّونُ عِوَضٌ عَنِ التنوين في الاسم المفرد.
Word 8: ماض
Role 8: صِفَةٌ مَجْرُورَةٌ، وعلامة جرها الكَسْرَةُ المُقَدَّرَةُ على الياءِ المَحْذُوفَةِ لَأَنَّهُ اسمٌ مَنْقُوص.
Word 9: جملة (مَنْ أَنْتَ)
Role 9: استئنافيَّةٌ، لا محل لها مِنَ الإعراب.
Word 10: جملة (ما أَنْتَ)
Role 10: استئنافية، لا محل لها مِنَ الإعراب.
Word 11: جملة (قد وَزَعْتَ)
Role 11: استئنافية، لا محل لها مِنَ الإعراب.

=== BLOCK 4: الشاهد الأول ===
(Component: TEMPLATE_C_POEM.html)
Title: أنا المهاجر
Poet:
Right Hemistich: أنا المُهَاجِرُ ذُو نَفْسَين، واحِدَةٌ
Left Hemistich: تسير سيري، وأخرى رَهْنُ أَوْطَانِي

=== BLOCK 5: الشرح والفكرة ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الشرح والفكرة
Content: <span class="text-accent font-bold">الشرح:</span> إِنَّني المهاجر الذي صارَ لَهُ روحان بَعْدَ مُغادرتِهِ أَرْضَ الوَطَنِ رُوْحٌ مُعَلَّقَةٌ بِجَسَدِهِ تُرَافِقُهُ فِي غُرْبَتِهِ، وتُشَارِكُهُ فِي مِحْنَتِهِ. ورُوْحٌ مَرْهُونَةٌ فِي الوَطَنِ، ساكنة فيه، نازعة إليه. <span class="text-accent font-bold">الفكرة:</span> التَّمَزُّقُ الرُّوحِيُّ بَيْنَ الغُرْبَةِ والوَطَنِ. <span class="text-accent font-bold">الأساليب:</span> ذو: اسم معرب بعلامة إعراب فَرْعِيَّة؛ لأنَّهُ مرفوع بالواو، أو لأنَّهُ مِنَ الأسماء الخمسة. نفسين: اسم معرب بعلامة إعرابٍ فَرْعِيَّة؛ لأنَّهُ مجرور بالياء، أو لأنَّهُ مثنى.

=== BLOCK 6: إعراب الشاهد الأول ===
(Component: TEMPLATE_C_IRAB.html)
Word 1: أنا
Role 1: ضميرُ رَفْعٍ مُنْفَصِلٌ مَبْنِي على السُّكُونِ فِي مَحَلِّ رَفْعٍ، مُبْتَدَأٌ.
Word 2: المُهَاجِرُ
Role 2: خَبَرٌ مَرْفُوعٌ.
Word 3: ذُو
Role 3: خَبَرٌ مَرْفُوع، وعلامةُ رَفْعِهِ الواو؛ لأَنَّهُ مِنَ الأَسْمَاءِ الخَمْسَةِ.
Word 4: نَفْسَين
Role 4: مُضَافُ إِلَيهِ مَجْرُور، وعلامةُ جَرِّهِ اليَاءُ لِأَنَّهُ مُثَنَّى والنُّونُ عِوَضٌ عَنِ التنوين في الاسم المُفْرَدِ.
Word 5: وَاحِدَةٌ
Role 5: مُبْتَدَأٌ مُؤَخَّرٌ خَبَرُهُ مُقَدَّمٌ مَحْذُوفٌ مَرْفُوع [التَّقْدِيرُ: مِنهُما واحِدَةٌ].
Word 6: سَيْرِي
Role 6: مَفْعُولُ مُطْلَقٌ مَنْصُوب، وعلامَةُ نَصْبِهِ الفَتْحَةُ الْمُقَدَّرَةُ على ما قبل ياءِ المُتَكَلِّمِ، مَنَعَ ظُهُورَهَا اشْتِغَالُ المَحَلِّ بِالحركة المناسبة. والياء، ضمير مُتَّصِلٌ مَبْنِي على السكون في محل جر، مُضَافُ إِلَيْهِ.
Word 7: وأُخْرَى
Role 7: الواو، حَرْفُ عَطْفٍ أُخْرَى، مُبْتَدَأٌ مُؤَخَّرٌ خَبَرُهُ مُقَدَّمٌ مَحذوف( مَرْفُوع، وعلامَةُ رَفْعِهِ الضَّمَّةُ الْمُقَدَّرَةُ على الأَلِفِ مَنَعَ ظُهُورَهَا التَّعَذُّرُ التَّقْدِيرُ: مِنهُمَا أُخْرَى.
Word 8: رَهْنُ
Role 8: صِفَةٌ مَرْفُوعَةٌ.
Word 9: أَوْطَانِي
Role 9: مُضَافُ إِلَيْهِ مَجْرُور، وعلامَةُ جَرِّهِ الكَسْرَةُ الظَّاهِرَةُ والياء، ضميرٌ مُتَّصِلٌ مَبْنِي على السُّكُون في محل جر، مُضَاف إليه.
Word 10: جملة (أنا المُهَاجِرُ ذُو نَفْسَين)
Role 10: استئنافيَّةٌ، لَا مَحَلَّ لها مِنَ الإعراب.
Word 11: جملة (منهما واحدة)
Role 11: استئنافية، لا محل لها مِنَ الإعراب.
Word 12: جملة (تسير)
Role 12: صِفَةٌ، مَحَلَّهَا الرَّفْعُ.
Word 13: جملة (منهما أُخْرَى)
Role 13: مَعْطُوفَةٌ، لا مَحَلَّ لها مِنَ الإعراب.

=== BLOCK 7: الشاهد الثاني ===
(Component: TEMPLATE_C_POEM.html)
Title: بَعُدْتُ عَنْهَا
Poet:
Right Hemistich: بَعُدْتُ عَنْهَا أَجُوبُ الأَرْضَ تَقْذِفُنِي
Left Hemistich: مُنَى، حَثَثْتُ لَهَا رَكْبِي وَأَطْعَانِي

=== BLOCK 8: الشرح والفكرة والبلاغة (تحذير) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: الشرح والفكرة
Content: <span class="text-accent font-bold">الشرح:</span> وقد ابتعدتُ عَنْ تِلْكَ الروح التي سَكَنَتِ الوَطَنَ، فَقَدْ رُحْتُ أَطوي الأَصْقَاعَ، وأَجُوبُ الفيافي والقِفَارَ لاهثاً، ساعيًا بِكُلِّ دَأْبٍ مِنْ أَجل تحقيق الطموحات والأحلام التي جَدَذْتُ السَّيْرَ نَحْوَهَا وَأَعْجَلْتُهُ. <span class="text-accent font-bold">الفكرة:</span> السَّعْي لِتَحْقِيقِ الأماني والأحلام. <span class="text-accent font-bold">البلاغة:</span> (تَقْذِفُنِي مُنَى) استعارة مكنية.

=== BLOCK 9: إعراب الشاهد الثاني ===
(Component: TEMPLATE_C_IRAB.html)
Word 1: الأَرْضَ
Role 1: مَفْعُولُ بِهِ مَنْصُوبٌ.
Word 2: تَقْذِفُنِي
Role 2: فِعْل مُضَارِعٌ مَرْفُوع والنُّونُ حَرْفُ وقاية. والياء، ضميرٌ مُتَّصِلٌ مَبْنِي على السُّكُونِ فِي مَحَلِّ نَصْبٍ، مَفْعُولُ بِهِ.
Word 3: مُنَى
Role 3: فَاعِلٌ مَرْفُوعٌ، وعلامَةُ رَفْعِهِ الضَّمَّةُ المُقَدَّرَةُ على الآلِفِ المَحْذُوفَةِ لَفْظًا، والمُثْبَتَةِ كِتَابَةً لِأَنَّهُ اسمٌ مَقْصُورٌ.
Word 4: رَكْبِي
Role 4: مَفْعُولُ بِهِ مَنْصُوب، وعلامَةُ نَصْبِهِ الفَتْحَةُ المُقَدَّرَةُ على ما قبل ياء المُتَكَلِّمِ، مَنَعَ ظُهُورَهَا اشْتِغَالُ المَحَلِّ بِالحَرَكَةِ المناسِبَةِ. والياء، ضميرٌ مُتَّصِلٌ مَبْنِي على السكون فِي مَحَلِّ جَرٍّ، مُضَاف إليه.
Word 5: وأَطْعَانِي
Role 5: الواو، حَرْفُ عَطْفٍ، أَطْعَانِي: اسمٌ مَعْطُوفٌ مَنْصُوب، وعلامَةُ نَصْبِهِ الفَتْحَةُ المُقَدَّرَةُ على ما قبل ياء المُتَكَلِّمِ، مَنَعَ ظُهُورَهَا اشْتِغَالُ الْمَحَلِّ بِالْحَرَكَةِ الْمَنَاسِبَةِ. والياء، ضمير مُتَّصِلٌ مَبْنِي على السُّكُونِ فِي مَحَلِّ جر، مضاف إليه.
Word 6: جملة (بَعُدْتُ عَنْهَا)
Role 6: صِفَةٌ، مَحَلُّها الرفع.
Word 7: جملة (أَجُوبُ)
Role 7: حالِيَّةٌ، مَحَلَّهَا النَّصْبُ.
Word 8: جملة (تَقْذِفُنِي مُنَى)
Role 8: حالِيَّةٌ، مَحَلُّهَا النَّصْبُ.
Word 9: جملة (حَثَثْتُ لَهَا رَكْبِي)
Role 9: صِفَةٌ، مَحَلُّهَا الرَّفْعُ.

=== BLOCK 10: الشاهد الثالث ===
(Component: TEMPLATE_C_POEM.html)
Title: ما إن أبالي
Poet:
Right Hemistich: ما إن أبالي مقامي في مغاربها
Left Hemistich: وفي مَشَارِقِها حُبِّي وإيماني

=== BLOCK 11: الشرح والفكرة ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الشرح والفكرة
Content: <span class="text-accent font-bold">الشرح:</span> إنني لا أكترثُ لإقامتي في أوطانِ الغَرْبِ مادام قَلْبِي مُتَعَلِّقًا بِمَحَبَّةِ وَطَنِي مَجْذُوبًا إليه، مُؤْمِنًا بِقِيَمِهِ الرُّوحِيَّةِ السَّامِيَةِ. <span class="text-accent font-bold">الفكرة:</span> إبْرَازُ الانْتِمَاءِ إلى قيم الوَطَنِ الرُّوحِيَّةِ (تأكيد عُمْقِ الانتماء إلى الوَطَنِ، تَفْضِيلُ الوَطَنِ على الغُربة). <span class="text-accent font-bold">البلاغة:</span> (مَغَارِبِهَا، مَشَارِقِها) طباق إيجاب.

=== BLOCK 12: المفردات (Core Matrix) ===
(Component: TEMPLATE_C_TABLE.html)
Header: الكلمة | المعنى
Row 1: المُهَاجِرُ | اسم فاعل فعله هَاجَرَ
Row 2: حَثَثْتُ | أَعْجَلْتُ
Row 3: رَكْبِي | الرَّاحِلَةُ يُرْتَحَلُ عليها
Row 4: مَغَارِبِهَا | اسم مكان فعله: غَرَبَ
Row 5: مَشَارِقِها | اسم مكان فعله شَرَقَ

=== BLOCK 13: إعراب الشاهد الثالث ===
(Component: TEMPLATE_CUT_BOX_PART_1.html)
Cut-Template: TEMPLATE_C_IRAB.html
Word 1: ما
Role 1: حَرْفُ نَفي.
Word 2: إِنْ
Role 2: حَرْفٌ زائِدٌ.
Word 3: أُبَالِي
Role 3: فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وعلامَةُ رَفْعِهِ الضَّمَّةُ الْمُقَدَّرَةُ على الياء، مَنَعَ ظُهُورَهَا الثِّقَلُ.
Word 4: مُقَامِي
Role 4: مَفْعُولُ بِهِ مَنْصُوب، وعلامَةُ نَصْبِهِ الفَتْحَةُ المُقَدَّرَةُ على ما قبل ياء المتكلم، مَنَعَ ظُهُورَهَا اشْتِغَالُ الْمَحَلِّ بِالْحَرَكَةِ المُنَاسِبَةِ. والياء، ضميرٌ مُتَّصِلٌ مَبْنِي على السُّكُونِ فِي مَحَلِّ جَرٍّ، مُضَاف إليه.
Word 5: وفي مَشَارِقِها
Role 5: الواو، واو الحال. في: حَرْفُ جر. مشارقها: اسم مجرُور، وعلامَةُ جَرِّهِ الكَسْرَةُ الظَّاهِرَةُ. وها، ضميرٌ مُتَّصِلٌ مَبْنِي على السُّكُون فِي مَحَلِّ جرٍّ، مُضَاف إليه. والجار والمَجْرُورُ مُتَعَلِّقان بِخَبَرٍ مُقَدَّم مَحذُوفٍ.
Word 6: حُبِّي
Role 6: مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوع، وعلامَةُ رَفْعِهِ الضَّمَّةُ المُقَدَّرة على ما قبل ياء المتكلم، مَنَعَ ظُهُورَهَا اشْتِغَالُ المحل بالحركة المناسبة. والياء، ضميرٌ مُتَّصِلٌ مَبْنِي على السكون في محل جر، مُضَاف إليه.
Word 7: وإيماني
Role 7: الواو، حَرْفُ عَطْفٍ، إيمَانِي: اسم مَعْطُوفٌ...

--- END STREAM ---
