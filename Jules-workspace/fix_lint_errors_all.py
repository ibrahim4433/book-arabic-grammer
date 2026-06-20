import os
import re

bad_classes_map = {
    'border-dashed': 'border-light',
    'border-2': 'border-light',
    'chips-container': 'flex flex-wrap gap-2mm',
    'gap-4mm': 'gap-2mm',
    'border-blue': 'border-light',
    'border-green': 'border-light',
    'border-red': 'border-light',
    'text-large': 'font-bold',
    'text-red': 'highlight-red',
    'mt-2': 'mt-2mm',
    'p-3mm': 'p-2mm'
}

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    for bad, good in bad_classes_map.items():
        # Using word boundaries to safely replace classes
        # \b doesn't work perfectly for dashes if the adjacent char is non-word, but CSS classes are alphanumeric + dashes
        # A safer regex for CSS classes: lookbehind and lookahead for non-word chars, but allowing dashes inside.
        # Actually, (?<![\w-])class-name(?![\w-]) works perfectly for CSS classes.
        pattern = r'(?<![\w-])' + re.escape(bad) + r'(?![\w-])'
        content = re.sub(pattern, good, content)

    # Remove <hr> tags
    content = re.sub(r'<hr\s*\/?>', '', content, flags=re.IGNORECASE)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {filepath}")

for root, dirs, files in os.walk('pages'):
    for file in files:
        if file.endswith('.html'):
            fix_file(os.path.join(root, file))
