import re
from bs4 import BeautifulSoup

def process_page_150():
    filepath = '/mnt/c/Documents and Settings/ibrah/Documents/GitHub/book-arabic-grammer/pages/page_150_enat1.html'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # We want to reorganize the page.
    # Currently there is a split-grid. Let's find it.
    split_grid = soup.find('div', class_='split-grid')
    if not split_grid:
        print("Could not find split-grid")
        return
        
    # We will clear the split grid and replace it with a single column layout
    # containing the grouped content.
    
    # But wait, maybe the user wants it to still be a split grid?
    # If we put all poet blocks sequentially, WeasyPrint will just render them.
    # We can just empty the split-grid and append the blocks inside it directly,
    # or remove the split-grid entirely and just append the blocks to the body.
    # Let's remove the split-grid and add the blocks.
    
    # We have three poets: نسيب عريضة, بدر الدين الحامد, نديم محمد.
    
    # 1. نسيب عريضة
    # Poem is "من أنت؟ ما أنت؟"
    # Q1, Q6, Q7
    
    # 2. بدر الدين الحامد
    # Poem 1: يقولون لي
    # Poem 2: أكان التلاقي
    # Q5
    
    # 3. نديم محمد
    # Poem: يا شعوري
    # Q2, Q3, Q4
    
    # Let's extract these blocks by their IDs or classes.
    
    # Q1: id="b150007"
    q1 = soup.find(id='b150007')
    # Q2: id="b150011"
    q2 = soup.find(id='b150011')
    # Q3: id="b150013"
    q3 = soup.find(id='b150013')
    # Q4: id="b150016"
    q4 = soup.find(id='b150016')
    # Q5: id="b150020"
    q5 = soup.find(id='b150020')
    # Q6: id="b150025"
    q6 = soup.find(id='b150025')
    # Q7: id="b150026"
    q7 = soup.find(id='b150026')
    
    # Poems
    poem_naseeb = soup.find(id='b150024')  # The full poem for نسيب
    poem_badr_1 = soup.find(id='b150009')  # يقولون لي
    poem_badr_2 = soup.find(id='b150019')  # أكان التلاقي
    poem_nadeem = soup.find(id='b150012')  # يا شعوري
    
    # Other blocks like b150027 (the weird dash block)
    block_27 = soup.find(id='b150027')
    
    # Rebuild the HTML elements
    def create_poet_header(name):
        div = soup.new_tag('div', attrs={'class': 'block-header poem-header mb-0'})
        span = soup.new_tag('span')
        span.string = name
        div.append(span)
        return div
    
    container = soup.new_tag('div')
    
    # Block 1: نسيب عريضة
    container.append(create_poet_header('نسيب عريضة'))
    if poem_naseeb: container.append(poem_naseeb)
    if q1: container.append(q1)
    if q6: container.append(q6)
    if q7: container.append(q7)
    
    # Block 2: بدر الدين الحامد
    container.append(create_poet_header('بدر الدين الحامد'))
    if poem_badr_1: container.append(poem_badr_1)
    if poem_badr_2: container.append(poem_badr_2)
    if q5: container.append(q5)
    
    # Block 3: نديم محمد
    container.append(create_poet_header('نديم محمد'))
    if poem_nadeem: container.append(poem_nadeem)
    if q2: container.append(q2)
    if q3: container.append(q3)
    if q4: container.append(q4)
    
    if block_27: container.append(block_27)
    
    # Insert new container where split grid was
    split_grid.replace_with(container)
    
    # Now write the file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
process_page_150()
