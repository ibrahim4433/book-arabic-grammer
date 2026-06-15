import os
import sys
import subprocess
import json
import re

# Add current directory to path
sys.path.append(os.getcwd())

TEMPLATE_DIR = "Jules-workspace/Templates"
OUTPUT_DIR = "pages"
VERIFY_SCRIPT = "Jules-workspace/verify_layout.py"

def read_template(filename):
    with open(os.path.join(TEMPLATE_DIR, filename), 'r', encoding='utf-8') as f:
        return f.read()

def get_base_template():
    return read_template("TEMPLATE_C_BASE.html")

def get_header(title, section, category, number, author_name, author_phone):
    t = read_template("TEMPLATE_C_HEADER.html")
    t = t.replace("[CHAPTER_TITLE]", title)
    t = t.replace("[SECTION_HEADER]", section)
    t = t.replace("[CATEGORY_HEADER]", category)
    t = t.replace("[LESSON_NUMBER]", str(number))
    t = t.replace("[AUTHOR_NAME]", author_name)
    t = t.replace("[AUTHOR_PHONE]", author_phone)
    return t

def get_block(title, content, benefit_title=None, benefit_text=None):
    t = read_template("TEMPLATE_C_BLOCK.html")
    t = t.replace("[BLOCK_TITLE]", title)
    t = t.replace("[CONTENT_TEXT]", content)

    if benefit_title and benefit_text:
        t = t.replace("[BENEFIT_TITLE]", benefit_title)
        t = t.replace("[BENEFIT_TEXT]", benefit_text)
    else:
        # Remove benefit box
        t = re.sub(r'<div class="benefit-box">.*?</div>', '', t, flags=re.DOTALL)

    return t

def get_benefit(title, text):
    t = read_template("TEMPLATE_C_BENEFIT.html")
    t = t.replace("[BENEFIT_TITLE]", title)
    t = t.replace("[BENEFIT_TEXT]", text)
    return t

def get_benefit_tip(title, text):
    t = read_template("TEMPLATE_C_BENEFIT_TIP.html")
    t = t.replace("[TIP_TITLE]", title)
    t = t.replace("[TIP_TEXT]", text)
    return t

def get_table(title, headers, rows):
    t = read_template("TEMPLATE_C_TABLE.html")
    t = t.replace("[TABLE_TITLE]", title)
    t = t.replace("[TABLE_HEADERS]", headers)
    t = t.replace("[TABLE_ROWS]", rows)
    return t

def get_poem(title, verses, poet_name, poet_bio=""):
    t = read_template("TEMPLATE_C_POEM.html")
    t = t.replace("[SECTION_TITLE]", "شاهد شعري")
    t = t.replace("[POEM_TITLE]", title)
    t = t.replace("[POET_NAME]", poet_name)
    t = t.replace("[POET_BIO]", poet_bio)
    t = t.replace("[POEM_VERSES]", verses)

    # Clean up empty placeholders
    t = t.replace("[POEM_TITLE]", "")
    t = t.replace("[POET_BIO]", "")

    # Fix bio-info class not in CSS
    t = t.replace('class="bio-info"', 'class="flex-1"')

    return t

def get_list(title, items, note_title=None, note_text=None):
    t = read_template("TEMPLATE_C_LIST.html")
    t = t.replace("[LIST_TITLE]", title)
    t = t.replace("[LIST_ITEMS]", items)

    if note_title and note_text:
        t = t.replace("[NOTE_TITLE]", note_title)
        t = t.replace("[NOTE_TEXT]", note_text)
    else:
        # Remove benefit box and separator
        t = re.sub(r'<hr class="separator-dashed">.*?<div class="benefit-box">.*?</div>', '', t, flags=re.DOTALL)
        t = re.sub(r'<div class="benefit-box">.*?</div>', '', t, flags=re.DOTALL)

    return t

