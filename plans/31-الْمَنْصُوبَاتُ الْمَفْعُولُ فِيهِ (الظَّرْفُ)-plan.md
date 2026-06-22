# **SESSION 31.0**

[TASK DEFINITION]
Objective: Implement الْمَنْصُوبَاتُ الْمَفْعُولُ فِيهِ (الظَّرْفُ).
File: `pages/31.0_nXX_الْمَنْصُوبَاتُ الْمَفْعُولُ فِيهِ (الظَّرْفُ).html` (Note: `nXX` must remain exactly as `nXX`. It represents the absolute lesson index and will be replaced later by the system.)
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Page Breaking: Do NOT estimate length manually , instead Use `Jules-workspace/verify_layout.py` after every block to determine exactly where to cut the content to ensure it fits the A4 constraints perfectly. If page is "FULL", continue in `pages/31.1_...` if page have a lot of blank space add exam elements from the lesson.
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
[LESSON_NUMBER]: 31
[CHAPTER_TITLE]: الْمَنْصُوبَاتُ الْمَفْعُولُ فِيهِ (الظَّرْفُ)
[CATEGORY_HEADER]: المستوى المتوسط
[SECTION_HEADER]: علم النحو
[AUTHOR_NAME]: أ. حنا خفيف
[AUTHOR_PHONE]:  

=== BLOCK 2: DEFINITION & RULE ===
(Component: TEMPLATE_C_BLOCK.html)
Title: تَعْرِيفُ الْمَفْعُولِ فِيهِ
Content: <p class="text-accent mb-2mm">هُوَ الزَّمَانُ الَّذِي تَمَّ فِيهِ (حَدَثَ فِيهِ) الْفِعْلُ، أَوِ الْمَكَانُ الَّذِي تَمَّ فِيهِ الْفِعْلُ. وَيُسَمَّى فِي النَّحْوِ (<span class="font-bold highlight-red">ظَرْفاً</span>)، وَهُوَ مِنَ الْمَنْصُوبَاتِ دَائِماً.</p><p class="text-accent mb-0">اِسْمٌ مَنْصُوبٌ يَدُلُّ عَلَى الْفَتْرَةِ الزَّمَنِيَّةِ أَوِ الْمَكَانِيَّةِ الَّتِي حَدَثَ ضِمْنَهَا الْفِعْلُ.</p>

=== BLOCK 3: THE CORE MATRIX ===
(Component: TEMPLATE_C_TABLE.html)
[TABLE_HEADER]: مُلَخَّصُ أَقْسَامِ الظَّرْفِ وَأَلْفَاظِهِ
[TABLE_CONTENT]:
- Column 1 Header: نَوْعُ الظَّرْفِ
- Column 2 Header: أَلْفَاظُهُ الشَّائِعَةُ
- Row 1:
  - Cell 1: <span class="font-bold">ظَرْفُ الزَّمَانِ</span>
  - Cell 2: ثَانِيَةٌ، دَقِيقَةٌ، سَاعَةٌ، يَوْمٌ، أُسْبُوعٌ، شَهْرٌ، سَنَةٌ، عَامٌ، صَبَاحٌ، ظُهْرٌ، عَصْرٌ، مَسَاءٌ، وَقْتٌ، حِينٌ، لَحْظَةٌ، أَبَدٌ، الْيَوْمَ، أَمْسِ، غَداً.
- Row 2:
  - Cell 1: <span class="font-bold">ظَرْفُ الْمَكَانِ</span>
  - Cell 2: فَوْقَ، تَحْتَ، يَمِينَ، شِمَالَ، خَلْفَ، أَمَامَ، وَرَاءَ، جَانِبَ.
- Row 3:
  - Cell 1: <span class="font-bold">الظُّرُوفُ الْمُشْتَرَكَةُ</span>
  - Cell 2: قَبْلَ، بَعْدَ، بَيْنَ، عِنْدَ. (يُخَصِّصُهَا لِأَحَدِهِمَا سِيَاقُ الْجُمْلَةِ وَمَا تُضَافُ إِلَيْهِ).

=== BLOCK 4: DEEP DIVE - Shared Adverbs ===
(Component: TEMPLATE_C_SPLIT.html)
LeftSide:
  (Component: TEMPLATE_C_BLOCK.html)
  Title: مِثَالٌ لِلزَّمَانِ
  Content: <p class="mb-2mm">سَأُقَابِلُكَ <span class="highlight-red font-bold">عِنْدَ</span> الظُّهْرِ.</p> (عِنْدَ: دَلَّتْ عَلَى الزَّمَانِ لِإِضَافَتِهَا إِلَى الظُّهْرِ).
RightSide:
  (Component: TEMPLATE_C_BLOCK.html)
  Title: مِثَالٌ لِلْمَكَانِ
  Content: <p class="mb-2mm">سَأُقَابِلُكَ <span class="highlight-blue font-bold">عِنْدَ</span> بَابِ الْمَدْرَسَةِ.</p> (عِنْدَ: دَلَّتْ عَلَى الْمَكَانِ لِإِضَافَتِهَا إِلَى بَابِ الْمَدْرَسَةِ).

