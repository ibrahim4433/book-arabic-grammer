import json
import subprocess

TEMPLATE_BASE = """<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="utf-8"/>
    <title>02 - عَلَاَّمَاتُ الْاِسْمِ</title>
    <link href="../styles/main.css" rel="stylesheet"/>
</head>
<body>
    <div class="force-new-page">
        {content}
    </div>
</body>
</html>"""

TEMPLATE_HEADER = """<header class="page-header-strip">
    <!-- Right: Lesson Number + Lesson Details -->
    <div class="header-section right">
        <div class="lesson-number">02</div>
        <div class="lesson-details">
            <div>المستوى التأسيسي</div>
            <div>علم النحو</div>
        </div>
    </div>
    <!-- Center: Title -->
    <div class="header-section center">
        <h1 class="header-title">عَلَاَّمَاتُ الْاِسْمِ</h1>
    </div>
    <!-- Left: Author Info -->
    <div class="header-section left">
        <div class="author-info">أ. حنا خفيف</div>
        <div class="author-info"> </div>
    </div>
</header>"""

TEMPLATE_BLOCK = """<section class="content-block">
    <div class="block-header">
        <span>{title}</span>
    </div>
    <div class="block-body">
        {content}
    </div>
</section>"""

TEMPLATE_BENEFIT_TIP = """<div class="benefit-box tip">
    <strong> {title}:</strong> {content}
</div>"""

TEMPLATE_TABLE = """<div class="block-body p-0">
    <table class="dense-table">
        <thead>
            <tr>
                <th>الْعَلَاَّمَةُ</th>
                <th>الْمِثَالُ</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>الْجَرُّ</td>
                <td>ذَهَبْتُ إِلَى الْبَيْتِ</td>
            </tr>
            <tr>
                <td>التَّنْوِينُ</td>
                <td>كِتَابًا ، قَلَمًا</td>
            </tr>
            <tr>
                <td>النِّدَاءُ</td>
                <td>يَا سَعِيدَ</td>
            </tr>
            <tr>
                <td>التَّعْرِيفُ ب ( الَ )</td>
                <td>الْفَصْلَ</td>
            </tr>
            <tr>
                <td>التَّاءُ الْمَرْبُوطَةُ ( ة )</td>
                <td>حَديقَةُ</td>
            </tr>
        </tbody>
    </table>
</div>"""

TEMPLATE_LIST_START = """<ul class="structured-list">"""
TEMPLATE_LIST_END = """</ul>"""
TEMPLATE_LIST_ITEM = """<li><span class="marker">•</span><div>{content}</div></li>"""

TEMPLATE_EXAM = """<!-- Regular Question -->
<div class="exam-question">
    <p class="m-0 mb-2mm">
        <span class="exam-number">{num}</span>
        {question}
    </p>
    <div class="border-light h-8mm bg-grey-lighter rounded"></div>
</div>"""


def generate_chips(items):
    res = '<div class="flex flex-wrap gap-2mm mt-1mm">\n'
    for it in items:
        res += f'    <span class="bg-grey-lighter rounded p-1mm">{it}</span>\n'
    res += "</div>"
    return res


# Now we construct the blocks
blocks = []

# Block 1
blocks.append(TEMPLATE_HEADER)

# Block 2
b2_content = """<p class="mt-1mm text-accent">أَقْسَامُ الْكَلَاَمِ فِي اللُّغَةَ الْعَرَبِيَّةَ ثَلَاثَةَ : اِسْمٌ ، وَفِعْلٌ ، وَحَرْفَ .</p>
<p>لِكَي نَتَعَلَّمُ الْإِعْرَابَ بِالصُّورَةِ الصَّحِيحَةِ ، يَجِبُ أَن نَبْدَأُ بِخَطْوَتِنَا الْأوْلَى وهِي التَّمْييزِ بَيْن هَذِه الْأَقْسَامِ</p>
<p>وَالْيَوْمُ سَنُرَكِّزُ عَلَى الْقِسْمِ الْأَوَّلِ : <strong>الْاِسْمُ</strong>.</p>"""
blocks.append(TEMPLATE_BLOCK.format(title="مُقَدَّمَةً", content=b2_content))