def get_exam(questions):
    t = read_template("TEMPLATE_C_EXAM.html")

    # Remove IDs placeholders
    t = t.replace('id="[BLOCK_ID]"', '')
    t = t.replace('id="[Q1_ID]"', '')
    t = t.replace('id="[Q2_ID]"', '')

    body_content = ""
    for i, (q_text, q_num) in enumerate(questions):
        is_last = (i == len(questions) - 1)
        classes = "exam-question"
        if is_last:
            classes += " mb-0 border-none pb-0"

        body_content += f'''
        <div class="{classes}">
            <p class="m-0 mb-2mm">
                <span class="exam-number">{q_num}</span>
                {q_text}
            </p>
            <div class="border-light h-8mm bg-grey-lighter rounded"></div>
        </div>
        '''

    pattern = r'(<div class="block-body">)(.*?)(</div>\s*</section>)'
    replacement = f'\\1{body_content}\\3'
    t = re.sub(pattern, replacement, t, flags=re.DOTALL)

    t = t.replace("[TOPIC]", "الأسلوب الخبري والإنشائي")

    return t


def create_page(blocks, page_num_sub):
    base = get_base_template()
    content = "\n".join(blocks)
    page = base.replace("<!-- INJECT_CONTENT_HERE -->", content)

    filename = f"{OUTPUT_DIR}/26.{page_num_sub}_nXX_الأسلوب الخبري والأسلوب الإنشائي.html"
    return filename, page

def verify_layout(filepath):
    try:
        # Quote the filepath to handle spaces
        result = subprocess.run(
            ["python3", VERIFY_SCRIPT, filepath],
            capture_output=True,
            text=True,
            check=False
        )
        output = result.stdout
        # verify_layout.py prints JSON to stdout
        try:
            data = json.loads(output)
            return data
        except json.JSONDecodeError:
            # Check if output contains JSON anywhere (maybe logging noise)
            match = re.search(r'\{.*\}', output, re.DOTALL)
            if match:
                try:
                    data = json.loads(match.group(0))
                    return data
                except:
                    pass
            print(f"JSON Decode Error. Output: {output}")
            return {"status": "FAIL", "details": output}
    except Exception as e:
        print(f"Error running verify_layout: {e}")
        return {"status": "FAIL"}

