import os
import sys
import re
import json
import shutil
import uuid
import random
import string

# Add current directory to path to allow importing verify_layout and id_manager
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from verify_layout import verify_layout
except ImportError:
    # If not found, try importing from current dir assuming script is run from Jules-workspace
    try:
        from verify_layout import verify_layout
    except ImportError:
        print("Could not import verify_layout. Make sure you are in the correct directory.")
        sys.exit(1)

try:
    from id_manager import IDManager
except ImportError:
    try:
        from id_manager import IDManager
    except ImportError:
        print("Could not import id_manager.")
        sys.exit(1)

# Initialize ID Manager
id_manager = IDManager(root_dir="pages")
# We will use a local set for IDs generated during this session to ensure they are unique
# even if not yet saved to file, but IDManager.generate_id reads files.
# Since we are creating new files, we can just use generate_id for each new block.
# However, generate_id reads files to check for duplicates.
# If we generate multiple IDs before saving, we might get duplicates if we don't update existing_ids.
# IDManager.generate_id updates self.existing_ids in memory. So it should be fine.
id_manager.scan_existing_ids()

TEMPLATES_DIR = os.path.join("Jules-workspace", "Templates")
OUTPUT_DIR = "pages"

def read_template(template_name):
    filepath = os.path.join(TEMPLATES_DIR, template_name)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix TEMPLATE_C_BLOCK: Replace <p> with <div> to allow complex content (nested p, div, section)
    if template_name == "TEMPLATE_C_BLOCK.html":
        content = content.replace('<p class="mt-1mm text-accent">', '<div class="mt-1mm text-accent">')
        content = content.replace('</p>', '</div>')

    return content

def generate_id():
    return id_manager.generate_id()

def render_template(template_content, data):
    # Replace placeholders
    for key, value in data.items():
        template_content = template_content.replace(f"[{key}]", str(value))

    # Remove unused benefit/note sections if not provided
    if "[BENEFIT_TITLE]" in template_content and "[BENEFIT_TITLE]" not in data:
         # Remove the benefit box div.
         # Assuming structure: <div class="benefit-box"> ... </div>
         # Regex to remove the div containing BENEFIT_TITLE
         pattern = r'<div class="benefit-box">\s*<strong>.*?\[BENEFIT_TITLE\].*?</div>'
         template_content = re.sub(pattern, '', template_content, flags=re.DOTALL)

    if "[NOTE_TITLE]" in template_content and "[NOTE_TITLE]" not in data:
         # Remove separator and benefit box
         pattern = r'<hr class="separator-dashed">\s*<div class="benefit-box">\s*<strong>.*?\[NOTE_TITLE\].*?</div>'
         template_content = re.sub(pattern, '', template_content, flags=re.DOTALL)

    return template_content

# Content Definitions
header_data = {
    "LESSON_NUMBER": "30",
    "CHAPTER_TITLE": "العاطفة",
    "CATEGORY_HEADER": "فوائد",
    "SECTION_HEADER": "المستوى الفني",
    "AUTHOR_NAME": "أ. الياس خفيف",
    "AUTHOR_PHONE": "994066850 963+"
}

# Block 2: Concept
block2_content = """<p class="text-accent text-justify mb-2mm">
    العاطِفَةُ هِيَ الشُّعُورُ الَّذِي يُخالِجُ الأَدِيبَ تِجاهَ مَوْقِفٍ أَوْ تَجْرِبَةٍ، كَالحُزْنِ والأَسَى والأَلَمِ والكَآبَةِ، أَوِ الفَرَحِ والإِعْجابِ والافْتِخارِ.
</p>
<p class="text-justify">
    ويَتِمُّ التَّعْبِيرُ عَنْ هَذا الشُّعُورِ بِأَدَواتٍ فَنِّيَّةٍ مُتَنَوِّعَةٍ، أَبْرَزُها: <span class="highlight-red">الأَلْفاظُ</span>، و<span class="highlight-blue">التَّراكِيبُ</span>، و<span class="highlight-green">الصُّورُ البَيانِيَّةُ</span>.
</p>"""

block2_data = {
    "BLOCK_TITLE": "مَفْهُومُ العاطِفَةِ وأَدَواتُها",
    "CONTENT_TEXT": block2_content
}

