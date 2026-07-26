# **SESSION 156**

[TASK DEFINITION]
Objective: Implement page 156.
File: `pages/page_156.html` (Note: Use the exact page number.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools. If it overflows, it is a catastrophic failure. Do NOT try to solve overflow by deleting text (Strict Typographer Rule). Solve it by choosing denser templates or omitting optional white-space.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`. Ensure exact visual continuity (same title, same classes).
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md` to identify the correct template to use for the continuation. You are forbidden from guessing. Scan the raw text for the preceding keyword to determine the active template and apply the correct `_PART_2.html` wrapping.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green`  for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   **Rule:** NO INLINE STYLES.
*   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
*   **Mapping:**
    *   `class="w-20pct"`
    *   `class="mt-2mm"`
    *   `class="text-center"`
    *   `class="font-bold"`
6. Templates: You are forbidden from inventing new HTML tags or classes or template elements. You must map all content using "Jules-workspace/Templates/" components as the STREAM says in suitable way. **CRITICAL 1-PAGE MODE RULE**: You MUST NOT use `<section>` tags when applying templates. Replace any `<section>` tags from the templates with `<div>` tags (keep `<header>` for page headers as is).
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). The ID MUST be applied to the `<div>` tag that replaced the `<section>` tag. Use "Jules-workspace/id_manager.py" to generate or verify them.
8. **Self-Correction:** Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files. If it fails, you MUST fix the errors (usually inline styles or forbidden section tags) before submitting.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...) .
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
15. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 156
[CHAPTER_TITLE]: page 156
[CATEGORY_HEADER]: 156
[SECTION_HEADER]: 156
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: أسئلة النص ===
(Component: TEMPLATE_C_LIST.html)
Title: أسئلة النص
Content:
<ul>
  <li>- ما مَوْقِفُ الشَّاعِرِ مِنْ غُرْبَتِهِ كَمَا بَدَا لَكَ فِي النَّصّ؟<br><span class="text-accent">ج -۱ بدا الشاعر في النَّصّ رافضا الغُربَة،َ مُرغمًا على العَيْشِ فيها.</span></li>
  <li>- ما أَبْرَزُ مَا أَرَّقَ الشَّاعِرَ الْمُهَاجِرَ؟ مِمَّا زَادَ شَوْقَهُ وَحَنِينَهُ إِليهم.<br><span class="text-accent">ج - أَرَّقَ الشَّاعِرَ بُعْدُهُ عَنِ الوَطَن،ِ فهذا البَعْدُ أَفْقَدَهُ المَنْزِل،َ وحلاوة العيش والأَحِبَّةَ وَالتَّوَاصُلَ مَعَهُم.</span></li>
</ul>

=== BLOCK 3: مهارات القراءة ===
(Component: TEMPLATE_C_LIST.html)
Title: مهارات القراءة
Content:
<ul>
  <li>- ما الدَّوافِعُ وَرَاءَ هِجْرَةِ الشَّاعِرِ عَنْ وَطَنِهِ؟<br><span class="text-accent">ج - ضِيقُ العَيْش،ِ وانقطاع الرِّزْقِ فِي وَطَنِ الشَّاعِرِ دَفَعَاهُ دَفْعًا إلى الغُرْبَة، طامحا إلى تحقيق أمانِيهِ فِي بُلُوغِ الغنى.</span></li>
  <li>- اذكُرُ مِنَ النَّصَ مَظْهَرَيْنِ مِنْ مَظَاهِرِ مُعَانَاةِ الشَّاعِرِ فِي غُرْبَتِه.ِ<br><span class="text-accent">١- مَظَهَرُ الْمُعَانَاةِ الْأَوَّل:ِ إضاعَةُ العُمُرِ جَرْيًا وراء الغنى - المُؤشِرُ : (تقاضاني الغنى عُمْرًا نَفَد).<br>٢- مَظَهَرُ المُعَاناة الثاني: فِقْدَانُ التَّواصل مَعَ الْمَحْبُوبَةِ - المُؤْشِرُ : (ترتدُّ الصَّبا دُوْنَ أَنْ تَحْمِلَ مِنْ سَلَمَايَ رَدْ).</span></li>
</ul>

=== BLOCK 4: الاستيعاب والفهم والتحليل: المستوى الفكري ===
(Component: TEMPLATE_C_LIST.html)
Title: الاستيعاب والفهم والتحليل: المستوى الفكري
Content:
<ul>
  <li>- وضح المَعَانِي الْمُخْتَلِفَةَ لِكَلِمَةِ (رَبِّع) مُسْتَعِينَا بِالمُعْجَم،ِ ثُمَّ اخْتَرْ مِنْهَا مَا يُنَاسِبُ النَّص.َّ<br><span class="text-accent">ج - الرَّبَّعُ : المَوْضِعُ يُنْزَلُ فِيهِ زَمَنَ الرَّبِيع، وهو الدار والمنزل.</span></li>
  <li>- كَوّنْ مُعْجَمًا لُغَوِيَّا لِكُلِّ مِنَ (الوَطَنِ، الغُرْبة)، مِنَ النَّص السَّابِق.ِ<br><span class="text-accent">- المُعْجَمُ اللُّغَوِيُّ لِلوَطْنِ : (وَطَنِي، شاطىء، رَبَّعِي، جنات الأنهار، الصبا).<br>- المُعْجَمُ اللُّغَوِيُّ لِلغَرْبَةِ : (النوى، البين، العنا، ...).</span></li>
  <li>- حَدَدِ الفِكْرَةَ العامة التي بني عليها النَّص،ُّ مُسْتَفِيدًا مِنَ الْمُعْجَمَين اللُّغَوِيينِ السَّابِقين.<br><span class="text-accent">ج- الشَّوْقُ والحنين إلى الوَطَن،ِ وَالمَعَانَاةُ فِي الغُرْبَة.ِ</span></li>
</ul>

=== BLOCK 5: ملامح مأساة الشاعر ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: ملامح مأساة الشاعر
Content:
- مِنْ مَلامِح مَأْسَاةِ الشَّاعِر،ِ تَرْكُ الوَطَنِ وَالأَهْلِ قَسْرًا، وَضَحْ ذَلِكَ مِنْ فَهْمِكَ الْمَقْطَعَ الْأَوَّل.َ
<span class="text-accent">ج - غادَرَ الشَّاعِرُ شَاطِيَ الوَطَنِ مُضطرا مُرْغَمًا، يدفعُهُ إِلى ذَلِكَ ضِيقُ العَيْشِ وَامْتِنَاعُ الرِّزْق،ِ فلو أُتِيْحَ لَهُ إِيقَافُ سَفِينَةِ الهِجْرَةِ لَمَا تَرَدَّدَ لَحْظَة،َ فَمُعَادَرَةُ الوَطَنِ أَفْقَدَتْهُ مَنْزِلَه،ُ وَأَهْلَهُ وَصَحْبَه،ُ وَحَرَمَتْهُ التمَتَّعَ بِمَظَاهِرِ جَمَالِ الوَطَن،ِ والتلَذُّذَ بحلاوة العَيْشِ وعُذُوبتِهِ فِيه.ِ</span>

=== BLOCK 6: الانتماء والمعاناة ===
(Component: TEMPLATE_C_LIST.html)
Title: الانتماء والمعاناة
Content:
<ul>
  <li>ه- يَبْرُزُ الانْتِمَاءُ إِلَى الوَطَنِ عَمِيقًا قَويا في المقطع الثاني هات مِنْهُ مَظْهَرَيْنَ لِذَلِك.َ<br><span class="text-accent">ج - المَظْهَرُ الأَوَّل:ُ انتساب الشَّاعِرِ إلى الوَطَنِ ومُنَادَاتِهِ بِالأَب.ِ - المُؤْشِرُ : (وَطَنِي مازِلْتُ أَدْعُوكَ أَبِي ...).<br>المَظْهَرُ الثَّانِي: جَعْلُ علاقتِهِ بِالوَطَنِ كَعلاقَةِ الروح بِالجَسَد.ِ - المُؤْشِرُ : (البيتُ التَّاسِعُ).</span></li>
  <li>- بَدَأَ الشَّاعِرُ مَقَاطِعَهُ الثلاثة بـ (وطني). ما دِلالَهُ ذَلِكَ فِي رَأَيْكَ؟<br><span class="text-accent">ج - يدلُ ذَلِكَ على محبة الشاعر لِوَطَنِهِ وَشَوْقِهِ إِلَيهِ وَتَعَلَّقِهِ بِه.ِ</span></li>
</ul>

=== BLOCK 7: ذروة المعاناة ===
(Component: TEMPLATE_C_BENEFIT.html)
Title: ذروة المعاناة
Content:
- بَلَغَتْ مُعَانَاةُ الشَّاعِرِ ذُرْوَتَهَا فِي المَقْطَعِ الأَخِيْر.ِ وَضَحْ ذَلِك.َ
<span class="text-accent">ج - تزداد معاناة الشاعر في غُرَبَتِهِ حِينَمَا يَحِنُ إِلَى لِقَاءِ المَحْبُوبَة، ويتوق إلى وصالها بَعْدَ طُوْلِ غِياب،ٍ فَتَحْتَدِمُ فِي نَفْسِهِ الْمُعَذِّبَةِ أَشْجَى الْمَشَاعِر،ِ وَتَرَفُ فِي قلبِهِ الْمُمَزَّقِ مَنَازِعُ الشَّوقِ وَآلَامُ الفُرْقَة.ِ وتلتهب الأشواق وتستعرُ حينما يُحَملُ رياح الصَّبَا رَسَائِلَ الشَّوقِ لِلْمَحْبُوبَة،ِ فتأتيه خالية الوفاضِ مِنْ دُوْنِ أَنْ تَحْمِلَ إِلَيهِ رَدًّا مِنْ مَحْبُوبَتِهِ يُفْعِمْ نَفْسَهُ بِالنَّشْوَةِ وَالحُبُور. وحينما يخذله الواقع يلجأ إلى الحلم والخيالِ عَلَّ ذَلِكَ يُحَقِّقُ لَهُ مَا عَجِزَ عن تحقيقه الواقع فيأتيه طيف المحبوبة زائرا، يَسْتَدِلُ عليهِ مُسْتِعِينَا بِسَمَاعٍ أَنَّاتِهِ وَزَفَرَاتِه،ِ وَمَا إِنْ يَقْتَرِبُ مِنهُ لِيُمَتَعَ نَفْسَهُ بِنَشْوَةٍ عَامِرَةٍ يَتَلاشى هذا الطَّيْفُ تاركا الشَّاعِرَ يزداد شَوْقًا إِلَى الْمَحْبُوبَة،ِ مِمَّا يُضَاعِفُ آلامَهُ وَمُعاناته.</span>

=== BLOCK 8: القيم الواردة في النص ===
(Component: TEMPLATE_C_TABLE.html)
Title: القيم الواردة في النص
Content:
- استَخْرِج عَدَدًا مِنَ القِيَمِ الوَارِدَةِ فِي النَّص،َ وَصَنِّفْهَا وَفْقَ الجدول :
| قِيَمٌ وَطَنِيَّةٌ | قيم وجدانية |
|---|---|
| حُبُّ الوَطَنِ والتَعَلَّقُ به والانتماء إليه. | - المعاناةُ بِسَبَبِ انْقِطَاعِ الوَصْلِ مَعَ المحبوبة. |
| استعذاب مرارَةِ العَيْشِ فِي الوَطَن.ِ | - اللَّهُفَةُ إلى لقاء المحبوبة. |

--- END STREAM ---
