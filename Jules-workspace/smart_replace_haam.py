import os
import re
import glob
import sys

# Configuration
SEARCH_DIR = 'pages/'
FILE_PATTERN = '*.html'

# Unicode Chars (Python string interpolation handles \uXXXX)
# Arabic letters range
ARABIC_LETTERS_RANGE = '\u0621-\u064A'
# Tashkeel chars
TASHKEEL = '[\u064B-\u065F\u0670]'
# Shadda char
SHADDA = '\u0651'

# Allowed Prefixes (normalized/stripped of tashkeel)
ALLOWED_PREFIXES = {
    '',
    'و', 'ف', 'ب', 'ك', 'ل',
    'ال', 'لل',
    'وال', 'فال', 'بال', 'كال', 'لال',
    'ول', 'فل'
}

# Allowed Suffixes characters (normalized/stripped of tashkeel)
ALLOWED_SUFFIX_CHARS = {'ة', 'ه', 'ا', 'ً'}

def remove_tashkeel(text):
    return re.sub(TASHKEEL, '', text)

def replacement_callback(match):
    full_match = match.group(0)
    prefix = match.group(1) if match.group(1) else ''
    root = match.group(2) # h..m
    tail = match.group(3) if match.group(3) else ''

    # 1. Validate Prefix
    clean_prefix = remove_tashkeel(prefix)
    if clean_prefix not in ALLOWED_PREFIXES:
        return full_match

    # 2. Validate Tail
    clean_tail = remove_tashkeel(tail)
    for char in clean_tail:
        if char not in ALLOWED_SUFFIX_CHARS:
            return full_match

    # 3. Apply Replacement
    new_root = "مُهِمّ"

    return prefix + new_root + tail

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return False

    # Construct Regex Pattern using normal strings (so \u works)
    # Note: We must escape the '[' and ']' for the character class of Arabic letters
    # But wait, ARABIC_LETTERS_RANGE is just the range string.
    # So we put it inside [].

    pattern_str = (
        r'(?<![' + ARABIC_LETTERS_RANGE + r'])'     # Lookbehind
        r'([' + ARABIC_LETTERS_RANGE + r']*)'       # Group 1: Prefix
        r'(ه' + TASHKEEL + r'*ا' + TASHKEEL + r'*م' + SHADDA + r'?)' # Group 2: Root (consuming optional Shadda)
        r'([' + ARABIC_LETTERS_RANGE + r'\u064B-\u065F\u0670]*)' # Group 3: Tail (Letters + Tashkeel)
        r'(?![a-zA-Z' + ARABIC_LETTERS_RANGE + r'])' # Lookahead
    )

    pattern = re.compile(pattern_str)

    new_content = pattern.sub(replacement_callback, content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    target_dir = sys.argv[1] if len(sys.argv) > 1 else SEARCH_DIR
    files = glob.glob(os.path.join(target_dir, FILE_PATTERN))

    print(f"Scanning {len(files)} files in {target_dir} for 'هام'/'هامة'...")

    count = 0
    for f in files:
        if process_file(f):
            print(f"Modified: {f}")
            count += 1

    print(f"Completed. {count} files updated.")

if __name__ == '__main__':
    main()
