import time
t0 = time.time()
def p(name): print(f"{time.time()-t0:.2f}s: {name}")

import sys
from pathlib import Path
p("sys/pathlib")
PROJECT_ROOT = Path('.').resolve()
sys.path.append(str(PROJECT_ROOT / "system-workspace/tools/automation"))
sys.path.append(str(PROJECT_ROOT / "Jules-workspace"))

import questionary
from rich.console import Console
p("rich/questionary")

from modules.text_processing import TextProcessor
p("TextProcessor")

from modules.jules_planner import JulesPlanner
p("JulesPlanner")

from modules.unified_flow import UnifiedFlowRunner
p("UnifiedFlowRunner")

from modules.repoless_jules import RepolessJulesClient
p("RepolessJulesClient")
