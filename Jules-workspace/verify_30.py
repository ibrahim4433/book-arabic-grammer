from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Page 30.0
        file_path_0 = os.path.abspath("pages/30.0_nXX_العاطفة.html")
        page.goto(f"file://{file_path_0}")
        page.screenshot(path="verification_30.0.png", full_page=True)
        print("Screenshot 30.0 saved.")

        # Page 30.1
        file_path_1 = os.path.abspath("pages/30.1_nXX_العاطفة.html")
        page.goto(f"file://{file_path_1}")
        page.screenshot(path="verification_30.1.png", full_page=True)
        print("Screenshot 30.1 saved.")

        browser.close()

if __name__ == "__main__":
    run()
