
from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Absolute path to the file
        file_path = os.path.abspath("pages/TEMPLATE_CHAPTER.html")
        url = f"file://{file_path}"

        print(f"Navigating to {url}")
        page.goto(url)

        # Take a screenshot of the split-grid section
        # We can also take a full page screenshot
        page.screenshot(path="verification/layout_before.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    run()
