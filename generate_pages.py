import os
import json
import subprocess

def run_verify(filepath):
    result = subprocess.run(['python', 'Jules-workspace/verify_layout.py', filepath], capture_output=True, text=True)
    try:
        output = result.stdout
        # isolate the JSON object
        json_str = output[output.find('{'):output.rfind('}')+1]
        return json.loads(json_str)
    except Exception as e:
        print("Error parsing verify_layout output:", e)
        print("Raw output:", result.stdout)
        return None

base_template = """<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="utf-8"/>
    <title>أَقْسَامُ الْكَلَاَمِ الْمُفِيدِ فِي اللُّغَةَ الْعَرَبِيَّةَ</title>
    <link href="../styles/main.css" rel="stylesheet"/>
</head>
<body>
    <div class="force-new-page">
{content}
    </div>
</body>
</html>
"""

blocks = [
    """
        <header class="page-header-strip" id="b00001">
            <div class="header-section right">
                <div class="lesson-number">01</div>
                <div class="lesson-details">
                    <div>المستوى التأسيسي</div>
                    <div>علم النحو</div>
                </div>
            </div>
            <div class="header-section center">
                <h1 class="header-title">أَقْسَامُ الْكَلَاَمِ الْمُفِيدِ فِي اللُّغَةَ الْعَرَبِيَّةَ</h1>
            </div>
            <div class="header-section left">
                <div class="author-info">أ. الياس خفيف</div>
                <div class="author-info">994066850 963+</div>
            </div>
        </header>
    """,
    """
        <section class="content-block" id="b00002">
            <div class="block-header">
                <span>مُقَدَّمَةً</span>
            </div>
            <div class="block-body">
                <p class="mt-1mm text-accent">
                    يُقَسِّمُ عُلَمَاءُ اللُّغَةَ الْعَرَبِيَّةَ مَا يَتَلَفَّظُ بِه الْإِنْسَانِ إِلَى خَمْسَةٍ أَقْسَامَ رَئِيسِيَّةَ لِفَهِمَ قَوَاعِدُ اللُّغَةَ الْعَرَبِيَّةَ بِشَكْلِ صَحِيحِ ، يَجِبُ أَوْلَا التَّمْييزِ بَيْن هَذِه الْمُصْطَلَحَاتِ الْخُمُسَةَ:
                </p>
                <div class="flex flex-wrap gap-2mm mt-2mm">
                    <span class="bg-grey-lighter rounded p-1mm">الْكَلِمَةُ</span>
                    <span class="bg-grey-lighter rounded p-1mm">الْكِلَاَمُ</span>
                    <span class="bg-grey-lighter rounded p-1mm">الْكَلْمُ</span>
                    <span class="bg-grey-lighter rounded p-1mm">الْقَوْلُ</span>
                    <span class="bg-grey-lighter rounded p-1mm">اللَّفْظُ</span>
                </div>
            </div>
        </section>
    """,
    """
        <section class="content-block" id="b00003">
            <div class="block-header">
                <span>١. الْكَلِمَةُ</span>
            </div>
            <div class="block-body">
                <p class="mt-1mm text-accent">
                    <strong>التَّعْرِيفَ:</strong> هِي اللَّفْظِ الْمَوْضُوعِ لِمُعَنَّى مُفْرَدَ. أي أَنّهَا لَفْظَةَ وَاحِدَةَ تَدَلٍّ عَلَى شَيْءِ مُعَيَّنِ بذَاتهُ.
                </p>
                <p><strong>أَمِثْلَةَ:</strong> <span class="highlight-red">بَحْرٌ</span> ، <span class="highlight-red">قَلَمٌ</span> ، <span class="highlight-red">شَجَرَةً</span> ، <span class="highlight-red">تِلْميذٌ</span> ، <span class="highlight-red">مُعَلِّمٌ</span> ، <span class="highlight-red">رَجُلٌ</span></p>
            </div>
        </section>
    """,
    """
        <div class="benefit-box warning" id="b00004">
            <strong>⚠️ مُلَاحِظَةً وَاِسْتِثْنَاءَ:</strong>
            <p>فِي بَعْضِ الْأَحْيَانِ فِي اللُّغَةَ الْعَرَبِيَّةَ ، قَد يُقْصَدُ بـ "الْكَلِمَةَ" جُمْلَةَ كَامِلَةَ أَو كَلَاَمَا طَوِيلَا، كَمَا فِي:</p>
            <ul class="structured-list">
                <li>
                    <span class="marker">•</span>
                    <span><strong>الشِّعْرَ الْعَرَبِيَّ:</strong> قَوْلُ الشَّاعِرِ: "أَقُولُ لهُ وقَد طَارَتْ شَعَاعًا ... مِنَ الْأَبْطَالِ وَيْحَكَ لَنْ تُرَاعِي"، فَالْمَقْصُودَ بِالْكَلِمَةِ هُنَا الْبَيْتُ كَامِلًا.</span>
                </li>
                <li>
                    <span class="marker">•</span>
                    <span><strong>الْخُطَبَ وَالْمَقُولَاتِ:</strong> مَقُولَةُ الْقَائِدِ الْمَشْهُورَةِ: "<span class="highlight-red">كَلِمَةُ</span> وَاحِدَةً أَقُولُهَا لَكُم اِتَّحَدُوا تَسُودُوا"، فَالْمَقْصُودَ بِالْكَلِمَةِ هُنَا الْجُمْلَةُ كَامِلَةٌ.</span>
                </li>
            </ul>
        </div>
    """,
    """
        <section class="poem-container" id="b00005">
            <div class="block-header poem-header">
                <span>الشاهد الشعري</span>
            </div>
            <div class="poem-verses">
                <div class="poem-line flex justify-between items-center mb-2mm">
                    <div class="hemistich w-45pct text-center font-bold">أَقُولُ لهُ وقَد طَارَتْ شَعَاعًا</div>
                    <div class="hemistich w-45pct text-center font-bold">مِنَ الْأَبْطَالِ وَيْحَكَ لَنْ تُرَاعِي</div>
                </div>
            </div>
        </section>
    """,
    """
        <div class="flex gap-2mm mb-1-5mm">
            <div class="irab-box flex-1" id="b00006">
                <div class="irab-word">وَيْحَكَ لَنْ تُرَاعِي</div>
                <div class="irab-details">اِسْتُخْدِمَتْ هُنَا بِمَعْنَى "الْكَلِمَةِ" لِلدَّلَالَةِ عَلَى جُمْلَةٍ كَامِلَةٍ.</div>
            </div>
        </div>
    """,
    """
        <section class="content-block" id="b00007">
            <div class="block-header">
                <span>٢. الْكِلَاَمُ</span>
            </div>
            <div class="block-body">
                <p class="mt-1mm text-accent">
                    <strong>التَّعْرِيفَ:</strong> هُو مَا تَرَكُّبٍ مِن كَلْمَتَيْنِ فأَكْثَرِ ، وَأَفَادَ مُعَنًّى يُحْسِنُ السُّكُوتُ عَلَيْهِ (أَيَّ جُمْلَةِ تَامَّةِ الْمُعَنَّى).
                </p>
                <p><strong>أَمِثْلَةَ:</strong></p>
                <ul class="structured-list">
                    <li>
                        <span class="marker">•</span>
                        <span><span class="highlight-red">السَّفَرُ مُفِيدٌ</span> (جُمْلَةَ اِسْمِيَّةَ مُكَوِّنَةَ مِن كَلْمَتَيْنِ وَتُفِيدُ مُعَنَّى تَامًّا).</span>
                    </li>
                    <li>
                        <span class="marker">•</span>
                        <span><span class="highlight-red">اِذْهَبْ</span> (تَبْدُو كَكَلِمَةِ وَاحِدَةِ ، لَكِنّهَا فِي الْأَصْلِ جُمْلَةً تَتَكَوَّنُ مِن كَلْمَتَيْنِ: الْفِعْلُ "اِذْهَبْ" وَالضَّمِيرَ الْمُسْتَتِرَ "أَنْت"، وَتُفِيدُ مُعَنَّى تَامًّا).</span>
                    </li>
                </ul>
            </div>
        </section>
    """,
    """
        <section class="content-block" id="b00008">
            <div class="block-header">
                <span>٣. الْكَلِمُ</span>
            </div>
            <div class="block-body">
                <p class="mt-1mm text-accent">
                    <strong>التَّعْرِيفَ:</strong> هُو مَا تَكَوُّنٍ مِن ثَلاث كَلِمَاتٍ فأَكْثَرِ ، <strong>سَوَاءً أَفَادَ مُعَنًّى يُحْسِنُ السُّكُوتُ عَلَيْهِ أَم لَم يُفِدْ</strong>.
                </p>
                <p><strong>أَمِثْلَةَ:</strong></p>
                <ul class="structured-list">
                    <li>
                        <span class="marker">•</span>
                        <span><span class="highlight-red">كَتَبَ الطَّالِبُ الدَّرْسَ</span> (مُكَوِّنٌ مِن 3 كَلِمَاتٍ ، وَأَفَادَ مُعَنَّى تَامًّا يُسَمَّى <strong>كَلَّمَ</strong> وَيُسَمَّى أيضاً <strong>كِلَاَمَ</strong>).</span>
                    </li>
                    <li>
                        <span class="marker">•</span>
                        <span><span class="highlight-red">إِنْ قَامَ زَيْدٌ...</span> أَو <span class="highlight-red">ضَعْ إِلَى نَحْفَظُ...</span> (مُكَوِّنٌ مِن 3 كَلِمَاتٍ ، لَكِنّهُ لَا يُفِيدُ مُعَنَّى تَامًّا يُسَمَّى <strong>كَلَّمَ</strong> فَقَط ، ولَا يُسَمَّى كَلَاَمَا).</span>
                    </li>
                </ul>
            </div>
        </section>
    """,
    """
        <section class="split-grid">
            <div class="content-block" id="b00009">
                <div class="block-header">
                    <span>٤. الْقَوْلُ</span>
                </div>
                <div class="block-body">
                    <p class="mt-1mm text-accent">
                        <strong>التَّعْرِيفَ:</strong> كَلٌّ مَا يَتَلَفَّظُ بِه الْإِنْسَانِ وَيَدُلُّ عَلَى مُعَنًّى ، سَوَاءً كَان مُفْرَدًا أَو مَرْكَبًا ، مُفِيدًا أَو غَيْر مُفِيدٍ. (وهُو أَعَمِّ مِن الْكَلِمَةِ وَالْكِلَاَمِ وَالْكَلْمِ).
                    </p>
                    <p><strong>أَمِثْلَةَ:</strong></p>
                    <ul class="structured-list">
                        <li>
                            <span class="marker">•</span>
                            <span><span class="highlight-red">أَسُدْ</span> (مُفْرَدٌ يَدُلُّ عَلَى مُعَنَّى قَوْلٍ ، وَكَلِمَةَ).</span>
                        </li>
                        <li>
                            <span class="marker">•</span>
                            <span><span class="highlight-red">طَالِبُ الْعِلْمِ</span> (مَرْكَبٌ يَدُلُّ عَلَى مُعَنًّى ، لَكِنّهُ لَا يُحْسِنُ السُّكُوتُ عَلَيْهِ قَوْلَ).</span>
                        </li>
                        <li>
                            <span class="marker">•</span>
                            <span><span class="highlight-red">الْعِلْمُ نُورٌ</span> (مَرْكَبٌ يَدُلُّ عَلَى مُعَنَّى تَامِّ قَوْلٍ ، وَكِلَاَمَ).</span>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="content-block" id="b00010">
                <div class="block-header">
                    <span>٥. اللَّفْظُ</span>
                </div>
                <div class="block-body">
                    <p class="mt-1mm text-accent">
                        <strong>التَّعْرِيفَ:</strong> هُو الصَّوْتِ الْمُشْتَمِلِ عَلَى بَعْضِ الْحُروفِ ، سَوَاءً أَفَادَ مُعَنًّى أَم لَم يُفِدْ.
                    </p>
                    <p><strong>أَمِثْلَةَ:</strong></p>
                    <ul class="structured-list">
                        <li>
                            <span class="marker">•</span>
                            <span><span class="highlight-red">سَيَّارَةَ</span> (صَوْتٌ بِحُروفٍ لَه مُعَنَّى لَفْظِ).</span>
                        </li>
                        <li>
                            <span class="marker">•</span>
                            <span><span class="highlight-red">لُزِّنَّ</span> أَو <span class="highlight-red">ديز</span> (مَقْلُوبَ كَلِمَةِ زَيْدِ) (صَوْتٌ بِحُروفٍ لَيْس لَه مُعَنَّى لَفْظٍ فَقَط ، ولَا يُسَمَّى كَلَمَّةٍ ولَا قَوْلًا).</span>
                        </li>
                    </ul>
                </div>
            </div>
        </section>
    """,
    """
        <section class="content-block" id="b00011">
            <div class="block-header">
                <span>مُلَخَّصَ الْفَرُوقِ</span>
            </div>
            <div class="block-body p-0">
                <table class="dense-table">
                    <thead>
                        <tr>
                            <th>الْعِبَارَةَ / اللَّفْظَ</th>
                            <th>هَل هِي لَفْظِ ؟</th>
                            <th>هَل هِي قَوْلِ ؟</th>
                            <th>هَل هِي كَلِمَةِ ؟</th>
                            <th>هَل هِي كِلَاَمِ ؟</th>
                            <th>هَل هِي كَلِمِ ؟</th>
                            <th>السَّبَبَ</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>بَيْتَ</td>
                            <td>نَعَم</td>
                            <td>نَعَم</td>
                            <td>نَعَم</td>
                            <td>لَا</td>
                            <td>لَا</td>
                            <td>لَفْظَ مُفْرَدَ لَه مُعَنَّى .</td>
                        </tr>
                        <tr>
                            <td>الْعِلْمُ نُورٌ</td>
                            <td>نَعَم</td>
                            <td>نَعَم</td>
                            <td>لَا</td>
                            <td>نَعَم</td>
                            <td>لَا</td>
                            <td>مَرْكَبٌ مِن كَلْمَتَيْنِ وَأَفَادَ مُعَنَّى تَامًّا يُحْسِنُ السُّكُوتُ عَلَيْهِ .</td>
                        </tr>
                        <tr>
                            <td>فَهِمَ الطَّالِبُ الدَّرْسَ</td>
                            <td>نَعَم</td>
                            <td>نَعَم</td>
                            <td>لَا</td>
                            <td>نَعَم</td>
                            <td>نَعَم</td>
                            <td>مَرْكَبٌ مِن 3 كَلِمَاتٍ وَأَفَادَ مُعَنَّى تَامًّا .( فهُو كِلَاَمٍ وَكَلِمِ مَعَا ).</td>
                        </tr>
                        <tr>
                            <td>لُزِّنَّ</td>
                            <td>نَعَم</td>
                            <td>لَا</td>
                            <td>لَا</td>
                            <td>لَا</td>
                            <td>لَا</td>
                            <td>مُجَرَّدَ حُروفِ تَخَرُّجٍ مِن الْفَمِ بِلَا أَيِّ مُعَنَّى .</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>
    """,
    """
        <div class="exam-question" id="b00013">
            <p class="m-0 mb-2mm">
                <span class="exam-number">١</span>
                حَدَّدَ نَوْعُ الْعِبَارَاتِ التَّالِيَةِ بِنَاءً عَلَى مَا دَرَسَتْ ( الْكَلِمَةَ ، الْكِلَاَمَ ، الْكَلْمَ ، الْقَوْلَ ، اللَّفْظَ ). مُلَاحِظَةً: قَد تَقْبَلُ الْعِبَارَةُ أَكْثَرَ مِن إِجَابَةِ:
            </p>
            <ul class="structured-list">
                <li><span class="marker">•</span><span>1. شَجَرَةُ</span></li>
                <li><span class="marker">•</span><span>2. السَّفَرُ مُفِيدٌ</span></li>
                <li><span class="marker">•</span><span>3. اِذْهَبْ</span></li>
                <li><span class="marker">•</span><span>4. كَتَبَ الطَّالِبُ الدَّرْسَ</span></li>
                <li><span class="marker">•</span><span>5. ضَعْ إِلَى نَحْفَظُ</span></li>
                <li><span class="marker">•</span><span>6. أَسَدُّ</span></li>
                <li><span class="marker">•</span><span>7. طَالِبُ الْعِلْمِ</span></li>
                <li><span class="marker">•</span><span>8. سَيَّارَةُ</span></li>
                <li><span class="marker">•</span><span>9. لُزِّنَّ</span></li>
            </ul>
            <div class="border-light h-8mm bg-grey-lighter rounded mt-2mm"></div>
        </div>
    """,
    """
        <div class="exam-question" id="b00014">
            <p class="m-0 mb-2mm">
                <span class="exam-number">٢</span>
                اِقْرَأْ الْمَقُولَاتِ وَالْأَشْعَارِ التَّالِيَةِ ، ثُمَّ أَجِبُ:<br>
                أ) يَقُولُ الشَّاعِرُ: "أَقُولُ لهُ وقَد طَارَتْ شَعَاعًا ... مِنَ الْأَبْطَالِ وَيْحَكَ لَنْ تُرَاعِي". مَا الْمَقْصُودِ بـ "كَلِمَةَ" (وَيَحْكِ لَن تُرَاعِي) فِي هَذَا السِّيَاقِ، وهَل هِي لَفْظَةٍ مُفْرَدَةٍ أَم جُمْلَةٌ؟<br>
                ب) الْمَقُولَةَ الْمَشْهُورَةَ: "كَلِمَةُ وَاحِدَةُ أَقُولُهَا لَكُم: اِتَّحَدُوا تَسُودُوا". لِمَاذَا أُطْلِقُ عَلَى عِبَارَةِ "اِتَّحَدُوا تَسُودُوا" بأَنّهَا "كَلِمَةَ" رَغْمٌ أَنّهَا جُمْلَةَ كَامِلَةَ؟
            </p>
            <div class="border-light h-8mm bg-grey-lighter rounded mt-2mm"></div>
        </div>
    """,
    """
        <div class="exam-question" id="b00015">
            <p class="m-0 mb-2mm">
                <span class="exam-number">٣</span>
                ضَعْ عُلَّامَةَ (صَحَّ) أَو (خَطَأَ) مَع تَصْحِيحِ الْخَطَأِ:<br>
                1. ( ) كُلّ كَلِمٍ هُو كَلَاَمِ مُفِيدِ يُحْسِنُ السُّكُوتُ عَلَيْهِ.<br>
                2. ( ) "الْعِلْمُ نُورٌ" تُعْتَبَرُ كَلَاَمًا لأَنّهَا تَتُكُّونَ مِن كَلْمَتَيْنِ وَتُفِيدُ مُعَنَّى تَامًّا.<br>
                3. ( ) أَيَّ صَوْتٍ يَخْرُجُ مِن فَمِ الْإِنْسَانِ يَحْتَوِي عَلَى حُروفِ يُسَمَّى "قَوْلًا" حَتَّى لَو لَم يَكُنُّ لَه مُعَنًّى.<br>
                4. ( ) جُمْلَةُ "اِذْهَبْ" هِي كَلِمَةِ وَاحِدَةِ ولَيْسَت كَلَاَمًا.
            </p>
            <div class="border-light h-8mm bg-grey-lighter rounded mt-2mm"></div>
        </div>
    """
]

