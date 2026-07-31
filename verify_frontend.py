import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(record_video_dir=".")
        await page.goto("file:///app/pages/page_134_h4pom.html")
        await page.screenshot(path="page_134_screenshot.png", full_page=True)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
