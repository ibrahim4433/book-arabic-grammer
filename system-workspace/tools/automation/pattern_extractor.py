#!/usr/bin/env python3
import os
import re
import json
from pathlib import Path
from collections import Counter

PROJECT_ROOT = Path(__file__).parent.parent.parent
PAGES_DIR = PROJECT_ROOT / "pages"
OUTPUT_FILE = PROJECT_ROOT / "assets/design_patterns.json"

TARGET_PATTERN = r"01\.\d_.*\.html|0[2-7]\.\d_.*\.html|08\.[0-4]_.*\.html"

def extract_classes(content):
    classes = []
    for line in content.splitlines():
        if 'class=' in line:
            m = re.search('class=' + chr(34) + '(.*?)' + chr(34), line) or re.search('class=' + chr(39) + '(.*?)' + chr(39), line)
            if m:
                classes.extend(m.group(1).split())
    return classes

def extract_structure(content):
    components = []
    if 'split-grid' in content: components.append('split-grid')
    if 'structured-list' in content: components.append('structured-list')
    if 'dense-table' in content: components.append('dense-table')
    if 'irab-box' in content: components.append('irab-box')
    if 'exam-question' in content: components.append('exam-question')
    if 'poem-container' in content: components.append('poem-container')
    return components

def main():
    print('🔍 Analyzing Gold Standard Pages (Lesson 1 to 08.4)...')
    stats = {
        'analyzed_files': 0,
        'common_classes': {},
        'structure_usage': Counter(),
        'color_usage': Counter()
    }
    all_classes = []
    files = [f for f in PAGES_DIR.glob('*.html') if re.match(TARGET_PATTERN, f.name)]
    for f in files:
        stats['analyzed_files'] += 1
        content = f.read_text(encoding='utf-8')
        file_classes = extract_classes(content)
        all_classes.extend(file_classes)
        components = extract_structure(content)
        stats['structure_usage'].update(components)
        if 'highlight-red' in content: stats['color_usage']['highlight-red'] += 1
        if 'highlight-blue' in content: stats['color_usage']['highlight-blue'] += 1
        if 'text-accent' in content: stats['color_usage']['text-accent'] += 1
    class_counts = Counter(all_classes)
    stats['common_classes'] = dict(class_counts.most_common(50))
    stats['structure_usage'] = dict(stats['structure_usage'])
    stats['color_usage'] = dict(stats['color_usage'])
    OUTPUT_FILE.parent.mkdir(exist_ok=True)
    OUTPUT_FILE.write_text(json.dumps(stats, indent=2, ensure_ascii=False), encoding='utf-8')
    print('✅ Extracted patterns from ' + str(stats['analyzed_files']) + ' files to ' + str(OUTPUT_FILE))

if __name__ == '__main__':
    main()
