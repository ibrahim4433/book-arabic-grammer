import os

html_content = """<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="utf-8"/>
    <title>الْمَفْعُولُ بِه وَأَنْوَاعَهُ وَعَلَاَّمَاتِ إِعْرَابِهِ</title>
    <link href="../styles/main.css" rel="stylesheet"/>
</head>
<body>
    <div class="force-new-page">

        <!-- BLOCK 1: Lesson Header -->
        <header class="page-header-strip">
            <!-- Right: Lesson Number + Lesson Details -->
            <div class="header-section right">
                <div class="lesson-number">11</div>
                <div class="lesson-details">
                    <div></div>
                    <div></div>
                </div>
            </div>
            <!-- Center: Title -->
            <div class="header-section center">
                <h1 class="header-title">الْمَفْعُولُ بِه وَأَنْوَاعَهُ وَعَلَاَّمَاتِ إِعْرَابِهِ</h1>
            </div>
            <!-- Left: Author Info -->
            <div class="header-section left">
                <div class="author-info">أ. الياس خفيف</div>
                <div class="author-info">994066850 963+</div>
            </div>
        </header>

        <!-- BLOCK 2: Introduction & Definition -->
        <section class="content-block">
            <div class="block-header">
                <span>مُقَدَّمَةٌ وَتَعْرِيفٌ</span>
            </div>
            <div class="block-body">
                <p>فِي الْجُمْلَةِ الْفِعْلِيَّةِ (الَّتِي تَتَكَوَّنُ مِنْ فِعْلٍ وَفَاعِلٍ)، قَدْ لَا يَكْتَمِلُ الْمَعْنَى إِلَّا بِذِكْرِ مَنْ أَوْ مَا وَقَعَ عَلَيْهِ هَذَا الْحَدَثِ. هَذَا الرُّكْنُ الْمُكَمِّلُ (فِي الْأَفْعَالِ الْمُتَعَدِّيَةِ) يُسَمَّى <span class="highlight-red">الْمَفْعُولَ بِهِ</span>.</p>
                <p class="text-accent"><strong>التَّعْرِيفُ:</strong> هُوَ الِاسْمُ الْمَنْصُوبُ الَّذِي وَقَعَ عَلَيْهِ فِعْلُ الْفَاعِلِ.</p>
                <p><strong>مِثَالٌ:</strong> يَشْرَبُ الْمَرِيضُ الدَّوَاءَ. (مَنْ يَشْرَبُ؟ الْمَرِيضُ الْفَاعِلُ. مَاذَا يَشْرَبُ؟ <span class="highlight-red">الدَّوَاءَ</span> الْمَفْعُولُ بِهِ).</p>
            </div>
        </section>

        <!-- BLOCK 3: Tip -->
        <div class="benefit-box tip">
            <strong>🌟 تَلْمِيحٌ كَيْفَ تَكْتَشِفُ الْمَفْعُولَ بِهِ فِي الْجُمْلَةِ؟:</strong> قِفْ قَبْلَ الْفِعْلِ وَاسْأَلْ: <strong>(مَاذَا؟)</strong>. الْإِجَابَةُ هِيَ الْمَفْعُولُ بِهِ.
        </div>

        <!-- BLOCK 4: Block For Table -->
        <section class="content-block">
            <div class="block-header">
                <span>الْإِعْرَابُ وَالْعَلَامَاتُ</span>
            </div>
            <div class="block-body">
                <p><strong>قَاعِدَةٌ ذَهَبِيَّةٌ:</strong> الْمَفْعُولُ بِهِ دَائِمًا <strong>(مَنْصُوبٌ)</strong>. وَتَخْتَلِفُ عَلَامَةُ نَصْبِهِ حَسَبَ نَوْعِ الْكَلِمَةِ.</p>

                <!-- BLOCK 5: Summary Table of Accusative Signs -->
                <div class="block-body p-0 mt-2mm">
                    <table class="dense-table">
                        <thead>
                            <tr>
                                <th>عَلَامَةُ النَّصْبِ</th>
                                <th>نَوْعُ الْكَلِمَةِ</th>
                                <th>مِثَالٌ</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>الْفَتْحَةُ (أَصْلِيَّةٌ)</td>
                                <td>لِلْمُفْرَدِ وَلِجَمْعِ التَّكْسِيرِ</td>
                                <td>غَرَسَ الْفَلَّاحُ <span class="highlight-red">الشَّجَرَةَ</span>، يَحْمِلُ الطَّالِبُ <span class="highlight-red">الْكُتُبَ</span></td>
                            </tr>
                            <tr>
                                <td>الْكَسْرَةُ (نِيَابَةً عَنِ الْفَتْحَةِ)</td>
                                <td>لِجَمْعِ الْمُؤَنَّثِ السَّالِمِ فَقَطْ</td>
                                <td>عَلَّقَ سَعِيدٌ <span class="highlight-red">اللَّوْحَاتِ</span> (مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْكَسْرَةِ)</td>
                            </tr>
                            <tr>
                                <td>الْيَاءُ (فَرْعِيَّةٌ)</td>
                                <td>لِلْمُثَنَّى وَلِجَمْعِ الْمُذَكَّرِ السَّالِمِ</td>
                                <td>حَفِظَ الطَّالِبُ <span class="highlight-red">الْقَصِيدَتَيْنِ</span>، كَافَأْتُ <span class="highlight-red">الْمُتَفَوِّقِينَ</span></td>
                            </tr>
                            <tr>
                                <td>الْأَلِفُ (فَرْعِيَّةٌ)</td>
                                <td>لِلْأَسْمَاءِ الْخَمْسَةِ</td>
                                <td>أَطِعْ <span class="highlight-red">أَبَاكَ</span> (مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْأَلِفِ)</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </section>

        <!-- BLOCK 6: Extra Info Note -->
        <div class="benefit-box">
            <strong>مُلَاحَظَةٌ حَوْلَ فِعْلِ الْأَمْرِ:</strong> إِذَا جَاءَ فِعْلُ أَمْرٍ مُوَجَّهٍ لِلْمُخَاطَبِ الْمُفْرَدِ كَقَوْلِنَا (اكْتُبِ الْوَاجِبَ، قُلِ الْحَقَّ)، يَكُونُ الْفَاعِلُ دَائِمًا مُسْتَتِرًا تَقْدِيرُهُ "أَنْتَ"، وَمَا بَعْدَ الْفِعْلِ يُعْرَبُ مَفْعُولًا بِهِ.
        </div>

        <!-- BLOCK 7: Types of Object Section -->
        <section class="content-block">
            <div class="block-header">
                <span>أَنْوَاعُ الْمَفْعُولِ بِهِ</span>
            </div>
            <div class="block-body">
                <p>الْمَفْعُولُ بِهِ لَا يَكُونُ دَائِمًا اسْمًا صَرِيحًا مَفْصُولًا (اسْمًا ظَاهِرًا)، بَلْ يَأْتِي كَثِيرًا عَلَى شَكْلِ <strong>ضَمِيرٍ مُتَّصِلٍ</strong> يَلْتَصِقُ بِآخِرِ الْفِعْلِ.</p>
                <p>إِذَا رَأَيْتَ أَحَدَ هَذِهِ الضَّمَائِرِ مُلْتَصِقًا بِـ <strong>فِعْلٍ</strong>، فَقُمْ بِإِعْرَابِهَا فَوْرًا: (ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبِ مَفْعُولٍ بِهِ).</p>

                <!-- BLOCK 8: Pronouns List -->
                <ul class="structured-list mt-2mm">
                    <li>
                        <span class="marker">•</span>
                        <span><strong>كَافُ الْخِطَابِ (كَ):</strong> مِثْلُ (يُسْعِدُ<span class="highlight-red">كَ</span> النَّجَاحُ، شَكَرَ<span class="highlight-red">كَ</span> النَّاسُ).</span>
                    </li>
                    <li>
                        <span class="marker">•</span>
                        <span><strong>هَاءُ الْغَائِبِ (هُ):</strong> مِثْلُ (الدَّرْسُ شَرَحَ<span class="highlight-red">هُ</span> الْمُعَلِّمُ).</span>
                    </li>
                    <li>
                        <span class="marker">•</span>
                        <span><strong>يَاءُ الْمُتَكَلِّمِ (نِي):</strong> مِثْلُ (عَالَجَ<span class="highlight-red">نِي</span> الطَّبِيبُ). <em>(تُسْبَقُ يَاءُ الْمُتَكَلِّمِ دَائِمًا بِنُونٍ تُسَمَّى "نُونَ الْوِقَايَةِ" لِتَحْمِيَ الْفِعْلَ مِنَ الْكَسْرِ).</em></span>
                    </li>
                    <li>
                        <span class="marker">•</span>
                        <span><strong>نَا الْمُتَكَلِّمَيْنِ الدَّالَّةُ عَلَى الْمَفْعُولَيْنِ (نَا):</strong> مِثْلُ (كَافَأَ<span class="highlight-red">نَا</span> الْمُدِيرُ). الْمُدِيرُ هُوَ الْمُكَافِئُ (الْفَاعِلُ)، وَنَحْنُ الْمُكَافَأُونَ (الْمَفْعُولُ بِهِ).</span>
                    </li>
                </ul>
            </div>
        </section>

        <!-- BLOCK 9: Warning Note -->
        <div class="benefit-box warning">
            <strong>⚠️ تَنْبِيهٌ هَامٌّ حَوْلَ (نَا):</strong> "نَا" قَدْ تَأْتِي فَاعِلًا مِثْلُ: كَتَبْ<span class="highlight-blue">نَا</span> الدَّرْسَ. نُفَرِّقُ بَيْنَهُمَا بِالْمَعْنَى وَحَرَكَةِ الْحَرْفِ الْأَخِيرِ مِنَ الْفِعْلِ الْمَاضِي؛ فَإِذَا كَانَ الْفِعْلُ الْمَاضِي مَبْنِيًّا عَلَى الْفَتْحِ "كَافَأَ<span class="highlight-red">نَا</span>"، كَانَتِ النَّا مَفْعُولًا بِهِ، وَإِذَا كَانَ مَبْنِيًّا عَلَى السُّكُونِ "كَتَبْ<span class="highlight-blue">نَا</span>"، كَانَتْ فَاعِلًا.
        </div>

        <!-- BLOCK 10: Parsing Evidence -->
        <div class="flex gap-2mm mb-1-5mm">
            <div class="irab-box flex-1">
                <div class="irab-word">الشَّجَرَةَ</div>
                <div class="irab-details">مَفْعُولٌ بِهِ مَنْصُوبٌ، وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ عَلَى آخِرِهِ.</div>
            </div>
            <div class="irab-box flex-1">
                <div class="irab-word">يُسْعِدُكَ</div>
                <div class="irab-details">فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْكَافُ: ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبِ مَفْعُولٍ بِهِ مُقَدَّمٍ.</div>
            </div>
        </div>

        <!-- EXAM BLOCK CONTAINER -->
        <section class="content-block">
            <div class="block-header bg-dark">
                <span>اخْتَبِرْ نَفْسَكَ</span>
            </div>
            <div class="block-body">

                <!-- BLOCK 11: Exam 1 -->
                <div class="exam-question mb-4mm">
                    <p class="m-0 mb-2mm">
                        <span class="exam-number">١</span>
                        اسْتَخْرِجِ الْمَفْعُولَ بِهِ مِنَ الْجُمَلِ الْآتِيَةِ وَاذْكُرْ عَلَامَةَ نَصْبِهِ:
                    </p>
                    <ul class="structured-list">
                        <li><span class="marker">•</span><span>غَرَسَ الْفَلَّاحُ الشَّجَرَةَ.</span></li>
                        <li><span class="marker">•</span><span>يَحْمِلُ الطَّالِبُ الْكُتُبَ.</span></li>
                        <li><span class="marker">•</span><span>أَطِعْ أَبَاكَ.</span></li>
                        <li><span class="marker">•</span><span>حَفِظَ الطَّالِبُ الْقَصِيدَتَيْنِ.</span></li>
                        <li><span class="marker">•</span><span>كَافَأْتُ الْمُتَفَوِّقِينَ.</span></li>
                        <li><span class="marker">•</span><span>عَلَّقَ سَعِيدٌ اللَّوْحَاتِ.</span></li>
                    </ul>
                    <div class="border-light h-8mm bg-grey-lighter mt-2mm"></div>
                </div>

                <!-- BLOCK 12: Exam 2 -->
                <div class="exam-question mb-4mm">
                    <p class="m-0 mb-2mm">
                        <span class="exam-number">٢</span>
                        أَعْرِبِ الضَّمَائِرَ الْمُتَّصِلَةَ بِالْأَفْعَالِ فِي الْجُمَلِ الْآتِيَةِ:
                    </p>
                    <ul class="structured-list">
                        <li><span class="marker">•</span><span>يُسْعِدُكَ النَّجَاحُ.</span></li>
                        <li><span class="marker">•</span><span>الدَّرْسُ شَرَحَهُ الْمُعَلِّمُ.</span></li>
                        <li><span class="marker">•</span><span>عَالَجَنِي الطَّبِيبُ.</span></li>
                    </ul>
                    <div class="border-light h-8mm bg-grey-lighter mt-2mm"></div>
                </div>

            </div>
        </section>

    </div>
</body>
</html>"""

with open("Jules-workspace/pages/11.0_nXX_الْمَفْعُولُ بِه وَأَنْوَاعَهُ وَعَلَاَّمَاتِ إِعْرَابِهِ.html", "w") as f:
    f.write(html_content)
