import os
from playwright.sync_api import sync_playwright

def verify_cover():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get absolute path to the HTML file
        file_path = os.path.abspath('pages/00_cover.html')
        url = f'file://{file_path}'

        print(f"Navigating to {url}")
        page.goto(url)

        # Take a screenshot of the entire page
        screenshot_path = 'verification/cover_page.png'
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    verify_cover()
