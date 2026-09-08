import os

with open('Jules-workspace/Templates/TEMPLATE_C_HEADER.html', 'r', encoding='utf-8') as f:
    header_template = f.read()

with open('Jules-workspace/Part-Templates/TEMPLATE_LIT_PART_3_EXPLANATION.html', 'r', encoding='utf-8') as f:
    explanation_template = f.read()

header = header_template.replace('[UNIQUE_ID]', 'b10001') \
                        .replace('[LESSON_NUMBER]', '001') \
                        .replace('[LEVEL_INFO]', 'المستوى التأسيسي') \
                        .replace('[TOPIC_INFO]', 'الأدب والنصوص') \
                        .replace('[MAIN_TITLE]', 'المهاجر') \
                        .replace('[AUTHOR_NAME]', 'أ. حنا خفيف') \
                        .replace('[AUTHOR_CONTACT]', '')

m1 = explanation_template.replace('[UNIQUE_ID_1]', 'b20001') \
                         .replace('[UNIQUE_ID_2]', 'b20002') \
                         .replace('[UNIQUE_ID_3]', 'b20003') \
                         .replace('[UNIQUE_ID_4]', 'b20004') \
                         .replace('[UNIQUE_ID_5]', 'b20005') \
                         .replace('[UNIQUE_ID_6]', 'b20006') \
                         .replace('[POEM_VERSE_HEMISTICHS]', '<span>المقطع الأول</span>') \
                         .replace('[EXPLANATION_CONTENT_ITEMS]', '<li>الكادِحُونَ يَتَمَنَّونَ الخَيْرَ لِجَمِيعِ الكائناتِ؛ فلا يَحْلُمُونَ بِمَوتِ فَرَاشَةٍ، ولا بِحُزْنِ وَرْدَةٍ، إِنَّهُم لَا يَحْلُمُونَ أَحْلَامًا عَظِيمَةً كبيرة، فلا يَحْلُمُونَ بِقَضَاءِ أَوْقَاتٍ سَعِيدَة على ظهر قارب يَطْفُو على صفحة الماء، تُكَلِّلُهُ أَشِعَةُ القَمَرِ الْفِضَيَّةِ فِي لَيْلَةِ أُنْسٍ صيفية، لا ولا يَحْلُمُونَ بِلَحَظَاتِ العِشق والغرام التي ينعم بِسَعَادَتِهَا العَاشِقُونَ.</li>') \
                         .replace('[IRAB_CONTENT_ITEMS]', '')

m2 = explanation_template.replace('[UNIQUE_ID_1]', 'b30001') \
                         .replace('[UNIQUE_ID_2]', 'b30002') \
                         .replace('[UNIQUE_ID_3]', 'b30003') \
                         .replace('[UNIQUE_ID_4]', 'b30004') \
                         .replace('[UNIQUE_ID_5]', 'b30005') \
                         .replace('[UNIQUE_ID_6]', 'b30006') \
                         .replace('[POEM_VERSE_HEMISTICHS]', '<span>المقطع الثاني</span>') \
                         .replace('[EXPLANATION_CONTENT_ITEMS]', '<li>الكادِحُونَ يَتَجَرَّعُونَ مَرَارَةَ الْمُعَانَاةِ وَعَلْقَمَ الحرمان وعذابَ الفَقْرِ والعَوَزِ، وَمَعَ كُل ذلك يَكْدَحُونَ لِيَصْنَعُوا السَّعَادَةَ لِغَيْرِهِم فَهُم مَنْ يَصْنَعُونَ زَوْرَقَ العاشق الحالم ، وهُم مَنْ يَنْسِجُونَ مِنْدِيلَ العِشْقِ لِكَلِفٍ مُولَعٍ مُغْرَمٍ.</li><li>إن هؤلاء الكادِحِينَ يَتَحَدَّونَ جَحِيمَ المعاناةِ، وَيَقْهَرُونَ قَسْوَةَ الأَلَمِ، فَيَصْنَعُونَ لَأَنْفُسِهِمُ الْمُسَرَّاتِ فَمَعَ أَنَّ كَفَّ القَدَرِ قَدْ أَلْقَتْ بِهِم في بقاع الأَرْضِ فَجَعَلَتْ رَحى الشَّقَاءِ تَعْرُكُ جَهْدَهُم فِي مَصَانِعِ الحَدِيدِ ومناجم الفحم، وتطحن قواهم تَحْتَ أَشِعَةِ الشَّمْسِ الحارقة، غير أن السعادة تملأ أعماقهم وتعمر أنفسهم لِأَنَّهُم يَحْلُمُونَ بِأَحْلامٍ مُتَوَاضِعَةٍ، فلا يَحْلُمُونَ أَحْلَامَ أَهْلِ الغَرَامِ المِثَالِيَّةِ.</li>') \
                         .replace('[IRAB_CONTENT_ITEMS]', '')

m3 = explanation_template.replace('[UNIQUE_ID_1]', 'b40001') \
                         .replace('[UNIQUE_ID_2]', 'b40002') \
                         .replace('[UNIQUE_ID_3]', 'b40003') \
                         .replace('[UNIQUE_ID_4]', 'b40004') \
                         .replace('[UNIQUE_ID_5]', 'b40005') \
                         .replace('[UNIQUE_ID_6]', 'b40006') \
                         .replace('[POEM_VERSE_HEMISTICHS]', '<span>المقطع الثالث</span>') \
                         .replace('[EXPLANATION_CONTENT_ITEMS]', '<li>إن هؤلاء الكادِحِينَ يَصْنَعُونَ لِأَنْفُسِهِم الأَفْرَاحَ وَالمَسَرَّاتِ على الرَّغْمِ مِنَ المعاناة والأَلَمِ اللَّذِينَ يُحِيطَانِ بِحَيَاتِهِم لِأَنَّهُم يَحْلُمُونَ أَحْلَامًا بَسِيطَةً مُتَوَاضِعَةً؛ فهم لا يَحْلُمُونَ إِلَّا بالحصولِ على لُقْمَةِ عَيْشِ تُقِيتُهُم وَتُسْكِنُ أَصْلَابَهُم.</li>') \
                         .replace('[IRAB_CONTENT_ITEMS]', '')

plan_content = f'''# **SESSION 001.3**

[TASK DEFINITION]
Objective: Implement Part 3 of المهاجر.
File: `pages/001.3_nXXX_المهاجر.html`
Reference: Follow patterns in design_patterns.json.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: TEMPLATE_C_HEADER.html ===
(Component: TEMPLATE_C_HEADER.html)
{header}

=== BLOCK 2: TEMPLATE_LIT_PART_3_EXPLANATION.html ===
(Component: TEMPLATE_LIT_PART_3_EXPLANATION.html)
{m1}

=== BLOCK 3: TEMPLATE_LIT_PART_3_EXPLANATION.html ===
(Component: TEMPLATE_LIT_PART_3_EXPLANATION.html)
{m2}

=== BLOCK 4: TEMPLATE_LIT_PART_3_EXPLANATION.html ===
(Component: TEMPLATE_LIT_PART_3_EXPLANATION.html)
{m3}

--- END STREAM ---'''

with open('plans/001.3_nXXX_المهاجر-plan_7p16l.md', 'w', encoding='utf-8') as f:
    f.write(plan_content)