# Block 3: Summary Matrix
# Table Rows
row_template = read_template("TEMPLATE_C_TABLE_ROW.html")
rows_html = ""
rows_data = [
    ("الحُزْنُ والأَسَى", "التَّراكِيبُ", "إِنْ كُنْتَ مُكْتَئِبًا، إِنْ كُنْتَ مُكْتَئِبًا لِعِزٍّ مَضَى"),
    ("الأَلَمُ والكَآبَةُ", "الصُّورُ البَيانِيَّةُ", "يُرْجِعُهُ تَنَدُّمُ، عِزٍّ قَدْ مَضَى"),
    ("الإِعْجابُ", "الصُّورُ البَيانِيَّةُ", "صُوَرٌ تَتَكَلَّمُ، تُطِلُّ مِنَ الثَّرَى صُوَرٌ")
]

for c1, c2, c3 in rows_data:
    row = row_template.replace("[CELL_1]", f'<span class="font-bold text-center block">{c1}</span>')
    row = row.replace("[CELL_2]", f'<span class="text-center block">{c2}</span>')
    row = row.replace("[CELL_3]", c3)
    rows_html += row

block3_data = {
    "TABLE_TITLE": "جَدْوَلُ تَحْلِيلِ العاطِفَةِ (نَماذِجُ)",
    "TABLE_HEADERS": "<th>الشُّعُورُ العاطِفِيُّ</th><th>الأَداةُ الفَنِّيَّةُ</th><th>المِثالُ التَّطْبِيقِيُّ</th>",
    "TABLE_ROWS": rows_html
}

# Block 4: Applied Model 1 (Admiration)
# Poem
poem_template = read_template("TEMPLATE_C_POEM.html")
# Removing bio card and header as they are not provided/needed inside a block content
# Or I can just construct the verses HTML and inject it into the block content directly
# since TEMPLATE_C_POEM is a full section.
# The plan says "(Component: TEMPLATE_C_POEM)" inside "(Component: TEMPLATE_C_BLOCK)".
# Nesting sections is valid but style-wise `poem-container` inside `content-block` might be double boxed.
# Let's try to use the classes directly for the poem part to avoid double headers/boxes if possible.
# But I must use templates.
# If I use TEMPLATE_C_POEM, I should strip the outer section if I want it seamless, or keep it.
# The plan says:
# Content:
# <div class="mb-4mm">
#    (Component: TEMPLATE_C_POEM)
#    ...
# </div>
# So I will render TEMPLATE_C_POEM and put it there.
# I need to remove [SECTION_TITLE], [POET_NAME] etc if empty.

def render_poem(right, left):
    content = read_template("TEMPLATE_C_POEM.html")
    # Clean up unused parts
    # Use exact regex or careful matching for nested divs
    # Remove header: Single div, safe
    content = re.sub(r'<div class="block-header poem-header">.*?</div>', '', content, flags=re.DOTALL)
    # Remove bio-card: Nested divs. <div class="bio-card">...<div class="bio-info">...</div>...</div>
    # The previous regex stopped at the first </div> which was bio-info's closing tag, leaving bio-card's closing tag.
    # We need to consume TWO closing divs.
    content = re.sub(r'<div class="bio-card">.*?</div>\s*</div>', '', content, flags=re.DOTALL)
    # Remove title: Simple tag
    content = re.sub(r'<h3.*?\[POEM_TITLE\].*?</h3>', '', content, flags=re.DOTALL)

    verse_html = f"""<div class="poem-line">
    <div class="hemistich">{right}</div>
    <div class="hemistich">{left}</div>
</div>"""
    content = content.replace("[POEM_VERSES]", verse_html)
    return content

block4_poem = render_poem("كُنْ غَدِيـــرًا يَسِيرُ في الأَرْضِ رَقْرا", "قًا فَيَسْقِي مِنْ جانِبَيْهِ الحُقُولا")

# List
list_item_template = read_template("TEMPLATE_C_LIST_ITEM.html")
l1 = list_item_template.replace("[MARKER]", "1").replace("[CONTENT]", '<span class="font-bold text-primary">الأَلْفاظُ:</span> (غَدِير، رَقراق، يَسْقِي).')
l2 = list_item_template.replace("[MARKER]", "2").replace("[CONTENT]", '<span class="font-bold text-primary">التَّراكيبُ:</span> (كُنْ غَدِيرًا، يَسِيرُ في الأَرْضِ، يَسْقِي مِنْ جانِبِهِ الحُقُولا).')

