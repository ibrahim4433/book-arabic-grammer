# **SESSION 23.0**

[TASK DEFINITION]
Objective: Implement حَالَاتُ بِنَاءِ الْمُضَارِعِ وَفِعْلِ الْأَمْرِ.
File: `pages/23.0_nXX_حَالَاتُ بِنَاءِ الْمُضَارِعِ وَفِعْلِ الْأَمْرِ.html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/23.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 23
[CHAPTER_TITLE]: حَالَاتُ بِنَاءِ الْمُضَارِعِ وَفِعْلِ الْأَمْرِ
[CATEGORY_HEADER]: المستوى التأسيسي
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. حنا خفيف
[AUTHOR_PHONE]:  

=== BLOCK 2: بناء الفعل المضارع ===
(Component: TEMPLATE_C_BLOCK.html)
Title: بِنَاءُ الْفِعْلِ الْمُضَارِعِ
Content: <p class="text-accent">كَمَا أَشَرْنَا، يُبْنَى الْفِعْلُ الْمُضَارِعُ (أَيْ يَلْزَمُ حَرَكَةً وَاحِدَةً وَلَا يَتَغَيَّرُ) فِي حَالَتَيْنِ فَقَطْ:</p>

=== BLOCK 3: حالات البناء (المضارع) ===
(Component: TEMPLATE_C_TABLE.html)
Headers: حَالَةُ الْبِنَاءِ | السَّبَبُ (نَوْعُ النُّونِ) | مِثَالٌ وَإِعْرَابٌ
Row 1: الْبِنَاءُ عَلَى السُّكُونِ | عِنْدَ اتِّصَالِهِ بِـ <span class="highlight-blue">نُونِ النِّسْوَةِ</span> | الطَّالِبَاتُ <span class="highlight-red">يَفْخُرْنَ</span> بِنَجَاحِهِنَّ. يَفْخُرْنَ: فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى السُّكُونِ. (وَالنُّونُ ضَمِيرُ فَاعِلٍ).
Row 2: الْبِنَاءُ عَلَى الْفَتْحِ | عِنْدَ اتِّصَالِهِ بِـ <span class="highlight-blue">نُونِ التَّوْكِيدِ</span> (الثَّقِيلَةِ الْمُشَدَّدَةِ أَوِ الْخَفِيفَةِ السَّاكِنَةِ) | لَـ <span class="highlight-red">يَشْرَبَنْ</span> / لَـ <span class="highlight-red">يَدْرُسَنَّ</span> الطَّالِبُ. يَشْرَبَنْ: مُضَارِعٌ مَبْنِيٌّ عَلَى الْفَتْحِ. (وَالنُّونُ حَرْفٌ لَا مَحَلَّ لَهُ لِلتَّوْكِيدِ فَقَطْ).

=== BLOCK 4: نماذج إعرابية لحالات متقدمة (المضارع) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: نَمَاذِجُ إِعْرَابِيَّةٌ لِحَالَاتٍ مُتَقَدِّمَةٍ (الْمُضَارِعِ)
Content:
[Use TEMPLATE_C_IRAB_ROW.html within block]
Word 1: لِيَتَعَلَّمَ
Details 1: (اللَّامُ) لَامُ التَّعْلِيلِ (تُفِيدُ السَّبَبَ). يَتَعَلَّمَ: مُضَارِعٌ مَنْصُوبٌ بِـ (أَنْ) مُضْمَرَةٍ (مَخْفِيَّةٍ) بَعْدَ لَامِ التَّعْلِيلِ، وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ.
Word 2: فَتَنْدَمَ
Details 2: لَا تَغْضَبْ فَتَنْدَمَ: (الْفَاءُ) فَاءُ السَّبَبِيَّةِ لِأَنَّهَا سُبِقَتْ بِنَهْيٍ. تَنْدَمَ: مُضَارِعٌ مَنْصُوبٌ بِـ (أَنْ) مُضْمَرَةٍ بَعْدَ فَاءِ السَّبَبِيَّةِ.
Word 3: لِيَفْهَمُوا
Details 3: مَا كَانَ لِيَفْهَمُوا: (اللَّامُ) لَامُ الْجُحُودِ (لِأَنَّهَا سُبِقَتْ بِـ كَوْنٍ مَنْفِيٍّ "مَا كَانَ"، تُفِيدُ شِدَّةَ النَّفْيِ). يَفْهَمُوا: مَنْصُوبٌ بِـ (أَنْ) مُضْمَرَةٍ، وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ.
Word 4: تَنْهَ
Details 4: لَا تَنْهَ عَنْ خُلُقٍ: لَا: نَاهِيَةٌ جَازِمَةٌ. تَنْهَ: مُضَارِعٌ مَجْزُومٌ بِـ لَا النَّاهِيَةِ، وَعَلَامَةُ جَزْمِهِ حَذْفُ حَرْفِ الْعِلَّةِ (الْأَلِفِ)، وَالْفَتْحَةُ دَلِيلٌ عَلَيْهَا.

=== BLOCK 5: تعريف فعل الأمر ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَعْرِيفُ فِعْلِ الْأَمْرِ
Content: <p class="text-accent">هُوَ طَلَبُ حُدُوثِ الْفِعْلِ فِي الزَّمَنِ الْمُسْتَقْبَلِ (أَيْ بَعْدَ الِانْتِهَاءِ مِنَ الْكَلَامِ، أُطْلِبُ مِنْكَ أَنْ تَفْعَلَ شَيْئاً).</p>

=== BLOCK 6: Benefit Warning ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: حُكْمُهُ الْبِنَاءُ دَائِمًا كَالْمَاضِي.

=== BLOCK 7: قاعدة ذهبية (Benefit Tip) ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Content:  قَاعِدَةٌ ذَهَبِيَّةٌ لِإِعْرَابِ الْأَمْرِ بِلَا حِفْظٍ: (يُبْنَى فِعْلُ الْأَمْرِ عَلَى مَا يُجْزَمُ بِهِ مُضَارِعُهُ). إِذَا كَانَ مُضَارِعُهُ يُجْزَمُ بِالسُّكُونِ (لَمْ يَكْتُبْ)، فَالْأَمْرُ يُبْنَى عَلَى السُّكُونِ (اُكْتُبْ).

=== BLOCK 8: حالات بناء فعل الأمر ===
(Component: TEMPLATE_C_TABLE.html)
Headers: عَلَامَةُ الْبِنَاءِ | الْحَالَةُ وَالسَّبَبُ | مِثَالٌ
Row 1: السُّكُونُ (الْأَصْلُ) | صَحِيحُ الْآخِرِ (وَلَمْ يَتَّصِلْ بِهِ شَيْءٌ) / أَوْ اتَّصَلَتْ بِهِ نُونُ النِّسْوَةِ | اجْلِسْ يَا سَعِيدُ / اكْتُبْنَ يَا فَتَيَاتُ.
Row 2: حَذْفُ حَرْفِ الْعِلَّةِ | مُعْتَلُّ الْآخِرِ (آخِرُهُ أَلِفٌ، وَاوٌ، أَوْ يَاءٌ) | اسْعَ (أَصْلُ مُضَارِعِهِ تَسْعَى) / ادْعُ (تَدْعُو) / ارْمِ (تَرْمِي). نَحْذِفُ الْحَرْفَ وَنَتْرُكُ حَرَكَةً تُنَاسِبُهُ.
Row 3: حَذْفُ النُّونِ | الْأَفْعَالُ الْخَمْسَةُ (إِذَا اتَّصَلَتْ بِهِ وَاوُ الْجَمَاعَةِ، أَلِفُ الِاثْنَيْنِ، يَاءُ الْمُؤَنَّثَةِ الْمُخَاطَبَةِ) | اذْهَبُوا / اذْهَبَا / اذْهَبِي. (الْوَاوُ وَالْأَلِفُ وَالْيَاءُ فَاعِلٌ).
Row 4: الْفَتْحُ | إِذَا اتَّصَلَتْ بِهِ نُونُ التَّوْكِيدِ (الثَّقِيلَةُ/الْخَفِيفَةُ) لِلتَّشْدِيدِ عَلَى الطَّلَبِ | اصْبِرَنَّ يَا رَجُلُ / اكْتُبَنْ هَذَا بِسُرْعَةٍ.

=== BLOCK 9: نماذج إعرابية (الأمر) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: نَمَاذِجُ إِعْرَابِيَّةٌ (الْأَمْرِ)
Content:
[Use TEMPLATE_C_IRAB_ROW.html within block]
Word 1: ادْعُ
Details 1: ادْعُ إِلَى الْخَيْرِ: فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ حَرْفِ الْعِلَّةِ (الْوَاوِ)، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ (أَنْتَ) وُجُوباً.
Word 2: احْفَظْ
Details 2: احْفَظْ دَرْسَكَ: فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ الظَّاهِرِ. وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ (أَنْتَ).
Word 3: اعْمَلُوا
Details 3: اعْمَلُوا بِجِدٍّ: فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ لِأَنَّ مُضَارِعَهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَ(وَاوُ الْجَمَاعَةِ) ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعِ فَاعِلٍ.

=== BLOCK 10: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: مَا عَلَامَةُ بِنَاءِ الْفِعْلِ الْمَاضِي فِي جُمْلَةِ: "الْطُّلَّابُ كَتَبُوا الْوَاجِبَ"؟ وَمَا السَّبَبُ؟
Number: ٢
Question: مَتَى يُبْنَى الْفِعْلُ الْمُضَارِعُ عَلَى السُّكُونِ؟ مَثِّلْ لِذَلِكَ.

--- END STREAM ---