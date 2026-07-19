import re
import os

input_file = 'system-workspace/text-data/raw/raw_001.txt'

with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
page_counter = 101

for line in lines:
    if re.search(r'PAGE X', line, re.IGNORECASE):
        # Replace the line with the numbered page marker
        # Preserve leading/trailing whitespace if any
        new_lines.append(f"----- PAGE {page_counter} -----\n")
        page_counter += 1
    else:
        new_lines.append(line)

with open(input_file, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"Updated raw_001.txt with page numbers up to {page_counter - 1}")
