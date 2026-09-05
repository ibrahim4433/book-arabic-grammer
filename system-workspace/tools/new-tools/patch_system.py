import re
from pathlib import Path

fpath = Path("system-workspace/tools/new-tools/system.py")
content = fpath.read_text(encoding="utf-8")

# 1. Update run_jules_planning_ui
content = content.replace("def run_jules_planning_ui(state_manager, is_1_page_mode=False):", "def run_jules_planning_ui(state_manager, is_1_page_mode=False, is_1_part_mode=False, part_instruction=''):")
content = content.replace("from modules.jules_planner import JulesPlanner", "from modules.jules_planner import JulesPlanner") # No change
content = content.replace("planner = JulesPlanner(\n            project_root=PROJECT_ROOT,\n            state_manager=state_manager,\n            is_1_page_mode=is_1_page_mode,\n        )", "planner = JulesPlanner(\n            project_root=PROJECT_ROOT,\n            state_manager=state_manager,\n            is_1_page_mode=is_1_page_mode,\n            is_1_part_mode=is_1_part_mode,\n            part_instruction=part_instruction\n        )")

# 2. Update run_jules_generation_ui
content = content.replace("def run_jules_generation_ui(state_manager, is_1_page_mode=False):", "def run_jules_generation_ui(state_manager, is_1_page_mode=False, is_1_part_mode=False):")
content = content.replace("generator = JulesPageGenerator(\n            project_root=PROJECT_ROOT,\n            state_manager=state_manager,\n            is_1_page_mode=is_1_page_mode,\n        )", "generator = JulesPageGenerator(\n            project_root=PROJECT_ROOT,\n            state_manager=state_manager,\n            is_1_page_mode=is_1_page_mode,\n            is_1_part_mode=is_1_part_mode\n        )")

# 3. Update run_full_auto_ui
content = content.replace("def run_full_auto_ui(state_manager, is_1_page_mode=False):", "def run_full_auto_ui(state_manager, is_1_page_mode=False, is_1_part_mode=False, part_instruction=''):")
content = content.replace("planner = JulesPlanner(\n            project_root=PROJECT_ROOT,\n            state_manager=state_manager,\n            is_1_page_mode=is_1_page_mode,\n        )", "planner = JulesPlanner(\n            project_root=PROJECT_ROOT,\n            state_manager=state_manager,\n            is_1_page_mode=is_1_page_mode,\n            is_1_part_mode=is_1_part_mode,\n            part_instruction=part_instruction\n        )")
content = content.replace("generator = JulesPageGenerator(\n                project_root=PROJECT_ROOT,\n                state_manager=state_manager,\n                is_1_page_mode=is_1_page_mode,\n            )", "generator = JulesPageGenerator(\n                project_root=PROJECT_ROOT,\n                state_manager=state_manager,\n                is_1_page_mode=is_1_page_mode,\n                is_1_part_mode=is_1_part_mode\n            )")

# 4. Update Main Menu
main_menu_old = '''        main_choice = questionary.select(
            "Select Category:",
            choices=[
                "1) book making by 1-lesson-1-plan method",
                "2) book making by 1-page-1-plan method",
                "3) OCR tools",
                "4) Book Style Tuning",
                "5) Settings",
                "6) Clear History",
                "7) auto smart merging/pulling tool",
                "8) refresh workspace code",
                "9) Close all open pull requests",
                "D) Delete all branches (except main)",
                "0) Quit",
            ],
            style=menu_style,
        ).ask()'''
        
main_menu_new = '''        main_choice = questionary.select(
            "Select Category:",
            choices=[
                "1) book making by 1-lesson-1-plan method",
                "2) book making by 1-page-1-plan method",
                "3) book making by 1-part method",
                "4) OCR tools",
                "5) Book Style Tuning",
                "6) Settings",
                "7) Clear History",
                "8) auto smart merging/pulling tool",
                "9) refresh workspace code",
                "A) Close all open pull requests",
                "D) Delete all branches (except main)",
                "0) Quit",
            ],
            style=menu_style,
        ).ask()'''
        
