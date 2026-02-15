# **SESSION 13.0**

[TASK DEFINITION]
Objective: Implement Lesson 13 (الإعلال).
File: `pages/13.0_n28_ilal.html`
Reference: Follow patterns in `BOOK_RULES.md`.

[CONSTRAINTS & PROTOCOLS]
1. Page Breaking: Use `tools/verify_layout.py` after every major block. If the status is 'FULL' or 'OVERFLOW', close the current file (e.g., `13.0_...`) and move the remaining content to the next sequential file (e.g., `13.1_...`).
2. Content: 100% Arabic with full Harakat. Preserve all diacritics from the source text.
3. Highlighting: Use `.highlight-red` for primary focus words (the words undergoing Il'al) and `.highlight-blue` for secondary elements if applicable.
4. Definitions: Must use `.text-accent` class for the main definition text.
5. IDs: Use `tools/id_manager.py` to generate unique IDs for all blocks (Header, Block, List, Exam, etc.).
6. Templates: Use `TEMPLATE_C_LIST` for lists instead of generic `<ul>` where possible.
7. Exam: Mandatory at the end of the lesson.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER)
Title: الإِعْلَالُ
Lesson: ١٣
Author: إِبْرَاهِيم أَبُو مُحَمَّد

=== BLOCK 2: Definition ===
(Component: TEMPLATE_C_BLOCK)
Title: تَعْرِيفُ الإِعْلَالِ
Content: <p class="text-accent">تَغْيِيرٌ يُصِيبُ حَرْفَ الْعِلَّةِ، وَلَهُ ثَلَاثَةُ أَنْوَاعٍ: الإِعْلَالُ بِالتَّسْكِينِ، وَالإِعْلَالُ بِالْحَذْفِ، وَالإِعْلَالُ بِالْقَلْبِ.</p>

=== BLOCK 3: Summary Matrix ===
(Component: TEMPLATE_C_TABLE)
Title: أَنْوَاعُ الإِعْلَالِ
Columns: النَّوْعُ | التَّعْرِيفُ | مِثَالٌ
Row 1: الإِعْلَالُ بِالتَّسْكِينِ | تَسْكِينُ حَرْفِ الْعِلَّةِ (الْوَاوِ أَوِ الْيَاءِ) لِثِقَلِ الْحَرَكَةِ. | يَسْمُو، يَمْشِي
Row 2: الإِعْلَالُ بِالْحَذْفِ | حَذْفُ حَرْفِ الْعِلَّةِ لِعِلَّةٍ صَرْفِيَّةٍ أَوْ الْتِقَاءِ سَاكِنَيْنِ. | قُلْ، يَرِثُ
Row 3: الإِعْلَالُ بِالْقَلْبِ | قَلْبُ حَرْفِ الْعِلَّةِ إِلَى حَرْفٍ آخَرَ (أَلِفٍ، وَاوٍ، يَاءٍ). | قَالَ، بَاعَ

=== BLOCK 4: I'lal bi-Taskin ===
(Component: TEMPLATE_C_LIST)
Title: أَوَّلاً- الإِعْلَالُ بِالتَّسْكِينِ
Intro: تَسْكِينُ أَحَدِ حَرْفَيِ الْعِلَّةِ (الْوَاو أَوِ الْيَاء)، لِأَنَّ الْأَلِفَ دَائِماً سَاكِنَةٌ. وَيَكُونُ ذَلِكَ فِي حَالَتَيْنِ:
Items:
1. إذا وقعَ حرفُ الواوِ، أو حرفُ الياءِ في لامِ الكلمةِ (آخِرِ الكلمةِ) مسبوقينِ بضمٍّ أو بكسرٍ. نحو: (<span class="highlight-red">يَسْمُوُ</span>، <span class="highlight-red">يَمْشِيُ</span>).
2. إذا وقعَ حرفُ الواوِ أو حرفُ الياءِ في عينِ الكلمةِ (وسطِ الكلمةِ) متحركينِ مسبوقينِ بحرفٍ صحيحٍ ساكنٍ. نحو: (<span class="highlight-red">يَقُوْمُ</span>؛ أصلُها: يَقْوُمُ)، و(<span class="highlight-red">يَبِيْنُ</span>؛ أصلُها: يَبْيِنُ).

