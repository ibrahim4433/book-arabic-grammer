import os
import re
import json
import subprocess
import shutil

# Configuration
PLAN_FILE = "plan.txt"
TEMPLATES_DIR = "Jules-workspace/Templates/"
OUTPUT_DIR = "pages/"
OUTPUT_BASE_NAME = "25"
OUTPUT_TITLE = "nXX_علامات الترقيم"

def load_template(filename):
    with open(os.path.join(TEMPLATES_DIR, filename), 'r', encoding='utf-8') as f:
        return f.read()

def parse_plan(plan_file):
    with open(plan_file, 'r', encoding='utf-8') as f:
        content = f.read()

    blocks = []
    content = content.split('--- END STREAM ---')[0]
    parts = re.split(r'=== BLOCK \d+: (.*?) ===', content)

    for i in range(1, len(parts), 2):
        block_title = parts[i].strip()
        block_content_raw = parts[i+1].strip()

        component_match = re.search(r'\(Component: (.*?)\)', block_content_raw)
        if not component_match:
            continue
        component = component_match.group(1)

        block_body = block_content_raw.replace(component_match.group(0), '').strip()

        data = {}
        lines = block_body.split('\n')
        current_key = None
        current_value = []

        for line in lines:
            line = line.strip()
            if not line: continue

            key_match = re.match(r'^(\[.*?\]|Title|Content|Number|Question|Answer):(.*)', line)
            if key_match:
                if current_key:
                    val = '\n'.join(current_value).strip()
                    if current_key in data:
                        if isinstance(data[current_key], list):
                            data[current_key].append(val)
                        else:
                            data[current_key] = [data[current_key], val]
                    else:
                        data[current_key] = val

                current_key = key_match.group(1).strip('[]')
                current_value = [key_match.group(2).strip()]
            else:
                if current_key:
                    current_value.append(line)

        if current_key:
            val = '\n'.join(current_value).strip()
            if current_key in data:
                if isinstance(data[current_key], list):
                    data[current_key].append(val)
                else:
                    data[current_key] = [data[current_key], val]
            else:
                data[current_key] = val

        blocks.append({
            'title': block_title,
            'component': component,
            'data': data,
            'raw_body': block_body
        })

    return blocks

def generate_block_html(block):
    comp = block['component']
    data = block['data']
    html = ""

    if comp == 'TEMPLATE_C_HEADER':
        template = load_template("TEMPLATE_C_HEADER.html")
        for k, v in data.items():
            if isinstance(v, list): v = v[0]
            template = template.replace(f"[{k}]", v)
        html = template

    elif comp == 'TEMPLATE_C_BLOCK':
        template = load_template("TEMPLATE_C_BLOCK.html")
        template = template.replace("[BLOCK_TITLE]", data.get('Title', ''))
        content = data.get('Content', '')
        if content.strip().startswith('<'):
            template = re.sub(r'<p class="mt-1mm text-accent">\s*\[CONTENT_TEXT\]\s*</p>', '[CONTENT_TEXT]', template, flags=re.DOTALL)
        template = template.replace("[CONTENT_TEXT]", content)
        template = re.sub(r'<div class="benefit-box">.*?</div>', '', template, flags=re.DOTALL)
        html = template

    elif comp == 'TEMPLATE_C_BENEFIT_TIP':
        template = load_template("TEMPLATE_C_BENEFIT_TIP.html")
        template = template.replace("[TIP_TITLE]", data.get('TIP_TITLE', ''))
        template = template.replace("[TIP_TEXT]", data.get('TIP_TEXT', ''))
        html = template

    elif comp == 'TEMPLATE_C_TABLE':
        template = load_template("TEMPLATE_C_TABLE.html")
        template = template.replace("[TABLE_TITLE]", data.get('Title', ''))
        template = template.replace("[TABLE_HEADERS]", data.get('TABLE_HEADERS', ''))
        template = template.replace("[TABLE_ROWS]", data.get('TABLE_ROWS', ''))
        html = template

    elif comp == 'TEMPLATE_C_LIST':
        template = load_template("TEMPLATE_C_LIST.html")
        template = template.replace("[LIST_TITLE]", data.get('Title', ''))
        template = template.replace("[LIST_ITEMS]", data.get('LIST_ITEMS', ''))
        template = re.sub(r'<div class="benefit-box">.*?</div>', '', template, flags=re.DOTALL)
        template = template.replace('<hr class="separator-dashed">', '')
        html = template

    elif comp == 'TEMPLATE_C_EXAM':
        template = load_template("TEMPLATE_C_EXAM.html")
        template = template.replace('id="[BLOCK_ID]"', '')
        template = template.replace('id="[Q1_ID]"', '')
        template = template.replace('id="[Q2_ID]"', '')
        topic = "علامات الترقيم"
        template = template.replace("[TOPIC]", topic)
        numbers = data.get('Number', [])
        questions = data.get('Question', [])
        if isinstance(numbers, str): numbers = [numbers]
        if isinstance(questions, str): questions = [questions]
        if len(numbers) == 2:
            template = template.replace('<span class="exam-number">1</span>', f'<span class="exam-number">{numbers[0]}</span>', 1)
            template = template.replace('[QUESTION_TEXT]', questions[0], 1)
            template = template.replace('<span class="exam-number">2</span>', f'<span class="exam-number">{numbers[1]}</span>', 1)
            template = template.replace('[QUESTION_TEXT]', questions[1], 1)
        html = template

    # APPLY FIXES FOR LINTER BEFORE RETURNING
    html = html.replace('text-green', 'highlight-green')
    html = html.replace('text-xl', '') # Remove as not in CSS

    return html