# Block 3
blocks.append(
    TEMPLATE_BENEFIT_TIP.format(
        title="مَعْلُومَةٌ مُهِمَّةٌ",
        content="كَيْف نَعْرُفُ أَنّ هَذِه الْكَلِمَةِ اِسْمٌ ؟ لِلْاِسْمَ عَلَاَّمَاتٍ مُمَيَّزَةٍ ، وَمَجْمُوعَاتٍ يَنْتَمِي إِلَيْهَا.",
    )
)

# Block 4
blocks.append(f"""<section class="content-block">
    <div class="block-header">
        <span>مُلَخَّصُ عَلَاَّمَاتِ الْاِسْمِ</span>
    </div>
    {TEMPLATE_TABLE}
</section>""")

# Block 5
b5_list = TEMPLATE_LIST_START + "\n"
b5_items = [
    """<strong>الْجَرُّ :</strong> أَنّ تَقَبُّلِ الْكَلِمَةِ دُخُولَ حَرْفِ الْجَرِّ عَلَيْهَا. مِثَالَ : ذَهَبْتُ إِلَى <span class="highlight-red">الْبَيْتِ</span>. ( كَلِمَةَ " الْبَيْتَ " اِسْمٌ لأَنّهَا سَبَّقَتْ بِحَرْفِ جَرِّ ).""",
    """<strong>التَّنْوِينُ :</strong> أَيَّ كَلِمَةِ تَقَبُّلِ التَّنْوِينِ ( ً ٍ ٌ ) هِي اِسْمٍ. أَمِثْلَةَ : اِشْتَرَيْتُ <span class="highlight-red">كِتَابًا</span>، أَو <span class="highlight-red">قَلَمًا</span>.""",
    """<strong>النِّدَاءُ :</strong> الْكَلِمَاتُ الَّتِي يُصْحِ نِدَاءَهَا هِي أَسْمَاءٍ. أَمِثْلَةَ : يَا <span class="highlight-red">سَعِيدَ</span>، يَا <span class="highlight-red">هِنْدَ</span>، يَا <span class="highlight-red">سَارَّةَ</span>.""",
    """<strong>التَّعْرِيفُ ب ( الَ ):</strong> أَيَّ كَلِمَةٍ تَبْدَأُ بِأدَاةِ التَّعْرِيفِ ( الَ ) أَو تَقْبَلُ دُخُولَهَا. أَمِثْلَةَ : فَصِلْ <span class="highlight-red">الْفَصْلَ</span>، كِتَابَ <span class="highlight-red">الْكِتَابَ</span>.""",
    """<strong>التَّاءُ الْمَرْبُوطَةُ ( ة ):</strong> الْكَلِمَةَ الَّتِي تَنْتَهِي بِتَاءِ مَرْبُوطَةِ هِي مِن الْأَسْمَاءِ دُون تَفْكِيرٍ. أَمِثْلَةَ : <span class="highlight-red">حَديقَةُ</span>، <span class="highlight-red">شَجَرَةَ</span>.""",
]
for item in b5_items:
    b5_list += TEMPLATE_LIST_ITEM.format(content=item) + "\n"
b5_list += TEMPLATE_LIST_END
b5_content = f"""<div class="mt-1mm">إِذَا قَبِلَتْ الْكَلِمَةَ إحْدَى هَذِه الْعَلَاَّمَاتِ الْخُمُسَ ، فهِي <strong>اِسْمَ</strong> بِلَا شَكٍّ.</div>
{b5_list}"""
blocks.append(TEMPLATE_BLOCK.format(title="أَوْلًا الْعَلَاَّمَاتُ النَّحْوِيَّةُ لِلْاِسْمَ", content=b5_content))

