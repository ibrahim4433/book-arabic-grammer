#!/usr/bin/env python3
import sys
import os
import json
import re
import subprocess
from pathlib import Path

# --- CONFIGURATION ---
PROJECT_ROOT = Path(__file__).parent.resolve()
MODULES_PATH = PROJECT_ROOT / "system workspace/tools/automation"

# --- CLI COLORS ---
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def check_dependencies():
    """Checks and installs missing dependencies from requirements.txt."""
    req_file = PROJECT_ROOT / "requirements.txt"
    if not req_file.exists():
        print(f"{Colors.WARNING}⚠️ requirements.txt not found. Skipping dependency check.{Colors.ENDC}")
        return

    print(f"{Colors.BLUE}🔍 Checking dependencies...{Colors.ENDC}")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", str(req_file)])
        print(f"{Colors.GREEN}✅ Dependencies are satisfied.{Colors.ENDC}")
    except subprocess.CalledProcessError as e:
        print(f"{Colors.FAIL}❌ Failed to install dependencies: {e}{Colors.ENDC}")
        sys.exit(1)

# Check dependencies BEFORE importing modules that might require them
check_dependencies()

# Add modules path to sys.path to allow imports despite spaces in directory names
if str(MODULES_PATH) not in sys.path:
    sys.path.append(str(MODULES_PATH))

# --- IMPORTS ---
try:
    from modules.vision import VisionClient
    from modules.text_processing import TextProcessor
    from modules.planner import Planner
    from modules.jules_planner import JulesPlanner
    from modules.compiler import Compiler
    from modules.auditor import Auditor
    from modules.state_manager import StateManager
    from modules.jules_page_generator import JulesPageGenerator
except ImportError as e:
    print(f"❌ Critical Error: Failed to import modules. Ensure 'system workspace/tools/automation/modules' exists.")
    print(f"Details: {e}")
    sys.exit(1)

# --- MENU SYSTEM ---
def print_header():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Colors.HEADER}{Colors.BOLD}=================================================={Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}   📘 ARABIC GRAMMAR BOOK - CONTROL ROOM (V2)   {Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}=================================================={Colors.ENDC}")
    print(f"Project Root: {PROJECT_ROOT}")
    print(f"Modules Path: {MODULES_PATH}\n")

def print_menu():
    print(f"{Colors.BLUE}[A] Full Auto Workflow (Images -> Book Page){Colors.ENDC}")
    print(f"{Colors.BLUE}[B] OCR Only (Images -> Raw Text){Colors.ENDC}")
    print(f"{Colors.BLUE}[C] Plan Generation (Raw Text -> Architect Plans){Colors.ENDC}")
    print(f"{Colors.BLUE}[D] Plan Generation with Jules (Raw Text -> Architect Plans){Colors.ENDC}")
    print(f"{Colors.BLUE}[E] Page Generation (Plans -> HTML){Colors.ENDC}")
    print(f"{Colors.BLUE}[F] System Status & Debug{Colors.ENDC}")
    print(f"{Colors.FAIL}[Q] Quit{Colors.ENDC}")
    print("-" * 50)

def main():
    state_manager = StateManager(PROJECT_ROOT)
    
    try:
        while True:
            print_header()
            print_menu()
            try:
                choice = input(f"{Colors.BOLD}Select Operation: {Colors.ENDC}").strip().upper()
            except EOFError:
                break
                
            if choice == 'Q':
                print("\nGoodbye.")
                break
                
            elif choice == 'B':
                run_ocr(state_manager)
                
            elif choice == 'C':
                run_planning(state_manager)
                
            elif choice == 'D':
                run_jules_planning(state_manager)

            elif choice == 'E':
                run_generation(state_manager)
                
            elif choice == 'A':
                run_full_auto(state_manager)
                
            elif choice == 'F':
                show_status(state_manager)
                
            else:
                print("Invalid option.")
            
            try:
                input(f"\n{Colors.WARNING}Press Enter to continue...{Colors.ENDC}")
            except EOFError:
                break
    except KeyboardInterrupt:
        print("\n\n🛑 Operation cancelled by user. Exiting...")
        sys.exit(0)

# --- WORKFLOW FUNCTIONS ---

