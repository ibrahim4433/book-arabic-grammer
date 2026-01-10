
from playwright.sync_api import sync_playwright
import os

def generate_verification_screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get absolute path for cover page
        cwd = os.getcwd()
        cover_path = f"file://{cwd}/pages/00_cover.html"
        chapter_path = f"file://{cwd}/pages/02_chapter1.html"

        # Screenshot Cover Page
        print(f"Navigating to {cover_path}")
        page.goto(cover_path)
        page.screenshot(path="verification/cover_page.png", full_page=True)
        print("Captured cover_page.png")

        # Screenshot Chapter 1
        print(f"Navigating to {chapter_path}")
        page.goto(chapter_path)
        page.screenshot(path="verification/chapter1.png", full_page=True)
        print("Captured chapter1.png")

        browser.close()

if __name__ == "__main__":
    generate_verification_screenshot()
