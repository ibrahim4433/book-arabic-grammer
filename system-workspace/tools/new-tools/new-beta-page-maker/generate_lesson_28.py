import os
import re
import sys
import json
import subprocess

# Ensure we can find modules
sys.path.append(os.path.join(os.getcwd(), 'Jules-workspace'))

OUTPUT_DIR = "pages"
TEMPLATE_DIR = "Jules-workspace/Templates"

# Load Templates
def load_template(name):
    path = os.path.join(TEMPLATE_DIR, name)
    if not os.path.exists(path):
        print(f"Error: Template {name} not found.")
        sys.exit(1)
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

T_BASE = load_template("TEMPLATE_C_BASE.html")
T_HEADER = load_template("TEMPLATE_C_HEADER.html")
T_BLOCK = load_template("TEMPLATE_C_BLOCK.html")
# Fix: Remove <p> wrapper from block template to allow rich content
T_BLOCK = re.sub(r'<p class="mt-1mm text-accent">\s*\[CONTENT_TEXT\]\s*</p>', '[CONTENT_TEXT]', T_BLOCK)

T_CHIPS = load_template("TEMPLATE_C_CHIPS.html")
T_TABLE = load_template("TEMPLATE_C_TABLE.html")
T_SPLIT = load_template("TEMPLATE_C_SPLIT.html")
T_BENEFIT_TIP = load_template("TEMPLATE_C_BENEFIT_TIP.html")
T_POEM = load_template("TEMPLATE_C_POEM.html")
T_IRAB_ROW = load_template("TEMPLATE_C_IRAB_ROW.html")
T_EXAM = load_template("TEMPLATE_C_EXAM.html")

