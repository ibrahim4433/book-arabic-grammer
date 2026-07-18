import os
import random
import re

# Template Paths
TEMPLATES_DIR = "Jules-workspace/Templates/"
PAGES_DIR = "pages/"
OUTPUT_FILE = os.path.join(PAGES_DIR, "23.0_nXX_أشهر مواطن الزيادة والحذف.html")


# Template content
def read_template(filename):
    with open(os.path.join(TEMPLATES_DIR, filename), encoding="utf-8") as f:
        return f.read()


TEMPLATE_BASE = read_template("TEMPLATE_C_BASE.html")
TEMPLATE_HEADER = read_template("TEMPLATE_C_HEADER.html")
TEMPLATE_BLOCK = read_template("TEMPLATE_C_BLOCK.html")
TEMPLATE_TABLE = read_template("TEMPLATE_C_TABLE.html")
TEMPLATE_TABLE_ROW = read_template("TEMPLATE_C_TABLE_ROW.html")
TEMPLATE_CHIPS = read_template("TEMPLATE_C_CHIPS.html")
TEMPLATE_SPLIT = read_template("TEMPLATE_C_SPLIT.html")
TEMPLATE_BENEFIT = read_template("TEMPLATE_C_BENEFIT.html")
TEMPLATE_IRAB_ROW = read_template("TEMPLATE_C_IRAB_ROW.html")
TEMPLATE_EXAM = read_template("TEMPLATE_C_EXAM.html")
TEMPLATE_PAGE_WRAPPER = read_template("TEMPLATE_C_PAGE_WRAPPER.html")

# Remove wrapper <p> from TEMPLATE_BLOCK to allow block-level content injection
TEMPLATE_BLOCK = re.sub(
    r"<p[^>]*>\s*\[CONTENT_TEXT\]\s*</p>", "[CONTENT_TEXT]", TEMPLATE_BLOCK, flags=re.DOTALL
)


def generate_id():
    return f"b{random.randint(10000, 99999)}"


def sanitize_content(content):
    # Mapping styles to allowed classes
    replacements = [
        ("text-teal-700", "text-primary"),
        ("text-teal-600", "text-primary"),
        ("text-teal-800", "text-primary"),
        ("text-red-700", "text-accent"),
        ("text-red-600", "text-accent"),
        ("text-red-800", "text-accent"),
        ("bg-gray-100", "bg-grey-lighter"),
        ("rounded-lg", "rounded"),
        ("text-xl", "font-bold"),
        ("w-1/3", "flex-1"),
        ("gap-4", "gap-2mm"),
        ("shadow-md", "shadow-card"),
        ("border-2", ""),
        ("border-teal-500", ""),
        ("border-red-500", ""),
        ("border-t-4", ""),
        ("text-gray-700", "text-grey"),
        ("leading-normal", ""),
        ("p-4", "p-2mm"),
        ("pr-4", ""),
        ("pr-2mm", ""),
        ("px-4", "p-2mm"),
        ("py-2", ""),
        ("text-teal-500", "text-primary"),
        ("border-light", "border-light"),
        ("highlight-blue", "highlight-blue"),
        ("highlight-red", "highlight-red"),
        ("highlight-green", "highlight-green"),
        ("items-start", ""),
    ]

    for old, new in replacements:
        content = content.replace(old, new)

    content = content.replace('class=""', "")
    return content


# Strip existing ID placeholder from Exam to avoid duplicates when injecting
TEMPLATE_EXAM = TEMPLATE_EXAM.replace('id="[BLOCK_ID]"', "")

# --- Block Construction ---

# Block 1: Header
header_content = TEMPLATE_HEADER.replace("[LESSON_NUMBER]", "23")
header_content = header_content.replace("[CHAPTER_TITLE]", "أشهر مواطن الزيادة والحذف")
header_content = header_content.replace("[CATEGORY_HEADER]", "الإملاء")
header_content = header_content.replace("[SECTION_HEADER]", "المستوى اللغوي")
header_content = header_content.replace("[AUTHOR_NAME]", "أ. حنا خفيف")
header_content = header_content.replace("[AUTHOR_PHONE]", " ")

