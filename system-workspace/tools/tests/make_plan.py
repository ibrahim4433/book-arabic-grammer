import re
import os

plan_content = """# **SESSION 001.1**

[TASK DEFINITION]
Objective: Implement Part 1 of المهاجر.
File: `pages/001.1_nXXX_المهاجر.html`
Reference: Follow patterns in design_patterns.json.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: TEMPLATE_C_HEADER.html ===
<header class="page-header-strip" id="hdr_001">
    <!-- Right: Lesson Number + Lesson Details -->
    <div class="header-section right">
        <div class="lesson-number">001</div>
        <div class="lesson-details">
            <div>المستوى التأسيسي</div>
            <div>الأدب والنصوص</div>
        </div>
    </div>
    <!-- Center: Title -->
    <div class="header-section center">
        <h1 class="header-title">المهاجر</h1>
    </div>
    <!-- Left: Author Info -->
    <div class="header-section left">
        <div class="author-info">أ. حنا خفيف</div>
        <div class="author-info"> </div>
    </div>
</header>

=== BLOCK 2: TEMPLATE_LIT_PART_1_POEM.html ===
<div class="split-grid mb-1mm w-full">
  <div id="bio_1">
    <div class="bio-card" id="bio_card_1">
      <div class="bio-image-container">
        <img alt="نديم محمد" class="poet-img" src="../input/integrated-pictures/pic_001.jpg"/>
      </div>
      <div class="bio-info p-0">
        <h4 class="m-0 text-dark">نديم محمد</h4>
        <p class="m-0 mt-1mm text-sm"></p>
        <ul class="structured-list mb-0">
          <li>تَعَلَّمَ القِرَاءَةَ وَالقُرْآنَ فِي القَرْيَةِ عَلَى يَدِ شَيْخِ الكُتَّابِ، ثُمَّ أُرْسِلَ إِلَى بَانِيَاسَ لِيَتَعَلَّمَ قَوَاعِدَ اللُّغَةِ العَرَبِيَّةِ، وَمِنْهَا إِلَى مَدْرَسَةِ (الفِرِير) فِي اللَّاذِقِيَّةِ.</li>
          <li>وَفِي عَامِ 1926م أُرْسِلَ إِلَى مَدْرَسَةِ (اللَّايِيك) فِي بَيْرُوتَ، وَمِنْهَا إِلَى فَرَنْسَا لِإِتْمَامِ الدِّرَاسَةِ فِي جَامِعَةِ مُونْبِلْيِيه، حَصَلَ عَلَى الإِجَازَةِ فِي الأَدَبِ العَرَبِيِّ.</li>
          <li>ثُمَّ انْتَقَلَ إِلَى سُوِيسْرَا لِدِرَاسَةِ الحُقُوقِ، وَلَكِنَّهُ عَادَ عَامَ 1930م لِأَسْبَابٍ خَاصَّةٍ مِنْ دُونِ أَنْ يُكْمِلَ دِرَاسَتَهُ.</li>
          <li>اتَّسَمَ بِحِسِّهِ المُرْهَفِ وَمُعَانَاتِهِ الذَّاتِيَّةِ العَمِيقَةِ.</li>
          <li>لَهُ عِدَّةُ مَجْمُوعَاتٍ مِنْهَا: (فَرَاشَاتٌ وَعَنَاكِبُ)، (فُرُوعٌ مِنْ أُصُولٍ)، وَمَجْمُوعَةُ (آلَامٍ) الَّتِي أُخِذَ مِنْهَا هَذَا النَّصُّ.</li>
        </ul>
      </div>
    </div>
  </div>
  <div id="intro_1">
    <div class="content-block" id="intro_block_1">
      <div class="block-header">
        <span>مَدْخَلٌ إِلَى النَّصِّ</span>
      </div>
      <div class="block-body p-0">
        <ul class="structured-list mb-0">
          <li>دَأَبَ الرُّومَانْسِيُّونَ عَلَى تَمْجِيدِ الأَلَمِ، بِوَصْفِهِ بَاعِثاً عَلَى الكِتَابَةِ وَالتَّوَهُّجِ الإِبْدَاعِيِّ، لِذَلِكَ نَرَاهُمْ يُعْطُونَ قِيَادَ نُفُوسِهِمْ لِلشُّعُورِ، فَتَنْسَابُ أَشْعَارُهُمْ مُخْضَلَّةً بِالدُّمُوعِ، مُتَوَّجَةً بِالآهَاتِ والأَحْزَانِ والشَّكْوَى، مُسْتَبْطِنَةً خَزَائِنَ اللَّاشُعُورِ، كَاشِفَةً عَمَّا تَوَارَى فِيهَا مِنْ حُبٍّ مُخْفِقٍ، وآمَالٍ مُنْكَسِرَةٍ، وأُمْنِيَّاتٍ خَائِبَةٍ، وَهَذَا مَا سَعَى الشَّاعِرُ إِلَى بَثِّهِ فِي تَضَاعِيفِ هَذِهِ الأَبْيَاتِ.</li>
          <li><strong>شَرْحُ المُفْرَدَاتِ الصَّعْبَةِ بِحَسَبِ وُرُودِهَا فِي النَّصِّ:</strong></li>
          <li>الذُّبَالِي: الشَّعْلَةُ السَّاطِعَةُ مِنَ النَّارِ.</li>
          <li>يُطَاوِلُنِي: يُغَالِبُنِي.</li>
          <li>أَرْكَزْتُ: ثَبَّتُّ.</li>
          <li>تَرْعَهُ: تُفْزِعُهُ وَتُخِيفُهُ. شِهَابٌ.</li>
          <li>الأَصِيلُ: الوَقْتُ حِينَ تَصْفَرُّ الشَّمْسُ لِمَغِيبِهَا.</li>
          <li>المَلَابُ: ضَرْبٌ مِنَ الطِّيبِ.</li>
          <li><strong>مَعَانِي النَّصِّ: مَعَانِي المَقْطَعِ الأَوَّلِ:</strong></li>
          <li>يَبْدَأُ الشَّاعِرُ المَقْطَعَ الأَوَّلَ بِنِدَاءِ شُعُورِهِ، وَنَعْتِهِ بِالحَيَّةِ الَّتِي تَنْفُثُ السَّمَّ، امْتَلَكَتْ أَلْفَ نَابٍ يَضُخُّ فِي قَلْبِهِ بِغَزَارَةٍ وَكَثَافَةٍ، وَكَأَنَّهَا قَدْ جَعَلَتْ حُزْنَهُ يَبْلُغُ الذِّرْوَةَ، وَاسْتِفْحَالَهُ، فَيُؤَكِّدُ أَنَّ شُعُورَهُ يَجْعَلُهُ السَّبَبَ فِي تَفَاقُمِ مَرَضِهِ. ثُمَّ لَا يَلْبَثُ أَنْ جَعَلَ عَذَابَهُ يَمْتَدُّ.</li>
        </ul>
      </div>
    </div>
  </div>
</div>
<div class="poem-container" id="poem_1">
  <div class="poem-verses m-0 p-0">
    <div class="poem-line">
        <span class="hemistich">يَا شُعُورِي يَا حَيَّةً تَنْفُثُ السُّمَّ</span>
        <span class="hemistich">مِنْ أَلْفِ نَابٍ فَيَجْرِي فِي القَلْبِ</span>
    </div>
    <div class="poem-line">
        <span class="hemistich">كَبُرَتْ فِيكَ عِلَّتِي وَتَنَاهَى</span>
        <span class="hemistich">فِيكَ حُزْنِي، وَطَالَ فِيكَ عَذَابِي</span>
    </div>
    <div class="poem-line">
        <span class="hemistich">أَيُّ عِرْقٍ لَمْ تَلْتَهِمْهُ، وَعَظْمٍ</span>
        <span class="hemistich">لَمْ تَرْعَهُ بِعَاصِفٍ أَوْ شِهَابِ؟</span>
    </div>
    <div class="poem-line">
        <span class="hemistich">شَهِدَ الحُبُّ مَا تَرَكْتَ لِأَثْوَا</span>
        <span class="hemistich">بِيَ مِنَ الجِسْمِ غَيْرَ جِلْدٍ خَرَابِ</span>
    </div>
    <div class="poem-line">
        <span class="hemistich">لَوْ بِغَيْرِ الهَوَى يُطَاوِلُنِي الدَّهْـ</span>
        <span class="hemistich">ـرُ لَأَرْكَزْتُ فِي النُّجُومِ قِبَابِي</span>
    </div>
    <div class="poem-line">
        <span class="hemistich">وَجَرَرْتُ بُرْدَ زَهْوِي عَلَى البَدْ</span>
        <span class="hemistich">رِ وَلَطَّمْتُ خَدَّهُ بِذُبَالِي</span>
    </div>
    <div class="poem-line">
        <span class="hemistich">وَلَطَّوْفْتُ بِالنَّعِيمِ فَرَشَّتْـ</span>
        <span class="hemistich">ـنِي حِسَانُ النَّعِيمِ بِالأَطْيَابِ</span>
    </div>
    <div class="poem-line">
        <span class="hemistich">وَتَسَجَّيْتُ الأَصِيلَ ثَوْبًا وَنَقَّيْـ</span>
        <span class="hemistich">ـتُ حَوَافِيهِ بِالنَّدَى وَالمَلَابِ</span>
    </div>
  </div>
</div>

--- END STREAM ---
"""

with open('plans/001.1_nXXX_المهاجر-plan_pbk5q.md', 'w', encoding='utf-8') as f:
    f.write(plan_content)
