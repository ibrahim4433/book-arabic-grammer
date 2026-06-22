import os
import sys
import json
import re
import subprocess
from bs4 import BeautifulSoup

# Paths
TEMPLATE_DIR = 'Jules-workspace/Templates/'
PAGES_DIR = 'pages/'
VERIFY_SCRIPT = 'Jules-workspace/verify_layout.py'
OUTPUT_FILE_1 = os.path.join(PAGES_DIR, '29-وظائف عناصر المستوى التركيبي.html')
OUTPUT_FILE_2 = os.path.join(PAGES_DIR, '29-1-وظائف عناصر المستوى التركيبي.html')

# Templates (lazy loading)
templates = {}

def load_template(name):
    with open(os.path.join(TEMPLATE_DIR, name), 'r', encoding='utf-8') as f:
        return f.read()

def get_template(name):
    if name not in templates:
        templates[name] = load_template(name)
    return templates[name]

def verify_content(html_content):
    temp_file = 'temp_verify.html'
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    # Run verify_layout.py
    try:
        result = subprocess.run(
            ['python3', VERIFY_SCRIPT, temp_file],
            capture_output=True,
            text=True
        )
        output = result.stdout
        # Output is JSON
        try:
            data = json.loads(output)
            return data
        except json.JSONDecodeError:
            print(f"Error decoding JSON from verify_layout.py: {output}")
            return {"status": "FAIL", "details": "JSON Decode Error"}
    except Exception as e:
        print(f"Error running verify_layout.py: {e}")
        return {"status": "FAIL", "details": str(e)}
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

def create_page(blocks, lesson_number, chapter_title):
    # Base
    base = get_template('TEMPLATE_C_BASE.html')

    # Header
    header = get_template('TEMPLATE_C_HEADER.html')
    header = header.replace('[LESSON_NUMBER]', str(lesson_number))
    header = header.replace('[CHAPTER_TITLE]', chapter_title)
    header = header.replace('[SECTION_HEADER]', 'المستوى الفني')
    header = header.replace('[CATEGORY_HEADER]', 'فوائد')
    header = header.replace('[AUTHOR_NAME]', 'أ. الياس خفيف')
    header = header.replace('[AUTHOR_PHONE]', '994066850 963+')

    content_html = header + "\n" + "\n".join(blocks)

    # Inject into Base
    full_html = base.replace('<!-- INJECT_CONTENT_HERE -->', content_html)
    return full_html

def clean_replace_content(template_html, content):
    # Replaces the <p class="mt-1mm text-accent">...[CONTENT_TEXT]...</p> with new content
    # Handles whitespace flexibility
    pattern = r'<p class="mt-1mm text-accent">\s*\[CONTENT_TEXT\]\s*</p>'
    return re.sub(pattern, content, template_html, flags=re.DOTALL)