block4_list_html = f"""<ul class="structured-list">
{l1}
{l2}
</ul>"""

block4_content = f"""<div class="mb-4mm">
    {block4_poem}
</div>
<p class="mb-2mm">أَسْهَمَتِ الأَلْفاظُ والتَّراكِيبُ الوارِدَةُ في البَيْتِ السَّابِقِ بِإِبْرازِ شُعُورِ <span class="highlight-red">الإِعْجابِ</span>:</p>
{block4_list_html}
"""

block4_data = {
    "BLOCK_TITLE": "نَمُوذَجٌ تَطْبِيقِيٌّ: شُعُورُ الإِعْجابِ",
    "CONTENT_TEXT": block4_content
}

# Block 5: Comparative Analysis (Split)
# We need a title block first
block5_title_data = {
    "BLOCK_TITLE": "مُقارَنَةٌ شُعُورِيَّةٌ بَيْنَ التَّراكِيبِ",
    "CONTENT_TEXT": "" # Empty content, just header
}
# But TEMPLATE_C_BLOCK with empty content might look weird (empty padding).
# I will use a minimal content or just the header if I can.
# Actually, I can put the split INSIDE a block? No, split is a section.
# I will just use the header block. I'll strip the body if it's empty in post-processing or regex.

block5_left = """<h4 class="text-center font-bold text-primary mb-2mm">التَّرْكِيبُ الأَوَّلُ</h4>
<div class="bg-grey-lighter p-2mm rounded mb-2mm text-center font-bold">
    سَتَبْقَى أَرْضُنا لَنا
</div>
<p class="text-justify">
    <span class="font-bold">الشُّعُورُ العاطِفِيُّ:</span> تَفاؤُلٌ، أو: حُبٌّ، أو: ثِقَةٌ، أو: أَمَلٌ.
</p>"""

block5_right = """<h4 class="text-center font-bold text-accent mb-2mm">التَّرْكِيبُ الثَّانِي</h4>
<div class="bg-grey-lighter p-2mm rounded mb-2mm text-center font-bold">
    رَكَزْنا فَوْقَ أَرْضِنا أَعْلامَنا
</div>
<p class="text-justify">
    <span class="font-bold">الشُّعُورُ العاطِفِيُّ:</span> افْتِخارٌ، أو: فَرَحٌ، أو: اعْتِزازٌ، أو: زَهْوٌ.
</p>"""

block5_split_data = {
    "LEFT_TITLE": "التَّرْكِيبُ الأَوَّلُ", # Visually Right in RTL? No, logical left.
    "RIGHT_TITLE": "التَّرْكِيبُ الثَّانِي",
    "LEFT_CONTENT": block5_left,
    "RIGHT_CONTENT": block5_right
}
# Wait, if I provide titles, I should remove the h4s from content to avoid duplication?
# The plan has h4s. The template has titles.
# I will use the template titles and remove h4 from content.
block5_left_clean = block5_left.replace('<h4 class="text-center font-bold text-primary mb-2mm">التَّرْكِيبُ الأَوَّلُ</h4>', '')
block5_right_clean = block5_right.replace('<h4 class="text-center font-bold text-accent mb-2mm">التَّرْكِيبُ الثَّانِي</h4>', '')

block5_split_data = {
    "LEFT_TITLE": "التَّرْكِيبُ الأَوَّلُ",
    "RIGHT_TITLE": "التَّرْكِيبُ الثَّانِي",
    "LEFT_CONTENT": block5_left_clean,
    "RIGHT_CONTENT": block5_right_clean
}


# Block 6: Applied Model 3 (Sadness)
block6_poem = render_poem("حارَ فِكْرِي وَضاقَ صَدْرِي وإِنْ حا", "رَ هُمُومًا يَضِيـــقُ عَنْها الفَضاءُ")
l6_1 = list_item_template.replace("[MARKER]", "1").replace("[CONTENT]", '<span class="font-bold text-primary">الأَلْفاظُ:</span> (حارَ، ضاقَ، هُمُومًا، يَضِيقُ).')
l6_2 = list_item_template.replace("[MARKER]", "2").replace("[CONTENT]", '<span class="font-bold text-primary">التَّراكِيبُ:</span> (حارَ فِكْرِي، ضاقَ صَدْرِي، حارَ هُمُومًا، يَضِيقُ عَنْها الفَضاءُ).')

