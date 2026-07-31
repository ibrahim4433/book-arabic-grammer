from playwright.sync_api import sync_playwright
import os
import shutil

# Ensure output directories exist
os.makedirs("/home/jules/verification/screenshots", exist_ok=True)
os.makedirs("/home/jules/verification/videos", exist_ok=True)

# Clear old videos if any
for file in os.listdir("/home/jules/verification/videos"):
    if file.endswith(".webm"):
        os.remove(os.path.join("/home/jules/verification/videos", file))

def run_cuj(page):
    # Navigate to the static HTML file
    page.goto("file:///app/pages/page_126_h4pom.html")
    page.wait_for_timeout(500)

    # Scroll slightly to show content if needed
    page.evaluate("window.scrollTo(0, document.body.scrollHeight / 3)")
    page.wait_for_timeout(500)

    # Take screenshot
    page.screenshot(path="/home/jules/verification/screenshots/verification.png")
    page.wait_for_timeout(1000)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos",
            viewport={"width": 1200, "height": 1600}
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()  # MUST close context to save the video
            browser.close()
