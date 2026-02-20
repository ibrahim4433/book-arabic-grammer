#!/usr/bin/env python3
import os
import subprocess
import json
import re
from pathlib import Path

# Config
PROJECT_ROOT = Path(__file__).parent.parent.parent
ARCHITECT_PROMPT = PROJECT_ROOT / "system workspace/Architect_GEM_MASTER.md"
AUDITOR_PROMPT = PROJECT_ROOT / "system workspace/Architect_AUDITOR.md"
PATTERNS_FILE = PROJECT_ROOT / "Jules workspace/design_patterns.json"
TOC_FILE = PROJECT_ROOT / "input/TOC.json"

# Global state for sticky model selection within a single run
CURRENT_MODEL_INDEX = 0
MODELS_CHAIN = [
    "gemini-3-pro-preview",
    "gemini-2.5-pro",
    "gemini-3-flash-preview",
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite"
]

def run_gemini(prompt_file, context_files, additional_text=""):
    """Runs Gemini CLI with the prompt and context files using a sticky fallback chain."""
    global CURRENT_MODEL_INDEX
    
    # Construct input stream
    input_content = prompt_file.read_text(encoding='utf-8') + "\n\n"
    input_content += additional_text + "\n\n"
    
    # Inject TOC context automatically if available
    if TOC_FILE.exists():
        input_content += f"=== TOC.json (Reference) ===\n" + TOC_FILE.read_text(encoding='utf-8') + "\n\n"
    
    for f in context_files:
        if f.exists():
            input_content += f"=== {f.name} ===\n" + f.read_text(encoding='utf-8') + "\n\n"

    for i in range(CURRENT_MODEL_INDEX, len(MODELS_CHAIN)):
        model = MODELS_CHAIN[i]
        try:
            print(f"⏳ Running Gemini CLI (Model: {model})...")
            cmd = ["gemini", "--prompt", "Follow context.", "--model", model, "--output-format", "text"]
            
            result = subprocess.run(
                cmd,
                input=input_content,
                capture_output=True,
                text=True,
                encoding='utf-8',
                check=False,
                timeout=300
            )
            
            if result.returncode == 0 and result.stdout.strip():
                if i != CURRENT_MODEL_INDEX:
                    print(f"🔄 Switched to model '{model}' for the remainder of this session.")
                CURRENT_MODEL_INDEX = i
                return result.stdout.strip()
                
            print(f"⚠️ Model '{model}' failed or quota exhausted.")
        except Exception as e:
            print(f"❌ Execution Error with {model}: {e}")
            
    return None

def extract_json(text):
    """Extracts JSON block from text."""
    try:
        match = re.search(r'\{.*\}', text, re.DOTALL)
        if match:
            return json.loads(match.group(0))
    except:
        pass
    return None

def refine_plan(raw_text_path, output_path):
    """
    Generates a plan, audits it, and loops until approved or max retries.
    """
    raw_path = Path(raw_text_path)
    if not raw_path.exists():
        print(f"❌ Raw file not found: {raw_path}")
        return False

    print(f"🧠 Starting Plan Refinement for {raw_path.name}...")
    
    # 1. Load Context
    patterns_content = ""
    if PATTERNS_FILE.exists():
        patterns_content = PATTERNS_FILE.read_text()
    
    current_plan = ""
    feedback = ""
    
    MAX_RETRIES = 3
    for attempt in range(1, MAX_RETRIES + 2):
        print(f"\n🔄 Attempt {attempt}/{MAX_RETRIES + 1}...")
        
        # A. Generate Draft
        if attempt == 1:
            # First run: Standard generation
            response = run_gemini(ARCHITECT_PROMPT, [raw_path], 
                                  additional_text=f"[DESIGN PATTERNS]\n{patterns_content}")
        else:
            # Retry: Include feedback
            retry_instruction = f"PREVIOUS ATTEMPT FAILED.\nFEEDBACK: {feedback}\n\nREGENERATE THE PLAN FIXING THESE ISSUES."
            response = run_gemini(ARCHITECT_PROMPT, [raw_path], 
                                  additional_text=f"{retry_instruction}\n\n[DESIGN PATTERNS]\n{patterns_content}")
        
        if not response:
            print("❌ Failed to generate plan.")
            return False
            
        current_plan = response

        # B. Audit
        print("🕵️ Auditing Plan...")
        # Create a temporary file for the plan to pass to Auditor
        temp_plan_path = PROJECT_ROOT / "output/temp_plan.txt"
        temp_plan_path.write_text(current_plan, encoding='utf-8')
        
        audit_response = run_gemini(AUDITOR_PROMPT, [raw_path, temp_plan_path], 
                                    additional_text=f"[DESIGN PATTERNS]\n{patterns_content}")
        
        audit_json = extract_json(audit_response)
        
        if not audit_json:
            print(f"⚠️ Auditor returned invalid JSON. Assuming plan is OK but risky.\nResponse: {audit_response}")
            # In strict mode we might retry, but let's break for now
            break
            
        score = audit_json.get("score", 0)
        status = audit_json.get("status", "REJECTED")
        print(f"   Score: {score}/10 | Status: {status}")
        
        if status == "APPROVED" or score >= 8:
            print("✅ Plan Approved!")
            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(current_plan, encoding='utf-8')
            print(f"💾 Saved to {output_path}")
            return True
        else:
            print(f"❌ Issues: {audit_json.get('critical_errors')}")
            feedback = audit_json.get("fix_instructions", "Fix critical errors.")

    print("❌ Max retries reached. Plan refinement failed.")
    return False

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python plan_refiner.py <raw_text_path> <output_plan_path>")
        sys.exit(1)
    
    refine_plan(sys.argv[1], sys.argv[2])
