import os
import sys
import re
import json
import subprocess
from datetime import datetime

# Paths
WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(WORKSPACE_DIR)
TEMPLATES_DIR = os.path.join(WORKSPACE_DIR, 'Templates')
PAGES_DIR = os.path.join(REPO_ROOT, 'pages')
VERIFY_SCRIPT = os.path.join(WORKSPACE_DIR, 'verify_layout.py')

# Ensure verify script exists
if not os.path.exists(VERIFY_SCRIPT):
    print(f"Error: {VERIFY_SCRIPT} not found.")
    sys.exit(1)

# Helper to load template
def load_template(name):
    path = os.path.join(TEMPLATES_DIR, name)
    if not os.path.exists(path):
        print(f"Error: Template {name} not found.")
        sys.exit(1)
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

# Helper to render template
def render_template(template_content, replacements):
    content = template_content
    for key, value in replacements.items():
        content = content.replace(key, str(value))
    return content

# Load templates
T_HEADER = load_template('TEMPLATE_C_HEADER.html')
T_BLOCK = load_template('TEMPLATE_C_BLOCK.html')
T_TABLE = load_template('TEMPLATE_C_TABLE.html')
T_SPLIT = load_template('TEMPLATE_C_SPLIT.html')
T_EXAM = load_template('TEMPLATE_C_EXAM.html')
T_PAGE_WRAPPER = load_template('TEMPLATE_C_PAGE_WRAPPER.html')
T_BASE = load_template('TEMPLATE_C_BASE.html')

