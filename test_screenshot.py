import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('file:///app/pages/page_117_h4pom.html')
        await page.screenshot(path='screenshot.png', full_page=True)
        await browser.close()

asyncio.run(main())
