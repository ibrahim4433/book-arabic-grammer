import os
import re
import glob
from bs4 import BeautifulSoup

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace هام -> مهم and هامة -> مهمة
    # Need to be careful to only replace whole words
    # هام is \bهام\b but in Arabic it's better to use regex with Arabic word boundaries or just simple replace
    # Let's use simple string replacement since these usually appear as "هام:" or "ملاحظة هامة"
    # Actually, let's use regex to ensure we don't break other words like "الهام" (though "الهام" is not a common word without Alif)
    content = re.sub(r'(?<![أ-ي])هام(?![أ-ي])', 'مهم', content)
    content = re.sub(r'(?<![أ-ي])هامة(?![أ-ي])', 'مهمة', content)

    soup = BeautifulSoup(content, 'html.parser')

    changed = False

    # 2. Delete all sections with id starting with b_auto_notes
    for tag in soup.find_all(id=re.compile(r'^b_auto_notes')):
        tag.decompose()
        changed = True

    # 3. Specific IDs
    b33333_div = soup.find(id='b33333')
    if b33333_div:
        # delete the phrase ”أَمِثْلَةَ إِضَافِيَّةً: ”
        target = b33333_div.find(string=re.compile("أَمِثْلَةَ إِضَافِيَّةً"))
        if target:
            if target.parent and target.parent.name == 'div':
                target.parent.decompose()
            else:
                target.extract()
            changed = True

    b55555_div = soup.find(id='b55555')
    if b55555_div:
        if 'flex-1' in b55555_div.get('class', []):
            b55555_div['class'].remove('flex-1')
            b55555_div['class'].append('w-full')
            # If parent is a flex row wrapper, we should maybe unwrap it or just let it be since w-full inside flex row takes full width anyway
            changed = True

    b66666_div = soup.find(id='b66666')
    if b66666_div:
        if 'warning' in b66666_div.get('class', []):
            b66666_div['class'].remove('warning')
            b66666_div['class'].append('tip')
        p_tag = b66666_div.find('p')
        if p_tag:
            p_tag.clear()
            strong = soup.new_tag('strong')
            strong.string = 'مُلَاحَظَةٌ: '
            p_tag.append(strong)
            p_tag.append('قَدْ يُطْلِقُ الْعَرَبُ عَلَى الْجُمْلَةِ الْمُفِيدَةِ اسْمَ «كَلِمَةٍ» مَجَازًا، كَمَا قَصَدَ الشَّاعِرُ فِي ﴿وَيْحَكَ لَنْ تُرَاعِي﴾.')
        changed = True

    b10104_div = soup.find(id='b10104')
    if b10104_div:
        p_tag = b10104_div.find('p')
        if p_tag:
            p_tag.clear()
            span = soup.new_tag('span', attrs={'class': 'exam-number'})
            span.string = '٣'
            p_tag.append(span)
            p_tag.append(' حَدِّدْ نَوْعَ كُلِّ عِبَارَةٍ (كَلِمَةٌ، كَلَامٌ، أَمْ كَلِمٌ) مِمَّا يَأْتِي: كِتَابٌ.')
            changed = True

    b10105_div = soup.find(id='b10105')
    if b10105_div:
        p_tag = b10105_div.find('p')
        if p_tag:
            p_tag.clear()
            span = soup.new_tag('span', attrs={'class': 'exam-number'})
            span.string = '٤'
            p_tag.append(span)
            p_tag.append(' حَدِّدْ نَوْعَ كُلِّ عِبَارَةٍ (كَلِمَةٌ، كَلَامٌ، أَمْ كَلِمٌ) مِمَّا يَأْتِي: قَدْ قَامَ زَيْدٌ أَمْسِ.')
            changed = True

    b85538_div = soup.find(id='b85538')
    if b85538_div:
        # fix i3rab boxes wide to be every one in a line and for a ine line
        # This implies b85538 is an irab-box or contains them.
        # Let's just add w-full and remove flex-1 or w-45pct.
        if 'irab-box' in b85538_div.get('class', []):
            if 'w-45pct' in b85538_div['class']: b85538_div['class'].remove('w-45pct')
            if 'flex-1' in b85538_div['class']: b85538_div['class'].remove('flex-1')
            if 'w-full' not in b85538_div['class']: b85538_div['class'].append('w-full')
            
            # Also check its siblings
            for sibling in b85538_div.find_next_siblings('div', class_='irab-box'):
                if 'w-45pct' in sibling['class']: sibling['class'].remove('w-45pct')
                if 'flex-1' in sibling['class']: sibling['class'].remove('flex-1')
                if 'w-full' not in sibling['class']: sibling['class'].append('w-full')
        changed = True

    # Check if there are other b_auto_notes ids not caught (sometimes they are inside other tags)
    
    new_content = str(soup)
    # Restore some formatting BS4 might mess up if needed, but it should be fine.
    # Actually BS4 replaces self-closing tags and might reformat.
    # Let's see if we can do this via regex to preserve exact formatting, or just trust BS4.
    # Actually, bs4 might encode unicode differently or change attributes.
    # Let's write the file.
    
    # Check if anything changed via soup or regex
    if str(soup) != content or new_content != content:
        # Apply regex changes back to the soup string
        final_content = re.sub(r'(?<![أ-ي])هام(?![أ-ي])', 'مهم', new_content)
        final_content = re.sub(r'(?<![أ-ي])هامة(?![أ-ي])', 'مهمة', final_content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(final_content)
        print(f"Updated {filepath}")

for f in glob.glob('pages/*.html'):
    process_file(f)
