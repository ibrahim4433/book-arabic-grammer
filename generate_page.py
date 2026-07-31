html_part1 = """<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="utf-8"/>
    <title>page 130</title>
    <link href="../styles/main.css" rel="stylesheet"/>
</head>
<body>
"""

html_part2 = """<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="utf-8"/>
    <title>page 130 part 2</title>
    <link href="../styles/main.css" rel="stylesheet"/>
</head>
<body>
"""

id_counter = 1000
def get_next_id():
    global id_counter
    id_counter += 1
    return f"b{id_counter}"

def add_header():
    uid = get_next_id()
    return f"""<header class="page-header-strip" id="{uid}">
    <div class="header-section right">
        <div class="lesson-number">130</div>
        <div class="lesson-details">
            <div></div>
            <div></div>
        </div>
    </div>
    <div class="header-section center">
        <h1 class="header-title">page 130</h1>
    </div>
    <div class="header-section left">
        <div class="author-info"></div>
        <div class="author-info"></div>
    </div>
</header>
"""

def add_block(title, content, use_accent=False):
    uid = get_next_id()
    accent_class = " accent" if use_accent else ""
    return f"""<div class="content-block" id="{uid}">
    <div class="block-header{accent_class}">
        <span>{title}</span>
    </div>
    <div class="block-body">
        <p class="mt-1mm text-accent">{content}</p>
    </div>
</div>
"""

def add_poem(title, right, left):
    uid = get_next_id()
    title_html = f"""<div class="block-header poem-header">
        <span>{title}</span>
    </div>""" if title else ""
    return f"""<div class="poem-container" id="{uid}">
    {title_html}
    <div class="poem-verses">
        <div class="poem-line flex justify-between items-center mb-2mm">
            <div class="hemistich w-45pct text-center font-bold">{right}</div>
            <div class="hemistich w-45pct text-center font-bold">{left}</div>
        </div>
    </div>
</div>
"""

def add_cut_part_1(title, content):
    uid = get_next_id()
    return f"""<div class="content-block border-open-bottom" id="{uid}">
    <div class="block-header">
        <span>{title} (يتبع)</span>
    </div>
    <div class="block-body fade-bottom">
        <p class="mt-1mm text-accent">{content}</p>
    </div>
</div>
"""

