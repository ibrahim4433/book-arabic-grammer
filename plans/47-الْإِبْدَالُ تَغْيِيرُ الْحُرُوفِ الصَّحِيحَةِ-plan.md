# **SESSION 47.0**

[TASK DEFINITION]
Objective: Implement الْإِبْدَالُ تَغْيِيرُ الْحُرُوفِ الصَّحِيحَةِ.
File: `pages/47.0_nXX_الْإِبْدَالُ تَغْيِيرُ الْحُرُوفِ الصَّحِيحَةِ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/47.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 47
[CHAPTER_TITLE]: الْإِبْدَالُ تَغْيِيرُ الْحُرُوفِ الصَّحِيحَةِ
[CATEGORY_HEADER]: المستوى المتوسط
[SECTION_HEADER]: علم الصرف
[AUTHOR_NAME]: أ. حنا خفيف
[AUTHOR_PHONE]:  

=== BLOCK 2: Definition ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَعْرِيفُ الإِبْدَالِ
Content: <p class="text-accent">هُوَ جَعْلُ حَرْفٍ مَكَانَ حَرْفٍ، وَهُوَ يَخْتَلِفُ عَنِ الْإِعْلَالِ بِأَنَّ الإِبْدَالَ قَدْ يَقَعُ فِي الحُرُوفِ الصَّحِيحَةِ وَالمُعْتَلَّةِ (مِثْل: اصْطَبَرَ بَدَلَ اسْتَبَرَ)، بَيْنَمَا الإِعْلَالُ يَخْتَصُّ بِحُرُوفِ العِلَّةِ فَقَطْ.</p>

=== BLOCK 3: The Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Columns: 3
Headers: الْقَاعِدَةُ | التَّوْضِيحُ | مِثَالٌ
Row 1: إِبْدَالُ الْوَاوِ وَالْيَاءِ إِلَى (هَمْزَةٍ) | إِذَا تَطَرَّفَتَا بَعْدَ أَلِفٍ زَائِدَةٍ أَوْ فِي صِيغَةِ مُنْتَهَى الْجُمُوعِ (فَعَائِل) | كِسَاء، عَجَائِز
Row 2: إِبْدَالُ (تَاءِ) (افْتَعَلَ) إِلَى حُرُوفٍ مُفَخَّمَةٍ | تُبْدَلُ (طَاءً) بَعْدَ الصَّادِ وَالضَّادِ، وَ(دَالًا) بَعْدَ الزَّايِ وَالدَّالِ | اضْطَرَّ، ازْدَهَرَ
Row 3: إِبْدَالُ (وَاوِ) الْفِعْلِ الْمِثَالِ إِلَى (تَاءٍ) | فِي صِيغَةِ (افْتَعَلَ) تُبْدَلُ الْوَاوُ تَاءً وَتُدْغَمُ | اتَّقَدَ

=== BLOCK 4: EXTRA INFO (Color Balancing) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: تَنْبِيهٌ هَامٌّ!
Content: <p>الإِبْدَالُ يَخْتَلِفُ عَنِ الْإِعْلَالِ بِأَنَّ الإِبْدَالَ قَدْ يَقَعُ فِي <span class="highlight-blue">الحُرُوفِ الصَّحِيحَةِ</span> وَالمُعْتَلَّةِ (مِثْل: <span class="highlight-red">اصْطَبَرَ</span> بَدَلَ اسْتَبَرَ)، بَيْنَمَا الإِعْلَالُ يَخْتَصُّ بِحُرُوفِ العِلَّةِ فَقَطْ.</p>

=== BLOCK 5: Deep Dive - Rule 1 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ١- إِبْدَالُ الْوَاوِ وَالْيَاءِ إِلَى (هَمْزَةٍ)
Content: <p>إِذَا تَطَرَّفَتَا بَعْدَ أَلِفٍ زَائِدَةٍ (جَاءَتَا فِي آخِرِ الْكَلِمَةِ).</p>
Child Component: TEMPLATE_C_LIST.html
[LIST_ITEM_CONTENT]: <span class="highlight-red">كِسَاء</span> : أَصْلُهَا كِسَاو (مِنْ يَكْسُو). تَحوَّلَتِ الْوَاوُ إِلى هَمْزَةٍ لأَنَّهَا جَاءَتْ فِي آخِرِ كَلِمَة بَعْدَ أَلِفٍ.
[LIST_ITEM_CONTENT]: <span class="highlight-red">بِنَاء</span> : أَصْلُهَا بِنَاي (مِنْ يَبْنِي). تَحوَّلَتِ الْيَاءُ إِلى هَمْزَةٍ لِنَفْسِ السَّبَبِ.

=== BLOCK 6: Extra Info for Rule 1 ===
(Component: TEMPLATE_C_BENEFIT.html)
Title: فَائِدَةٌ صَرْفِيَّةٌ
Content: <p>وَكَذَلِكَ فِي صِيغَةِ مُنْتَهَى الْجُمُوعِ (فَعَائِل): <span class="highlight-blue">عَجَائِز</span> (أَصْلُهَا عَجَاوِز)، <span class="highlight-blue">قَصَائِد</span> (أَصْلُهَا قَصَايِد)، <span class="highlight-blue">صَحَائِف</span> (صَحَايِف).</p>

=== BLOCK 7: Deep Dive - Rule 2 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٢- إِبْدَالُ (تَاءِ) مُشْتَقَّاتِ (افْتَعَلَ) إِلَى حُرُوفٍ مُفَخَّمَةٍ
Content: <p>لِسُهُولَةِ النُّطْقِ:</p>
Child Component: TEMPLATE_C_LIST.html
[LIST_ITEM_CONTENT]: تُبْدَلُ التَّاءُ (طَاءً) بَعْدَ الصَّادِ وَالضَّادِ: <span class="highlight-red">اضْطَرَّ</span> (أَصْلُهَا اضْتَرَّ! وَلَكِنَّ نُطْقَ الضَّادِ الْمُفَخَّمَةِ مَعَ التَّاءِ الْمُرَقَّقَةِ صَعْبٌ، فَأُبْدِلَتْ لِطَاءٍ). <span class="highlight-red">اصْطَحَبَ</span> (أَصْلُهَا اصْتَحَبَ). <span class="highlight-red">اصْطَبَرَ</span> (أَصْلُهَا اصْتَبَرَ).
[LIST_ITEM_CONTENT]: تُبْدَلُ التَّاءُ (دَالًا) بَعْدَ الزَّايِ وَالدَّالِ: <span class="highlight-red">ازْدَهَرَ</span> (أَصْلُهَا ازْتَهَرَ! أُبْدِلَتِ التَّاءُ دَالاً). <span class="highlight-red">ادَّعَى</span> (أَصْلُهَا ادْتَعَى، أُبْدِلَتْ التاء دالاً وأُدغمت).

=== BLOCK 8: Deep Dive - Rule 3 ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٣- إِبْدَالُ (وَاوِ) الْفِعْلِ الْمِثَالِ إِلَى (تَاءٍ) فِي صِيغَةِ (افْتَعَلَ)
Content:
Child Component: TEMPLATE_C_LIST.html
[LIST_ITEM_CONTENT]: <span class="highlight-red">اتَّقَدَ</span> (أَصْلُهَا اوْتَقَدَ مِنْ وَقَدَ. أُبْدِلَتِ الْوَاوُ تَاءً وَأُدْغِمَتْ فِي تَاءِ افْتَعَلَ).
[LIST_ITEM_CONTENT]: <span class="highlight-red">اتَّصَفَ</span> (أَصْلُهَا اوْتَصَفَ مِنْ وَصَفَ).
[LIST_ITEM_CONTENT]: <span class="highlight-red">اتَّصَلَ</span> (مِنْ وَصَلَ).

=== BLOCK 9: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: مَا هُوَ تَعْرِيفُ الْإِبْدَالِ، وَكَيْفَ يَخْتَلِفُ عَنِ الْإِعْلَالِ؟
Number: ٢
Question: مَا أَصْلُ كَلِمَةِ (كِسَاء) وَكَلِمَةِ (بِنَاء)؟
Number: ٣
Question: لِمَاذَا أُبْدِلَتِ التَّاءُ (طَاءً) فِي (اضْطَرَّ)؟
Number: ٤
Question: هَاتِ أَصْلَ كَلِمَةِ (اتَّقَدَ) مَعَ الشَّرْحِ.

--- END STREAM ---