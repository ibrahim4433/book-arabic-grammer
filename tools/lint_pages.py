import os
import re
import sys

# Configuration
PAGES_DIR = 'pages/'
FORBIDDEN_CLASSES = ['list-disc', 'list-decimal', 'list-reset', 'list-none']
FORBIDDEN_STYLE_PROPS = ['color', 'background', 'margin', 'padding']
ALLOWED_STYLE_EXCEPTIONS = [] # Add specific exceptions if needed

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def lint_file(filepath):
    errors = []
    warnings = []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return [f"Error reading file: {e}"], []

    # Check 1: Forbidden Classes
    for cls in FORBIDDEN_CLASSES:
        # Simple regex to find class="..." containing the forbidden class
        # This handles class="list-disc" or class="mb-5 list-disc"
        pattern = r'class=["\'][^"\']*' + re.escape(cls) + r'[^"\']*["\']'
        matches = re.finditer(pattern, content)
        for match in matches:
            errors.append(f"Forbidden class found: '{cls}'")

    # Check 2: UL without structured-list
    # Find all <ul> tags
    ul_matches = re.finditer(r'<ul([^>]*)>', content)
    for match in ul_matches:
        attrs = match.group(1)
        if 'structured-list' not in attrs:
            errors.append(f"Generic <ul> found without 'structured-list' class")

    # Check 3: Forbidden Inline Styles
    # Find all style="..."
    style_matches = re.finditer(r'style=["\']([^"\']*)["\']', content)
    for match in style_matches:
        style_content = match.group(1).lower()
        for prop in FORBIDDEN_STYLE_PROPS:
            if f"{prop}" in style_content:
                # Heuristic: check if it's really a property (e.g. "background-color:" or "color:")
                # simple check: prop followed by colon or part of a hyphenated prop
                if re.search(fr'{prop}[-a-z]*\s*:', style_content):
                     warnings.append(f"Inline style found with forbidden property: '{prop}' in style='{style_content}'")

    return errors, warnings

def main():
    if not os.path.exists(PAGES_DIR):
        print(f"{RED}Directory not found: {PAGES_DIR}{RESET}")
        sys.exit(1)

    files = sorted([f for f in os.listdir(PAGES_DIR) if f.endswith('.html')])
    total_errors = 0

    print(f"Linting {len(files)} files in {PAGES_DIR}...\n")

    for filename in files:
        filepath = os.path.join(PAGES_DIR, filename)
        errors, warnings = lint_file(filepath)

        if errors or warnings:
            print(f"{os.path.basename(filepath)}:")
            for err in errors:
                print(f"  {RED}[ERROR] {err}{RESET}")
            for warn in warnings:
                print(f"  {YELLOW}[WARN]  {warn}{RESET}")
            print("")
            total_errors += len(errors)

    if total_errors > 0:
        print(f"{RED}FAILED: Found {total_errors} errors.{RESET}")
        sys.exit(1)
    else:
        print(f"{GREEN}SUCCESS: All checks passed.{RESET}")
        sys.exit(0)

if __name__ == "__main__":
    main()