# We need to fill remaining space on the last page.
fill_blocks = [
    """
        <div class="benefit-box tip" id="b00016">
            <strong>💡 فَائِدَةٌ:</strong>
            <p>تَذَكَّرْ دَائِمًا أَنَّ الْكَلِمَةَ هِيَ الْأَسَاسُ، وَبِتَجْمِيعِهَا نَحْصُلُ عَلَى الْكَلَامِ وَالْكَلِمِ وَالْقَوْلِ. فَهْمُكَ لِهَذِهِ الْأَقْسَامِ يُسَهِّلُ عَلَيْكَ دِرَاسَةَ النَّحْوِ.</p>
        </div>
    """,
    """
        <div class="benefit-box tip" id="b00017">
            <strong>💡 تَنْبِيهٌ مُهِمٌّ:</strong>
            <p>لَا يَشْتَرِطُ فِي "الْكَلِمِ" إِفَادَةُ الْمَعْنَى التَّامِّ، بَيْنَمَا "الْكَلَامُ" لَا يَكُونُ كَلَامًا إِلَّا إِذَا أَفَادَ مَعْنًى يَحْسُنُ السُّكُوتُ عَلَيْهِ.</p>
        </div>
    """,
    """
        <div class="benefit-box tip" id="b00018">
            <strong>💡 مَعْلُومَةٌ إِضَافِيَّةٌ:</strong>
            <p>اَللَّفْظُ أَعَمُّ مِنْ كُلِّ مَا سَبَقَ، فَهُوَ يَشْمَلُ كُلَّ صَوْتٍ يَخْرُجُ مِنْ فَمِ الْإِنْسَانِ سَوَاءٌ كَانَ لَهُ مَعْنًى أَمْ لَا.</p>
        </div>
    """,
    """
        <div class="benefit-box tip" id="b00019">
            <strong>💡 خُلَاصَةٌ:</strong>
            <p>يُمْكِنُنَا أَنْ نَقُولَ: كُلُّ كَلَامٍ قَوْلٌ وَلَفْظٌ، وَلَيْسَ كُلُّ قَوْلٍ وَلَفْظٍ كَلَامًا.</p>
        </div>
    """
]

