import re
import json
import os

input_file = 'system-workspace/text-data/raw/raw_001.txt'
output_indexed = 'system-workspace/text-data/raw_001_indexed.txt'
output_toc = 'input/TOC.json'

with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

indexed_lines = []
toc = {}

for i, line in enumerate(lines):
    indexed_lines.append(f"[raw_001.txt:{i+1}] {line}")
    
    m = re.match(r'^-+\s*PAGE\s+(\d+)\s*-+', line.strip(), re.IGNORECASE)
    if m:
        page_num_int = int(m.group(1))
        # Ensure it's padded or just converted to string
        # Since it starts from 101, it's already 3 digits, so :02d doesn't truncate it, it will just leave it as 3 digits
        page_key = f"{page_num_int}"
        page_num_str = str(page_num_int)
        
        # Add page to TOC immediately upon finding the marker
        toc[page_key] = {
            "title": f"page {page_num_str}",
            "level": page_num_str,
            "Unit": page_num_str,
            "author": "أ.الياس خفيف",
            "author_number": "994066850 963+"
        }

with open(output_indexed, 'w', encoding='utf-8') as f:
    f.writelines(indexed_lines)

os.makedirs(os.path.dirname(output_toc), exist_ok=True)

with open(output_toc, 'w', encoding='utf-8') as f:
    json.dump(toc, f, ensure_ascii=False, indent=4)

print(f"Created {output_indexed} with {len(indexed_lines)} lines.")
print(f"Created {output_toc} with {len(toc)} entries.")
