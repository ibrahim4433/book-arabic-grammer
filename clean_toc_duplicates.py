import glob
from bs4 import BeautifulSoup

def clean_duplicates():
    for filepath in glob.glob('pages/00.*_TOC.html'):
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            
        tables = soup.find_all('table')
        for table in tables:
            trs = table.find_all('tr')
            seen_titles = set()
            for tr in trs:
                title_td = tr.find('td', class_='font-bold')
                if title_td:
                    title_text = title_td.get_text().strip()
                    if title_text in seen_titles:
                        tr.decompose()
                    else:
                        seen_titles.add(title_text)
                        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(soup.encode(formatter=None).decode('utf-8'))
        print(f"Cleaned duplicates in {filepath}")

if __name__ == '__main__':
    clean_duplicates()
