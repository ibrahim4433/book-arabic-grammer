import os
import re

TEMPLATES_DIR = "Jules-workspace/Templates/"
OUTPUT_FILE_1 = "pages/16.0_nXX_المنقوص والمقصور والممدود.html"
OUTPUT_FILE_2 = "pages/16.1_nXX_المنقوص والمقصور والممدود.html"


def read_template(filename):
    with open(os.path.join(TEMPLATES_DIR, filename), encoding="utf-8") as f:
        return f.read()


def generate_page():
    # Read Templates
    t_header = read_template("TEMPLATE_C_HEADER.html")
    t_block = read_template("TEMPLATE_C_BLOCK.html")
    t_split = read_template("TEMPLATE_C_SPLIT.html")
    t_table = read_template("TEMPLATE_C_TABLE.html")
    t_list = read_template("TEMPLATE_C_LIST.html")
    t_list_item = read_template("TEMPLATE_C_LIST_ITEM.html")
    t_irab = read_template("TEMPLATE_C_IRAB.html")
    t_irab_row = read_template("TEMPLATE_C_IRAB_ROW.html")
    t_irab_box_compact = read_template("TEMPLATE_C_IRAB_BOX_COMPACT.html")
    t_exam = read_template("TEMPLATE_C_EXAM.html")
    t_page_wrapper = read_template("TEMPLATE_C_PAGE_WRAPPER.html")
    t_base = read_template("TEMPLATE_C_BASE.html")
    t_benefit = read_template("TEMPLATE_C_BENEFIT_TIP.html")

    # Fix for missing irab-stack class in CSS
    t_irab = t_irab.replace('class="irab-stack"', 'class="flex flex-col"')

    blocks = []

    # === BLOCK 1: Lesson Header ===
    block1 = (
        t_header.replace("[LESSON_NUMBER]", "16")
        .replace("[CHAPTER_TITLE]", "المنقوص والمقصور والممدود")
        .replace("[CATEGORY_HEADER]", "الصرف")
        .replace("[SECTION_HEADER]", "المستوى اللغوي")
        .replace("[AUTHOR_NAME]", "أ. حنا خفيف")
        .replace("[AUTHOR_PHONE]", " ")
    )
    blocks.append(block1)

    # === BLOCK 2: Definitions (Split View) ===
    # Left Content
    left_content = (
        '<p class="text-accent">اسم مُعْرَبٌ، ينتهي <span class="highlight-red">بياء أصلية</span> مسبوقة بكسر.</p>'
        + '<p>نحو: <span class="highlight-blue">المحامي</span>، <span class="highlight-blue">الرَّاعِي</span>.</p>'
    )
    # Right Content
    right_content = (
        '<p class="text-accent">اسم مُعْرَبٌ، ينتهي <span class="highlight-red">بألفٍ</span> قبلها فتحة.</p>'
        + '<p>نحو: <span class="highlight-blue">الهوَى</span>، <span class="highlight-blue">العصَا</span>.</p>'
    )

    block2 = (
        t_split.replace("[LEFT_TITLE]", "الاسْمُ المَنْقُوصُ")
        .replace("[LEFT_CONTENT]", left_content)
        .replace("[RIGHT_TITLE]", "الاسْمُ المَقْصُورُ")
        .replace("[RIGHT_CONTENT]", right_content)
    )
    blocks.append(block2)

    # === BLOCK 3: The Extended Noun (Mamdoub) ===
    content3 = (
        '<p class="text-accent">اسم معرب آخرُهُ <span class="highlight-red">همزةٌ</span> بعدَ <span class="highlight-blue">ألفٍ زائدة</span>.</p>'
        + '<p>نحو: <span class="highlight-green">بناء</span>، <span class="highlight-green">حسناء</span>.</p>'
    )
    # Since TEMPLATE_C_BLOCK has benefit box, remove it if not used
    # But wait, TEMPLATE_C_BLOCK has [BENEFIT_TITLE] and [BENEFIT_TEXT].
    # I should remove the benefit box div if empty. I'll do a simple replace or regex if needed.
    # For now, I'll just replace with empty string and clean up manually or with regex later.
    # Actually, the template is:
    # <div class="benefit-box">
    #     <strong> [BENEFIT_TITLE]:</strong> [BENEFIT_TEXT]
    # </div>
    # I can replace the whole div with empty string if I don't use it.
    # Also, TEMPLATE_C_BLOCK wraps content in <p>, but content3 has its own <p>.
    # We need to remove the wrapper <p> from the template for this block.
    # Using a more robust regex to handle potential whitespace variations
    t_block_custom = re.sub(
        r"<p[^>]*>\s*\[CONTENT_TEXT\]\s*</p>", "[CONTENT_TEXT]", t_block, flags=re.DOTALL
    )

    # Check if replacement worked (for debugging, though we can't see stdout easily in verify step without running)
    if t_block_custom == t_block:
        # Fallback: try removing specific lines if regex failed
        t_block_custom = t_block.replace('<p class="mt-1mm text-accent">', "").replace(
            "</p>", "", 1
        )
        # Clean up potential mess if indentation remains
        t_block_custom = t_block_custom.replace("                [CONTENT_TEXT]", "[CONTENT_TEXT]")

    block3 = t_block_custom.replace("[BLOCK_TITLE]", "الاسْمُ المَمْدُودُ").replace(
        "[CONTENT_TEXT]", content3
    )
    # Remove benefit box
    block3 = re.sub(r'<div class="benefit-box">.*?</div>', "", block3, flags=re.DOTALL)
    blocks.append(block3)

    # === BLOCK 4: The Core Matrix (Summary Table) ===
    table_header = """
  <th class="w-20pct">النوع</th>
  <th class="w-25pct">التعريف</th>
  <th class="w-25pct">عند التثنية</th>
  <th class="w-30pct">عند الجمع السالم</th>
"""
    table_rows = """
<tr>
  <td class="font-bold highlight-red">المنقوص</td>
  <td>ياء لازمة قبلها كسر</td>
  <td>تُرَدُّ الياء المحذوفة<br><span class="text-sm">(قاضٍ -> قاضيان)</span></td>
  <td>تُحْذَفُ الياء ويضم/يكسر ما قبلها<br><span class="text-sm">(الراعي -> راعُونَ/راعِين)</span></td>
</tr>
<tr>
  <td class="font-bold highlight-blue">المقصور (ثلاثي)</td>
  <td>ألف قبلها فتحة</td>
  <td>تُرَدُّ الألفُ إلى أصلها<br><span class="text-sm">(فتى -> فتيان، عصا -> عصوان)</span></td>
  <td rowspan="2">تُحْذَفُ الألفُ وتفتح ما قبلها<br><span class="text-sm">(مصطفى -> مصطفَوْن)</span></td>
</tr>
<tr>
  <td class="font-bold highlight-blue">المقصور (فوق 3)</td>
  <td>ألف قبلها فتحة</td>
  <td>تُقْلَبُ الألفُ ياءً<br><span class="text-sm">(مشفى -> مشفيان)</span></td>
</tr>
<tr>
  <td class="font-bold highlight-green">الممدود (أصلية)</td>
  <td>همزة أصلية</td>
  <td>تبقى على حالها<br><span class="text-sm">(قرّاء -> قرّاءان)</span></td>
  <td>تبقى على حالها<br><span class="text-sm">(قرّاء -> قرّاؤون)</span></td>
</tr>
<tr>
  <td class="font-bold highlight-green">الممدود (منقلبة)</td>
  <td>منقلبة عن واو/ياء</td>
  <td>تبقى أو تُقلَب واوًا<br><span class="text-sm">(دعاء -> دعاءان/دعاوَان)</span></td>
  <td>(حسب القياس)</td>
</tr>
<tr>
  <td class="font-bold highlight-green">الممدود (للتأنيث)</td>
  <td>زائدة للتأنيث</td>
  <td>تُقْلَب واوًا<br><span class="text-sm">(حسناء -> حسناوان)</span></td>
  <td>تُقْلَب واوًا<br><span class="text-sm">(حسناوات)</span></td>
</tr>
"""
    block4 = (
        t_table.replace("[TABLE_TITLE]", "جدول مقارنة الأحكام")
        .replace("[TABLE_HEADERS]", table_header)
        .replace("[TABLE_ROWS]", table_rows)
    )
    blocks.append(block4)

    # === BLOCK 5: Deep Dive - Al-Manqoos Details ===
    # Using TEMPLATE_C_LIST
    item1_content = (
        '<span class="font-bold highlight-red">حذف الياء:</span> تُحْذَفُ يَاءُ الاسم المنقوص إذا كان <span class="highlight-blue">نكرةً</span> في حالتي <span class="highlight-blue">الرفع والجر</span>.'
        + "<br>مثال: (جاءَ محامٍ، مرَرْتُ بوادٍ)."
    )
    item2_content = (
        '<span class="font-bold highlight-green">بقاؤها:</span> تبقى ياء الاسم المنقوص في ثلاث حالات:'
        + "<br>1. إذا كان معرفاً بـ (ال): (جاء الساعي)."
        + "<br>2. إذا كان مضافاً: (جاء ساعي البريد)."
        + "<br>3. إذا كان منصوبًا بتنوين النصب: (رأيتُ ساعيًا)."
    )

    # Use default markers or check if marker is needed. The template has [MARKER].
    # I'll use a bullet point or similar. The example used '🔹'.
    item1 = t_list_item.replace("[MARKER]", "🔹").replace("[CONTENT]", item1_content)
    item2 = t_list_item.replace("[MARKER]", "🔹").replace("[CONTENT]", item2_content)

    block5 = t_list.replace("[LIST_TITLE]", "أحكام الاسم المنقوص التفصيلية").replace(
        "[LIST_ITEMS]", item1 + "\n" + item2
    )
    # Remove benefit box from list template too
    block5 = re.sub(r'<div class="benefit-box">.*?</div>', "", block5, flags=re.DOTALL)
    # Also need to remove the <hr> if no benefit box
    block5 = re.sub(r'<hr class="separator-dashed">', "", block5)
    blocks.append(block5)

    # === BLOCK 6: Irab Examples (Manqoos) ===
    # TEMPLATE_C_IRAB_ROW with TEMPLATE_C_IRAB_BOX_COMPACT
    box1 = t_irab_box_compact.replace("[WORD]", "محامٍ").replace(
        "[DETAILS]",
        'فاعل مرفوع، وعلامة رفعه الضَّمَّة المقدرة على <span class="highlight-red">الياء المحذوفة</span>؛ لأنه اسم منقوص.',
    )
    box2 = t_irab_box_compact.replace("[WORD]", "وادٍ").replace(
        "[DETAILS]",
        'اسم مجرور، وعلامة جرّه الكسرة المقدرة على <span class="highlight-red">الياء المحذوفة</span>؛ لأنه اسم منقوص.',
    )

    block6 = t_irab_row.replace("[IRAB_BOXES]", box1 + "\n" + box2)
    blocks.append(block6)

    # === BLOCK 7: Deep Dive - Al-Maqsur Details ===
    item3_content = (
        '<span class="font-bold highlight-red">حذف الألف (لفظًا):</span> تُحْذَفُ ألفُه لفظًا إذا كان <span class="highlight-blue">منونًا</span> بتنوين النَّصب، أو الرفع، أو الجرّ.'
        + "<br>أمثلة: (رأيتُ فتى)، (قالَ فتى)، (مررْتُ بفتًى)."
    )
    item4_content = '<span class="font-bold highlight-green">بقاؤها:</span> تبقى ألفُ الاسم المقصور لفظًا وكتابة، إذا كان معرفاً بـ (ال). نحو: الهوى.'

    item3 = t_list_item.replace("[MARKER]", "🔹").replace("[CONTENT]", item3_content)
    item4 = t_list_item.replace("[MARKER]", "🔹").replace("[CONTENT]", item4_content)

    block7 = t_list.replace("[LIST_TITLE]", "أحكام الاسم المقصور التفصيلية").replace(
        "[LIST_ITEMS]", item3 + "\n" + item4
    )
    block7 = re.sub(r'<div class="benefit-box">.*?</div>', "", block7, flags=re.DOTALL)
    block7 = re.sub(r'<hr class="separator-dashed">', "", block7)
    blocks.append(block7)

    # === BLOCK 8: Irab Example (Maqsur) ===
    # Using TEMPLATE_C_IRAB? Wait, plan says TEMPLATE_C_IRAB.
    # But it's just one word.
    # TEMPLATE_C_IRAB is <section>... [SENTENCE_TO_PARSE] ... [IRAB_BOXES] ... </section>
    # I'll use "فتى" as the sentence or maybe the full sentence from example (e.g. "فتى")
    # Plan: Word: فتى Details: ...
    # I'll use a single IRAB BOX inside the IRAB block.
    # Or I can use IRAB_ROW if I want it inline? But the plan usually implies a section if it's a block.
    # Let's use TEMPLATE_C_IRAB but with empty sentence or just the word.
    # Actually, TEMPLATE_C_IRAB has a header "إِعْرَابُ جُمْلَةٍ".
    # I'll put "فتى" in [SENTENCE_TO_PARSE].

    box3 = t_irab_box_compact.replace("[WORD]", "فتى").replace(
        "[DETAILS]",
        'فاعلٌ مرفوعٌ، وعلامة رفعه الضَّمَّةُ المقدرة على <span class="highlight-red">الألف المحذوفة (لفظًا)</span> المثبتة كتابةً؛ لأنه اسم مقصور.',
    )
    # Wait, TEMPLATE_C_IRAB expects [IRAB_BOXES] to be inside a .irab-stack div?
    # No, the template has <div class="irab-stack">[IRAB_BOXES]</div>
    # So I just provide the boxes.

    block8 = t_irab.replace("[SENTENCE_TO_PARSE]", "فتى").replace("[IRAB_BOXES]", box3)
    blocks.append(block8)

    # === BLOCK 9: Deep Dive - Al-Mamdoub Types ===
    item5_content = '<span class="font-bold text-accent">أصلية:</span> مثل (قرأ: قارئ، قرّاء). <span class="highlight-green">حكمها:</span> تبقى على حالها في المثنى والجمع السالم.'
    item6_content = '<span class="font-bold text-accent">منقلبة عن واو أو ياء:</span> مثل (دعا، يدعو: دعاو، دعاء) أو (بنى، يبني: بناي، بناء). <span class="highlight-green">حكمها:</span> تبقى على حالها، أو تُرَدُّ إلى أصلها (واوًا أو ياءً).'
    item7_content = '<span class="font-bold text-accent">زائدة للتأنيث:</span> مثل (حَسُنَ: حسناء). <span class="highlight-green">حكمها:</span> تقلب واوًا عند التثنية والجمع.'

    item5 = t_list_item.replace("[MARKER]", "🔹").replace("[CONTENT]", item5_content)
    item6 = t_list_item.replace("[MARKER]", "🔹").replace("[CONTENT]", item6_content)
    item7 = t_list_item.replace("[MARKER]", "🔹").replace("[CONTENT]", item7_content)

    block9 = t_list.replace("[LIST_TITLE]", "أنواع همزة الممدود وتفاصيلها").replace(
        "[LIST_ITEMS]", item5 + "\n" + item6 + "\n" + item7
    )
    block9 = re.sub(r'<div class="benefit-box">.*?</div>', "", block9, flags=re.DOTALL)
    block9 = re.sub(r'<hr class="separator-dashed">', "", block9)
    blocks.append(block9)

    # === BLOCK 10: Solved Exam Models ===
    table_rows_10 = """
<tr>
  <td class="font-bold">2013 علمي (أولى)<br>نوع (نِضال) ووزن (أَنْزَلْتُهُ)</td>
  <td>نِضال: اسم جامد معنى.<br>وزْنُ (أَنْزَلْتُهُ): أَفْعَلْتُهُ.</td>
</tr>
<tr>
  <td class="font-bold">2013 علمي (ثانية)<br>العلة في (يسقي) ووزن (شفيتم)</td>
  <td>العلة في (يسقي): إعلال بالتسكين.<br>وزن (شَفَيْتُم): (فَعَلْتُم).</td>
</tr>
<tr>
  <td class="font-bold">2014 علمي (أولى)<br>العلة في (كانت) ووزن (اختاروا)</td>
  <td>العلة في (كانت): إعلال بالقلب.<br>وزن (اختاروا): افتعلوا.</td>
</tr>
<tr>
  <td class="font-bold">2014 علمي (ثانية)<br>العلة في (يقى) ووزن (ينطلق)</td>
  <td>العلة في (يقى): إعلالٌ بالقلب.<br>وزن (ينطلق): ينفعل.</td>
</tr>
"""
    table_header_10 = """
  <th class="w-30pct">السؤال (الدورة)</th>
  <th>الجواب النموذجي</th>
"""
    block10 = (
        t_table.replace("[TABLE_TITLE]", "نماذج امتحانية محلولة (دورات سابقة)")
        .replace("[TABLE_HEADERS]", table_header_10)
        .replace("[TABLE_ROWS]", table_rows_10)
    )
    blocks.append(block10)

    # === BLOCK 12 (New): Extra Examples Table ===
    table_header_12 = """
  <th class="w-25pct">الكلمة</th>
  <th class="w-25pct">نوعها</th>
  <th class="w-25pct">المثنى</th>
  <th class="w-25pct">الجمع</th>
"""
    table_rows_12 = """
<tr>
  <td class="font-bold highlight-blue">المرتجي</td>
  <td>منقوص</td>
  <td>المرتجيان</td>
  <td>المرتجُون</td>
</tr>
<tr>
  <td class="font-bold highlight-red">الصغرى</td>
  <td>مقصور</td>
  <td>الصغريان</td>
  <td>الصغريات</td>
</tr>
<tr>
  <td class="font-bold highlight-green">سماء</td>
  <td>ممدود (منقلبة)</td>
  <td>سماءان / سماوان</td>
  <td>سماوات</td>
</tr>
<tr>
  <td class="font-bold highlight-green">صحراء</td>
  <td>ممدود (زائدة)</td>
  <td>صحراوان</td>
  <td>صحراوات</td>
</tr>
<tr>
  <td class="font-bold highlight-blue">الداعي</td>
  <td>منقوص</td>
  <td>الداعيان</td>
  <td>الداعُون</td>
</tr>
"""
    block12 = (
        t_table.replace("[TABLE_TITLE]", "أمثلة تطبيقية إضافية")
        .replace("[TABLE_HEADERS]", table_header_12)
        .replace("[TABLE_ROWS]", table_rows_12)
    )
    # Don't append to blocks yet, we will add it to page 2

    # === BLOCK 11: Final Evaluation (Expanded) ===
    # Manually constructing exam body for 4 questions
    q1_html = """<div class="exam-question" id="q1">
            <p class="m-0 mb-2mm">
                <span class="exam-number">1</span>
                ما نوع الهمزة في كلمة (صحراء) وما حكمها عند التثنية؟
            </p>
            <div class="border-light h-8mm bg-grey-lighter rounded"></div>
        </div>"""

    q2_html = """<div class="exam-question" id="q2">
            <p class="m-0 mb-2mm">
                <span class="exam-number">2</span>
                ثنِّ كلمة (قاضٍ) في حالة الرفع، وكلمة (عصا) في حالة النصب.
            </p>
            <div class="border-light h-8mm bg-grey-lighter rounded"></div>
        </div>"""

    q3_html = """<div class="exam-question" id="q3">
            <p class="m-0 mb-2mm">
                <span class="exam-number">3</span>
                هاتِ المثنى والجمع لكل من: (عصا، فتى، راضٍ، بناء).
            </p>
            <div class="border-light h-8mm bg-grey-lighter rounded"></div>
        </div>"""

    q4_html = """<div class="exam-question mb-0 border-none pb-0" id="q4">
            <p class="m-0 mb-2mm">
                <span class="exam-number">4</span>
                علل كتابة الألف في: (دنيا، قضايا، مستشفى).
            </p>
            <div class="border-light h-8mm bg-grey-lighter rounded"></div>
        </div>"""

    exam_body = q1_html + "\n" + q2_html + "\n" + q3_html + "\n" + q4_html

    # We need to inject this into the exam template.
    # The template has structure:
    # <div class="block-body">
    #    <!-- Question 1 --> ...
    # </div>
    # I'll replace the whole block-body content or use regex to replace questions.
    # Easier: Construct the block header and wrap body.
    block11 = f"""<section class="content-block" id="b_exam">
    <div class="block-header bg-dark">
        <span> اخْتَبِرْ نَفْسَكَ (المنقوص والمقصور والممدود)</span>
    </div>
    <div class="block-body">
        {exam_body}
    </div>
</section>"""

    blocks.append(block11)

    # === EXTRA CONTENT FOR PAGE 2 ===
    # Benefit Tip
    benefit_tip = t_benefit.replace("[TIP_TITLE]", "قاعدة إملائية (الألف اللينة)").replace(
        "[TIP_TEXT]",
        "تكتب الألف في الاسم المقصور الثلاثي طويلة إذا كان أصلها واوًا (مثل: عصا)، ومقصورة إذا كان أصلها ياءً (مثل: فتى). أما في الاسم فوق الثلاثي فتكتب مقصورة (مثل: مشفى) إلا إذا سبقتها ياء فتكتب طويلة (مثل: دنيا).",
    )

    # === SPLIT BLOCKS ===
    # Page 1: Blocks 1 (Header), 2, 3, 4, 5, 6, 7, 8 (Irab Maqsoor)
    # Page 2: Header (Modified), 9, 10, 12 (New Table), 11 (Exam) + Extras

    # Indices in blocks list:
    # 0: Header
    # 1: Split
    # 2: Mamdoub
    # 3: Table
    # 4: List Manqoos
    # 5: Irab Manqoos
    # 6: List Maqsoor
    # 7: Irab Maqsoor
    # 8: List Mamdoub (Start of Page 2)
    # 9: Table Exams
    # 10: Exam (Modified with 4 questions)

    page1_blocks = blocks[:8]
    # Page 2 content starts from index 8
    page2_blocks_content = [blocks[8], blocks[9], block12, blocks[10]]

    # Create Page 2 Header
    header_p2 = (
        t_header.replace("[LESSON_NUMBER]", "16")
        .replace("[CHAPTER_TITLE]", "المنقوص والمقصور والممدود ")
        .replace("[CATEGORY_HEADER]", "الصرف")
        .replace("[SECTION_HEADER]", "المستوى اللغوي")
        .replace("[AUTHOR_NAME]", "أ. حنا خفيف")
        .replace("[AUTHOR_PHONE]", " ")
    )

    page2_blocks = [header_p2] + page2_blocks_content + [benefit_tip]

    # === GENERATE FILES ===

    # Page 1
    content1 = "\n".join(page1_blocks)
    page1 = t_page_wrapper.replace("<!-- INJECT_CONTENT_HERE -->", content1)
    html1 = t_base.replace("<!-- INJECT_CONTENT_HERE -->", page1)

    with open(OUTPUT_FILE_1, "w", encoding="utf-8") as f:
        f.write(html1)
    print(f"Generated {OUTPUT_FILE_1}")

    # Page 2
    content2 = "\n".join(page2_blocks)
    page2 = t_page_wrapper.replace("<!-- INJECT_CONTENT_HERE -->", content2)
    html2 = t_base.replace("<!-- INJECT_CONTENT_HERE -->", page2)

    with open(OUTPUT_FILE_2, "w", encoding="utf-8") as f:
        f.write(html2)
    print(f"Generated {OUTPUT_FILE_2}")


if __name__ == "__main__":
    generate_page()