=== BLOCK 5: I'lal bi-Hadhf (Part 1: Mithal & Ajwaf) ===
(Component: TEMPLATE_C_LIST)
Title: ثانياً - الإِعْلَالُ بِالْحَذْفِ
Intro: هُوَ حَذْفُ حَرْفِ الْعِلَّةِ. وَيَتِمُّ فِي الْمَوَاضِعِ الْآتِيَةِ:
Items:
1. <strong>في أوَّلِ الكلمةِ (المثالُ):</strong> في المضارع والأمر. نحو: (<span class="highlight-red">يَرِثُ</span>، <span class="highlight-red">زِنْ</span>).
2. <strong>في وسطِ الكلمةِ (الأجوفُ):</strong> عند التقاء الساكنين. نحو: (<span class="highlight-red">قُلْ</span>).

=== BLOCK 6: I'lal bi-Hadhf (Part 2: Naqis) ===
(Component: TEMPLATE_C_LIST)
Title: تَابِعُ الإِعْلَالِ بِالْحَذْفِ (النَّاقِصُ)
Intro: فِي آخِرِ الكلمةِ (الفعلُ المعتلُّ الناقصُ):
Items:
1. آخِرِ المضارعِ المجزومِ: <span class="highlight-red">لَمْ يَمْشِ</span> (حُذِفتِ الياءُ).
2. آخِرِ أمرِ المفردِ المذكَّرِ: <span class="highlight-red">اسعَ</span> (حُذِفتِ الألفُ).
3. آخِرِ الماضي المتصل بـ(تاء التأنيث) أو (واو الجماعة): <span class="highlight-red">مَشَتْ</span>، <span class="highlight-red">دَعَوْا</span>.

=== BLOCK 7: I'lal bi-Qalb (Part 1: To Alif) ===
(Component: TEMPLATE_C_LIST)
Title: ثالِثاً - الإِعْلَالُ بِالْقَلْبِ
Intro: ١- قَلْبُ الواوِ أو الياءِ ألفاً (إذا تحرَّكتا وانفتحَ ما قبلهما):
Items:
1. <span class="highlight-red">قالَ</span> (أصلُها قَوَلَ).
2. <span class="highlight-red">باعَ</span> (أصلُها بَيَعَ).
3. <span class="highlight-red">سَمَا</span> (أصلُها سَمَوَ).
4. <span class="highlight-red">جَرَى</span> (أصلُها جَرَيَ).

=== BLOCK 8: I'lal bi-Qalb (Part 2: Waw to Ya) ===
(Component: TEMPLATE_C_LIST)
Title: تَابِعُ الإِعْلَالِ بِالْقَلْبِ
Intro: ٢- قَلْبُ الواوِ ياءً:
Items:
1. تطرَّفَتْ بعدَ كسرٍ: <span class="highlight-red">رَضِيَ</span>، <span class="highlight-red">قَوِيَ</span>.
2. وقَعَتْ حشواً بينَ كسرةٍ وألفٍ: <span class="highlight-red">قِيامٌ</span>، <span class="highlight-red">صِيامٌ</span>.
3. سُكِّنَتْ بعدَ كسرٍ: <span class="highlight-red">ميزانٌ</span>، <span class="highlight-red">ميعادٌ</span>.
4. اجتمعَتِ الواوُ والياءُ وسُبِقَتْ إحداهما بالسكون: <span class="highlight-red">سيِّدٌ</span>، <span class="highlight-red">ميِّتٌ</span>.

=== BLOCK 9: I'lal bi-Qalb (Part 3: Ya to Waw) ===
(Component: TEMPLATE_C_LIST)
Title: تَابِعُ الإِعْلَالِ بِالْقَلْبِ
Intro: ٣- قَلْبُ الياءِ واواً (إذا سكنت الياء بعد ضم):
Items:
1. <span class="highlight-red">مُوقِن</span> (أصلها مُيْقِن).
2. <span class="highlight-red">مُوسِر</span> (أصلها مُيْسِر).

=== BLOCK 10: Exam ===
(Component: TEMPLATE_C_EXAM)
Title: 📝 اخْتَبِرْ نَفْسَكَ (الإِعْلَالُ)
Question 1: بَيِّنْ نَوْعَ الإِعْلَالِ فِي كَلِمَةِ (يَقُولُ) وَأَصْلَهَا.
Question 2: لِمَ حُذِفَتِ الْوَاوُ فِي كَلِمَةِ (يَثِقُ)؟
Question 3: مَا أَصْلُ كَلِمَةِ (مِيزَان) وَمَاذَا حَدَثَ فِيهَا مِن إِعْلَالٍ؟

--- END STREAM ---