def run_ocr(state_manager):
    print(f"\n{Colors.BOLD}>>> Running OCR Module...{Colors.ENDC}")
    input_dir = PROJECT_ROOT / "input"
    images = sorted(list(input_dir.glob("*.jpg")) + list(input_dir.glob("*.png")))
    
    if not images:
        print("⚠️ No images found in input/.")
        return

    # Check state to skip processed
    to_process = []
    # Simplified logic: If we have raw text matching the image name, skip?
    # For now, let's process all or ask user.
    # But VisionClient handles batch. 
    
    # Actually, TextProcessor merges raw files. VisionClient outputs raw files?
    # Wait, VisionClient returns text. We need to save it.
    
    vision = VisionClient()
    output_dir = PROJECT_ROOT / "system workspace/text-data/raw"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for img in images:
        out_file = output_dir / f"raw_{img.stem}.txt"
        if out_file.exists():
            print(f"⏭️ Skipping {img.name} (already processed).")
            continue
            
        text = vision.extract_text([img])
        if text:
            out_file.write_text(text, encoding='utf-8')
            print(f"✅ Saved: {out_file.name}")
            # Update state (Using Image Name as key for now, will map to Lesson later)
            state_manager.update_lesson_status(f"Image_{img.stem}", "OCR_DONE", {"raw": str(out_file)})
        else:
            print(f"❌ Failed to extract {img.name}")

def run_planning(state_manager):
    print(f"\n{Colors.BOLD}>>> Running Planner Module...{Colors.ENDC}")
    
    # 1. Text Processing (Merge & Index)
    tp = TextProcessor()
    if not tp.validate_toc():
        return
        
    print("1. Merging Raw Text...")
    merged_path = tp.merge_raw_text()
    if not merged_path: return
    
    print("2. Generating Lesson Index (Mapping)...")
    mapping = tp.generate_lesson_index()
    if not mapping: return
    
    # 2. Plan Generation
    planner = Planner()
    
    for lesson_title, range_info in mapping.items():
        print(f"\nplanning for: {lesson_title}")
        # Extract content for this lesson from merged file based on range
        # Start/End logic in TextProcessor mapping is tricky.
        # "start": "raw_1.txt:5"
        # We need to parse the merged file to find these lines.
        # This is complex. For V2, let's assume we pass the WHOLE merged text 
        # and let the Planner (Architect) extract the specific lesson? 
        # No, context window limits.
        
        # Simplified logic for now: Pass the WHOLE raw text (if small enough) 
        # or just the specific raw files if mapping tells us which files.
        # Mapping says "start": "raw_1.txt:5".
        # So we can identify the raw file(s) involved.
        
        # Logic: Find all raw files between start and end.
        start_file = range_info["start"].split(":")[0]
        end_file = range_info["end"].split(":")[0]
        
        # Get Lesson Number
        lesson_number = tp.get_lesson_number(lesson_title)
        
        # Clean Title (Remove "09 - " etc)
        # Regex to remove number and dash prefix
        clean_title = re.sub(r'^\d+\s*-\s*', '', lesson_title).strip()
        
        # Read content
        # (Implementation details omitted for brevity, logic needed here)
        # For prototype, we'll just skip detailed slicing and pass full merged text 
        # if it's < 30k tokens.
        
        plan_filename = f"{lesson_number}-{clean_title}-plan.md"
        plan_path = planner.generate_plan(
            raw_lesson_text=merged_path.read_text(encoding='utf-8'),
            output_filename=plan_filename,
            lesson_number=lesson_number,
            lesson_title=clean_title
        )
        if plan_path:
            state_manager.update_lesson_status(lesson_title, "PLAN_READY", {"plan": str(plan_path)})

def run_jules_planning(state_manager):
    print(f"\n{Colors.BOLD}>>> Running Jules Planner Module...{Colors.ENDC}")
    # We initialize JulesPlanner with the PROJECT_ROOT
    planner = JulesPlanner(PROJECT_ROOT)
    planner.run_batch_planning(max_concurrent=5)

def run_generation(state_manager):
    print(f"\n{Colors.BOLD}>>> Running Jules Page Generation Module (Batch)...{Colors.ENDC}")
    
    try:
        generator = JulesPageGenerator(project_root=PROJECT_ROOT)
        generator.run_batch_generation(max_concurrent=5)
    except Exception as e:
        print(f"❌ Error in Page Generation: {e}")

def run_full_auto(state_manager):
    run_ocr(state_manager)
    run_planning(state_manager)
    run_generation(state_manager)

def show_status(state_manager):
    print(f"\n{Colors.BOLD}>>> System Status...{Colors.ENDC}")
    lessons = state_manager.get_all_lessons()
    for title, info in lessons.items():
        print(f"{title}: {info['status']}")

if __name__ == "__main__":
    main()
