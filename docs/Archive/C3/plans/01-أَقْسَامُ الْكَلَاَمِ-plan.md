# **SESSION 01.0**

[TASK DEFINITION]
Objective: Implement أَقْسَامُ الْكَلَاَمِ.
File: `pages/01.0_nXX_أَقْسَامُ الْكَلَاَمِ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/01.1_...` if page have a lot of blank space add exam elements from the lesson.
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
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
15. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 01
[CHAPTER_TITLE]: أَقْسَامُ الْكَلَاَمِ
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. حنا خفيف
[AUTHOR_PHONE]:  

=== BLOCK 2: مُقَدَّمَةً ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مُقَدَّمَةً
Content: <p class="text-accent mb-2mm">يُقَسِّمُ عُلَمَاءُ اللُّغَةَ الْعَرَبِيَّةَ مَا يَتَلَفَّظُ بِه الْإِنْسَانِ إِلَى خَمْسَةٍ أَقْسَامَ رَئِيسِيَّةَ. هَذَا التَّقْسِيمُ يُسَاعِدُنَا عَلَى فَهْمِ كَيْفِيَّةِ بِنَاءِ الْجُمَلِ وَتَرْكِيبِهَا بِطَرِيقَةٍ صَحِيحَةٍ.</p><p class="m-0">لِفَهِمَ قَوَاعِدُ اللُّغَةَ الْعَرَبِيَّةَ بِشَكْلِ صَحِيحِ (خَاصَّةً لِلْمُبْتَدِئِينَ)، يَجِبُ أَوْلَا التَّمْييزِ بَيْن هَذِه الْمُصْطَلَحَاتِ الْخُمُسَةَ: الْكَلِمَةُ، الْكِلَاَمُ، الْكَلْمُ، الْقَوْلُ، اللَّفْظُ.</p>

=== BLOCK 3: ١. الْكَلِمَةُ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ١. الْكَلِمَةُ
Content: <p class="text-accent mb-2mm">هِي اللَّفْظِ الْمَوْضُوعِ لِمُعَنَّى مُفْرَدَ. أي أَنّهَا لَفْظَةَ وَاحِدَةَ تَدَلٍّ عَلَى شَيْءِ مُعَيَّنِ بذَاتهُ ولا تُكَوِّنُ جُمْلَةً بِمُفْرَدِهَا.</p>
<div class="font-bold mb-2mm text-primary">أَمِثْلَةَ أَسَاسِيَّةً:</div>
(Inject: TEMPLATE_C_CHIPS.html)
Chips: بَحْرٌ, قَلَمٌ, شَجَرَةً, تِلْميذٌ, مُعَلِّمٌ, رَجُلٌ
(End Inject)
<div class="font-bold mt-2mm mb-2mm text-primary">أَمِثْلَةَ إِضَافِيَّةً:</div>
(Inject: TEMPLATE_C_CHIPS.html)
Chips: مَدْرَسَةٌ, كِتَابٌ, شَمْسٌ, قَمَرٌ, ذَهَبَ, فِي
(End Inject)
<p class="text-sm mt-2mm mb-0 text-center">(كُلُّ وَاحِدَةٍ مِنْ هَذِهِ تُسَمَّى "كَلِمَةً").</p>

=== BLOCK 4: الشاهد الشعري ===
(Component: TEMPLATE_C_POEM.html)
Line 1 - Hemistich 1: أَقُولُ لَهُ وقَد طَارَتْ شَعَاعًا
Line 1 - Hemistich 2: مِنَ الْأَبْطَالِ <span class="highlight-red">وَيْحَكَ لَنْ تُرَاعِي</span>

=== BLOCK 5: إعراب الشاهد ===
(Component: TEMPLATE_C_IRAB_ROW.html)
Box 1 Word: وَيْحَكَ لَنْ تُرَاعِي
Box 1 Details: جُمْلَةٌ كَامِلَةٌ (كَلَامٌ)، أَطْلَقَ عَلَيْهَا الشَّاعِرُ اسْمَ "كَلِمَةٍ" مَجَازاً.

=== BLOCK 6: ملاحظة مجازية ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: <p class="m-0">ملاحظة: الشاعر يقصد بـ"وَيْحَكَ لَنْ تُرَاعِي" أنها جملة كاملة، ولكن العرب قد يطلقون على الجملة المفيدة اسم "كلمة" مجازاً.</p>

