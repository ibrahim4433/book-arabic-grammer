import os

with open('Jules-workspace/Templates/TEMPLATE_C_HEADER.html', 'r', encoding='utf-8') as f:
    header_tpl = f.read()
with open('Jules-workspace/Part-Templates/TEMPLATE_LIT_PART_1_POEM.html', 'r', encoding='utf-8') as f:
    poem_tpl = f.read()

# Strictly inject the exact metadata variables as requested in the prompt
header_tpl = header_tpl.replace('[LEVEL_INFO]', '[CATEGORY_HEADER]') \
                       .replace('[TOPIC_INFO]', '[SECTION_HEADER]') \
                       .replace('[AUTHOR_CONTACT]', '[AUTHOR_PHONE]') \
                       .replace('[MAIN_TITLE]', '[CHAPTER_TITLE]')

header = header_tpl.replace('[UNIQUE_ID]', 'b00001') \
                   .replace('[CATEGORY_HEADER]', 'المستوى التأسيسي') \
                   .replace('[SECTION_HEADER]', 'الأدب والنصوص') \
                   .replace('[AUTHOR_NAME]', 'أ. حنا خفيف') \
                   .replace('[AUTHOR_PHONE]', '') \
                   .replace('[CHAPTER_TITLE]', 'المهاجر') \
                   .replace('[LESSON_NUMBER]', '001')

verses = [
    "المَلَايِينُ الَّتِي تَكْدَحُ، لَا تَحْلُمُ فِي مَوْتِ فَرَاشَةٍ",
    "وَبِأَحْزَانِ البَنَفْسَجْ",
    "أَوْ شِرَاعٍ يَتَوَهَّجْ",
    "تَحْتَ ضَوْءِ القَمَرِ الأَخْضَرِ فِي لَيْلَةِ صَيْفٍ",
    "أَوْ غَرَامِيَّاتِ مَجْنُونٍ بِطَيْفِ",
    "المَلَايِينُ الَّتِي تَكْدَحُ",
    "تَعْرَى",
    "تَتَمَزَّقُ",
    "المَلَايِينُ الَّتِي تَصْنَعُ لِلْحَالِمِ زَوْرَقْ",
    "المَلَايِينُ الَّتِي تَصْنَعُ مِنْدِيلاً لِمُغْرَمْ",
    "المَلَايِينُ الَّتِي تَبْكِي",
    "تُغَنِّي",
    "تَتَأَلَّمْ",
    "فِي زَوَايَا الأَرْضِ، فِي مَصْنَعِ صُلْبٍ، أَوْ بِمَنْجَمْ",
    "إِنَّهَا تَصْنَعُ قُرْصَ الشَّمْسِ مِنْ مَوْتٍ مُحَتَّمْ",
    "إِنَّهَا تَضْحَكُ مِنْ أَعْمَاقِهَا",
    "تَضْحَكُ",
    "تُغْرَمْ",
    "لَا كَمَا يُغْرَمُ مَجْنُونٌ بِطَيْفِ",
    "تَحْتَ ضَوْءِ القَمَرِ الأَخْضَرِ فِي لَيْلَةِ صَيْفِ",
    "المَلَايِينُ الَّتِي تَبْكِي",
    "تُغَنِّي",
    "تَتَأَلَّمْ",
    "تَحْتَ شَمْسِ اللَّيْلِ بِاللُّقْمَةِ تَحْلُم"
]

poem_verses_html = ""
for verse in verses:
    poem_verses_html += f'<div class="poem-line"><span class="hemistich">{verse}</span><span class="hemistich"></span></div>\n'

poem = poem_tpl.replace('[UNIQUE_ID_1]', 'b00002') \
               .replace('[UNIQUE_ID_2]', 'b00003') \
               .replace('[UNIQUE_ID_3]', 'b00004') \
               .replace('[UNIQUE_ID_4]', 'b00005') \
               .replace('[UNIQUE_ID_5]', 'b00006') \
               .replace('[POET_NAME]', 'عَبْد الوَهَّاب البَيَّاتِي') \
               .replace('[POET_DATES]', '') \
               .replace('[POET_BIO_LIST]', '') \
               .replace('[INTRO_LIST]', '<li>الحجمة</li>') \
               .replace('[LESSON_NUMBER]', '001') \
               .replace('[POEM_VERSES]', poem_verses_html)

plan = f'''# **SESSION 001.1**

[TASK DEFINITION]
Objective: Implement Part 1 of المهاجر.
File: `pages/001.1_nXXX_المهاجر.html`
Reference: Follow patterns in design_patterns.json.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: TEMPLATE_C_HEADER.html ===
(Component: TEMPLATE_C_HEADER.html)
{header}

=== BLOCK 2: TEMPLATE_LIT_PART_1_POEM.html ===
(Component: TEMPLATE_LIT_PART_1_POEM.html)
{poem}

--- END STREAM ---
'''
os.makedirs('plans', exist_ok=True)
with open('plans/001.1_nXXX_المهاجر-plan_7p16l.md', 'w', encoding='utf-8') as f:
    f.write(plan)
