import os
import json

toc_path = 'C3_Lessons_Text/TOC.json'
with open(toc_path, 'r', encoding='utf-8') as f:
    toc = json.load(f)

toc_keys = list(toc.keys())
current_lesson_idx = 0
last_written_loc = None

full_raw_indexed_lines = []
index_data = {}

for file_num in range(1, 14):
    file_name = f'raw{file_num}.txt'
    file_path = os.path.join('C3_Lessons_Text', file_name)
    
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
                
            loc = f'{file_name}:{line_num}'
            
            if line.startswith('===') and line.endswith('==='):
                # End previous lesson
                if current_lesson_idx > 0:
                    prev_key = toc_keys[current_lesson_idx - 1]
                    title = toc[prev_key]['title']
                    index_data[title]['end'] = last_written_loc
                
                # Start new lesson
                if current_lesson_idx < len(toc_keys):
                    curr_key = toc_keys[current_lesson_idx]
                    title = toc[curr_key]['title']
                    index_data[title] = {'start': loc, 'end': loc}
                    current_lesson_idx += 1
            
            full_raw_indexed_lines.append(f'[{loc}]  {line}\n')
            last_written_loc = loc

# Close the final lesson
if current_lesson_idx > 0:
    prev_key = toc_keys[current_lesson_idx - 1]
    title = toc[prev_key]['title']
    index_data[title]['end'] = last_written_loc

with open('C3_Lessons_Text/full_raw_indexed.txt', 'w', encoding='utf-8') as f:
    f.writelines(full_raw_indexed_lines)

with open('C3_Lessons_Text/raw_to_lesson_index.json', 'w', encoding='utf-8') as f:
    json.dump(index_data, f, ensure_ascii=False, indent=4)

print(f"Processed {current_lesson_idx} lessons. Output files created.")
