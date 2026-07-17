# **SESSION 12.0**

[TASK DEFINITION]
Objective: Implement الصحيح والمعتل.
File: `pages/12.0_nXX_الصحيح والمعتل.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/[LESSON_NUMBER].1_...` if page have a lot of blank space add exam elements from the lesson.
3. text Content: 100% Arabic with full Harakat.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green`  for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   **Rule:** NO INLINE STYLES.
*   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
*   **Mapping:**
    *   `style="width: 20%"` -> `class="w-20pct"`
    *   `style="margin-top: 2mm"` -> `class="mt-2mm"`
    *   `style="text-align: center"` -> `class="text-center"`
    *   `style="font-weight: bold"` -> `class="font-bold"`
6. Templates: You are forbidden from inventing new HTML tags or classes or template elements. You must map all content using "Jules-workspace/Templates/" components as the STREAM says in suitable way.
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). use "Jules-workspace/id_manager.py" to generate or verify them.
8. **Self-Correction:** Run "Jules-workspace/lint_pages.py" after creating html files. If it fails, you MUST fix the errors (usually inline styles) before submitting.
9. Do not summarize examples. 
10. Do not provide uncompleted text content using (...) .
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.  
12. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal 

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER)
[LESSON_NUMBER]: 12
[CHAPTER_TITLE]: الصحيح والمعتل
[CATEGORY_HEADER]: الصرف
[SECTION_HEADER]: المستوى اللغوي
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition of Sound and Weak ===
(Component: TEMPLATE_C_BLOCK)
Title: مفهوم الفعل الصحيح والفعل المعتل
Content: <p class="text-accent text-right mb-2mm"><strong>الفِعْلُ الصَّحِيحُ:</strong> هوَ ما كانَتْ حُروفُهُ الأَصْلِيَّةُ خاليةً مِنْ حُروفِ العِلَّةِ (الألف، الواو، الياء).</p><p class="text-accent text-right"><strong>الفِعْلُ المُعْتَلُّ:</strong> هوَ ما كانَ أَحَدُ حُروفِهِ الأَصْلِيَّةِ حَرْفَ عِلَّةٍ.</p>

=== BLOCK 3: The Sound Verb Types (Matrix) ===
(Component: TEMPLATE_C_TABLE)
Title: أَقْسَامُ الفِعْلِ الصَّحِيحِ
Columns: النَّوْع, التَّعْرِيف, أَمْثِلَة
Rows:
- السَّالِم || ما خَلَتْ أُصولُهُ مِنَ الهَمْزَةِ وَالتَّضْعِيفِ. || <span class="highlight-blue">كَتَبَ</span>، <span class="highlight-blue">جَلَسَ</span>، <span class="highlight-blue">فَهِمَ</span>
- المَهْمُوز || ما كانَ أَحَدُ أُصولِهِ هَمْزَةً. || <span class="highlight-red">أَمَرَ</span>، <span class="highlight-red">سَأَلَ</span>، <span class="highlight-red">لَجَأَ</span>
- المُضَعَّف || ما كانَ أَحَدُ أُصولِهِ مُشَدَّدًا (مُضَعَّفًا). || <span class="highlight-green">صَدَّ</span>، <span class="highlight-green">جَدَّ</span>، <span class="highlight-green">مَدَّ</span>

=== BLOCK 4: The Weak Verb Types (Core Matrix) ===
(Component: TEMPLATE_C_TABLE)
Title: أَقْسَامُ الفِعْلِ المُعْتَلِّ
Columns: النَّوْع, مَوْضِعُ العِلَّةِ, أَمْثِلَة
Rows:
- المِثَال || أَوَّلُهُ حَرْفُ عِلَّةٍ. || <span class="highlight-blue">وَصَلَ</span>، <span class="highlight-blue">وَجَدَ</span>، <span class="highlight-blue">يَئِسَ</span>
- الأَجْوَف || أَوْسَطُهُ (عَيْنُهُ) حَرْفُ عِلَّةٍ. || <span class="highlight-red">قَالَ</span>، <span class="highlight-red">صَامَ</span>، <span class="highlight-red">بَاعَ</span>
- النَّاقِص || آخِرُهُ (لَامُهُ) حَرْفُ عِلَّةٍ. || <span class="highlight-green">مَشَى</span>، <span class="highlight-green">دَنَا</span>، <span class="highlight-green">رَمَى</span>

=== BLOCK 5: The Mixed Weak (Lafif) ===
(Component: TEMPLATE_C_SPLIT)
[LEFT_TITLE]: اللَّفِيفُ المَفْرُوق
[LEFT_CONTENT]:
(Component: TEMPLATE_C_BLOCK)
Title: تَعْرِيفُهُ
Content: هوَ ما كانَ فيهِ حَرْفَا عِلَّةٍ، بَيْنَهُمَا فاصِلٌ (حَرْفٌ صَحِيحٌ).
(Component: TEMPLATE_C_LIST)
Items:
- مِثْل: <span class="highlight-red">وَعَى</span>
- مِثْل: <span class="highlight-red">وَشَى</span>
- مِثْل: <span class="highlight-red">وَقَى</span>

[RIGHT_TITLE]: اللَّفِيفُ المَقْرُون
[RIGHT_CONTENT]:
(Component: TEMPLATE_C_BLOCK)
Title: تَعْرِيفُهُ
Content: هوَ ما كانَ فيهِ حَرْفَا عِلَّةٍ مُتَتَالِيَانِ (دونَ فاصِلٍ).
(Component: TEMPLATE_C_LIST)
Items:
- مِثْل: <span class="highlight-blue">رَوَى</span>
- مِثْل: <span class="highlight-blue">هَوَى</span>
- مِثْل: <span class="highlight-blue">طَوَى</span>

=== BLOCK 6: Golden Tip ===
(Component: TEMPLATE_C_BENEFIT_TIP)
Title: فائِدَةٌ صَرْفِيَّةٌ مُهِمَّةٌ
Content: لِمَعْرِفَةِ نَوْعِ الفِعْلِ (صَحِيح أَمْ مُعْتَلّ)، يَجِبُ الرُّجُوعُ إِلى <span class="highlight-red">الماضِي المُجَرَّدِ</span> (الأُصولِ الثَّلاثَةِ)، وَحَذْفُ أَحْرُفِ الزِّيادَةِ. مِثال: (يَسْتَخْرِجُ) -> (خَرَجَ) -> صَحِيحٌ سالِمٌ.

=== BLOCK 7: Lesson Evaluation ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: صَنِّفِ الأَفْعَالَ الآتِيَةَ إِلَى صَحِيحٍ وَمُعْتَلٍّ مَعَ بَيانِ النَّوْعِ: (نَامَ - شَدَّ - وَعَدَ - قَرَأَ - رَضِيَ - طَوَى).

--- END STREAM ---
