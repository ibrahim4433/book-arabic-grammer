import os
import re
import sys
from bs4 import BeautifulSoup

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

def check_exam_compliance(soup, errors):
    """
    Enforces the 'Golden Standard' for Exams (Test Yourself).
    1. Header must be .bg-dark.
    2. Questions must have answer boxes.
    """
    # 1. Check Headers
    headers = soup.find_all(class_='block-header')
    for header in headers:
        text = header.get_text()
        if 'اخْتَبِرْ نَفْسَكَ' in text or 'Test Yourself' in text:
            classes = header.get('class', [])
            if 'bg-dark' not in classes:
                errors.append(f"Exam Header '{text.strip()}' must have class '.bg-dark'. Found: {classes}")
            if 'accent' in classes:
                errors.append(f"Exam Header '{text.strip()}' must NOT have class '.accent'.")

    # 2. Check Questions (Must have answer box)
    questions = soup.find_all(class_='exam-question')
    for q in questions:
        # Look for the answer box
        answer_box = q.find(class_='bg-grey-lighter')
        if not answer_box:
            # Check if it is a 'Solved Exercise' (has answers in text).
            # If so, it shouldn't use .exam-question class?
            # OR, if we enforce exams to be unsolved, this is an error.
            # But wait, existing solved exercises use .exam-question?
            # Let's check 06.0. It uses .exam-question.
            # If I enforce this now, 06.0 will fail.
            # I must exclude pages that are NOT being converted yet?
            # Or strict enforcement: If you use .exam-question, you MUST have an answer box.
            # If it's a solved exercise, use .content-block + .structured-list, NOT .exam-question?
            # That seems like a good semantic distinction.
            # But 06.0 uses .exam-question.
            # I will mark it as error, which forces me to fix 06.0/07.1 as well?
            # No, I decided NOT to convert 06.0/07.1 because they are solved.
            # So I should probably RENAME the class in 06.0/07.1 to something else, like .exercise-item?
            # Or just allow it if it has a .marker?
            # The target style has an answer box.

            # Refined Rule: If it lacks an answer box, it's suspicious.
            # But let's look at the target: <div class="border-light h-8mm bg-grey-lighter rounded"></div>
            errors.append(f"Exam Question (id={q.get('id', 'N/A')}) missing Answer Box (div.bg-grey-lighter).")

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

    # Check 2: Class Whitelist & Forbidden
    class_attrs = re.findall(r'class=["\']([^"\']*)["\']', content)
    used_classes = set()
    for attr in class_attrs:
        classes = attr.split()
        for cls in classes:
            used_classes.add(cls)

    if allowed_classes:
        for cls in used_classes:
            if cls not in allowed_classes:
                errors.append(f"Class '{cls}' is NOT defined in styles/main.css.")

    for cls in used_classes:
        if cls in FORBIDDEN_CLASSES:
            errors.append(f"Class '{cls}' is explicitly FORBIDDEN. Use .structured-list instead.")

    # Check 3: UL compliance
    ul_matches = re.finditer(r'<ul([^>]*)>', content)
    for match in ul_matches:
        attrs = match.group(1)
        if 'structured-list' not in attrs and 'toc-list' not in attrs:
            errors.append(f"Generic <ul> found without 'structured-list' class.")

    # Check 3.5: Anti-Bloat Structural Checks
    if re.search(r'<hr[^>]*>', content, re.IGNORECASE):
        errors.append("STRICT VIOLATION: Forbidden tag <hr> found. Do not hallucinate dividers.")
    
    # Simple check for nested benefit boxes (this checks if a benefit box contains another benefit box string within it, simplified using regex)
    # Actually, a simpler way is to use BeautifulSoup below.

    # Check 4: BeautifulSoup Semantic Checks
    try:
        soup = BeautifulSoup(content, 'html.parser')
        check_exam_compliance(soup, errors)
        
        # Anti-Bloat: Nested benefit boxes
        for box in soup.find_all(class_='benefit-box'):
            if box.find(class_='benefit-box'):
                errors.append("STRICT VIOLATION: Nested benefit-box found. Do not nest them.")
                
    except Exception as e:
        warnings.append(f"Could not parse HTML for semantic checks: {e}")

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
