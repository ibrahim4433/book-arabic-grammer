import os
from playwright.sync_api import sync_playwright

def verify_irab(page, filepath, screenshot_path):
    abs_path = os.path.abspath(filepath)
    page.goto(f"file://{abs_path}")

    # Wait for the irab blocks to be visible
    page.wait_for_selector(".irab-box")

    # Take a full page screenshot
    page.screenshot(path=screenshot_path, full_page=True)
    print(f"Screenshot saved to {screenshot_path}")

def main():
    os.makedirs("verification", exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Verify Page 17
        print("Verifying Page 17...")
        verify_irab(page, "pages/05.2_n17_mansubat.html", "verification/page_17_irab.png")

        # Verify Page 18
        print("Verifying Page 18...")
        verify_irab(page, "pages/05.3_n17a_mansubat.html", "verification/page_18_irab.png")

        browser.close()

if __name__ == "__main__":
    main()
