const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  // Navigate to the file
  await page.goto('file:///app/pages/page_152_h4pom.html');

  // Take a screenshot
  await page.screenshot({ path: 'frontend_screenshot.png', fullPage: true });

  console.log('Screenshot saved as frontend_screenshot.png');
  await browser.close();
})();
