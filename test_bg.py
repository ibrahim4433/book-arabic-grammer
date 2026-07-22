from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('http://localhost:8000/preview?file=01.0_n02_verbs.html', wait_until='networkidle')
    page.wait_for_timeout(2000)
    
    bg = page.evaluate("() => { const el = document.querySelector('.global-background-layer'); return el ? window.getComputedStyle(el).backgroundImage : 'NOT FOUND'; }")
    print(f"Global background layer image: {bg}")
    
    paged = page.evaluate("() => document.querySelectorAll('.pagedjs_page').length")
    print(f"Paged.js pages: {paged}")
    
    browser.close()
