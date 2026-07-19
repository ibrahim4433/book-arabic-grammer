import re
import difflib

def get_text(text):
    return re.sub(r'[^\u0600-\u06FF]', '', text)

# Regex patterns for headers and footers to ignore
header_footer_patterns = [
    r"الطريق المباشر",
    r"مكتبة المجد",
    r"حلب - الجميلية",
    r"جلب - الجميلية",
    r"شارع اسكندرون",
    r"شارع الستكسديوي",
    r"تتتارع الماكدفيوي",
    r"الطريق المباشر",
    r"\d{7,8}-\d{7,8}",
    r"^\s*\d+\s*$",
    r"^\s*[\(]?\d+[\)]?\s*$",
    r"^\s*[\u0660-\u0669]+\s*$",
    r"^[^\u0600-\u06FF]+$" # No arabic characters
]
combined_pattern = re.compile("|".join(header_footer_patterns))

out_lines = open('output.txt', 'r', encoding='utf-8').readlines()
raw_lines = [l for l in open('system-workspace/text-data/raw/raw_001.txt', 'r', encoding='utf-8').readlines() if not re.match(r'^\s*---\s*Page\s+\d+\s*---\s*', l)]

raw_norm = ""
raw_char_to_line = []
for i, line in enumerate(raw_lines):
    norm = get_text(line)
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
    # Find the first real content line after the page break
    anchor_lines = []
    for k in range(p['line_idx']+1, min(len(out_lines), p['line_idx']+20)):
        line = out_lines[k].strip()
        if not line: continue
        if combined_pattern.search(line): continue
        if len(get_text(line)) < 10: continue
        anchor_lines.append(line)
        if sum(len(get_text(l)) for l in anchor_lines) > 50:
            break
            
    if not anchor_lines:
        print(f"Warning: No anchor found for Page {p['num']}")
        continue
        
    anchor_text = get_text(''.join(anchor_lines))[:100]
    
    window_start = max(0, last_raw_idx - 1000)
    window_end = min(len(raw_norm), last_raw_idx + 8000)
    window = raw_norm[window_start:window_end]
    
    best_score = 0
    best_idx = window_start
    
    for i in range(0, len(window) - len(anchor_text) + 1, 3):
        sub_window = window[i:i+len(anchor_text)]
        sm = difflib.SequenceMatcher(None, anchor_text, sub_window)
        score = sm.ratio()
        if score > best_score:
            best_score = score
            best_idx = window_start + i
            if score > 0.95:
                break
                
    # Lower threshold to 0.20 to catch the worst OCR errors
    if best_score > 0.20:
        line_num = raw_char_to_line[best_idx]
        while line_num in page_inserts:
            line_num += 1
        page_inserts[line_num] = p['num']
        last_raw_idx = best_idx
    else:
        # Fallback to the previous index
        print(f"Warning: Extremely poor match for Page {p['num']}, score: {best_score}. Using fallback position.")
        line_num = raw_char_to_line[last_raw_idx]
        while line_num in page_inserts:
            line_num += 1
        page_inserts[line_num] = p['num']

new_raw_lines = []
for i, line in enumerate(raw_lines):
    if i in page_inserts:
        new_raw_lines.append(f"\n--- Page {page_inserts[i]} ---\n\n")
    new_raw_lines.append(line)

with open('system-workspace/text-data/raw/raw_001.txt', 'w', encoding='utf-8') as f:
    f.writelines(new_raw_lines)
print(f"Inserted {len(page_inserts)} page markers exactly.")