# Block 2: Definition
block2_content = """
<p class="text-right text-grey">
    <span class="text-accent font-bold">الزِّيَادَةُ:</span> هِيَ كِتَابَةُ حَرْفٍ زَائِدٍ فِي الْكَلِمَةِ لَا يُلْفَظُ، وَلَكِنَّهُ يُثْبَتُ رَسْمًا لِعِلَّةٍ صَرْفِيَّةٍ أَوْ إِمْلَائِيَّةٍ.<br>
    <span class="text-accent font-bold">الْحَذْفُ:</span> هُوَ إِسْقَاطُ حَرْفٍ مِنَ الْكَلِمَةِ رَسْمًا وَخَطًّا، مَعَ بَقَائِهِ فِي اللَّفْظِ أَحْيَانًا، أَوْ حَذْفِهِ لَفْظًا وَخَطًّا فِي مَوَاضِعَ أُخْرَى.
</p>
"""
block2 = TEMPLATE_BLOCK.replace("[BLOCK_TITLE]", "مفهوم الزيادة والحذف")
block2 = block2.replace("[CONTENT_TEXT]", sanitize_content(block2_content))
block2 = re.sub(r'<div class="benefit-box">.*?</div>', "", block2, flags=re.DOTALL)

# Block 3: Summary Matrix
headers3 = "<th>النَّوْعُ</th><th>الْمَوْضِعُ</th><th>مِثَالٌ</th>"
rows_data3 = [
    (
        '<span class="font-bold text-primary">الزِّيَادَةُ (تُكْتَبُ وَلَا تُلْفَظُ)</span>',
        "بَعْدَ وَاوِ الْجَمَاعَةِ، تَنْوِينِ النَّصْبِ، إِطْلَاقِ الشِّعْرِ، فِي (عَمْرو، أُولَئِكَ)",
        '<span class="highlight-red">سَافَرُوا</span>، <span class="highlight-red">كِتَابًا</span>، <span class="highlight-red">عَمْرو</span>',
    ),
    (
        '<span class="font-bold text-accent">الْحَذْفُ (تُلْفَظُ وَلَا تُكْتَبُ)</span>',
        "أَلِفُ (اللَّهُ، الرَّحْمَنُ)، (مَا) الِاسْتِفْهَامِيَّةُ، (نُونُ) مِنْ/عَنْ، لَامُ الَّذِي",
        '<span class="highlight-red">اللَّهُ</span>، <span class="highlight-red">لِمَ؟</span>، <span class="highlight-red">الَّذِي</span>',
    ),
]
rows_html3 = ""
for r in rows_data3:
    row = (
        TEMPLATE_TABLE_ROW.replace("[CELL_1]", r[0])
        .replace("[CELL_2]", r[1])
        .replace("[CELL_3]", r[2])
    )
    rows_html3 += row

block3 = TEMPLATE_TABLE.replace("[TABLE_TITLE]", "مُلَخَّصُ مَوَاطِنِ الزِّيَادَةِ وَالْحَذْفِ")
block3 = block3.replace("[TABLE_HEADERS]", headers3)
block3 = block3.replace("[TABLE_ROWS]", sanitize_content(rows_html3))

# Block 4: Ziyadat al-Alif
block4_content = """
<p class="text-right text-grey mb-2mm">تُزَادُ الْأَلِفُ فِي الْمَوَاضِعِ التَّالِيَةِ وَلَا تُلْفَظُ:</p>
<ul class="structured-list">
    <li class="mb-1mm">
        <span class="text-primary font-bold ml-2mm">1.</span>
        <p>
            <span class="font-bold text-primary">أَلِفُ التَّفْرِيقِ:</span> تُزَادُ بَعْدَ <span class="highlight-blue">وَاوِ الْجَمَاعَةِ</span> لِلتَّفْرِيقِ بَيْنَهَا وَبَيْنَ الْوَاوِ الْأَصْلِيَّةِ، نَحْوَ: <span class="highlight-red">سَافَرُوا</span>، <span class="highlight-red">لَمْ يَكْتُبُوا</span>، <span class="highlight-red">ادْرُسُوا</span>.
        </p>
    </li>
    <li class="mb-1mm">
        <span class="text-primary font-bold ml-2mm">2.</span>
        <p>
            <span class="font-bold text-primary">أَلِفُ تَنْوِينِ النَّصْبِ:</span> فِي آخِرِ الِاسْمِ الْمَنْصُوبِ الْمُنَوَّنِ غَيْرِ الْمُنْتَهِي بِتَاءٍ مَرْبُوطَةٍ أَوْ هَمْزَةٍ قَبْلَهَا أَلِفٌ، نَحْوَ: <span class="highlight-red">رَأَيْتُ شَابًّا</span>، <span class="highlight-red">قَرَأْتُ كِتَابًا</span>.
        </p>
    </li>
    <li class="mb-1mm">
        <span class="text-primary font-bold ml-2mm">3.</span>
        <p>
            <span class="font-bold text-primary">أَلِفُ الْإِطْلَاقِ:</span> تُزَادُ فِي آخِرِ بَعْضِ أَبْيَاتِ الشِّعْرِ لِضَرُورَةِ الْوَزْنِ وَالْقَافِيَةِ.
        </p>
    </li>
</ul>
"""
block4 = TEMPLATE_BLOCK.replace("[BLOCK_TITLE]", "أَوَّلًا: مَوَاطِنُ زِيَادَةِ الْأَلِفِ")
block4 = block4.replace("[CONTENT_TEXT]", sanitize_content(block4_content))
block4 = re.sub(r'<div class="benefit-box">.*?</div>', "", block4, flags=re.DOTALL)

