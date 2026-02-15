import sys
from pathlib import Path

# Add the modules directory to path
sys.path.append("system workspace/tools/automation")
sys.path.append("system workspace/tools/automation/modules")

from modules.planner import Planner

def test_ibdal_plan():
    planner = Planner(project_root=".")
    
    raw_text = Path("/tmp/raw_ibdal.txt").read_text(encoding='utf-8')
    
    # We pass the metadata explicitly to the planner
    planner.generate_plan(
        raw_lesson_text=raw_text,
        output_filename="11 - الإبدال-plan.md",
        lesson_number="١١",
        lesson_title="الإِبْدَالُ"
    )

if __name__ == "__main__":
    test_ibdal_plan()
