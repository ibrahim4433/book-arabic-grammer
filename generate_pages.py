import os
import re
import json
import subprocess

def read_template(name):
    with open(f"Jules-workspace/Templates/{name}", "r", encoding="utf-8") as f:
        return f.read()

TEMPLATE_BASE = read_template("TEMPLATE_C_BASE.html")
TEMPLATE_WRAPPER = read_template("TEMPLATE_C_PAGE_WRAPPER.html")

def wrap_content(title, content):
    wrapper = TEMPLATE_WRAPPER.replace("<!-- Content components go here -->", content)
    base = TEMPLATE_BASE.replace("[PAGE_TITLE]", title).replace("<!-- Content components go here -->\n    </div>", wrapper + "\n    </div>")
    # Clean up base if wrapper was substituted correctly
    if "<div class=\"force-new-page\">" in base and wrapper in base:
         # TEMPLATE_BASE actually has:
         # <div class="force-new-page">
         #     <!-- Content components go here -->
         # </div>
         pass
    # A cleaner approach for base:
    base = read_template("TEMPLATE_C_BASE.html")
    base = base.replace("[PAGE_TITLE]", title)

    # Check if base contains the force-new-page div already
    if 'class="force-new-page"' in base:
        base = base.replace("<!-- Content components go here -->", content)
    else:
        wrapped = TEMPLATE_WRAPPER.replace("<!-- Content components go here -->", content)
        base = base.replace("<body>\n", f"<body>\n{wrapped}\n")

    # Clean out any id="[UNIQUE_ID]"
    base = re.sub(r'\s*id="\[UNIQUE_ID\]"', '', base)
    return base

def verify_layout(filepath):
    result = subprocess.run(["python3", "Jules-workspace/verify_layout.py", filepath], capture_output=True, text=True)
    try:
        # verify_layout prints JSON
        output = result.stdout
        json_str = output[output.find('{'):output.rfind('}')+1]
        return json.loads(json_str)
    except Exception as e:
        print("Error verifying layout:", e)
        print("Output was:", result.stdout)
        return {"status": "FAIL"}

def create_block_header():
    t = read_template("TEMPLATE_C_HEADER.html")
    t = t.replace("[LESSON_NUMBER]", "03")
    t = t.replace("[LEVEL_INFO]", "المستوى التأسيسي")
    t = t.replace("[TOPIC_INFO]", "علم النحو")
    t = t.replace("[MAIN_TITLE]", "أَنْوَاعُ الْفِعْلِ وَعَلَاَّمَاتِهِ")
    t = t.replace("[AUTHOR_NAME]", "أ. الياس خفيف")
    t = t.replace("[AUTHOR_CONTACT]", "994066850 963+")
    return t

def create_block_intro():
    t = read_template("TEMPLATE_C_BLOCK.html")
    t = t.replace("[BLOCK_TITLE]", "مُقَدَّمَةً")
    content = """<p class="text-accent">الْفِعْلُ فِي اللُّغَةَ الْعَرَبِيَّةَ هُو : <strong>حَدَثَ مُقْتَرِنٌ بِزَمَنِ</strong>.</p>
<p>أي أَنّهُ يَدُلُّ عَلَى عَمَلٍ أَو حَرَكَةُ (الْحَدَثَ) حَصَّلَتْ فِي وَقْتِ مُعَيَّنِ (الزَّمَنَ).</p>"""
    t = t.replace("<p class=\"mt-1mm text-accent\">\n            [CONTENT]\n        </p>", f"<div>{content}</div>")
    return t

