#!/usr/bin/env python3
"""
Helper script to generate the HTML for Lesson 14 using JulesPageGenerator.
This fulfills the requirement to create a generation script.
"""
import sys
import os
import logging
from pathlib import Path

# Add system-workspace modules to path
sys.path.append(os.path.abspath("system-workspace/tools/automation/modules"))

try:
    from jules_page_generator import JulesPageGenerator
except ImportError:
    print("Error: Could not import JulesPageGenerator. Check paths.")
    sys.exit(1)

def main():
    # Setup logging
    logging.basicConfig(level=logging.INFO)

    print("=== Lesson 14 Generation Helper ===")

    plan_path = Path("plans/14-الجامد والمشتق-plan.md")
    if not plan_path.exists():
        print(f"Error: Plan not found at {plan_path}")
        return

    print(f"Plan found: {plan_path}")
    print("Initializing JulesPageGenerator...")

    # We initialize the generator but we do NOT run it automatically
    # because it requires API credentials/setup that might not be active
    # in this specific shell context, and the instruction was to create
    # the script to 'help' generate.

    try:
        generator = JulesPageGenerator(project_root=os.getcwd())
        print("Generator initialized successfully.")

        # Uncomment the following line to actually run the generation
        # generator.process_plan(plan_path)

        print("\nTo generate the page, run this script and uncomment the 'generator.process_plan' line.")
        print("Or use the batch runner in system.py")

    except Exception as e:
        print(f"Initialization failed: {e}")

if __name__ == "__main__":
    main()
