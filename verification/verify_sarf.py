from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Verify Page 1: 09.0_n29_sarf.html
        path1 = os.path.abspath("pages/09.0_n29_sarf.html")
        print(f"Loading {path1}")
        page.goto(f"file://{path1}")
        page.wait_for_load_state("networkidle")

        # Take screenshot of Page 1
        page.screenshot(path="verification/09.0_sarf_preview.png", full_page=True)
        print("Captured verification/09.0_sarf_preview.png")

        # Verify Page 2: 09.1_n30_sarf.html
        path2 = os.path.abspath("pages/09.1_n30_sarf.html")
        print(f"Loading {path2}")
        page.goto(f"file://{path2}")
        page.wait_for_load_state("networkidle")

        # Take screenshot of Page 2
        page.screenshot(path="verification/09.1_sarf_preview.png", full_page=True)
        print("Captured verification/09.1_sarf_preview.png")

        browser.close()

if __name__ == "__main__":
    run()