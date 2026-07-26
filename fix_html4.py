from bs4 import BeautifulSoup

def fix_html():
    with open('pages/page_108_tbuuz.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Find all <p> tags
    for p in soup.find_all('p'):
        # If <p> contains <div> or <table>, unwrap it
        if p.find('div') or p.find('table'):
            p.unwrap()

    with open('pages/page_108_tbuuz.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == "__main__":
    fix_html()