def create_block_types():
    t = read_template("TEMPLATE_C_BENEFIT.html")
    t = t.replace("[TITLE]", "أَقْسَامُ الْفِعْلِ")

    chips = read_template("TEMPLATE_C_CHIPS.html")
    chips = chips.replace("""    <span class="bg-grey-lighter rounded p-1mm">[CHIP_TEXT]</span>
    <span class="bg-grey-lighter rounded p-1mm">[CHIP_TEXT]</span>
    <div class="bg-grey-lighter rounded p-1mm"><span class="font-bold">[BOLD_PREFIX]:</span> [CHIP_TEXT]</div>""",
    """<span class="bg-grey-lighter rounded p-1mm">الْمَاضِي</span>
    <span class="bg-grey-lighter rounded p-1mm">الْمُضَارِعَ</span>
    <span class="bg-grey-lighter rounded p-1mm">الْأَمْرَ</span>""")

    content = f"""<p>وَيَنْقَسِمُ الْفِعْلُ فِي اللُّغَةَ الْعَرَبِيَّةَ إِلَى ثَلَاثَةِ أَقْسَامِ رَئِيسِيَّةِ حَسْب الزَّمَنِ:</p>
{chips}"""
    t = t.replace("[CONTENT]", content)
    return t

def create_block_past():
    t = read_template("TEMPLATE_C_BLOCK.html")
    t = t.replace("[BLOCK_TITLE]", "١. الْفِعْلِ الْمَاضِي")
    content = """<p class="text-accent"><strong>التَّعْرِيفَ:</strong> هُو مَا دَلٍّ عَلَى حَدَثِ وَقْعٍ وَاِنْتَهَى <strong>قَبْل</strong> زَمَانَ التَّكَلُّمِ (أَيَّ قَبْل أَنّ أَتَحَدُّثٌ عَنهُ).</p>
<p><strong>أَمِثْلَةَ:</strong> <span class="highlight-green">دَخَلَ</span> ، <span class="highlight-green">خَرَجَ</span> ، <span class="highlight-green">فَهِمَ</span>.</p>"""
    t = t.replace("<p class=\"mt-1mm text-accent\">\n            [CONTENT]\n        </p>", f"<div>{content}</div>")
    return t

def create_block_past_signs():
    t = read_template("TEMPLATE_C_BLOCK.html")
    t = t.replace("[BLOCK_TITLE]", "عَلَاَّمَاتِ الْفِعْلِ الْمَاضِي")

    lst = read_template("TEMPLATE_C_LIST.html")
    items = """<li><span class="marker">•</span> <span><strong>تَاءُ التَّأْنِيثِ السَّاكِنَةَ (تْ):</strong> مِثْل (سَمِعَ<span class="highlight-red">تْ</span>، قَرَأَ<span class="highlight-red">تْ</span>، خَرَجَ<span class="highlight-red">تْ</span>، قَالَتْ).</span></li>
<li><span class="marker">•</span> <span><strong>تَاءُ الْفَاعِلِ الْمُتَحَرِّكَةِ (تُ، تَ، تِ):</strong> مِثْل (كَتَبْ<span class="highlight-red">تُ</span> لِلْمُتَكَلِّمَ، كَتَبْ<span class="highlight-red">تَ</span> لِلْمُخَاطِبَ، كَتَبْ<span class="highlight-red">تِ</span> لِلْمُخَاطَبَةَ الْمُؤَنَّثَةَ).</span></li>
<li><span class="marker">•</span> <span><strong>نُونُ النِّسْوَةِ (نَ):</strong> مِثْل (الطَّالِبَاتُ فَهِمْ<span class="highlight-red">نَ</span> الشَّرْحَ).</span></li>
<li><span class="marker">•</span> <span><strong>دُخُولُ (قَدْ) قِبَلَهُ:</strong> مِثْل الْمِثَالِ: "<span class="highlight-blue">قَدْ</span> أَفْلَحَ الْمُجْتَهِدُونَ".</span></li>"""
    lst = re.sub(r'<li>.*?</li>', '', lst, flags=re.DOTALL).replace('</ul>', items + '\n</ul>')

    content = f"""<p>كَيْف أَتَأَكُّدٌ أَنّ هَذَا الْفِعْلُ مَاضٍ؟ إِذَا قَبْل إحْدَى الْعَلَاَّمَاتِ التَّالِيَةِ فِي آخِرِهِ:</p>\n{lst}"""
    t = t.replace("<p class=\"mt-1mm text-accent\">\n            [CONTENT]\n        </p>", f"<div>{content}</div>")
    return t

