from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('http://127.0.0.1:8000')
    
    # Wait for the iframe to load
    page.wait_for_selector('iframe#previewFrame')
    iframeElement = page.locator('iframe#previewFrame').element_handle()
    frame = iframeElement.content_frame()
    
    # Wait for the page content inside the iframe
    frame.wait_for_selector('.page-header-strip')
    
    # Run the getUsedVariables function on the header element
    result = frame.evaluate('''() => {
        let target = document.querySelector('.page-header-strip');
        if (!target) return "No target";
        
        let vars = new Set();
        let logs = [];
        try {
            for (let i = 0; i < document.styleSheets.length; i++) {
                let sheet = document.styleSheets[i];
                try {
                    for (let j = 0; j < sheet.cssRules.length; j++) {
                        let rule = sheet.cssRules[j];
                        if (rule.type === 1) { // CSSRule.STYLE_RULE
                            if (rule.selectorText.includes(':root') || rule.selectorText.includes('html') || rule.selectorText === 'body') continue;
                            
                            let cleanSelector = rule.selectorText.replace(/::?(before|after|hover|active|focus|nth-child\\([^)]+\\))/g, '').trim();
                            if (!cleanSelector) continue;
                            
                            try {
                                if (target.matches(cleanSelector) || target.querySelector(cleanSelector)) {
                                    const matches = rule.style.cssText.match(/var\\(--[a-zA-Z0-9-]+\\b/g);
                                    if (matches) {
                                        logs.push(`Matched ${cleanSelector} with ${matches}`);
                                        matches.forEach(m => vars.add(m.substring(4)));
                                    }
                                }
                            } catch(e) {}
                        }
                    }
                } catch(e) { logs.push("Sheet rule error: " + e.message); }
            }
        } catch(e) { logs.push("Sheet error: " + e.message); }
        
        return {vars: Array.from(vars), logs: logs};
    }''')
    
    print("Variables:", result['vars'])
    print("Logs:", result['logs'])
    browser.close()
