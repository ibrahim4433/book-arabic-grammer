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
T_TABLE_ROW = load_template('TEMPLATE_C_TABLE_ROW.html')
T_SPLIT = load_template('TEMPLATE_C_SPLIT.html')
T_LIST = load_template('TEMPLATE_C_LIST.html')
T_LIST_ITEM = load_template('TEMPLATE_C_LIST_ITEM.html')
T_TIP = load_template('TEMPLATE_C_BENEFIT_TIP.html')
T_EXAM = load_template('TEMPLATE_C_EXAM.html')
T_PAGE_WRAPPER = load_template('TEMPLATE_C_PAGE_WRAPPER.html')
T_BASE = load_template('TEMPLATE_C_BASE.html')

# Content Definitions
BLOCKS_DATA = [
    # BLOCK 1: Lesson Header
    {
        'type': 'HEADER',
        'data': {
            '[LESSON_NUMBER]': '12',
            '[CHAPTER_TITLE]': 'الصحيح والمعتل',
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
            '[BLOCK_TITLE]': 'مفهوم الفعل الصحيح والفعل المعتل',
            '[CONTENT_TEXT]': '<p class="text-accent text-right mb-2mm"><strong>الفِعْلُ الصَّحِيحُ:</strong> هوَ ما كانَتْ حُروفُهُ الأَصْلِيَّةُ خاليةً مِنْ حُروفِ العِلَّةِ (الألف، الواو، الياء).</p><p class="text-accent text-right"><strong>الفِعْلُ المُعْتَلُّ:</strong> هوَ ما كانَ أَحَدُ حُروفِهِ الأَصْلِيَّةِ حَرْفَ عِلَّةٍ.</p>',
            # No benefit box for this block
        }
    },
    # BLOCK 3: Sound Verb Types
    {
        'type': 'TABLE',
        'data': {
            '[TABLE_TITLE]': 'أَقْسَامُ الفِعْلِ الصَّحِيحِ',
            'headers': ['النَّوْع', 'التَّعْرِيف', 'أَمْثِلَة'],
            'rows': [
                ['السَّالِم', 'ما خَلَتْ أُصولُهُ مِنَ الهَمْزَةِ وَالتَّضْعِيفِ.', '<span class="highlight-blue">كَتَبَ</span>، <span class="highlight-blue">جَلَسَ</span>، <span class="highlight-blue">فَهِمَ</span>'],
                ['المَهْمُوز', 'ما كانَ أَحَدُ أُصولِهِ هَمْزَةً.', '<span class="highlight-red">أَمَرَ</span>، <span class="highlight-red">سَأَلَ</span>، <span class="highlight-red">لَجَأَ</span>'],
                ['المُضَعَّف', 'ما كانَ أَحَدُ أُصولِهِ مُشَدَّدًا (مُضَعَّفًا).', '<span class="highlight-green">صَدَّ</span>، <span class="highlight-green">جَدَّ</span>، <span class="highlight-green">مَدَّ</span>']
            ]
        }
    },
    # BLOCK 4: Weak Verb Types
    {
        'type': 'TABLE',
        'data': {
            '[TABLE_TITLE]': 'أَقْسَامُ الفِعْلِ المُعْتَلِّ',
            'headers': ['النَّوْع', 'مَوْضِعُ العِلَّةِ', 'أَمْثِلَة'],
            'rows': [
                ['المِثَال', 'أَوَّلُهُ حَرْفُ عِلَّةٍ.', '<span class="highlight-blue">وَصَلَ</span>، <span class="highlight-blue">وَجَدَ</span>، <span class="highlight-blue">يَئِسَ</span>'],
                ['الأَجْوَف', 'أَوْسَطُهُ (عَيْنُهُ) حَرْفُ عِلَّةٍ.', '<span class="highlight-red">قَالَ</span>، <span class="highlight-red">صَامَ</span>، <span class="highlight-red">بَاعَ</span>'],
                ['النَّاقِص', 'آخِرُهُ (لَامُهُ) حَرْفُ عِلَّةٍ.', '<span class="highlight-green">مَشَى</span>، <span class="highlight-green">دَنَا</span>، <span class="highlight-green">رَمَى</span>']
            ]
        }
    },
    # BLOCK 5: Mixed Weak (Lafif)
    {
        'type': 'SPLIT',
        'data': {
            '[LEFT_TITLE]': 'اللَّفِيفُ المَفْرُوق',
            'left_content': [
                {
                    'type': 'BLOCK',
                    'data': {
                        '[BLOCK_TITLE]': 'تَعْرِيفُهُ',
                        '[CONTENT_TEXT]': 'هوَ ما كانَ فيهِ حَرْفَا عِلَّةٍ، بَيْنَهُمَا فاصِلٌ (حَرْفٌ صَحِيحٌ).'
                    }
                },
                {
                    'type': 'LIST',
                    'data': {
                        'items': ['<span class="highlight-red">وَعَى</span>', '<span class="highlight-red">وَشَى</span>', '<span class="highlight-red">وَقَى</span>'],
                        'markers': ['مِثْل:', 'مِثْل:', 'مِثْل:']
                    }
                }
            ],
            '[RIGHT_TITLE]': 'اللَّفِيفُ المَقْرُون',
            'right_content': [
                {
                    'type': 'BLOCK',
                    'data': {
                        '[BLOCK_TITLE]': 'تَعْرِيفُهُ',
                        '[CONTENT_TEXT]': 'هوَ ما كانَ فيهِ حَرْفَا عِلَّةٍ مُتَتَالِيَانِ (دونَ فاصِلٍ).'
                    }
                },
                {
                    'type': 'LIST',
                    'data': {
                        'items': ['<span class="highlight-blue">رَوَى</span>', '<span class="highlight-blue">هَوَى</span>', '<span class="highlight-blue">طَوَى</span>'],
                        'markers': ['مِثْل:', 'مِثْل:', 'مِثْل:']
                    }
                }
            ]
        }
    },
    # BLOCK 6: Golden Tip
    {
        'type': 'TIP',
        'data': {
            '[TIP_TITLE]': 'فائِدَةٌ صَرْفِيَّةٌ مُهِمَّةٌ',
            '[TIP_TEXT]': 'لِمَعْرِفَةِ نَوْعِ الفِعْلِ (صَحِيح أَمْ مُعْتَلّ)، يَجِبُ الرُّجُوعُ إِلى <span class="highlight-red">الماضِي المُجَرَّدِ</span> (الأُصولِ الثَّلاثَةِ)، وَحَذْفُ أَحْرُفِ الزِّيادَةِ. مِثال: (يَسْتَخْرِجُ) -> (خَرَجَ) -> صَحِيحٌ سالِمٌ.'
        }
    },
    # BLOCK 7: Exam
    {
        'type': 'EXAM',
        'data': {
            '[TOPIC]': 'الصحيح والمعتل',
            '[QUESTION_TEXT]': 'صَنِّفِ الأَفْعَالَ الآتِيَةَ إِلَى صَحِيحٍ وَمُعْتَلٍّ مَعَ بَيانِ النَّوْعِ: (نَامَ - شَدَّ - وَعَدَ - قَرَأَ - رَضِيَ - طَوَى).'
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
            # Regex to remove benefit box div
            template = re.sub(r'<div class="benefit-box">.*?</div>', '', template, flags=re.DOTALL)

        # Check if content starts with <p or has multiple paragraphs
        if content.strip().startswith('<p'):
            # Replace the wrapper <p> in template with just CONTENT
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
            # Assuming row has 3 cells matching T_TABLE_ROW
            row_map = {
                '[CELL_1]': row[0],
                '[CELL_2]': row[1],
                '[CELL_3]': row[2]
            }
            rows_html += render_template(T_TABLE_ROW, row_map)

        return render_template(T_TABLE, {
            '[TABLE_TITLE]': b_data['[TABLE_TITLE]'],
            '[TABLE_HEADERS]': headers_html,
            '[TABLE_ROWS]': rows_html
        })

    elif b_type == 'LIST':
        # Render Items
        items_html = ""
        items = b_data['items']
        markers = b_data.get('markers', ['-'] * len(items))

        for i, item in enumerate(items):
            items_html += render_template(T_LIST_ITEM, {
                '[MARKER]': markers[i],
                '[CONTENT]': item
            })

        template = T_LIST
        # Remove Header if no title
        if '[LIST_TITLE]' not in b_data:
             template = re.sub(r'<div class="block-header">.*?</div>', '', template, flags=re.DOTALL)

        # Remove Note if no note
        if '[NOTE_TITLE]' not in b_data:
             template = re.sub(r'<hr class="separator-dashed">', '', template)
             template = re.sub(r'<div class="benefit-box">.*?</div>', '', template, flags=re.DOTALL)

        return render_template(template, {
            '[LIST_ITEMS]': items_html
        })

    elif b_type == 'SPLIT':
        # Render nested content
        left_html = ""
        for item in b_data['left_content']:
            left_html += render_block_html(item)

        right_html = ""
        for item in b_data['right_content']:
            right_html += render_block_html(item)

        return render_template(T_SPLIT, {
            '[LEFT_TITLE]': b_data['[LEFT_TITLE]'],
            '[LEFT_CONTENT]': left_html,
            '[RIGHT_TITLE]': b_data['[RIGHT_TITLE]'],
            '[RIGHT_CONTENT]': right_html
        })

    elif b_type == 'TIP':
        return render_template(T_TIP, b_data)

    elif b_type == 'EXAM':
        template = T_EXAM
        # Remove Q2 by splitting at the comment
        if '<!-- Question 2' in template:
            parts = template.split('<!-- Question 2')
            # parts[0] contains Header + Body Start + Q1 + spacing
            # We just need to close the body and section
            template = parts[0] + "    </div>\n</section>"

        # Also clean up Q1 bottom border if it's the only one
        # We can replace Q1's class to match Q2's "mb-0 border-none pb-0"
        template = template.replace('<div class="exam-question" id="[Q1_ID]">', '<div class="exam-question mb-0 border-none pb-0" id="[Q1_ID]">')

        return render_template(template, {
            '[BLOCK_ID]': 'b_exam', # Will be replaced by id_manager
            '[TOPIC]': b_data['[TOPIC]'],
            '[Q1_ID]': 'q1',
            '[QUESTION_TEXT]': b_data['[QUESTION_TEXT]']
        })

    return ""

def create_page_content(blocks_html):
    # Wrap in PAGE_WRAPPER (force-new-page)
    # The content of PAGE_WRAPPER is just a div.
    wrapper = T_PAGE_WRAPPER.replace('<!-- INJECT_CONTENT_HERE -->', "".join(blocks_html))

    # Wrap in BASE
    final_html = T_BASE.replace('<!-- INJECT_CONTENT_HERE -->', wrapper)
    return final_html

def verify_page_layout(html_content):
    temp_file = os.path.join(PAGES_DIR, 'temp_verify.html')
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    try:
        result = subprocess.run(
            ['python', VERIFY_SCRIPT, temp_file],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print("Verify script failed/overflowed (exit code). Output:")
            print(result.stdout)
            print(result.stderr)
            # Depending on script, exit code might be 0 even if overflow.
            # verify_layout.py exits 0 and prints JSON.

        output = result.stdout.strip()
        # Find JSON part
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

    # Try adding to current page
    test_blocks = current_blocks_html + [rendered]

    # If this is a new page (empty blocks), add header first (unless it is the header itself)
    if not current_blocks_html and block['type'] != 'HEADER':
        # Add header with continuation title if page > 0
        if current_page_idx > 0:
            h_data = BLOCKS_DATA[0]['data'].copy()
            h_data['[CHAPTER_TITLE]'] += ' (تابع)'
            cont_header = render_block_html({'type': 'HEADER', 'data': h_data})
            test_blocks = [cont_header, rendered]
        else:
            # Should not happen if first block is header
            test_blocks = [header_html, rendered]

    page_html = create_page_content(test_blocks)
    status = verify_page_layout(page_html)

    print(f"Block {i} ({block['type']}) -> Page {current_page_idx}: {status}")

    if status == 'OVERFLOW':
        # Must save current page and start new one
        # Save current page
        # Re-construct page without the overflowing block
        if not current_blocks_html:
            print("Error: Single block overflows page!")
            # Save anyway?
            final_html = create_page_content([rendered]) # or split internally?
            # For now, just save it and warn
        else:
            final_html = create_page_content(current_blocks_html)

        filename = f"12.{current_page_idx}_nXX_الصحيح والمعتل.html"
        filepath = os.path.join(PAGES_DIR, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(final_html)
        final_files.append(filepath)
        print(f"Saved {filename}")

        # Start new page
        current_page_idx += 1
        current_blocks_html = []

        # Add header for new page
        h_data = BLOCKS_DATA[0]['data'].copy()
        h_data['[CHAPTER_TITLE]'] += ' (تابع)'
        cont_header = render_block_html({'type': 'HEADER', 'data': h_data})
        current_blocks_html.append(cont_header)

        # Add the block that caused overflow
        current_blocks_html.append(rendered)

    else:
        # Fits
        if not current_blocks_html and block['type'] != 'HEADER':
             # Logic for first block on new page if it wasn't header (already handled in test_blocks logic but need to apply to current_blocks_html)
             if current_page_idx > 0:
                h_data = BLOCKS_DATA[0]['data'].copy()
                h_data['[CHAPTER_TITLE]'] += ' (تابع)'
                cont_header = render_block_html({'type': 'HEADER', 'data': h_data})
                current_blocks_html.append(cont_header)

        # If it's the header block itself (i=0), we just append it
        current_blocks_html.append(rendered)

# Save final page
if current_blocks_html:
    filename = f"12.{current_page_idx}_nXX_الصحيح والمعتل.html"
    filepath = os.path.join(PAGES_DIR, filename)
    final_html = create_page_content(current_blocks_html)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_html)
    final_files.append(filepath)
    print(f"Saved {filename}")

print("Generation Complete.")
print("Generated Files:", final_files)