# Content Definitions
BLOCKS_DATA = [
    # BLOCK 1: Lesson Header
    {
        'type': 'HEADER',
        'data': {
            '[LESSON_NUMBER]': '13',
            '[CHAPTER_TITLE]': 'الإبدال',
            '[CATEGORY_HEADER]': 'الصرف',
            '[SECTION_HEADER]': 'المستوى اللغوي',
            '[AUTHOR_NAME]': 'أ. الياس خفيف',
            '[AUTHOR_PHONE]': '994066850 963+'
        }
    },
    # BLOCK 2: Definition
    {
        'type': 'BLOCK',
        'data': {
            '[BLOCK_TITLE]': 'تَعْرِيفُ الإِبْدَالِ',
            '[CONTENT_TEXT]': '<p class="text-accent text-center font-bold text-primary p-2mm">هُوَ جَعْلُ حَرْفٍ مَكَانَ حَرْفٍ، سَوَاءٌ أَكَانَ الحَرْفُ صَحِيحًا أَمْ مُعْتَلًّا.</p>',
        }
    },
    # BLOCK 3: Hamza Substitution Rules
    {
        'type': 'SPLIT',
        'data': {
            '[LEFT_TITLE]': 'إِذَا تَطَرَّفَتَا بَعْدَ أَلِفٍ زَائِدَةٍ',
            '[LEFT_CONTENT]': '''
<div class="p-2mm">
    <ul class="structured-list">
        <li class="mb-2mm">
            <span class="marker">•</span>
            <span class="font-bold highlight-red">كِسَاء</span>: أَصْلُ هَذِهِ الهَمْزَةِ <span class="highlight-blue">وَاو</span> (يَكْسُو، كِسَاو)، وتَحوَّلَتْ إِلى هَمْزَةٍ لأَنَّهَا جَاءَتْ فِي آخِرِ كَلِمَة (كِسَاء) بَعْدَ أَلِفٍ زَائِدَة.
        </li>
        <li class="mb-2mm">
            <span class="marker">•</span>
            <span class="font-bold highlight-red">بِنَاء</span>: أَصْلُ هَذِهِ الهَمْزَةِ <span class="highlight-blue">يَاء</span> (يَبْنِي، بِنَاي)، وتَحوَّلَتْ إِلى هَمْزَةٍ لأَنَّهَا جَاءَتْ فِي آخِرِ كَلِمَة (بِنَاء) بَعْدَ أَلِفٍ زَائِدَة.
        </li>
    </ul>
</div>
''',
            '[RIGHT_TITLE]': 'فِي اسْمِ الفَاعِلِ مِنَ الأَجْوَفِ',
            '[RIGHT_CONTENT]': '''
<div class="p-2mm">
    <p class="mb-2mm">إِذَا وَقَعَا عَيْنًا فِي اسْمِ الفَاعِلِ المَصُوغِ مِنَ الفِعْلِ الثُّلَاثِي الأَجْوَفِ:</p>
    <ul class="structured-list">
        <li class="mb-2mm">
            <span class="marker">•</span>
            <span class="font-bold highlight-red">عَائِد</span>: أَصْلُ هَذِهِ الهَمْزَةِ <span class="highlight-blue">وَاو</span> (يَعُودُ، عَاوِد).
        </li>
        <li class="mb-2mm">
            <span class="marker">•</span>
            <span class="font-bold highlight-red">صَائِد</span>: أَصْلُ هَذِهِ الهَمْزَةِ <span class="highlight-blue">يَاء</span> (يَصِيدُ، صَايِد).
        </li>
        <li class="mb-2mm text-grey-dark text-sm">
            <span class="marker">ℹ️</span>
            <span class="font-bold">أَمْثِلَةٌ أُخْرَى:</span> (قَالَ، قَائِل) - (بَاعَ، بَائِع).
        </li>
    </ul>
</div>
'''
        }
    },
    # BLOCK 4: Plural Substitution
    {
        'type': 'BLOCK',
        'data': {
            '[BLOCK_TITLE]': 'إِبْدَالُ حُرُوفِ المَدِّ هَمْزَةً فِي (فَعَائِل)',
            '[CONTENT_TEXT]': '''
<p class="mb-2mm">يُبْدَلُ حَرْفُ المَدِّ (ي، و، ا) فِي المُفْرَدِ المُؤَنَّثِ هَمْزَةً إِذَا وَقَعَ بَعْدَ أَلِفِ صِيَغِ مُنْتَهَى الجُمُوعِ (فَعَائِل):</p>
<ul class="structured-list">
    <li class="bg-grey-lighter p-2mm rounded mb-2mm">
        <span class="marker">✅</span>
        <span class="font-bold text-primary">عَجَائِز:</span> أَصْلُهَا (عَجَاوِز) مِن (عَجَزَ). تَحَوَّلَتِ الوَاوُ إِلى هَمْزَةٍ لأَنَّهَا وَقَعَتْ بَعْدَ أَلِفِ صِيغَةِ مُنْتَهَى الجُمُوعِ.
    </li>
    <li class="bg-grey-lighter p-2mm rounded mb-2mm">
        <span class="marker">✅</span>
        <span class="font-bold text-primary">قَصَائِد:</span> أَصْلُهَا (قَصَايِد) مِن (قَصَدَ). تَحَوَّلَتِ اليَاءُ إِلى هَمْزَةٍ لأَنَّهَا وَقَعَتْ بَعْدَ أَلِفِ صِيغَةِ مُنْتَهَى الجُمُوعِ.
    </li>
    <li class="p-1mm text-sm text-grey-dark">
        <span class="marker">ℹ️</span>
        أَمْثِلَةٌ أُخْرَى: (صَحِيفَة، صَحَائِف)، (وَدِيعَة، وَدَائِع)، (قِلَادَة، قَلَائِد).
    </li>
</ul>
'''
        }
    },
    # BLOCK 5a: Ifti'āl Rules Matrix (Part 1)
    {
        'type': 'TABLE',
        'data': {
            '[TABLE_TITLE]': 'قَوَاعِدُ الإِبْدَالِ فِي صِيغَةِ (افْتَعَلَ)',
            'headers': ['القَاعِدَة', 'المِثَال', 'الأَصْل', 'التَّعْلِيل'],
            'rows': [
                ["تُبْدَلُ تَاءُ (افْتَعَلَ) طَاءً بَعْدَ الضَّادِ", "اضْطَرَّ", "اضْتَرَّ", "وَقَعَتِ التَّاءُ بَعْدَ حَرْفِ الضَّادِ"],
                ["تُبْدَلُ تَاءُ (افْتَعَلَ) طَاءً بَعْدَ الصَّادِ", "اصْطَحَبَ", "اصْتَحَبَ", "وَقَعَتِ التَّاءُ بَعْدَ حَرْفِ الصَّادِ"]
            ]
        }
    },
    # BLOCK 5b: Ifti'āl Rules Matrix (Part 2)
    {
        'type': 'TABLE',
        'data': {
            '[TABLE_TITLE]': 'قَوَاعِدُ الإِبْدَالِ فِي صِيغَةِ (افْتَعَلَ) ',
            'headers': ['القَاعِدَة', 'المِثَال', 'الأَصْل', 'التَّعْلِيل'],
            'rows': [
                ["تُبْدَلُ تَاءُ (افْتَعَلَ) دَالًا بَعْدَ الزَّايِ", "ازْدَهَرَ", "ازْتَهَرَ", "وَقَعَتِ التَّاءُ بَعْدَ حَرْفِ الزَّايِ"],
                ["تُبْدَلُ الوَاوُ تَاءً إِذَا وَقَعَتْ فَاءً لِـ (افْتَعَلَ)", "اتَّقَدَ", "اوتَقَدَ", "جَاءَتْ مُقَابِلَةً لِفَاءِ المِيزَانِ الصَّرْفِي"]
            ]
        }
    },
    # BLOCK 6a: Solved Applications (Part 1)
    {
        'type': 'TABLE',
        'data': {
            '[TABLE_TITLE]': 'أَمْثِلَةٌ تَطْبِيقِيَّةٌ مُجَابٌ عَنْهَا',
            'headers': ['الكَلِمَة', 'العِلَّة الصَّرْفِيَّة'],
            'rows': [
                ["قَالَ", "إِعْلَالٌ بِالقَلْبِ، قُلِبَتِ الوَاو أَلِفًا؛ لِتَحَرُّكِهَا بَعْدَ فَتْحٍ."],
                ["عُدْ", "إِعْلَالٌ بِالحَذْفِ، حُذِفَ حَرْفُ العِلَّةِ لِوُجُودِ سَاكِنٍ بَعْدَه."],
                ["دَنَا", "إِعْلَالٌ بِالقَلْبِ، قُلِبَتِ الوَاو أَلِفًا؛ لِتَحَرُّكِهَا بَعْدَ فَتْحٍ."],
                ["غُزَتْ", "إِعْلَالٌ بِالحَذْفِ، حُذِفَ حَرْفُ العِلَّةِ لِوُقُوعِهِ فِي آخِرِ الفِعْلِ المَاضِي الَّذِي اتَّصَلَتْ بِهِ تَاءُ التَّأْنِيثِ."],
                ["يَزْدَهِي (١)", "إِبْدَالٌ، أُبْدِلَتِ التَّاءُ دَالًا لِوُقُوعِهَا بَعْدَ الزَّايِ فِي صِيغَةِ (افْتَعَلَ)."],
                ["يَزْدَهِي (٢)", "إِعْلَالٌ بِالتَّسْكِينِ، سُكِّنَتِ اليَاء لِتَطَرُّفِهَا بَعْدَ كَسْرٍ."]
            ]
        }
    },
    # BLOCK 6b: Solved Applications (Part 2)
    {
        'type': 'TABLE',
        'data': {
            '[TABLE_TITLE]': 'أَمْثِلَةٌ تَطْبِيقِيَّةٌ مُجَابٌ عَنْهَا ',
            'headers': ['الكَلِمَة', 'العِلَّة الصَّرْفِيَّة'],
            'rows': [
                ["صَائِد", "إِبْدَال، أُبْدِلَتِ اليَاء هَمْزَةً؛ لأَنَّهَا وَقَعَتْ عَيْنًا فِي صِيغَةِ اسْمِ الفَاعِلِ مِنَ الأَجْوَفِ."],
                ["سَائِل", "إِبْدَال، أُبْدِلَتِ اليَاءُ هَمْزَةً؛ لأَنَّهَا وَقَعَتْ عَيْنًا فِي صِيغَةِ اسْمِ الفَاعِلِ مِنَ الأَجْوَفِ."],
                ["أَخْفِي", "إِعْلَالٌ بِالتَّسْكِينِ، سُكِّنَتِ اليَاءُ لأَنَّهَا تَطَرَّفَتْ بَعْدَ كَسْرٍ."],
                ["مُلْقَاة", "إِعْلَالٌ بِالقَلْبِ، قُلِبَتِ اليَاءُ أَلِفًا؛ لأَنَّهَا تَحَرَّكَتْ بَعْدَ فَتْحٍ."],
                ["كُنْتُ", "إِعْلَالٌ بِالحَذْفِ، حُذِفَ حَرْفُ العِلَّةِ لِوُجُودِ سَاكِنٍ بَعْدَه."],
                ["آتَاهُ", "إِعْلَالٌ بِالقَلْبِ: قُلِبَتِ اليَاءُ أَلِفًا؛ لأَنَّهَا جَاءَتْ مُتَحَرِّكَةً بَعْدَ فَتْحٍ."],
                ["يَصْطَلِكُ", "إِبْدَالٌ: أُبْدِلَتِ التَّاءُ طَاءً؛ لِمَجِيئِهَا بَعْدَ الصَّادِ فِي صِيغَةِ (افْتَعَلَ)."],
                ["يَضْطَرِبُ", "إِبْدَالٌ: أُبْدِلَتِ التَّاءُ طَاءً؛ لِمَجِيئِهَا بَعْدَ الضَّادِ فِي صِيغَةِ (افْتَعَلَ)."],
                ["مَعَاد", "إِعْلَالٌ بِالقَلْبِ، قُلِبَتِ الوَاو أَلِفًا؛ لِتَحَرُّكِهَا بَعْدَ فَتْحٍ."],
                ["أَعْطَتْ", "إِعْلَالٌ بِالحَذْفِ، حُذِفَ حَرفُ العِلَّةِ لوُقوعِهِ في آخِرِ الفِعْلِ الماضِي المُتَّصِلِ بِتَاءِ التَّأْنِيثِ."],
                ["تَقَاضِي", "إِعْلَالٌ بالتَّسكِينِ؛ سَكَنَتِ الياءُ لِتَطَرُّفِها بعدَ كَسرٍ."],
                ["أَسْتَزِيدُ", "إِعْلَالٌ بالتَّسكِينِ، سَكَنَتِ الياءُ؛ لتَحَرُّكِها بَعدَ حَرْفٍ صَحِيحٍ ساكِنٍ."]
            ]
        }
    },
    # BLOCK TIP: Extra Benefit
    {
        'type': 'BLOCK',
        'data': {
            '[BLOCK_TITLE]': 'فَائِدَةٌ صَرْفِيَّةٌ',
            '[CONTENT_TEXT]': 'انتَبِهْ: الإِبْدَالُ قَدْ يَقَعُ فِي الحُرُوفِ الصَّحِيحَةِ وَالمُعْتَلَّةِ (مِثْل: اصْطَبَرَ)، بَيْنَمَا الإِعْلَالُ يَخْتَصُّ بِحُرُوفِ العِلَّةِ فَقَطْ.'
        }
    },
    # BLOCK 7: Exam
    {
        'type': 'EXAM',
        'data': {
            '[TOPIC]': 'الإبدال',
            '[QUESTION_TEXT]': 'بَيِّنِ العِلَّةَ الصَّرْفِيَّةَ (إِبْدَال أَوْ إِعْلَال) فِي الكَلِمَاتِ الآتِيَةِ مَعَ التَّعْلِيلِ: (سَمَاء - اصْطَبَرَ - ادَّعَى).',
            '[QUESTION_TEXT_2]': 'وَضِّحِ الإِبْدَال فِي كَلِمَةِ (اتَّقَدَ) مَعَ ذِكْرِ السَّبَبِ.',
            '[QUESTION_TEXT_3]': 'بَيِّنْ نَوْعَ الإِبْدَالِ فِي كَلِمَةِ (مُتَّصِل) وَمَا أَصْلُهَا.'
        }
    }
]

