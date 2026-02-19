# **SESSION 09.0**

[TASK DEFINITION]
Objective: Implement Lesson 14 - The Solid and The Derived (الجامد والمشتق).
File: `pages/14.0_nxx_jamid_mushtaq.html`
Reference: Follow patterns in `design_patterns.json` and `BOOK_RULES.md`.

[CONSTRAINTS & PROTOCOLS]
1.  **Page Breaking:** Use `python3 "Jules workspace/verify_layout.py"` after every major block. If the status is "FULL" or "OVERFLOW", close the current file (e.g., `09.0_...`) and move the remaining content to the next sequential file (e.g., `09.1_...`).
2.  **Content:** 100% Arabic with full Harakat. Preserve ALL diacritics.
3.  **Highlighting:** Use `.highlight-red` for primary focus words and `.highlight-blue` for secondary focus.
4.  **Definitions:** Must use `.text-accent` class for the main definition text.
5.  **Tables:** Use `TEMPLATE_C_TABLE` for lists of weights/forms.
6.  **Comparison:** Use `TEMPLATE_C_SPLIT` for comparing similar concepts.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER)
Title: الجَامِدُ وَالمُشْتَقُّ
Lesson: ٩


=== BLOCK 2: Definition of Jamid and Mushtaq ===
(Component: TEMPLATE_C_BLOCK)
Title: تَعْرِيفُ الجَامِدِ وَالمُشْتَقِّ
Content:
<p class="text-accent">أَسْمَاءُ العَرَبِيَّةِ نَوْعَانِ: جَامِدَةٌ وَمُشْتَقَّةٌ. وَالاسْمُ الجَامِدُ هُوَ الاسْمُ الَّذِي لَا يُؤْخَذُ مِنْ غَيْرِهِ، أَمَّا الاسْمُ المُشْتَقُّ فَهُوَ الاسْمُ الَّذِي يُؤْخَذُ مِنْ غَيْرِهِ.</p>

<!-- VERIFY_LAYOUT -->

