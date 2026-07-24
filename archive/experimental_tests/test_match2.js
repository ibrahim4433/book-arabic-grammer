const cssText = 'color: var(--color-primary);';
const matches = cssText.match(/var\(--[a-zA-Z0-9-]+\b/g);
console.log(matches);
