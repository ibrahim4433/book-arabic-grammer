# **SESSION 64.0**

[TASK DEFINITION]
Objective: Implement الْمُحَسِّنَاتُ الْبَدِيعِيَّةُ (زِينَةُ الْكَلَامِ).
File: `pages/64.0_nXX_الْمُحَسِّنَاتُ الْبَدِيعِيَّةُ (زِينَةُ الْكَلَامِ).html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/64.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 64
[CHAPTER_TITLE]: الْمُحَسِّنَاتُ الْبَدِيعِيَّةُ (زِينَةُ الْكَلَامِ)
[CATEGORY_HEADER]: المستوى المتقدم
[SECTION_HEADER]: علم البلاغة
[AUTHOR_NAME]: أ. حنا خفيف
[AUTHOR_PHONE]:  

=== BLOCK 2: Definition Block ===
(Component: TEMPLATE_C_BLOCK.html)
Title: عِلمُ البَديعِ
Content: <p class="text-accent mt-1mm">هُوَ عِلْمٌ يَهْتَمُّ بِزَخْرَفَةِ الْكَلَامِ وَتَجْمِيلِهِ بَعْدَ إِيصَالِ الْمَعْنَى.</p><p>وَيُقْسَمُ إِلَى <span class="highlight-blue">مُحَسِّنَاتٍ لَفْظِيَّةٍ</span> (تُجَمِّلُ الصَّوْتَ)، وَ<span class="highlight-blue">مُحَسِّنَاتٍ مَعْنَوِيَّةٍ</span> (تُعْمِقُ الْمَعْنَى).</p>

=== BLOCK 3: The Core Matrix ===
(Component: TEMPLATE_C_TABLE.html)
Title: مُلَخَّصُ أَقْسَامِ عِلْمِ الْبَدِيعِ
Headers: النَّوْعُ | التَّعْرِيفُ | أَمْثِلَةٌ مِنَ الْمُحَسِّنَاتِ
Row 1: الْمُحَسِّنَاتُ اللَّفْظِيَّةُ | تُجَمِّلُ الصَّوْتَ | الْجِنَاسُ، التَّصْرِيعُ، السَّجْعُ
Row 2: الْمُحَسِّنَاتُ الْمَعْنَوِيَّةُ | تُعْمِقُ الْمَعْنَى | الطِّبَاقُ، الْمُقَابَلَةُ

=== BLOCK 4: First Section Header & First Type ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَوَّلًا: الْمُحَسِّنَاتُ اللَّفْظِيَّةُ (زِينَةُ الصَّوْتِ)
Content: <p class="text-accent mt-1mm">١. الْجِنَاسُ (تَشَابُهُ الْكَلِمَتَيْنِ): كَلِمَتَانِ تَتَشَابَهَانِ فِي الْحُرُوفِ (مُوسِيقَى جَمِيلَةٌ) وَتَخْتَلِفَانِ فِي الْمَعْنَى. وَلَهُ نَوْعَانِ:</p>
(Inject TEMPLATE_C_LIST.html inside this block body)
List Items:
- <strong>جِنَاسٌ تَامٌّ (تَطَابُقٌ ١٠٠٪):</strong> فِي النَّوْعِ، وَالْعَدَدِ، وَالتَّشْكِيلِ، وَالتَّرْتِيبِ.<br>مِثَالٌ: شَاهَدْتُ (<span class="highlight-red">الْمَغْرِبَ</span>) فِي دَوْلَةِ (<span class="highlight-red">الْمَغْرِبِ</span>).
- <strong>جِنَاسٌ نَاقِصٌ (اخْتِلَافٌ بَسِيطٌ):</strong> اخْتِلَافٌ فِي حَرْفٍ، أَوْ حَرَكَةٍ.<br>مِثَالٌ: (<span class="highlight-blue">عَالِم</span>، <span class="highlight-blue">ظَالِم</span>) اخْتِلَافٌ فِي الْحَرْفِ. (<span class="highlight-blue">عِبْرَة</span>، <span class="highlight-blue">عَبرَة</span>) اخْتِلَافٌ فِي التَّشْكِيلِ. (<span class="highlight-blue">صَفَائِح</span>، <span class="highlight-blue">صَحَائِف</span>) اخْتِلَافٌ فِي التَّرْتِيبِ.

=== BLOCK 5: Benefit Box ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Content:  قِيمَتُهُ الْفَنِّيَّةُ: يَمْنَحُ الْكَلَامَ إِيقَاعًا مُوسِيقِيًّا عَذْبًا يَطْرَبُ لَهُ الْأُذُنُ، وَيَلْفِتُ الِانْتِبَاهَ لِلْمَعْنَى.

=== BLOCK 6: Second Type ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٢. التَّصْرِيعُ (خَاصٌّ بِالشِّعْرِ)
Content: <p class="text-accent mt-1mm">اتِّفَاقُ الْحَرْفِ الْأَخِيرِ مِنَ الشَّطْرِ الْأَوَّلِ مَعَ الْحَرْفِ الْأَخِيرِ مِنَ الشَّطْرِ الثَّانِي (وَيَكُونُ غَالِبًا فِي الْبَيْتِ الْأَوَّلِ لِلْقَصِيدَةِ).</p>

=== BLOCK 7: Poem Example ===
(Component: TEMPLATE_C_POEM.html followed by TEMPLATE_C_IRAB_ROW.html)
Poem lines:
Hemistich 1: سَكَتُّ فَغَرَّ أَعْدَائِي السُّكُوتُ
Hemistich 2: وَظَنُّونِي لِأَهْلِي قَدْ نَسِيتُ
Irab Row:
- Word 1: السُّكُوتُ / نَسِيتُ
- Details 1: تَصْرِيعٌ لِاتِّفَاقِ الْحَرْفِ الْأَخِيرِ (التَّاء) فِي نِهَايَةِ الشَّطْرَيْنِ.

=== BLOCK 8: Third Type ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٣. السَّجْعُ (خَاصٌّ بِالنَّثْرِ)
Content: <p class="text-accent mt-1mm">تَوَافُقُ الْحُرُوفِ الْأَخِيرَةِ فِي نِهَايَاتِ الْجُمَلِ (فَوَاصِلِ الْفِقْرَةِ).</p>
<p>مِثَالٌ: النَّجَاحُ هَدَفٌ <span class="highlight-red">مَشْرُوعٌ</span> ، وَتَخْطِيطٌ <span class="highlight-red">مَتْبُوعٌ</span> ، وَعَمَلٌ <span class="highlight-red">مَصْنُوعٌ</span> .</p>

=== BLOCK 9: Second Section Header & Types of Meaning ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ثَانِيًا: الْمُحَسِّنَاتُ الْمَعْنَوِيَّةُ (زِينَةُ الْمَعْنَى وَالتَّضَادُّ)
Content: <p class="text-accent mt-1mm">١. الطِّبَاقُ (الْكَلِمَةُ وَعَكْسُهَا): يَجْمَعُ بَيْنَ كَلِمَةٍ وَضِدِّهَا فِي نَفْسِ الْجُمْلَةِ لِيُبْرِزَ الْمَعْنَى (بِالضِّدِّ تَتَمَيَّزُ الْأَشْيَاءُ). لَهُ نَوْعَانِ:</p>
(Inject TEMPLATE_C_LIST.html inside this block body)
List Items:
- <strong>طِبَاقُ إِيجَابٍ (كَلِمَتَانِ مُخْتَلِفَتَانِ):</strong> <span class="highlight-green">كَبِير</span> وَ<span class="highlight-green">صَغِير</span>. <span class="highlight-green">طَوِيل</span> وَ<span class="highlight-green">قَصِير</span>. <span class="highlight-green">نَاجِح</span> وَ<span class="highlight-green">رَاسِب</span>.
- <strong>طِبَاقُ سَلْبٍ (نَفْسُ الْكَلِمَةِ مَعَ نَفْيِهَا):</strong> <span class="highlight-green">يَجْتَهِدُونَ</span> وَ<span class="highlight-green">لَا يَجْتَهِدُونَ</span>. <span class="highlight-green">اقْرَأْ</span> وَ<span class="highlight-green">لَا تَقْرَأْ</span>.

=== BLOCK 10: Fourth Type (Al-Muqabalah) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: ٢. الْمُقَابَلَةُ (جُمْلَةٌ عَكْسُ جُمْلَةٍ)
Content: <p class="text-accent mt-1mm">الْإِتْيَانُ بِمَعْنَيَيْنِ (أَوْ كَلِمَتَيْنِ) عَلَى الْأَقَلِّ، ثُمَّ الْإِتْيَانُ بِمَا يُضَادُّهُمَا عَلَى التَّرْتِيبِ فِي الْجُمْلَةِ التَّالِيَةِ.</p>
<p>مِثَالٌ: (<span class="highlight-red">يُقَدِّمُ</span> <span class="highlight-blue">لَهُمُ</span> <span class="highlight-green">النَّافِعَ</span>) وَ (<span class="highlight-red">يَمْنَعُ</span> <span class="highlight-blue">عَنْهُمُ</span> <span class="highlight-green">الضَّارَّ</span>).</p>
<p>يُقَدِّمُ عَكْس يَمْنَعُ. لَهُم عَكْس عَنْهُم. النَّافِعَ عَكْس الضَّارَّ.</p>

=== BLOCK 11: Benefit Box (Orange/Warning to ensure color balance) ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content:  قِيمَتُهُمَا الْفَنِّيَّةُ: إِظْهَارُ الْمَعْنَى بِجَلَاءٍ وَوُضُوحٍ (مِنْ خِلَالِ التَّضَادِّ)، وَإِثَارَةُ خَيَالِ الْمُتَلَقِّي، وَإِعْمَالُ الْعَقْلِ فِي الْمُتَنَاقِضَاتِ.

=== BLOCK 12: Exam ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: مَا الْفَرْقُ بَيْنَ الْمُحَسِّنَاتِ اللَّفْظِيَّةِ وَالْمَعْنَوِيَّةِ مَعَ ذِكْرِ مِثَالٍ لِكُلٍّ مِنْهُمَا؟

--- END STREAM ---