=== BLOCK 3: Types of Jamid (Solid Nouns) ===
(Component: TEMPLATE_C_SPLIT)
Title: أَقْسَامُ الاسْمِ الجَامِدِ
Left Content (Ma'na):
<h4 class="text-accent">ب- الاسْمُ الجَامِدُ المَعْنَى</h4>
<p>وَهُوَ الاسْمُ الَّذِي يُدْرَكُ بِالعَقْلِ، وَيُسَمَّى <span class="highlight-red">المَصْدَرُ</span>، وَمِنْهُ تُؤْخَذُ الأَفْعَالُ وَالأَسْمَاءُ المُشْتَقَّةُ.</p>
<p><strong>مِثْلُ:</strong> (نَجَاح، أَمَل).</p>
Right Content (Dhat):
<h4 class="text-accent">أ- الاسْمُ الجَامِدُ الذَّاتِ</h4>
<p>وَهُوَ الاسْمُ الَّذِي يُدْرَكُ بِإِحْدَى الحَوَاسِّ الخَمْسِ.</p>
<p><strong>مِثْلُ:</strong> (شَجَرَة، كُرْسِيّ، قَلَم، ...).</p>

<!-- VERIFY_LAYOUT -->

=== BLOCK 4: Types of Mushtaq (Derived Nouns) ===
(Component: TEMPLATE_C_BLOCK)
Title: الأَسْمَاءُ المُشْتَقَّةُ
Content:
<p>وَهِيَ:</p>
<div class="chips-container">
    <span class="chip">اسْمُ الفَاعِلِ</span>
    <span class="chip">مُبَالَغَةُ اسْمِ الفَاعِلِ</span>
    <span class="chip">اسْمُ المَفْعُولِ</span>
    <span class="chip">الصِّفَةُ المُشَبَّهَةُ بِاسْمِ الفَاعِلِ</span>
    <span class="chip">اسْمُ الآلَةِ</span>
    <span class="chip">اسْمُ المَكَانِ</span>
    <span class="chip">اسْمُ الزَّمَانِ</span>
    <span class="chip">اسْمُ التَّفْضِيلِ</span>
</div>
<p class="mt-2mm">وَإِلَيْكَ عَرْضُ هَذِهِ المُشْتَقَّاتِ:</p>

<!-- VERIFY_LAYOUT -->

=== BLOCK 5: Ism Fa'il (Active Participle) ===
(Component: TEMPLATE_C_BLOCK)
Title: ١- اسْمُ الفَاعِلِ
Content:
<p class="text-accent">اسْمٌ يَدُلُّ عَلَى مَنْ قَامَ بِالفِعْلِ.</p>
<ul class="structured-list">
    <li>
        <span class="list-icon">١</span>
        <div class="list-item-content">
            <strong>مِنَ الفِعْلِ الثُّلَاثِيِّ:</strong> يُصَاغُ عَلَى وَزْنِ <span class="highlight-red">فَاعِل</span>.
            <br>مِثْلُ: (كَتَبَ ⇐ <span class="highlight-red">كَاتِب</span>).
        </div>
    </li>
    <li>
        <span class="list-icon">٢</span>
        <div class="list-item-content">
            <strong>مِنَ الفِعْلِ فَوْقَ الثُّلَاثِيِّ:</strong> عَلَى وَزْنِ مُضَارِعِهِ بِإِبْدَالِ حَرْفِ المُضَارَعَةِ مِيمًا مَضْمُومَةً وَكَسْرِ الحَرْفِ الَّذِي قَبْلَ آخِرِهِ.
            <br>مِثْلُ: (كَرَّمَ ⇐ <span class="highlight-red">مُكَرِّم</span>).
        </div>
    </li>
</ul>
<div class="benefit-box mt-4mm">
    <strong>عَمَلُ اسْمِ الفَاعِلِ:</strong>
    <p>قَدْ يَعْمَلُ اسْمُ الفَاعِلِ عَمَلَ الفِعْلِ الَّذِي أُخِذَ مِنْهُ:</p>
    <ul class="dense-list">
        <li>إِنْ كَانَ لَازِمًا رَفَعَ فَاعِلًا: (جَاءَ <span class="highlight-red">الضَّاحِكُ</span> سِنُّهُ).</li>
        <li>إِنْ كَانَ مُتَعَدِّيًا نَصَبَ مَفْعُولًا بِهِ: (جَاءَ <span class="highlight-red">نَاكِسًا</span> رَأْسَهُ).</li>
    </ul>
    <p class="text-sm text-grey">يَعْمَلُ عِنْدَمَا يَكُونُ مُنَوَّنًا أَوْ مُعَرَّفًا بِـ (ال).</p>
</div>

<!-- VERIFY_LAYOUT -->

=== BLOCK 6: Mubalaghat Ism Fa'il (Hyperbole) ===
(Component: TEMPLATE_C_BLOCK)
Title: ٢- مُبَالَغَةُ اسْمِ الفَاعِلِ
Content:
<p class="text-accent">اسْمٌ يَدُلُّ عَلَى اسْمِ الفَاعِلِ فِي حَالِ المُبَالَغَةِ وَالإِكْثَارِ مِنَ القِيَامِ بِالفِعْلِ.</p>
<p>تُصَاغُ مِنَ الفِعْلِ الثُّلَاثِيِّ المُتَعَدِّي، (وَقَدْ تُصَاغُ مِنْ اللَّازِمِ عَلَى وَزْنِ فَعَّال مِثْلَ ضَحَّاك). وَأَوْزَانُهَا:</p>
<table class="dense-table w-100pct mt-2mm">
    <thead>
        <tr>
            <th>الوَزْن</th>
            <th>المِثَال</th>
        </tr>
    </thead>
    <tbody>
        <tr><td><span class="highlight-red">فَعَّال</span></td><td>جَلَّاد</td></tr>
        <tr><td><span class="highlight-red">فَعَّالَة</span></td><td>عَلَّامَة</td></tr>
        <tr><td><span class="highlight-red">مِفْعَال</span></td><td>مِعْطَاء</td></tr>
        <tr><td><span class="highlight-red">فَعُول</span></td><td>أَكُول</td></tr>
        <tr><td><span class="highlight-red">فَعِيل</span></td><td>رَحِيم</td></tr>
    </tbody>
</table>
<div class="benefit-box mt-2mm">
    <strong>عَمَلُهَا:</strong> تَعْمَلُ عَمَلَ اسْمِ الفَاعِلِ (رَفْعُ فَاعِلٍ وَنَصْبُ مَفْعُولٍ). مِثْلُ: (جَاءَ <span class="highlight-red">الضَّحَّاكُ</span> سِنُّهُ)، (جَاءَ <span class="highlight-red">الذَّكَّارُ</span> رَبَّهُ).
</div>

<!-- VERIFY_LAYOUT -->

=== BLOCK 7: Ism Maf'ul (Passive Participle) ===
(Component: TEMPLATE_C_BLOCK)
Title: ٣- اسْمُ المَفْعُولِ
Content:
<p class="text-accent">اسْمٌ يَدُلُّ عَلَى مَنْ وَقَعَ عَلَيْهِ الفِعْلُ.</p>
<ul class="structured-list">
    <li>
        <span class="list-icon">١</span>
        <div class="list-item-content">
            <strong>مِنَ الفِعْلِ الثُّلَاثِيِّ (المَبْنِيِّ لِلمَجْهُولِ):</strong> عَلَى وَزْنِ <span class="highlight-red">مَفْعُول</span>.
            <br>مِثْلُ: (كُتِبَ ⇐ <span class="highlight-red">مَكْتُوب</span>).
        </div>
    </li>
    <li>
        <span class="list-icon">٢</span>
        <div class="list-item-content">
            <strong>مِنَ الفِعْلِ فَوْقَ الثُّلَاثِيِّ:</strong> عَلَى وَزْنِ مُضَارِعِهِ المَبْنِيِّ لِلمَجْهُولِ بِإِبْدَالِ حَرْفِ المُضَارَعَةِ مِيمًا مَضْمُومَةً وَفَتْحِ مَا قَبْلَ آخِرِهِ.
            <br>مِثْلُ: (اسْتُخْرِجَ ⇐ <span class="highlight-red">مُسْتَخْرَج</span>).
        </div>
    </li>
</ul>
<div class="benefit-box mt-2mm">
    <strong>عَمَلُهُ:</strong> يَعْمَلُ عَمَلَ فِعْلِهِ المَبْنِيِّ لِلمَجْهُولِ، فَيَرْفَعُ نَائِبَ فَاعِلٍ. مِثْلُ: (الأَبُ <span class="highlight-red">مَشْكُورٌ</span> فَضْلُهُ).
</div>

<!-- VERIFY_LAYOUT -->

=== BLOCK 8: Sifah Mushabbahah (Adjective) ===
(Component: TEMPLATE_C_BLOCK)
Title: ٤- الصِّفَةُ المُشَبَّهَةُ بِاسْمِ الفَاعِلِ
Content:
<p class="text-accent">اسْمٌ يُشْتَقُّ مِنَ المَصْدَرِ لِيَدُلَّ عَلَى صِفَةٍ ثَابِتَةٍ فِي المَوْصُوفِ.</p>
<p>تُصَاغُ مِنَ الفِعْلِ الثُّلَاثِيِّ اللَّازِمِ عَلَى الأَوْزَانِ الآتِيَةِ:</p>
<div class="chips-container">
    <span class="chip">فَعِيل (كَرِيم)</span>
    <span class="chip">فُعَال (شُجَاع)</span>
    <span class="chip">فَعَال (جَبَان)</span>
    <span class="chip">فَعِل (بَطِل)</span>
    <span class="chip">فَعْل (فَرْح)</span>
    <span class="chip">فِعْل (شِهْم)</span>
    <span class="chip">فُعْل (صُلْب)</span>
</div>
<p class="mt-2mm"><strong>وَمَا دَلَّ عَلَى لَوْنٍ أَوْ عَيْبٍ أَوْ حِلْيَةٍ:</strong> عَلَى وَزْنِ <span class="highlight-red">أَفْعَل</span> (مُؤَنَّثُهُ فَعْلَاء).</p>
<p>مِثْلُ: (أَحْمَر/حَمْرَاء - أَعْرَج/عَرْجَاء - أَحْوَر/حَوْرَاء).</p>
<div class="benefit-box mt-2mm">
    <strong>عَمَلُهَا:</strong> تَعْمَلُ عَمَلَ فِعْلِهَا، فَتَرْفَعُ فَاعِلًا. مِثْلُ: (الطَّبِيبُ <span class="highlight-red">عَظِيمٌ</span> دَوْرُهُ).
</div>

<!-- VERIFY_LAYOUT -->

=== BLOCK 9: Ism Al-Alah (Instrument) ===
(Component: TEMPLATE_C_BLOCK)
Title: ٥- اسْمُ الآلَةِ
Content:
<p class="text-accent">اسْمٌ يَدُلُّ عَلَى آلَةِ حُدُوثِ الفِعْلِ.</p>
<p>يُصَاغُ غَالِبًا مِنَ الفِعْلِ الثُّلَاثِيِّ المُتَعَدِّي عَلَى الأَوْزَانِ:</p>
<table class="dense-table w-100pct">
    <thead>
        <tr>
            <th>الوَزْن</th>
            <th>المِثَال</th>
        </tr>
    </thead>
    <tbody>
        <tr><td><span class="highlight-red">مِفْعَل</span></td><td>مِثْقَب</td></tr>
        <tr><td><span class="highlight-red">مِفْعَال</span></td><td>مِصْبَاح</td></tr>
        <tr><td><span class="highlight-red">مِفْعَلَة</span></td><td>مِرْوَحَة</td></tr>
        <tr><td><span class="highlight-red">فَعَّال</span></td><td>بَرَّاد</td></tr>
        <tr><td><span class="highlight-red">فَعَّالَة</span></td><td>غَسَّالَة</td></tr>
    </tbody>
</table>

<!-- VERIFY_LAYOUT -->

=== BLOCK 10: Ism Zaman & Makan (Time/Place) ===
(Component: TEMPLATE_C_BLOCK)
Title: ٦- اسْمُ المَكَانِ وَاسْمُ الزَّمَانِ
Content:
<p class="text-accent">اسْمَانِ يُشْتَقَّانِ مِنَ المَصْدَرِ لِلدَّلَالَةِ عَلَى مَكَانِ أَوْ زَمَانِ حُدُوثِ الفِعْلِ.</p>
<p>يُفَرَّقُ بَيْنَهُمَا بِالسِّيَاقِ:</p>
<ul class="dense-list">
    <li><strong>مَكَان:</strong> مَبْدَأُ السِّبَاقِ سَاحَةُ الجَامِعَةِ.</li>
    <li><strong>زَمَان:</strong> مَبْدَأُ السِّبَاقِ السَّاعَةَ العَاشِرَةَ.</li>
</ul>

<h4 class="mt-3mm mb-2mm text-accent font-bold">صِيَاغَتُهُمَا:</h4>
<div class="split-grid">
    <div class="content-block">
        <div class="block-header text-sm">مِنَ الثُّلَاثِيِّ</div>
        <div class="block-body">
            <ul class="structured-list">
                <li>
                    <span class="highlight-red">مَفْعَل</span> (بِفَتْحِ العَيْنِ):
                    <br>- إِذَا كَانَ مُضَارِعُهُ مَفْتُوحَ العَيْنِ (يَسْبَح ⇐ <span class="highlight-red">مَسْبَح</span>).
                    <br>- إِذَا كَانَ مُضَارِعُهُ مَضْمُومَ العَيْنِ (يَدْخُل ⇐ <span class="highlight-red">مَدْخَل</span>).
                    <br>- إِذَا كَانَ مُعْتَلَّ الآخِرِ (يَلْهَى ⇐ <span class="highlight-red">مَلْهَى</span>).
                </li>
                <li>
                    <span class="highlight-red">مَفْعِل</span> (بِكَسْرِ العَيْنِ):
                    <br>- إِذَا كَانَ مُضَارِعُهُ مَكْسُورَ العَيْنِ (يَعْرِض ⇐ <span class="highlight-red">مَعْرِض</span>).
                    <br>- إِذَا كَانَ مُعْتَلَّ الفَاءِ صَحِيحَ اللَّامِ (وَقَفَ ⇐ <span class="highlight-red">مَوْقِف</span>).
                </li>
            </ul>
        </div>
    </div>
    <div class="content-block">
        <div class="block-header text-sm">مِنْ فَوْقِ الثُّلَاثِيِّ</div>
        <div class="block-body">
            <p>كَمَا يُصَاغُ <strong>اسْمُ المَفْعُولِ</strong> (مِيمٌ مَضْمُومَةٌ وَفَتْحُ مَا قَبْلَ الآخِرِ).</p>
            <p>مِثْلُ: (اجْتَمَعَ ⇐ <span class="highlight-red">مُجْتَمَع</span>).</p>
            <p>(انْتَدَى ⇐ <span class="highlight-red">مُنْتَدَى</span>).</p>
        </div>
    </div>
</div>

<!-- VERIFY_LAYOUT -->

=== BLOCK 11: Ism Tafdil (Elative) ===
(Component: TEMPLATE_C_BLOCK)
Title: ٧- اسْمُ التَّفْضِيلِ
Content:
<p class="text-accent">اسْمٌ يَدُلُّ عَلَى أَنَّ شَيْئَيْنِ اشْتَرَكَا فِي صِفَةٍ وَزَادَ أَحَدُهُمَا عَلَى الآخَرِ فِيهَا.</p>
<p>يُصَاغُ عَلَى وَزْنِ <span class="highlight-red">أَفْعَل</span> (لِلْمُذَكَّرِ) وَ <span class="highlight-red">فُعْلَى</span> (لِلْمُؤَنَّثِ) بِشُرُوطٍ سَبْعَةٍ:</p>
<div class="chips-container">
    <span class="chip">ثُلَاثِيًّا</span>
    <span class="chip">تَامًّا</span>
    <span class="chip">مُثْبَتًا</span>
    <span class="chip">مُتَصَرِّفًا</span>
    <span class="chip">مَبْنِيًّا لِلْمَعْلُومِ</span>
    <span class="chip">قَابِلًا لِلتَّفَاوُتِ</span>
    <span class="chip">لَيْسَتْ صِفَتُهُ (أَفْعَل-فَعْلَاء)</span>
</div>
<p class="mt-2mm">مِثْلُ: (أَنْفَع، أَفْضَل).</p>
<div class="benefit-box mt-2mm">
    <strong>إِذَا لَمْ يَسْتَوْفِ الشُّرُوطَ:</strong>
    <p>نَأْتِي بِاسْمٍ مُنَاسِبٍ (أَشَدُّ، أَكْثَرُ...) ثُمَّ نَأْتِي بِمَصْدَرِ الفِعْلِ مَنْصُوبًا عَلَى التَّمْيِيزِ.</p>
    <p>مِثْلُ: (الصِّدْقُ <span class="highlight-red">أَشَدُّ تَأْثِيرًا</span> مِنَ الكَذِبِ).</p>
    <p class="text-sm text-grey">لَا يُصَاغُ مُطْلَقًا مِنَ الجَامِدِ (نِعْمَ، بِئْسَ) وَغَيْرِ القَابِلِ لِلتَّفَاوُتِ (مَاتَ، عَمِيَ).</p>
</div>

<!-- VERIFY_LAYOUT -->

=== BLOCK 12: Applied Examples 1-4 ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: حَدِّدِ التَّصْنِيفَ الصَّحِيحَ: (رَجُلٌ - رَغْبَةٌ - قَوِيٌّ).
Answer: (رَجُلٌ): جَامِدُ ذَاتٍ. (رَغْبَةٌ): جَامِدُ مَعْنًى. (قَوِيٌّ): مُشْتَقٌّ.

=== BLOCK 13: Applied Examples 5-8 ===
(Component: TEMPLATE_C_EXAM)
Number: ٥
Question: بَيِّنِ المَعَانِيَ لِلْجِذْرِ (غَزَلَ): (المَغْزُولُ، المِغْزَلُ، المَغْزِلُ، الغَزَّالُ).
Answer: المَغْزُولُ (مَفْعُول). المِغْزَلُ (آلَة). المَغْزِلُ (مَكَان). الغَزَّالُ (مُبَالَغَة).

=== BLOCK 14: Applied Examples 9-10 ===
(Component: TEMPLATE_C_EXAM)
Number: ٩
Question: بَيِّنْ نَوْعَ كُلٍّ مِنَ المُشْتَقَّاتِ الآتِيَةِ: (مَقَام - مُتَحَرِّك - وَقْع - فَصَاح - مِنْقَار).
Answer: مَقَام: مَكَان. مُتَحَرِّك: فَاعِل. وَقْع: فَاعِل (أَوْ مَصْدَر). فَصَاح: صِفَة مُشَبَّهَة. مِنْقَار: آلَة.

=== BLOCK 15: Applied Examples 11-12 ===
(Component: TEMPLATE_C_EXAM)
Number: ١١
Question: عَلِّلْ: (عَمِيق) صِفَة مُشَبَّهَة، وَ(عَلِيم) صِيغَة مُبَالَغَة، رَغْمَ أَنَّهُمَا عَلَى وَزْنِ (فَعِيل)؟
Answer: عَمِيق فِعْلُهَا لَازِم (عَمُقَ) فَلَا تُصَاغُ فَاعِل (عَامِق). عَلِيم فِعْلُهَا مُتَعَدٍّ (عَلِمَ) فَتُصَاغُ فَاعِل (عَالِم).

=== BLOCK 16: Applied Examples 13-14 ===
(Component: TEMPLATE_C_EXAM)
Number: ١٣
Question: حَدِّدْ نَوْعَ المُشْتَقَّاتِ: (أَزْهَد، حَرِيص، مُرَاقِب، جَبَان).
Answer: أَزْهَد: تَفْضِيل. حَرِيص: صِفَة. مُرَاقِب: فَاعِل. جَبَان: صِفَة.

<!-- VERIFY_LAYOUT -->

=== BLOCK 17: Masadir (Sources) Intro ===
(Component: TEMPLATE_C_BLOCK)
Title: ٨- المَصَادِرُ
Content:
<p class="text-accent">المَصْدَرُ اسْمٌ يَدُلُّ عَلَى الحَدَثِ مُجَرَّدًا مِنَ الزَّمَنِ.</p>
<p>هُوَ الأَصْلُ الَّذِي تَصْدُرُ عَنْهُ الأَفْعَالُ وَالمُشْتَقَّاتُ.</p>

<h4 class="text-accent font-bold mt-3mm">أَوَّلًا: المَصَادِرُ السَّمَاعِيَّةُ (الثُّلَاثِيَّة)</h4>
<p>مَصَادِرُ الأَفْعَالِ الثُّلَاثِيَّةِ سَمَاعِيَّةٌ تُعْرَفُ بِالرُّجُوعِ إِلَى المُعْجَمَاتِ.</p>
<div class="chips-container">
    <span class="chip">شَرِبَ ⇐ شُرْب</span>
    <span class="chip">ذَهَبَ ⇐ ذَهَاب</span>
    <span class="chip">رَحِمَ ⇐ رَحْمَة</span>
    <span class="chip">طَافَ ⇐ طَوَفَان</span>
</div>

<!-- VERIFY_LAYOUT -->

=== BLOCK 18: Masadir Qiyasiyyah Table ===
(Component: TEMPLATE_C_TABLE)
Title: ثَانِيًا: المَصَادِرُ القِيَاسِيَّةُ (الرُّبَاعِيَّة)
Columns: وَزْنُ الفِعْلِ, وَزْنُ المَصْدَرِ, مِثَال
Rows:
فَعَّلَ | تَفْعِيل | عَلَّمَ ⇐ تَعْلِيم
أَفْعَلَ | إِفْعَال | أَقْبَلَ ⇐ إِقْبَال
فَاعَلَ | مُفَاعَلَة | شَارَكَ ⇐ مُشَارَكَة
فَعْلَلَ | فَعْلَلَة | زَلْزَلَ ⇐ زَلْزَلَة

=== BLOCK 19: Masadir Quint/Hex Table ===
(Component: TEMPLATE_C_BLOCK)
Title: مَصَادِرُ الخُمَاسِيِّ وَالسُّدَاسِيِّ
Content:
<ul class="structured-list">
    <li>
        <span class="list-icon">١</span>
        <div class="list-item-content">
            <strong>مَبْدُوءٌ بِهَمْزَةِ وَصْلٍ:</strong> نَضَعُ أَلِفًا قَبْلَ الآخِرِ.
            <br>(اعْتَمَدَ ⇐ <span class="highlight-red">اعْتِمَاد</span>)، (اسْتَقْبَلَ ⇐ <span class="highlight-red">اسْتِقْبَال</span>).
        </div>
    </li>
    <li>
        <span class="list-icon">٢</span>
        <div class="list-item-content">
            <strong>مَبْدُوءٌ بِتَاءٍ:</strong> نَضَعُ ضَمَّةً قَبْلَ الآخِرِ.
            <br>(تَدَافَعَ ⇐ <span class="highlight-red">تَدَافُع</span>)، (تَقَدَّمَ ⇐ <span class="highlight-red">تَقَدُّم</span>).
        </div>
    </li>
</ul>

<!-- VERIFY_LAYOUT -->

=== BLOCK 20: Special Cases (Masadir) ===
(Component: TEMPLATE_C_BLOCK)
Title: حَالَاتٌ خَاصَّةٌ
Content:
<ul class="dense-list">
    <li>(فَاعَلَ) قَدْ يَأْتِي عَلَى <span class="highlight-red">فِعَال</span>: (قَاتَلَ ⇐ قِتَال).</li>
    <li>(فَعَّلَ) مُعْتَلُّ الآخِرِ/مَهْمُوزٌ يَأْتِي عَلَى <span class="highlight-red">تَفْعِلَة</span>: (رَبَّى ⇐ تَرْبِيَة).</li>
    <li>خُمَاسِيٌّ مَبْدُوءٌ بِتَاءٍ مُعْتَلُّ الآخِرِ: تُقْلَبُ الأَلِفُ يَاءً (تَمَادَى ⇐ تَمَادِي).</li>
    <li>رُبَاعِيٌّ/سُدَاسِيٌّ قَبْلَ آخِرِهِ أَلِفٌ: تُزَادُ تَاءٌ مَرْبُوطَةٌ (أَفَادَ ⇐ إِفَادَة).</li>
</ul>
<div class="benefit-box mt-2mm">
    <strong>عَمَلُ المَصْدَرِ:</strong> يَعْمَلُ عَمَلَ فِعْلِهِ، فَيَرْفَعُ فَاعِلًا (نَادِرًا) وَيَنْصِبُ مَفْعُولًا بِهِ.
    <br>مِثْلُ: (إِطْعَامُكَ <span class="highlight-blue">اليَتِيمَ</span> شَرَفٌ).
</div>

<!-- VERIFY_LAYOUT -->

=== BLOCK 21: Masdar Mimi & Sina'i ===
(Component: TEMPLATE_C_SPLIT)
Title: المَصْدَرُ المِيمِيُّ وَالصِّنَاعِيُّ
Left Content (Sina'i):
<h4 class="text-accent">المَصْدَرُ الصِّنَاعِيُّ</h4>
<p>اسْمٌ لَحِقَتْهُ يَاءُ النِّسْبَةِ وَتَاءُ التَّأْنِيثِ (يَّة) لِلدَّلَالَةِ عَلَى مَعْنَى المَصْدَرِ.</p>
<p>مِثْلُ: (وَطَنِيَّة، حُرِّيَّة).</p>
<p class="text-sm text-grey">يَجِبُ أَلَّا يَكُونَ صِفَةً لِمَا قَبْلَهُ (وَإِلَّا كَانَ اسْمًا مَنْسُوبًا).</p>
Right Content (Mimi):
<h4 class="text-accent">المَصْدَرُ المِيمِيُّ</h4>
<p>مَصْدَرٌ مَبْدُوءٌ بِمِيمٍ زَائِدَةٍ.</p>
<p>وَزْنُهُ كَاسْمِ الزَّمَانِ وَالمَكَانِ، وَيُفَرَّقُ بِالسِّيَاقِ.</p>
<p>مِثْلُ: (مَوْقِف).</p>

<!-- VERIFY_LAYOUT -->

=== BLOCK 22: Masdar Mu'awwal ===
(Component: TEMPLATE_C_BLOCK)
Title: المَصْدَرُ المُؤَوَّلُ
Content:
<p>تَرْكِيبٌ يَتَكَوَّنُ مِنْ حَرْفٍ مَصْدَرِيٍّ وَصِلَتِهِ، يُمْكِنُ تَأْوِيلُهُ بِمَصْدَرٍ صَرِيحٍ.</p>
<h4 class="text-sm font-bold mt-2mm">أَشْكَالُهُ:</h4>
<div class="chips-container">
    <span class="chip">أَنْ + الفِعْل (أَرَادَ أَنْ يَقُولَ)</span>
    <span class="chip">أَنَّ + اسْمُهَا وَخَبَرُهَا (عَلِمْتُ أَنَّكَ نَاجِحٌ)</span>
    <span class="chip">مَا + الفِعْل (انْهَضْ كَمَا نَهَضَ)</span>
</div>

<!-- VERIFY_LAYOUT -->

=== BLOCK 23: Masdar Examples (Q&A) 1-5 ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: هَاتِ مَصْدَرَ كُلٍّ مِنَ الأَفْعَالِ: (هَدَّمْتُ، وَارَى، اكْفَهَرَّ، يَتَجَلَّى، يُبْدِعُ، تَعَاطَى).
Answer: تَهْدِيم - مُوَارَاة - اكْفِهْرَار - تَجَلِّي - إِبْدَاع - تَعَاطِي.

<!-- VERIFY_LAYOUT -->

=== BLOCK 24: Nisbah (Attribution) ===
(Component: TEMPLATE_C_BLOCK)
Title: ٩- النِّسْبَةُ
Content:
<p class="text-accent">إِضَافَةُ يَاءٍ مُشَدَّدَةٍ مَسْبُوقَةٍ بِكَسْرٍ إِلَى آخِرِ الِاسْمِ.</p>
<table class="dense-table w-100pct mt-2mm">
    <thead>
        <tr>
            <th>النوع</th>
            <th>القاعدة</th>
            <th>مثال</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>مَخْتُوم بِتَاء</td><td>تُحْذَفُ التَّاء</td><td>مَكَّة ⇐ مَكِّيّ</td></tr>
        <tr><td>مَقْصُور (ألفه 3)</td><td>تُقْلَبُ وَاوًا</td><td>فَتَى ⇐ فَتَوِيّ</td></tr>
        <tr><td>مَمْدُود (همزة تأنيث)</td><td>تُقْلَبُ وَاوًا</td><td>صَحْرَاء ⇐ صَحْرَاوِيّ</td></tr>
    </tbody>
</table>

<!-- VERIFY_LAYOUT -->

=== BLOCK 25: Manqous, Maqsour, Mamdoud ===
(Component: TEMPLATE_C_SPLIT)
Title: المَنْقُوصُ، المَقْصُورُ، المَمْدُودُ
Left Content (Maqsour/Mamdoud):
<h4 class="text-accent">المَقْصُورُ</h4>
<p>آخِرُهُ أَلِفٌ لَازِمَةٌ (فَتَى).</p>
<p class="text-sm">- تُقَدَّرُ الحَرَكَاتُ.</p>
<h4 class="text-accent mt-2mm">المَمْدُودُ</h4>
<p>آخِرُهُ هَمْزَةٌ بَعْدَ أَلِفٍ زَائِدَةٍ (بِنَاء).</p>
Right Content (Manqous):
<h4 class="text-accent">المَنْقُوصُ</h4>
<p>آخِرُهُ يَاءٌ لَازِمَةٌ مَكْسُورٌ مَا قَبْلَهَا (القَاضِي).</p>
<ul class="dense-list text-sm">
    <li>تُحْذَفُ يَاؤُهُ إِذَا كَانَ نَكِرَةً مَرْفُوعَةً أَوْ مَجْرُورَةً (جَاءَ قَاضٍ).</li>
    <li>تَبْقَى إِذَا كَانَ مُعَرَّفًا أَوْ مَنْصُوبًا.</li>
</ul>

<!-- VERIFY_LAYOUT -->

=== BLOCK 26: Sarf Exams ===
(Component: TEMPLATE_C_EXAM)
Number: س
Question: أَسْئِلَةُ الدَّوْرَاتِ (٢٠١٣-٢٠١٤): العِلَّةُ الصَّرْفِيَّةُ فِي (يَسْقِي)؟ وَزْنُ (شَفَيْتُم)؟
Answer: إِعْلَالٌ بِالتَّسْكِينِ. - فَعَلْتُم.

<!-- VERIFY_LAYOUT -->

=== BLOCK 27: Imla' (Spelling) - Hamza ===
(Component: TEMPLATE_C_BLOCK)
Title: ٣- الإِمْلَاءُ (الهَمْزَةُ)
Content:
<h4 class="text-accent font-bold">١- الهَمْزَةُ الأَوَّلِيَّةُ</h4>
<div class="split-grid">
    <div class="content-block">
        <div class="block-header text-sm">القَطْع (أَ/إِ)</div>
        <div class="block-body">
            <p>مَاضِي الرُّبَاعِيِّ وَأَمْرُهُ وَمَصْدَرُهُ (أَقْبَلَ).</p>
            <p>جَمِيعُ الحُرُوفِ (إِنَّ).</p>
        </div>
    </div>
    <div class="content-block">
        <div class="block-header text-sm">الوَصْل (ا)</div>
        <div class="block-body">
            <p>أَمْرُ الثُّلَاثِيِّ (اُكْتُبْ).</p>
            <p>مَاضِي الخُمَاسِيِّ وَالسُّدَاسِيِّ (اسْتَقْبَلَ).</p>
            <p>الأَسْمَاءُ العَشَرَةُ (ابْن، اسْم).</p>
        </div>
    </div>
</div>

<h4 class="text-accent font-bold mt-4mm">٢- الهَمْزَةُ المُتَوَسِّطَةُ</h4>
<p>نُقَارِنُ بَيْنَ حَرَكَتِهَا وَحَرَكَةِ مَا قَبْلَهَا (الأَقْوَى: كَسْرَة > ضَمَّة > فَتْحَة > سُكُون).</p>
<div class="chips-container">
    <span class="chip">لِئَن (كَسْرَة)</span>
    <span class="chip">بُؤْس (ضَمَّة)</span>
    <span class="chip">سَأَل (فَتْحَة)</span>
</div>

<h4 class="text-accent font-bold mt-4mm">٣- الهَمْزَةُ المُتَطَرِّفَةُ</h4>
<p>تُكْتَبُ حَسَبَ حَرَكَةِ الحَرْفِ الَّذِي قَبْلَهَا فَقَطْ.</p>
<div class="chips-container">
    <span class="chip">يُومِئ (كَسْر)</span>
    <span class="chip">تَبَاطُؤ (ضَمّ)</span>
    <span class="chip">مَبْدَأ (فَتْح)</span>
    <span class="chip">دِفْء (سُكُون)</span>
</div>

<!-- VERIFY_LAYOUT -->

=== BLOCK 28: Alif Layyina ===
(Component: TEMPLATE_C_TABLE)
Title: الأَلِفُ اللَّيِّنَةُ
Columns: المَوْقِع, الحَالَة, الرَّسْم
Rows:
ثُلَاثِيّ | أَصْلُهَا وَاو | مَمْدُودَة (دَنَا)
ثُلَاثِيّ | أَصْلُهَا يَاء | مَقْصُورَة (سَقَى)
فَوْقَ ثُلَاثِيّ | سُبِقَتْ بِيَاء | مَمْدُودَة (دُنْيَا)
فَوْقَ ثُلَاثِيّ | لَمْ تُسْبَقْ بِيَاء | مَقْصُورَة (مُصْطَفَى)

=== BLOCK 29: Ta' Marbouta & Mabsouta ===
(Component: TEMPLATE_C_SPLIT)
Title: التَّاءُ المَبْسُوطَةُ وَالمَرْبُوطَةُ
Left Content (Marbouta):
<h4 class="text-accent">التَّاءُ المَرْبُوطَةُ (ة)</h4>
<p>تُلْفَظُ هَاءً عِنْدَ الوَقْفِ.</p>
<ul class="dense-list">
    <li>مُفْرَد مُؤَنَّث (شَجَرَة).</li>
    <li>جَمْع تَكْسِير لَيْسَ فِي مُفْرَدِهِ تَاء (قُضَاة).</li>
</ul>
Right Content (Mabsouta):
<h4 class="text-accent">التَّاءُ المَبْسُوطَةُ (ت)</h4>
<p>تُلْفَظُ تَاءً دَائِمًا.</p>
<ul class="dense-list">
    <li>تَاءُ التَّأْنِيثِ/الرَّفْعِ.</li>
    <li>أَصْلِيَّة (بَيْت).</li>
    <li>جَمْع مُؤَنَّث سَالِم (مُؤْمِنَات).</li>
</ul>

<!-- VERIFY_LAYOUT -->

=== BLOCK 30: Hamzat Inna & Ziyadah/Hadhf ===
(Component: TEMPLATE_C_BLOCK)
Title: هَمْزَةُ إِنَّ وَمَوَاطِنُ الزِّيَادَةِ وَالحَذْفِ
Content:
<h4 class="text-accent font-bold">كَسْرُ هَمْزَةِ إِنَّ:</h4>
<div class="chips-container">
    <span class="chip">بِدَايَة الكَلَام</span>
    <span class="chip">بَعْدَ القَوْل</span>
    <span class="chip">بَعْدَ القَسَم</span>
    <span class="chip">اللَّام المُزَحْلَقَة</span>
</div>

<h4 class="text-accent font-bold mt-3mm">الزِّيَادَةُ وَالحَذْفُ:</h4>
<ul class="dense-list">
    <li><strong>زِيَادَةُ الأَلِفِ:</strong> بَعْدَ وَاوِ الجَمَاعَةِ (سَافَرُوا)، تَنْوِين النَّصْب (شَابًّا).</li>
    <li><strong>حَذْفُ الأَلِفِ:</strong> (الله، الرَّحْمَن، إِلَه، لَكِنْ، هَؤُلَاءِ).</li>
    <li><strong>حَذْفُ النُّونِ:</strong> مِنْ/عَنْ + مَا/مَنْ ⇐ (مِمَّنْ، عَمَّ).</li>
</ul>

<!-- VERIFY_LAYOUT -->

=== BLOCK 31: Fasl, Wasl & Punctuation ===
(Component: TEMPLATE_C_BLOCK)
Title: الفَصْلُ وَالوَصْلُ وَالتَّرْقِيمُ
Content:
<h4 class="text-accent font-bold">الفَصْلُ وَالوَصْلُ:</h4>
<ul class="dense-list">
    <li><strong>تُوصَلُ (مَا):</strong> مَعَ (إِنَّ، أَيْنَ، كُلَّ) ⇐ (إِنَّمَا، أَيْنَمَا، كُلَّمَا).</li>
    <li><strong>تُوصَلُ (لَا):</strong> مَعَ (أَنْ) النَّاصِبَة ⇐ (أَلَّا).</li>
</ul>

<h4 class="text-accent font-bold mt-3mm">عَلَامَاتُ التَّرْقِيمِ:</h4>
<div class="chips-container">
    <span class="chip">. (النِّهَايَة)</span>
    <span class="chip">: (القَوْل/التَّفْصِيل)</span>
    <span class="chip">، (الفَصْل)</span>
    <span class="chip">؛ (السَّبَبِيَّة)</span>
    <span class="chip">! (التَّعَجُّب)</span>
    <span class="chip">؟ (السُّؤَال)</span>
</div>

<!-- VERIFY_LAYOUT -->

=== BLOCK 32: Imla' Examples 1-5 ===
(Component: TEMPLATE_C_EXAM)
Number: ١
Question: عَلِّلْ كِتَابَةَ الهَمْزَةِ: (أَدْرَكَ، سُؤَال، نَشْئًا، انْطَفِئْ، أَزْعُمُ).
Answer: أَدْرَكَ (قَطْع رُبَاعِيّ). سُؤَال (مُتَوَسِّطَة سَاكِنَة بَعْدَ ضَمّ). نَشْئًا (مُتَطَرِّفَة بَعْدَ سَاكِن مُتَّصِل). انْطَفِئْ (مُتَطَرِّفَة بَعْدَ كَسْر). أَزْعُمُ (مُضَارَعَة).

=== BLOCK 33: Imla' Examples 6-10 ===
(Component: TEMPLATE_C_EXAM)
Number: ٦
Question: عَلِّلْ التَّاء: (الجُنَاة، تَخَذَتْ). عَلِّلْ الأَلِف: (الرَّدَى، عَلَا). تَنْوِين نَصْب: (نِدَاء، ظَمَأ).
Answer: الجُنَاة (جَمْع تَكْسِير). تَخَذَتْ (تَأْنِيث). الرَّدَى (ثُلَاثِيّ يَاء). عَلَا (ثُلَاثِيّ وَاو). نِدَاءً (قَبْلَهَا أَلِف). ظَمَأً (عَلَى أَلِف).

=== BLOCK 34: Imla' Examples 11-15 ===
(Component: TEMPLATE_C_EXAM)
Number: ١١
Question: (يُطْفِئُ) ⇐ مَصْدَر، فَاعِل، مَفْعُول. (عَزَّى/تَعَزَّى) تَعْلِيل الأَلِف.
Answer: إِطْفَاء، مُطْفِئ، مُطْفَأ. عَزَّى (ثُلَاثِيّ). تَعَزَّى (فَوْق ثُلَاثِيّ).

=== BLOCK 35: Imla' Examples 16-24 ===
(Component: TEMPLATE_C_EXAM)
Number: ١٦
Question: مَاضِي (يُضِيءُ) وَمَصْدَرُهُ وَالتَّعْلِيل. (آخَر - إِثْرَاء).
Answer: أَضَاءَ، إِضَاءَة (رُبَاعِيّ). آخَر (مَاضِي رُبَاعِيّ). إِثْرَاء (مَصْدَر رُبَاعِيّ).

=== BLOCK 36: Previous Exam Questions (Imla') ===
(Component: TEMPLATE_C_EXAM)
Number: س
Question: (٢٠١٣-٢٠١٦): تَعْلِيل (دَهْشَة، أَخْرَجْتُ، قُدَمَاء، كَثِيرَة، المَرْآة، نَشْأَة).
Answer: دَهْشَة/كَثِيرَة/المَرْآة (مُفْرَد مُؤَنَّث). أَخْرَجْتُ (تَاء رَفْع). قُدَمَاء (مُتَطَرِّفَة بَعْدَ سَاكِن). نَشْأَة (مَفْتُوحَة بَعْدَ سَاكِن).

--- END STREAM ---