=== BLOCK 5: EXTRA INFO - WARNING ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Title: تَنْبِيهٌ مُهِمٌّ لِلْإِعْرَابِ
Content: <p class="font-bold mb-2mm">لَيْسَتْ كُلُّ هَذِهِ الْكَلِمَاتِ تُعْرَبُ ظَرْفاً دَائِماً!</p><p>الْأَجْدَرُ بِكَ لِفَهْمِ دَرْسِ الْمَفْعُولِ فِيهِ لَيْسَ الِانْشِغَالَ بِحِفْظِ الْأَسْمَاءِ، وَإِنَّمَا الِانْتِبَاهُ إِلَى عَلَاقَةِ هَذِهِ الْأَسْمَاءِ بِالْفِعْلِ (يَجِبُ أَنْ تَتَضَمَّنَ مَعْنَى "فِي"):</p>
(Component: TEMPLATE_C_LIST.html)
- [LIST_ITEM_CONTENT]: إِذَا حَدَّدَتْ زَمَانَ أَوْ مَكَانَ حُدُوثِ الْفِعْلِ (يُمْكِنُكَ أَنْ تَضَعَ قَبْلَهَا كَلِمَةَ "فِي" وَيَصِحَّ الْمَعْنَى) ← <span class="highlight-red font-bold">مَفْعُولٌ فِيهِ</span> (ظَرْفُ زَمَانٍ/مَكَانٍ مَنْصُوبٌ).
- [LIST_ITEM_CONTENT]: إِذَا لَمْ تُحَدِّدِ الزَّمَانَ/الْمَكَانَ (أَيْ كَانَتْ هِيَ الْفَاعِلُ أَوْ نَتَحَدَّثُ عَنْهَا بِذَاتِهَا) ← <span class="highlight-blue font-bold">تُعْرَبُ حَسَبَ مَوْقِعِهَا</span> (فَاعِلٌ، مَفْعُولٌ بِهِ، مُبْتَدَأٌ...).

=== BLOCK 6: DEEP DIVE - Examples to Distinguish ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَمْثِلَةٌ تَوْضِيحِيَّةٌ هَامَّةٌ جِدّاً لِلتَّفْرِيقِ
Content:
(Component: TEMPLATE_C_LIST.html)
- [LIST_ITEM_CONTENT]: ١. تَجَوَّلْتُ فِي الْحَدِيقَةِ <span class="highlight-red font-bold">سَاعَةً</span>. (أَيْ تَجَوَّلْتُ فِي الْحَدِيقَةِ "فِي مُدَّةِ" سَاعَةٍ. دَلَّتْ عَلَى الزَّمَنِ ← <span class="font-bold">مَفْعُولٌ فِيهِ ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ</span>).
- [LIST_ITEM_CONTENT]: ٢. اشْتَرَيْتُ <span class="highlight-blue font-bold">سَاعَةً</span> جَدِيدَةً. (هُنَا وَقَعَ عَلَيْهَا فِعْلُ الشِّرَاءِ، وَلَا تَعْنِي أَنِّي اشْتَرَيْتُ "فِي زَمَانِ السَّاعَةِ" ← <span class="font-bold">إِذَنْ هِيَ مَفْعُولٌ بِهِ مَنْصُوبٌ</span>).
- [LIST_ITEM_CONTENT]: ٣. جَاءَتْ <span class="highlight-green font-bold">سَاعَةُ</span> الْفَرَحِ. (السَّاعَةُ هِيَ الَّتِي قَامَتْ بِفِعْلِ الْمَجِيءِ، وَهِيَ الْفَاعِلُ ← <span class="font-bold">إِذَنْ هِيَ فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ</span>).
- [LIST_ITEM_CONTENT]: ٤. <span class="highlight-red font-bold">يَوْمُ</span> الْعُطْلَةِ <span class="highlight-blue font-bold">يَوْمٌ</span> جَمِيلٌ. (<span class="highlight-red">يَوْمُ</span> الْأُولَى: مُبْتَدَأٌ، <span class="highlight-blue">يَوْمٌ</span> الثَّانِيَةُ: خَبَرٌ. لِأَنَّنَا نَتَحَدَّثُ عَنِ الْيَوْمِ ذَاتِهِ وَلَيْسَ عَنْ فِعْلٍ حَدَثَ فِيهِ).

=== BLOCK 7: EXTRA INFO - TIP ===
(Component: TEMPLATE_C_BENEFIT_TIP.html)
Title: إِضَافَةٌ مُفِيدَةٌ (الْقَاعِدَةُ)
Content: كُلُّ اسْمٍ يَأْتِي بَعْدَ ظَرْفِ الْمَكَانِ غَيْرِ الْمُنَوَّنِ يُعْرَبُ مُضَافاً إِلَيْهِ.

