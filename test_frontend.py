import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("file:///app/pages/page_106_h4pom.html")
        await page.wait_for_load_state('networkidle')
        await page.screenshot(path="screenshot_106.png", full_page=True)
        await browser.close()

asyncio.run(run())