# Block 5: Chips
chips_content = """
<div class="flex flex-wrap gap-2mm justify-center">
    <span class="bg-grey-lighter rounded p-2mm font-bold text-primary border-light">عَمْرو</span>
    <span class="bg-grey-lighter rounded p-2mm font-bold text-primary border-light">أُولَئِكَ</span>
    <span class="bg-grey-lighter rounded p-2mm font-bold text-primary border-light">أُولَاء</span>
    <span class="bg-grey-lighter rounded p-2mm font-bold text-primary border-light">أُولُو</span>
    <span class="bg-grey-lighter rounded p-2mm font-bold text-primary border-light">أُولَات</span>
    <span class="bg-grey-lighter rounded p-2mm font-bold text-primary border-light">أُولِي</span>
</div>
"""
block5_inner = TEMPLATE_CHIPS.replace("[CHIPS_CONTENT]", sanitize_content(chips_content))
block5_wrapped = TEMPLATE_BLOCK.replace("[BLOCK_TITLE]", "ثَانِيًا: مَوَاطِنُ زِيَادَةِ الْوَاوِ")
block5_wrapped = block5_wrapped.replace("[CONTENT_TEXT]", block5_inner)
block5_wrapped = re.sub(r'<div class="benefit-box">.*?</div>', "", block5_wrapped, flags=re.DOTALL)

# Block 6: Split
left_content = """
<p class="mb-2mm">تُحْذَفُ الْأَلِفُ كِتَابَةً فَقَطْ (تُلْفَظُ وَلَا تُكْتَبُ) فِي الْكَلِمَاتِ التَّالِيَةِ:</p>
<ul class="structured-list">
    <li class="mb-1mm"><span class="highlight-red">اللَّهُ</span>، <span class="highlight-red">الرَّحْمَنُ</span>، <span class="highlight-red">إِلَهٌ</span></li>
    <li class="mb-1mm"><span class="highlight-red">السَّمَوَاتُ</span></li>
    <li class="mb-1mm"><span class="highlight-red">هَذَا</span>، <span class="highlight-red">هَذِهِ</span>، <span class="highlight-red">هَذَانِ</span>، <span class="highlight-red">هَؤُلَاءِ</span>، <span class="highlight-red">هَكَذَا</span></li>
    <li class="mb-1mm"><span class="highlight-red">ذَلِكَ</span>، <span class="highlight-red">أُولَئِكَ</span></li>
    <li class="mb-1mm"><span class="highlight-red">لَكِنَّ</span>، <span class="highlight-red">لَكِنْ</span></li>
</ul>
"""
right_content = """
<p class="mb-2mm">تُحْذَفُ أَلِفُ (مَا) الِاسْتِفْهَامِيَّةِ إِذَا دَخَلَ عَلَيْهَا حَرْفُ جَرٍّ:</p>
<ul class="structured-list">
    <li class="mb-1mm">لِ + مَا = <span class="highlight-red font-bold">لِمَ؟</span></li>
    <li class="mb-1mm">بِ + مَا = <span class="highlight-red font-bold">بِمَ؟</span></li>
    <li class="mb-1mm">عَلَى + مَا = <span class="highlight-red font-bold">عَلَامَ؟</span></li>
    <li class="mb-1mm">إِلَى + مَا = <span class="highlight-red font-bold">إِلَامَ؟</span></li>
    <li class="mb-1mm">مِنْ + مَا = <span class="highlight-red font-bold">مِمَّ؟</span></li>
    <li class="mb-1mm">عَنْ + مَا = <span class="highlight-red font-bold">عَمَّ؟</span></li>
</ul>
"""
block6 = TEMPLATE_SPLIT.replace("[LEFT_TITLE]", "حَذْفُ الْأَلِفِ مِنَ الْأَسْمَاءِ")
block6 = block6.replace("[RIGHT_TITLE]", "حَذْفُ الْأَلِفِ مِنْ (مَا) الِاسْتِفْهَامِيَّةِ")
block6 = block6.replace("[LEFT_CONTENT]", sanitize_content(left_content))
block6 = block6.replace("[RIGHT_CONTENT]", sanitize_content(right_content))

