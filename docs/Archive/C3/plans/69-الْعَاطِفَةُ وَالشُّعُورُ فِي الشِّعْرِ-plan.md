# **SESSION 69.0**

[TASK DEFINITION]
Objective: Implement الْعَاطِفَةُ وَالشُّعُورُ فِي الشِّعْرِ.
File: `pages/69.0_nXX_الْعَاطِفَةُ وَالشُّعُورُ فِي الشِّعْرِ.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Use `verify_layout.py`.
3. text Content: 100% Arabic with full Harakat.
4. Highlighting: Use `.highlight-red`, `.highlight-blue`, `.highlight-green`.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide: NO INLINE STYLES.
7. Templates: Use only "Jules-workspace/Templates/" components.
8. Unique IDs: Use id_manager.py.
9. Self-Correction: Run lint_pages.py.
10. No Summarizing: Do not summarize examples.
11. Tashkeel: Preserve exact Tashkeel.
12. Visual Density: Dense page.
13. Balanced Colors: 1 orange element.
14. Wrapper: `TEMPLATE_C_PAGE_WRAPPER.html`.
15. Exam Section: End of lesson.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[CATEGORY_HEADER]: المستوى المتقدم
[SECTION_HEADER]: علم البلاغة
[AUTHOR_NAME]: أ. حنا خفيف
[AUTHOR_PHONE]:  
[CHAPTER_TITLE]: الْعَاطِفَةُ وَالشُّعُورُ فِي الشِّعْرِ
[LESSON_NUMBER]: 69

=== BLOCK 2: مَفْهُومُ العاطِفَةِ (إِحْسَاسُ الشَّاعِرِ) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مَفْهُومُ العاطِفَةِ (إِحْسَاسُ الشَّاعِرِ)
Content: <p class="text-accent mt-1mm">الْقَصِيدَةُ لَيْسَتْ كَلِمَاتٍ فَقَطْ، بَلْ هِيَ مَشَاعِرُ دَاخِلِيَّةٌ صَادِقَةٌ يَنْقُلُهَا لَنَا الشَّاعِرُ (<span class="highlight-green">حُزْن</span>، <span class="highlight-green">فَرَح</span>، <span class="highlight-green">شَوْق</span>، <span class="highlight-green">إِعْجَاب</span>، <span class="highlight-green">تَمَرُّد</span>، <span class="highlight-green">غَضَب</span>، <span class="highlight-green">أَمَل</span>، <span class="highlight-green">خَيْبَة</span>).</p>

=== BLOCK 3: أَسْلِحَةُ الشَّاعِرِ (أَدَوَاتٌ فَنِّيَّةٌ) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَسْلِحَةُ الشَّاعِرِ (أَدَوَاتٌ فَنِّيَّةٌ)
Content: <div class="mt-1mm text-accent">وَيُوَصِّلُ لَنَا الشَّاعِرُ إِحْسَاسَهُ هَذَا عَبْرَ ثَلَاثَةِ أَسْلِحَةٍ (أَدَوَاتٍ فَنِّيَّةٍ):</div>
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: <strong>الْأَلْفَاظُ :</strong> كَلِمَاتٌ مُفْرَدَةٌ.
[LIST_ITEM_CONTENT]: <strong>التَّرَاكِيبُ :</strong> جُمَلٌ كَامِلَةٌ.
[LIST_ITEM_CONTENT]: <strong>الصُّوَرُ الْبَيَانِيَّةُ :</strong> الْخَيَالُ وَالتَّشْبِيهَاتُ.

=== BLOCK 4: كَيْفَ نَسْتَخْرِجُ الْعَاطِفَةَ؟ (نَمَاذِجُ) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: كَيْفَ نَسْتَخْرِجُ الْعَاطِفَةَ؟ (نَمَاذِجُ)
Content: <p class="mt-1mm">١. شُعُورُ (<span class="highlight-red">الْحُزْنِ وَالْيَأْسِ</span>):</p>
(Component: TEMPLATE_C_POEM.html)
[HEMISTICH_RIGHT]: حَارَ فِكْرِي
[HEMISTICH_LEFT]: وَضَاقَ صَدْرِي
[POET_NAME]: الشَّاعِرُ
[POET_DETAILS]:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: <strong>الْعَاطِفَةُ:</strong> <span class="highlight-green">حُزْنٌ وَأَلَمٌ</span>.
[LIST_ITEM_CONTENT]: <strong>الْأَدَوَاتُ الَّتِي أَظْهَرَتْهَا:</strong> (<span class="highlight-blue">أَلْفَاظٌ</span>: ضَاقَ، حَارَ) (<span class="highlight-blue">تَرَاكِيبُ</span>: ضَاقَ صَدْرِي).

=== BLOCK 5: نَمُوذَجُ شُعُورِ الْأَمَلِ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: نَمُوذَجُ شُعُورِ الْأَمَلِ
Content: <p class="mt-1mm">٢. شُعُورُ (<span class="highlight-red">الْأَمَلِ وَالتَّفَاؤُلِ</span>):</p>
(Component: TEMPLATE_C_POEM.html)
[HEMISTICH_RIGHT]: وَتَوَقَّعْ إِذَا السَّمَاءُ اكْفَهَرَّتْ
[HEMISTICH_LEFT]: مَطَراً يُحْيِي السُّهُولَا
[POET_NAME]: الشَّاعِرُ
[POET_DETAILS]:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: <strong>الْعَاطِفَةُ:</strong> <span class="highlight-green">أَمَلٌ وَتَفَاؤُلٌ بِالْمُسْتَقْبَلِ</span>.
[LIST_ITEM_CONTENT]: <strong>الْأَدَوَاتُ:</strong> (<span class="highlight-blue">أَلْفَاظٌ</span>: مَطَر، يُحْيِي) (<span class="highlight-blue">صُورَةٌ بَيَانِيَّةٌ</span>: مَطَرٌ يُحْيِي السُّهُولَا).

=== BLOCK 6: نَمُوذَجُ شُعُورِ الِافْتِخَارِ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: نَمُوذَجُ شُعُورِ الِافْتِخَارِ
Content: <p class="mt-1mm">٣. شُعُورُ (<span class="highlight-red">الِافْتِخَارِ وَالاعْتِزَازِ</span>):</p>
(Component: TEMPLATE_C_POEM.html)
[HEMISTICH_RIGHT]: نَحْنُ أَهْرَقْنَا
[HEMISTICH_LEFT]: عَلَيْهَا دَمَنَا
[POET_NAME]: الشَّاعِرُ
[POET_DETAILS]:
(Component: TEMPLATE_C_LIST.html)
[LIST_ITEM_CONTENT]: <strong>الْعَاطِفَةُ:</strong> <span class="highlight-green">فَخْرٌ وَاعْتِزَازٌ بِالتَّضْحِيَةِ</span>.
[LIST_ITEM_CONTENT]: <strong>التَّرَاكِيبُ:</strong> (<span class="highlight-blue">أَهْرَقْنَا دَمَنَا</span>).

=== BLOCK 7: الْمُلَخَّصُ (THE CORE MATRIX) ===
(Component: TEMPLATE_C_TABLE.html)
[TABLE_HEADER_1]: الْعَاطِفَةُ
[TABLE_HEADER_2]: الْأَدَوَاتُ الفَنِّيَّةُ
[TABLE_ROW_1_COL_1]: حُزْنٌ وَأَلَمٌ
[TABLE_ROW_1_COL_2]: ضَاقَ صَدْرِي، حَارَ
[TABLE_ROW_2_COL_1]: أَمَلٌ وَتَفَاؤُلٌ
[TABLE_ROW_2_COL_2]: مَطَراً يُحْيِي، يُحْيِي
[TABLE_ROW_3_COL_1]: فَخْرٌ وَاعْتِزَازٌ
[TABLE_ROW_3_COL_2]: أَهْرَقْنَا دَمَنَا

=== BLOCK 8: مَعْلُومَةٌ إِضَافِيَّةٌ ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: <strong>تَنْبِيهٌ هَامٌّ:</strong> لَا يُمْكِنُ فَهْمُ عَاطِفَةِ الشَّاعِرِ دُونَ النَّظَرِ إِلَى الْأَلْفَاظِ وَالتَّرَاكِيبِ الَّتِي اِسْتَخْدَمَهَا فِي سِيَاقِ الْقَصِيدَةِ.

=== BLOCK 9: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: اِسْتَخْرِجْ الْعَاطِفَةَ مِنَ الْبَيْتِ الشِّعْرِيِّ التَّالِي مُوَضِّحاً الْأَدَوَاتِ الَّتِي اِسْتَخْدَمَهَا الشَّاعِرُ: "أَنَا الَّذِي نَظَرَ الْأَعْمَى إِلَى أَدَبِي".
Number: ٢
Question: هَلْ يُمْكِنُ أَنْ تَخْلُوَ الْقَصِيدَةُ مِنَ الْعَاطِفَةِ؟ اشْرَحْ ذَلِكَ مُعْتَمِداً عَلَى مَفْهُومِ الْعَاطِفَةِ الَّذِي دَرَسْتَهُ.

--- END STREAM ---