def render_block_html(block):
    b_type = block['type']
    b_data = block['data']

    if b_type == 'HEADER':
        return render_template(T_HEADER, b_data)

    elif b_type == 'BLOCK':
        # Handle wrapping <p> issue
        content = b_data.get('[CONTENT_TEXT]', '')
        template = T_BLOCK

        # Remove benefit box if not used
        if '[BENEFIT_TITLE]' not in b_data:
            template = re.sub(r'<div class="benefit-box">.*?</div>', '', template, flags=re.DOTALL)

        # Check if content starts with <p or has multiple paragraphs/lists
        if content.strip().startswith('<p') or '<ul' in content:
            # Replace the wrapper <p> in template with just CONTENT
            # The template is: <p class="mt-1mm text-accent">\n[CONTENT_TEXT]\n</p>
            # We will use regex to find this block and replace it.
            template = re.sub(r'<p class="mt-1mm text-accent">\s*\[CONTENT_TEXT\]\s*</p>', '[CONTENT_TEXT]', template, flags=re.DOTALL)

        return render_template(template, b_data)

    elif b_type == 'TABLE':
        # Render Headers
        headers_html = ""
        for h in b_data['headers']:
            headers_html += f"<th>{h}</th>"

        # Render Rows
        rows_html = ""
        for row in b_data['rows']:
            # Create TR manually based on row length
            row_str = "<tr>"
            for cell in row:
                row_str += f"<td>{cell}</td>"
            row_str += "</tr>"
            rows_html += row_str

        return render_template(T_TABLE, {
            '[TABLE_TITLE]': b_data['[TABLE_TITLE]'],
            '[TABLE_HEADERS]': headers_html,
            '[TABLE_ROWS]': rows_html
        })

    elif b_type == 'SPLIT':
        # Render nested content - allow raw string or list of blocks
        # Here we just pass raw HTML from data

        return render_template(T_SPLIT, {
            '[LEFT_TITLE]': b_data['[LEFT_TITLE]'],
            '[LEFT_CONTENT]': b_data['[LEFT_CONTENT]'],
            '[RIGHT_TITLE]': b_data['[RIGHT_TITLE]'],
            '[RIGHT_CONTENT]': b_data['[RIGHT_CONTENT]']
        })

    elif b_type == 'EXAM':
        template = T_EXAM
        # Extract Header and Body wrapper from template to preserve style
        # Template structure: <section ...> <div class="block-header ...>...</div> <div class="block-body"> ... </div> </section>
        # We will reconstruct the inner body content.

        # 1. Get the start of the template up to <div class="block-body">
        body_start_idx = template.find('<div class="block-body">')
        if body_start_idx == -1:
             return "" # Error

        header_part = template[:body_start_idx + len('<div class="block-body">')]
        footer_part = "    </div>\n</section>"

        # Collect questions
        questions = []
        questions.append(b_data['[QUESTION_TEXT]'])
        if '[QUESTION_TEXT_2]' in b_data:
            questions.append(b_data['[QUESTION_TEXT_2]'])
        if '[QUESTION_TEXT_3]' in b_data:
            questions.append(b_data['[QUESTION_TEXT_3]'])

        # Generate HTML for questions
        questions_html = ""
        for i, q_text in enumerate(questions):
            num = i + 1
            qid = f"q{num}"

            # Determine class: last item gets special class
            if i == len(questions) - 1:
                div_class = "exam-question mb-0 border-none pb-0"
            else:
                div_class = "exam-question"

            q_html = f'''
        <div class="{div_class}" id="{qid}">
            <p class="m-0 mb-2mm">
                <span class="exam-number">{num}</span>
                {q_text}
            </p>
            <div class="border-light h-8mm bg-grey-lighter rounded"></div>
        </div>'''
            questions_html += q_html

        # Construct final HTML
        content = header_part + questions_html + footer_part

        # Replace remaining placeholders in Header
        content = content.replace('[BLOCK_ID]', 'b_exam')
        content = content.replace('[TOPIC]', b_data['[TOPIC]'])

        return content

    return ""

