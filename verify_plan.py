import sys
import re
import json

def audit_plan(plan_path):
    with open(plan_path, 'r', encoding='utf-8') as f:
        plan_content = f.read()

    errors = []
    warnings = []

    # 1. Content Integrity & Volume
    if "BLOCK 4" not in plan_content:
        errors.append("Block Count: Plan does not have at least 4 substantial content blocks.")

    # 2. Design Compliance
    if "TEMPLATE_C_TABLE" not in plan_content:
        errors.append("Density: Missing Summary Table (Matrix).")

    if "verify_layout" not in plan_content:
        errors.append("One-Page Law: Missing reference to verify_layout.py in constraints.")

    # 3. Technical & Anti-Bloat
    if "id_manager.py" not in plan_content:
        errors.append("IDs: Missing instruction to use id_manager.py.")

    # Remove the constraint section where rules are literally stated to avoid false positives
    stream_content = plan_content.split('--- START STREAM ---')[-1] if '--- START STREAM ---' in plan_content else plan_content

    if "style=" in stream_content:
        errors.append("Anti-Bloat: Found inline styles in the stream content.")

    if "<hr>" in stream_content:
        errors.append("Anti-Bloat: Found forbidden tag <hr> in the stream content.")

    score = 10 - len(errors) * 2 - len(warnings)
    if score < 0:
        score = 0

    status = "REJECTED" if errors else "APPROVED"

    result = {
        "score": score,
        "status": status,
        "critical_errors": errors,
        "warnings": warnings,
        "fix_instructions": "Review errors and adjust the plan accordingly." if errors else ""
    }

    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        audit_plan(sys.argv[1])
    else:
        audit_plan("plans/page_131-plan.md")
