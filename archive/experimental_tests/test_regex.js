const cssText = 'border-radius: var(--radius); color: var(--color-primary, red);';
const matches1 = cssText.match(/var\(--[a-zA-Z0-9-]+\b/g);
console.log(matches1);

const matches2 = cssText.match(/var\(--[a-zA-Z0-9-]+/g);
console.log(matches2);
