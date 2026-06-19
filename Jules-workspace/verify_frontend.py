import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        await page.goto(f"file:///app/Jules-workspace/pages/12.0_nXX_الضَّمَائِرُ (الجزء الثاني).html")
        await page.evaluate("""() => {
            const link = document.createElement('link');
            link.rel = 'stylesheet';
            link.href = 'file:///app/Jules-workspace/styles/main.css';
            document.head.appendChild(link);
        }""")
        await page.wait_for_timeout(500)
        await page.screenshot(path="page1.png", full_page=True)

        await page.goto(f"file:///app/Jules-workspace/pages/12.1_nXX_الضَّمَائِرُ (الجزء الثاني)_تابع.html")
        await page.evaluate("""() => {
            const link = document.createElement('link');
            link.rel = 'stylesheet';
            link.href = 'file:///app/Jules-workspace/styles/main.css';
            document.head.appendChild(link);
        }""")
        await page.wait_for_timeout(500)
        await page.screenshot(path="page2.png", full_page=True)

        await browser.close()

asyncio.run(main())