page_num = 0
current_blocks = []

def save_page(num, blocks_to_save):
    suffix = str(num)
    title = "أَقْسَامُ الْكَلَاَمِ الْمُفِيدِ فِي اللُّغَةَ الْعَرَبِيَّةَ"
    filename = f"pages/01.{suffix}_nXX_{title}.html"
    content = "\n".join(blocks_to_save)
    full_html = base_template.format(content=content)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(full_html)
    return filename

for i, block in enumerate(blocks):
    current_blocks.append(block)
    temp_file = save_page(page_num, current_blocks)
    result = run_verify(temp_file)
    print(f"Adding block {i+1}, status: {result['status']}, remaining height: {result['remaining_height_mm']}")

    if result['status'] == 'OVERFLOW' or (result['status'] == 'FAIL' and result.get('recommendation') == 'SPLIT'):
        print(f"Page {page_num} is full. Splitting...")
        overflow_block = current_blocks.pop()
        save_page(page_num, current_blocks)
        page_num += 1

        continuation_header = """
        <header class="page-header-strip" id="b_cont_{}">
            <div class="header-section right">
                <div class="lesson-number">01</div>
                <div class="lesson-details">
                    <div>المستوى التأسيسي</div>
                    <div>علم النحو</div>
                </div>
            </div>
            <div class="header-section center">
                <h1 class="header-title">أَقْسَامُ الْكَلَاَمِ الْمُفِيدِ فِي اللُّغَةَ الْعَرَبِيَّةَ (تابع)</h1>
            </div>
            <div class="header-section left">
                <div class="author-info">أ. الياس خفيف</div>
                <div class="author-info">994066850 963+</div>
            </div>
        </header>
        """.format(page_num)

        current_blocks = [continuation_header, overflow_block]

final_file = save_page(page_num, current_blocks)
final_result = run_verify(final_file)
print(f"Final page {page_num} status: {final_result['status']}, blank percentage: {final_result['blank_space_percentage']}")

# Now try adding fill blocks until UNDERFLOW fails (OVERFLOW)
for block in fill_blocks:
    if run_verify(final_file)['status'] == 'FAIL':
         print("File failing... skipping filler")
         break
    if run_verify(final_file)['status'] == 'PASS':
        break # We hit >80% limit successfully
    current_blocks.append(block)
    temp_file = save_page(page_num, current_blocks)
    result = run_verify(temp_file)
    print(f"Adding fill block, status: {result['status']}, remaining height: {result['remaining_height_mm']}")
    if result['status'] == 'OVERFLOW' or (result['status'] == 'FAIL' and result.get('recommendation') == 'SPLIT'):
        current_blocks.pop()
        save_page(page_num, current_blocks)
        break

final_file = save_page(page_num, current_blocks)
final_result = run_verify(final_file)
print(f"Final page {page_num} final status: {final_result['status']}, blank percentage: {final_result['blank_space_percentage']}")
