import os
import re

header_template = """<header class="page-header-strip" id="[UNIQUE_ID]">
    <!-- Right: Lesson Number + Lesson Details -->
    <div class="header-section right">
        <div class="lesson-number">[LESSON_NUMBER]</div>
        <div class="lesson-details">
            <div>[LEVEL_INFO]</div>
            <div>[TOPIC_INFO]</div>
        </div>
    </div>
    <!-- Center: Title -->
    <div class="header-section center">
        <h1 class="header-title">[MAIN_TITLE]</h1>
    </div>
    <!-- Left: Author Info -->
    <div class="header-section left">
        <div class="author-info">[AUTHOR_NAME]</div>
        <div class="author-info">[AUTHOR_CONTACT]</div>
    </div>
</header>"""

comp_template = """<div class="split-grid mt-2mm">
  <div id="[UNIQUE_ID_1]">
    <!-- Block 2 -->
    <div class="exam-question mt-2mm" id="[UNIQUE_ID_2]">
      <p class="m-0 mb-0">
        <span class="exam-number">[QUESTION_NUMBER_1]</span>
        [QUESTION_TEXT_1]
      </p>
      <div class="benefit-box bg-grey-lighter mt-1mm p-2mm" id="[UNIQUE_ID_3]">
        <p class="m-0"><strong>الجواب:</strong><br/>[ANSWER_TEXT_1]</p>
      </div>
    </div>
    <!-- Block 3 -->
    <div class="content-block mt-2mm" id="[UNIQUE_ID_4]">
      <div class="block-header">
        <span>[BENEFIT_TITLE]</span>
      </div>
      <div class="block-body p-2mm">
        <ul class="structured-list">
          [BENEFIT_LIST_ITEMS]
        </ul>
      </div>
    </div>
    <!-- Block 4 -->
    <div class="exam-question mt-2mm" id="[UNIQUE_ID_5]">
      <p class="m-0 mb-0">
        <span class="exam-number">[QUESTION_NUMBER_2]</span>
        [QUESTION_TEXT_2]
      </p>
      <div class="benefit-box bg-grey-lighter mt-1mm p-2mm" id="[UNIQUE_ID_6]">
        <p class="m-0"><strong>الجواب:</strong><br/>[ANSWER_TEXT_2]</p>
      </div>
    </div>
  </div>
</div>"""

header = header_template.replace("[LEVEL_INFO]", "المستوى التأسيسي")\
    .replace("[TOPIC_INFO]", "الأدب والنصوص")\
    .replace("[MAIN_TITLE]", "المهاجر")\
    .replace("[AUTHOR_NAME]", "أ. حنا خفيف")\
    .replace("[AUTHOR_CONTACT]", "")\
    .replace("[LESSON_NUMBER]", "001")

q1_q2 = comp_template.replace("[QUESTION_NUMBER_1]", "١-")\
    .replace("[QUESTION_TEXT_1]", "المستوى الفني: عَبَّرَ الشَّاعِرُ عَنْ مَضَامِينِ الأَدَبِ الوَاقِعِيِّ مُسْتَعْمِلاً أَدَوَاتٍ: (السَّرْد، الصُّورَة، التَّدَاعِي، تَضْمِين بَعْضِ قِصَصِ التُّرَاثِ الحَاضِرَةِ فِي وِجْدَانِ الجَمَاعَةِ). هَاتِ مِثَالاً لِكُلِّ مِنْهَا.")\
    .replace("[ANSWER_TEXT_1]", "السَّرْد: المَلَايِينُ الَّتِي تَكْدَحُ لَا تَحْلُمُ بِمَوْتِ فَرَاشَة<br>الصُّورَة: أَحْزَانُ البَنَفْسَج<br>التَّدَاعِي: إِنَّهَا تَضْحَكُ مِنْ أَعْمَاقِهَا<br>تَضْمِين قِصَصِ التُّرَاثِ الحَاضِرَةِ فِي وِجْدَانِ الجَمَاعَةِ: تُغْرَمُ، لَا كَمَا يُغْرَمُ مَجْنُونٌ بِطَيْف")\
    .replace("[QUESTION_NUMBER_2]", "٢-")\
    .replace("[QUESTION_TEXT_2]", "لَجَأَ الشَّاعِرُ إِلَى الجُمَلِ الخَبَرِيَّةِ فِي النَّصِّ كُلِّهِ. اذْكُرْ مُسَوِّغَاتِ ذَلِكَ.")\
    .replace("[ANSWER_TEXT_2]", "لَجَأَ الشَّاعِرُ إِلَى الأُسْلُوبِ الخَبَرِيِّ مِنْ أَجْلِ نَقْلِ المَعْلُومَاتِ أَوِ الأَخْبَارِ وَالوَصْفِ وَالتَّصْوِيرِ وَتَقْرِيرِ الحَقَائِقِ، وَتَثْبِيتِهَا فِي ذِهْنِ المُتَلَقِّي.")