# Block 7: Table (Custom Rowspan)
headers7 = "<th>الْقَاعِدَةُ</th><th>الْمُعَادَلَةُ</th><th>النَّتِيجَةُ</th>"
rows_html7 = """
<tr>
    <td class="font-bold text-primary" rowspan="2">حَذْفُ نُونِ (مِنْ / عَنْ)</td>
    <td>مِنْ + مَنْ</td>
    <td><span class="highlight-red">مِمَّنْ</span></td>
</tr>
<tr>
    <td>عَنْ + مَا</td>
    <td><span class="highlight-red">عَمَّ</span> (مَعَ حَذْفِ الْأَلِفِ)</td>
</tr>
<tr>
    <td class="font-bold text-primary" rowspan="3">إِدْغَامُ (إِنْ / أَنْ)</td>
    <td>إِنْ (الشَّرْطِيَّة) + مَا</td>
    <td><span class="highlight-red">إِمَّا</span></td>
</tr>
<tr>
    <td>إِنْ (الشَّرْطِيَّة) + لَا</td>
    <td><span class="highlight-red">إِلَّا</span></td>
</tr>
<tr>
    <td>أَنْ (الْمَصْدَرِيَّة) + مَا</td>
    <td><span class="highlight-red">أَمَّا</span></td>
</tr>
"""
block7 = TEMPLATE_TABLE.replace("[TABLE_TITLE]", "حَذْفُ النُّونِ وَالْإِدْغَامُ")
block7 = block7.replace("[TABLE_HEADERS]", headers7)
block7 = block7.replace("[TABLE_ROWS]", sanitize_content(rows_html7))

# Block 8: Table
headers8 = "<th>الْحَالَةُ</th><th>الشَّرْحُ</th><th>الْأَمْثِلَةُ</th>"
rows_data8 = [
    (
        '<span class="font-bold text-primary">لَامٌ وَاحِدَةٌ مُشَدَّدَةٌ</span>',
        "لِلْمُفْرَدِ بِنَوْعَيْهِ، وَجَمْعِ الْمُذَكَّرِ",
        '<span class="highlight-blue">الَّذِي</span>، <span class="highlight-blue">الَّتِي</span>، <span class="highlight-blue">الَّذِينَ</span>',
    ),
    (
        '<span class="font-bold text-primary">لَامَانِ اثْنَتَانِ</span>',
        "لِلْمُثَنَّى بِنَوْعَيْهِ، وَجَمْعِ الْمُؤَنَّثِ",
        '<span class="highlight-blue">اللَّذَانِ</span>، <span class="highlight-blue">اللَّتَانِ</span>، <span class="highlight-blue">اللَّوَاتِي</span>، <span class="highlight-blue">اللَّائِي</span>',
    ),
    (
        '<span class="font-bold text-primary">دُخُولُ لَامِ الْجَرِّ</span>',
        "تُكْتَبُ بِلَامَيْنِ عِنْدَ دُخُولِ اللَّامِ عَلَيْهَا",
        '<span class="highlight-blue">لِلَّذِينَ</span>، <span class="highlight-blue">لِلَّذِي</span>، <span class="highlight-blue">لِلَّتَيْنِ</span>',
    ),
]
rows_html8 = ""
for r in rows_data8:
    row = (
        TEMPLATE_TABLE_ROW.replace("[CELL_1]", r[0])
        .replace("[CELL_2]", r[1])
        .replace("[CELL_3]", r[2])
    )
    rows_html8 += row

block8 = TEMPLATE_TABLE.replace("[TABLE_TITLE]", "اللَّامُ مَعَ الْأَسْمَاءِ الْمَوْصُولَةِ")
block8 = block8.replace("[TABLE_HEADERS]", headers8)
block8 = block8.replace("[TABLE_ROWS]", sanitize_content(rows_html8))

# Block 9: Benefit
block9_content = """
<p>
    تُزَادُ الْوَاوُ فِي كَلِمَةِ (<span class="highlight-red">عَمْرو</span>) فِي حَالَتَيِ الرَّفْعِ وَالْجَرِّ لِلتَّفْرِيقِ بَيْنَهَا وَبَيْنَ (<span class="highlight-blue">عُمَر</span>) الْمَمْنُوعَةِ مِنَ الصَّرْفِ. أَمَّا فِي حَالَةِ النَّصْبِ فَتُحْذَفُ الْوَاوُ وَتُنَوَّنُ الْأَلِفُ: (<span class="highlight-green">رَأَيْتُ عَمْرًا</span>).
</p>
"""
block9 = f"""
<section class="content-block">
    <div class="block-header accent">
        <span>فَائِدَةٌ (عَمْرو وَ عُمَر)</span>
    </div>
    <div class="block-body">
        {sanitize_content(block9_content)}
    </div>
</section>
"""