=== BLOCK 7: الْكِلَاَمُ وَالْكَلْمُ ===
(Component: TEMPLATE_C_SPLIT.html)
RightSide:
  (Component: TEMPLATE_C_BLOCK.html)
  Title: ٢. الْكِلَاَمُ
  Content: <p class="text-accent mb-2mm">هُو مَا تَرَكُّبٍ مِن كَلْمَتَيْنِ فأَكْثَرِ ، وَأَفَادَ مُعَنًّى يُحْسِنُ السُّكُوتُ عَلَيْهِ (أَيَّ جُمْلَةِ تَامَّةِ الْمُعَنَّى، إِذَا سَمِعَهَا الشَّخْصُ فَهِمَ الْقَصْدَ وَلَمْ يَنْتَظِرْ كَلَاماً إِضَافِيّاً).</p>
  <div class="font-bold mb-2mm text-primary">أَمِثْلَةَ:</div>
  (Inject: TEMPLATE_C_LIST.html)
  Items:
  - <span class="highlight-red">السَّفَرُ مُفِيدٌ</span> (جُمْلَةَ اِسْمِيَّةَ مُكَوِّنَةَ مِن كَلْمَتَيْنِ وَتُفِيدُ مُعَنَّى تَامًّا).
  - <span class="highlight-blue">اِذْهَبْ</span> (تَبْدُو كَكَلِمَةِ وَاحِدَةِ ، لَكِنّهَا فِي الْأَصْلِ جُمْلَةً تَتَكَوَّنُ مِن كَلْمَتَيْنِ: الْفِعْلُ "اِذْهَبْ" وَالضَّمِيرَ الْمُسْتَتِرَ "أَنْت"، وَتُفِيدُ مُعَنَّى تَامًّا).
  - <span class="highlight-red">الْعِلْمُ نُورٌ.</span> (كلام مفيد).
  - <span class="highlight-red">نَجَحَ الطَّالِبُ فِي الِامْتِحَانِ.</span> (كلام مفيد).
  - <span class="highlight-blue">اِقْرَأْ.</span> (كلام مفيد، لأن التقدير: اقرأ أنت).
  (End Inject)

LeftSide:
  (Component: TEMPLATE_C_BLOCK.html)
  Title: ٣. الْكَلْمُ
  Content: <p class="text-accent mb-2mm">هُو مَا تَكَوُّنٍ مِن ثَلاث كَلِمَاتٍ فأَكْثَرِ ، سَوَاءً أَفَادَ مُعَنًّى يُحْسِنُ السُّكُوتُ عَلَيْهِ أَم لَم يُفِدْ. الشرط الوحيد هنا هو "العدد" (ثلاث كلمات أو أكثر).</p>
  <div class="font-bold mb-2mm text-primary">أَمِثْلَةَ:</div>
  (Inject: TEMPLATE_C_LIST.html)
  Items:
  - <span class="highlight-red">كَتَبَ الطَّالِبُ الدَّرْسَ</span> (مُكَوِّنٌ مِن ٣ كَلِمَاتٍ ، وَأَفَادَ مُعَنَّى تَامًّا يُسَمَّى كَلَّمَ وَيُسَمَّى أيضاً كِلَاَمَ ).
  - <span class="highlight-blue">إِنْ قَامَ زَيْدٌ</span> أَو <span class="highlight-blue">ضَعْ إِلَى نَحْفَظُ</span> (مُكَوِّنٌ مِن ٣ كَلِمَاتٍ ، لَكِنّهُ لَا يُفِيدُ مُعَنَّى تَامًّا يُسَمَّى كَلَّمَ فَقَط ، ولَا يُسَمَّى كَلَاَمَا).
  - <span class="highlight-red">الشَّمْسُ مُشْرِقَةٌ الْيَوْمَ.</span> (كلم وكلام).
  - <span class="highlight-blue">إِذَا جَاءَ الْمُعَلِّمُ</span> (كلم فقط، لأنه غير مفيد رغم أنه ٣ كلمات).
  (End Inject)

=== BLOCK 8: الْمُلَخَّصُ ===
(Component: TEMPLATE_C_TABLE.html)
Headers: | الْمُصْطَلَحُ | التَّعْرِيفُ | مِثَالٌ |
Rows:
| الْكَلِمَةُ | لَفْظَةَ وَاحِدَةَ تَدَلٍّ عَلَى شَيْءِ مُعَيَّنِ | بَحْرٌ / شَجَرَةً |
| الْكِلَاَمُ | مَا تَرَكُّبٍ مِن كَلْمَتَيْنِ فأَكْثَرِ وَأَفَادَ مُعَنًّى | السَّفَرُ مُفِيدٌ |
| الْكَلْمُ | مَا تَكَوُّنٍ مِن ثَلاث كَلِمَاتٍ فأَكْثَرِ (مُفِيدٍ أَوْ غَيْرِ مُفِيدٍ) | إِنْ قَامَ زَيْدٌ / الشَّمْسُ مُشْرِقَةٌ الْيَوْمَ |

=== BLOCK 9: اِخْتَبِرْ نَفْسَكَ ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: حَدِّدْ نَوْعَ كُلِّ عِبَارَةٍ (كَلِمَةٌ، كَلَامٌ، أَمْ كَلِمٌ) مِمَّا يَأْتِي: السَّمَاءُ صَافِيَةٌ.

=== BLOCK 10: اِخْتَبِرْ نَفْسَكَ ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: حَدِّدْ نَوْعَ كُلِّ عِبَارَةٍ (كَلِمَةٌ، كَلَامٌ، أَمْ كَلِمٌ) مِمَّا يَأْتِي: إِنْ جَاءَ أَحْمَدُ.

--- END STREAM ---
