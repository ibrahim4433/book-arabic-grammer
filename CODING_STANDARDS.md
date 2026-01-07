# **Coding Standards & Quality Gates**

## **HTML / Content Rules**

1. **Semantic Structure:** Use \<article\>, \<section\>, \<h1\>–\<h3\>.  
2. **RTL Enforcement:** Every HTML file must start with:  
   \<\!DOCTYPE html\>  
   \<html lang="ar" dir="rtl"\>

3. **Diacritics (Tashkeel):** All Arabic text MUST have full diacritics.  
4. **Color Coding (Grammar):**  
   * Use \<span class="highlight-red"\> for **I'rab signs** (Grammatical endings).  
   * Use \<span class="highlight-blue"\> for **Particles** (Harf Jar, etc.).  
   * Use \<span class="keyword"\> for **Definitions**.

## **CSS / Design Rules**

1. **Paged Media:** Always define @page with correct margins (e.g., margin: 20mm).  
2. **Avoid Breaks:**  
   h1, h2, .grammar-box, table { break-inside: avoid; page-break-inside: avoid; }

3. **Variables:** Use CSS variables for colors (defined in :root).  
   * \--color-primary (Teal/Green)  
   * \--color-accent (Red/Orange for grammar)

## **Python Build Rules**

1. **Path Handling:** Use os.path and glob to reliably find files across OS environments.  
2. **Error Handling:** The script should fail gracefully if a file is missing.
