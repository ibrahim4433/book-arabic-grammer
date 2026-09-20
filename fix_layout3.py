import re

with open('pages/011.003_nXXX_exercises on the poem_w0hg0.html', 'r') as f:
    content = f.read()

# Make qa tables more dense
content = re.sub(r'exam-question mt-1mm', 'exam-question mt-0', content)
content = re.sub(r'benefit-box mt-1mm p-1mm', 'benefit-box mt-0 p-0', content)
content = re.sub(r'm-0 mb-0', 'm-0', content)

with open('pages/011.003_nXXX_exercises on the poem_w0hg0.html', 'w') as f:
    f.write(content)
