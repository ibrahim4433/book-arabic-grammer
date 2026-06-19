# **SESSION 05.0**

[TASK DEFINITION]
Objective: Implement الْمُفْرَدُ وَالْمُثَنَّى وَالْجَمْعُ بِأَنْوَاعِهِ.
File: `pages/05.0_nXX_الْمُفْرَدُ وَالْمُثَنَّى وَالْجَمْعُ بِأَنْوَاعِهِ.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/05.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 05
[CHAPTER_TITLE]: الْمُفْرَدُ وَالْمُثَنَّى وَالْجَمْعُ بِأَنْوَاعِهِ
[CATEGORY_HEADER]:
[SECTION_HEADER]:
[AUTHOR_NAME]: أ. الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: مُقَدَّمَةً ===
(Component: TEMPLATE_C_BLOCK.html)
Title: مُقَدَّمَةً
Content:
يَنْقَسِمُ الْاِسْمُ فِي اللُّغَةَ الْعَرَبِيَّةَ مِن حَيْث الْعَدَدِ (الْكَمِّيَّةَ) إِلَى ثَلَاثَةِ أَقْسَامِ رَئِيسِيَّةِ:
(Component: TEMPLATE_C_CHIPS.html) (Nested)
- ١. الْمُفْرَدُ
- ٢. الْمُثَنَّى
- ٣. الْجَمْعُ (بِأَنْوَاعِهِ الثَّلَاثَةَ)

=== BLOCK 3: الْمُفْرَدُ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ١. الْمُفْرَدُ
Content:
<span class="text-accent">**التَّعْرِيفَ:** هُو كُلّ اِسْمٍ يَدُلُّ عَلَى وَاحِدِ (مُذَكَّرَ) أَو وَاحِدَةُ (مُؤَنَّثَ).</span>
(Component: TEMPLATE_C_LIST.html) (Nested)
- لِلْإشَارَةَ إِلَى الْمُفْرَدِ الْمُذَكَّرِ نَسْتَخْدِمُ: <span class="highlight-blue">**هَذَا**</span> (مِثْل: هَذَا تِلْميذٌ مُجْتَهِدٌ).
- لِلْإشَارَةَ إِلَى الْمُفْرَدَةِ الْمُؤَنَّثَةِ نَسْتَخْدِمُ: <span class="highlight-blue">**هَذِه**</span> (مِثْل: هَذِه تِلْميذَةٌ مُجْتَهِدَةٌ).

=== BLOCK 4: الْمُثَنَّى ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٢. الْمُثَنَّى
Content:
<span class="text-accent">**التَّعْرِيفَ:** هُو كُلّ اِسْمِ دَلٍّ عَلَى اِثْنَينِ أَو اثنتين، بِزِيَادَةِ (<span class="highlight-red">أَلَّفَ وَنَوَّنَ</span>) أَو (<span class="highlight-red">ياء وَنَوْنَ</span>) مَكْسُورَةَ (<span class="highlight-blue">ِ</span>) عَلَى مُفْرَدِهِ.</span>
**أَمِثْلَةَ:**
(Component: TEMPLATE_C_LIST.html) (Nested)
- قَلَمَ: قَلَمِ<span class="highlight-red">**انِ**</span> / قَلَمَ<span class="highlight-red">**يْنِ**</span>.
- شَجَرَةَ: شَجَرَتْ<span class="highlight-red">**انِ**</span> / شَجَرَتْ<span class="highlight-red">**يْنِ**</span>. (تُقَلِّبُ التَّاءُ الْمَرْبُوطَةُ إِلَى مَفْتُوحَةٍ).

=== BLOCK 5: مُلَاحِظَةً الْمُثَنَّى ===
(Component: TEMPLATE_C_BENEFIT.html)
Title: مُلَاحِظَةً
Content:
إِذَا حَذَفَنَا الْألْفُ وَالنُّونُ أَو الياء وَالنُّونَ يَعُودُ الْاِسْمُ مُفْرَدًا كَمَا كَان.

=== BLOCK 6: إِعْرَابَ الْمُثَنَّى ===
(Component: TEMPLATE_C_SPLIT.html)
Logically Right:
(Component: TEMPLATE_C_BLOCK.html)
Title: إِعْرَابَ الْمُثَنَّى (الرَّفْعِ)
Content:
**فِي حَالَةِ الرَّفْعِ:** يُرَفِّعُ بـ <span class="highlight-red">**الْألْفَ**</span>.
مِثَالٌ: التِّلْميذُ<span class="highlight-red">**انِ**</span> مُجْتَهِدَ<span class="highlight-red">**انِ**</span> (مُبْتَدَأٍ وَخَبَرِ مَرْفُوعَانِ بِالْألْفِ).

Logically Left:
(Component: TEMPLATE_C_BLOCK.html)
Title: إِعْرَابَ الْمُثَنَّى (النَّصْبِ وَالْجَرِّ)
Content:
**فِي حَالَةِ النَّصْبِ:** يُنَصِّبُ بـ <span class="highlight-red">**الياء**</span>.
مِثَالٌ: قَابَلْتُ الصَّدِيقَ<span class="highlight-red">**يْنِ**</span> (مَفْعُولٌ بِه مَنْصُوبِ بالياء).
**فِي حَالَةِ الْجَرِّ:** يُجْرِ بـ <span class="highlight-red">**الياء**</span>.
مِثَالٌ: سَلَّمْتُ هِنْدَ عَلَى المعلمت<span class="highlight-red">**يْنِ**</span> (اِسْمَ مَجْرُورَ بالياء).

=== BLOCK 7: الْجَمْعُ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٣. الْجَمْعُ
Content:
<span class="text-accent">**التَّعْرِيفَ:** هُو كُلّ اِسْمِ دَلٍّ عَلَى أَكْثَرِ مِن اِثْنَينِ أَو اثنتين. وَيَنْقَسِمُ إِلَى ثَلَاثَةِ أَنْوَاعٍ:</span>

=== BLOCK 8: أ. جَمَعَ الْمُذَكَّرُ السَّالِمُ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أ. جَمَعَ الْمُذَكَّرُ السَّالِمُ
Content:
<span class="text-accent">هُو مَا دَلٍّ عَلَى أَكْثَرِ مِن اِثْنَينِ (لِلْعُقَلَاءَ الذُّكورَ فَقَط) بِزِيَادَةِ (<span class="highlight-red">واو وَنَوْنَ</span>) أَو (<span class="highlight-red">ياء وَنَوْنَ</span>) مَفْتُوحَةَ (<span class="highlight-blue">َ</span>) عَلَى مُفْرَدِهِ.</span>
**أَمِثْلَةَ:** مُعَلِّمُ: مُعَلِّمُ<span class="highlight-red">**وَنَّ**</span> / مُعَلِّمَ<span class="highlight-red">**يِنَ**</span>.
**الْإِعْرَابَ:**
(Component: TEMPLATE_C_LIST.html) (Nested)
- يُرْفَعُ بـ <span class="highlight-red">**الواو**</span>: الْمُجْتَهِدَ<span class="highlight-red">**وَنَّ**</span> نَاجِحَ<span class="highlight-red">**وَنَّ**</span>.
- يُنْصَبُ بـ <span class="highlight-red">**الياء**</span>: قَابَلْتُ الْمُتَفَوِّقَ<span class="highlight-red">**يِنَ**</span>.
- يُجْرِ بـ <span class="highlight-red">**الياء**</span>: سَلَّمْتُ عَلَى الفائز<span class="highlight-red">**يِنَ**</span>.

=== BLOCK 9: سُمِّيَ سَالِمَا ===
(Component: TEMPLATE_C_BENEFIT.html)
Title: مَعْلُومَةٌ
Content:
سُمِّيَ سَالِمَا لأَنّ حُروفِ الْمُفْرَدِ تُسَلِّمُ مِن التَّغْيِيرِ عِنْد الْجَمْعِ.

=== BLOCK 10: ب. جَمَعَ الْمُؤَنَّثُ السَّالِمُ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ب. جَمَعَ الْمُؤَنَّثُ السَّالِمُ
Content:
<span class="text-accent">هُو مَا دَلٍّ عَلَى أَكْثَرِ مِن اثنتين بِزِيَادَةِ (<span class="highlight-red">أَلَفٌّ وَتَاءُ</span>) عَلَى مُفْرَدِهِ.</span>
**أَمِثْلَةَ:** مُعَلِّمَةُ: مُعَلِّمُ<span class="highlight-red">**ات**</span>، مُهَنْدِسَةَ: مُهَنْدِسَ<span class="highlight-red">**ات**</span>. (تُحْذَفُ التَّاءَ الْمَرْبُوطَةَ وَتُزَادُ أَلَفٌّ وَتَاءُ).
**الْإِعْرَابَ:**
(Component: TEMPLATE_C_LIST.html) (Nested)
- يُرْفَعُ بـ <span class="highlight-red">**الضَّمَّةَ**</span>: الطَّبِيبَاتُ مُخْلِصَاتُ.
- يُنْصَبُ وَيُجَرُّ بـ <span class="highlight-red">**الْكَسْرَةَ**</span>: عَلَّقْتُ اللَّوْحَاتِ (مَفْعُولٌ بِه مَنْصُوبٍ بِالْكَسْرَةِ).

=== BLOCK 11: ج. جَمَعَ التَّكْسيرُ ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ج. جَمَعَ التَّكْسيرُ
Content:
<span class="text-accent">هُو مَا دَلٍّ عَلَى أَكْثَرِ مِن اِثْنَينِ أَو اثنتين، مَع **تَغَيَّرَ وَتَكَسَّرَ صُورَةُ مُفْرَدِهِ** (سَوَاءً بِزِيَادَةِ حُروفٍ، نَقْصَ حُروفٍ، أَو تَغَيُّرُ حَرَكَاتٍ). ولَا يَنْتَهِي بِنِهَايَاتٍ ثَابِتَةٍ.</span>
**أَمِثْلَةَ:** طَالَبَ: طُلَاَّبٌ، طِفْلَ: أَطْفَالٍ، كِتَابَ: كُتُبٍ، أَسَدٌّ: أُسْدِ.
**الْإِعْرَابَ (مِثْل الْمُفْرَدِ تَمَامًا):**
(Component: TEMPLATE_C_LIST.html) (Nested)
- يُرْفَعُ بـ <span class="highlight-red">**الضَّمَّةَ**</span>: حَضَرَ الطُّلَاَّبُ.
- يُنْصَبُ بـ <span class="highlight-red">**الْفَتْحَةَ**</span>: كَتَبُوا الدُّرُوسَ.
- يُجْرِ بـ <span class="highlight-red">**الْكَسْرَةَ**</span>: مِن الْكُتُبِ.

=== BLOCK 12: تَحْذِيرٌ (الْكَلِمَاتِ الْمُخَادِعَةِ) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: اِحْذَرْ مِن الْكَلِمَاتِ الْمُخَادِعَةِ!
Content:
(Component: TEMPLATE_C_LIST.html) (Nested)
- هُنَاك كَلِمَاتٍ تَنْتَهِي بـ (<span class="highlight-red">يِنَ</span>) لَكِنّهَا <span class="text-accent">**جَمَعَ تَكْسيرُ**</span> (لأَنّ مُفْرَدِهَا تَكْسِرُ): مَسَاكِينَ (مُفْرَدَهَا مِسْكِينٌ ولَيْس مُسَّاكِ)، بَسَاتِينَ، شَيَاطِينَ، مَيَادِينَ، قَوَانِينَ، فَنُونٌ.
- هُنَاك كَلِمَاتٍ تَنْتَهِي بـ (<span class="highlight-red">ات</span>) لَكِنّهَا <span class="text-accent">**جَمَعَ تَكْسيرُ**</span> (لأَنّ التَّاءِ أَصِلِيَّةَ): أَصُوَّاتٍ (مُفْرَدَهَا صَوْتَ)، أَوََقَاتٌ، أَبِيَاتٍ.

=== BLOCK 13: جَدْوَلُ إِعْرَابِ الْأَسْمَاءِ ===
(Component: TEMPLATE_C_TABLE.html)
Headers: النَّوْعُ | حَالَةُ الرَّفْعِ | حَالَةُ النَّصْبِ | حَالَةُ الْجَرِّ
Row 1: الْمُفْرَدُ | الضَّمَّةُ | الْفَتْحَةُ | الْكَسْرَةُ
Row 2: الْمُثَنَّى | الْأَلِفُ | الْيَاءُ | الْيَاءُ
Row 3: جَمْعُ الْمُذَكَّرِ السَّالِمِ | الْوَاوُ | الْيَاءُ | الْيَاءُ
Row 4: جَمْعُ الْمُؤَنَّثِ السَّالِمِ | الضَّمَّةُ | الْكَسْرَةُ | الْكَسْرَةُ
Row 5: جَمْعُ التَّكْسِيرِ | الضَّمَّةُ | الْفَتْحَةُ | الْكَسْرَةُ

=== BLOCK 14: السُّؤَالَ الْأَوَّلَ ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: ثَنِّ وَاِجْمَعْ الْكَلِمَاتِ التَّالِيَةِ جَمْعًا مُنَاسِبًا:
<br>١. عَامِلٌ: (الْمُثَنَّى: ..........) (الْجَمْعُ: ..........)
<br>٢. طَالِبَةٌ: (الْمُثَنَّى: ..........) (الْجَمْعُ: ..........)

=== BLOCK 15: السُّؤَالَ الثَّانِي ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٢
Question: حَدَّدَ نَوْعُ الْجَمْعِ فِي الْكَلِمَاتِ الْمُلَوَّنَةِ:
<br>١. يَعْطِفُ الْغَنِيُّ عَلَى <span class="highlight-red">الْمَسَاكِينِ</span>. (نَوْعَ الْجَمْعِ: ............)
<br>٢. <span class="highlight-red">الْمُهَنْدِسُونَ</span> مَاهِرُونَ. (نَوْعُ الْجَمْعِ: ............)
<br>٣. سَمِعْتُ <span class="highlight-red">أصواتاً</span> عَالِيَةً. (نَوْعَ الْجَمْعِ: ............)

=== BLOCK 16: السُّؤَالَ الثَّالِثَ ===
(Component: TEMPLATE_C_EXAM.html)
Number: ٣
Question: أَعْرَبَ الْكَلِمَةُ الْمُلَوَّنَةُ فِي الْجَمَلِ الْآتِيَةِ:
<br>١. قَابَلْتُ <span class="highlight-red">صَدِيقَيْنِ</span> فِي الْمَكْتَبَةِ. (الْإِعْرَابُ: .......................................)
<br>٢. <span class="highlight-red">التِّلْميذَانِ</span> حَاضِرَانِ. (الْإِعْرَابُ: .......................................)
<br>٣. كَرَّمَتْ الْمُدِيرَةُ <span class="highlight-red">الْمُعَلِّمَاتِ</span>. (الْإِعْرَابَ: .......................................)

--- END STREAM ---
