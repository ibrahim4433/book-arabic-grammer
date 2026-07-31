import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        cwd = os.getcwd()
        await page.goto(f'file://{cwd}/pages/page_114_h4pom.html')
        await page.screenshot(path='screenshot_final_1.png')
        await page.goto(f'file://{cwd}/pages/page_115_h4pom.html')
        await page.screenshot(path='screenshot_final_2.png')
        await browser.close()

asyncio.run(main())