def create_block_note1():
    t = read_template("TEMPLATE_C_BENEFIT_TIP.html")
    t = t.replace("[TITLE]", "مُلَاحِظَةً")
    t = t.replace("[CONTENT]", "<p>نُونُ النِّسْوَةِ تَدْخُلُ عَلَى جَمِيعِ الْأَفْعَالِ.</p>")
    return t

def create_block_present():
    t = read_template("TEMPLATE_C_BLOCK.html")
    t = t.replace("[BLOCK_TITLE]", "٢. الْفِعْلُ الْمُضَارِعُ")
    content = """<p class="text-accent"><strong>التَّعْرِيفَ:</strong> هُو مَا دَلٍّ عَلَى حَدَثٍ يَقُعُّ <strong>فِي زَمَانِ التَّكَلُّمِ</strong> (الْآن) أَو <strong>بَعْدهُ</strong> (فِي الْمُسْتَقْبَلِ).</p>
<p><strong>أَمِثْلَةَ:</strong> <span class="highlight-green">يَقْرَأُ</span> ، <span class="highlight-green">يَسْمَعُ</span> ، <span class="highlight-green">يَكْتُبُ</span>.</p>"""
    t = t.replace("<p class=\"mt-1mm text-accent\">\n            [CONTENT]\n        </p>", f"<div>{content}</div>")
    return t

def create_block_present_signs():
    t = read_template("TEMPLATE_C_BLOCK.html")
    t = t.replace("[BLOCK_TITLE]", "عَلَاَّمَاتِ الْفِعْلِ الْمُضَارِعِ")

    lst = read_template("TEMPLATE_C_LIST.html")
    items = """<li><span class="marker">•</span> <span><strong>دُخُولُ (السِّينَ) أَو (سَوْف) قِبَلَهُ:</strong> مِثْل (<span class="highlight-blue">سَ</span>أُذَاكِرُ دُرُوسَي، <span class="highlight-blue">سَوْف</span> أُذَاكِرُ دُرُوسَي).</span></li>
<li><span class="marker">•</span> <span><strong>دُخُولُ (لَم) و(لَن) قِبَلَهُ:</strong> مِثْل (<span class="highlight-blue">لَم</span> أُهْمِلْ دُرُوسَي، <span class="highlight-blue">لَن</span> أُهْمِلَ دُرُوسَي).</span></li>
<li><span class="marker">•</span> <span><strong>دُخُولُ (قَدْ) قِبَلَهُ:</strong> (تَدُلُّ هُنَا إِمَّا عَلَى التَّقْليلِ مِثْل: <span class="highlight-blue">قَد</span> يَنْجَحُ الْكَسُولُ، أَو عَلَى التَّكْثيرِ مِثْل: <span class="highlight-blue">قَد</span> يَنْجَحُ الْمُجْتَهِدُ).</span></li>
<li><span class="marker">•</span> <span><strong>الْبَدْءُ بِحُروفِ الْمُضَارِعَةِ (أ، ن، ي، ت):</strong> وَيَجْمَعُهَا كَلِمَةُ (أَنِيتُ) أَو (نَأْتِي). <br><strong>أَمِثْلَةَ:</strong> <span class="highlight-red">أَ</span>حْفَظُ، <span class="highlight-red">نَ</span>حْفَظُ، <span class="highlight-red">يَ</span>حْفَظُ، <span class="highlight-red">تَ</span>حْفَظُ.</span></li>"""
    lst = re.sub(r'<li>.*?</li>', '', lst, flags=re.DOTALL).replace('</ul>', items + '\n</ul>')

    content = f"""<p>يَتَمَيَّزُ الْفِعْلُ الْمُضَارِعُ بِعَلَاَّمَاتِ خَاصَّةٍ لَا تَدَخُّلٍ عَلَى غَيْرهُ:</p>\n{lst}"""
    t = t.replace("<p class=\"mt-1mm text-accent\">\n            [CONTENT]\n        </p>", f"<div>{content}</div>")
    return t

