from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        cwd = os.getcwd()

        files = [
            "pages/01.0_n03_verbs.html",
            "pages/02.0_n06_pronouns.html",
            "pages/03.0_n08_mubtada.html",
            "pages/04.0_n12_follow.html",
            "pages/05.0_n15_mansubat.html"
        ]

        for filepath in files:
            url = f"file://{cwd}/{filepath}"
            print(f"Checking {url}")
            page.goto(url)
            # Take a full page screenshot
            name = filepath.split('/')[-1].replace('.html', '.png')
            page.screenshot(path=f"verification/{name}", full_page=True)

        browser.close()

if __name__ == "__main__":
    run()
