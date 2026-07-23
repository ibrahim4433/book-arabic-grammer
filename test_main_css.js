const fs = require('fs');
const css = fs.readFileSync('styles/main.css', 'utf8');

// Simulate the logic!
const cssRules = css.split('}');
let vars = new Set();
let targetSelector = '.irab-word'; // We are targeting .irab-word

for (let rule of cssRules) {
    if (!rule.includes('{')) continue;
    let [selector, style] = rule.split('{');
    selector = selector.trim();
    if (selector.includes(targetSelector)) {
        console.log("Matched rule:", selector);
        const matches = style.match(/var\(--[a-zA-Z0-9-]+\b/g);
        console.log("Matches:", matches);
        if (matches) {
            matches.forEach(m => vars.add(m.substring(4)));
        }
    }
}
console.log("Vars:", Array.from(vars));