def create_block_note2():
    t = read_template("TEMPLATE_C_BENEFIT_TIP.html")
    t = t.replace("[TITLE]", "تَنْبِيه")
    t = t.replace("[CONTENT]", "<p>هَمْزَةُ الْفِعْلِ الْمُضَارِعِ تَكَوَّنَ دَائِمَا هَمْزَةِ قَطْعِ.</p>")
    return t

def create_block_imperative():
    t = read_template("TEMPLATE_C_BLOCK.html")
    t = t.replace("[BLOCK_TITLE]", "٣. فعَلّ الْأَمْرِ")
    content = """<p class="text-accent"><strong>التَّعْرِيفَ:</strong> هُو مَا دَلٍّ عَلَى حَدَثِ <strong>يُطْلَبُ</strong> حُدوثَهُ <strong>بَعْد</strong> زَمَانَ التَّكَلُّمِ.</p>
<p><strong>أَمِثْلَةَ:</strong> <span class="highlight-green">اِسْمَعْ</span> ، <span class="highlight-green">اُكْتُبْ</span> ، <span class="highlight-green">أَغْلِقْ</span>.</p>"""
    t = t.replace("<p class=\"mt-1mm text-accent\">\n            [CONTENT]\n        </p>", f"<div>{content}</div>")
    return t

def create_block_imperative_signs():
    t = read_template("TEMPLATE_C_BLOCK.html")
    t = t.replace("[BLOCK_TITLE]", "عَلَاَّمَاتٍ فعَلّ الْأَمْرِ")

    lst = read_template("TEMPLATE_C_LIST.html")
    items = """<li><span class="marker">•</span> <span><strong>دَلَالَتُهُ عَلَى الطَّلَبِ بِصِيغَتِهِ:</strong> مِثْل (<span class="highlight-red">اِحْفَظْ</span>، <span class="highlight-red">اِفْهَمْ</span>).</span></li>
<li><span class="marker">•</span> <span><strong>قَبُولُهُ ياء الْمُخَاطَبَةَ:</strong> مِثْل (اِحْفَظِ<span class="highlight-red">ي</span>، اِفْهَمِ<span class="highlight-red">ي</span>).</span></li>"""
    lst = re.sub(r'<li>.*?</li>', '', lst, flags=re.DOTALL).replace('</ul>', items + '\n</ul>')

    content = f"""<p>لَهَّ عَلَاَمَتَانِ يَجِبُ أَن تَجْتَمِعَا فِيهِ:</p>\n{lst}"""
    t = t.replace("<p class=\"mt-1mm text-accent\">\n            [CONTENT]\n        </p>", f"<div>{content}</div>")
    return t

def create_block_warning():
    t = read_template("TEMPLATE_C_BENEFIT_WARNING.html")
    t = t.replace("[TITLE]", "تَنْبِيهَاتِ هَامَةِ")

    lst = read_template("TEMPLATE_C_LIST.html")
    items = """<li><span class="marker">•</span> <span>إِذَا دَلَّتْ الْكَلِمَةَ عَلَى الطَّلَبِ ولَكِنّهَا <strong>لَم تَقْبَلُ ياء الْمُخَاطَبَةَ</strong>، فهِي (اِسْمٌ فعَلّ أَمْرِ) مِثْل: <span class="highlight-blue">صَهْ</span> (بِمُعَنَّى اسكت).</span></li>
<li><span class="marker">•</span> <span>إِذَا قَبِلَتْ الْكَلِمَةَ ياء الْمُخَاطَبَةَ ولَكِنّهَا <strong>لَم تَدُلُّ عَلَى الطَّلَبِ</strong>، فهِي فعَلّ مُضَارِعِ مِثْل: <span class="highlight-green">تُذَاكِرِينَ</span>.</span></li>"""
    lst = re.sub(r'<li>.*?</li>', '', lst, flags=re.DOTALL).replace('</ul>', items + '\n</ul>')
    t = t.replace("[CONTENT]", lst)
    return t