# Block 10: Irab
irab_content = """
    <div class="bg-white p-2mm rounded flex-1 text-center border-light">
        <div class="font-bold text-primary mb-1mm">سَافَرُوا</div>
        <div class="text-grey text-sm">
            <span class="font-bold text-primary">سَافَرَ:</span> فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ.<br>
            <span class="font-bold text-primary">الْوَاوُ:</span> ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعِ فَاعِلٍ.<br>
            <span class="font-bold text-primary">الْأَلِفُ:</span> لِلتَّفْرِيقِ، حَرْفٌ زَائِدٌ لَا مَحَلَّ لَهُ.
        </div>
    </div>
    <div class="bg-white p-2mm rounded flex-1 text-center border-light">
        <div class="font-bold text-accent mb-1mm">لِمَ؟</div>
        <div class="text-grey text-sm">
            <span class="font-bold text-accent">اللَّامُ:</span> حَرْفُ جَرٍّ.<br>
            <span class="font-bold text-accent">مَا:</span> اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ، وَحُذِفَتْ أَلِفُهُ لِاتِّصَالِهِ بِحَرْفِ الْجَرِّ.
        </div>
    </div>
"""
block10_inner = TEMPLATE_IRAB_ROW.replace("[IRAB_BOXES]", sanitize_content(irab_content))
block10_wrapped = TEMPLATE_BLOCK.replace("[BLOCK_TITLE]", "نَمَاذِجُ إِعْرَابِيَّةٌ")
block10_wrapped = block10_wrapped.replace("[CONTENT_TEXT]", block10_inner)
block10_wrapped = re.sub(
    r'<div class="benefit-box">.*?</div>', "", block10_wrapped, flags=re.DOTALL
)

# Block 11: Exam
question_text = """
بَيِّنْ مَوْطِنَ الزِّيَادَةِ أَوْ الْحَذْفِ فِي الْكَلِمَاتِ الْمُلَوَّنَةِ فِي الْجُمَلِ الْآتِيَةِ:
<div class="structured-list mt-2mm">
    <p class="mb-1mm">1. قَالَ تَعَالَى: {وَالَّذِينَ آمَنُوا وَعَمِلُوا الصَّالِحَاتِ <span class="highlight-red">أُولَئِكَ</span> أَصْحَابُ الْجَنَّةِ}.</p>
    <p class="mb-1mm">2. <span class="highlight-red">عَلَامَ</span> تَتَنَافَسُونَ وَالدُّنْيَا زَائِلَةٌ؟</p>
    <p class="mb-1mm">3. <span class="highlight-red">هَذَا</span> طَالِبٌ مُجْتَهِدٌ يَعْرِفُ وَاجِبَهُ.</p>
</div>
"""
block11 = TEMPLATE_EXAM.replace("[TOPIC]", "أشهر مواطن الزيادة والحذف")
block11 = block11.replace("[QUESTION_TEXT]", sanitize_content(question_text), 1)

# Safer removal of Question 2 by string splitting
if "<!-- Question 2" in block11:
    block11 = block11.split("<!-- Question 2")[0] + "</div></section>"

block11 = block11.replace("[Q1_ID]", generate_id())


# Assemble content
full_content = (
    header_content
    + block2
    + block3
    + block4
    + block5_wrapped
    + block6
    + block7
    + block8
    + block9
    + block10_wrapped
    + block11
)


def inject_ids(html_content):
    def replace_func(match):
        tag = match.group(0)
        if "id=" in tag:
            return tag
        return f'{tag[:-1]} id="{generate_id()}">'

    html_content = re.sub(
        r'<section[^>]*class="[^"]*\bcontent-block\b[^"]*"[^>]*>', replace_func, html_content
    )
    html_content = re.sub(
        r'<div[^>]*class="[^"]*\bcontent-block\b[^"]*"[^>]*>', replace_func, html_content
    )
    return html_content


final_content = inject_ids(full_content)

# Correct wrapping with TEMPLATE_C_BASE
page_content = TEMPLATE_PAGE_WRAPPER.replace("<!-- INJECT_CONTENT_HERE -->", final_content)
final_page = TEMPLATE_BASE.replace("<!-- INJECT_CONTENT_HERE -->", page_content)

# Ensure directory exists
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(final_page)

print(f"Generated {OUTPUT_FILE}")
