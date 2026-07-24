# **SESSION 119**

[TASK DEFINITION]
Objective: Implement page 119.
File: `pages/page_119.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools. If it overflows, it is a catastrophic failure. Do NOT try to solve overflow by deleting text (Strict Typographer Rule). Solve it by choosing denser templates or omitting optional white-space.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`. Ensure exact visual continuity (same title, same classes).
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md` to identify the correct template to use for the continuation. You are forbidden from guessing.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice. (Note: The "Typo Exception" was strictly applied to unscramble the severely OCR-corrupted list in "مؤشرات النمط الوصفي" to maintain grammatical accuracy and meaning).
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green` for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   **Rule:** NO INLINE STYLES.
*   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
7. Templates: You are forbidden from inventing new HTML tags or classes or template elements. You must map all content using "Jules-workspace/Templates/" components.
8. **CRITICAL 1-PAGE MODE RULE**: You MUST NOT use `<section>` tags when applying templates. Replace any `<section>` tags from the templates with `<div>` tags (keep `<header>` for page headers as is).
9. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). The ID MUST be applied to the `<div>` tag that replaced the `<section>` tag. Use "Jules-workspace/id_manager.py" to generate or verify them.
10. Do not summarize examples. Do not provide uncompleted text content using (...) unless it was literally in the raw text.
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense. Do NOT leave empty space.
13. Balanced page colors between teal and orange: make sure every page has minimum 1 element in orange instead of all teal (e.g., using `.block-header accent`).
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
15. Exam section always be in the end of the lesson (in the final page of that lesson), and without the answers! The answers to textual analysis questions are placed in regular blocks.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 119
[CHAPTER_TITLE]: page 119
[CATEGORY_HEADER]: 119
[SECTION_HEADER]: 119
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: مؤشرات النمط الوصفي (Cut Box Continuation) ===
(Component: TEMPLATE_CUT_BOX_PART_2.html wrapping TEMPLATE_C_BLOCK.html)
Title: مُؤَشِّرَاتُ النَّمَطِ الوَصْفِي
Content:
Use `TEMPLATE_C_LIST.html` with the following list (unscrambled via Typo Exception):
- ١- الإكثار مِنَ الصفات أو الجمل الاسمية التي تمكن من إطلاق الصفات والنعوت.
- ٢- استعمال الأفعال الدالة على حالة الموصوف، والمضارع للدلالة على الحركة والحيوية والاستمرار.
- ٣- اعتماد الفعل الماضي، وبدخول (كان) على هذه الجمل، ينتقل الوَصْفُ مِنَ الحاضر إلى الماضي.
- ٤- استعمال الفعل الماضي لوَصْفِ حادث مَضَى.
- ٥- الإكثار مِنَ الأساليب الانفعالية، كالتعجب والتمني والاستفهام.
- ٦- تحديد واضح لزمان والمكان واستخدام روابطهما.
- ٧- كثرة الصُّور الفنيَّةِ المُوَثِّرَةِ فِي النَّفْسِ، والخيالية الموحية.
- ٨- استعمال المصادر، والأفعال الدالة على الانفعال.
- ٩- تكوين حَقْلِ مُعْجَمي خاص بالموصوف.
- ١٠- اندماج ذات الكاتب بالموصوف، والنَّظَرُ إليه من خلال حالتِهِ النَّفُسِية.

=== BLOCK 3: مؤشرات النمط السردي ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مُؤَشِّرَاتُ النَّمَطِ السَّرْدِي
Content:
Use `TEMPLATE_C_LIST.html` with:
- اعتماد الحوار الذي يضفي على السرد الواقعية والحركة والحياة، ويساعد في الكشف عن الطبائع: قال الشيخ منتعشا: (وكم ... يدان).
- استعمال الأفعال الماضية: (تحسس، تلا، صاح، أزاحت، أصابت، طار، .....)

=== BLOCK 4: مناقشة وتحليل - أسلوب الحوار والرمز ===
(Component: TEMPLATE_C_BLOCK.html) (Use `.block-header accent` for Orange color balance)
Title: مُنَاقَشَةٌ وَتَحْلِيلٌ
Content:
Use `TEMPLATE_C_LIST.html` to present the Q&A:
- <span class="text-accent font-bold">السؤال:</span> لجأ الشَّاعِرُ إلى أسلوب الحوار في النص لِلْكَشْفِ عَنْ أَعْمَاقِ الشَّحْصِيَّات وتوجهاتها. وَضَحْ ذَلِكَ مِنَ النَّصِّ.
  <br><span class="highlight-blue">الجواب:</span> تمكن الشاعر من خلال إجراء الحوار بين الشيخ وابنته من الكشف عن طبيعة كل منهما؛ فعندما أنطق الفتاة بالقول: (ولكن المنازل يا أبي أطلال)، كشف عن نفسيتها المتشائمة، وأظهر اليأس الذي تسرب إلى نفسها. وعندما أنطق الشيخ بالقول: (تبنيها يدان) كشف عن نفسيته المتفائلة، وأظهر أن الأمل لم يزل يسري في كيانه.
- <span class="text-accent font-bold">السؤال:</span> اتكأ الشاعر على الرمز فِي نَصِّهِ، فَمَا الذي رَمَزَ إِليهِ كُلِّ مِن: (الجسر، النهر، الطريق)؟
  <br><span class="highlight-blue">الجواب:</span> ج - الجسر: طريق العودة. - النهر: حاجز حدودي يحول دون تحقق حلم العودة. - الطريق: العودة.