# Blocks Data
blocks = [
    # Block 1: Header
    {
        "type": "HEADER",
        "data": {
            "[LESSON_NUMBER]": "28",
            "[CHAPTER_TITLE]": "الصُّورَةُ البَيَانِيَّةُ",
            "[CATEGORY_HEADER]": "فَوَائِدُ",
            "[SECTION_HEADER]": "المُسْتَوَى الفَنِّيُّ",
            "[AUTHOR_NAME]": "أ. اليَاس خَفِيف",
            "[AUTHOR_PHONE]": " "
        }
    },
    # Block 2: Definition of Imagery
    {
        "type": "BLOCK",
        "id": "b28001",
        "title": "عِلْمُ البَيَانِ",
        "content": '<p class="text-accent font-bold text-justify mb-4mm">عِلْمُ البَيَانِ فِي البَلَاغَةِ العَرَبِيَّةِ يَدْرُسُ الصُّورَةَ البَيَانِيَّةَ (الفَنِّيَّةَ). وَيُقْسَمُ إِلَى ثَلَاثَةِ أَقْسَامٍ هِيَ: (التَّشْبِيهُ، وَالاسْتِعَارَةُ، وَالكِنَايَةُ).</p>'
    },
    # Block 3: Simile Definition
    {
        "type": "BLOCK",
        "id": "b28002",
        "title": "أَوَّلًا - التَّشْبِيهُ",
        "content": '<p class="text-accent font-bold text-justify mb-4mm">هُوَ عَقْدُ مُقَارَنَةٍ بَيْنَ شَيْئَيْنِ اشْتَرَكَا بِصِفَةٍ وَاحِدَةٍ، وَتَكُونُ هَذِهِ الصِّفَةُ فِي المُشَبَّهِ بِهِ أَقْوَى مِنْهَا فِي المُشَبَّهِ. نَحْوَ: خَالِدٌ كَالبَحْرِ فِي الجُودِ.</p>\n<div class="benefit-box bg-grey-lighter p-2mm rounded border-light mb-4mm">\n    <h4 class="text-primary font-bold mb-2mm">أَرْكَانُ التَّشْبِيهِ:</h4>\n    <p class="text-dark">المُشَبَّهُ، وَالمُشَبَّهُ بِهِ (وَهُمَا الرُّكْنَانِ الأَسَاسِيَّانِ)، وَالأَدَاةُ، وَوَجْهُ الشَّبَهِ.</p>\n</div>'
    },
    # Block 4: Simile Tools (Chips)
    {
        "type": "CHIPS",
        "id": "b28003",
        "title": "أَدَوَاتُ التَّشْبِيهِ",
        "content_raw": "الكَافُ | كَأَنَّ | مِثْلُ | شِبْهُ | أَشْبَهُ | شَبِيهُ | يُشْبِهُ | شَابَهَ | حَاكَى | يُحَاكِي | مَاثَلَ | يُمَاثِلُ"
    },
    # Block 5: Simile Types Matrix
    {
        "type": "TABLE",
        "id": "b28004",
        "title": "أَنْوَاعُ التَّشْبِيهِ (بِحَسَبِ الأَرْكَانِ)",
        "headers": ["النَّوْعُ", "التَّعْرِيفُ", "المِثَالُ"],
        "rows_html": """
<tr>
    <td class="font-bold text-primary">تَشْبِيهٌ تَامُّ الأَرْكَانِ</td>
    <td>هُوَ الَّذِي يَشْتَمِلُ عَلَى الأَرْكَانِ الأَرْبَعَةِ.</td>
    <td>خَالِدٌ <span class="highlight-red">مِثْلُ</span> البَحْرِ <span class="highlight-blue">فِي الجُودِ</span>.</td>
</tr>
<tr>
    <td class="font-bold text-primary">تَشْبِيهٌ مُؤَكَّدٌ</td>
    <td>هُوَ الَّذِي حُذِفَتْ مِنْهُ الأَدَاةُ.</td>
    <td>خَالِدٌ ... بَحْرٌ <span class="highlight-blue">فِي الجُودِ</span>.</td>
</tr>
<tr>
    <td class="font-bold text-primary">تَشْبِيهٌ مُجْمَلٌ</td>
    <td>هُوَ الَّذِي حُذِفَ مِنْهُ وَجْهُ الشَّبَهِ.</td>
    <td>خَالِدٌ <span class="highlight-red">مِثْلُ</span> البَحْرِ ...</td>
</tr>
<tr>
    <td class="font-bold text-primary">تَشْبِيهٌ بَلِيغٌ</td>
    <td>هُوَ الَّذِي حُذِفَتْ مِنْهُ الأَدَاةُ وَوَجْهُ الشَّبَهِ.</td>
    <td>خَالِدٌ ... بَحْرٌ ...</td>
</tr>
"""
    },
    # Block 6: Representative Simile
    {
        "type": "BLOCK",
        "id": "b28005",
        "title": "التَّشْبِيهُ التَّمْثِيلِيُّ",
        "content": '<p class="text-accent font-bold text-justify mb-2mm">هُوَ مَا كَانَ وَجْهُ الشَّبَهِ فِيهِ هَيْئَةً مُنْتَزَعَةً مِنْ مُتَعَدِّدٍ؛ أَيْ هُوَ تَشْبِيهُ صُورَةٍ بِصُورَةٍ أُخْرَى.</p>\n<div class="poem-container mb-2mm">\n    <div class="poem-line flex justify-between items-center mb-2mm">\n        <div class="hemistich w-45pct text-center font-bold">تَمْشِي المَصَالِحُ فِي أَقْلَامِ دَوْلَتِنَا</div>\n        <div class="hemistich w-45pct text-center font-bold">مَشْيَ الخَنَافِسِ فِي جَزٍّ مِنَ الصُّوفِ</div>\n    </div>\n</div>\n<ul class="structured-list p-0">\n    <li class="mb-1mm"><span class="marker">•</span><span class="font-bold text-primary">المُشَبَّهُ:</span> صُورَةُ سَيْرِ المُعَامَلَاتِ الرَّسْمِيَّةِ فِي الدَّوَائِرِ الحُكُومِيَّةِ.</li>\n    <li class="mb-1mm"><span class="marker">•</span><span class="font-bold text-primary">المُشَبَّهُ بِهِ:</span> صُورَةُ مَشْيِ الخُنْفُسَاءِ فِي جَزٍّ مِنَ الصُّوفِ.</li>\n    <li class="mb-1mm"><span class="marker">•</span><span class="font-bold text-primary">وَجْهُ الشَّبَهِ:</span> بُطْءُ السَّيْرِ وَالتَّعَثُّرِ.</li>\n</ul>'
    },
    # Block 7: Metaphor Intro
    {
        "type": "BLOCK",
        "id": "b28006",
        "title": "ثَانِيًا - الاسْتِعَارَةُ",
        "content": '<p class="text-accent font-bold text-justify">هِيَ تَشْبِيهٌ بَلِيغٌ، حُذِفَ مِنْهُ أَحَدُ رُكْنَيْهِ (المُشَبَّهُ، أَوْ المُشَبَّهُ بِهِ)، وَلَهَا نَوْعَانِ:</p>'
    },
    # Block 8: Metaphor Types Split
    {
        "type": "BLOCK",
        "id": "b28007_title",
        "title": "أَنْوَاعُ الاسْتِعَارَةِ",
        "content": ""
    },
    {
        "type": "SPLIT",
        "id": "b28007",
        "left_title": "اسْتِعَارَةٌ تَصْرِيحِيَّةٌ",
        "left_content": '<p class="text-justify mb-2mm">فِيهَا يُحْذَفُ <span class="highlight-red">المُشَبَّهُ</span>، وَيُصَرَّحُ بِالمُشَبَّهِ بِهِ.</p><p class="text-sm text-grey mb-1mm">مِثَالٌ (أَحْمَد شَوْقِي):</p><p class="font-bold text-center mb-1mm">يَا أَيُّهَا السَّيْفُ المُجَرَّدُ فِي الفَلَا</p><p class="text-sm text-grey">شَبَّهَ المُجَاهِدَ (مَحْذُوف) بِالسَّيْفِ (مُصَرَّح بِهِ).</p>',
        "right_title": "اسْتِعَارَةٌ مَكْنِيَّةٌ",
        "right_content": '<p class="text-justify mb-2mm">فِيهَا يُحْذَفُ <span class="highlight-red">المُشَبَّهُ بِهِ</span>، وَتَبْقَى إِحْدَى قَرَائِنِهِ (صِفَاتِهِ) تَدُلُّ عَلَيْهِ.</p><p class="text-sm text-grey mb-1mm">مِثَالٌ (بِشَارَة الخُورِي):</p><p class="font-bold text-center mb-1mm">يَا جِهَادًا صَفَّقَ المَجْدُ لَهُ</p><p class="text-sm text-grey">شَبَّهَ المَجْدَ بِإِنْسَانٍ (مَحْذُوف) وَأَبْقَى صِفَةَ التَّصْفِيقِ.</p>'
    },
    # Block 9: Personification & Embodiment Split
    {
        "type": "BLOCK",
        "id": "b28008_title",
        "title": "التَّشْخِيصُ وَالتَّجْسِيمُ",
        "content": ""
    },
    {
        "type": "SPLIT",
        "id": "b28008",
        "left_title": "التَّشْخِيصُ",
        "left_content": '<p class="text-justify mb-2mm">هُوَ مَنْحُ الحَيَاةِ لِغَيْرِ الإِنْسَانِ، وَمَنْحُ صِفَاتِ الأَشْخَاصِ لِلْجَمَادِ.</p><ul class="structured-list text-sm"><li><span class="marker">•</span>أَشْوَاقُ السَّنَابِلِ</li><li><span class="marker">•</span>نَبْضُ المَصَانِعِ</li></ul><p class="mt-2mm text-xs text-grey">وَظِيفَتُهُ: تَوْكِيدُ المَعْنَى وَإِبْرَازُهُ.</p>',
        "right_title": "التَّجْسِيمُ",
        "right_content": '<p class="text-justify mb-2mm">هُوَ تَحْوِيلُ الأَشْيَاءِ المَعْنَوِيَّةِ مِنْ مَجَالِهَا التَّجْرِيدِيِّ إِلَى مَجَالٍ آخَرَ حِسِّيٍّ.</p><p class="font-bold text-center mb-1mm">وَتَصُبُّ الحَيَاةَ فِي مَسْمَعَيَّا</p><p class="text-sm text-grey">شَبَّهَ الحَيَاةَ (مَعْنَوِيّ) بِمَاءٍ يُصَبُّ (حِسِّيّ).</p>'
    },
    # Block 10: Functions Intro
    {
        "type": "BLOCK",
        "id": "b28009",
        "title": "وَظِيفَةُ الصُّورَةِ البَيَانِيَّةِ (القِيمَةُ الفَنِّيَّةُ)",
        "content": '<p class="text-justify">لِلصُّورَةِ البَيَانِيَّةِ (التَّشْبِيه، الاسْتِعَارَة) وَظَائِفُ مُتَعَدِّدَةٌ تُبْرِزُ المَعْنَى وَتُؤَثِّرُ فِي المُتَلَقِّي، مِنْهَا:</p>'
    },
    # Block 11: Function - Explanation
    {
        "type": "BLOCK",
        "id": "b28010",
        "title": "١- الشَّرْحُ وَالتَّوْضِيحُ",
        "content": '<p class="text-justify mb-2mm">تُعَدُّ خُطْوَةً أَوَّلِيَّةً فِي إِقْنَاعِ المُتَلَقِّي بِمَعْنًى مِنَ المَعَانِي، حَيْثُ تَنْتَقِلُ الصُّورَةُ مِنَ الوَاضِحِ إِلَى الأَوْضَحِ.</p>'
    },
    {
        "type": "TIP",
        "title": "القَالِبُ النَّظَرِيُّ للإِجَابَةِ",
        "content": "شَرَحَتِ الصُّورَةُ مَعْنَى: (... [المَعْنَى/الفِكْرَة] ...) وَوَضَّحَتْ ذَلِكَ المَعْنَى مِنْ خِلَالِ تَشْبِيهِ ... [المُشَبَّهُ] ... بِـ ... [المُشَبَّهُ بِهِ] ...، فَأَقْنَعَتِ المُتَلَقِّيَ بِمَضْمُونِ المَعْنَى وَصِدْقِهِ."
    },
    # Block 12: Function - Exaggeration
    {
        "type": "BLOCK",
        "id": "b28011",
        "title": "٢- المُبَالَغَةُ",
        "content": '<p class="text-justify mb-2mm">يُقْصَدُ بِهَا التَّعْبِيرُ عَنِ الشَّيْءِ بِصُورَتِهِ العُلْيَا (المَثَلِ الأَعْلَى)، حَتَّى يُصْبِحَ الغَائِبُ حَاضِرًا وَالمُتَخَيَّلُ مُتَحَقِّقًا.</p>'
    },
    {
        "type": "TIP",
        "title": "القَالِبُ النَّظَرِيُّ للإِجَابَةِ",
        "content": "بَالَغَ الشَّاعِرُ فِي شَرْحِ مَعْنَى: (... [المَعْنَى] ...) وَتَوْضِيحِهِ بِتَشْبِيهِهِ ... [المُشَبَّهُ] ... بِـ ... [المُشَبَّهُ بِهِ] ...، حَيْثُ أَرَادَ أَنْ يُوصِلَ إِلَى المُتَلَقِّي الحَدَّ الأَعْلَى مِنْ ... [الصِّفَة] ...، فَجَعَلَ المُتَخَيَّلَ كَالمُتَحَقِّقِ."
    },
    # Block 13: Functions - Beautification & Uglification
    {
        "type": "BLOCK",
        "id": "b28012_title",
        "title": "٣- التَّحْسِينُ وَالتَّقْبِيحُ",
        "content": ""
    },
    {
        "type": "SPLIT",
        "id": "b28012",
        "left_title": "التَّحْسِينُ",
        "left_content": '<p class="text-justify mb-2mm">جَعْلُ الحَسَنِ يَجْرِي فِي الصُّورَةِ لِجَذْبِ المُتَلَقِّي واسْتِمَالَتِهِ.</p><div class="bg-grey-lighter p-2mm rounded border-light text-sm"><span class="font-bold text-accent">القَالِبُ:</span> حَسَّنَ الشَّاعِرُ مَعْنَى (...) بِتَشْبِيهِهِ (...) بـ (...)، فَأَثَّرَ ذَلِكَ فِي المُتَلَقِّي، وَأَثَارَ انْفِعَالَ (الحُبِّ/الإِعْجَابِ)، وَأَدَّى إِلَى جَذْبِهِ واسْتِمَالَتِهِ.</div>',
        "right_title": "التَّقْبِيحُ",
        "right_content": '<p class="text-justify mb-2mm">جَعْلُ القُبْحِ يَجْرِي فِي الصُّورَةِ لِلتَّنْفِيرِ مِنْهَا.</p><div class="bg-grey-lighter p-2mm rounded border-light text-sm"><span class="font-bold text-accent">القَالِبُ:</span> قَبَّحَ الشَّاعِرُ مَعْنَى (...) بِتَشْبِيهِهِ (...) بـ (...)، فَأَثَّرَ ذَلِكَ فِي المُتَلَقِّي، وَأَثَارَ انْفِعَالَ (الكُرْهِ/الاشْمِئْزَازِ)، وَأَدَّى إِلَى نُفُورِهِ.</div>'
    },
    # Block 14: Functions - Description & Suggestion
    {
        "type": "BLOCK",
        "id": "b28013_title",
        "title": "٤- الوَصْفُ وَالإِيحَاءُ",
        "content": ""
    },
    {
        "type": "SPLIT",
        "id": "b28013",
        "left_title": "الوَصْفُ وَالمُحَاكَاةُ",
        "left_content": '<p class="text-justify mb-2mm">تَظْهَرُ عِنْدَ الاتِّبَاعِيِّينَ، حَيْثُ تَسْتَمِدُّ الصُّوَرُ عَنَاصِرَهَا مِنَ الوَاقِعِ المَحْسُوسِ.</p><div class="bg-grey-lighter p-2mm rounded border-light text-sm"><span class="font-bold text-primary">القَالِبُ:</span> اسْتَمَدَّتِ الصُّورَةُ عَنَاصِرَهَا مِنَ الوَاقِعِ المَحْسُوسِ (المُحَاكَاة)، حَيْثُ شَبَّهَ (...) بـ (...)، وَكِلَاهُمَا عُنْصُرَانِ حِسِّيَّانِ.</div>',
        "right_title": "الإِيحَاءُ",
        "right_content": '<p class="text-justify mb-2mm">تَظْهَرُ عِنْدَ الإِبْدَاعِيِّينَ، فَتُوحِي بِدِلَالَاتٍ مَعْنَوِيَّةٍ وَتُثِيرُ المَشَاعِرَ.</p><div class="bg-grey-lighter p-2mm rounded border-light text-sm"><span class="font-bold text-primary">القَالِبُ:</span> جَعَلَ الشَّاعِرُ الصُّورَةَ مُوحِيَةً بِتَشْبِيهِ (...) بـ (...)، فَهَذَا أَوْحَى بِـ (... وَ ...)، وَأَثَارَ مَشَاعِرَ (...).</div>'
    },
    # Block 15: Functions - Projection & Symbolism
    {
        "type": "BLOCK",
        "id": "b28014_title",
        "title": "٥- إِضْفَاءُ النَّفْسِيَّةِ وَالرَّمْزُ",
        "content": ""
    },
    {
        "type": "SPLIT",
        "id": "b28014",
        "left_title": "إِضْفَاءُ نَفْسِيَّةِ المُبْدِعِ",
        "left_content": '<p class="text-justify mb-2mm">تَنْقُلُ الطَّبِيعَةَ وَالأَشْيَاءَ بَعْدَ انْفِعَالِ المُبْدِعِ بِهَا، فَتَتَلَوَّنُ بِمَشَاعِرِهِ.</p><div class="bg-grey-lighter p-2mm rounded border-light text-sm"><span class="font-bold text-primary">القَالِبُ:</span> شَخَّصَ الشَّاعِرُ (...) وَنَقَلَهُ بَعْدَ انْفِعَالِهِ بِهِ، فَتَلَوَّنَ بِمَشَاعِرِهِ وَرُؤَاهُ، حَيْثُ أَضْفَى عَلَيْهِ مَشَاعِرَ (...).</div>',
        "right_title": "الرَّمْزُ",
        "right_content": '<p class="text-justify mb-2mm">وَسِيلَةٌ لِلإِشَارَةِ وَالاخْتِصَارِ وَالتَّكْثِيفِ، تَخْتَبِئُ فِيهَا الدَّلَالَاتُ.</p><div class="bg-grey-lighter p-2mm rounded border-light text-sm"><span class="font-bold text-primary">القَالِبُ:</span> رَمَزَ الشَّاعِرُ بـ (...) لـِ (...)، فَاخْتَصَرَ الكَلَامَ، وَكَثَّفَ المَعْنَى، وَأَوْحَى بِدِلَالَاتٍ مُخْتَلِفَةٍ.</div>'
    },
    # Block 16: Metonymy Intro
    {
        "type": "BLOCK",
        "id": "b28015",
        "title": "ثَالِثًا - الكِنَايَةُ",
        "content": '<p class="text-accent font-bold text-justify mb-2mm">هِيَ كَلَامٌ أُطْلِقَ، وَأُرِيدَ مَا يُلَازِمُهُ مِنْ مَعْنًى، مَعَ جَوَازِ إِرَادَةِ المَعْنَى الحَقِيقِيِّ. وَهِيَ تَعْبِيرٌ عَنِ المَعْنَى تَلْمِيحًا لَا تَصْرِيحًا.</p>\n<div class="bg-grey-lighter p-2mm rounded border-light"><span class="font-bold text-accent">القِيمَةُ الفَنِّيَّةُ:</span> تَقْرِيبُ المَعْنَى مِنَ الذِّهْنِ، وَتَأْكِيدُهُ.</div>'
    },
    # Block 17: Metonymy Types Matrix
    {
        "type": "TABLE",
        "id": "b28016",
        "title": "أَنْوَاعُ الكِنَايَةِ",
        "headers": ["النَّوْعُ", "الشَّرْحُ", "المِثَالُ"],
        "rows_html": """
<tr>
    <td class="font-bold text-primary">كِنَايَةٌ عَنْ صِفَةٍ</td>
    <td>المُكَنَّى عَنْهُ صِفَةٌ مَعْنَوِيَّةٌ (كَالشَّجَاعَةِ، الجُودِ...).</td>
    <td>طَوِيلُ النِّجَادِ رَفِيعُ العِمَادِ.<br><span class="text-xs text-grey">(كِنَايَةٌ عَنْ طُولِ القَامَةِ وَعِظَمِ الشَّأْنِ)</span></td>
</tr>
<tr>
    <td class="font-bold text-primary">كِنَايَةٌ عَنْ مَوْصُوفٍ</td>
    <td>يُطْلَبُ بِهَا المَوْصُوفُ نَفْسُهُ (اسْمُ ذَاتٍ).</td>
    <td>يَا أُمَّ الحَضَارَةِ.<br><span class="text-xs text-grey">(كِنَايَةٌ عَنْ مَدِينَةِ دِمَشْقَ)</span></td>
</tr>
<tr>
    <td class="font-bold text-primary">كِنَايَةٌ عَنْ نِسْبَةٍ</td>
    <td>نِسْبَةُ أَمْرٍ لِآخَرَ، أَوْ نَفْيُهُ عَنْهُ.</td>
    <td>المَجْدُ بَيْنَ ثَوْبَيْهِ.<br><span class="text-xs text-grey">(نِسْبَةُ المَجْدِ إِلَى المَمْدُوحِ)</span></td>
</tr>
"""
    },
    # Block 18: Evidence Poem
    {
        "type": "POEM",
        "id": "b28017",
        "title": "شَوَاهِدُ تَطْبِيقِيَّةٌ",
        "verses": """
<div class="poem-line flex justify-between items-center mb-2mm">
    <div class="hemistich w-45pct text-center font-bold">كُلَّمَا قُلْتُ فِي غَدٍ أُدْرِكُ السُّؤْ</div>
    <div class="hemistich w-45pct text-center font-bold">لَ أَتَانِي غَدٌ بِمَا لَا أَشَاءُ</div>
</div>
    <div class="poem-line flex justify-between items-center mb-2mm">
    <div class="hemistich w-45pct text-center font-bold">كُنْ هَزَارًا فِي عُشِّهِ يَتَغَنَّى</div>
    <div class="hemistich w-45pct text-center font-bold">وَمَعَ الكَبْلِ لَا يُبَالِي الكُبُولَا</div>
</div>
<div class="poem-line flex justify-between items-center mb-2mm">
    <div class="hemistich w-45pct text-center font-bold">هَاهُنَا وَارَيْتُ أَجْدَادِي هُنَا</div>
    <div class="hemistich w-45pct text-center font-bold">وَهُمُ اخْتَارُوا ثَرَاهَا كَفَنَا</div>
</div>
"""
    },
    # Block 19: Rhetorical Analysis
    {
        "type": "IRAB",
        "id": "b28018",
        "title": "التَّحْلِيلُ البَلَاغِيُّ لِلشَّوَاهِدِ",
        "boxes": """
<div class="irab-box flex-1 bg-white border-light rounded text-center">
    <div class="irab-word bg-primary text-white p-2mm font-bold rounded">أَتَانِي غَدٌ</div>
    <div class="irab-details p-2mm text-sm">
        <span class="font-bold text-accent">اسْتِعَارَةٌ مَكْنِيَّةٌ</span><br>
        شَبَّهَ الغَدَ بِإِنْسَانٍ يَأْتِي، فَحَذَفَ المُشَبَّهَ بِهِ وَأَبْقَى لَازِمَةً (أَتَانِي).<br>
        <span class="text-xs text-grey">الوَظِيفَةُ: التَّشْخِيصُ وَالتَّوْضِيحُ.</span>
    </div>
</div>
<div class="irab-box flex-1 bg-white border-light rounded text-center">
    <div class="irab-word bg-primary text-white p-2mm font-bold rounded">كُنْ هَزَارًا</div>
    <div class="irab-details p-2mm text-sm">
        <span class="font-bold text-accent">تَشْبِيهٌ مُؤَكَّدٌ</span><br>
        شَبَّهَ المُخَاطَبَ بِالهَزَارِ، وَحَذَفَ الأَدَاةَ.<br>
        <span class="text-xs text-grey">الوَظِيفَةُ: التَّحْسِينُ وَالتَّوْضِيحُ.</span>
    </div>
</div>
<div class="irab-box flex-1 bg-white border-light rounded text-center">
    <div class="irab-word bg-primary text-white p-2mm font-bold rounded">ثَرَاهَا كَفَنَا</div>
    <div class="irab-details p-2mm text-sm">
        <span class="font-bold text-accent">تَشْبِيهٌ بَلِيغٌ</span><br>
        شَبَّهَ الثَّرَى بِالكَفَنِ، حُذِفَتِ الأَدَاةُ وَوَجْهُ الشَّبَهِ.<br>
        <span class="text-xs text-grey">الوَظِيفَةُ: الإِيحَاءُ بِالتَّضْحِيَةِ.</span>
    </div>
</div>
"""
    },
    # Block 20: Exam
    {
        "type": "EXAM",
        "id": "b28019",
        "topic": "الصورة البيانية",
        "questions": [
            "س١- اسْتَخْرِجِ الصُّورَةَ البَيَانِيَّةَ مِنْ قَوْلِهِ: (رَايَاتُنَا بَصَرُ الضَّرِيرِ)، وَسَمِّهَا، وَحَلِّلْهَا.",
            "س٢- مَيِّزِ التَّشْخِيصَ مِنَ التَّجْسِيمِ فِي العِبَارَتَيْنِ: (أَشْوَاقُ سُنْبُلَةٍ)، (يَصُبُّ فِيهَا النُّورَ).",
            "س٣- اشْرَحْ وَظِيفَةَ \"الشَّرْحِ وَالتَّوْضِيحِ\" فِي قَوْلِ الشَّاعِرَةِ: (أَغْرَقُ فِي بَحْرِ يَأْسٍ).",
            "س٤- هَاتِ مِنَ الأَبْيَاتِ مِثَالًا لِكِنَايَةٍ عَنْ نِسْبَةٍ."
        ]
    },
    # Block 21: Summary Table (Filler)
    {
        "type": "TABLE",
        "id": "b28020",
        "title": "مُلَخَّصُ البَحْثِ (مُقَارَنَة)",
        "headers": ["الصُّورَةُ", "الأَسَاسُ", "الوَظِيفَةُ"],
        "rows_html": """
<tr>
    <td class="font-bold text-primary">التَّشْبِيهُ</td>
    <td>المُشَارَكَةُ فِي الصِّفَةِ</td>
    <td>التَّوْضِيحُ وَالتَّحْسِينُ</td>
</tr>
<tr>
    <td class="font-bold text-primary">الاسْتِعَارَةُ</td>
    <td>المُشَابَهَةُ (حَذْفُ أَحَدِ الطَّرَفَيْنِ)</td>
    <td>التَّشْخِيصُ وَالتَّجْسِيمُ</td>
</tr>
<tr>
    <td class="font-bold text-primary">الكِنَايَةُ</td>
    <td>التَّلَازُمُ بَيْنَ اللِّفْظِ وَمَعْنَاهُ</td>
    <td>تَقْرِيبُ المَعْنَى وَتَأْكِيدُهُ</td>
</tr>
"""
    },
    # Block 22: Solved Exercises (Filler)
    {
        "type": "BLOCK",
        "id": "b28021",
        "title": "نَمَاذِجُ مُجَابَةٌ",
        "content": """<ul class="structured-list">
    <li class="mb-2mm"><span class="marker">•</span><span class="font-bold">«العِلْمُ نُورٌ»</span>: <span class="text-primary">تَشْبِيهٌ بَلِيغٌ</span>؛ حُذِفَتِ الأَدَاةُ وَوَجْهُ الشَّبَهِ.</li>
    <li class="mb-2mm"><span class="marker">•</span><span class="font-bold">«ضَحِكَ الزَّمَانُ»</span>: <span class="text-primary">اسْتِعَارَةٌ مَكْنِيَّةٌ</span>؛ شَبَّهَ الزَّمَانَ بِإِنْسَانٍ يَضْحَكُ.</li>
    <li class="mb-2mm"><span class="marker">•</span><span class="font-bold">«فُلَانٌ كَثِيرُ الرَّمَادِ»</span>: <span class="text-primary">كِنَايَةٌ عَنْ صِفَةِ</span> الكَرَمِ وَالجُودِ.</li>
</ul>"""
    },
    # Block 23: Warning (Filler)
    {
        "type": "BLOCK",
        "id": "b28022",
        "title": "تَنْبِيهٌ هَامٌّ",
        "content": """<div class="benefit-box warning rounded border-light">
    <strong class="text-accent block mb-2mm">الخَلْطُ بَيْنَ التَّشْبِيهِ البَلِيغِ وَالاسْتِعَارَةِ:</strong>
    <p class="mb-2mm text-justify">يَجِبُ التَّمْيِيزُ بَيْنَهُمَا مِنْ خِلَالِ وُجُودِ الطَّرَفَيْنِ (المُشَبَّهِ وَالمُشَبَّهُ بِهِ) أَوْ غِيَابِ أَحَدِهِمَا.</p>
    <ul class="structured-list">
        <li class="mb-1mm"><span class="marker">•</span><span class="font-bold">«خَالِدٌ أَسَدٌ»</span>: <span class="text-primary">تَشْبِيهٌ بَلِيغٌ</span> (الطَّرَفَانِ مَذْكُورَانِ).</li>
        <li class="mb-1mm"><span class="marker">•</span><span class="font-bold">«زَأَرَ خَالِدٌ»</span>: <span class="text-primary">اسْتِعَارَةٌ مَكْنِيَّةٌ</span> (حُذِفَ الأَسَدُ وَبَقِيَتْ صِفَتُهُ).</li>
    </ul>
</div>"""
    }
]

