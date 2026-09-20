import sys
from pathlib import Path
sys.path.append(str(Path("/mnt/c/Documents and Settings/ibrah/Documents/GitHub/book-arabic-grammer/system-workspace/tools/automation/modules")))
from jules_page_generator import JulesPageGenerator

generator = JulesPageGenerator(
    project_root="/mnt/c/Documents and Settings/ibrah/Documents/GitHub/book-arabic-grammer",
    is_1_part_mode=True,
    part_number=[str(i) for i in range(1, 51)]
)

def dummy_callback(t, s, m):
    print(f"[{s}] {t}: {m}")

generator.run_batch_generation(max_concurrent=1, update_callback=dummy_callback, excluded_lessons=set(), only_lessons=["1", "2", "3"])