# Block Definitions
def get_blocks():
    blocks = []

    # Block 2: Definition
    b2 = get_template('TEMPLATE_C_BLOCK.html')
    b2 = b2.replace('[BLOCK_TITLE]', 'وَظِيفَةُ الْجُمْلَةِ الْاسْمِيَّةِ')
    b2 = clean_replace_content(b2, '<p class="text-accent text-justify">تَدُلُّ الْجُمْلَةُ الْاسْمِيَّةُ عَلَى <span class="highlight-red">الثَّبَاتِ وَالِاسْتِقْرَارِ وَالدَّيْمُومَةِ</span>؛ وَذَلِكَ مِنْ جِهَةِ ثَبَاتِ الْحَالِ، وَثَبَاتِ الْمَوْقِفِ، وَدَيْمُومَةِ الصِّفَةِ، وَاسْتِقْرَارِ الْعَاطِفَةِ. وَيَنْبَغِي لِلطَّالِبِ أَنْ يَعِيَ أَنَّ الْجُمْلَةَ الْاسْمِيَّةَ كُلُّ جُمْلَةٍ تَبْدَأُ بِمُبْتَدَأٍ (سَوَاءٌ أَكَانَ اسْمًا أَمْ ضَمِيرًا)، أَوْ تَبْدَأُ بِحَرْفٍ مُشَبَّهٍ بِالْفِعْلِ. وَتَبْقَى هَذِهِ الْجُمْلَةُ اسْمِيَّةً سَوَاءٌ أَكَانَ خَبَرُهَا مُفْرَدًا (اسْمًا)، أَوْ جُمْلَةً فِعْلِيَّةً أَوْ جُمْلَةً اسْمِيَّةً.</p>')
    # Remove benefit placeholders
    b2 = b2.replace('<div class="benefit-box">\n                <strong> [BENEFIT_TITLE]:</strong> [BENEFIT_TEXT]\n            </div>', '')
    b2 = b2.replace('id="[BLOCK_ID]"', '')
    blocks.append(b2)

    # Block 3: Tip
    b3 = get_template('TEMPLATE_C_BENEFIT_TIP.html')
    b3 = b3.replace('[TIP_TITLE]', 'كَيْفِيَّةُ الْإِجَابَةِ')
    b3 = b3.replace('[TIP_TEXT]', 'بِمَقْدُورِ الطَّالِبِ اعْتِمَادُ الْقَالِبِ النَّظَرِيِّ الْآتِي فِي إِجَابَتِهِ، حِينَمَا يُسْأَلُ عَنْ دَوْرِ اسْتِعْمَالِ الْجُمْلَةِ الْاسْمِيَّةِ فِي خِدْمَةِ الْمَعْنَى. يَنْبَغِي لِلطَّالِبِ أَنْ يُشِيرَ فِي إِجَابَتِهِ إِلَى الْمَعَانِي الَّتِي أَرَادَ الشَّاعِرُ أَنْ يُؤَكِّدَ ثَبَاتَهَا وَاسْتِقْرَارَهَا وَدَيْمُومَتَهَا مِنْ خِلَالِ اسْتِعْمَالِ الْجُمْلَةِ الْاسْمِيَّةِ، أَيْ؛ يَجِبُ رَبْطُ الثَّبَاتِ وَالِاسْتِقْرَارِ وَالدَّيْمُومَةِ بِالْمَعْنَى.')
    blocks.append(b3)

    # Block 4: Theory
    b4 = get_template('TEMPLATE_C_BLOCK.html')
    b4 = b4.replace('[BLOCK_TITLE]', 'الْقَالِبُ النَّظَرِيُّ لِلْإِجَابَةِ')
    b4 = clean_replace_content(b4, '<p class="text-justify mb-2mm">حَاوَلَ الشَّاعِرُ مِنْ خِلَالِ اسْتِعْمَالِ الْجُمْلَةِ الْاسْمِيَّةِ أَنْ يَعْرِضَ الْمَعَانِيَ بِصُورَةِ <span class="highlight-red">الثَّبَاتِ وَالِاسْتِقْرَارِ وَالدَّيْمُومَةِ</span>. فَهَذَا الِاسْتِعْمَالُ مَكَّنَهُ مِنَ الْإِشَارَةِ إِلَى ثَبَاتِ .... [ نَذْكُرُ هُنَا الْمَعْنَى أَوِ الْمَعَانِي الَّتِي دَلَّتْ عَلَيْهَا الْجُمْلَةُ الْاسْمِيَّةُ] .... .</p><p class="text-justify">وَبِمَقْدُورِ الطَّالِبِ أَنْ يُشِيرَ إِلَى ثَبَاتِ الشُّعُورِ الْعَاطِفِيِّ، فَيَقُولُ: .....، كَمَا أَسْهَمَتِ الْجُمْلَةُ الْاسْمِيَّةُ، بِالتَّأْكِيدِ عَلَى ثَبَاتِ الْعَاطِفَةِ، فَ..... [نَذْكُرُ هُنَا الشُّعُورَ الْعَاطِفِيَّ] .... ثَابِتٌ دَائِمٌ لَا يَتَبَدَّلُ.</p>')
    b4 = b4.replace('<div class="benefit-box">\n                <strong> [BENEFIT_TITLE]:</strong> [BENEFIT_TEXT]\n            </div>', '')
    b4 = b4.replace('id="[BLOCK_ID]"', '')
    blocks.append(b4)

    # Block 5: Split 1
    # Add Header Block
    b5_header = get_template('TEMPLATE_C_BLOCK.html')
    b5_header = b5_header.replace('[BLOCK_TITLE]', 'الْمِثَالُ التَّطْبِيقِيُّ الْأَوَّلُ')
    # Remove content
    b5_header = b5_header.replace('<p class="mt-1mm text-accent">\n                [CONTENT_TEXT]\n            </p>', '')
    b5_header = b5_header.replace('<div class="benefit-box">\n                <strong> [BENEFIT_TITLE]:</strong> [BENEFIT_TEXT]\n            </div>', '')
    b5_header = b5_header.replace('id="[BLOCK_ID]"', '')
    # Remove empty body to avoid whitespace?
    # Actually, keep it for consistent spacing structure, or remove it.
    # If I remove it, I might break structure if CSS expects it.
    # But an empty div with padding is fine.
    blocks.append(b5_header)

    b5 = get_template('TEMPLATE_C_SPLIT.html')
    # Left (Poem) -> Visually Right
    poem_1_content = """
    <div>
        <h4 class="m-0 text-dark">جَمِيل صِدْقِي الزَّهَاوِي</h4>
    </div>
    <div class="poem-verses mt-2mm">
        <div class="poem-line"><span class="hemistich">لَهُمْ أَثَرٌ لِلْجَوْرِ فِي كُلِّ بَلْدَةٍ</span><span class="hemistich">يُمَثِّلُ مِنْ أَطْمَاعِهِمْ مَا يُمَثِّلُ</span></div>
    </div>
    """
    b5 = b5.replace('[LEFT_TITLE]', 'النَّصُّ')
    b5 = b5.replace('[LEFT_CONTENT]', poem_1_content)

    # Right (Analysis) -> Visually Left
    analysis_1_content = '<p class="text-justify mb-2mm"><strong>تَحْدِيدُ الْجُمْلَةِ الْاسْمِيَّةِ:</strong> <span class="highlight-blue">(لَهُمْ أَثَرٌ لِلْجَوْرِ)</span>.</p><p class="text-justify"><strong>أَثَرُهَا فِي خِدْمَةِ الْمَعْنَى:</strong> حَاوَلَ الشَّاعِرُ مِنْ خِلَالِ اسْتِعْمَالِ الْجُمْلَةِ الْاسْمِيَّةِ أَنْ يَعْرِضَ الْمَعْنَى بِصُورَةِ الثَّبَاتِ وَالِاسْتِقْرَارِ وَالدَّيْمُومَةِ. فَهَذَا الِاسْتِعْمَالُ مَكَّنَهُ مِنَ الْإِشَارَةِ إِلَى <span class="highlight-red">ثَبَاتِ ظُلْمِ الْعُثْمَانِيِّينَ وَاسْتِقْرَارِهِ</span>، فَالظُّلْمُ صِفَةٌ دَائِمَةٌ مُلَازِمَةٌ لَهُمْ لَا تَمَّحِي عَنْهُمْ عَبْرَ الزَّمَنِ.</p>'
    b5 = b5.replace('[RIGHT_TITLE]', 'التَّحْلِيلُ وَالْإِجَابَةُ')
    b5 = b5.replace('[RIGHT_CONTENT]', analysis_1_content)
    blocks.append(b5)

    # Block 6: Split 2
    b6_header = get_template('TEMPLATE_C_BLOCK.html')
    b6_header = b6_header.replace('[BLOCK_TITLE]', 'الْمِثَالُ التَّطْبِيقِيُّ الثَّانِي')
    b6_header = b6_header.replace('<p class="mt-1mm text-accent">\n                [CONTENT_TEXT]\n            </p>', '')
    b6_header = b6_header.replace('<div class="benefit-box">\n                <strong> [BENEFIT_TITLE]:</strong> [BENEFIT_TEXT]\n            </div>', '')
    b6_header = b6_header.replace('id="[BLOCK_ID]"', '')
    blocks.append(b6_header)

    b6 = get_template('TEMPLATE_C_SPLIT.html')
    poem_2_content = """
    <div>
        <h4 class="m-0 text-dark">جُورْج صَيْدَح</h4>
    </div>
    <div class="poem-verses mt-2mm">
        <div class="poem-line"><span class="hemistich">فِيهِ رَبْعِي، فِيهِ جَنَّاتٌ جَرَتْ</span><span class="hemistich">تَحْتَهَا الْأَنْهَارُ وَالرِّزْقُ جَمَدْ</span></div><div class="poem-line"><span class="hemistich">فِيهِ مُرُّ الْعَيْشِ يَحْلُو وَأَرَى</span><span class="hemistich">فِي سِوَاهُ زُبْدَةَ الْعَيْشِ زَبَدْ</span></div><div class="poem-line"><span class="hemistich">وَطَنِي مَا زِلْتُ أَدْعُوكَ أَبِي</span><span class="hemistich">وَجِرَاحُ الْيُتْمِ فِي قَلْبِ الْوَلَدْ</span></div>
    </div>
    """
    b6 = b6.replace('[LEFT_TITLE]', 'النَّصُّ')
    b6 = b6.replace('[LEFT_CONTENT]', poem_2_content)

    analysis_2_content = '<p class="text-justify mb-2mm"><strong>تَحْدِيدُ الْجُمَلِ الْاسْمِيَّةِ:</strong> (فِيهِ رَبْعِي)، (فِيهِ جَنَّاتٌ)، (الرِّزْقُ جَمَدْ)، (فِيهِ مُرُّ الْعَيْشِ يَحْلُو)، (جِرَاحُ الْيُتْمِ فِي قَلْبِ الْوَلَدِ).</p><p class="text-justify"><strong>أَثَرُهَا فِي خِدْمَةِ الْمَعْنَى:</strong> حَاوَلَ الشَّاعِرُ مِنْ خِلَالِ اسْتِعْمَالِ الْجُمْلَةِ الْاسْمِيَّةِ أَنْ يَعْرِضَ الْمَعْنَى بِصُورَةِ الثَّبَاتِ وَالِاسْتِقْرَارِ وَالدَّيْمُومَةِ. فَهَذَا الِاسْتِعْمَالُ مَكَّنَهُ مِنَ الْإِشَارَةِ إِلَى <span class="highlight-red">ثَبَاتِ الْخَيْرِ وَاسْتِقْرَارِ الْجَمَالِ فِي وَطَنِهِ</span> الَّذِي يَغْدُو فِيهِ الْمُرُّ عَذْبًا سَائِغًا، وَيَسْتَحِيلُ فِيهِ كَدَرُ الْعَيْشِ صَفَاءً عَلَى الدَّوَامِ، كَذَلِكَ أَفَادَهُ هَذَا الِاسْتِعْمَالُ فِي التَّعْبِيرِ عَنْ <span class="highlight-blue">ثَبَاتِ مُعَانَاتِهِ وَدَيْمُومَةِ شَقَائِهِ</span> بِسَبَبِ الْبُعْدِ عَنْ وَطَنِهِ. كَمَا أَسْهَمَتِ الْجُمْلَةُ الْاسْمِيَّةُ، بِالتَّأْكِيدِ عَلَى ثَبَاتِ الْعَاطِفَةِ (مَشَاعِرَ الْإِعْجَابِ وَالْمَحَبَّةِ).</p>'
    b6 = b6.replace('[RIGHT_TITLE]', 'التَّحْلِيلُ وَالْإِجَابَةُ')
    b6 = b6.replace('[RIGHT_CONTENT]', analysis_2_content)
    blocks.append(b6)

    # Block 7: Verbal Sentence
    b7 = get_template('TEMPLATE_C_BLOCK.html')
    b7 = b7.replace('[BLOCK_TITLE]', 'وَظِيفَةُ الْجُمْلَةِ الْفِعْلِيَّةِ')
    b7 = clean_replace_content(b7, '<p class="text-accent text-justify">تَدُلُّ الْجُمْلَةُ الْفِعْلِيَّةُ عَلَى <span class="highlight-red">التَّغَيُّرِ وَالْحَرَكَةِ</span> فَتَبْعَثُ فِي النَّصِّ الْحَيَوِيَّةَ؛ ذَلِكَ أَنَّ أَزْمِنَةَ الْأَفْعَالِ الْمُخْتَلِفَةَ تَظْهَرُ فِي النَّصِّ سِيَاقَاتٍ زَمَنِيَّةً وَفَضَاءَاتٍ حَرَكِيَّةً مُخْتَلِفَةً، وَهَذَا يُؤَدِّي إِلَى تَبَدِّي الْحَرَكَةِ وَالتَّغَيُّرِ وَالْحَيَوِيَّةِ فِي النَّصِّ.</p>')
    b7 = b7.replace('<div class="benefit-box">\n                <strong> [BENEFIT_TITLE]:</strong> [BENEFIT_TEXT]\n            </div>', '')
    b7 = b7.replace('id="[BLOCK_ID]"', '')
    blocks.append(b7)

    # Block 8: Table
    b8 = get_template('TEMPLATE_C_TABLE.html')
    b8 = b8.replace('[TABLE_TITLE]', 'مُقَارَنَةٌ بَيْنَ وَظَائِفِ الْجُمَلِ')
    b8 = b8.replace('[TABLE_HEADERS]', '<th>نَوْعُ الْجُمْلَةِ</th><th>الْوَظِيفَةُ وَالدَّلَالَةُ</th><th>الْأَثَرُ فِي الْمَعْنَى</th>')

    row_t = get_template('TEMPLATE_C_TABLE_ROW.html')
    r1 = row_t.replace('[CELL_1]', '<strong>الْجُمْلَةُ الْاسْمِيَّةُ</strong>').replace('[CELL_2]', 'الثَّبَاتُ، الِاسْتِقْرَارُ، الدَّيْمُومَةُ').replace('[CELL_3]', 'تَأْكِيدُ صِفَةٍ مُلَازِمَةٍ، أَوْ حَالَةٍ شُعُورِيَّةٍ دَائِمَةٍ لَا تَتَبَدَّلُ.')
    r2 = row_t.replace('[CELL_1]', '<strong>الْجُمْلَةُ الْفِعْلِيَّةُ</strong>').replace('[CELL_2]', 'التَّغَيُّرُ، الْحَرَكَةُ، الْحَيَوِيَّةُ').replace('[CELL_3]', 'عَرْضُ الْأَحْدَاثِ فِي سِيَاقٍ حَرَكِيٍّ مُتَغَيِّرٍ وَمُتَجَدِّدٍ.')

    b8 = b8.replace('[TABLE_ROWS]', r1 + "\n" + r2)
    blocks.append(b8)

    # Block 9: Exam
    b9 = get_template('TEMPLATE_C_EXAM.html')
    b9 = b9.replace('[BLOCK_ID]', '') # id_manager will fix
    b9 = b9.replace('[TOPIC]', 'الْمُسْتَوَى التَّرْكِيبِيِّ')
    b9 = b9.replace('[Q1_ID]', '')
    b9 = b9.replace('[Q2_ID]', '')

    q1_text = 'اسْتَعْمَلَ الشَّاعِرُ فِي الْبَيْتِ الْآتِي جُمْلَةً اسْمِيَّةً، حَدِّدْهَا، ثُمَّ بَيِّنْ أَثَرَهَا فِي خِدْمَةِ الْمَعْنَى:<br>قَالَ الشَّاعِرُ: وَالْيَأْسُ يَقْطَعُ أَحْيَانًا بِصَاحِبِهِ ** لَا تَيْأَسَنَّ فَإِنَّ الصَّانِعَ اللهُ'
    q2_text = 'مَا الْفَرْقُ بَيْنَ وَظِيفَةِ الْجُمْلَةِ الْاسْمِيَّةِ وَوَظِيفَةِ الْجُمْلَةِ الْفِعْلِيَّةِ مِنْ حَيْثُ الدَّلَالَةُ عَلَى الزَّمَنِ وَالْحَرَكَةِ؟'

    # Regex replacement for questions is safer if I manually do it.
    # The template has [QUESTION_TEXT] twice.
    # I can split by [QUESTION_TEXT].
    parts = b9.split('[QUESTION_TEXT]')
    # parts[0] + q1 + parts[1] + q2 + parts[2]
    if len(parts) == 3:
        b9 = parts[0] + q1_text + parts[1] + q2_text + parts[2]
    else:
        print("Warning: TEMPLATE_C_EXAM structure unexpected")

    blocks.append(b9)

    return blocks

