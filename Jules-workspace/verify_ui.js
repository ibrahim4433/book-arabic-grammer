const { chromium } = require('playwright');
const path = require('path');

(async () => {
    const browser = await chromium.launch();
    const page = await browser.newPage();
    const filePath = path.resolve(__dirname, 'pages/35.0_nXX_الْمُنَادَى (نِدَاءُ مَا فِيهِ أَلْ).html');
    await page.goto(`file://${filePath}`);

    // Inject absolute CSS path
    await page.evaluate(() => {
        const link = document.createElement('link');
        link.rel = 'stylesheet';
        link.href = 'file:///app/styles/main.css';
        document.head.appendChild(link);
    });

    // Wait for CSS to load and apply
    await page.waitForTimeout(1000);

    await page.screenshot({ path: 'screenshot.png', fullPage: true });
    await browser.close();
})();