def check_layout(html_content):
    page_wrapper = load_template("TEMPLATE_C_PAGE_WRAPPER.html")
    page_content = page_wrapper.replace("<!-- INJECT_CONTENT_HERE -->", html_content)
    base_template = load_template("TEMPLATE_C_BASE.html")
    full_html = base_template.replace("<!-- INJECT_CONTENT_HERE -->", page_content)

    with open("temp_verify.html", "w", encoding="utf-8") as f:
        f.write(full_html)

    result = subprocess.run(
        ["python3", "Jules-workspace/verify_layout.py", "temp_verify.html"],
        capture_output=True, text=True
    )

    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        print("Error decoding json from verify_layout:", result.stdout)
        return {"status": "FAIL"}

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    blocks = parse_plan(PLAN_FILE)
    pages = []
    current_page_blocks = []
    page_num = 0
    header_block = None

    if blocks and blocks[0]['component'] == 'TEMPLATE_C_HEADER':
        header_block = blocks[0]

    print(f"Total blocks to process: {len(blocks)}")

    for i, block in enumerate(blocks):
        block_html = generate_block_html(block)

        # Test addition
        test_blocks = current_page_blocks + [block_html]
        status = check_layout('\n'.join(test_blocks))

        if status['status'] == 'OVERFLOW':
            print(f"Page {page_num} overflowed at block {i+1} ({block['title']}). Splitting.")

            # Save current page
            pages.append('\n'.join(current_page_blocks))
            page_num += 1
            current_page_blocks = []

            # Add Continuation Header
            if header_block:
                new_header = header_block.copy()
                new_header['data'] = header_block['data'].copy()
                title = new_header['data'].get('CHAPTER_TITLE', '')
                if 'تابع' not in title:
                    new_header['data']['CHAPTER_TITLE'] = title + " (تابع)"
                header_html = generate_block_html(new_header)
                current_page_blocks.append(header_html)

            # Add current block to new page
            current_page_blocks.append(block_html)

            # Check if this single block overflows
            status_new = check_layout('\n'.join(current_page_blocks))
            if status_new['status'] == 'OVERFLOW':
                print(f"WARNING: Block {i+1} overflows even on a new page!")

        elif status['status'] == 'FAIL':
            # Stop execution or skip?
            # If verification fails, we can't trust layout.
            # But we should try to continue.
            print(f"Layout check FAILED for block {i+1}. Details: {status.get('details')}")
            current_page_blocks.append(block_html)
        else:
            current_page_blocks.append(block_html)

    # Add last page
    if current_page_blocks:
        pages.append('\n'.join(current_page_blocks))

    # Write pages to files
    for i, page_content in enumerate(pages):
        filename = f"{OUTPUT_BASE_NAME}.{i}_{OUTPUT_TITLE}.html"
        filepath = os.path.join(OUTPUT_DIR, filename)

        page_template = load_template("TEMPLATE_C_PAGE_WRAPPER.html")
        page_content_wrapped = page_template.replace("<!-- INJECT_CONTENT_HERE -->", page_content)

        base_template = load_template("TEMPLATE_C_BASE.html")
        full_html = base_template.replace("<!-- INJECT_CONTENT_HERE -->", page_content_wrapped)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(full_html)
        print(f"Generated {filepath}")

    if os.path.exists("temp_verify.html"):
        os.remove("temp_verify.html")

if __name__ == "__main__":
    main()
