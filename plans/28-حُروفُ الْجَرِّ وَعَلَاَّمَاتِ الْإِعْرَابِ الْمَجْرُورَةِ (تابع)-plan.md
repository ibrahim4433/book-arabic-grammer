# **SESSION 28.0**

[TASK DEFINITION]
Objective: Implement حُروفُ الْجَرِّ وَعَلَاَّمَاتِ الْإِعْرَابِ الْمَجْرُورَةِ (تابع).
File: `pages/28.0_nXX_حُروفُ الْجَرِّ وَعَلَاَّمَاتِ الْإِعْرَابِ الْمَجْرُورَةِ (تابع).html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/28.1_...` if page have a lot of blank space add exam elements from the lesson.
3. text Content: 100% Arabic with full Harakat.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green`  for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   **Rule:** NO INLINE STYLES.
*   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
*   **Mapping:**
    *   inline style width: 20% -> `class="w-20pct"`
    *   inline style margin-top: 2mm -> `class="mt-2mm"`
    *   inline style text-align: center -> `class="text-center"`
    *   inline style font-weight: bold -> `class="font-bold"`
6. Templates: You are forbidden from inventing new HTML tags or classes or template elements. You must map all content using "Jules-workspace/Templates/" components as the STREAM says in suitable way.
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). use "Jules-workspace/id_manager.py" to generate or verify them.
8. **Self-Correction:** Run "Jules-workspace/lint_pages.py" after creating html files. If it fails, you MUST fix the errors (usually inline styles) before submitting.
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
[LESSON_NUMBER]: 28
[CHAPTER_TITLE]: حُروفُ الْجَرِّ وَعَلَاَّمَاتِ الْإِعْرَابِ الْمَجْرُورَةِ (تابع)
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition & Rule ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ب. الياء (وهِي عُلَّامَةٍ فَرْعِيَّةٍ)
Content:
<p class="text-accent mb-4">تَأْتِي الياء (بَدَلاً مِنَ الْكَسْرَةِ) مَع ثَلَاثَةِ أَنْوَاعٍ مِن الْأَسْمَاءِ أيضاً:</p>
(Component: TEMPLATE_C_LIST.html inside Block Body)
[LIST_ITEM_CONTENT]: <span class="font-bold">الْمُثَنَّى:</span> أَلْقَيْتُ مُحَاضَرَاتٍ فِي <span class="highlight-red">الْمُدَرِّسَتَيْنِ</span>. (و: سَلَّمْتُ عَلَى <span class="highlight-red">الطَّالِبَيْنِ</span>).
[LIST_ITEM_CONTENT]: <span class="font-bold">جَمَعَ الْمُذَكَّرُ السَّالِمُ:</span> أَعْطَيْتُ الْهَدَايَا لِـ<span class="highlight-red">لْمُتَمَيِّزِينَ</span>. (و: مَرَرْتُ بِ<span class="highlight-red">الْمُعَلِّمِينَ</span>).
[LIST_ITEM_CONTENT]: <span class="font-bold">الْأَسْمَاءُ الْخُمُسَةَ:</span> ذَهَبْتُ إِلَى <span class="highlight-red">أَبِيكَ</span> وَ<span class="highlight-red">أَخِيكَ</span>. (و: سَلَّمْتُ عَلَى <span class="highlight-red">ذِي</span> الْعِلْمِ).

=== BLOCK 3: The Core Matrix ===
(Component: TEMPLATE_C_BLOCK.html with TEMPLATE_C_TABLE.html)
Title: خلاصة علامة الجر (الياء)
Table Content:
[HEADER_1]: نوع الاسم
[HEADER_2]: علامة الجر
[HEADER_3]: مثال
[ROW_1_COL_1]: الْمُثَنَّى
[ROW_1_COL_2]: الياء
[ROW_1_COL_3]: أَلْقَيْتُ مُحَاضَرَاتٍ فِي الْمُدَرِّسَتَيْنِ
[ROW_2_COL_1]: جَمَعَ الْمُذَكَّرُ السَّالِمُ
[ROW_2_COL_2]: الياء
[ROW_2_COL_3]: أَعْطَيْتُ الْهَدَايَا لِـلْمُتَمَيِّزِينَ
[ROW_3_COL_1]: الْأَسْمَاءُ الْخُمُسَةَ
[ROW_3_COL_2]: الياء
[ROW_3_COL_3]: ذَهَبْتُ إِلَى أَبِيكَ

=== BLOCK 4: Evidence & Parsing ===
(Component: TEMPLATE_C_BLOCK.html)
Title: إِعْرَابُ الشَّوَاهِدِ
Content:
(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: فِي
[DETAILS_1]: حَرْفُ جَرٍّ.
[WORD_2]: الْمَدْرَسَتَيْنِ
[DETAILS_2]: اِسْمٌ مَجْرُورُ بالياء لأَنَّهُ مُثَنَّى ، وَالنُّونُ مَكْسُورَةُ.

(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: اللَّاَمُ
[DETAILS_1]: حَرْفَ جَرٍّ .
[WORD_2]: الْمُتَمَيِّزِينَ
[DETAILS_2]: اِسْمٌ مَجْرُورَ بالياء لأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ ، وَالنُّونُ مَفْتُوحَةُ.

(Component: TEMPLATE_C_IRAB_ROW.html)
[WORD_1]: إِلَى
[DETAILS_1]: حَرْفُ جَرٍّ.
[WORD_2]: أَبِيكَ
[DETAILS_2]: مَجْرُورُ بالياء لأَنّهُ مِن الْأَسْمَاءِ الْخُمُسَةَ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.

=== BLOCK 5: Deep Dive / Extra Info ===
(Component: TEMPLATE_C_BLOCK.html)
Title: فائدة نحوية
Content:
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
تذكّر دائماً أن حروف الجر تختص بالأسماء فقط، ولا تدخل على الأفعال أو الحروف الأخرى. لذلك يعتبر دخول حرف الجر على الكلمة من أهم العلامات التي تميز الاسم عن غيره.

(Component: TEMPLATE_C_BENEFIT_TIP.html)
إذا اتصلت حروف الجر (الباء، الكاف، اللام) بالاسم، فإنها لا تُفصل عنه في الكتابة، بل تُكتب متصلة به مباشرة كما في: (بِالْقَلَمِ، كَالْقَمَرِ، لِلْمُعَلِّمِ). حروف الجر مبنية دائماً، أي أن حركتها لا تتغير بتغير موقعها في الجملة، وهي لا محل لها من الإعراب سوى أنها تجر الاسم الذي بعدها.

(Component: TEMPLATE_C_BENEFIT.html)
الاسم المجرور يكون مجروراً بالكسرة الظاهرة إذا كان مفرداً أو جمع تكسير أو جمع مؤنث سالم، ومجروراً بالياء إذا كان مثنى أو جمع مذكر سالم أو من الأسماء الخمسة. الجر هو من خصائص الأسماء، كما أن الجزم من خصائص الأفعال، ولا يدخل أحدهما على الآخر في اللغة العربية. يجب الانتباه إلى التفريق بين (لام الجر) المكسورة دائماً، وبين (لام الابتداء) المفتوحة، وكذلك (لام التعليل) التي تنصب الفعل المضارع. من المهم جداً ضبط أواخر الكلمات المجرورة بالحركات الصحيحة، وخاصة الكسرة، لأن ذلك يعكس الفهم الصحيح لقواعد النحو العربي الأصيلة. احرص على مراجعة علامات الإعراب الأصلية والفرعية بشكل دوري لتثبيت الفهم وتجنب الأخطاء الشائعة في الإعراب.

=== BLOCK 6: Evaluation (Exam) ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: اِسْتَخْرَجَ حَرْفُ الْجَرِّ وَالْاِسْمِ الْمَجْرُورِ وَبَيِّنِ عَلَاَّمَةِ جَرِّهِ وَالسَّبَبِ فِي الْجَمَلِ الْآتِيَةِ : ١. يَبْدُو وَجْهُ الطِّفْلِ كَالْْبَدْرِ . ٢. يَفْخُرُ الْمُعَلِّمُ بِالطَّالِبَيْنِ الْمُتَفَوِّقِينَ . ٣. شَرَحْتُ الدَّرْسَ فِي الْفَصْلَيْنِ .

Number: ٢
Question: صَحَّحَ الْخَطَأُ فِي الْجَمَلِ الْآتِيَةِ : ١. سَلَّمْتُ عَلَى الْمُهَنْدِسُونَ فِي الْمَوْقِعِ . ٢. أَخَذْتُ الْقَلَمَ مِن أَخُوكَ .

--- END STREAM ---