q3_q4 = comp_template.replace("[QUESTION_NUMBER_1]", "٣-")\
    .replace("[QUESTION_TEXT_1]", "أَكْثَرَ الشَّاعِرُ مِنَ التَّفَاصِيلِ الجُزْئِيَّةِ المُنْتَزَعَةِ مِنْ حَيَاةِ الكَادِحِينَ. اخْتَرْ أَمْثِلَةً لِهَذِهِ التَّفَاصِيلِ، وَبَيِّنْ دَوْرَهَا فِي التَّأْثِيرِ الجَمَالِيِّ فِي المُتَلَقِّي.")\
    .replace("[ANSWER_TEXT_1]", "الأَمْثِلَةُ: المَلَايِينُ الَّتِي تَصْنَعُ لِلْحَالِمِ زَوْرَق، المَلَايِينُ الَّتِي تَصْنَعُ مِنْدِيلاً لِمُغْرَمٍ، المَلَايِينُ الَّتِي تَبْكِي، تُغَنِّي، تَتَأَلَّمُ فِي زَوَايَا الأَرْضِ، فِي مَصْنَعِ صُلْبٍ أَوْ بِمَنْجَمٍ.<br>دَوْرُهَا فِي التَّأْثِيرِ الجَمَالِيِّ: أَسْهَمَتْ هَذِهِ التَّفَاصِيلُ الجُزْئِيَّةُ الصَّغِيرَةُ فِي عَرْضِ الفِكَرِ وَالقَضَايَا العَامَّةِ لِلْمُتَلَقِّي، وَتَعْمِيقِهَا فِي وِجْدَانِهِ؛ ذَلِكَ أَنَّ الشَّاعِرَ لَمْ يَعْرِضْ هَذِهِ الفِكَرَ وَالقَضَايَا عَرْضاً مُبَاشِراً، وَإِنَّمَا عَرَضَهَا بِلُغَةِ الشِّعْرِ، وَرُؤْيَاهُ الإِبْدَاعِيَّةِ.")\
    .replace("[QUESTION_NUMBER_2]", "٤-")\
    .replace("[QUESTION_TEXT_2]", "اسْتَخْرِجْ مِنَ المَقْطَعِ الأَوَّلِ: (كِنَايَة، اسْتِعَارَة مَكْنِيَّة)، وَبَيِّنْ وَظِيفَةً لِكُلِّ مِنْهُمَا.")\
    .replace("[ANSWER_TEXT_2]", "الكِنَايَةُ: المَلَايِينُ الَّتِي تَكْدَحُ، لَا تَحْلُمُ فِي مَوْتِ فَرَاشَة - وَظِيفَتُهَا تَأْكِيدُ إِنْسَانِيَّةِ الطَّبَقَةِ الكَادِحَةِ، وَتَقْرِيبُ ذَلِكَ مِنْ ذِهْنِ المُتَلَقِّي.<br>الِاسْتِعَارَةُ المَكْنِيَّةُ: (أَحْزَانُ البَنَفْسَج) - وَظِيفَتُهَا الإِيحَاءُ، حَيْثُ جَعَلَ الشَّاعِرُ الصُّورَةَ مُوحِيَةً بِتَشْبِيهِهِ البَنَفْسَجَ بِإِنْسَانٍ، فَهَذَا أَوْحَى بِإِنْسَانِيَّةِ الكَادِحِينَ وَلُطْفِهِمْ وَرِقَّتِهِمْ.")

