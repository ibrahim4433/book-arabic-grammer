import os
from playwright.sync_api import sync_playwright

def verify(page):
    cwd = os.getcwd()
    filepath = os.path.join(cwd, "pages/25.0_nXX_علامات الترقيم.html")
    url = f"file://{filepath}"

    print(f"Navigating to {url}")
    page.goto(url)

    # Wait for content to render
    page.wait_for_timeout(1000)

    # Screenshot full page
    screenshot_path = "verification_25.0.png"
    page.screenshot(path=screenshot_path, full_page=True)
    print(f"Screenshot saved to {screenshot_path}")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        verify(page)
        browser.close()
