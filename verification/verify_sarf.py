from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Calculate absolute path
        file_path = os.path.abspath("pages/09.0_n28_sarf.html")
        page.goto(f"file://{file_path}")

        # Wait for fonts to load or just wait a bit
        page.wait_for_timeout(1000)

        # Screenshot full page
        page.screenshot(path="verification/sarf_full.png", full_page=True)

        # Screenshot specific interesting blocks if needed
        # Block 3 (Scale)
        page.locator("#b68888").screenshot(path="verification/sarf_block3.png")

        # Block 4 (Benefit)
        page.locator("#b60840").screenshot(path="verification/sarf_block4.png")

        # Block 7 (Exam)
        page.locator("#b19393").screenshot(path="verification/sarf_block7.png")

        browser.close()

if __name__ == "__main__":
    run()
