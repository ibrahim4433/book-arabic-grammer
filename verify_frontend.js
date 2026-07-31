const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file:///app/pages/page_132_h4pom.html');
  await page.screenshot({ path: 'screenshot.png', fullPage: true });
  await browser.close();
})();
