from playwright.sync_api import sync_playwright
import os

files = [
    "pages/03.2_n10_mubtada.html",
    "pages/03.3_n11_mubtada.html",
    "pages/04.2_n14_follow.html",
    "pages/04.3_n14_follow_cont.html",
    "pages/08.1_n24_irab_jumal.html",
    "pages/08.2_n24_irab_jumal_cont.html"
]

def verify_pages():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for file_path in files:
            abs_path = os.path.abspath(file_path)
            print(f"Verifying {abs_path}...")
            page.goto(f"file://{abs_path}")

            # Screenshot full page
            screenshot_path = f"verification/{os.path.basename(file_path)}.png"
            page.screenshot(path=screenshot_path, full_page=True)
            print(f"Screenshot saved: {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    verify_pages()