def main():
    blocks = get_blocks()

    page_1_blocks = []
    page_2_blocks = []

    current_page = 1

    # Page 1
    for block in blocks:
        if current_page == 1:
            page_1_blocks.append(block)
            # Verify
            full_html = create_page(page_1_blocks, 29, 'وظائف عناصر المستوى التركيبي')
            res = verify_content(full_html)

            if res['status'] == 'OVERFLOW':
                print("Page 1 Full. Moving to Page 2.")
                # Remove last block
                page_1_blocks.pop()
                page_2_blocks.append(block)
                current_page = 2
            else:
                pass # Continue adding
        else:
            # Page 2
            page_2_blocks.append(block)
            # We assume Page 2 won't overflow for now (based on content size)
            # If it does, we'd need Page 3 loop. But for now 2 pages max is likely.

    # Save Page 1
    p1_html = create_page(page_1_blocks, 29, 'وظائف عناصر المستوى التركيبي')
    with open(OUTPUT_FILE_1, 'w', encoding='utf-8') as f:
        f.write(p1_html)
    print(f"Saved {OUTPUT_FILE_1}")

    # Save Page 2 if exists
    if page_2_blocks:
        # Add fillers for UNDERFLOW

        # 1. Tip
        tip = get_template('TEMPLATE_C_BENEFIT_TIP.html')
        tip = tip.replace('[TIP_TITLE]', 'فَائِدَةٌ بَلَاغِيَّةٌ')
        tip = tip.replace('[TIP_TEXT]', 'عِنْدَ دِرَاسَةِ وَظِيفَةِ الْجُمْلَةِ، لَا تَكْتَفِ بِذِكْرِ "الثَّبَاتِ" أَوْ "التَّجَدُّدِ" فَقَطْ، بَلْ عَلَيْكَ رَبْطُ هَذِهِ الدَّلَالَةِ بِالْمَعْنَى الْعَامِّ لِلنَّصِّ وَبِعَاطِفَةِ الشَّاعِرِ، لِتَكُونَ الْإِجَابَةُ مُتَكَامِلَةً. وَمِنَ الْمُهِمِّ أَيْضًا مُلَاحَظَةُ السِّيَاقِ الَّذِي وَرَدَتْ فِيهِ الْجُمْلَةُ لِفَهْمِ عُمْقِ الْمَعْنَى.')
        page_2_blocks.insert(0, tip)

        # 2. Irab Block
        # Ensure TEMPLATE_C_IRAB.html and TEMPLATE_C_IRAB_BOX.html are loaded
        irab_template = get_template('TEMPLATE_C_IRAB.html') # Assuming it exists, verify name
        # Wait, I verified names earlier. TEMPLATE_C_IRAB.html exists.
        irab_template = irab_template.replace('[SENTENCE_TO_PARSE]', 'لَهُمْ أَثَرٌ')
        irab_template = irab_template.replace('irab-stack', 'flex flex-col gap-2mm')
        irab_template = irab_template.replace('id="[BLOCK_ID]"', '')

        box = get_template('TEMPLATE_C_IRAB_BOX.html')
        b1 = box.replace('[WORD]', 'لَهُمْ').replace('[PARSING_DETAILS]', 'اللَّامُ حَرْفُ جَرٍّ، وَ(هُمْ) ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ بِحَرْفِ الْجَرِّ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِخَبَرٍ مُقَدَّمٍ مَحْذُوفٍ.')
        b2 = box.replace('[WORD]', 'أَثَرٌ').replace('[PARSING_DETAILS]', 'مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ عَلَى آخِرِهِ.')

        irab_template = irab_template.replace('[IRAB_BOXES]', b1 + b2)

        # Determine insertion point. Currently [Tip, Table, Exam]. Insert Irab after Table?
        # Table is likely at index 1 now.
        # Check logic: page_2_blocks had [Table, Exam].
        # Insert Tip at 0 -> [Tip, Table, Exam].
        # Insert Irab at 2 -> [Tip, Table, Irab, Exam].
        page_2_blocks.insert(2, irab_template)

        # 3. Irab Block 2
        irab_template_2 = get_template('TEMPLATE_C_IRAB.html')
        irab_template_2 = irab_template_2.replace('[SENTENCE_TO_PARSE]', 'الرِّزْقُ جَمَدْ')
        irab_template_2 = irab_template_2.replace('irab-stack', 'flex flex-col gap-2mm')
        irab_template_2 = irab_template_2.replace('id="[BLOCK_ID]"', '')

        box = get_template('TEMPLATE_C_IRAB_BOX.html')
        b3 = box.replace('[WORD]', 'الرِّزْقُ').replace('[PARSING_DETAILS]', 'مُبْتَدَأٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ عَلَى آخِرِهِ.')
        b4 = box.replace('[WORD]', 'جَمَدْ').replace('[PARSING_DETAILS]', 'فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ الظَّاهِرِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ (هُوَ)، وَالْجُمْلَةُ الْفِعْلِيَّةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ.')

        irab_template_2 = irab_template_2.replace('[IRAB_BOXES]', b3 + b4)

        page_2_blocks.insert(3, irab_template_2)

        # 4. Extra Exercise
        extra_ex = get_template('TEMPLATE_C_BLOCK.html')
        extra_ex = extra_ex.replace('[BLOCK_TITLE]', 'تَدْرِيبٌ إِضَافِيٌّ')

        q3_html = """
        <div class="exam-question border-none pb-0">
            <p class="m-0 mb-2mm">
                <span class="exam-number">3</span>
                مَيِّزِ الْجُمْلَةَ الْاسْمِيَّةَ مِنَ الْفِعْلِيَّةِ فِي قَوْلِهِ تَعَالَى: ﴿الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ﴾، وَبَيِّنْ دَلَالَتَهَا.
            </p>
            <div class="border-light h-8mm bg-grey-lighter rounded"></div>
        </div>
        """
        extra_ex = clean_replace_content(extra_ex, q3_html)
        extra_ex = extra_ex.replace('<div class="benefit-box">\n                <strong> [BENEFIT_TITLE]:</strong> [BENEFIT_TEXT]\n            </div>', '')
        extra_ex = extra_ex.replace('id="[BLOCK_ID]"', '')

        page_2_blocks.insert(4, extra_ex)

        # 5. Summary Benefit
        summary = get_template('TEMPLATE_C_BENEFIT.html')
        summary = summary.replace('[BENEFIT_TITLE]', 'خُلَاصَةٌ')
        summary = summary.replace('[BENEFIT_TEXT]', 'الْجُمْلَةُ الْاسْمِيَّةُ تُفِيدُ الثَّبَاتَ وَالِاسْتِقْرَارَ، بَيْنَمَا تُفِيدُ الْجُمْلَةُ الْفِعْلِيَّةُ التَّجَدُّدَ وَالْحُدُوثَ وَالْحَرَكَةَ.')

        page_2_blocks.insert(5, summary)

        p2_html = create_page(page_2_blocks, 29, 'وظائف عناصر المستوى التركيبي (تابع)')
        with open(OUTPUT_FILE_2, 'w', encoding='utf-8') as f:
            f.write(p2_html)
        print(f"Saved {OUTPUT_FILE_2}")

if __name__ == '__main__':
    main()
