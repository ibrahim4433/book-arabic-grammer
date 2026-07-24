const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  page.on('console', msg => console.log('CONSOLE:', msg.text()));
  page.on('pageerror', err => console.log('PAGE ERROR:', err.message));
  await page.goto('http://localhost:8000/preview?file=01.0_n02_verbs.html', { waitUntil: 'networkidle' });
  await page.waitForTimeout(2000);
  const bodyClass = await page.evaluate(() => document.body.className);
  console.log('Body classes:', bodyClass);
  const pagedjsPages = await page.evaluate(() => document.querySelectorAll('.pagedjs_page').length);
  console.log('Paged.js pages count:', pagedjsPages);
  await browser.close();
})();