=== BLOCK 8: DEEP DIVE - Applied Examples ===
(Component: TEMPLATE_C_BLOCK.html)
Title: أَمْثِلَةٌ تَطْبِيقِيَّةٌ مُكَثَّفَةٌ (الْمَفْعُولُ فِيهِ)
Content:
(Component: TEMPLATE_C_LIST.html)
- [LIST_ITEM_CONTENT]: ١. يَظْهَرُ الْقَمَرُ <span class="highlight-red font-bold">مَسَاءً</span>. (مَسَاءً: ظَرْفُ زَمَانٍ مَنْصُوبٌ).
- [LIST_ITEM_CONTENT]: ٢. انْتَظَرْتُ صَدِيقِي <span class="highlight-blue font-bold">عِنْدَ</span> بَابِ الْمَدْرَسَةِ. (عِنْدَ: ظَرْفُ مَكَانٍ مَنْصُوبٌ).
- [LIST_ITEM_CONTENT]: ٣. لَا تُغَادِرُ النَّمْلَةُ مَسْكَنَهَا <span class="highlight-red font-bold">شِتَاءً</span>. (شِتَاءً: ظَرْفُ زَمَانٍ مَنْصُوبٌ).
- [LIST_ITEM_CONTENT]: ٤. بَقِيتُ فِي دِمَشْقَ <span class="highlight-blue font-bold">شَهْرَيْنِ</span>. (شَهْرَيْنِ: ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُثَنَّى).
- [LIST_ITEM_CONTENT]: ٥. قَفَزَ الْحِصَانُ <span class="highlight-red font-bold">فَوْقَ</span> الْحَاجِزِ. (فَوْقَ: ظَرْفُ مَكَانٍ مَنْصُوبٌ).
- [LIST_ITEM_CONTENT]: ٦. اسْتَيْقَظْتُ <span class="highlight-blue font-bold">قَبْلَ</span> طُلُوعِ الشَّمْسِ. (قَبْلَ: ظَرْفُ زَمَانٍ مَنْصُوبٌ).
- [LIST_ITEM_CONTENT]: ٧. وَقَفْتُ <span class="highlight-red font-bold">لَحْظَةً</span> <span class="highlight-blue font-bold">أَمَامَ</span> الْمِرْآةِ. (لَحْظَةً: ظَرْفُ زَمَانٍ، أَمَامَ: ظَرْفُ مَكَانٍ).
- [LIST_ITEM_CONTENT]: ٨. تَجْمَعُ النَّمْلَةُ الْقَمْحَ <span class="highlight-red font-bold">صَيْفاً</span>. (صَيْفاً: ظَرْفُ زَمَانٍ مَنْصُوبٌ).

=== BLOCK 9: EVIDENCE (Parsing) ===
(Component: TEMPLATE_C_BLOCK.html)
Title: نَمُوذَجُ إِعْرَابٍ (الْمَفْعُولُ فِيهِ)
Content:
<p class="font-bold text-center mb-2mm">"وَقَفْتُ أَمَامَ الْمِرْآةِ"</p>
(Component: TEMPLATE_C_IRAB.html)
- Word 1: وَقَفْتُ
- Details 1: فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.
- Word 2: أَمَامَ
- Details 2: <span class="highlight-red font-bold">مَفْعُولٌ فِيهِ (ظَرْفُ مَكَانٍ) مَنْصُوبٌ</span> وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ عَلَى آخِرِهِ، وَهُوَ مُضَافٌ.
- Word 3: الْمِرْآةِ
- Details 3: <span class="highlight-blue font-bold">مُضَافٌ إِلَيْهِ مَجْرُورٌ</span> وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ الظَّاهِرَةُ عَلَى آخِرِهِ.

<p class="font-bold text-center mt-4mm mb-2mm">"سَافَرَ أَبِي صَبَاحاً"</p>
(Component: TEMPLATE_C_IRAB.html)
- Word 1: سَافَرَ
- Details 1: فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ الظَّاهِرِ عَلَى آخِرِهِ.
- Word 2: أَبِي
- Details 2: فَاعِلٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الْمُقَدَّرَةُ عَلَى مَا قَبْلِ الْيَاءِ (يَاءِ الْمُتَكَلِّمِ)، وَهُوَ مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.
- Word 3: صَبَاحاً
- Details 3: <span class="highlight-red font-bold">مَفْعُولٌ فِيهِ (ظَرْفُ زَمَانٍ) مَنْصُوبٌ</span> وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ عَلَى آخِرِهِ.

=== BLOCK 10: EVALUATION ===
(Component: TEMPLATE_C_EXAM.html)
Number: ١
Question: اسْتَخْرِجِ الْمَفْعُولَ فِيهِ (الظَّرْفَ) وَبَيِّنْ نَوْعَهُ (زَمَانٌ أَوْ مَكَانٌ) فِي الْجُمَلِ الْآتِيَةِ: ١. اخْتَبَأَ الطِّفْلُ خَلْفَ الْبَابِ. ٢. سَأَزُورُكَ غَداً. ٣. يَقَعُ مَنْزِلُنَا جَانِبَ الْمَسْجِدِ. ٤. نَمْتُ عَصْراً.

--- END STREAM ---