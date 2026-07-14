import json, re, sys
from pathlib import Path
sys.path.append('system-workspace/tools/automation/modules')
from text_processing import TextProcessor

PROJECT_ROOT = Path(".")
tp = TextProcessor(".")
l_num = "07"
mapping = json.loads((PROJECT_ROOT / "system-workspace/text-data/raw_to_lesson_index.json").read_text(encoding='utf-8'))

found_t = None
for t, info in mapping.items():
    res = tp.get_lesson_number(t)
    if res == l_num:
        found_t = t
        break

print("Result of next():", found_t)