def main():
    blocks = []

    # --- BLOCK 1 ---
    blocks.append(get_header(
        title="الأسلوب الخبري والأسلوب الإنشائي",
        section="المستوى الفني",
        category="فوائد",
        number=26,
        author_name="أ. الياس خفيف",
        author_phone="994066850 963+"
    ))

    # --- BLOCK 2 ---
    blocks.append(get_block(
        title="الأسلوب الخبري والأسلوب الإنشائي (علم المعاني)",
        content='''<p class="text-accent mb-2mm">
يُقسَمُ الكلامُ، في البلاغةِ العربيَّةِ، إلى قسمين، هما: الخبرُ، والإنشاءُ. ويُدْرَسَانِ ضمن (علم المعاني).
</p>'''
    ))

    # --- BLOCK 3 ---
    blocks.append(get_block(
        title="أولًا - الأسلوب الخبري",
        content='''<p class="text-accent mb-2mm">
كلامٌ يحتملُ الصِّدْقَ أو الكذِبَ، ويصحُّ أنْ نقولَ لقائلِهِ: إنَّهُ صادقٌ فيه أو كاذبٌ.
</p>
<div class="mb-2mm">
    <strong>آ- أغراضُ الخبرِ:</strong> يُلقى الخبرُ لأحدِ غرضين:
</div>
<ul class="structured-list">
    <li>
        <span class="marker">•</span>
        <span class="font-bold text-primary">فائدةُ الخَبَرِ:</span> إفادةُ المُخاطَبِ الحُكْمَ الذي تضمَّنَتْهُ الجملةُ، لأنَّهُ لا يعرفُهُ مِنْ قبلُ، نحو: <span class="highlight-blue">(عمرُ بنُ عبدِ العزيزِ أعدلُ خُلفاءِ بني أميَّةَ).</span>
    </li>
    <li>
        <span class="marker">•</span>
        <span class="font-bold text-primary">لازمُ الفائدةِ:</span> إفادةُ المُخاطَبِ أنَّ المُتكلِّمَ عالِمٌ بالخبر الذي وردَ في الجملةِ، نحو: <span class="highlight-blue">(كُنْتَ تجلِسُ في الحديقةِ البارحةَ).</span>
    </li>
</ul>'''
    ))

    # --- BLOCK 4 ---
    blocks.append(get_benefit(
        title="أغراضٌ بلاغيَّةٌ أُخرى للخبر",
        text='''<p>
وقد يخرجُ الخبرُ عَنِ الغرضينِ الرّئيسينِ إلى أغراضٍ أُخرى تُفهَمُ مِنْ سياقِ الكلامِ، أهمُّها: <span class="font-bold">(الفخرُ، إظهارُ الضَّعْفِ، الهجاءُ، ..).</span>
</p>'''
    ))

    # --- BLOCK 5 ---
    blocks.append(get_table(
        title="ب - أنواعُ الخبرِ (مِنْ حيثُ عددِ المُؤكِّدات)",
        headers='''<th>النوع</th>
<th>تعريفه</th>
<th>مثال</th>''',
        rows='''<tr>
    <td class="font-bold text-primary">١- الخبرُ الابتدائيُّ</td>
    <td>هو الخبرُ الخالي من المُؤكِّدات</td>
    <td>نجَحَ خالدٌ</td>
</tr>
<tr>
    <td class="font-bold text-primary">٢- الخبرُ الطَّلبيُّ</td>
    <td>هو الخبرُ الذي ورد فيهِ مُؤكِّدٌ واحدٌ</td>
    <td>واللهِ نَجَحَ خالدٌ</td>
</tr>
<tr>
    <td class="font-bold text-primary">٣- الخبرُ الإنكاريُّ</td>
    <td>هو الخبرُ الذي ورد فيهِ مُؤكِّدان، أو أكثر</td>
    <td>واللهِ قد نَجَحَ خالدٌ</td>
</tr>'''
    ))

    # --- BLOCK 6 ---
    blocks.append(get_benefit_tip(
        title="أشهرُ المُؤكِّدات",
        text='''<div class="flex flex-wrap gap-1mm">
    <span class="bg-white p-1mm rounded border-light">إِنَّ</span>
    <span class="bg-white p-1mm rounded border-light">أَنَّ</span>
    <span class="bg-white p-1mm rounded border-light">لامُ الابتداءِ</span>
    <span class="bg-white p-1mm rounded border-light">اللَّامُ المُزحلقَةُ</span>
    <span class="bg-white p-1mm rounded border-light">قَدْ</span>
    <span class="bg-white p-1mm rounded border-light">القسَمُ</span>
    <span class="bg-white p-1mm rounded border-light">نونا التوكيدِ</span>
    <span class="bg-white p-1mm rounded border-light">أحرفُ التنبيهِ</span>
    <span class="bg-white p-1mm rounded border-light">الأحرفُ الزَّائدةُ</span>
    <span class="bg-white p-1mm rounded border-light">أمّا الشَّرطيَّةُ</span>
</div>'''
    ))

    # --- BLOCK 7 ---
    blocks.append(get_block(
        title="ثانيًا - الأسلوب الإنشائي",
        content='''<p class="text-accent mb-2mm">
الإنشاءُ كلامٌ لا يحتملُ الصِّدقَ أو الكذِبَ، ولا يصحُّ أنْ نقولَ لقائلِهِ: إنَّهُ صادقٌ فيه أو كاذبٌ.
</p>'''
    ))

    # --- BLOCK 8 ---
    blocks.append(get_table(
        title="أقسام الإنشاء",
        headers='''<th>نوع الإنشاء</th>
<th>تعريفه</th>
<th>أشكاله</th>''',
        rows='''<tr>
    <td class="font-bold text-primary">الإنشاء غير الطلبي</td>
    <td>وهو ما لا يستدعي مطلوبًا</td>
    <td>التَّعجُّب، المدح والذَّمّ، القَسَم، الترجي</td>
</tr>
<tr>
    <td class="font-bold text-primary">الإنشاء الطَّلبيّ</td>
    <td>يُطلب به حصولُ شيءٍ لم يكن حاصلًا وقتَ الطّلب</td>
    <td>الأمر، النّهي، النداء، التمني، الاستفهام</td>
</tr>'''
    ))

    # --- BLOCK 9 ---
    blocks.append(get_table(
        title="خروج الإنشاء الطَّلبيّ عن معناه الأصليّ",
        headers='''<th>نوعه</th>
<th>أدواته وصيغه</th>
<th>الأغراض البلاغية (من السياق)</th>''',
        rows='''<tr>
    <td class="font-bold text-primary">الأمر</td>
    <td>فعل الأمر، المضارع المقترن بلام الأمر، اسم فعل الأمر</td>
    <td>الدُّعاءُ، التحدّي، التمني، الالتماس، الحثُّ، الوعظ، الإرشاد، ...</td>
</tr>
<tr>
    <td class="font-bold text-primary">النَّهي</td>
    <td>له حالة واحدة: (لا) الناهية الجازمة + الفعل المضارع</td>
    <td>(يُفهم من السياق كالتهديد، التوبيخ، التحقير...)</td>
</tr>
<tr>
    <td class="font-bold text-primary">النداء</td>
    <td>
        <div class="text-sm">
            <div>(أ، أيْ، يا): للقريب</div>
            <div>(يا، أيا، هيا): للبعيد</div>
            <div>(وا): للنّدبة والاستغاثة</div>
        </div>
        <div class="text-xs mt-1mm text-grey-dark">قد يُنادى البعيد بحرف نداء القريب للتحبُّب، والعكس للتعظيم أو التحقير.</div>
    </td>
    <td>اللوم والتوبيخ، التّعظيم، العتاب، الزّجْر، الاستغاثة، الذّمّ، التحقير، التنبيه، الإغراء، ...</td>
</tr>
<tr>
    <td class="font-bold text-primary">التمني</td>
    <td>اداته (ليت)، وقد يشاركها في طلب التمنّي (لو، لعل)</td>
    <td>إن كان الشّيءُ مُمكِن الحصول سُمّي ترجيًا، ويكون بـ (لعل، عسى)</td>
</tr>
<tr>
    <td class="font-bold text-primary">الاستفهام</td>
    <td>الحرفان: (الهمزة، وهل). الأسماء: (مَنْ، منذا، ما، ماذا، متى، أيّان، أين، أنّى، كيف، أي، كَمْ).</td>
    <td>النفي، التقرير، التهكّم والسُّخرية، التحقير، التعجُّب، التشويق، التمنّي، الأمر، التحسُّر، الإنكار، التعظيم، ...</td>
</tr>'''
    ))

    # --- BLOCK 10 ---
    blocks.append(get_header(
        title="أمثلة تطبيقية",
        section="تطبيقات",
        category="شواهد",
        number=26,
        author_name="أ. الياس خفيف",
        author_phone="994066850 963+"
    ))

    # --- BLOCK 11 ---
    blocks.append(get_poem(
        title="",
        verses='''<div class="poem-line">
<span class="hemistich">أَيُهَذَا الشَّــاكي وَمَا بِكَ دَاءٌ</span>
<span class="hemistich">كَيْفَ تَغْدُو إِذَا غَدَوْتَ عَلِيــــــلا؟</span>
</div>''',
        poet_name="الشاعر",
        poet_bio="(إيليا أبو ماضي)"
    ))

    # --- BLOCK 12 ---
    blocks.append(get_block(
        title="تحليل المثال الأول",
        content='''<p><strong>س١- إلامَ خَرَجَ الاستفهامُ في قول الشّاعر؟</strong></p>
<p class="mt-2mm"><span class="highlight-green">ج١- خَرَجَ الاستفهامُ إلى معنى التّعجُّبِ والإنكار.</span></p>'''
    ))

    # --- BLOCK 13 ---
    blocks.append(get_poem(
        title="",
        verses='''<div class="poem-line">
<span class="hemistich">يا أَخِي في الشَّـــرقِ، في كُلِّ سَـــكَنْ</span>
<span class="hemistich">يا أَخِي في الأرضِ، في كُلِّ وَطَنْ</span>
</div>
<div class="poem-line">
<span class="hemistich">أَنَا أَدْعُوكَ... فَهَلْ تَعْرِفُنِي؟</span>
<span class="hemistich">يَا أَخَا أَعْرِفُهُ... رَغْمَ المِحَنْ سَــــاءْ</span>
</div>
<div class="poem-line">
<span class="hemistich">لَمْ أَعُدْ مَقْبَرَةً تَحكي البِلَى</span>
<span class="hemistich">لَمْ أَعُدْ سَــــاقِيَةً تَبكي الدِّمَــــــنْ</span>
</div>
<div class="poem-line">
<span class="hemistich">فَلَقَدْ ثُرْنَا عَلَى أَنْفُسِــــــنَا</span>
<span class="hemistich">ومحونا وصـــمـــة الذِّلَّةِ فيــــــن</span>
</div>''',
        poet_name="الشاعر"
    ))

    # --- BLOCK 14 ---
    blocks.append(get_block(
        title="تحليل المثال الثاني",
        content='''<p><strong>س٢- استخرج من الأبيات: (إنشاء طلبي بصيغة النّداء، إنشاء طلبي بصيغة الاستفهام، خبر ابتدائيّ، خبر إنكاري)، وحدد الغرض منها.</strong></p>
<ul class="structured-list mt-2mm">
    <li><span class="marker">•</span> <strong>النّداءُ:</strong> <span class="highlight-blue">يا أخي في الشّرق، يا أخي في الأرض، يا أخا أعرفُه.</span> – الغرضُ منه: <span class="text-accent">الاستغاثة والعتاب.</span></li>
    <li><span class="marker">•</span> <strong>الاستفهام:</strong> <span class="highlight-blue">هل تعرفُني؟.</span> الغرضُ منه: <span class="text-accent">التّحسُّرُ والتّمنّي.</span></li>
    <li><span class="marker">•</span> <strong>خبر ابتدائيّ:</strong> <span class="highlight-blue">لم أعُدْ مَقْبرةً، لم أعُدْ ساقيةً...</span> الغرضُ منه: <span class="text-accent">الفخرُ.</span></li>
    <li><span class="marker">•</span> <strong>خبر إنكاري:</strong> <span class="highlight-blue">لقَدْ ثُرْنا على أنفُسِنا.</span> الغرضُ منه: <span class="text-accent">الفخرُ.</span></li>
</ul>'''
    ))

    # --- BLOCK 15 ---
    blocks.append(get_poem(
        title="",
        verses='''<div class="poem-line">
<span class="hemistich">يَطُولُ عَلى قَلبِي الإنتِظَارُ</span>
<span class="hemistich">وَأغْرَقُ في بَحْرِ يَأْسٍ حَزِينْ</span>
</div>
<div class="poem-line">
<span class="hemistich">دَقَائِق... ثُمَّ أَخِيبُ، وأَهْتِــــــ</span>
<span class="hemistich">ــــــفُ: لا شَيْءَ يُشْــــبِهُ يوتوبيــــــا</span>
</div>''',
        poet_name="الشاعرة"
    ))

    # --- BLOCK 16 ---
    blocks.append(get_block(
        title="تحليل المثال الثالث",
        content='''<p><strong>س٣- هاتِ مثالين على الأسلوب الخبريّ، واذْكُر الغرَضَ البلاغيّ لِكُلٍّ منهما.</strong></p>
<ul class="structured-list mt-2mm">
    <li><span class="marker">•</span> <span class="highlight-blue">أغْرَقُ في بَحْرِ يَأْسٍ حزين.</span> – الغرضُ منه: <span class="text-accent">إظهارُ الضَّعْف.</span></li>
    <li><span class="marker">•</span> <span class="highlight-blue">دقائق ثمّ أخيبُ.</span> – الغرضُ منه: <span class="text-accent">إظهارُ خيبة الأمل.</span></li>
</ul>'''
    ))

    # --- BLOCK 17 ---
    blocks.append(get_poem(
        title="",
        verses='''<div class="poem-line">
<span class="hemistich">أَلا مَنْ يُرِينِي غَايتِي قَبْلَ مَذْهَبِي؟</span>
<span class="hemistich">ومِن أين والغَايَاتُ بَعْدَ المَذَاهِبِ؟!</span>
</div>''',
        poet_name="الشاعر"
    ))

    # --- BLOCK 18 ---
    blocks.append(get_block(
        title="تحليل المثال الرابع",
        content='''<p><strong>س٤- ما الغرَضُ مِنَ الاستفهام في البيت الآتي؟</strong></p>
<p class="mt-2mm"><span class="highlight-green">ج ٤ – الغرضُ منه التّحسُّرُ واللّوعَةُ واللَّهْفَةُ.</span></p>'''
    ))

    # --- BLOCK 19 ---
    blocks.append(get_poem(
        title="",
        verses='''<div class="poem-line">
<span class="hemistich">يَا غَائِصًا بالطِّينِ لا تَنْصَــــــبِ</span>
<span class="hemistich">يُوهِي عَزِيمتَــــه وَلا وصَــــــبِ</span>
</div>
<div class="poem-line">
<span class="hemistich">صَبْرًا على الأيّام إِنْ عَبَــــــثَتْ</span>
<span class="hemistich">هَيْهَاتَ يفــرجُ ضيقَهــــا غَضَــــــبِ</span>
</div>
<div class="poem-line">
<span class="hemistich">مَــــــا أَنــــــتَ أوّل كادِح غَرَّت</span>
<span class="hemistich">آمــــــالَــــهُ، وَكَبــــــا بــــهِ الــــدَّأَبِ</span>
</div>''',
        poet_name="الشاعر"
    ))

    # --- BLOCK 20 ---
    blocks.append(get_block(
        title="تحليل المثال الخامس",
        content='''<p><strong>س٥- استخدَم الشّاعر أسلوبين مُختلِفَين (إنشائيّ – خبري) للتّخفيف من مُعاناة البنّاء. حَدِّدْهُما.</strong></p>
<ul class="structured-list mt-2mm">
    <li><span class="marker">•</span> <strong>الأسلوبُ الإنشائيُّ:</strong> <span class="highlight-blue">يا غائِصًا بالطِّينِ</span> (في البيتِ الأوَّلِ). <span class="highlight-blue">صبرًا على الأيَّامِ</span> (في البيتِ الثَّاني).</li>
    <li><span class="marker">•</span> <strong>الأسلوبُ الخبريُّ:</strong> <span class="highlight-blue">هَيهاتَ يَفرُجُ ضيقَها غضَبٌ</span> (في البيتِ الثَّاني). <span class="highlight-blue">ما أنتَ أوَّلُ كادِحٍ عَثَرت آمالُهُ</span> (في البيتِ الثَّالثِ). <span class="highlight-blue">كبا بهِ الدَّأبُ</span> (في البيتِ الثَّالثِ).</li>
</ul>
<p class="mt-2mm"><strong>س- ما الغَرضُ مِن أسلوبِ النِّداءِ (يا غائِصًا)؟</strong></p>
<p class="mt-1mm"><span class="highlight-green">ج- إظهارُ الحسرةِ.</span></p>'''
    ))

    # --- BLOCK 21 ---
    blocks.append(get_list(
        title="تطبيقات إضافية (سَمِّ الأساليبَ وبَيِّنِ الغرضَ)",
        items='''<li>
    <div class="w-full">
        <div class="font-bold text-primary">والموتُ أهونُ مِن خَطبِهِ</div>
        <div>أسلوبٌ خَبَريٌّ، نوعُهُ ابتدائيٌّ. - غرَضُهُ: <span class="text-accent">إظهارُ مشاعرِ الذُّلِّ والانكِسارِ.</span></div>
    </div>
</li>
<li>
    <div class="w-full">
        <div class="font-bold text-primary">يا ريحُ، يا إبَرًا تَخيطُ لي الشِّراعَ</div>
        <div>إنشاءٌ طَلبيٌّ بصيغةِ النِّداءِ. - غرَضُهُ: <span class="text-accent">الاستِغاثَةُ.</span></div>
    </div>
</li>
<li>
    <div class="w-full">
        <div class="font-bold text-primary">ليتَ السَّفائنَ لا تُقاضي راكبيها</div>
        <div>إنشاءٌ طَلبيٌّ بصيغةِ التَّمنّي. - غرَضُهُ: <span class="text-accent">التَّمنّي والتَّحسُّرِ.</span></div>
    </div>
</li>
<li>
    <div class="w-full">
        <div class="font-bold text-primary">متى أعودُ إلى العراقِ؟ متى أعودُ؟</div>
        <div>إنشاءٌ طَلبيٌّ بصيغةِ الاستِفهامِ. - غرَضُهُ: <span class="text-accent">إظهارُ تَمنّي العودةِ.</span></div>
    </div>
</li>'''
    ))

    # --- BLOCK 22 ---
    blocks.append(get_exam([
        ('''<div class="mb-2mm">قالَ الشَّاعِرُ مُحَمَّد مَهدي الجواهري (٢٠١٣ عِلمي):</div>
<div class="poem-container text-center font-bold mb-2mm text-primary">
    وَكَلَّفْتُ نَفْسِي أَنْ تُحَقِّقَ سُؤْلَها<br>
    سِرَاعًا، أَوِ الموتَ الزُّؤَامَ سِراعَا
</div>
<div>استخرِجْ مِنَ البيتِ أسلوبًا خبريًّا، ثُمَّ اذكُرْ نوعَهُ.</div>''', "١"),
        ('''<div class="mb-2mm">قالَ الشَّاعِرُ إيليا أبو ماضي (٢٠١٣ عِلمي):</div>
<div class="poem-container text-center font-bold mb-2mm text-primary">
    كُنْ مَعَ الفَجْرِ نسمةً تُوسِعُ الأَزْ<br>
    هارَ شَمًّا وَتارَةً تقبيـــــــلا
</div>
<div>هاتِ مِنَ البيتِ أسلوبًا خبريًّا، واذكُرْ نوعَهُ.</div>''', "٢"),
        ('''<div class="mb-2mm">قالَ الشَّاعِرُ محمَّد الفيتوري (٢٠١٤ عِلمي):</div>
<div class="poem-container text-center font-bold mb-2mm text-primary">
    نحنُ أهرقْنَا عليها دَمَنَا<br>
    ومَزَجْنَا بثرَاها عظْمَنَا
</div>
<div>استخرِجْ مِنَ البيتِ أسلوبًا خبريًّا، واذكُر نوعَه.</div>''', "٣")
    ]))


    # --- LAYOUT LOGIC ---
    current_page_blocks = []
    page_sub = 0
    final_files = []

    # Track current header info
    current_header = {
        "title": "الأسلوب الخبري والأسلوب الإنشائي",
        "section": "المستوى الفني",
        "category": "فوائد",
        "number": 26,
        "author_name": "أ. الياس خفيف",
        "author_phone": "994066850 963+"
    }

    def extract_header_info(block_html):
        # Simple regex to extract header info if it's a header block
        if 'class="page-header-strip"' in block_html:
            # Extract Title
            m_title = re.search(r'<h1 class="header-title">(.*?)</h1>', block_html)
            title = m_title.group(1) if m_title else ""

            # Extract Section/Category (Simplified assumption based on template structure)
            # The template has:
            # <div class="lesson-details">
            #    <div>[SECTION_HEADER]</div>
            #    <div>[CATEGORY_HEADER]</div>
            # </div>
            m_details = re.findall(r'<div class="lesson-details">\s*<div>(.*?)</div>\s*<div>(.*?)</div>', block_html, re.DOTALL)
            if m_details:
                section, category = m_details[0]
            else:
                section, category = "", ""

            return {
                "title": title,
                "section": section,
                "category": category,
                "number": 26, # Assuming constant
                "author_name": "أ. الياس خفيف", # Assuming constant
                "author_phone": "994066850 963+" # Assuming constant
            }
        return None

    for i, block in enumerate(blocks):
        # Check if this block is a header and update current info
        new_header = extract_header_info(block)
        if new_header:
            current_header.update(new_header)

        current_page_blocks.append(block)

        # Verify layout
        temp_file, content = create_page(current_page_blocks, page_sub)

        # Write to file
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write(content)

        result = verify_layout(temp_file)
        print(f"Adding Block {i+1}... Status: {result['status']}")

        if result['status'] == 'OVERFLOW':
            print("  -> Overflow! Splitting...")
            # Remove the last block (it caused overflow)
            current_page_blocks.pop()

            # Re-verify without the block
            temp_file, content = create_page(current_page_blocks, page_sub)
            with open(temp_file, 'w', encoding='utf-8') as f:
                f.write(content)

            res_prev = verify_layout(temp_file)

            if res_prev['status'] == 'UNDERFLOW':
                 print(f"  -> Page {page_sub} is UNDERFLOW. Filling with generic content...")
                 # Add generic exam or benefit to fill space
                 filler = get_benefit("فائدة", "انتبه إلى أن البلاغة تتطلب ذوقاً أدبياً رفيعاً لفهم الأغراض البلاغية.")
                 current_page_blocks.append(filler)

                 # Write again
                 temp_file, content = create_page(current_page_blocks, page_sub)
                 with open(temp_file, 'w', encoding='utf-8') as f:
                     f.write(content)

            final_files.append(temp_file)
            print(f"  -> Saved {temp_file}")

            # Start new page
            page_sub += 1
            current_page_blocks = []

            # Check if the block we popped is a header itself
            # If it is, we don't add a continuation header.
            # If it's not, we add a continuation header based on current_header.

            popped_block_is_header = extract_header_info(block) is not None

            if not popped_block_is_header:
                # Add header with (تابع)
                header_تابع = get_header(
                    title=f"{current_header['title']} (تابع)",
                    section=current_header['section'],
                    category=current_header['category'],
                    number=current_header['number'],
                    author_name=current_header['author_name'],
                    author_phone=current_header['author_phone']
                )
                current_page_blocks.append(header_تابع)

            current_page_blocks.append(block) # The block that caused overflow

    # Process remaining blocks
    if current_page_blocks:
        temp_file, content = create_page(current_page_blocks, page_sub)
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write(content)

        result = verify_layout(temp_file)
        if result['status'] == 'UNDERFLOW':
             print(f"  -> Final Page {page_sub} is UNDERFLOW. Filling...")
             # Add filler
             filler = get_benefit("فائدة إضافية", "تذكر أن الخبر الإنكاري يحتاج إلى مؤكدين فأكثر.")
             current_page_blocks.append(filler)
             create_page(current_page_blocks, page_sub)

        final_files.append(temp_file)
        print(f"  -> Saved {temp_file}")

if __name__ == "__main__":
    main()
