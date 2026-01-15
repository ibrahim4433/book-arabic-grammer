
from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the HTML file directly
        # Absolute path to the file
        cwd = os.getcwd()
        file_path = f"file://{cwd}/pages/TEMPLATE_CHAPTER.html"

        print(f"Navigating to: {file_path}")
        page.goto(file_path)

        # Wait for fonts to load (a simple wait is usually enough for local files,
        # but we can also wait for a specific element)
        page.wait_for_selector(".page-header-strip")

        # Take a screenshot of the Header area specifically
        header = page.locator(".page-header-strip")
        header.screenshot(path="verification/header_screenshot.png")

        # Take a full page screenshot as well
        page.screenshot(path="verification/full_page_screenshot.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    run()