def render_block(block):
    t = ""
    if block["type"] == "HEADER":
        t = T_HEADER
        for k, v in block["data"].items():
            t = t.replace(k, v)

    elif block["type"] == "BLOCK":
        t = T_BLOCK
        # Fix: Remove unused benefit placeholder BEFORE replacing content
        # This prevents the regex from swallowing content that looks like a benefit box (e.g. nested benefit-box)
        t = re.sub(r'<div class="benefit-box[^>]*>.*?\[BENEFIT_TITLE\].*?</div>', '', t, flags=re.DOTALL)

        t = t.replace("[BLOCK_ID]", block.get("id", ""))
        t = t.replace("[BLOCK_TITLE]", block.get("title", ""))
        t = t.replace("[CONTENT_TEXT]", block.get("content", ""))

        # Remove empty block-body if content is empty (for Title-only blocks)
        if not block.get("content") or block.get("content").strip() == "":
             t = re.sub(r'<div class="block-body">\s*</div>', '', t, flags=re.DOTALL)

    elif block["type"] == "CHIPS":
        t = T_CHIPS
        items = block["content_raw"].split("|")
        chips_html = ""
        for item in items:
            chips_html += f'<span class="bg-grey-lighter p-2mm rounded border-light">{item.strip()}</span>'

        chips_component = T_CHIPS.replace("[CHIPS_CONTENT]", chips_html)

        t = T_BLOCK
        # Fix: Remove unused benefit placeholder BEFORE replacing content
        t = re.sub(r'<div class="benefit-box[^>]*>.*?\[BENEFIT_TITLE\].*?</div>', '', t, flags=re.DOTALL)

        t = t.replace("[BLOCK_ID]", block.get("id", ""))
        t = t.replace("[BLOCK_TITLE]", block.get("title", ""))
        t = t.replace("[CONTENT_TEXT]", chips_component)

    elif block["type"] == "TABLE":
        t = T_TABLE
        t = t.replace("[BLOCK_ID]", block.get("id", ""))
        t = t.replace("[TABLE_TITLE]", block.get("title", ""))

        headers_html = ""
        for h in block["headers"]:
            headers_html += f'<th class="text-primary font-bold">{h}</th>'

        t = t.replace("[TABLE_HEADERS]", headers_html)
        t = t.replace("[TABLE_ROWS]", block["rows_html"])

    elif block["type"] == "SPLIT":
        t = T_SPLIT
        t = t.replace("[BLOCK_ID]", block.get("id", ""))
        t = t.replace("[LEFT_TITLE]", block.get("left_title", ""))
        t = t.replace("[LEFT_CONTENT]", block.get("left_content", ""))
        t = t.replace("[RIGHT_TITLE]", block.get("right_title", ""))
        t = t.replace("[RIGHT_CONTENT]", block.get("right_content", ""))

        if 'id="' not in t and block.get("id"):
             t = t.replace('<section class="split-grid">', f'<section class="split-grid" id="{block.get("id", "")}">')

    elif block["type"] == "TIP":
        t = T_BENEFIT_TIP
        t = t.replace("[TIP_TITLE]", block.get("title", ""))
        t = t.replace("[TIP_TEXT]", block.get("content", ""))

    elif block["type"] == "POEM":
        t = T_POEM
        t = t.replace("[BLOCK_ID]", block.get("id", ""))
        t = t.replace("[SECTION_TITLE]", block.get("title", ""))
        t = t.replace("[POEM_VERSES]", block.get("verses", ""))

        t = t.replace("[POET_NAME]", "")
        t = t.replace("[POET_BIO]", "")
        t = t.replace("[POEM_TITLE]", "")

        t = re.sub(r'<div class="bio-card">.*?</div>', '', t, flags=re.DOTALL)
        t = re.sub(r'<h3[^>]*>\s*</h3>', '', t)

        if 'id="' not in t and block.get("id"):
             t = t.replace('<section class="poem-container">', f'<section class="poem-container" id="{block.get("id", "")}">')

    elif block["type"] == "IRAB":
        t = T_IRAB_ROW
        t = t.replace("[IRAB_BOXES]", block.get("boxes", ""))
        if block.get("id"):
             t = t.replace('<div class="flex', f'<div id="{block.get("id")}" class="flex')

    elif block["type"] == "EXAM":
        questions_html = ""
        for i, q_text in enumerate(block["questions"]):
            num = i + 1
            is_last = (i == len(block["questions"]) - 1)
            margin_class = "mb-0 border-none pb-0" if is_last else ""

            q_html = f"""
            <div class="exam-question {margin_class}" id="{block.get('id', '')}_q{num}">
                <p class="m-0 mb-2mm">
                    <span class="exam-number">{num}</span>
                    {q_text}
                </p>
                <div class="border-light h-8mm bg-grey-lighter rounded"></div>
            </div>
            """
            questions_html += q_html

        t = T_BLOCK
        # Fix: Remove unused benefit placeholder BEFORE replacing content
        t = re.sub(r'<div class="benefit-box[^>]*>.*?\[BENEFIT_TITLE\].*?</div>', '', t, flags=re.DOTALL)

        t = t.replace("[BLOCK_ID]", block.get("id", ""))
        t = t.replace("[BLOCK_TITLE]", f" اخْتَبِرْ نَفْسَكَ ({block.get('topic', '')})")
        t = t.replace('class="block-header"', 'class="block-header bg-dark"')
        t = t.replace("[CONTENT_TEXT]", questions_html)

    return t

