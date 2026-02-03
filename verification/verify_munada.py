from playwright.sync_api import Page, expect, sync_playwright
import os

def test_munada_pages(page: Page):
    # Verify Page 1
    page.goto("http://localhost:8000/pages/08.0_n20_munada.html")
    expect(page.get_by_text("المنادى", exact=True).first).to_be_visible()
    # Check for specific content
    expect(page.get_by_text("المُنَادَى اسمٌ وَقَعَ بَعْدَ حَرْفٍ مِن أحرفِ النِّداءِ")).to_be_visible()
    page.screenshot(path="verification/08.0_n20_munada.png", full_page=True)

    # Verify Page 2
    page.goto("http://localhost:8000/pages/08.1_n21_munada_p2.html")
    expect(page.get_by_text("المنادى (تابع)")).to_be_visible()
    # Check for specific content like the poem
    expect(page.get_by_text("الدَّرْبُ أبْصَرَ")).to_be_visible()
    page.screenshot(path="verification/08.1_n21_munada_p2.png", full_page=True)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            test_munada_pages(page)
        finally:
            browser.close()
