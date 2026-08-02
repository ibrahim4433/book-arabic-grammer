from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("file:///app/pages/page_106_6pqjt.html")
    page.screenshot(path="screenshot.png", full_page=True)
    browser.close()
