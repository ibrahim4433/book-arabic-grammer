from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the page
        file_path = os.path.abspath("pages/03.3_n11_mubtada.html")
        page.goto(f"file://{file_path}")

        # Locate the Irab section. It has id="b80521" (from my previous read)
        # Or I can just screenshot the whole page or specific elements.
        # Let's target specific irab-box elements to see the white text.
        # id="b70648" is one irab-box.

        element = page.locator("#b70648")
        if element.is_visible():
            element.screenshot(path="verification/irab_box_b70648.png")
            print("Screenshot saved to verification/irab_box_b70648.png")
        else:
            print("Element #b70648 not found or not visible")

        # Take another screenshot of the split grid irab row
        element2 = page.locator("#b40127")
        if element2.is_visible():
            element2.screenshot(path="verification/irab_box_b40127.png")
            print("Screenshot saved to verification/irab_box_b40127.png")
        else:
             print("Element #b40127 not found or not visible")

        browser.close()

if __name__ == "__main__":
    run()
