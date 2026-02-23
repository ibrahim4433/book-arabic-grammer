# **SESSION 18.0**

[TASK DEFINITION]
Objective: Implement الهمزة المتوسطة.
File: `pages/18.0_nXX_الهمزة المتوسطة.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/18.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 18
[CHAPTER_TITLE]: الهمزة المتوسطة
[CATEGORY_HEADER]: الإملاء
[SECTION_HEADER]: المستوى اللغوي
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: Definition & Rule ===
(Component: TEMPLATE_C_BLOCK)
Title: تَعْرِيفُ الْهَمْزَةِ الْمُتَوَسِّطَةِ
Content: هِيَ الْهَمْزَةُ الَّتِي تَقَعُ فِي <span class="text-accent">وَسَطِ الْكَلِمَةِ</span>. وَلِكِتَابَتِهَا قَاعِدَةٌ عَامَّةٌ تَعْتَمِدُ عَلَى الْمُقَارَنَةِ بَيْنَ <span class="highlight-red">حَرَكَتِهَا</span> وَحَرَكَةِ <span class="highlight-blue">الْحَرْفِ الَّذِي قَبْلَهَا</span>، فَنَرْسُمُهَا عَلَى الْحَرْفِ الَّذِي يُنَاسِبُ <span class="font-bold">أَقْوَى الْحَرَكَتَيْنِ</span>.

=== BLOCK 3: Strength of Vowels ===
(Component: TEMPLATE_C_CHIPS)
Title: تَسَلْسُلُ قُوَّةِ الْحَرَكَاتِ
List: ["الْكَسْرَةُ (أَقْوَى شَيْءٍ)", "الضَّمَّةُ", "الْفَتْحَةُ", "السُّكُونُ (أَضْعَفُ شَيْءٍ)"]

=== BLOCK 4: General Rule Matrix ===
(Component: TEMPLATE_C_TABLE)
Title: جَدْوَلُ الْقَاعِدَةِ الْعَامَّةِ
Headers: ["الْحَرَكَةُ الْأَقْوَى", "الْحَرْفُ الْمُنَاسِبُ", "أَمْثِلَةٌ"]
Rows: [
  ["الْكَسْرَةُ", "النَّبْرَةُ (ـئـ)", "تَئِن، سُئِل، بِئْر"],
  ["الضَّمَّةُ", "الْوَاوُ (ـؤـ)", "مُؤْمِن، يُؤَدِّي، سُؤَال"],
  ["الْفَتْحَةُ", "الْأَلِفُ (ـأـ)", "سَأَلَ، رَأْس، الْبَأْس"]
]

=== BLOCK 5: Detailed Analysis ===
(Component: TEMPLATE_C_SPLIT)
Title: أَمْثِلَةٌ تَطْبِيقِيَّةٌ مُفَصَّلَةٌ
[LEFT_TITLE]: الْكَلِمَاتُ
[LEFT_CONTENT]:
(Component: TEMPLATE_C_LIST)
Title:
Items: ["١. <span class='highlight-red'>تَئِن</span>", "٢. <span class='highlight-red'>الْبَأْس</span>", "٣. <span class='highlight-red'>سَأَلَ</span>"]

[RIGHT_TITLE]: التَّحْلِيلُ وَالتَّعْلِيلُ
[RIGHT_CONTENT]:
(Component: TEMPLATE_C_LIST)
Title:
Items: ["١. هَمْزَةٌ مُتَوَسِّطَةٌ <span class='highlight-red'>مَكْسُورَةٌ</span> سُبِقَتْ <span class='highlight-blue'>بِفَتْحٍ</span>. (الْكَسْرُ أَقْوَى مِنَ الْفَتْحِ -> نَبْرَة).", "٢. هَمْزَةٌ مُتَوَسِّطَةٌ <span class='highlight-red'>سَاكِنَةٌ</span> سُبِقَتْ <span class='highlight-blue'>بِفَتْحٍ</span>. (الْفَتْحُ أَقْوَى مِنَ السُّكُونِ -> أَلِف).", "٣. هَمْزَةٌ مُتَوَسِّطَةٌ <span class='highlight-red'>مَفْتُوحَةٌ</span> سُبِقَتْ <span class='highlight-blue'>بِفَتْحٍ</span>. (تَمَاثَلَتِ الْحَرَكَتَانِ -> أَلِف)."]

=== BLOCK 6: Exceptions Header ===
(Component: TEMPLATE_C_BLOCK)
Title: الْحَالَاتُ الشَّاذَّةُ
Content: تَشِذُّ عَنِ الْقَاعِدَةِ الْعَامَّةِ حَالَتَانِ رَئِيسِيَّتَانِ، حَيْثُ لَا نَنْظُرُ إِلَى قُوَّةِ الْحَرَكَاتِ بَلْ نَتَّبِعُ قَاعِدَةً خَاصَّةً.

=== BLOCK 7: Exceptions Details ===
(Component: TEMPLATE_C_SPLIT)
Title: تَفْصِيلُ الْحَالَاتِ الشَّاذَّةِ
[LEFT_TITLE]: الْهَمْزَةُ عَلَى السَّطْرِ
[LEFT_CONTENT]:
(Component: TEMPLATE_C_BLOCK)
Title:
Content: تُكْتَبُ الْهَمْزَةُ الْمُتَوَسِّطَةُ عَلَى <span class="highlight-red">السَّطْرِ</span> إِذَا جَاءَتْ <span class="highlight-blue">مَفْتُوحَةً</span> بَعْدَ:
<br>١. <span class="font-bold">أَلِفٍ سَاكِنَةٍ</span>. مِثْلُ: <span class="highlight-red">عَبَاءَة</span>.
<br>٢. <span class="font-bold">وَاوٍ سَاكِنَةٍ</span>. مِثْلُ: <span class="highlight-red">السَّمَوْءَل</span> (حَالَةٌ شَاذَّةٌ).

[RIGHT_TITLE]: الْهَمْزَةُ عَلَى النَّبْرَةِ
[RIGHT_CONTENT]:
(Component: TEMPLATE_C_BLOCK)
Title:
Content: تُكْتَبُ الْهَمْزَةُ الْمُتَوَسِّطَةُ عَلَى <span class="highlight-red">النَّبْرَةِ</span> إِذَا جَاءَتْ <span class="highlight-blue">مُتَحَرِّكَةً</span> بَعْدَ:
<br>١. <span class="font-bold">يَاءٍ سَاكِنَةٍ</span>.
<br>أَمْثِلَةٌ:
<br>- <span class="highlight-red">بِيْئَة</span> (مَفْتُوحَةٌ بَعْدَ يَاءٍ سَاكِنَةٍ).
<br>- <span class="highlight-red">فَيْئُهَا</span> (مَضْمُومَةٌ بَعْدَ يَاءٍ سَاكِنَةٍ).

=== BLOCK 8: Benefit Tip ===
(Component: TEMPLATE_C_BENEFIT_TIP)
Title: فَائِدَةٌ هَامَّةٌ
Content: تَذَكَّرْ دَائِمًا أَنَّ <span class="font-bold highlight-red">الْكَسْرَةَ</span> هِيَ أَقْوَى الْحَرَكَاتِ عَلَى الْإِطْلَاقِ، وَوُجُودُهَا (سَوَاءٌ عَلَى الْهَمْزَةِ أَوْ عَلَى الْحَرْفِ الَّذِي قَبْلَهَا) يَجْعَلُ الْهَمْزَةَ تُكْتَبُ عَلَى <span class="highlight-blue">النَّبْرَةِ</span> دَائِمًا، مَا لَمْ تَكُنْ حَالَةً شَاذَّةً تَتَعَلَّقُ بِالسَّطْرِ.

=== BLOCK 9: Exam ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: عَلِّلْ كِتَابَةَ الْهَمْزَةِ فِي كَلِمَةِ (<span class="highlight-red">مُؤْمِن</span>) وَفْقَ الْقَاعِدَةِ الْعَامَّةِ.
Number: ٢
Question: عَلِّلْ كِتَابَةَ الْهَمْزَةِ فِي كَلِمَةِ (<span class="highlight-red">بِيْئَة</span>) وَاذْكُرْ هَلْ هِيَ حَالَةٌ قِيَاسِيَّةٌ أَمْ شَاذَّةٌ.

--- END STREAM ---
