# Module 8: The Paged Media CSS Architecture

Welcome to the first Master Class module. 

In standard web development, CSS is used to design websites that scroll vertically forever. But in this repository, our ultimate output is not a website; it is a physical, printed A4 book.

Standard CSS does not understand the concept of a physical piece of paper. To bridge this gap, this repository uses **Paged Media Level 3**, a specialized branch of CSS designed exclusively for print, interpreted by the WeasyPrint engine.

In this module, we will dissect the global stylesheet (`styles/main.css`) to understand exactly how Python and CSS work together to define physical dimensions, automatic pagination, and typography.

---

## Beginner Primer: CSS Variables and Fallbacks

In this module, you will look at CSS. CSS is the language that makes HTML look pretty. 

**1. What is a CSS Variable?**
If you want the main color of your book to be Teal (`#6c7a89`), you could write that exact color code 500 times across your CSS file. But if you ever want to change the book theme to Blue, you'd have to find and replace all 500 instances!
Instead, we define it once at the very top of the file in the `:root` block:
```css
:root {
    --color-primary: #6c7a89;
}
```
Now, whenever we want to use Teal, we just write `color: var(--color-primary);`. Change it once at the top, and it instantly updates everywhere!

**2. What is a Font Fallback?**
You will see code like: `font-family: 'Noto Naskh Arabic', "Segoe UI Emoji", serif;`
Why so many fonts? If the PDF renderer tries to draw a special character (like an emoji) and the first font (`Noto Naskh Arabic`) doesn't support it, it will "fall back" to the next font in the list. If that fails, it falls back again. This prevents ugly missing-character boxes () from ruining the book!

---

## Lesson 1: Defining the Physical Paper (`@page`)

When you open `styles/main.css`, the very first major ruleset you see is not `body` or `html`. It is the `@page` rule.

### Real Code: The A4 Setup

```css
/* 1. PAGE SETUP - "THE OLD BOOK" DENSITY */
@page {
    size: A4;
    /* Small margins like the classic book to maximize space */
    margin: 5mm 5mm 9mm 5mm;

    /* FOOTER - Automatic Page Numbering */
    @bottom-center {
        content: counter(page, arabic-indic);
        font-family: 'Noto Kufi Arabic';
        font-weight: bold;
        font-size: 12pt;
        color: var(--color-primary);
    }

    @bottom-left { content: none; }
}

@page blank {
    margin: 0;
    size: A4;
    @bottom-center { content: none; }
}
```

**Line-by-Line Breakdown:**
1.  **`@page`**: This is a Paged Media pseudo-selector. It targets the physical sheet of paper that WeasyPrint will generate.
2.  **`size: A4;`**: We explicitly tell the rendering engine the exact dimensions of the PDF.
3.  **`margin: 5mm 5mm 9mm 5mm;`**: Notice the use of millimeters (`mm`), a physical measurement, rather than pixels (`px`) or relative sizes (`rem`). The bottom margin is set to `9mm` to leave room for the footer. This exactly matches the `PRINTABLE_BOTTOM_MM = PAGE_HEIGHT_MM - 9.0` math we saw in `verify_layout.py`.
4.  **`@bottom-center`**: This creates a dedicated physical region at the bottom of the page that ignores standard HTML flow.
5.  **`content: counter(page, arabic-indic);`**: This is brilliant. We don't write page numbers in HTML. WeasyPrint automatically counts the pages and injects the Arabic numeral (e.g., ١, ٢, ٣) dynamically into the PDF!
6.  **`@page blank`**: A named page layout. If we want a specific HTML file to act as a cover page, we can force it to use this layout to strip away the margins and page numbers.

---

## Lesson 2: Preventing Awkward Cuts (Page Breaks)

When printing a webpage, browsers often cut a paragraph horizontally in half at the bottom of the page. In a professional grammar book, cutting an Arabic definition or an exam question in half is unacceptable.

To fix this, we use CSS fragmentation properties on our atomic components.

### Real Code: Protecting the Blocks

```css
/* 3. DENSE CONTENT CARDS (The "Blocks") */
.content-block {
    background: var(--color-white);
    border-radius: var(--radius);
    box-shadow: var(--shadow-card);
    margin-bottom: var(--spacing-std);
    overflow: hidden; /* Ensures header color doesn't bleed */
    page-break-inside: avoid; /* Keep blocks intact */
}
```

**Line-by-Line Breakdown:**
*   **`page-break-inside: avoid;`**: This is the magic rule. When WeasyPrint encounters a `.content-block` (like a definition or rule box) that crosses the `297mm` A4 limit, it refuses to cut it. Instead, it pushes the *entire block* to the next page.

*(Note: This is exactly why the 1-Page Law and `verify_layout.py` exist! If WeasyPrint pushes a block to the next page, but our HTML file is only supposed to be 1 page, WeasyPrint will secretly generate a second page, ruining our 1-HTML=1-Page mapping. Our verifier catches this before it happens!)*

---

## Lesson 3: Strict Typographical Weights

Arabic typography requires extreme precision. The `GEMINI.md` rules state: *"All structural Arabic text must use bold weights (`font-weight: 700` or `900`). Normal or medium weights (`400`, `500`) are strictly forbidden."*

Why? Because fine diacritics (Tashkeel) like a small Fatha (َ ) or Kasra (ِ ) become invisible on printed A4 paper if the font is too thin.

### Real Code: Forcing the Fonts

```css
@font-face {
    font-family: 'Noto Kufi Arabic';
    src: url('../assets/fonts/NotoKufiArabic-Bold.ttf') format('truetype');
    font-weight: 700;
    font-style: normal;
}

@font-face {
    font-family: 'Noto Kufi Arabic';
    src: url('../assets/fonts/NotoKufiArabic-Black.ttf') format('truetype');
    font-weight: 900;
    font-style: normal;
}

.lesson-number {
    font-family: 'Noto Kufi Arabic';
    font-size: var(--font-number-size);
    color: var(--color-primary);
    font-weight: 900;
    line-height: 1;
}
```

**Line-by-Line Breakdown:**
1.  **`@font-face`**: We explicitly load the local TTF font files so the PDF renderer doesn't rely on system fonts (which could ruin the layout on different machines).
2.  **`font-weight: 700/900`**: Notice that we *only* load the Bold (700) and Black (900) font weights. If a developer accidentally writes `font-weight: 400;` in HTML, the CSS engine literally does not have the file to render it, forcing adherence to the rule.
3.  **`.lesson-number`**: Crucial structural elements are forced to maximum weight (`900`) and use Kufi (a geometric, highly legible Arabic script) rather than Naskh (standard book text) to create visual hierarchy.

### Review
You now understand the specialized CSS required to bridge web technologies with physical printing.
*   You know how `@page` defines margins and physical dimensions in millimeters.
*   You've seen how `content: counter(page, arabic-indic)` automates pagination perfectly.
*   You know why `page-break-inside: avoid` protects content (and why it requires our layout verifiers).
*   You understand the physical necessity behind forcing `font-weight: 700`.

In **Module 9: The Markdown-to-HTML Generator Engine**, we will leave the CSS behind and look at the Python orchestration script that dynamically injects AI markdown into these very HTML templates.
