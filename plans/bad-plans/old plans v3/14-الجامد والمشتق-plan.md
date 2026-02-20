# **SESSION 14.0**

[TASK DEFINITION]
Objective: Implement the introductory page for Lesson 14: "الجامد والمشتق" (Rigid and Derived Nouns).
File: `pages/14.0_n33_aljamid_walmushtaq.html`
Reference: Follow patterns in design_patterns.json and existing morphological lessons (e.g., Chapter 01).

[CONSTRAINTS & PROTOCOLS]
1. Page Breaking: Use `tools/verify_layout.py` after every block. If "FULL", continue the content in `pages/14.1_...`.
2. Content: 100% Arabic with full Harakat. No English.
3. Highlighting: Use `.highlight-red` for the core grammatical focus (derived endings/morphemes) and `.highlight-blue` for standard examples.
4. Definitions: Every definition must use the `.text-accent` class within a `TEMPLATE_C_BLOCK`.
5. Numerals: Use Arabic-Indic digits (١، ٢، ٣، ٤...) for all visible numbering.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER)
Title: الجَامِدُ وَالمُشْتَقُّ
Lesson: ١٤
Author: إِبْرَاهِيم أَبُو مُحَمَّد

=== BLOCK 2: Definition of Rigid vs Derived ===
(Component: TEMPLATE_C_BLOCK)
Title: تَعْرِيفُ الجَامِدِ وَالمُشْتَقِّ
Content: أَسْمَاءُ العَرَبِيَّةِ نَوْعَانِ: <span class="text-accent">جَامِدَةٌ وَمُشْتَقَّةٌ</span>. فَالِاسْمُ <span class="highlight-blue">الجَامِدُ</span> هُوَ الَّذِي <span class="highlight-red">لَا يُؤْخَذُ</span> مِنْ غَيْرِهِ، أَمَّا الِاسْمُ <span class="highlight-blue">المُشْتَقُّ</span> فَهُوَ الَّذِي <span class="highlight-red">يُؤْخَذُ</span> مِنْ غَيْرِهِ.

=== BLOCK 3: Rigid Nouns (Types) ===
(Component: TEMPLATE_C_SPLIT)
Left_Title: جَامِدُ الذَّاتِ
Left_Content: هُوَ الَّذِي <span class="text-accent">يُدْرَكُ بِإِحْدَى الحَوَاسِّ الخَمْسِ</span>.<br>مِثْلُ: (شَجَرَة، كُرْسِيّ، قَلَم، رَجُل).
Right_Title: جَامِدُ المَعْنَى (المَصْدَر)
Right_Content: هُوَ الَّذِي <span class="text-accent">يُدْرَكُ بِالعَقْلِ</span>، وَمِنْهُ تُؤْخَذُ الأَفْعَالُ وَالمُشْتَقَّاتُ.<br>مِثْلُ: (نَجَاح، أَمَل، رَغْبَة).

=== BLOCK 4: List of Derived Nouns ===
(Component: TEMPLATE_C_LIST)
Title: الأَسْمَاءُ المُشْتَقَّةُ
List_Items: 
- اسْمُ الفَاعِلِ.
- مُبَالَغَةُ اسْمِ الفَاعِلِ.
- اسْمُ المَفْعُولِ.
- الصِّفَةُ المُشَبَّهَةُ بِاسْمِ الفَاعِلِ.
- اسْمُ الآلَةِ.
- اسْمَا المَكَانِ وَالزَّمَانِ.
- اسْمُ التَّفْضِيلِ.

=== BLOCK 5: Ism al-Fa'il (Definition & Formulation) ===
(Component: TEMPLATE_C_BLOCK)
Title: ١- اسْمُ الفَاعِلِ
Content: اسْمٌ يَدُلُّ عَلَى <span class="text-accent">مَنْ قَامَ بِالفِعْلِ</span>. يُصَاغُ عَلَى النَّحْوِ الآتِي:

=== BLOCK 6: Formulation Table ===
(Component: TEMPLATE_C_TABLE)
Header: الفِعْلُ | الصِّيَاغَةُ | المِثَالُ
Rows:
- الثُّلَاثِيُّ | عَلَى وَزْنِ <span class="highlight-red">فَاعِل</span> | كَتَبَ ← <span class="highlight-blue">كَاتِب</span>
- فَوْقَ الثُّلَاثِيِّ | مِيمٌ مَضْمُومَةٌ وَكَسْرُ مَا قَبْلَ الآخِرِ | كَرَّمَ ← <span class="highlight-blue">مُكَرِّم</span>

=== BLOCK 7: Work of Ism al-Fa'il ===
(Component: TEMPLATE_C_BENEFIT)
Title: عَمَلُ اسْمِ الفَاعِلِ
Content: قَدْ يَعْمَلُ اسْمُ الفَاعِلِ عَمَلَ فِعْلِهِ، فَيَرْفَعُ <span class="highlight-red">فَاعِلًا</span> (جَاءَ الضَّاحِكُ <span class="highlight-blue">سِنُّهُ</span>)، أَوْ يَنْصِبُ <span class="highlight-red">مَفْعُولًا بِهِ</span> (جَاءَ نَاكِسًا <span class="highlight-blue">رَأْسَهُ</span>)، وَذَلِكَ إِذَا كَانَ مُنَوَّنًا أَوْ مُعَرَّفًا بِـ (ال).

=== BLOCK 8: Exam ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: حَدِّدِ الِاسْمَ الجَامِدَ وَالمُشْتَقَّ فِيمَا يَأْتِي: (قَلَمٌ، نَجَاحٌ، قَارِئٌ، مُسْتَخْرِجٌ).

--- END STREAM ---