def create_page_content(blocks_html):
    # Wrap in PAGE_WRAPPER (force-new-page)
    wrapper = T_PAGE_WRAPPER.replace('<!-- INJECT_CONTENT_HERE -->', "".join(blocks_html))

    # Wrap in BASE
    final_html = T_BASE.replace('<!-- INJECT_CONTENT_HERE -->', wrapper)
    return final_html

def verify_page_layout(html_content):
    temp_file = os.path.join(PAGES_DIR, 'temp_verify_13.html')
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    try:
        result = subprocess.run(
            ['python', VERIFY_SCRIPT, temp_file],
            capture_output=True,
            text=True
        )
        # Check return code first
        if result.returncode != 0:
            # Check output for OVERFLOW
            if "OVERFLOW" in result.stdout or "OVERFLOW" in result.stderr:
                return 'OVERFLOW'
            # Or try to parse JSON if printed
            match = re.search(r'\{.*\}', result.stdout, re.DOTALL)
            if match:
                json_str = match.group(0)
                try:
                    data = json.loads(json_str)
                    return data.get('status', 'FAIL')
                except:
                    pass
            # Fallback
            print(f"Verify script failed with code {result.returncode}")
            return 'FAIL'

        output = result.stdout.strip()
        match = re.search(r'\{.*\}', output, re.DOTALL)
        if match:
            json_str = match.group(0)
            data = json.loads(json_str)
            return data.get('status', 'UNKNOWN')
        else:
            print("Could not parse verify output.")
            return 'FAIL'
    except Exception as e:
        print(f"Error running verify: {e}")
        return 'FAIL'
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

