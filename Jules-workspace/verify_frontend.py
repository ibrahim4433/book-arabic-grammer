import os
from playwright.sync_api import sync_playwright

def verify():
    pages_dir = os.path.abspath('pages')
    if not os.path.exists('verification'):
        os.makedirs('verification')

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Page 1
        p1 = os.path.join(pages_dir, '29-وظائف عناصر المستوى التركيبي.html')
        url1 = f'file://{p1}'
        print(f"Navigating to {url1}")
        page.goto(url1)
        page.screenshot(path='verification/page1.png', full_page=True)

        # Page 2
        p2 = os.path.join(pages_dir, '29-1-وظائف عناصر المستوى التركيبي.html')
        url2 = f'file://{p2}'
        print(f"Navigating to {url2}")
        page.goto(url2)
        page.screenshot(path='verification/page2.png', full_page=True)

        browser.close()

if __name__ == '__main__':
    verify()
