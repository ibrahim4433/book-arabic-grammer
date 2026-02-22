import os
import re

# Define paths
TEMPLATE_DIR = "Jules-workspace/Templates/"
OUTPUT_FILE_1 = "pages/13.0_nXX_الإعلال.html"
OUTPUT_FILE_2 = "pages/13.1_nXX_الإعلال.html"

def read_template(filename):
    with open(os.path.join(TEMPLATE_DIR, filename), "r", encoding="utf-8") as f:
        return f.read()

def clean_block_template(tpl, remove_p=False):
    no_benefit = tpl.split('<div class="benefit-box">')[0] + '</div>\n    </section>'
    if remove_p:
        pattern = r'<p class="[^"]*">\s*\[CONTENT_TEXT\]\s*</p>'
        no_benefit = re.sub(pattern, '[CONTENT_TEXT]', no_benefit, flags=re.DOTALL)
    return no_benefit

def generate_pages():
    # Read templates
    tpl_base = read_template("TEMPLATE_C_BASE.html")
    tpl_wrapper = read_template("TEMPLATE_C_PAGE_WRAPPER.html")
    tpl_header = read_template("TEMPLATE_C_HEADER.html")
    tpl_block = read_template("TEMPLATE_C_BLOCK.html")
    tpl_table = read_template("TEMPLATE_C_TABLE.html")
    tpl_split = read_template("TEMPLATE_C_SPLIT.html")
    tpl_list = read_template("TEMPLATE_C_LIST.html")
    tpl_list_item = read_template("TEMPLATE_C_LIST_ITEM.html")
    tpl_benefit_tip = read_template("TEMPLATE_C_BENEFIT_TIP.html")
    tpl_irab_row = read_template("TEMPLATE_C_IRAB_ROW.html")
    tpl_irab_box = read_template("TEMPLATE_C_IRAB_BOX.html")
    tpl_chips = read_template("TEMPLATE_C_CHIPS.html")
    tpl_exam = read_template("TEMPLATE_C_EXAM.html")

    # --- SHARED: Header Function ---
    def get_header(suffix=""):
        title = "الإعلال" + suffix
        return tpl_header.replace("[LESSON_NUMBER]", "13") \
                         .replace("[CHAPTER_TITLE]", title) \
                         .replace("[CATEGORY_HEADER]", "الصرف") \
                         .replace("[SECTION_HEADER]", "المستوى اللغوي") \
                         .replace("[AUTHOR_NAME]", "أ. الياس خفيف") \
                         .replace("[AUTHOR_PHONE]", "994066850 963+")

    # --- PAGE 1 CONTENT ---

    # Block 2
    def_content = '<p class="text-accent mb-2mm">الإعلال: هو تغييرٌ يصيب حرف العلّة، وله ثلاثة أنواع:</p>'
    tpl_block_clean_p = clean_block_template(tpl_block, remove_p=True)
    block2_html = tpl_block_clean_p.replace("[BLOCK_TITLE]", "تعريف الإعلال") \
                                   .replace("[CONTENT_TEXT]", def_content)

    # Block 3
    rows = ""
    rows += "<tr><td>الإعلال بالتّسكين</td><td>تسكينُ أحد حرفي العلّة (الواو أو الياء) لثقلهما، فالألف ساكنة دائمًا.</td><td>يَسْمُوْ (أصله يَسْمُوُ)، يَمْشِيْ (أصله يَمْشِيُ)</td></tr>"
    rows += "<tr><td>الإعلال بالحذْف</td><td>حذفُ حرفِ العلةِ للتخلص من التقاء الساكنين أو في حالات الجزم والبناء.</td><td>قُلْ (حذفت الواو)، لَمْ يَمْشِ (حذفت الياء)</td></tr>"
    rows += "<tr><td>الإعلال بالقلب</td><td>قَلبُ حرفِ العِلَّةِ إلى حرفٍ آخر (ألف، واو، ياء) لعلة صرفية.</td><td>قَالَ (أصله قَوَلَ)، صِيَام (أصله صِوَام)، مُوْقِن (أصله مُيْقِن)</td></tr>"
    block3_html = tpl_table.replace("[TABLE_TITLE]", "أنواع الإعلال الثلاثة") \
                           .replace("[TABLE_HEADERS]", "<th>النّوع</th><th>التّعريف</th><th>مثال</th>") \
                           .replace("[TABLE_ROWS]", rows)

    # Block 4
    left_content = '<p>إذا وقع حرفُ <span class="highlight-red">الواوِ</span> أو <span class="highlight-red">الياءِ</span> في لامِ الكلمةِ (آخرِها) مسبوقينِ بحركة مجانسة:</p><ul class="structured-list"><li><span class="highlight-blue">الواو:</span> إذا سُبقت بضمٍّ تَسْكُن (يَسْمُوْ).</li><li><span class="highlight-blue">الياء:</span> إذا سُبقت بكسرٍ تَسْكُن (يَمْشِيْ).</li></ul>'
    right_content = '<p>إذا وقع حرفُ <span class="highlight-red">الواوِ</span> أو <span class="highlight-red">الياءِ</span> في عينِ الكلمةِ (وسطِها) مُتَحرِّكَينِ مسبوقينِ بحرفٍ <span class="highlight-blue">صحيحٍ ساكنٍ</span>:</p><p class="text-sm">يُسَكَّنانِ وتُنقَل حركتُهما إلى الساكن الصحيح قبلهما.</p><p class="text-center mt-2mm"><span class="highlight-green">يَقُوْمُ</span> (أصلها يَقْوُمُ) | <span class="highlight-green">يَبِيْنُ</span> (أصلها يَبْيِنُ)</p>'
    block4_html = tpl_split.replace("[LEFT_TITLE]", "الحالة الأولى: في لام الكلمة") \
                           .replace("[LEFT_CONTENT]", left_content) \
                           .replace("[RIGHT_TITLE]", "الحالة الثانية: في عين الكلمة") \
                           .replace("[RIGHT_CONTENT]", right_content)

    # Block 5
    items = ""
    content1 = '<strong>في أول الكلمة (المثال):</strong> يُحذف حرف العلة في المضارع والأمر من المثال الواوي.<br>مثال: <span class="highlight-red">يَزِنُ</span> (حُذِفَت الواو لوقوعها في أول المضارع)، <span class="highlight-red">زِنْ</span> (حُذِفَت الواو في الأمر).'
    items += tpl_list_item.replace("[MARKER]", "1").replace("[CONTENT]", content1)
    content2 = '<strong>في وسط الكلمة (الأجوف):</strong> يُحذف حرف العلة إذا التقى بساكن بعده.<br>مثال: <span class="highlight-red">قُلْ</span> (حُذِفَت الواو لالتقاء الساكنين).'
    items += tpl_list_item.replace("[MARKER]", "2").replace("[CONTENT]", content2)
    nested_ul = '<ul class="structured-list"><li><strong>المضارع المجزوم:</strong> <span class="highlight-blue">لَمْ يَمْشِ</span> (حُذِفَت الياء).</li><li><strong>أمر المفرد المذكر:</strong> <span class="highlight-blue">اسْعَ</span> (حُذِفَت الألف).</li><li><strong>الماضي المتصل بـ (تْ) أو (وا):</strong> <span class="highlight-blue">مَشَتْ</span> (حُذِفَت الألف)، <span class="highlight-blue">دَعَوْا</span> (حُذِفَت الألف).</li></ul>'
    content3 = '<strong>في آخر الكلمة (الناقص):</strong></span>' + nested_ul + '<span>'
    items += tpl_list_item.replace("[MARKER]", "3").replace("[CONTENT]", content3)
    list_no_benefit = tpl_list.split('<hr class="separator-dashed">')[0] + '</div>\n    </section>'
    block5_html = list_no_benefit.replace("[LIST_TITLE]", "مواضع الإعلال بالحذْف") \
                                 .replace("[LIST_ITEMS]", items)

    # Block 6
    block6_html = tpl_benefit_tip.replace("[TIP_TITLE]", "قاعدة هامة") \
                                 .replace("[TIP_TEXT]", "الحرفُ الصّحيحُ أقدرُ على تحمُّلِ الحركةِ من الحرفِ المعتلِّ، لذا في الإعلال بالتسكين (عين الكلمة) تُنقل الحركة من المعتل إلى الصحيح الساكن قبله.")

    # Block 7
    chip_class = "bg-grey-lighter rounded p-1mm border-light"
    chips_content = f'<span class="{chip_class}">قَالَ (قَوَلَ)</span><span class="{chip_class}">بَاعَ (بَيَعَ)</span><span class="{chip_class}">سَمَا (سَمَوَ)</span><span class="{chip_class}">جَرَى (جَرَيَ)</span>'
    chips_html = tpl_chips.replace("[CHIPS_CONTENT]", chips_content)
    part1 = f'''<div class="mb-4mm">
<p class="font-bold text-accent">١- قلب الواو أو الياء ألفًا:</p>
<p>إذا تحرّكتا وانفتح ما قبلهما.</p>
{chips_html}
</div>'''
    part2 = '''<div class="mb-4mm">
<p class="font-bold text-accent">٢- قلب الواو ياءً:</p>
<ul class="structured-list">
<li>تطَرَّفَتْ بعدَ كسرٍ: <span class="highlight-red">رَضِيَ</span> (رَضِوَ)، <span class="highlight-red">قَوِيَ</span> (قَوِوَ).</li>
<li>وقَعَتْ حشوًا بينَ كسرةٍ وألفٍ: <span class="highlight-red">قِيَام</span> (قِوَام)، <span class="highlight-red">صِيَام</span> (صِوَام).</li>
<li>سُكِّنَتْ بعدَ كَسْرٍ: <span class="highlight-red">مِيْزَان</span> (مِوْزَان)، <span class="highlight-red">مِيْعَاد</span> (مِوْعَاد).</li>
<li>اجتمعَتِ الواو والياءُ (الأولى ساكنة): <span class="highlight-red">سَيِّد</span> (سَيْوِد)، <span class="highlight-red">مَيِّت</span> (مَيْوِت).</li>
</ul>
</div>'''
    part3 = '''<div>
<p class="font-bold text-accent">٣- قلب الياء واوًا:</p>
<p>إذا سكنت بعد ضمٍّ.</p>
<p class="text-center"><span class="highlight-green">مُوْقِن</span> (أصلها مُيْقِن) | <span class="highlight-green">مُوْسِر</span> (أصلها مُيْسِر)</p>
</div>'''
    qalb_content = part1 + part2 + part3
    block7_html = tpl_block_clean_p.replace("[BLOCK_TITLE]", "مواضع الإعلال بالقلب") \
                                   .replace("[CONTENT_TEXT]", qalb_content)

    # --- PAGE 2 CONTENT ---

    # Block 8 (Irab)
    box1 = tpl_irab_box.replace("[WORD]", "يَقُومُ").replace("[PARSING_DETAILS]", "فعل مضارع مرفوع، وفيه إعلال بالتسكين، أصله (يَقْوُمُ)، نُقلت حركة الواو إلى القاف الساكنة قبلها فصارت (يَقُومُ).")
    box2 = tpl_irab_box.replace("[WORD]", "لَمْ يَمْشِ").replace("[PARSING_DETAILS]", "فعل مضارع مجزوم بلم، وعلامة جزمه حذف حرف العلة (الياء) من آخره، وهو إعلال بالحذف.")
    box3 = tpl_irab_box.replace("[WORD]", "قَالَ").replace("[PARSING_DETAILS]", "فعل ماض مبني على الفتح، وفيه إعلال بالقلب، أصله (قَوَلَ)، تحركت الواو وانفتح ما قبلها فقلبت ألفًا.")
    block8_html = tpl_irab_row.replace("[IRAB_BOXES]", box1 + box2 + box3)

    # New Benefit: Origin of Alif
    origin_content = '''
    <p>لمعرفة أصل الألف (واو أو ياء) نرجع إلى:</p>
    <ul class="structured-list">
        <li><strong>المضارع:</strong> (قَال -> يَقُول -> واو)، (بَاع -> يَبِيع -> ياء).</li>
        <li><strong>المصدر:</strong> (سَعَى -> سَعْيًا -> ياء)، (دَعَا -> دَعْوَةً -> واو).</li>
        <li><strong>إسناد الفعل لضمير رفع:</strong> (دَعَا -> دَعَوْتُ)، (رَمَى -> رَمَيْتُ).</li>
    </ul>
    '''
    # Using clean block template (no benefit box) but populated with benefit-like content
    new_benefit_html = tpl_block_clean_p.replace("[BLOCK_TITLE]", "فائدة: معرفة أصل الألف") \
                                        .replace("[CONTENT_TEXT]", origin_content)

    # Block 10 (Conjugation Table - Extra Content for Density)
    rows_tasreef = ""
    rows_tasreef += "<tr><td>أنا</td><td>قُلْتُ (حذف)</td><td>أَقُولُ</td><td>-</td><td>مَشَيْتُ</td><td>أَمْشِي</td><td>-</td></tr>"
    rows_tasreef += "<tr><td>أنتَ</td><td>قُلْتَ (حذف)</td><td>تَقُولُ</td><td>قُلْ (حذف)</td><td>مَشَيْتَ</td><td>تَمْشِي</td><td>امْشِ (حذف)</td></tr>"
    rows_tasreef += "<tr><td>هو</td><td>قَالَ (قلب)</td><td>يَقُولُ</td><td>-</td><td>مَشَى (قلب)</td><td>يَمْشِي</td><td>-</td></tr>"
    rows_tasreef += "<tr><td>هي</td><td>قَالَتْ (قلب)</td><td>تَقُولُ</td><td>-</td><td>مَشَتْ (حذف)</td><td>تَمْشِي</td><td>-</td></tr>"
    rows_tasreef += "<tr><td>نحن</td><td>قُلْنَا (حذف)</td><td>نَقُولُ</td><td>-</td><td>مَشَيْنَا</td><td>نَمْشِي</td><td>-</td></tr>"
    rows_tasreef += "<tr><td>هم</td><td>قَالُوا (قلب)</td><td>يَقُولُونَ</td><td>قُولُوا</td><td>مَشَوْا (حذف)</td><td>يَمْشُونَ (حذف)</td><td>امْشُوا (حذف)</td></tr>"
    rows_tasreef += "<tr><td>هنّ</td><td>قُلْنَ (حذف)</td><td>يَقُلْنَ (حذف)</td><td>قُلْنَ (حذف)</td><td>مَشَيْنَ</td><td>يَمْشِينَ</td><td>امْشِينَ</td></tr>"

    block_tasreef_html = tpl_table.replace("[TABLE_TITLE]", "تطبيقات إعلالية: تصريف (قَالَ) و(مَشَى)") \
                                  .replace("[TABLE_HEADERS]", "<th>الضمير</th><th>الماضي (قَالَ)</th><th>المضارع (يَقُولُ)</th><th>الأمر (قُلْ)</th><th>الماضي (مَشَى)</th><th>المضارع (يَمْشِي)</th><th>الأمر (امْشِ)</th>") \
                                  .replace("[TABLE_ROWS]", rows_tasreef)

    # Block 9 (Exam)
    q1_text = "بيّن نوع الإعلال وسببه في الكلمات الآتية: (يَصُومُ - ادْعُ - مِيقَات)."
    q2_text = "هاتِ أصل الكلمات الآتية وبيّن ما حدث فيها من تغيير: (بَاعَ - مَشَى)."
    q3_text = "علّل حذف حرف العلة في كلمة (قُلْ) وقلبه ياءً في كلمة (سَيِّد)."
    q4_text = "استخرج كلمات فيها إعلال من قوله تعالى: ﴿قَالَ رَبِّ إِنِّي وَهَنَ الْعَظْمُ مِنِّي﴾ وبين نوعه."
    q5_text = "هاتِ اسم الفاعل من (قَامَ) واسم المفعول من (خَافَ) واشرح الإعلال فيهما."

    exam_parts = tpl_exam.split('<div class="block-body">')
    exam_header = exam_parts[0] + '<div class="block-body">'
    exam_footer = '</div>\n</section>'

    def q_html(n, text, last=False):
        cls = "exam-question mb-0 border-none pb-0" if last else "exam-question"
        return f'''<div class="{cls}" id="[Q{n}_ID]">
            <p class="m-0 mb-2mm">
                <span class="exam-number">{n}</span>
                {text}
            </p>
            <div class="border-light h-8mm bg-grey-lighter rounded"></div>
        </div>'''

    exam_body = q_html(1, q1_text) + q_html(2, q2_text) + q_html(3, q3_text) + q_html(4, q4_text) + q_html(5, q5_text, True)
    block9_html = exam_header.replace("[TOPIC]", "الإعلال") + exam_body + exam_footer

    # --- ASSEMBLY ---

    # Page 1
    content_p1 = get_header() + "\n" + block2_html + "\n" + block3_html + "\n" + block4_html + "\n" + block5_html + "\n" + block6_html + "\n" + block7_html
    page1_wrapper = tpl_wrapper.replace("<!-- INJECT_CONTENT_HERE -->", content_p1)
    final_html_1 = tpl_base.replace("<!-- INJECT_CONTENT_HERE -->", page1_wrapper)
    final_html_1 = re.sub(r' id="\[.*?\]"', '', final_html_1)

    # Page 2
    content_p2 = get_header(" (تابع)") + "\n" + block8_html + "\n" + new_benefit_html + "\n" + block_tasreef_html + "\n" + block9_html
    page2_wrapper = tpl_wrapper.replace("<!-- INJECT_CONTENT_HERE -->", content_p2)
    final_html_2 = tpl_base.replace("<!-- INJECT_CONTENT_HERE -->", page2_wrapper)
    final_html_2 = re.sub(r' id="\[.*?\]"', '', final_html_2)

    # Write files
    with open(OUTPUT_FILE_1, "w", encoding="utf-8") as f:
        f.write(final_html_1)
    print(f"Generated {OUTPUT_FILE_1}")

    with open(OUTPUT_FILE_2, "w", encoding="utf-8") as f:
        f.write(final_html_2)
    print(f"Generated {OUTPUT_FILE_2}")

if __name__ == "__main__":
    generate_pages()
