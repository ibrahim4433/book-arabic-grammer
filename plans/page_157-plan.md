# **SESSION 157**

[TASK DEFINITION]
Objective: Implement page 157.
File: `pages/page_157.html` (Note: Use the exact page number.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice. (Applied "Typo Exception" to correct obvious OCR errors and removed stray page number).
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   **Rule:** NO INLINE STYLES.
*   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
*   **Mapping:**
    *   `style="width: 20%"` -> `class="w-20pct"`
    *   `style="margin-top: 2mm"` -> `class="mt-2mm"`
    *   `style="text-align: center"` -> `class="text-center"`
    *   `style="font-weight: bold"` -> `class="font-bold"`
6. Templates: Replace `<section>` tags with `<div>` tags (keep `<header>`). Apply `bXXXXX` IDs directly to the replacement `<div>`.
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). Use "Jules-workspace/id_manager.py".
8. Self-Correction: Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...) .
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal (Ignored if no content fits the rule, per strict typographer rule)
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html`
15. The Strict Typographer Rule overrides the mandatory Exam section rule. If the raw text does not contain exam questions (e.g., it only contains a page footer string or answered exercises), do not fabricate or append an Exam block.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 157
[CHAPTER_TITLE]: page 157
[CATEGORY_HEADER]: 157
[SECTION_HEADER]: 157
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Poem Segment ===
(Component: TEMPLATE_C_POEM.html)
Title: - قَالَ الشَّاعِرُ المهجَرِي إلياس فرحات:
Bio:
Lines:
- نَائِحٌ أَقْعَدَهُ وَجْدٌ مُقِيم في الحشا | بَيْنَ خُمُودِ وَاتِّقَادِ
- كُلَّمَا افْتَرَّ لَهُ البَدْرُ الوسيم | عَضَّهُ الحزن بِأَنياب حِدَادِ
- يَذْكُرُ الرَّبْعَ القَدِيمَ فَيُنَادِي | أَيْنَ جَنَّاتُ النَّعِيم مِن بلادي؟!

=== BLOCK 3: The Core Matrix (Content Analysis) ===
(Component: TEMPLATE_C_TABLE.html)
Title: وازن بين هذا المقطع والمقطعِ الأَوَّلِ مِنَ النَّصِ مِنْ حَيْثُ الْمَضْمُون،ِ ثُمَّ اذْكُرُ مُعَلِّلًا إِلَى أَيْهِمَا تَمِيل؟
Headers: | ج - التَّشَابُهُ : | الاختلافُ : |
Row 1: | - كلا الشَّاعِرَين يُظْهِرُ الْمَعَانَاةَ بِسَبَبِ الْبُعْدِ عَنِ الوَطَنِ | - صَيْدَحٌ أَبْرَزَ حَسْرَتَهُ ومعاناتَهُ وَحَنِيْنَهُ وَإِعجابَهُ مُسْتَعْمِلَا ضَمِيرَ المتكلم، بينما فرحات أَبْرَزَ الْحَسْرَةَ وَالْمُعَانَاةَ والحنين والإعجاب مُسْتَعْمِلًا ضَمِيرَ الغَائِب.ِ |
Row 2: | - أو : كلا الشَّاعِرَين يُظْهِرُ الشَّوْقَ وَالْحَنِينَ إِلَى الوَطَن.ِ | - صيدح أشَارَ إِلَى سَبَبِ مُغَادَرَتِهِ الوَطَن،َ بينما فرحاتِ لَمْ يُشِرُ إِلَى ذَلِك.َ |
Row 3: | - أو : كلا الشاعرين يُظْهِرُ الإِعْجَابَ بِجَمَالِ الوَطَنِ | صيدَحٌ أَشار إلى انْقِطاع الرزق فِي الوَطَنِ رغم وَفْرَةِ الخَيْرَات،ِ بينما اكتفى فرحات بالإشارة إلى وَفْرَةِ الخَيْرَات.ِ |
Row 4: | - أو : كلا الشَّاعِرَين يُظْهِرُ وَفْرَةَ الخَيْرَاتِ فِي الوَطَن.ِ | |
Row 5: | - أو : كلا الشَّاعِرَين يُظْهِرُ التَّحَسُّرَ على تَرْكِ الوَطَنِ عُنْوَةً (قَسْرًا) . | |

=== BLOCK 4: Artistic Level Table 1 (Verbal Sentences) ===
(Component: TEMPLATE_C_TABLE.html)
Title: المستوى الفني: - تَوْزَعُ الْجُمَلُ الخَبَرِيَّةُ بَيْنَ فِعْلِيَّةٍ وَالاسْمِيَّةِ فِي البَيْتَين الثَّالِثِ والرَّابِعِ صَنِّفْهَا فِي جَدْوَلِ وَفْقَ الآتي:
Headers: | الجمل الفِعْلِيَّةُ | الوظيفة الدلالية |
Row 1: | غاب خلف البحر عنى شاطئ | تحقق غياب الشاعر عن الوطن. |
Row 2: | أرقني - رَقَد | تحقق معاناة الشاعر في غربته. |
Row 3: | جَرَتْ تحتها الأنهار | تحقق وفرة الْخَيْرَاتِ فِي الوَطَن.ِ |

=== BLOCK 5: Artistic Level Table 2 (Nominal Sentences) ===
(Component: TEMPLATE_C_TABLE.html)
Title:
Headers: | الجمل الاسمية | الوظيفة الدلالية |
Row 1: | كل ما أَرَّقَنِي فِيهِ رَقَد | استمرار مُعاناة الشاعر، وثباتها وديمومتها. |
Row 2: | فِيهِ رَبِّعِي - فِيهِ جَنَّاتُ | إعطاء صورة ثابتة دائمة لِلوَطَنِ كَمَا يَرَاهُ الشَّاعِرُ . |
Row 3: | الرزق جَمَد | الدلالة على ثَبَاتِ حَالة ضِيْقِ العَيْشِ ودَيْمُومَةِ انقطاع الرِّزْق.ِ |

=== BLOCK 6: Q&A List (Styles, Pronouns, Personification) ===
(Component: TEMPLATE_C_LIST.html)
List Items:
- - استخرج مِنَ المَقَاطِعِ السَّابِقَةِ ثلاثَةَ أَسَالِيْبَ إِنْشَائِيَّةٍ مُتَنَوَعَة،ٍ ثُمَّ بَيِّنْ خِدْمَتَهَا لِلتعبيرِ عَنِ المناخ الانفعالي الأَكْثَرِ حُضُورًا فِي النَّصِ كُلِّه.ِ
- ج - وَطَنِي : أُسلوبُ إِنْشَاء طَلَبِيّ بِصِيغَةِ النداء. - أين أنا مِنْ أَوَدّ؟ أو ما لِلحَظ بعد الجزر مد؟ هل دَرَى الدهر الذي فَرَّقَنَا أَنَّهُ فَرَّقَ روحًا من جَسَد؟ حَتَّامَ تَرْتَدُ الصَّبا دُوْنَ أَنْ تَحْمِلَ مِنْ سَلْمَايَ رَد؟ : أُسلوبُ إِنْشَاء طَلَبِي بصيغة الاستفهام.
- - فَقَسَمًا لولا أنيني ما اهتدى لسريري طيفها لَمَّا وَفَد : أُسلوبُ إِنْشَاء غَيْرَ طَلَبِي.
- - استعمال هذه الأساليب الإنشانِيَّةِ أَظْهَرَ الانفعالات التي تَتَزَاحَمُ فِي صَدْرِ الشَّاعِر،ِ فَأَظْهَرَتْهُ مَأْزومًا نَفْسِيًّا يَشْعُرُ بالاضطراب والقلق.
- - ما الضَّمِيرُ الذي أَكْثَرَ الشَّاعِرُ مِنِ اسْتِعْماله في النص؟ وما علاقَةُ ذَلِكَ بِالنَّصَ؟
- ضمير المُتَكَلِّمِ ذَلِكَ أَنَّ الشَّاعِرَ يَتَحَدَّثُ عَنْ تَجْرِبِةٍ ذَاتِيَّة،ٍ ومُعاناةٍ شَخْصِيَّةِ بِسَبَبِ بُعْدِهِ عَنْ وَطَنِه.ِ
- - استخرج مِنَ البيتِ السَّادِسِ تَشْخِيْصًا، وبين وظيفَتَهُ فِي تَجْلِيَةِ الْمَشَاعِرِ وَتَدَفُّقِهَا.
- ج - التَّشْخِيصُ : (وَطَنِي مَا زِلْتُ أَدعوك أبي)، شخص الشَّاعِرُ الوَطَنَ وَجَعَلَهُ أَبًا يَنْتَسِبُ إِلَيْه،ِ لِيُجَلِّيَ مَشَاعِرَ المَحَبَّةِ وَالشَّوق والحنين والاعتزاز.

=== BLOCK 7: Table (Contrast / Tibaq Answers) ===
(Component: TEMPLATE_C_TABLE.html)
Title: ه - أَكْثَرَ الشَّاعِرُ مِنِ اسْتِعْمَالِ الطَّبَاقِ . اسْتَخْرِجُ مِنَ النَّص مثالين على ذَلِك،َ واذكر وظيفته في خدمة المَعْنَى وَفْقَ الْجَدُولِ الْآتي:
Headers: | الطباق | وظيفته |
Row 1: | جَرَت،ْ جَمَد | يُوَضِّحُ الطِّبَاقُ مُعَانَاةَ الشَّاعِرِ مِنْ خلال إبراز التناقضِ الْحَادِ بَيْنَ وَفْرَةِ الْخَيْرَاتِ وَانْقِطَاعِ الرَّزْق.ِ |
Row 2: | مر، يحلو | هذا الطباق يوضح عُذُوبة العيش في أَحْضَانِ الوَطَنِ مهما كانَ ضَنْكًا ضَيِّقًا، ومرارته في الغربة مهما كانَ رَغِيدًا. وهذا يُثير خيال المُتَلَقِي ويُحَفِّزُهُ لِلْمُقارنة بين هاتين الحالتين المتناقضتين، كما يُمَكِّنُ مِنْ إعمال العقل بين مرارة العيش وحلاوته لِيُدْرِكَ الفَرْقَ الشَّاسِعَ بِينَهُما. فَضْلًا عَنْ إِبراز مَوْقِفِ الشَّاعِرِ الرَّافِضِ لِلْغُرْبَةِ الطَّامِحِ لِلعَوْدَةِ إِلَى رُبُوعِ الوَطَن.ِ |
Row 3: | الجزر، مد | يثير خيال المتلقي ويمنحهُ الفرصة لتخيل الحالة المزرِيَةِ التي كان يحياها الشاعر وهو يُبْحِرُ مُرْغَمًا مِنْ شُطْآنِ وطنه، وحالة تَرَقُبِ العَوْدَةِ وَتَمَنِّي الرجوع، فيمكنهُ مِنْ إِدراك الفَرْقِ الشَّاسِعِ بين الحالتين المتناقضتين. |

--- END STREAM ---
