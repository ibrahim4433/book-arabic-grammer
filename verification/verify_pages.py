
import os
from playwright.sync_api import sync_playwright

def verify_pages():
    cwd = os.getcwd()
    page1_path = f"file://{cwd}/pages/09.0_n28_sigh_ziyada.html"
    page2_path = f"file://{cwd}/pages/10.0_n29_sahih_muatal.html"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print(f"Navigating to {page1_path}")
        page.goto(page1_path)
        page.screenshot(path="verification/09.0_screenshot.png", full_page=True)
        print("Screenshot 1 taken")

        print(f"Navigating to {page2_path}")
        page.goto(page2_path)
        page.screenshot(path="verification/10.0_screenshot.png", full_page=True)
        print("Screenshot 2 taken")

        browser.close()

if __name__ == "__main__":
    verify_pages()
