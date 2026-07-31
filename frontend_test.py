import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(
            viewport={'width': 800, 'height': 1120} # A4-ish vertical
        )
        page = await context.new_page()

        await page.goto("file:///app/pages/page_164_h4pom.html")
        await page.wait_for_timeout(1000) # Give it a second to render

        await page.screenshot(path="screenshot.png", full_page=True)
        print("Screenshot saved to screenshot.png")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
