import os
import re
import sys

TEMPLATES_DIR = 'Templates/'

RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

def lint_template(filepath):
    errors = []
    filename = os.path.basename(filepath)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return [f"Error reading file: {e}"]

    # 1. No <hr> tags
    if re.search(r'<hr[^>]*>', content, re.IGNORECASE):
        errors.append("Forbidden tag <hr> found. Templates should be modular.")

    # 2. No inline styles
    if re.search(r'style=["\'][^"\']*["\']', content, re.IGNORECASE):
        errors.append("Inline style found. All styling must be in main.css.")

    # 3. No generic <ul> without structured-list
    ul_matches = re.finditer(r'<ul([^>]*)>', content, re.IGNORECASE)
    for match in ul_matches:
        attrs = match.group(1)
        if 'structured-list' not in attrs and 'toc-list' not in attrs:
            errors.append("Generic <ul> found without 'structured-list' class.")

    # 4. Anti-Bloat: TEMPLATE_C_BLOCK shouldn't have hardcoded benefit boxes
    if filename == 'TEMPLATE_C_BLOCK.html':
        if 'benefit-box' in content:
            errors.append("TEMPLATE_C_BLOCK should be a clean shell. Do not hardcode benefit-box inside it.")

    return errors

def main():
    global TEMPLATES_DIR
    if not os.path.exists(TEMPLATES_DIR):
        # Allow running from root directory as well
        TEMPLATES_DIR = 'Jules-workspace/Templates/'
        if not os.path.exists(TEMPLATES_DIR):
            print(f"{RED}[ERROR] Templates directory not found.{RESET}")
            sys.exit(1)

    templates = [os.path.join(TEMPLATES_DIR, f) for f in os.listdir(TEMPLATES_DIR) if f.endswith('.html') and not f.startswith('TEMPLATE_CHAPTER')]
    
    total_errors = 0
    print("Running Anti-Bloat Pre-Flight Check on Templates...")
    
    for filepath in templates:
        errors = lint_template(filepath)
        if errors:
            print(f"{os.path.basename(filepath)}:")
            for err in errors:
                print(f"  {RED}[ERROR] {err}{RESET}")
            total_errors += len(errors)

    if total_errors > 0:
        print(f"\n{RED}PRE-FLIGHT FAILED: Found {total_errors} template violations. Fix them to prevent generation bloat.{RESET}")
        sys.exit(1)
    else:
        print(f"{GREEN}PRE-FLIGHT SUCCESS: All templates are clean and modular.{RESET}")
        sys.exit(0)

if __name__ == "__main__":
    main()
