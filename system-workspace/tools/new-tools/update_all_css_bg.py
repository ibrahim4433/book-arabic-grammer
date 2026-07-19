import os
import re

target_css_bg = "background-image: url('../assets/page-background/background.jpg');"

# Recursively find all css files
css_files = []
for root, dirs, files in os.walk('.'):
    # skip .git or node_modules just in case
    if '.git' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.css'):
            css_files.append(os.path.join(root, file))

for css_file in css_files:
    try:
        with open(css_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace background-image: url('...'); inside .global-background-layer or anywhere it matches
        new_content = re.sub(r"background-image:\s*url\([^)]+\);", target_css_bg, content)
        
        if new_content != content:
            with open(css_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {css_file}")
    except Exception as e:
        print(f"Error processing {css_file}: {e}")
