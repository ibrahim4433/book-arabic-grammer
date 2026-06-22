import os
import re
import random

# Configuration
TEMPLATES_DIR = 'Jules-workspace/Templates/'
OUTPUT_FILE = 'pages/18-الهمزة المتوسطة.html'

def load_template(filename):
    path = os.path.join(TEMPLATES_DIR, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Remove explicit ID placeholders
    content = re.sub(r'\s*id="\[[^\]]+\]"', '', content)
    return content

def generate_id():
    return f"b{random.randint(10000, 99999)}"

def clean_block(content):
    content = re.sub(r'<div class="benefit-box">\s*<strong> \[BENEFIT_TITLE\]:</strong> \[BENEFIT_TEXT\]\s*</div>', '', content)
    content = re.sub(r'<hr class="separator-dashed">\s*<div class="benefit-box">\s*<strong> \[NOTE_TITLE\]:</strong> \[NOTE_TEXT\]\s*</div>', '', content)
    return content

def main():
    t_base = load_template('TEMPLATE_C_BASE.html')
    t_header = load_template('TEMPLATE_C_HEADER.html')
    t_block = load_template('TEMPLATE_C_BLOCK.html')
    t_chips = load_template('TEMPLATE_C_CHIPS.html')
    t_table = load_template('TEMPLATE_C_TABLE.html')
    t_table_row = load_template('TEMPLATE_C_TABLE_ROW.html')
    t_split = load_template('TEMPLATE_C_SPLIT.html')
    t_list = load_template('TEMPLATE_C_LIST.html')
    t_list_item = load_template('TEMPLATE_C_LIST_ITEM.html')
    t_benefit = load_template('TEMPLATE_C_BENEFIT_TIP.html')
    t_exam = load_template('TEMPLATE_C_EXAM.html')
    t_wrapper = load_template('TEMPLATE_C_PAGE_WRAPPER.html')

    content_blocks = []

    # 1. Header
    header = t_header.replace('[LESSON_NUMBER]', '18') \
                     .replace('[CHAPTER_TITLE]', 'الهمزة المتوسطة') \
                     .replace('[CATEGORY_HEADER]', 'الإملاء') \
                     .replace('[SECTION_HEADER]', 'المستوى اللغوي') \
                     .replace('[AUTHOR_NAME]', 'أ. الياس خفيف') \
                     .replace('[AUTHOR_PHONE]', '994066850 963+')
    content_blocks.append(header)

    # 2. Definition
    block2 = t_block.replace('[BLOCK_TITLE]', 'تَعْرِيفُ الْهَمْزَةِ الْمُتَوَسِّطَةِ') \
                    .replace('[CONTENT_TEXT]', 'هِيَ الْهَمْزَةُ الَّتِي تَقَعُ فِي <span class="text-accent">وَسَطِ الْكَلِمَةِ</span>. وَلِكِتَابَتِهَا قَاعِدَةٌ عَامَّةٌ تَعْتَمِدُ عَلَى الْمُقَارَنَةِ بَيْنَ <span class="highlight-red">حَرَكَتِهَا</span> وَحَرَكَةِ <span class="highlight-blue">الْحَرْفِ الَّذِي قَبْلَهَا</span>، فَنَرْسُمُهَا عَلَى الْحَرْفِ الَّذِي يُنَاسِبُ <span class="font-bold">أَقْوَى الْحَرَكَتَيْنِ</span>.')
    content_blocks.append(clean_block(block2))

    # 3. Chips
    items = ["الْكَسْرَةُ (أَقْوَى شَيْءٍ)", "الضَّمَّةُ", "الْفَتْحَةُ", "السُّكُونُ (أَضْعَفُ شَيْءٍ)"]
    chips_html = "".join([f'<span class="bg-grey-lighter rounded p-1mm">{item}</span>\n' for item in items])
    block3_content = t_chips.replace('[CHIPS_CONTENT]', chips_html)
    block3_wrapper = t_block.replace('[BLOCK_TITLE]', 'تَسَلْسُلُ قُوَّةِ الْحَرَكَاتِ')
    block3_wrapper = re.sub(r'<p class="mt-1mm text-accent">.*?</p>', block3_content, block3_wrapper, flags=re.DOTALL)
    content_blocks.append(clean_block(block3_wrapper))

    # 4. Table
    headers = ["الْحَرَكَةُ الْأَقْوَى", "الْحَرْفُ الْمُنَاسِبُ", "أَمْثِلَةٌ"]
    headers_html = "".join([f"<th>{h}</th>" for h in headers])
    rows_data = [
        ["الْكَسْرَةُ", "النَّبْرَةُ (ـئـ)", "تَئِن، سُئِل، بِئْر"],
        ["الضَّمَّةُ", "الْوَاوُ (ـؤـ)", "مُؤْمِن، يُؤَدِّي، سُؤَال"],
        ["الْفَتْحَةُ", "الْأَلِفُ (ـأـ)", "سَأَلَ، رَأْس، الْبَأْس"]
    ]
    rows_html = "".join([
        t_table_row.replace('[CELL_1]', r[0]).replace('[CELL_2]', r[1]).replace('[CELL_3]', r[2])
        for r in rows_data
    ])
    block4 = t_table.replace('[TABLE_TITLE]', 'جَدْوَلُ الْقَاعِدَةِ الْعَامَّةِ') \
                    .replace('[TABLE_HEADERS]', headers_html) \
                    .replace('[TABLE_ROWS]', rows_html)
    content_blocks.append(block4)

    # 5. Split
    block5_title = t_block.replace('[BLOCK_TITLE]', 'أَمْثِلَةٌ تَطْبِيقِيَّةٌ مُفَصَّلَةٌ') \
                          .replace('[CONTENT_TEXT]', 'إِلَيْكَ تَفْصِيلُ الْأَمْثِلَةِ وَتَعْلِيلِهَا:')
    content_blocks.append(clean_block(block5_title))

    left_items = ["١. <span class='highlight-red'>تَئِن</span>", "٢. <span class='highlight-red'>الْبَأْس</span>", "٣. <span class='highlight-red'>سَأَلَ</span>"]
    right_items = ["١. هَمْزَةٌ مُتَوَسِّطَةٌ <span class='highlight-red'>مَكْسُورَةٌ</span> سُبِقَتْ <span class='highlight-blue'>بِفَتْحٍ</span>. (الْكَسْرُ أَقْوَى مِنَ الْفَتْحِ -> نَبْرَة).", "٢. هَمْزَةٌ مُتَوَسِّطَةٌ <span class='highlight-red'>سَاكِنَةٌ</span> سُبِقَتْ <span class='highlight-blue'>بِفَتْحٍ</span>. (الْفَتْحُ أَقْوَى مِنَ السُّكُونِ -> أَلِف).", "٣. هَمْزَةٌ مُتَوَسِّطَةٌ <span class='highlight-red'>مَفْتُوحَةٌ</span> سُبِقَتْ <span class='highlight-blue'>بِفَتْحٍ</span>. (تَمَاثَلَتِ الْحَرَكَتَانِ -> أَلِف)."]

    left_ul = '<ul class="structured-list">' + "".join([t_list_item.replace('[MARKER]', '•').replace('[CONTENT]', i) for i in left_items]) + '</ul>'
    right_ul = '<ul class="structured-list">' + "".join([t_list_item.replace('[MARKER]', '•').replace('[CONTENT]', i) for i in right_items]) + '</ul>'

    block5 = t_split.replace('[LEFT_TITLE]', 'الْكَلِمَاتُ').replace('[LEFT_CONTENT]', left_ul) \
                    .replace('[RIGHT_TITLE]', 'التَّحْلِيلُ وَالتَّعْلِيلُ').replace('[RIGHT_CONTENT]', right_ul)
    content_blocks.append(block5)

    # 6. Exceptions Header
    block6 = t_block.replace('[BLOCK_TITLE]', 'الْحَالَاتُ الشَّاذَّةُ') \
                    .replace('[CONTENT_TEXT]', 'تَشِذُّ عَنِ الْقَاعِدَةِ الْعَامَّةِ حَالَتَانِ رَئِيسِيَّتَانِ، حَيْثُ لَا نَنْظُرُ إِلَى قُوَّةِ الْحَرَكَاتِ بَلْ نَتَّبِعُ قَاعِدَةً خَاصَّةً.')
    content_blocks.append(clean_block(block6))

    # 7. Exceptions Split
    left_body = 'تُكْتَبُ الْهَمْزَةُ الْمُتَوَسِّطَةُ عَلَى <span class="highlight-red">السَّطْرِ</span> إِذَا جَاءَتْ <span class="highlight-blue">مَفْتُوحَةً</span> بَعْدَ:<br>١. <span class="font-bold">أَلِفٍ سَاكِنَةٍ</span>. مِثْلُ: <span class="highlight-red">عَبَاءَة</span>.<br>٢. <span class="font-bold">وَاوٍ سَاكِنَةٍ</span>. مِثْلُ: <span class="highlight-red">السَّمَوْءَل</span> (حَالَةٌ شَاذَّةٌ).'
    right_body = 'تُكْتَبُ الْهَمْزَةُ الْمُتَوَسِّطَةُ عَلَى <span class="highlight-red">النَّبْرَةِ</span> إِذَا جَاءَتْ <span class="highlight-blue">مُتَحَرِّكَةً</span> بَعْدَ:<br>١. <span class="font-bold">يَاءٍ سَاكِنَةٍ</span>.<br>أَمْثِلَةٌ:<br>- <span class="highlight-red">بِيْئَة</span> (مَفْتُوحَةٌ بَعْدَ يَاءٍ سَاكِنَةٍ).<br>- <span class="highlight-red">فَيْئُهَا</span> (مَضْمُومَةٌ بَعْدَ يَاءٍ سَاكِنَةٍ).'
    block7 = t_split.replace('[LEFT_TITLE]', 'الْهَمْزَةُ عَلَى السَّطْرِ').replace('[LEFT_CONTENT]', f'<p class="mt-1mm text-accent">{left_body}</p>') \
                    .replace('[RIGHT_TITLE]', 'الْهَمْزَةُ عَلَى النَّبْرَةِ').replace('[RIGHT_CONTENT]', f'<p class="mt-1mm text-accent">{right_body}</p>')
    content_blocks.append(block7)

    # 8. Benefit
    block8 = t_benefit.replace('[TIP_TITLE]', 'فَائِدَةٌ هَامَّةٌ') \
                      .replace('[TIP_TEXT]', 'تَذَكَّرْ دَائِمًا أَنَّ <span class="font-bold highlight-red">الْكَسْرَةَ</span> هِيَ أَقْوَى الْحَرَكَاتِ عَلَى الْإِطْلَاقِ، وَوُجُودُهَا (سَوَاءٌ عَلَى الْهَمْزَةِ أَوْ عَلَى الْحَرْفِ الَّذِي قَبْلَهَا) يَجْعَلُ الْهَمْزَةَ تُكْتَبُ عَلَى <span class="highlight-blue">النَّبْرَةِ</span> دَائِمًا، مَا لَمْ تَكُنْ حَالَةً شَاذَّةً تَتَعَلَّقُ بِالسَّطْرِ.')
    content_blocks.append(block8)

    # 9. Exam
    block9 = t_exam.replace('[TOPIC]', 'الهمزة المتوسطة') \
                   .replace('[QUESTION_TEXT]', 'عَلِّلْ كِتَابَةَ الْهَمْزَةِ فِي كَلِمَةِ (<span class="highlight-red">مُؤْمِن</span>) وَفْقَ الْقَاعِدَةِ الْعَامَّةِ.', 1) \
                   .replace('[QUESTION_TEXT]', 'عَلِّلْ كِتَابَةَ الْهَمْزَةِ فِي كَلِمَةِ (<span class="highlight-red">بِيْئَة</span>) وَاذْكُرْ هَلْ هِيَ حَالَةٌ قِيَاسِيَّةٌ أَمْ شَاذَّةٌ.', 1)
    content_blocks.append(block9)

    # Final Assembly
    full_content = "\n".join(content_blocks)
    final_html = t_base.replace('<!-- INJECT_CONTENT_HERE -->', t_wrapper.replace('<!-- INJECT_CONTENT_HERE -->', full_content))

    # Inject IDs with robust regex
    def inject_id(match):
        return f'{match.group(1)} id="{generate_id()}"'

    # Match class attributes containing specific keywords, capture the whole attribute
    final_html = re.sub(r'(class="[^"]*?\bcontent-block\b[^"]*?")', inject_id, final_html)
    final_html = re.sub(r'(class="[^"]*?\bexam-question\b[^"]*?")', inject_id, final_html)
    final_html = re.sub(r'(class="[^"]*?\bbenefit-box\b[^"]*?")', inject_id, final_html)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(final_html)

    print(f"Generated {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
