import re

files_to_fix = {
    "pages/039.0_n083_page_103.html": [
        (r'class="font-bold w-20pct p-0"', 'class="font-bold w-15pct p-0"')
    ],
    "pages/105.0_n149_page_168.html": [
        (r'class="w-40pct font-bold"', 'class="w-15pct font-bold"'),
        (r'class="w-30pct font-bold p-1mm"', 'class="w-15pct font-bold p-1mm"')
    ]
}

for filepath, replacements in files_to_fix.items():
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        for old, new in replacements:
            content = re.sub(old, new, content)
            
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed table on {filepath}")
    except Exception as e:
        print(f"Error on {filepath}: {e}")

