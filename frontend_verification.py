import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        # Record video
        context = await browser.new_context(record_video_dir=".")
        page = await context.new_page()

        await page.goto("file:///app/pages/page_131_h4pom.html")
        await page.wait_for_timeout(2000)

        await page.screenshot(path="screenshot.png", full_page=True)
        await context.close()
        await browser.close()

asyncio.run(run())
