import os
from playwright.sync_api import sync_playwright

def verify_pages():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Verify Cover Page
        cover_path = os.path.abspath('pages/00_cover.html')
        print(f"Navigating to file://{cover_path}")
        page.goto(f"file://{cover_path}")
        page.screenshot(path="verification/00_cover.png", full_page=True)
        print("Captured 00_cover.png")

        # Verify Chapter 1
        chapter1_path = os.path.abspath('pages/02_chapter1.html')
        print(f"Navigating to file://{chapter1_path}")
        page.goto(f"file://{chapter1_path}")
        page.screenshot(path="verification/02_chapter1.png", full_page=True)
        print("Captured 02_chapter1.png")

        browser.close()

if __name__ == "__main__":
    verify_pages()
