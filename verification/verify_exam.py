import os
from playwright.sync_api import sync_playwright

def verify_exam(page):
    # Navigate to the file
    filepath = os.path.abspath("pages/08.4_n27_irab_jumal.html")
    page.goto(f"file://{filepath}")

    # Locate the exam section
    exam_section = page.locator("#b67194")

    # Wait for it to be visible
    exam_section.wait_for()

    # Take screenshot of the specific element
    exam_section.screenshot(path="verification/exam_screenshot.png")
    print("Screenshot saved to verification/exam_screenshot.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify_exam(page)
        finally:
            browser.close()