=== BLOCK 5: الصور الفنية (The Core Matrix) ===
(Component: TEMPLATE_C_TABLE.html inside TEMPLATE_C_BLOCK.html)
Title: تَحْلِيلُ الصُّوَرِ الفَنِّيَّةِ
Intro Text: حلل الصورتين الآتيتين : (هِجْرَةُ الدَّم، القتل كالتدخين)، ثُمَّ اذْكُرُ وظيفةً مِنْ وَظَائِفِ كُلِّ مِنْهُما.
Table Data:
| الصُّورَةُ | تَسْمِيَتُهَا | التَّحْلِيلُ | الوَظِيفَةُ |
|---|---|---|---|
| ج - الصورة (هِجْرَةُ الدَّم). | تَسْمِيَةُ الصورة: استعارة مكنية. | تحليل الصورة: شبه الدم بكائن مهاجر، وحذف المشبه به وأبقى شيئًا من لوازمه وهو: "هجرة". | <span class="highlight-green">تسمية الوظيفة: الإيحاء.</span> شرح الوظيفة أو توضيح الوظيفة: جَعَلَ الشَّاعِرُ الصورة موحِيَةً بتشبيهه الدم بكائن مهاجر، فهذا أوحى بالموت والقتل والخطر، وأثار مشاعر الخوف والحزن. |
| الصورة: (القتل كالتدخين). | تَسْمِيةُ الصورة: تشبيه مجمل. | تحليل الصورة: المشبه القتل المشبه به : التدخين. أداة التشبيه: الكاف. وجه الشبه : محذوف. | <span class="highlight-green">تَسْمِيةُ الوَظِيفة: الشرح والتوضيح.</span> شرح الوظيفة أو توضيح الوظيفة: شرحَتِ الصُّورَةُ وَوَضَحَتْ معنى: "إدمان الصهاينة على القتل والاستمتاع به" من خلال تشبيه القتل بالتدخين، فأقنعت المتلقي بمضمون المعنى وصدقه. |

=== BLOCK 6: توافق المعاني والصور ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَوَافُقُ المَعَانِي مَعَ الصُّوَرِ
Content:
Intro: ه - اسْتَخْرِجُ مِنَ المَقْطَعَين الثَّالِثِ والرَّابِعِ صُورًا تُوَضَحُ الْمَعَانِي الْآتية: (تَعَاظُمُ حُلُمِ الْعَوْدَةِ - عَدَمُ شَرْعِيَّةِ الوُجُودِ الصَّهْيَوِنِي فِي فَلِسْطِينَ - كَثْرَةُ القَتْلَى الفِلِسْطِينِيِّينَ الْحَالِمِينَ بِالعَوْدَةِ).
Use `TEMPLATE_C_LIST.html`:
- جه- عَدَمُ شَرْعِيَّةِ الوُجُودِ الصَّهْيَوَنِي فِي فِلِسْطِينَ : (لكن الجنود الطيبين الطالعين على فهارس دفتر قذفته أمعاء السنين).
- كَثْرَةُ القَتْلَى الْفِلِسْطِييِّينَ الحَالِمِينَ بِالعَوْدَةِ : (النهر يبصق ضفتيه قطعا من اللحم المفتت).
- تَعَاظُمُ حُلُمِ العَوْدَة:ِ (لسعة الذكرى)، (طعم الحب حين يصير أكبر من عباده).

=== BLOCK 7: العاطفة والموسيقا الداخلية ===
(Component: TEMPLATE_C_SPLIT.html containing two elements)
Right Column (TEMPLATE_C_BENEFIT.html):
Title: تتبع العاطفة في النص
Intro: تَتَبَّعْ عَاطِفَةً كُلِّ مِنَ الشَّيْخِ وَابْنَتِهِ مِنْ خِلال الحوار الذي دارَ بَيْنَهُما، مُؤيِّدًا مَا تَذْهَبُ إِلَيهِ بِالشَّوَاهِدِ الْمُنَاسِبَة.ِ
Content: Use `TEMPLATE_C_LIST.html`
- ج ٦- كلام الشيخ : أظهر أنه يشعر بالتفاؤل والأمل - الشاهد قوله: (تبنيها يدان).
- كلام ابنة الشيخ : أظهر أنها تشعر باليأس والقنوط والتشاؤم. - الشاهد قولها: (ولكن المنازل يا أبي أطلال).

Left Column (TEMPLATE_C_BENEFIT_TIP.html):
Title: مصادر الموسيقا الداخلية
Intro: مِنْ مَصَادِرِ الموسيقا الداخلية (تكرار الكلمات، تكرار الحروف). مَثِّلْ لِذَلِكَ مِنَ النَّص،ِ ثُمَّ اذْكُرُ مَصَادِرَ أُخْرَى أَعْنَتِ الإِيقَاعَ الْمُوسِيقِي.َّ
Content: Use `TEMPLATE_C_LIST.html`
- <span class="text-accent">تكرار الكلمات:</span> ج- - تكرار الكلمات في المقطع الأول : (الطريق، الطريق)، (العائدين، عائدين)، (الجسر، الجسر)، (الحدود، الحدود). في المقطع الثاني: (الجسر، الجسر)، (الطلقة، الطلقة).
- <span class="text-accent">تكرار الحروف:</span> تكرار حرفي الحاء والدال في السطرين: (حرس الحدود مرابط / يحمي الحدود من الحنين).
- <span class="text-accent">تكرار الصيغ الاشتقَاقِيَّةِ:</span> ومن مصادر الموسيقا التي أغنت الإيقاع الموسيقي: - تكرار الصيع الاشتقَاقِيَّةِ : المقطع الثاني: (تقتلوها، اقتلوني)، (يعلم، الحلم)، المقطع الثالث: (القتل، يقتلوا)..

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: المستوى الإبداعي:

--- END STREAM ---
