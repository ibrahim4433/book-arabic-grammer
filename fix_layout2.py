import re

with open('pages/011.003_nXXX_exercises on the poem_w0hg0.html', 'r') as f:
    content = f.read()

# Replace mb-2mm with mb-0 on repetitive elements to condense space
content = re.sub(r'exam-question mt-2mm', 'exam-question mt-1mm', content)
content = re.sub(r'mt-2mm', 'mt-1mm', content)
content = re.sub(r'mb-2mm', 'mb-0', content)
content = re.sub(r'p-2mm', 'p-1mm', content)
content = re.sub(r'exam-question\s+', 'exam-question ', content)

with open('pages/011.003_nXXX_exercises on the poem_w0hg0.html', 'w') as f:
    f.write(content)