block6_content = f"""<div class="mb-4mm">
    {block6_poem}
</div>
<p class="mb-2mm">أَسْهَمَتِ الأَلْفاظُ والتَّراكِيبُ في البَيْتِ السَّابِقِ بِإِبْرازِ شُعُورِ <span class="highlight-red">الحُزْنِ</span> لَدَى الشَّاعِرِ:</p>
<ul class="structured-list">
{l6_1}
{l6_2}
</ul>
"""

block6_data = {
    "BLOCK_TITLE": "نَمُوذَجٌ تَطْبِيقِيٌّ: شُعُورُ الحُزْنِ",
    "CONTENT_TEXT": block6_content
}

# Block 7: Applied Model 4 (Optimism)
block7_poem = render_poem("وَتَوَقَّعْ إِذا السَّـــماءُ اكْفَهَرَّتْ", "مَطَرًا في السُّهُولِ يُحْيِي السُّهُولا")
l7_1 = list_item_template.replace("[MARKER]", "1").replace("[CONTENT]", '<span class="font-bold text-primary">التَّرْكِيبُ:</span> (تَوَقَّعْ مَطَرًا)، أو: (مَطَرًا يُحْيِي السُّهُولا).')
l7_2 = list_item_template.replace("[MARKER]", "2").replace("[CONTENT]", '<span class="font-bold text-primary">الأَلْفاظُ:</span> (مَطَرًا، يُحْيِي).')
l7_3 = list_item_template.replace("[MARKER]", "3").replace("[CONTENT]", '<span class="font-bold text-primary">الصُّورَةُ البَيانِيَّةُ:</span> (مَطَرًا يُحْيِي السُّهُولا).')

block7_content = f"""<div class="mb-4mm">
    {block7_poem}
</div>
<p class="mb-2mm text-justify">
    <span class="font-bold">الشُّعُورُ العاطِفِيُّ:</span> التَّفاؤُلُ، أو: الأَمَلُ، أو: الإِعْجابُ.
</p>
<p class="mb-2mm text-justify">
    <span class="font-bold">الأَداةُ الَّتِي أَبْرَزَتْهُ:</span>
</p>
<ul class="structured-list">
{l7_1}
{l7_2}
{l7_3}
</ul>
"""

block7_data = {
    "BLOCK_TITLE": "نَمُوذَجٌ تَطْبِيقِيٌّ: شُعُورُ التَّفاؤُلِ",
    "CONTENT_TEXT": block7_content
}

# Block 8: Exam
# Adjusting exam template for 1 question
exam_template = read_template("TEMPLATE_C_EXAM.html")
# Remove question 2 (Target specifically the second question div which has distinct classes)
# The template has: <div class="exam-question mb-0 border-none pb-0" id="[Q2_ID]">
# We use a specific regex to avoid matching Q1
exam_template = re.sub(r'<div class="exam-question mb-0 border-none pb-0".*?\[Q2_ID\].*?</div>', '', exam_template, flags=re.DOTALL)
exam_data = {
    "BLOCK_ID": generate_id(),
    "TOPIC": "العاطِفَة",
    "Q1_ID": generate_id(),
    "QUESTION_TEXT": """حَدِّدِ الشُّعُورَ العاطِفِيَّ وأَداةَ التَّعْبِيرِ عَنْهُ (أَلْفاظٌ، تَراكِيبُ) في البَيْتِ الآتي:
<div class="text-center font-bold mt-2mm text-primary">
    أَنا الَّذِي نَظَرَ الأَعْمَى إِلَى أَدَبِي     وَأَسْمَعَتْ كَلِماتِي مَنْ بِهِ صَمَمُ
</div>"""
}