elements_all = []
elements_all.append(add_block("- إلغاء التَّجْزِئَةِ والتَّخَلُّص مِنْ قُيُودِ الْمُسْتَعْمِرِين (رَفْضُ التَّجْزِئَةِ وَإِنْكَارُ الحُدُودِ الوَهْمِيَّةِ التي رسمها المسْتَعْمرون):", "", True))
elements_all.append(add_poem("سلامة عبيد:", "وتلاشَتْ مَعَ القُيُودِ أَسَاطِيـ", "ـرُ حُدُودٍ رَهِيبَةٌ نَكْرَاءُ"))
elements_all.append(add_block("- التفاؤل بالمُسْتَقْبَلِ المُشْرِقِ الوَاعِدِ بَعْدَ قِيَامِ الْوَحْدَةِ:", ""))
elements_all.append(add_poem("سلامة عبيد:", "وبَدَا الغَدُ الضَّحُوكُ طَلِيقًا", "وبِهِ مِنْ سَنَا الرَّجَاءِ سَنَاءُ"))
elements_all.append(add_block("- الدعوة إلى الإِشَادَةِ بِالأُمَّةِ العَرَبِيَّةِ لِتَحَرُّرِهَا وَاسْتِقْلَالِهَا (الاعتِزَازُ بِتَحَرُّرِ الْأُمَّةِ العَرَبِيَّةِ):", ""))
elements_all.append(add_poem("سلامة عبيد:", "وتَغَنَّيْ أَنَّا سُدْنَا", "وَإِنَّا فِي أَرْضِنَا طُلَقَاءُ"))
elements_all.append(add_block("- تَمْجِيدُ الأُمَّةِ العَرَبِيَّةِ وَالتَّغَنِي بِصِفَاتِهَا :", ""))
elements_all.append(add_poem("سلامة عبيد:", "دَرْبُ تَوْحِيدِ أُمَّةٍ جَبَلَتُهَا", "مِنْ عَبِيرِ الْمُكَارِمِ العَلْيَاءُ"))
elements_all.append(add_block("١٠- التَّحْذِيرُ مِنَ التَّجْزِئَةِ وَنَبْذُ الفُرْقَةِ:", ""))
elements_all.append(add_poem("سلامة عبيد:", "أَيُّهَا التَّائِهُونَ فِي مَهْمَهِ الأَمْـ", "ـسِ سَرَابٌ دُرُوبُكُم وَشَقَاءُ"))
elements_all.append(add_block("١١- الدَّعْوَةُ إلى الوَحْدَةِ العَرَبِيَّةِ (تَحْفِيزُ المتَرَدِّدِين للالتحاق بِرَكْبِ الوحْدَةِ العَرَبِيَّةِ):", ""))
elements_all.append(add_poem("سلامة عبيد:", "أَيُّهَا التَّائِهُونَ فِي مَهْمَهِ الْأَمْسِ", "سَرَابٌ دُرُوبُكُم وَشَقَاءُ"))
elements_all.append(add_poem("", "أَقْبِلُوا أَيُّهَا الْحَيَارَى فَهَذَا الد", "ـرْبُ طَلْقٌ مُشَوِّقٌ وَضَّاءُ"))
elements_all.append(add_poem("", "دَرْبُ تَوْحِيدِ أُمَّةٍ جَبَلَتْهَا", "مِنْ عَبِيرِ المكَارِمِ العَلْيَاءُ"))
elements_all.append(add_block("١٢- الإشارة إلى ثمارِ الوَحْدَةِ (وَصْفُ جَمَالِ الْحَيَاةِ بَعْدَ قِيَامِ الوَحْدَةِ):", ""))
elements_all.append(add_poem("سلامة عبيد:", "أَزْهَرَتْ وَاحَةُ العُرُوبَةِ وَافْتَرْ", "رَتْ وَمَاسَتْ جِنَاهَا الْخَضْرَاءُ"))
elements_all.append(add_poem("", "وتَثَنَّتْ فِيهَا الجَدَاوِلُ سَكْرَى", "وتَرَامَتْ فِي رُبُوعِهَا الأَفْيَاءُ"))
elements_all.append(add_block("١٣- التَّفَاؤُلُ بِقِيَامِ الوَحْدَةِ (الإيمان بِقُدْرَةِ الجَمَاهِيرِ الْعَرَبِيَّةِ على بِنَاءِ مَا هَدَّمَهُ المُسْتَعْمِرُ):", "", True))
elements_all.append(add_poem("سلامة عبيد:", "في غدٍ تَزْحَفُ الْجُمُوعُ لِتَبْنِي", "بِيَدَيْهَا مَا هَدَّمَ الأَعْدَاءُ"))
elements_all.append(add_block("١٤- إشراك الطبيعة بالفرح بالوحدة :", ""))
elements_all.append(add_poem("سلامة عبيد:", "إِنَّهَا فَرْحَةُ الْحَيَاةِ فَمِيدِي", "يَا رَوَابِي وَهَلِّلِي يَا سَمَاءُ"))
elements_all.append(add_block("ثالثاً - الأدب الوطني:", "<br> ١- التَّعْبِيرُ عَنْ مَشَاعِرِ الفَرَحِ وَالزَّهْوِ بِتَحْقِيقِ الجلاء (الفرح بجلاء المسْتَعْمر الغَرْبِي عَنْ أَرْضِ الوَطَنِ):"))
elements_all.append(add_poem("بدر الدين الحامد:", "يَوْمُ الجَلَاءِ هُوَ الدُّنْيَا وَزَهْوَتُهَا", "لَنَا ابْتِهَاجٌ وَلِلْبَاغِينَ إِرْغَامُ"))
elements_all.append(add_poem("عمر أبو ريشة:", "يا عروس المجد تِيْهِي واسحبي", "فِي مَغَانِينَا ذُيُولَ الشُّهُبِ"))
elements_all.append(add_poem("عمر أبو ريشة:", "يا عروس المجدِ طَابَ الْمُلْتَقَى", "بَعْدَمَا طَالَ جَوَى المُغْتَرِبِ"))
elements_all.append(add_poem("شفيق جبري:", "حُلْمٌ على جَنَبَاتِ الشَّامِ أَمْ عِيدُ", "لا الهم هم ولا التَّسْهِيدُ تَسْهِيدُ"))
elements_all.append(add_block("٢- تصوير هزيمة المستَعْمِرِ وَخَيْبَتِهِ فِي تَوْطِيدِ وُجُودِه على أَرْضِنا (السُّخْرِيَةُ مِنَ المُسْتَعْمر والشَّمَاتَةُ بهَزِيمَتِهِ):", ""))
elements_all.append(add_poem("عمر أبو ريشة:", "دَرَجَ البَغْيُ عَلَيْهَا حِقْبَةً", "وَهَوَى دُونَ بُلُوغِ الْأَرَبِ"))
elements_all.append(add_poem("", "وارْتَمَى كِبْرُ الليالي دُونَهَا", "لَيِّنَ النَّابِ كَلِيلَ الْمُخْلَبِ"))
elements_all.append(add_cut_part_1("٣- تَمْجِيدُ التَّضْحِيَاتِ الَّتِي قَدَّمَهَا الشَّعْبُ السوري لنيل استقلاله، والاعتزاز بها (تَمْجِيدُ الشهادة والشُّهَدَاء، التضحيات المشرفة للأجدادِ مِنْ أَجْلِ الوَطَنِ):", "عمر أبو ريشة : <br> بدر الدين الحامد:"))

