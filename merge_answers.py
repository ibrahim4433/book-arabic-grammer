import os
from bs4 import BeautifulSoup

with open('pages/98.00_p120_Answers.html', encoding='utf-8') as f:
    soup1 = BeautifulSoup(f.read(), 'html.parser')

with open('pages/98.43_p163_Answers.html', encoding='utf-8') as f:
    soup2 = BeautifulSoup(f.read(), 'html.parser')

# Get the container in soup1 where we should append.
# The answers are inside <div class="force-new-page">
container1 = soup1.find('div', class_='force-new-page')

# We want to extract the answers from soup2 (ignore header and body/html tags)
# Basically, any <div class="block-header"> and <div class="block-body"> and <div class="exam-question">
# Actually, everything inside <div class="force-new-page"> EXCEPT the <header>
container2 = soup2.find('div', class_='force-new-page')

if container2:
    for child in container2.find_all(recursive=False):
        if child.name == 'header':
            continue # Skip the header because we don't want parts!
        container1.append(child)

with open('pages/98.00_p120_Answers.html', 'w', encoding='utf-8') as f:
    f.write(str(soup1))

# Delete the merged file
os.remove('pages/98.43_p163_Answers.html')
print('Merged successfully')