q5_q6 = comp_template.replace("[QUESTION_NUMBER_1]", "٥-")\
    .replace("[QUESTION_TEXT_1]", "أَسْهَمَ تَنَوُّعُ القَوَافِي وَالأَنْغَامِ فِي إِبْرَازِ المَشَاعِرِ المُتَنَوِّعَةِ، وَحَرَكَتِهَا الانْفِعَالِيَّةِ، ادْرُسْ ذَلِكَ فِي المَقْطَعِ الثَّانِي مِنَ النَّصِّ.")\
    .replace("[ANSWER_TEXT_1]", "أَدَّى تَنَوُّعُ القَوَافِي وَالأَنْغَامِ فِي الأَسْطُرِ الشِّعْرِيَّةِ إِلَى تَنَوُّعِ المَشَاعِرِ العَاطِفِيَّةِ، عَلَى النَّحْوِ الآتِي:<br>- مَشَاعِرُ الحُبِّ وَالرِّقَّةِ: أَبْرَزَ التَّنَوُّعُ هُنَا مَشَاعِرَ الأَمَلِ.<br>- ... تُغَنِّي، ... تَضْحَكُ: أَبْرَزَ التَّنَوُّعُ هُنَا مَشَاعِرَ الفَرَحِ.<br>- ... تَبْكِي، ... تَكْدَحُ، ... تَعْرَى، ... تُمَزَّقُ، ... تَتَأَلَّمُ، ... مَنْجَمٍ: أَبْرَزَ التَّنَوُّعُ هُنَا مَشَاعِرَ الأَلَمِ.<br>- ... يُغْرَمُ، ... بِطَيْفٍ: أَبْرَزَ التَّنَوُّعُ هُنَا مَشَاعِرَ الحُزْنِ.")\
    .replace("[QUESTION_NUMBER_2]", "٦-")\
    .replace("[QUESTION_TEXT_2]", "قَطِّعْ عَروضِيّاً السَّطْرَ الأَوَّلَ مِنَ النَّصِّ، وَاذْكُرِ التَّفْعِيلَةَ الَّتِي بُنِيَ عَلَيْهَا.")\
    .replace("[ANSWER_TEXT_2]", "تَقْطِيعُ السَّطْرِ الأَوَّلِ مِنَ النَّصِّ، وَذِكْرُ التَّفْعِيلَةِ الَّتِي بُنِيَ عَلَيْهَا:")

plan = f"""# **SESSION 001.4**

[TASK DEFINITION]
Objective: Implement Part 4 of المهاجر.
File: `pages/001.4_nXXX_المهاجر.html`
Reference: Follow patterns in design_patterns.json.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: TEMPLATE_C_HEADER.html ===
(Component: TEMPLATE_C_HEADER.html)
{header}

=== BLOCK 2: TEMPLATE_LIT_PART_4_COMPREHENSION.html ===
(Component: TEMPLATE_LIT_PART_4_COMPREHENSION.html)
{q1_q2}

=== BLOCK 3: TEMPLATE_LIT_PART_4_COMPREHENSION.html ===
(Component: TEMPLATE_LIT_PART_4_COMPREHENSION.html)
{q3_q4}

=== BLOCK 4: TEMPLATE_LIT_PART_4_COMPREHENSION.html ===
(Component: TEMPLATE_LIT_PART_4_COMPREHENSION.html)
{q5_q6}

--- END STREAM ---
"""

# Fix the IDs in the plan and remove empty benefit blocks
plan = re.sub(r'<!-- Block 3 -->\s*<div class="content-block mt-2mm" id="\[UNIQUE_ID_4\]">\s*<div class="block-header">\s*<span>\[BENEFIT_TITLE\]</span>\s*</div>\s*<div class="block-body p-2mm">\s*<ul class="structured-list">\s*\[BENEFIT_LIST_ITEMS\]\s*</ul>\s*</div>\s*</div>', '', plan)

id_counter_2 = 10001
def replace_id_2(match):
    global id_counter_2
    res = f'b{id_counter_2}'
    id_counter_2 += 1
    return res

plan = re.sub(r'\[UNIQUE_ID(?:_[0-9]+)?\]', replace_id_2, plan)

os.makedirs('plans', exist_ok=True)
with open('plans/001.4_nXXX_المهاجر-plan_7p16l.md', 'w', encoding='utf-8') as f:
    f.write(plan)