# Block 6
b6_list = TEMPLATE_LIST_START + "\n"
b6_items = [
    """<strong>الْإِنْسَانَ :</strong> أَيَّ اِسْمٍ لِذِكْرٍ أَو أُنْثَى""",
    """<strong>الْحَيَوَانَ وَالطُّيُورَ وَالْحَشَرَاتِ :</strong> مِثْل ( <span class="highlight-green">عَصْفُورٌ</span> ، <span class="highlight-green">طَائِرٌ</span> ، <span class="highlight-green">فَرَاشَةَ</span> ).""",
    """<strong>النَّبَاتَاتِ :</strong> مِثْل ( <span class="highlight-green">شَجَرَةً</span> ، <span class="highlight-green">زَهْرَةً</span> ، <span class="highlight-green">فَوَاكِهَ</span> ، <span class="highlight-green">خُضْرُوَاتُ</span> ).""",
    """<strong>الْجَمَادَاتِ :</strong> الْأَشْيَاءُ الَّتِي لَا حَيَاةٍ فِيهَا ( <span class="highlight-green">حَجَرٌ</span> ، <span class="highlight-green">قَلَمَ</span> ).""",
    """<strong>الصَّفَّاتِ :</strong> مِثْل ( <span class="highlight-green">طَوِيلٌ</span> ، <span class="highlight-green">قَصِيرٌ</span> ، <span class="highlight-green">كَرِيمٌ</span> ، <span class="highlight-green">بِخَيْلِ</span> ).""",
    """<strong>الْمُصَادَرَ ( الْأَحْدَاثَ الْمُجَرَّدَةَ مِن الزَّمَنِ ):</strong> مِثْل ( <span class="highlight-green">خُرُوجٌ</span> ، <span class="highlight-green">إعْلَاَنٌ</span> ، <span class="highlight-green">زِيَارَةَ</span> ).""",
]
for item in b6_items:
    b6_list += TEMPLATE_LIST_ITEM.format(content=item) + "\n"
b6_list += TEMPLATE_LIST_END
b6_content = f"""<div class="mt-1mm">يُمْكِنُنَا أيضاً تَمْييزَ الْأَسْمَاءِ مِن خِلَال دَلَالَتِهَا فِي الْحَيَاةِ ، فَالْاِسْمَ يَشْمَلُ كُلّ مَا يُشِيرُ إِلَى</div>
{b6_list}"""
blocks.append(
    TEMPLATE_BLOCK.format(
        title="ثَانِيًا الْمُعَنَّى وَالدَّلَالَةُ ( الطَّرِيقَةَ الْعَمَلِيَّةَ لِمَعْرِفَةَ الْاِسْمِ )", content=b6_content
    )
)

# Block 7
b7_list = TEMPLATE_LIST_START + "\n"
b7_data = [
    ("أَسَمَاءَ الْإشَارَةِ :", ["هَذَا", "هَذِه", "هَذَان", "هَاتَان", "هَؤُلَاء"]),
    ("الْأَسْمَاءَ الْمَوْصُولَةَ :", ["الَّذِي", "الَّتِي", "الْلَذَان", "الْلَتَان", "الَّذِين", "الْلَاتِي", "الْلَائِي"]),
    ("الضَّمَائِرَ :", ["هُو", "هِي", "أَنْتُم", "هُم", "نَحْن", "أَنْتُمَا"]),
    ("أَسَمَاءَ الْاِسْتِفْهَامِ :", ["مَنٌّ", "مَاذَا", "لِمَاذَا", "مَتَى", "أَيْن", "كَيْف"]),
]
for title, chips in b7_data:
    chips_html = generate_chips(chips)
    b7_list += TEMPLATE_LIST_ITEM.format(content=f"<strong>{title}</strong>\n{chips_html}") + "\n"