# Define list of blocks to process
# Each item is (template_name, data_dict)
blocks_to_add = [
    ("TEMPLATE_C_BLOCK.html", block2_data),
    ("TEMPLATE_C_TABLE.html", block3_data),
    ("TEMPLATE_C_BLOCK.html", block4_data),
    ("TEMPLATE_C_BLOCK.html", block5_title_data), # Title for split
    ("TEMPLATE_C_SPLIT.html", block5_split_data),
    ("TEMPLATE_C_BLOCK.html", block6_data),
    ("TEMPLATE_C_BLOCK.html", block7_data),
    ("TEMPLATE_C_EXAM.html", exam_data)
]

# Filler content generators
filler_idx = 0
fillers_list = [
    ("exam", "سُؤالٌ إِضافِيٌّ: اِسْتَخْرِجْ شُعُورًا عاطِفِيًّا مِنْ نَصِّكَ المَدْرَسِيِّ وحَدِّدْ أَداتَهُ."),
    ("tip", "العاطِفَةُ الصَّادِقَةُ تَمْنَحُ النَّصَّ قُوَّةً وتَأْثِيرًا في المُتَلَقِّي."),
    ("exam", "سُؤالٌ إِضافِيٌّ: هَلْ يُمْكِنُ أَنْ تَتَعَدَّدَ العَواطِفُ في بَيْتٍ واحِدٍ؟ وَضِّحْ ذَلِكَ."),
    ("tip", "تَتَنَوَّعُ المَشاعِرُ العاطِفِيَّةُ بَيْنَ الفَرَحِ والحُزْنِ والأَلَمِ والتَّفاؤُلِ واليَأْسِ."),
    ("exam", "سُؤالٌ إِضافِيٌّ: كَيْفَ تُسْهِمُ الصُّورَةُ البَيانِيَّةُ في إِبْرازِ العاطِفَةِ؟"),
    ("tip", "صِدْقُ العاطِفَةِ هُوَ المِعْيارُ الأَساسِيُّ لِجَوْدَةِ الشِّعْرِ الوِجْدانِيِّ."),
    ("exam", "سُؤالٌ إِضافِيٌّ: ما الفَرْقُ بَيْنَ الشُّعُورِ والْعاطِفَةِ؟"),
    ("tip", "يَلْجَأُ الشَّاعِرُ إِلى الطَّبِيعَةِ لِيَبُثَّها شَكْواهُ ويُعَبِّرَ عَنْ عاطِفَتِهِ.")
]

def get_next_filler():
    global filler_idx
    kind, text = fillers_list[filler_idx % len(fillers_list)]
    filler_idx += 1

    if kind == "exam":
        qid = generate_id()
        return f"""
        <div class="exam-question mb-0 border-none pb-0" id="{qid}">
            <p class="m-0 mb-2mm">
                <span class="exam-number">+</span>
                {text}
            </p>
            <div class="border-light h-8mm bg-grey-lighter rounded"></div>
        </div>
        """
    else:
        return read_template("TEMPLATE_C_BENEFIT_TIP.html").replace("[TIP_TITLE]", "فائِدَة").replace("[TIP_TEXT]", text)

# Helper to write page and check layout
def write_and_check(content_blocks, page_num):
    # Construct full HTML
    base = read_template("TEMPLATE_C_BASE.html")
    header = read_template("TEMPLATE_C_HEADER.html")
    header = render_template(header, header_data)

    # If not page 0, maybe mark header as continuation?
    # Plan says "header of the continuation page(s) must include an indicator like ".
    if page_num > 0:
        header = header.replace(header_data["CHAPTER_TITLE"], header_data["CHAPTER_TITLE"] + " (تابِع)")

    body_content = header + "\n" + "\n".join(content_blocks)

    # Wrap in simple div if needed, but base template just injects content
    full_html = base.replace("<!-- INJECT_CONTENT_HERE -->", body_content)

    # Fix IDs
    # We already assigned IDs to Exam. But other blocks need IDs.
    # The IDManager auto_tag can be used, or we can manually inject unique IDs into blocks.
    # To be safe and compliant, let's inject IDs into .content-block if missing.
    # Simple regex injection for now.

    def inject_id(match):
        return match.group(0).rstrip('>') + f' id="{generate_id()}">'

    # Inject ID to content-block if it doesn't have one
    # This is a bit hacky on the full string, but works for checking layout.
    # Note: id_manager.py does this cleanly with soup.
    # For now, let's just save. verify_layout doesn't care about IDs for layout check.

    filename = f"pages/30.{page_num}_nXX_العاطفة.html"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(full_html)

    return filename

