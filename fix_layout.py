import re

with open('pages/page_159_4q30t.html', 'r') as f:
    content = f.read()

# Let's add an orange element. e.g. for BLOCK 4 or BLOCK 5 header.
content = content.replace('<div class="block-header">\n<span>خلاصة</span>', '<div class="block-header accent">\n<span>خلاصة</span>')

with open('pages/page_159_4q30t.html', 'w') as f:
    f.write(content)
