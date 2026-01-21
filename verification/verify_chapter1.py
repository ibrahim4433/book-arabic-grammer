from playwright.sync_api import sync_playwright
import os

def test_chapter1(page):
    # Get absolute path to the file
    cwd = os.getcwd()
    file_path = f"file://{cwd}/pages/02_chapter1.html"
    print(f"Navigating to: {file_path}")

    page.goto(file_path)

    # Wait for content to load (since it's static file, it's instant, but safe to wait for body)
    page.wait_for_selector("body")

    # Take screenshot of the whole page
    # Since we use print styling @page, the browser view might differ.
    # We will just screenshot the viewport to verify content structure.
    # We force a large viewport to see everything.
    page.set_viewport_size({"width": 1000, "height": 1500})

    screenshot_path = "verification/chapter1_verify.png"
    page.screenshot(path=screenshot_path, full_page=True)
    print(f"Screenshot saved to {screenshot_path}")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            test_chapter1(page)
        finally:
            browser.close()
