from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Go to the file
        filepath = os.path.abspath("pages/09.0_n28_sarf_mizan.html")
        page.goto(f"file://{filepath}")

        # Wait for the page to load (though static, good practice)
        page.wait_for_load_state("networkidle")

        # Take a full page screenshot
        page.screenshot(path="verification/lesson_28.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    run()
