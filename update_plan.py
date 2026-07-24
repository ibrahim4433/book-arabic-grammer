import sys

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply text-accent class to definitions
    content = content.replace("المفردات:", "<span class=\"text-accent\">المفردات:</span>")
    content = content.replace("الشرح:", "<span class=\"text-accent\">الشرح:</span>")
    content = content.replace("الفكرة:", "<span class=\"text-accent\">الفكرة:</span>")

    # Remove the artifact from block 16
    content = content.replace("-\n۷۸۱", "")
    content = content.replace("-\n-", "")

    # Convert the raw text table in Block 5 to a proper markdown representation of what goes into the template
    block_5_old = """=== BLOCK 5: الأساليب 1 ===
(Component: TEMPLATE_C_TABLE.html)
Title: الأساليب
Content:
تغني بأمتي: أسلوب أمر. صِيغَتُهُ فِعل أمر.
(إنها عادت)، (إِنَّا فِي أَرْضِنَا طَلَقَاءُ): أسلوب توكيد. المؤكد: إن. نوع التوكيد: جائز."""

    block_5_new = """=== BLOCK 5: الأساليب 1 ===
(Component: TEMPLATE_C_TABLE.html)
Title: الأساليب
Content:
تغني بأمتي: أسلوب أمر. صِيغَتُهُ فِعل أمر.
(إنها عادت)، (إِنَّا فِي أَرْضِنَا طَلَقَاءُ): أسلوب توكيد. المؤكد: إن. نوع التوكيد: جائز.
(Note to generator: Map this into rows/columns in the dense-table layout)"""

    content = content.replace(block_5_old, block_5_new)

    # Similarly for Block 9
    block_9_old = """=== BLOCK 9: البلاغة والتراكيب 2 ===
(Component: TEMPLATE_C_TABLE.html)
Title: البلاغة والتراكيب
Content:
الأداة التراكيب المثال: سَرَابٌ دُرُوبُكُمْ وَشَقَاءُ.
البلاغة: (سَرَابٌ دُرُوبُكُمُ): تشبيه بليغ"""

    block_9_new = """=== BLOCK 9: البلاغة والتراكيب 2 ===
(Component: TEMPLATE_C_TABLE.html)
Title: البلاغة والتراكيب
Content:
الأداة التراكيب المثال: سَرَابٌ دُرُوبُكُمْ وَشَقَاءُ.
البلاغة: (سَرَابٌ دُرُوبُكُمُ): تشبيه بليغ
(Note to generator: Map this into rows/columns in the dense-table layout)"""

    content = content.replace(block_9_old, block_9_new)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

process_file('plans/page_128-plan.md')