b7_list += TEMPLATE_LIST_END
b7_content = f"""<div class="mt-1mm">هُنَاك كَلِمَاتٍ فِي اللُّغَةَ الْعَرَبِيَّةَ هِي مِن الْأَسْمَاءِ بِالرَّغْمِ مِن أَنّهَا لَا تَتَغَيَّرُ حَرَكَتُهَا ، مِثْل:</div>
{b7_list}"""
blocks.append(
    TEMPLATE_BLOCK.format(title="ثَالِثًا أَسَمَاءُ مَبْنِيَّةُ ( أَنْوَاعَ خَاصَّةٍ مِن الْأَسْمَاءِ )", content=b7_content)
)

# Block 8: Exams
exam_content = f"""<section class="content-block">
    <div class="block-header bg-dark text-white">
        <span>اِخْتَبَرَ نَفْسَكَ</span>
    </div>
    <div class="block-body">
{TEMPLATE_EXAM.format(num="١", question="اِسْتَخْرَجَ الْأَسْمَاءُ مِن بَيْن الْكَلِمَاتِ التَّالِيَةِ وَضَعَ خَطًّا تَحْتهَا : ( مُعَلِّمًا - إِلَى - شَجَرَةً - كَيْف - كَتَبٍّ - هَذِه )")}
{TEMPLATE_EXAM.format(num="٢", question="اُذْكُرْ عُلَّامَةَ الْاِسْمِ فِي الْكَلِمَاتِ الْمُلَوَّنَةِ فِي الْجَمَلِ التَّالِيَةِ : ١. ذَهَبْتُ إِلَى الْحَديقَةِ الْعَظِيمَةَ . ٢. يَا طَالِبُ الْعِلْمِ . ٣. رَأَيْتُ عَصْفُورًا يَطِيرُ . ٤. الْقَلَمُ جَدِيدٌ .")}
{TEMPLATE_EXAM.format(num="٣", question="صَنَّفَ الْأَسْمَاءُ التَّالِيَةُ حَسْب دَلَالَتِهَا ( إِنْسَانٌ ، حَيَوَانَ / طَيْرٌ ، نَبَاتٌ ، جَمَادٌ ، صَفَّةً ، مَصْدَرٌ ، اِسْمَ إشَارَةٍ ، ضَمِيرٌ ، اِسْمَ اِسْتِفْهَامِ ) : ١. هِنْدٌ ٢. خُرُوجٌ ٣. طَوِيلٌ ٤. نَحْن ٥. مَاذَا ٦. هَؤُلَاء ٧. فَرَاشَةٌ")}
    </div>
</section>"""
blocks.append(exam_content)

# Logic to append blocks and verify
current_page_idx = 0
current_blocks = []


def save_page(idx, content_blocks):
    filename = f"Jules-workspace/pages/02.{idx}_nXX_عَلَاَّمَاتُ الْاِسْمِ.html"
    if idx > 0 and 'class="page-header-strip"' not in content_blocks[0]:
        # Add a continued header
        continued_header = TEMPLATE_HEADER.replace("عَلَاَّمَاتُ الْاِسْمِ", "عَلَاَّمَاتُ الْاِسْمِ ")
        html = TEMPLATE_BASE.format(content="\n".join([continued_header] + content_blocks))
    else:
        html = TEMPLATE_BASE.format(content="\n".join(content_blocks))

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    return filename


def check_overflow(filename):
    res = subprocess.run(
        ["python3", "Jules-workspace/verify_layout.py", filename], capture_output=True, text=True
    )
    try:
        json_str = res.stdout[res.stdout.find("{") : res.stdout.rfind("}") + 1]
        data = json.loads(json_str)
        return data.get("status") == "OVERFLOW"
    except Exception as e:
        print("Error parsing layout verification:", e, res.stdout)
        return False


for i, block in enumerate(blocks):
    current_blocks.append(block)
    filename = save_page(current_page_idx, current_blocks)

    if check_overflow(filename):
        # We overflowed. Pop the last block.
        current_blocks.pop()
        save_page(current_page_idx, current_blocks)

        # Start new page
        current_page_idx += 1
        current_blocks = [block]
        save_page(current_page_idx, current_blocks)

print(f"Done. Generated {current_page_idx + 1} pages.")