def generate_pages():
    current_page_idx = 0
    current_content = []

    current_content.append(render_block(blocks[0]))

    for i in range(1, len(blocks)):
        block = blocks[i]
        block_html = render_block(block)
        current_content.append(block_html)

        temp_filename = f"{OUTPUT_DIR}/temp_check.html"
        full_html = T_BASE.replace("<!-- INJECT_CONTENT_HERE -->", "\n".join(current_content))

        with open(temp_filename, 'w', encoding='utf-8') as f:
            f.write(full_html)

        try:
            result_json = subprocess.check_output([sys.executable, "Jules-workspace/verify_layout.py", temp_filename], stderr=subprocess.STDOUT)
            result = json.loads(result_json)
        except Exception as e:
            try:
                if isinstance(e, subprocess.CalledProcessError):
                     result = json.loads(e.output)
                else:
                     raise e
            except:
                print(f"Error checking layout: {e}")
                continue

        if result["status"] == "FAIL":
            print(f"Layout check FAILED: {result.get('details')}")
            sys.exit(1)

        if result["status"] == "OVERFLOW":
            current_content.pop()

            save_filename = f"{OUTPUT_DIR}/28.{current_page_idx}_nXX_الصورة البيانية.html"
            final_html = T_BASE.replace("<!-- INJECT_CONTENT_HERE -->", "\n".join(current_content))
            with open(save_filename, 'w', encoding='utf-8') as f:
                f.write(final_html)
            print(f"Saved {save_filename} (Reason: Overflow)")

            current_page_idx += 1
            current_content = []

            current_content.append(block_html)

    if current_content:
        save_filename = f"{OUTPUT_DIR}/28.{current_page_idx}_nXX_الصورة البيانية.html"
        final_html = T_BASE.replace("<!-- INJECT_CONTENT_HERE -->", "\n".join(current_content))
        with open(save_filename, 'w', encoding='utf-8') as f:
            f.write(final_html)
        print(f"Saved {save_filename} (Final)")

    if os.path.exists(f"{OUTPUT_DIR}/temp_check.html"):
        os.remove(f"{OUTPUT_DIR}/temp_check.html")

if __name__ == "__main__":
    generate_pages()
