from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(
        record_video_dir="videos/"
    )
    page.goto("file:///app/pages/page_124_h4pom.html")
    page.wait_for_timeout(2000)
    page.screenshot(path="screenshot.png", full_page=True)
    video_path = page.video.path()
    print(video_path)
    browser.close()