def create_block_note3():
    t = read_template("TEMPLATE_C_BENEFIT_TIP.html")
    t = t.replace("[TITLE]", "مُلَاحِظَةً: دَلَالَاتٍ بَلَاغِيَّةٍ لِفِعْلَ الْأَمْرِ حَسْب الرُّتْبَةِ")

    lst = read_template("TEMPLATE_C_LIST.html")
    items = """<li><span class="marker">•</span> <span>مِن الْاِبْنِ لأَبِيهُ: يُسَمَّى <strong>رَجَاءً</strong> (مِثْل: يَا أبِي <span class="highlight-green">سَامِحْنِِي</span>).</span></li>
<li><span class="marker">•</span> <span>مِن الْمُعَلِّمِ لِلتِّلْميذَ: يُسَمَّى <strong>أَمْرًا</strong> (مِثْل: <span class="highlight-green">اِقْرَأْ</span> دَرَسَكَ).</span></li>
<li><span class="marker">•</span> <span>بَيْن المتساويين (مِن شَخْصٍ لِصَدِيقَهُ): يُسَمَّى <strong>طَلَبًا</strong> أَو اِلْتِمَاسَا (مِثْل: يَا صَدِيقِي <span class="highlight-green">اِسْمَعْ</span> كِلَاَمَي).</span></li>"""
    lst = re.sub(r'<li>.*?</li>', '', lst, flags=re.DOTALL).replace('</ul>', items + '\n</ul>')
    t = t.replace("[CONTENT]", lst)
    return t

def create_block_summary():
    t = read_template("TEMPLATE_C_BLOCK.html")
    t = t.replace("[BLOCK_TITLE]", "مُلَخَّصُ أَنْوَاعِ الْفِعْلِ وَعَلَامَاتِهِ")

    table = read_template("TEMPLATE_C_TABLE.html")
    table = table.replace("[HEADER_1]", "نَوْعُ الْفِعْلِ")
    table = table.replace("[HEADER_2]", "الزَّمَنُ")

    # Needs to support 4 columns according to the plan
    # Table template only has 3. Let's modify it to 4.
    table = table.replace("<th>[HEADER_3]</th>", "<th>أَهَمُّ الْعَلَامَاتِ</th>\n                <th>مِثَالٌ</th>")

    rows = """<tr>
                <td>الْمَاضِي</td>
                <td>قَبْلَ زَمَانِ التَّكَلُّمِ</td>
                <td>تَاءُ التَّأْنِيثِ، تَاءُ الْفَاعِلِ، نُونُ النِّسْوَةِ</td>
                <td>كَتَبَتْ، كَتَبْتُ</td>
            </tr>
            <tr>
                <td>الْمُضَارِعُ</td>
                <td>فِي زَمَانِ التَّكَلُّمِ أَو بَعْدَهُ</td>
                <td>السِّينُ، سَوْفَ، لَمْ، لَنْ، قَدْ، أَنِيتُ</td>
                <td>سَيَكْتُبُ، يَكْتُبُ</td>
            </tr>
            <tr>
                <td>الْأَمْرُ</td>
                <td>بَعْدَ زَمَانِ التَّكَلُّمِ</td>
                <td>دَلَالَتُهُ عَلَى الطَّلَبِ، قَبُولُ ياء الْمُخَاطَبَةَ</td>
                <td>اُكْتُبْ، اُكْتُبِي</td>
            </tr>"""
    table = re.sub(r'<tr>\s*<td>\[CELL_1\]</td>\s*<td>\[CELL_2\]</td>\s*<td>\[CELL_3\]</td>\s*</tr>', rows, table)

    t = t.replace("<p class=\"mt-1mm text-accent\">\n            [CONTENT]\n        </p>", table)
    return t