# Main Generation Loop
current_blocks_html = []
current_page_idx = 0
final_files = []

# Prepare header html for reuse
header_html = render_block_html(BLOCKS_DATA[0])

# Process blocks
for i, block in enumerate(BLOCKS_DATA):
    rendered = render_block_html(block)

    # If first block (Header), just add it
    if i == 0:
        current_blocks_html.append(rendered)
        continue

    # Try adding to current page
    test_blocks = current_blocks_html + [rendered]

    # Check layout
    page_html = create_page_content(test_blocks)
    status = verify_page_layout(page_html)

    print(f"Block {i} ({block['type']}) -> Page {current_page_idx}: {status}")

    if status == 'OVERFLOW':
        # Overflow! Save current page without the new block.

        # If current_blocks_html is empty (unlikely given header), warn
        if not current_blocks_html:
            print("Error: Single block overflows page!")
            # Save anyway
            final_html = create_page_content([rendered])
        else:
            final_html = create_page_content(current_blocks_html)

        filename = f"13.{current_page_idx}_nXX_الإبدال.html"
        filepath = os.path.join(PAGES_DIR, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(final_html)
        final_files.append(filepath)
        print(f"Saved {filename}")

        # Start new page
        current_page_idx += 1
        current_blocks_html = []

        # Add Continuation Header
        h_data = BLOCKS_DATA[0]['data'].copy()
        h_data['[CHAPTER_TITLE]'] += ' '
        cont_header = render_block_html({'type': 'HEADER', 'data': h_data})
        current_blocks_html.append(cont_header)

        # Add the block that caused overflow
        current_blocks_html.append(rendered)

    else:
        # Fits
        current_blocks_html.append(rendered)

# Save final page
if current_blocks_html:
    filename = f"13.{current_page_idx}_nXX_الإبدال.html"
    filepath = os.path.join(PAGES_DIR, filename)
    final_html = create_page_content(current_blocks_html)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_html)
    final_files.append(filepath)
    print(f"Saved {filename}")

print("Generation Complete.")
print("Generated Files:", final_files)