# Main Building Loop
current_blocks = []
page_num = 0
final_files = []

# Verify Layout wrapper
def check_layout(filename):
    # Capture output of verify_layout
    # It prints JSON to stdout
    import subprocess
    result = subprocess.run(["python3", "Jules-workspace/verify_layout.py", filename], capture_output=True, text=True)
    try:
        # Find JSON object in stdout (in case of extra logs)
        stdout = result.stdout.strip()
        start = stdout.find('{')
        end = stdout.rfind('}') + 1
        if start != -1 and end != -1:
            json_str = stdout[start:end]
            return json.loads(json_str)
        else:
            return json.loads(stdout)
    except Exception as e:
        print(f"Error parsing verify_layout output: {e}")
        print("Raw stdout:", result.stdout)
        return {"status": "FAIL"}

# Process blocks
i = 0
while i < len(blocks_to_add):
    template_name, data = blocks_to_add[i]

    # Special handling for empty block title (Block 5 header)
    if template_name == "TEMPLATE_C_BLOCK.html" and data.get("CONTENT_TEXT") == "":
         # Render manually to remove empty body div if possible
         raw_tpl = read_template(template_name)
         block_html = render_template(raw_tpl, data)
         # Remove block-body if empty content
         block_html = block_html.replace('<div class="block-body">\n            <p class="mt-1mm text-accent">\n                \n            </p>\n            \n        </div>', '')
    elif template_name == "TEMPLATE_C_EXAM.html":
        # Already handled regex in preparation
        block_html = render_template(exam_template, data) # Use pre-processed exam_template
    else:
        raw_tpl = read_template(template_name)
        block_html = render_template(raw_tpl, data)

    # Add to current page
    current_blocks.append(block_html)

    # Write temp file to check
    temp_filename = write_and_check(current_blocks, page_num)

    # Verify
    layout = check_layout(temp_filename)

    if layout["status"] == "OVERFLOW":
        # Remove last block
        current_blocks.pop()
        # Save valid page (previous state)
        write_and_check(current_blocks, page_num) # Re-write without overflowing block

        # Check if underflow (unlikely if we just overflowed, but possible if block was huge)
        # If underflow, we might want to split the block? No, plan doesn't say split content inside block.
        # It says "ensure remaining page is filled with relevant exercises".

        # Check if finalized page is Underflow and try to fill
        layout = check_layout(temp_filename)
        while layout["status"] == "UNDERFLOW":
            print(f"Page {page_num} Underflow ({layout['blank_space_percentage']}% blank). Adding filler.")
            filler = get_next_filler()

            current_blocks.append(filler)
            temp_filename = write_and_check(current_blocks, page_num)
            layout = check_layout(temp_filename)

            if layout["status"] == "OVERFLOW":
                # Filler caused overflow. Remove it and stop filling.
                current_blocks.pop()
                temp_filename = write_and_check(current_blocks, page_num)
                break

        # Finalize this page
        print(f"Page {page_num} finalized.")
        final_files.append(temp_filename)

        # Start new page
        page_num += 1
        current_blocks = [block_html] # Start with the block that didn't fit

    elif layout["status"] == "FAIL":
        print("Layout check failed. Stopping.")
        sys.exit(1)
    else:
        # PASS or UNDERFLOW, continue adding
        pass

    i += 1

# Process last page
temp_filename = write_and_check(current_blocks, page_num)
layout = check_layout(temp_filename)

# Handle Underflow on last page
while layout["status"] == "UNDERFLOW":
    print(f"Page {page_num} Underflow ({layout['blank_space_percentage']}% blank). Adding filler.")
    filler = get_next_filler()
    current_blocks.append(filler)
    temp_filename = write_and_check(current_blocks, page_num)
    layout = check_layout(temp_filename)

    if layout["status"] == "OVERFLOW":
        # Filler caused overflow. Remove it and stop.
        current_blocks.pop()
        write_and_check(current_blocks, page_num)
        break

final_files.append(temp_filename)
print("Generation Complete.")

# Post-process to add IDs properly using id_manager
id_manager.auto_tag(files=final_files)
