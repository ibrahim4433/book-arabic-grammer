import os
import re
import sys

# Configuration
PAGES_DIR = 'pages/'
STYLES_FILE = 'styles/main.css'

# Specific forbidden patterns even if they exist in CSS (Design System Rules)
FORBIDDEN_CLASSES = ['list-disc', 'list-decimal', 'list-reset', 'list-none']

# Extensions to ignore when parsing CSS for classes
IGNORED_CSS_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'ttf', 'woff', 'woff2', 'eot', 'svg'}

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def parse_allowed_classes(css_file):
    if not os.path.exists(css_file):
        print(f"{RED}[ERROR] CSS file not found: {css_file}{RESET}")
        sys.exit(1)

    with open(css_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Simple regex to find class selectors
    # We look for .classname
    # We filter out typical file extensions that might appear in url(...)
    candidates = set(re.findall(r'\.([a-zA-Z][a-zA-Z0-9_-]*)', content))

    allowed = set()
    for c in candidates:
        if c.lower() not in IGNORED_CSS_EXTENSIONS:
            allowed.add(c)

    return allowed

def suggest_fix_for_style(style_content):
    style_content = style_content.lower()
    suggestions = []

    if 'color' in style_content:
        suggestions.append("Use .text-primary (Teal), .text-accent (Orange), or .text-grey.")
    if 'background' in style_content:
        suggestions.append("Use .benefit-box.warning, .benefit-box.tip, or .bg-grey-lighter.")
    if 'margin' in style_content:
        suggestions.append("Use spacing utilities: .m-0, .mb-1mm, .mt-2mm, etc.")
    if 'padding' in style_content:
        suggestions.append("Use spacing utilities: .p-0, .p-1mm, .pl-0.")
    if 'width' in style_content:
        suggestions.append("Use width utilities: .w-20pct, .w-50pct, .w-full.")
    if 'border-radius' in style_content:
        suggestions.append("Use .rounded.")

    if not suggestions:
        return "Remove inline style and use a CSS class."
    return " ".join(suggestions)

def lint_file(filepath, allowed_classes=None):
    # Auto-load allowed classes if not provided
    if allowed_classes is None and os.path.exists(STYLES_FILE):
        try:
            allowed_classes = parse_allowed_classes(STYLES_FILE)
        except Exception:
            pass

    errors = []
    warnings = []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return [f"Error reading file: {e}"], []

    # Check 1: Inline Styles (STRICT BAN)
    style_matches = re.finditer(r'style=["\']([^"\']*)["\']', content)
    for match in style_matches:
        style_content = match.group(1)
        suggestion = suggest_fix_for_style(style_content)
        errors.append(f"STRICT VIOLATION: Inline style found: '{style_content}'. {suggestion}")

    # Extract all classes used in the HTML
    class_attrs = re.findall(r'class=["\']([^"\']*)["\']', content)
    used_classes = set()
    for attr in class_attrs:
        classes = attr.split()
        for cls in classes:
            used_classes.add(cls)

    # Check 2: Whitelist (Draconian)
    if allowed_classes:
        for cls in used_classes:
            if cls not in allowed_classes:
                errors.append(f"Class '{cls}' is NOT defined in styles/main.css (Hallucinated Class). Add it to CSS or fix typo.")

    # Check 3: Forbidden Classes (Design System Violations)
    for cls in used_classes:
        if cls in FORBIDDEN_CLASSES:
            errors.append(f"Class '{cls}' is explicitly FORBIDDEN by Design System. Use .structured-list instead.")

    # Check 4: UL without structured-list
    # Note: 'toc-list' is allowed.
    ul_matches = re.finditer(r'<ul([^>]*)>', content)
    for match in ul_matches:
        attrs = match.group(1)
        if 'structured-list' not in attrs and 'toc-list' not in attrs:
            errors.append(f"Generic <ul> found without 'structured-list' class.")

    return errors, warnings

def main():
    target_files = []
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if os.path.isfile(arg):
            target_files = [arg]
        elif os.path.isdir(arg):
             target_files = sorted([os.path.join(arg, f) for f in os.listdir(arg) if f.endswith('.html')])
    else:
        if not os.path.exists(PAGES_DIR):
            print(f"{RED}Directory not found: {PAGES_DIR}{RESET}")
            sys.exit(1)
        target_files = sorted([os.path.join(PAGES_DIR, f) for f in os.listdir(PAGES_DIR) if f.endswith('.html')])

    print(f"Parsing {STYLES_FILE} for allowed classes...")
    allowed_classes = parse_allowed_classes(STYLES_FILE)
    print(f"Found {len(allowed_classes)} allowed classes.\n")

    total_errors = 0
    files_with_errors = 0

    print(f"Linting {len(target_files)} files...\n")

    for filepath in target_files:
        # Skip cover images folder if it gets picked up (it shouldn't as we filter .html)
        errors, warnings = lint_file(filepath, allowed_classes)

        if errors:
            print(f"{os.path.basename(filepath)}:")
            for err in errors:
                print(f"  {RED}[ERROR] {err}{RESET}")
            total_errors += len(errors)
            files_with_errors += 1

    if total_errors > 0:
        print(f"\n{RED}FAILED: Found {total_errors} errors in {files_with_errors} files.{RESET}")
        sys.exit(1)
    else:
        print(f"{GREEN}SUCCESS: All checks passed. Zero inline styles found.{RESET}")
        sys.exit(0)

if __name__ == "__main__":
    main()
