import re
import difflib

def get_text(lines):
    return re.sub(r'[^\u0600-\u06FF]', '', ''.join(lines))

out_lines = open('output.txt', 'r', encoding='utf-8').readlines()
raw_lines = open('system-workspace/text-data/raw/raw_001.txt', 'r', encoding='utf-8').readlines()

raw_norm = ""
raw_char_to_line = []
for i, line in enumerate(raw_lines):
    norm = re.sub(r'[^\u0600-\u06FF]', '', line)
    raw_norm += norm
    raw_char_to_line.extend([i] * len(norm))

pages = []
for i, line in enumerate(out_lines):
    m = re.match(r'^---\s*Page\s+(\d+)\s*---', line.strip())
    if m:
        pages.append({'num': int(m.group(1)), 'line_idx': i})

page_inserts = {}
last_raw_idx = 0

for p in pages:
    snippet_lines = out_lines[p['line_idx']+1 : p['line_idx']+15]
    snippet = get_text(snippet_lines)
    if not snippet: continue
    
    # use 100 chars for matching
    search_target = snippet[:100]
    if len(search_target) < 30: continue
    
    window_start = max(0, last_raw_idx - 500)
    window_end = min(len(raw_norm), last_raw_idx + 6000)
    window = raw_norm[window_start:window_end]
    
    best_score = 0
    best_idx = window_start
    
    for i in range(0, len(window) - len(search_target), 5):
        sub_window = window[i:i+len(search_target)]
        sm = difflib.SequenceMatcher(None, search_target, sub_window)
        score = sm.ratio()
        if score > best_score:
            best_score = score
            best_idx = window_start + i
            if score > 0.95:
                break
                
    if best_score > 0.3: # A decent fuzzy match
        line_num = raw_char_to_line[best_idx]
        while line_num in page_inserts:
            line_num += 1
        page_inserts[line_num] = p['num']
        last_raw_idx = best_idx
    else:
        print(f"Warning: Poor match for Page {p['num']}, score: {best_score}")

new_raw_lines = []
for i, line in enumerate(raw_lines):
    if i in page_inserts:
        new_raw_lines.append(f"\n--- Page {page_inserts[i]} ---\n\n")
    # Clean any previously inserted duplicate markers just in case
    if not re.match(r'^---\s*Page', line):
        new_raw_lines.append(line)

with open('system-workspace/text-data/raw/raw_001_paged.txt', 'w', encoding='utf-8') as f:
    f.writelines(new_raw_lines)
print(f"Inserted {len(page_inserts)} page markers into raw_001_paged.txt.")
