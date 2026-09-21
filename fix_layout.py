import re

with open('pages/011.003_nXXX_exercises on the poem_w0hg0.html', 'r') as f:
    content = f.read()

# Remove .solved class
content = content.replace('exam-question solved', 'exam-question')
content = content.replace('benefit-box mt-2mm p-2mm', 'benefit-box mt-1mm p-1mm bg-grey-lighter')

with open('pages/011.003_nXXX_exercises on the poem_w0hg0.html', 'w') as f:
    f.write(content)