# In the previous run, we included elements_all[:19].
# And the overflow was at b1019, which is the 19th element: Poem 8
# Wait. elements_all[17] is Block 13.
# elements_all[18] is Poem 8.
# So elements_all[:19] goes up to (and including) Poem 8.
# And it overflowed! "Page count is 2 (expected 1). Content overflows. Split into multiple files or condense content."
# So elements_all[:19] is too big.
# We must split at elements_all[:17], which means we exclude Block 13 and Poem 8 from part 1.
# Let's verify:
# We did elements_all[:17] previously, and we got UNDERFLOW with 32.68mm blank space remaining!
# 32.68mm is about 11.0% blank space.
# Wait! "an 'UNDERFLOW' status with less than 20% blank space is considered acceptable and does not require layout adjustments to pass the strict 1-Page Law constraint."
# Memory says:
# "When verifying HTML layout with verify_layout.py, an 'UNDERFLOW' status with less than 20% blank space is considered acceptable and does not require layout adjustments to pass the strict 1-Page Law constraint."
# This means elements_all[:17] is PERFECT!

part_1_html = add_header() + "".join(elements_all[:17])

# Let's add header to part 2
def add_header_part_2():
    uid = get_next_id()
    return f"""<header class="page-header-strip" id="{uid}">
    <div class="header-section right">
        <div class="lesson-number">130</div>
        <div class="lesson-details">
            <div></div>
            <div></div>
        </div>
    </div>
    <div class="header-section center">
        <h1 class="header-title">page 130 (تتمة)</h1>
    </div>
    <div class="header-section left">
        <div class="author-info"></div>
        <div class="author-info"></div>
    </div>
</header>
"""
part_2_html = add_header_part_2() + "".join(elements_all[17:])

html_part1 += part_1_html + "</body>\n</html>"
html_part2 += part_2_html + "</body>\n</html>"

with open("pages/page_130_h4pom.html", "w", encoding="utf-8") as f:
    f.write(html_part1)

with open("pages/page_130_h4pom_part2.html", "w", encoding="utf-8") as f:
    f.write(html_part2)
