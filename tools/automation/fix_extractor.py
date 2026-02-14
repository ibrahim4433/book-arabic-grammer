import sys
content = open("beta-utilities/pattern_extractor.py").read()
new_func = """def extract_classes(content):
    classes = []
    for line in content.splitlines():
        if 'class=' in line:
            m = re.search('class=' + chr(34) + '(.*?)' + chr(34), line) or re.search('class=' + chr(39) + '(.*?)' + chr(39), line)
            if m:
                classes.extend(m.group(1).split())
    return classes"""
start_tag = "def extract_classes(content):"
end_tag = "def extract_structure(content):"
start_idx = content.find(start_tag)
end_idx = content.find(end_tag)
if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_func + "\n\n" + content[end_idx:]
    with open("beta-utilities/pattern_extractor.py", "w") as f:
        f.write(content)
