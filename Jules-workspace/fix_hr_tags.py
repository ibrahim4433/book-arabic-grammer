import os
import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Remove all <hr> tags with any attributes
    content = re.sub(r'<hr[^>]*>', '', content, flags=re.IGNORECASE)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {filepath}")

for root, dirs, files in os.walk('pages'):
    for file in files:
        if file.endswith('.html'):
            fix_file(os.path.join(root, file))
