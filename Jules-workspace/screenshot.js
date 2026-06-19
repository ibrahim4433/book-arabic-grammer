const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file:///app/Jules-workspace/pages/17.0_nXX_الْجُمْلَةُ الِاسْمِيَّةُ (الْمُبْتَدَأُ وَالْخَبَرُ) وَإِعْرَابُهُمَا (تابع).html');
  await page.evaluate(() => {
      const link = document.createElement('link');
      link.rel = 'stylesheet';
      link.href = 'file:///app/Jules-workspace/styles/main.css';
      document.head.appendChild(link);
  });
  await page.waitForTimeout(1000);
  await page.screenshot({ path: '/app/Jules-workspace/screenshot.png', fullPage: true });
  await browser.close();
})();