def create_block_exam(number, question, title=None):
    t = read_template("TEMPLATE_C_EXAM.html")
    if title:
        # Prepend a block-header with bg-dark as required by exam rules
        header = f'<div class="block-header bg-dark">\n    <span>{title}</span>\n</div>\n'
        t = header + t

    t = t.replace("[QUESTION_NUMBER]", f"{number}")
    t = t.replace("[QUESTION_TEXT]", question)
    return t

blocks = [
    create_block_header(),
    create_block_intro(),
    create_block_types(),
    create_block_past(),
    create_block_past_signs(),
    create_block_note1(),
    create_block_present(),
    create_block_present_signs(),
    create_block_note2(),
    create_block_imperative(),
    create_block_imperative_signs(),
    create_block_warning(),
    create_block_note3(),
    create_block_summary(),
    create_block_exam("١", "اِسْتَخْرَجَ الْأَفْعَالُ مِن بَيْن الْكَلِمَاتِ التَّالِيَةِ ، وَحَدَّدَ نَوْعُهَا (مَاضٍ ، مُضَارِعٌ ، أَمْرَ): (تَقَدَّمَ - تَعَلَّمْ - أَكْتُبُ)", "تَدْرِيبَاتٍ وَتَطْبِيقَاتٍ عَمَلِيَّةٍ (مُسْتَخْرَجَةً مِن الدَّرْسِ)"),
    create_block_exam("٢", "ضَعْ عُلَّامَةَ (صَحَّ) أَو (خَطَأَ) مَع تَصْحِيحِ الْخَطَأِ:<br>١. كَلِمَةُ \"تُذَاكِرِينَ\" هِي فعَلّ أَمْرٍ لأَنّهَا تَقَبُّلَ ياء الْمُخَاطَبَةَ.<br>٢. تَاءُ الْفَاعِلِ الْمُتَحَرِّكَةِ لَا تَتَّصِلُ إِلَّا بِالْفِعْلِ الْمَاضِي.<br>٣. إِذَا سَبَقَ الْفِعْلُ ب (سَوْف) فهُو فعَلّ مَاضٍ يَدُلُّ عَلَى الْمُسْتَقْبَلِ.<br>٤. فعَلّ الْأَمْرِ يَجِبُ أَن يَجْمَعُ بَيْن الدَّلَالَةِ عَلَى الطَّلَبِ وَقَبُولِ ياء الْمُخَاطَبَةَ."),
    create_block_exam("٣", "صَنَّفَ الْأَفْعَالُ فِي الْجَمَلِ التَّالِيَةِ حَسْب نَوْعِهَا (مَاضٍ ، مُضَارِعٌ ، أَمْرَ):<br>١. قَالَتْ سَارَّةُ الْحَقِّ.<br>٢. لَمْ أُهْمِلْ وَاجِبِيٌّ.<br>٣. يَا طَالِبَةُ اِجْتَهِدِي.<br>٤. قَدْ أَفْلَحَ الْمُجْتَهِدُونَ.<br>٥. سَوْفَ نُسَافِرُ غَدًا.")
]

page_num = 0
current_content = ""
for i, block in enumerate(blocks):
    # Try adding the block
    temp_content = current_content + "\n" + block

    title = f"03.{page_num}_nXX_أَنْوَاعُ الْفِعْلِ وَعَلَاَّمَاتِهِ"
    if page_num > 0:
        title += " (تابع)"

    filepath = f"pages/{title}.html"

    html = wrap_content(title, temp_content)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

    res = verify_layout(filepath)
    if res.get("status") == "OVERFLOW" and current_content != "":
        # We need to split
        # Revert the current page to without this block
        html = wrap_content(f"03.{page_num}_nXX_أَنْوَاعُ الْفِعْلِ وَعَلَاَّمَاتِهِ" + (" (تابع)" if page_num > 0 else ""), current_content)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)

        # Start new page
        page_num += 1
        current_content = block

        title = f"03.{page_num}_nXX_أَنْوَاعُ الْفِعْلِ وَعَلَاَّمَاتِهِ (تابع)"
        filepath = f"pages/{title}.html"
        html = wrap_content(title, current_content)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
    else:
        current_content = temp_content

print("Pages generation completed.")
