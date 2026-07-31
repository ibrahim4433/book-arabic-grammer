const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  await page.goto('file:///app/pages/page_130_h4pom.html');
  await page.waitForLoadState('networkidle');
  await page.screenshot({ path: 'screenshot_page130.png', fullPage: true });

  await page.goto('file:///app/pages/page_130_h4pom_part2.html');
  await page.waitForLoadState('networkidle');
  await page.screenshot({ path: 'screenshot_page130_part2.png', fullPage: true });

  await browser.close();
})();
