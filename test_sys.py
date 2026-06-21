import json, re, sys
from pathlib import Path
sys.path.append('system-workspace/tools/automation/modules')
from jules_planner import JulesPlanner

PROJECT_ROOT = Path(".")
planner = JulesPlanner(PROJECT_ROOT)

l_num = "07"
try:
    mapping = json.loads((PROJECT_ROOT / "system-workspace/text-data/raw_to_lesson_index.json").read_text(encoding='utf-8'))
    title = next((t for t, info in mapping.items() if planner.tp.get_lesson_number(t) == l_num), f"Lesson {l_num}")
    clean_t = re.sub(r'^\d+\s*-\s*', '', title).strip()
    expected_path = f"plans/{l_num}-{clean_t}-plan.md"
    failed_data = [(l_num, title, expected_path)]
except Exception as e:
    print("Exception!", e)
    failed_data = [(l_num, f"Lesson {l_num}", f"plans/{l_num}-plan.md")]

print("failed_data:", failed_data)
