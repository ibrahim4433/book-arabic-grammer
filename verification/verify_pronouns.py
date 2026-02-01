import os
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Use absolute path
        cwd = os.getcwd()
        filepath = os.path.join(cwd, 'pages/02.0_n06_pronouns.html')
        page.goto(f"file://{filepath}")

        # Wait for fonts to load
        page.wait_for_timeout(1000)

        # Screenshot full page
        page.screenshot(path="verification/pronouns_refactor.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    run()