content = content.replace(main_menu_old, main_menu_new)

menu_logic_old = '''        elif main_op == "3":
            sub_choice = questionary.select(
                "Select Operation (OCR tools):",
                choices=[
                    "A) Images -> Raw ( JULES )",
                    "B) Images -> Raw ( API/CLI )",
                    "C) Images -> Raw ( Local-utilities )",
                    "D) Images -> Raw ( Local-AI-network )",
                    "E) Video / Youtube -> Raw",
                    "X) Back to Main Menu",
                ],
                style=menu_style,
            ).ask()'''
            
menu_logic_new = '''        elif main_op == "3":
            sub_choice = questionary.select(
                "Select Operation (1-part method):",
                choices=[
                    "A) Full Auto Workflow",
                    "B) Raw Processing (Auto-Paginated Index & TOC)",
                    "C) Plan Generation (Jules Batch - 1-Part Method)",
                    "D) Page Generation (Jules Batch - 1-Part Method)",
                    "E) Audit & Verify Pages",
                    "X) Back to Main Menu",
                ],
                style=menu_style,
            ).ask()
            
            if sub_choice and not sub_choice.startswith("X"):
                sub_op = sub_choice[0]
                op_ran = True
                part_instruction = ""
                if sub_op in ["A", "C"]:
                    part_instruction = questionary.text("Enter custom instruction for this Part (or leave empty):").ask()
                
                if sub_op == "A":
                    run_full_auto_ui(state_manager, is_1_part_mode=True, part_instruction=part_instruction)
                elif sub_op == "B":
                    run_raw_processing_auto(state_manager)
                elif sub_op == "C":
                    run_jules_planning_ui(state_manager, is_1_part_mode=True, part_instruction=part_instruction)
                elif sub_op == "D":
                    run_jules_generation_ui(state_manager, is_1_part_mode=True)
                elif sub_op == "E":
                    run_audit_and_verify(state_manager)

        elif main_op == "4":
            sub_choice = questionary.select(
                "Select Operation (OCR tools):",
                choices=[
                    "A) Images -> Raw ( JULES )",
                    "B) Images -> Raw ( API/CLI )",
                    "C) Images -> Raw ( Local-utilities )",
                    "D) Images -> Raw ( Local-AI-network )",
                    "E) Video / Youtube -> Raw",
                    "X) Back to Main Menu",
                ],
                style=menu_style,
            ).ask()'''
            
content = content.replace(menu_logic_old, menu_logic_new)

# Shift indices for 4,5,6,7,8,9
content = content.replace('elif main_op == "4":\n            sub_choice = questionary.select(\n                "Select Operation (Book Style Tuning):",', 'elif main_op == "5":\n            sub_choice = questionary.select(\n                "Select Operation (Book Style Tuning):",')
content = content.replace('elif main_op == "5":\n            op_ran = True\n            run_settings()', 'elif main_op == "6":\n            op_ran = True\n            run_settings()')
content = content.replace('elif main_op == "6":\n            if questionary.confirm("Are you sure you want to completely clear the project state history?").ask():', 'elif main_op == "7":\n            if questionary.confirm("Are you sure you want to completely clear the project state history?").ask():')
content = content.replace('elif main_op == "7":\n            op_ran = True\n            run_auto_smart_merging()', 'elif main_op == "8":\n            op_ran = True\n            run_auto_smart_merging()')
content = content.replace('elif main_op == "8":\n            op_ran = True\n            run_refresh_workspace_code()', 'elif main_op == "9":\n            op_ran = True\n            run_refresh_workspace_code()')
content = content.replace('elif main_op == "9":\n            op_ran = True\n            run_close_all_prs()', 'elif main_op == "A":\n            op_ran = True\n            run_close_all_prs()')

fpath.write_text(content, encoding="utf-8")
print("Done patching system.py")
